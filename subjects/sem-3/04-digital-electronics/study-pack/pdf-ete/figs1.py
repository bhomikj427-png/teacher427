"""Figures for DE-ETE-v1.pdf: shared helpers, cover, Part A (combinational) and Part B (MSI).

Every public function returns inline SVG. Everything is generated (matplotlib, schemdraw, the site's K-map
renderer). The DE-v1 figure module (../pdf/figs.py) is loaded and its public figures re-exported, so the
ETE-half figures (shift registers, timing, FSM blocks, logic families, memories, PLDs) are reused unchanged.
"""
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("de_v1_figs", HERE.parent / "pdf" / "figs.py")
v1 = importlib.util.module_from_spec(_spec)
sys.modules["de_v1_figs"] = v1
_spec.loader.exec_module(v1)
globals().update({k: getattr(v1, k) for k in dir(v1) if not k.startswith("_") and callable(getattr(v1, k))
                  and getattr(getattr(v1, k), "__module__", "") == "de_v1_figs"})

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon, Circle, Rectangle  # noqa: E402
import schemdraw  # noqa: E402
import schemdraw.elements as elm  # noqa: E402
import schemdraw.logic as lg  # noqa: E402

kfig = v1.kfig
INK, MUTED, LINE, SOFT = v1.INK, v1.MUTED, v1.LINE, v1.SOFT
ACC, G1, G2, G3, BAD = v1.ACC, v1.G1, v1.G2, v1.G3, v1.BAD
TINT = "#e8eefe"
_svg, _canvas, _box, _arrow, _line = v1._svg, v1._canvas, v1._box, v1._arrow, v1._line
schemdraw.use("svg")
schemdraw.svgconfig.text = "text"      # real <text>, so the browser font supplies ⊕ and ⊙


def _nat(fig):
    """matplotlib figure -> svg shown at its natural size (figure width in inches), never scaled up."""
    w = fig.get_figwidth() * 25.4
    return f'<div style="width:{w:.0f}mm;max-width:100%;margin:0 auto">{_svg(fig)}</div>'


# ------------------------------------------------------------------ schemdraw helpers
def _d(unit=1.6, fs=12):
    d = schemdraw.Drawing(show=False)
    d.config(unit=unit, fontsize=fs, lw=1.4, color=INK, font="Segoe UI, Arial, sans-serif")
    return d


def _sd(d, width=None):
    """schemdraw drawing -> svg; width = display width in mm."""
    s = d.get_imagedata("svg").decode()
    s = s[s.index("<svg"):]
    m = re.search(r'width="([\d.]+)pt"', s)
    w = width or float(m.group(1)) * 0.3528 * 0.8
    s = re.sub(r'(<svg[^>]*?)\sheight="[^"]+"\swidth="[^"]+"', r"\1", s, count=1)
    return f'<div style="width:{w:.0f}mm;max-width:100%;margin:0 auto">{s}</div>'


def _wire(d, src, dst, xm):
    d += elm.Line().endpoints(src, (xm, src[1]))
    d += elm.Line().endpoints((xm, src[1]), (xm, dst[1]))
    d += elm.Line().endpoints((xm, dst[1]), dst)


def _inputs(d, g, labs, length=0.7):
    for k, lab in enumerate(labs):
        d += elm.Line().at(getattr(g, f"in{k + 1}")).left(length).label(lab, loc="left")


# ------------------------------------------------------------------ cover
def flow_map():
    parts = [("A", "Combinational\nlogic design", "Boolean algebra, K-map,\nNAND/NOR, adders"),
             ("B", "MSI devices", "MUX, decoder, encoder,\ncomparator, parity, ALU"),
             ("C", "Sequential\nlogic", "latches, flip-flops,\nregisters, counters, timing"),
             ("D", "State\nmachines", "FSM design, reduction,\nASM, generators, async"),
             ("E", "Logic families,\nmemories, PLDs", "TTL, ECL, CMOS,\nRAM/ROM, PLA/PAL")]
    fig, ax = _canvas(9.6, 2.5, (-0.2, 12.4), (-1.6, 1.9))
    for i, (p, t, s) in enumerate(parts):
        x = i * 2.5
        _box(ax, x, 0.3, 2.1, 1.3, t, fc=TINT, ec=ACC, fs=9.2, r=0.14, weight="bold")
        ax.text(x + 0.12, 1.5, p, fontsize=8, color=ACC, weight="bold", va="top")
        ax.text(x + 1.05, 0.1, s, fontsize=7.6, color=MUTED, ha="center", va="top")
        if i:
            _arrow(ax, (x - 0.4, 0.95), (x, 0.95), color=ACC)
    ax.text(0, -1.0, "no memory: output = f(present inputs)", fontsize=8.5, color=G1, weight="bold")
    _line(ax, [0, 4.6], [-1.15, -1.15], color=G1, lw=2)
    ax.text(5.0, -1.0, "memory: output = f(inputs, stored state)", fontsize=8.5, color=G2, weight="bold")
    _line(ax, [5.0, 9.6], [-1.15, -1.15], color=G2, lw=2)
    ax.text(10.0, -1.0, "what gates are made of", fontsize=8.5, color=G3, weight="bold")
    _line(ax, [10.0, 12.1], [-1.15, -1.15], color=G3, lw=2)
    return _svg(fig)


# ------------------------------------------------------------------ Part A
def gates_row():
    d = _d(fs=11)
    specs = [(lg.And, "AND", "A·B"), (lg.Or, "OR", "A + B"), (lg.Not, "NOT", "A'"), (lg.Nand, "NAND", "(A·B)'"),
             (lg.Nor, "NOR", "(A + B)'"), (lg.Xor, "XOR", "A ⊕ B"), (lg.Xnor, "XNOR", "A ⊙ B")]
    for i, (G, name, ex) in enumerate(specs):
        g = d.add(G().right().at((i * 3.1, 0)).anchor("out"))
        d += elm.Label().at((i * 3.1 - 0.9, 1.0)).label(name, fontsize=11)
        d += elm.Label().at((i * 3.1 - 0.9, -1.0)).label(ex, fontsize=11, color=ACC)
    return _sd(d, 172)


def _cells_of(term, names, pos=False):
    """Minterm indices covered by a product term (or, with pos, the zeros covered by a sum term)."""
    n = len(names)
    t = term.replace(" ", "").strip("()").replace("+", "")
    want = {}
    i = 0
    while i < len(t):
        v = t[i]; i += 1
        comp = i < len(t) and t[i] == "'"
        if comp:
            i += 1
        want[v] = (0 if comp else 1) if not pos else (1 if comp else 0)
    return [m for m in range(2 ** n) if all(((m >> (n - 1 - names.index(v))) & 1) == b for v, b in want.items())]


def km(names, ones, dcs=(), terms=(), pos=False, cs=44, split=None, idx=True, title=None):
    """K-map of F(names) with the given groups drawn. names: string, one char per variable."""
    n = len(names)
    k = split or n // 2
    cells = {m: "1" for m in ones}
    cells.update({m: "X" for m in dcs})
    groups = [{"cells": _cells_of(t, names, pos), "term": t, "color": i % 5, **({"zeros": True} if pos else {})}
              for i, t in enumerate(terms)]
    return kfig.kmap(cells, groups, rv=names[:k], cv=names[k:], cs=cs, show_idx=idx, title=title, emph0=pos)


def km5(names, ones, dcs, terms):
    cells = {m: "1" for m in ones}
    cells.update({m: "X" for m in dcs})
    groups = [{"cells": _cells_of(t, names), "term": t, "color": i % 5} for i, t in enumerate(terms)]
    s = kfig.kmap5(cells, groups, cs=38)
    return s.replace("wx", names[1:3]).replace("yz", names[3:]).replace("v = 0", names[0] + " = 0").replace("v = 1", names[0] + " = 1")


def two_level(terms, g1="And", g2="Or", out="F", width=None, single=()):
    """Two-level circuit: one first-level gate per term into one output gate. single: literals wired straight in."""
    d = _d()
    G1_, G2_ = getattr(lg, g1), getattr(lg, g2)
    n = len(terms) + len(single)
    ys = [(n - 1) * 0.9 - i * 1.8 for i in range(n)]
    o = G2_(inputs=n).right().at((6.2, 0)).anchor("in1" if n == 2 else f"in{(n + 1) // 2}")
    if n == 2:
        o = G2_(inputs=2).right().at((6.2, 0.33)).anchor("in1")
    d += o
    for i, labs in enumerate(terms):
        g = d.add(G1_(inputs=len(labs)).right().at((2.2, ys[i])).anchor("out"))
        _inputs(d, g, labs)
        _wire(d, g.out, getattr(o, f"in{i + 1}"), 3.2 + 0.45 * (i if ys[i] >= 0 else n - 1 - i))
    for j, lab in enumerate(single):
        i = len(terms) + j
        pin = getattr(o, f"in{i + 1}")
        d += elm.Line().endpoints((0.35 - 0.7, ys[i]), (3.2, ys[i])).label(lab, loc="left")
        _wire(d, (3.2, ys[i]), pin, 3.2 + 0.45 * (n - 1 - i))
    d += elm.Line().at(o.out).right(0.7).label(out, loc="right")
    return _sd(d, width)


def nor_inverter():
    d = _d()
    g = d.add(lg.Nor().right())
    d += elm.Line().at(g.in1).left(0.5)
    d += elm.Line().down(g.in1[1] - g.in2[1])
    d += elm.Line().right(0.5)
    mid = (g.in1[0] - 0.5, (g.in1[1] + g.in2[1]) / 2)
    d += lg.Dot().at(mid)
    d += elm.Line().at(mid).left(0.9).label("P", loc="left")
    d += elm.Line().at(g.out).right(0.8).label("F = (P + P)' = P'", loc="right")
    return _sd(d, 78)


def universal_nand():
    """NOT, AND, OR built from NAND gates only."""
    d = _d(fs=11)
    g = d.add(lg.Nand().right().at((0, 0)).anchor("out"))
    d += elm.Line().at(g.in1).left(0.4); d += elm.Line().down(g.in1[1] - g.in2[1]); d += elm.Line().right(0.4)
    d += elm.Line().at((g.in1[0] - 0.4, 0)).left(0.6).label("X", loc="left")
    d += elm.Line().at(g.out).right(0.5).label("X'", loc="right")
    a = d.add(lg.Nand().right().at((5.2, 0)).anchor("out")); _inputs(d, a, ["X", "Y"], 0.5)
    b = d.add(lg.Nand().right().at((7.6, 0)).anchor("out"))
    d += elm.Line().endpoints(a.out, (a.out[0] + 0.45, 0))
    d += elm.Line().endpoints((a.out[0] + 0.45, b.in1[1]), (a.out[0] + 0.45, b.in2[1]))
    d += elm.Line().endpoints((a.out[0] + 0.45, b.in1[1]), b.in1); d += elm.Line().endpoints((a.out[0] + 0.45, b.in2[1]), b.in2)
    d += elm.Line().at(b.out).right(0.5).label("X·Y", loc="right")
    x0 = 12.6
    for y, lab in ((0.9, "X"), (-0.9, "Y")):
        n = d.add(lg.Nand().right().at((x0, y)).anchor("out"))
        d += elm.Line().at(n.in1).left(0.4); d += elm.Line().down(n.in1[1] - n.in2[1]); d += elm.Line().right(0.4)
        d += elm.Line().at((n.in1[0] - 0.4, y)).left(0.6).label(lab, loc="left")
    o = d.add(lg.Nand().right().at((x0 + 2.6, 0)).anchor("out"))
    _wire(d, (x0, 0.9), o.in1, x0 + 0.4); _wire(d, (x0, -0.9), o.in2, x0 + 0.4)
    d += elm.Line().at(o.out).right(0.5).label("X + Y", loc="right")
    for x, t in ((-1.2, "NOT"), (5.4, "AND"), (12.6, "OR")):
        d += elm.Label().at((x, 2.0)).label(t, fontsize=11, color=ACC)
    return _sd(d, 172)


def xor_nand():
    d = _d(fs=11)
    g1 = d.add(lg.Nand().right().at((2, 0)).anchor("out"))
    g2 = d.add(lg.Nand().right().at((5.2, 1.1)).anchor("out"))
    g3 = d.add(lg.Nand().right().at((5.2, -1.1)).anchor("out"))
    g4 = d.add(lg.Nand().right().at((8.2, 0)).anchor("out"))
    d += elm.Line().endpoints(g1.in1, (-0.6, g1.in1[1])); d += elm.Line().endpoints((-0.6, g1.in1[1]), (-0.6, g2.in1[1]))
    d += elm.Line().endpoints((-1.3, g2.in1[1]), g2.in1).label("A", loc="left")
    d += elm.Line().endpoints(g1.in2, (-0.6, g1.in2[1])); d += elm.Line().endpoints((-0.6, g1.in2[1]), (-0.6, g3.in2[1]))
    d += elm.Line().endpoints((-1.3, g3.in2[1]), g3.in2).label("B", loc="left")
    d += lg.Dot().at((-0.6, g2.in1[1])); d += lg.Dot().at((-0.6, g3.in2[1]))
    d += elm.Line().endpoints(g1.out, (2.6, 0)); d += lg.Dot().at((2.6, 0))
    _wire(d, (2.6, 0), g2.in2, 2.6); _wire(d, (2.6, 0), g3.in1, 2.6)
    _wire(d, g2.out, g4.in1, 5.8); _wire(d, g3.out, g4.in2, 5.8)
    d += elm.Line().at(g4.out).right(0.6).label("A ⊕ B", loc="right")
    d += elm.Label().at((2.2, -0.75)).label("(AB)'", fontsize=10, color=MUTED)
    return _sd(d, 110)


def half_adder():
    d = _d()
    x = d.add(lg.Xor().right().at((3, 0.9)).anchor("out"))
    a = d.add(lg.And().right().at((3, -0.9)).anchor("out"))
    d += elm.Line().endpoints((-0.6, x.in1[1]), x.in1).label("A", loc="left")
    d += elm.Line().endpoints((-0.6, x.in2[1]), x.in2).label("B", loc="left")
    _wire(d, (0.2, x.in1[1]), a.in1, 0.2); _wire(d, (0.6, x.in2[1]), a.in2, 0.6)
    d += lg.Dot().at((0.2, x.in1[1])); d += lg.Dot().at((0.6, x.in2[1]))
    d += elm.Line().at(x.out).right(0.6).label("S = A ⊕ B", loc="right")
    d += elm.Line().at(a.out).right(0.6).label("C = A·B", loc="right")
    return _sd(d, 80)


def full_adder_2ha():
    fig, ax = _canvas(7.6, 2.4, (-1.4, 11.6), (-1.6, 2.4))
    _box(ax, 1.0, 0.3, 2.2, 1.6, "half\nadder 1", fc=TINT, ec=ACC, fs=9)
    _box(ax, 5.0, 0.9, 2.2, 1.6 - 0.3, "half\nadder 2", fc=TINT, ec=ACC, fs=9)
    for y, t in ((1.5, "A"), (0.7, "B")):
        _arrow(ax, (0, y), (1.0, y)); ax.text(-0.1, y, t, ha="right", va="center", fontsize=10, weight="bold")
    _arrow(ax, (3.2, 1.5), (5.0, 1.5)); ax.text(4.1, 1.66, "A ⊕ B", ha="center", fontsize=8.5, color=MUTED)
    _line(ax, [0, 4.4, 4.4], [-0.6, -0.6, 1.15]); _arrow(ax, (4.4, 1.15), (5.0, 1.15))
    ax.text(-0.1, -0.6, "C_in", ha="right", va="center", fontsize=10, weight="bold")
    _arrow(ax, (7.2, 1.9), (10.2, 1.9)); ax.text(10.3, 1.9, "S = A ⊕ B ⊕ Cin", va="center", fontsize=9.5, weight="bold", color=ACC)
    _box(ax, 8.4, -1.0, 1.1, 1.0, "OR", fs=9, r=0.3)
    _line(ax, [7.2, 7.8, 7.8], [1.2, 1.2, -0.3]); _arrow(ax, (7.8, -0.3), (8.4, -0.3))
    ax.text(7.9, 0.5, "(A ⊕ B)·Cin", fontsize=8.5, color=MUTED)
    _line(ax, [3.2, 3.7, 3.7], [0.7, 0.7, -0.75]); _arrow(ax, (3.7, -0.75), (8.4, -0.75))
    ax.text(5.6, -1.05, "A·B", fontsize=8.5, color=MUTED)
    _arrow(ax, (9.5, -0.5), (10.2, -0.5)); ax.text(10.3, -0.5, "C_out", va="center", fontsize=9.5, weight="bold", color=ACC)
    return _nat(fig)


def ripple_adder(sub=False):
    """4-bit ripple-carry adder; with sub=True the XOR row and mode line M make it an adder/subtractor."""
    fig, ax = _canvas(8.4, 3.3 if sub else 2.5, (-1.2, 12.6), (-1.4, 4.4 if sub else 2.9))
    for i in range(4):
        k = 3 - i
        x = i * 3.0
        _box(ax, x, 0, 2.0, 1.3, "full\nadder", fc=TINT, ec=ACC, fs=9)
        ax.text(x + 0.55, 2.55 if not sub else 4.1, f"A{k}", ha="center", fontsize=9.5, weight="bold")
        _arrow(ax, (x + 0.55, 2.4 if not sub else 3.95), (x + 0.55, 1.3))
        if sub:
            ax.add_patch(Circle((x + 1.45, 2.45), 0.3, fc="white", ec=G1, lw=1.4)); ax.text(x + 1.45, 2.45, "⊕", ha="center", va="center", fontsize=11, color=G1)
            ax.text(x + 1.3, 4.1, f"B{k}", ha="center", fontsize=9.5, weight="bold")
            _arrow(ax, (x + 1.3, 3.95), (x + 1.3, 2.72)); _arrow(ax, (x + 1.45, 2.15), (x + 1.45, 1.3))
            _line(ax, [x + 1.9, x + 1.9, x + 1.62], [3.3, 2.75, 2.68], color=G1)
        else:
            ax.text(x + 1.45, 2.55, f"B{k}", ha="center", fontsize=9.5, weight="bold")
            _arrow(ax, (x + 1.45, 2.4), (x + 1.45, 1.3))
        _arrow(ax, (x + 1.0, 0), (x + 1.0, -0.75)); ax.text(x + 1.0, -1.1, f"S{k}", ha="center", fontsize=9.5, weight="bold", color=ACC)
        if i:
            _arrow(ax, (x, 0.65), (x - 1.0, 0.65), color=G2); ax.text(x - 0.5, 0.82, f"C{k + 1}", ha="center", fontsize=8.5, color=G2)
    _arrow(ax, (0, 0.65), (-0.9, 0.65), color=G2); ax.text(-0.95, 0.65, "C_out", ha="right", va="center", fontsize=9, color=G2, weight="bold")
    _arrow(ax, (12.0, 0.65), (11.0, 0.65), color=G2)
    ax.text(12.05, 0.65, "C0 = M" if sub else "C0 = 0", va="center", fontsize=9, color=G2, weight="bold")
    if sub:
        _line(ax, [1.9, 12.0, 12.0], [3.3, 3.3, 0.65], color=G1)
        ax.text(12.1, 3.3, "M", va="center", fontsize=10, weight="bold", color=G1)
        ax.text(5.5, -1.35 + 0.02, "", fontsize=1)
    return _svg(fig)


def cla_delay():
    """Carry settling time: ripple grows with n, look-ahead does not."""
    fig, ax = plt.subplots(figsize=(4.6, 2.2))
    n = [1, 2, 4, 8, 16]
    ax.plot(n, [2 * k + 1 for k in n], "-o", color=G1, lw=1.6, ms=4, label="ripple carry: (2n + 1)T")
    ax.plot(n, [4] * 5, "-o", color=G2, lw=1.6, ms=4, label="carry look-ahead: constant")
    ax.set_xlabel("number of bits n", fontsize=8.5); ax.set_ylabel("delay (gate delays T)", fontsize=8.5)
    ax.set_xticks(n); ax.tick_params(labelsize=8); ax.legend(fontsize=8, frameon=False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    return _nat(fig)


def bcd_adder():
    fig, ax = _canvas(7.6, 3.5, (-2.4, 11.4), (-4.4, 2.6))
    _box(ax, 0, 0, 6.0, 1.2, "4-bit binary adder:  Z = A + B + Cin", fc=TINT, ec=ACC, fs=9)
    ax.text(1.5, 2.2, "A (BCD digit)", ha="center", fontsize=9, weight="bold"); _arrow(ax, (1.5, 2.0), (1.5, 1.2))
    ax.text(4.5, 2.2, "B (BCD digit)", ha="center", fontsize=9, weight="bold"); _arrow(ax, (4.5, 2.0), (4.5, 1.2))
    _arrow(ax, (3.0, 0), (3.0, -2.0)); ax.text(3.15, -0.6, "Z3 Z2 Z1 Z0", fontsize=8.5, color=MUTED)
    _line(ax, [0, -1.0, -1.0], [0.6, 0.6, -1.15]); ax.text(-1.1, 0.75, "K (carry)", ha="right", fontsize=8.5, color=MUTED)
    _box(ax, -2.2, -1.9, 3.6, 0.75, "Y = K + Z3Z2 + Z3Z1", fc="#fdeee3", ec=G1, fs=9, weight="bold")
    _line(ax, [3.0, 1.4], [-1.35, -1.35], color=MUTED, ls=":")
    _box(ax, 0, -3.2, 6.0, 1.2, "4-bit binary adder:  S = Z + 0YY0", fc=TINT, ec=ACC, fs=9)
    _line(ax, [1.4, 7.0, 7.0, 6.0], [-1.7, -1.7, -2.6, -2.6], color=G1); _arrow(ax, (6.4, -2.6), (6.0, -2.6), color=G1)
    ax.text(7.1, -2.6, "0110 if Y = 1\n0000 if Y = 0", va="center", fontsize=8.5, color=G1)
    _arrow(ax, (3.0, -3.2), (3.0, -4.0)); ax.text(3.2, -4.0, "BCD sum S3 S2 S1 S0", va="center", fontsize=9, weight="bold", color=ACC)
    ax.text(7.1, -1.55, "Y is also the carry\nto the next digit", fontsize=8.3, color=G1, va="bottom")
    return _nat(fig)


def serial_adder():
    fig, ax = _canvas(7.4, 2.5, (-0.6, 11.8), (-2.1, 2.5))
    _box(ax, 0, 1.2, 3.4, 0.9, "shift register A", fc=TINT, ec=ACC, fs=9)
    _box(ax, 0, -0.4, 3.4, 0.9, "shift register B", fc=TINT, ec=ACC, fs=9)
    _box(ax, 5.2, 0.0, 1.8, 1.7, "full\nadder", fs=9.5, weight="bold")
    _arrow(ax, (3.4, 1.65), (5.2, 1.4)); _arrow(ax, (3.4, 0.05), (5.2, 0.7))
    ax.text(3.5, 0.75, "LSB first", fontsize=8, color=MUTED)
    _box(ax, 8.2, -1.6, 1.6, 1.0, "D flip-flop\n(carry)", fc="#eaf6ef", ec=G2, fs=8.5)
    _line(ax, [7.0, 9.0, 9.0], [0.4, 0.4, -0.6], color=G2); ax.text(7.2, 0.52, "C_out", fontsize=8.5, color=G2)
    _line(ax, [8.2, 4.6, 4.6], [-1.1, -1.1, 0.25], color=G2); _arrow(ax, (4.6, 0.25), (5.2, 0.25), color=G2)
    ax.text(5.6, -1.4, "C_in for the next bit", fontsize=8.5, color=G2)
    _line(ax, [7.0, 10.6, 10.6, -0.4, -0.4], [1.3, 1.3, 2.35, 2.35, 1.65], color=G1); _arrow(ax, (-0.4, 1.65), (0, 1.65), color=G1)
    ax.text(8.0, 1.45, "sum bit S shifts back into A", fontsize=8.5, color=G1, va="bottom")
    return _nat(fig)


# ------------------------------------------------------------------ Part B
def mux_fig(sel, data, out="F", w=2.6, title=None):
    """A 2^k:1 MUX with labelled data inputs (top = I0) and select lines."""
    n = len(data)
    h = max(2.2, 0.52 * n + 0.6)
    fig, ax = _canvas(w, 0.42 * n + 1.3, (-2.6, 4.2), (-1.5, h + 0.7))
    ax.add_patch(Polygon([(0, 0), (0, h), (1.7, h - 0.55), (1.7, 0.55)], closed=True, fc=TINT, ec=ACC, lw=1.5))
    for i, lab in enumerate(data):
        y = h - (i + 0.5) * h / n
        _line(ax, [-0.7, 0], [y, y])
        ax.text(0.12, y, f"I{i}", va="center", fontsize=7.6, color=MUTED)
        col = {"0": MUTED, "1": G2}.get(lab, G1)
        ax.text(-0.8, y, lab, ha="right", va="center", fontsize=9.5, weight="bold", color=col)
    _arrow(ax, (1.7, h / 2), (2.6, h / 2)); ax.text(2.7, h / 2, out, va="center", fontsize=10.5, weight="bold", color=ACC)
    k = len(sel)
    for j, s in enumerate(sel):
        x = 0.35 + j * (1.1 / max(k - 1, 1)) if k > 1 else 0.85
        yb = 0.55 * x / 1.7
        _line(ax, [x, x], [-0.7, yb]); ax.text(x, -0.85, s, ha="center", va="top", fontsize=9.5, weight="bold")
    ax.text(0.85, h + 0.25, title or f"{n}:1 MUX", ha="center", fontsize=9, color=ACC, weight="bold")
    return _nat(fig)


def mux_tree():
    fig, ax = _canvas(5.0, 2.6, (-1.6, 9.0), (-1.6, 4.6))
    def m(x, y, h, lab):
        ax.add_patch(Polygon([(x, y), (x, y + h), (x + 1.2, y + h - 0.35), (x + 1.2, y + 0.35)], closed=True, fc=TINT, ec=ACC, lw=1.4))
        ax.text(x + 0.6, y + h / 2, lab, ha="center", va="center", fontsize=8, color=ACC)
    m(0, 2.4, 1.8, "2:1"); m(0, 0, 1.8, "2:1"); m(4.2, 1.1, 2.0, "2:1")
    for y, t in ((3.75, "I0"), (2.85, "I1"), (1.35, "I2"), (0.45, "I3")):
        _line(ax, [-0.7, 0], [y, y]); ax.text(-0.8, y, t, ha="right", va="center", fontsize=9, weight="bold")
    _line(ax, [1.2, 3.0, 3.0, 4.2], [3.3, 3.3, 2.6, 2.6]); _line(ax, [1.2, 3.0, 3.0, 4.2], [0.9, 0.9, 1.6, 1.6])
    _arrow(ax, (5.4, 2.1), (6.3, 2.1)); ax.text(6.4, 2.1, "F", va="center", fontsize=10.5, weight="bold", color=ACC)
    ax.plot([0.6, 0.6], [-0.9, 2.58], color=G1, lw=1.3, zorder=0)
    ax.text(0.6, -1.05, "S0", ha="center", va="top", fontsize=9.5, weight="bold", color=G1)
    _line(ax, [4.8, 4.8], [-0.9, 1.28], color=G2); ax.text(4.8, -1.05, "S1", ha="center", va="top", fontsize=9.5, weight="bold", color=G2)
    return _nat(fig)


def decoder_fig(ins=("A", "B", "C_in"), sums=(("S", (1, 2, 4, 7), ACC), ("C_out", (3, 5, 6, 7), G1)), gate="OR", w=6.0, enable=None):
    """n:2^n decoder with OR (or NOR/NAND) gates collecting chosen minterm outputs."""
    n = 2 ** len(ins)
    H = 0.55 * n + 0.4
    fig, ax = _canvas(w, 0.36 * n + 0.9, (-2.4, 11.2), (-0.9, H + 0.6))
    _box(ax, 0, 0, 2.4, H, "", fc=TINT, ec=ACC)
    ax.text(1.2, H + 0.25, f"{len(ins)}:{n} decoder", ha="center", fontsize=9, color=ACC, weight="bold")
    for i, t in enumerate(ins):
        y = H - 0.9 - i * 0.8
        _arrow(ax, (-1.0, y), (0, y)); ax.text(-1.1, y, t, ha="right", va="center", fontsize=10, weight="bold")
    if enable:
        _arrow(ax, (-1.0, 0.5), (0, 0.5)); ax.text(-1.1, 0.5, enable, ha="right", va="center", fontsize=9.5, weight="bold", color=G2)
    ys = {}
    for k in range(n):
        y = H - 0.45 - k * 0.55
        ys[k] = y
        ax.text(2.3, y, f"m{k}", ha="right", va="center", fontsize=8.5, color=MUTED)
        _line(ax, [2.4, 3.0], [y, y], color=MUTED, lw=1)
    for j, (name, mins, col) in enumerate(sums):
        gx = 6.4
        gy = H - (j + 0.5) * H / len(sums)
        _box(ax, gx, gy - 0.6, 1.5, 1.2, gate, fs=9, ec=col, r=0.3, color=col, weight="bold")
        xv = 3.4 + 0.75 * j
        for q, k in enumerate(mins):
            ty = gy + 0.42 - q * 0.84 / max(len(mins) - 1, 1)
            _line(ax, [3.0, xv + 0.25 * q, xv + 0.25 * q, gx], [ys[k], ys[k], ty, ty], color=col, lw=1.1)
            ax.plot(3.0, ys[k], "o", ms=3, color=col)
        _arrow(ax, (gx + 1.5, gy), (gx + 2.3, gy), color=col)
        ax.text(gx + 2.4, gy, name, va="center", fontsize=9.5, weight="bold", color=col)
    return _nat(fig)


def demux_fig():
    fig, ax = _canvas(3.4, 2.1, (-2.6, 5.6), (-1.5, 3.2))
    ax.add_patch(Polygon([(0, 0.55), (0, 2.05), (1.7, 2.6), (1.7, 0)], closed=True, fc=TINT, ec=ACC, lw=1.5))
    _arrow(ax, (-1.0, 1.3), (0, 1.3)); ax.text(-1.1, 1.3, "D", ha="right", va="center", fontsize=10, weight="bold")
    for i in range(4):
        y = 2.3 - i * 0.66
        _arrow(ax, (1.7, y), (2.6, y)); ax.text(2.7, y, f"Y{i} = D·m{i}", va="center", fontsize=8.8)
    for x, s in ((0.6, "S1"), (1.15, "S0")):
        _line(ax, [x, x], [-0.7, 0.55 - 0.55 * x / 1.7]); ax.text(x, -0.85, s, ha="center", va="top", fontsize=9.5, weight="bold")
    ax.text(0.85, 2.85, "1:4 DEMUX", ha="center", fontsize=9, color=ACC, weight="bold")
    return _nat(fig)


SEG = {0: "abcdef", 1: "bc", 2: "abged", 3: "abgcd", 4: "fgbc", 5: "afgcd", 6: "afgedc", 7: "abc", 8: "abcdefg", 9: "abcdfg"}


def seven_seg():
    fig, ax = _canvas(8.6, 1.9, (-2.6, 19.0), (-0.9, 3.3))
    def digit(x, on, lab=None, names=False):
        seg = {"a": ((0.15, 2.4), (0.85, 2.4)), "b": ((1.0, 2.3), (1.0, 1.3)), "c": ((1.0, 1.1), (1.0, 0.1)),
               "d": ((0.15, 0.0), (0.85, 0.0)), "e": ((0.0, 1.1), (0.0, 0.1)), "f": ((0.0, 2.3), (0.0, 1.3)), "g": ((0.15, 1.2), (0.85, 1.2))}
        for s, ((x1, y1), (x2, y2)) in seg.items():
            ax.plot([x + x1, x + x2], [y1, y2], color=BAD if s in on else "#e3e3de", lw=3.6 if not names else 4.5, solid_capstyle="round")
            if names:
                ox, oy = {"a": (0.5, 2.75), "b": (1.35, 1.8), "c": (1.35, 0.6), "d": (0.5, -0.4), "e": (-0.35, 0.6), "f": (-0.35, 1.8), "g": (0.5, 1.5)}[s]
                ax.text(x + ox, oy, s, ha="center", va="center", fontsize=9, weight="bold")
        if lab is not None:
            ax.text(x + 0.5, -0.65, lab, ha="center", fontsize=8.5, color=MUTED)
    digit(-1.6, "", names=True)
    for dgt in range(10):
        digit(1.4 + dgt * 1.75, SEG[dgt], str(dgt))
    return _svg(fig)


def mux_display():
    fig, ax = _canvas(7.2, 2.3, (-0.4, 12.4), (-1.6, 3.0))
    _box(ax, 0, 1.2, 2.4, 1.2, "BCD → 7-seg\ndecoder/driver", fc=TINT, ec=ACC, fs=8.5)
    _line(ax, [2.4, 11.2], [1.8, 1.8], lw=2.4); ax.text(6.8, 2.0, "segment lines a–g, shared by every digit", ha="center", fontsize=8.5, color=MUTED)
    for i in range(4):
        x = 4.0 + i * 2.0
        _box(ax, x, -0.2, 1.0, 1.4, "8", fs=13, color=BAD if i == 1 else "#d5d5d0", weight="bold", ec=G2 if i == 1 else LINE)
        _line(ax, [x + 0.5, x + 0.5], [1.2, 1.8], color=MUTED)
        _arrow(ax, (x + 0.5, -1.0), (x + 0.5, -0.2), color=G2 if i == 1 else MUTED)
        ax.text(x + 0.5, -1.3, f"EN{i}", ha="center", fontsize=8.5, color=G2 if i == 1 else MUTED, weight="bold")
    _box(ax, -0.2, -1.5, 2.8, 1.0, "scan counter\n+ decoder", fs=8.5)
    _arrow(ax, (2.4, -1.0), (3.6, -1.0)); _arrow(ax, (1.2, 0.4), (1.2, 1.2)); ax.text(1.35, 0.7, "BCD of the\nenabled digit", fontsize=7.8, color=MUTED, va="center")
    _line(ax, [1.2, 1.2], [-0.5, 0.4], color=MUTED, ls=":")
    return _nat(fig)


def comparator_flow():
    fig, ax = _canvas(8.0, 1.7, (-0.3, 13.6), (-1.2, 1.9))
    for i, k in enumerate((3, 2, 1, 0)):
        x = i * 3.3
        _box(ax, x, 0, 2.3, 1.3, f"A{k} vs B{k}", fc=TINT, ec=ACC, fs=9.5, weight="bold")
        ax.text(x + 1.15, 1.55, "MSB" if k == 3 else ("LSB" if k == 0 else ""), ha="center", fontsize=8, color=MUTED)
        ax.text(x + 1.15, -0.35, "different → decided here", ha="center", fontsize=7.6, color=G1, va="top")
        if i < 3:
            _arrow(ax, (x + 2.3, 0.65), (x + 3.3, 0.65), color=G2); ax.text(x + 2.8, 0.82, "equal", ha="center", fontsize=8, color=G2)
    _arrow(ax, (12.2, 0.65), (13.0, 0.65), color=G2); ax.text(13.05, 0.65, "A = B", va="center", fontsize=9, weight="bold", color=G2)
    return _svg(fig)


def parity_fig():
    d = _d(fs=11)
    x1 = d.add(lg.Xor().right().at((2.0, 0.9)).anchor("out")); _inputs(d, x1, ["A", "B"], 0.5)
    x2 = d.add(lg.Xor().right().at((2.0, -0.9)).anchor("out")); _inputs(d, x2, ["C", "D"], 0.5)
    x3 = d.add(lg.Xor().right().at((5.0, 0)).anchor("out"))
    _wire(d, x1.out, x3.in1, 2.6); _wire(d, x2.out, x3.in2, 2.6)
    d += elm.Line().at(x3.out).right(0.8).label("P = A ⊕ B ⊕ C ⊕ D", loc="right")
    return _sd(d, 105)


def shift_types():
    rows = [("start", "110110", None), ("logical left 2", "011000", (4, 5)), ("logical right 1", "011011", (0,)),
            ("circular left 2", "011011", (4, 5)), ("circular right 1", "011011", (0,)), ("arithmetic right 1", "111011", (0,))]
    fig, ax = _canvas(7.2, 2.3, (-4.2, 11.5), (-0.3, 6.5))
    notes = ["", "vacated bits ← 0", "vacated bit ← 0", "bits that fall off re-enter at the right", "the bit that falls off re-enters at the left", "vacated bit ← copy of the sign bit"]
    for r, ((name, bits, hl), note) in enumerate(zip(rows, notes)):
        y = 5.4 - r * 1.05
        ax.text(-0.25, y + 0.4, name, ha="right", va="center", fontsize=9, weight="bold" if r else "normal", color=INK if r else MUTED)
        for i, b in enumerate(bits):
            new = hl and i in hl
            ax.add_patch(Rectangle((i * 0.8, y), 0.8, 0.8, fc="#fdeee3" if new else "white", ec=G1 if new else LINE, lw=1.2))
            ax.text(i * 0.8 + 0.4, y + 0.4, b, ha="center", va="center", fontsize=10, family="Consolas", color=G1 if new else INK, weight="bold" if new else "normal")
        ax.text(5.1, y + 0.4, note, va="center", fontsize=8.3, color=MUTED)
    return _nat(fig)


def alu_fig():
    fig, ax = _canvas(7.0, 2.6, (-2.2, 12.0), (-1.7, 3.4))
    _box(ax, 0, 1.6, 2.6, 1.3, "arithmetic\nunit", fc=TINT, ec=ACC, fs=9)
    _box(ax, 0, -0.4, 2.6, 1.3, "logic\nunit", fc="#eaf6ef", ec=G2, fs=9)
    for y in (2.5, 2.0, 0.5, 0.0):
        _arrow(ax, (-1.0, y), (0, y))
    ax.text(-1.1, 2.25, "A_i, B_i,\nC_i", ha="right", va="center", fontsize=9, weight="bold")
    ax.text(-1.1, 0.25, "A_i, B_i", ha="right", va="center", fontsize=9, weight="bold")
    ax.add_patch(Polygon([(5.0, -0.2), (5.0, 2.7), (6.3, 2.2), (6.3, 0.3)], closed=True, fc="white", ec=INK, lw=1.4))
    ax.text(5.65, 1.25, "2:1\nMUX", ha="center", va="center", fontsize=8.5)
    _arrow(ax, (2.6, 2.25), (5.0, 2.25)); _arrow(ax, (2.6, 0.25), (5.0, 0.25))
    _arrow(ax, (6.3, 1.25), (7.4, 1.25)); ax.text(7.5, 1.25, "F_i", va="center", fontsize=10.5, weight="bold", color=ACC)
    _line(ax, [5.65, 5.65], [-1.1, 0.05], color=G1); ax.text(5.65, -1.25, "S2: 0 = arithmetic, 1 = logic", ha="center", va="top", fontsize=8.5, color=G1, weight="bold")
    _line(ax, [1.0, 1.0], [-1.1, -0.4], color=G1); _line(ax, [1.6, 1.6, 3.3, 3.3, 1.6, 1.6], [-1.1, -0.75, -0.75, 1.25, 1.25, 1.6], color=G1)
    ax.text(1.3, -1.25, "S1 S0: which operation", ha="center", va="top", fontsize=8.5, color=G1, weight="bold")
    _arrow(ax, (1.3, 2.9), (1.3, 3.3)); ax.text(1.45, 3.2, "C_i+1 to the next stage", fontsize=8.3, color=MUTED, va="center")
    ax.text(8.6, 2.4, "one-bit slice;\nn slices side by side\nmake an n-bit ALU", fontsize=8.5, color=MUTED, va="center")
    return _nat(fig)
