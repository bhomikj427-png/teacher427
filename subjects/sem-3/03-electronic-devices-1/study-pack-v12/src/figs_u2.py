"""Figures for 02a-drift and 02b-diffusion-continuity (all generated with matplotlib).

Curves come from the same equations verify_u2.py checks: v = μE/(1 + μE/v_sat), the doping-dependent
mobility fit (Caughey–Thomas form, MINIMOS parameters), n(x) = n0·e^(-x/L), and so on.
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "study-pack" / "pdf"))
from figs import (_fig, _canvas, _svg, INK, MUTED, LINE, ACC, G1, G2, G3, BAD, NCOL, PCOL)  # noqa: E402
from matplotlib.patches import Rectangle, Circle, Polygon  # noqa: E402

kT = 0.0259


def mu_fit(N, carrier="n"):
    """Doping-dependent mobility, Si, 300 K (Caughey–Thomas form, MINIMOS parameters)."""
    mmax, mmin, nref, a = (1430, 80, 1.12e17, 0.72) if carrier == "n" else (460, 45, 2.23e17, 0.72)
    return mmin + (mmax - mmin) / (1 + (N / nref) ** a)


# ---------------------------------------------------------------- 02a
def _walk(ax, x0, y0, drift, seed, color, steps=9):
    rng = np.random.default_rng(seed)
    pts = [(x0, y0)]
    for _ in range(steps):
        ang = rng.uniform(0, 2 * np.pi)
        pts.append((pts[-1][0] + 0.55 * np.cos(ang) + drift, pts[-1][1] + 0.55 * np.sin(ang)))
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=1.1)
    for (a, b), (c, d) in zip(pts[:-1], pts[1:]):
        ax.annotate("", (c, d), (a, b), arrowprops=dict(arrowstyle="->", color=color, lw=0.8))
    ax.plot([x0], [y0], "o", color=INK, ms=4)
    ax.plot([xs[-1]], [ys[-1]], "s", color=color, ms=4)
    return xs[-1] - x0


def thermal_walk():
    fig, ax = _fig(4.0, 2.6)
    ax.set_aspect("equal"); ax.axis("off")
    _walk(ax, 0, 0, 0.0, 55, INK, steps=14)
    (x0, y0), (x1, y1) = ax.dataLim.get_points()
    cx = (x0 + x1) / 2
    ax.set_xlim(cx - 1.9, cx + 1.9); ax.set_ylim(y0 - 0.55, y1 + 0.4)
    ax.text(cx, y1 + 0.2, "no field: E = 0", ha="center", fontsize=9, weight="bold")
    ax.text(cx, y0 - 0.45, "● start   ■ end   each corner = a collision", ha="center", fontsize=7.6, color=MUTED)
    return _svg(fig)


def drift_walk():
    fig, axs = _fig(7.0, 2.6, ncols=2)
    for ax, (name, d, c, seed) in zip(axs, (("hole: drifts along E", 0.22, BAD, 10), ("electron: drifts against E", -0.22, ACC, 15))):
        ax.set_xlim(-3.2, 3.2); ax.set_ylim(-1.9, 2.1); ax.set_aspect("equal"); ax.axis("off")
        x0 = -1.0 if d > 0 else 1.0
        net = _walk(ax, x0, 0, d, seed, c)
        ax.annotate("", (x0 + net, -1.45), (x0, -1.45), arrowprops=dict(arrowstyle="->", color=c, lw=1.8))
        ax.text(x0 + net / 2, -1.8, "net shift = drift", ha="center", fontsize=7.8, color=c)
        ax.annotate("", (0.9, 1.85), (-0.9, 1.85), arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
        ax.text(0, 2.0, "field E", ha="center", fontsize=8.5)
        ax.text(0, -2.35, name, ha="center", fontsize=9, weight="bold")
    return _svg(fig)


def vsat_plot():
    fig, ax = _fig(5.4, 3.1)
    E = np.logspace(2, 6, 300)
    for mu, c, lab in ((1350, ACC, r"Si electrons (μ$_\mathrm{n}$ = 1350)"), (480, BAD, r"Si holes (μ$_\mathrm{p}$ = 480)")):
        ax.loglog(E, mu * E / (1 + mu * E / 1e7), color=c, lw=1.8, label=lab)
    ax.loglog(E, 1350 * E, color=ACC, lw=0.9, ls="--")
    ax.text(1.6e2, 2.3e7, r"dashed: v$_\mathrm{d}$ = μE if it never saturated", fontsize=7.6, color=ACC)
    ax.axhline(1e7, color=MUTED, lw=0.8, ls=":"); ax.text(1.3e2, 1.15e7, "v_sat ≈ 10⁷ cm/s", fontsize=8, color=MUTED)
    ax.plot([7.4e3], [1e7 / 2], "o", color=INK, ms=4)
    ax.annotate(r"E = v$_\mathrm{sat}$/μ$_\mathrm{n}$ = 7.4 kV/cm:" "\n" r"v$_\mathrm{d}$ is half of v$_\mathrm{sat}$", (7.4e3, 5e6), (1.0e4, 3e5), fontsize=7.6,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.set_xlabel("electric field E (V/cm), log scale"); ax.set_ylabel("drift velocity v_d (cm/s), log scale")
    ax.set_ylim(5e4, 5e7); ax.legend(frameon=False, fontsize=7.8, loc="lower right")
    return _svg(fig)


def mobility_doping():
    fig, ax = _fig(5.4, 3.0)
    N = np.logspace(14, 20, 300)
    ax.loglog(N, mu_fit(N, "n"), color=ACC, lw=1.8, label=r"electrons μ$_\mathrm{n}$")
    ax.loglog(N, mu_fit(N, "p"), color=BAD, lw=1.8, label=r"holes μ$_\mathrm{p}$")
    for Nv, c, car in ((1e16, ACC, "n"), (5e17, ACC, "n"), (1e16, BAD, "p")):
        ax.plot([Nv], [mu_fit(Nv, car)], "o", color=c, ms=4)
    ax.annotate(r"5 × 10$^{17}$: μ$_\mathrm{n}$ ≈ 420" "\n(slide 52 used 400)", (5e17, mu_fit(5e17)), (2e18, 900), fontsize=7.6, color=ACC,
                arrowprops=dict(arrowstyle="-", color=ACC, lw=0.7))
    ax.set_xlabel("doping N_D or N_A (cm⁻³), log scale"); ax.set_ylabel("mobility μ (cm²/V·s), log scale")
    ax.set_ylim(30, 2500); ax.legend(frameon=False, fontsize=8, loc="lower left")
    return _svg(fig)


def flux_box():
    fig, ax = _canvas(6.6, 2.5, (0, 10.5), (-0.6, 3.4))
    d = 0.6
    ax.add_patch(Polygon([(0.5, 0.3), (8.0, 0.3), (8.0, 2.2), (0.5, 2.2)], fc="#f7f7f4", ec=INK, lw=1))
    ax.add_patch(Polygon([(0.5, 2.2), (0.5 + d, 2.2 + d), (8.0 + d, 2.2 + d), (8.0, 2.2)], fc="#efefea", ec=INK, lw=1))
    ax.add_patch(Polygon([(8.0, 0.3), (8.0 + d, 0.3 + d), (8.0 + d, 2.2 + d), (8.0, 2.2)], fc="#e6e6e0", ec=INK, lw=1))
    ax.add_patch(Rectangle((3.8, 0.3), 1.0, 1.9, fc="#d6f3f1", ec="#14a3a3", lw=1.2))
    rng = np.random.default_rng(2)
    for _ in range(14):
        x, y = rng.uniform(3.85, 4.75), rng.uniform(0.4, 2.1)
        ax.add_patch(Circle((x, y), 0.07, fc="white", ec=BAD, lw=1))
    ax.annotate("", (4.8, -0.25), (3.8, -0.25), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9))
    ax.text(4.3, -0.55, "Δx", ha="center", fontsize=8.5)
    ax.annotate("", (8.4, 2.75), (7.2, 2.75), arrowprops=dict(arrowstyle="->", color=INK, lw=1.3)); ax.text(7.8, 3.1, "field E", ha="center", fontsize=8.5)
    ax.annotate("", (7.0, 1.6), (5.2, 1.6), arrowprops=dict(arrowstyle="->", color=BAD, lw=1.4))
    ax.text(6.1, 1.75, "holes: v_d along E", ha="center", fontsize=7.8, color=BAD)
    ax.annotate("", (1.4, 0.9), (3.2, 0.9), arrowprops=dict(arrowstyle="->", color=ACC, lw=1.4))
    ax.text(2.3, 1.05, "electrons: against E", ha="center", fontsize=7.8, color=ACC)
    ax.text(3.0, 3.25, "slice of area A, width Δx: holes inside = p·A·Δx", ha="center", fontsize=8.5)
    ax.text(9.1, 1.3, "every hole in the\nslice crosses its\nright face within\nΔx / v_d seconds", fontsize=7.6, color=MUTED, va="center")
    return _svg(fig)


def ni_T_sigma():
    fig, ax = _fig(4.8, 2.7)
    T = np.array([25, 35, 45, 55, 65, 75]); ni = np.array([8.1e9, 1.7e10, 3.5e10, 6.9e10, 1.3e11, 2.3e11])
    ax.semilogy(T, ni, "o-", color=ACC, lw=1.5, ms=4)
    for t, v in zip(T, ni):
        ax.text(t, v * 1.35, f"{v:.1e}".replace("e+", "×10^").replace("×10^09", "×10⁹").replace("×10^10", "×10¹⁰").replace("×10^11", "×10¹¹"),
                ha="center", fontsize=6.8, color=MUTED)
    ax.set_xlabel("temperature (°C)"); ax.set_ylabel("n_i (cm⁻³), log scale")
    ax.set_ylim(5e9, 5e11); ax.set_xlim(20, 80)
    return _svg(fig)


def sigma_doping():
    fig, ax = _fig(5.4, 3.0)
    N = np.logspace(13, 19, 300)
    q = 1.6e-19
    ax.loglog(N, q * N * mu_fit(N, "n"), color=ACC, lw=1.8, label=r"n-type: σ ≈ qN$_\mathrm{D}$μ$_\mathrm{n}$")
    ax.loglog(N, q * N * mu_fit(N, "p"), color=BAD, lw=1.8, label=r"p-type: σ ≈ qN$_\mathrm{A}$μ$_\mathrm{p}$")
    ax.axhline(3.12e-6, color=MUTED, lw=0.9, ls=":"); ax.text(1.3e13, 5e-6, "intrinsic Si: σ = 3.12 × 10⁻⁶", fontsize=7.8, color=MUTED)
    ax.plot([5e17], [32], "o", color=ACC, ms=4)
    ax.annotate("slide 52: N_D = 5 × 10¹⁷,\nσ ≈ 32 (Ω·cm)⁻¹", (5e17, 32), (1e18, 1e-2), fontsize=7.6, color=ACC,
                arrowprops=dict(arrowstyle="-", color=ACC, lw=0.7))
    ax.set_xlabel("doping (cm⁻³), log scale"); ax.set_ylabel("conductivity σ ((Ω·cm)⁻¹), log scale")
    ax.set_ylim(1e-7, 1e3); ax.legend(frameon=False, fontsize=7.8, loc="upper left")
    return _svg(fig)


def bar_resistor():
    fig, ax = _canvas(6.2, 2.2, (0, 10), (-0.4, 3.1))
    d = 0.7
    ax.add_patch(Polygon([(1.5, 0.4), (7.5, 0.4), (7.5, 1.6), (1.5, 1.6)], fc=NCOL, ec=INK, lw=1))
    ax.add_patch(Polygon([(1.5, 1.6), (1.5 + d, 1.6 + d), (7.5 + d, 1.6 + d), (7.5, 1.6)], fc="#c9defc", ec=INK, lw=1))
    ax.add_patch(Polygon([(7.5, 0.4), (7.5 + d, 0.4 + d), (7.5 + d, 1.6 + d), (7.5, 1.6)], fc="#b8d3fb", ec=INK, lw=1))
    ax.annotate("", (7.5, 0.05), (1.5, 0.05), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9)); ax.text(4.5, -0.3, "length L (current flows this way)", ha="center", fontsize=8)
    ax.annotate("", (7.5 + d, 2.3), (7.5, 1.6), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9)); ax.text(8.4, 2.1, "width W", fontsize=8)
    ax.annotate("", (8.45, 1.6), (8.45, 0.4), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9)); ax.text(8.6, 0.95, "thickness t", fontsize=8)
    ax.text(4.5, 2.75, "cross-section A = W × t", ha="center", fontsize=8.5)
    for x in (0.3, 8.9):
        pass
    ax.plot([0.4, 1.5], [1.0, 1.0], color=INK, lw=1.3); ax.plot([7.5 + d / 2, 9.6], [1.0 + d / 2, 1.0 + d / 2], color=INK, lw=1.3)
    ax.text(0.3, 1.25, "+V", fontsize=8.5); ax.text(9.35, 1.6, "0 V", fontsize=8.5)
    ax.text(4.5, 1.0, "n-type, resistivity ρ", ha="center", fontsize=8.5)
    return _svg(fig)


def sheet_squares():
    fig, ax = _canvas(7.0, 2.2, (0, 12), (-0.6, 3.0))
    for i, (x, s) in enumerate(((0.3, 0.7), (1.7, 1.6))):
        ax.add_patch(Rectangle((x, 1.0), s, s, fc=NCOL, ec=INK, lw=1))
        ax.text(x + s / 2, 0.75, "R_s" if i == 0 else "R_s too", ha="center", fontsize=8, va="top")
    ax.text(1.6, 2.85, "a square of any size", ha="center", fontsize=8.5, weight="bold")
    ax.text(1.6, -0.45, "longer by k, wider by k:\nthe two cancel", ha="center", fontsize=7.6, color=MUTED)
    x0 = 4.4
    for k in range(5):
        ax.add_patch(Rectangle((x0 + k * 1.3, 1.0), 1.3, 1.3, fc=NCOL, ec=INK, lw=1, ls="--" if 0 < k else "-"))
        ax.text(x0 + k * 1.3 + 0.65, 1.65, str(k + 1), ha="center", va="center", fontsize=9, color=MUTED)
    ax.annotate("", (x0 + 6.5, 0.75), (x0, 0.75), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9)); ax.text(x0 + 3.25, 0.35, "L", ha="center", fontsize=8.5)
    ax.annotate("", (x0 - 0.2, 2.3), (x0 - 0.2, 1.0), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9)); ax.text(x0 - 0.45, 1.65, "W", ha="right", va="center", fontsize=8.5)
    ax.text(x0 + 3.25, 2.85, "top view of a resistor: L/W = 5 squares in series", ha="center", fontsize=8.5, weight="bold")
    ax.text(x0 + 3.25, -0.4, "R = 5 × R_s", ha="center", fontsize=9, color=ACC)
    return _svg(fig)


# ---------------------------------------------------------------- 02b
def diffusion_spread():
    fig, ax = _fig(5.6, 2.8)
    x = np.linspace(-4, 4, 400)
    for s, c, lab in ((0.3, INK, "t₀: all bunched"), (0.8, ACC, "t₁ later"), (1.6, G1, "t₂ later still")):
        y = np.exp(-x ** 2 / (2 * s ** 2)) / s * 0.3
        ax.plot(x, y, color=c, lw=1.7, label=lab)
    ax.annotate("", (3.4, 0.08), (1.9, 0.08), arrowprops=dict(arrowstyle="->", color=BAD, lw=1.3))
    ax.annotate("", (-3.4, 0.08), (-1.9, 0.08), arrowprops=dict(arrowstyle="->", color=BAD, lw=1.3))
    ax.text(1.5, 0.45, "net flow:\ncrowded → sparse", ha="left", fontsize=7.8, color=BAD)
    ax.set_xlabel("position x"); ax.set_ylabel("carriers per cm³ at x")
    ax.set_yticks([]); ax.legend(frameon=False, fontsize=8)
    return _svg(fig)


def crossing_count():
    fig, ax = _canvas(6.4, 2.2, (0, 10), (-0.5, 3.0))
    ax.plot([5, 5], [0.0, 2.6], color=INK, lw=1.2, ls="--"); ax.text(5, 2.75, "plane at x", ha="center", fontsize=8.5)
    rng = np.random.default_rng(4)
    for _ in range(26):
        ax.add_patch(Circle((rng.uniform(0.6, 4.7), rng.uniform(0.2, 2.4)), 0.09, fc=ACC))
    for _ in range(7):
        ax.add_patch(Circle((rng.uniform(5.3, 9.4), rng.uniform(0.2, 2.4)), 0.09, fc=ACC))
    ax.annotate("", (6.4, 1.6), (3.6, 1.6), arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
    ax.annotate("", (3.9, 0.8), (6.1, 0.8), arrowprops=dict(arrowstyle="->", color=INK, lw=0.8))
    ax.text(2.6, -0.35, "crowded side: 26 carriers,\nhalf head right = 13", ha="center", fontsize=7.6)
    ax.text(7.4, -0.35, "sparse side: 7 carriers,\nhalf head left = 3.5", ha="center", fontsize=7.6)
    return _svg(fig)


def fick_slopes():
    fig, axs = _fig(6.6, 2.5, ncols=2)
    x = np.linspace(0, 1, 100)
    for ax, y, lab, arrow in ((axs[0], 1 - 0.8 * x, "dn/dx < 0  →  flow towards +x", (0.35, 0.65)),
                              (axs[1], 0.2 + 0.8 * x, "dn/dx > 0  →  flow towards −x", (0.65, 0.35))):
        ax.plot(x, y, color=ACC, lw=1.8)
        ax.annotate("", (arrow[1], 0.3), (arrow[0], 0.3), arrowprops=dict(arrowstyle="->", color=BAD, lw=1.6))
        ax.text(0.5, 0.15, "flux F", ha="center", fontsize=8, color=BAD)
        ax.set_title(lab, fontsize=8.5); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(0, 1.1)
        ax.set_xlabel("position x"); ax.set_ylabel("n (or p) at x")
    return _svg(fig)


def diff_signs():
    fig, axs = _fig(6.8, 2.4, ncols=2)
    x = np.linspace(0, 1, 100)
    for ax, (car, c, cur) in zip(axs, (("electrons (charge −q)", ACC, "current → −x"), ("holes (charge +q)", BAD, "current → +x"))):
        ax.plot(x, 1 - 0.8 * x, color=c, lw=1.8)
        ax.annotate("", (0.55, 0.32), (0.15, 0.32), arrowprops=dict(arrowstyle="->", color=c, lw=1.5)); ax.text(0.35, 0.37, "particles → +x", ha="center", fontsize=7.8, color=c)
        ax.annotate("", (0.15 if c == ACC else 0.55, 0.1), (0.55 if c == ACC else 0.15, 0.1), arrowprops=dict(arrowstyle="->", color=INK, lw=1.5))
        ax.text(0.35, 0.15, cur, ha="center", fontsize=7.8)
        ax.set_title(car + ", same falling profile", fontsize=8.3); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(0, 1.1)
        ax.set_xlabel("position x"); ax.set_ylabel("concentration")
    return _svg(fig)


def equilibrium_balance():
    fig, axs = _fig(7.2, 3.3, ncols=3, gridspec_kw=dict(wspace=0.45))
    x = np.linspace(0, 1.5, 300)                     # µm
    n = 10 ** (17 - 2 / (1 + np.exp(-(x - 0.75) / 0.12)))   # 1e17 -> 1e15
    Ec = kT * np.log(2.8e19 / n)                      # E_C - E_F (eV), E_F = 0
    a = axs[0]
    a.plot(x, Ec, color=INK, lw=1.6); a.axhline(0, color=BAD, ls="--", lw=1.1)
    a.text(0.05, Ec[0] + 0.012, "E_C", fontsize=8); a.text(1.0, 0.012, "E_F (flat)", fontsize=8, color=BAD)
    a.set_ylim(-0.03, 0.32); a.set_ylabel("energy above E_F (eV)"); a.set_xlabel("x (µm)")
    a.set_title("① bands", fontsize=8.5)
    b = axs[1]
    b.semilogy(x, n, color=ACC, lw=1.6); b.set_ylabel("n (cm⁻³), log"); b.set_xlabel("x (µm)"); b.set_title("② electrons", fontsize=8.5)
    D = 35.0
    dn = np.gradient(n, x * 1e-4)
    Jd = 1.6e-19 * D * dn
    c = axs[2]
    c.plot(x, Jd / 1e3, color=G1, lw=1.5, ls="--", label="J_n diffusion")
    c.plot(x, -Jd / 1e3, color=G2, lw=1.5, label="J_n drift")
    c.axhline(0, color=INK, lw=1.4); c.text(1.05, 1.0, "sum = 0", fontsize=8)
    c.set_ylabel("J (kA/cm²)"); c.set_xlabel("x (µm)"); c.set_title("③ the two currents", fontsize=8.5)
    c.legend(frameon=False, fontsize=7, loc="lower right")
    return _svg(fig)


def gr_events():
    fig, ax = _canvas(7.4, 2.3, (0, 13), (-0.9, 3.0))
    for i, (title, before_top, before_bot, after_top, after_bot, arrow_up) in enumerate(
            (("generation", False, True, True, False, True), ("recombination", True, False, False, True, False))):
        x0 = 0.5 + i * 6.6
        for j, (top, bot, lab) in enumerate(((before_top, before_bot, "before"), (after_top, after_bot, "after"))):
            x = x0 + j * 2.9
            ax.plot([x, x + 2.2], [2.3, 2.3], color=ACC, lw=1.6); ax.plot([x, x + 2.2], [0.4, 0.4], color=ACC, lw=1.6)
            ax.text(x + 2.3, 2.3, "E_C", fontsize=7.5, va="center"); ax.text(x + 2.3, 0.4, "E_V", fontsize=7.5, va="center")
            ax.add_patch(Circle((x + 1.1, 2.42), 0.1, fc=ACC if top else "white", ec=ACC, lw=1.1))
            ax.add_patch(Circle((x + 1.1, 0.28), 0.1, fc=ACC if bot else "white", ec=ACC, lw=1.1))
            ax.text(x + 1.1, -0.15, lab, ha="center", fontsize=7.8, color=MUTED)
            if j == 0:
                ax.annotate("", (x + 1.1, 2.2) if arrow_up else (x + 1.1, 0.5), (x + 1.1, 0.5) if arrow_up else (x + 1.1, 2.2),
                            arrowprops=dict(arrowstyle="->", color=INK, lw=1))
        ax.text(x0 + 2.5, -0.7, title + (": energy in, a pair appears" if i == 0 else ": energy out, a pair vanishes"),
                ha="center", fontsize=8.5, weight="bold")
    return _svg(fig)


def direct_vs_trap():
    fig, ax = _canvas(7.4, 2.4, (0, 13), (-0.9, 3.1))
    for i in range(2):
        x = 0.8 + i * 6.6
        ax.plot([x, x + 3.6], [2.4, 2.4], color=ACC, lw=1.6); ax.plot([x, x + 3.6], [0.4, 0.4], color=ACC, lw=1.6)
        ax.text(x + 3.7, 2.4, "E_C", fontsize=7.5, va="center"); ax.text(x + 3.7, 0.4, "E_V", fontsize=7.5, va="center")
        ax.add_patch(Circle((x + 1.2, 2.52), 0.1, fc=ACC))
        ax.add_patch(Circle((x + 1.2, 0.28), 0.1, fc="white", ec=ACC, lw=1.1))
    ax.annotate("", (2.0, 0.5), (2.0, 2.3), arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    ax.annotate("photon", (2.3, 1.4), (3.1, 1.6), fontsize=8, color=G1, arrowprops=dict(arrowstyle="-", color=G1, lw=0.7))
    ax.text(2.6, -0.7, "direct (band-to-band): GaAs, gives light", ha="center", fontsize=8.5, weight="bold")
    x = 7.4
    ax.plot([x + 0.6, x + 3.0], [1.4, 1.4], color=BAD, lw=1.2, ls="--"); ax.text(x + 3.1, 1.4, "E_T (trap)", fontsize=7.5, va="center", color=BAD)
    ax.annotate("", (x + 1.5, 1.5), (x + 1.2, 2.3), arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    ax.annotate("", (x + 1.25, 0.5), (x + 1.5, 1.3), arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    ax.text(x + 0.3, 1.95, "①", fontsize=8.5); ax.text(x + 0.3, 0.85, "②", fontsize=8.5)
    ax.text(9.2, -0.7, "through a trap (SRH): Si, gives heat", ha="center", fontsize=8.5, weight="bold")
    return _svg(fig)


def lifetime_decay():
    fig, ax = _fig(5.2, 2.8)
    t = np.linspace(0, 5, 300)
    ax.plot(t, np.exp(-t), color=ACC, lw=1.8)
    for tt in (1, 2, 3):
        ax.plot([tt], [np.exp(-tt)], "o", color=BAD, ms=4)
        ax.text(tt + 0.08, np.exp(-tt) + 0.05, f"{np.exp(-tt):.3f}", fontsize=8, color=BAD)
    ax.axvline(1, color=MUTED, ls=":", lw=0.8)
    ax.set_xlabel("time since the light went off, t / τ (in lifetimes)")
    ax.set_ylabel("Δp(t) / Δp(0): fraction of\nextra holes still left")
    ax.set_ylim(0, 1.05); ax.set_xlim(0, 5)
    return _svg(fig)


def continuity_box():
    fig, ax = _canvas(6.6, 2.5, (0, 11), (-0.6, 3.4))
    ax.plot([0.3, 10.7], [2.4, 2.4], color=LINE, lw=1); ax.plot([0.3, 10.7], [0.4, 0.4], color=LINE, lw=1)
    ax.add_patch(Rectangle((4.2, 0.4), 2.4, 2.0, fc="#d6f3f1", ec="#14a3a3", lw=1.3))
    ax.annotate("", (4.15, 1.4), (2.3, 1.4), arrowprops=dict(arrowstyle="->", color=ACC, lw=1.8))
    ax.text(2.0, 1.75, "F_n(x) × A\nelectrons in per s", ha="center", fontsize=8, color=ACC)
    ax.annotate("", (8.5, 1.4), (6.65, 1.4), arrowprops=dict(arrowstyle="->", color=ACC, lw=1.8))
    ax.text(8.9, 1.75, "F_n(x + Δx) × A\nelectrons out per s", ha="center", fontsize=8, color=ACC)
    ax.text(5.4, 1.4, "(R − G)·AΔx\nlost per s\ninside", ha="center", va="center", fontsize=7.8, color=BAD)
    ax.annotate("", (6.6, 0.05), (4.2, 0.05), arrowprops=dict(arrowstyle="<->", color=INK, lw=0.9))
    ax.text(4.2, -0.35, "x", ha="center", fontsize=8.5); ax.text(6.6, -0.35, "x + Δx", ha="center", fontsize=8.5)
    ax.text(5.4, 3.0, "box: face area A, width Δx, electrons inside = n·A·Δx", ha="center", fontsize=8.5)
    return _svg(fig)


def diff_length():
    fig, ax = _fig(5.4, 2.8)
    L = 35.2
    x = np.linspace(0, 150, 300)
    ax.plot(x, np.exp(-x / L), color=BAD, lw=1.8)
    for xx in (L, 50):
        ax.plot([xx], [np.exp(-xx / L)], "o", color=INK, ms=4)
    ax.annotate("x = L_p = 35.2 µm: 1/e = 0.368 left", (L, np.exp(-1)), (50, 0.6), fontsize=7.8,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.annotate("x = 50 µm: 0.242", (50, np.exp(-50 / L)), (70, 0.3), fontsize=7.8,
                arrowprops=dict(arrowstyle="-", color=INK, lw=0.7))
    ax.set_xlabel("distance x into the n-type side from where holes enter (µm)")
    ax.set_ylabel("Δp(x) / Δp(0): fraction\nof injected holes left")
    ax.set_ylim(0, 1.05); ax.set_xlim(0, 150)
    return _svg(fig)


def poisson_stack():
    fig, axs = _fig(6.8, 2.5, ncols=3, gridspec_kw=dict(wspace=0.4))
    x = np.linspace(-1.5, 1.5, 400)
    rho = np.where((x > -1) & (x < 0), -1, 0) + np.where((x >= 0) & (x < 1), 1, 0)
    Ef = np.where(x < -1, 0, np.where(x < 0, -(x + 1), np.where(x < 1, -(1 - x), 0)))
    V = np.cumsum(-Ef) * (x[1] - x[0])
    for ax, y, lab, c in ((axs[0], rho, "① charge ρ(x)", INK), (axs[1], Ef, "② field E(x)", ACC), (axs[2], V, "③ potential V(x)", G2)):
        ax.plot(x, y, color=c, lw=1.7); ax.axhline(0, color=MUTED, lw=0.6)
        ax.set_title(lab, fontsize=8.5); ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel("position x")
    axs[0].text(-0.5, -0.75, "−", ha="center", fontsize=12); axs[0].text(0.5, 0.55, "+", ha="center", fontsize=12)
    axs[1].text(0, -1.25, "slope = ρ/ε", ha="center", fontsize=7.8, color=ACC); axs[1].set_ylim(-1.4, 0.3)
    axs[2].text(-1.45, V.max() * 0.92, "slope = −E", ha="center", fontsize=7.8, color=G2)
    return _svg(fig)


FIGS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith("_") and k not in
        ("Path", "Rectangle", "Circle", "Polygon", "mu_fit")}
