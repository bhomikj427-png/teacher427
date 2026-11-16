"""Figures for 03a-pn-junction-equilibrium and 03b-diode-iv-capacitance (all generated with matplotlib).

Curves come from the same equations verify_u3.py checks: the depletion-approximation solution for
N_A = 1e17, N_D = 1e16 (the running example), I = I_s(e^(V/ηV_T) − 1) with I_s = 1 pA, C_T = εA/W, etc.
"""
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "study-pack" / "pdf"))
from figs import (_fig, _canvas, _svg, _box, _arrow, INK, MUTED, LINE, SOFT, ACC, G1, G2, G3, BAD, NCOL, PCOL)  # noqa: E402
from matplotlib.patches import Rectangle, Circle, Polygon  # noqa: E402

VT = 0.0259
q, eps = 1.6e-19, 1.04e-12
NA, ND, ni = 1e17, 1e16, 1e10
VBI = VT * math.log(NA * ND / ni**2)


def _W(V):
    return math.sqrt(2 * eps / q * (1 / NA + 1 / ND) * V)


W0 = _W(VBI)
XN, XP = W0 * NA / (NA + ND), W0 * ND / (NA + ND)


def _profile(x_cm, Vj=VBI):
    """Depletion-approximation ρ/q, E, ψ for junction voltage Vj (x in cm, junction at 0)."""
    W = _W(Vj); xn, xp = W * NA / (NA + ND), W * ND / (NA + ND)
    rho = np.where((x_cm > -xp) & (x_cm < 0), -NA, np.where((x_cm >= 0) & (x_cm < xn), ND, 0.0))
    E = np.where((x_cm > -xp) & (x_cm < 0), -q * NA * (x_cm + xp) / eps,
                 np.where((x_cm >= 0) & (x_cm < xn), -q * ND * (xn - x_cm) / eps, 0.0))
    psi = np.where(x_cm <= -xp, 0.0,
                   np.where(x_cm < 0, q * NA * (x_cm + xp) ** 2 / (2 * eps),
                            np.where(x_cm < xn, Vj - q * ND * (xn - x_cm) ** 2 / (2 * eps), Vj)))
    return rho, E, psi, xn, xp


def _off(ax):
    ax.axis("off")


# ================================================================== 03a
def diode_symbol():
    fig, ax = _canvas(7.2, 2.0, (0, 14.4), (0, 4.0))
    ax.add_patch(Rectangle((0.6, 1.2), 0.25, 1.6, fc=MUTED, ec=INK))
    ax.add_patch(Rectangle((0.85, 1.2), 2.2, 1.6, fc=PCOL, ec=INK))
    ax.add_patch(Rectangle((3.05, 1.2), 2.2, 1.6, fc=NCOL, ec=INK))
    ax.add_patch(Rectangle((5.25, 1.2), 0.25, 1.6, fc=MUTED, ec=INK))
    ax.plot([0, 0.6], [2, 2], color=INK); ax.plot([5.5, 6.1], [2, 2], color=INK)
    ax.text(1.95, 2.0, "p", ha="center", va="center", fontsize=13, color=BAD, weight="bold")
    ax.text(4.15, 2.0, "n", ha="center", va="center", fontsize=13, color=ACC, weight="bold")
    ax.text(3.05, 3.35, "one piece of silicon, two dopings", ha="center", fontsize=8.5)
    ax.text(0.72, 0.65, "metal\ncontact", ha="center", fontsize=7.2, color=MUTED)
    ax.text(5.38, 0.65, "metal\ncontact", ha="center", fontsize=7.2, color=MUTED)
    ax.text(3.05, 0.65, "junction", ha="center", fontsize=7.6, color=G1); ax.plot([3.05, 3.05], [1.0, 1.2], color=G1)
    ax.annotate("", (7.4, 2), (6.5, 2), arrowprops=dict(arrowstyle="->", lw=1.5, color=INK))
    # symbol
    y = 2.0
    ax.plot([8.0, 10.2], [y, y], color=INK, lw=1.5); ax.plot([11.2, 13.4], [y, y], color=INK, lw=1.5)
    ax.add_patch(Polygon([(10.2, y + 0.6), (10.2, y - 0.6), (11.2, y)], closed=True, fc=INK, ec=INK))
    ax.plot([11.2, 11.2], [y - 0.6, y + 0.6], color=INK, lw=2)
    ax.text(8.6, 2.45, "anode (p)", fontsize=8.5, ha="center"); ax.text(12.8, 2.45, "cathode (n)", fontsize=8.5, ha="center")
    ax.annotate("", (12.4, 1.05), (9.0, 1.05), arrowprops=dict(arrowstyle="->", lw=1.6, color=G2))
    ax.text(10.7, 0.45, "current flows easily this way (the arrow of the symbol)", ha="center", fontsize=7.8, color=G2)
    return _svg(fig)


def fab_steps():
    fig, axs = _fig(7.6, 3.6, nrows=2, ncols=3, gridspec_kw=dict(hspace=0.45, wspace=0.12))
    titles = ["① n⁺ wafer + thin n layer", "② grow oxide (SiO₂)", "③ resist + mask + UV light",
              "④ etch a window in the oxide", "⑤ diffuse boron through it", "⑥ add metal contacts"]
    for k, (ax, t) in enumerate(zip(axs.flat, titles)):
        ax.set_xlim(0, 10); ax.set_ylim(0, 7); _off(ax)
        ax.add_patch(Rectangle((0, 0), 10, 2.2, fc="#c7d7f5", ec=INK, lw=0.7)); ax.text(9.7, 0.3, "n⁺", ha="right", fontsize=7)
        ax.add_patch(Rectangle((0, 2.2), 10, 2.3, fc=NCOL, ec=INK, lw=0.7)); ax.text(9.7, 2.5, "n", ha="right", fontsize=7)
        ax.set_title(t, fontsize=8)
        if k >= 1:
            gap = k >= 3
            for x0, w in (((0, 3.6), (6.4, 3.6)) if gap else ((0, 10),)):
                ax.add_patch(Rectangle((x0, 4.5), w, 0.45, fc="#e9f7fb", ec=INK, lw=0.6))
        if k == 2:
            ax.add_patch(Rectangle((0, 4.95), 10, 0.35, fc="#f6c98b", ec=INK, lw=0.5))
            for x0 in (0, 6.4):
                ax.add_patch(Rectangle((x0, 5.6), 3.6, 0.35, fc=MUTED, ec=INK, lw=0.5))
            for x in np.linspace(0.6, 9.4, 8):
                ax.annotate("", (x, 5.95), (x, 6.9), arrowprops=dict(arrowstyle="->", color=G3, lw=0.8))
        if k == 4:
            for x in np.linspace(0.8, 9.2, 7):
                ax.annotate("", (x, 5.1), (x, 6.7), arrowprops=dict(arrowstyle="->", color=G2, lw=1.2))
        if k >= 4:
            ax.add_patch(Polygon([(3.4, 4.5), (6.6, 4.5), (6.2, 3.3), (3.8, 3.3)], fc=PCOL, ec=INK, lw=0.8))
            ax.text(5, 3.8, "p", ha="center", fontsize=8, color=BAD, weight="bold")
        if k == 5:
            ax.add_patch(Rectangle((3.2, 4.5), 3.6, 0.6, fc=MUTED, ec=INK, lw=0.6))
            ax.add_patch(Rectangle((0, -0.5), 10, 0.5, fc=MUTED, ec=INK, lw=0.6))
            ax.set_ylim(-0.6, 7)
    return _svg(fig)


def abrupt_profile():
    fig, axs = _fig(7.2, 2.7, ncols=2, gridspec_kw=dict(wspace=0.35))
    x = np.linspace(-1, 1, 400)
    na_real = 10 ** (17 - 3.5 / (1 + np.exp(-(x + 0.05) / 0.06)))
    for ax in axs:
        ax.set_yscale("log"); ax.set_ylim(1e13, 1e18); ax.set_xlabel("position x (µm from the junction)")
        ax.axvline(0, color=G1, lw=0.8, ls="--")
    axs[0].semilogy(x, na_real, color=BAD, lw=1.7, label="N_A (acceptors)")
    axs[0].semilogy(x, np.full_like(x, ND), color=ACC, lw=1.7, label="N_D (donors)")
    axs[0].set_title("real: boron fades out with depth", fontsize=8.5)
    axs[0].set_ylabel("dopant atoms per cm³ (log)")
    axs[1].semilogy(x[x < 0], np.full((x < 0).sum(), NA), color=BAD, lw=1.9)
    axs[1].semilogy(x[x >= 0], np.full((x >= 0).sum(), ND), color=ACC, lw=1.9)
    axs[1].text(-0.95, 1.4e17, "p side: N_A = 10¹⁷", fontsize=8, color=BAD)
    axs[1].text(0.05, 1.4e16, "n side: N_D = 10¹⁶", fontsize=8, color=ACC)
    axs[1].text(0.03, 2e13, "x = 0: junction", fontsize=7.5, color=G1)
    axs[1].set_title("model: an abrupt step (this file)", fontsize=8.5)
    axs[0].legend(frameon=False, fontsize=7.5, loc="lower left")
    return _svg(fig)


def carrier_profile():
    fig, ax = _fig(5.8, 3.0)
    x = np.linspace(-0.25e-4, 0.55e-4, 600)
    _, _, psi, xn, xp = _profile(x)
    p = NA * np.exp(-psi / VT); n = ni**2 / NA * np.exp(psi / VT)
    xu = x * 1e4
    ax.semilogy(xu, p, color=BAD, lw=1.9, label="holes p(x)")
    ax.semilogy(xu, n, color=ACC, lw=1.9, label="electrons n(x)")
    ax.semilogy(xu, np.where(xu < 0, NA, ni**2 / ND), color=BAD, lw=0.9, ls=":")
    ax.semilogy(xu, np.where(xu < 0, ni**2 / NA, ND), color=ACC, lw=0.9, ls=":")
    ax.axvspan(-xp * 1e4, xn * 1e4, color=G1, alpha=0.08)
    ax.text(xn * 1e4 / 2 - 0.02, 3e17, "depletion region", fontsize=7.6, color=G1, ha="center")
    ax.text(-0.24, 1.6e17, "10¹⁷ holes", fontsize=7.5, color=BAD); ax.text(-0.24, 1.6e3, "10³ electrons", fontsize=7.5, color=ACC)
    ax.text(0.38, 1.6e16, "10¹⁶ electrons", fontsize=7.5, color=ACC); ax.text(0.38, 1.6e4, "10⁴ holes", fontsize=7.5, color=BAD)
    ax.set_ylim(1e2, 1e18); ax.set_xlabel("position x (µm); p side left, n side right")
    ax.set_ylabel("carriers per cm³ (log)")
    ax.text(0.33, 3e7, "dotted: the step each side\nwould have if the carriers\ncould not cross", fontsize=7, color=MUTED)
    ax.legend(frameon=False, fontsize=7.5, loc="center left")
    return _svg(fig)


def _ions_panel(ax, title, deplete):
    ax.set_xlim(0, 10); ax.set_ylim(-1.1, 4.9); ax.set_aspect("equal"); _off(ax)
    ax.add_patch(Rectangle((0, 0), 5, 3.4, fc=PCOL, ec=INK, lw=0.9)); ax.add_patch(Rectangle((5, 0), 5, 3.4, fc=NCOL, ec=INK, lw=0.9))
    dl, dr = (4.3, 6.4) if deplete else (5, 5)
    if deplete:
        ax.add_patch(Rectangle((dl, 0), dr - dl, 3.4, fc="white", ec=G1, lw=1.1, ls="--"))
    rng = np.random.default_rng(3)
    for i in range(4):
        for j in range(3):
            x, y = 0.6 + i * 1.1, 0.6 + j * 1.05
            ax.add_patch(Circle((x, y), 0.28, fc="white", ec=BAD, lw=0.8)); ax.text(x, y, "−", ha="center", va="center", fontsize=8, color=BAD)
            if x < dl - 0.2:
                ax.add_patch(Circle((x + 0.42 + rng.uniform(-0.05, 0.05), y + 0.33), 0.13, fc="white", ec=INK, lw=0.8))
    for i in range(4):
        for j in range(3):
            x, y = 5.6 + i * 1.1, 0.6 + j * 1.05
            ax.add_patch(Circle((x, y), 0.28, fc="white", ec=ACC, lw=0.8)); ax.text(x, y, "+", ha="center", va="center", fontsize=8, color=ACC)
            if x > dr + 0.2:
                ax.add_patch(Circle((x + 0.42, y + 0.33), 0.13, fc=INK, ec=INK))
    ax.text(5, 4.55, title, ha="center", fontsize=8.3, weight="bold")
    if not deplete:
        _arrow(ax, (3.6, 3.65), (6.4, 3.65), color=INK, lw=1.0); ax.text(5, 3.8, "holes cross →", ha="center", fontsize=6.8)
        _arrow(ax, (6.4, -0.3), (3.6, -0.3), color=INK, lw=1.0); ax.text(5, -0.85, "← electrons cross", ha="center", fontsize=6.8)
    else:
        ax.text((dl + dr) / 2, -0.5, "depletion region", ha="center", fontsize=7.2, color=G1)


def depletion_ions():
    fig, axs = _fig(7.4, 2.5, ncols=2, gridspec_kw=dict(wspace=0.06))
    _ions_panel(axs[0], "① at contact: carriers cross", False)
    _ions_panel(axs[1], "② a strip of bare ions is left", True)
    fig.text(0.5, -0.03, "⊖ acceptor ion (fixed)   ⊕ donor ion (fixed)   ○ hole (mobile)   ● electron (mobile)", ha="center", fontsize=7.6, color=MUTED)
    return _svg(fig)


def balance_arrows():
    fig, ax = _canvas(6.6, 2.8, (0, 13.2), (0, 5.6))
    ax.add_patch(Rectangle((0.3, 0.3), 4.2, 4.6, fc=PCOL, ec=INK, lw=0.8)); ax.add_patch(Rectangle((8.7, 0.3), 4.2, 4.6, fc=NCOL, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((4.5, 0.3), 4.2, 4.6, fc="white", ec=G1, lw=1.0, ls="--"))
    ax.text(2.4, 4.4, "p side", ha="center", fontsize=8.5, color=BAD); ax.text(10.8, 4.4, "n side", ha="center", fontsize=8.5, color=ACC)
    ax.text(6.6, 5.15, "field E points n → p", ha="center", fontsize=8.3, color=G3)
    _arrow(ax, (8.3, 4.65), (4.9, 4.65), color=G3, lw=2)
    rows = [("hole diffusion (crowd on the left)", (4.9, 3.6), (8.3, 3.6), BAD, "-"),
            ("hole drift (pushed along E)", (8.3, 2.8), (4.9, 2.8), BAD, "--"),
            ("electron diffusion (crowd on the right)", (8.3, 1.9), (4.9, 1.9), ACC, "-"),
            ("electron drift (pushed against E)", (4.9, 1.1), (8.3, 1.1), ACC, "--")]
    for lab, a, b, c, ls in rows:
        _arrow(ax, a, b, color=c, lw=1.6, ls=ls)
        ax.text(6.6, a[1] + 0.18, lab, ha="center", fontsize=6.9, color=c)
    ax.text(6.6, 0.45, "each pair cancels: no net current", ha="center", fontsize=7.6, weight="bold")
    return _svg(fig)


def band_bending():
    fig, ax = _fig(5.8, 3.0)
    x = np.linspace(-0.25e-4, 0.55e-4, 500)
    _, _, psi, xn, xp = _profile(x)
    Ev_p = -0.120
    Ec = Ev_p + 1.12 - psi; Ev = Ev_p - psi
    xu = x * 1e4
    ax.plot(xu, Ec, color=INK, lw=1.8); ax.plot(xu, Ev, color=INK, lw=1.8); ax.axhline(0, color=BAD, lw=1.2, ls="--")
    ax.text(-0.24, Ec[0] + 0.04, "E_C", fontsize=8.5); ax.text(-0.24, Ev[0] - 0.12, "E_V", fontsize=8.5)
    ax.text(0.3, 0.04, "E_F: one flat line", fontsize=8.5, color=BAD)
    ax.axvspan(-xp * 1e4, xn * 1e4, color=G1, alpha=0.08)
    ax.annotate("", (0.47, Ec[-1]), (0.47, Ec[0]), arrowprops=dict(arrowstyle="<->", color=G3, lw=1.2))
    ax.text(0.485, (Ec[0] + Ec[-1]) / 2, "qV_bi\n= 0.775 eV", fontsize=8, color=G3, va="center")
    ax.text(-0.24, -0.55, "p side: E_F near E_V", fontsize=7.6, color=MUTED); ax.text(0.3, -0.62, "n side: E_F near E_C", fontsize=7.6, color=MUTED)
    ax.set_xlabel("position x (µm)"); ax.set_ylabel("electron energy (eV), E_F = 0"); ax.set_xlim(-0.25, 0.62)
    return _svg(fig)


def vbi_ladder():
    fig, axs = _fig(5.6, 3.6, nrows=2, sharex=True, gridspec_kw=dict(hspace=0.15, height_ratios=[1.3, 1]))
    x = np.linspace(-0.25e-4, 0.55e-4, 500)
    _, _, psi, xn, xp = _profile(x)
    xu = x * 1e4
    axs[0].semilogy(xu, NA * np.exp(-psi / VT), color=BAD, lw=1.9)
    axs[0].set_ylabel("holes per cm³ (log)"); axs[0].set_ylim(1e3, 1e18)
    axs[0].text(-0.24, 2e17, "p_p = N_A = 10¹⁷", fontsize=8, color=BAD); axs[0].text(0.31, 3e4, "p_n = n_i²/N_D = 10⁴", fontsize=8, color=BAD)
    axs[0].annotate("", (0.15, 1e4), (0.15, 1e17), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
    axs[0].text(0.17, 3e10, "ratio 10¹³ = e^(V_bi/V_T)", fontsize=8)
    axs[1].plot(xu, psi, color=G2, lw=1.9); axs[1].set_ylabel("potential ψ (V)")
    axs[1].text(0.3, 0.6, "V_bi = 0.775 V", fontsize=8.5, color=G2)
    axs[1].set_xlabel("position x (µm)")
    for a in axs:
        a.axvspan(-xp * 1e4, xn * 1e4, color=G1, alpha=0.08)
    return _svg(fig)


def rho_plot():
    fig, ax = _fig(5.8, 2.6)
    x = np.linspace(-0.12e-4, 0.42e-4, 1200)
    rho, _, _, xn, xp = _profile(x)
    xu = x * 1e4
    ax.plot(xu, rho / 1e16, color=G3, lw=1.8); ax.axhline(0, color=MUTED, lw=0.7)
    ax.fill_between(xu, rho / 1e16, 0, where=rho < 0, color=BAD, alpha=0.18)
    ax.fill_between(xu, rho / 1e16, 0, where=rho > 0, color=ACC, alpha=0.18)
    ax.text(-0.075, -10.5, "−qN_A\n(10¹⁷)", ha="center", fontsize=7.6, color=BAD)
    ax.text(xn * 1e4 / 2, 1.6, "+qN_D (10¹⁶)", ha="center", fontsize=7.6, color=ACC)
    ax.text(xn * 1e4 / 2, -4, "shaded areas are equal:\nN_A·x_p = N_D·x_n", ha="center", fontsize=7.8)
    ax.set_xticks([-xp * 1e4, xn * 1e4]); ax.set_xticklabels(["−x_p = −0.030", "x_n = 0.303"])
    ax.set_ylim(-13, 4); ax.set_ylabel("charge density ρ/q\n(10¹⁶ per cm³)"); ax.set_xlabel("position x (µm)")
    return _svg(fig)


def field_plot():
    fig, ax = _fig(5.8, 2.6)
    x = np.linspace(-0.12e-4, 0.42e-4, 1200)
    _, E, _, xn, xp = _profile(x)
    xu = x * 1e4
    ax.plot(xu, E / 1e3, color=BAD, lw=1.9); ax.axhline(0, color=MUTED, lw=0.7)
    ax.fill_between(xu, E / 1e3, 0, color=BAD, alpha=0.1)
    ax.plot([0], [E.min() / 1e3], "o", color=INK, ms=4)
    ax.text(0.015, E.min() / 1e3 - 3, "E_max = −46.6 kV/cm at x = 0", fontsize=7.8)
    ax.text(-0.115, -14, "steep: slope\n−qN_A/ε", fontsize=7.3, color=MUTED)
    ax.text(0.2, -25, "gentle: slope +qN_D/ε", fontsize=7.3, color=MUTED)
    ax.text(0.2, -40, "negative E = points to −x,\ni.e. from n to p", fontsize=7.3, color=G3)
    ax.set_xticks([-xp * 1e4, xn * 1e4]); ax.set_xticklabels(["−x_p", "x_n"])
    ax.set_ylim(-55, 6); ax.set_ylabel("field E (kV/cm)"); ax.set_xlabel("position x (µm)")
    return _svg(fig)


def potential_plot():
    fig, ax = _fig(5.8, 2.6)
    x = np.linspace(-0.12e-4, 0.42e-4, 1200)
    _, _, psi, xn, xp = _profile(x)
    xu = x * 1e4
    ax.plot(xu, psi, color=G2, lw=1.9)
    ax.annotate("", (0.39, VBI), (0.39, 0), arrowprops=dict(arrowstyle="<->", color=G2))
    ax.text(0.395, VBI / 2, "V_bi\n0.775 V", fontsize=8, color=G2, va="center")
    ax.annotate("", (xn * 1e4, -0.12), (-xp * 1e4, -0.12), arrowprops=dict(arrowstyle="<->", color=G1))
    ax.text(xn * 1e4 / 2, -0.25, "W = x_p + x_n = 0.333 µm", ha="center", fontsize=7.8, color=G1)
    ax.text(-0.115, 0.3, "most of the drop is\non the n side (91 %)", fontsize=7.3, color=MUTED)
    ax.set_xticks([-xp * 1e4, xn * 1e4]); ax.set_xticklabels(["−x_p", "x_n"])
    ax.set_ylim(-0.33, 0.9); ax.set_ylabel("potential ψ (V)"); ax.set_xlabel("position x (µm)")
    return _svg(fig)


def bias_W():
    fig, axs = _fig(7.2, 2.9, nrows=3, gridspec_kw=dict(hspace=0.55))
    for ax, (Va, lab) in zip(axs, ((0.6, "forward 0.6 V: barrier 0.25 V"), (0.0, "no bias: barrier 0.85 V"), (-2.0, "reverse 2 V: barrier 2.85 V"))):
        r = math.sqrt((0.85 - Va) / 0.85)
        ax.set_xlim(-3, 3); ax.set_ylim(0, 1); _off(ax)
        ax.add_patch(Rectangle((-3, 0), 3, 1, fc=PCOL, ec=INK, lw=0.7)); ax.add_patch(Rectangle((0, 0), 3, 1, fc=NCOL, ec=INK, lw=0.7))
        w = 1.1 * r
        ax.add_patch(Rectangle((-0.15 * w, 0), w, 1, fc="white", ec=G1, lw=1.2, ls="--"))
        ax.text(-2.9, 0.35, lab, fontsize=7.8)
        ax.text(2.9, 0.35, f"W = {r:.2f} × W₀", fontsize=7.8, ha="right", color=G1)
    return _svg(fig)


def voltage_drops():
    fig, ax = _canvas(7.4, 1.9, (0, 14.8), (0, 3.8))
    segs = [(0.3, 0.6, MUTED, "metal"), (0.9, 1.2, "#f3b9b9", "p⁺\ncontact"), (2.1, 3.4, PCOL, "p neutral"), (5.5, 2.4, "white", "depletion\nV_j"),
            (7.9, 3.4, NCOL, "n neutral"), (11.3, 1.2, "#b9cdf3", "n⁺\ncontact"), (12.5, 0.6, MUTED, "metal")]
    for x0, w, c, t in segs:
        ax.add_patch(Rectangle((x0, 1.2), w, 1.4, fc=c, ec=INK, lw=0.7, ls="--" if c == "white" else "-"))
        if w > 0.7:
            ax.text(x0 + w / 2, 1.9, t, ha="center", va="center", fontsize=7.2)
    ax.text(3.8, 0.7, "≈ 0 V (good conductors)", ha="center", fontsize=7.2, color=MUTED)
    ax.text(9.6, 0.7, "≈ 0 V", ha="center", fontsize=7.2, color=MUTED)
    ax.text(6.7, 3.2, "almost all of V_a lands here: V_j = V_bi − V_a", ha="center", fontsize=8.2, color=G1, weight="bold")
    ax.text(0.2, 0.5, "+", fontsize=11, color=BAD); ax.text(13.3, 0.5, "−", fontsize=11, color=ACC)
    ax.text(6.7, 0.15, "forward bias: + on p, − on n", ha="center", fontsize=7.2)
    return _svg(fig)


# ================================================================== 03b
IS = 1e-12


def _I(v, n=1, Is=IS):
    return Is * (np.exp(v / (n * VT)) - 1)


def iv_lin_log():
    fig, axs = _fig(7.4, 2.9, ncols=2, gridspec_kw=dict(wspace=0.38))
    v = np.linspace(-5, 0.75, 2000)
    i = _I(v) * 1e3
    axs[0].plot(v, np.where(i > 12, np.nan, i), color=ACC, lw=1.8)
    axs[0].axhline(0, color=MUTED, lw=0.6); axs[0].axvline(0, color=MUTED, lw=0.6)
    axs[0].set_xlabel("voltage across diode V_D (V)"); axs[0].set_ylabel("current I_D (mA)"); axs[0].set_ylim(-1, 12)
    axs[0].set_title("① linear scale (deck slide 75)", fontsize=8.5)
    axs[0].text(-4.8, 1.0, "reverse: looks like zero", fontsize=7.5); axs[0].text(-1.6, 9, "forward:\nsteep above\n≈ 0.6 V", fontsize=7.5)
    v2 = np.linspace(-0.3, 0.75, 600)
    axs[1].semilogy(v2, np.abs(_I(v2)), color=ACC, lw=1.8)
    axs[1].set_xlabel("V_D (V)"); axs[1].set_ylabel("|I_D| (A), log scale"); axs[1].set_ylim(1e-13, 1e-1)
    axs[1].axhline(1e-12, color=BAD, lw=0.8, ls=":"); axs[1].text(-0.28, 2e-12, "|I| → I_s = 1 pA", fontsize=7.5, color=BAD)
    axs[1].set_title("② log scale: the same curve", fontsize=8.5)
    axs[1].text(0.05, 1e-4, "straight line:\nexponential", fontsize=7.5)
    return _svg(fig)


def barrier_bias():
    fig, axs = _fig(7.4, 2.6, ncols=3, gridspec_kw=dict(wspace=0.15))
    x = np.linspace(-1, 1, 300)
    for ax, (Va, t) in zip(axs, ((-0.5, "reverse: V_a = −0.5 V"), (0.0, "no bias"), (0.5, "forward: V_a = +0.5 V"))):
        h = 0.775 - Va
        ec = h / 2 * (1 - np.tanh(x / 0.18))
        ax.plot(x, ec, color=INK, lw=1.7); ax.set_ylim(-0.3, 1.45); ax.set_xlim(-1, 1); _off(ax)
        e = np.linspace(0, 1.4, 200)
        ax.fill_betweenx(e, 1, 1 - 0.55 * np.exp(-e / 0.12), color=ACC, alpha=0.3)
        ax.plot([0.25, 1], [h, h], color=BAD, lw=0.8, ls=":")
        ax.annotate("", (-0.85, h), (-0.85, 0), arrowprops=dict(arrowstyle="<->", color=G3))
        ax.text(-0.8, h / 2, f"q(V_bi − V_a)\n= {h:.3f} eV", fontsize=7, color=G3, va="center")
        ax.set_title(t, fontsize=8.2)
        m, e = f"{math.exp(-h / VT):.1e}".split("e")
        ax.text(0.0, -0.22, f"share able to cross: {m} × 10$^{{{int(e)}}}$", fontsize=7, ha="center", color=ACC)
    return _svg(fig)


def eqn_points():
    fig, ax = _fig(5.4, 2.8)
    v = np.linspace(0, 0.68, 500)
    ax.plot(v, _I(v) * 1e3, color=ACC, lw=1.8, label="η = 1")
    ax.plot(v, _I(v, 2) * 1e3, color=G1, lw=1.5, ls="--", label="η = 2 (same I_s)")
    for vv in (0.5, 0.6, 0.66):
        ax.plot([vv], [_I(vv) * 1e3], "o", color=INK, ms=4)
    ax.annotate("0.6 V → 11.5 mA", (0.6, 11.5), (0.33, 30), fontsize=7.8, arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.annotate("0.66 V → 116 mA\n(off the top)", (0.66, 120), (0.42, 85), fontsize=7.8, arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.annotate("0.5 V → 0.24 mA", (0.5, 0.24), (0.15, 12), fontsize=7.8, arrowprops=dict(arrowstyle="-", lw=0.7))
    ax.set_ylim(-2, 120); ax.set_xlabel("V_D (V)"); ax.set_ylabel("I_D (mA)")
    ax.legend(frameon=False, fontsize=7.8, loc="upper left")
    return _svg(fig)


def decades():
    fig, axs = _fig(7.4, 2.8, ncols=2, gridspec_kw=dict(wspace=0.38))
    v = np.linspace(0.3, 0.72, 400)
    axs[0].semilogy(v, _I(v), color=ACC, lw=1.8)
    for k in range(3):
        v0 = 0.537 + k * 0.0596
        axs[0].plot([v0], [IS * math.exp(v0 / VT)], "o", color=INK, ms=3.5)
    axs[0].text(0.54, 2e-5, "1 mA → 10 mA → 100 mA:\none decade per 59.6 mV", fontsize=7.4)
    axs[0].set_xlabel("V_D (V)"); axs[0].set_ylabel("I_D (A), log"); axs[0].set_title("forward, log scale", fontsize=8.5)
    v2 = np.linspace(-0.3, 0.06, 400)
    axs[1].plot(v2, _I(v2) / IS, color=ACC, lw=1.8); axs[1].axhline(-1, color=BAD, ls=":", lw=0.9)
    axs[1].axhline(0, color=MUTED, lw=0.6); axs[1].axvline(0, color=MUTED, lw=0.6)
    axs[1].text(-0.29, -0.85, "flat at −I_s", fontsize=7.6, color=BAD)
    axs[1].set_ylim(-1.3, 2); axs[1].set_xlabel("V_D (V)"); axs[1].set_ylabel("I_D / I_s")
    axs[1].set_title("near zero and reverse", fontsize=8.5)
    return _svg(fig)


def is_origin():
    fig, ax = _canvas(6.6, 2.5, (0, 13.2), (0, 5.0))
    ax.add_patch(Rectangle((0.3, 0.6), 4.4, 3.4, fc=PCOL, ec=INK, lw=0.8)); ax.add_patch(Rectangle((8.5, 0.6), 4.4, 3.4, fc=NCOL, ec=INK, lw=0.8))
    ax.add_patch(Rectangle((4.7, 0.6), 3.8, 3.4, fc="white", ec=G1, lw=1.0, ls="--"))
    ax.text(2.5, 4.3, "p side: a few electrons\n(minority, from heat)", ha="center", fontsize=7.4)
    ax.text(10.7, 4.3, "n side: a few holes\n(minority, from heat)", ha="center", fontsize=7.4)
    for x, y in ((3.3, 2.6), (4.2, 1.5)):
        ax.add_patch(Circle((x, y), 0.17, fc=INK))
    _arrow(ax, (4.4, 2.6), (8.1, 2.6), color=ACC, lw=1.6); ax.text(6.6, 2.8, "electron swept to n", ha="center", fontsize=7, color=ACC)
    for x, y in ((9.0, 1.5), (9.8, 2.6)):
        ax.add_patch(Circle((x, y), 0.17, fc="white", ec=INK))
    _arrow(ax, (8.7, 1.5), (4.9, 1.5), color=BAD, lw=1.6); ax.text(6.6, 1.15, "hole swept to p", ha="center", fontsize=7, color=BAD)
    ax.text(6.6, 0.15, "the field takes every minority carrier that reaches the edge: I_s is set by how many heat makes, not by V", ha="center", fontsize=7.2)
    return _svg(fig)


def temp_iv():
    fig, ax = _fig(5.4, 2.8)
    v = np.linspace(0.3, 0.8, 400)
    i25 = IS * 1e3 * np.exp((v - 0.0) / VT)
    i75 = IS * 1e3 * np.exp((v + 0.1) / VT)
    ax.plot(v, np.where(i25 > 25, np.nan, i25), color=ACC, lw=1.8, label="25 °C")
    ax.plot(v, np.where(i75 > 25, np.nan, i75), color=BAD, lw=1.8, label="75 °C")
    vv = VT * math.log(10e-3 / IS)
    ax.annotate("", (vv - 0.1, 10), (vv, 10), arrowprops=dict(arrowstyle="->", color=INK))
    ax.text(0.31, 15, "same 10 mA at 0.1 V less\n(−2 mV/°C × 50 °C)", fontsize=7.5)
    ax.set_xlabel("V_D (V)"); ax.set_ylabel("I_D (mA)"); ax.set_ylim(0, 25)
    ax.legend(frameon=False, fontsize=7.8, loc="upper left")
    return _svg(fig)


def static_dynamic():
    fig, ax = _fig(5.4, 3.0)
    v = np.linspace(0, 0.64, 400)
    ax.plot(v, _I(v) * 1e3, color=INK, lw=1.8)
    vq, iq = 0.6, _I(0.6) * 1e3
    ax.plot([vq], [iq], "o", color=INK, ms=5); ax.text(vq + 0.005, iq - 2.0, "Q (0.6 V, 11.5 mA)", fontsize=7.8)
    ax.plot([0, vq], [0, iq], color=G1, lw=1.4, ls="--")
    ax.text(0.08, 9, "chord from the origin:\nR_D = V/I = 52 Ω", fontsize=7.6, color=G1)
    rd = VT / (iq / 1e3)
    vt = np.linspace(0.565, 0.635, 10)
    ax.plot(vt, iq + (vt - vq) / rd * 1e3, color=BAD, lw=1.6)
    ax.text(0.3, 22, "tangent at Q:\nr_d = 1/slope = 2.25 Ω", fontsize=7.6, color=BAD)
    ax.set_xlim(0, 0.66); ax.set_ylim(-1, 30); ax.set_xlabel("V_D (V)"); ax.set_ylabel("I_D (mA)")
    return _svg(fig)


def _diode(ax, x, y, s=0.5, color=INK):
    ax.add_patch(Polygon([(x - s, y + s * 0.8), (x - s, y - s * 0.8), (x + s * 0.6, y)], closed=True, fc=color, ec=color))
    ax.plot([x + s * 0.6] * 2, [y - s * 0.8, y + s * 0.8], color=color, lw=2)


def model_circuit():
    fig, axs = _fig(7.6, 2.5, ncols=4, gridspec_kw=dict(wspace=0.1))
    for ax in axs:
        ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.set_aspect("equal"); _off(ax)
    a = axs[0]
    a.plot([1, 1, 9, 9, 1], [1, 6, 6, 1, 1], color=INK, lw=1.2)
    a.add_patch(Rectangle((0.6, 2.8), 0.8, 1.4, fc="white", ec=INK)); a.text(0.0, 3.4, "5 V", fontsize=8, ha="right")
    a.add_patch(Rectangle((3.6, 5.6), 2.4, 0.8, fc="white", ec=INK)); a.text(4.8, 6.6, "1 kΩ", fontsize=8, ha="center")
    a.add_patch(Rectangle((8.4, 2.6), 1.2, 1.8, fc="white", ec="white")); _diode(a, 9, 3.5, 0.6)
    a.text(5, 0.1, "the circuit", ha="center", fontsize=8.2, weight="bold")
    specs = (("① ideal", "short wire", None, None), ("② simplified", "0.7 V battery", "0.7 V", None), ("③ piecewise-linear", "0.7 V + r_av", "0.7 V", "r_av"))
    for ax, (t, s, bat, r) in zip(axs[1:], specs):
        ax.plot([5, 5], [6.5, 0.5], color=INK, lw=1.2)
        if bat:
            ax.add_patch(Rectangle((4.4, 3.9), 1.2, 0.2, fc="white", ec="white"))
            ax.plot([4.2, 5.8], [4.1, 4.1], color=INK, lw=1.6); ax.plot([4.6, 5.4], [3.8, 3.8], color=INK, lw=2.6)
            ax.text(6.0, 3.8, bat, fontsize=7.6)
        if r:
            ax.add_patch(Rectangle((4.6, 1.3), 0.8, 1.6, fc="white", ec=INK)); ax.text(5.6, 1.9, r, fontsize=7.6)
        ax.text(5, 0.0, t, ha="center", fontsize=8.2, weight="bold"); ax.text(5, 6.7, s, ha="center", fontsize=7.4, color=MUTED)
    return _svg(fig)


def ct_plot():
    fig, axs = _fig(7.4, 2.8, ncols=2, gridspec_kw=dict(wspace=0.32, width_ratios=[1, 1.35]))
    a = axs[0]; a.set_xlim(0, 10); a.set_ylim(0, 7); a.set_aspect("equal"); _off(a)
    a.add_patch(Rectangle((0.3, 1), 3.2, 4.6, fc=PCOL, ec=INK, lw=0.8)); a.add_patch(Rectangle((6.5, 1), 3.2, 4.6, fc=NCOL, ec=INK, lw=0.8))
    a.add_patch(Rectangle((3.5, 1), 3.0, 4.6, fc="white", ec=G1, ls="--"))
    for y in np.linspace(1.5, 5.1, 5):
        a.text(3.85, y, "−", fontsize=9, color=BAD, ha="center", va="center"); a.text(6.15, y, "+", fontsize=9, color=ACC, ha="center", va="center")
    a.text(1.9, 3.3, "plate", ha="center", fontsize=7.5); a.text(8.1, 3.3, "plate", ha="center", fontsize=7.5)
    a.text(5.0, 6.1, "gap = W\n(insulator)", ha="center", fontsize=7.5, color=G1)
    a.text(5.0, 0.2, "① a parallel-plate capacitor", ha="center", fontsize=8.2, weight="bold")
    b = axs[1]
    VR = np.linspace(0, 20, 300)
    C = np.array([eps * 1e-4 / _W(VBI + r) for r in VR]) * 1e12
    b.plot(VR, C, color=ACC, lw=1.9)
    for r in (0, 5, 20):
        c = eps * 1e-4 / _W(VBI + r) * 1e12
        b.plot([r], [c], "o", color=INK, ms=4); b.text(r + 0.4, c + 0.12, f"{c:.2f} pF", fontsize=7.5)
    b.set_xlabel("reverse voltage V_R (V)"); b.set_ylabel("C_T (pF)"); b.set_ylim(0, 3.6)
    b.set_title("the running junction, area 100 µm × 100 µm", fontsize=8.2)
    return _svg(fig)


def stored_charge():
    fig, ax = _fig(5.8, 2.8)
    L = 1.0
    xr = np.linspace(0.3, 4, 300); xl = np.linspace(-4, -0.3, 300)
    for amp, ls, lab in ((1.0, "-", "current I"), (2.0, "--", "current 2I")):
        ax.plot(xr, amp * np.exp(-(xr - 0.3) / L), color=BAD, lw=1.6, ls=ls)
        ax.plot(xl, 0.5 * amp * np.exp((xl + 0.3) / L), color=ACC, lw=1.6, ls=ls)
    ax.fill_between(xr, np.exp(-(xr - 0.3) / L), 0, color=BAD, alpha=0.15)
    ax.fill_between(xl, 0.5 * np.exp((xl + 0.3) / L), 0, color=ACC, alpha=0.15)
    ax.axvspan(-0.3, 0.3, color=G1, alpha=0.12)
    ax.text(1.5, 1.75, "extra holes injected into n,\ndying away over L_p (02b step 12)", fontsize=7.4, color=BAD)
    ax.text(-3.9, 1.1, "extra electrons\ninjected into p", fontsize=7.4, color=ACC)
    ax.text(-3.9, 1.75, "shaded area = stored charge Q", fontsize=7.4)
    ax.text(2.2, 1.0, "dashed: double the current\n→ double the stored charge", fontsize=7.2, color=MUTED)
    ax.set_xlabel("distance from the junction (diffusion lengths)"); ax.set_ylabel("extra minority carriers\n(relative)")
    ax.set_ylim(0, 2.2); ax.set_yticks([])
    return _svg(fig)


def recovery():
    fig, axs = _fig(6.4, 3.2, nrows=2, sharex=True, gridspec_kw=dict(hspace=0.25))
    t = np.linspace(-100, 400, 1000)
    ts, tt = 110, 30
    v = np.where(t < 0, 10, -5)
    i = np.where(t < 0, 10, np.where(t < ts, -5, -5 * np.exp(-(t - ts) / (tt / 2.3))))
    axs[0].plot(t, v, color=ACC, lw=1.7); axs[0].set_ylabel("source (V)"); axs[0].axhline(0, color=MUTED, lw=0.6)
    axs[0].text(-95, 7, "+10 V", fontsize=7.6); axs[0].text(200, -3.5, "−5 V", fontsize=7.6)
    axs[1].plot(t, i, color=BAD, lw=1.8); axs[1].axhline(0, color=MUTED, lw=0.6); axs[1].set_ylabel("diode current (mA)")
    axs[1].axvline(0, color=MUTED, lw=0.6, ls=":"); axs[1].axvline(ts, color=MUTED, lw=0.6, ls=":"); axs[1].axvline(ts + tt, color=MUTED, lw=0.6, ls=":")
    axs[1].annotate("", (ts, -7), (0, -7), arrowprops=dict(arrowstyle="<->")); axs[1].text(ts / 2, -9.5, "t_s = 110 ns", ha="center", fontsize=7.6)
    axs[1].annotate("", (ts + tt, -7), (ts, -7), arrowprops=dict(arrowstyle="<->")); axs[1].text(ts + tt + 5, -9.5, "t_t ≈ 30 ns", fontsize=7.6)
    axs[1].text(-95, 7, "I_F = +10 mA", fontsize=7.6); axs[1].text(190, -5.5, "I_R = −5 mA flows backwards\nuntil t_s", fontsize=7.4)
    axs[1].set_ylim(-11, 12); axs[1].set_xlabel("time t (ns); the source flips at t = 0")
    return _svg(fig)


FIGS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith("_") and k not in
        ("Path", "Rectangle", "Circle", "Polygon", "_fig", "_canvas", "_svg", "_box", "_arrow", "_W", "_profile", "_I")}
