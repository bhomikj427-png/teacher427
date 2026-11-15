"""Figures for 01a-silicon-bands-carriers and 01b-fermi-level (all generated with matplotlib).

Curves come from the same equations verify_u1.py checks. Where a tail would be too thin to see at the
real kT, the figure uses a wider kT and says so in its own label.
"""
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "study-pack" / "pdf"))
from figs import (_fig, _canvas, _svg, INK, MUTED, LINE, ACC, G1, G2, G3, BAD, NCOL, PCOL)  # noqa: E402
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch  # noqa: E402

k_eV = 8.617e-5


# ---------------------------------------------------------------- lattice pictures
def _lattice(kind):
    fig, ax = _canvas(3.3, 3.1, (-0.7, 4.7), (-1.5, 3.7))
    sp = 1.33
    pts = [(i * sp, j * sp) for i in range(4) for j in range(3)]
    centre = (sp * 1, sp * 1)
    for (x, y) in pts:            # bonds: two dots between neighbours
        for dx, dy in ((sp, 0), (0, sp)):
            if (x + dx, y + dy) in pts or (round(x + dx, 3), round(y + dy, 3)) in [(round(a, 3), round(b, 3)) for a, b in pts]:
                ax.plot([x, x + dx], [y, y + dy], color=LINE, lw=3, zorder=0)
                mx, my = x + dx / 2, y + dy / 2
                off = (0, 0.1) if dx else (0.1, 0)
                broken = kind == "broken" and (x, y) == (sp * 2, sp * 1) and dx
                missing = kind == "acceptor" and (x, y) == centre and dx
                for s in (1, -1):
                    px, py = mx + s * off[0], my + s * off[1]
                    if (broken or missing) and s == 1:
                        ax.add_patch(Circle((px, py), 0.09, fc="white", ec=BAD, lw=1.4, zorder=3))
                    else:
                        ax.add_patch(Circle((px, py), 0.065, fc=INK, ec="none", zorder=3))
    for (x, y) in pts:
        lab, fc = "Si", "#eef2f7"
        if (x, y) == centre and kind == "donor":
            lab, fc = "P", "#dcfce7"
        if (x, y) == centre and kind == "acceptor":
            lab, fc = "B", "#fde2e2"
        ax.add_patch(Circle((x, y), 0.3, fc=fc, ec=INK, lw=1, zorder=2))
        ax.text(x, y, lab, ha="center", va="center", fontsize=8.5, zorder=4, weight="bold" if lab != "Si" else "normal")
    if kind == "broken":
        ax.add_patch(Circle((sp * 2.75, sp * 1.6), 0.08, fc=ACC, ec="none", zorder=5))
        ax.annotate("free electron", (sp * 2.75, sp * 1.6), (sp * 0.2, -1.1), fontsize=8, color=ACC,
                    arrowprops=dict(arrowstyle="-", color=ACC, lw=0.8))
        ax.annotate("hole", (sp * 2.5, sp * 1.08), (sp * 2.3, -1.1), fontsize=8, color=BAD,
                    arrowprops=dict(arrowstyle="-", color=BAD, lw=0.8))
    if kind == "donor":
        ax.add_patch(Circle((sp * 0.62, sp * 1.55), 0.08, fc=ACC, ec="none", zorder=5))
        ax.annotate("5th electron:\nno bond to join", (sp * 0.62, sp * 1.55), (-0.6, -1.3), fontsize=7.5, color=ACC,
                    arrowprops=dict(arrowstyle="-", color=ACC, lw=0.8))
    if kind == "acceptor":
        ax.annotate("bond short of\none electron = hole", (sp * 1.5, sp * 1.08), (sp * 1.3, -1.3), fontsize=7.5, color=BAD,
                    arrowprops=dict(arrowstyle="-", color=BAD, lw=0.8))
    titles = {"pure": "0 K: every bond full", "broken": "300 K: one bond broken", "donor": "phosphorus (5 valence e⁻)",
              "acceptor": "boron (3 valence e⁻)"}
    ax.text(sp * 1.5, 3.4, titles[kind], ha="center", fontsize=9, weight="bold")
    return fig


def lattice_pure_broken():
    a, b = _lattice("pure"), _lattice("broken")
    return '<div class="two">' + _svg(a) + _svg(b) + "</div>"


def lattice_dopants():
    return '<div class="two">' + _svg(_lattice("donor")) + _svg(_lattice("acceptor")) + "</div>"


def hole_motion():
    fig, ax = _canvas(8.4, 1.9, (0, 12.4), (-0.6, 2.2))
    for f in range(3):
        x0 = 0.3 + f * 4.2
        for s in range(4):
            x = x0 + s * 1.0
            hole = s == [1, 2, 3][f]
            if hole:
                ax.add_patch(Circle((x + 0.5, 1.0), 0.13, fc="white", ec=BAD, lw=1.5))
            else:
                ax.add_patch(Circle((x + 0.5, 1.0), 0.11, fc=INK, ec="none"))
            ax.plot([x + 0.15, x + 0.85], [0.75, 0.75], color=LINE, lw=2.5)
        if f < 2:
            hx = x0 + ([1, 2, 3][f]) * 1.0 + 0.5
            ax.annotate("", (hx, 1.35), (hx + 1.0, 1.35), arrowprops=dict(arrowstyle="->", color=ACC, lw=1.2,
                                                                         connectionstyle="arc3,rad=0.4"))
            ax.text(hx + 0.5, 1.75, "electron hops left", ha="center", fontsize=7.5, color=ACC)
        ax.text(x0 + 2.0, 0.2, f"step {f + 1}", ha="center", fontsize=8.5, color=MUTED)
    ax.text(6.2, -0.45, "electrons step left one at a time  →  the vacancy (hole) travels right, like a + charge",
            ha="center", fontsize=8.5, color=BAD)
    return _svg(fig)


# ---------------------------------------------------------------- bands
def levels_to_bands():
    fig, ax = _fig(5.6, 3.0)
    a = np.linspace(0.3, 1.0, 300)          # spacing, arbitrary units; 1 = isolated
    spread = np.exp(-(a - 0.3) * 4.5)
    for E0, w, c, lab in ((2.0, 1.0, ACC, "upper level → conduction band"), (0.0, 0.8, BAD, "outer (valence) level → valence band")):
        ax.fill_between(a, E0 - w * spread, E0 + w * spread, color=c, alpha=0.18, lw=0)
        ax.plot(a, E0 - w * spread, color=c, lw=1); ax.plot(a, E0 + w * spread, color=c, lw=1)
        ax.text(0.99, E0 + w * 0.12 + 0.12, lab, ha="left", fontsize=8, color=c)
    x_si = 0.42
    ax.axvline(x_si, color=INK, ls="--", lw=0.9)
    lo = 2.0 - 1.0 * math.exp(-(x_si - 0.3) * 4.5)
    hi = 0.0 + 0.8 * math.exp(-(x_si - 0.3) * 4.5)
    ax.annotate("", (x_si - 0.012, lo), (x_si - 0.012, hi), arrowprops=dict(arrowstyle="<->", color=G2, lw=1.3))
    ax.text(x_si - 0.025, (lo + hi) / 2, "E_g: no\nstates", fontsize=8, color=G2, va="center", ha="left")
    ax.text(x_si + 0.01, -1.5, "spacing in a\nsilicon crystal", ha="right", fontsize=8)
    ax.set_xlim(1.02, 0.28); ax.set_ylim(-1.7, 3.3)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("distance between atoms  →  atoms pushed closer (right)")
    ax.set_ylabel("electron energy  ↑")
    ax.text(1.0, 3.05, "far apart: each atom has its own sharp levels", fontsize=8, color=MUTED)
    return _svg(fig)


def ni_vs_T():
    fig, ax = _fig(5.4, 2.9)
    T = np.linspace(250, 500, 300)
    for name, ni300, Eg, c in (("Ge  (E_g 0.66 eV)", 2.4e13, 0.66, G1), ("Si  (E_g 1.12 eV)", 1.5e10, 1.12, ACC),
                               ("GaAs  (E_g 1.42 eV)", 1.8e6, 1.42, G3)):
        ni = ni300 * (T / 300) ** 1.5 * np.exp(Eg / (2 * k_eV) * (1 / 300 - 1 / T))
        ax.semilogy(T, ni, color=c, lw=1.7)
        ax.text(503, ni[-1], name, fontsize=8, color=c, va="center")
    ax.axvline(300, color=MUTED, ls=":", lw=0.9); ax.text(302, 3e5, "300 K", fontsize=8, color=MUTED)
    ax.set_xlabel("temperature T (K)"); ax.set_ylabel("n_i  (carriers per cm³)")
    ax.set_xlim(250, 500)
    return _svg(fig)


def dopant_levels():
    fig, ax = _canvas(8.0, 2.4, (0, 11), (0, 3.3))
    for i, (name, lvl, lab, txt, c) in enumerate([("donor (P, As)", 2.45, "E_D", "45 meV: heat frees\nthe 5th electron", ACC),
                                                  ("acceptor (B)", 1.05, "E_A", "45 meV: a valence electron\njumps in, leaving a hole", BAD)]):
        x = 0.6 + i * 5.4
        ax.add_patch(Rectangle((x, 2.75), 3.4, 0.45, fc=NCOL, ec="none"))
        ax.add_patch(Rectangle((x, 0.3), 3.4, 0.45, fc=PCOL, ec="none"))
        ax.plot([x, x + 3.4], [2.75, 2.75], color=INK, lw=1.3); ax.text(x + 3.5, 2.75, "E_C", va="center", fontsize=8.5)
        ax.plot([x, x + 3.4], [0.75, 0.75], color=INK, lw=1.3); ax.text(x + 3.5, 0.75, "E_V", va="center", fontsize=8.5)
        for j in range(5):
            ax.plot([x + 0.2 + j * 0.65, x + 0.6 + j * 0.65], [lvl, lvl], color=c, lw=1.6)
        ax.text(x + 3.5, lvl, lab, va="center", fontsize=8.5, color=c)
        if i == 0:
            ax.add_patch(Circle((x + 0.4, lvl + 0.12), 0.08, fc=ACC)); ax.add_patch(Circle((x + 1.05 + 0.2, 2.98), 0.08, fc=ACC))
            ax.annotate("", (x + 1.25, 2.88), (x + 1.05, lvl + 0.1), arrowprops=dict(arrowstyle="->", color=ACC, lw=1))
        else:
            ax.add_patch(Circle((x + 1.25, lvl + 0.1), 0.08, fc=BAD)); ax.add_patch(Circle((x + 1.25, 0.55), 0.09, fc="white", ec=BAD, lw=1.3))
            ax.annotate("", (x + 1.25, lvl), (x + 1.25, 0.68), arrowprops=dict(arrowstyle="->", color=BAD, lw=1))
        ax.text(x + 1.7, 3.25 + 0.0, name, ha="center", fontsize=9, weight="bold")
        ax.text(x + 2.6, 1.75, txt, ha="center", va="center", fontsize=7.8, color=MUTED)
        ax.text(x - 0.1, 1.75, "E_g\n1.12 eV", ha="right", va="center", fontsize=7.5, color=MUTED)
    ax.text(5.5, 0.02, "level spacing drawn wider than real: 45 meV is 1/25 of the gap", ha="center", fontsize=7.5, color=MUTED)
    return _svg(fig)


# ---------------------------------------------------------------- 01b
def seats():
    """States as seats: short lines; filled = dot."""
    fig, ax = _canvas(6.2, 3.1, (0, 9), (0, 4.6))
    rng = np.random.default_rng(3)
    ax.add_patch(Rectangle((0.5, 2.9), 5, 1.5, fc=NCOL, ec="none")); ax.add_patch(Rectangle((0.5, 0.2), 5, 1.5, fc=PCOL, ec="none"))
    for row in range(5):
        y = 3.0 + row * 0.28
        for col in range(10):
            x = 0.7 + col * 0.48
            ax.plot([x, x + 0.3], [y, y], color=INK, lw=1)
            if row == 0 and col in (2, 7):
                ax.add_patch(Circle((x + 0.15, y + 0.08), 0.06, fc=ACC))
        y = 1.6 - row * 0.28
        for col in range(10):
            x = 0.7 + col * 0.48
            ax.plot([x, x + 0.3], [y, y], color=INK, lw=1)
            if not (row == 0 and col in (4, 8)):
                ax.add_patch(Circle((x + 0.15, y + 0.08), 0.06, fc=INK))
            else:
                ax.add_patch(Circle((x + 0.15, y + 0.08), 0.07, fc="white", ec=BAD, lw=1.2))
    ax.text(5.7, 3.65, "conduction band:\nseats almost all empty\n(2 filled = 2 free electrons)", fontsize=8, va="center", color=ACC)
    ax.text(5.7, 0.95, "valence band:\nseats almost all filled\n(2 empty = 2 holes)", fontsize=8, va="center", color=BAD)
    ax.text(5.7, 2.3, "gap: no seats at all", fontsize=8, va="center", color=MUTED)
    ax.text(0.3, 2.3, "energy ↑", rotation=90, fontsize=8, va="center", ha="center")
    ax.text(3.0, 4.52, "each short line = one state (a seat an electron can sit in)", ha="center", fontsize=8.5)
    return _svg(fig)


def fermi_read():
    fig, ax = _fig(5.6, 3.0)
    x = np.linspace(-0.2, 0.2, 400)
    ax.plot(x, np.where(x < 0, 1.0, 0.0), color=MUTED, lw=1.1, ls="--", label="T = 0 K: a step")
    ax.plot(x, 1 / (1 + np.exp(x / 0.0259)), color=ACC, lw=1.8, label="T = 300 K")
    pts = [(0, 0.5, "E = E_F:\nexactly ½", (0.03, 0.62)), (0.0259, 0.269, "1 kT above:\n0.27", (0.07, 0.38)),
           (0.0777, 0.0474, "3 kT above:\n0.047", (0.11, 0.17)), (-0.0777, 0.953, "3 kT below:\n0.953", (-0.19, 0.72))]
    for xp, yp, t, tp in pts:
        ax.plot([xp], [yp], "o", color=BAD, ms=4.5)
        ax.annotate(t, (xp, yp), tp, fontsize=7.8, color=BAD, arrowprops=dict(arrowstyle="-", color=BAD, lw=0.7))
    ax.set_xlabel("E − E_F : how far the seat sits above the Fermi level (eV)")
    ax.set_ylabel("f(E): chance that seat is filled")
    ax.legend(frameon=False, fontsize=8, loc="lower left")
    ax.set_xlim(-0.2, 0.2); ax.set_ylim(-0.03, 1.05)
    return _svg(fig)


def _band_axes(ax, Ec=1.12, Ev=0.0):
    ax.axhline(Ec, color=INK, lw=1); ax.axhline(Ev, color=INK, lw=1)
    ax.axhspan(Ec, Ec + 0.6, color=NCOL, lw=0); ax.axhspan(Ev - 0.6, Ev, color=PCOL, lw=0)
    ax.set_ylim(Ev - 0.55, Ec + 0.55); ax.set_yticks([])


def fermi_rotated():
    fig, axs = _fig(6.4, 3.0, ncols=2, gridspec_kw=dict(width_ratios=[1, 1.4], wspace=0.08))
    kt = 0.09   # drawn wider than real (0.0259) so the tails are visible
    E = np.linspace(-0.55, 1.67, 500)
    EF = 0.56
    a = axs[0]; _band_axes(a); a.set_xticks([])
    a.axhline(EF, color=BAD, ls="--", lw=1.1)
    a.set_xlim(0, 1)
    a.text(0.5, 1.35, "conduction\nband", ha="center", fontsize=8); a.text(0.5, -0.3, "valence\nband", ha="center", fontsize=8)
    a.text(0.5, EF + 0.05, "E_F", ha="center", fontsize=8.5, color=BAD)
    a.text(1.02, 1.12, "E_C", fontsize=8, va="center"); a.text(1.02, 0.0, "E_V", fontsize=8, va="center")
    a.set_ylabel("energy E ↑")
    b = axs[1]; _band_axes(b)
    fE = 1 / (1 + np.exp((E - EF) / kt))
    b.plot(fE, E, color=ACC, lw=1.7)
    b.axhline(EF, color=BAD, ls="--", lw=1.1)
    m = E > 1.12; b.fill_betweenx(E[m], 0, fE[m], color=ACC, alpha=0.5)
    m2 = E < 0; b.fill_betweenx(E[m2], fE[m2], 1, color=BAD, alpha=0.5)
    b.annotate("f > 0 inside the conduction\nband: free electrons", (0.02, 1.2), (0.35, 1.42), fontsize=7.5, color=ACC,
               arrowprops=dict(arrowstyle="-", color=ACC, lw=0.7))
    b.annotate("1 − f > 0 inside the valence\nband: holes", (0.98, -0.08), (0.3, -0.42), fontsize=7.5, color=BAD,
               arrowprops=dict(arrowstyle="-", color=BAD, lw=0.7))
    b.text(0.55, 0.62, "f = ½", fontsize=8, color=BAD)
    b.set_xlim(0, 1.05); b.set_xticks([0, 0.5, 1]); b.set_xlabel("f(E)  (kT drawn 3.5× real)")
    return _svg(fig)


def dos_plot():
    fig, ax = _fig(4.2, 3.0)
    Ec, Ev = 1.12, 0.0
    E1 = np.linspace(Ec, Ec + 0.5, 200); E2 = np.linspace(Ev - 0.5, Ev, 200)
    ax.plot(np.sqrt(E1 - Ec), E1, color=ACC, lw=1.8); ax.plot(0.62 * np.sqrt(Ev - E2), E2, color=BAD, lw=1.8)
    ax.plot([0, 0], [Ev, Ec], color=MUTED, lw=2.5)
    ax.axhline(Ec, color=INK, lw=0.8, ls=":"); ax.axhline(Ev, color=INK, lw=0.8, ls=":")
    ax.text(0.05, 1.5, "g_c(E) grows as √(E − E_C)", fontsize=8.5, color=ACC)
    ax.text(0.05, -0.47, "g_v(E) grows as √(E_V − E)", fontsize=8.5, color=BAD)
    ax.text(0.04, 0.56, "gap: g = 0", fontsize=8.5, color=MUTED, va="center")
    ax.text(-0.02, Ec, "E_C ", ha="right", va="center", fontsize=8); ax.text(-0.02, Ev, "E_V ", ha="right", va="center", fontsize=8)
    ax.set_yticks([]); ax.set_xticks([]); ax.set_xlim(0, 0.75)
    ax.set_xlabel("g(E): seats per unit energy  →"); ax.set_ylabel("energy E ↑")
    return _svg(fig)


def gf_product():
    fig, axs = _fig(7.0, 3.0, ncols=3, sharey=True, gridspec_kw=dict(wspace=0.12))
    Ec, Ev, EF, kt = 1.12, 0.0, 0.56, 0.12   # kt widened so the products show
    E = np.linspace(-0.55, 1.67, 600)
    gc = np.where(E > Ec, np.sqrt(np.clip(E - Ec, 0, None)), 0); gv = np.where(E < Ev, 0.62 * np.sqrt(np.clip(Ev - E, 0, None)), 0)
    f = 1 / (1 + np.exp((E - EF) / kt))
    for a in axs:
        _band_axes(a); a.axhline(EF, color=BAD, ls="--", lw=0.9)
    axs[0].plot(gc, E, color=ACC, lw=1.6); axs[0].plot(gv, E, color=BAD, lw=1.6); axs[0].set_xlabel("① seats g(E)"); axs[0].set_xticks([])
    axs[1].plot(f, E, color=INK, lw=1.6); axs[1].set_xlabel("② chance filled f(E)"); axs[1].set_xticks([0, 1])
    n = gc * f; p = gv * (1 - f)
    s = 1 / max(n.max(), p.max()) * 0.6
    axs[2].fill_betweenx(E, 0, n * s, color=ACC, alpha=0.6); axs[2].fill_betweenx(E, 0, p * s, color=BAD, alpha=0.6)
    axs[2].set_xticks([]); axs[2].set_xlabel("③ = ① × ②  (enlarged)")
    axs[2].text(0.12, 1.3, "area = n", fontsize=8.5, color=ACC); axs[2].text(0.12, -0.25, "area = p", fontsize=8.5, color=BAD)
    axs[0].set_ylabel("energy E ↑"); axs[0].text(0.05, EF + 0.04, "E_F", fontsize=8, color=BAD)
    return _svg(fig)


def nc_equivalent():
    fig, axs = _fig(6.6, 2.8, ncols=2, sharey=True, gridspec_kw=dict(wspace=0.15))
    x = np.linspace(0, 6, 400)                   # (E - E_C)/kT
    g = np.sqrt(x); occ = np.exp(-x); n = g * occ
    a = axs[0]
    a.plot(g / g.max(), x, color=MUTED, lw=1.2, ls="--", label="seats g(E)")
    a.fill_betweenx(x, 0, n / n.max() * 0.8, color=ACC, alpha=0.55, label="electrons g·f")
    a.set_ylabel("height above E_C  (in units of kT)"); a.set_xlabel("real band: seats spread upward,\nfilling dies off within a few kT")
    a.legend(frameon=False, fontsize=7.5, loc="upper right"); a.set_xticks([])
    b = axs[1]
    b.add_patch(Rectangle((0, 0), 0.8, 0.35, fc=ACC, alpha=0.55, ec=ACC))
    b.text(0.4, 0.75, "$N_C$ seats, all placed at $E_C$,\neach filled with chance\n$e^{-(E_C - E_F)/kT}$", ha="center", fontsize=8)
    b.set_xlim(0, 1); b.set_xticks([])
    b.set_xlabel("bookkeeping: same total electrons\nfrom one number N_C")
    for a in axs:
        a.axhline(0, color=INK, lw=1); a.set_ylim(-0.2, 6)
    a.text(1.02, 0, "E_C", transform=a.get_yaxis_transform(), fontsize=8, va="center")
    return _svg(fig)


def boltz_compare():
    fig, ax = _fig(5.2, 2.8)
    x = np.linspace(0, 8, 300)
    ax.semilogy(x, 1 / (1 + np.exp(x)), color=ACC, lw=2.2, label="exact  f = 1/(1 + $e^{x}$)")
    ax.semilogy(x, np.exp(-x), color=G1, lw=1.3, ls="--", label="approximation  $e^{-x}$")
    ax.axvspan(3, 8, color="#e8f5ee", lw=0)
    ax.text(5.5, 0.25, "x ≥ 3: the two agree\nwithin 5 %", ha="center", fontsize=8, color=G2)
    ax.set_xlabel("x = (E − E_F)/kT  : seat height above E_F, in kT"); ax.set_ylabel("chance filled (log scale)")
    ax.legend(frameon=False, fontsize=8, loc="lower left")
    return _svg(fig)


def ef_positions():
    fig, ax = _canvas(8.6, 2.5, (0, 12), (0, 3.5))
    for i, (name, ef, note) in enumerate([("intrinsic: n = p", 1.75, "E_F at mid-gap"),
                                          ("n-type: n ≫ p", 2.4, "E_F moves up toward E_C"),
                                          ("p-type: p ≫ n", 1.1, "E_F moves down toward E_V")]):
        x = 0.4 + i * 4
        ax.add_patch(Rectangle((x, 2.75), 2.8, 0.35, fc=NCOL, ec="none")); ax.add_patch(Rectangle((x, 0.4), 2.8, 0.35, fc=PCOL, ec="none"))
        ax.plot([x, x + 2.8], [2.75, 2.75], color=INK, lw=1.3); ax.text(x + 2.9, 2.75, "E_C", va="center", fontsize=8.5)
        ax.plot([x, x + 2.8], [0.75, 0.75], color=INK, lw=1.3); ax.text(x + 2.9, 0.75, "E_V", va="center", fontsize=8.5)
        ax.plot([x, x + 2.8], [1.75, 1.75], color=MUTED, lw=0.8, ls=":"); ax.text(x - 0.08, 1.75, "E_i", va="center", ha="right", fontsize=7.5, color=MUTED)
        ax.plot([x, x + 2.8], [ef, ef], color=BAD, lw=1.3, ls="--"); ax.text(x + 2.9, ef, "E_F", va="center", fontsize=8.5, color=BAD)
        if ef != 1.75:
            ax.annotate("", (x + 1.4, ef), (x + 1.4, 1.75), arrowprops=dict(arrowstyle="->", color=BAD, lw=1))
        ne, nh = (3, 3) if i == 0 else ((9, 1) if i == 1 else (1, 9))
        for j in range(ne):
            ax.add_patch(Circle((x + 0.25 + j * 0.28, 2.93), 0.08, fc=ACC, ec="none"))
        for j in range(nh):
            ax.add_patch(Circle((x + 0.25 + j * 0.28, 0.57), 0.08, fc="white", ec=BAD, lw=1.1))
        ax.text(x + 1.4, 3.3, name, ha="center", fontsize=9, weight="bold")
        ax.text(x + 1.4, 0.1, note, ha="center", fontsize=8.3, color=MUTED)
    return _svg(fig)


def ef_vs_doping():
    fig, ax = _fig(5.4, 2.9)
    N = np.logspace(14, 18.5, 200)
    ax.semilogx(N, 0.0259 * np.log(N / 1e10), color=ACC, lw=1.8, label="n-type: E_F − E_i = kT ln(N_D/n_i)")
    ax.semilogx(N, -0.0259 * np.log(N / 1e10), color=BAD, lw=1.8, label="p-type: E_F − E_i = −kT ln(N_A/n_i)")
    ax.axhline(0.56, color=INK, lw=0.9); ax.axhline(-0.56, color=INK, lw=0.9); ax.axhline(0, color=MUTED, lw=0.8, ls=":")
    ax.text(1.5e18, 0.6, "E_C", fontsize=8); ax.text(1.5e18, -0.66, "E_V", fontsize=8); ax.text(1.2e14, 0.03, "E_i (mid-gap)", fontsize=8, color=MUTED)
    ax.plot([1e16], [0.358], "o", color=ACC, ms=4); ax.annotate("10¹⁶: 0.358 eV", (1e16, 0.358), (2e14, 0.42), fontsize=7.5, color=ACC,
                                                           arrowprops=dict(arrowstyle="-", color=ACC, lw=0.7))
    ax.set_xlabel("doping N_D or N_A (cm⁻³), log scale"); ax.set_ylabel("E_F − E_i  (eV)")
    ax.set_ylim(-0.7, 0.75); ax.legend(frameon=False, fontsize=7.3, loc="lower left")
    return _svg(fig)


FIGS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith("_") and k not in
        ("Path", "Rectangle", "Circle", "FancyBboxPatch")}
