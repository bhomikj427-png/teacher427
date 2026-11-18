"""Build the ECE2102 Digital Electronics ETE study pack (format: study-pack-format.md v1.2).

Run:  python build.py [file-prefix ...]
Figures and numbers are reused from the v1 pack (../../study-pack/pdf-ete/figs*.py, checked by its verify.py).
"""
import sys
from pathlib import Path

import matplotlib  # Agg canvas: tools/figlib's overlap check needs get_renderer() (the svg backend has none)
matplotlib.use("Agg")

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


def _kmy(ones, groups, dcs=()):
    """3-variable map for 2-state-bit machines: rows Y1, columns Y2 X (cell index = 4*Y1 + 2*Y2 + X)."""
    cells = {m: "1" for m in ones}
    cells.update({m: "X" for m in dcs})
    s = figs1.kfig.kmap(cells, [{"cells": c, "term": t, "color": i} for i, (c, t) in enumerate(groups)],
                        rv="A", cv="BC", cs=42, show_idx=True)
    return s.replace(">A</text>", ">Y₁</text>").replace(">BC</text>", ">Y₂X</text>")


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
import figs_u3  # noqa: E402  (v1.3 unit-3 figures, S2: waveforms + figs_u3_sch schematics)
ALL.update(figs_u3.FIGS)
import figs_u3c  # noqa: E402  (v1.3 unit-3 counter figures, S3)
ALL.update(figs_u3c.FIGS)
import figs_u4  # noqa: E402  (v1.3 unit-4 state-machine figures, S4)
ALL.update(figs_u4.FIGS)
import figs_u2  # noqa: E402  (v1.3 unit-2 MUX/decoder figures, S5)
ALL.update(figs_u2.FIGS)
import figs_u2b  # noqa: E402  (v1.3 figures for 04 and 08, S6)
ALL.update(figs_u2b.FIGS)
import figs_u2c  # noqa: E402  (v1.3 figures for 07, S6)
ALL.update(figs_u2c.FIGS)
import figs_u3r  # noqa: E402  (v1.3 figures for 11 and 14, S7)
ALL.update(figs_u3r.FIGS)
import matplotlib.pyplot as _plt  # noqa: E402  the v1 modules select the svg backend on import; figlib's check needs Agg
_plt.switch_backend("Agg")

ALL["adder_sub"] = lambda: figs1.ripple_adder(True)
ALL["km_T1"] = lambda: _km([1, 3, 5, 7], [([1, 3, 5, 7], "T1 = Q0")])
ALL["km_T2"] = lambda: _km([3, 7], [([3, 7], "T2 = Q1Q0")])
ALL["km_D1_down"] = lambda: _km([0, 3, 4, 7], [([0, 4], "Q1'Q0'"), ([3, 7], "Q1Q0")])
ALL["km_D2_down"] = lambda: _km([0, 5, 6, 7], [([6, 7], "Q2Q1"), ([5, 7], "Q2Q0"), ([0], "Q2'Q1'Q0'")])
ALL["km_J0_gray"] = lambda: _km([0, 6], [([0, 1], "Q2'Q1'"), ([6, 7], "Q2Q1")], dcs=[1, 3, 5, 7])
ALL["km_K0_gray"] = lambda: _km([3, 5], [([2, 3], "Q2'Q1"), ([4, 5], "Q2Q1'")], dcs=[0, 2, 4, 6])
ALL["km_cnt_D1"] = lambda: _kmy([3, 4, 5], [([4, 5], "Y1Y2'"), ([3], "Y1'Y2X")])
ALL["km_cnt_D2"] = lambda: _kmy([1, 4, 7], [([1], "Y1'Y2'X"), ([4], "Y1Y2'X'"), ([7], "Y1Y2X")])
ALL["km_gray_D1"] = lambda: _kmy([3, 6, 7], [([6, 7], "Y1Y2"), ([3, 7], "Y2X")])
ALL["km_gray_D2"] = lambda: _kmy([1, 3, 5, 7], [([1, 3, 5, 7], "X")])
ALL["km_T_1101"] = lambda: _kmy([3, 4, 5], [([4, 5], "Y1Y2'"), ([3], "Y1'Y2X")])
ALL["km_J_1101"] = lambda: _kmy([1, 5], [([1, 3, 5, 7], "X")], dcs=[2, 3, 6, 7])
ALL["km_K_1101"] = lambda: _kmy([2, 6], [([0, 2, 4, 6], "X'")], dcs=[0, 1, 4, 5])

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
