# Upload to GitHub

Extract the contents of this ZIP **into the root** of the existing `MS_QHGM` clone, not into a nested directory. Keep the existing `.git` folder, which is not included in this ZIP. If `marajo_data.xyz` is already present, compare its SHA-256 hash before replacing it.

Run from the repository root (Git Bash):

```bash
git status
git add -A
git --no-pager diff --cached --check
git --no-pager diff --cached --stat
git commit -m "docs: add reproducibility and data provenance guidance"
git push origin main
```

If Git reports no changes staged, skip the commit. Do not upload `.venv`, caches or notebook-generated outputs. Before re-submission, examine `REPRODUCIBILITY.md` and `DATA_AVAILABILITY.md` and complete the unverified items.
