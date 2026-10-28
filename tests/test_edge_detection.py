"""Regression tests for the published edge detector and MS-QHGM core."""
import unittest
import numpy as np
from edge_detection import normalize01, detect_edge_ridges
from ms_qhgm import qhgm

class EdgeTests(unittest.TestCase):
    def test_normalize01_finite(self):
        result = normalize01(np.array([[0., 1.], [2., 3.]]))
        self.assertTrue(np.isfinite(result).all())
        self.assertAlmostEqual(result.min(), 0.)
    def test_ridges(self):
        x = np.linspace(-3, 3, 51)
        f = np.tile(np.exp(-x*x), (31, 1))
        response, threshold, ridges = detect_edge_ridges(f)
        self.assertEqual(ridges.shape, f.shape)
        self.assertTrue(np.isfinite(response).all())
        self.assertGreater(int(ridges.sum()), 0)
    def test_quantile_scaling(self):
        a=np.arange(1.,13.).reshape(3,4)
        self.assertTrue(np.allclose(qhgm(a)[0], qhgm(a*5)[0]))
