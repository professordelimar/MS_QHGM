# Audit and validation record

Source: user-provided `repositorio.zip`. This report does not claim complete reproduction of manuscript figures.

## Removed

- `.venv/` (third-party packages and binaries), `.pytest_cache/` and generated `__pycache__`/`.pyc`: build and runtime artifacts.
- `edge_detection_fixed.py`: its one-line epsilon correction was merged into `edge_detection.py` to avoid competing implementations.
- `notebooks/gravdata-bouguer.ipynb`: same extracted code cells as `notebooks/gravdata.ipynb`; retain the latter.
- `results/.gitkeep`, empty shapefile placeholder README directories: not executable source or reproducibility inputs.
- Saved notebook outputs: cleared so repository contains source rather than stale cell output.

## Retained cautiously

- Ten remaining notebooks, including the distinct Marajó and methodological workflows.
- Thirteen `gravmag` source modules: retained as source and potential indirect numerical dependencies; no untested internal function deletion was attempted.
- `marajo_data.xyz`, because it is the only substantive provided real-data input.

## Limitations

- External shapefile and some data inputs referenced by notebooks were not included.
- Notebooks have not been executed end-to-end; some require local path normalization and software not installed in the audit environment.
- Numerical validation addresses core smoke/regression tests, not the scientific claims or all figures in the submitted manuscript.
- Dependency ranges are initial conservative bounds, not a fully pinned lockfile.
- License and attribution require author review.
