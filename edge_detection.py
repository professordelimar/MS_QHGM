"""Automatic ridge extraction used in the MS-QHGM experiments."""

import numpy as np

EPS = 1e-15


def normalize01(a, eps=EPS):
    """Normalize a finite array to the interval [0, 1]."""
    a = np.asarray(a, dtype=float)
    amin = np.nanmin(a)
    amax = np.nanmax(a)
    return (a - amin) / (amax - amin + eps)


def otsu_threshold(data, nbins=256, eps=EPS):
    """Compute an Otsu threshold from a normalized response distribution."""
    values = np.asarray(data, dtype=float)
    values = values[np.isfinite(values)]
    hist, bin_edges = np.histogram(values, bins=nbins, range=(0.0, 1.0))
    hist = hist.astype(float)
    probability = hist / np.sum(hist)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    omega = np.cumsum(probability)
    mu = np.cumsum(probability * bin_centers)
    mu_total = mu[-1]
    sigma_b2 = (mu_total * omega - mu) ** 2 / (omega * (1.0 - omega) + eps)
    return bin_centers[np.nanargmax(sigma_b2)]


def detect_edge_ridges(response, border=4, nbins=256):
    """Detect local response maxima along either grid direction above Otsu threshold."""
    R = normalize01(response)
    threshold = otsu_threshold(R, nbins=nbins)

    maxima_x = np.zeros_like(R, dtype=bool)
    maxima_x[:, 1:-1] = (R[:, 1:-1] >= R[:, :-2]) & (R[:, 1:-1] > R[:, 2:])

    maxima_y = np.zeros_like(R, dtype=bool)
    maxima_y[1:-1, :] = (R[1:-1, :] >= R[:-2, :]) & (R[1:-1, :] > R[2:, :])

    ridges = (maxima_x | maxima_y) & (R >= threshold)

    if border > 0:
        ridges[:border, :] = False
        ridges[-border:, :] = False
        ridges[:, :border] = False
        ridges[:, -border:] = False

    return R, threshold, ridges
