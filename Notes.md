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
- Cécile edits and commits/pushes directly herself too, in parallel with Claude sessions —
  git history has both (short messages like "unix", "derecho", "cesm maze", "some prereq" are
  hers; longer descriptive ones are Claude's). Both work in the same checkout, so a file can
  change on disk between one tool call and the next — treat that as normal, re-read rather
  than assume staleness. Watch for cells accidentally left as `code` type when they should be
  `markdown` from manual Jupyter edits (renders as an unstyled, unhighlighted code block and
  throws a Sphinx lexer warning at build time — easy to miss by eye, easy to confirm via the
  build warning).

## October 2026 "improve overall" pass (less repetition, consistent format, undergrad level)

- **Style guide lives in `STYLE.md`** (voice, one H1 per page, sentence-case headings, the
  only allowed callouts). Follow it for every edit. In short, callouts are MyST colon fences:
  `:::{admonition} Exercise N: ...` + `:class: exercise`, `Hints` with `:class: hint dropdown`,
  `Solution` with `:class: solution dropdown`, plus `:::{note}` / `{tip}` / `{important}` /
  `{warning}`. No `<div class="alert">`, `<details>`, `<font>`, inline `style=`, or
  `> **Important:**` blockquotes anywhere. `:class:` values are space-separated.
- Colon fences need `parse: myst_enable_extensions: [colon_fence, ...]` in `_config.yml`
  (set explicitly). `only_build_toc_files: true` keeps `Notes.md`/`STYLE.md` out of the site.
- **`tools/lint_notebooks.py`** — run before building: strips empty code cells (they render
  as blank boxes), flags forbidden markup, multiple H1s, comma-separated `:class:`,
  unbalanced `:::` fences, broken relative links and missing images. Exit code 1 on problems.
- **Look and feel** is all in `_static/custom.css` (+ `custom.js`): Google fonts (Source
  Sans 3 body/headings, Source Code Pro code) via `@import`; CESM-blue accent through the
  theme's `--pst-color-primary`; blue H1s; striped tables with shaded header row; exercise
  callouts (blue) and solution callouts (green); exercise/homework pages tinted amber (class
  added by `custom.js` from the URL containing "exercise"/"homework"). Dark-mode values exist
  but are unverified.
- What got deduplicated: chapter 4 had three stacked drafts of the workflow page and two of
  Exercise 1 (kept Cécile's newest, folded in the `qstat`/log/archive checks); `3.2` had two
  "where are we" sections; `1.2` had two `less`/`more` sections and two formats; the
  project-code fallback was explained in four places and now lives only in `9.2` (others
  link). Chapters 5–7, 9–10 were rewritten in the undergrad voice; 1–4 kept Cécile's wording.
- Session-2 exercises (6.2, 6.4) use the homework case `b1850_hw`, with a one-line fallback
  to `case01` from Exercise 2.

## Open items / things to confirm with Cécile

- `5.4_homework.ipynb` still says "Send the list of commands you used to both Aneesh and
  Cecile on Slack" — course staff names may need updating each year.
- Instructor fallback paths for students whose runs didn't finish:
  `/glade/u/home/tliefer/cases/case01` (6.2) and
  `/glade/derecho/scratch/amiller/archive/case01/atm/hist` (6.4). The scratch one is almost
  certainly purged by now; both are kept verbatim pending her say-so.
- Dark-mode colours in `custom.css` are best-effort, never viewed in a browser.
- The solution for Exercise 5 states the B1850 default `co2vmr` is about `284.7e-6`
  (doubled `569.4e-6`) — worth a one-time check against a real `CaseDocs/atm_in`.
