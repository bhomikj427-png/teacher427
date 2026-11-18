"""Unit 2 figures for files 04 (adders) and 08 (shifter / ALU): v1.3, S6."""
import re

import figs1
import matplotlib.pyplot as plt  # noqa: F401
from figs1 import ACC, G1, G2, INK, MUTED, TINT, _arrow, _box, _line, _nat
from figs_u2 import _and, _bez, _cv, _dot, _mux, _not, _or

import schemdraw.elements as elm
import schemdraw.logic as lg

plt = figs1.plt


def _rich(ax, x, y, s, fs, ha, va, color, weight):
    """Text with real subscripts (_x) AND the glyph U+2295, which mathtext cannot show: laid out piece by piece."""
    fig = ax.figure
    rend = fig.canvas.get_renderer()
    p0, p1 = ax.transData.transform((0, 0)), ax.transData.transform((1, 1))
    ppx, ppy = p1[0] - p0[0], p1[1] - p0[1]
    objs = []
    for k, part in enumerate(re.split(r"_([A-Za-z0-9]+)", s)):
        if not part:
            continue
        sub = k % 2 == 1
        t = ax.text(0, 0, part.replace(" ", chr(160)), fontsize=fs * (0.72 if sub else 1), ha="left", va=va,
                    color=color, weight=weight)
        objs.append((t, t.get_window_extent(rend).width / ppx, sub))
    tot = sum(w for _, w, _ in objs)
    cx = x - tot / 2 if ha == "center" else (x - tot if ha == "right" else x)
    for t, w, sub in objs:
        t.set_position((cx, y - (0.22 * fs * fig.dpi / 72 / ppy if sub else 0)))
        cx += w


def _t(ax, x, y, s, fs=9.5, ha="center", va="center", color=INK, weight="normal"):
    if "⊕" in s and re.search(r"[A-Za-z]{1,2}_[A-Za-z0-9]", s):   # mathtext (subscripts) has no U+2295 glyph
        return _rich(ax, x, y, s, fs, ha, va, color, weight)
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


from matplotlib.patches import Circle  # noqa: E402


def _xnor(ax, x, yc, w=1.2, h=1.0):
    a, b, o = _xor(ax, x, yc, w, h)
    ax.add_patch(Circle((o[0] + 0.08, yc), 0.08, fc="white", ec=INK, lw=1.3, zorder=4))
    return a, b, (o[0] + 0.16, yc)


def _cl(ax, x, y, s, **k):
    """bold input / output label"""
    k.setdefault("fs", 10.5)
    k.setdefault("weight", "bold")
    _t(ax, x, y, s, **k)


# ------------------------------------------------------------------ 4. half subtractor
def half_sub():
    fig, ax = _cv((-1.0, 8.4), (-1.1, 3.4), 0.4)
    xa, xb, xo = _xor(ax, 3.0, 2.2)
    _, _, ao = _and(ax, 3.4, 0.2)
    _cl(ax, -0.1, 2.45, "A", ha="right")
    _cl(ax, -0.1, 1.95, "B", ha="right")
    _pl(ax, [(0, 2.45), xa])
    _pl(ax, [(0, 1.95), xb])
    _dot(ax, 0.9, 2.45)
    _pl(ax, [(0.9, 2.45), (0.9, 0.45), (1.5, 0.45)])
    _, nout = _not(ax, 1.5, 0.45)
    _pl(ax, [nout, (3.4, 0.45)])
    _t(ax, 2.83, 0.62, "A'", fs=8.5, color=MUTED, va="bottom")
    _dot(ax, 0.4, 1.95)
    _pl(ax, [(0.4, 1.95), (0.4, -0.05), (3.4, -0.05)])
    _arrow(ax, xo, (5.2, 2.2))
    _cl(ax, 5.3, 2.2, "D = A ⊕ B", ha="left", color=ACC, fs=10)
    _arrow(ax, ao, (5.2, 0.2))
    _cl(ax, 5.3, 0.2, "b_out = A'B", ha="left", color=ACC, fs=10)
    return _nat(fig)


# ------------------------------------------------------------------ 5. full subtractor from two half subtractors
def full_sub_2hs():
    fig, ax = _cv((-1.2, 16.6), (-2.0, 3.6), 0.29)
    _box(ax, 1.2, 0.9, 3.2, 2.0, "half\nsubtractor 1", fc=TINT, ec=ACC, fs=9)
    _box(ax, 7.4, 0.9, 3.2, 2.0, "half\nsubtractor 2", fc=TINT, ec=ACC, fs=9)
    for y, n in ((2.4, "A"), (1.4, "B")):
        _arrow(ax, (0.2, y), (1.2, y))
        _cl(ax, 0.1, y, n, ha="right", fs=10)
    _arrow(ax, (4.4, 2.4), (7.4, 2.4))
    _t(ax, 5.9, 2.55, "A ⊕ B", fs=8.5, color=MUTED, va="bottom")
    _arrow(ax, (6.1, 1.4), (7.4, 1.4))
    _cl(ax, 6.0, 1.4, "b_in", ha="right", fs=10)
    ox, oy = 12.2, 0.2
    oh, ol, oo = _or(ax, ox, oy)
    _pl(ax, [(2.8, 0.9), (2.8, -1.2), (11.4, -1.2), (11.4, ol[1])])
    _arrow(ax, (11.4, ol[1]), ol)
    _t(ax, 4.0, -1.05, "A'B", fs=8.5, color=MUTED, va="bottom", ha="left")
    _pl(ax, [(10.6, 1.4), (11.0, 1.4), (11.0, oh[1])])
    _arrow(ax, (11.0, oh[1]), oh)
    _t(ax, 10.85, 1.58, "(A ⊕ B)'b_in", fs=8.5, color=MUTED, va="bottom", ha="left")
    _arrow(ax, (10.6, 2.4), (13.6, 2.4))
    _cl(ax, 13.7, 2.4, "D", ha="left", color=ACC)
    _arrow(ax, oo, (14.3, oy))
    _cl(ax, 14.4, oy, "b_out", ha="left", color=ACC, fs=10)
    return _nat(fig)


# ------------------------------------------------------------------ 6. full adder / subtractor cell
def _stage(ax, x0, Q, ptop, ptag):
    xa, xb, xn = x0 + 2.4, x0 + 2.4, x0 + 5.2
    pa, qa, oa = _xor(ax, xa, 8.4)          # XOR(P, Q) -> sum
    pb, qb, ob = _xor(ax, xb, 3.6)          # XOR(P, E)
    ah, al, ao = _and(ax, xn, 5.8)          # AND(., Q)
    xp, xq = x0, x0 + 0.9
    _pl(ax, [(xp, ptop), (xp, 3.85)])
    _pl(ax, [(xq, 9.4), (xq, 6.05)])
    _pl(ax, [(xp, 8.65), pa])
    if ptag:
        _dot(ax, xp, 8.65)
    _pl(ax, [(xq, 8.15), qa]); _dot(ax, xq, 8.15)
    _pl(ax, [(xp, 3.85), pb]); _dot(ax, xp, 3.85)
    _pl(ax, [(xq, 6.05), ah]); _dot(ax, xq, 6.05)
    xe = x0 + 1.8
    _pl(ax, [(xe, 2.0), (xe, qb[1]), qb]); _dot(ax, xe, 2.0)
    _pl(ax, [ob, (x0 + 4.6, ob[1]), (x0 + 4.6, al[1])])
    _arrow(ax, (x0 + 4.6, al[1]), al)
    if ptag:
        _cl(ax, xp, 9.75, ptag, fs=10)
    _cl(ax, xq, 9.75, Q, fs=10)
    return oa, ao


def addsub_cell():
    fig, ax = _cv((-1.2, 24.6), (0.3, 10.9), 0.25)
    x1, x2 = 0.6, 10.6
    s1, a1 = _stage(ax, x1, "B_i", 9.4, "A_i")
    # stage 2: P = A_i xor B_i arrives on the wire at y = 8.4
    s2, a2 = _stage(ax, x2, "C_i", 8.65, None)
    _pl(ax, [s1, (x2, s1[1])]); _dot(ax, x2, s1[1])
    _t(ax, 8.0, 8.8, "A_i ⊕ B_i", fs=8.5, color=MUTED, va="bottom")
    _t(ax, x1 + 3.8, 3.0, "A_i ⊕ E", fs=8, color=MUTED, ha="left", va="top")
    _t(ax, x2 + 3.8, 3.0, "(A_i ⊕ B_i) ⊕ E", fs=8, color=MUTED, ha="left", va="top")
    _t(ax, a1[0] + 0.15, 6.3, "(A_i ⊕ E)B_i", fs=8, color=MUTED, ha="left", va="bottom")
    _t(ax, a2[0] + 0.15, 6.3, "((A_i ⊕ B_i) ⊕ E)C_i", fs=8, color=MUTED, ha="left", va="bottom")
    # E lane
    _pl(ax, [(-0.4, 2.0), (x2 + 1.8, 2.0)])
    _cl(ax, -0.5, 2.0, "E", ha="right")
    # sum / difference output
    _arrow(ax, s2, (s2[0] + 1.9, s2[1]))
    _cl(ax, s2[0] + 2.0, s2[1], "S_i / D_i", ha="left", color=ACC, fs=10)
    # OR
    oh, ol, oo = _or(ax, 19.4, 3.4)
    _pl(ax, [a1, (8.2, a1[1]), (8.2, 0.9), (18.2, 0.9), (18.2, ol[1])])
    _arrow(ax, (18.2, ol[1]), ol)
    _pl(ax, [a2, (18.6, a2[1]), (18.6, oh[1])])
    _arrow(ax, (18.6, oh[1]), oh)
    _arrow(ax, oo, (oo[0] + 0.8, oo[1]))
    _cl(ax, oo[0] + 0.9, oo[1] + 0.12, r"$\mathrm{C}_{\mathrm{i+1}}$", ha="left", color=ACC, fs=10, va="bottom")
    _t(ax, oo[0] + 0.9, oo[1] - 0.05, "carry / borrow", fs=8, color=MUTED, ha="left", va="top")
    _t(ax, x1 + 3.5, 10.45, "stage 1", fs=8.5, color=MUTED)
    _t(ax, x2 + 3.5, 10.45, "stage 2", fs=8.5, color=MUTED)
    return _nat(fig)


# ------------------------------------------------------------------ 7. barrel shifter
def barrel4():
    fig, ax = _cv((-0.9, 9.2), (-1.7, 13.3), 0.36)
    names = ["D3", "D2", "D1", "D0"]
    rx = [0.4, 1.2, 2.0, 2.8]
    for n, x in zip(names, rx):
        _cl(ax, x, 12.85, n, color=G1, fs=9.5)
        _line(ax, [x, x], [12.4, 0.25], color=G1)
    cols = {"Y3": [0, 1, 2, 3], "Y2": [1, 2, 3, 0], "Y1": [2, 3, 0, 1], "Y0": [3, 0, 1, 2]}
    for y0, (yn, idx) in zip((9.9, 6.6, 3.3, 0.0), cols.items()):
        out, pins = _mux(ax, 5.2, y0, 2.0, data=None, label="4:1", sel=("S1", "S0"), dlen=0, outside=False)
        for (px, py), d in zip(pins, idx):
            _line(ax, [rx[d], px], [py, py], color=G1)
            _dot(ax, rx[d], py, G1)
            ax.text(px - 0.12, py, names[d], ha="right", va="center", fontsize=7.6, color=G1,
                    bbox=dict(fc="white", ec="none", pad=0.6))
        _arrow(ax, out, (out[0] + 0.9, out[1]))
        _cl(ax, out[0] + 1.0, out[1], yn, ha="left", color=ACC)
    return _nat(fig)


# ------------------------------------------------------------------ 8. 1-bit logic unit
def lu41():
    fig, ax = _cv((-0.8, 10.4), (-1.7, 7.9), 0.37)
    mo, pins = _mux(ax, 7.0, 0.0, 6.4, data=None, label="4:1", sel=("S1", "S0"), dlen=0, outside=False)
    ya = [5.6, 4.0, 2.4, 0.8]
    xa_, xb_ = 0.6, 1.4
    _cl(ax, xa_, 7.2, "A", fs=10.5)
    _cl(ax, xb_, -0.8, "B", fs=10.5, va="top")
    _line(ax, [xa_, xa_], [6.9, 1.05])
    _line(ax, [xb_, xb_], [-0.5, 3.75])
    # NOT
    _pl(ax, [(xa_, 5.6), (3.2, 5.6)]); _dot(ax, xa_, 5.6)
    _, no = _not(ax, 3.2, 5.6)
    _pl(ax, [no, pins[0]])
    # AND, OR, XOR
    h, l, o = _and(ax, 3.2, ya[1])
    _pl(ax, [(xa_, h[1]), h]); _dot(ax, xa_, h[1]); _pl(ax, [(xb_, l[1]), l]); _dot(ax, xb_, l[1]); _pl(ax, [o, pins[1]])
    h, l, o = _or(ax, 3.2, ya[2], 1.2, 1.0)
    _pl(ax, [(xa_, h[1]), h]); _dot(ax, xa_, h[1]); _pl(ax, [(xb_, l[1]), l]); _dot(ax, xb_, l[1]); _pl(ax, [o, pins[2]])
    h, l, o = _xor(ax, 3.04, ya[3])
    _pl(ax, [(xa_, h[1]), h]); _dot(ax, xa_, h[1]); _pl(ax, [(xb_, l[1]), l]); _dot(ax, xb_, l[1]); _pl(ax, [o, pins[3]])
    for y, s in zip(ya, ("A'", "AB", "A + B", "A ⊕ B")):
        _t(ax, 5.6, y + 0.12, s, fs=8.5, color=MUTED, va="bottom")
    _arrow(ax, mo, (mo[0] + 1.0, mo[1]))
    _cl(ax, mo[0] + 1.1, mo[1], "Y", ha="left", color=ACC)
    return _nat(fig)


# ------------------------------------------------------------------ 9. first two stages of the arithmetic circuit
def arith2():
    fig, ax = _cv((-2.8, 16.4), (-0.6, 8.7), 0.29)
    xs = {1: 0.0, 0: 7.4}
    ybus = {"S1": 0.7, "S0": 0.1}
    for i, ox in xs.items():
        mx, my, mh = ox + 2.5, 1.6, 2.4
        out, pins = _mux(ax, mx, my, mh, data=None, label="4:1", sel=(), dlen=0, outside=False)
        # B_i and its inverter
        xd = ox + 0.6
        _cl(ax, ox - 0.1, pins[0][1], f"B_{i}", ha="right", fs=9.5)
        _pl(ax, [(ox, pins[0][1]), pins[0]]); _dot(ax, xd, pins[0][1])
        _pl(ax, [(xd, pins[0][1]), (xd, pins[3][1]), (xd + 0.4, pins[3][1])])
        _, no = _not(ax, xd + 0.4, pins[3][1])
        _pl(ax, [no, pins[3]])
        _t(ax, (no[0] + mx) / 2 - 0.1, pins[3][1] - 0.14, f"B_{i}'", fs=8, color=MUTED, va="top")
        for k, lab in ((1, "0"), (2, "1")):
            _pl(ax, [(ox + 1.5, pins[k][1]), pins[k]])
            _t(ax, ox + 1.4, pins[k][1], lab, ha="right", fs=9.5, weight="bold", color=MUTED if lab == "0" else G2)
        # selects: S1 (left stub) and S0 (right stub) down to the shared buses
        for j, nm in enumerate(("S1", "S0")):
            sx = mx + 1.5 * (0.26 + 0.5 * j)
            yb = my + 0.4 * (sx - mx) / 1.5
            _pl(ax, [(sx, yb), (sx, ybus[nm])]); _dot(ax, sx, ybus[nm])
        # full adder
        _box(ax, ox + 2.6, 5.2, 2.6, 1.4, f"full\nadder {i}", fc=TINT, ec=ACC, fs=9)
        _pl(ax, [out, (ox + 4.6, out[1])])
        _arrow(ax, (ox + 4.6, out[1]), (ox + 4.6, 5.2))
        _t(ax, ox + 4.75, 4.0, f"Y_{i}", ha="left", fs=9.5, weight="bold")
        _arrow(ax, (ox + 3.0, 7.9), (ox + 3.0, 6.6))
        _cl(ax, ox + 3.0, 8.05, f"X_{i} = A_{i}", fs=9.5, va="bottom")
        _arrow(ax, (ox + 4.7, 6.6), (ox + 4.7, 7.9))
        _cl(ax, ox + 4.7, 8.05, f"F_{i}", fs=9.5, va="bottom", color=ACC)
    # shared select buses
    _pl(ax, [(-0.4, 0.7), (xs[0] + 2.9 + 0.5, 0.7)])
    _pl(ax, [(-0.4, 0.1), (13.3, 0.1), (13.3, 5.9)])
    _cl(ax, -0.5, 0.7, "S1 = S", ha="right", fs=9)
    _cl(ax, -0.5, 0.1, "S0 = C_in", ha="right", fs=9)
    # carries
    _arrow(ax, (xs[0] + 2.6, 5.9), (xs[1] + 5.2, 5.9))
    _cl(ax, (xs[0] + 2.6 + xs[1] + 5.2) / 2, 6.05, "C_1", fs=9.5, va="bottom")
    _arrow(ax, (xs[1] + 2.6, 5.9), (1.3, 5.9))
    _cl(ax, 1.2, 5.9, "C_2", ha="right", fs=9.5)
    _arrow(ax, (13.3, 5.9), (xs[0] + 5.2, 5.9))
    _cl(ax, 13.5, 5.9, "C_0 = C_in", ha="left", fs=9.5)
    return _nat(fig)


# ------------------------------------------------------------------ 10. one ALU bit as blocks
def alu_block():
    fig, ax = _cv((-2.6, 14.2), (-0.6, 11.4), 0.33)
    _box(ax, 4.4, 5.6, 4.2, 2.6, "arithmetic stage\n(MUX + full adder)", fc=TINT, ec=ACC, fs=9)
    _box(ax, 4.4, 0.6, 4.2, 2.4, "logic unit", fc=TINT, ec=ACC, fs=9)
    xd, xc = 1.0, 2.2
    # data bundle A_i, B_i
    _pl(ax, [(-0.4, 4.8), (xd, 4.8)]); _dot(ax, xd, 4.8)
    _cl(ax, -0.5, 4.8, "A_i, B_i", ha="right", fs=9.5)
    _pl(ax, [(xd, 7.4), (xd, 2.4)])
    _arrow(ax, (xd, 7.4), (4.4, 7.4)); _arrow(ax, (xd, 2.4), (4.4, 2.4))
    _dot(ax, xd, 7.4); _dot(ax, xd, 2.4)
    # code bundle S1 S0
    _cl(ax, xc, 10.3, "S1 S0", fs=9.5)
    _t(ax, xc, 9.75, "(S, C_in if M = 0)", fs=7.5, color=MUTED, va="center")
    _pl(ax, [(xc, 9.4), (xc, 1.2)])
    _arrow(ax, (xc, 6.2), (4.4, 6.2)); _arrow(ax, (xc, 1.2), (4.4, 1.2))
    _dot(ax, xc, 6.2); _dot(ax, xc, 1.2)
    # carry
    _arrow(ax, (7.8, 9.4), (7.8, 8.2)); _cl(ax, 7.8, 9.55, "C_i", fs=9.5, va="bottom")
    _arrow(ax, (5.2, 8.2), (5.2, 9.4)); _cl(ax, 5.2, 9.55, r"$\mathrm{C}_{\mathrm{i+1}}$", fs=9.5, va="bottom")
    # output MUX 2:1
    mo, pins = _mux(ax, 10.8, 3.0, 2.6, n=2, data=None, label="2:1", sel=("M",), dlen=0, outside=False)
    _pl(ax, [(8.6, 7.4), (10.0, 7.4), (10.0, pins[0][1])]); _arrow(ax, (10.0, pins[0][1]), pins[0])
    _pl(ax, [(8.6, 2.4), (10.0, 2.4), (10.0, pins[1][1])]); _arrow(ax, (10.0, pins[1][1]), pins[1])
    _t(ax, 9.9, 7.55, "M = 0", fs=8, color=MUTED, ha="right", va="bottom")
    _t(ax, 9.9, 2.55, "M = 1", fs=8, color=MUTED, ha="right", va="bottom")
    _arrow(ax, mo, (mo[0] + 1.0, mo[1]))
    _cl(ax, mo[0] + 1.1, mo[1], "F_i", ha="left", color=ACC)
    return _nat(fig)


FIGS = {"fa_kmaps": fa_kmaps, "cla_delay2": cla_delay2, "ha_nand": ha_nand, "half_sub": half_sub,
        "full_sub_2hs": full_sub_2hs, "addsub_cell": addsub_cell, "barrel4": barrel4, "lu41": lu41,
        "arith2": arith2, "alu_block": alu_block}
