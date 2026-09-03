# Notes

Working notes for building/maintaining this Jupyter Book. Not part of the published book
(deliberately left out of `_toc.yml`).

## Where things live

- **Live site**: https://cecilehannay.github.io/CESM-Tutorial-CU/
- **Repo**: https://github.com/cecilehannay/CESM-Tutorial-CU (personal account, not the NCAR
  org — NCAR org policy blocks GitHub Actions on new repos there; moved here so the
  build-and-deploy workflow could actually run. `_config.yml` and `README.md` point here too.)
- Source material: `Tutorial-CESM-CU-2025.pptx` (70-slide "Running CESM on Derecho" deck by
  Cécile Hannay) — kept local only, in `.gitignore`, not committed.

## How to build locally

```bash
export PATH="$HOME/.local/bin:$PATH"
jupyter-book build .
rm -rf _build   # after checking, don't commit build output
```
Needs classic Jupyter Book, not the new MyST-based v2:
```bash
pip install --user "jupyter-book<2"
```
A plain `pip install jupyter-book` grabs v2, which doesn't understand this `_config.yml`/
`_toc.yml` format at all.

## Deployment

`.github/workflows/gh-page_builder.yml` builds the book and pushes `_build/html` to a
`gh-pages` branch on every push to `main`. Two one-time settings needed on GitHub (already
done for the current repo, but needed again if the repo ever moves):
1. Settings → Actions → General → Workflow permissions → "Read and write permissions"
   (default read-only blocks the push to `gh-pages`).
2. Settings → Pages → Build and deployment → Source → "Deploy from a branch" → `gh-pages` / `(root)`.

## Structure

10 numbered chapters (`01.Prerequisites` … `10.Wrap-up`) plus an `11.Additional-Materials`
part for optional/self-paced content (namelist challenge exercises, a quick Python/`xarray`
look at output, and the "why use CESM" aside). Modeled on
`/glade/u/home/hannay/CESM-Tutorial-AGU`'s layout.

- Chapter folders keep their `NN.Name` prefix (e.g. `05.Run-length/`).
- Section notebook **files** carry an `N.M_` prefix matching their position in `_toc.yml`
  (e.g. `5.1_xml_files.ipynb`) — but the page **titles/headings inside** the notebooks do
  *not* repeat that number (tried Jupyter Book's `numbered: true` toctree option to get this
  automatically; it crashes the build for this TOC layout — files referenced from a different
  chapter than they physically live in trigger a `KeyError`/`UnboundLocalError` in
  `sphinx-external-toc`'s section-numbering collector — so numbers are set by hand in
  filenames only).
- Chapter-level `title.ipynb` files are never renamed/numbered (the folder prefix already
  covers it).
- Two files physically live in a different chapter folder than their topic name suggests,
  because they were moved into Additional Materials by TOC position:
  `11.Additional-Materials/11.1_why_cesm.ipynb` and `.../11.3_more_exercises.ipynb`.
- The "Overview of CESM directories" diagrams (`images/cesm_directories_*.png`) were rendered
  from the original pptx slides, not hand-drawn: downloaded a portable LibreOffice (RPM
  tarball, extracted with `rpm2cpio`/`cpio`, no root/module needed — nothing installed
  system-wide, would need re-downloading to scratch if more slides need rendering later),
  converted the deck to PDF headless, rasterized specific pages with `pdftoppm`, and either
  cropped or (for slides where content overlapped the banner) pixel-diffed against a clean
  slide to mask out just the "Community Earth System Model Tutorial" footer banner.

## Conventions

- No `Co-Authored-By: Claude` trailer on commits (user asked to stop adding it partway
  through; earlier commits still have it, left as-is).
- Cross-notebook links are relative markdown links (`../05.Run-length/5.1_xml_files.ipynb`);
  images use `../../images/...` relative paths, not absolute GitHub Pages URLs (one snuck in
  from a manual edit and had to be fixed back to relative — absolute URLs only work once
  already deployed, break local preview builds).
- Cécile edits notebooks directly in Jupyter herself sometimes — watch for cells accidentally
  left as `code` type when they should be `markdown` (renders as an unstyled, unhighlighted
  code block and throws a Sphinx lexer warning at build time — easy to miss by eye, easy to
  confirm via the build warning).

## Open items / things mentioned but not yet done

- `unix.ipynb` prerequisites page exists and is linked in; `title.ipynb` for Prerequisites
  also promises brief intros/links for a text editor and Jupyter notebooks specifically —
  no pages for those two yet.
- Possible further length/clarity passes on other concept-heavy pages (xml_files,
  namelist_overview) if the same "duplicate tables" pattern shows up there too.
