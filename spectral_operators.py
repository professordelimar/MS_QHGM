"""Independent NumPy FFT operators compatible with the MS-QHGM module API.

Research reference implementation, not a verified numerical clone of GravMag.
Coordinates must be regular meshgrids in metres, field[y,x].
"""
import numpy as np


def _spacing(X, Y, f):
    X, Y, f = [np.asarray(a, dtype=float) for a in (X, Y, f)]
    if f.ndim != 2 or X.shape != f.shape or Y.shape != f.shape:
        raise ValueError('X, Y and field must be identically shaped 2D arrays')
    if not np.isfinite(f).all():
        raise ValueError('field must have finite values')
    if min(f.shape) < 3:
        raise ValueError('grid must have at least three nodes per axis')
    dx = float(np.median(np.diff(X, axis=1)))
    dy = float(np.median(np.diff(Y, axis=0)))
    if not np.isfinite([dx,dy]).all() or dx == 0 or dy == 0:
        raise ValueError('invalid grid intervals')
    tol = 1e-6
    if not (np.allclose(np.diff(X, axis=1), dx, rtol=tol, atol=tol*abs(dx)) and
            np.allclose(np.diff(Y, axis=0), dy, rtol=tol, atol=tol*abs(dy)) and
            np.allclose(X, X[0,:][None,:], rtol=tol, atol=tol*abs(dx)) and
            np.allclose(Y, Y[:,0][:,None], rtol=tol, atol=tol*abs(dy))):
        raise ValueError('X and Y must describe an axis-aligned regular meshgrid')
    return f, abs(dy), abs(dx), np.sign(dy), np.sign(dx)


def _extend(field, pad_factor, pad_mode, taper):
    if pad_factor < 0:
        raise ValueError('pad_factor must be nonnegative')
    ny, nx = field.shape
    py, px = int(round(ny * pad_factor)), int(round(nx * pad_factor))
    if pad_mode != 'reflect':
        raise ValueError('reference implementation supports reflect padding only')
    padded = np.pad(field, ((py,py),(px,px)), mode='reflect')
    if taper and (py or px):
        # Cosine transition of PADDED EXTENSIONS only, leaving original samples unchanged.
        wy = np.ones(padded.shape[0]); wx = np.ones(padded.shape[1])
        if py:
            ramp = np.sin(np.linspace(0, np.pi/2, py, endpoint=False))**2
            wy[:py] = ramp; wy[-py:] = ramp[::-1]
        if px:
            ramp = np.sin(np.linspace(0, np.pi/2, px, endpoint=False))**2
            wx[:px] = ramp; wx[-px:] = ramp[::-1]
        padded = padded * np.outer(wy,wx)
    return padded, (slice(py, py+ny), slice(px, px+nx))


def _operate(X, Y, f, kind, *, n=1, height=None, pad_factor=0.5,
             pad_mode='reflect', taper=True, flatten=False):
    f, dy, dx, sy, sx = _spacing(X, Y, f)
    if kind != 'upward' and (not isinstance(n,int) or n < 1):
        raise ValueError('derivative order must be positive integer')
    if kind == 'upward' and (height is None or height < 0):
        raise ValueError('upward continuation height must be nonnegative')
    padded, crop = _extend(f, pad_factor, pad_mode, taper)
    ky = 2*np.pi*np.fft.fftfreq(padded.shape[0], d=dy)*sy
    kx = 2*np.pi*np.fft.fftfreq(padded.shape[1], d=dx)*sx
    if kind == 'x': factor = (1j*kx[None,:])**n
    elif kind == 'y': factor = (1j*ky[:,None])**n
    elif kind == 'upward': factor = np.exp(-float(height)*np.hypot(ky[:,None],kx[None,:]))
    else: raise ValueError(kind)
    result = np.fft.ifft2(np.fft.fft2(padded)*factor).real[crop]
    return result.ravel() if flatten else result


def my_xderiv(X, Y, field, n=1, pad_factor=0.5, pad_mode='reflect', taper=True, flatten=False):
    return _operate(X,Y,field,'x',n=n,pad_factor=pad_factor,pad_mode=pad_mode,taper=taper,flatten=flatten)


def my_yderiv(X, Y, field, n=1, pad_factor=0.5, pad_mode='reflect', taper=True, flatten=False):
    return _operate(X,Y,field,'y',n=n,pad_factor=pad_factor,pad_mode=pad_mode,taper=taper,flatten=flatten)


def my_upward_continuation(X, Y, field, height, pad_factor=0.5, pad_mode='reflect', taper=True, flatten=False):
    return _operate(X,Y,field,'upward',height=height,pad_factor=pad_factor,pad_mode=pad_mode,taper=taper,flatten=flatten)
