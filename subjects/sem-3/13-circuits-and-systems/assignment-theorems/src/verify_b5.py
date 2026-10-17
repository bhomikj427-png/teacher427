"""Batch 5 check: Sadiku 5e section 4.4 source transformation (PP 4.6-4.7, Probs. 4.20-4.32).

Every circuit is solved as drawn (full netlist, no transformation), so the source-transformation
answers in the write-up are checked by a different route. Run: python verify_b5.py
"""
from verify import solve


def show(name, val, ref=""):
    print(f"{name:10s} {val.real:+.5f}" + (f"   book: {ref}" if ref else ""))


# PP 4.6: 1 = L (top of 6Ω/5A/3Ω), 2 = M, 3 = R. 5 V: + on the right (M side)
V, _ = solve(3, [("Z", 1, 0, 6), ("I", 0, 1, 5), ("Z", 1, 0, 3), ("V", "s", 2, 1, 5), ("Z", 2, 0, 7),
                 ("I", 0, 2, 3), ("Z", 2, 3, 1), ("Z", 3, 0, 4)])
show("PP4.6 io", V[2] / 7, "1.78 A")
# PP 4.7: 1 = top node, 2 = top of dependent source (− at top): V2 = −2 ix, ix = V1/10
V, _ = solve(2, [("I", 0, 1, 0.024), ("Z", 1, 0, 10), ("Z", 1, 2, 5), ("E", "d", 0, 2, 1, 0, 0.2)])
show("PP4.7 ix", V[1] / 10, "7.059 mA")
# 4.20: Thevenin of the whole thing at the rails
e = [("I", 0, 1, 3), ("Z", 1, 0, 10), ("Z", 1, 2, 20), ("V", "a", 2, 0, 12), ("Z", 1, 3, 40), ("V", "b", 3, 0, 16)]
V, _ = solve(3, e); voc = V[1]
_, I = solve(3, e + [("V", "_sc", 1, 0, 0)])
show("4.20 Vth", voc, "even (160/7)"); show("4.20 Rth", voc / I["_sc"], "even (40/7)")
# 4.21 sample design V=20, R1=5, R2=20, I=2
V, _ = solve(2, [("V", "s", 1, 0, 20), ("Z", 1, 2, 5), ("Z", 2, 0, 20), ("I", 0, 2, 2)])
show("4.21 vo", V[2], "design (24 V)"); show("4.21 io", (20 - V[2]) / 5, "design (-0.8 A)")
# 4.22: 2 A downward on the left
V, _ = solve(3, [("I", 1, 0, 2), ("Z", 1, 0, 5), ("Z", 1, 2, 5), ("Z", 2, 0, 4), ("Z", 2, 3, 10), ("V", "s", 3, 0, 20)])
show("4.22 i", V[2] / 4, "even")
# 4.23
V, _ = solve(3, [("I", 0, 1, 3), ("Z", 1, 0, 10), ("Z", 1, 2, 8), ("Z", 2, 0, 6), ("Z", 2, 3, 3), ("V", "s", 3, 0, 15)])
i8 = (V[1] - V[2]) / 8
show("4.23 i8", i8, "1 A"); show("4.23 P8", abs(i8) ** 2 * 8, "8 W")
# 4.24: 1 = 40V+, 2 = A, 3 = B; Vx = V1 - V2; dep 2Vx up into B; 3 A from A to B
V, _ = solve(3, [("V", "s", 1, 0, 40), ("Z", 1, 2, 8), ("Z", 2, 3, 10), ("I", 2, 3, 3), ("Z", 3, 0, 10),
                 ("G", 0, 3, 1, 2, 2)])
show("4.24 Vx", V[1] - V[2], "even")
# 4.25: T1 = 1, T2 = 2, B1 = 3, X = 4 (between 2 Ω and 30 V), B2 = ground
V, _ = solve(4, [("I", 1, 3, 3), ("Z", 1, 3, 4), ("Z", 1, 2, 9), ("I", 1, 2, 2), ("Z", 2, 0, 5), ("I", 2, 0, 6),
                 ("Z", 3, 4, 2), ("V", "s", 4, 0, 30)])
show("4.25 vo", V[3] - V[4], "-6.6 V")
# 4.26: 1 = L, 2 = M, 3 = 20V+
V, _ = solve(3, [("I", 0, 1, 6), ("Z", 1, 0, 2), ("I", 1, 2, 3), ("Z", 1, 2, 5), ("Z", 2, 3, 4), ("V", "s", 3, 0, 20)])
show("4.26 io", (V[2] - V[3]) / 4, "even (7/11)")
# 4.27
V, _ = solve(4, [("V", "a", 1, 0, 50), ("Z", 1, 2, 10), ("Z", 2, 0, 40), ("Z", 2, 3, 12), ("I", 0, 3, 8),
                 ("Z", 3, 4, 20), ("V", "b", 4, 0, 40)])
show("4.27 vx", V[2] - V[3], "-48 V")
# 4.28: 1 = 8V+, 2 = after 1 Ω, 3 = B. Vo = V2 - V3; dep (1/3)Vo from B down to ground
V, _ = solve(3, [("V", "s", 1, 0, 8), ("Z", 1, 2, 1), ("Z", 2, 3, 4), ("Z", 3, 0, 3), ("G", 3, 0, 2, 3, 1 / 3)])
show("4.28 Io", (V[2] - V[3]) / 4, "even")
# 4.29: 1 = L, 2 = M, 3 = R (vo). dep: V3 - V2 = 3 vo
V, _ = solve(3, [("I", 0, 1, 0.003), ("Z", 1, 3, 4000), ("Z", 1, 2, 2000), ("E", "d", 3, 2, 3, 0, 3), ("Z", 3, 0, 1000)])
show("4.29 vo", V[3], "3 V")
# 4.30: 1 = 12V+, 4 = after ammeter, 2 = A, 3 = B
V, I = solve(4, [("V", "s", 1, 0, 12), ("V", "am", 1, 4, 0), ("Z", 4, 2, 24), ("Z", 2, 0, 30), ("Z", 2, 3, 60),
                 ("Z", 3, 0, 10), ("F", 0, 3, "am", 0.7)])
show("4.30 ix", I["am"], "even")
# 4.31: 1 = 12V+, 2 = M, 3 = dep top. vx = V1 - V2
V, _ = solve(3, [("V", "s", 1, 0, 12), ("Z", 1, 2, 3), ("Z", 2, 0, 8), ("Z", 2, 3, 6), ("E", "d", 3, 0, 1, 2, 2)])
show("4.31 vx", V[1] - V[2], "3.652 V")
# 4.32: 1 = 60V+, 4 = after ammeter, 2 = A, 3 = B
V, I = solve(4, [("V", "s", 1, 0, 60), ("V", "am", 1, 4, 0), ("Z", 4, 2, 15), ("Z", 2, 0, 50), ("Z", 2, 3, 10),
                 ("F", 2, 3, "am", 0.5), ("Z", 3, 0, 40)])
show("4.32 ix", I["am"], "even")
