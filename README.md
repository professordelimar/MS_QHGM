# Multiscale quantile-normalized horizontal gradients for robust gravity edge detection

**Reproducibility repository for a manuscript submitted to *Computers & Geosciences*.**

**Corresponding author:** Nelson Ribeiro-Filho  
**Repository:** https://github.com/professordelimar/MS_QHGM  
**Status:** Research code under verification; complete end-to-end reproduction has **not yet** been independently validated.

## Overview

This repository contains the Python implementation and Jupyter notebooks associated with the manuscript *Multiscale quantile-normalized horizontal gradients for robust gravity edge detection*. The research investigates multiscale processing and quantile-based normalization of horizontal-gradient responses for identifying gravity-field edges, with synthetic experiments and an application to gravity data from the Marajó Basin, Brazil.

The purpose of this repository is to provide the computational workflow, supporting routines, and instructions needed to inspect and reproduce the reported analyses. **Results should be considered reproducible only after the input data, computational environment, and numerical outputs have been independently checked.**

## Repository organization

```text
MS_QHGM/
├── README.md
├── requirements.txt                # maintain and verify dependency versions
├── ms_qhgm.py                     # existing implementation: retain until compared
├── edge_detection.py             # original edge-detection utilities
├── edge_detection_fixed.py       # minimal fix for undefined `eps`
├── gravmag/                       # local scientific-computing modules
│   ├── __init__.py
│   ├── auxiliars.py
│   ├── constants.py
│   ├── cylinder.py
│   ├── derivative.py
│   ├── filtering.py
│   ├── grids.py
│   ├── hexagonalprism.py
│   ├── polygonalprism.py
│   ├── prism.py
│   ├── sphere.py
│   ├── statistical.py
│   └── synthetic.py
└── notebooks/
    ├── ms_cgtp_01_formulation.ipynb
    ├── ms_cgtp_01_formulation_figures.ipynb
    ├── gravdata.ipynb
    ├── gravdata-anomaly.ipynb
    ├── gravdata-bouguer.ipynb
    ├── gravdata-bouguer_corrected.ipynb
    ├── gravdata-disturbance.ipynb
    ├── gravdata-isostatic.ipynb
    ├── gravdata-Copy1.ipynb
    ├── location-marajo(1)_modified.ipynb
    └── location-marajo(2)_modified.ipynb
```

The listed notebooks and Python files correspond to a consolidated source-code archive. Other existing repository files, if present, should be examined before deletion; the published `ms_qhgm.py` is not included in the archive and has not yet been compared against the other implementations.

## Requirements and installation

Python 3 and Jupyter are required. Relevant imports found in the notebooks include NumPy, SciPy, Matplotlib, pandas, `cmcrameri`, GeoPandas, Cartopy and other geospatial libraries; the exact environment and versions must be verified for full reproduction.

```bash
git clone https://github.com/professordelimar/MS_QHGM.git
cd MS_QHGM
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install jupyter
```

**Important:** The existing `requirements.txt` must be checked and updated to include all actually used dependencies and compatible versions. This installation procedure has not been validated on a fresh machine.

## Using the source code

From the repository root:

```bash
python -c "from gravmag import filtering, derivative, grids, synthetic, prism; print('gravmag imports OK')"
python -c "import edge_detection_fixed; print('edge detection imports OK')"
python -m jupyter notebook
```

Open `notebooks/ms_cgtp_01_formulation.ipynb` for the method-oriented experiments and `notebooks/ms_cgtp_01_formulation_figures.ipynb` for the related figures. The `gravdata-*.ipynb` and `location-marajo*.ipynb` notebooks are related to gravity-data processing and visualization for the Marajó Basin.

**Working-directory warning:** Some notebooks originally used absolute local paths for `gravmag` and external data. Update these paths to the repository root and the local input-data directories before running. Import success is not a substitute for verifying the numerical outputs.

## Data availability and reproducibility limitations

The Jupyter notebooks for the Marajó Basin reference external geographical inputs, including ESRI Shapefiles such as `marajo_basin.shp` and `estrutural_marajo/estrutural_marajo.shp`. A complete Shapefile usually comprises several companion files (for example, `.shp`, `.shx`, `.dbf`, and `.prj`). Other potential-field datasets and local file paths may also be required.

These datasets **are not part of the code-only archive** and their publication rights, provenance, processing history, and download locations must be documented before full reproduction can be claimed. Do not assume the notebooks will run without these inputs.

Recommended validation steps before journal resubmission:

1. Confirm the license and attribution of every included `gravmag` component.
2. Resolve notebook-local and absolute data paths.
3. Pin tested dependency versions in `requirements.txt` or an environment lock file.
4. Provide a small self-contained example with known inputs and expected numerical outputs.
5. Run the key notebooks in a clean environment and compare their generated figures and quantitative values with those in the manuscript.
6. Add an exact commit hash or archived release to the manuscript's Code Availability statement.

## Method and provenance

The implementation uses potential-field operations from the included `gravmag` modules, together with edge-detection routines and the multiscale workflows in the notebooks. The complete mathematical definitions, processing parameters, synthetic configurations, and interpretation of the Marajó Basin results are described in the associated manuscript.

The repository contains two versions of the edge utility script: `edge_detection.py` is retained as the original, while `edge_detection_fixed.py` defines the numerical epsilon `eps` used by the original functions. The revised file has received only a minimal correction; equivalence of all downstream scientific results has **not** been established.

## Citation

If this software supports your research, cite the associated manuscript **once publication metadata are available**, and identify the exact repository commit or release used. Until publication, please refer to the repository title, author, GitHub URL, and commit identifier; do not invent a DOI.

## Code availability for the manuscript

The code associated with this study is maintained at https://github.com/professordelimar/MS_QHGM. A specific version (commit/release), computational environment, example inputs, and validation outputs should be recorded before the final editorial resubmission.

## License and third-party attribution

Do not assume that all `gravmag` modules and derived materials are eligible for redistribution under the same license. Preserve original copyright and attribution notices, and add or reconcile a repository `LICENSE` file only after confirming ownership and third-party licensing conditions. Dataset licenses may differ from software licenses.

## Contact

**Nelson Ribeiro-Filho** — corresponding author.  
GitHub: https://github.com/professordelimar
