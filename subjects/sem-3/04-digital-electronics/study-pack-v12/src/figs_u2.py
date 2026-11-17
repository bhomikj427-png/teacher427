"""Unit 2 MUX / decoder / encoder figures for files 05-06 (v1.3, S5 2026-11-17)."""
import math

import figs1
import numpy as np
from figs1 import ACC, G1, G2, INK, MUTED, TINT, _arrow, _canvas, _box, _line, _nat
from matplotlib.patches import Circle, Polygon

plt = figs1.plt


def _cv(xlim, ylim, s):
    return _canvas(s * (xlim[1] - xlim[0]), s * (ylim[1] - ylim[0]), xlim, ylim)


def _dcol(lab):
    return {"0": MUTED, "1": G2}.get(lab, G1)


# ------------------------------------------------------------------ gate shapes
def _and(ax, x, yc, w=1.2, h=1.0, ec=INK):
    t = np.linspace(-math.pi / 2, math.pi / 2, 30)
    pts = [(x, yc - h / 2)] + [(x + w / 2 + (w / 2) * math.cos(a), yc + (h / 2) * math.sin(a)) for a in t] + [(x, yc + h / 2)]
    ax.add_patch(Polygon(pts, closed=True, fc=TINT, ec=ec, lw=1.4, zorder=3))
    return (x, yc + h / 4), (x, yc - h / 4), (x + w, yc)


def _bez(p0, p1, p2, n=24):
    out = []
    for i in range(n + 1):
        t = i / n
        out.append(((1 - t) ** 2 * p0[0] + 2 * t * (1 - t) * p1[0] + t * t * p2[0],
                    (1 - t) ** 2 * p0[1] + 2 * t * (1 - t) * p1[1] + t * t * p2[1]))
    return out


def _or(ax, x, yc, w=1.2, h=1.0, ec=INK):
    top = _bez((x, yc + h / 2), (x + 0.6 * w, yc + h / 2), (x + w, yc))
    bot = _bez((x + w, yc), (x + 0.6 * w, yc - h / 2), (x, yc - h / 2))
    back = _bez((x, yc - h / 2), (x + 0.3 * w, yc), (x, yc + h / 2))
    ax.add_patch(Polygon(top + bot + back, closed=True, fc=TINT, ec=ec, lw=1.4, zorder=3))
    xi = x + 0.11 * w
    return (xi, yc + h / 4), (xi, yc - h / 4), (x + w, yc)


def _not(ax, x, yc, w=0.6, h=0.5):
    ax.add_patch(Polygon([(x, yc - h / 2), (x, yc + h / 2), (x + w, yc)], closed=True, fc=TINT, ec=INK, lw=1.4, zorder=3))
    ax.add_patch(Circle((x + w + 0.08, yc), 0.08, fc="white", ec=INK, lw=1.3, zorder=3))
    return (x, yc), (x + w + 0.16, yc)


def _dot(ax, x, y, col=INK):
    ax.plot(x, y, "o", ms=3.6, color=col, zorder=5)


# ------------------------------------------------------------------ trapezoid MUX
def _mux(ax, x, y, h, w=1.5, n=4, data=None, label="4:1", sel=(), dlen=0.6, outside=True, names=True, slant=0.4):
    """Trapezoid MUX, lower-left corner (x, y). Returns (output point, list of pin points)."""
    ax.add_patch(Polygon([(x, y), (x, y + h), (x + w, y + h - slant), (x + w, y + slant)], closed=True, fc=TINT, ec=ACC, lw=1.5, zorder=2))
    pins = []
    for i in range(n):
        py = y + h - (i + 0.5) * h / n
        pins.append((x, py))
        _line(ax, [x - dlen, x], [py, py])
        if names:
            ax.text(x + 0.1, py, f"I{i}", va="center", fontsize=7.4, color=MUTED, zorder=4)
        if outside and data is not None:
            ax.text(x - dlen - 0.1, py, data[i], ha="right", va="center", fontsize=9.5, weight="bold", color=_dcol(data[i]))
    ax.text(x + w * 0.66, y + h / 2, label, ha="center", va="center", fontsize=8, color=ACC, weight="bold", zorder=4)
    k = len(sel)
    for j, s in enumerate(sel):
        sx = x + w * (0.5 if k == 1 else 0.26 + 0.5 * j / (k - 1))
        yb = y + slant * (sx - x) / w
        _line(ax, [sx, sx], [yb - 0.6, yb])
        ax.text(sx, yb - 0.7, s, ha="center", va="top", fontsize=9.5, weight="bold", color=MUTED if s == "0" else INK)
    return (x + w, y + h / 2), pins


# ------------------------------------------------------------------ 10. 2:1 MUX and its gates
def mux21():
    fig, ax = _cv((-1.6, 11.8), (-1.4, 3.2), 0.4)
    ax.add_patch(Polygon([(0, 0), (0, 2.2), (1.5, 1.8), (1.5, 0.4)], closed=True, fc=TINT, ec=ACC, lw=1.5))
    for lab, yy in (("I0", 1.65), ("I1", 0.55)):
        _line(ax, [-0.6, 0], [yy, yy])
        ax.text(-0.7, yy, lab, ha="right", va="center", fontsize=9.5, weight="bold", color=G1)
    ax.text(0.95, 1.1, "2:1", ha="center", va="center", fontsize=8, color=ACC, weight="bold")
    _line(ax, [0.75, 0.75], [-0.6, 0.2])
    ax.text(0.75, -0.7, "S", ha="center", va="top", fontsize=9.5, weight="bold")
    _arrow(ax, (1.5, 1.1), (2.4, 1.1))
    ax.text(2.5, 1.1, "Z", va="center", fontsize=10.5, weight="bold", color=ACC)
    ax.text(3.9, 1.1, "=", ha="center", va="center", fontsize=16, color=MUTED)
    # circuit
    xl = 5.2
    a2hi, a2lo, a2o = _and(ax, 7.0, 1.9)      # S . I1
    a1hi, a1lo, a1o = _and(ax, 7.0, 0.3)      # S' . I0
    o_hi, o_lo, o_o = _or(ax, 9.3, 1.1)
    ys = {"I1": 2.15, "S": 1.65, "I0": 0.05}
    for lab, yy in ys.items():
        ax.text(xl - 0.1, yy, lab, ha="right", va="center", fontsize=9.5, weight="bold", color=G1 if lab != "S" else INK)
    _line(ax, [xl, 7.0], [2.15, 2.15])
    _line(ax, [xl, 7.0], [1.65, 1.65])
    _line(ax, [xl, 7.0], [0.05, 0.05])
    _dot(ax, 5.8, 1.65)
    _line(ax, [5.8, 5.8, 6.0], [1.65, 0.55, 0.55])
    (_, _), (ox, oy) = _not(ax, 6.0, 0.55)
    _line(ax, [ox, 7.0], [oy, 0.55])
    ax.text(6.35, 0.95, "S'", ha="center", va="bottom", fontsize=8.6, color=MUTED)
    _line(ax, [a2o[0], 8.7, 8.7, o_hi[0]], [a2o[1], a2o[1], o_hi[1], o_hi[1]])
    _line(ax, [a1o[0], 8.7, 8.7, o_lo[0]], [a1o[1], a1o[1], o_lo[1], o_lo[1]])
    _arrow(ax, o_o, (11.0, 1.1))
    ax.text(11.1, 1.1, "Z", va="center", fontsize=10.5, weight="bold", color=ACC)
    ax.text(8.0, -0.6, "Z = S'I0 + SI1", ha="center", va="top", fontsize=9.5, color=ACC)
    return _nat(fig)


# ------------------------------------------------------------------ 11. Problem-set Q5 MUX tree
def ps1q5():
    fig, ax = _cv((-2.0, 8.6), (-1.0, 7.4), 0.4)
    m1_out, p1 = _mux(ax, 0, 4.4, 2.4, data=["D'", "D'", "0", "D"], sel=("B", "C"))
    m2_out, p2 = _mux(ax, 0, 0.0, 2.4, data=["1", "D", "D", "1"], sel=("B", "C"))
    m3_out, p3 = _mux(ax, 5.2, 2.2, 2.4, data=None, sel=("0", "A"), outside=False)
    ax.text(0.75, 7.15, "MUX1", ha="center", fontsize=8, color=MUTED)
    ax.text(0.75, 2.75, "MUX2", ha="center", fontsize=8, color=MUTED)
    ax.text(5.95, 5.0, "MUX3", ha="center", fontsize=8, color=MUTED)
    _line(ax, [m1_out[0], 3.4, 3.4, p3[0][0] - 0.6], [m1_out[1], m1_out[1], p3[0][1], p3[0][1]])
    _line(ax, [m2_out[0], 3.9, 3.9, p3[1][0] - 0.6], [m2_out[1], m2_out[1], p3[1][1], p3[1][1]])
    for i in (2, 3):
        ax.text(p3[i][0] - 0.7, p3[i][1], "0", ha="right", va="center", fontsize=9.5, weight="bold", color=MUTED)
    _arrow(ax, m3_out, (m3_out[0] + 0.9, m3_out[1]))
    ax.text(m3_out[0] + 1.0, m3_out[1], "F", va="center", fontsize=10.5, weight="bold", color=ACC)
    return _nat(fig)


# ------------------------------------------------------------------ 12. cascading with enables
def cascade_en():
    fig, ax = _cv((-2.0, 8.2), (-2.4, 9.0), 0.36)
    tout, _ = _mux(ax, 0, 5.0, 2.4, data=["I0", "I1", "I2", "I3"], sel=("S1", "S0"), names=False)
    bout, _ = _mux(ax, 0, 0.0, 2.4, data=["I4", "I5", "I6", "I7"], sel=("S1", "S0"), names=False)
    for x0, y0, lab in ((0.9, 5.0, "G' = S2"), (0.9, 0.0, "G' = S2'")):
        yt = y0 + 2.4 - 0.4 * 0.9 / 1.5
        _line(ax, [x0, x0], [yt, yt + 0.55], color=G2)
        ax.text(x0, yt + 0.65, lab, ha="center", va="bottom", fontsize=9.5, weight="bold", color=G2)
    gh, gl, go = _or(ax, 4.6, 3.7, w=1.3, h=1.1)
    _line(ax, [tout[0], 3.6, 3.6, gh[0]], [tout[1], tout[1], gh[1], gh[1]])
    _line(ax, [bout[0], 3.6, 3.6, gl[0]], [bout[1], bout[1], gl[1], gl[1]])
    _arrow(ax, go, (go[0] + 0.9, go[1]))
    ax.text(go[0] + 1.0, go[1], "F", va="center", fontsize=10.5, weight="bold", color=ACC)
    ax.text(5.3, 2.5, "OR", ha="center", va="center", fontsize=8, color=MUTED)
    ax.text(4.0, -1.9, "disabled MUX outputs 0", ha="center", va="top", fontsize=9, color=MUTED)
    return _nat(fig)


# ------------------------------------------------------------------ 13. 4:16 decoder from two 3:8
def dec416():
    fig, ax = _cv((-4.2, 6.0), (-1.4, 10.2), 0.4)
    for y0, ttl in ((4.6, "top"), (0.0, "bot")):
        _box(ax, 0, y0, 2.4, 4.0, "", fc=TINT, ec=ACC)
        ax.text(1.2, y0 + 2.0, "3:8\ndecoder", ha="center", va="center", fontsize=9, color=ACC, weight="bold")
    ytop = {"x": 7.9, "y": 7.4, "z": 6.9}
    ybot = {"x": 3.5, "y": 3.0, "z": 2.5}
    xv = {"x": -1.2, "y": -1.8, "z": -2.4}
    for n in "xyz":
        ax.text(-3.6, ytop[n], n, ha="right", va="center", fontsize=10, weight="bold")
        _line(ax, [-3.5, 0], [ytop[n]] * 2)
        _arrow(ax, (xv[n], ytop[n]), (0, ytop[n]))
        _line(ax, [xv[n], xv[n]], [ytop[n], ybot[n]])
        _arrow(ax, (xv[n], ybot[n]), (0, ybot[n]))
        _dot(ax, xv[n], ytop[n])
    # enables
    _arrow(ax, (1.2, 9.4), (1.2, 8.6), color=G2)
    ax.text(1.2, 9.5, "w'", ha="center", va="bottom", fontsize=10, weight="bold", color=G2)
    ax.text(1.2, 8.4, "EN", ha="center", va="top", fontsize=7.4, color=MUTED)
    _arrow(ax, (1.2, -0.8), (1.2, 0.0), color=G2)
    ax.text(1.2, -0.9, "w", ha="center", va="top", fontsize=10, weight="bold", color=G2)
    ax.text(1.2, 0.2, "EN", ha="center", va="bottom", fontsize=7.4, color=MUTED)
    for y0, lab in ((4.6, "D0 … D7"), (0.0, "D8 … D15")):
        ys = [y0 + 3.7 - k * 0.5 for k in range(8)]
        for yy in ys:
            _line(ax, [2.4, 3.0], [yy, yy], color=MUTED, lw=1)
        _line(ax, [3.0, 3.0], [ys[-1], ys[0]], color=ACC)
        _arrow(ax, (3.0, (ys[0] + ys[-1]) / 2), (3.6, (ys[0] + ys[-1]) / 2), color=ACC)
        ax.text(3.7, (ys[0] + ys[-1]) / 2, lab, va="center", fontsize=9.5, weight="bold", color=ACC)
    return _nat(fig)


# ------------------------------------------------------------------ 14. 4:2 encoder as gates
def enc42():
    fig, ax = _cv((-1.4, 9.2), (-1.0, 4.6), 0.42)
    ys = {"w3": 3.9, "w2": 2.7, "w1": 1.5}
    for n, yy in ys.items():
        ax.text(-0.1, yy, n, ha="right", va="center", fontsize=10, weight="bold")
    g1h, g1l, g1o = _or(ax, 5.0, 3.0, w=1.3, h=1.0)     # y1 = w3 + w2
    g0h, g0l, g0o = _or(ax, 5.0, 0.7, w=1.3, h=1.0)     # y0 = w3 + w1
    _line(ax, [0, 3.6, 3.6, g1h[0]], [3.9, 3.9, g1h[1], g1h[1]])
    _line(ax, [0, 3.3, 3.3, g1l[0]], [2.7, 2.7, g1l[1], g1l[1]])
    # w1 -> y0 upper pin
    _line(ax, [0, 4.0, 4.0, g0h[0]], [1.5, 1.5, g0h[1], g0h[1]])
    # w3 branch down to y0 lower pin
    _line(ax, [2.6, 2.6, g0l[0]], [3.9, g0l[1], g0l[1]])
    _dot(ax, 2.6, 3.9)
    _line(ax, [0, 1.3], [0.0, 0.0], color=MUTED)
    ax.text(1.5, 0.0, "w0 not used", va="center", fontsize=8.6, color=MUTED)
    _arrow(ax, g1o, (g1o[0] + 0.9, g1o[1]))
    ax.text(g1o[0] + 1.0, g1o[1], "y1", va="center", fontsize=10.5, weight="bold", color=ACC)
    _arrow(ax, g0o, (g0o[0] + 0.9, g0o[1]))
    ax.text(g0o[0] + 1.0, g0o[1], "y0", va="center", fontsize=10.5, weight="bold", color=ACC)
    return _nat(fig)


# ------------------------------------------------------------------ 15. priority-encoder K-maps
def _kmp(ones, groups, dcs, title):
    cells = {m: "1" for m in ones}
    cells.update({m: "X" for m in dcs})
    s = figs1.kfig.kmap(cells, [{"cells": c, "term": t, "color": i} for i, (c, t) in enumerate(groups)],
                        rv="AB", cv="CD", cs=42, show_idx=True, title=title)
    return s.replace(">AB</text>", ">D₃D₂</text>").replace(">CD</text>", ">D₁D₀</text>")


def prio_km():
    a = _kmp(list(range(4, 16)), [([4, 5, 6, 7, 12, 13, 14, 15], "D2"), (list(range(8, 16)), "D3")], [0], "x")
    b = _kmp([2, 3] + list(range(8, 16)), [(list(range(8, 16)), "D3"), ([2, 3, 10, 11], "D1D2'")], [0], "y")
    return f'<div style="display:flex;gap:8mm;justify-content:center;flex-wrap:wrap">{a}{b}</div>'


FIGS = {
    "u2_mux41": lambda: figs1.mux_fig(["S1", "S0"], ["I0", "I1", "I2", "I3"], out="Y"),
    "u2_ex415": lambda: figs1.mux_fig(["A", "B", "C"], ["0", "0", "1", "1", "0", "1", "1", "1"], out="F"),
    "u2_ex416": lambda: figs1.mux_fig(["x", "y"], ["z", "z'", "0", "1"], out="F"),
    "u2_mte5": lambda: figs1.mux_fig(["P", "Q", "R"], ["1", "S", "S'", "0", "1", "1", "S", "S"], out="F"),
    "u2_ex419": lambda: figs1.mux_fig(["A", "B"], ["D", "C'D'", "CD", "1"], out="F"),
    "u2_ls151": lambda: figs1.mux_fig(["A2", "A1", "A0"], ["0", "1", "0", "1", "0", "1", "1", "0"], out="Y", title="74LS151, G' = 0"),
    "u2_fa_dec": lambda: figs1.decoder_fig(ins=("x", "y", "z"), sums=(("S", (1, 2, 4, 7), ACC), ("C", (3, 5, 6, 7), G1))),
    "u2_ps1q7": lambda: figs1.decoder_fig(ins=("A", "B", "C"), sums=(("Y", (0, 3, 5, 6, 7), ACC),), gate="NOR"),
    "u2_sl18": lambda: figs1.decoder_fig(ins=("A", "B"), sums=(("F", (0, 2), ACC),), w=4.6),
    "u2_mux21": mux21,
    "u2_ps1q5": ps1q5,
    "u2_cascade_en": cascade_en,
    "u2_dec416": dec416,
    "u2_enc42": enc42,
    "u2_prio_km": prio_km,
}
