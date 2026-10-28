# Multiscale quantile-normalized horizontal gradients for robust gravity edge detection

**Research code for the manuscript submitted to *Computers & Geosciences*.**  
**Corresponding author:** Nelson Ribeiro-Filho  
**Repository:** https://github.com/professordelimar/MS_QHGM

## Scope

This repository provides the MS-QHGM numerical implementation, edge-ridge detection, local `gravmag` potential-field routines, synthetic examples, tests and original analysis notebooks for gravity data from the Marajó Basin, Brazil. The public data file `marajo_data.xyz` is retained. Some notebooks require additional input data and have **not** been validated for full, cell-by-cell numerical reproduction.

## Structure

- `ms_qhgm.py`: multiscale quantile normalization and gradient combination.
- `edge_detection.py`: ridge extraction (undefined `eps` from the source archive corrected).
- `spectral_operators.py`: spectral gradients and upward continuation used by the standalone demonstration.
- `gravmag/`: local field-processing utilities imported by research notebooks.
- `examples/synthetic_example.py`: executable, self-contained Gaussian-field demonstration (not a prism forward model).
- `quick_test.py`: deterministic smoke test.
- `tests/`: numerical and edge-detection regression tests.
- `notebooks/`: research notebooks with code preserved and saved outputs cleared.
- `marajo_data.xyz`: original XYZ data.
- `DATA_AVAILABILITY.md`: scope and provenance limitations for real-data inputs.
- `REPRODUCIBILITY.md`: independently repeatable checks and remaining validation tasks.
- `requirements.txt`: core Python requirements.
- `requirements-notebooks.txt`: optional geospatial and notebook requirements; platform-specific dependencies may require additional setup.

## Installation (Python 3.12 recommended)

Windows PowerShell, in the repository root:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If `py -3.12` is unavailable, install a supported Python distribution and use its executable in place of `py -3.12`. The virtual environment must not be committed. For the optional notebook/geographic dependencies, run:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-notebooks.txt
```

## Verify the core implementation

```powershell
.\.venv\Scripts\python.exe -m pytest tests -v
.\.venv\Scripts\python.exe quick_test.py
.\.venv\Scripts\python.exe examples/synthetic_example.py
```

These tests exercise the spectral operators, quantile scaling, edge detector, and a deterministic Gaussian input. They do **not** verify exact agreement with published manuscript figures.

## Notebooks and Marajó Basin inputs

The `notebooks/` directory preserves method, figures, survey processing, and geographical plotting scripts. Some notebooks contain legacy absolute paths, assume a particular working directory, or refer to external inputs including full Shapefile sets (e.g., `*.shp`, `*.shx`, `*.dbf`, `*.prj`) that are not in this ZIP. `marajo_data.xyz` alone is not sufficient to execute all notebooks. These notebooks must be adapted to portable paths and their outputs compared with the article before claiming end-to-end reproducibility. No computed figures or results are represented as independently verified here.

## Reproducibility and citation

Please cite the associated article when bibliographic metadata become available, and cite the exact repository commit/release used. Before journal resubmission, archive an immutable release, document all external datasets and provenance, and compare figures/numeric outputs from a clean environment to the manuscript.

## Code availability statement

Source code and reproducible synthetic core example: https://github.com/professordelimar/MS_QHGM . The associated geographical workflows require supplementary external data as documented above.

## Licensing

No blanket software or dataset license is asserted for this archive. See `REPRODUCIBILITY.md` and `DATA_AVAILABILITY.md` for outstanding provenance, rights and reproducibility questions. The authors should select a compatible license after verifying module and dataset ownership.
