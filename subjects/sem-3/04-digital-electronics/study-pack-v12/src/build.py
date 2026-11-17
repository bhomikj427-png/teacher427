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



# Figures whose v1 source functions are gone: reuse the rendered copies from DE-ETE-v1.html
# (extract_v1figs.py -> v1figs.json), keyed by the v1 placeholder.
import json  # noqa: E402
_V1 = json.loads((HERE / "v1figs.json").read_text(encoding="utf-8"))
_ALIAS = {
    "fsm_blocks": "fsm_block(False) + fsm_block(True)", "lfsr3": 'chain(3, "lfsr")',
    "shift4": 'chain(4, "shift")', "johnson4": 'chain(4, "johnson")', "johnson_waves": "johnson_waves()",
    "ripple_counter": "ripple_counter() + ripple_waves()", "setup_hold": "setup_hold()",
    "timing_path": "timing_path()", "astable_555": "astable_555()", "ring_osc": "ring_osc()",
    "hazard": "hazard_kmap() + glitch()", "noise_bands": "noise_bands()", "fanout_fig": "fanout_fig()",
    "ttl_nand": "ttl_nand()", "tristate_bus": "tristate_bus()", "ecl_gate": "ecl_gate()",
    "cmos_inv": 'commons("CMOS_Inverter.svg", 170)', "cmos_nand": 'commons("CMOS_NAND.svg", 190)',
    "memory_org": "memory_org()", "sram_cell": 'commons("SRAM_Cell_(6_Transistors).svg", 300)',
    "dram_cell": "dram_cell()", "pld_arrays": "pld_arrays()", "jk_wave_noq": "jk_wave(show_q=False)",
}
for _n, _k in _ALIAS.items():
    ALL[_n] = (lambda s: (lambda: s))(_V1[_k])
# K-maps, MUX and two-level figures drawn with arguments in v1: v1arg0, v1arg1, ... in v1figs.json order
_ARGS = [k for k in _V1 if k.startswith(("km(", "km5(", "mux_fig(", "two_level("))]
for _i, _k in enumerate(_ARGS):
    ALL[f"v1arg{_i}"] = (lambda s: (lambda: s))(_V1[_k])

import figs_u1  # noqa: E402  (v1.3 unit-1 figures, S1)
ALL.update(figs_u1.FIGS)

ALL["adder_sub"] = lambda: figs1.ripple_adder(True)
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
