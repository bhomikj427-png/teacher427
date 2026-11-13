"""Figures for EDC-ETE-v1.pdf, Parts E (BJT), F (feedback), G (oscillators). Each public function returns inline SVG."""
import numpy as np
import schemdraw.elements as elm
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

from figs import (_fig, _canvas, _svg, _sd, _d, _box, _arrow, W, RES, CAP, DOT, TXT, GND, OUT, RC,
                  INK, MUTED, LINE, SOFT, ACC, G1, G2, G3, BAD, NCOL, PCOL)


# ================================================================== Part E: BJT
def bjt_struct():
    fig, ax = _canvas(8.6, 3.2, (0, 14), (0, 5.4))
    ax.add_patch(Rectangle((2.0, 1.6), 3.2, 1.8, fc=NCOL, ec=INK)); ax.add_patch(Rectangle((5.2, 1.6), 0.7, 1.8, fc=PCOL, ec=INK))
    ax.add_patch(Rectangle((5.9, 1.6), 4.4, 1.8, fc="#eaf1ff", ec=INK))
    ax.text(3.6, 2.5, "Emitter\nn⁺ (heavily doped)", ha="center", va="center", fontsize=8.6)
    ax.text(5.55, 3.55, "Base: p (thin, lightly doped)", ha="center", fontsize=8.6, color=BAD)
    ax.text(8.1, 2.5, "Collector\nn (moderately doped, largest)", ha="center", va="center", fontsize=8.6)
    for x, name in ((1.2, "E"), (11.1, "C")):
        ax.plot([x, x + 0.8] if name == "E" else [x - 0.8, x], [2.5, 2.5], color=INK, lw=1.3); ax.text(x + (-0.25 if name == "E" else 0.25), 2.5, name, ha="center", va="center", fontsize=11, weight="bold")
    ax.plot([5.55, 5.55], [1.6, 0.7], color=INK, lw=1.3); ax.text(5.55, 0.4, "B", ha="center", fontsize=11, weight="bold")
    _arrow(ax, (2.4, 2.0), (9.8, 2.0), color=ACC, lw=1.6); ax.text(8.6, 1.35, "≈ 99% of the electrons reach the collector → I_C", fontsize=7.8, color=ACC, ha="center", va="top")
    _arrow(ax, (5.3, 2.0), (5.5, 1.1), color=BAD, lw=1.1); ax.text(5.4, 0.95, "≈ 1% recombine in the base → I_B", fontsize=7.8, color=BAD, va="center", ha="right")
    ax.text(5.1, 4.55, "EB junction: forward biased", ha="right", fontsize=8.3, color=G2); ax.text(6.0, 4.55, "CB junction: reverse biased", fontsize=8.3, color=G1)
    ax.plot([5.2, 5.2], [3.95, 4.7], color=G2, lw=0.9, ls=":"); ax.plot([5.9, 5.9], [3.95, 4.7], color=G1, lw=0.9, ls=":")
    ax.text(11.6, 3.9, "I_E = I_C + I_B\nI_C = β I_B = α I_E", fontsize=10, weight="bold", va="center")
    return _svg(fig)


def bjt_symbols():
    d = _d(unit=2.2)
    q = elm.BjtNpn(circle=True).at((0, 0)); d += q
    TXT(d, (-0.3, 0), "B", fs=11); TXT(d, (1.0, 1.0), "C", fs=11); TXT(d, (1.0, -1.0), "E", fs=11); TXT(d, (0.6, -1.9), "npn: arrow\npoints out", fs=10)
    q2 = elm.BjtPnp(circle=True).at((3.4, 0)); d += q2
    TXT(d, (3.1, 0), "B", fs=11); TXT(d, (4.4, 1.0), "C", fs=11); TXT(d, (4.4, -1.0), "E", fs=11); TXT(d, (4.0, -1.9), "pnp: arrow\npoints in", fs=10)
    return _sd(d, 56)


def bjt_out_curves():
    """CE output curves with the DC load line of the deck's fixed-bias example (VCC = 12 V, RC = 2.2 k, beta = 50)."""
    fig, ax = _fig(5.8, 3.2)
    v = np.linspace(0, 13, 500)
    for ib in (20, 40, 47.08, 60, 80, 100):
        ic = 50 * ib * 1e-3 * (1 - np.exp(-v / 0.12)) * (1 + v / 150)
        hot = abs(ib - 47.08) < 0.01
        ax.plot(v, ic, color=BAD if hot else ACC, lw=1.7 if hot else 1.2)
        ax.text(13.1, ic[-1], f"I_B = {47 if hot else ib} μA", fontsize=7.8, va="center", color=BAD if hot else INK)
    ax.plot([0, 12], [12 / 2.2, 0], color=INK, lw=1.4); ax.plot([6.82], [2.35], "o", color=BAD, ms=5)
    ax.annotate("Q-point\n(6.82 V, 2.35 mA)", (6.82, 2.35), (7.6, 3.4), fontsize=8.3, color=BAD, arrowprops=dict(arrowstyle="-", color=BAD, lw=0.8))
    ax.text(0.25, 5.62, "V_CC/R_C = 5.45 mA", fontsize=8); ax.text(12.15, 0.28, "V_CC", fontsize=8)
    ax.axvspan(0, 0.3, color=G1, alpha=0.18); ax.text(0.38, 4.5, "saturation", fontsize=8, color=G1, rotation=90, va="center")
    ax.text(6, 0.12, "cutoff: I_B = 0", fontsize=8, color=MUTED, ha="center"); ax.text(9.8, 4.6, "active region", fontsize=8.5, color=MUTED)
    ax.set_xlim(0, 16.6); ax.set_ylim(0, 6.2); ax.set_xlabel("V_CE (V)"); ax.set_ylabel("I_C (mA)")
    return _svg(fig)


def _npn(d, at):
    q = elm.BjtNpn(circle=True).theta(0).anchor("base").at(at); d += q
    return q


def bjt_bias_three():
    d = _d(unit=2.1, fs=10)
    yt = 5.4
    # (a) fixed bias: deck L26-27 slide 15
    q = _npn(d, (1.6, 2.4)); xc = q.collector.x
    RES(d, (0.6, yt), (0.6, 2.4), "R_B\n240 kΩ"); W(d, (0.6, 2.4), (1.6, 2.4))
    RES(d, (xc, yt), q.collector, "R_C\n2.2 kΩ", loc="bottom"); W(d, (0.6, yt), (xc, yt)); W(d, q.emitter, (xc, 0.2)); GND(d, (xc, 0.2))
    TXT(d, (1.5, yt + 0.45), "V_CC = +12 V", fs=10); TXT(d, (1.4, -1.0), "(a) fixed bias, β = 50", fs=10)
    # (b) emitter-stabilised: slide 27
    ox = 5.6
    q = _npn(d, (ox + 1.6, 2.6)); xc = q.collector.x
    RES(d, (ox + 0.6, yt), (ox + 0.6, 2.6), "R_B\n430 kΩ"); W(d, (ox + 0.6, 2.6), (ox + 1.6, 2.6))
    RES(d, (xc, yt), q.collector, "R_C\n2 kΩ", loc="bottom"); W(d, (ox + 0.6, yt), (xc, yt))
    RES(d, q.emitter, (xc, 0.2), "R_E\n1 kΩ", loc="bottom"); GND(d, (xc, 0.2))
    TXT(d, (ox + 1.5, yt + 0.45), "V_CC = +20 V", fs=10); TXT(d, (ox + 1.4, -1.0), "(b) emitter bias, β = 50", fs=10)
    # (c) voltage divider
    ox = 11.2
    q = _npn(d, (ox + 1.6, 2.6)); xc = q.collector.x
    RES(d, (ox + 0.6, yt), (ox + 0.6, 2.6), "R_1\n39 kΩ"); RES(d, (ox + 0.6, 2.6), (ox + 0.6, 0.2), "R_2\n3.9 kΩ"); W(d, (ox + 0.6, 2.6), (ox + 1.6, 2.6)); DOT(d, (ox + 0.6, 2.6))
    RES(d, (xc, yt), q.collector, "R_C\n10 kΩ", loc="bottom"); W(d, (ox + 0.6, yt), (xc, yt))
    RES(d, q.emitter, (xc, 0.2), "R_E\n1.5 kΩ", loc="bottom"); W(d, (ox + 0.6, 0.2), (xc, 0.2)); GND(d, (xc, 0.2))
    TXT(d, (ox + 1.5, yt + 0.45), "V_CC = +22 V", fs=10); TXT(d, (ox + 1.4, -1.0), "(c) voltage divider, β = 100", fs=10)
    return _sd(d, 165)


def h_model():
    d = _d(unit=2.2)
    d += elm.Dot(open=True).at((0, 2.6)).label("B", loc="left")
    RES(d, (0, 2.6), (2.4, 2.6), "h_ie")
    d += elm.SourceControlledV().endpoints((2.4, 0), (2.4, 2.6)).label("$h_{re} v_{ce}$", loc="bottom")
    d += elm.SourceControlledI().endpoints((5.0, 2.6), (5.0, 0)).label("$h_{fe} i_b$", loc="bottom")
    RES(d, (7.0, 2.6), (7.0, 0), "$1/h_{oe}$", loc="bottom"); W(d, (5.0, 2.6), (8.4, 2.6)); DOT(d, (7.0, 2.6)); DOT(d, (7.0, 0)); DOT(d, (2.4, 0)); DOT(d, (5.0, 0))
    d += elm.Dot(open=True).at((8.4, 2.6)).label("C", loc="right")
    W(d, (0, 0), (8.4, 0)); d += elm.Dot(open=True).at((0, 0)).label("E", loc="left"); d += elm.Dot(open=True).at((8.4, 0)).label("E", loc="right")
    TXT(d, (1.2, 3.4), "$i_b$", fs=12, color=ACC); TXT(d, (7.9, 3.0), "$i_c$", fs=12, color=ACC)
    TXT(d, (0.3, 1.3), "$v_{be}$", fs=12); TXT(d, (8.6, 1.3), "$v_{ce}$", fs=12)
    return _sd(d, 100)


def darlington():
    d = _d(unit=2.2)
    q1 = elm.BjtNpn(circle=True).theta(0).anchor("base").at((0.8, 2.4)); d += q1
    q2 = elm.BjtNpn(circle=True).theta(0).anchor("base").at((q1.emitter.x + 0.8, q1.emitter.y - 0.7)); d += q2
    W(d, q1.emitter, (q1.emitter.x, q2.base.y)); W(d, (q1.emitter.x, q2.base.y), q2.base)
    yt = 4.2
    W(d, q1.collector, (q1.collector.x, yt)); W(d, q2.collector, (q2.collector.x, yt)); W(d, (q1.collector.x, yt), (q2.collector.x, yt))
    DOT(d, (q2.collector.x, yt)); W(d, (q2.collector.x, yt), (q2.collector.x, yt + 0.6)); d += elm.Dot(open=True).at((q2.collector.x, yt + 0.6)).label("C", loc="top")
    d += elm.Dot(open=True).at((0, 2.4)).label("B", loc="left"); W(d, (0, 2.4), (0.8, 2.4))
    W(d, q2.emitter, (q2.emitter.x, q2.emitter.y - 0.6)); d += elm.Dot(open=True).at((q2.emitter.x, q2.emitter.y - 0.6)).label("E", loc="bottom")
    TXT(d, (0.4, 3.0), "I_B", fs=10, color=ACC); TXT(d, (q1.emitter.x - 0.9, q1.emitter.y - 0.4), "$(1+β_1)I_B$", fs=10, color=ACC)
    TXT(d, (1.2, 3.4), "Q_1", fs=10); TXT(d, (q2.base.x + 1.6, q2.base.y), "Q_2", fs=10)
    return _sd(d, 52)


def two_stage():
    fig, ax = _canvas(7.6, 1.5, (0, 12), (0, 2.4))
    _box(ax, 2.2, 0.6, 2.2, 1.2, "Stage 1\nA_v1", fc="#e8eefe", ec=ACC); _box(ax, 6.6, 0.6, 2.2, 1.2, "Stage 2\nA_v2", fc="#e8eefe", ec=ACC)
    _arrow(ax, (0.5, 1.2), (2.2, 1.2)); _arrow(ax, (4.4, 1.2), (6.6, 1.2)); _arrow(ax, (8.8, 1.2), (10.6, 1.2))
    ax.text(0.4, 1.4, "v_i", fontsize=10); ax.text(5.5, 1.42, "v_o1", fontsize=9, ha="center"); ax.text(10.75, 1.2, "v_o", fontsize=10, va="center")
    ax.text(5.5, 0.72, "coupling:\nRC, transformer\nor direct", fontsize=7.4, ha="center", color=MUTED, va="top")
    ax.text(5.5, 2.2, "A_v = A_v1 × A_v2      (in dB the gains add)", ha="center", fontsize=9.5, weight="bold")
    return _svg(fig)


# ================================================================== Part F: feedback
def fb_block():
    fig, ax = _canvas(7.4, 2.6, (0, 12), (0, 4.2))
    ax.add_patch(Circle((2.6, 3.0), 0.38, fc="white", ec=INK, lw=1.3)); ax.text(2.6, 3.0, "Σ", ha="center", va="center", fontsize=11)
    ax.text(2.1, 3.35, "+", fontsize=10); ax.text(2.75, 2.35, "−", fontsize=12, color=BAD)
    _box(ax, 5.0, 2.4, 2.4, 1.2, "Amplifier\ngain A", fc="#e8eefe", ec=ACC); _box(ax, 5.0, 0.3, 2.4, 1.1, "Feedback\nnetwork β", fc=SOFT, ec=INK)
    _arrow(ax, (0.6, 3.0), (2.22, 3.0)); _arrow(ax, (2.98, 3.0), (5.0, 3.0)); _arrow(ax, (7.4, 3.0), (11.2, 3.0))
    ax.plot([9.4, 9.4], [3.0, 0.85], color=INK, lw=1.3); _arrow(ax, (9.4, 0.85), (7.4, 0.85)); ax.plot([9.4], [3.0], "o", color=INK, ms=4)
    ax.plot([5.0, 2.6], [0.85, 0.85], color=INK, lw=1.3); _arrow(ax, (2.6, 0.85), (2.6, 2.62))
    ax.text(0.5, 3.2, "V_s", fontsize=10); ax.text(4.0, 3.2, "V_i = V_s − V_f", fontsize=9, ha="center"); ax.text(10.4, 3.2, "V_o", fontsize=10)
    ax.text(3.7, 0.5, "V_f = β V_o", fontsize=9, ha="center", color=BAD); ax.text(9.55, 1.9, "sample\nthe output", fontsize=7.8, color=MUTED)
    ax.text(1.0, 1.9, "mix with\nthe input", fontsize=7.8, color=MUTED)
    return _svg(fig)


def fb_topologies():
    fig, ax = _canvas(9.2, 4.6, (0, 16), (0, 8))
    specs = [("Voltage-series", "series", "V", 0, 4.2), ("Voltage-shunt", "shunt", "V", 8.2, 4.2),
             ("Current-series", "series", "I", 0, 0.2), ("Current-shunt", "shunt", "I", 8.2, 0.2)]
    for name, mix, samp, x0, y0 in specs:
        _box(ax, x0 + 2.6, y0 + 1.9, 2.0, 1.1, "A", fc="#e8eefe", ec=ACC, fs=11); _box(ax, x0 + 2.6, y0 + 0.3, 2.0, 0.9, "β", fc=SOFT, ec=INK, fs=11)
        ax.text(x0 + 3.6, y0 + 3.35, name, ha="center", fontsize=9.5, weight="bold")
        # output side
        ax.plot([x0 + 4.6, x0 + 6.6], [y0 + 2.75, y0 + 2.75], color=INK, lw=1.2); ax.plot([x0 + 4.6, x0 + 6.6], [y0 + 2.15, y0 + 2.15], color=INK, lw=1.2)
        ax.add_patch(Rectangle((x0 + 6.6, y0 + 2.05), 0.25, 0.8, fc="white", ec=INK)); ax.text(x0 + 7.0, y0 + 2.45, "R_L", fontsize=8, va="center")
        if samp == "V":   # shunt (parallel) connection at output
            ax.plot([x0 + 5.6, x0 + 5.6, x0 + 4.6], [y0 + 2.75, y0 + 0.95, y0 + 0.95], color=BAD, lw=1.2); ax.plot([x0 + 5.2, x0 + 5.2, x0 + 4.6], [y0 + 2.15, y0 + 0.55, y0 + 0.55], color=BAD, lw=1.2)
            ax.text(x0 + 5.75, y0 + 1.45, "across\nthe load", fontsize=7.2, color=BAD)
        else:             # series connection at output (in the load loop)
            ax.plot([x0 + 5.4, x0 + 5.4, x0 + 4.6], [y0 + 2.15, y0 + 0.95, y0 + 0.95], color=BAD, lw=1.2); ax.plot([x0 + 6.2, x0 + 6.2, x0 + 4.6], [y0 + 2.15, y0 + 0.55, y0 + 0.55], color=BAD, lw=1.2)
            ax.plot([x0 + 5.4, x0 + 6.2], [y0 + 2.15, y0 + 2.15], color="white", lw=3)
            ax.text(x0 + 6.35, y0 + 1.3, "in series\nwith the load", fontsize=7.2, color=BAD)
        # input side
        if mix == "series":
            ax.add_patch(Circle((x0 + 0.5, y0 + 2.45), 0.28, fc="white", ec=INK)); ax.text(x0 + 0.5, y0 + 2.45, "~", ha="center", va="center", fontsize=10)
            ax.plot([x0 + 0.5, x0 + 0.5, x0 + 2.6], [y0 + 2.73, y0 + 2.75, y0 + 2.75], color=INK, lw=1.2)
            ax.plot([x0 + 2.6, x0 + 2.0, x0 + 2.0, x0 + 2.6], [y0 + 2.15, y0 + 2.15, y0 + 0.95, y0 + 0.95], color=G2, lw=1.2)
            ax.plot([x0 + 0.5, x0 + 0.5, x0 + 2.6], [y0 + 2.17, y0 + 0.55, y0 + 0.55], color=G2, lw=1.2)
            ax.text(x0 + 0.72, y0 + 1.3, "V_f in series\nwith V_s", fontsize=7.2, color=G2)
        else:
            ax.add_patch(Circle((x0 + 0.5, y0 + 2.45), 0.28, fc="white", ec=INK)); ax.text(x0 + 0.5, y0 + 2.45, "↑", ha="center", va="center", fontsize=9)
            ax.plot([x0 + 0.5, x0 + 0.5, x0 + 2.6], [y0 + 2.73, y0 + 2.75, y0 + 2.75], color=INK, lw=1.2); ax.plot([x0 + 0.5, x0 + 0.5, x0 + 2.6], [y0 + 2.17, y0 + 2.15, y0 + 2.15], color=INK, lw=1.2)
            ax.plot([x0 + 1.6, x0 + 1.6, x0 + 2.6], [y0 + 2.75, y0 + 0.95, y0 + 0.95], color=G2, lw=1.2); ax.plot([x0 + 1.2, x0 + 1.2, x0 + 2.6], [y0 + 2.15, y0 + 0.55, y0 + 0.55], color=G2, lw=1.2)
            ax.text(x0 + 0.05, y0 + 1.2, "I_f in parallel\nwith I_s", fontsize=7.2, color=G2)
    ax.text(8, -0.35, "green: how the feedback signal is mixed at the input · red: how the output is sampled", ha="center", fontsize=8, color=MUTED); ax.set_ylim(-0.6, 8)
    return _svg(fig)


def fb_bw():
    fig, ax = _fig(5.4, 2.7)
    f = np.logspace(0, 8, 500); fl, fh, A = 100, 2e4, 1000
    mag = lambda A0, lo, hi: A0 / np.sqrt(1 + (lo / f) ** 2) / np.sqrt(1 + (f / hi) ** 2)
    ax.loglog(f, mag(A, fl, fh), color=MUTED, lw=1.5, label="without feedback"); ax.loglog(f, mag(A / 101, fl / 101, fh * 101), color=ACC, lw=1.8, label="with feedback")
    ax.set_ylim(1, 3000); ax.set_xlabel("frequency (Hz)"); ax.set_ylabel("gain")
    ax.annotate("", (2e4, 400), (100, 400), arrowprops=dict(arrowstyle="<->", color=MUTED)); ax.text(1400, 460, "BW", fontsize=8, color=MUTED, ha="center")
    ax.annotate("", (2.02e6, 4.4), (1, 4.4), arrowprops=dict(arrowstyle="<->", color=ACC)); ax.text(1400, 5.1, "BW × (1 + βA)", fontsize=8, color=ACC, ha="center")
    ax.text(3e5, 250, "gain ÷ (1 + βA)\nbandwidth × (1 + βA)\ngain × BW unchanged", fontsize=8); ax.legend(frameon=False, fontsize=8, loc="upper left"); ax.set_xlim(1, 1e9)
    return _svg(fig)


# ================================================================== Part G: oscillators
def osc_block():
    fig, ax = _canvas(6.6, 2.3, (0, 11), (0, 3.8))
    _box(ax, 3.6, 2.2, 2.6, 1.2, "Amplifier A", fc="#e8eefe", ec=ACC); _box(ax, 3.6, 0.3, 2.6, 1.1, "Frequency-selective\nfeedback β", fc=SOFT, ec=INK, fs=8.6)
    _arrow(ax, (6.2, 2.8), (10.2, 2.8)); ax.plot([8.4, 8.4], [2.8, 0.85], color=INK, lw=1.3); _arrow(ax, (8.4, 0.85), (6.2, 0.85)); ax.plot([8.4], [2.8], "o", color=INK, ms=4)
    ax.plot([3.6, 1.6, 1.6], [0.85, 0.85, 2.8], color=INK, lw=1.3); _arrow(ax, (1.6, 2.8), (3.6, 2.8))
    ax.text(9.2, 3.0, "V_o", fontsize=10); ax.text(1.75, 1.8, "V_f = β V_o\nreturns in phase", fontsize=8, color=BAD); ax.text(0.2, 3.3, "no input signal", fontsize=8.5, color=MUTED)
    ax.text(8.6, 1.7, "loop gain βA = 1\ntotal phase 0° or 360°", fontsize=8.6, weight="bold")
    return _svg(fig)


def phase_shift_osc():
    d = _d(unit=2.1, fs=10)
    op = elm.Opamp().theta(0).at((0, 0)).anchor("in1"); d += op
    W(d, op.in2, (op.in2.x - 0.5, op.in2.y)); W(d, (op.in2.x - 0.5, op.in2.y), (op.in2.x - 0.5, op.in2.y - 0.4)); GND(d, (op.in2.x - 0.5, op.in2.y - 0.4))
    # Rf
    W(d, op.in1, (op.in1.x, 1.6)); RES(d, (op.in1.x, 1.6), (op.out.x, 1.6), "R_f = 29R"); W(d, (op.out.x, 1.6), op.out); DOT(d, op.out); DOT(d, op.in1)
    # ladder from output
    y = -3.6; x0 = op.out.x + 0.6
    W(d, op.out, (x0, op.out.y)); W(d, (x0, op.out.y), (x0, y)); OUT(d, (x0 + 0.8, op.out.y), "V_o"); W(d, (x0, op.out.y), (x0 + 0.8, op.out.y))
    xs = [x0, x0 - 2.3, x0 - 4.6, x0 - 6.9]
    for i in range(3):
        CAP(d, (xs[i], y), (xs[i + 1], y), "C", loc="bottom")
        if i < 2:
            RES(d, (xs[i + 1], y), (xs[i + 1], y - 2.0), "R", loc="bottom"); DOT(d, (xs[i + 1], y)); GND(d, (xs[i + 1], y - 2.0))
    RES(d, (xs[3], y), (xs[3], op.in1.y), "R"); W(d, (xs[3], op.in1.y), op.in1)
    return _sd(d, 120)


def wien_osc():
    d = _d(unit=2.1, fs=10)
    op = elm.Opamp().theta(0).at((0, 0)).anchor("in2").flip(); d += op      # + input on top after flip
    xo = op.out.x + 0.8
    W(d, op.out, (xo, op.out.y)); OUT(d, (xo + 0.6, op.out.y), "V_o"); W(d, (xo, op.out.y), (xo + 0.6, op.out.y)); DOT(d, (xo, op.out.y))
    # positive feedback: series RC from output to + input, parallel RC from + input to ground
    yp = op.in2.y; xn = op.in2.x - 1.0
    W(d, (xo, op.out.y), (xo, 2.6)); RES(d, (xo, 2.6), (xo - 2.4, 2.6), "R"); CAP(d, (xo - 2.4, 2.6), (xn, 2.6), "C"); W(d, (xn, 2.6), (xn, yp)); W(d, (xn, yp), op.in2); DOT(d, (xn, yp))
    W(d, (xn, yp), (xn - 1.6, yp)); DOT(d, (xn - 1.0, yp)) if False else None
    RES(d, (xn, yp), (xn, yp - 2.6), "R"); W(d, (xn - 1.6, yp), (xn - 1.6, yp - 0.3)); CAP(d, (xn - 1.6, yp - 0.3), (xn - 1.6, yp - 2.6), "C")
    W(d, (xn - 1.6, yp - 2.6), (xn, yp - 2.6)); GND(d, (xn, yp - 2.6))
    # negative feedback: R2 from output to - input, R1 to ground
    ym = op.in1.y
    W(d, (xo, op.out.y), (xo, ym - 1.6)); RES(d, (xo, ym - 1.6), (op.in1.x, ym - 1.6), "$R_2 = 2R_1$", loc="bottom"); W(d, (op.in1.x, ym - 1.6), op.in1) if False else None
    W(d, op.in1, (op.in1.x - 0.3, ym)); W(d, (op.in1.x - 0.3, ym), (op.in1.x - 0.3, ym - 1.6)); W(d, (op.in1.x - 0.3, ym - 1.6), (op.in1.x, ym - 1.6)); DOT(d, (op.in1.x - 0.3, ym - 1.6))
    RES(d, (op.in1.x - 0.3, ym - 1.6), (op.in1.x - 0.3, ym - 3.6), "R_1", loc="bottom"); GND(d, (op.in1.x - 0.3, ym - 3.6))
    return _sd(d, 105)


def lc_tanks():
    d = _d(unit=2.1, fs=10)

    def tank(ox, kind):
        nonlocal d
        y1, y0 = 2.4, 0.0
        if kind == "Hartley":
            d += elm.Inductor2().endpoints((ox, y0), (ox + 2.0, y0)).label("L_1", loc="bottom"); d += elm.Inductor2().endpoints((ox + 2.0, y0), (ox + 4.0, y0)).label("L_2", loc="bottom")
            CAP(d, (ox, y1), (ox + 4.0, y1), "C")
        else:
            CAP(d, (ox, y0), (ox + 2.0, y0), "C_1", loc="bottom"); CAP(d, (ox + 2.0, y0), (ox + 4.0, y0), "C_2", loc="bottom")
            d += elm.Inductor2().endpoints((ox, y1), (ox + 4.0, y1)).label("L")
        W(d, (ox, y0), (ox, y1)); W(d, (ox + 4.0, y0), (ox + 4.0, y1)); DOT(d, (ox + 2.0, y0)); GND(d, (ox + 2.0, y0))
        d += elm.Dot(open=True).at((ox, y1 + 0.9)).label("to amplifier input", loc="top"); W(d, (ox, y1), (ox, y1 + 0.9))
        d += elm.Dot(open=True).at((ox + 4.0, y1 + 0.9)).label("from amplifier output", loc="top"); W(d, (ox + 4.0, y1), (ox + 4.0, y1 + 0.9))
        TXT(d, (ox + 2.0, -1.9), {"Hartley": "Hartley: tapped inductor\n$L_{eq} = L_1 + L_2$", "Colpitts": "Colpitts: tapped capacitor\n$C_{eq} = C_1C_2/(C_1+C_2)$"}[kind], fs=10)
    tank(0, "Hartley"); tank(7.6, "Colpitts")
    return _sd(d, 140)


def crystal_fig():
    d = _d(unit=2.1, fs=10)
    d += elm.Crystal().endpoints((0, 1.2), (2.0, 1.2)).label("symbol", loc="bottom")
    TXT(d, (2.9, 1.2), "=", fs=14)
    x0 = 3.8
    RES(d, (x0, 2.0), (x0 + 1.8, 2.0), "R_s"); d += elm.Inductor2().endpoints((x0 + 1.8, 2.0), (x0 + 3.6, 2.0)).label("L_s"); CAP(d, (x0 + 3.6, 2.0), (x0 + 5.4, 2.0), "C_s")
    CAP(d, (x0, 0.2), (x0 + 5.4, 0.2), "C_p  (holder + plates)", loc="bottom")
    W(d, (x0, 2.0), (x0, 0.2)); W(d, (x0 + 5.4, 2.0), (x0 + 5.4, 0.2)); W(d, (x0 - 0.6, 1.1), (x0, 1.1)); W(d, (x0 + 5.4, 1.1), (x0 + 6.0, 1.1)); DOT(d, (x0, 1.1)); DOT(d, (x0 + 5.4, 1.1))
    c = _sd(d, 96)
    fig, ax = _fig(3.5, 2.3)
    f = np.linspace(0.6, 1.6, 2000); fs_, fp = 1.0, 1.12
    X = (f ** 2 - fs_ ** 2) / (f * (fp ** 2 - f ** 2))
    X[np.abs(X) > 9] = np.nan
    ax.plot(f, X, color=ACC, lw=1.6); ax.axhline(0, color=INK, lw=0.8)
    ax.axvline(fs_, color=BAD, lw=0.8, ls=":"); ax.axvline(fp, color=BAD, lw=0.8, ls=":")
    ax.set_xticks([fs_, fp]); ax.set_xticklabels(["$f_s$", "$f_p$"]); ax.set_yticks([0]); ax.set_ylim(-9, 9); ax.set_xlabel("frequency"); ax.set_ylabel("reactance X")
    ax.text(1.055, 5.5, "inductive", fontsize=7.6, ha="center", color=G2, rotation=90); ax.text(0.75, -7.5, "capacitive", fontsize=7.6, color=MUTED); ax.text(1.3, -7.5, "capacitive", fontsize=7.6, color=MUTED)
    return f'<div class="two">{c}{_svg(fig)}</div>'
