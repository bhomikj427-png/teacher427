"""Build the ECE2102 Digital Electronics ETE study pack (format: study-pack-format.md v1.2).

Run:  python build.py [file-prefix ...]
Figures and numbers are reused from the v1 pack (../../study-pack/pdf-ete/figs*.py, checked by its verify.py).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(HERE.parents[1] / "study-pack" / "pdf-ete"))
from study_pack_build import build  # noqa: E402
import figs1, figs2  # noqa: E402,E401

ALL = {}
for m in (figs1, figs2):
    ALL.update({k: getattr(m, k) for k in dir(m) if not k.startswith("_") and callable(getattr(m, k))})


def _km(ones, groups, dcs=()):
    """3-variable map with rows Q2 and columns Q1Q0."""
    cells = {m: "1" for m in ones}
    cells.update({m: "X" for m in dcs})
    s = figs1.kfig.kmap(cells, [{"cells": c, "term": t, "color": i} for i, (c, t) in enumerate(groups)],
                        rv="A", cv="BC", cs=42, show_idx=True)
    return s.replace(">A</text>", ">Q₂</text>").replace(">BC</text>", ">Q₁Q₀</text>")


ALL["km_T1"] = lambda: _km([1, 3, 5, 7], [([1, 3, 5, 7], "T1 = Q0")])
ALL["km_T2"] = lambda: _km([3, 7], [([3, 7], "T2 = Q1Q0")])

# K-map classes from the site stylesheet (the renderer is shared with the site), light theme only.
KCSS = "\n".join(l for l in (ROOT / "site" / "static" / "style.css").read_text(encoding="utf-8").splitlines()
                 if l.lstrip().startswith((".k-", ".c0", ".c1", ".c2", ".c3", ".c4", ".fig-svg")))
VARS = (":root { --card:#fff; --soft:#f4f4f0; --g0:#2f5bea; --g1:#e0661b; --g2:#12925a; --g3:#b23fbf; --g4:#c2410c;"
        " --one:#1c1f24; --zero:#b7bac0; --x:#d97706; --bad:#d92d20; --good:#12925a; }\n"
        ".two { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; align-items: center; break-inside: avoid; }\n"
        ".two > * { min-width: 0; }\n")

if __name__ == "__main__":
    build(HERE, pack="ECE2102 Digital Electronics · ETE Study Pack", combined="ECE2102-DE-ETE-study-pack.pdf",
          figures=ALL, extra_css=VARS + KCSS, only=sys.argv[1:])
