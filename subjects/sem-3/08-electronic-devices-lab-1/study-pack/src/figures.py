"""All figures for the ECE2130 lab pack. Every function returns an SVG string.

Circuits: schemdraw, redrawn from the lab manual (same values).
Plots: matplotlib, from the LTspice runs in sim/out/*.npz (python sim/sims.py).
"""
import io
from pathlib import Path

import numpy as np
import schemdraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

schemdraw.use("svg")
SIM = Path(__file__).resolve().parent / "sim" / "out"
FONT = "Arial"
INK = "#1f2937"
ACCENT = "#1d4ed8"
WARN = "#b91c1c"
GOOD = "#15803d"
MUTED = "#6b7280"
ORANGE = "#c2410c"

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"], "mathtext.fontset": "dejavusans", "font.size": 10,
    "axes.edgecolor": "#9ca3af", "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#374151", "ytick.color": "#374151", "axes.labelcolor": "#111827",
    "svg.fonttype": "path", "axes.grid": True, "grid.color": "#e5e7eb", "grid.linewidth": 0.6,
})


import re as _re
from matplotlib.text import Text as _Text

_SUB = _re.compile(r"(?<![\w$])([A-Za-z]+)_([A-Za-z0-9]+)")


def _sub(s):
    """'V_CE' -> '$V_{CE}$' so labels show real subscripts (no raw underscores)."""
    return s if "$" in s else _SUB.sub(r"$\1_{\2}$", s)


_orig_label = elm.Element.label


def _label(self, label, *a, **k):
    return _orig_label(self, _sub(label) if isinstance(label, str) else label, *a, **k)


elm.Element.label = _label


def L(name):
    return np.load(SIM / f"{name}.npz")


def _d(unit=2.6, fs=12):
    d = schemdraw.Drawing(show=False)
    d.config(unit=unit, fontsize=fs, font=FONT, color=INK, lw=1.5)
    return d


def _svg(d):
    return d.get_imagedata("svg").decode()


def _plt(fig):
    for t in fig.findobj(_Text):
        t.set_text(_sub(t.get_text()))
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    s = buf.getvalue()
    return s[s.index("<svg"):]


# ------------------------------------------------------------------ drawing helpers
def W(d, a, b):
    d += elm.Line().endpoints(a, b)


def RES(d, a, b, lab, loc=None):
    e = elm.Resistor().endpoints(a, b)
    d += e.label(lab, loc=loc) if loc else e.label(lab)


def CAP(d, a, b, lab, loc=None, color=None):
    e = elm.Capacitor().endpoints(a, b)
    if color:
        e = e.color(color)
    d += e.label(lab, loc=loc) if loc else e.label(lab)


def DOT(d, p, open_=False):
    d += elm.Dot(open=open_).at(p)


def TXT(d, p, s, color=INK, fs=12, halign="center"):
    d += elm.Label().at(p).label(s, color=color, fontsize=fs, halign=halign)


def GND(d, p):
    d += elm.Ground().at(p)


def OUT(d, p, s):
    d += elm.Dot(open=True).at(p).label(s, loc="right")


# ------------------------------------------------------------------ concept figures
def dso_screen():
    fig, ax = plt.subplots(figsize=(5.2, 3.5))
    t = np.linspace(0, 10, 800)
    ax.plot(t, 2 * np.sin(2 * np.pi * t / 4), color=ACCENT, lw=2.2)
    ax.set_xlim(0, 10); ax.set_ylim(-4, 4)
    ax.set_xticks(range(0, 11)); ax.set_yticks(range(-4, 5))
    ax.set_xticklabels([]); ax.set_yticklabels([])
    ax.grid(True, color="#9ca3af", lw=0.6)
    ax.set_facecolor("#f8fafc")
    ax.annotate("", xy=(1, 2), xytext=(1, -2), arrowprops=dict(arrowstyle="<->", color=WARN, lw=1.5))
    ax.text(1.15, 0.3, "4 div\npeak-to-peak", color=WARN, fontsize=9)
    ax.annotate("", xy=(5, -3.3), xytext=(9, -3.3), arrowprops=dict(arrowstyle="<->", color=GOOD, lw=1.5))
    ax.text(6.2, -3.05, "4 div = one period T", color=GOOD, fontsize=9)
    ax.set_xlabel("horizontal: TIME/DIV knob (e.g. 0.25 ms/div)")
    ax.set_ylabel("vertical: VOLTS/DIV knob\n(e.g. 2 V/div)")
    return _plt(fig)


def diode_iv():
    v = np.linspace(-7.5, 0.85, 1200)
    i = np.where(v > 0, 1e-14 * (np.exp(v / 0.026) - 1), 0) * 1e3
    i = np.clip(i, -40, 40)
    vz = 6.2
    rev = np.where(v < -vz, (v + vz) / 0.02, 0)
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot(v, np.clip(i + rev, -40, 40), color=ACCENT, lw=2.2)
    ax.axhline(0, color=MUTED, lw=0.8); ax.axvline(0, color=MUTED, lw=0.8)
    ax.set_xlim(-7.5, 1.2); ax.set_ylim(-40, 40)
    ax.set_xlabel("V across diode (V)   [anode − cathode]"); ax.set_ylabel("I (mA)")
    ax.annotate("forward: conducts above\n≈ 0.7 V (silicon)", xy=(0.75, 25), xytext=(-3.6, 25), fontsize=9,
                arrowprops=dict(arrowstyle="->", color=MUTED))
    ax.annotate("reverse, below V_Z:\nonly µA leakage (≈ open)", xy=(-3, 0), xytext=(-5.2, 12), fontsize=9,
                arrowprops=dict(arrowstyle="->", color=MUTED))
    ax.annotate("breakdown at −V_Z: voltage stays\n≈ V_Z while current changes a lot", xy=(-6.45, -15),
                xytext=(-5.6, -32), fontsize=9, color=WARN, arrowprops=dict(arrowstyle="->", color=WARN))
    return _plt(fig)


def bandwidth_concept():
    f = np.logspace(1, 7, 600)
    g = 36 / np.sqrt(1 + (300 / f) ** 2) / np.sqrt(1 + (f / 7e5) ** 2)
    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    ax.semilogx(f, g, color=ACCENT, lw=2.2)
    ax.axhline(36, color=MUTED, ls=":", lw=1); ax.axhline(36 * 0.707, color=WARN, ls="--", lw=1.2)
    ax.text(12, 37, "A_max (midband)", fontsize=9, color=MUTED)
    ax.text(12, 26.5, "0.707 × A_max  (= −3 dB)", fontsize=9, color=WARN)
    for x, lab in [(300, "f_L"), (7e5, "f_H")]:
        ax.axvline(x, color=WARN, lw=1, ls="--"); ax.text(x * 1.1, 3, lab, color=WARN, fontsize=10)
    ax.annotate("", xy=(300, 14), xytext=(7e5, 14), arrowprops=dict(arrowstyle="<->", color=GOOD))
    ax.text(9e3, 15, "bandwidth = f_H − f_L", color=GOOD, ha="center", fontsize=9)
    ax.text(30, 8, "coupling &\nbypass C's\nlose the signal", fontsize=8, color=MUTED, ha="center")
    ax.text(3e6, 8, "transistor's\ninternal C's", fontsize=8, color=MUTED, ha="center")
    ax.set_xlabel("frequency (Hz), log scale"); ax.set_ylabel("voltage gain V_o / V_in")
    ax.set_ylim(0, 42)
    return _plt(fig)


# ------------------------------------------------------------------ Exp 1
def exp01_circuit():
    d = _d()
    d += elm.SourceV().endpoints((0, 0), (0, 3)).label("V_S\n0–15 V", loc="bottom")
    RES(d, (0, 3), (3, 3), "1 kΩ")
    d += elm.MeterA().endpoints((3, 3), (5.6, 3)).label("ammeter\nI_Z")
    d += elm.Zener().endpoints((5.6, 0), (5.6, 3)).label("Zener\n(cathode up)", loc="bottom")
    W(d, (5.6, 3), (9.2, 3)); d += elm.MeterV().endpoints((9.2, 3), (9.2, 0)).label("voltmeter:\nV_Z", loc="bottom")
    W(d, (9.2, 0), (0, 0)); DOT(d, (5.6, 3)); DOT(d, (5.6, 0))
    return _svg(d)


def exp01_plot():
    s = L("exp01"); vz, iz = s["vz"], s["iz"]
    fig, ax = plt.subplots(figsize=(6, 3.4))
    ax.plot(vz, iz, color=ACCENT, lw=2.2, marker="")
    for k in range(0, 16):
        j = np.argmin(abs(s["vs"] - k)); ax.plot(vz[j], iz[j], "o", color=ACCENT, ms=4)
    v2, v8 = np.interp(2, iz, vz), np.interp(8, iz, vz)
    ax.set_xlim(0, 7); ax.set_xlabel("V_Z (V)  [reverse voltage across zener]")
    ax.set_ylabel("I_Z (mA)")
    ax.annotate("knee ≈ 6.2 V", xy=(6.15, 0.3), xytext=(3.6, 1.6), fontsize=9, arrowprops=dict(arrowstyle="->", color=MUTED))
    ax.text(0.3, 7.6, "dots = the manual's 1 V steps of V_S", fontsize=8.5, color=MUTED)
    ax2 = ax.inset_axes([0.08, 0.35, 0.42, 0.42])
    ax2.plot(vz, iz, color=ACCENT, lw=1.8); ax2.set_xlim(6.15, 6.42); ax2.set_ylim(0, 9)
    ax2.plot([v2, v8, v8], [2, 2, 8], color=WARN, lw=1.3)
    ax2.text(v8 - 0.005, 4.5, "ΔI_Z\n= 6 mA", color=WARN, fontsize=7.5, ha="right")
    ax2.text(v2, 0.6, f"ΔV_Z = {v8 - v2:.3f} V", color=WARN, fontsize=7.5)
    ax2.tick_params(labelsize=7); ax2.set_title("zoom: r_z = ΔV_Z / ΔI_Z", fontsize=7.5)
    return _plt(fig)


# ------------------------------------------------------------------ Exp 2
def _zreg(src_lab, load_lab):
    d = _d()
    d += elm.SourceV().endpoints((0, 0), (0, 3)).label(src_lab, loc="bottom")
    RES(d, (0, 3), (3, 3), "R1 1 kΩ")
    d += elm.Zener().endpoints((3, 0), (3, 3)).label("D1\nBZX84C6V2L\n(6.2 V)", loc="bottom")
    W(d, (3, 3), (5.6, 3)); RES(d, (5.6, 3), (5.6, 0), load_lab, loc="bottom")
    W(d, (5.6, 0), (0, 0)); DOT(d, (3, 3)); DOT(d, (3, 0)); GND(d, (3, 0))
    TXT(d, (4.3, 3.45), "V_o", color=ACCENT)
    return _svg(d)


def exp02_line_circuit():
    return _zreg("V1\n.dc V1 0 20 1", "R2 1 kΩ")


def exp02_load_circuit():
    return _zreg("V1 = 20 V", "R2 {R}\n.step param\nR 100 1100 100")


def exp02_line_plot():
    s = L("exp02a")
    fig, ax = plt.subplots(figsize=(5.8, 3.1))
    ax.plot(s["vin"], s["vo"], "o-", color=ACCENT, ms=3.5, lw=1.8)
    ax.axvspan(14, 17, color="#fef3c7", alpha=0.8)
    ax.text(15.5, 3.2, "14–17 V:\nregulated", ha="center", fontsize=9)
    ax.text(3, 4.6, "below ≈ 12 V: zener OFF,\nV_o = V_in/2 (divider)", fontsize=9, color=MUTED)
    ax.set_xlabel("V_in (V)"); ax.set_ylabel("V_o (V)"); ax.set_ylim(0, 7.2)
    return _plt(fig)


def exp02_load_plot():
    import json
    r = json.loads((SIM / "results.json").read_text())["exp02_load"]
    fig, ax = plt.subplots(figsize=(5.8, 3.0))
    ax.plot(r["R"], r["vo"], "o-", color=ACCENT, ms=4, lw=1.8)
    ax.axhline(r["VNL"], color=GOOD, ls="--", lw=1)
    ax.text(150, r["VNL"] + 0.12, f"no load: V_NL = {r['VNL']:.3f} V", color=GOOD, fontsize=9)
    ax.text(480, 2.6, "R_L too small: load steals the\ncurrent, zener drops out", fontsize=9, color=WARN)
    ax.set_xlabel("R_L (Ω)"); ax.set_ylabel("V_o (V)"); ax.set_ylim(0, 7.3)
    return _plt(fig)


# ------------------------------------------------------------------ Exp 3
def _clip(pos):
    d = _d()
    d += elm.SourceSin().endpoints((0, 0), (0, 3)).label("V_i\n10 V peak\n1 kHz", loc="bottom")
    RES(d, (0, 3), (3, 3), "1 kΩ")
    if pos:
        d += elm.Diode().endpoints((3, 3), (3, 1.4)).label("1N4007", loc="bottom")
        d += elm.SourceV().endpoints((3, 0), (3, 1.4)).label("2 V", loc="bottom")
    else:
        d += elm.Diode().endpoints((3, 1.4), (3, 3)).label("1N4007", loc="bottom")
        d += elm.SourceV().endpoints((3, 1.4), (3, 0)).label("2 V", loc="bottom")
    W(d, (3, 3), (5, 3)); W(d, (3, 0), (5, 0)); W(d, (0, 0), (3, 0))
    OUT(d, (5, 3), "V_o → DSO"); OUT(d, (5, 0), "DSO ground")
    DOT(d, (3, 3))
    return _svg(d)


def exp03a_circuit():
    return _clip(True)


def exp03b_circuit():
    return _clip(False)


def exp03_wave():
    fig, axs = plt.subplots(1, 2, figsize=(7.4, 2.8), sharey=True)
    for ax, tag, title in [(axs[0], "a", "Fig 3.1(a): clips the top"), (axs[1], "b", "Fig 3.2(a): clips the bottom")]:
        s = L(f"exp03{tag}"); t = s["t"] * 1e3
        ax.plot(t, s["vin"], color=MUTED, lw=1.2, ls="--", label="V_i")
        ax.plot(t, s["vo"], color=ACCENT, lw=2.2, label="V_o")
        lv = 2.66 if tag == "a" else -2.66
        ax.axhline(lv, color=WARN, lw=0.9, ls=":")
        ax.text(2.05, lv + (0.6 if tag == "a" else -1.6), f"{lv:+.2f} V", color=WARN, fontsize=9)
        ax.set_title(title, fontsize=10); ax.set_xlabel("time (ms)")
    axs[0].set_ylabel("volts"); axs[0].legend(fontsize=8, loc="lower left")
    return _plt(fig)


# ------------------------------------------------------------------ Exp 4
def exp04_circuit():
    d = _d()
    d += elm.SourceSin().endpoints((0, 0), (0, 3)).label("V1\nSINE(0 5 1k)", loc="bottom")
    CAP(d, (0, 3), (3, 3), "C1 0.01 µF")
    d += elm.Diode().endpoints((3, 3), (3, 0)).label("D1\n1N914", loc="bottom")
    W(d, (3, 3), (5.4, 3)); RES(d, (5.4, 3), (5.4, 0), "R1\n1 MΩ", loc="bottom"); W(d, (5.4, 0), (0, 0))
    DOT(d, (3, 3)); DOT(d, (3, 0)); GND(d, (3, 0)); TXT(d, (4.2, 3.45), "V_o", color=ACCENT)
    return _svg(d)


def exp04_wave():
    s = L("exp04"); t = s["t"] * 1e3
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    ax.plot(t, s["vin"], color=MUTED, lw=1.2, ls="--", label="V_in (±5 V)")
    ax.plot(t, s["vo"], color=ACCENT, lw=2.2, label="V_o")
    ax.axhline(0.48, color=WARN, lw=0.9, ls=":"); ax.axhline(-9.39, color=WARN, lw=0.9, ls=":")
    ax.text(5.05, 0.3, "+0.48 V", color=WARN, fontsize=9); ax.text(5.05, -9.6, "−9.39 V", color=WARN, fontsize=9)
    ax.set_xlabel("time (ms)"); ax.set_ylabel("volts"); ax.legend(fontsize=8, loc="lower left")
    ax.set_xlim(0, 5.6)
    return _plt(fig)


# ------------------------------------------------------------------ Exp 5
def exp05_circuit():
    d = _d()
    d += elm.SourceV().endpoints((0, 0), (0, 3)).label("V_be", loc="bottom")
    RES(d, (0, 3), (3, 3), "R1 2 kΩ"); W(d, (3, 3), (4, 3))
    q = elm.BjtNpn(circle=True).anchor("base").at((4, 3)).label("Q1\nBC547B", loc="right"); d += q
    W(d, q.collector, (q.collector.x, 5)); RES(d, (q.collector.x, 5), (8, 5), "R2 62 kΩ")
    d += elm.SourceV().endpoints((8, 0), (8, 5)).label("V_ce\n10 V", loc="bottom")
    W(d, q.emitter, (q.emitter.x, 0)); W(d, (0, 0), (8, 0)); GND(d, (q.emitter.x, 0))
    TXT(d, (3.5, 3.4), "base", color=ACCENT, fs=10); TXT(d, (q.collector.x - 0.75, 4.4), "collector", color=ACCENT, fs=10)
    return _svg(d)


def exp05_in_plot():
    s = L("exp05in2")
    fig, ax = plt.subplots(figsize=(5.8, 3.2))
    ax.plot(s["vb0"], s["ib0"], color=MUTED, lw=2, label="V_CE = 0 V")
    ax.plot(s["vb5"], s["ib5"], color=ACCENT, lw=2.2, label="V_CE = 5 V")
    v10, v30 = np.interp(10, s["ib5"], s["vb5"]), np.interp(30, s["ib5"], s["vb5"])
    ax.plot([v10, v30, v30], [10, 10, 30], color=WARN, lw=1.3)
    ax.text(v30 + 0.004, 18, "ΔI_B = 20 µA", color=WARN, fontsize=9)
    ax.text(v10 - 0.075, 12, f"ΔV_BE = {1000 * (v30 - v10):.1f} mV", color=WARN, fontsize=9)
    ax.set_xlim(0.45, 0.75); ax.set_ylim(0, 60)
    ax.set_xlabel("V_BE (V)"); ax.set_ylabel("I_B (µA)"); ax.legend(fontsize=8, loc="upper left")
    return _plt(fig)


def exp05_out_plot():
    s = L("exp05out")
    fig, ax = plt.subplots(figsize=(6.2, 3.5))
    cols = [MUTED, ACCENT, GOOD, ORANGE]
    for k, ib in enumerate([0, 20, 40, 60]):
        ax.plot(s[f"vce{k}"], s[f"ic{k}"], color=cols[k], lw=2)
        ax.text(12.1, s[f"ic{k}"][-1], f"I_B = {ib} µA", fontsize=8.5, color=cols[k], va="center")
    ax.axvspan(0, 0.3, color="#fee2e2", alpha=0.7); ax.text(0.35, 17.5, "saturation\n(V_CE < 0.3 V)", fontsize=8, color=WARN)
    ax.text(6, 1.0, "cut-off: I_B = 0 → I_C ≈ 0", fontsize=8, color=MUTED)
    ax.text(4.5, 13.3, "active region: flat lines, I_C ≈ h_fe × I_B", fontsize=8.5, color=INK)
    ax.plot([5, 5], [np.interp(5, s["vce1"], s["ic1"]), np.interp(5, s["vce2"], s["ic2"])], color=WARN, lw=1.6)
    ax.text(5.15, 8.3, "ΔI_C → h_fe", color=WARN, fontsize=8.5)
    ax.plot([4, 10], [np.interp(4, s["vce1"], s["ic1"]), np.interp(10, s["vce1"], s["ic1"])], color=ORANGE, lw=0)
    ax.annotate("slope → h_oe", xy=(9, np.interp(9, s["vce1"], s["ic1"])), xytext=(8.5, 3.0), fontsize=8.5,
                color=ORANGE, arrowprops=dict(arrowstyle="->", color=ORANGE))
    ax.set_xlim(0, 14.5); ax.set_ylim(-0.5, 19.5)
    ax.set_xlabel("V_CE (V)"); ax.set_ylabel("I_C (mA)")
    return _plt(fig)


# ------------------------------------------------------------------ CE stage (Exp 6, 8, additional)
def _ce_stage(d, ox, v, src=True, cc=True, load=None, bypass_note=None, rail=None, bjt="BC547"):
    """Voltage-divider-biased CE stage. Returns dict of key points."""
    yb, yr = 3, 6.2
    xin, xb = ox + 2.4, ox + 4.4
    if src:
        d += elm.SourceSin().endpoints((ox, 0), (ox, yb)).label(v["Vs"], loc="bottom")
        RES(d, (ox, yb), (xin, yb), v["Rs"])
    CAP(d, (xin, yb), (xb, yb), v["Cin"])
    RES(d, (xb, yr), (xb, yb), v["R1"]); RES(d, (xb, yb), (xb, 0), v["R2"], loc="bottom")
    W(d, (xb, yb), (xb + 1, yb)); DOT(d, (xb, yb))
    q = elm.BjtNpn(circle=True).anchor("base").at((xb + 1, yb)).label(bjt, loc="right"); d += q
    xc = q.collector.x
    RES(d, (xc, yr), (xc, 4.5), v["Rc"]); W(d, (xc, 4.5), q.collector)
    RES(d, q.emitter, (xc, 0), v["Re"], loc="bottom")
    W(d, q.emitter, (xc + 2.3, q.emitter.y)); DOT(d, q.emitter)
    CAP(d, (xc + 2.3, q.emitter.y), (xc + 2.3, 0), v["Ce"], loc="bottom", color=WARN if bypass_note else None)
    if bypass_note:
        TXT(d, (xc + 2.3, -0.9), bypass_note, color=WARN, fs=10)
    W(d, (xb, yr), (xc, yr)); DOT(d, (xc, 4.5))
    pts = {"c": (xc, 4.5), "in": (xin, yb), "rail_l": (xb, yr), "rail_r": (xc, yr), "x_end": xc + 2.3}
    if cc:
        xo = xc + 4.0
        CAP(d, (xc, 4.5), (xo, 4.5), v["Cc"])
        if load:
            RES(d, (xo, 4.5), (xo, 0), load, loc="bottom"); DOT(d, (xo, 4.5))
            W(d, (xo, 4.5), (xo + 1, 4.5)); OUT(d, (xo + 1, 4.5), "V_o")
            pts["x_end"] = xo
        else:
            OUT(d, (xo, 4.5), "V_o → CRO")
            pts["x_end"] = max(pts["x_end"], xo)
    if rail:
        TXT(d, ((xb + xc) / 2, yr + 0.45), rail, color=WARN)
    return pts


CE6 = {"Vs": "V_s", "Rs": "2.2 kΩ", "Cin": "10 µF", "R1": "25 kΩ", "R2": "8.2 kΩ", "Rc": "560 Ω",
       "Re": "560 Ω", "Ce": "47 µF", "Cc": "10 µF"}


def exp06_circuit():
    d = _d(unit=2.2, fs=11)
    p = _ce_stage(d, 0, CE6, rail="+15 V")
    W(d, (0, 0), (p["x_end"], 0)); GND(d, (4.4, 0))
    return _svg(d)


def exp06_freq():
    import json
    s = L("exp06ac"); r = json.loads((SIM / "results.json").read_text())["exp06"]
    fig, ax = plt.subplots(figsize=(6.2, 3.1))
    db = 20 * np.log10(s["g"])
    ax.semilogx(s["f"], db, color=ACCENT, lw=2.2)
    top = r["AmaxdB"]
    ax.axhline(top - 3, color=WARN, ls="--", lw=1)
    for x, lab in [(r["fL"], f"f_L ≈ {r['fL']:.0f} Hz"), (r["fH"], f"f_H ≈ {r['fH'] / 1e3:.0f} kHz")]:
        ax.axvline(x, color=WARN, lw=1, ls="--"); ax.text(x * 1.12, top - 14, lab, color=WARN, fontsize=9)
    ax.text(15, top + 0.8, f"midband {top:.1f} dB (gain {r['Amax']:.0f})", fontsize=9, color=INK)
    ax.text(15, top - 2.6, "−3 dB line", fontsize=8.5, color=WARN)
    ax.set_xlim(10, 1e8); ax.set_ylim(top - 30, top + 4)
    ax.set_xlabel("frequency (Hz)"); ax.set_ylabel("gain (dB) = 20 log(V_o / V_s)")
    return _plt(fig)


def exp06_clip():
    fig, axs = plt.subplots(1, 2, figsize=(7.4, 2.7))
    for ax, amp, title in [(axs[0], 20, "V_s = 20 mV: clean sine"), (axs[1], 500, "V_s = 500 mV: clipped")]:
        s = L(f"exp06tr{amp}")
        t = (s["t"] - s["t"][0]) * 1e3
        ax.plot(t, s["vo"], color=ACCENT if amp == 20 else WARN, lw=2)
        ax.set_title(title, fontsize=10); ax.set_xlabel("time (ms)")
    axs[0].set_ylabel("V_o (V)")
    return _plt(fig)


# ------------------------------------------------------------------ Exp 7
def exp07_circuit():
    d = _d()
    d += elm.SourceSin().endpoints((0, 0), (0, 3)).label("V2\n0.5 V\n1 kHz", loc="bottom")
    CAP(d, (0, 3), (2.6, 3), "C2 10 µF")
    RES(d, (2.6, 6.2), (2.6, 3), "R2\n33 kΩ", loc="bottom"); RES(d, (2.6, 3), (2.6, 0), "R3\n3.3 kΩ", loc="bottom")
    W(d, (2.6, 3), (4.4, 3)); DOT(d, (2.6, 3))
    q = elm.BjtNpn(circle=True).anchor("base").at((4.4, 3)); d += q
    TXT(d, (q.collector.x + 0.3, 4.3), "Q1 BC547B", fs=11, halign="left")
    W(d, q.collector, (q.collector.x, 6.2)); W(d, (2.6, 6.2), (q.collector.x, 6.2))
    TXT(d, (3.8, 6.65), "+15 V", color=WARN)
    RES(d, q.emitter, (q.emitter.x, 0), "R4\n2 kΩ", loc="bottom"); DOT(d, q.emitter)
    CAP(d, q.emitter, (q.emitter.x + 2.6, q.emitter.y), "C1 10 µF", loc="bottom"); OUT(d, (q.emitter.x + 2.6, q.emitter.y), "V_out")
    W(d, (0, 0), (q.emitter.x, 0)); GND(d, (2.6, 0))
    return _svg(d)


def exp07_tr():
    s = L("exp07tr"); t = s["t"] * 1e3; m = t > 6
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    ax.plot(t[m], s["vin"][m], color=MUTED, lw=1.5, ls="--", label="V_in (0.5 V peak)")
    ax.plot(t[m], s["vo"][m], color=ACCENT, lw=2.2, label="V_out")
    ax.set_xlabel("time (ms)"); ax.set_ylabel("volts"); ax.legend(fontsize=8, loc="lower right")
    return _plt(fig)


def exp07_freq():
    s = L("exp07ac"); m = (s["f"] >= 100) & (s["f"] <= 1e7)
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    ax.semilogx(s["f"][m], s["g"][m], color=ACCENT, lw=2.2)
    ax.set_ylim(0, 1.2); ax.axhline(0.966, color=MUTED, lw=0.8, ls=":")
    ax.text(150, 1.03, "gain ≈ 0.97, flat over the whole 200 Hz – 1 MHz sweep", fontsize=9)
    ax.set_xlabel("frequency (Hz)"); ax.set_ylabel("V_out / V_in")
    return _plt(fig)


# ------------------------------------------------------------------ Exp 8
def exp08_circuit():
    d = _d(unit=2.2, fs=11)
    v = {"Vs": "V2\nAC 1 V", "Rs": "R6 2.2 kΩ", "Cin": "C2 6 µF", "R1": "R2\n68 kΩ", "R2": "R3\n22 kΩ",
         "Rc": "R1\n4.7 kΩ", "Re": "R4\n2.2 kΩ", "Ce": "C1 47 µF", "Cc": "C3 0.33 µF"}
    p = _ce_stage(d, 0, v, load="R5\n47 kΩ", bypass_note="remove C1 → negative feedback ON", rail="+15 V", bjt="2N2222")
    W(d, (0, 0), (p["x_end"], 0)); GND(d, (4.4, 0))
    return _svg(d)


def exp08_freq():
    import json
    r = json.loads((SIM / "results.json").read_text())["exp08"]
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    for tag, col, lab in [("with_Ce", ACCENT, "with C1 (no feedback)"), ("no_Ce", WARN, "C1 removed (negative feedback)")]:
        s = L(f"exp08{tag}"); m = s["f"] <= 1e8
        ax.semilogx(s["f"][m], 20 * np.log10(s["g"][m]), color=col, lw=2.2, label=lab)
        for x in (r[tag]["fL"], r[tag]["fH"]):
            ax.plot([x], [r[tag]["AmaxdB"] - 3], "o", color=col, ms=5)
    ax.set_xlabel("frequency (Hz)"); ax.set_ylabel("gain (dB)"); ax.legend(fontsize=8.5, loc="center left")
    ax.set_ylim(-20, 48)
    ax.text(2, 44, "dots = −3 dB points (f_L, f_H)", fontsize=8.5, color=MUTED)
    return _plt(fig)


# ------------------------------------------------------------------ Exp 9
def jfet_structure():
    fig, ax = plt.subplots(figsize=(3.6, 3.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.add_patch(plt.Rectangle((3, 1), 4, 8, fc="#dbeafe", ec=INK))
    for x in (2.2, 6.8):
        ax.add_patch(plt.Rectangle((x, 3.5), 1.0, 3, fc="#fecaca", ec=INK))
    for x in (3.2, 5.7):
        ax.add_patch(plt.Polygon([(x, 3.3), (x + 1.1 * (1 if x < 5 else 0), 3.3), (x + 1.1 * (1 if x < 5 else 0), 6.7), (x, 6.7)] if x < 5 else
                                 [(x, 3.3), (6.8, 3.3), (6.8, 6.7), (x, 6.7)], fc="none", ec=WARN, hatch="///", lw=0))
    ax.text(5, 9.4, "Drain (D)", ha="center"); ax.text(5, 0.25, "Source (S)", ha="center")
    ax.text(5, 5, "n\nchannel", ha="center", va="center", fontsize=9)
    ax.text(2.7, 5, "p", ha="center", va="center", color=WARN); ax.text(7.3, 5, "p", ha="center", va="center", color=WARN)
    ax.plot([0.5, 2.2], [5, 5], color=INK); ax.plot([7.8, 9.5], [5, 5], color=INK); ax.plot([0.5, 0.5], [5, 2], color=INK)
    ax.plot([9.5, 9.5], [5, 2], color=INK); ax.plot([0.5, 9.5], [2, 2], color=INK, ls="--", lw=0.6)
    ax.text(0.2, 1.2, "Gate (G): both p regions", fontsize=9)
    ax.text(5, 7.4, "hatched = depletion\n(no carriers)", ha="center", fontsize=8, color=WARN)
    return _plt(fig)


def exp09_circuit():
    d = _d()
    d += elm.SourceV().endpoints((0, 0), (0, 3)).label("V_gs\n0 → −3 V", loc="bottom")
    W(d, (0, 3), (2.5, 3))
    j = elm.JFetN(circle=True).reverse().anchor("gate").at((2.5, 3)).label("J1\n2N3819", loc="right"); d += j
    W(d, j.drain, (j.drain.x, 5)); W(d, (j.drain.x, 5), (6, 5))
    d += elm.SourceV().endpoints((6, 0), (6, 5)).label("V_ds\n0 → 16 V", loc="bottom")
    W(d, j.source, (j.source.x, 0)); W(d, (0, 0), (6, 0)); GND(d, (j.source.x, 0))
    return _svg(d)


def exp09_out():
    s = L("exp09out")
    fig, ax = plt.subplots(figsize=(6.2, 3.4))
    cols = [ACCENT, GOOD, ORANGE, MUTED]
    for k, vg in enumerate([0, -1, -2, -3]):
        m = s[f"vds{k}"] <= 10
        ax.plot(s[f"vds{k}"][m], s[f"id{k}"][m], color=cols[k], lw=2.1)
        ax.text(10.15, s[f"id{k}"][m][-1], f"V_GS = {vg} V", color=cols[k], fontsize=8.5, va="center")
    ax.axvline(3, color=WARN, lw=0.9, ls="--"); ax.text(3.1, 1.9, "pinch-off\n(V_DS ≈ |V_P| at V_GS = 0)", color=WARN, fontsize=8.5)
    ax.text(0.15, 12.6, "ohmic region:\nacts like a resistor", fontsize=8, color=MUTED)
    ax.text(5.5, 12.6, "saturation: I_D ≈ constant", fontsize=8.5)
    ax.set_xlim(0, 12.2); ax.set_ylim(-0.3, 14)
    ax.set_xlabel("V_DS (V)"); ax.set_ylabel("I_D (mA)")
    return _plt(fig)


def exp09_tr():
    s = L("exp09tr")
    fig, ax = plt.subplots(figsize=(5.4, 3.0))
    ax.plot(s["vgs"], s["id"], color=ACCENT, lw=2.2, label="LTspice, V_DS = 8 V")
    vg = np.linspace(-3, 0, 50)
    ax.plot(vg, 11.85 * (1 - vg / -3) ** 2, "o", color=WARN, ms=3, label=r"Shockley: $I_{DSS}(1 - V_{GS}/V_{P})^{2}$")
    ax.annotate("I_DSS ≈ 11.85 mA", xy=(0, 11.85), xytext=(-2.6, 11), fontsize=9, arrowprops=dict(arrowstyle="->", color=MUTED))
    ax.annotate("V_P ≈ −3 V", xy=(-3, 0), xytext=(-4.8, 3), fontsize=9, arrowprops=dict(arrowstyle="->", color=MUTED))
    ax.set_xlabel("V_GS (V)"); ax.set_ylabel("I_D (mA)"); ax.legend(fontsize=8, loc="upper left", bbox_to_anchor=(0, 0.82))
    return _plt(fig)


# ------------------------------------------------------------------ Exp 10
def exp10_circuit():
    d = _d(unit=2.3, fs=11)
    d += elm.SourceSin().endpoints((0, 0), (0, 3)).label("V_in\n0.1 V\n1 kHz", loc="bottom")
    CAP(d, (0, 3), (2.6, 3), "C1 1 µF")
    RES(d, (2.6, 6.2), (2.6, 3), "RA\n6.8 MΩ"); RES(d, (2.6, 3), (2.6, 0), "RB\n1 MΩ", loc="bottom")
    W(d, (2.6, 3), (3.6, 3)); DOT(d, (2.6, 3))
    j = elm.JFetN(circle=True).reverse().anchor("gate").at((3.6, 3)).label("J1\n2N5434", loc="right"); d += j
    xd = j.drain.x
    RES(d, (xd, 6.2), (xd, 4.5), "R1\n3.3 kΩ"); W(d, (xd, 4.5), j.drain)
    RES(d, j.source, (xd, 0), "Rs\n2.2 kΩ", loc="bottom"); DOT(d, j.source)
    W(d, j.source, (xd + 2.2, j.source.y)); CAP(d, (xd + 2.2, j.source.y), (xd + 2.2, 0), "Cs\n100 µF", loc="bottom")
    CAP(d, (xd, 4.5), (xd + 4.0, 4.5), "C2 0.5 µF"); DOT(d, (xd, 4.5))
    RES(d, (xd + 4.0, 4.5), (xd + 4.0, 0), "R2\n10 kΩ", loc="bottom"); W(d, (xd + 4.0, 4.5), (xd + 5.0, 4.5))
    OUT(d, (xd + 5.0, 4.5), "output"); DOT(d, (xd + 4.0, 4.5))
    W(d, (2.6, 6.2), (xd, 6.2)); TXT(d, (3.6, 6.65), "+12 V", color=WARN)
    W(d, (0, 0), (xd + 4.0, 0)); GND(d, (2.6, 0))
    return _svg(d)


def exp10_tr():
    s = L("exp10tr"); t = s["t"] * 1e3; m = t > 6
    fig, ax = plt.subplots(figsize=(6.2, 2.7))
    ax.plot(t[m], s["vin"][m], color=MUTED, lw=1.5, ls="--", label="V_in (0.2 V p-p)")
    ax.plot(t[m], s["vo"][m], color=ACCENT, lw=2.2, label="output (≈ 4.7 V p-p, inverted)")
    ax.set_xlabel("time (ms)"); ax.set_ylabel("volts"); ax.legend(fontsize=8, loc="lower right")
    return _plt(fig)


def exp10_freq():
    import json
    s = L("exp10ac"); r = json.loads((SIM / "results.json").read_text())["exp10"]
    m = (s["f"] >= 10) & (s["f"] <= 1e9)
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    ax.semilogx(s["f"][m], 20 * np.log10(s["g"][m]), color=ACCENT, lw=2.2)
    top = r["AmaxdB"]; ax.axhline(top - 3, color=WARN, ls="--", lw=1)
    for x, lab in [(r["fL"], f"f_L ≈ {r['fL']:.0f} Hz"), (r["fH"], f"f_H ≈ {r['fH'] / 1e6:.1f} MHz")]:
        ax.axvline(x, color=WARN, ls="--", lw=1); ax.text(x * 1.15, top - 15, lab, color=WARN, fontsize=9)
    ax.set_ylim(top - 30, top + 4); ax.set_xlabel("frequency (Hz)"); ax.set_ylabel("gain (dB)")
    ax.text(15, top + 0.8, f"midband {top:.1f} dB (gain {r['Amax']:.1f})", fontsize=9)
    return _plt(fig)


# ------------------------------------------------------------------ Exp 11
def rc_ladder():
    d = _d(unit=2.2, fs=11)
    W(d, (0, 2.5), (0.6, 2.5)); TXT(d, (0, 3.0), "from collector\n(0°)", fs=10)
    x = 0.6
    for k, ph in enumerate(["60°", "120°", "180°"]):
        CAP(d, (x, 2.5), (x + 2.4, 2.5), "C")
        RES(d, (x + 2.4, 2.5), (x + 2.4, 0), "R", loc="bottom"); DOT(d, (x + 2.4, 2.5))
        TXT(d, (x + 2.4, 3.1), f"≈ {ph}", color=WARN, fs=10)
        x += 2.4
    W(d, (x, 2.5), (x + 0.8, 2.5)); TXT(d, (x + 1.4, 2.2), "to base", fs=10)
    W(d, (0.6, 0), (x, 0)); GND(d, (0.6, 0))
    return _svg(d)


def exp11_circuit():
    d = _d(unit=2.3, fs=11)
    RES(d, (2, 7), (2, 3), "R4\n57 kΩ"); RES(d, (2, 3), (2, 0), "R3\n10 kΩ")
    W(d, (2, 3), (3, 3)); DOT(d, (2, 3))
    q = elm.BjtNpn(circle=True).anchor("base").at((3, 3)).label("Q1\nBC547B", loc="right"); d += q
    xc = q.collector.x
    RES(d, (xc, 7), (xc, 4.5), "R1\n6.8 kΩ", loc="bottom"); W(d, (xc, 4.5), q.collector)
    RES(d, q.emitter, (xc, 0), "R2\n1.5 kΩ", loc="bottom"); DOT(d, q.emitter)
    W(d, q.emitter, (xc + 1.9, q.emitter.y)); CAP(d, (xc + 1.9, q.emitter.y), (xc + 1.9, 0), "C1\n100 nF", loc="bottom")
    W(d, (2, 7), (xc, 7)); TXT(d, (2.9, 7.45), "+10 V", color=WARN)
    x = xc
    for k, (cn, rn) in enumerate([("C2", "R5"), ("C3", "R6")]):
        step = 3.6 if k == 0 else 2.8
        CAP(d, (x, 4.5), (x + step, 4.5), f"{cn} 0.5 nF"); DOT(d, (x, 4.5))
        RES(d, (x + step, 4.5), (x + step, 0), f"{rn}\n10 kΩ", loc="bottom")
        x += step
    CAP(d, (x, 4.5), (x + 2.8, 4.5), "C4 0.5 nF"); DOT(d, (x, 4.5)); x += 2.8
    W(d, (x, 4.5), (x, -1)); W(d, (x, -1), (1, -1)); W(d, (1, -1), (1, 3)); W(d, (1, 3), (2, 3))
    W(d, (2, 0), (x - 2.8, 0)); GND(d, (2, 0))
    TXT(d, ((1 + x) / 2, -0.55), "feedback wire: 3rd C back to the base (3rd 'R' = R3 || R4 || transistor input)", color=MUTED, fs=10)
    return _svg(d)


def exp11_wave():
    s = L("exp11_0.5n"); t = s["t"] * 1e3; m = (t > 8) & (t < 8.6)
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    ax.plot(t[m], s["vo"][m], color=ACCENT, lw=2)
    ax.set_xlabel("time (ms)"); ax.set_ylabel("collector V (V)")
    ax.set_title("C = 0.5 nF: about 8.4 cycles in 0.6 ms → f ≈ 14 kHz", fontsize=10)
    return _plt(fig)


# ------------------------------------------------------------------ Exp 12
def exp12_circuit():
    d = _d()
    d += elm.SourceV().endpoints((0, 0), (0, 3)).label("V2 PULSE\n(0 5 0 0 0 1m 2m 10)", loc="bottom")
    W(d, (0, 3), (2, 3))
    m = elm.NFet().reverse().anchor("gate").at((2, 3)).label("M1\nFDR6580", loc="right"); d += m
    RES(d, (m.drain.x, 6.6), (m.drain.x, 4.5), "R1 1 kΩ"); W(d, (m.drain.x, 4.5), m.drain)
    TXT(d, (m.drain.x, 7.05), "V_DD = +5 V", color=WARN)
    W(d, (m.drain.x, 4.5), (m.drain.x + 2.5, 4.5)); OUT(d, (m.drain.x + 2.5, 4.5), "inverter output"); DOT(d, (m.drain.x, 4.5))
    W(d, m.source, (m.source.x, 0)); W(d, (0, 0), (m.source.x, 0)); GND(d, (m.source.x, 0))
    return _svg(d)


def exp12_tr():
    s = L("exp12tr"); t = s["t"] * 1e3; m = t < 6
    fig, ax = plt.subplots(figsize=(6.2, 2.7))
    ax.plot(t[m], s["vin"][m], color=MUTED, lw=1.6, ls="--", label="input (gate)")
    ax.plot(t[m], s["vo"][m], color=ACCENT, lw=2.2, label="output (drain)")
    ax.set_xlabel("time (ms)"); ax.set_ylabel("volts"); ax.set_ylim(-0.5, 7.2); ax.legend(fontsize=8, loc="upper right")
    ax.text(2.1, 6.2, "input HIGH → output LOW, and the reverse", fontsize=8.5, color=INK)
    return _plt(fig)


def exp12_vtc():
    import json
    s = L("exp12vtc"); r = json.loads((SIM / "results.json").read_text())["exp12_vtc"]
    fig, ax = plt.subplots(figsize=(5.8, 3.2))
    ax.plot(s["vin"], s["vo"], color=ACCENT, lw=2.2)
    ax.plot([0, 5], [0, 5], color=MUTED, lw=0.8, ls=":")
    ax.plot([r["VM"]], [r["VM"]], "o", color=WARN); ax.text(r["VM"] + 0.12, r["VM"] + 0.1, f"V_M ≈ {r['VM']:.2f} V", color=WARN, fontsize=9)
    ax.text(1.3, 4.6, f"V_OH = 5.0 V (input LOW)", fontsize=9); ax.text(2.6, 0.25, "V_OL ≈ 0 V (input HIGH)", fontsize=9)
    ax.set_xlabel("V_in (V)"); ax.set_ylabel("V_out (V)")
    ax2 = ax.inset_axes([0.5, 0.35, 0.45, 0.4])
    ax2.plot(s["vin"], s["vo"], color=ACCENT, lw=1.8); ax2.set_xlim(0.4, 0.9); ax2.set_ylim(-0.2, 5.2)
    for x, lab in [(r["VIL"], "V_IL"), (r["VIH"], "V_IH")]:
        ax2.axvline(x, color=WARN, lw=0.8, ls="--"); ax2.text(x + 0.005, 2.5, lab, color=WARN, fontsize=7.5, rotation=90)
    ax2.tick_params(labelsize=7); ax2.set_title("zoom 0.4–0.9 V", fontsize=7.5)
    return _plt(fig)


# ------------------------------------------------------------------ Additional: two-stage
def expA_circuit():
    d = _d(unit=2.0, fs=10)
    v1 = {"Vs": "V2\n0.5 V", "Rs": "R6 2.2k", "Cin": "C2 10µ", "R1": "R2\n25k", "R2": "R3\n8.2k",
          "Rc": "R1\n560", "Re": "R4\n560", "Ce": "C1\n47µ", "Cc": ""}
    v2 = {"Cin": "C3 10µ", "R1": "R8\n25k", "R2": "R9\n8.2k", "Rc": "R7\n560", "Re": "R10\n560", "Ce": "C4\n47µ", "Cc": "C6 10µ"}
    p1 = _ce_stage(d, 0, v1, src=True, cc=False, bjt="Q1")
    ox2 = 9.0
    p2 = _ce_stage(d, ox2, v2, src=False, cc=True, load="R11\n1k", bjt="Q2")
    W(d, p1["c"], (p2["in"][0], p1["c"][1])); W(d, (p2["in"][0], p1["c"][1]), p2["in"])
    W(d, p1["rail_r"], p2["rail_l"]); TXT(d, (9.5, 6.65), "+15 V", color=WARN)
    W(d, (0, 0), (p2["x_end"], 0)); GND(d, (4.4, 0))
    return _svg(d)


def expA_freq():
    import json
    s = L("expA"); r = json.loads((SIM / "results.json").read_text())["expA"]
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    for f, g, col, lab, key in [(s["f1"], s["g1"], ACCENT, "one stage (1 kΩ load)", "one"),
                                (s["f2"], s["g2"], WARN, "two stages", "two")]:
        ax.semilogx(f, 20 * np.log10(g), color=col, lw=2.2, label=lab)
        for x in (r[key]["fL"], r[key]["fH"]):
            ax.plot([x], [r[key]["dB"] - 3], "o", color=col, ms=5)
    ax.set_xlabel("frequency (Hz)"); ax.set_ylabel("gain (dB)"); ax.legend(fontsize=8.5, loc="lower center")
    ax.set_ylim(-10, 72); ax.text(15, 66, "dots = −3 dB points", fontsize=8.5, color=MUTED)
    return _plt(fig)


def design_circuit():
    d = _d(unit=2.3, fs=11)
    g, yr = -3.2, 6.4
    d += elm.SourceSin().endpoints((0, g), (0, 3)).label("v_s\n≈ 18 mV", loc="bottom")
    CAP(d, (0, 3), (2.4, 3), "Cin 10 µF")
    RES(d, (2.4, yr), (2.4, 3), "R1\n220 kΩ"); RES(d, (2.4, 3), (2.4, g), "R2\n33 kΩ", loc="bottom")
    W(d, (2.4, 3), (3.4, 3)); DOT(d, (2.4, 3))
    q1 = elm.BjtNpn(circle=True).anchor("base").at((3.4, 3)); d += q1
    TXT(d, (q1.collector.x + 0.2, 2.75), "Q1", fs=11, halign="left")
    xc = q1.collector.x
    RES(d, (xc, yr), (xc, 4.5), "RC\n8.2 kΩ"); W(d, (xc, 4.5), q1.collector); DOT(d, (xc, 4.5))
    W(d, q1.emitter, (xc, 2.0)); RES(d, (xc, 2.0), (xc, -0.6), "RE1 82 Ω\n(unbypassed)")
    RES(d, (xc, -0.6), (xc, g), "RE2\n820 Ω"); DOT(d, (xc, -0.6))
    W(d, (xc, -0.6), (xc + 1.6, -0.6)); CAP(d, (xc + 1.6, -0.6), (xc + 1.6, g), "CE\n100 µF", loc="bottom")
    W(d, (xc, 4.5), (6.9, 4.5))
    q2 = elm.BjtNpn(circle=True).anchor("base").at((6.9, 4.5)); d += q2
    TXT(d, (q2.collector.x + 0.2, 4.25), "Q2", fs=11, halign="left")
    W(d, q2.collector, (q2.collector.x, yr)); W(d, (2.4, yr), (q2.collector.x, yr))
    TXT(d, (4.9, yr + 0.45), "+9 V", color=WARN)
    xe = q2.emitter.x
    RES(d, q2.emitter, (xe, g), "RE\n1.8 kΩ", loc="bottom"); DOT(d, q2.emitter)
    CAP(d, q2.emitter, (xe + 2.6, q2.emitter.y), "Cout 100 µF"); OUT(d, (xe + 2.6, q2.emitter.y), "v_o")
    W(d, (0, g), (xe, g)); GND(d, (2.4, g))
    TXT(d, (2.0, -4.3), "stage 1: CE (sets gain and R_in)", color=ACCENT, fs=10)
    TXT(d, (7.6, -4.3), "stage 2: emitter follower (sets R_out)", color=ACCENT, fs=10)
    return _svg(d)


ALL = {name: fn for name, fn in globals().items()
       if callable(fn) and not name.startswith("_") and name not in
       {"L", "W", "RES", "CAP", "DOT", "TXT", "GND", "OUT", "Path"} and fn.__module__ == __name__}
