"""Unit 5 figures for files 18 (logic families) and 19 (memories and PLDs) (v1.3, S8)."""
import figlib as fl
import figs1
from figs1 import ACC, BAD, G1, G2, INK, MUTED, SOFT, TINT, _arrow, _box, _line, _nat
from figs_u2 import _and, _cv, _dot, _mux, _not, _or
from figs_u2b import _cl, _pl, _t, _xor
from matplotlib.patches import Circle, Rectangle

GREEN = "#d8f0e2"


# ------------------------------------------------------------------ shared switch drawing
def _sw(ax, x, yt, yb, closed, col=INK, lw=1.5):
    """Vertical switch: contacts at (x, yt) and (x, yb). Closed = straight line, open = tilted blade."""
    if closed:
        _line(ax, [x, x], [yt, yb], color=col, lw=lw)
    else:
        _line(ax, [x, x + 0.5], [yb, yt - 0.28], color=col, lw=lw)
    for y in (yt, yb):
        ax.add_patch(Circle((x, y), 0.1, fc="white", ec=INK, lw=1.2, zorder=5))


def _gnd(ax, x, y):
    """Ground symbol; the wire ends at (x, y)."""
    for k, w in enumerate((0.5, 0.32, 0.15)):
        _line(ax, [x - w, x + w], [y - 0.16 * k] * 2)


def _zig(ax, x, y0, y1, n=6, a=0.22):
    pts = [(x, y0)]
    for k in range(n):
        yy = y0 + (y1 - y0) * (k + 0.5) / n
        pts.append((x + (a if k % 2 == 0 else -a), yy))
    pts.append((x, y1))
    _pl(ax, pts)


# ------------------------------------------------------------------ 1. propagation delay of an inverting gate
def tpd5():
    f, ax = fl.fig(7.4, 4.4)
    off = 9.0
    ax.plot([0, 9, 11, 39, 41, 60], [off, off, off + 5, off + 5, off, off], color=ACC, lw=1.7, solid_joinstyle="miter")
    ax.plot([0, 16, 18, 50, 52, 60], [5, 5, 0, 0, 5, 5], color=ACC, lw=1.7, solid_joinstyle="miter")
    for y in (off + 2.5, 2.5):
        ax.plot([0, 60], [y, y], color=MUTED, lw=0.9, ls=":")
        ax.text(60.8, y, "50 %", ha="left", va="center", fontsize=8.5, color=MUTED)
    ya = 7.0
    for x, y0 in ((10, off + 2.5), (40, off + 2.5), (17, 2.5), (51, 2.5)):
        ax.plot([x, x], [y0, ya], color=G1, lw=0.9, ls=(0, (3, 3)))
        ax.plot(x, y0, "o", ms=3.5, color=G1, zorder=5)
    for a, b, s in ((10, 17, "t_PHL = 7 ns"), (40, 51, "t_PLH = 11 ns")):
        ax.annotate("", xy=(b, ya), xytext=(a, ya),
                    arrowprops=dict(arrowstyle="<->", color=BAD, lw=1.4, shrinkA=0, shrinkB=0))
        ax.text(b + 0.9, ya, s, ha="left", va="center", fontsize=9.5, color=BAD, weight="bold")
    ax.set_xlim(0, 60)
    ax.set_ylim(-1.0, 15.0)
    ax.set_xticks(range(0, 61, 10))
    ax.set_yticks([0, 5, off, off + 5])
    ax.set_yticklabels(["0", "5", "0", "5"], fontsize=8.5)
    for nm, y in (("OUT", 2.5), ("IN", off + 2.5)):
        ax.annotate(nm, xy=(-0.075, y), xycoords=("axes fraction", "data"), ha="right", va="center",
                    fontsize=9.5, weight="bold")
    ax.set_xlabel("time (ns)")
    ax.set_ylabel("voltage (V)", labelpad=18)
    return fl.svg(f)


# ------------------------------------------------------------------ 2. rise and fall time
def rise_fall():
    f, ax = fl.fig(7.4, 3.5)
    ax.plot([0, 10, 15, 40, 47.5, 55], [0, 0, 5, 5, 0, 0], color=ACC, lw=1.8, solid_joinstyle="miter")
    for y, s in ((0.5, "10 % (0.5 V)"), (4.5, "90 % (4.5 V)")):
        ax.plot([0, 55], [y, y], color=MUTED, lw=0.9, ls=(0, (4, 3)))
        ax.text(55.8, y, s, ha="left", va="center", fontsize=9, color=MUTED)
    for x, y in ((10.5, 0.5), (14.5, 4.5), (40.75, 4.5), (46.75, 0.5)):
        ax.plot([x, x], [0, y], color=G1, lw=0.9, ls=":")
        ax.plot(x, y, "o", ms=5, color=G1, zorder=5)
    ya = 0.27
    for a, b in ((10.5, 14.5), (40.75, 46.75)):
        ax.annotate("", xy=(b, ya), xytext=(a, ya),
                    arrowprops=dict(arrowstyle="<->", color=BAD, lw=1.4, shrinkA=0, shrinkB=0))
    ax.text(15.0, ya, "t_r = 4 ns", ha="left", va="center", fontsize=9.5, color=BAD, weight="bold")
    ax.text(40.3, ya, "t_f = 6 ns", ha="right", va="center", fontsize=9.5, color=BAD, weight="bold")
    ax.set_xlim(0, 55)
    ax.set_ylim(0, 5.5)
    ax.set_xticks(range(0, 56, 5))
    ax.set_yticks(range(0, 6))
    fl.axes(ax, "time (ns)", "voltage (V)")
    return fl.svg(f)


# ------------------------------------------------------------------ 3. TTL noise margins
def noise_ttl():
    f, ax = fl.fig(7.4, 4.6)
    L0, R0, W = 1.0, 6.6, 2.4

    def band(x0, lo, hi, txt, hatch=False, bold=True):
        if hatch:
            ax.add_patch(Rectangle((x0, lo), W, hi - lo, fc=SOFT, ec=MUTED, lw=1.0, hatch="///"))
            ax.text(x0 + W / 2, (lo + hi) / 2, txt, ha="center", va="center", fontsize=9, color=INK,
                    bbox=dict(fc="white", ec="none", pad=1.5))
        else:
            ax.add_patch(Rectangle((x0, lo), W, hi - lo, fc=GREEN, ec=INK, lw=1.2))
            ax.text(x0 + W / 2, (lo + hi) / 2, txt, ha="center", va="center", fontsize=9, weight="bold", color=G2)

    band(L0, 2.4, 5.0, "HIGH")
    band(L0, 0.4, 2.4, "never output", hatch=True)
    band(L0, 0.0, 0.4, "LOW")
    band(R0, 2.0, 5.0, "read as HIGH")
    band(R0, 0.8, 2.0, "not defined", hatch=True)
    band(R0, 0.0, 0.8, "read as LOW")
    ax.text(L0 + W / 2, 5.2, "output (guaranteed)", ha="center", va="bottom", fontsize=10, weight="bold")
    ax.text(R0 + W / 2, 5.2, "input (accepted)", ha="center", va="bottom", fontsize=10, weight="bold")
    xm = 5.0
    gk = dict(color=MUTED, lw=0.9, ls=(0, (3, 3)))
    ax.plot([L0 + W, xm], [2.4, 2.4], **gk)
    ax.plot([xm, R0], [2.0, 2.0], **gk)
    ax.plot([L0 + W, xm], [0.4, 0.4], **gk)
    ax.plot([xm, R0], [0.8, 0.8], **gk)
    for a, b, ya, lab in ((2.4, 2.0, 2.9, "NM_H = 0.4 V"), (0.4, 0.8, 1.35, "NM_L = 0.4 V")):
        ax.annotate("", xy=(xm, b), xytext=(xm, a),
                    arrowprops=dict(arrowstyle="<->", color=BAD, lw=1.5, shrinkA=0, shrinkB=0))
        top = max(a, b)
        ax.plot([xm, xm], [top, ya - 0.05], color=BAD, lw=0.9)
        ax.text(xm, ya, lab, ha="center", va="bottom", fontsize=9.5, color=BAD, weight="bold")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.7)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.set_yticks([0, 0.4, 0.8, 2.0, 2.4, 5])
    ax.set_yticklabels(["0", "0.4", "0.8", "2.0", "2.4", "5"])
    ax.set_ylabel("voltage (V)")
    return fl.svg(f)


# ------------------------------------------------------------------ 4. fan-out
def _fan(ax, ox, low):
    _t(ax, ox + 5.6, 7.3, "output LOW: driver sinks" if low else "output HIGH: driver sources",
       fs=10, weight="bold", color=INK)
    yd = 3.4
    _box(ax, ox, yd - 0.8, 1.6, 1.6, "driver", fc=TINT, ec=ACC, fs=9.5, r=0.1)
    xb, xl = ox + 5.0, ox + 8.8
    _line(ax, [ox + 1.6, xb], [yd, yd])
    ys = (5.8, 4.0, 1.0)
    _line(ax, [xb, xb], [ys[2], ys[0]])
    _dot(ax, xb, yd)
    for y, nm in zip(ys, ("load 1", "load 2", "load N")):
        _line(ax, [xb, xl], [y, y])
        _dot(ax, xb, y)
        _box(ax, xl, y - 0.45, 2.0, 0.9, nm, fc=SOFT, ec=INK, fs=9, r=0.08)
        if low:
            _arrow(ax, (ox + 7.6, y), (ox + 6.2, y), color=G1, lw=1.8)
        else:
            _arrow(ax, (ox + 6.2, y), (ox + 7.6, y), color=G1, lw=1.8)
        _t(ax, ox + 6.9, y + 0.38, "I_IL = 1.6 mA" if low else "I_IH = 40 µA", fs=8.5, color=G1, weight="bold",
           va="bottom")
    _t(ax, xl + 1.0, 2.5, "⋮", fs=13, color=MUTED)
    if low:
        _arrow(ax, (ox + 4.4, yd), (ox + 2.0, yd), color=BAD, lw=1.8)
    else:
        _arrow(ax, (ox + 2.0, yd), (ox + 4.4, yd), color=BAD, lw=1.8)
    _t(ax, ox + 3.2, yd + 0.38, "I_OL ≤ 16 mA" if low else "I_OH ≤ 0.4 mA", fs=8.5, color=BAD, weight="bold",
       va="bottom")


def fanout():
    fig, ax = _cv((-0.4, 23.8), (0.1, 7.9), 0.31)
    _fan(ax, 0.0, True)
    _fan(ax, 12.4, False)
    return _nat(fig)


# ------------------------------------------------------------------ 5. CMOS inverter as two switches
def _inv_panel(ax, ox, a1):
    _t(ax, ox + 7.0, 8.7, "A = 1" if a1 else "A = 0", fs=11, weight="bold", color=ACC)
    x = ox + 6.6
    _line(ax, [x - 1.0, x + 1.0], [7.6, 7.6], lw=2.2)
    _t(ax, x + 1.2, 7.6, "V_DD", fs=10, ha="left", weight="bold")
    _line(ax, [x, x], [7.6, 6.6])
    _sw(ax, x, 6.6, 5.0, closed=not a1)
    _line(ax, [x, x], [5.0, 3.8])
    _dot(ax, x, 3.8)
    _sw(ax, x, 3.8, 2.2, closed=a1)
    _line(ax, [x, x], [2.2, 1.2])
    _gnd(ax, x, 1.2)
    _t(ax, x + 1.0, 1.0, "0 V (ground)", fs=9, ha="left", color=MUTED)
    _t(ax, x - 0.9, 5.8, "pMOS (on when A = 0)", fs=9, ha="right")
    _t(ax, x - 0.9, 3.0, "nMOS (on when A = 1)", fs=9, ha="right")
    _line(ax, [x, x + 3.0], [3.8, 3.8])
    _t(ax, x + 0.5, 4.15, "X", fs=9.5, weight="bold", color=ACC, ha="left", va="bottom")
    _t(ax, x + 3.2, 3.8, "X = 0 V (0)" if a1 else "X = V_DD (1)", fs=10, weight="bold", color=G2 if not a1 else MUTED,
       ha="left")


def cmos_sw():
    fig, ax = _cv((-0.2, 26.6), (0.3, 9.3), 0.28)
    _inv_panel(ax, 0.0, False)
    _inv_panel(ax, 13.4, True)
    return _nat(fig)


# ------------------------------------------------------------------ 6. CMOS NAND / NOR structure
def _pair(ax, xm, ytop, par, tag, names):
    """Two switches between (xm, ytop) and the lower node. Returns the y of the lower node."""
    if par:
        xa, xb = xm - 1.0, xm + 1.0
        _line(ax, [xm, xm], [ytop, ytop - 0.4])
        _line(ax, [xa, xb], [ytop - 0.4, ytop - 0.4])
        _dot(ax, xm, ytop - 0.4)
        for x in (xa, xb):
            _line(ax, [x, x], [ytop - 0.4, ytop - 0.8])
            _sw(ax, x, ytop - 0.8, ytop - 2.2, closed=False)
            _line(ax, [x, x], [ytop - 2.2, ytop - 2.6])
        _line(ax, [xa, xb], [ytop - 2.6, ytop - 2.6])
        _dot(ax, xm, ytop - 2.6)
        _line(ax, [xm, xm], [ytop - 2.6, ytop - 3.0])
        _t(ax, xa - 0.4, ytop - 1.5, f"{names[0]} ({tag})", fs=9, ha="right", weight="bold")
        _t(ax, xb + 0.85, ytop - 1.5, f"{names[1]} ({tag})", fs=9, ha="left", weight="bold")
        return ytop - 3.0
    _line(ax, [xm, xm], [ytop, ytop - 0.6])
    _sw(ax, xm, ytop - 0.6, ytop - 2.0, closed=False)
    _line(ax, [xm, xm], [ytop - 2.0, ytop - 2.4])
    _sw(ax, xm, ytop - 2.4, ytop - 3.8, closed=False)
    _line(ax, [xm, xm], [ytop - 3.8, ytop - 4.4])
    _t(ax, xm - 0.5, ytop - 1.3, f"{names[0]} ({tag})", fs=9, ha="right", weight="bold")
    _t(ax, xm - 0.5, ytop - 3.1, f"{names[1]} ({tag})", fs=9, ha="right", weight="bold")
    return ytop - 4.4


def _cmos2(ax, ox, title, up_par):
    xm = ox + 6.6
    _t(ax, xm, 12.0, title, fs=11, weight="bold", color=ACC)
    ytop = 11.0
    _line(ax, [xm - 1.4, xm + 1.4], [ytop, ytop], lw=2.2)
    _t(ax, xm + 1.6, ytop, "V_DD", fs=10, ha="left", weight="bold")
    yx = _pair(ax, xm, ytop, up_par, "p", ("A", "B"))
    # output node X
    _dot(ax, xm, yx)
    _line(ax, [xm, xm + 3.0], [yx, yx])
    _t(ax, xm + 3.2, yx, "X", fs=10.5, ha="left", weight="bold", color=ACC)
    ylo = _pair(ax, xm, yx, not up_par, "n", ("A", "B"))
    _gnd(ax, xm, ylo)
    _t(ax, xm + 1.0, ylo - 0.15, "0 V", fs=9, ha="left", color=MUTED)
    _t(ax, xm - 4.6, ytop - 2.0, "pull-up (pMOS)", fs=8.5, ha="right", color=MUTED)
    _t(ax, xm - 4.6, yx - 2.0, "pull-down (nMOS)", fs=8.5, ha="right", color=MUTED)


def cmos_nand_nor():
    fig, ax = _cv((-0.6, 25.8), (-0.2, 12.6), 0.285)
    _cmos2(ax, 0.0, "(a) NAND", True)
    _cmos2(ax, 13.0, "(b) NOR", False)
    return _nat(fig)


# ------------------------------------------------------------------ 7. totem-pole vs open-collector
def totem_oc():
    fig, ax = _cv((-0.8, 24.2), (-0.2, 9.8), 0.3)
    # (a)
    _t(ax, 5.0, 9.2, "(a) two totem-pole outputs joined", fs=10, weight="bold", color=ACC)
    x1, x2 = 2.4, 7.4
    _line(ax, [1.6, 8.2], [8.0, 8.0], lw=2.2)
    _t(ax, 1.4, 8.0, "+5 V", fs=9.5, ha="right", weight="bold")
    for x, up, lab in ((x1, True, "gate 1 (output HIGH)"), (x2, False, "gate 2 (output LOW)")):
        _line(ax, [x, x], [8.0, 7.2])
        _sw(ax, x, 7.2, 5.8, closed=up)
        _line(ax, [x, x], [5.8, 5.2])
        _sw(ax, x, 4.6, 3.2, closed=not up)
        _line(ax, [x, x], [3.2, 2.6])
        _gnd(ax, x, 2.6)
        _t(ax, x, 1.7, lab, fs=9)
    _line(ax, [x1, x2], [5.2, 5.2])
    _dot(ax, x1, 5.2)
    _dot(ax, x2, 5.2)
    _line(ax, [x2, x2 + 1.2], [5.2, 5.2])
    _t(ax, x2 + 1.35, 5.2, "tied output", fs=8.5, ha="left", color=MUTED)
    red = [(x1, 8.0), (x1, 5.2), (x2, 5.2), (x2, 2.6)]
    _line(ax, [p[0] for p in red], [p[1] for p in red], color=BAD, lw=3.2)
    _arrow(ax, (x1, 6.8), (x1, 6.3), color=BAD, lw=3.2, head=11)
    _arrow(ax, ((x1 + x2) / 2 - 0.4, 5.2), ((x1 + x2) / 2 + 0.4, 5.2), color=BAD, lw=3.2, head=11)
    _arrow(ax, (x2, 4.3), (x2, 3.7), color=BAD, lw=3.2, head=11)
    _t(ax, (x1 + x2) / 2, 6.3, "large current", fs=9.5, weight="bold", color=BAD)
    # (b)
    ox = 12.8
    _t(ax, ox + 5.0, 9.2, "(b) open-collector outputs + pull-up", fs=10, weight="bold", color=ACC)
    xr, g1, g2 = ox + 1.6, ox + 4.6, ox + 7.4
    _line(ax, [ox + 0.8, ox + 8.2], [8.0, 8.0], lw=2.2)
    _t(ax, ox + 0.6, 8.0, "+5 V", fs=9.5, ha="right", weight="bold")
    _line(ax, [xr, xr], [8.0, 7.5])
    _zig(ax, xr, 7.5, 6.3)
    _line(ax, [xr, xr], [6.3, 5.8])
    _t(ax, xr + 0.5, 6.9, "R", fs=10, ha="left", weight="bold")
    _line(ax, [xr, ox + 9.0], [5.8, 5.8])
    _dot(ax, xr, 5.8)
    _t(ax, ox + 9.2, 5.8, "Y", fs=11, ha="left", weight="bold", color=ACC)
    for x, nm in ((g1, "gate 1"), (g2, "gate 2")):
        _dot(ax, x, 5.8)
        _line(ax, [x, x], [5.8, 5.2])
        _sw(ax, x, 5.2, 3.8, closed=False)
        _line(ax, [x, x], [3.8, 3.0])
        _gnd(ax, x, 3.0)
        _t(ax, x, 2.1, nm, fs=9)
    _t(ax, ox + 4.6, 0.7, "Y = 0 if any switch is on (wired-AND)", fs=9.5, weight="bold", color=G2)
    return _nat(fig)


# ------------------------------------------------------------------ 8. ROM 8 x 4
def _x(ax, x, y, s=0.2):
    ax.plot([x - s, x + s], [y - s, y + s], color=ACC, lw=2.0, solid_capstyle="round", zorder=6)
    ax.plot([x - s, x + s], [y + s, y - s], color=ACC, lw=2.0, solid_capstyle="round", zorder=6)


def rom8x4():
    fig, ax = _cv((-2.6, 16.2), (1.2, 12.9), 0.4)
    ys = [11.5 - k for k in range(8)]
    _box(ax, 0.6, ys[7] - 0.5, 2.6, ys[0] - ys[7] + 1.0, "3-to-8\ndecoder", fc=TINT, ec=ACC, fs=9.5, r=0.1, weight="bold")
    mid = (ys[0] + ys[7]) / 2
    for nm, y in zip(("A₂", "A₁", "A₀"), (mid + 1.2, mid, mid - 1.2)):
        _arrow(ax, (-0.8, y), (0.6, y))
        _t(ax, -1.0, y, nm, fs=10, ha="right", weight="bold")
    xv = (6.0, 8.2, 10.4, 12.6)
    for k, y in enumerate(ys):
        _line(ax, [3.2, 13.4], [y, y], color=INK, lw=1.2)
        _t(ax, 3.45, y + 0.05, f"D{k}", fs=8.5, ha="left", va="bottom", color=MUTED, weight="bold")
    gy = 2.3
    marks = {"F3": (2, 5, 7), "F2": (0, 7), "F1": (1, 4), "F0": (1, 5, 7)}
    for x, (nm, ks) in zip(xv, marks.items()):
        _line(ax, [x, x], [ys[0] + 0.55, gy + 0.43], color=G1, lw=1.4)
        _or(ax, x - 0.3, gy, 1.0, 0.9)
        _arrow(ax, (x + 0.7, gy), (x + 1.2, gy))
        _t(ax, x + 1.3, gy, nm, fs=10.5, ha="left", weight="bold", color=ACC)
        for k in ks:
            _x(ax, x, ys[k])
    return _nat(fig)


# ------------------------------------------------------------------ 9. PLA
def _orn(ax, x, yc, w, h, ys, xs_in):
    """OR gate with len(ys) input wires from xs_in to its back curve."""
    _or(ax, x, yc, w, h)
    for y in ys:
        t = (1 + 2 * (y - yc) / h) / 2
        xe = x + 0.6 * w * t * (1 - t)
        _line(ax, [xs_in, xe], [y, y])
    return (x + w, yc)


def _inputs(ax, xs, names, ytop, yj, nw=0.3):
    """Input labels with a plain rail and an inverted rail beside it. xs = list of (x_true, x_comp)."""
    for (xa, xb), nm in zip(xs, names):
        _t(ax, xa, ytop + 0.35, nm, fs=10.5, weight="bold", color=ACC)
        _line(ax, [xa, xa], [ytop, yj])
        _dot(ax, xa, yj)
        _line(ax, [xa, xa + nw], [yj, yj])
        _, out = _not(ax, xa + nw, yj)
        _line(ax, [out[0], xb], [yj, yj])


def pla():
    fig, ax = _cv((-3.4, 24.6), (-0.6, 13.9), 0.265)
    rx = {"A": 1.0, "A'": 2.3, "B": 3.9, "B'": 5.2, "C": 6.8, "C'": 8.1}
    _inputs(ax, [(1.0, 2.3), (3.9, 5.2), (6.8, 8.1)], "ABC", 13.1, 12.2, 0.3)
    yt = [10.2, 9.1, 8.0, 6.9]
    ybot = 5.9
    for nm, x in rx.items():
        _line(ax, [x, x], [12.2, ybot])
        _t(ax, x, ybot - 0.4, nm, fs=9.5, weight="bold", color=INK)
    labs = ["1: AB", "2: AC", "3: BC", "4: A'B'C'"]
    uses = [("A", "B"), ("A", "C"), ("B", "C"), ("A'", "B'", "C'")]
    outs = []
    for y, lb, us in zip(yt, labs, uses):
        _line(ax, [0.2, 9.3], [y, y])
        _t(ax, 0.0, y, lb, fs=9, ha="right", weight="bold")
        _, _, o = _and(ax, 9.3, y, 1.2, 0.7)
        outs.append(o)
        for u in us:
            _x(ax, rx[u], y, 0.17)
    xv2, xv1 = 11.8, 13.2
    for y in yt:
        _line(ax, [10.5, 13.9], [y, y])
    g1, g2 = 4.4, 1.4
    _line(ax, [xv1, xv1], [yt[0] + 0.45, g1 + 0.6], color=G1)
    _line(ax, [xv2, xv2], [yt[0] + 0.45, g2 + 0.6], color=G1)
    for i in (0, 1, 2):
        _x(ax, xv1, yt[i], 0.17)
    for i in (0, 1, 3):
        _x(ax, xv2, yt[i], 0.17)
    for (xv, yg, nm, const, desc, lab) in ((xv1, g1, "OR 1", "1", "fuse blown → 1: output inverted",
                                            "F₁ = (AB + AC + BC)'"),
                                           (xv2, g2, "OR 2", "0", "fuse intact → 0", "F₂ = AB + AC + A'B'C'")):
        _or(ax, xv - 0.35, yg, 1.2, 1.2)
        _t(ax, xv + 0.25, yg - 0.95, nm, fs=8.5, color=MUTED, weight="bold")
        xo = xv - 0.35 + 1.2
        xg = 15.5
        _, _, o = _xor(ax, xg, yg, 1.2, 1.2)
        _pl(ax, [(xo, yg), (xg - 0.35, yg), (xg - 0.35, yg + 0.3), (xg + 0.135, yg + 0.3)])
        _pl(ax, [(xg + 0.135, yg - 0.3), (xg - 0.15, yg - 0.3), (xg - 0.15, yg - 1.0)])
        _t(ax, xg - 0.15, yg - 1.25, const, fs=10, weight="bold", color=G1 if const == "1" else MUTED)
        _t(ax, xg + 0.3, yg - 1.25, desc, fs=8.5, ha="left", color=MUTED)
        _arrow(ax, o, (o[0] + 0.7, yg))
        _t(ax, o[0] + 0.85, yg, lab, fs=9.5, ha="left", weight="bold", color=ACC)
    return _nat(fig)


# ------------------------------------------------------------------ 10. PAL with feedback
def pal():
    fig, ax = _cv((-3.6, 23.6), (0.6, 14.6), 0.275)
    names = ["A", "A'", "B", "B'", "C", "C'", "D", "D'", "w", "w'"]
    rx = dict(zip(names, (1.0, 2.2, 3.5, 4.7, 6.0, 7.2, 8.5, 9.7, 11.0, 12.2)))
    _inputs(ax, [(1.0, 2.2), (3.5, 4.7), (6.0, 7.2), (8.5, 9.7)], "ABCD", 13.9, 12.9, 0.2)
    yj = 12.9
    # w / w' from the feedback wire
    _dot(ax, 11.0, yj)
    _line(ax, [11.0, 11.2], [yj, yj])
    _, out = _not(ax, 11.2, yj)
    _line(ax, [out[0], 12.2], [yj, yj])
    ymap = {}
    for g in range(4):
        for j in range(3):
            ymap[3 * g + j + 1] = 11.8 - 0.75 * (3 * g + j) - 0.35 * g
    ybot = ymap[12] - 0.5
    for nm, x in rx.items():
        _line(ax, [x, x], [yj, ybot])
        _t(ax, x, ybot - 0.4, nm, fs=9, weight="bold")
    marks = {1: ("A", "B", "C'"), 2: ("A'", "B'", "C", "D'"), 4: ("A",), 5: ("B", "C", "D"),
             7: ("A'", "B"), 8: ("C", "D"), 9: ("B'", "D'"), 10: ("w",), 11: ("A", "C'", "D'"),
             12: ("A'", "B'", "C'", "D")}
    prod = {1: "ABC'", 2: "A'B'CD'", 4: "A", 5: "BCD", 7: "A'B", 8: "CD", 9: "B'D'", 10: "w", 11: "AC'D'",
            12: "A'B'C'D"}
    for k, y in ymap.items():
        _line(ax, [0.4, 13.4], [y, y])
        _and(ax, 13.4, y, 1.0, 0.55)
        if k in marks:
            _t(ax, 0.2, y, str(k), fs=8.5, ha="right", color=MUTED)
            for u in marks[k]:
                _x(ax, rx[u], y, 0.16)
            _t(ax, 14.55, y + 0.15, prod[k], fs=7.5, ha="left", va="bottom", color=MUTED)
        else:
            _t(ax, 0.2, y, f"{k}: unused (= 0)", fs=8.5, ha="right", color=MUTED)
    outn = ("w", "x", "y", "z")
    for g in range(4):
        ks = (3 * g + 1, 3 * g + 2, 3 * g + 3)
        yc = ymap[ks[1]]
        xo = 17.0
        for k in ks:
            _line(ax, [14.4, 16.9], [ymap[k], ymap[k]])
        o = _orn(ax, xo, yc, 1.1, 2.0, [ymap[k] for k in ks], 14.4)
        _arrow(ax, o, (o[0] + 1.0, yc))
        _t(ax, o[0] + 1.15, yc, outn[g], fs=10.5, ha="left", weight="bold", color=ACC)
        if g == 0:
            xf = o[0] + 0.45
            _dot(ax, xf, yc)
            _line(ax, [xf, xf, 11.0], [yc, 14.2, 14.2])
            _arrow(ax, (11.0, 14.2), (11.0, yj + 0.05))
            _t(ax, 14.6, 14.4, "feedback", fs=8.5, color=MUTED, va="bottom")
    return _nat(fig)


# ------------------------------------------------------------------ 11. PLD architectures
def pld_types():
    fig, ax = _cv((-2.4, 14.2), (-1.3, 6.4), 0.46)
    rows = (("PROM", 5.0, False, True), ("PAL", 2.9, True, False), ("PLA", 0.8, True, True))
    for nm, y, a_prog, o_prog in rows:
        _t(ax, -0.2, y + 0.6, nm, fs=11, ha="right", weight="bold")
        _arrow(ax, (1.0, y + 0.6), (2.6, y + 0.6))
        _t(ax, 1.8, y + 0.8, "inputs", fs=8.5, va="bottom", color=MUTED)
        if a_prog:
            _box(ax, 2.6, y, 3.8, 1.2, "AND array\n(programmable)", fc=TINT, ec=ACC, fs=8.5, r=0.1, weight="bold", color=ACC)
        else:
            _box(ax, 2.6, y, 3.8, 1.2, "AND array\n(fixed: decoder)", fc=SOFT, ec=MUTED, fs=8.5, r=0.1, color=MUTED)
        _arrow(ax, (6.4, y + 0.6), (7.6, y + 0.6))
        if o_prog:
            _box(ax, 7.6, y, 3.8, 1.2, "OR array\n(programmable)", fc=TINT, ec=ACC, fs=8.5, r=0.1, weight="bold", color=ACC)
        else:
            _box(ax, 7.6, y, 3.8, 1.2, "OR array\n(fixed)", fc=SOFT, ec=MUTED, fs=8.5, r=0.1, color=MUTED)
        _arrow(ax, (11.4, y + 0.6), (12.8, y + 0.6))
        _t(ax, 12.1, y + 0.8, "outputs", fs=8.5, va="bottom", color=MUTED)
    ax.add_patch(Rectangle((2.6, -0.85), 0.5, 0.35, fc=TINT, ec=ACC, lw=1.2))
    ax.add_patch(Rectangle((3.25, -0.85), 0.5, 0.35, fc=SOFT, ec=MUTED, lw=1.2))
    _t(ax, 3.95, -0.67, "coloured = programmable, grey = fixed", fs=8.5, ha="left", color=MUTED)
    return _nat(fig)


FIGS = {
    "u5_tpd": tpd5,
    "u5_rise_fall": rise_fall,
    "u5_noise_ttl": noise_ttl,
    "u5_fanout": fanout,
    "u5_cmos_sw": cmos_sw,
    "u5_cmos_nand_nor": cmos_nand_nor,
    "u5_totem_oc": totem_oc,
    "u5_rom8x4": rom8x4,
    "u5_pla": pla,
    "u5_pal": pal,
    "u5_pld_types": pld_types,
}
