## Independent numerical example (no proprietary GravMag required)

This repository also provides an independent NumPy implementation of the
horizontal Fourier derivatives and upward continuation used by the MS-QHGM
reference interface. It is intended as an executable demonstration. **Its
numerical equivalence to the separately distributed GravMag implementation
has not yet been established**. Existing publication figures and quantitative
results must not be represented as reproduced by this demonstration.

### Requirements

Python 3.10+ and NumPy. From the root of `MS_QHGM`, run:

```bash
python -m pip install numpy
python examples/synthetic_example.py
python -m unittest discover -s tests -v
```

Expected example status: `MS-QHGM end-to-end example: PASSED`.

The example uses analytic Gaussian gravity-like anomalies and is **not**
the exact prism-based synthetic model published in the manuscript.

### Modules

- `spectral_operators.py`: `my_xderiv`, `my_yderiv`, and `my_upward_continuation`, compatible in calling signature with `compute_ms_qhgm` in `ms_qhgm.py`.
- `examples/synthetic_example.py`: end-to-end core HGM/QHGM/MS-QHGM and ridge extraction demonstration.
- `tests/test_spectral.py`: numerical unit/smoke tests.

The spectral boundary-extension taper is an independent implementation and
must be compared against the original GravMag code before claiming exact
reproducibility of publication results. The remainder of the manuscript's
notebooks, geospatial input files, exact prism modeling and quantitative
metrics require their own end-to-end validation.

### Licensing

A separate open-source license for the MS_QHGM repository should be agreed
by all rights holders and added before submission. Do not assume that public
access alone grants reuse rights, and do not copy proprietary GravMag source
into this repository without the necessary permissions.
