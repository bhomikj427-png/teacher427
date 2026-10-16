"""Figures for DE-v1.pdf. Every public function returns an inline SVG string.

All figures are generated (matplotlib / schemdraw) except the four Wikimedia Commons schematics in
img/ (provenance printed under each). Values drawn here are the ones checked by verify.py.
"""
import io
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, FancyArrowPatch, Rectangle

INK, MUTED, LINE, SOFT = "#1c1f24", "#6a707a", "#c9cbc4", "#f0f0eb"
ACC, G1, G2, G3, BAD = "#2f5bea", "#e0661b", "#12925a", "#b23fbf", "#d92d20"

plt.rcParams.update({
    "font.family": ["Segoe UI", "DejaVu Sans"], "font.size": 10, "svg.fonttype": "none",
    "axes.edgecolor": INK, "text.color": INK,
})

plt.rcParams.update({"mathtext.fontset": "custom", "mathtext.rm": "Segoe UI", "mathtext.it": "Segoe UI:italic"})
_SUB = re.compile(r"\b([A-Za-z]{1,2})_([A-Za-z0-9]+(?:,[a-z]+)?)")


def _m(t):
    return _SUB.sub(lambda g: r"$\mathrm{%s}_{\mathrm{%s}}$" % (g.group(1), g.group(2)), t) if isinstance(t, str) else t


import matplotlib.axes as _ma, matplotlib.figure as _mf  # noqa: E402
_at, _ft = _ma.Axes.text, _mf.Figure.text
_ma.Axes.text = lambda self, x, y, t, *a, **k: _at(self, x, y, _m(t), *a, **k)
_mf.Figure.text = lambda self, x, y, t, *a, **k: _ft(self, x, y, _m(t), *a, **k)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "web"))
import figures as kfig  # noqa: E402  (the site's K-map renderer, reused)


def _svg(fig):
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", pad_inches=0.04, transparent=True)
    plt.close(fig)
    s = buf.getvalue()
    s = s[s.index("<svg"):]
    s = re.sub(r'width="[\d.]+pt" height="[\d.]+pt"', 'class="mpl"', s, count=1)
    return s


def _canvas(w, h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def _box(ax, x, y, w, h, text="", fc="white", ec=INK, lw=1.4, fs=10, r=0.08, color=INK, weight="normal", ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw, ls=ls))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=color, weight=weight)


def _arrow(ax, p, q, color=INK, lw=1.3, rad=0.0, ls="-", head=8):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=f"-|>,head_length={head/20},head_width={head/34}",
                                 connectionstyle=f"arc3,rad={rad}", color=color, lw=lw, ls=ls,
                                 shrinkA=0, shrinkB=0, mutation_scale=10))


def _line(ax, xs, ys, color=INK, lw=1.3, ls="-"):
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle="round")


# ================================================================== flow map
def flow_map():
    nodes = [
        ("Boolean +\nK-map", 0), ("Adders,\nparity", 0), ("MUX, decoder,\ncomparator, ALU", 0),
        ("Flip-flops,\nwaveforms", 0), ("Synchronous\ncounter design", 0),
        ("Ripple counters,\nshift registers", 1), ("Timing\nanalysis", 1), ("FSM design,\nreduction", 1),
        ("ASM, generators,\nasync circuits", 1), ("Logic families\nTTL·ECL·CMOS", 1), ("Memories\n+ PLDs", 1),
    ]
    fig, ax = _canvas(9.6, 3.3, (-0.2, 12.2), (-0.3, 4.1))
    pos = []
    for i, _ in enumerate(nodes):
        row, k = divmod(i, 6)
        x = 0.1 + k * 2.0 if row == 0 else 0.1 + (5 - k) * 2.0
        y = 2.6 if row == 0 else 0.3
        pos.append((x, y))
    for i, ((t, part), (x, y)) in enumerate(zip(nodes, pos)):
        fc, ec, col = (SOFT, LINE, MUTED) if part == 0 else ("#e8eefe", ACC, INK)
        _box(ax, x, y, 1.75, 1.05, t, fc=fc, ec=ec, fs=8.6, color=col, r=0.14)
        ax.text(x + 0.1, y + 0.93, str(i + 1), fontsize=7, color=ACC if part else MUTED, weight="bold", va="top")
    for i in range(len(nodes) - 1):
        (x1, y1), (x2, y2) = pos[i], pos[i + 1]
        if y1 == y2:
            a, b = ((x1 + 1.75, y1 + 0.52), (x2, y2 + 0.52)) if x2 > x1 else ((x1, y1 + 0.52), (x2 + 1.75, y2 + 0.52))
        else:
            a, b = (x1 + 0.87, y1), (x2 + 0.87, y2 + 1.05)
        _arrow(ax, a, b, color=MUTED if i < 4 else ACC, lw=1.2)
    ax.text(0.1, 3.95, "MTE half — study-pack 01–09 · recap in Part A", fontsize=8.5, color=MUTED, va="top")
    ax.text(0.1, -0.05, "ETE half — taught in full in Parts B–D", fontsize=8.5, color=ACC, va="top", weight="bold")
    return _svg(fig)


def sub_map(items, color=ACC):
    """Small left-to-right chain: list of labels."""
    n = len(items)
    fig, ax = _canvas(1.7 * n, 0.9, (-0.05, 2.0 * n - 0.3), (-0.05, 0.95))
    for i, t in enumerate(items):
        _box(ax, i * 2.0, 0, 1.7, 0.85, t, fc="#e8eefe", ec=color, fs=8.4, r=0.12)
        if i:
            _arrow(ax, (i * 2.0 - 0.3, 0.42), (i * 2.0, 0.42), color=color)
    return _svg(fig)


# ================================================================== waveforms
def waves(rows, n, title=None, marks=(), delay=None, w=8.6, edge="neg", shade=None):
    """rows: list of (name, levels). levels: list of 0/1 per half-unit step (len n) or
    list of (t, level) breakpoints when tuple. CLK auto if name == 'CLK'."""
    h = 0.55 * len(rows) + 0.4
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(-1.4, n + 0.2); ax.set_ylim(-0.6 * len(rows) - 0.1, 0.5); ax.axis("off")
    if shade:
        for (a, b, c) in shade:
            ax.add_patch(Rectangle((a, -0.6 * len(rows)), b - a, 0.6 * len(rows) + 0.4, fc=c, alpha=0.13, lw=0))
    for r, (name, lev) in enumerate(rows):
        y0 = -0.6 * r
        ax.text(-0.25, y0 - 0.2, name, ha="right", va="center", fontsize=9.5, color=INK, weight="bold" if name != "CLK" else "normal")
        if isinstance(lev[0], tuple):
            pts = lev
        else:
            pts = [(i, v) for i, v in enumerate(lev)]
        xs, ys = [], []
        for k, (t, v) in enumerate(pts):
            if k:
                xs.append(t); ys.append(ys[-1])
            xs.append(t); ys.append(v)
        xs.append(n); ys.append(ys[-1])
        ax.plot(xs, [y0 - 0.4 + 0.4 * v for v in ys], color=ACC if name != "CLK" else MUTED, lw=1.6, solid_joinstyle="miter")
    for (x, txt, col) in marks:
        ax.axvline(x, color=col, lw=0.8, ls=(0, (3, 3)))
        if txt:
            ax.text(x, 0.42, txt, ha="center", fontsize=8, color=col)
    if title:
        ax.set_title(title, fontsize=9.5, color=MUTED, loc="left")
    return _svg(fig)


def clk(n_cycles, half=1.0):
    return [(i * half, (i + 1) % 2) for i in range(int(n_cycles * 2))]


# ================================================================== register chains
def chain(n=4, kind="shift", taps=None, title=None, w=8.4):
    """Row of D flip-flops sharing CLK. kind: shift | ring | johnson | lfsr."""
    fig, ax = _canvas(w, 2.4, (-1.3, 2.3 * n + 0.6), (-1.35, 1.7))
    for i in range(n):
        x = i * 2.3
        _box(ax, x, 0, 1.3, 1.1, "", r=0.05)
        ax.text(x + 0.12, 0.8, "D", fontsize=9); ax.text(x + 1.18, 0.8, "Q", fontsize=9, ha="right")
        ax.text(x + 0.65, 1.22, f"Q{i}" if kind != "lfsr" else f"Q{i+1}", ha="center", fontsize=9.5, weight="bold", color=ACC)
        ax.add_patch(Polygon([(x + 0.55, 0), (x + 0.65, 0.16), (x + 0.75, 0)], closed=True, fc="none", ec=INK, lw=1))
        _line(ax, [x + 0.65, x + 0.65], [-0.45, 0])
        if i < n - 1:
            _arrow(ax, (x + 1.3, 0.85), (x + 2.3, 0.85))
    _line(ax, [-0.6, (n - 1) * 2.3 + 0.65], [-0.45, -0.45], color=MUTED)
    ax.text(-0.65, -0.45, "CLK", ha="right", va="center", fontsize=9, color=MUTED)
    end = (n - 1) * 2.3 + 1.3
    if kind == "shift":
        _arrow(ax, (-1.0, 0.85), (0, 0.85)); ax.text(-1.05, 0.85, "Serial\nin", ha="right", va="center", fontsize=8.5)
        _arrow(ax, (end, 0.85), (end + 0.55, 0.85)); ax.text(end + 0.6, 0.85, "Serial\nout", va="center", fontsize=8.5)
    else:
        lab = {"ring": "Q", "johnson": "Q'", "lfsr": "⊕"}[kind]
        col = {"ring": G2, "johnson": G1, "lfsr": G3}[kind]
        _line(ax, [end, end + 0.35, end + 0.35, -0.5, -0.5], [0.85, 0.85, -1.05, -1.05, 0.85], color=col, lw=1.5)
        _arrow(ax, (-0.5, 0.85), (0, 0.85), color=col)
        ax.text((end - 0.5) / 2, -1.25, {"ring": "feedback: last Q → first D",
                                         "johnson": "feedback: last Q' (complemented) → first D",
                                         "lfsr": "feedback: XOR of the tap outputs → first D"}[kind],
                ha="center", fontsize=8.5, color=col)
        if kind == "lfsr":
            cx, cy = -0.5, 0.2
            ax.add_patch(Circle((cx, cy), 0.22, fc="white", ec=col, lw=1.5)); ax.text(cx, cy, "⊕", ha="center", va="center", fontsize=12, color=col)
            for t in taps or []:
                tx = t * 2.3 + 1.3 if t < n - 1 else end
                _line(ax, [tx + 0.15, tx + 0.15, ], [0.85, 1.55], color=col, lw=1.2) if False else None
            # tap from Q(n-2) drawn over the top to the XOR
            tx = (n - 2) * 2.3 + 1.3 + 0.5
            _line(ax, [tx, tx, -0.9, -0.9, cx - 0.22], [0.85, 1.55, 1.55, cy, cy], color=col, lw=1.2)
            ax.text(tx + 0.08, 1.38, "tap", fontsize=8, color=col)
    if title:
        ax.set_title(title, fontsize=9.5, color=MUTED, loc="left")
    return _svg(fig)


def ripple_counter():
    fig, ax = _canvas(8.2, 2.1, (-1.4, 7.4), (-0.9, 1.6))
    for i in range(3):
        x = i * 2.6
        _box(ax, x, 0, 1.3, 1.1, "", r=0.05)
        ax.text(x + 0.12, 0.8, "T=1", fontsize=8.5); ax.text(x + 1.18, 0.8, "Q", fontsize=9, ha="right")
        ax.text(x + 0.65, 1.22, f"Q{i}", ha="center", fontsize=9.5, weight="bold", color=ACC)
        ax.add_patch(Polygon([(x + 0.55, 0), (x + 0.65, 0.16), (x + 0.75, 0)], closed=True, fc="none", ec=INK, lw=1))
        ax.add_patch(Circle((x + 0.65, -0.07), 0.07, fc="white", ec=INK, lw=1))
        if i == 0:
            _line(ax, [-1.0, 0.65, 0.65], [-0.5, -0.5, -0.14]); ax.text(-1.05, -0.5, "CLK", ha="right", va="center", fontsize=9, color=MUTED)
        else:
            px = (i - 1) * 2.6 + 1.3
            _line(ax, [px, px + 0.45, px + 0.45, x + 0.65, x + 0.65], [0.85, 0.85, -0.5, -0.5, -0.14], color=G1, lw=1.4)
        _arrow(ax, (x + 1.3, 0.85), (x + 1.75, 0.85))
    ax.text(3.0, -0.8, "each flip-flop is clocked by the Q of the one before (negative edge, ○ = falling-edge input)",
            ha="center", fontsize=8.5, color=G1)
    return _svg(fig)


# ================================================================== timing analysis
def timing_path():
    fig, ax = _canvas(8.6, 2.9, (-0.3, 10.3), (-1.9, 1.5))
    _box(ax, 0, 0, 1.4, 1.2, "FF1", fs=10, weight="bold")
    ax.add_patch(FancyBboxPatch((3.0, 0.05), 3.0, 1.1, boxstyle="round,pad=0,rounding_size=0.5", fc=SOFT, ec=MUTED, lw=1.2))
    ax.text(4.5, 0.6, "combinational logic", ha="center", va="center", fontsize=9.5, color=MUTED)
    _box(ax, 7.6, 0, 1.4, 1.2, "FF2", fs=10, weight="bold")
    _arrow(ax, (1.4, 0.6), (3.0, 0.6)); _arrow(ax, (6.0, 0.6), (7.6, 0.6))
    ax.text(2.2, 0.75, "Q", fontsize=9); ax.text(6.8, 0.75, "D", fontsize=9)
    # budget bar
    segs = [("t_pd(FF) clk→Q", 0, 2.6, ACC), ("t_comb (longest path)", 2.6, 6.6, G1), ("t_su", 6.6, 8.0, BAD), ("slack", 8.0, 9.4, G2)]
    for lab, a, b, c in segs:
        ax.add_patch(Rectangle((a, -1.15), b - a, 0.45, fc=c, alpha=0.22, ec=c, lw=1.2))
        ax.text((a + b) / 2, -0.93, lab, ha="center", va="center", fontsize=8.3, color=INK)
    _line(ax, [0, 0], [-1.6, -0.55], color=MUTED); _line(ax, [9.4, 9.4], [-1.6, -0.55], color=MUTED)
    ax.text(0, -1.78, "clock edge n", ha="center", fontsize=8, color=MUTED)
    ax.text(9.4, -1.78, "clock edge n+1", ha="center", fontsize=8, color=MUTED)
    ax.text(4.7, -1.55, "T_clk ≥ t_pd + t_comb,max + t_su", ha="center", fontsize=9.5, weight="bold")
    return _svg(fig)


def setup_hold():
    fig, ax = _canvas(7.2, 2.0, (-0.5, 9.5), (-1.5, 1.2))
    _line(ax, [0, 4, 4, 9], [0.2, 0.2, 0.9, 0.9], color=MUTED, lw=1.6); ax.text(-0.15, 0.55, "CLK", ha="right", va="center", fontsize=9, color=MUTED)
    ax.add_patch(Rectangle((2.3, -1.2), 1.7, 2.3, fc=BAD, alpha=0.12, lw=0))
    ax.add_patch(Rectangle((4.0, -1.2), 1.0, 2.3, fc=G1, alpha=0.15, lw=0))
    ax.text(3.15, 1.0, "t_su", ha="center", fontsize=9, color=BAD, weight="bold")
    ax.text(4.5, 1.0, "t_h", ha="center", fontsize=9, color=G1, weight="bold")
    ax.plot([0, 1.6, 1.9, 6.0, 6.3, 9], [-0.2, -0.2, -0.85, -0.85, -0.2, -0.2], color=ACC, lw=1.6)
    ax.plot([0, 1.6, 1.9, 6.0, 6.3, 9], [-0.85, -0.85, -0.2, -0.2, -0.85, -0.85], color=ACC, lw=1.6)
    ax.text(-0.15, -0.52, "D", ha="right", va="center", fontsize=9.5, weight="bold")
    ax.text(7.4, -1.4, "D must not change inside the shaded window", ha="center", fontsize=8.5, color=MUTED)
    return _svg(fig)


# ================================================================== FSM
def fsm_block(mealy=False):
    fig, ax = _canvas(4.6, 2.2, (-0.9, 8.2), (-1.3, 2.2))
    _box(ax, 0, 0.3, 2.0, 1.2, "next-state\nlogic", fs=9)
    _box(ax, 3.0, 0.3, 1.8, 1.2, "state\nregister", fs=9, fc="#e8eefe", ec=ACC)
    _box(ax, 5.8, 0.3, 1.8, 1.2, "output\nlogic", fs=9)
    _arrow(ax, (2.0, 0.9), (3.0, 0.9)); _arrow(ax, (4.8, 0.9), (5.8, 0.9)); _arrow(ax, (7.6, 0.9), (8.1, 0.9))
    ax.text(8.1, 1.15, "z", fontsize=10, weight="bold")
    _line(ax, [5.3, 5.3, -0.4, -0.4], [0.9, -0.5, -0.5, 0.6]); _arrow(ax, (-0.4, 0.6), (0, 0.6))
    _arrow(ax, (-0.8, 1.2), (0, 1.2)); ax.text(-0.85, 1.2, "x", ha="right", va="center", fontsize=10, weight="bold")
    ax.text(3.9, 1.65, "CLK ▲", ha="center", fontsize=8, color=MUTED)
    if mealy:
        _line(ax, [-0.6, -0.6, 6.7], [1.2, 1.95, 1.95], color=G1, lw=1.6); _arrow(ax, (6.7, 1.95), (6.7, 1.5), color=G1, lw=1.6)
        ax.text(3.0, 2.05, "input also feeds the output logic", fontsize=8.3, color=G1)
    ax.text(3.9, -1.15, "Mealy:  z = f(state, x)" if mealy else "Moore:  z = f(state)", ha="center",
            fontsize=10, weight="bold", color=G1 if mealy else ACC)
    return _svg(fig)


def state_diagram(states, edges, size=(6.0, 2.6), lim=((-1, 9), (-1.4, 2.4)), r=0.5):
    """states: {name: (x, y, label_inside)}, edges: (a, b, label, rad) ; a == b -> self loop."""
    fig, ax = _canvas(*size, *lim)
    for nm, (x, y, inner) in states.items():
        ax.add_patch(Circle((x, y), r, fc="#e8eefe", ec=ACC, lw=1.5))
        ax.text(x, y, inner, ha="center", va="center", fontsize=9, weight="bold")
    for a, b, lab, rad in edges:
        (x1, y1, _), (x2, y2, _) = states[a], states[b]
        if a == b:
            up = 1 if rad >= 0 else -1
            ax.add_patch(FancyArrowPatch((x1 - 0.3, y1 + up * 0.4), (x1 + 0.3, y1 + up * 0.4),
                                         connectionstyle=f"arc3,rad={-1.6 * up}", arrowstyle="-|>,head_length=0.4,head_width=0.22",
                                         color=INK, lw=1.2, mutation_scale=10))
            ax.text(x1, y1 + up * 1.2, lab, ha="center", va="center", fontsize=8.6, color=G1)
            continue
        import math
        dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy); ux, uy = dx / d, dy / d
        p = (x1 + ux * r, y1 + uy * r); q = (x2 - ux * r, y2 - uy * r)
        _arrow(ax, p, q, rad=rad, lw=1.2)
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        off = -rad * d * 0.5
        ax.text(mx - uy * off, my + ux * off, lab, ha="center", va="center", fontsize=8.6, color=G1,
                bbox=dict(fc="white", ec="none", pad=0.6))
    return _svg(fig)


def mealy_010():
    st = {"S0": (0, 0, "S0"), "S1": (3.5, 0, "S1"), "S2": (7, 0, "S2")}
    ed = [("S0", "S0", "1/0", 1), ("S0", "S1", "0/0", 0.25), ("S1", "S1", "0/0", 1), ("S1", "S2", "1/0", 0.25),
          ("S2", "S1", "0/1", 0.25), ("S2", "S0", "1/0", -0.32)]
    return state_diagram(st, ed, size=(6.6, 3.2), lim=((-1, 8), (-2.4, 2.0)))


def moore_010():
    st = {"S0": (0, 0, "S0/0"), "S1": (3.3, 0, "S1/0"), "S2": (6.6, 0, "S2/0"), "S3": (9.9, 0, "S3/1")}
    ed = [("S0", "S0", "1", 1), ("S0", "S1", "0", 0.0), ("S1", "S1", "0", 1), ("S1", "S2", "1", 0.0),
          ("S2", "S3", "0", 0.25), ("S3", "S2", "1", 0.25), ("S3", "S1", "0", 0.42), ("S2", "S0", "1", -0.42)]
    return state_diagram(st, ed, size=(8.0, 3.8), lim=((-1, 11), (-3.0, 2.6)), r=0.55)


def asm_010():
    fig, ax = _canvas(5.2, 7.4, (-3.2, 5.0), (-11.5, 1.0))
    def sbox(y, name, out):
        _box(ax, -0.9, y, 1.8, 0.8, f"{name}\n{out}", fs=9, fc="#e8eefe", ec=ACC, r=0.02)
        ax.text(-1.0, y + 0.85, f"{name}", fontsize=0, alpha=0)
    def dia(y, lab="x"):
        ax.add_patch(Polygon([(0, y + 0.45), (0.75, y), (0, y - 0.45), (-0.75, y)], closed=True, fc="white", ec=INK, lw=1.3))
        ax.text(0, y, lab, ha="center", va="center", fontsize=9.5, weight="bold")
    ys = [0, -3, -6, -9]
    names = [("S0", "z=0"), ("S1", "z=0"), ("S2", "z=0"), ("S3", "z=1")]
    for y, (n, o) in zip(ys, names):
        sbox(y, n, o); _line(ax, [0, 0], [y, y - 0.6]); dia(y - 1.05)
    # exits: x = 0 goes down/right, x = 1 goes left
    # S0: 0 -> S1, 1 -> S0
    def lab(x, y, t): ax.text(x, y, t, fontsize=8.5, color=G1, weight="bold")
    _arrow(ax, (0, -1.5), (0, -3 + 0.8)); lab(0.1, -1.95, "0")
    _line(ax, [-0.75, -1.8, -1.8, -0.9], [-1.05, -1.05, 0.4, 0.4]); _arrow(ax, (-1.2, 0.4), (-0.9, 0.4)); lab(-1.3, -0.95, "1")
    # S1: 0 -> S1 (loop), 1 -> S2
    _arrow(ax, (0, -4.5), (0, -6 + 0.8)); lab(0.1, -4.95, "1")
    _line(ax, [0.75, 1.6, 1.6, 0.9], [-4.05, -4.05, -2.6, -2.6]); _arrow(ax, (1.2, -2.6), (0.9, -2.6)); lab(0.9, -3.95, "0")
    # S2: 0 -> S3, 1 -> S0
    _arrow(ax, (0, -7.5), (0, -9 + 0.8)); lab(0.1, -7.95, "0")
    _line(ax, [-0.75, -2.6, -2.6, -0.9], [-7.05, -7.05, 0.55, 0.55]); _arrow(ax, (-1.3, 0.55), (-0.9, 0.55)); lab(-1.3, -6.95, "1")
    # S3: 0 -> S1, 1 -> S2
    _line(ax, [0.75, 2.4, 2.4, 0.9], [-10.05, -10.05, -2.75, -2.75]); _arrow(ax, (1.2, -2.75), (0.9, -2.75)); lab(0.9, -9.95, "0")
    _line(ax, [0, 0, 3.3, 3.3, 0.9], [-10.5, -11.0, -11.0, -5.6, -5.6]); _arrow(ax, (1.2, -5.6), (0.9, -5.6)); lab(0.1, -10.85, "1")
    ax.text(2.6, 0.55, "state box = 1 clock\nMoore output inside", fontsize=8, color=MUTED)
    return _svg(fig)


# ================================================================== generators
def astable_555():
    import numpy as np
    fig, ax = plt.subplots(figsize=(7.6, 2.3))
    tau1, tau2 = 1.1, 1.0
    t, vc, out = [], [], []
    tt, v, state = 0.0, 1 / 3, 1
    while tt < 8:
        dt = 0.01
        if state:
            v = 1 - (1 - v) * np.exp(-dt / tau1)
            if v >= 2 / 3: state = 0
        else:
            v = v * np.exp(-dt / tau2)
            if v <= 1 / 3: state = 1
        t.append(tt); vc.append(v); out.append(state); tt += dt
    ax.plot(t, vc, color=ACC, lw=1.6, label="capacitor voltage")
    ax.plot(t, [1.15 + 0.4 * o for o in out], color=G1, lw=1.6, label="output")
    for y, lab in ((2 / 3, "⅔ V_CC"), (1 / 3, "⅓ V_CC")):
        ax.axhline(y, color=MUTED, lw=0.8, ls=(0, (3, 3))); ax.text(8.05, y, lab, va="center", fontsize=8.5, color=MUTED)
    ax.text(-0.1, 1.35, "OUT", ha="right", va="center", fontsize=9, weight="bold", color=G1)
    ax.text(-0.1, 0.5, "V_C", ha="right", va="center", fontsize=9, weight="bold", color=ACC)
    ax.set_xlim(-0.8, 8.8); ax.set_ylim(-0.25, 1.7); ax.axis("off")
    ax.text(0, -0.12, "rise: charge through R₁+R₂, t_H = 0.693(R₁+R₂)C      fall: discharge through R₂, t_L = 0.693·R₂·C", fontsize=8.3, color=MUTED)
    return _svg(fig)


def ring_osc():
    import schemdraw
    import schemdraw.logic as lg
    import schemdraw.elements as elm
    schemdraw.use("svg")
    d = schemdraw.Drawing(show=False)
    d.config(fontsize=11, color=INK, lw=1.3)
    d += (g1 := lg.Not().right())
    d += (g2 := lg.Not().right())
    d += (g3 := lg.Not().right())
    d += (g4 := lg.Not().right())
    d += (g5 := lg.Not().right())
    d += elm.Line().right(0.6).label("out", loc="right")
    d += elm.Line().down(1.4).at(g5.out)
    d += elm.Line().tox(g1.in1.x - 0.5)
    d += elm.Line().up(1.4)
    d += elm.Line().right(0.5)
    s = d.get_imagedata("svg").decode()
    return s[s.index("<svg"):]


# ================================================================== hazard
def hazard_kmap():
    ones = (1, 3, 4, 5, 9, 11, 13, 14, 15)
    cells = {m: "1" for m in ones}
    groups = [{"cells": [1, 3, 9, 11], "term": "B'D", "color": 0},
              {"cells": [1, 5, 9, 13], "term": "C'D", "color": 2},
              {"cells": [4, 5], "term": "A'BC'", "color": 3},
              {"cells": [14, 15], "term": "ABC", "color": 4},
              {"cells": [9, 11, 13, 15], "term": "AD  (added: hazard cover)", "color": 1}]
    return kmap_css_wrap(kfig.kmap(cells, groups, rv="AB", cv="CD", cs=50, show_idx=True))


def kmap_css_wrap(svg):
    return svg


def glitch():
    rows = [("A", [(0, 1)]), ("B", [(0, 1), (3, 0)]), ("term 1", [(0, 1), (3, 0)]),
            ("term 2", [(0, 0), (3.6, 1)]), ("F", [(0, 1), (3, 0), (3.6, 1)])]
    return waves(rows, 7, marks=[(3, "B falls", BAD), (3.6, "", BAD)], w=6.4,
                 shade=[(3, 3.6, BAD)])


# ================================================================== logic families
def noise_bands():
    fig, ax = _canvas(6.6, 3.3, (-0.4, 9.6), (-0.5, 5.6))
    def band(x, lo, hi, c, lab):
        ax.add_patch(Rectangle((x, lo), 2.4, hi - lo, fc=c, alpha=0.18, ec=c, lw=1))
        ax.text(x + 1.2, (lo + hi) / 2, lab, ha="center", va="center", fontsize=8.5)
    # output side (driver)
    band(0.5, 2.4, 5.0, G2, "valid HIGH out"); band(0.5, 0, 0.4, ACC, "LOW out")
    band(6.0, 2.0, 5.0, G2, "read as HIGH"); band(6.0, 0, 0.8, ACC, "read as LOW")
    ax.add_patch(Rectangle((6.0, 0.8), 2.4, 1.2, fc=BAD, alpha=0.10, ec=BAD, lw=1, ls="--"))
    ax.text(7.2, 1.4, "undefined", ha="center", va="center", fontsize=8.5, color=BAD)
    ax.text(1.7, 5.25, "driver output", ha="center", fontsize=9.5, weight="bold")
    ax.text(7.2, 5.25, "receiver input", ha="center", fontsize=9.5, weight="bold")
    for y, lab in ((2.4, "V_OH = 2.4"), (0.4, "V_OL = 0.4")):
        ax.text(0.45, y, lab, ha="right", va="center", fontsize=8.5)
    for y, lab in ((2.0, "V_IH = 2.0"), (0.8, "V_IL = 0.8")):
        ax.text(8.45, y, lab, ha="left", va="center", fontsize=8.5)
    _arrow(ax, (4.2, 2.0), (4.2, 2.4), color=G1); _arrow(ax, (4.2, 2.4), (4.2, 2.0), color=G1)
    ax.text(4.35, 2.2, "NM_H = 0.4 V", va="center", fontsize=8.8, color=G1, weight="bold")
    _arrow(ax, (4.2, 0.4), (4.2, 0.8), color=G1); _arrow(ax, (4.2, 0.8), (4.2, 0.4), color=G1)
    ax.text(4.35, 0.6, "NM_L = 0.4 V", va="center", fontsize=8.8, color=G1, weight="bold")
    _line(ax, [2.9, 6.0], [2.4, 2.4], color=MUTED, ls=":"); _line(ax, [2.9, 6.0], [2.0, 2.0], color=MUTED, ls=":")
    _line(ax, [2.9, 6.0], [0.4, 0.4], color=MUTED, ls=":"); _line(ax, [2.9, 6.0], [0.8, 0.8], color=MUTED, ls=":")
    ax.text(4.5, -0.4, "standard TTL, V_CC = 5 V (volts)", ha="center", fontsize=8.3, color=MUTED)
    return _svg(fig)


def fanout_fig():
    fig, ax = _canvas(7.4, 2.9, (-0.5, 11), (-2.5, 1.9))
    _box(ax, 0, -0.5, 1.6, 1.0, "driver\n(LOW)", fs=9, fc="#e8eefe", ec=ACC)
    _line(ax, [1.6, 3.0], [0, 0])
    for i, y in enumerate([1.3, 0.45, -0.45, -1.3]):
        _line(ax, [3.0, 3.0, 5.3], [0, y, y], color=MUTED)
        _box(ax, 5.3, y - 0.3, 1.3, 0.6, f"load {i+1}" if i < 3 else "load N", fs=8.5)
        _arrow(ax, (4.7, y + 0.12), (3.7, y + 0.12), color=G1, lw=1.1)
    ax.text(4.2, 1.6, "I_IL = 1.6 mA each", fontsize=8.3, color=G1, ha="center")
    ax.text(0.0, -2.3, "LOW output must SINK  N × I_IL ≤ I_OL = 16 mA  →  N ≤ 10", fontsize=9, ha="left", weight="bold")
    return _svg(fig)


def tristate_bus():
    fig, ax = _canvas(6.6, 2.9, (-0.5, 10.5), (-2.4, 2.2))
    _line(ax, [0, 10], [-1.6, -1.6], lw=2.6, color=INK); ax.text(10.1, -1.6, "BUS", va="center", fontsize=9.5, weight="bold")
    for i, (lab, en) in enumerate((("A", 0), ("B", 1), ("C", 0))):
        x = 1.0 + i * 3.2
        c = G2 if en else MUTED
        ax.add_patch(Polygon([(x, 0.9), (x + 1.0, 0.4), (x, -0.1)], closed=True, fc="white", ec=c, lw=1.5))
        _line(ax, [x - 0.6, x], [0.4, 0.4], color=c); ax.text(x - 0.7, 0.4, lab, ha="right", va="center", fontsize=10, weight="bold")
        _line(ax, [x + 1.0, x + 1.5, x + 1.5], [0.4, 0.4, -1.6], color=c, lw=1.5 if en else 1, ls="-" if en else (0, (3, 3)))
        _line(ax, [x + 0.5, x + 0.5], [0.65, 1.5], color=c); ax.text(x + 0.5, 1.6, f"EN={en}", ha="center", fontsize=8.5, color=c)
        ax.text(x + 1.6, -0.6, "drives" if en else "Hi-Z", fontsize=8.5, color=c, weight="bold")
    ax.text(5.0, -2.25, "exactly one enable is 1 at a time; disabled outputs float (high impedance)", ha="center", fontsize=8.5, color=MUTED)
    return _svg(fig)


def ecl_gate():
    import schemdraw
    import schemdraw.elements as elm
    schemdraw.use("svg")
    d = schemdraw.Drawing(show=False)
    d.config(fontsize=11, color=INK, lw=1.3, unit=2.2)
    d += (q1 := elm.BjtNpn(circle=True).label("Q1", loc="left"))
    d += elm.Line().left(1).at(q1.base).label("A", loc="left")
    d += elm.Line().right(2.6).at(q1.emitter)
    d += (q2 := elm.BjtNpn(circle=True).reverse().anchor("emitter").label("Q2", loc="right"))
    d += elm.Line().right(1).at(q2.base).label("VBB (ref)", loc="right")
    d += elm.Resistor().down().at((q1.emitter[0] + 1.3, q1.emitter[1])).label("RE", loc="bottom")
    d += elm.Label().label("VEE = −5.2 V", loc="bottom")
    d += elm.Resistor().up().at(q1.collector).label("RC1", loc="top")
    d += elm.Ground().flip().label("VCC = 0 V", loc="right")
    d += elm.Resistor().up().at(q2.collector).label("RC2", loc="top")
    d += elm.Ground().flip()
    d += elm.Line().left(0.9).at(q1.collector).label("NOR side", loc="left")
    d += elm.Line().right(0.9).at(q2.collector).label("OR side", loc="right")
    s = d.get_imagedata("svg").decode()
    return s[s.index("<svg"):]


def dram_cell():
    fig, ax = _canvas(3.2, 3.2, (-2.2, 3.4), (-3.0, 2.6))
    _line(ax, [0, 0], [2.4, 0.9], color=G2, lw=1.8); ax.text(0.15, 2.3, "bit line", fontsize=9, color=G2)
    _line(ax, [0, 0.45, 0.45], [0.9, 0.9, 0.7]); _line(ax, [0.45, 0.45], [-0.7, -0.5])
    _line(ax, [0.45, 0.45], [0.75, -0.75], lw=2.2)          # channel
    _line(ax, [0.75, 0.75], [0.6, -0.6], lw=2.2)            # gate plate
    _line(ax, [0.75, 2.6], [0, 0], color=G1, lw=1.8); ax.text(1.2, 0.18, "word line", fontsize=9, color=G1)
    _line(ax, [0.45, 0, 0], [-0.7, -0.7, -1.4])
    _line(ax, [-0.5, 0.5], [-1.4, -1.4], lw=2.2); _line(ax, [-0.5, 0.5], [-1.65, -1.65], lw=2.2)
    _line(ax, [0, 0], [-1.65, -2.2])
    for i, w in enumerate((0.5, 0.33, 0.16)):
        _line(ax, [-w, w], [-2.2 - i * 0.15] * 2)
    ax.text(0.65, -1.55, "C: the bit\nis charge", fontsize=8.5, va="center")
    ax.text(-0.25, 0.0, "access\nNMOS", fontsize=8.3, ha="right", va="center", color=MUTED)
    return _svg(fig)


def memory_org():
    fig, ax = _canvas(6.6, 3.4, (-0.6, 10.3), (-2.4, 3.6))
    _box(ax, 0, -0.3, 1.8, 3.2, "row\ndecoder", fs=9, fc="#e8eefe", ec=ACC)
    ax.text(-0.15, 1.3, "address\n(k lines)", ha="right", va="center", fontsize=8.5)
    _arrow(ax, (-0.1, 1.3), (0, 1.3))
    for r in range(4):
        y = 2.5 - r * 0.8
        _line(ax, [1.8, 8.4], [y, y], color=G1, lw=1.2)
        for c in range(4):
            x = 3.0 + c * 1.5
            ax.add_patch(Rectangle((x - 0.25, y - 0.25), 0.5, 0.5, fc=SOFT, ec=MUTED, lw=1))
    for c in range(4):
        _line(ax, [3.3 + c * 1.5, 3.3 + c * 1.5], [2.9, -0.8], color=G2, lw=1.2)
    _box(ax, 2.6, -1.5, 5.6, 0.6, "sense amplifiers / write drivers", fs=8.5)
    ax.text(5.4, -2.15, "data (m lines)", ha="center", fontsize=8.5)
    _arrow(ax, (5.4, -1.5), (5.4, -1.95))
    ax.text(8.6, 2.5, "word line", va="center", fontsize=8.5, color=G1)
    ax.text(7.8, 3.2, "bit lines", fontsize=8.5, color=G2)
    ax.text(5.4, 3.35, "2ᵏ words × m bits", ha="center", fontsize=9.5, weight="bold")
    return _svg(fig)


def pld_arrays():
    fig, axs = plt.subplots(1, 3, figsize=(9.0, 2.7))
    for ax, (name, andp, orp) in zip(axs, (("PROM", "fixed", "prog"), ("PLA", "prog", "prog"), ("PAL", "prog", "fixed"))):
        ax.set_xlim(-0.5, 7.5); ax.set_ylim(-0.6, 5.2); ax.set_aspect("equal"); ax.axis("off")
        for i in range(3):
            _line(ax, [i * 0.8 + 0.3] * 2, [0.2, 4.4], color=MUTED, lw=1)
        for j in range(4):
            y = 0.6 + j * 1.0
            _line(ax, [0, 2.4], [y, y], color=MUTED, lw=1)
            for i in range(3):
                if andp == "prog":
                    ax.text(i * 0.8 + 0.3, y, "×", ha="center", va="center", fontsize=13, color=G1, weight="bold")
                elif (j + i) % 2 == 0:
                    ax.plot(i * 0.8 + 0.3, y, "o", ms=3.5, color=INK)
            _line(ax, [2.4, 6.6], [y, y], color=MUTED, lw=1)
        for k in range(2):
            x = 3.6 + k * 1.6
            _line(ax, [x, x], [0.2, 4.4], color=MUTED, lw=1)
            for j in range(4):
                y = 0.6 + j * 1.0
                if orp == "prog":
                    ax.text(x, y, "×", ha="center", va="center", fontsize=13, color=G1, weight="bold")
                elif (j // 2) == k:
                    ax.plot(x, y, "o", ms=3.5, color=INK)
        ax.text(1.1, 4.75, "AND", ha="center", fontsize=8.5, color=G1 if andp == "prog" else MUTED, weight="bold")
        ax.text(4.4, 4.75, "OR", ha="center", fontsize=8.5, color=G1 if orp == "prog" else MUTED, weight="bold")
        ax.set_title(name, fontsize=11, weight="bold", color=ACC)
        ax.text(3.5, -0.45, f"AND {andp} · OR {orp}".replace("prog", "programmable"), ha="center", fontsize=7.8, color=MUTED)
    fig.text(0.5, -0.02, "× = programmable connection     ● = fixed connection", ha="center", fontsize=8.5, color=MUTED)
    return _svg(fig)


def pla_impl():
    """F1 = AB' + AC, F2 = BC + AC on a 3-input, 3-product, 2-output PLA."""
    fig, ax = _canvas(6.4, 3.4, (-1.2, 10.4), (-1.4, 5.0))
    lits = ["A", "A'", "B", "B'", "C", "C'"]
    prods = [("P1 = AB'", {"A", "B'"}), ("P2 = AC", {"A", "C"}), ("P3 = BC", {"B", "C"})]
    for i, l in enumerate(lits):
        x = i * 0.7
        _line(ax, [x, x], [0.0, 4.2], color=MUTED, lw=1); ax.text(x, 4.4, l, ha="center", fontsize=9, weight="bold")
    for j, (pn, s) in enumerate(prods):
        y = 3.4 - j * 1.2
        _line(ax, [-0.3, 7.6], [y, y], color=MUTED, lw=1); ax.text(-0.4, y, pn, ha="right", va="center", fontsize=8.5, color=G1)
        for i, l in enumerate(lits):
            if l in s:
                ax.plot(i * 0.7, y, "o", ms=6, color=G1)
    for k, (fn, uses) in enumerate((("F1", (0, 1)), ("F2", (1, 2)))):
        x = 5.4 + k * 1.6
        _line(ax, [x, x], [0.0, 4.2], color=MUTED, lw=1); ax.text(x, -0.4, fn, ha="center", fontsize=10, weight="bold", color=ACC)
        for j in uses:
            ax.plot(x, 3.4 - j * 1.2, "o", ms=6, color=ACC)
    ax.text(4.5, -1.15, "AC is generated once and shared by both outputs", ha="center", fontsize=8.5, color=MUTED)
    return _svg(fig)


def commons(fname, w=260):
    import base64
    p = Path(__file__).resolve().parent / "img" / fname
    b = base64.b64encode(p.read_bytes()).decode()
    return f'<img class="img" style="max-width:{w}px" src="data:image/svg+xml;base64,{b}"/>'


def ripple_waves():
    d = 0.12
    edges = [2 * k + 2 for k in range(8)]          # falling CLK edges at t = 2, 4, ...
    def toggles(src_falls, delay):
        lev, out, falls = 0, [(0, 0)], []
        for t in src_falls:
            lev ^= 1; out.append((t + delay, lev))
            if lev == 0: falls.append(t + delay)
        return out, falls
    clk_pts = [(0, 1)] + [(t, v) for k in range(8) for t, v in ((2 * k + 1, 1), (2 * k + 2, 0))]
    clk_pts = [(0, 0)] + [p for k in range(8) for p in ((2 * k + 1, 1), (2 * k + 2, 0))]
    q0, f0 = toggles(edges, d * 2)
    q1, f1 = toggles(f0, d * 2)
    q2, _ = toggles(f1, d * 2)
    return waves([("CLK", clk_pts), ("Q0", q0), ("Q1", q1), ("Q2", q2)], 17,
                 shade=[(8, 8 + 6 * d, BAD)], marks=[(8, "edge 4: 011 → 100", BAD)], w=8.6)


def johnson_waves():
    rows = [("CLK", [(0, 0)] + [p for k in range(9) for p in ((2 * k + 1, 1), (2 * k + 2, 0))])]
    for i in range(4):
        rows.append((f"Q{i}", [(0, 0), (2 * i + 1, 1), (2 * i + 9, 0)]))
    return waves(rows, 18, w=8.6, marks=[(1, "", MUTED), (17, "repeats", MUTED)])


def ttl_nand():
    return commons("7400_Circuit.svg", 330) + ('<div class="prov">Standard 7400 TTL NAND, totem-pole output · Wikimedia Commons, CC BY 2.0 de. '
        'German labels: V₁…V₄ = transistors Q1…Q4, V₅ = diode D, U = voltage.</div>')
