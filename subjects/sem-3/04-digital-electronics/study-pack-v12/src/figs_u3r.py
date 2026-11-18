"""Unit 3 register figures for file 11 and timing-analysis figures for file 14 (v1.3, S7)."""
import figlib as fl
import figs1
from figs1 import ACC, BAD, G1, G2, INK, MUTED, SOFT, TINT, _arrow, _box, _line, _nat
from figs_u2 import _and, _cv, _dot, _mux, _not, _or
from figs_u2b import _cl, _pl, _t
from figs_u3c import state_ring
from matplotlib.patches import Circle, Polygon, Rectangle

LBL = "#6a707a"


# ------------------------------------------------------------------ flip-flop box helper
def _ff(ax, x, y, w=1.8, h=1.8, dy=None, clk="bottom", cy=0.5, cx=None, name=None, fs=9):
    """D flip-flop box. Returns pin points D, Q, C (clock)."""
    dy = h / 2 if dy is None else dy
    _box(ax, x, y, w, h, "", ec=ACC, r=0.05)
    ax.text(x + 0.15, y + dy, "D", va="center", fontsize=fs, weight="bold")
    ax.text(x + w - 0.15, y + dy, "Q", ha="right", va="center", fontsize=fs, weight="bold")
    pins = {"D": (x, y + dy), "Q": (x + w, y + dy)}
    if clk == "bottom":
        c = x + (w / 2 if cx is None else cx)
        ax.add_patch(Polygon([(c - 0.2, y), (c, y + 0.28), (c + 0.2, y)], closed=True, fc="none", ec=INK, lw=1.1))
        pins["C"] = (c, y)
    elif clk == "left":
        yy = y + cy
        ax.add_patch(Polygon([(x, yy - 0.2), (x + 0.28, yy), (x, yy + 0.2)], closed=True, fc="none", ec=INK, lw=1.1))
        pins["C"] = (x, yy)
    if name:
        ax.text(x + w / 2, y + h + 0.3, name, ha="center", va="center", fontsize=9, color=ACC, weight="bold")
    return pins


def _bub(ax, x, y):
    ax.add_patch(Circle((x, y), 0.11, fc="white", ec=INK, lw=1.1, zorder=4))


# ------------------------------------------------------------------ 1. 4-bit parallel register
def reg4():
    fig, ax = _cv((-4.3, 4.4), (-1.9, 9.6), 0.36)
    xc = -1.3
    cys = []
    for i in range(4):
        y = (3 - i) * 2.4
        p = _ff(ax, 0, y, 1.8, 1.6, dy=1.15, clk="left", cy=0.45, name=f"FF{i}")
        _arrow(ax, (-3.1, p["D"][1]), p["D"])
        _cl(ax, -3.2, p["D"][1], "D" + "₀₁₂₃"[i], ha="right", fs=10)
        _arrow(ax, p["Q"], (3.1, p["Q"][1]))
        _cl(ax, 3.2, p["Q"][1], "Q" + "₀₁₂₃"[i], ha="left", color=ACC, fs=10)
        cys.append(p["C"][1])
        _line(ax, [xc, 0], [p["C"][1], p["C"][1]], color=MUTED, lw=1.4)
        _dot(ax, xc, p["C"][1])
    _line(ax, [xc, xc], [-0.9, cys[0]], color=MUTED, lw=1.4)
    _cl(ax, xc, -1.05, "CLK", va="top", color=MUTED, fs=9.5)
    return _nat(fig)


# ------------------------------------------------------------------ 2. SIPO waveforms
def _step(ax, pts, y0, h, xmax, color, lw=1.6):
    xs, ys = [], []
    for k, (t, v) in enumerate(pts):
        if k:
            xs.append(t); ys.append(ys[-1])
        xs.append(t); ys.append(v)
    xs.append(xmax); ys.append(ys[-1])
    ax.plot(xs, [y0 + h * v for v in ys], color=color, lw=lw, solid_joinstyle="miter")


def sipo_waves():
    f, ax = fl.fig(7.4, 3.6)
    ax.set_xlim(-0.95, 4.95); ax.set_ylim(-1.0, 6.3); ax.axis("off")
    xmax = 4.9
    clk = [(0, 0)] + [p for t in (1, 2, 3, 4) for p in ((t, 1), (t + 0.5, 0))]
    rows = [("CLK", clk, MUTED), ("Serial in", [(0, 0), (0.5, 1), (2.5, 0), (3.5, 1), (4.5, 0)], G1),
            ("Q₀", [(0, 0), (1, 1), (3, 0), (4, 1)], ACC), ("Q₁", [(0, 0), (2, 1), (4, 0)], ACC),
            ("Q₂", [(0, 0), (3, 1)], ACC), ("Q₃", [(0, 0), (4, 1)], ACC)]
    for i, (nm, pts, col) in enumerate(rows):
        y0 = 5.0 - i * 1.0
        ax.text(-0.1, y0 + 0.3, nm, ha="right", va="center", fontsize=9.5, weight="bold" if nm != "CLK" else "normal")
        _step(ax, pts, y0, 0.6, xmax, col)
    for t in (1, 2, 3, 4):
        ax.plot([t, t], [-0.1, 5.85], color=G2, lw=0.9, ls=(0, (3, 3)))
    words = ("1000", "1100", "0110", "1011")
    ax.text(-0.1, -0.45, "Q₀Q₁Q₂Q₃", ha="right", va="center", fontsize=9, color=MUTED)
    for t, wd in zip((1, 2, 3, 4), words):
        ax.text(t, -0.45, wd, ha="center", va="center", fontsize=10, weight="bold", color=G2)
    return fl.svg(f)


# ------------------------------------------------------------------ 3. PISO register
def piso():
    P, w, h = 7.4, 1.8, 1.8
    fig, ax = _cv((-11.6, 3 * P + w + 4.4), (-3.3, 6.7), 0.23)
    SH, SHN, DT = 4.8, 3.8, 5.9
    xs = [i * P for i in range(4)]
    # control line and inverter
    _line(ax, [-7.0, xs[3] - 3.9], [SH, SH])
    _t(ax, -7.2, SH, "SHIFT/LOAD'", fs=9, weight="bold", color=G1, ha="right", va="center")
    xt = -6.3
    _dot(ax, xt, SH)
    _pl(ax, [(xt, SH), (xt, SHN), (-5.9, SHN)])
    _, nout = _not(ax, -5.9, SHN)
    _line(ax, [nout[0], xs[3] - 3.4], [SHN, SHN])
    _t(ax, -4.2, SHN + 0.15, "SHIFT'", fs=8.5, color=MUTED, va="bottom")
    # clock bus
    yclk = -1.7
    _line(ax, [-6.2, xs[3] + 0.9], [yclk, yclk], color=MUTED, lw=1.4)
    _t(ax, -6.3, yclk, "CLK", fs=9, color=MUTED, ha="right")
    for i, x0 in enumerate(xs):
        p = _ff(ax, x0, 0, w, h, dy=0.9, clk="bottom", name=f"FF{i}")
        _line(ax, [p["C"][0]] * 2, [yclk, 0], color=MUTED, lw=1.4)
        _dot(ax, p["C"][0], yclk, col=MUTED)
        _t(ax, x0 + w + 0.2, 1.2, "Q" + "₀₁₂₃"[i], fs=9, weight="bold", color=ACC, ha="left", va="bottom")
        # parallel input label
        xd = x0 - (3.2 if i == 0 else 4.4)
        _line(ax, [xd, xd], [DT - 0.05, 0.7 if i == 0 else 1.7])
        _t(ax, xd, DT, "D" + "₀₁₂₃"[i], fs=9.5, weight="bold", va="bottom")
        xsn = x0 - (2.7 if i == 0 else 3.4)       # SHIFT' drop
        _dot(ax, xsn, SHN)
        if i == 0:
            xa = x0 - 2.2
            th, tl, to = _and(ax, xa, 0.9, 1.0, 0.8)
            _pl(ax, [(xsn, SHN), (xsn, th[1]), th])
            _pl(ax, [(xd, tl[1]), tl])
            _arrow(ax, to, (x0, 0.9))
        else:
            xa = x0 - 3.0
            xo = x0 - 1.6
            th, tl, to = _and(ax, xa, 1.9, 1.0, 0.8)           # SHIFT' . D_i
            bh, bl, bo = _and(ax, xa, -0.1, 1.0, 0.8)          # SHIFT . Q_(i-1)
            oh, ol, oo = _or(ax, xo, 0.9, 0.9, 0.9)
            _pl(ax, [(xsn, SHN), (xsn, th[1]), th])
            _pl(ax, [(xd, tl[1]), tl])
            xsh = x0 - 3.9
            _dot(ax, xsh, SH)
            _pl(ax, [(xsh, SH), (xsh, bh[1]), bh])
            xq = x0 - 4.9
            _dot(ax, xq, 0.9)
            _pl(ax, [(xq, 0.9), (xq, bl[1]), bl])
            xv = x0 - 1.8
            _pl(ax, [to, (xv, to[1]), (xv, oh[1]), oh])
            _pl(ax, [bo, (xv, bo[1]), (xv, ol[1]), ol])
            _arrow(ax, oo, (x0, 0.9))
        if i < 3:
            _line(ax, [x0 + w, xs[i + 1] - 4.9], [0.9, 0.9])
    _arrow(ax, (xs[3] + w, 0.9), (xs[3] + w + 2.0, 0.9))
    _t(ax, xs[3] + w + 0.2, 0.7, "serial out", fs=9.5, weight="bold", color=ACC, ha="left", va="top")
    _t(ax, xs[2] - 2.0, -2.6, "D = SHIFT·Q₁ + SHIFT'·D₂", fs=9.5, weight="bold", color=G1)
    return _nat(fig)


# ------------------------------------------------------------------ 4. universal shift register stage
def univ_stage():
    fig, ax = _cv((0.0, 13.3), (-2.0, 6.9), 0.4)
    x, y, hh = 5.6, 0.8, 4.4
    out, pins = _mux(ax, x, y, hh, w=1.5, n=4, label="4:1", sel=("S₁", "S₀"), outside=False, names=False)
    labs = ("00: Qᵢ (hold)", "01: Qᵢ₋₁ (shift right)", "10: Qᵢ₊₁ (shift left)", "11: Dᵢ (load)")
    for (px, py), s in zip(pins, labs):
        ax.text(px - 0.7, py, s, ha="right", va="center", fontsize=9.5, color=INK)
    fy = out[1] - 0.9
    p = _ff(ax, 9.0, fy, 1.8, 1.8, dy=0.9, clk="bottom")
    _arrow(ax, out, p["D"])
    _arrow(ax, p["Q"], (12.2, p["Q"][1]))
    _cl(ax, 12.3, p["Q"][1], "Qᵢ", ha="left", color=ACC, fs=10.5)
    xl = 11.5
    _dot(ax, xl, p["Q"][1])
    ytop = 6.0
    xv = pins[0][0] - 0.3
    _pl(ax, [(xl, p["Q"][1]), (xl, ytop), (xv, ytop), (xv, pins[0][1])])
    _dot(ax, xv, pins[0][1])
    _line(ax, [p["C"][0]] * 2, [fy - 1.0, fy], color=MUTED, lw=1.4)
    _t(ax, p["C"][0], fy - 1.2, "CLK", fs=9.5, color=MUTED, va="top")
    _t(ax, 6.7, -1.5, "end stages: Q₀'s 01 input is DSR, Q₃'s 10 input is DSL", fs=9, color=MUTED)
    return _nat(fig)


# ------------------------------------------------------------------ 5. 4-bit ring counter
def ring4():
    fig, ax = _cv((-1.9, 16.8), (-3.5, 4.5), 0.34)
    P, w, h = 4.2, 1.8, 2.0
    yc, ys = -1.0, -1.9
    xs = [i * P for i in range(4)]
    _line(ax, [xs[0] + 1.4, xs[3] + 1.4], [yc, yc], color=MUTED, lw=1.4)
    _t(ax, xs[3] + 1.7, yc, "CLK", fs=9, color=MUTED, ha="left")
    _line(ax, [xs[0] + 0.6, xs[3] + 0.6], [ys, ys], color=G1, lw=1.4)
    _t(ax, xs[0] + 0.4, ys, "START'", fs=9.5, weight="bold", color=G1, ha="right")
    for i, x in enumerate(xs):
        p = _ff(ax, x, 0, w, h, dy=1.4, clk="bottom", cx=1.4, name=f"FF{i}")
        _line(ax, [p["C"][0]] * 2, [yc, 0], color=MUTED, lw=1.4)
        _dot(ax, p["C"][0], yc, col=MUTED)
        _bub(ax, x + 0.6, -0.11)
        _line(ax, [x + 0.6] * 2, [ys, -0.22], color=G1, lw=1.4)
        _dot(ax, x + 0.6, ys, col=G1)
        ax.text(x + 0.6, 0.55, "PRE'" if i == 0 else "CLR'", ha="center", va="center", fontsize=7.5, color=G1, weight="bold")
        ax.text(x + w + 0.25, 1.65, "Q" + "₀₁₂₃"[i], ha="left", va="bottom", fontsize=9.5, weight="bold", color=ACC)
        if i < 3:
            _arrow(ax, (x + w, 1.4), (xs[i + 1], 1.4))
    xl = xs[3] + w + 1.3
    _dot(ax, xl, 1.4)
    _line(ax, [xs[3] + w, xl], [1.4, 1.4])
    _pl(ax, [(xl, 1.4), (xl, 3.6), (-1.1, 3.6), (-1.1, 1.4)])
    _arrow(ax, (-1.1, 1.4), (0, 1.4))
    _t(ax, 7.0, 3.85, "Q₃ loops back to D₀", fs=8.5, color=MUTED, va="bottom")
    _t(ax, 7.0, -2.9, "START' = 0 presets FF0 to 1 and clears FF1–FF3 to 0", fs=8.8, color=MUTED)
    return _nat(fig)


# ------------------------------------------------------------------ 6, 7. state rings
def ring_states():
    return state_ring(["1000", "0100", "0010", "0001"], title="4-bit ring counter, Q₀Q₁Q₂Q₃", r=1.6)


def johnson_lockout():
    a = state_ring(["0000", "1000", "1100", "1110", "1111", "0111", "0011", "0001"], title="the 8 states used", r=2.4)
    b = state_ring(["0100", "1010", "1101", "0110", "1011", "0101", "0010", "1001"],
                   title="the 8 unused states: a second loop", r=2.4)
    return ('<div style="display:flex;gap:6mm;justify-content:center;align-items:flex-start">'
            + "".join(f'<div style="flex:1 1 0;min-width:0">{s}</div>' for s in (a, b)) + "</div>")


# ------------------------------------------------------------------ 8. serial adder
def serial_adder():
    fig, ax = _cv((-3.4, 16.0), (-1.8, 9.7), 0.34)
    for yb, nm in ((6.4, "A"), (3.6, "B")):
        _box(ax, 2.4, yb, 5.4, 1.6, f"Shift register {nm}", fc=TINT, ec=ACC, r=0.08, fs=9.5)
        ax.text(2.55, yb + 1.2, "SI", ha="left", va="center", fontsize=8.5, color=MUTED)
        ax.text(7.65, yb + 0.8, "SO", ha="right", va="center", fontsize=8.5, color=MUTED)
        ax.add_patch(Polygon([(2.4, yb + 0.2), (2.68, yb + 0.4), (2.4, yb + 0.6)], closed=True, fc="none", ec=INK, lw=1.1))
    # FA
    _box(ax, 9.4, 3.2, 2.2, 3.8, "", fc="white", ec=ACC, r=0.08)
    _t(ax, 10.5, 5.1, "FA", fs=11, weight="bold", color=ACC)
    for yy, s in ((6.4, "x"), (5.2, "y"), (4.0, "z")):
        _t(ax, 9.55, yy, s, fs=9, ha="left", weight="bold")
    _t(ax, 11.45, 6.4, "S", fs=9, ha="right", weight="bold")
    _t(ax, 11.45, 3.8, "C", fs=9, ha="right", weight="bold")
    # register outputs into FA
    _pl(ax, [(7.8, 7.2), (8.5, 7.2), (8.5, 6.4)]); _arrow(ax, (8.5, 6.4), (9.4, 6.4))
    _pl(ax, [(7.8, 4.4), (8.2, 4.4), (8.2, 5.2)]); _arrow(ax, (8.2, 5.2), (9.4, 5.2))
    # S back to A.SI
    _pl(ax, [(11.6, 6.4), (12.4, 6.4), (12.4, 9.2), (0.6, 9.2), (0.6, 7.6)])
    _arrow(ax, (0.6, 7.6), (2.4, 7.6))
    # external input into B.SI
    _arrow(ax, (0.0, 4.8), (2.4, 4.8))
    _t(ax, -0.1, 4.8, "external input", fs=8.8, color=MUTED, ha="right")
    # carry flip-flop
    p = _ff(ax, 12.8, 0.2, 2.0, 2.0, dy=1.5, clk="left", cy=0.5)
    _t(ax, 13.9, 1.0, "carry", fs=9, weight="bold", color=ACC)
    _pl(ax, [(11.6, 3.8), (12.2, 3.8), (12.2, 1.7)]); _arrow(ax, (12.2, 1.7), (12.8, 1.7))
    _t(ax, 13.8, 3.5, "Clear", fs=9, weight="bold", va="bottom")
    _arrow(ax, (13.8, 3.45), (13.8, 2.2))
    _pl(ax, [(14.8, 1.7), (15.4, 1.7), (15.4, -0.8), (8.6, -0.8), (8.6, 4.0)])
    _arrow(ax, (8.6, 4.0), (9.4, 4.0))
    # clock AND gate
    th, tl, to = _and(ax, 0.0, 0.0, 1.2, 1.0)
    for pt, s in ((th, "Shift-right"), (tl, "CP")):
        _arrow(ax, (-0.6, pt[1]), pt)
        _t(ax, -0.7, pt[1], s, fs=8.8, ha="right")
    _pl(ax, [to, (1.6, 0.0), (1.6, 6.8)])
    _line(ax, [1.6, 11.9, 11.9], [0.0, 0.0, 0.7], color=INK)
    _arrow(ax, (11.9, 0.7), (12.8, 0.7))
    for yy in (6.8, 4.0):
        _line(ax, [1.6, 2.4], [yy, yy]); _dot(ax, 1.6, yy)
    _t(ax, 6.0, 0.3, "gated clock", fs=8.5, color=MUTED, va="bottom")
    return _nat(fig)


# ------------------------------------------------------------------ timing figures (figlib)
def _wave(ax, pts, xmax, color=ACC, lw=1.7, ls="-"):
    xs, ys = [], []
    for k, (t, v) in enumerate(pts):
        if k:
            xs.append(t); ys.append(ys[-1])
        xs.append(t); ys.append(v)
    xs.append(xmax); ys.append(ys[-1])
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_joinstyle="miter")


def _lvl(ax, name, ymax=1.5):
    ax.set_yticks([0, 1])
    ax.set_ylim(-0.2, ymax)
    ax.set_ylabel(name, rotation=0, ha="right", va="center", labelpad=10, fontsize=9.5, weight="bold")
    ax.spines["bottom"].set_visible(False)
    ax.tick_params(axis="x", length=0, labelbottom=False)
    ax.tick_params(axis="y", labelsize=8.5)


def _lastx(ax, xl):
    ax.spines["bottom"].set_visible(True)
    ax.tick_params(axis="x", length=3, labelbottom=True)
    ax.set_xlabel(xl)


CLK40 = [(0, 0), (10, 1), (20, 0), (30, 1)]


def tpd():
    f, axs = fl.fig(7.4, 4.0, nrows=3, sharex=True)
    for ax, nm in zip(axs, ("CLK", "D", "Q")):
        _lvl(ax, nm)
    _wave(axs[0], CLK40, 40, MUTED)
    _wave(axs[1], [(0, 0), (2, 1)], 40)
    _wave(axs[2], [(0, 0), (18, 1)], 40)
    axs[0].set_xlim(0, 40)
    for ax in axs:
        ax.axvline(10, color=G1, lw=0.9, ls=(0, (3, 3)))
    axs[2].annotate("", xy=(18, 0.5), xytext=(10, 0.5), arrowprops=dict(arrowstyle="<->", color=BAD, lw=1.4,
                                                                       shrinkA=0, shrinkB=0))
    axs[2].text(14, 0.6, r"$t_{\mathrm{pd}}$ = 8 ns", ha="center", va="bottom", fontsize=9.5, color=BAD, weight="bold")
    _lastx(axs[2], "time (ns)")
    return fl.svg(f)


def meta():
    import math
    f, axs = fl.fig(7.4, 3.6, nrows=2, sharex=True, gridspec_kw={"height_ratios": [1, 1.4]})
    for ax, nm in zip(axs, ("CLK", "Q")):
        _lvl(ax, nm)
    axs[0].set_ylim(-0.2, 1.9)
    axs[1].set_ylim(-0.2, 1.3)
    _wave(axs[0], CLK40, 40, MUTED)
    axs[0].axvspan(7, 12, color=G1, alpha=0.18, lw=0)
    axs[0].text(9.5, 1.2, "setup + hold window", ha="center", va="bottom", fontsize=9, color=G1, weight="bold")
    axs[0].set_xlim(0, 40)
    q = axs[1]
    q.axhspan(0.42, 0.58, color=MUTED, alpha=0.22, lw=0)
    q.text(0.8, 0.64, "invalid: neither 0 nor 1", ha="left", va="bottom", fontsize=9, color=MUTED)
    xs, ys = [0, 15, 18], [0, 0, 0.5]
    t = 18.0
    while t <= 30:
        xs.append(t); ys.append(0.5 + 0.035 * math.sin(2.6 * (t - 18)))
        t += 0.25
    xs.append(30); ys.append(0.5)
    q.plot(xs + [31.2, 40], ys + [1, 1], color=ACC, lw=1.7)
    q.plot(xs + [31.2, 40], ys + [0, 0], color=BAD, lw=1.7, ls=(0, (1.5, 2.2)))
    q.text(32.5, 0.5, "resolves to 1 or 0\nafter an unknown time", ha="left", va="center", fontsize=9, color=INK)
    _lastx(q, "time (ns)")
    return fl.svg(f)


def _bar_fig(w, h, xmax, ymax, xl):
    f, ax = fl.fig(w, h)
    ax.set_xlim(0, xmax); ax.set_ylim(-1.0, ymax)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(xl)
    return f, ax


TP, TC, TS = "#c9d7fb", "#fbd9bf", "#c3ecd8"


def _seg(ax, a, b, y, hh, col, label, hatch=None, lab_y=None, fs=9.5, ha="center", ec=INK):
    ax.add_patch(Rectangle((a, y), b - a, hh, fc=col, ec=ec, lw=1.1, hatch=hatch))
    if label:
        ax.text((a + b) / 2 if ha == "center" else a, y + hh / 2 if lab_y is None else lab_y, label,
                ha=ha, va="center", fontsize=fs)


def budget():
    f, ax = _bar_fig(7.4, 2.6, 28, 2.6, "time after the launching clock edge (ns)")
    ax.set_xticks(range(0, 29, 4))
    _seg(ax, 0, 8, 0, 1, TP, r"$t_{\mathrm{pd}}$ = 8")
    _seg(ax, 8, 20, 0, 1, TC, r"$t_{\mathrm{comb,max}}$ = 12")
    _seg(ax, 20, 23, 0, 1, TS, r"$t_{\mathrm{su}}$ = 3")
    ax.plot([25, 25], [-0.3, 2.15], color=INK, lw=1.5)
    ax.text(24.7, 2.15, "next edge at 40 MHz (25 ns): 2 ns spare", ha="right", va="center", fontsize=9, color=INK, weight="bold")
    ax.plot([20, 20], [-0.3, 1.6], color=BAD, lw=1.5, ls=(0, (4, 3)))
    ax.text(19.7, 1.6, "next edge at 50 MHz (20 ns): too early", ha="right", va="center", fontsize=9, color=BAD, weight="bold")
    ax.set_xlim(0, 28)
    return fl.svg(f)


def _hold(xmax, win, wl, wcol, mark, ml, mcol, edge=None):
    f, ax = _bar_fig(7.4, 2.7, xmax, 2.6, "time after the clock edge (ns)")
    ax.set_xticks(range(0, xmax + 1, 2))
    ax.add_patch(Rectangle((win[0], -0.45), win[1] - win[0], 2.3, fc=wcol, alpha=0.18, lw=0))
    ax.text(win[0], 2.05, wl, ha="left", va="center", fontsize=9, color=wcol, weight="bold")
    _seg(ax, 0, 8, 0, 1, TP, r"$t_{\mathrm{pd}}$ = 8")
    _seg(ax, 8, 9, 0, 1, TC, "")
    ax.text(8.15, -0.2, r"$t_{\mathrm{comb,min}}$ = 1", ha="left", va="top", fontsize=9)
    ax.annotate("", xy=(mark, 1.05), xytext=(mark, 1.4), arrowprops=dict(arrowstyle="-|>", color=mcol, lw=1.5,
                                                                          shrinkA=0, shrinkB=0))
    ax.text(xmax - 0.1, 1.55, ml, ha="right", va="center", fontsize=9, color=mcol, weight="bold")
    if edge is not None:
        ax.plot([edge, edge], [-0.7, 1.3], color=INK, lw=1.2, ls=(0, (4, 3)))
        ax.text(edge - 0.1, -0.7, "CLK2 edge (8 ns late)", ha="right", va="center", fontsize=9)
    ax.set_xlim(0, xmax)
    return f


def hold0():
    return fl.svg(_hold(12, (0, 2), r"$t_{\mathrm{h}}$ = 2: capturing FF still reading the old D", G1,
                        9, "new D arrives at 9 ns: after the window, safe", G2))


def hold8():
    return fl.svg(_hold(14, (8, 10), r"capture edge at 8 + $t_{\mathrm{h}}$ = 2", BAD,
                        9, "new D at 9 ns: inside the window, hold violated", BAD, edge=8))


def skew3():
    f, axs = fl.fig(7.4, 4.0, nrows=3, sharex=True, gridspec_kw={"height_ratios": [1, 1, 1.05]})
    _lvl(axs[0], "CLK₁\n(launch)")
    _lvl(axs[1], "CLK₂\n(capture)")
    _wave(axs[0], [(0, 1), (10, 0), (20, 1), (30, 0)], 30, MUTED)
    _wave(axs[1], [(0, 0), (3, 1), (13, 0), (23, 1)], 30, MUTED)
    ax = axs[2]
    ax.set_ylim(-0.9, 1.9); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.set_ylabel("data", rotation=0, ha="right", va="center", labelpad=10, fontsize=9.5, weight="bold")
    _seg(ax, 0, 8, 0, 1, TP, r"$t_{\mathrm{pd}}$")
    _seg(ax, 8, 20, 0, 1, TC, r"$t_{\mathrm{comb,max}}$")
    _seg(ax, 20, 23, 0, 1, TS, "", hatch="///")
    ax.text(21.5, -0.15, r"$t_{\mathrm{su}}$", ha="center", va="top", fontsize=9.5)
    ax.text(22.6, 1.35, "data ready at 20 = 23 − $t_{\\mathrm{su}}$: just in time", ha="right", va="center", fontsize=9,
            color=G2, weight="bold")
    axs[0].set_xlim(0, 30)
    for a in axs:
        a.axvline(3, color=G1, lw=0.9, ls=(0, (3, 3)))
        a.axvline(23, color=G1, lw=0.9, ls=(0, (3, 3)))
    axs[1].annotate("", xy=(3, 0.5), xytext=(0, 0.5), arrowprops=dict(arrowstyle="<->", color=BAD, lw=1.4,
                                                                      shrinkA=0, shrinkB=0))
    axs[1].text(1.5, 0.62, "δ = 3 ns", ha="center", va="bottom", fontsize=9.5, color=BAD, weight="bold")
    _lastx(ax, "time (ns)")
    return fl.svg(f)


FIGS = {
    "u3r_reg4": reg4,
    "u3r_sipo_waves": sipo_waves,
    "u3r_piso": piso,
    "u3r_univ_stage": univ_stage,
    "u3r_ring4": ring4,
    "u3r_ring_states": ring_states,
    "u3r_johnson_lockout": johnson_lockout,
    "u3r_serial_adder": serial_adder,
    "u3r_tpd": tpd,
    "u3r_meta": meta,
    "u3r_budget": budget,
    "u3r_hold0": hold0,
    "u3r_hold8": hold8,
    "u3r_skew3": skew3,
}
