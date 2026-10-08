"""Post-pass checks for the tutorial notebooks.

- strips empty code cells (they render as blank boxes)
- flags forbidden markup, multiple H1s, comma-separated :class:, unbalanced ::: fences
- checks that relative .ipynb links and ../../images/ paths exist
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN = [
    ('<div class="alert', "bootstrap alert div"),
    ("<details", "details/summary"),
    ("<font", "font tag"),
    ("style=", "inline style"),
    ("> **Important", "blockquote callout"),
    ("```{dropdown}", "backtick dropdown directive"),
    ("https://cecilehannay.github.io", "absolute self-link"),
]
problems = []
stripped = 0
for p in sorted(glob.glob(f"{ROOT}/notebooks/*/*.ipynb")):
    rel = os.path.relpath(p, ROOT)
    nb = json.load(open(p))
    cells = nb["cells"]
    keep = [c for c in cells if not (c["cell_type"] == "code" and not "".join(c["source"]).strip())]
    if len(keep) != len(cells):
        stripped += len(cells) - len(keep)
        nb["cells"] = keep
        json.dump(nb, open(p, "w"), indent=1); open(p, "a").write("\n")
    md = "\n".join("".join(c["source"]) for c in keep if c["cell_type"] == "markdown")
    # H1 count (ignore lines inside code fences)
    in_fence = False; h1 = 0
    for line in md.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence; continue
        if not in_fence and re.match(r"^# ", line):
            h1 += 1
    if h1 != 1:
        problems.append(f"{rel}: {h1} H1 headings")
    for needle, label in FORBIDDEN:
        if needle in md:
            problems.append(f"{rel}: contains {label} ({needle!r})")
    for m in re.finditer(r"^:class:\s*(.+)$", md, re.M):
        if "," in m.group(1):
            problems.append(f"{rel}: comma in :class: -> {m.group(0).strip()!r}")
    opens = len(re.findall(r"^:{3,}\{", md, re.M)); closes = len(re.findall(r"^:{3,}\s*$", md, re.M))
    if opens != closes:
        problems.append(f"{rel}: unbalanced colon fences (open={opens}, close={closes})")
    base = os.path.dirname(p)
    for m in re.finditer(r"\]\(([^)\s#]+\.ipynb)(?:#[^)]*)?\)", md):
        if not os.path.exists(os.path.normpath(os.path.join(base, m.group(1)))):
            problems.append(f"{rel}: broken link {m.group(1)}")
    for m in re.finditer(r"\]\((\.\./\.\./images/[^)\s]+)\)", md):
        if not os.path.exists(os.path.normpath(os.path.join(base, m.group(1)))):
            problems.append(f"{rel}: missing image {m.group(1)}")

print(f"stripped {stripped} empty code cell(s)")
print("\n".join(problems) if problems else "no problems found")
sys.exit(1 if problems else 0)
