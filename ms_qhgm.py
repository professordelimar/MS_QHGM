"""Reference implementation of MS-QHGM.

Multiscale Quantile-Normalized Horizontal Gradient Magnitude for gravity edge detection.
"""

from __future__ import annotations

import numpy as np

EPS = 1e-15


def normalize01(a, eps=EPS):
    a = np.asarray(a, dtype=float)
    amin = np.nanmin(a)
    amax = np.nanmax(a)
    return (a - amin) / (amax - amin + eps)


def horizontal_gradient(fx, fy):
    """Horizontal gradient magnitude from first horizontal derivatives."""
    return np.sqrt(np.asarray(fx, dtype=float) ** 2 + np.asarray(fy, dtype=float) ** 2)


def qhgm(hgm, q=75.0, eps=EPS):
    """Quantile-normalized horizontal gradient magnitude."""
    hgm = np.asarray(hgm, dtype=float)
    lam = np.nanpercentile(hgm, q)
    response = hgm / (hgm + lam + eps)
    return response, lam


def analysis_heights(dx, dy, multipliers=(0.0, 5.0, 10.0, 20.0)):
    """Return the fixed analysis heights used by MS-QHGM."""
    delta = max(float(dx), float(dy))
    return delta * np.asarray(multipliers, dtype=float)


def ms_qhgm_from_hgm_scales(hgm_scales, q=75.0, eps=EPS):
    """Combine HGM maps from multiple scales into the final MS-QHGM response."""
    q_scales = []
    lambdas = []
    for hgm in hgm_scales:
        qmap, lam = qhgm(hgm, q=q, eps=eps)
        q_scales.append(qmap)
        lambdas.append(lam)

    q_scales = np.asarray(q_scales)
    mean_response = np.nanmean(q_scales, axis=0)
    final = normalize01(mean_response, eps=eps)
    return final, q_scales, np.asarray(lambdas), mean_response


def compute_ms_qhgm(
    X, Y, field, derivative_module, filtering_module, q=75.0,
    multipliers=(0.0, 5.0, 10.0, 20.0), pad_factor=0.5,
    pad_mode="reflect", taper=True, eps=EPS
):
    """Compute HGM, QHGM and MS-QHGM using the project's gravmag API.

    The derivative module must provide ``my_xderiv`` and ``my_yderiv`` and the
    filtering module must provide ``my_upward_continuation`` with the signatures
    used by the research notebooks in this repository.
    """
    X = np.asarray(X, dtype=float)
    Y = np.asarray(Y, dtype=float)
    field = np.asarray(field, dtype=float)

    if X.shape != Y.shape or X.shape != field.shape:
        raise ValueError("X, Y and field must have identical 2D shapes.")

    dx = float(np.nanmedian(np.diff(X, axis=1)))
    dy = float(np.nanmedian(np.diff(Y, axis=0)))
    heights = analysis_heights(abs(dx), abs(dy), multipliers=multipliers)

    hgm_scales = []
    q_scales = []
    lambdas = []

    for height in heights:
        if np.isclose(height, 0.0):
            f_h = field
        else:
            f_h = filtering_module.my_upward_continuation(
                X, Y, field, height=height, pad_factor=pad_factor,
                pad_mode=pad_mode, taper=taper, flatten=False
            )

        fx = derivative_module.my_xderiv(
            X, Y, f_h, n=1, pad_factor=pad_factor,
            pad_mode=pad_mode, taper=taper, flatten=False
        )
        fy = derivative_module.my_yderiv(
            X, Y, f_h, n=1, pad_factor=pad_factor,
            pad_mode=pad_mode, taper=taper, flatten=False
        )

        hgm = horizontal_gradient(fx, fy)
        qmap, lam = qhgm(hgm, q=q, eps=eps)
        hgm_scales.append(hgm)
        q_scales.append(qmap)
        lambdas.append(lam)

    q_scales = np.asarray(q_scales)
    mean_response = np.nanmean(q_scales, axis=0)
    final = normalize01(mean_response, eps=eps)

    return {
        "MSQHGM": final,
        "QHGM": q_scales[0],
        "HGM": np.asarray(hgm_scales)[0],
        "HGM_scales": np.asarray(hgm_scales),
        "QHGM_scales": q_scales,
        "lambdas": np.asarray(lambdas),
        "heights": heights,
        "mean_response": mean_response,
    }
