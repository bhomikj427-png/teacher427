"""Figures for EDC-ETE-v1.pdf (core helpers + cover + Parts A and B). Each public function returns inline SVG.

Everything is generated: circuits with schemdraw (helpers reused from the ED lab pack), plots and
sketches with matplotlib. Plotted curves come from the same equations verify.py checks.
"""
import io
import re
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "08-electronic-devices-lab-1" / "study-pack" / "src"))
import figures as lab  # noqa: E402  (schemdraw helpers: _d, _svg, W, RES, CAP, DOT, TXT, GND, OUT)
import schemdraw.elements as elm  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Polygon  # noqa: E402

INK, MUTED, LINE, SOFT = "#1c1f24", "#6a707a", "#c9cbc4", "#f0f0eb"
ACC, G1, G2, G3, BAD = "#2f5bea", "#e0661b", "#12925a", "#b23fbf", "#d92d20"
NCOL, PCOL = "#dbeafe", "#fde2e2"   # n-type blue tint, p-type red tint
RC = {"font.family": ["Segoe UI", "DejaVu Sans"], "font.size": 9.5, "svg.fonttype": "none", "axes.grid": False,
      "axes.edgecolor": INK, "text.color": INK, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
      "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.9,
      "mathtext.fontset": "custom", "mathtext.rm": "Segoe UI", "mathtext.it": "Segoe UI:italic"}
W, RES, CAP, DOT, TXT, GND, OUT = lab.W, lab.RES, lab.CAP, lab.DOT, lab.TXT, lab.GND, lab.OUT
_SUB = re.compile(r"(?<![\w$\\{])([A-Za-z]{1,2})_([A-Za-z0-9]+)")


def _m(t):
    return _SUB.sub(lambda g: r"$\mathrm{%s}_{\mathrm{%s}}$" % (g.group(1), g.group(2)), t) if isinstance(t, str) and "$" not in t else t


def _svg(fig):
    from matplotlib.text import Text
    for t in fig.findobj(Text):
        t.set_text(_m(t.get_text()))
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", pad_inches=0.04, transparent=True)
    plt.close(fig)
    s = buf.getvalue()
    s = s[s.index("<svg"):]
    return re.sub(r'width="[\d.]+pt" height="[\d.]+pt"', 'class="mpl"', s, count=1)


def _fig(w, h, **kw):
    with plt.rc_context(RC):
        return plt.subplots(figsize=(w, h), **kw)


def _canvas(w, h, xlim, ylim):
    fig, ax = _fig(w, h)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def _box(ax, x, y, w, h, text="", fc="white", ec=INK, lw=1.3, fs=9.5, r=0.08, color=INK, weight="normal", ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw, ls=ls))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=color, weight=weight)


def _arrow(ax, p, q, color=INK, lw=1.3, rad=0.0, ls="-"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>,head_length=0.4,head_width=0.22", connectionstyle=f"arc3,rad={rad}",
                                 color=color, lw=lw, ls=ls, shrinkA=0, shrinkB=0, mutation_scale=10))


def _axes(ax, xl="", yl=""):
    ax.set_xlabel(xl); ax.set_ylabel(yl)


def _sd(d, width=None):
    """schemdraw drawing -> svg, optionally with a fixed display width in mm."""
    s = lab._svg(d)
    if width:
        s = f'<div style="width:{width}mm;margin:0 auto">' + re.sub(r'(<svg[^>]*?)\swidth="[^"]+"\sheight="[^"]+"', r"\1", s, count=1) + "</div>"
    return s


def _d(unit=2.4, fs=11):
    return lab._d(unit=unit, fs=fs)


# ================================================================== cover
def flow_map():
    nodes = [("1 · Semi-\nconductors", "A"), ("2 · PN junction,\ndiode circuits", "B"), ("3 · JFET", "C"), ("4 · MOSFET", "D"),
             ("5 · BJT,\namplifiers", "E"), ("6 · Feedback", "F"), ("7 · Oscillators", "G")]
    fig, ax = _canvas(9.6, 2.6, (-0.2, 14.3), (-1.3, 2.3))
    for i, (t, p) in enumerate(nodes):
        x = i * 2.05
        _box(ax, x, 0.6, 1.8, 1.15, t, fc="#e8eefe", ec=ACC, fs=8.4, r=0.14)
        ax.text(x + 0.9, 1.98, f"Part {p}", ha="center", fontsize=8, color=ACC, weight="bold")
        if i:
            _arrow(ax, (x - 0.25, 1.17), (x, 1.17), color=ACC, lw=1.2)
    notes = ["carriers,\ndrift, diffusion", "one junction", "junction controls\na channel", "oxide gate controls\na channel",
             "two junctions,\ncurrent control", "output fed back,\nsubtracting", "output fed back,\nadding"]
    for i, t in enumerate(notes):
        ax.text(i * 2.05 + 0.9, 0.42, t, ha="center", va="top", fontsize=7.4, color=MUTED)
    ax.text(0, -1.05, "Each part uses the one before it. Read in order.", fontsize=8.5, color=MUTED)
    return _svg(fig)


def sub_map(items, color=ACC):
    n = len(items)
    fig, ax = _canvas(min(9.6, 1.62 * n), 0.9, (-0.05, 2.0 * n - 0.3), (-0.05, 0.95))
    for i, t in enumerate(items):
        _box(ax, i * 2.0, 0, 1.7, 0.85, t, fc="#e8eefe", ec=color, fs=8.0, r=0.12)
        if i:
            _arrow(ax, (i * 2.0 - 0.3, 0.42), (i * 2.0, 0.42), color=color, lw=1.1)
    return _svg(fig)


# ================================================================== Part A
def bands():
    fig, ax = _canvas(8.6, 2.5, (0, 12), (0, 3.6))
    specs = [("Conductor", 0.0, "bands overlap:\nelectrons always free"), ("Semiconductor", 1.0, "small gap: heat frees\na few electrons"),
             ("Insulator", 2.0, "gap too wide:\nalmost none free")]
    for i, (name, gap, note) in enumerate(specs):
        x = 0.4 + i * 4
        top = 1.55 if gap == 0 else 1.75 + gap * 0.42
        ax.add_patch(Rectangle((x, top), 2.6, 0.75, fc=NCOL, ec=INK, lw=1))
        ax.add_patch(Rectangle((x, 0.75), 2.6, 0.95, fc=PCOL, ec=INK, lw=1))
        ax.text(x + 1.3, top + 0.37, "conduction band", ha="center", va="center", fontsize=8)
        ax.text(x + 1.3, 1.1 if gap else 1.0, "valence band", ha="center", va="center", fontsize=8)
        if gap:
            ax.annotate("", (x + 2.85, top), (x + 2.85, 1.7), arrowprops=dict(arrowstyle="<->", color=ACC, lw=1.1))
            ax.text(x + 2.95, (top + 1.7) / 2, "E_g ≈ 1 eV" if gap == 1 else "E_g > 5 eV", fontsize=8, color=ACC, va="center")
        ax.text(x + 1.3, 3.4 if gap < 2 else 3.52, name, ha="center", fontsize=9.5, weight="bold")
        ax.text(x + 1.3, 0.6, note, ha="center", va="top", fontsize=7.8, color=MUTED)
    return _svg(fig)


def doping_bands():
    fig, ax = _canvas(8.6, 2.5, (0, 12), (0, 3.5))
    for i, (name, ef, lvl, note) in enumerate([("Intrinsic (pure)", 1.75, None, "n = p = n_i"),
                                               ("n-type (donors, e.g. P, As)", 2.15, 2.55, "n ≈ N_D (majority),  p tiny"),
                                               ("p-type (acceptors, e.g. B)", 1.35, 0.95, "p ≈ N_A (majority),  n tiny")]):
        x = 0.4 + i * 4
        ax.plot([x, x + 2.8], [2.75, 2.75], color=INK, lw=1.4); ax.text(x + 2.9, 2.75, "E_C", va="center", fontsize=8.5)
        ax.plot([x, x + 2.8], [0.75, 0.75], color=INK, lw=1.4); ax.text(x + 2.9, 0.75, "E_V", va="center", fontsize=8.5)
        ax.plot([x, x + 2.8], [ef, ef], color=BAD, lw=1.2, ls="--"); ax.text(x + 2.9, ef, "E_F", va="center", fontsize=8.5, color=BAD)
        if lvl:
            ax.plot([x + 0.3, x + 2.5], [lvl, lvl], color=G2, lw=1.2, ls=":")
            ax.text(x + 0.3, lvl + (-0.25 if lvl > 2 else 0.07), "donor level" if lvl > 2 else "acceptor level", fontsize=7.5, color=G2)
        ne, nh = (3, 3) if i == 0 else ((9, 1) if i == 1 else (1, 9))
        for j in range(ne):
            ax.add_patch(Circle((x + 0.25 + j * 0.28, 2.95), 0.09, fc=ACC, ec="none"))
        for j in range(nh):
            ax.add_patch(Circle((x + 0.25 + j * 0.28, 0.55), 0.09, fc="white", ec=BAD, lw=1.1))
        ax.text(x + 1.4, 3.35, name, ha="center", fontsize=9, weight="bold")
        ax.text(x + 1.4, 0.12, note, ha="center", fontsize=8.6, color=MUTED)
    ax.text(0.4, 1.95, "● electron", fontsize=7.5, color=ACC); ax.text(0.4, 1.45, "○ hole", fontsize=7.5, color=BAD)
    return _svg(fig)


def fermi_plot():
    fig, ax = _fig(5.2, 2.5)
    E = np.linspace(-0.3, 0.3, 400)
    ax.plot(E, np.where(E < 0, 1.0, 0.0), color=MUTED, lw=1.2, label="0 K (step)")
    for T, c in ((300, ACC), (600, G1)):
        ax.plot(E, 1 / (1 + np.exp(E / (8.617e-5 * T))), color=c, lw=1.6, label=f"{T} K")
    ax.plot([0], [0.5], "o", color=BAD, ms=5); ax.annotate("f(E_F) = ½ at any T", (0, 0.5), (0.04, 0.68), fontsize=8.5, color=BAD,
                                                            arrowprops=dict(arrowstyle="-", color=BAD, lw=0.8))
    ax.set_xlabel("E − E_F  (eV)"); ax.set_ylabel("f(E): chance a state is filled"); ax.legend(frameon=False, fontsize=8)
    return _svg(fig)


def drift_diff():
    fig, ax = _canvas(8.8, 2.3, (0, 12), (0, 3.2))
    ax.add_patch(Rectangle((0.3, 0.7), 4.9, 1.7, fc=SOFT, ec=INK))
    _arrow(ax, (0.6, 2.75), (4.9, 2.75), color=INK); ax.text(2.75, 2.92, "electric field E", ha="center", fontsize=8.5)
    ax.add_patch(Circle((3.8, 1.9), 0.13, fc=ACC, ec="none")); _arrow(ax, (3.6, 1.9), (2.0, 1.9), color=ACC)
    ax.text(1.9, 1.9, "electron", ha="right", va="center", fontsize=8, color=ACC)
    ax.add_patch(Circle((1.6, 1.15), 0.13, fc="white", ec=BAD, lw=1.2)); _arrow(ax, (1.8, 1.15), (3.4, 1.15), color=BAD)
    ax.text(3.5, 1.15, "hole", va="center", fontsize=8, color=BAD)
    ax.text(2.75, 0.3, "DRIFT: a field pushes charges.  v_d = μE", ha="center", fontsize=8.8, weight="bold")
    ax.add_patch(Rectangle((6.6, 0.7), 4.9, 1.7, fc=SOFT, ec=INK))
    rng = np.random.default_rng(3)
    xs = 6.7 + 4.6 * rng.random(170) ** 2.6; ys = 0.8 + 1.5 * rng.random(170)
    ax.scatter(xs, ys, s=5, color=ACC)
    _arrow(ax, (7.6, 2.75), (10.6, 2.75), color=INK); ax.text(9.05, 2.92, "net flow: crowded → empty", ha="center", fontsize=8.5)
    ax.text(9.05, 0.3, "DIFFUSION: no field needed, only a concentration slope", ha="center", fontsize=8.8, weight="bold")
    return _svg(fig)


def sheet_res():
    fig, ax = _canvas(5.4, 2.2, (0, 8), (0, 3.3))
    ax.add_patch(Polygon([(1, 1), (6, 1), (7, 1.9), (2, 1.9)], fc=NCOL, ec=INK))
    ax.add_patch(Polygon([(1, 0.6), (6, 0.6), (6, 1), (1, 1)], fc="#c7dafc", ec=INK))
    ax.add_patch(Polygon([(6, 0.6), (7, 1.5), (7, 1.9), (6, 1)], fc="#b3cbf7", ec=INK))
    ax.annotate("", (6, 0.35), (1, 0.35), arrowprops=dict(arrowstyle="<->", color=INK)); ax.text(3.5, 0.05, "L (current flows along L)", ha="center", fontsize=8.5)
    ax.annotate("", (7.25, 1.95), (6.3, 1.1), arrowprops=dict(arrowstyle="<->", color=INK)); ax.text(7.2, 1.3, "W", fontsize=9)
    ax.annotate("", (0.8, 1.0), (0.8, 0.6), arrowprops=dict(arrowstyle="<->", color=INK)); ax.text(0.35, 0.72, "t", fontsize=9)
    _arrow(ax, (0.2, 1.5), (1.3, 1.5), color=BAD); ax.text(0.15, 1.7, "I", color=BAD, fontsize=9)
    ax.text(4, 2.75, "R = ρL / (W·t) = (ρ/t)·(L/W) = R_s × (number of squares)", ha="center", fontsize=9.2, weight="bold")
    return _svg(fig)


def gr_fig():
    fig, ax = _canvas(8.4, 2.1, (0, 12), (0, 3))
    for i, (name, kind) in enumerate([("Generation", "g"), ("Direct recombination", "r"), ("Recombination through a trap (indirect)", "t")]):
        x = 0.3 + i * 4
        ax.plot([x, x + 3], [2.3, 2.3], color=INK, lw=1.3); ax.plot([x, x + 3], [0.8, 0.8], color=INK, lw=1.3)
        ax.text(x + 3.05, 2.3, "E_C", fontsize=8, va="center"); ax.text(x + 3.05, 0.8, "E_V", fontsize=8, va="center")
        if kind == "g":
            _arrow(ax, (x + 1.5, 0.85), (x + 1.5, 2.25), color=G2); ax.text(x + 1.65, 1.5, "heat or light\ngives E ≥ E_g", fontsize=7.6, color=G2)
        elif kind == "r":
            _arrow(ax, (x + 1.5, 2.25), (x + 1.5, 0.85), color=BAD); ax.text(x + 1.65, 1.5, "electron drops,\nfills a hole", fontsize=7.6, color=BAD)
        else:
            ax.plot([x + 1.0, x + 2.0], [1.55, 1.55], color=G3, lw=1.3, ls=":"); ax.text(x + 2.05, 1.55, "trap", fontsize=7.6, color=G3, va="center")
            _arrow(ax, (x + 1.5, 2.25), (x + 1.5, 1.6), color=BAD); _arrow(ax, (x + 1.5, 1.5), (x + 1.5, 0.85), color=BAD)
        ax.add_patch(Circle((x + 1.5, 2.42), 0.1, fc=ACC, ec="none")); ax.add_patch(Circle((x + 1.5, 0.68), 0.1, fc="white", ec=BAD, lw=1.1))
        ax.text(x + 1.5, 0.15, name, ha="center", fontsize=8.6, weight="bold")
    return _svg(fig)


# ================================================================== Part B
def junction():
    with plt.rc_context(RC):
        fig, axs = plt.subplots(4, 1, figsize=(5.6, 5.2), sharex=True, gridspec_kw={"height_ratios": [1.15, 1, 1, 1], "hspace": 0.28})
    xp, xn = -0.4, 1.0     # p side more heavily doped, so narrower
    a = axs[0]; a.axis("off"); a.set_ylim(0, 1)
    a.add_patch(Rectangle((-2, 0.1), 2, 0.8, fc=PCOL, ec=INK)); a.add_patch(Rectangle((0, 0.1), 2, 0.8, fc=NCOL, ec=INK))
    a.add_patch(Rectangle((xp, 0.1), xn - xp, 0.8, fc="white", ec=G1, lw=1.3, ls="--"))
    for y in (0.3, 0.5, 0.7):
        a.text(xp / 2, y, "−", ha="center", va="center", color=BAD, fontsize=11, weight="bold")
        for x in (0.25, 0.65):
            a.text(x, y, "+", ha="center", va="center", color=ACC, fontsize=10, weight="bold")
    a.text(-1.2, 0.5, "p\n(holes)", ha="center", va="center", fontsize=9); a.text(1.5, 0.5, "n\n(electrons)", ha="center", va="center", fontsize=9)
    a.text(0.3, 0.98, "depletion region: fixed ions, no free carriers", ha="center", fontsize=8.3, color=G1)
    x = np.linspace(-2, 2, 800)
    Na, Nd = 2.5, 1.0
    rho = np.where((x > xp) & (x < 0), -Na, np.where((x >= 0) & (x < xn), Nd, 0.0))
    E = np.where((x > xp) & (x < 0), -Na * (x - xp), np.where((x >= 0) & (x < xn), -Nd * (xn - x), 0.0))
    V = -np.cumsum(E) * (x[1] - x[0])
    for a, y, lab_, c in ((axs[1], rho, "charge density ρ", G3), (axs[2], E, "electric field E", BAD), (axs[3], V, "potential V", ACC)):
        a.plot(x, y, color=c, lw=1.6); a.axhline(0, color=LINE, lw=0.7); a.set_yticks([]); a.set_ylabel(lab_, fontsize=8.5)
        a.axvline(xp, color=G1, lw=0.6, ls="--"); a.axvline(xn, color=G1, lw=0.6, ls="--")
    axs[1].text(-0.2, -1.7, "−qN_A", fontsize=8, ha="center", color=G3); axs[1].text(0.5, 0.45, "+qN_D", fontsize=8, ha="center", color=G3)
    axs[2].text(0.05, E.min() * 0.92, "peak at the junction, points n → p", fontsize=8, color=BAD)
    axs[3].annotate("", (1.7, V.max()), (1.7, 0), arrowprops=dict(arrowstyle="<->", color=ACC)); axs[3].text(1.75, V.max() / 2, "V_bi", fontsize=9, color=ACC)
    axs[3].set_xticks([xp, 0, xn]); axs[3].set_xticklabels(["$-x_p$", "0", "$x_n$"]); axs[3].set_xlim(-2, 2.2)
    return _svg(fig)


def diode_iv():
    fig, ax = _fig(5.4, 3.0)
    v = np.linspace(-1.0, 0.9, 600)
    for vk, c, name in ((0.7, ACC, "Si"), (0.3, G1, "Ge")):
        i = 4e-3 * (np.exp((v - vk) / 0.045) )
        ax.plot(v, np.where(i * 1e3 > 22, np.nan, i * 1e3) - (0.4 if name == "Si" else 1.2) * (v < 0), color=c, lw=1.7, label=name)
    ax.set_ylim(-4, 22); ax.set_xlim(-1.05, 1.0)
    ax.axhline(0, color=INK, lw=0.8); ax.axvline(0, color=INK, lw=0.8)
    ax.set_xticks([0.3, 0.7]); ax.set_xticklabels(["0.3 V", "0.7 V"]); ax.set_yticks([])
    ax.text(-0.08, 13, "forward: I rises\nexponentially\nafter the knee", fontsize=8.5, ha="right"); ax.text(-0.95, -3.4, "reverse: only −I_s (nA to μA, drawn enlarged)", fontsize=8.5)
    ax.set_xlabel("V_D"); ax.set_ylabel("I_D"); ax.legend(frameon=False, fontsize=8.5, loc="upper left")
    for s in ("left", "bottom"):
        ax.spines[s].set_visible(False)
    return _svg(fig)


def diode_models():
    with plt.rc_context(RC):
        fig, axs = plt.subplots(1, 3, figsize=(8.4, 2.1))
    for ax, name, pts in ((axs[0], "Ideal: a switch", [(-1, 0), (0, 0), (0, 1)]),
                          (axs[1], "Simplified: switch + 0.7 V", [(-1, 0), (0.55, 0), (0.55, 1)]),
                          (axs[2], "Piecewise-linear: + r_av", [(-1, 0), (0.55, 0), (0.95, 1)])):
        ax.plot(*zip(*pts), color=ACC, lw=2); ax.axhline(0, color=INK, lw=0.7); ax.axvline(0, color=INK, lw=0.7)
        ax.set_xlim(-1, 1.1); ax.set_ylim(-0.15, 1.1); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(name, fontsize=9)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.text(1.05, -0.12, "V_D", fontsize=8, ha="right"); ax.text(0.04, 1.02, "I_D", fontsize=8)
        if pts[1][0]:
            ax.text(0.55, -0.13, "0.7 V", fontsize=8, ha="center", color=BAD)
    axs[2].text(0.98, 0.55, "slope = 1/r_av", fontsize=8, color=MUTED)
    return _svg(fig)


def load_line():
    fig, ax = _fig(5.4, 3.1)
    v = np.linspace(0, 10, 600)
    i_d = 18.5 * np.exp((v - 0.78) / 0.045)
    ax.plot(v, np.where(i_d > 24, np.nan, i_d), color=ACC, lw=1.7, label="diode curve")
    ax.plot([0, 10], [20, 0], color=INK, lw=1.4, label="load line: I_D = (E − V_D)/R")
    ax.plot([0.78], [18.5], "o", color=BAD); ax.annotate("Q-point\n(0.78 V, 18.5 mA)", (0.78, 18.5), (2.2, 19.5), fontsize=8.5, color=BAD,
                                                         arrowprops=dict(arrowstyle="-", color=BAD, lw=0.8))
    ax.set_xlim(0, 10.6); ax.set_ylim(0, 24); ax.set_xticks([0, 2, 4, 6, 8, 10]); ax.set_yticks([0, 5, 10, 15, 20])
    ax.text(0.15, 20.6, "E/R = 20 mA", fontsize=8.5); ax.text(8.2, 2.6, "E = 10 V", fontsize=8.5)
    ax.set_xlabel("V_D (V)"); ax.set_ylabel("I_D (mA)"); ax.legend(frameon=False, fontsize=8.3, loc="center right")
    return _svg(fig)


def ckt_load_line():
    d = _d()
    d += elm.SourceV().endpoints((0, 0), (0, 2.6)).label("E\n10 V")
    d += elm.Diode().endpoints((0, 2.6), (3, 2.6)).label("Si")
    RES(d, (3, 2.6), (3, 0), "R\n0.5 kΩ", loc="bottom"); W(d, (3, 0), (0, 0)); GND(d, (0, 0))
    return _sd(d, 60)


def ckt_two_source():
    """Deck L08 S14: E1 = 10 V, R1 = 4.7k, Si diode, R2 = 2.2k to E2 = -5 V."""
    d = _d()
    d += elm.Dot(open=True).at((0, 2.4)).label("E_1 = +10 V", loc="left")
    RES(d, (0, 2.4), (2.6, 2.4), "R_1  4.7 kΩ\n+ V_1 −")
    d += elm.Diode().endpoints((2.6, 2.4), (5, 2.4)).label("Si")
    DOT(d, (5, 2.4)); W(d, (5, 2.4), (6.4, 2.4)); OUT(d, (6.4, 2.4), "V_o")
    RES(d, (5, 2.4), (5, 0), "R_2  2.2 kΩ\n+ V_2 −", loc="bottom")
    d += elm.Dot(open=True).at((5, 0)).label("E_2 = −5 V", loc="bottom")
    return _sd(d, 85)


def _sine(ax, n=2, amp=1.0, color=INK, lw=1.3, **kw):
    t = np.linspace(0, n, 400 * n)
    ax.plot(t, amp * np.sin(2 * np.pi * t), color=color, lw=lw, **kw)
    return t


def rect_waves():
    with plt.rc_context(RC):
        fig, axs = plt.subplots(3, 1, figsize=(5.2, 3.5), sharex=True, gridspec_kw={"hspace": 0.35})
    t = np.linspace(0, 2, 800); s = np.sin(2 * np.pi * t)
    rows = ((s, "input v_i", INK, None), (np.maximum(s, 0), "half-wave v_o", ACC, 0.318), (np.abs(s), "full-wave v_o", G2, 0.636))
    for ax, (y, name, c, dc) in zip(axs, rows):
        ax.plot(t, y, color=c, lw=1.6); ax.fill_between(t, 0, y, color=c, alpha=0.12); ax.axhline(0, color=LINE, lw=0.7)
        ax.set_yticks([0, 1]); ax.set_yticklabels(["0", "$V_m$"]); ax.set_ylabel(name, fontsize=8.5); ax.set_ylim(-1.15 if dc is None else -0.15, 1.2)
        if dc:
            ax.plot([0, 2], [dc, dc], color=BAD, lw=1.1, ls="--"); ax.text(2.05, dc, f"V_dc = {dc} V_m", fontsize=8.3, color=BAD, va="center")
    axs[2].set_xticks([0, 0.5, 1, 1.5, 2]); axs[2].set_xticklabels(["0", "T/2", "T", "3T/2", "2T"]); axs[2].set_xlim(0, 2.75)
    return _svg(fig)


def ckt_hw():
    d = _d()
    d += elm.SourceSin().endpoints((0, 0), (0, 2.4)).label("v_i")
    d += elm.Diode().endpoints((0, 2.4), (3, 2.4)).label("D")
    RES(d, (3, 2.4), (3, 0), "R", loc="bottom"); W(d, (3, 0), (0, 0))
    W(d, (3, 2.4), (4.2, 2.4)); OUT(d, (4.2, 2.4), "v_o"); DOT(d, (3, 2.4))
    return _sd(d, 52)


def bridge_fig():
    """Bridge rectifier: v_i on the left/right corners, + output at the top corner, − at the bottom."""
    d = _d(unit=2.0)
    L, T, R_, Bm = (0, 1.8), (1.8, 3.6), (3.6, 1.8), (1.8, 0)
    d += elm.Diode().endpoints(L, T).label("D_1"); d += elm.Diode().endpoints(R_, T).label("D_2")
    d += elm.Diode().endpoints(Bm, L).label("D_4", loc="bottom"); d += elm.Diode().endpoints(Bm, R_).label("D_3", loc="bottom")
    d += elm.SourceSin().endpoints((-2.4, 0.6), (-2.4, 3.0)).label("v_i")
    W(d, (-2.4, 3.0), (-1.2, 3.0)); W(d, (-1.2, 3.0), (-1.2, 1.8)); W(d, (-1.2, 1.8), L)
    W(d, (-2.4, 0.6), (-2.4, -1.6)); W(d, (-2.4, -1.6), (4.6, -1.6)); W(d, (4.6, -1.6), (4.6, 1.8)); W(d, (4.6, 1.8), R_)
    W(d, T, (1.8, 4.4)); W(d, (1.8, 4.4), (6.8, 4.4)); RES(d, (6.8, 4.4), (6.8, -0.8), "R")
    W(d, (6.8, -0.8), (1.8, -0.8)); W(d, (1.8, -0.8), Bm)
    for p_ in (L, T, R_, Bm):
        DOT(d, p_)
    TXT(d, (7.6, 3.4), "+", fs=13); TXT(d, (7.6, 1.8), "v_o", fs=12); TXT(d, (7.6, 0.2), "−", fs=13)
    return _sd(d, 92)


def ckt_ct():
    d = _d(unit=2.0)
    x = elm.Transformer(t1=4, t2=8).at((0, 0)).tap(name="ct", pos=4, side="secondary"); d += x
    d += elm.Diode().at(x.s1).right().length(2.4).label("D_1"); p1 = d.here
    d += elm.Diode().at(x.s2).right().length(2.4).label("D_2", loc="bottom"); p2 = d.here
    W(d, p1, (p1[0] + 0.8, p1[1])); W(d, p2, (p2[0] + 0.8, p2[1])); W(d, (p1[0] + 0.8, p1[1]), (p2[0] + 0.8, p2[1]))
    mid = (p1[0] + 0.8, (p1[1] + p2[1]) / 2); DOT(d, mid)
    RES(d, mid, (x.ct[0] + 0.6, x.ct[1]), "R"); W(d, (x.ct[0] + 0.6, x.ct[1]), x.ct)
    TXT(d, (-0.9, (x.p1[1] + x.p2[1]) / 2), "v_i")
    return _sd(d, 80)


def _wave_panel(ax, t, vi, vo, lvl=None, ylab=("v_i", "v_o"), ylim=None):
    ax.plot(t, vi, color=MUTED, lw=1.1, ls="--", label=ylab[0]); ax.plot(t, vo, color=ACC, lw=1.8, label=ylab[1])
    ax.axhline(0, color=LINE, lw=0.7); ax.set_xticks([]); ax.legend(frameon=False, fontsize=8, loc="upper right", ncol=2)
    if ylim:
        ax.set_ylim(*ylim)
    for y, txt in (lvl or []):
        ax.axhline(y, color=BAD, lw=0.8, ls=":"); ax.text(t[-1] * 1.01, y, txt, fontsize=8, color=BAD, va="center")


def clip_series():
    d = _d()
    d += elm.Dot(open=True).at((0, 2.2)).label("v_i", loc="left")
    d += elm.BatteryCell().endpoints((0, 2.2), (1.8, 2.2)).label("5 V\n−  +")
    d += elm.Diode().endpoints((1.8, 2.2), (4.2, 2.2)).label("ideal")
    RES(d, (4.2, 2.2), (4.2, 0), "R", loc="bottom"); DOT(d, (4.2, 2.2)); W(d, (4.2, 2.2), (5.4, 2.2)); OUT(d, (5.4, 2.2), "v_o")
    W(d, (4.2, 0), (0, 0)); d += elm.Dot(open=True).at((0, 0))
    c = _sd(d, 62)
    fig, ax = _fig(3.9, 2.0)
    t = np.linspace(0, 1, 500); vi = 20 * np.sin(2 * np.pi * t); vo = np.where(vi > -5, vi + 5, 0)
    _wave_panel(ax, t, vi, vo, [(25, "25 V"), (-5, "v_i = −5 V:\ndiode switches")], ylim=(-24, 34)); ax.set_yticks([-20, 0, 20])
    return f'<div class="two">{c}{_svg(fig)}</div>'


def clip_parallel():
    d = _d()
    d += elm.Dot(open=True).at((0, 2.6)).label("v_i", loc="left")
    RES(d, (0, 2.6), (2.6, 2.6), "R"); DOT(d, (2.6, 2.6)); W(d, (2.6, 2.6), (4, 2.6)); OUT(d, (4, 2.6), "v_o")
    d += elm.Diode().endpoints((2.6, 1.2), (2.6, 2.6)).label("ideal", loc="bottom")
    d += elm.BatteryCell().endpoints((2.6, 0), (2.6, 1.2)).label("4 V", loc="bottom")
    W(d, (2.6, 0), (0, 0)); d += elm.Dot(open=True).at((0, 0))
    c = _sd(d, 52)
    fig, ax = _fig(3.9, 2.0)
    t = np.linspace(0, 1, 500)
    vi = 16 * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * t)); vo = np.maximum(vi, 4)
    _wave_panel(ax, t, vi, vo, [(4, "4 V"), (16, "16 V")], ylim=(-18, 24)); ax.set_yticks([-16, 0, 16])
    return f'<div class="two">{c}{_svg(fig)}</div>'


def clamper():
    d = _d()
    d += elm.Dot(open=True).at((0, 2.6)).label("v_i", loc="left")
    CAP(d, (0, 2.6), (2.4, 2.6), "C = 0.1 μF\n−  V_C  +"); DOT(d, (2.4, 2.6)); DOT(d, (4.4, 2.6))
    d += elm.Diode().endpoints((2.4, 1.2), (2.4, 2.6)).label("ideal", loc="bottom")
    d += elm.BatteryCell().endpoints((2.4, 0), (2.4, 1.2)).label("5 V", loc="bottom")
    W(d, (2.4, 2.6), (4.4, 2.6)); RES(d, (4.4, 2.6), (4.4, 0), "R\n100 kΩ", loc="bottom"); W(d, (4.4, 2.6), (5.6, 2.6)); OUT(d, (5.6, 2.6), "v_o")
    W(d, (4.4, 0), (0, 0)); d += elm.Dot(open=True).at((0, 0))
    c = _sd(d, 66)
    fig, ax = _fig(3.9, 2.2)
    t = np.linspace(0, 2, 800); sq = np.where((t % 1) < 0.5, 10.0, -20.0)
    _wave_panel(ax, t, sq, sq + 25, [(35, "35 V"), (5, "5 V")], ylim=(-24, 46)); ax.set_yticks([-20, 0, 10])
    return f'<div class="two">{c}{_svg(fig)}</div>'


def doubler():
    d = _d()
    d += elm.SourceSin().endpoints((0, 0), (0, 2.4)).label("V_m sin ωt")
    CAP(d, (0, 2.4), (2.4, 2.4), "C_1\n+ V_m −"); DOT(d, (2.4, 2.4))
    d += elm.Diode().endpoints((2.4, 2.4), (2.4, 0)).label("D_1", loc="bottom")
    d += elm.Diode().endpoints((4.8, 2.4), (2.4, 2.4)).label("D_2")
    CAP(d, (4.8, 2.4), (4.8, 0), "C_2\n$2V_m$", loc="bottom"); W(d, (4.8, 0), (0, 0))
    return _sd(d, 64)


def zener_iv():
    fig, ax = _fig(4.6, 2.7)
    v = np.linspace(-6.2, 0.8, 700)
    i = 1.0 * np.exp((v - 0.7) / 0.05) - 1.0 * np.exp((-v - 5.6) / 0.07)
    ax.plot(v, np.clip(i, -22, 22), color=ACC, lw=1.7)
    ax.axhline(0, color=INK, lw=0.8); ax.axvline(0, color=INK, lw=0.8); ax.set_ylim(-24, 24); ax.set_xlim(-7, 1.6)
    ax.set_xticks([-5.6, 0.7]); ax.set_xticklabels(["$-V_Z$", "0.7 V"]); ax.set_yticks([])
    ax.text(-5.3, -14, "breakdown: V stays ≈ V_Z\nwhile I changes a lot\n(the regulator region)", fontsize=8.3, color=BAD)
    ax.text(-3.8, 2.5, "reverse: ≈ 0", fontsize=8.3, color=MUTED); ax.set_xlabel("V"); ax.set_ylabel("I")
    for s in ("left", "bottom"):
        ax.spines[s].set_visible(False)
    return _svg(fig)


def zener_reg():
    d = _d()
    d += elm.SourceV().endpoints((0, 0), (0, 2.6)).label("V_i\n16 V")
    RES(d, (0, 2.6), (2.8, 2.6), "R = 1 kΩ\nI_R →"); DOT(d, (2.8, 2.6))
    d += elm.Zener().endpoints((2.8, 0), (2.8, 2.6)).label("V_Z = 10 V\nI_Z ↓", loc="bottom")
    W(d, (2.8, 2.6), (5.2, 2.6)); RES(d, (5.2, 2.6), (5.2, 0), "R_L\nI_L ↓", loc="bottom"); W(d, (5.2, 0), (0, 0)); DOT(d, (2.8, 0))
    return _sd(d, 70)


def tunnel_iv():
    fig, ax = _fig(4.4, 2.5)
    v = np.linspace(0, 0.62, 400)
    i = 4.2 * (v / 0.065) * np.exp(1 - v / 0.065) / 4.2 + 0.02 * (np.exp(v / 0.11) - 1)
    ax.plot(v, i, color=ACC, lw=1.8)
    ip, iv_ = i[np.argmax(i[:120])], i[120 + np.argmin(i[120:300])]
    vp, vv = v[np.argmax(i[:120])], v[120 + np.argmin(i[120:300])]
    ax.plot([vp, vv], [ip, iv_], "o", color=BAD, ms=4)
    ax.text(vp - 0.005, ip + 0.04, "peak (V_p, I_p)", ha="right", fontsize=8.3, color=BAD); ax.text(vv - 0.02, iv_ - 0.16, "valley (V_v, I_v)", fontsize=8.3, color=BAD)
    ax.axvspan(vp, vv, color=G1, alpha=0.12); ax.text((vp + vv) / 2, 1.2, "negative resistance:\nV ↑ but I ↓", ha="center", va="top", fontsize=8.2, color=G1)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlabel("forward voltage V"); ax.set_ylabel("I"); ax.set_ylim(0, 1.25); ax.set_xlim(-0.12, 0.64)
    return _svg(fig)


def special_symbols():
    d = _d(unit=2.2)
    for i, (el, name) in enumerate(((elm.Diode, "pn diode"), (elm.Zener, "Zener"), (elm.Schottky, "Schottky"), (elm.LED, "LED"),
                                    (elm.Photodiode, "photodiode"), (elm.DiodeTunnel, "tunnel"), (elm.Varactor, "varactor"))):
        d += el().at((i * 2.7, 0)).right().label(name, loc="bottom")
    return _sd(d, 165)
