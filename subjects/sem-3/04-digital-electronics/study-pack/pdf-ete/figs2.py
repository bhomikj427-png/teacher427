"""Figures for DE-ETE-v1.pdf, Parts C-E (sequential logic, state machines, logic families).

New figures only; the shift-register, timing, FSM-block, logic-family, memory and PLD figures come from
../pdf/figs.py through figs1. Waveforms are produced by the same simulation (qm.py) that verify.py checks.
"""
import math

from matplotlib.patches import Polygon, Circle, Rectangle, FancyBboxPatch, Ellipse

import figs1 as f1
import qm

v1 = f1.v1
INK, MUTED, LINE, SOFT, ACC, G1, G2, G3, BAD, TINT = f1.INK, f1.MUTED, f1.LINE, f1.SOFT, f1.ACC, f1.G1, f1.G2, f1.G3, f1.BAD, f1.TINT
_svg, _nat, _canvas, _box, _arrow, _line = f1._svg, f1._nat, f1._canvas, f1._box, f1._arrow, f1._line
lg, elm = f1.lg, f1.elm

# ------------------------------------------------------------------ waveform data (shared with verify.py)
CLK6 = [(0, 0)] + [p for k in range(6) for p in ((2 * k + 1, 1), (2 * k + 2, 0))]
RISE, FALL = [1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12]
HIGHS = [(t, t + 1) for t in RISE]
W_D = [(0, 0), (1.5, 1), (2.5, 0), (4.5, 1), (5.35, 0), (5.7, 1), (6.5, 0), (9.5, 1), (10.5, 0)]
W_J = [(0, 1), (2.5, 0), (4.5, 1), (8.5, 0)]
W_K = [(0, 0), (2.5, 1), (6.5, 0), (8.5, 1), (10.5, 0)]
W_T = [(0, 1), (3.5, 0), (6.5, 1), (10.5, 0)]


def latch_vs_ff():
    ql = qm.compress(qm.d_latch(W_D, HIGHS))
    qf = qm.compress(qm.edge_ff("D", {"D": W_D}, RISE))
    return v1.waves([("CLK", CLK6), ("D", W_D), ("Q latch", ql), ("Q flip-flop", qf)], 12.6, w=8.2,
                    shade=[(a, b, G1) for a, b in HIGHS], marks=[(t, "↑", MUTED) for t in RISE])


def jk_wave(edge="pos", show_q=True):
    q = qm.compress(qm.edge_ff("JK", {"J": W_J, "K": W_K}, RISE if edge == "pos" else FALL))
    rows = [("CLK", CLK6), ("J", W_J), ("K", W_K)] + ([("Q", q)] if show_q else [("Q", [(0, 0)])])
    return v1.waves(rows, 12.6, w=8.2, marks=[(t, "↑" if edge == "pos" else "↓", G1) for t in (RISE if edge == "pos" else FALL)])


def t_wave():
    q = qm.compress(qm.edge_ff("T", {"T": W_T}, FALL))
    return v1.waves([("CLK", CLK6), ("T", W_T), ("Q", q)], 12.6, w=8.2, marks=[(t, "↓", G1) for t in FALL])


# ------------------------------------------------------------------ latches and flip-flops
def sr_latch():
    d = f1._d()
    g1 = d.add(lg.Nor().right().at((3, 1.3)).anchor("out"))
    g2 = d.add(lg.Nor().right().at((3, -1.3)).anchor("out"))
    d += elm.Line().endpoints((0.2, g1.in1[1]), g1.in1).label("R", loc="left")
    d += elm.Line().endpoints((0.2, g2.in2[1]), g2.in2).label("S", loc="left")
    d += elm.Line().endpoints(g1.out, (4.6, 1.3)).label("Q", loc="right")
    d += elm.Line().endpoints(g2.out, (4.6, -1.3)).label("Q'", loc="right")
    for (ox, oy), pin in (((3.7, 1.3), g2.in1), ((3.7, -1.3), g1.in2)):
        s = 1 if oy > 0 else -1
        d += lg.Dot().at((ox, oy))
        for a, b in (((ox, oy), (ox, s * 0.55)), ((ox, s * 0.55), (0.7, -s * 0.3)), ((0.7, -s * 0.3), (0.7, pin[1])), ((0.7, pin[1]), pin)):
            d += elm.Line().endpoints(a, b)
    return f1._sd(d, 70)


def ff_symbols():
    fig, ax = _canvas(8.4, 2.2, (-1.2, 17.6), (-2.2, 2.6))
    specs = [("SR", ("S", "R"), "Q⁺ = S + R'Q   (SR = 0)"), ("D", ("D",), "Q⁺ = D"), ("JK", ("J", "K"), "Q⁺ = JQ' + K'Q"), ("T", ("T",), "Q⁺ = T ⊕ Q")]
    for i, (name, ins, eq) in enumerate(specs):
        x = i * 4.7
        _box(ax, x, 0, 2.2, 2.2, "", ec=ACC, r=0.06)
        ys = (1.75, 0.45) if len(ins) == 2 else (1.75,)
        for y, t in zip(ys, ins):
            _line(ax, [x - 0.6, x], [y, y]); ax.text(x + 0.15, y, t, va="center", fontsize=9.5, weight="bold")
        ax.add_patch(Polygon([(x, 0.9), (x + 0.3, 1.1), (x, 1.3)], closed=True, fc="none", ec=INK, lw=1.1))
        _line(ax, [x - 0.6, x], [1.1, 1.1], color=MUTED); ax.text(x - 0.65, 1.1, "CLK", ha="right", va="center", fontsize=7.5, color=MUTED)
        _line(ax, [x + 2.2, x + 2.8], [1.75, 1.75]); ax.text(x + 2.05, 1.75, "Q", ha="right", va="center", fontsize=9.5, weight="bold")
        _line(ax, [x + 2.2, x + 2.8], [0.45, 0.45]); ax.text(x + 2.05, 0.45, "Q'", ha="right", va="center", fontsize=9.5, weight="bold")
        ax.text(x + 1.1, 2.4, name + " flip-flop", ha="center", fontsize=9, color=ACC, weight="bold")
        ax.text(x + 1.1, -0.55, eq, ha="center", fontsize=8.6, weight="bold")
    ax.text(0, -1.5, "▷ on the clock pin = edge-triggered (a bubble ○ in front of it = negative edge). Q⁺ = Q after the clock edge.", fontsize=8.3, color=MUTED)
    return _svg(fig)


def ms_jk():
    fig, ax = _canvas(7.4, 2.4, (-1.6, 12.6), (-1.9, 2.9))
    _box(ax, 1.2, 0, 2.6, 2.0, "master\nJK latch\nopen: CLK = 1", fc=TINT, ec=ACC, fs=8.5)
    _box(ax, 6.2, 0, 2.6, 2.0, "slave\nSR latch\nopen: CLK = 0", fc="#eaf6ef", ec=G2, fs=8.5)
    for y, t in ((1.6, "J"), (0.4, "K")):
        _arrow(ax, (0.2, y), (1.2, y)); ax.text(0.1, y, t, ha="right", va="center", fontsize=10, weight="bold")
    _arrow(ax, (3.8, 1.6), (6.2, 1.6)); _arrow(ax, (3.8, 0.4), (6.2, 0.4))
    _arrow(ax, (8.8, 1.6), (10.2, 1.6)); ax.text(10.3, 1.6, "Q", va="center", fontsize=10, weight="bold", color=ACC)
    _arrow(ax, (8.8, 0.4), (10.2, 0.4)); ax.text(10.3, 0.4, "Q'", va="center", fontsize=10, weight="bold", color=ACC)
    _line(ax, [-1.2, 2.5, 2.5], [-1.2, -1.2, 0], color=G1); ax.text(-1.25, -1.2, "CLK", ha="right", va="center", fontsize=9, color=G1, weight="bold")
    _line(ax, [2.5, 4.6], [-1.2, -1.2], color=G1)
    ax.add_patch(Polygon([(4.6, -0.85), (4.6, -1.55), (5.25, -1.2)], closed=True, fc="white", ec=G1, lw=1.3)); ax.add_patch(Circle((5.36, -1.2), 0.11, fc="white", ec=G1, lw=1.3))
    _line(ax, [5.47, 7.5, 7.5], [-1.2, -1.2, 0], color=G1); ax.text(6.5, -1.05, "CLK'", fontsize=8.5, color=G1, ha="center", va="bottom")
    _line(ax, [9.5, 9.5, 0.6, 0.6], [1.6, 2.6, 2.6, 2.0], color=MUTED, ls=(0, (3, 3))); ax.text(5.0, 2.68, "Q and Q' fed back to the master's input gates", ha="center", fontsize=8, color=MUTED)
    return _nat(fig)


def counter_T():
    """3-bit synchronous up counter, T flip-flops, negative-edge clock: T0 = 1, T1 = Q0, T2 = Q1·Q0."""
    fig, ax = _canvas(7.8, 2.6, (-2.0, 12.4), (-2.1, 2.6))
    for i in range(3):
        x = i * 4.2
        _box(ax, x, 0, 1.8, 1.8, "", ec=ACC, r=0.05)
        ax.text(x + 0.15, 1.4, "T", va="center", fontsize=9.5, weight="bold"); ax.text(x + 1.65, 1.4, "Q", ha="right", va="center", fontsize=9.5, weight="bold")
        ax.text(x + 0.9, 2.05, f"FF{i}", ha="center", fontsize=9, color=ACC, weight="bold")
        ax.add_patch(Polygon([(x + 0.7, 0), (x + 0.9, 0.25), (x + 1.1, 0)], closed=True, fc="none", ec=INK, lw=1.1))
        ax.add_patch(Circle((x + 0.9, -0.11), 0.11, fc="white", ec=INK, lw=1.1))
        _line(ax, [x + 0.9, x + 0.9], [-0.22, -1.3], color=MUTED)
        _line(ax, [x + 1.8, x + 2.4], [1.4, 1.4]); ax.text(x + 2.45, 1.62, f"Q{i}", fontsize=9.5, weight="bold", color=ACC)
    _line(ax, [-1.2, 9.3], [-1.3, -1.3], color=MUTED); ax.text(-1.25, -1.3, "CLK", ha="right", va="center", fontsize=9, color=MUTED)
    _line(ax, [-0.8, 0], [1.4, 1.4]); ax.text(-0.85, 1.4, "1", ha="right", va="center", fontsize=10, weight="bold")
    _line(ax, [2.4, 4.2], [1.4, 1.4]); ax.plot(2.9, 1.4, "o", ms=3.5, color=INK)
    _line(ax, [2.9, 2.9, 7.0], [1.4, 0.55, 0.55])
    _box(ax, 7.0, 0.35, 0.95, 1.3, "AND", fs=7.6, r=0.3)
    _line(ax, [6.6, 6.6, 7.0], [1.4, 1.25, 1.25]); ax.plot(6.6, 1.4, "o", ms=3.5, color=INK)
    _line(ax, [7.95, 8.4], [1.0, 1.0]); _line(ax, [8.4, 8.4], [1.0, 1.4])
    ax.text(3.3, -1.95, "T0 = 1  ·  T1 = Q0  ·  T2 = Q1·Q0  ·  all three flip-flops share one clock", fontsize=8.8, color=G1, weight="bold")
    return _svg(fig)


def sipo_xor():
    """Deck 09 slide 24: 4-bit right-shift register, serial input = XOR of the last two stages."""
    fig, ax = _canvas(4.4, 1.8, (-2.2, 7.2), (-2.0, 1.6))
    for i, b in enumerate("0110"):
        ax.add_patch(Rectangle((i * 1.1, 0), 1.1, 1.0, fc=TINT, ec=ACC, lw=1.3)); ax.text(i * 1.1 + 0.55, 0.5, b, ha="center", va="center", fontsize=11, weight="bold")
        ax.text(i * 1.1 + 0.55, 1.2, f"Q{i}", ha="center", fontsize=8.5, color=MUTED)
    ax.add_patch(Circle((1.6, -1.2), 0.33, fc="white", ec=G1, lw=1.4)); ax.text(1.6, -1.2, "⊕", ha="center", va="center", fontsize=12, color=G1)
    _line(ax, [2.75, 2.75, 1.93], [0, -1.05, -1.05], color=G1); _line(ax, [4.4, 5.0, 5.0, 1.93], [0.5, 0.5, -1.35, -1.35], color=G1)
    _line(ax, [1.27, -0.8, -0.8], [-1.2, -1.2, 0.5], color=G1); _arrow(ax, (-0.8, 0.5), (0, 0.5), color=G1)
    ax.text(-0.9, -0.3, "serial in\n= Q2 ⊕ Q3", ha="right", va="center", fontsize=8.5, color=G1)
    ax.text(5.2, 0.9, "shift →", fontsize=8.5, color=MUTED)
    return _nat(fig)


# ------------------------------------------------------------------ state machines
def mealy_1101():
    st = {"A": (0, 0, "A"), "B": (3.3, 0, "B"), "C": (6.6, 0, "C"), "D": (9.9, 0, "D")}
    ed = [("A", "A", "0/0", 1), ("A", "B", "1/0", 0.22), ("B", "A", "0/0", 0.22), ("B", "C", "1/0", 0.0), ("C", "C", "1/0", 1),
          ("C", "D", "0/0", 0.0), ("D", "B", "1/1", 0.36), ("D", "A", "0/0", -0.34)]
    return v1.state_diagram(st, ed, size=(8.0, 3.2), lim=((-1.2, 11.1), (-2.6, 2.3)), r=0.55)


def moore_1101():
    st = {"A": (0, 0, "A/0"), "B": (3.0, 0, "B/0"), "C": (6.0, 0, "C/0"), "D": (9.0, 0, "D/0"), "E": (12.0, 0, "E/1")}
    ed = [("A", "A", "0", 1), ("A", "B", "1", 0.3), ("B", "A", "0", 0.3), ("B", "C", "1", 0.0), ("C", "C", "1", 1),
          ("C", "D", "0", 0.0), ("D", "E", "1", 0.0), ("D", "A", "0", -0.3), ("E", "C", "1", 0.42), ("E", "A", "0", -0.36)]
    return v1.state_diagram(st, ed, size=(8.6, 3.7), lim=((-1.2, 13.2), (-3.6, 2.5)), r=0.6)


def implication_chart():
    """Implication table for the 5-state machine of deck 12 (slides 10 and 16)."""
    fig, ax = _canvas(4.6, 3.6, (-1.0, 6.4), (-1.0, 4.6))
    rows, cols = "BCDE", "ABCD"
    cell = {("B", "A"): ("B–E", False), ("C", "A"): ("B–C\nB–E", False), ("C", "B"): ("✓", True),
            ("D", "A"): ("×", False), ("D", "B"): ("×", False), ("D", "C"): ("×", False),
            ("E", "A"): ("×", False), ("E", "B"): ("×", False), ("E", "C"): ("×", False), ("E", "D"): ("A–B", False)}
    for i, r in enumerate(rows):
        y = 3 - i
        ax.text(-0.3, y + 0.5, r, ha="right", va="center", fontsize=10.5, weight="bold")
        for j, c in enumerate(cols[:i + 1]):
            txt, ok = cell[(r, c)]
            out = txt == "×"
            ax.add_patch(Rectangle((j, y), 1, 1, fc="#eaf6ef" if ok else ("#f4f4f0" if out else "#fff4f2"), ec=INK, lw=1.1))
            ax.text(j + 0.5, y + 0.5, txt, ha="center", va="center", fontsize=8.5 if len(txt) > 1 else 12,
                    color=G2 if ok else (MUTED if out else BAD), weight="bold")
            if not ok and not out:
                _line(ax, [j + 0.08, j + 0.92], [y + 0.08, y + 0.92], color=BAD, lw=0.9)
    for j, c in enumerate(cols):
        ax.text(j + 0.5, -0.35, c, ha="center", va="center", fontsize=10.5, weight="bold")
    ax.text(2.3, 3.75, "× : outputs differ", fontsize=8.3, color=MUTED)
    ax.text(2.3, 3.3, "pair listed, struck out: it depends\non a pair that is not equivalent", fontsize=8.3, color=BAD, va="top")
    ax.text(3.3, 2.15, "✓ : equivalent", fontsize=8.3, color=G2)
    return _nat(fig)


def asm_1101():
    """ASM chart of the Mealy 1101 detector: z is a conditional output on D's x = 1 exit."""
    fig, ax = _canvas(5.4, 7.6, (-3.6, 5.6), (-12.4, 1.2))

    def sbox(y, name):
        _box(ax, -0.9, y, 1.8, 0.8, name, fs=10, fc=TINT, ec=ACC, r=0.02, weight="bold")

    def dia(y):
        ax.add_patch(Polygon([(0, y + 0.45), (0.75, y), (0, y - 0.45), (-0.75, y)], closed=True, fc="white", ec=INK, lw=1.3))
        ax.text(0, y, "x", ha="center", va="center", fontsize=9.5, weight="bold")

    def lab(x, y, t):
        ax.text(x, y, t, fontsize=8.5, color=G1, weight="bold")

    ys = [0, -3, -6, -9]
    for y, n in zip(ys, "ABCD"):
        sbox(y, n); _line(ax, [0, 0], [y, y - 0.6]); dia(y - 1.05)
    # A: 1 -> B (down), 0 -> A (loop left)
    _arrow(ax, (0, -1.5), (0, -2.2)); lab(0.1, -1.95, "1")
    _line(ax, [-0.75, -1.7, -1.7, -0.9], [-1.05, -1.05, 0.4, 0.4]); _arrow(ax, (-1.2, 0.4), (-0.9, 0.4)); lab(-1.3, -0.95, "0")
    # B: 1 -> C (down), 0 -> A (left)
    _arrow(ax, (0, -4.5), (0, -5.2)); lab(0.1, -4.95, "1")
    _line(ax, [-0.75, -2.4, -2.4, -0.9], [-4.05, -4.05, 0.55, 0.55]); _arrow(ax, (-1.3, 0.55), (-0.9, 0.55)); lab(-1.3, -3.95, "0")
    # C: 0 -> D (down), 1 -> C (loop right)
    _arrow(ax, (0, -7.5), (0, -8.2)); lab(0.1, -7.95, "0")
    _line(ax, [0.75, 1.7, 1.7, 0.9], [-7.05, -7.05, -5.6, -5.6]); _arrow(ax, (1.2, -5.6), (0.9, -5.6)); lab(0.9, -6.95, "1")
    # D: 0 -> A (far left), 1 -> oval z -> B (right)
    _line(ax, [-0.75, -3.1, -3.1, -0.9], [-10.05, -10.05, 0.7, 0.7]); _arrow(ax, (-1.3, 0.7), (-0.9, 0.7)); lab(-1.3, -9.95, "0")
    _line(ax, [0, 0], [-10.5, -10.9]); lab(0.1, -10.8, "1")
    ax.add_patch(Ellipse((0, -11.35), 1.7, 0.85, fc="#fdeee3", ec=G1, lw=1.4)); ax.text(0, -11.35, "z = 1", ha="center", va="center", fontsize=9.5, weight="bold", color=G1)
    _line(ax, [0.85, 3.0, 3.0, 0.9], [-11.35, -11.35, -2.6, -2.6]); _arrow(ax, (1.3, -2.6), (0.9, -2.6))
    ax.text(2.0, 0.6, "state box\n= one clock", fontsize=8, color=MUTED)
    ax.text(1.1, -11.95, "conditional output box:\nz depends on x (Mealy)", fontsize=8, color=G1, va="top")
    return _svg(fig)


def mem_decode():
    """4K x 8 from four 1K x 8 chips: a 2:4 decoder on A11 A10 drives the chip selects."""
    fig, ax = _canvas(7.0, 2.6, (-2.6, 12.4), (-1.6, 3.6))
    _box(ax, 0, 0.2, 1.8, 2.6, "2:4\ndecoder", fc=TINT, ec=ACC, fs=9)
    _arrow(ax, (-1.0, 1.5), (0, 1.5)); ax.text(-1.1, 1.5, "A11 A10", ha="right", va="center", fontsize=9.5, weight="bold")
    for i in range(4):
        x = 3.6 + i * 2.1
        _box(ax, x, 0.6, 1.6, 1.6, f"1K × 8\nchip {i}", fs=8.5)
        y = 2.5 - i * 0.55
        _line(ax, [1.8, 2.6 + i * 0.25, 2.6 + i * 0.25], [y, y, 3.2 - i * 0.12], color=G1, lw=1.1)
        _line(ax, [2.6 + i * 0.25, x + 0.8, x + 0.8], [3.2 - i * 0.12, 3.2 - i * 0.12, 2.2], color=G1, lw=1.1)
        _line(ax, [x + 0.8, x + 0.8], [0.6, -0.4], color=MUTED)
        ax.text(x + 0.8, 0.45, f"{i * 1024}–{i * 1024 + 1023}", ha="center", va="top", fontsize=7.4, color=MUTED, bbox=dict(fc="white", ec="none", pad=0.5))
    ax.text(11.9, 3.05, "chip-select\nlines", fontsize=8, color=G1, va="center")
    _line(ax, [-1.0, 10.7], [-0.4, -0.4], lw=2.2); ax.text(-1.1, -0.4, "A9–A0", ha="right", va="center", fontsize=9.5, weight="bold")
    ax.text(4.8, -1.1, "address lines A9–A0 and the 8 data lines go to every chip", fontsize=8.3, color=MUTED, ha="center")
    return _nat(fig)
