"""All figures for the ECE2107 study pack. Every function returns an SVG string.

Circuits: schemdraw (svg backend). Plots: matplotlib -> SVG.
Values are the professor's (class notes); verified by nodal simulation 2026-09-25.
"""
import io
import numpy as np
import schemdraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

schemdraw.use("svg")
FONT = "Arial"
INK = "#1f2937"
ACCENT = "#1d4ed8"
WARN = "#b91c1c"
MUTED = "#6b7280"

plt.rcParams.update({
    "font.family": ["Arial", "DejaVu Sans"], "mathtext.fontset": "dejavusans", "font.size": 10, "axes.edgecolor": "#9ca3af",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#374151", "ytick.color": "#374151", "axes.labelcolor": "#111827",
    "svg.fonttype": "path",
})


def _d():
    d = schemdraw.Drawing(show=False)
    d.config(unit=2.6, fontsize=13, font=FONT, color=INK, lw=1.6)
    return d


def _svg(d):
    return d.get_imagedata("svg").decode()


def _plt(fig):
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    s = buf.getvalue()
    return s[s.index("<svg"):]


# ---------------------------------------------------------------- 01 elements
def sources():
    d = _d()
    d.config(unit=2.2, fontsize=12)
    items = [
        (elm.SourceV, "Independent V", "fixed V"),
        (elm.SourceI, "Independent I", "fixed I"),
        (elm.SourceControlledV, "VCVS", r"$V = \mu V_x$"),
        (elm.SourceControlledV, "CCVS", r"$V = r I_x$"),
        (elm.SourceControlledI, "VCCS", r"$I = g V_x$"),
        (elm.SourceControlledI, "CCCS", r"$I = \beta I_x$"),
    ]
    for k, (E, name, law) in enumerate(items):
        x = k * 3.1
        e = E().at((x, 0)).up()
        d += e
        d += elm.Label().at((x, -0.7)).label(name, fontsize=12)
        d += elm.Label().at((x, -1.25)).label(law, fontsize=11, color=ACCENT)
    return _svg(d)


def continuity_plot():
    t = np.linspace(-1, 5, 800)
    iL = np.where(t < 0, 0, 10 * (1 - np.exp(-t)))
    vL = np.where(t < 0, 0, 10 * np.exp(-t))
    fig, ax = plt.subplots(2, 1, figsize=(6.2, 3.6), sharex=True)
    ax[0].plot(t, iL, color=ACCENT, lw=2)
    ax[0].set_ylabel("$i_L$ (mA)")
    ax[0].annotate("smooth at t = 0:\ncurrent cannot jump", xy=(0.05, 0.3), xytext=(1.4, 2.0),
                   arrowprops=dict(arrowstyle="->", color=MUTED), fontsize=9)
    ax[1].plot(t, vL, color=WARN, lw=2)
    ax[1].set_ylabel("$v_L$ (V)")
    ax[1].set_xlabel("t / τ")
    ax[1].annotate("jumps 0 → 10 V at t = $0^+$", xy=(0.02, 10), xytext=(1.2, 7.5),
                   arrowprops=dict(arrowstyle="->", color=MUTED), fontsize=9)
    for a in ax:
        a.axvline(0, color="#d1d5db", lw=1, ls="--")
    fig.suptitle("RL switched onto 10 V at t = 0 (R = 1 kΩ)", fontsize=10)
    return _plt(fig)


# ---------------------------------------------------------------- 02 dividers
def srctx():
    d = _d()
    d += (V := elm.SourceV().up().label("V"))
    d += elm.Resistor().right().label("R")
    d += elm.Dot(open=True).label("a", loc="right")
    d += elm.Line().at(V.start).right().length(2.6)
    d += elm.Dot(open=True).label("b", loc="right")
    d += elm.Label().at((4.3, 1.3)).label(r"$\Leftrightarrow$", fontsize=22)
    d += (I := elm.SourceI().at((7.2, 0)).up().label("I = V/R"))
    d += elm.Line().right().length(1.6)
    d += elm.Dot()
    d.push()
    d += elm.Resistor().down().label("R", loc="bottom")
    d.pop()
    d += elm.Line().right().length(1.2)
    d += elm.Dot(open=True).label("a", loc="right")
    d += elm.Line().at(I.start).right().length(2.8)
    d += elm.Dot(open=True).label("b", loc="right")
    return _svg(d)


def vdr():
    d = _d()
    d += (V := elm.SourceV().up().label("15 V"))
    d += elm.Resistor().right().label("3 kΩ").label(r"$+\ V_1\ -$", loc="bottom", color=ACCENT)
    d += elm.Resistor().right().label("6 kΩ").label(r"$+\ V_2\ -$", loc="bottom", color=ACCENT)
    d += elm.Line().down()
    d += elm.Line().to(V.start)
    return _svg(d)


def cdr12():
    d = _d()
    d += (S := elm.SourceI().up().label("12 A"))
    for k, (r, i) in enumerate([("3 kΩ", "$I_1$"), ("6 kΩ", "$I_2$"), ("4 kΩ", "$I_3$")]):
        d += elm.Line().right().length(2.2)
        d.push()
        d += (R := elm.Resistor().down().label(r, loc="bottom"))
        d += elm.CurrentLabelInline(direction="in").at(R).label(i)
        d.pop()
    d += elm.Line().at(S.start).right().length(6.6)
    return _svg(d)


def acvdr():
    d = _d()
    d += (V := elm.SourceSin().up().label("10 sin(2000t + 30°) V"))
    d += elm.Resistor().right().label("3 kΩ").label("$v_1$", loc="bottom", color=ACCENT)
    d += elm.Resistor().down().label("7 kΩ", loc="bottom").label("$v_2$", loc="top", color=ACCENT)
    d += elm.Line().to(V.start)
    return _svg(d)


def acplot():
    t = np.linspace(0, 2 * 2 * np.pi / 2000, 600)
    ph = np.deg2rad(30)
    fig, ax = plt.subplots(figsize=(6.2, 2.6))
    for amp, c, lab in [(10, INK, "v (source)"), (7, ACCENT, "$v_2$ = 0.7 v"), (3, WARN, "$v_1$ = 0.3 v")]:
        ax.plot(t * 1e3, amp * np.sin(2000 * t + ph), color=c, lw=1.8, label=lab)
    ax.axhline(0, color="#d1d5db", lw=0.8)
    ax.set_xlabel("t (ms)")
    ax.set_ylabel("volts")
    ax.legend(frameon=False, fontsize=9, loc="upper right", ncol=3)
    ax.set_ylim(-11, 13.5)
    ax.set_title("Same zero-crossings, same phase: only the size is divided", fontsize=10)
    return _plt(fig)


def ladder():
    d = _d()
    d.config(unit=2.2)
    d += elm.Dot(open=True).label("a", loc="left")
    d += elm.Line().right().length(1)
    d.push()
    d += elm.Resistor().down().label("3 kΩ", loc="bottom")
    d += (g := elm.Line().left().length(1))
    d += elm.Dot(open=True).label("b", loc="left")
    d.pop()
    vals = [("5 kΩ", "7 kΩ"), ("11 kΩ", "13 kΩ")]
    for s, p in vals:
        d += elm.Resistor().right().label(s)
        d.push()
        d += elm.Resistor().down().label(p, loc="bottom")
        d.pop()
    d += elm.Line().right().length(1).linestyle(":")
    d += elm.Label().at((7.1, 0)).label("to ∞", fontsize=12, color=MUTED)
    d += elm.Line().at(g.start).right().length(2 * 2.2).linestyle("-")
    d += elm.Line().right().length(1).linestyle(":")
    return _svg(d)


def ladder_plot():
    p = [n for n in range(3, 400) if all(n % q for q in range(2, int(n ** .5) + 1))]
    ns, rs = [], []
    for n in range(1, 30, 2):
        vals = p[:n]
        z = vals[-1]
        for j in range(n - 2, -1, -1):
            z = vals[j] + z if j % 2 else 1 / (1 / vals[j] + 1 / z)
        ns.append(n)
        rs.append(z)
    fig, ax = plt.subplots(figsize=(6.2, 2.5))
    ax.plot(ns, rs, "o-", color=ACCENT, ms=4)
    ax.axhline(rs[-1], color=WARN, ls="--", lw=1)
    ax.text(ns[-1], rs[-1] + 0.03, f"→ {rs[-1]:.4f} kΩ", color=WARN, ha="right", fontsize=9)
    ax.set_xlabel("resistors kept (ladder cut off after that many)")
    ax.set_ylabel("$R_{ab}$ (kΩ)")
    ax.set_title("Values 3, 5, 7, 11, 13, … : far sections barely matter", fontsize=10)
    return _plt(fig)


# ---------------------------------------------------------------- 03 superposition
def _sp_base(d, left="src", right="src", i_label="I"):
    if left == "src":
        d += (V := elm.SourceV().up().label("10 V"))
    else:
        d += (V := elm.Line().up().label("short", color=WARN))
    d += elm.Resistor().right().label("4 Ω")
    d += elm.Dot().label("A", loc="top")
    d.push()
    d += (R := elm.Resistor().down().label("2 Ω", loc="bottom"))
    d += elm.CurrentLabelInline(direction="in").at(R).label(i_label)
    d.pop()
    d += elm.Line().right()
    if right == "src":
        d += elm.SourceI().down().reverse().label("2 A", loc="bottom")
    else:
        d += elm.Gap().down().label("open", color=WARN, loc="bottom")
    d += elm.Line().to(V.start)
    return d


def sp_q():
    return _svg(_sp_base(_d()))


def sp_c1():
    return _svg(_sp_base(_d(), right="open", i_label="$I_1$"))


def sp_c2():
    return _svg(_sp_base(_d(), left="short", i_label="$I_2$"))


def sp_5v():
    d = _d()
    d += (V1 := elm.SourceV().up().label("5 V"))
    d += elm.Line().right()
    d.push()
    d += (R := elm.Resistor().down().label("1 kΩ", loc="bottom"))
    d += elm.CurrentLabelInline(direction="in").at(R).label("$I_1$")
    d.pop()
    d += elm.Line().right()
    d += elm.SourceV().down().reverse().label("5 V", loc="bottom")
    d += elm.Line().to(V1.start)
    return _svg(d)


def deactivate():
    d = _d()
    d.config(unit=2.2)
    d += elm.SourceV().at((0, 0)).up().label("V")
    d += elm.Label().at((1.4, 1.1)).label("→", fontsize=22)
    d += elm.Line().at((2.8, 0)).up().label("short (0 Ω)", loc="bottom", color=ACCENT)
    d += elm.SourceI().at((7.5, 0)).up().label("I")
    d += elm.Label().at((8.9, 1.1)).label("→", fontsize=22)
    d += elm.Line().at((10.3, 0)).up().length(0.7)
    d += elm.Dot(open=True)
    d += elm.Gap().up().length(0.8).label("open (∞ Ω)", loc="bottom", color=ACCENT)
    d += elm.Dot(open=True)
    d += elm.Line().up().length(0.7)
    d += elm.SourceControlledV().at((15.6, 0)).up().label("2I")
    d += elm.Label().at((17.5, 1.1)).label("stays ON", color=WARN, fontsize=12)
    return _svg(d)


# ---------------------------------------------------------------- 04 Thevenin
def _th_left(d):
    d += (V := elm.SourceV().up().label("10 V"))
    d += elm.Resistor().right().label("2 kΩ").label("I →", loc="bottom", ofst=0.15, color=ACCENT)
    d += (A := elm.Dot().label("A", loc="top"))
    d.push()
    d += elm.Resistor().down().length(1.3).label("2 kΩ", loc="bottom")
    d += elm.SourceControlledV().down().reverse().length(1.3).label("2I", loc="bottom")
    d.pop()
    return V, A


def th_q():
    d = _d()
    V, A = _th_left(d)
    d += elm.Resistor().right().label("2 kΩ")
    d += elm.Dot().label("B", loc="top")
    d += (L := elm.Resistor().down().label("$R_L$ = 1 kΩ", loc="bottom"))
    d += elm.CurrentLabelInline(direction="in").at(L).label("$I_L$")
    d += elm.Line().to(V.start)
    return _svg(d)


def th_voc():
    d = _d()
    V, A = _th_left(d)
    d += elm.Resistor().right().label("2 kΩ")
    d += elm.Dot(open=True).label("B (+)", loc="right")
    d += elm.Gap().down().label("$V_{oc} = V_{Th}$", loc="bottom", color=ACCENT)
    d += elm.Dot(open=True)
    d += elm.Line().to(V.start)
    return _svg(d)


def th_isc():
    d = _d()
    V, A = _th_left(d)
    d += elm.Resistor().right().label("2 kΩ")
    d += elm.Dot().label("B", loc="top")
    d += (S := elm.Line().down().label("short", loc="bottom", color=WARN))
    d += elm.CurrentLabelInline(direction="in").at(S).label("$I_{sc}$")
    d += elm.Line().to(V.start)
    return _svg(d)


def th_test():
    d = _d()
    d += (V := elm.Line().up().label("short", color=WARN))
    d += elm.Resistor().right().label("2 kΩ").label("I →", loc="bottom", ofst=0.15, color=ACCENT)
    d += elm.Dot().label("A", loc="top")
    d.push()
    d += elm.Resistor().down().length(1.3).label("2 kΩ", loc="bottom")
    d += elm.SourceControlledV().down().reverse().length(1.3).label("2I (on)", loc="bottom")
    d.pop()
    d += elm.Resistor().right().label("2 kΩ")
    d += elm.Dot().label("B", loc="top")
    d += elm.SourceV().down().reverse().label("$V_t$", loc="bottom").label("$I_t$ ←", loc="top", ofst=0.1)
    d += elm.Line().to(V.start)
    return _svg(d)


def th_eq(vth="$V_{Th}$", rth="$R_{Th}$", rl="$R_L$", il="$I_L$"):
    d = _d()
    d += (V := elm.SourceV().up().label(vth))
    d += elm.Resistor().right().label(rth)
    d += (L := elm.Resistor().down().label(rl, loc="bottom"))
    d += elm.CurrentLabelInline(direction="in").at(L).label(il)
    d += elm.Line().to(V.start)
    return _svg(d)


def th_eq_num():
    return th_eq("6.67 V", "2.67 kΩ", "1 kΩ", "$I_L$")


def no_eq_num():
    d = _d()
    d += (S := elm.SourceI().up().label("$I_N$ = 2.5 mA"))
    d += elm.Line().right().length(2.2)
    d.push()
    d += elm.Resistor().down().label("$R_N$ = 2.67 kΩ", loc="bottom")
    d.pop()
    d += elm.Line().right().length(4.4)
    d += (L := elm.Resistor().down().label("1 kΩ", loc="bottom"))
    d += elm.CurrentLabelInline(direction="in").at(L).label("$I_L$")
    d += elm.Line().to(S.start)
    return _svg(d)


# ---------------------------------------------------------------- 05 MPT
def mpt_q(v="10 V", r="10 kΩ"):
    d = _d()
    d += (V := elm.SourceV().up().label(v))
    d += elm.Resistor().right().label(r)
    d += elm.ResistorVar().down().label("$R_L$", loc="bottom")
    d += elm.Line().to(V.start)
    return _svg(d)


def mpt_q5():
    return mpt_q("10 V", "5 kΩ")


def mpt_curve():
    rl = np.linspace(0.2, 50, 600)
    p = 100 * rl / (10 + rl) ** 2        # mW with kΩ
    eta = rl / (10 + rl) * 100
    fig, ax = plt.subplots(2, 1, figsize=(6.2, 4.2), sharex=True)
    ax[0].plot(rl, p, color=ACCENT, lw=2)
    ax[0].plot([10], [2.5], "o", color=WARN)
    ax[0].annotate("peak: $R_L = R_{Th}$ = 10 kΩ,  P = 2.5 mW", xy=(10, 2.5), xytext=(17, 0.6),
                   arrowprops=dict(arrowstyle="->", color=MUTED), fontsize=9)
    ax[0].set_ylabel("$P_{load}$ (mW)")
    ax[1].plot(rl, eta, color=INK, lw=2)
    ax[1].plot([10], [50], "o", color=WARN)
    ax[1].annotate("only 50 % at the power peak", xy=(10, 50), xytext=(19, 35),
                   arrowprops=dict(arrowstyle="->", color=MUTED), fontsize=9)
    ax[1].set_ylabel("efficiency η (%)")
    ax[1].set_xlabel("$R_L$ (kΩ)")
    ax[1].set_ylim(0, 100)
    fig.suptitle("10 V source, $R_{Th}$ = 10 kΩ: sweep the load", fontsize=10)
    return _plt(fig)


# ---------------------------------------------------------------- 06 transients
def timeline():
    fig, ax = plt.subplots(figsize=(6.4, 1.7))
    ax.axis("off")
    ax.set_xlim(-3, 8.5)
    ax.set_ylim(-1.3, 1.4)
    ax.annotate("", xy=(8.4, 0), xytext=(-3, 0), arrowprops=dict(arrowstyle="->", color=INK))
    ax.axvspan(-3, -0.05, ymin=0.35, ymax=0.62, color="#dbeafe")
    ax.axvspan(0.05, 5, ymin=0.35, ymax=0.62, color="#fee2e2")
    ax.axvspan(5, 8.4, ymin=0.35, ymax=0.62, color="#dbeafe")
    for x, lab in [(-0.25, "$0^-$"), (0.25, "$0^+$"), (5, "5τ")]:
        ax.plot([x, x], [-0.15, 0.15], color=INK)
        ax.text(x, -0.55, lab, ha="center", fontsize=10)
    ax.text(-1.6, 0.85, "old steady state", ha="center", fontsize=9, color=ACCENT)
    ax.text(2.5, 0.85, "transient", ha="center", fontsize=9, color=WARN)
    ax.text(6.7, 0.85, "new steady state (∞)", ha="center", fontsize=9, color=ACCENT)
    ax.text(0, -1.15, "switch operates at t = 0", ha="center", fontsize=9, color=MUTED)
    return _plt(fig)


def r_sw():
    d = _d()
    d += (V := elm.SourceV().up().label("V"))
    d += elm.Switch().right().label("t = 0\n(closes)")
    d += elm.Resistor().down().label("R", loc="bottom")
    d += elm.Line().to(V.start)
    return _svg(d)


def rl_close():
    d = _d()
    d += (V := elm.SourceV().up().label("V"))
    d += elm.Switch().right().label("t = 0 (closes)")
    d += elm.Resistor().right().label("R")
    d += elm.Inductor2().down().label("L", loc="bottom")
    d += elm.Line().to(V.start)
    return _svg(d)


def rl_snaps():
    d = _d()
    d.config(unit=1.9, fontsize=11)
    titles = [(r"$t = 0^{-}$", "switch open", "open"), (r"$t = 0^{+}$", "L acts as OPEN", "Lopen"),
              (r"$t = \infty$", "L acts as SHORT", "Lshort")]
    for k, (title, sub, mode) in enumerate(titles):
        x0 = k * 6.2
        col = WARN if k == 1 else ACCENT
        d += elm.Label().at((x0 + 1.9, 3.5)).label(title, fontsize=12, color=col)
        d += elm.Label().at((x0 + 1.9, 2.95)).label(sub, fontsize=11, color=col)
        d += (V := elm.SourceV().at((x0, 0)).up().label("V"))
        if mode == "open":
            d += elm.Gap().right().length(1.9).label("open", color=MUTED)
        else:
            d += elm.Line().right().length(1.9)
        d += elm.Resistor().right().length(1.9).label("R")
        if mode == "Lshort":
            d += elm.Line().down().label("short", loc="bottom", color=ACCENT)
        elif mode == "Lopen":
            d += elm.Gap().down().label("open", loc="bottom", color=WARN)
        else:
            d += elm.Inductor2().down().label("L", loc="bottom")
        d += elm.Line().to(V.start)
    return _svg(d)


def xt_plot():
    t = np.linspace(0, 6, 500)
    x = 10 * (1 - np.exp(-t))
    fig, ax = plt.subplots(figsize=(6.2, 2.9))
    ax.plot(t, x, color=ACCENT, lw=2)
    ax.axhline(10, color=MUTED, ls="--", lw=1)
    ax.text(6, 10.3, "x(∞)", ha="right", fontsize=9, color=MUTED)
    ax.plot([0, 1], [0, 10], color=WARN, lw=1, ls=":")
    ax.annotate("initial slope reaches x(∞) at t = τ", xy=(0.55, 5.5), xytext=(2.0, 3.2),
                fontsize=8.5, color=WARN, arrowprops=dict(arrowstyle="->", color=WARN))
    for n, lab in [(1, "63.2 %"), (5, "99.3 %")]:
        ax.plot([n], [10 * (1 - np.exp(-n))], "o", color=INK, ms=4)
        ax.annotate(lab, (n, 10 * (1 - np.exp(-n))), xytext=(n + 0.15, 10 * (1 - np.exp(-n)) - 1.6),
                    fontsize=9)
    ax.text(0.1, 0.4, "x($0^+$)", fontsize=9, color=MUTED)
    ax.set_xlabel("t / τ")
    ax.set_ylabel("x(t)")
    ax.set_ylim(-0.5, 11.5)
    ax.set_title("x(t) = x(∞) + [x($0^+$) − x(∞)]·$e^{-t/τ}$", fontsize=10)
    return _plt(fig)


def rl_rise_plot():
    t = np.linspace(0, 6, 400)
    fig, ax = plt.subplots(figsize=(6.2, 2.5))
    ax.plot(t, 10 * (1 - np.exp(-t)), color=ACCENT, lw=2)
    ax.axhline(10, color=MUTED, ls="--", lw=1)
    ax.set_xlabel("t (µs)")
    ax.set_ylabel("i (mA)")
    ax.set_title("V = 10 V, R = 1 kΩ, L = 1 mH:  i(t) = 10(1 − $e^{-t/τ}$) mA,  τ = 1 µs", fontsize=10)
    return _plt(fig)


def rl_open():
    d = _d()
    d += (V := elm.SourceV().up().label("10 V"))
    d += elm.Switch(action="open").right().label("t = 0 (opens)")
    d += elm.Resistor().right().label("1 kΩ")
    d += elm.Inductor2().down().label("1 mH", loc="bottom")
    d += elm.Line().to(V.start)
    return _svg(d)


def rl_discharge():
    d = _d()
    d += (R := elm.Resistor().up().label("1 kΩ"))
    d += elm.Line().right()
    d += (L := elm.Inductor2().down().label("1 mH", loc="bottom"))
    d += elm.CurrentLabelInline(direction="in").at(L).label("i(t)")
    d += elm.Line().to(R.start)
    return _svg(d)


def rl_decay_plot():
    t = np.linspace(0, 6, 400)
    fig, ax = plt.subplots(figsize=(6.2, 2.4))
    ax.plot(t, 10 * np.exp(-t), color=ACCENT, lw=2)
    ax.set_xlabel("t (µs)")
    ax.set_ylabel("i (mA)")
    ax.set_title("R–L loop closed on itself after t = 0:  i(t) = 10·$e^{-t/τ}$ mA,  τ = 1 µs", fontsize=10)
    return _plt(fig)


ALL = {name: fn for name, fn in globals().items()
       if callable(fn) and not name.startswith("_") and fn.__module__ == __name__
}
