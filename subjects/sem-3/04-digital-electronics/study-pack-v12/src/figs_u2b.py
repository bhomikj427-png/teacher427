"""Unit 2 figures for files 04 (adders) and 08 (shifter / ALU): v1.3, S6."""
import figs1
import matplotlib.pyplot as plt  # noqa: F401
from figs1 import ACC, G1, G2, INK, MUTED, TINT, _arrow, _box, _line, _nat
from figs_u2 import _and, _bez, _cv, _dot, _mux, _not, _or

import schemdraw.elements as elm
import schemdraw.logic as lg

plt = figs1.plt


def _t(ax, x, y, s, fs=9.5, ha="center", va="center", color=INK, weight="normal"):
    ax.text(x, y, s, ha=ha, va=va, fontsize=fs, color=color, weight=weight)


def _pl(ax, pts, color=INK):
    _line(ax, [p[0] for p in pts], [p[1] for p in pts], color=color)


def _xor(ax, x, yc, w=1.2, h=1.0, ec=INK):
    """XOR: an OR shape set back 0.16 with an extra curve; pins sit on the extra curve."""
    d = 0.16
    _, _, o = _or(ax, x + d, yc, w, h, ec)
    back = _bez((x, yc - h / 2), (x + 0.3 * w, yc), (x, yc + h / 2))
    ax.plot([p[0] for p in back], [p[1] for p in back], color=ec, lw=1.4, zorder=3, solid_capstyle="round")
    xi = x + 0.1125 * w
    return (xi, yc + h / 4), (xi, yc - h / 4), o


def _sub(t):
    return f'<tspan dy="3" font-size="70%">{t}</tspan>'


# ------------------------------------------------------------------ 1. full-adder K-maps
def fa_kmaps():
    def one(ones, terms, title):
        return figs1.km("ABC", ones, terms=terms, title=title, cs=42)

    a = one([1, 2, 4, 7], (), "S")
    b = one([3, 5, 6, 7], ("AB", "BC", "AC"), "C_out")
    out = []
    for s in (a, b):
        s = s.replace(">C_out</text>", ">C" + _sub("out") + "</text>")
        s = s.replace('k-var" x="62" y="44">BC</text>', 'k-var" x="62" y="44">B C' + _sub("in") + "</text>")
        s = s.replace('k-chip-t" x="80.4" y="193.5">BC</text>', 'k-chip-t" x="80.4" y="193.5">BC' + _sub("in") + "</text>")
        s = s.replace('k-chip-t" x="140.8" y="193.5">AC</text>', 'k-chip-t" x="140.8" y="193.5">AC' + _sub("in") + "</text>")
        out.append(s)
    return ('<div style="display:flex;gap:6mm;justify-content:center;align-items:flex-start">'
            + "".join(f'<div style="flex:1 1 0;min-width:0">{s}</div>' for s in out) + "</div>")


# ------------------------------------------------------------------ 2. carry delay with the 4T line
def cla_delay2():
    fig, ax = plt.subplots(figsize=(4.1, 2.5))
    n = [2, 4, 8, 16]
    r = [5, 9, 17, 33]
    ax.plot(n, r, "-o", color=G1, lw=1.6, ms=4, label="ripple carry: (2n + 1)T")
    ax.plot(n, [4] * 4, "-o", color=G2, lw=1.6, ms=4, label="carry look-ahead: 4T")
    ax.set_xlabel("number of bits n", fontsize=8.5)
    ax.set_ylabel("delay until all outputs settle (T)", fontsize=8.5)
    ax.set_xticks(n)
    ax.set_ylim(0, 36)
    ax.tick_params(labelsize=8)
    for x, y in zip(n, r):
        ax.annotate(str(y), (x, y), xytext=(-5, 5), textcoords="offset points", ha="right", va="bottom", fontsize=8, color=G1)
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    return _nat(fig)


# ------------------------------------------------------------------ 3. half adder from 5 NAND gates
def ha_nand():
    d = figs1._d(fs=11)
    L = lg.Nand
    g1 = d.add(L().right().at((2, 0)).anchor("out"))
    g2 = d.add(L().right().at((5.2, 1.1)).anchor("out"))
    g3 = d.add(L().right().at((5.2, -1.1)).anchor("out"))
    g4 = d.add(L().right().at((8.2, 0)).anchor("out"))
    g5 = d.add(L().right().at((8.2, -2.9)).anchor("out"))
    d += elm.Line().endpoints(g1.in1, (-0.6, g1.in1[1])); d += elm.Line().endpoints((-0.6, g1.in1[1]), (-0.6, g2.in1[1]))
    d += elm.Line().endpoints((-1.3, g2.in1[1]), g2.in1).label("A", loc="left")
    d += elm.Line().endpoints(g1.in2, (-0.6, g1.in2[1])); d += elm.Line().endpoints((-0.6, g1.in2[1]), (-0.6, g3.in2[1]))
    d += elm.Line().endpoints((-1.3, g3.in2[1]), g3.in2).label("B", loc="left")
    d += lg.Dot().at((-0.6, g2.in1[1])); d += lg.Dot().at((-0.6, g3.in2[1]))
    d += elm.Line().endpoints(g1.out, (2.6, 0)); d += lg.Dot().at((2.6, 0))
    figs1._wire(d, (2.6, 0), g2.in2, 2.6); figs1._wire(d, (2.6, 0), g3.in1, 2.6)
    figs1._wire(d, g2.out, g4.in1, 5.8); figs1._wire(d, g3.out, g4.in2, 5.8)
    d += elm.Line().at(g4.out).right(0.6).label("S = A ⊕ B", loc="right")
    # gate 5: both inputs tied, fed from (AB)'
    tx = g5.in1[0] - 0.4
    ym = (g5.in1[1] + g5.in2[1]) / 2
    d += elm.Line().endpoints((2.6, 0), (2.6, ym))
    d += elm.Line().endpoints((2.6, ym), (tx, ym))
    d += elm.Line().endpoints((tx, g5.in1[1]), (tx, g5.in2[1]))
    d += elm.Line().endpoints((tx, g5.in1[1]), g5.in1); d += elm.Line().endpoints((tx, g5.in2[1]), g5.in2)
    d += lg.Dot().at((tx, ym))
    d += elm.Line().at(g5.out).right(0.6).label("C = AB", loc="right")
    d += elm.Label().at((3.5, 0.4)).label("(AB)'", fontsize=10, color=MUTED)
    for k, (x, y) in enumerate([(1.1, 0.75), (4.3, 1.95), (4.3, -1.95), (7.2, 0.8), (7.2, -2.2)], 1):
        d += elm.Label().at((x, y)).label(str(k), fontsize=10, color=MUTED)
    return figs1._sd(d, 120)


# ------------------------------------------------------------------ 4. half subtractor
def half_sub():
    fig, ax = _cv((-1.0, 8.9), (-2.7, 3.0), 0.4)
    (xa, xb), _, xo = _xor(ax, 3.0, 1.3)[0], None, _xor(ax, 3.0, 1.3)[2]
    return None


FIGS = {}
