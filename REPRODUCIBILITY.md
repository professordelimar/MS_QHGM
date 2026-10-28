# Verification and reproducibility

## Minimum recommended runtime

Use a clean Python 3.12 virtual environment. From repository root on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest tests -v
.\.venv\Scripts\python.exe quick_test.py
.\.venv\Scripts\python.exe examples/synthetic_example.py
```

If `python` is not Python 3.12, invoke the Python 3.12 executable explicitly when creating the environment.

On Linux/macOS, activate a clean environment and run the same `python -m ...` commands.

## Validation scope

The tests cover numerical properties of the spectral operators, quantile normalization and edge ridge routines; the examples use deterministic, synthetic inputs. These are **smoke tests**, not full scientific validation against the quantitative experiments and figures in the manuscript.

## Still needed for an independently reproducible paper

1. Map every figure and numerical table in the manuscript to a script/notebook, seed, input dataset and output file.
2. Provide missing geological/geographic assets and document input provenance and rights.
3. Replace absolute notebook input paths with portable relative paths.
4. Run every notebook in a fresh environment, record package versions and compare numerical and graphical outputs with the submitted PDF.
5. Tag a specific Git commit or release after this validation; use that identifier in the code availability statement.

## License and attribution

A repository-wide LICENSE is intentionally not supplied: the provenance and redistribution permissions for bundled `gravmag` modules and included data are unverified. Authors must confirm rights and choose a compatible license before submission. Do not automatically assume the author owns third-party components.
