"""End-to-end core MS-QHGM example without external gravmag dependency."""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ms_qhgm import compute_ms_qhgm
from edge_detection import detect_edge_ridges
import spectral_operators as ops

def main():
    x = np.arange(-10000.,10000.1,250.)
    y = np.arange(-7500.,7500.1,250.)
    X,Y = np.meshgrid(x,y)
    # Analytic gravity-like Gaussian anomaly; not a prism forward model.
    field = -5*np.exp(-((X+2000)/2200)**2-(Y/4200)**2) - 3*np.exp(-((X-3300)/1200)**2-(Y/3500)**2)
    result = compute_ms_qhgm(X,Y,field,ops,ops)
    response, threshold, ridges = detect_edge_ridges(result['MSQHGM'])
    assert np.isfinite(response).all()
    assert np.isfinite(result['MSQHGM']).all()
    assert np.all((response>=0)&(response<=1))
    assert int(ridges.sum())>0
    print('MS-QHGM end-to-end example: PASSED')
    print('Analysis heights (m):', result['heights'])
    print('Ridge pixels:', int(ridges.sum()))
    print('Otsu threshold:', float(threshold))

if __name__ == '__main__': main()
