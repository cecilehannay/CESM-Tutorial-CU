# CESM-Tutorial-CU editorial style guide (for this rewrite pass)

Audience: undergraduates and a few early grad students, "Climate Modeling Laboratory" at CU.
Two 75-minute hands-on sessions on Derecho. Many have never used a terminal or an HPC system.

## Voice
- Second person, present tense, direct: "You will...", "Run...", "Check that...".
- Short sentences. One idea per paragraph. Prefer concrete examples (`case01`) over abstractions.
- Define jargon on first use in a page, in plain words, then use the term. Don't over-explain; the glossary (11.4) exists.
- Warm but not gushing. Reassurance ("Don't worry if...") at most once per page, only where students genuinely get stuck.
- Say *why* a step matters in one clause when it isn't obvious ("...so Derecho knows which allocation to charge").
- Keep Cécile's own wording where it already exists (chapters 01–04 were largely written by her); fix typos, duplication, and formatting, don't rewrite her sentences for taste.

## Page structure
- Exactly ONE H1 per notebook: the page title, in the first markdown cell. Never a second `# ` later in the page.
- Sentence case for titles and headings (capitalize only the first word and proper nouns/acronyms): "Change the length of a run", "Output, log, and timing files", "Exercise 2: Extend a run".
- Sections are `##`; use `###` sparingly. No `<hr>` separators — headings do that job.
- Each content page opens with 1–3 sentences saying what the page covers or what the student will do.
- Chapter `title.ipynb` pages: H1 + a short paragraph (2–5 sentences) on what the chapter covers and what the student will be able to do; optionally one image.
- Do NOT repeat material that lives on another page — link to it instead with a relative link, e.g. `[Project code issues](../09.Troubleshooting/9.2_project_code_issues.ipynb)`. Never absolute `https://cecilehannay.github.io/...` links to our own pages.
- Images: keep existing relative paths (`../../images/...`). Don't add or remove images unless told.
- No trailing empty code cells. Notebooks are markdown cells only (except 11.2 which has real code cells).

## Callouts — use ONLY these (MyST colon fences, so code blocks inside can use normal ```)
Exercise statement (top of an exercise page, right after the intro sentence):
:::{admonition} Exercise 2: Extend a run
:class: exercise
What the student must do, as a short numbered or bulleted list.
:::

Hints (collapsed):
:::{admonition} Hints
:class: hint dropdown
...
:::

Solution (collapsed):
:::{admonition} Solution
:class: solution dropdown
...
:::

Other callouts: `:::{note}`, `:::{tip}`, `:::{important}`, `:::{warning}` (same fence syntax, no title line needed).
Optional-material notice at the top of a page: `:::{admonition} This exercise is optional` + `:class: warning`.
Collapsible reference material inside a long page: `:::{admonition} Title` + `:class: note dropdown`.

Rules:
- `:class:` values are space-separated (NOT comma-separated).
- If a callout must contain another callout, give the outer one four colons `::::`.
- Blank line after the `:class:` line is optional; blank line before the closing `:::` is fine.
- Do NOT use: `<div class="alert ...">`, `<details>/<summary>`, `<font ...>`, inline `style=` attributes, `> **Important:**` blockquote callouts, backtick-fenced ```{dropdown}``` directives (their inner code fences break).
- Plain inline HTML like `<code>` or `<br>` inside table cells is fine where already used.

## Code blocks
- Shell commands in ```bash; sample output in ```text; file contents (xml/namelist) in ```text or ```fortran.
- One command per line; brief `# comments` only when the command isn't self-explanatory.
- Placeholders: `$USER`, `$CASE`, `CASE_NAME`; always say once on the page that they must be replaced.

## Exercises
- Exercise pages: intro sentence → `exercise` admonition with the task → (optional) step-by-step guidance → `Hints` dropdown → `Solution` dropdown → "How to check it worked" (what file/line to look for).
- Session 2 exercises (chapters 6–7) use the homework case `b1850_hw`; add a one-line fallback: students who didn't finish the homework can use `case01` from Exercise 2 instead.
- Keep instructor-specific fallback paths (e.g. `/glade/u/home/tliefer/cases/case01`) as they are; Cécile owns those.

## Writing notebooks
- Regenerate each notebook with Python (nbformat 4, nbformat_minor 5), markdown cells with `"id"` fields, kernelspec/language_info metadata copied from the existing file. Split content into a few logical cells (title cell, then one cell per major section is fine).
- Do not run `jupyter-book build` (shared `_build` dir; the coordinator builds once at the end). Do not run git.
- After writing, re-open each file with json.load to make sure it's valid, and grep your output for forbidden markup (`<div class="alert`, `<details>`, `<font`, `style=`, "> **Important").
