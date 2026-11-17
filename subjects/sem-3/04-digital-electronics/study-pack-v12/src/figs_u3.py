"""Unit 3 figures for files 09-10 (v1.3, S2 2026-11-17).

Waveforms use the v1 drawer `figs1.v1.waves` (matplotlib); every output trace is produced by
simulation (qm.edge_ff / qm.d_latch, or the small async/JK-latch simulators below), and verify.py u3
re-simulates the same input data with its own ff_next and compares with the values the pack prints.
Gate-level schematics are in figs_u3_sch.py.

Input waveforms were read from the exam images (S2): MTE 2025 Q7 = practice set 2 Q3(a) inputs;
practice set 2 Q3(b) adds CLR/PR; practice set 2 Q2 (D latch, JK latch). Time unit = half a clock
period for the flip-flop questions (rising edges at odd t, falling at even t); one grid square for
the latch question (shifted +2 so the initial Q shows before the first enable).
"""
import figs1
import figs2
import qm
from figs1 import ACC, G1, G2, MUTED, BAD

waves = figs1.v1.waves

# ------------------------------------------------------------------ question data (shared with verify.py)
CLK7 = [(0, 0)] + [p for k in range(7) for p in ((2 * k + 1, 1), (2 * k + 2, 0))]
RISE7 = [1, 3, 5, 7, 9, 11, 13]
FALL7 = [2, 4, 6, 8, 10, 12, 14]
J7 = [(0, 0), (1, 1), (2, 0), (5, 1), (6, 0), (7.5, 1), (10, 0), (12, 1), (14, 0)]
K7 = [(0, 0), (2.5, 1), (3, 0), (3.5, 1), (4.5, 0), (9.5, 1), (10, 0), (10.5, 1), (14, 0)]
CLR3B = [(0, 1), (0.2, 0), (0.5, 1), (10.8, 0), (11.5, 1)]   # active-low
PR3B = [(0, 1), (7.25, 0), (7.5, 1)]                          # active-low

# practice set 2 Q2 (+2 shift): D latch panel and JK latch panel
EN_D = [(0, 0), (2, 1), (8, 0), (10, 1), (12, 0), (14, 1), (19, 0), (24, 1), (28, 0)]
D_D = [(0, 0), (4, 1), (6, 0), (7, 1), (9, 0), (18, 1), (20, 0), (22, 1), (28, 0)]
EN_JK = [(0, 0), (2, 1), (8, 0), (14, 1), (18, 0), (24, 1), (28, 0)]
J_JK = [(0, 0), (2, 1), (4, 0), (10, 1), (12, 0), (16, 1), (20, 0), (26, 1), (28, 0)]
K_JK = [(0, 0), (5, 1), (6, 0), (7, 1), (9, 0), (19, 1), (20, 0), (21, 1), (28, 0)]


def highs(sig):
    """[a, b) intervals where a piecewise signal is 1."""
    out, start = [], None
    for t, v in sig:
        if v and start is None:
            start = t
        elif not v and start is not None:
            out.append((start, t)); start = None
    return out


def async_jk(edges, q0=0):
    """Negative-edge JK with active-low CLR and PR (PS2 Q3b): Q forced while CLR or PR is 0."""
    ev = sorted({t for t, _ in CLR3B + PR3B} | set(edges))
    q, out = q0, [(0, q0)]
    for t in ev:
        if t in edges:
            j, k = qm.level(J7, t - 1e-6), qm.level(K7, t - 1e-6)
            q = (j & (1 - q)) | ((1 - k) & q)
        if qm.level(CLR3B, t) == 0:
            q = 0
        elif qm.level(PR3B, t) == 0:
            q = 1
        out.append((t, q))
    return qm.compress(out)


def jk_latch(q0=1, step=0.25):
    """High-level JK latch (PS2 Q2): Q follows the JK table while EN = 1; J = K = 1 with EN = 1 toggles
    every gate delay (drawn every `step`): race-around. Returns breakpoints and the race interval."""
    q, out, race = q0, [(0, q0)], []
    t = 0.0
    while t < 28.999:
        if qm.level(EN_JK, t):
            j, k = qm.level(J_JK, t), qm.level(K_JK, t)
            if j and k:
                race.append(t)
                q ^= 1
            else:
                q = (j & (1 - q)) | ((1 - k) & q)
        out.append((t, q))
        t = round(t + step, 6)
    return qm.compress(out), (min(race), max(race) + step) if race else None


def _marks(ts, sym, col=G1):
    return [(t, sym, col) for t in ts]


# ------------------------------------------------------------------ 09 figures
def clock():
    clk = [(0, 0)] + [p for k in range(4) for p in ((2 * k + 1, 1), (2 * k + 2, 0))]
    return waves([("CLK", clk)], 9, w=7.2, marks=_marks([1, 3, 5, 7], "↑ rising", G1)[:1]
                 + _marks([2], "↓ falling", BAD) + [(3, "", G1), (5, "", G1), (7, "", G1)]
                 + [(4, "", BAD), (6, "", BAD), (8, "", BAD)],
                 title="one period T = from one ↑ to the next (2 units); high time = 1 unit; duty cycle = 1/2 = 50 %")


def tdiv():
    clk = [(0, 0)] + [p for k in range(8) for p in ((2 * k + 1, 1), (2 * k + 2, 0))]
    rise = [2 * k + 1 for k in range(8)]
    qa = qm.compress(qm.edge_ff("T", {"T": [(0, 1)]}, rise))
    qa_rise = [t for (t, v) in qa if v == 1 and t > 0]
    qb = qm.compress(qm.edge_ff("T", {"T": [(0, 1)]}, qa_rise))
    return waves([("CLK", clk), ("Q_A", qa), ("Q_B", qb)], 17, w=8.2, marks=_marks(rise, "↑"))


def race():
    clk = [(0, 0), (1, 1), (4, 0), (6, 1), (9, 0)]
    q, pts = 0, [(0, 0)]
    for a, b in ((1, 4), (6, 9)):
        t = a + 0.3
        while t < b:
            q ^= 1; pts.append((round(t, 2), q)); t += 0.3
    return waves([("CLK", clk), ("J = K", [(0, 1)]), ("Q", pts)], 10, w=7.6,
                 shade=[(1, 4, BAD), (6, 9, BAD)],
                 title="level-triggered JK, J = K = 1: Q toggles again and again while CLK = 1; its value at the fall is unknown")


def jk_kmap():
    return figs1.km("JKQ", [1, 4, 5, 6], terms=["JQ'", "K'Q"], cs=48)


def conv_jk_d():
    return (figs1.km("DQ", [2], [1, 3], terms=["D"], cs=48, title="J")
            + figs1.km("DQ", [1], [0, 2], terms=["D'"], cs=48, title="K"))


def conv_t_d():
    return figs1.km("DQ", [1, 2], terms=["D'Q", "DQ'"], cs=48, title="T")


# ------------------------------------------------------------------ 10 figures
def dff():
    q = qm.compress(qm.edge_ff("D", {"D": figs2.W_D}, figs2.RISE))
    return waves([("CLK", figs2.CLK6), ("D", figs2.W_D), ("Q", q)], 12.6, w=8.2, marks=_marks(figs2.RISE, "↑"))


def mte7(show_q=True):
    rows = [("CLK", CLK7), ("J", J7), ("K", K7)]
    if show_q:
        rows.append(("Q", qm.compress(qm.edge_ff("JK", {"J": J7, "K": K7}, RISE7))))
    return waves(rows, 15, w=8.4, marks=[(t, f"↑{i + 1}", G1) for i, t in enumerate(RISE7)])


def ps2q3a():
    q = qm.compress(qm.edge_ff("JK", {"J": J7, "K": K7}, FALL7))
    return waves([("CLK", CLK7), ("J", J7), ("K", K7), ("Q", q)], 15, w=8.4,
                 marks=[(t, f"↓{i + 1}", BAD) for i, t in enumerate(FALL7)])


def ps2q3b():
    return waves([("CLK", CLK7), ("J", J7), ("K", K7), ("CLR'", CLR3B), ("PR'", PR3B), ("Q", async_jk(FALL7))], 15,
                 w=8.4, marks=[(t, f"↓{i + 1}", BAD) for i, t in enumerate(FALL7)])


def ps2q2d():
    q = qm.compress(qm.d_latch(D_D, highs(EN_D), q0=1))
    return waves([("EN", EN_D), ("D", D_D), ("Q", q)], 29, w=8.4, shade=[(a, b, G2) for a, b in highs(EN_D)])


def ps2q2jk():
    q, (a, b) = jk_latch()
    return waves([("EN", EN_JK), ("J", J_JK), ("K", K_JK), ("Q", q)], 29, w=8.4,
                 shade=[(x, y, G2) for x, y in highs(EN_JK)] + [(a, b, BAD)],
                 marks=[(a, "race-around", BAD)])


FIGS = {
    "u3_clock": clock, "u3_tdiv": tdiv, "u3_race": race, "u3_jk_kmap": jk_kmap,
    "u3_conv_jk_d": conv_jk_d, "u3_conv_t_d": conv_t_d,
    "u3_dff": dff, "u3_mte7_noq": lambda: mte7(False), "u3_mte7": mte7, "u3_ps2q3a": ps2q3a,
    "u3_ps2q3b": ps2q3b, "u3_ps2q2d": ps2q2d, "u3_ps2q2jk": ps2q2jk,
}

try:
    import figs_u3_sch
    FIGS.update(figs_u3_sch.FIGS)
except ImportError:  # schematics module not written yet
    pass
