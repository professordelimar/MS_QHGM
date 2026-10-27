# MS-QHGM

**Multiscale Quantile-Normalized Horizontal Gradient Magnitude for robust gravity edge detection**

This repository contains the reference implementation, synthetic experiments, real-data notebooks, and supporting material for the MS-QHGM method. MS-QHGM combines quantile normalization of the horizontal gradient magnitude with a fixed multiscale upward-continuation scheme to improve the representation of gravity-gradient edges when source amplitudes, structural wavelengths, and noise levels vary across a study area.

## Associated manuscript

**Multiscale Quantile-Normalized Horizontal Gradients for Robust Gravity Edge Detection**

The repository accompanies the manuscript submitted to *Computers & Geosciences*.

## Method summary

For each analysis height `h`, the horizontal gradient magnitude is

```text
H_h = sqrt(f_x,h^2 + f_y,h^2)
```

The scale-specific reference amplitude is the 75th percentile

```text
lambda_h = Q_0.75(H_h)
```

and the quantile-normalized response is

```text
Q_h = H_h / (H_h + lambda_h)
```

The fixed analysis heights are

```text
{0, 5*Delta, 10*Delta, 20*Delta}
Delta = max(dx, dy)
```

The normalized responses are averaged with equal weights and the final mean is rescaled to `[0, 1]`.

## Repository contents

### Reference code

- `ms_qhgm.py`: clean reference implementation of HGM, QHGM and MS-QHGM.
- `edge_detection.py`: automatic local-maximum ridge extraction with Otsu thresholding.

### Synthetic experiments

- `ms_cgtp_01_formulation.ipynb`: development notebook containing the synthetic methodology, sensitivity tests, and earlier formulation history.
- `ms_cgtp_01_formulation_figures.ipynb`: development notebook used to prepare synthetic figures and quantitative comparisons.

These two notebooks preserve the methodological development history. The final method specification is the formulation described in `ms_qhgm.py` and in the manuscript.

### Marajó Basin application

- `gravdata-bouguer.ipynb`: Bouguer-field application.
- `gravdata-bouguer_corrected.ipynb`: corrected Bouguer-field application.
- `gravdata-disturbance.ipynb`: gravity-disturbance application.
- `gravdata-isostatic.ipynb`: isostatic-disturbance application.
- `gravdata-anomaly.ipynb`: gravity-anomaly application.
- `gravdata.ipynb`: complete real-data processing notebook.
- `location-marajo(1)_modified.ipynb`: regional location map.
- `location-marajo(2)_modified.ipynb`: Marajó Basin outline workflow.
- `marajo_data.xyz`: gridded gravity dataset used by the real-data notebooks.

The manuscript uses the corrected Bouguer field as the principal real-data application.

## External files required by the real-data notebooks

Two shapefile datasets referenced by the notebooks were not present in the source archive used to prepare this repository package:

```text
marajo_basin_shapefile/marajo_basin.shp
estrutural_marajo/estrutural_marajo.shp
```

Place the complete shapefile sets in those directories before running the map and structural-overlay cells.

The notebooks also use a local `gravmag` package that provides the spectral derivative, upward-continuation, grid, synthetic, and prism routines used in the study. Set the environment variable `GRAVMAG_PARENT` to the directory containing the `gravmag` package before starting Jupyter.

Windows PowerShell example:

```powershell
$env:GRAVMAG_PARENT="C:\path\to\geophysics"
```

Linux or macOS example:

```bash
export GRAVMAG_PARENT=/path/to/geophysics
```

## Installation

Create a Python environment and install the public dependencies:

```bash
pip install -r requirements.txt
```

Then make sure the project-specific `gravmag` package is available through `GRAVMAG_PARENT` or already importable in the active Python environment.

## Running the notebooks

Start Jupyter from the repository root so that the relative paths to `marajo_data.xyz`, the shapefile directories, and `results/` remain valid:

```bash
jupyter notebook
```

The notebooks write generated figures to `results/`. Generated outputs in that directory are ignored by Git.

## Real-data grid used in the manuscript

The Marajó Basin dataset is processed on a `201 x 141` grid with approximate spacings of `5.561 km` and `5.529 km`. The MS-QHGM analysis heights are therefore approximately `0`, `27.804`, `55.607`, and `111.214 km`.

## Automatic ridge extraction

The post-processing detector used for HGM, QHGM, and MS-QHGM:

1. normalizes each response independently to `[0, 1]`;
2. identifies local maxima along either horizontal grid direction;
3. applies an Otsu threshold computed from the response itself;
4. removes the outer four grid cells.

Geological information is not used by the detector.

## Reproducibility note

The final MS-QHGM definition uses the 75th percentile at each scale, equal weighting across the four normalized scales, and final min-max normalization. These parameters are fixed across the synthetic and real-data analyses. Upward-continuation heights are analysis scales and should not be interpreted directly as source depths.

## Citation

If you use this repository, please cite the associated manuscript once the final bibliographic information and DOI are available.


## Quick test

A deterministic quick test is provided in
`quick_test.py`.

It checks quantile normalization, positive
amplitude-scaling invariance, four-scale
aggregation, and automatic ridge extraction.

Install NumPy and run:

```bash
python -m pip install numpy
python quick_test.py
```

A successful run prints:

```text
MS-QHGM quick test: PASSED
```

This lightweight test does not require the
external `gravmag` package.

Note that this test verifies the core
normalization and aggregation functions.
It does not reproduce the full synthetic
gravity experiments or the Marajo Basin
application described in the manuscript.


## External dependency: GravMag

The MS-QHGM research workflows use the
GravMag computational geophysics library,
developed and maintained by Nelson Ribeiro-Filho.

Repository:
https://github.com/professordelimar/gravmag

### Installation

Clone both repositories into the same
parent directory:

```bash
git clone https://github.com/professordelimar/gravmag.git
git clone https://github.com/professordelimar/MS_QHGM.git
```

Install the public Python dependencies:

```bash
cd gravmag
python -m pip install -r requirements.txt

cd ../MS_QHGM
python -m pip install -r requirements.txt
```

### Making GravMag available

Set GRAVMAG_PARENT to the parent directory
containing the cloned gravmag repository.

On Windows PowerShell:

```powershell
$env:GRAVMAG_PARENT = (Resolve-Path ..).Path
```

On Linux or macOS:

```bash
export GRAVMAG_PARENT="$(cd .. && pwd)"
```

The research notebooks use the GravMag
modules for potential-field modeling,
spectral differentiation, upward continuation,
and related numerical operations.

The dependency should be installed or
made importable before executing notebooks
that require it.
