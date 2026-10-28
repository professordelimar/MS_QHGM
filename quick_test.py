
import numpy as np

from ms_qhgm import (
    qhgm,
    analysis_heights,
    ms_qhgm_from_hgm_scales,
)
from edge_detection import detect_edge_ridges


def main():
    # Deterministic synthetic gradient distributions
    x = np.linspace(-5000, 5000, 101)
    y = np.linspace(-4000, 4000, 81)
    X, Y = np.meshgrid(x, y)

    hgm = (
        np.exp(-((X + 1500) / 600) ** 2)
        + 0.5 * np.exp(-((X - 1800) / 900) ** 2)
    )

    # Check single-scale quantile normalization
    qmap, lam = qhgm(hgm, q=75.0)

    assert np.all(np.isfinite(qmap))
    assert np.all(qmap >= 0)
    assert np.all(qmap <= 1)

    # Check positive amplitude-scaling invariance
    qmap_scaled, _ = qhgm(10.0 * hgm, q=75.0)
    assert np.allclose(qmap, qmap_scaled)

    # Exercise multiscale aggregation using four
    # prescribed synthetic gradient maps
    hgm_scales = [
        hgm,
        0.8 * hgm,
        0.6 * hgm,
        0.4 * hgm,
    ]

    ms, scales, lambdas, mean = (
        ms_qhgm_from_hgm_scales(hgm_scales)
    )

    assert ms.shape == hgm.shape
    assert scales.shape[0] == 4
    assert len(lambdas) == 4
    assert np.all(np.isfinite(ms))

    # Test ridge extraction
    response, threshold, ridges = (
        detect_edge_ridges(ms)
    )

    assert ridges.shape == hgm.shape
    assert ridges.dtype == bool
    assert np.sum(ridges) > 0

    print("MS-QHGM quick test: PASSED")
    print("Analysis heights:",
          analysis_heights(250, 250))
    print("Detected ridge pixels:",
          int(np.sum(ridges)))
    print("Otsu threshold:", float(threshold))


if __name__ == "__main__":
    main()
