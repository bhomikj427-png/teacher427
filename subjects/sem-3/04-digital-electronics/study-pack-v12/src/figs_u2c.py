"""Unit 2 figures for file 07 (display, comparator, parity): v1.3, S6."""
import figs1
from figs1 import ACC, G1, G2, INK, MUTED, SOFT, TINT, _arrow, _box, _line, _nat
from figs_u2 import _and, _cv, _dot, _not
from figs_u2b import _cl, _pl, _t, _xnor, _xor

plt = figs1.plt


# ------------------------------------------------------------------ 1. segment a K-map
def seg_kmap_a():
    return figs1.km("ABCD", ones=[0, 2, 3, 5, 6, 7, 8, 9], dcs=[10, 11, 12, 13, 14, 15],
                    terms=("A", "C", "BD", "B'D'"), title="a")


# ------------------------------------------------------------------ 2. 1-bit comparator
def comp1():
    fig, ax = _cv((-1.0, 11.4), (-1.5, 8.2), 0.36)
    xa, xb = 0.6, 1.5
    _cl(ax, xa, 7.7, "A")
    _cl(ax, xb, -1.0, "B", va="top")
    _line(ax, [xa, xa], [7.4, 0.3])
    _line(ax, [xb, xb], [-0.7, 5.7])
    # top: AND(A', B)
    _pl(ax, [(xa, 6.3), (2.6, 6.3)]); _dot(ax, xa, 6.3)
    _, na = _not(ax, 2.6, 6.3)
    th, tl, to = _and(ax, 4.4, 6.0, 1.3, 1.2)
    _pl(ax, [na, th])
    _t(ax, 3.9, 6.5, "A'", fs=8.5, color=MUTED, va="bottom")
    _pl(ax, [(xb, tl[1]), tl]); _dot(ax, xb, tl[1])
    # middle: XNOR(A, B)
    mh, ml, mo = _xnor(ax, 4.2, 3.0, 1.3, 1.2)
    _pl(ax, [(xa, mh[1]), mh]); _dot(ax, xa, mh[1])
    _pl(ax, [(xb, ml[1]), ml]); _dot(ax, xb, ml[1])
    # bottom: AND(A, B')
    bh, bl, bo = _and(ax, 4.4, 0.0, 1.3, 1.2)
    _pl(ax, [(xa, bh[1]), bh]); _dot(ax, xa, bh[1])
    _pl(ax, [(xb, bl[1]), (2.6, bl[1])]); _dot(ax, xb, bl[1])
    _, nb = _not(ax, 2.6, bl[1])
    _pl(ax, [nb, bl])
    _t(ax, 3.9, bl[1] - 0.2, "B'", fs=8.5, color=MUTED, va="top")
    for p, lab in ((to, "L (A < B) = A'B"), (mo, "E (A = B)"), (bo, "G (A > B) = AB'")):
        _arrow(ax, p, (6.6, p[1]))
        _cl(ax, 6.7, p[1], lab, ha="left", color=ACC, fs=9.5)
    return _nat(fig)


# ------------------------------------------------------------------ 3. 2-bit comparator K-maps
def _km4(ones, groups, title):
    """4-variable map drawn as W X Y Z (W = MSB), shown as A1 A0 B1 B0."""
    cells = {m: "1" for m in ones}
    gs = [{"cells": figs1._cells_of(t, "WXYZ"), "term": lab, "color": i} for i, (t, lab) in enumerate(groups)]
    svg = figs1.kfig.kmap(cells, gs, rv="AB", cv="CD", cs=42, show_idx=True, title=title)
    return svg.replace(">AB</text>", ">A₁A₀</text>").replace(">CD</text>", ">B₁B₀</text>")


def comp2_kmaps():
    g = _km4([4, 8, 9, 12, 13, 14], [("WY'", "A₁B₁'"), ("XY'Z'", "A₀B₁'B₀'"), ("WXZ'", "A₁A₀B₀'")], "G (A &gt; B)")
    l = _km4([1, 2, 3, 6, 7, 11], [("W'Y", "A₁'B₁"), ("X'YZ", "A₀'B₁B₀"), ("W'X'Z", "A₁'A₀'B₀")], "L (A &lt; B)")
    return ('<div style="display:flex;gap:6mm;justify-content:center;align-items:flex-start">'
            + "".join(f'<div style="flex:1 1 0;min-width:0">{s}</div>' for s in (g, l)) + "</div>")


# ------------------------------------------------------------------ 4. cascading two 4-bit comparators
def comp_cascade():
    fig, ax = _cv((-1.2, 15.8), (-1.2, 6.9), 0.3)
    ys = (2.9, 2.0, 1.1)
    outs = ("A>B", "A=B", "A<B")
    ins = ("I(A>B)", "I(A=B)", "I(A<B)")
    for x0, title, ah, bh in ((1.8, "7485 (bits 7–4)", "A7–A4", "B7–B4"), (8.8, "7485 (bits 3–0)", "A3–A0", "B3–B0")):
        _box(ax, x0, 0.0, 4.6, 4.6, "", fc=TINT, ec=ACC, r=0.12)
        _t(ax, x0 + 2.3, 3.75, title, fs=9, weight="bold", color=ACC)
        for dx, nm, lab in ((1.2, "A", ah), (3.4, "B", bh)):
            _arrow(ax, (x0 + dx, 5.9), (x0 + dx, 4.6))
            _t(ax, x0 + dx, 6.0, lab, fs=9.5, weight="bold", va="bottom")
            _t(ax, x0 + dx, 4.35, nm, fs=8, color=MUTED)
        for y, o, i in zip(ys, outs, ins):
            _t(ax, x0 + 0.15, y, o, fs=8.5, ha="left")
            _t(ax, x0 + 4.45, y, i, fs=8.5, ha="right")
    # low chip outputs -> high chip cascade inputs
    for y in ys:
        _arrow(ax, (8.8, y), (6.4, y))
    # final outputs of the 8-bit comparison
    for y, o in zip(ys, outs):
        _arrow(ax, (1.8, y), (0.8, y))
        _cl(ax, 0.7, y, o, ha="right", color=ACC, fs=9.5)
    # tied cascade inputs of the low chip
    for y, c in zip(ys, ("0", "1", "0")):
        _line(ax, [13.4, 14.4], [y, y])
        _t(ax, 14.5, y, c, ha="left", fs=10, weight="bold", color=G2 if c == "1" else MUTED)
    _t(ax, 11.1, -0.65, "cascade inputs tied: 0, 1, 0", fs=8.5, color=MUTED)
    return _nat(fig)


# ------------------------------------------------------------------ 5. parity: daisy chain vs tree
def parity_chain_tree():
    fig, ax = _cv((-0.8, 12.8), (-1.3, 9.9), 0.34)
    yc = 8.0
    # --- daisy chain
    _t(ax, 0.0, 9.35, "daisy chain", fs=10, weight="bold", color=ACC, ha="left")
    _cl(ax, 0.9, yc + 0.25, "A", ha="right", fs=10)
    _cl(ax, 0.9, yc - 0.25, "B", ha="right", fs=10)
    p1, q1, o1 = _xor(ax, 1.6, yc)
    _pl(ax, [(1.0, yc + 0.25), p1]); _pl(ax, [(1.0, yc - 0.25), q1])
    p2, q2, o2 = _xor(ax, 4.4, yc)
    _pl(ax, [o1, (3.7, yc), (3.7, yc + 0.25), p2])
    p3, q3, o3 = _xor(ax, 7.0, yc)
    _pl(ax, [o2, (6.5, yc), (6.5, yc + 0.25), p3])
    for xv, n, q in ((3.9, "C", q2), (6.7, "D", q3)):
        _pl(ax, [(xv, yc - 1.2), (xv, q[1]), q])
        _cl(ax, xv, yc - 1.3, n, va="top", fs=10)
    _pl(ax, [o3, (9.0, yc)]); _dot(ax, 9.0, yc)
    _arrow(ax, (9.0, yc), (9.7, yc))
    _cl(ax, 9.8, yc, "P_even", ha="left", color=ACC, fs=10)
    yn = yc - 1.5
    _pl(ax, [(9.0, yc), (9.0, yn), (9.3, yn)])
    _, nout = _not(ax, 9.3, yn)
    _arrow(ax, nout, (nout[0] + 0.7, yn))
    _cl(ax, nout[0] + 0.8, yn, "P_odd", ha="left", color=ACC, fs=10)
    _cl(ax, 4.5, 5.3, "3 gate delays", color=G1, fs=9.5)
    _line(ax, [-0.4, 12.4], [4.65, 4.65], color="#c9cbc4", lw=1)
    # --- tree
    _t(ax, 0.0, 4.15, "tree", fs=10, weight="bold", color=ACC, ha="left")
    ya, yb, yo = 2.9, 0.9, 1.9
    for y, (n1, n2) in ((ya, ("A", "B")), (yb, ("C", "D"))):
        _cl(ax, 0.9, y + 0.25, n1, ha="right", fs=10)
        _cl(ax, 0.9, y - 0.25, n2, ha="right", fs=10)
        p, q, o = _xor(ax, 1.6, y)
        _pl(ax, [(1.0, y + 0.25), p]); _pl(ax, [(1.0, y - 0.25), q])
    pc, qc, oc = _xor(ax, 4.6, yo)
    _pl(ax, [(2.96, ya), (3.9, ya), (3.9, pc[1]), pc])
    _pl(ax, [(2.96, yb), (3.9, yb), (3.9, qc[1]), qc])
    _arrow(ax, oc, (oc[0] + 0.8, yo))
    _cl(ax, oc[0] + 0.9, yo, "P_even", ha="left", color=ACC, fs=10)
    _cl(ax, 4.0, -0.5, "2 gate delays", color=G2, fs=9.5)
    return _nat(fig)


# ------------------------------------------------------------------ 6. parity generator + link + checker
def parity_system():
    fig, ax = _cv((-1.0, 18.8), (-0.4, 8.6), 0.27)
    yX, yY, yP, yZ = 6.5, 5.8, 2.6, 0.9
    _box(ax, 0.5, 0.3, 5.5, 7.3, "", fc="white", ec=ACC, r=0.12)
    _box(ax, 9.6, 0.3, 5.6, 7.3, "", fc="white", ec=ACC, r=0.12)
    _box(ax, 6.4, 0.3, 2.8, 7.3, "", fc="white", ec=MUTED, ls="--", r=0.12)
    _t(ax, 3.25, 7.95, "sender: even parity generator", fs=8.5, weight="bold", color=ACC)
    _t(ax, 12.4, 7.95, "receiver: even parity checker", fs=8.5, weight="bold", color=ACC)
    _t(ax, 7.8, 7.15, "link", fs=9, color=MUTED)
    # sender
    for y, n in ((yX, "X"), (yY, "Y"), (yZ, "Z")):
        _cl(ax, 0.3, y, n, ha="right", fs=10)
    p1, q1, o1 = _xor(ax, 2.2, 4.2, 1.2, 1.4)
    p2, q2, o2 = _xor(ax, 4.2, 2.6, 1.2, 1.4)
    _pl(ax, [(0.3, yX), (10.935, yX)]); _pl(ax, [(0.3, yY), (10.935, yY)]); _pl(ax, [(0.3, yZ), (10.2, yZ)])
    _pl(ax, [(0.9, yX), (0.9, q1[1]), q1]); _dot(ax, 0.9, yX)
    _pl(ax, [(1.5, yY), (1.5, p1[1]), p1]); _dot(ax, 1.5, yY)
    _pl(ax, [o1, (3.9, o1[1]), (3.9, p2[1]), p2])
    _pl(ax, [(3.4, yZ), (3.4, q2[1]), q2]); _dot(ax, 3.4, yZ)
    _pl(ax, [o2, (9.6, o2[1])])
    _cl(ax, 5.55, o2[1] + 0.2, "P", fs=10, va="bottom", ha="center")
    # receiver
    r1p, r1q, r1o = _xor(ax, 10.8, 6.15, 1.2, 1.4)
    r2p, r2q, r2o = _xor(ax, 10.8, 1.75, 1.2, 1.4)
    _pl(ax, [(9.6, yP), (10.2, yP), (10.2, r2p[1]), r2p]); _pl(ax, [(10.2, yZ), (10.2, r2q[1]), r2q])
    r3p, r3q, r3o = _xor(ax, 13.2, 3.95, 1.2, 1.4)
    _pl(ax, [r1o, (12.8, r1o[1]), (12.8, r3p[1]), r3p])
    _pl(ax, [r2o, (12.8, r2o[1]), (12.8, r3q[1]), r3q])
    _pl(ax, [r3o, (15.2, r3o[1])])
    _arrow(ax, (15.2, r3o[1]), (16.0, r3o[1]))
    _cl(ax, 16.1, r3o[1] + 0.2, "E", ha="left", color=ACC, fs=10.5, va="bottom")
    _t(ax, 16.1, r3o[1] - 0.1, "(1 = error)", ha="left", fs=8.5, color=MUTED, va="top")
    return _nat(fig)


FIGS = {"seg_kmap_a": seg_kmap_a, "comp1": comp1, "comp2_kmaps": comp2_kmaps, "comp_cascade": comp_cascade,
        "parity_chain_tree": parity_chain_tree, "parity_system": parity_system}
