"""Figures for the ECE2131 lab pack. Every function returns an SVG string.

Pin diagrams: from the manual's own figures (7400/02/04/08/10/11/32/86, 7485, 74180, 74151/153/157, 74138, 7473)
and the standard TI datasheets for those the manual leaves blank (7474, 7483, 7420, 7427, 74139).
"""
import io
import re
from pathlib import Path

import numpy as np
import schemdraw
import schemdraw.elements as elm
import schemdraw.logic as lg
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.text import Text

schemdraw.use("svg")
SIM = Path(__file__).resolve().parent / "sim" / "out"
INK, ACCENT, WARN, GOOD, MUTED = "#1f2937", "#1d4ed8", "#b91c1c", "#15803d", "#6b7280"
plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"], "mathtext.fontset": "dejavusans", "font.size": 10,
    "axes.edgecolor": "#9ca3af", "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "svg.fonttype": "path", "axes.grid": True, "grid.color": "#e5e7eb", "grid.linewidth": 0.6,
})
_SUB = re.compile(r"(?<![\w$])([A-Za-z]+)_([A-Za-z0-9]+)")


def _sub(s):
    return s if "$" in s else _SUB.sub(r"$\1_{\2}$", s)


def _plt(fig):
    for t in fig.findobj(Text):
        t.set_text(_sub(t.get_text()))
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    s = buf.getvalue()
    return s[s.index("<svg"):]


def _svg(d):
    return d.get_imagedata("svg").decode()


# ------------------------------------------------------------------ pin diagrams
Q2 = ["1A", "1B", "1Y", "2A", "2B", "2Y", "GND", "3Y", "3A", "3B", "4Y", "4A", "4B", "VCC"]
T3 = ["1A", "1B", "2A", "2B", "2C", "2Y", "GND", "3Y", "3A", "3B", "3C", "1Y", "1C", "VCC"]
PINS = {
    "7400": ("Quad 2-input NAND", Q2), "7408": ("Quad 2-input AND", Q2), "7432": ("Quad 2-input OR", Q2),
    "7486": ("Quad 2-input XOR", Q2),
    "7402": ("Quad 2-input NOR", ["1Y", "1A", "1B", "2Y", "2A", "2B", "GND", "3A", "3B", "3Y", "4A", "4B", "4Y", "VCC"]),
    "7404": ("Hex inverter", ["1A", "1Y", "2A", "2Y", "3A", "3Y", "GND", "4Y", "4A", "5Y", "5A", "6Y", "6A", "VCC"]),
    "7410": ("Triple 3-input NAND", T3), "7411": ("Triple 3-input AND", T3), "7427": ("Triple 3-input NOR", T3),
    "7420": ("Dual 4-input NAND", ["1A", "1B", "NC", "1C", "1D", "1Y", "GND", "2Y", "2A", "2B", "NC", "2C", "2D", "VCC"]),
    "7483": ("4-bit binary full adder", ["A3", "S2", "A2", "B2", "VCC", "S1", "B1", "A1", "S0", "A0", "B0", "GND",
                                         "Cin", "Cout", "S3", "B3"]),
    "7485": ("4-bit magnitude comparator", ["B3", "I(A<B)", "I(A=B)", "I(A>B)", "A>B", "A=B", "A<B", "GND",
                                            "B0", "A0", "B1", "A1", "A2", "B2", "A3", "VCC"]),
    "74180": ("9-bit parity generator/checker", ["I6", "I7", "PE", "PO", "ΣE", "ΣO", "GND", "I0", "I1", "I2", "I3",
                                                  "I4", "I5", "VCC"]),
    "74151": ("8:1 multiplexer", ["I3", "I2", "I1", "I0", "Y", "Y'", "E'", "GND", "S2", "S1", "S0", "I7", "I6", "I5",
                                  "I4", "VCC"]),
    "74153": ("Dual 4:1 multiplexer", ["1E'", "S1", "1I3", "1I2", "1I1", "1I0", "1Y", "GND", "2Y", "2I0", "2I1", "2I2",
                                       "2I3", "S0", "2E'", "VCC"]),
    "74157": ("Quad 2:1 multiplexer", ["S", "1A", "1B", "1Y", "2A", "2B", "2Y", "GND", "3Y", "3B", "3A", "4Y", "4B",
                                       "4A", "E'", "VCC"]),
    "74138": ("3:8 decoder / 1:8 demux", ["A0", "A1", "A2", "E1'", "E2'", "E3", "O7'", "GND", "O6'", "O5'", "O4'",
                                          "O3'", "O2'", "O1'", "O0'", "VCC"]),
    "74139": ("Dual 2:4 decoder", ["1E'", "1A0", "1A1", "1Y0'", "1Y1'", "1Y2'", "1Y3'", "GND", "2Y3'", "2Y2'", "2Y1'",
                                   "2Y0'", "2A1", "2A0", "2E'", "VCC"]),
    "7474": ("Dual D flip-flop, +edge, preset & clear", ["1CLR'", "1D", "1CLK", "1PR'", "1Q", "1Q'", "GND", "2Q'", "2Q",
                                                          "2PR'", "2CLK", "2D", "2CLR'", "VCC"]),
    "7473": ("Dual JK flip-flop, −edge, clear (VCC pin 4!)", ["1CLK", "1CLR'", "1K", "VCC", "2CLK", "2CLR'", "2J",
                                                              "2Q'", "2Q", "2K", "GND", "1Q", "1Q'", "1J"]),
}


def dip(ic):
    title, pins = PINS[ic]
    n = len(pins); h = n // 2
    fig, ax = plt.subplots(figsize=(3.1, 0.34 * h + 0.9))
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-0.6, h + 0.9); ax.axis("off"); ax.grid(False)
    ax.add_patch(plt.Rectangle((-1, 0), 2, h, fc="#f8fafc", ec=INK, lw=1.2))
    ax.add_patch(matplotlib.patches.Arc((0, h), 0.6, 0.6, theta1=180, theta2=360, color=INK, lw=1.2))
    for k in range(h):
        y = h - 0.5 - k
        for side, num in ((-1, k + 1), (1, n - k)):
            lab = pins[num - 1]
            col = WARN if lab == "VCC" else (INK if lab == "GND" else (MUTED if lab == "NC" else ACCENT))
            ax.plot([side, side * 1.25], [y, y], color=INK, lw=1)
            ax.text(side * 1.33, y, str(num), ha="right" if side < 0 else "left", va="center", fontsize=8.5, color=MUTED)
            ax.text(side * 0.92, y, lab, ha="left" if side < 0 else "right", va="center", fontsize=8.5, color=col,
                    fontweight="bold" if lab in ("VCC", "GND") else "normal")
    ax.text(0, h + 0.55, f"{ic}: {title}", ha="center", fontsize=9, fontweight="bold")
    return _plt(fig)


def _dipfn(ic):
    def f():
        return dip(ic)
    return f


# ------------------------------------------------------------------ K-maps (Exp 3)
def kmap_f():
    d = schemdraw.Drawing(show=False); d.config(fontsize=12)
    mins = [1, 3, 5, 7, 8, 12, 14]
    tt = [(format(m, "04b"), "1") for m in mins]
    d += lg.Kmap(names="WXYZ", truthtable=tt, groups={"0..1": {"color": "#2563eb", "fill": "#2563eb22"},
                                                    "1.00": {"color": "#dc2626", "fill": "#dc262622"},
                                                    "11.0": {"color": "#16a34a", "fill": "#16a34a22"}})
    return _svg(d)


def kmap_fbar():
    d = schemdraw.Drawing(show=False); d.config(fontsize=12)
    zeros = [0, 2, 4, 6, 9, 10, 11, 13, 15]
    tt = [(format(m, "04b"), "1") for m in zeros]
    d += lg.Kmap(names="WXYZ", truthtable=tt, groups={"0..0": {"color": "#2563eb", "fill": "#2563eb22"},
                                                    "1..1": {"color": "#dc2626", "fill": "#dc262622"},
                                                    "101.": {"color": "#16a34a", "fill": "#16a34a22"}})
    return _svg(d)


def _two_level(Gate, terms):
    """Two-level circuit: one gate per term, all into one output gate of the same type."""
    d = schemdraw.Drawing(show=False); d.config(fontsize=12, lw=1.4)
    ys = [2.4, 0, -2.4]
    outs = []
    for y, labs in zip(ys, terms):
        g = Gate(inputs=len(labs)).right().at((0, y)).anchor("in1" if len(labs) == 2 else "in2"); d += g
        for k, lab in enumerate(labs):
            p = getattr(g, f"in{k + 1}")
            d += elm.Line().at(p).left(0.7).label(lab, loc="left")
        outs.append(g.out)
    o = Gate(inputs=3).right().at((5.6, 0)).anchor("in2"); d += o
    for k, (src, dst) in enumerate(zip(outs, (o.in1, o.in2, o.in3))):
        xm = 3.0 + 0.5 * k
        d += elm.Line().endpoints(src, (xm, src[1]))
        d += elm.Line().endpoints((xm, src[1]), (xm, dst[1]))
        d += elm.Line().endpoints((xm, dst[1]), dst)
    d += elm.Line().right().at(o.out).length(0.7).label("f", loc="right")
    return _svg(d)


def exp3_nand():
    return _two_level(lg.Nand, [["W'", "Z"], ["W", "Y'", "Z'"], ["W", "X", "Z'"]])


def exp3_nor():
    return _two_level(lg.Nor, [["W", "Z"], ["W'", "Z'"], ["W'", "X", "Y'"]])


def counter_timing():
    d = schemdraw.Drawing(show=False); d.config(fontsize=15)
    comp = lambda w: w[0] + "".join("." if w[i] == w[i - 1] else w[i] for i in range(1, len(w)))
    q = lambda div: "".join("01"[(k // div) % 2] for k in range(17))
    d += lg.TimingDiagram({"signal": [
        {"name": "CLK", "wave": "N" + "." * 16},
        {"name": "QA", "wave": comp(q(1))}, {"name": "QB", "wave": comp(q(2))},
        {"name": "QC", "wave": comp(q(4))}, {"name": "QD", "wave": comp(q(8))}]},
        ygap=0.7, risetime=0.08, yheight=0.8)
    return _svg(d)


def fsm1010():
    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.set_xlim(-1.2, 11.0); ax.set_ylim(-2.6, 2.1); ax.axis("off"); ax.grid(False)
    S = {"A": (0, 0), "B": (3.3, 0), "C": (6.6, 0), "D": (9.9, 0)}
    sub = {"A": "nothing yet · 00\n(x=0: stay)", "B": "seen '1' · 01\n(x=1: stay)", "C": "seen '10' · 11",
           "D": "seen '101' · 10"}
    for k, (x, y) in S.items():
        ax.add_patch(plt.Circle((x, y), 0.55, fc="#eff6ff", ec=ACCENT, lw=1.6))
        ax.text(x, y, k, ha="center", va="center", fontsize=14, fontweight="bold")
        ax.text(x, 0.75, sub[k], ha="center", fontsize=8.5, color=MUTED)

    def arr(a, b, lab, rad=0.0, col=INK):
        A, B = S[a], S[b]
        ax.annotate("", xy=B, xytext=A, arrowprops=dict(arrowstyle="-|>", color=col, lw=1.4,
                                                        connectionstyle=f"arc3,rad={rad}", shrinkA=17, shrinkB=17))
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        dx, dy = B[0] - A[0], B[1] - A[1]
        lx, ly = mx + 0.5 * rad * dy, my - 0.5 * rad * dx
        ax.text(lx, ly + (0.12 if rad == 0 else (0.12 if ly > 0 else -0.3)), lab, ha="center", fontsize=10, color=col)

    arr("A", "B", "1/0"); arr("B", "C", "0/0"); arr("C", "D", "1/0")
    arr("C", "A", "0/0", rad=-0.32)
    arr("D", "C", "0/1  ← 1010 found", rad=-0.5, col=WARN)
    arr("D", "B", "1/0", rad=-0.62)
    ax.text(5.0, 1.85, "arrow label = input x / output Z  (Mealy)", ha="center", fontsize=9, color=MUTED)
    return _plt(fig)


def ttl_nand_circuit():
    d = schemdraw.Drawing(show=False); d.config(unit=2.0, fontsize=11, lw=1.4, color=INK)
    yr = 8
    L = lambda a, b: elm.Line().endpoints(a, b)
    d += elm.Resistor().endpoints((0, yr), (0, 4)).label("R1\n4 kΩ")
    d += L((0, 4), (0.6, 4))
    q1 = elm.BjtNpn(circle=True).anchor("base").at((0.6, 4)); d += q1
    d += elm.Label().at((q1.base.x - 0.1, 3.35)).label("Q1", halign="right")
    d += L(q1.emitter, (q1.emitter.x, 2.3))
    d += elm.Dot(open=True).at((q1.emitter.x, 2.3)).label("inputs A, B\n(Q1 has two emitters)", loc="bottom")
    d += L(q1.collector, (3.2, q1.collector.y))
    q2 = elm.BjtNpn(circle=True).anchor("base").at((3.2, q1.collector.y)); d += q2
    xc = q2.collector.x
    d += elm.Label().at((xc + 0.15, q2.base.y - 0.45)).label("Q2", halign="left")
    d += elm.Resistor().endpoints((xc, yr), (xc, 6.2)).label("R2\n1.6 kΩ")
    d += L((xc, 6.2), q2.collector)
    d += L(q2.emitter, (xc, 3.0))
    d += elm.Resistor().endpoints((xc, 3.0), (xc, 0)).label("R3\n1 kΩ")
    d += L((xc, 6.2), (5.4, 6.2))
    q4 = elm.BjtNpn(circle=True).anchor("base").at((5.4, 6.2)); d += q4
    xo = q4.collector.x
    d += elm.Label().at((xo + 0.2, 6.0)).label("Q4", halign="left")
    d += elm.Resistor().endpoints((xo, yr), q4.collector).label("R4 130 Ω", loc="bottom")
    d += elm.Diode().endpoints(q4.emitter, (xo, 3.7)).label("D", loc="bottom")
    d += L((xc, 3.0), (5.4, 3.0))
    q3 = elm.BjtNpn(circle=True).anchor("base").at((5.4, 3.0)); d += q3
    d += L((xo, 3.7), q3.collector)
    d += elm.Label().at((xo + 0.2, 2.8)).label("Q3", halign="left")
    d += L(q3.emitter, (xo, 0))
    d += L((xo, 3.7), (xo + 1.6, 3.7)); d += elm.Dot(open=True).at((xo + 1.6, 3.7)).label("Y = (AB)'", loc="right")
    for p in ((xc, 6.2), (xc, 3.0), (xo, 3.7)):
        d += elm.Dot().at(p)
    d += L((0, yr), (xo, yr)); d += elm.Label().at(((xo) / 2, yr + 0.4)).label("VCC = +5 V", color=WARN)
    d += L((xc, 0), (xo, 0)); d += elm.Ground().at((xc, 0))
    return _svg(d)


def ttl_vtc():
    fig, ax = plt.subplots(figsize=(5.8, 3.0))
    for nm, col, lab in (("nand", ACCENT, "NAND: A swept, B = 1"), ("nor", WARN, "NOR: A swept, B = 0")):
        s = np.load(SIM / f"{nm}_vtc.npz")
        ax.plot(s["vin"], s["vout"], color=col, lw=2.1, label=lab, ls="-" if nm == "nand" else "--")
    ax.axvspan(0, 0.8, color="#dcfce7", alpha=0.6); ax.axvspan(2.0, 5, color="#dbeafe", alpha=0.5)
    ax.text(0.05, 1.8, "valid LOW in\n(< 0.8 V)", fontsize=8.5); ax.text(2.8, 1.8, "valid HIGH in (> 2.0 V)", fontsize=8.5)
    ax.set_xlabel("V_A (V)"); ax.set_ylabel("V_Y (V)"); ax.legend(fontsize=8.5, loc="upper right")
    return _plt(fig)


ALL = {f"pin{ic}": _dipfn(ic) for ic in PINS}
ALL.update({n: f for n, f in list(globals().items()) if callable(f) and n in {
    "kmap_f", "kmap_fbar", "exp3_nand", "exp3_nor", "counter_timing", "fsm1010", "ttl_nand_circuit", "ttl_vtc"}})
