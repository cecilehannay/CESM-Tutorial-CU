# Notes

## 2026-09-02
- Directory contains `Tutorial-CESM-CU-2025.pptx` (70-slide "Running CESM on Derecho" tutorial by Cécile Hannay).
- Built a Jupyter Book from the pptx content, structured like `/glade/u/home/hannay/CESM-Tutorial-AGU`:
  `_config.yml`, `_toc.yml`, `README.md`, `LICENSE`, `images/`, `notebooks/`.
- 10 chapters (01.Prerequisites through 10.Wrap-up), 36 notebooks total, following the outline
  from slide 11 of the pptx.
- Content and diagrams/screenshots were extracted directly from the pptx (via `python-pptx`);
  decorative clipart/logos were filtered out, kept images renamed descriptively in `images/`.
- Verified the book builds cleanly with classic Jupyter Book (`pip install --user "jupyter-book<2"`;
  note: `pip install jupyter-book` alone now installs the newer MyST-based v2, which is
  incompatible with this `_config.yml`/`_toc.yml` format — must pin `<2`).
- TODO / things to fill in later: exact tutorial date/time/location for the README, and
  whether to add a GitHub repo (currently `_config.yml` points to a placeholder
  `NCAR/CESM-Tutorial-CU` repo URL).
