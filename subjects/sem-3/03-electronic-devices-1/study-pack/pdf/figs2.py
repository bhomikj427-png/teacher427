"""Figures for EDC-ETE-v1.pdf, Parts C (JFET) and D (MOSFET). Each public function returns inline SVG."""
import numpy as np
import schemdraw.elements as elm
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

from figs import (_fig, _canvas, _svg, _sd, _d, _box, _arrow, W, RES, CAP, DOT, TXT, GND, OUT, RC,
                  INK, MUTED, LINE, SOFT, ACC, G1, G2, G3, BAD, NCOL, PCOL)


# ================================================================== Part C: JFET
def jfet_struct():
    """n-channel JFET cross-section at V_GS = 0 (left) and with reverse gate bias (right)."""
    fig, ax = _canvas(8.4, 3.0, (0, 14), (0, 5))
    for k, (x0, dep, title) in enumerate(((0.8, 0.35, "V_GS = 0: channel wide open"), (8.0, 0.95, "V_GS negative: depletion widens,\nchannel narrows"))):
        ax.add_patch(Rectangle((x0 + 1, 0.6), 3, 3.4, fc=NCOL, ec=INK))
        for gx in (x0 + 0.4, x0 + 4.0):
            ax.add_patch(Rectangle((gx, 1.4), 0.6, 1.8, fc=PCOL, ec=INK)); ax.text(gx + 0.3, 2.3, "p", ha="center", va="center", fontsize=9, color=BAD)
        ax.add_patch(Polygon([(x0 + 1, 1.3), (x0 + 1 + dep, 1.5), (x0 + 1 + dep * 1.25, 3.2), (x0 + 1, 3.3)], fc="white", ec=G1, hatch="////", lw=0.8))
        ax.add_patch(Polygon([(x0 + 4, 1.3), (x0 + 4 - dep, 1.5), (x0 + 4 - dep * 1.25, 3.2), (x0 + 4, 3.3)], fc="white", ec=G1, hatch="////", lw=0.8))
        ax.text(x0 + 2.5, 2.3, "n\nchannel", ha="center", va="center", fontsize=8.5)
        ax.text(x0 + 2.5, 4.2, "Drain (D)", ha="center", fontsize=8.8); ax.text(x0 + 2.5, 0.2, "Source (S)", ha="center", fontsize=8.8)
        ax.text(x0 - 0.1, 2.3, "Gate\n(G)", ha="right", va="center", fontsize=8.8)
        _arrow(ax, (x0 + 2.5, 0.9), (x0 + 2.5, 1.4), color=ACC); _arrow(ax, (x0 + 2.5, 3.25), (x0 + 2.5, 3.75), color=ACC)
        ax.text(x0 + 2.5, 4.72, title, ha="center", fontsize=8.6, weight="bold", va="center")
    ax.text(7.0, 0.3, "hatched =\ndepletion region", ha="center", fontsize=7.8, color=G1)
    ax.text(7.0, 3.7, "electrons\nflow S → D", ha="center", fontsize=7.8, color=ACC)
    return _svg(fig)


def _shock(vgs, idss=8.0, vp=-4.0):
    return idss * (1 - vgs / vp) ** 2


def jfet_curves():
    with plt.rc_context(RC):
        fig, (a, b) = plt.subplots(1, 2, figsize=(8.6, 3.0), gridspec_kw={"width_ratios": [1, 1.5], "wspace": 0.05}, sharey=True)
    vg = np.linspace(-4, 0, 200)
    a.plot(vg, _shock(vg), color=ACC, lw=1.8); a.set_xlim(-4.4, 0); a.set_ylim(0, 9.2)
    a.set_xticks([-4, -3, -2, -1, 0]); a.set_xlabel("V_GS (V)"); a.set_ylabel("I_D (mA)"); a.set_title("Transfer curve", fontsize=9)
    a.text(-4.3, 0.35, "V_P = −4 V", fontsize=8, color=BAD); a.text(-1.9, 8.3, "I_DSS = 8 mA", fontsize=8, color=BAD)
    a.yaxis.tick_right(); a.spines["left"].set_visible(False); a.spines["right"].set_visible(True)
    vd = np.linspace(0, 14, 400)
    for vgs in (0, -1, -2, -3):
        isat = _shock(vgs); vsat = vgs + 4
        i = np.where(vd < vsat, isat * (2 * vd / vsat - (vd / vsat) ** 2), isat)
        b.plot(vd, i, color=ACC, lw=1.6); b.text(14.1, isat, f"V_GS = {vgs} V", fontsize=8, va="center")
        a.plot([vgs, 0], [isat, isat], color=LINE, lw=0.7, ls=":")
    vs = np.linspace(0, 4, 50); b.plot(vs, 8 * (vs / 4) ** 2, color=G1, lw=1, ls="--")
    b.text(3.2, 8.6, "pinch-off locus\nV_DS = V_GS − V_P", fontsize=7.8, color=G1)
    b.text(9, 3.0, "left of the dashed line: ohmic region", fontsize=8, color=MUTED, ha="center"); b.text(8, 5.2, "saturation (constant-current) region", fontsize=8, color=MUTED, ha="center")
    b.set_xlim(0, 17.5); b.set_xlabel("V_DS (V)"); b.set_title("Drain (output) curves", fontsize=9); b.tick_params(left=False)
    b.spines["left"].set_visible(False)
    return _svg(fig)


def _jfet(d, at, lab_="", anchor="gate"):
    j = elm.JFetN(circle=True).theta(0).reverse().anchor(anchor).at(at)
    if lab_:
        j = j.label(lab_, loc="right")
    d += j
    return j


def jfet_self_bias():
    d = _d()
    j = _jfet(d, (2.4, 2.6))
    RES(d, (j.drain.x, 5.6), j.drain, "R_D\n3.3 kΩ", loc="bottom"); RES(d, j.source, (j.source.x, 0), "R_S\n1 kΩ", loc="bottom")
    RES(d, (1.2, 2.6), (1.2, 0), "R_G\n1 MΩ"); W(d, (1.2, 2.6), (2.4, 2.6)); DOT(d, (1.2, 2.6))
    W(d, (1.2, 0), (j.source.x, 0)); GND(d, (j.source.x, 0))
    d += elm.Dot(open=True).at((j.drain.x, 5.6)).label("V_DD = +20 V", loc="top")
    return _sd(d, 52)


def jfet_divider():
    """Professor's sheet Q17 (Fig. 9)."""
    d = _d()
    j = _jfet(d, (2.6, 2.4))
    yt = 5.4
    RES(d, (1.2, yt), (1.2, 2.4), "R_1\n6.8 MΩ"); RES(d, (1.2, 2.4), (1.2, -0.4), "R_2\n1 MΩ")
    W(d, (1.2, 2.4), (2.6, 2.4)); DOT(d, (1.2, 2.4))
    RES(d, (j.drain.x, yt), j.drain, "R_D\n3.3 kΩ", loc="bottom"); RES(d, j.source, (j.source.x, -0.4), "R_S\n1.8 kΩ", loc="bottom")
    W(d, (1.2, yt), (j.drain.x, yt)); W(d, (1.2, -0.4), (j.source.x, -0.4)); GND(d, (j.source.x, -0.4))
    d += elm.Dot(open=True).at(((1.2 + j.drain.x) / 2, yt)).label("V_DD = +12 V", loc="top")
    DOT(d, j.drain); TXT(d, (j.drain.x + 1.6, j.drain.y + 0.1), "V_D = 7 V", color=BAD, fs=11)
    return _sd(d, 62)


def fet_cs_amp(kind="jfet"):
    d = _d(unit=2.2)
    d += elm.Dot(open=True).at((0, 2.6)).label("v_i", loc="left")
    CAP(d, (0, 2.6), (1.6, 2.6), "C_1")
    RES(d, (1.6, 2.6), (1.6, 0), "R_G", loc="bottom"); DOT(d, (1.6, 2.6)); W(d, (1.6, 2.6), (2.8, 2.6))
    j = _jfet(d, (2.8, 2.6))
    RES(d, (j.drain.x, 5.6), j.drain, "R_D"); RES(d, j.source, (j.source.x, 0), "R_S")
    xs = j.source.x
    W(d, j.source, (xs + 1.6, j.source.y)); CAP(d, (xs + 1.6, j.source.y), (xs + 1.6, 0), "C_S", loc="bottom"); DOT(d, j.source)
    DOT(d, j.drain); CAP(d, j.drain, (xs + 2.6, j.drain.y), "C_2"); OUT(d, (xs + 2.6, j.drain.y), "v_o")
    W(d, (0.6, 0), (xs + 1.6, 0)); GND(d, (xs, 0))
    d += elm.Dot(open=True).at((xs, 5.6)).label("+V_DD", loc="top")
    return _sd(d, 70)


def fet_small_signal():
    d = _d(unit=2.2)
    d += elm.Dot(open=True).at((0, 2.4)).label("G", loc="left"); W(d, (0, 2.4), (1.2, 2.4))
    TXT(d, (0.6, 1.2), "$v_{gs}$", fs=12)
    d += elm.Dot(open=True).at((1.2, 2.4)); d += elm.Dot(open=True).at((1.2, 0))
    d += elm.SourceControlledI().endpoints((3.2, 2.4), (3.2, 0)).label("$g_m v_{gs}$", loc="bottom")
    RES(d, (5.2, 2.4), (5.2, 0), "r_d", loc="bottom"); W(d, (3.2, 2.4), (6.6, 2.4)); DOT(d, (5.2, 2.4)); DOT(d, (5.2, 0))
    d += elm.Dot(open=True).at((6.6, 2.4)).label("D", loc="right")
    W(d, (0, 0), (6.6, 0)); d += elm.Dot(open=True).at((0, 0)).label("S", loc="left"); d += elm.Dot(open=True).at((6.6, 0)).label("S", loc="right")
    return _sd(d, 78)


# ================================================================== Part D: MOSFET
def mos_struct():
    fig, ax = _canvas(8.6, 3.1, (0, 14), (0, 5.2))
    for k, (x0, on) in enumerate(((0.4, False), (7.4, True))):
        ax.add_patch(Rectangle((x0, 0.5), 6, 2.4, fc=PCOL, ec=INK)); ax.text(x0 + 3, 1.0, "p-type substrate (body)", ha="center", fontsize=8.5)
        for sx, name in ((x0 + 0.4, "n⁺"), (x0 + 4.2, "n⁺")):
            ax.add_patch(Rectangle((sx, 2.1), 1.4, 0.8, fc=NCOL, ec=INK)); ax.text(sx + 0.7, 2.5, name, ha="center", va="center", fontsize=9)
        ax.add_patch(Rectangle((x0 + 1.8, 2.9), 2.4, 0.22, fc="#fde68a", ec=INK)); ax.add_patch(Rectangle((x0 + 1.8, 3.12), 2.4, 0.35, fc="#9ca3af", ec=INK))
        ax.text(x0 + 4.35, 3.0, "oxide (SiO₂)", fontsize=7.5, va="center"); ax.text(x0 + 3.0, 3.3, "gate", ha="center", va="center", fontsize=7.8, color="white")
        for tx, name in ((x0 + 1.1, "S"), (x0 + 3.0, "G"), (x0 + 4.9, "D")):
            y0 = 3.47 if name == "G" else 2.9
            ax.plot([tx, tx], [y0, 4.1], color=INK, lw=1.2); ax.text(tx, 4.25, name, ha="center", fontsize=10, weight="bold")
        if on:
            ax.add_patch(Rectangle((x0 + 1.8, 2.72), 2.4, 0.18, fc=ACC, ec="none")); ax.text(x0 + 3.0, 2.45, "induced n channel", ha="center", fontsize=8, color=ACC)
            _arrow(ax, (x0 + 1.4, 2.81), (x0 + 4.6, 2.81), color="white", lw=0.8)
        else:
            ax.text(x0 + 3.0, 2.45, "no channel", ha="center", fontsize=8, color=BAD)
        ax.text(x0 + 3, 4.85, "V_GS > V_T : ON (electrons pulled under the gate)" if on else "V_GS < V_T : OFF (two back-to-back junctions)", ha="center", fontsize=8.8, weight="bold")
        ax.text(x0 + 3, 0.15, "L = channel length (S to D), W = width into the page", ha="center", fontsize=7.4, color=MUTED)
    return _svg(fig)


def mos_symbols():
    d = _d(unit=2.2)
    items = ((elm.NFet, "n-channel\nenhancement"), (elm.PFet, "p-channel\nenhancement"), (elm.NMos, "n-channel\n(4-terminal)"), (elm.JFetN, "n-JFET\n(compare)"))
    for i, (el, name) in enumerate(items):
        e = el().at((i * 3.4, 0)); d += e
        TXT(d, (i * 3.4 + 0.5, -2.7), name, fs=10)
    return _sd(d, 120)


def mos_curves():
    with plt.rc_context(RC):
        fig, (a, b) = plt.subplots(1, 2, figsize=(8.6, 3.0), gridspec_kw={"width_ratios": [1, 1.5], "wspace": 0.28})
    K, vt = 0.5, 2.0
    vg = np.linspace(0, 7, 300)
    a.plot(vg, np.where(vg > vt, K * (vg - vt) ** 2, 0), color=ACC, lw=1.8, label="enhancement")
    vg2 = np.linspace(-4, 3, 300); a.plot(vg2 + 0, 8 * (1 + vg2 / 4) ** 2 * 0.5, color=G1, lw=1.5, ls="--", label="depletion")
    a.axvline(0, color=LINE, lw=0.7); a.set_ylim(0, 12.5); a.set_xlim(-4.3, 7.2)
    a.set_xticks([-4, 0, 2]); a.set_xticklabels(["$V_P$", "0", "$V_T$"]); a.set_yticks([]); a.set_xlabel("V_GS"); a.set_ylabel("I_D")
    a.set_title("Transfer curves (n-channel)", fontsize=9); a.legend(frameon=False, fontsize=8, loc="upper left")
    a.text(0.15, 4.25, "I_DSS", fontsize=8, color=G1)
    vd = np.linspace(0, 12, 400)
    for vgs in (3, 4, 5, 6):
        vov = vgs - vt; isat = K * vov ** 2
        b.plot(vd, np.where(vd < vov, K * (2 * vov * vd - vd ** 2), isat), color=ACC, lw=1.6); b.text(12.1, isat, f"V_GS = {vgs} V", fontsize=8, va="center")
    vs = np.linspace(0, 4, 50); b.plot(vs, K * vs ** 2, color=G1, lw=1, ls="--")
    b.text(4.1, 8.4, "V_DS = V_GS − V_T", fontsize=8, color=G1)
    b.text(8.5, 3.1, "left of the dashed line: triode · right: saturation", fontsize=8, color=MUTED, ha="center")
    b.set_xlim(0, 15.4); b.set_ylim(0, 9.4); b.set_xlabel("V_DS (V)"); b.set_ylabel("I_D (mA)"); b.set_title("Drain curves: K = 0.5 mA/V², V_T = 2 V", fontsize=9)
    return _svg(fig)


def _nfet(d, at, anchor="gate"):
    m = elm.NFet().theta(0).reverse().anchor(anchor).at(at); d += m
    return m


def mos_bias_three():
    d = _d(unit=2.1, fs=10)
    # (a) voltage divider
    m = _nfet(d, (2.4, 2.4)); yt = 5.2
    RES(d, (1.2, yt), (1.2, 2.4), "R_1\n7 MΩ"); RES(d, (1.2, 2.4), (1.2, -0.3), "R_2\n3 MΩ")
    W(d, (1.2, 2.4), (2.4, 2.4)); DOT(d, (1.2, 2.4))
    RES(d, (m.drain.x, yt), m.drain, "R_D\n3 kΩ", loc="bottom"); RES(d, m.source, (m.source.x, -0.3), "R_S\n1 kΩ", loc="bottom")
    W(d, (1.2, yt), (m.drain.x, yt)); W(d, (1.2, -0.3), (m.source.x, -0.3)); GND(d, (m.source.x, -0.3))
    TXT(d, ((1.2 + m.drain.x) / 2, yt + 0.4), "V_DD = +20 V", fs=10); TXT(d, (2.2, -1.5), "(a) voltage-divider bias", fs=10)
    # (b) drain-to-gate feedback
    ox = 7.6
    m2 = _nfet(d, (ox + 1.6, 2.4)); yj = 4.3
    RES(d, (m2.drain.x, yt + 0.6), (m2.drain.x, yj), "R_D  4 kΩ", loc="bottom"); W(d, (m2.drain.x, yj), m2.drain); DOT(d, (m2.drain.x, yj))
    W(d, (m2.drain.x, yj), (ox + 0.4, yj)); RES(d, (ox + 0.4, yj), (ox + 0.4, 2.4), "R_G\n10 MΩ"); W(d, (ox + 0.4, 2.4), (ox + 1.6, 2.4))
    W(d, m2.source, (m2.source.x, -0.3)); GND(d, (m2.source.x, -0.3))
    TXT(d, (m2.drain.x, yt + 1.0), "V_DD = +12 V", fs=10); TXT(d, (ox + 1.4, -1.5), "(b) drain-feedback bias", fs=10)
    return _sd(d, 125)


def mos_ss_table():
    d = _d(unit=2.1, fs=10)
    # CS
    def stage(ox, kind):
        nonlocal d
        m = _nfet(d, (ox + 1.4, 2.4))
        if kind == "CS":
            RES(d, (m.drain.x, 4.9), m.drain, "R_D"); W(d, m.source, (m.source.x, 0.4)); GND(d, (m.source.x, 0.4))
            d += elm.Dot(open=True).at((ox + 0.4, 2.4)).label("v_i", loc="left"); W(d, (ox + 0.4, 2.4), (ox + 1.4, 2.4))
            DOT(d, m.drain); W(d, m.drain, (m.drain.x + 1.0, m.drain.y)); OUT(d, (m.drain.x + 1.0, m.drain.y), "v_o")
        elif kind == "CD":
            W(d, m.drain, (m.drain.x, 4.9)); RES(d, m.source, (m.source.x, -0.4), "R_S"); GND(d, (m.source.x, -0.4))
            d += elm.Dot(open=True).at((ox + 0.4, 2.4)).label("v_i", loc="left"); W(d, (ox + 0.4, 2.4), (ox + 1.4, 2.4))
            DOT(d, m.source); W(d, m.source, (m.source.x + 1.0, m.source.y)); OUT(d, (m.source.x + 1.0, m.source.y), "v_o")
        else:
            RES(d, (m.drain.x, 4.9), m.drain, "R_D"); GND(d, (ox + 0.6, 2.0)); W(d, (ox + 0.6, 2.4), (ox + 1.4, 2.4)); W(d, (ox + 0.6, 2.4), (ox + 0.6, 2.0))
            W(d, m.source, (m.source.x, 0.6)); d += elm.Dot(open=True).at((m.source.x, 0.6)).label("v_i", loc="bottom")
            DOT(d, m.drain); W(d, m.drain, (m.drain.x + 1.0, m.drain.y)); OUT(d, (m.drain.x + 1.0, m.drain.y), "v_o")
        d += elm.Dot(open=True).at((m.drain.x, 4.9)).label("+V_DD", loc="top")
        TXT(d, (ox + 2.0, -1.4), {"CS": "Common source", "CD": "Common drain\n(source follower)", "CG": "Common gate"}[kind], fs=10)
    stage(0, "CS"); stage(5.6, "CD"); stage(11.2, "CG")
    return _sd(d, 150)


def cmos_inv():
    d = _d(unit=2.1, fs=10)
    p = elm.PFet().theta(0).reverse().anchor("gate").at((1.6, 3.6)); d += p
    n = elm.NFet().theta(0).reverse().anchor("gate").at((1.6, 1.4)); d += n
    W(d, p.drain, n.drain) if abs(p.drain.x - n.drain.x) < 1e-6 else None
    W(d, (1.6, 3.6), (1.0, 3.6)); W(d, (1.6, 1.4), (1.0, 1.4)); W(d, (1.0, 3.6), (1.0, 1.4)); DOT(d, (1.0, 2.5))
    d += elm.Dot(open=True).at((0.2, 2.5)).label("V_in", loc="left"); W(d, (0.2, 2.5), (1.0, 2.5))
    xm = n.drain.x; ym = (p.drain.y + n.drain.y) / 2
    DOT(d, (xm, ym)); W(d, (xm, ym), (xm + 1.2, ym)); OUT(d, (xm + 1.2, ym), "V_out")
    d += elm.Dot(open=True).at(p.source).label("V_DD", loc="top"); GND(d, n.source)
    TXT(d, (xm + 1.3, 3.6), "pMOS: ON when\nV_in is LOW", fs=9, color=MUTED, halign="left")
    TXT(d, (xm + 1.3, 1.3), "nMOS: ON when\nV_in is HIGH", fs=9, color=MUTED, halign="left")
    return _sd(d, 62)


def cmos_vtc():
    fig, ax = _fig(3.6, 2.6)
    v = np.linspace(0, 5, 400)
    ax.plot(v, 5 / (1 + np.exp((v - 2.5) * 6)), color=ACC, lw=1.8)
    ax.set_xticks([0, 2.5, 5]); ax.set_xticklabels(["0", "$V_{DD}/2$", "$V_{DD}$"]); ax.set_yticks([0, 5]); ax.set_yticklabels(["0", "$V_{DD}$"])
    ax.set_xlabel("V_in"); ax.set_ylabel("V_out"); ax.text(0.2, 4.3, "nMOS off,\npMOS on", fontsize=8, color=MUTED); ax.text(3.3, 0.6, "nMOS on,\npMOS off", fontsize=8, color=MUTED)
    ax.text(2.65, 2.6, "both on briefly:\nthe only time\ncurrent flows", fontsize=7.8, color=BAD)
    return _svg(fig)


def _gate_net(ax, x, y, name, p=False):
    """Tiny transistor glyph: box with gate label."""
    ax.add_patch(Rectangle((x - 0.32, y - 0.28), 0.64, 0.56, fc=PCOL if p else NCOL, ec=INK, lw=1, zorder=3))
    ax.text(x, y, name, ha="center", va="center", fontsize=8.5, zorder=4)
    if p:
        ax.add_patch(plt.Circle((x - 0.4, y), 0.07, fc="white", ec=INK, lw=0.9, zorder=4))


def cmos_gates():
    """Switch-network view of CMOS NAND, NOR and f = (a(b+c))'. Blue = nMOS (pull-down), red = pMOS (pull-up)."""
    fig, ax = _canvas(8.8, 3.9, (0, 15), (0, 6.6))
    L = lambda xs, ys: ax.plot(xs, ys, color=INK, lw=1.1)

    def rails(x0, w, title, f):
        L([x0, x0 + w], [6.0, 6.0]); ax.text(x0 + w / 2, 6.12, "V_DD", ha="center", fontsize=8)
        L([x0, x0 + w], [0.5, 0.5]); ax.text(x0 + w / 2, 0.18, "GND", ha="center", fontsize=8)
        ax.text(x0 + w / 2, 6.45, title, ha="center", fontsize=9, weight="bold")
        ax.plot([x0 + w / 2], [3.25], "o", color=INK, ms=3.5); L([x0 + w / 2, x0 + w + 0.1], [3.25, 3.25]); ax.text(x0 + w + 0.15, 3.25, f, fontsize=8.5, va="center")
    # NAND: pMOS parallel, nMOS series
    x0 = 0.3; rails(x0, 3.6, "NAND", "(ab)′"); c = x0 + 1.8
    for dx, nm in ((-0.9, "a"), (0.9, "b")):
        L([c + dx, c + dx], [6.0, 4.2]); _gate_net(ax, c + dx, 5.0, nm, p=True)
    L([c - 0.9, c + 0.9], [4.2, 4.2]); L([c, c], [4.2, 0.5]); _gate_net(ax, c, 2.4, "a"); _gate_net(ax, c, 1.4, "b")
    # NOR: pMOS series, nMOS parallel
    x0 = 5.0; rails(x0, 3.6, "NOR", "(a+b)′"); c = x0 + 1.8
    L([c, c], [6.0, 2.3]); _gate_net(ax, c, 5.2, "a", p=True); _gate_net(ax, c, 4.2, "b", p=True)
    L([c - 0.9, c + 0.9], [2.3, 2.3])
    for dx, nm in ((-0.9, "a"), (0.9, "b")):
        L([c + dx, c + dx], [2.3, 0.5]); _gate_net(ax, c + dx, 1.4, nm)
    # complex gate
    x0 = 9.7; rails(x0, 4.4, "f = (a·(b + c))′", "f"); c = x0 + 2.2
    # pull-up: a' || (b' series c')
    L([c - 1.1, c - 1.1], [6.0, 4.0]); _gate_net(ax, c - 1.1, 5.0, "a", p=True)
    L([c + 1.1, c + 1.1], [6.0, 4.0]); _gate_net(ax, c + 1.1, 5.45, "b", p=True); _gate_net(ax, c + 1.1, 4.6, "c", p=True)
    L([c - 1.1, c + 1.1], [4.0, 4.0]); L([c, c], [4.0, 2.4])
    # pull-down: a series (b || c)
    _gate_net(ax, c, 2.75, "a"); L([c - 0.9, c + 0.9], [2.4, 2.4]); L([c - 0.9, c + 0.9], [0.9, 0.9]); L([c, c], [0.9, 0.5])
    for dx, nm in ((-0.9, "b"), (0.9, "c")):
        L([c + dx, c + dx], [2.4, 0.9]); _gate_net(ax, c + dx, 1.65, nm)
    ax.text(0.3, -0.35, "Each box is one transistor, labelled with its gate input. Red with a bubble = pMOS (closes on 0). Blue = nMOS (closes on 1).", fontsize=7.8, color=MUTED)
    ax.set_ylim(-0.5, 6.7)
    return _svg(fig)


def finfet_fig():
    fig, ax = _canvas(7.6, 2.9, (0, 13), (0, 5))
    # planar
    ax.add_patch(Rectangle((0.4, 0.6), 5, 1.6, fc=PCOL, ec=INK)); ax.text(2.9, 1.0, "substrate", ha="center", fontsize=8)
    ax.add_patch(Rectangle((0.8, 1.8), 1.2, 0.4, fc=NCOL, ec=INK)); ax.add_patch(Rectangle((3.8, 1.8), 1.2, 0.4, fc=NCOL, ec=INK))
    ax.add_patch(Rectangle((2.0, 2.2), 1.8, 0.5, fc="#9ca3af", ec=INK)); ax.text(2.9, 2.45, "gate", ha="center", va="center", fontsize=8, color="white")
    ax.text(1.4, 2.0, "S", ha="center", va="center", fontsize=8); ax.text(4.4, 2.0, "D", ha="center", va="center", fontsize=8)
    ax.text(2.9, 3.4, "Planar MOSFET\ngate touches the channel on 1 side", ha="center", fontsize=8.6, weight="bold")
    # finfet (end view of fin)
    ax.add_patch(Rectangle((7.6, 0.6), 5, 0.8, fc=PCOL, ec=INK)); ax.text(10.1, 0.95, "substrate", ha="center", fontsize=8)
    ax.add_patch(Rectangle((9.7, 1.4), 0.8, 1.7, fc=NCOL, ec=INK)); ax.text(10.1, 2.2, "fin\n(channel)", ha="center", va="center", fontsize=7.5)
    ax.add_patch(Polygon([(8.6, 1.4), (8.6, 3.6), (11.6, 3.6), (11.6, 1.4), (10.7, 1.4), (10.7, 3.25), (9.5, 3.25), (9.5, 1.4)], fc="#9ca3af", ec=INK))
    ax.text(10.1, 3.42, "gate", ha="center", va="center", fontsize=8, color="white")
    ax.text(10.1, 4.2, "FinFET (looking along the fin)\ngate wraps the fin on 3 sides", ha="center", fontsize=8.6, weight="bold")
    return _svg(fig)
