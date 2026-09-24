"""Concept figures for the MEE2003 study pack (matplotlib -> inline SVG).
Every plotted number comes from the pack's own worked problems (verified by script 2026-09-25)."""
import io
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK, ACC, WARN, OK, MUTED = "#1f2937", "#1d4ed8", "#b91c1c", "#15803d", "#6b7280"
plt.rcParams.update({
    "font.family": ["Segoe UI", "Arial", "DejaVu Sans"], "font.size": 10, "axes.edgecolor": "#9ca3af",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "svg.fonttype": "path", "axes.labelcolor": "#111827",
})


def _svg(fig):
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    s = buf.getvalue()
    return s[s.index("<svg"):]


def ppc():
    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    x = np.linspace(0, 1, 100)
    for r, c, lab in [(1.0, ACC, "PPC today"), (1.25, OK, "more resources / better tech"), (0.75, WARN, "fewer resources")]:
        ax.plot(r * x, r * np.sqrt(1 - x ** 2), color=c, lw=2 if r == 1 else 1.4, ls="-" if r == 1 else "--", label=lab)
    ax.plot(0.45, 0.45, "o", color=MUTED); ax.annotate("inside = idle resources", (0.45, 0.45), (0.5, 0.2),
                                                      arrowprops=dict(arrowstyle="->", color=MUTED), fontsize=8.5, color=MUTED)
    ax.set_xlabel("Roads built"); ax.set_ylabel("Other goods"); ax.set_xticks([]); ax.set_yticks([])
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    return _svg(fig)


def demand_shift():
    fig, (a, b) = plt.subplots(1, 2, figsize=(7.2, 2.9))
    q = np.linspace(1, 9, 50)
    a.plot(q, 10 - q, color=ACC, lw=2)
    a.annotate("", (6, 4), (3, 7), arrowprops=dict(arrowstyle="->", color=WARN, lw=1.6))
    a.plot([3, 6], [7, 4], "o", color=WARN)
    a.set_title("Change in QUANTITY demanded\n(own price → move along)", fontsize=9.5)
    b.plot(q, 10 - q, color=ACC, lw=2, label="D₁")
    b.plot(q, 12 - q, color=OK, lw=2, label="D₂ (increase)")
    b.plot(q, 8 - q, color=WARN, lw=1.5, ls="--", label="D₃ (decrease)")
    b.set_title("Change in DEMAND\n(other factor → whole curve shifts)", fontsize=9.5)
    b.legend(fontsize=8, frameon=False)
    for ax in (a, b):
        ax.set_xlabel("Quantity"); ax.set_ylabel("Price"); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(0, 12)
    fig.tight_layout()
    return _svg(fig)


def tax_p1():
    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    P = np.linspace(1.4, 4.2, 100)
    ax.plot(0.5 * (5 - P), P, color=ACC, lw=2, label="Demand  Xd = ½(5 − P)")
    ax.plot(2 * P - 3, P, color=OK, lw=2, label="Supply  Xs = 2P − 3")
    ax.plot(2 * (P - 1.2) - 3, P, color=WARN, lw=2, ls="--", label="Supply with tax  2(P − 6/5) − 3")
    ax.plot(1.4, 2.2, "o", color=INK); ax.annotate("E: P = 2.20, Q = 1.40", (1.4, 2.2), (1.55, 1.75), fontsize=8.5)
    ax.plot(0.92, 3.16, "o", color=WARN); ax.annotate("E′: P′ = 3.16, Q′ = 0.92", (0.92, 3.16), (0.1, 3.75), fontsize=8.5, color=WARN,
                                                       arrowprops=dict(arrowstyle="->", color=WARN))
    ax.hlines(1.96, 0, 0.92, color=MUTED, ls=":"); ax.annotate("seller gets 1.96", (0.02, 1.99), fontsize=8, color=MUTED)
    ax.set_xlim(0, 2.2); ax.set_ylim(1.4, 4.9); ax.set_xlabel("Quantity X"); ax.set_ylabel("Price P (₹)")
    ax.legend(fontsize=7.8, frameon=False, loc="upper right")
    return _svg(fig)


def elasticity_degrees():
    fig, axs = plt.subplots(1, 5, figsize=(9.2, 2.2))
    q = np.linspace(0.5, 4, 50)
    data = [("E = ∞\nperfectly elastic", [0.5, 4], [2, 2]), ("E = 0\nperfectly inelastic", [2, 2], [0.5, 4]),
            ("E = 1\nunitary", q, 2 / q * 1.2), ("E > 1\nrelatively elastic", q, 3 - 0.35 * q),
            ("E < 1\nrelatively inelastic", q, 5 - 1.2 * q)]
    for ax, (t, x, y) in zip(axs, data):
        ax.plot(x, y, color=ACC, lw=2); ax.set_title(t, fontsize=8.5)
        ax.set_xlim(0, 4.3); ax.set_ylim(0, 4.3); ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlabel("Q", fontsize=8); ax.set_ylabel("P", fontsize=8)
    fig.tight_layout()
    return _svg(fig)


def cloud_eac():
    fig, ax = plt.subplots(figsize=(5.0, 2.6))
    ax.barh(["A on-demand", "B reserved"], [180000, 84000], color=ACC, label="running cost / yr")
    ax.barh(["B reserved"], [100529], left=[84000], color="#93c5fd", label="upfront × (A/P,10%,3)")
    for y, v in [(0, 180000), (1, 184529)]:
        ax.text(v + 3000, y, f"₹{v:,}", va="center", fontsize=9)
    ax.axvline(140000, color=WARN, ls="--"); ax.text(140000, 1.42, "slide's 1,40,000 ✗", color=WARN, fontsize=8, ha="center")
    ax.set_xlim(0, 225000); ax.set_xlabel("Equivalent annual cost (₹)"); ax.legend(fontsize=8, frameon=False, loc="lower right")
    return _svg(fig)


def estimate_accuracy():
    fig, ax = plt.subplots(figsize=(5.2, 1.9))
    for y, (lo, hi, lab, c) in enumerate([(-5, 10, "Definitive (late, full design)", OK), (-50, 100, "ROM (earliest, ballpark)", WARN)]):
        ax.barh(y, hi - lo, left=lo, color=c, alpha=0.8, height=0.5)
        ax.text(hi + 3, y, f"{lo:+d}% … {hi:+d}%", va="center", fontsize=9)
    ax.set_yticks([0, 1]); ax.set_yticklabels(["Definitive", "ROM"]); ax.axvline(0, color=INK, lw=0.8)
    ax.set_xlim(-60, 135); ax.set_xlabel("error vs actual cost (%)")
    return _svg(fig)


def eoq_curve():
    D, S, H = 1200, 20, 8.4
    Q = np.linspace(15, 250, 300)
    oc, hc = D / Q * S, Q / 2 * H
    fig, ax = plt.subplots(figsize=(5.4, 3.3))
    ax.plot(Q, oc, color=WARN, lw=1.6, label="ordering (D/Q)·S")
    ax.plot(Q, hc, color=OK, lw=1.6, label="holding (Q/2)·H")
    ax.plot(Q, oc + hc, color=ACC, lw=2.4, label="total inventory cost")
    q = np.sqrt(2 * D * S / H)
    ax.axvline(q, color=MUTED, ls=":"); ax.plot(q, 2 * D / q * S, "o", color=ACC)
    ax.annotate(f"Q* = {q:.1f}\nTC = ₹{2 * D / q * S:.0f}\n(ordering = holding)", (q, 635), (q + 45, 950), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=MUTED))
    ax.plot(100, 660, "s", color=INK); ax.annotate("current Q = 100: ₹660", (100, 660), (150, 300), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=MUTED))
    ax.set_ylim(0, 1400); ax.set_xlabel("Order quantity Q (batteries)"); ax.set_ylabel("₹ per year")
    ax.legend(fontsize=8, frameon=False); ax.set_title("Battery problem: D = 1200, S = ₹20, H = ₹8.40", fontsize=9.5)
    return _svg(fig)


def payback_cumulative():
    flows = [70000, 60000, 55000, 40000, 30000, 25000]
    cum = np.cumsum(flows)
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    ax.bar(range(1, 7), cum / 1000, color=[ACC if c < 200000 else "#93c5fd" for c in cum])
    ax.axhline(200, color=WARN, ls="--"); ax.text(0.55, 206, "investment $200k", color=WARN, fontsize=8.5)
    ax.axvline(3.375, color=INK, ls=":"); ax.text(3.45, 40, "payback\n3.375 yr", fontsize=8.5)
    ax.set_xlabel("Year"); ax.set_ylabel("Cumulative inflow ($ thousand)")
    return _svg(fig)


def discounting():
    yrs = np.arange(0, 6)
    fig, ax = plt.subplots(figsize=(5.0, 2.8))
    v = 1000 / 1.1 ** yrs
    ax.bar(yrs, v, color=ACC)
    for y, x in zip(yrs, v):
        ax.text(y, x + 15, f"{x:.0f}", ha="center", fontsize=8.5)
    ax.set_xlabel("Years until the $1000 arrives"); ax.set_ylabel("Worth today at 10% ($)")
    ax.set_title("P = F / (1+i)ⁿ : the further away, the less it is worth", fontsize=9.5)
    return _svg(fig)


def npv_irr():
    r = np.linspace(0.0, 0.30, 200)
    f = lambda i: -50000 + 15000 * (1 - (1 + i) ** -5) / i if i else 25000
    y = np.array([f(i) for i in r])
    fig, ax = plt.subplots(figsize=(5.4, 3.3))
    ax.plot(r * 100, y / 1000, color=ACC, lw=2, label="NPV of the machine")
    ax.axhline(0, color=INK, lw=0.8)
    pts = [(0.10, 6861.80), (0.15, 282.33), (0.20, -5140.82)]
    for i, v in pts:
        ax.plot(i * 100, v / 1000, "o", color=OK if v > 0 else WARN)
        ax.annotate(f"{v:+,.0f}", (i * 100, v / 1000), (i * 100 + 0.6, v / 1000 + 1.2), fontsize=8.5)
    ax.plot([15, 20], [0.28233, -5.14082], color=WARN, ls="--", lw=1.2, label="interpolation chord")
    ax.plot(15.24, 0, "*", color=INK, ms=10); ax.annotate("IRR ≈ 15.24 %\n(chord: 15.26 %)", (15.24, 0), (19, 4), fontsize=8.5,
                                                          arrowprops=dict(arrowstyle="->", color=MUTED))
    ax.set_xlabel("Discount rate i (%)"); ax.set_ylabel("NPV ($ thousand)"); ax.legend(fontsize=8, frameon=False)
    return _svg(fig)


def furnace_rate():
    r = np.linspace(0.01, 0.40, 200)
    y = -100 + 20 * (1 - (1 + r) ** -10) / r
    fig, ax = plt.subplots(figsize=(5.0, 2.8))
    ax.plot(r * 100, y, color=ACC, lw=2); ax.axhline(0, color=INK, lw=0.8)
    ax.plot(10, 22.89, "o", color=OK); ax.annotate("10%: +22.9 → high-eff", (10, 22.89), (13, 40), fontsize=8.5)
    ax.plot(30, -38.17, "o", color=WARN); ax.annotate("30%: −38.2 → standard", (30, -38.17), (18, -55), fontsize=8.5)
    ax.set_xlabel("Discount rate (%)"); ax.set_ylabel("NPV of paying $100 more ($)")
    ax.set_title("Furnace: extra $100 now to save $20/yr for 10 yr", fontsize=9.5)
    return _svg(fig)


ALL = {k: v for k, v in globals().items() if callable(v) and not k.startswith("_") and k not in ("np", "plt")}
