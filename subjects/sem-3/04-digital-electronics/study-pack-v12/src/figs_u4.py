"""Unit 4 state-machine figures for files 15-16 (v1.3, S4 2026-11-17)."""
import math

import figs1
from figs1 import ACC, BAD, G1, G2, INK, MUTED, TINT, _arrow, _box, _canvas, _line, _nat
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle
from matplotlib.path import Path

plt = figs1.plt


def _cv(xlim, ylim, s):
    return _canvas(s * (xlim[1] - xlim[0]), s * (ylim[1] - ylim[0]), xlim, ylim)


# ------------------------------------------------------------------ state-diagram helpers
def _circ(ax, x, y, r, txt, ec=ACC, fs=9, fc=TINT):
    ax.add_patch(Circle((x, y), r, fc=fc, ec=ec, lw=1.5, zorder=3))
    ax.text(x, y, txt, ha="center", va="center", fontsize=fs, weight="bold", zorder=4)


def _edge(ax, P, a, b, lab, rad=0.0, ls=None, col=INK, r=0.55, off=0.27, t=0.5, fs=8.6, lcol=None):
    """Arrow a -> b between circles of radius r. Positive rad bends to the right-hand normal (dy, -dx).
    ls = side of the label along that normal (default: the side the arc bends to)."""
    (x1, y1), (x2, y2) = P[a], P[b]
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    nx, ny = uy, -ux
    th = math.atan(2 * rad)
    c, s = math.cos(th), math.sin(th)
    p = (x1 + r * (c * ux + s * nx), y1 + r * (c * uy + s * ny))
    q = (x2 + r * (-c * ux + s * nx), y2 + r * (-c * uy + s * ny))
    _arrow(ax, p, q, color=col, rad=rad, lw=1.4 if col != INK else 1.3)
    dd = math.hypot(q[0] - p[0], q[1] - p[1])
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    qx, qy = (q[1] - p[1]) / dd, -(q[0] - p[0]) / dd
    cx, cy = mx + rad * dd * qx, my + rad * dd * qy
    bx = (1 - t) ** 2 * p[0] + 2 * t * (1 - t) * cx + t * t * q[0]
    by = (1 - t) ** 2 * p[1] + 2 * t * (1 - t) * cy + t * t * q[1]
    if ls is None:
        ls = 1 if rad > 0 else (-1 if rad < 0 else 1)
    ax.text(bx + ls * off * qx, by + ls * off * qy, lab, ha="center", va="center", fontsize=fs,
            color=lcol or (col if col != INK else INK), weight="bold" if col != INK else "normal", zorder=5)


def _loop(ax, P, a, lab, ang=90, r=0.55, h=0.7, w=36, col=INK, lo=0.3, fs=8.6, dx=0.0, dy=0.0):
    x, y = P[a]
    A = math.radians(ang)
    ux, uy = math.cos(A), math.sin(A)
    p0 = (x + r * math.cos(A - math.radians(w)), y + r * math.sin(A - math.radians(w)))
    p1 = (x + r * math.cos(A + math.radians(w)), y + r * math.sin(A + math.radians(w)))
    k = (r + h - r * math.cos(math.radians(w))) / 0.75
    pth = Path([p0, (p0[0] + k * ux, p0[1] + k * uy), (p1[0] + k * ux, p1[1] + k * uy), p1],
               [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])
    ax.add_patch(FancyArrowPatch(path=pth, arrowstyle="-|>,head_length=0.4,head_width=0.24", color=col,
                                 lw=1.4 if col != INK else 1.3, mutation_scale=10, shrinkA=0, shrinkB=0))
    ax.text(x + (r + h + lo) * ux + dx, y + (r + h + lo) * uy + dy, lab, ha="center", va="center", fontsize=fs,
            color=col, weight="bold" if col != INK else "normal", zorder=5)


def _reset(ax, P, a, r=0.55, L=1.2, side="left", fs=8.4):
    x, y = P[a]
    if side == "left":
        _arrow(ax, (x - r - L, y), (x - r, y), color=MUTED)
        ax.text(x - r - L / 2, y + 0.25, "reset", ha="center", va="bottom", fontsize=fs, color=MUTED)


# ------------------------------------------------------------------ 1. partial 1101 chain
def chain_1101():
    P = {"A": (0, 0), "B": (3, 0), "C": (6, 0), "D": (9, 0)}
    xl, yl = (-1.0, 10.0), (-1.0, 2.4)
    fig, ax = _cv(xl, yl, 0.55)
    for k, (x, y) in P.items():
        _circ(ax, x, y, 0.55, k)
    _edge(ax, P, "A", "B", "1/0", ls=-1)
    _edge(ax, P, "B", "C", "1/0", ls=-1)
    _edge(ax, P, "C", "D", "0/0", ls=-1)
    _edge(ax, P, "D", "B", "1/1", rad=0.5, col=G1, off=0.3)
    return _nat(fig)


# ------------------------------------------------------------------ 2. 1010 non-overlapping vs overlapping
def d1010():
    xl, yl = (-1.5, 12.6), (-4.8, 3.0)
    fig, ax = _cv(xl, yl, 0.5)
    for k, (ox, title, over) in enumerate(((0.0, "Non-overlapping", False), (8.0, "Overlapping", True))):
        P = {"S0": (ox, 0), "S1": (ox + 3.2, 0), "S2": (ox + 3.2, -3.2), "S3": (ox, -3.2)}
        for n, (x, y) in P.items():
            _circ(ax, x, y, 0.55, n)
        ax.text(ox + 1.6, 2.5, title, ha="center", va="center", fontsize=10, weight="bold", color=ACC)
        _loop(ax, P, "S0", "0/0")
        _loop(ax, P, "S1", "1/0")
        _edge(ax, P, "S0", "S1", "1/0", ls=-1)
        _edge(ax, P, "S1", "S2", "0/0", ls=-1, off=0.32)
        _edge(ax, P, "S2", "S0", "0/0", t=0.28, ls=1, off=0.3)
        _edge(ax, P, "S3", "S1", "1/0", t=0.28, ls=-1, off=0.3)
        _edge(ax, P, "S2", "S3", "1/0", ls=1, off=0.28)
        if over:
            _edge(ax, P, "S3", "S2", "0/1", rad=0.5, col=G1, ls=1, off=0.3)
        else:
            _edge(ax, P, "S3", "S0", "0/1", col=G1, ls=-1, off=0.34)
    return _nat(fig)


# ------------------------------------------------------------------ 3. 1101 detector, gray encoding, D flip-flops
def gray_circuit():
    xl, yl = (-2.9, 18.7), (-3.9, 8.9)
    fig, ax = _cv(xl, yl, 0.4)
    gate = dict(fc=TINT, ec=ACC, fs=8.5, r=0.2)

    def dot(x, y):
        ax.plot(x, y, "o", ms=3.5, color=INK, zorder=6)

    def stub(x0, x1, y, name):
        _line(ax, [x0, x1], [y, y])
        ax.text(x0 - 0.1, y, name, ha="right", va="center", fontsize=9, weight="bold", color=ACC)

    # gates
    _box(ax, 3.6, 7.0, 1.6, 1.2, "AND", **gate)
    _box(ax, 3.6, 4.4, 1.6, 1.2, "AND", **gate)
    _box(ax, 6.4, 5.3, 1.5, 1.8, "OR", **gate)
    stub(3.1, 3.6, 7.9, "Y1")
    stub(3.1, 3.6, 7.3, "Y2")
    stub(3.1, 3.6, 4.7, "Y2")
    _line(ax, [5.2, 5.8, 5.8, 6.4], [7.6, 7.6, 6.7, 6.7])
    _line(ax, [5.2, 5.8, 5.8, 6.4], [5.0, 5.0, 5.7, 5.7])
    # flip-flops
    for (y0, nm, ys, yc, yr, who) in ((4.2, "FF1", 6.2, 5.4, 4.6, "Y1"), (0.0, "FF2", 2.0, 1.2, 0.4, "Y2")):
        _box(ax, 10.4, y0, 2.2, 2.4, "", ec=ACC, r=0.06)
        ax.text(10.55, ys, "D", va="center", fontsize=9, weight="bold")
        ax.text(10.55, yr, "R", va="center", fontsize=9, weight="bold")
        ax.add_patch(Polygon([(10.4, yc - 0.2), (10.65, yc), (10.4, yc + 0.2)], closed=True, fc="none", ec=INK, lw=1.1))
        ax.text(12.45, ys, "Q", ha="right", va="center", fontsize=9, weight="bold")
        ax.text(12.45, yc, "Q'", ha="right", va="center", fontsize=9, weight="bold")
        ax.text(11.5, y0 + 2.65, f"{nm}  ({who})", ha="center", va="center", fontsize=9, color=ACC, weight="bold")
    # OR -> D1
    _line(ax, [7.9, 10.4], [6.2, 6.2])
    # X input, bus, D2 = X
    _line(ax, [0.4, 10.4], [2.0, 2.0])
    ax.text(0.3, 2.0, "X", ha="right", va="center", fontsize=9.5, weight="bold", color=ACC)
    dot(1.5, 2.0)
    _line(ax, [1.5, 1.5, 3.6], [2.0, 5.3, 5.3])
    # clock and reset
    _line(ax, [0.4, 9.2], [-1.8, -1.8], color=MUTED)
    ax.text(0.3, -1.8, "CLK", ha="right", va="center", fontsize=9, color=MUTED)
    _line(ax, [9.2, 9.2], [-1.8, 5.4], color=MUTED)
    for y in (1.2, 5.4):
        _line(ax, [9.2, 10.4], [y, y], color=MUTED)
        dot(9.2, y)
    _line(ax, [0.4, 8.2], [-0.9, -0.9], color=G1)
    ax.text(0.3, -0.9, "Reset (to 00)", ha="right", va="center", fontsize=9, color=G1)
    _line(ax, [8.2, 8.2], [-0.9, 4.6], color=G1)
    for y in (0.4, 4.6):
        _line(ax, [8.2, 10.4], [y, y], color=G1)
        dot(8.2, y)
    # outputs and Z
    _line(ax, [12.6, 13.0, 13.0, 15.4], [6.2, 6.2, 4.0, 4.0])
    ax.text(13.15, 5.1, "Y1", ha="left", va="center", fontsize=9, weight="bold", color=ACC)
    _line(ax, [12.6, 13.2], [2.0, 2.0])
    ax.text(13.3, 2.0, "Y2", ha="left", va="center", fontsize=9, weight="bold", color=ACC)
    _line(ax, [12.6, 14.4, 14.4, 15.4], [1.2, 1.2, 2.8, 2.8])
    ax.text(13.5, 0.9, "Y2'", ha="center", va="center", fontsize=9, weight="bold", color=ACC)
    _line(ax, [14.9, 15.4], [3.4, 3.4])
    ax.text(14.8, 3.4, "X", ha="right", va="center", fontsize=9, weight="bold", color=ACC)
    _box(ax, 15.4, 2.4, 1.6, 2.0, "AND", **gate)
    _arrow(ax, (17.0, 3.4), (17.8, 3.4), color=G1)
    ax.text(18.0, 3.4, "Z", ha="left", va="center", fontsize=10, weight="bold", color=G1)
    ax.text(8.0, -3.2, "D1 = Y1Y2 + XY2   ·   D2 = X   ·   Z = XY1Y2'", ha="center", va="center", fontsize=9.5,
            color=G1, weight="bold")
    return _nat(fig)


# ------------------------------------------------------------------ 4. 111 detector, Mealy vs Moore
def d111():
    xl, yl = (-2.2, 19.4), (-4.4, 3.6)
    fig, ax = _cv(xl, yl, 0.42)
    # Mealy
    P = {"A": (0, 0), "B": (2.8, 0), "C": (5.6, 0)}
    for n, (x, y) in P.items():
        _circ(ax, x, y, 0.55, n)
    ax.text(2.8, 3.0, "Mealy: 3 states", ha="center", va="center", fontsize=10, weight="bold", color=ACC)
    _reset(ax, P, "A")
    _loop(ax, P, "A", "0/0", ang=105, lo=0.28)
    _edge(ax, P, "A", "B", "1/0", rad=-0.3, ls=1)
    _edge(ax, P, "B", "A", "0/0", rad=-0.3, ls=1)
    _edge(ax, P, "B", "C", "1/0", ls=-1)
    _loop(ax, P, "C", "1/1", ang=70, col=G1)
    _edge(ax, P, "C", "A", "0/0", rad=-0.45, ls=1, off=0.3)
    # Moore
    ox = 9.2
    Q = {"A": (ox, 0), "B": (ox + 2.8, 0), "C": (ox + 5.6, 0), "D": (ox + 8.4, 0)}
    for n, (x, y) in Q.items():
        _circ(ax, x, y, 0.6, n + ("/1" if n == "D" else "/0"), ec=G1 if n == "D" else ACC, fs=8.6)
    ax.text(ox + 4.2, 3.0, "Moore: 4 states", ha="center", va="center", fontsize=10, weight="bold", color=ACC)
    _reset(ax, Q, "A", r=0.6)
    _loop(ax, Q, "A", "0", ang=105, r=0.6, lo=0.28)
    _edge(ax, Q, "A", "B", "1", rad=-0.3, ls=1, r=0.6)
    _edge(ax, Q, "B", "A", "0", rad=-0.3, ls=1, r=0.6)
    _edge(ax, Q, "B", "C", "1", ls=-1, r=0.6)
    _edge(ax, Q, "C", "D", "1", ls=-1, r=0.6)
    _loop(ax, Q, "D", "1", ang=70, r=0.6, col=G1)
    _edge(ax, Q, "C", "A", "0", rad=-0.55, ls=1, r=0.6, off=0.3)
    _edge(ax, Q, "D", "A", "0", rad=-0.8, ls=1, r=0.6, off=0.3)
    return _nat(fig)


# ------------------------------------------------------------------ 5. 111 timing diagram, simulated
def _runs(pts, T):
    """[(t, v)] breakpoints -> list of (t0, t1, v) with equal neighbours merged."""
    out = []
    for k, (t, v) in enumerate(pts):
        t1 = pts[k + 1][0] if k + 1 < len(pts) else T
        if out and out[-1][2] == v:
            out[-1] = (out[-1][0], t1, v)
        else:
            out.append((t, t1, v))
    return out


def timing_111():
    T = 8.5
    edges = list(range(1, 9))
    xbp = [(0, 0), (0.5, 1), (2.6, 0), (3.6, 1)]

    def xv(t):
        v = 0
        for tt, vv in xbp:
            if tt <= t:
                v = vv
        return v

    mealy = {("A", 0): "A", ("A", 1): "B", ("B", 0): "A", ("B", 1): "C", ("C", 0): "A", ("C", 1): "C"}
    moore = {("A", 0): "A", ("A", 1): "B", ("B", 0): "A", ("B", 1): "C", ("C", 0): "A", ("C", 1): "D",
             ("D", 0): "A", ("D", 1): "D"}
    sm, so = ["A"], ["A"]
    for e in edges:
        sm.append(mealy[(sm[-1], xv(e))])
        so.append(moore[(so[-1], xv(e))])
    assert sm[1:] == list("BCABCCCC"), sm
    assert so[1:] == list("BCABCDDD"), so
    stm = [(0, sm[0])] + [(e, s) for e, s in zip(edges, sm[1:])]
    sto = [(0, so[0])] + [(e, s) for e, s in zip(edges, so[1:])]
    # Mealy Z: state == C and X == 1, evaluated on every interval between state/X changes
    cuts = sorted({0, T} | {t for t, _ in stm} | {t for t, _ in xbp})
    zm_pts = []
    for a, b in zip(cuts, cuts[1:]):
        mid = (a + b) / 2
        s = [v for t, v in stm if t <= mid][-1]
        zm_pts.append((a, 1 if (s == "C" and xv(mid) == 1) else 0))
    zm = _runs(zm_pts, T)
    zm1 = [(a, b) for a, b, v in zm if v]
    assert zm1 == [(2.0, 2.6), (5.0, 8.5)], zm1
    zo_pts = [(t, 1 if s == "D" else 0) for t, s in sto]
    zo1 = [(a, b) for a, b, v in _runs(zo_pts, T) if v]
    assert zo1 == [(6.0, 8.5)], zo1

    clk = [(0, 0)]
    for e in edges:
        clk += [(e, 1), (e + 0.5, 0)]
    names = ["CLK", "X", "state (Mealy)", "Z Mealy", "state (Moore)", "Z Moore"]
    fig, ax = plt.subplots(figsize=(8.2, 4.1))
    ax.set_xlim(-2.5, T + 0.3)
    ax.set_ylim(-6.3, 0.9)
    ax.axis("off")
    H = 0.55

    def dig(r, pts, color=ACC, lw=1.6):
        base = -r
        xs, ys = [], []
        for k, (t, v) in enumerate(pts):
            if k:
                xs.append(t)
                ys.append(ys[-1])
            xs.append(t)
            ys.append(base + H * v)
        xs.append(T)
        ys.append(ys[-1])
        ax.plot(xs, ys, color=color, lw=lw, solid_joinstyle="miter", zorder=3)

    def bus(r, pts, color=ACC):
        base = -r
        for k, (t, s) in enumerate(pts):
            t1 = pts[k + 1][0] if k + 1 < len(pts) else T
            ch = 0.07
            ax.add_patch(Polygon([(t + ch, base + H), (t1 - ch, base + H), (t1, base + H / 2), (t1 - ch, base),
                                  (t + ch, base), (t, base + H / 2)], closed=True, fc=TINT, ec=color, lw=1.4, zorder=2))
            ax.text((t + t1) / 2, base + H / 2, s, ha="center", va="center", fontsize=9.5, weight="bold", zorder=4)

    for r, nm in enumerate(names):
        ax.text(-0.2, -r + H / 2, nm, ha="right", va="center", fontsize=9.5, weight="bold" if nm != "CLK" else "normal",
                color=MUTED if nm == "CLK" else INK)
    for e in edges:
        ax.plot([e, e], [0.7, -5.2], color=MUTED, lw=0.8, ls=(0, (1, 3)), alpha=0.7, zorder=1)
    dig(0, clk, MUTED)
    dig(1, xbp)
    bus(2, stm)
    dig(3, [(a, v) for a, b, v in zm], G1)
    bus(4, sto)
    dig(5, [(a, v) for a, b, v in _runs(zo_pts, T)], G1)
    # false output on the Mealy Z row
    a, b = zm1[0]
    ax.plot([a, a, b, b], [-3, -3 + H, -3 + H, -3], color=BAD, lw=2.4, zorder=4)
    ax.text(2.75, -3 + H / 2, "← false output", ha="left", va="center", fontsize=8.4, color=BAD, weight="bold",
            bbox=dict(fc="white", ec="none", pad=0.8), zorder=6)
    # time axis
    ax.plot([0, T], [-5.55, -5.55], color=INK, lw=1)
    for e in range(0, 9):
        ax.plot([e, e], [-5.55, -5.65], color=INK, lw=1)
        ax.text(e, -5.75, str(e), ha="center", va="top", fontsize=8.5, color=INK)
    ax.text(T + 0.05, -5.55, "t", ha="left", va="center", fontsize=9, style="italic")
    return _nat(fig)


# ------------------------------------------------------------------ 6. 1011 Moore detector (overlap)
def moore_1011():
    xl, yl = (-1.4, 12.6), (-2.9, 3.4)
    fig, ax = _cv(xl, yl, 0.5)
    pit = 2.8
    P = {f"S{i}": (i * pit, 0) for i in range(5)}
    r = 0.6
    for n, (x, y) in P.items():
        _circ(ax, x, y, r, n + ("/1" if n == "S4" else "/0"), ec=G1 if n == "S4" else ACC, fs=8.6)
    _loop(ax, P, "S0", "0", ang=125, r=r, lo=0.28)
    _loop(ax, P, "S1", "1", ang=125, r=r, lo=0.28)
    _edge(ax, P, "S0", "S1", "1", ls=-1, r=r)
    _edge(ax, P, "S1", "S2", "0", ls=-1, r=r)
    _edge(ax, P, "S2", "S3", "1", rad=-0.3, ls=1, r=r)
    _edge(ax, P, "S3", "S2", "0", rad=-0.3, ls=1, r=r)
    _edge(ax, P, "S3", "S4", "1", ls=-1, r=r, col=G1)
    _edge(ax, P, "S2", "S0", "0", rad=-0.5, ls=1, r=r, off=0.3)
    _edge(ax, P, "S4", "S2", "0", rad=-0.72, ls=1, r=r, off=0.3)
    _edge(ax, P, "S4", "S1", "1", rad=0.52, ls=1, r=r, off=0.3)
    return _nat(fig)


# ------------------------------------------------------------------ 7. implication table, 8 states
def impl8():
    xl, yl = (-1.0, 7.4), (-2.0, 7.2)
    fig, ax = _cv(xl, yl, 0.56)
    rows, cols = "BCDEFGH", "ABCDEFG"
    special = {("D", "A"): "BE", ("E", "B"): "AD, CF", ("F", "C"): "AD", ("H", "G"): "BG, CH"}
    keep = {("D", "A"), ("E", "B"), ("F", "C")}
    for i, rr in enumerate(rows):
        y = 6 - i
        ax.text(-0.25, y + 0.5, rr, ha="right", va="center", fontsize=10.5, weight="bold")
        for j in range(i + 1):
            cc = cols[j]
            k = (rr, cc)
            fc = "#eaf6ef" if k in keep else "white"
            ax.add_patch(Rectangle((j, y), 1, 1, fc=fc, ec=G2 if k in keep else INK, lw=1.6 if k in keep else 1.1))
            if k in special:
                bad = k == ("H", "G")
                if bad:
                    _line(ax, [j + 0.08, j + 0.92], [y + 0.08, y + 0.92], color=BAD, lw=1.2)
                ax.text(j + 0.5, y + 0.5, special[k], ha="center", va="center", fontsize=8,
                        weight="bold", color=BAD if bad else INK)
            else:
                ax.text(j + 0.5, y + 0.48, "×", ha="center", va="center", fontsize=13, color=MUTED)
    for j, cc in enumerate(cols):
        ax.text(j + 0.5, -0.35, cc, ha="center", va="center", fontsize=10.5, weight="bold")
    ax.text(3.6, 6.4, "× : outputs differ", fontsize=8.5, color=MUTED, va="center")
    ax.text(3.6, 5.6, "struck out: depends on a pair\nthat is not equivalent", fontsize=8.5, color=BAD, va="center")
    ax.text(3.5, -1.3, "Survivors: A≡D, B≡E, C≡F", ha="center", va="center", fontsize=10, weight="bold", color=G1)
    return _nat(fig)


# ------------------------------------------------------------------ 8. merger diagram
def merger5():
    xl, yl = (-3.4, 4.0), (-4.2, 2.8)
    fig, ax = _cv(xl, yl, 0.58)
    R = 2.0
    ang = {n: math.radians(90 - 72 * k) for k, n in enumerate("ABCDE")}
    P = {n: (R * math.cos(a), R * math.sin(a)) for n, a in ang.items()}
    cols = {"ABD": ACC, "ACD": G1, "ACE": G2}
    for tri, c in cols.items():
        ax.add_patch(Polygon([P[v] for v in tri], closed=True, fc=c, ec="none", alpha=0.15, zorder=1))
    for a, b in ("AB", "AC", "AD", "AE", "BD", "CD", "CE"):
        _line(ax, [P[a][0], P[b][0]], [P[a][1], P[b][1]], lw=1.6)
    for a, b in ("BC", "BE", "DE"):
        _line(ax, [P[a][0], P[b][0]], [P[a][1], P[b][1]], color=BAD, lw=0.9, ls=(0, (3, 3)))
    for n, (x, y) in P.items():
        ax.add_patch(Circle((x, y), 0.3, fc="white", ec=ACC, lw=1.5, zorder=5))
        ax.text(x, y, n, ha="center", va="center", fontsize=10, weight="bold", zorder=6)
    ax.text(0, -2.95, "maximal compatibles: (ABD) (ACD) (ACE)", ha="center", va="center", fontsize=9.5,
            color=G1, weight="bold")
    y = -3.65
    for x, nm in ((-3.0, "ABD"), (-1.8, "ACD"), (-0.6, "ACE")):
        ax.add_patch(Rectangle((x, y - 0.15), 0.3, 0.3, fc=cols[nm], ec="none", alpha=0.35))
        ax.text(x + 0.4, y, nm, ha="left", va="center", fontsize=8.5)
    _line(ax, [0.9, 1.5], [y, y], color=BAD, lw=0.9, ls=(0, (3, 3)))
    ax.text(1.6, y, "incompatible pair", ha="left", va="center", fontsize=8.5, color=BAD)
    return _nat(fig)


# ------------------------------------------------------------------ 9. the three ASM elements
def asm_boxes():
    xl, yl = (-2.4, 13.4), (-4.1, 3.0)
    fig, ax = _cv(xl, yl, 0.5)
    lab = dict(ha="center", va="top", fontsize=8.6, color=INK)
    # (a) state box
    x = 0.0
    _arrow(ax, (x, 2.0), (x, 0.6))
    _box(ax, x - 1.1, -0.6, 2.2, 1.2, "Z = 1", fc=TINT, ec=ACC, r=0.03, fs=10, weight="bold")
    ax.text(x - 1.1, 0.85, "S1", ha="left", va="center", fontsize=8.5, color=ACC, weight="bold")
    ax.text(x + 1.1, 0.85, "01", ha="right", va="center", fontsize=8.5, color=MUTED)
    _arrow(ax, (x, -0.6), (x, -2.0))
    ax.text(x, -2.4, "state box: one clock period;\nMoore outputs inside", **lab)
    # (b) decision box
    x = 5.2
    _arrow(ax, (x, 2.0), (x, 0.7))
    ax.add_patch(Polygon([(x, 0.7), (x + 1.1, 0), (x, -0.7), (x - 1.1, 0)], closed=True, fc="white", ec=INK, lw=1.4))
    ax.text(x, 0, "X", ha="center", va="center", fontsize=10, weight="bold")
    _arrow(ax, (x, -0.7), (x, -2.0))
    ax.text(x + 0.15, -1.35, "1", ha="left", va="center", fontsize=9, color=G1, weight="bold")
    _arrow(ax, (x + 1.1, 0), (x + 2.3, 0))
    ax.text(x + 1.7, 0.25, "0", ha="center", va="bottom", fontsize=9, color=G1, weight="bold")
    ax.text(x, -2.4, "decision box:\ntests an input", **lab)
    # (c) conditional output box
    x = 10.6
    _arrow(ax, (x, 2.0), (x, 0.5))
    ax.add_patch(Ellipse((x, 0), 2.4, 1.0, fc="#fdeee3", ec=G1, lw=1.5))
    ax.text(x, 0, "Z = 1", ha="center", va="center", fontsize=10, weight="bold", color=G1)
    _arrow(ax, (x, -0.5), (x, -2.0))
    ax.text(x, -2.4, "conditional output box:\nMealy output, only on this path", **lab)
    return _nat(fig)


# ------------------------------------------------------------------ 10-11. ASM charts
def _asm_state(ax, y, name, code, h, content=None):
    _box(ax, -0.9, y, 1.8, h, name if content is None else f"{name}\n{content}", fs=9.5, fc=TINT, ec=ACC, r=0.02,
         weight="bold")
    ax.text(1.0, y + h - 0.15, code, ha="left", va="center", fontsize=8, color=MUTED)


def _asm_dia(ax, yc, lab):
    ax.add_patch(Polygon([(0, yc + 0.42), (0.75, yc), (0, yc - 0.42), (-0.75, yc)], closed=True, fc="white", ec=INK, lw=1.3))
    ax.text(0, yc, lab, ha="center", va="center", fontsize=9.5, weight="bold")


def _bl(ax, x, y, t, ha="center", va="bottom"):
    ax.text(x, y, t, ha=ha, va=va, fontsize=8.8, color=G1, weight="bold")


def _dot(ax, x, y):
    ax.plot(x, y, "o", ms=3.2, color=INK, zorder=6)


def asm_1010():
    xl, yl = (-3.1, 3.7), (-11.6, 2.7)
    fig, ax = _cv(xl, yl, 0.52)
    P, h = 2.6, 0.7
    ys = [0, -P, -2 * P, -3 * P]
    for k, y in enumerate(ys):
        _asm_state(ax, y, f"S{k}", format(k, "02b"), h)
        _line(ax, [0, 0], [y, y - 0.33])
        _asm_dia(ax, y - 0.75, "X")
        if k < 3:
            _arrow(ax, (0, y - 1.17), (0, ys[k + 1] + h))
    yc = [y - 0.75 for y in ys]
    # entry to S0
    _arrow(ax, (0, 2.4), (0, h))
    # S0: 1 -> S1, 0 -> S0 entry (left)
    _bl(ax, -0.12, yc[0] - 0.8, "1", ha="right", va="center")
    _line(ax, [-0.75, -1.5, -1.5], [yc[0], yc[0], 1.2])
    _arrow(ax, (-1.5, 1.2), (0, 1.2))
    _bl(ax, -1.12, yc[0] + 0.06, "0")
    # S1: 0 -> S2, 1 -> S1 entry (right, joins S3's return)
    s1_join = ys[1] + h + 0.35
    _bl(ax, -0.12, yc[1] - 0.8, "0", ha="right", va="center")
    _line(ax, [0.75, 1.7, 1.7], [yc[1], yc[1], s1_join])
    _dot(ax, 1.7, s1_join)
    _bl(ax, 1.2, yc[1] + 0.06, "1")
    # S2: 1 -> S3, 0 -> S0 entry (far left)
    _bl(ax, -0.12, yc[2] - 0.8, "1", ha="right", va="center")
    _line(ax, [-0.75, -2.3, -2.3], [yc[2], yc[2], 1.8])
    _arrow(ax, (-2.3, 1.8), (0, 1.8))
    _bl(ax, -1.5, yc[2] + 0.06, "0")
    # S3: 1 -> S1 entry (right), 0 -> Z oval -> S2 entry
    _line(ax, [0.75, 2.4, 2.4], [yc[3], yc[3], s1_join])
    _arrow(ax, (2.4, s1_join), (0, s1_join))
    _bl(ax, 1.55, yc[3] + 0.06, "1")
    _bl(ax, -0.12, yc[3] - 0.7, "0", ha="right", va="center")
    zc = yc[3] - 1.45
    _arrow(ax, (0, yc[3] - 0.42), (0, zc + 0.42))
    ax.add_patch(Ellipse((0, zc), 1.7, 0.84, fc="#fdeee3", ec=G1, lw=1.4))
    ax.text(0, zc, "Z = 1", ha="center", va="center", fontsize=9.5, weight="bold", color=G1)
    s2_join = ys[2] + h + 0.35
    _line(ax, [0.85, 3.1, 3.1], [zc, zc, s2_join])
    _arrow(ax, (3.1, s2_join), (0, s2_join))
    ax.text(0, zc - 0.65, "conditional output box:\nZ depends on X (Mealy)", ha="center", va="top", fontsize=8, color=G1)
    return _nat(fig)


def asm_count2():
    xl, yl = (-2.7, 3.7), (-10.3, 3.0)
    fig, ax = _cv(xl, yl, 0.52)
    P, h = 3.0, 1.05
    ys = [0, -P, -2 * P, -3 * P]
    for k, y in enumerate(ys):
        _asm_state(ax, y, f"S{k}", format(k, "02b"), h, content=f"Out = {format(k, '02b')}")
    _arrow(ax, (0, 2.6), (0, h))
    top = 1.9                              # shared return line into S0's entry
    xr = [1.9, 2.5, 3.1]
    for k in range(3):
        y = ys[k]
        yc = y - 0.75
        _line(ax, [0, 0], [y, y - 0.33])
        _asm_dia(ax, yc, "E")
        _arrow(ax, (0, yc - 0.42), (0, ys[k + 1] + h))
        _bl(ax, -0.12, yc - 0.8, "1", ha="right", va="center")
        if k == 0:
            _line(ax, [-0.75, -1.5, -1.5], [yc, yc, 1.4])
            _arrow(ax, (-1.5, 1.4), (0, 1.4))
            _bl(ax, -1.12, yc + 0.06, "0")
        else:
            _line(ax, [0.75, xr[k - 1], xr[k - 1]], [yc, yc, top])
            _dot(ax, xr[k - 1], top)
            _bl(ax, 1.3, yc + 0.06, "0")
    y3 = ys[3]
    _line(ax, [0, 0, xr[2], xr[2]], [y3, y3 - 0.6, y3 - 0.6, top])
    ax.text(1.55, y3 - 0.5, "E = 0 or 1", ha="center", va="bottom", fontsize=8.2, color=G1, weight="bold")
    _arrow(ax, (xr[2], top), (0, top))
    return _nat(fig)


# ------------------------------------------------------------------ 12. serial adder
def serial_adder():
    xl, yl = (-1.4, 19.4), (-1.9, 5.6)
    fig, ax = _cv(xl, yl, 0.4)
    ax.text(4.8, 4.9, "block diagram", ha="center", va="center", fontsize=9.5, weight="bold", color=ACC)
    _box(ax, 0.3, 2.3, 1.8, 1.0, "A", fc=TINT, ec=ACC, fs=10, weight="bold")
    _box(ax, 0.3, 0.7, 1.8, 1.0, "B", fc=TINT, ec=ACC, fs=10, weight="bold")
    _box(ax, 4.6, 0.5, 2.6, 3.0, "Adder\nFSM", fc=TINT, ec=ACC, fs=10, weight="bold")
    _box(ax, 9.0, 1.5, 2.0, 1.0, "Sum\nregister", fc=TINT, ec=ACC, fs=9, weight="bold")
    _arrow(ax, (2.1, 2.8), (4.6, 2.8))
    ax.text(3.35, 3.0, "a", ha="center", va="bottom", fontsize=9.5, weight="bold", color=G1)
    _arrow(ax, (2.1, 1.2), (4.6, 1.2))
    ax.text(3.35, 1.4, "b", ha="center", va="bottom", fontsize=9.5, weight="bold", color=G1)
    _arrow(ax, (7.2, 2.0), (9.0, 2.0))
    ax.text(8.1, 2.2, "s", ha="center", va="bottom", fontsize=9.5, weight="bold", color=G1)
    # shared clock
    _line(ax, [-0.7, 10.0], [-0.6, -0.6], color=MUTED)
    ax.text(5.0, -0.35, "CLK", ha="center", va="bottom", fontsize=9, color=MUTED)
    _line(ax, [-0.7, -0.7], [-0.6, 2.8], color=MUTED)
    _arrow(ax, (-0.7, 2.8), (0.3, 2.8), color=MUTED)
    _line(ax, [-0.7, 0.0], [1.2, 1.2], color=MUTED)
    _arrow(ax, (-0.7, 1.2), (0.3, 1.2), color=MUTED)
    ax.plot(-0.7, 1.2, "o", ms=3.5, color=MUTED, zorder=6)
    for x, ytop in ((5.9, 0.5), (10.0, 1.5)):
        _arrow(ax, (x, -0.6), (x, ytop), color=MUTED)
        ax.plot(x, -0.6, "o", ms=3.5, color=MUTED, zorder=6)
    # Mealy diagram
    P = {"G": (14.0, 2.0), "H": (18.0, 2.0)}
    r = 0.78
    ax.text(16.0, 4.9, "Mealy FSM: state = carry", ha="center", va="center", fontsize=9.5, weight="bold", color=ACC)
    for n, (x, y) in P.items():
        _circ(ax, x, y, r, f"{n}\n{'carry 0' if n == 'G' else 'carry 1'}", fs=7.6)
    _reset(ax, P, "G", r=r, L=1.1)
    _loop(ax, P, "G", "00/0, 01/1, 10/1", ang=90, r=r, h=0.55, lo=0.3)
    _loop(ax, P, "H", "01/0, 10/0, 11/1", ang=90, r=r, h=0.55, lo=0.3)
    _edge(ax, P, "G", "H", "11/0", rad=-0.25, ls=1, r=r)
    _edge(ax, P, "H", "G", "00/1", rad=-0.25, ls=1, r=r)
    ax.text(16.0, -0.35, "arc label = a b / s", ha="center", va="center", fontsize=8.5, color=MUTED)
    return _nat(fig)



def mealy_1101_v2():
    """figs2.mealy_1101 with the two back arcs bent further (v1 copy had a '1/0' / '1/1' label overlap)."""
    st = {"A": (0, 0, "A"), "B": (3.3, 0, "B"), "C": (6.6, 0, "C"), "D": (9.9, 0, "D")}
    ed = [("A", "A", "0/0", 1), ("A", "B", "1/0", 0.22), ("B", "A", "0/0", 0.22), ("B", "C", "1/0", 0.0), ("C", "C", "1/0", 1),
          ("C", "D", "0/0", 0.0), ("D", "B", "1/1", 0.6), ("D", "A", "0/0", -0.45)]
    return figs1.v1.state_diagram(st, ed, size=(8.0, 3.8), lim=((-1.2, 11.1), (-3.2, 3.4)), r=0.55)

FIGS = {
    "u4_mealy_1101": mealy_1101_v2,
    "u4_chain_1101": chain_1101,
    "u4_1010": d1010,
    "u4_gray_circuit": gray_circuit,
    "u4_111": d111,
    "u4_111_timing": timing_111,
    "u4_1011_moore": moore_1011,
    "u4_impl8": impl8,
    "u4_merger5": merger5,
    "u4_asm_boxes": asm_boxes,
    "u4_asm_1010": asm_1010,
    "u4_asm_count2": asm_count2,
    "u4_serial_adder": serial_adder,
}
