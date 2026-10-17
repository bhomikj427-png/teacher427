"""Batch 7 check: Sadiku 5e section 4.8 maximum power (PP 4.13, Probs. 4.66-4.75).

Thevenin by netlist (verify_b6a.thev), then the load resistance is swept on the FULL circuit
(log-spaced, then refined) and the peak power compared with V_th^2 / (4 R_th).
Run: python verify_b7.py
"""
import numpy as np
from verify import solve
from verify_b6a import thev


def p_load(n, e, a, b, r):
    V, _ = solve(n, e + [("Z", a, b, r)])
    return abs(V[a] - V[b]) ** 2 / r


def sweep(n, e, a, b, lo=1e-3, hi=1e6):
    rs = np.geomspace(lo, hi, 4001)
    ps = [p_load(n, e, a, b, r) for r in rs]
    k = int(np.argmax(ps))
    fine = np.linspace(rs[max(k - 1, 0)], rs[min(k + 1, len(rs) - 1)], 4001)
    pf = [p_load(n, e, a, b, r) for r in fine]
    k = int(np.argmax(pf))
    return pf[k], fine[k]


def rep(name, n, e, a, b=0, ref=""):
    voc, isc, r = thev(n, e, a, b)
    pm = voc ** 2 / (4 * r) if r > 0 else float("nan")
    p, rb = sweep(n, e, a, b)
    print(f"{name:7s} Vth {voc:+.4f}  Rth {r:+.4f}  Pmax {pm:.5f} | sweep: R {rb:.4f}  P {p:.5f}   {ref}")
    return voc, r


rep("PP4.13", 4, [("V", "s", 1, 0, 9), ("Z", 1, 2, 2), ("Z", 2, 3, 1), ("E", "d", 3, 0, 1, 2, 3), ("Z", 2, 4, 4)], 4,
    ref="book 4.222 Ω, 2.901 W")
rep("4.66", 4, [("V", "s", 1, 0, 20), ("Z", 1, 2, 3), ("Z", 2, 3, 2), ("V", "t", 4, 3, 10), ("Z", 4, 0, 5),
                ("I", 4, 0, 6)], 2, 4, ref="even")
rep("4.67", 3, [("Z", 1, 2, 80), ("Z", 2, 3, 20), ("Z", 1, 0, 10), ("Z", 3, 0, 90), ("V", "s", 1, 3, 40)], 2,
    ref="App D 25 Ω, 7.84 W")
# 4.68: power in the 10 Ω as R varies (R in series with the 12 V)
best = None
for R in np.concatenate([[1e-9], np.geomspace(1e-4, 1e4, 20001)]):
    V, _ = solve(3, [("V", "s", 1, 0, 12), ("Z", 1, 2, R), ("Z", 2, 3, 10), ("V", "e", 3, 0, 8), ("Z", 2, 0, 20)])
    p = abs(V[2] - V[3]) ** 2 / 10
    if best is None or p > best[0]:
        best = (p, R)
print(f"4.68    best R {best[1]:.3g}  P10 {best[0]:.4f} W   (even)")
rep("4.69", 3, [("V", "s", 1, 0, 100), ("Z", 1, 2, 10e3), ("Z", 2, 0, 40e3), ("Z", 2, 3, 22e3),
                ("G", 0, 3, 2, 0, 0.003), ("Z", 3, 0, 30e3)], 3, ref="App D ∞ (theoretically)")
rep("4.70", 4, [("V", "s", 1, 0, 4), ("Z", 1, 2, 5), ("Z", 2, 0, 15), ("Z", 2, 3, 5), ("Z", 0, 4, 6),
                ("G", 2, 3, 0, 4, 3)], 3, 4, ref="even")
rep("4.71", 4, [("V", "s", 1, 0, 8), ("Z", 1, 2, 3000), ("Z", 2, 0, 1000), ("E", "d", 0, 3, 2, 0, 120),
                ("Z", 3, 4, 10e3), ("Z", 4, 0, 40e3)], 4, ref="App D 8 kΩ, 1.152 W")
e72 = [("I", 0, 1, 4), ("Z", 1, 0, 2), ("Z", 1, 2, 4), ("Z", 2, 3, 6), ("I", 2, 3, 2), ("V", "s", 0, 4, 20)]
voc, r = rep("4.72", 4, e72, 3, 4, ref="even")
V, _ = solve(4, e72 + [("Z", 3, 4, 8)])
print("   4.72 i(RL=8)", ((V[3] - V[4]) / 8).real)
rep("4.73", 3, [("V", "s", 1, 0, 60), ("Z", 1, 2, 10), ("Z", 1, 3, 25), ("Z", 2, 0, 20), ("Z", 3, 0, 5)], 2, 3,
    ref="App D 20.77 W")
# 4.74 sample values vs the formulas
vs, R1, R2, R3, R4 = 10, 2, 3, 4, 5
rep("4.74", 3, [("V", "s", 1, 0, vs), ("Z", 1, 2, R1), ("Z", 2, 0, R2), ("Z", 1, 3, R3), ("Z", 3, 0, R4)], 2, 3,
    ref=f"formula Rth {R1*R2/(R1+R2)+R3*R4/(R3+R4):.4f}, Vth {vs*(R2/(R1+R2)-R4/(R3+R4)):+.4f}")
R = 1000
rep("4.75", 4, [("V", "a", 1, 0, 1), ("V", "b", 2, 0, 2), ("V", "c", 3, 0, 3), ("Z", 1, 4, R), ("Z", 2, 4, R),
                ("Z", 3, 4, R)], 4, ref="App D R = 1 kΩ, 3 mW")
