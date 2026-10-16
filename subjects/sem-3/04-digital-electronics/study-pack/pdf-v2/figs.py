"""Figures for the v2 demo chapter. Large type, one idea per figure. Every function returns inline SVG."""
import io
import re

import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, FancyArrowPatch, Rectangle

INK, MUTED, FAINT, SOFT = "#1c1f24", "#7a808a", "#c9ccd2", "#f3f3ef"
ACC, ACC_SOFT, G1, G2, BAD = "#2f5bea", "#e8eefe", "#e0661b", "#12925a", "#d92d20"

plt.rcParams.update({"font.family": ["Segoe UI", "DejaVu Sans"], "font.size": 13, "svg.fonttype": "none",
                     "text.color": INK})


def _svg(fig):
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", pad_inches=0.05, transparent=True)
    plt.close(fig)
    s = buf.getvalue()
    s = s[s.index("<svg"):]
    return re.sub(r'width="[\d.]+pt" height="[\d.]+pt"', 'class="mpl"', s, count=1)


def _canvas(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def _pill(ax, x, y, w, h, text, state="future", fs=12, num=None):
    fc, ec, col, ls, lw = {"done": (SOFT, FAINT, MUTED, "-", 1.2), "now": (ACC_SOFT, ACC, INK, "-", 2.2),
                           "future": ("white", FAINT, MUTED, (0, (3, 3)), 1.2)}[state]
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={h/2}", fc=fc, ec=ec, lw=lw, ls=ls))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=col,
            weight="bold" if state == "now" else "normal")
    if num is not None:
        ax.add_patch(Circle((x - 0.05, y + h), 0.3, fc=ACC if state == "now" else ("white" if state == "future" else FAINT),
                            ec=ACC if state == "now" else FAINT, lw=1.2))
        ax.text(x - 0.05, y + h, str(num), ha="center", va="center", fontsize=11,
                color="white" if state == "now" else MUTED, weight="bold")


def _arrow(ax, p, q, color=INK, lw=1.5, rad=0.0, ls="-"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>,head_length=0.45,head_width=0.25", connectionstyle=f"arc3,rad={rad}",
                                 color=color, lw=lw, ls=ls, shrinkA=0, shrinkB=0, mutation_scale=12))


def _line(ax, xs, ys, color=INK, lw=1.5, ls="-"):
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, solid_capstyle="round")


# ------------------------------------------------------------------ staircase maps
def staircase(labels, now, w=6.2, note=None):
    """Staircase river: each stop strictly lower than the one before (staircase rule)."""
    n = len(labels)
    step_x, step_y, pw, ph = 1.0, 1.0, 5.2, 0.78
    xr = step_x * (n - 1) + pw + (5.0 if note else 0.4)
    fig, ax = _canvas(w, 0.75 * n + 0.4, (-0.6, xr), (-step_y * (n - 1) - 0.4, ph + 0.5))
    for i, lab in enumerate(labels):
        x, y = i * step_x, -i * step_y
        st = "done" if i < now else ("now" if i == now else "future")
        if i:
            px, py = (i - 1) * step_x, -(i - 1) * step_y
            _arrow(ax, (px + 0.55, py), (x - 0.02, y + ph / 2), color=ACC if i <= now else FAINT, lw=1.4,
                   ls="-" if i <= now else (0, (3, 3)))
        _pill(ax, x, y, pw, ph, lab, st, num=i + 1, fs=14)
    if note:
        ax.text(now * step_x + pw + 0.35, -now * step_y + ph / 2, note, va="center", fontsize=14, color=ACC, weight="bold")
    return _svg(fig)


def bridge(a, b, word):
    fig, ax = _canvas(7.2, 1.5, (-0.2, 11.2), (-0.6, 1.4))
    _pill(ax, 0, 0, 3.6, 0.9, a, "done", fs=13)
    _pill(ax, 7.4, 0, 3.6, 0.9, b, "now", fs=13)
    _arrow(ax, (3.75, 0.45), (7.25, 0.45), color=G1, lw=2.2)
    ax.text(5.5, 0.82, word, ha="center", fontsize=12, color=G1, weight="bold")
    return _svg(fig)


# ------------------------------------------------------------------ flip-flop primitives
def _ff(ax, x, y, label=None, w=1.5, h=1.3, qbar=False, dlab="D", qlab="Q"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.06", fc="white", ec=INK, lw=1.6))
    ax.text(x + 0.14, y + h - 0.32, dlab, fontsize=12)
    ax.text(x + w - 0.14, y + h - 0.32, qlab, fontsize=12, ha="right")
    ax.add_patch(Polygon([(x + w / 2 - 0.13, y), (x + w / 2, y + 0.2), (x + w / 2 + 0.13, y)], closed=True, fc="none", ec=INK, lw=1.3))
    if label:
        ax.text(x + w / 2, y + h + 0.22, label, ha="center", fontsize=13, weight="bold", color=ACC)


def dff_symbol():
    fig, ax = _canvas(4.2, 2.4, (-1.6, 4.2), (-1.3, 2.0))
    _ff(ax, 0, 0, w=2.0, h=1.6)
    _arrow(ax, (-1.2, 1.28), (0, 1.28)); ax.text(-1.3, 1.28, "D", ha="right", va="center", fontsize=14, weight="bold")
    _arrow(ax, (2.0, 1.28), (3.2, 1.28)); ax.text(3.3, 1.28, "Q", va="center", fontsize=14, weight="bold", color=ACC)
    _line(ax, [-1.2, 1.0, 1.0], [-0.7, -0.7, 0]); ax.text(-1.3, -0.7, "CLK", ha="right", va="center", fontsize=12, color=MUTED)
    ax.text(1.0, -1.15, "▲ = acts only at the clock's rising edge", ha="center", fontsize=10.5, color=MUTED)
    return _svg(fig)


def waves(rows, n, w=8.0, edges=(), notes=(), shade=()):
    """rows: (name, [(t, level), ...], color)."""
    fig, ax = plt.subplots(figsize=(w, 0.72 * len(rows) + 0.5))
    ax.set_xlim(-1.3, n + 0.2); ax.set_ylim(-0.75 * len(rows), 0.55); ax.axis("off")
    for (a, b, c) in shade:
        ax.add_patch(Rectangle((a, -0.75 * len(rows) + 0.15), b - a, 0.75 * len(rows) + 0.3, fc=c, alpha=0.12, lw=0))
    for t in edges:
        ax.axvline(t, color=FAINT, lw=1, ls=(0, (2, 3)), ymax=0.97)
    for r, (name, pts, col) in enumerate(rows):
        y0 = -0.75 * r
        ax.text(-0.3, y0 - 0.22, name, ha="right", va="center", fontsize=12.5, weight="bold", color=col)
        if pts is None:
            continue
        xs, ys = [], []
        for k, (t, v) in enumerate(pts):
            if k:
                xs.append(t); ys.append(ys[-1])
            xs.append(t); ys.append(v)
        xs.append(n); ys.append(ys[-1])
        ax.plot(xs, [y0 - 0.45 + 0.45 * v for v in ys], color=col, lw=2.0, solid_joinstyle="miter")
    for (x, txt) in notes:
        ax.text(x, 0.35, txt, ha="center", fontsize=10.5, color=G1, weight="bold")
    return _svg(fig)


def clock(n_cycles):
    return [(0, 0)] + [p for k in range(n_cycles) for p in ((2 * k + 1, 1), (2 * k + 2, 0))]


def dff_waves(answer=False):
    d = [(0, 0), (0.6, 1), (3.4, 0), (4.4, 1), (5.4, 0), (8.6, 1)]
    q = [(0, 0), (1, 1), (7, 0), (9, 1)]
    rows = [("CLK", clock(5), MUTED), ("D", d, INK), ("Q", q if answer else None, ACC)]
    return waves(rows, 10, edges=[1, 3, 5, 7, 9], w=8.4)


def check1_waves(answer=False):
    d = [(0, 1), (2.4, 0), (3.6, 1), (4.2, 0), (6.5, 1)]
    q = [(0, 0), (1, 1), (3, 0), (7, 1)]
    rows = [("CLK", clock(4), MUTED), ("D", d, INK), ("Q", q if answer else None, ACC)]
    return waves(rows, 8.6, edges=[1, 3, 5, 7], w=8.0,
                 shade=[(3.6, 4.2, G1)] if answer else ())


# ------------------------------------------------------------------ registers
def register():
    fig, ax = _canvas(8.4, 3.0, (-1.6, 13.2), (-1.6, 3.2))
    for i in range(4):
        x = i * 3.4
        _ff(ax, x, 0, label=None)
        _line(ax, [x - 0.5, x - 0.5, x], [2.4, 1.0, 1.0]); ax.text(x - 0.5, 2.6, f"D{i}", ha="center", fontsize=12, weight="bold")
        _line(ax, [x + 1.5, x + 1.9, x + 1.9], [1.0, 1.0, 2.4], color=ACC); ax.text(x + 1.9, 2.6, f"Q{i}", ha="center", fontsize=12, weight="bold", color=ACC)
        _line(ax, [x + 0.75, x + 0.75], [-0.75, 0], color=MUTED)
    _line(ax, [-1.2, 3 * 3.4 + 0.75], [-0.75, -0.75], color=MUTED)
    ax.text(-1.3, -0.75, "CLK", ha="right", va="center", fontsize=12, color=MUTED)
    ax.text(5.8, -1.35, "one shared clock → at one edge, every Q copies its own D", ha="center", fontsize=11.5, color=MUTED)
    return _svg(fig)


def chain(kind="shift", n=4):
    fig, ax = _canvas(8.6, 3.0, (-1.8, 2.8 * n - 0.6), (-1.75, 2.0))
    for i in range(n):
        x = i * 2.8
        _ff(ax, x, 0, label=f"Q{i}")
        _line(ax, [x + 0.75, x + 0.75], [-0.6, 0], color=MUTED)
        if i < n - 1:
            _arrow(ax, (x + 1.5, 1.0), (x + 2.8, 1.0), color=ACC if kind == "shift" else INK)
    _line(ax, [-1.2, (n - 1) * 2.8 + 0.75], [-0.6, -0.6], color=MUTED)
    ax.text(-1.3, -0.6, "CLK", ha="right", va="center", fontsize=12, color=MUTED)
    end = (n - 1) * 2.8 + 1.5
    if kind == "shift":
        _arrow(ax, (-1.3, 1.0), (0, 1.0)); ax.text(-1.35, 1.35, "serial in", ha="center", fontsize=10.5)
        _arrow(ax, (end, 1.0), (end + 0.9, 1.0)); ax.text(end + 0.5, 1.35, "serial out", ha="center", fontsize=10.5)
    else:
        col = G2 if kind == "ring" else G1
        _line(ax, [end, end + 0.45, end + 0.45, -0.7, -0.7], [1.0, 1.0, -1.2, -1.2, 1.0], color=col, lw=2.2)
        _arrow(ax, (-0.7, 1.0), (0, 1.0), color=col, lw=2.2)
        ax.text((end - 0.7) / 2, -1.6, "last Q → first D" if kind == "ring" else "last Q, inverted (Q3′) → first D",
                ha="center", fontsize=11.5, color=col, weight="bold")
        if kind == "johnson":
            ax.add_patch(Circle((end + 0.45, -0.1), 0.17, fc="white", ec=col, lw=2))
            ax.text(end + 0.75, -0.1, "NOT", va="center", fontsize=10, color=col, weight="bold")
    return _svg(fig)


def johnson_waves():
    rows = [("CLK", clock(9), MUTED)] + [(f"Q{i}", [(0, 0), (2 * i + 1, 1), (2 * i + 9, 0)], ACC) for i in range(4)]
    return waves(rows, 18, w=8.8, edges=[1, 17], notes=[(9, "8 clocks = one full cycle")])


def two_loops():
    main = ["0000", "1000", "1100", "1110", "1111", "0111", "0011", "0001"]
    lock = ["0100", "1010", "1101", "0110", "1011", "0101", "0010", "1001"]
    import math
    fig, ax = _canvas(9.0, 4.2, (-4.4, 15.4), (-4.2, 4.6))
    for cx, states, col, title in ((0, main, ACC, "the 8 states\nyou want"), (11.0, lock, BAD, "the other 8:\nstuck here")):
        r = 3.1
        pts = []
        for k in range(8):
            a = math.pi / 2 - 2 * math.pi * k / 8
            pts.append((cx + r * math.cos(a), r * math.sin(a)))
        for k in range(8):
            (x1, y1), (x2, y2) = pts[k], pts[(k + 1) % 8]
            dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy); sh = 0.62
            _arrow(ax, (x1 + dx / d * sh, y1 + dy / d * sh), (x2 - dx / d * sh, y2 - dy / d * sh), color=col, lw=1.3, rad=-0.15)
        for (x, y), st in zip(pts, states):
            ax.text(x, y, st, ha="center", va="center", fontsize=12.5, family="Consolas", color=col, weight="bold",
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=col, lw=1.4))
        ax.text(cx, 0, title, ha="center", va="center", fontsize=13, color=col, weight="bold")
    return _svg(fig)


def decode_gate():
    fig, ax = _canvas(5.4, 1.9, (-1.6, 6.6), (-1.0, 1.9))
    ax.add_patch(Polygon([(0, -0.6), (1.0, -0.6), (1.0, 1.4), (0, 1.4)], closed=True, fc="none", ec="none"))
    import numpy as np
    th = np.linspace(-np.pi / 2, np.pi / 2, 40)
    _line(ax, [0, 0, 0.9], [-0.6, 1.4, 1.4]); _line(ax, [0, 0.9], [-0.6, -0.6])
    ax.plot(0.9 + 1.0 * np.cos(th), 0.4 + 1.0 * np.sin(th), color=INK, lw=1.5)
    for y, lab in ((0.95, "Q1"), (-0.15, "Q2′")):
        _line(ax, [-1.0, 0], [y, y]); ax.text(-1.1, y, lab, ha="right", va="center", fontsize=13, weight="bold")
    _arrow(ax, (1.9, 0.4), (3.0, 0.4)); ax.text(3.1, 0.4, "= 1 only in state 1100", va="center", fontsize=12, color=ACC, weight="bold")
    return _svg(fig)
