"""Unit 3 counter figures for files 12-13 (v1.3, S3 2026-11-17). Waveforms are simulated, not typed."""
import math

import figs1
import qm
from figs1 import ACC, BAD, G1, G2, INK, MUTED, TINT, _arrow, _box, _canvas, _line, _nat
from matplotlib.patches import Circle, Polygon

waves = figs1.v1.waves


# ------------------------------------------------------------------ A. ripple-counter schematic
def ripple_sch(n, down=False, nand=None):
    sp, bw, bh = 4.0, 1.6, 2.0          # box pitch, width, height
    xmax = (n - 1) * sp + (bw + 1.4)
    ybot = -3.9 if nand else -1.5
    if nand:
        tap_max = (max(nand)) * sp + 2.2
        xr = tap_max + 1.0
        xmax = max(xmax, xr + 1.3 + 0.2 + 0.6)
    xlim = (-2.2, xmax + 0.3)
    ylim = (ybot - 0.9, 2.6)
    fig, ax = _canvas(0.44 * (xlim[1] - xlim[0]), 0.44 * (ylim[1] - ylim[0]), xlim, ylim)
    for i in range(n):
        x = i * sp
        _box(ax, x, 0, bw, bh, "", ec=ACC, r=0.05)
        ax.text(x + 0.15, 1.5, "T", va="center", fontsize=9, weight="bold")
        ax.text(x + bw - 0.12, 1.5, "Q", ha="right", va="center", fontsize=9, weight="bold")
        ax.text(x + bw - 0.12, 0.6, "Q'", ha="right", va="center", fontsize=9, weight="bold")
        ax.text(x + bw / 2 - 0.3, bh + 0.28, f"FF{i}", ha="center", va="center", fontsize=9, color=ACC, weight="bold")
        # T tied to 1
        _line(ax, [x - 0.7, x], [1.5, 1.5])
        ax.text(x - 0.78, 1.5, "1", ha="right", va="center", fontsize=9, weight="bold")
        # negative-edge clock pin: triangle + bubble
        cx = x + 0.5
        ax.add_patch(Polygon([(cx - 0.2, 0), (cx, 0.28), (cx + 0.2, 0)], closed=True, fc="none", ec=INK, lw=1.1))
        ax.add_patch(Circle((cx, -0.11), 0.11, fc="white", ec=INK, lw=1.1))
        _line(ax, [cx, cx], [-0.22, -0.9], color=G1 if i else MUTED, lw=1.4)
        # outputs
        _line(ax, [x + bw, x + 2.2], [1.5, 1.5])
        _line(ax, [x + 2.2, x + 2.2], [1.5, 1.95])
        ax.text(x + 2.2, 2.1, f"Q{i}", ha="center", va="bottom", fontsize=9, weight="bold", color=ACC)
        if i < n - 1:
            src_y = 0.6 if down else 1.5
            xv = x + 2.6
            _line(ax, [x + bw, xv] if down else [x + 2.2, xv], [src_y, src_y], color=G1, lw=1.4)
            _line(ax, [xv, xv, x + sp + 0.5], [src_y, -0.9, -0.9], color=G1, lw=1.4)
    _line(ax, [-1.2, 0.5], [-0.9, -0.9], color=MUTED, lw=1.4)
    ax.text(-1.28, -0.9, "CLK", ha="right", va="center", fontsize=9, color=MUTED)
    if nand:
        busy = -1.8
        nin = sorted(nand)
        for i in range(n):
            x = i * sp
            _line(ax, [x + 1.2, x + 1.2], [0, busy])
            ax.plot(x + 1.2, busy, "o", ms=3.5, color=INK)
        ax.text(1.3 + 0.05, -0.45, "CLR'", ha="left", va="center", fontsize=8.5, color=INK)
        # NAND gate right of the right-most tap
        ys = {nin[-1]: -2.6, nin[0]: -3.1}
        for i in nin:
            tx = i * sp + 2.2
            ax.plot(tx, 1.5, "o", ms=3.5, color=INK)
            _line(ax, [tx, tx, xr], [1.5, ys[i], ys[i]], color=G2, lw=1.4)
        _box(ax, xr, -3.4, 1.3, 1.1, "NAND", fs=8.5, r=0.3)
        ax.add_patch(Circle((xr + 1.3 + 0.1, -2.85), 0.1, fc="white", ec=INK, lw=1.3))
        xo = xr + 1.3 + 0.2 + 0.5
        _line(ax, [xr + 1.5, xo, xo, 1.2], [-2.85, -2.85, busy, busy])
        txt = ("NAND on " + ", ".join(f"Q{i}" for i in reversed(nin)) + " → CLR' of all: clears at "
               + format(sum(1 << i for i in nin), f"0{n}b"))
    elif down:
        txt = "negative-edge flip-flops, each clocked by the Q' before it: counts down"
    else:
        txt = "negative-edge flip-flops, each clocked by the Q before it: counts up"
    ax.text((xlim[0] + xlim[1]) / 2, ybot - 0.55, txt, ha="center", va="center", fontsize=8.8, color=G1, weight="bold")
    return _nat(fig)


# ------------------------------------------------------------------ B. ripple waveforms (simulated)
def _clk(k):
    return [(0, 0)] + [p for j in range(k) for p in ((2 * j + 1, 1), (2 * j + 2, 0))]


def _ripple_sim(n, edges, down=False):
    """Q breakpoints of n negative-edge T flip-flops (T = 1); stage i is clocked by the fall (rise if down) of stage i-1."""
    falls = [2 * j + 2 for j in range(edges)]
    qs = [qm.compress(qm.edge_ff("T", {"T": [(0, 1)]}, falls))]
    for _ in range(1, n):
        want = 1 if down else 0
        nxt = [t for (t, v) in qs[-1] if v == want and t > 0]
        qs.append(qm.compress(qm.edge_ff("T", {"T": [(0, 1)]}, nxt)))
    return falls, qs


def _count(qs, t):
    return sum(qm.level(q, t) << i for i, q in enumerate(qs))


def ripple_waves(n, edges, down, expect):
    falls, qs = _ripple_sim(n, edges, down)
    got = [_count(qs, t) for t in falls]
    assert got == expect, f"ripple {n} down={down}: simulated {got} != {expect}"
    rows = [("CLK", _clk(edges))] + [(f"Q{i}", q) for i, q in enumerate(qs)]
    return waves(rows, 2 * edges + 1, w=8.4, marks=[(t, str(c), G1) for t, c in zip(falls, got)])


# ------------------------------------------------------------------ C. propagation-delay zoom
def delay():
    def u(ns):
        return (ns + 5) / 5
    clk = [(0, 1), (u(0), 0)]
    q0 = [(0, 1), (u(10), 0)]
    q1 = [(0, 1), (u(20), 0)]
    q2 = [(0, 0), (u(30), 1)]
    return waves([("CLK", clk), ("Q0", q0), ("Q1", q1), ("Q2", q2)], 9, w=8.2,
                 shade=[(u(10), u(20), BAD), (u(20), u(30), BAD)],
                 marks=[(u(0), "↓ CLK", G1), (u(14), "010 (2)", BAD), (u(22), "000 (0)", BAD),
                        (u(30), "100 (4) settled", G1)],
                 title="each stage waits one t_pd = 10 ns for the one before: 011 → 010 → 000 → 100")


# ------------------------------------------------------------------ D. MOD-6 by reset
def mod6_waves():
    edges, blip = 12, 0.3
    s, ev = 0, [(0, 0)]                      # (time, state)
    nand = [(0, 1)]
    settled = []
    for j in range(edges):
        t = 2 * j + 2
        s = (s + 1) % 8
        ev.append((t, s))
        if s == 6:                           # Q2 = Q1 = 1: NAND drops, asynchronous clear after the blip
            nand += [(t, 0), (t + blip, 1)]
            s = 0
            ev.append((t + blip, s))
        settled.append(s)
    assert settled == [1, 2, 3, 4, 5, 0] * 2, settled
    bits = [qm.compress([(t, (v >> i) & 1) for t, v in ev]) for i in range(3)]
    nand = qm.compress(nand)
    falls = [2 * j + 2 for j in range(edges)]
    marks = []
    for t, c in zip(falls, settled):
        marks.append((t, str(c), G1))
    shade = [(12, 12 + blip, BAD), (24, 24 + blip, BAD)]
    rows = [("CLK", _clk(edges))] + [(f"Q{i}", b) for i, b in enumerate(bits)] + [("NAND", nand)]
    return waves(rows, 2 * edges + 1, w=9.4, marks=marks, shade=shade,
                 title="shaded: 110 for an instant (0.3 of a half-period), NAND drops to 0 and clears the counter to 000")


# ------------------------------------------------------------------ E. cascade
def cascade():
    fig, ax = _canvas(7.2, 1.9, (-0.2, 12.4), (-1.3, 2.0))
    _box(ax, 2.0, 0, 3.2, 1.6, "MOD-4 counter\n(2 flip-flops)", fc=TINT, ec=ACC, fs=9.5)
    _box(ax, 7.0, 0, 3.2, 1.6, "MOD-8 counter\n(3 flip-flops)", fc=TINT, ec=ACC, fs=9.5)
    for a, b, lab in ((0.1, 2.0, "32 kHz"), (5.2, 7.0, "8 kHz"), (10.2, 12.1, "1 kHz")):
        _arrow(ax, (a, 0.8), (b, 0.8))
        ax.text((a + b) / 2, 1.0, lab, ha="center", va="bottom", fontsize=9, color=G1, weight="bold")
    ax.text(6.1, -0.8, "MOD-4 then MOD-8 = MOD-(4 × 8) = MOD-32", ha="center", va="center", fontsize=9.5,
            color=G1, weight="bold")
    return _nat(fig)


# ------------------------------------------------------------------ F. state diagrams
def state_ring(labels, extra=(), title=None, r=2.0):
    """Ring of states, clockwise from the top. extra: chains (outside..., ring_target) drawn dashed in BAD."""
    s, rc = 0.5, 0.55                         # inches per unit, circle radius
    n = len(labels)
    ang = {l: math.radians(90 - 360 * k / n) for k, l in enumerate(labels)}
    pos = {l: (r * math.cos(a), r * math.sin(a)) for l, a in ang.items()}
    rout = r + 1.7
    chains = []
    for ch in extra:
        tgt = ch[-1]
        outs = list(ch[:-1])
        for j, lab in enumerate(reversed(outs)):          # nearest the target first
            a = ang[tgt] + math.radians(12 + 24 * j)
            pos[lab] = (rout * math.cos(a), rout * math.sin(a))
        chains.append(ch)
    ex = max(abs(p[0]) for p in pos.values()) + rc + 0.1
    ey = max(abs(p[1]) for p in pos.values()) + rc + 0.1
    ex = max(ex, 4.6 / (2 * s))
    fig, ax = _canvas(2 * ex * s, 2 * ey * s + 0.3, (-ex, ex), (-ey, ey))

    def link(a, b, col, ls):
        (x0, y0), (x1, y1) = pos[a], pos[b]
        d = math.hypot(x1 - x0, y1 - y0)
        ux, uy = (x1 - x0) / d, (y1 - y0) / d
        _arrow(ax, (x0 + ux * rc, y0 + uy * rc), (x1 - ux * (rc + 0.03), y1 - uy * (rc + 0.03)), color=col, ls=ls, lw=1.4)

    for k, l in enumerate(labels):
        link(l, labels[(k + 1) % n], ACC, "-")
    for ch in chains:
        for a, b in zip(ch, ch[1:]):
            link(a, b, BAD, (0, (3, 2)))
    for l, (x, y) in pos.items():
        ring = l in ang
        ax.add_patch(Circle((x, y), rc, fc=TINT if ring else "white", ec=ACC if ring else BAD, lw=1.4,
                            ls="-" if ring else (0, (3, 2))))
        ax.text(x, y, l, ha="center", va="center", fontsize=8.5, weight="bold", color=INK if ring else BAD)
    if title:
        ax.set_title(title, fontsize=9.5, color=MUTED, loc="left")
    return _nat(fig)


GRAY3 = ["000", "001", "011", "010", "110", "111", "101", "100"]

FIGS = {
    "u3c_ripple3": lambda: ripple_sch(3),
    "u3c_ripple3_down": lambda: ripple_sch(3, down=True),
    "u3c_mod6": lambda: ripple_sch(3, nand=[1, 2]),
    "u3c_decade": lambda: ripple_sch(4, nand=[1, 3]),
    "u3c_ripple2_waves": lambda: ripple_waves(2, 4, False, [1, 2, 3, 0]),
    "u3c_ripple3_waves": lambda: ripple_waves(3, 8, False, [1, 2, 3, 4, 5, 6, 7, 0]),
    "u3c_ripple3_down_waves": lambda: ripple_waves(3, 8, True, [7, 6, 5, 4, 3, 2, 1, 0]),
    "u3c_delay": delay,
    "u3c_mod6_waves": mod6_waves,
    "u3c_cascade": cascade,
    "u3c_sd2": lambda: state_ring(["00", "01", "10", "11"], title="2-bit up counter: one arrow per clock edge", r=1.6),
    "u3c_sd_gray": lambda: state_ring(GRAY3, title="3-bit Gray counter: one bit changes on every arrow", r=2.4),
    "u3c_sd_decade": lambda: state_ring(
        [format(i, "04b") for i in range(10)],
        extra=[("1010", "1011", "0110"), ("1100", "1101", "0100"), ("1110", "1111", "0010")],
        title="decade counter: every unused state reaches the count within two clocks (self-starting)", r=3.0),
    "u3c_sd_mod6": lambda: state_ring(
        [format(i, "03b") for i in range(6)], extra=[("110", "111", "000")],
        title="MOD-6: 110 → 111 → 000, self-starting", r=2.0),
}
