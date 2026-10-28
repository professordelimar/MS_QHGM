"""Unittest numerical smoke tests for independent spectral operators."""
import sys
import unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import spectral_operators as s

class SpectralTests(unittest.TestCase):
    def setUp(self):
        x=np.arange(-8000.,8001.,250.)
        y=np.arange(-6000.,6001.,250.)
        self.X,self.Y=np.meshgrid(x,y)
        self.f=np.exp(-(self.X/2500.)**2-(self.Y/2400.)**2)

    def test_shapes_finiteness(self):
        for out in [s.my_xderiv(self.X,self.Y,self.f),
                    s.my_yderiv(self.X,self.Y,self.f),
                    s.my_upward_continuation(self.X,self.Y,self.f,1250)]:
            self.assertEqual(out.shape,self.f.shape)
            self.assertTrue(np.isfinite(out).all())

    def test_horizontal_derivatives_centered_gaussian(self):
        # At the center the true derivatives vanish by symmetry.
        gx=s.my_xderiv(self.X,self.Y,self.f)
        gy=s.my_yderiv(self.X,self.Y,self.f)
        iy,ix=np.unravel_index(np.argmax(self.f),self.f.shape)
        self.assertLess(abs(gx[iy,ix]),2e-5)
        self.assertLess(abs(gy[iy,ix]),2e-5)

    def test_upward_smoothing(self):
        continued=s.my_upward_continuation(self.X,self.Y,self.f,1250)
        self.assertLess(continued.max(),self.f.max())

    def test_no_continuation_identity_away_from_boundaries(self):
        out=s.my_upward_continuation(self.X,self.Y,self.f,0)
        np.testing.assert_allclose(out,self.f,atol=1e-12,rtol=1e-12)

if __name__=='__main__': unittest.main()
