"""Unit 4 figures for file 17 (timing issues, generators, asynchronous circuits) (v1.3, S9)."""
import figlib as fl
from figs1 import ACC, BAD, G1, INK, MUTED
from matplotlib.patches import Polygon, Rectangle


def _trace(ax, base, pts, xend, color=INK, lw=1.7, h=1.0):
    """Step trace: pts = [(t, level), ...] sorted by t, first at t = 0; level 0/1 drawn at base / base + h."""
    xs, ys = [], []
    for k, (t, lv) in enumerate(pts):
        if k:
            xs.append(t)
            ys.append(base + pts[k - 1][1] * h)
        xs.append(t)
        ys.append(base + lv * h)
    xs.append(xend)
    ys.append(base + pts[-1][1] * h)
    ax.plot(xs, ys, color=color, lw=lw, solid_joinstyle="miter")


def _name(ax, y, txt):
    ax.annotate(txt, xy=(-0.02, y), xycoords=("axes fraction", "data"), ha="right", va="center",
                fontsize=9.5, weight="bold")


def _guides(ax, xs, y0, y1):
    for x in xs:
        ax.plot([x, x], [y0, y1], color=MUTED, lw=0.8, ls=":", zorder=1)


def _dbl(ax, a, b, y, col):
    ax.annotate("", xy=(b, y), xytext=(a, y),
                arrowprops=dict(arrowstyle="<->", color=col, lw=1.4, shrinkA=0, shrinkB=0))


def _timeaxes(ax, xmax, ylo, yhi, step, label="time (ns)"):
    ax.set_xlim(0, xmax)
    ax.set_ylim(ylo, yhi)
    if step:
        ax.set_xticks(range(0, xmax + 1, step))
    else:
        ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(label)


# ------------------------------------------------------------------ 1. decoding glitch
def decode_glitch():
    f, ax = fl.fig(7.4, 4.2)
    rows = {"CLK": 6.0, "Q1": 4.0, "Q0": 2.0, "Y": 0.0}
    _guides(ax, (10, 17, 19), -0.8, 7.2)
    ax.add_patch(Rectangle((17, -0.25), 2, 5.5, fc=BAD, alpha=0.12, ec="none", zorder=0))
    _trace(ax, 6.0, [(0, 0), (10, 1), (25, 0)], 40, ACC)
    _trace(ax, 4.0, [(0, 0), (19, 1)], 40, ACC)
    _trace(ax, 2.0, [(0, 1), (17, 0)], 40, ACC)
    _trace(ax, 0.0, [(0, 0), (17, 1), (19, 0)], 40, BAD, lw=2.0)
    _name(ax, 6.5, "CLK")
    _name(ax, 4.5, "Q1")
    _name(ax, 2.5, "Q0")
    _name(ax, 0.5, "Y = Q1'Q0'")
    ax.text(5, 7.5, "state 01", ha="center", va="center", fontsize=8.5, color=MUTED)
    ax.text(32.5, 7.5, "state 10", ha="center", va="center", fontsize=8.5, color=MUTED)
    _dbl(ax, 17, 19, -0.5, BAD)
    ax.text(19.7, -0.5, "glitch: state 00 for 2 ns", ha="left", va="center", fontsize=9.5, color=BAD, weight="bold")
    _timeaxes(ax, 40, -1.1, 8.0, 5)
    return fl.svg(f)


# ------------------------------------------------------------------ 2. two-flip-flop synchroniser
def sync2():
    f, (ab, ax) = fl.fig(7.6, 5.0, nrows=2, gridspec_kw=dict(height_ratios=[1.0, 1.9], hspace=0.28))
    # --- block diagram
    ab.set_xlim(0, 11.6)
    ab.set_ylim(0, 3.4)
    ab.axis("off")
    for x0, nm in ((2.8, "D  FF1"), (6.4, "D  FF2")):
        fl.box(ab, x0, 1.2, 1.6, 1.5, nm, fc="#e8eefe", ec=ACC, weight="bold")
        xc = x0 + 0.8
        ab.add_patch(Polygon([(xc - 0.14, 1.2), (xc + 0.14, 1.2), (xc, 1.45)], closed=True, fc="white", ec=INK, lw=1.1))
        ab.plot([xc, xc], [0.55, 1.2], color=INK, lw=1.3)
    ab.plot([3.6, 7.2], [0.55, 0.55], color=INK, lw=1.3)
    ab.text(3.4, 0.55, "CLK", ha="right", va="center", fontsize=9.5, weight="bold")
    ab.text(0.05, 2.0, "async input A", ha="left", va="center", fontsize=9.5)
    fl.arrow(ab, (1.65, 2.0), (2.8, 2.0))
    fl.arrow(ab, (4.4, 2.0), (6.4, 2.0))
    ab.text(5.4, 2.3, "Q1", ha="center", va="bottom", fontsize=9.5)
    fl.arrow(ab, (8.0, 2.0), (8.7, 2.0))
    ab.text(8.8, 2.0, "A_sync (to the system)", ha="left", va="center", fontsize=9.5)
    # --- timing
    _guides(ax, (20, 30), 0.4, 10.6)
    _trace(ax, 9.0, [(0, 0), (10, 1), (15, 0), (20, 1), (25, 0), (30, 1), (35, 0), (40, 1)], 45, ACC)
    ax.add_patch(Rectangle((18.5, 6.4), 2.5, 1.4, fc=MUTED, alpha=0.18, ec="none", zorder=0))
    _trace(ax, 6.6, [(0, 0), (19.6, 1)], 45, ACC)
    ax.add_patch(Rectangle((20, 4.0), 6, 1.0, fc=BAD, alpha=0.15, ec="none", zorder=0))
    ax.plot([20, 26], [4.5, 4.5], color=ACC, lw=1.7)
    ax.plot([26, 26, 45], [4.5, 5.0, 5.0], color=ACC, lw=1.7, solid_joinstyle="miter")
    ax.plot([0, 20, 20], [4.0, 4.0, 4.5], color=ACC, lw=1.7, solid_joinstyle="miter")
    _trace(ax, 0.8, [(0, 0), (30, 1)], 45, ACC)
    _name(ax, 9.5, "CLK")
    _name(ax, 7.1, "A")
    _name(ax, 4.5, "Q1")
    _name(ax, 1.3, "A_sync")
    ax.text(19.8, 8.1, "setup/hold window", ha="right", va="bottom", fontsize=8.5, color=MUTED)
    ax.text(20.6, 5.45, "metastable\n(undecided)", ha="left", va="bottom", fontsize=8.5, color=BAD)
    _dbl(ax, 20, 30, 3.5, BAD)
    ax.text(25, 3.3, "one clock period\nto settle", ha="center", va="top", fontsize=8.5, color=BAD, weight="bold")
    _timeaxes(ax, 45, 0.2, 10.8, 10)
    return fl.svg(f)


# ------------------------------------------------------------------ 3. switch bounce
def bounce():
    f, ax = fl.fig(7.4, 3.4)
    _guides(ax, (5, 20), -0.3, 4.2)
    pts = [(0, 0), (5, 1), (6, 0), (6.8, 1), (7.6, 0), (8.0, 1), (8.5, 0), (8.8, 1),
           (20, 0), (20.5, 1), (21.0, 0), (21.3, 1), (21.6, 0)]
    _trace(ax, 2.2, pts, 30, INK)
    _trace(ax, 0.0, [(0, 0), (5, 1), (20, 0)], 30, G1, lw=2.0)
    _name(ax, 2.7, "switch contact")
    _name(ax, 0.5, "latch Q")
    ax.text(4.6, 3.55, "press", ha="right", va="center", fontsize=9.5, weight="bold")
    ax.text(20.5, 3.55, "release", ha="left", va="center", fontsize=9.5, weight="bold")
    ax.plot([5.1, 5.1, 8.8, 8.8], [3.5, 3.65, 3.65, 3.5], color=BAD, lw=1.3)
    ax.text(6.95, 3.8, "bounces", ha="center", va="bottom", fontsize=9.5, color=BAD, weight="bold")
    _timeaxes(ax, 30, -0.4, 4.4, 0, "time")
    return fl.svg(f)


# ------------------------------------------------------------------ 4. static-1 hazard
def static1():
    f, ax = fl.fig(7.4, 5.2)
    _guides(ax, (10, 12, 13, 15, 16, 18), -0.4, 13.8)
    _trace(ax, 12.6, [(0, 1), (10, 0)], 30, ACC)
    _trace(ax, 10.6, [(0, 0), (12, 1)], 30, ACC)
    _trace(ax, 8.6, [(0, 1), (13, 0)], 30, ACC)
    _trace(ax, 6.6, [(0, 0), (15, 1)], 30, ACC)
    _trace(ax, 4.6, [(0, 1), (16, 0), (18, 1)], 30, ACC)
    # the dip drawn in BAD on top
    ax.plot([16, 16, 18, 18], [5.6, 4.6, 4.6, 5.6], color=BAD, lw=2.2, solid_joinstyle="miter", zorder=4)
    _trace(ax, 0.0, [(0, 1)], 30, G1, lw=2.0)
    for y, nm in ((13.1, "A"), (11.1, "A'"), (9.1, "AB"), (7.1, "A'C"), (5.1, "F = AB + A'C"),
                  (0.5, "F with BC added")):
        _name(ax, y, nm)
    _dbl(ax, 16, 18, 3.9, BAD)
    ax.text(18.6, 3.6, "static-1 hazard:\n2 ns dip (= NOT delay)", ha="left", va="center", fontsize=9, color=BAD,
            weight="bold")
    _timeaxes(ax, 30, -0.6, 14.0, 5)
    return fl.svg(f)


FIGS = {"u4b_decode_glitch": decode_glitch, "u4b_sync": sync2, "u4b_bounce": bounce, "u4b_static1": static1}
