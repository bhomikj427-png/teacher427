"""Batch 6b check: Sadiku 5e Thevenin/Norton, Probs. 4.49-4.65 (same method as verify_b6a.py)."""
from verify import solve
from verify_b6a import rep, rtest

# 4.49 (Fig. 4.102 with V = 40, I = 3, R1 = 10, R2 = 40, R3 = 20)
rep("4.49", 3, [("V", "s", 1, 0, 40), ("Z", 1, 2, 10), ("Z", 2, 0, 40), ("Z", 2, 3, 20), ("I", 2, 3, 3)], 3,
    ref="App D 28 Ω, 3.286 A")
# 4.50: left part only: 1 = top-left, 2 = after 6 Ω, 3 = a ; 12 V + on the left
rep("4.50L", 3, [("I", 0, 1, 2), ("Z", 1, 0, 4), ("Z", 1, 2, 6), ("V", "s", 2, 3, 12)], 3, ref="even (left of a-b)")
V, _ = solve(3, [("I", 0, 1, 2), ("Z", 1, 0, 4), ("Z", 1, 2, 6), ("V", "s", 2, 3, 12), ("Z", 3, 0, 5), ("I", 0, 3, 4)])
print("   4.50 i", V[3].real / 5)
# 4.51: 1 = 120V+, 2 = a, 3 = b (= c), d = ground
e = [("V", "s", 1, 0, 120), ("Z", 1, 2, 6), ("Z", 2, 0, 3), ("Z", 2, 3, 4), ("I", 0, 3, 6), ("Z", 3, 0, 2)]
rep("4.51ab", 3, e, 2, 3, ref="App D 2 Ω, 7 A")
rep("4.51cd", 3, e, 3, 0, ref="App D 1.5 Ω, 12.667 A")
# 4.52: 1 = 6V+, 2 = node after 3 kΩ (wired to ground through the io branch, via ammeter), 3 = a
rep("4.52", 3, [("V", "s", 1, 0, 6), ("Z", 1, 2, 3000), ("V", "am", 2, 0, 0), ("F", 3, 0, "am", 20), ("Z", 3, 0, 2000)],
    3, ref="even")
# 4.53: 1 = 18V+, 2 = M (vo), 3 = a ; 0.25 vo pushed from a into M
rep("4.53", 3, [("V", "s", 1, 0, 18), ("Z", 1, 2, 6), ("Z", 2, 0, 3), ("Z", 2, 3, 2), ("G", 3, 2, 2, 0, 0.25)], 3,
    ref="App D 3 Ω, 1 A")
# 4.54 = Chakraborty 5.27 with 50 Ω
rep("4.54", 4, [("V", "s", 1, 0, 3), ("V", "am", 1, 4, 0), ("Z", 4, 2, 1000), ("E", "d", 2, 0, 3, 0, 2),
                ("F", 3, 0, "am", 40), ("Z", 3, 0, 50)], 3, ref="even")
# 4.55: 1 = 2V+, 4 = after ammeter (I), 2 = top of 0.001Vab source, 3 = a
rep("4.55", 4, [("V", "s", 1, 0, 2), ("V", "am", 1, 4, 0), ("Z", 4, 2, 8000), ("E", "d", 2, 0, 3, 0, 0.001),
                ("F", 3, 0, "am", 80), ("Z", 3, 0, 50e3)], 3, ref="App D 100 kΩ, −20 mA")
# 4.56: 1 = 36V+, 2 = A, 3 = B, 4 = C (Vo)
voc, isc, r = rep("4.56", 4, [("V", "s", 1, 0, 36), ("Z", 1, 2, 12e3), ("Z", 2, 0, 24e3), ("Z", 2, 3, 2e3),
                              ("I", 3, 0, 3e-3), ("Z", 3, 4, 10e3)], 4, ref="even (Norton seen by 1 kΩ)")
print("   4.56 Vo", isc * (r * 1000 / (r + 1000)))
# 4.57: 1 = 50V+, 2 = X (vx), 3 = a ; 0.5 vx up into a
rep("4.57", 3, [("V", "s", 1, 0, 50), ("Z", 1, 2, 3), ("Z", 2, 0, 6), ("Z", 2, 3, 2), ("G", 0, 3, 2, 0, 0.5),
                ("Z", 3, 0, 10)], 3, ref="App D 10 Ω, 166.67 V, 16.667 A")
# 4.58 sample values R1 = 1k, R2 = 2k, b = 50: dependent current source alone feeds the output node
try:
    print("4.58 Rtest", rtest(3, [("V", "s", 1, 0, 1), ("V", "am", 1, 4, 0), ("Z", 4, 2, 1000), ("Z", 2, 0, 2000),
                                  ("F", 3, 2, "am", 50)], 3))
except Exception as ex:
    print("4.58 test source: singular (R_th infinite):", type(ex).__name__)
# 4.59: top rail 1, a 2, b 3, bottom ground
rep("4.59", 3, [("I", 0, 1, 8), ("Z", 1, 2, 10), ("Z", 2, 0, 50), ("Z", 1, 3, 20), ("Z", 3, 0, 40)], 2, 3,
    ref="App D 22.5 Ω, 40 V, 1.7778 A")
# 4.60: b = ground, a = 1, P = 2, Q = 3, X = 4 (between 10 V and 5 Ω); 18 V + at a; 10 V + on the a side
rep("4.60", 4, [("V", "s18", 1, 2, 18), ("Z", 2, 3, 4), ("I", 3, 2, 3), ("Z", 3, 0, 6), ("I", 1, 0, 2),
                ("V", "s10", 1, 4, 10), ("Z", 4, 0, 5)], 1, ref="even")
# 4.61: 1 = TL, 6 = below left 12V (above 2 Ω), 2 = TR (a), 3 = M, 4 = below M's 6 Ω (top of 12 V, − at top),
#       5 = below right 12 V (above 2 Ω), b = ground
rep("4.61", 6, [("V", "L", 1, 6, 12), ("Z", 6, 0, 2), ("Z", 1, 2, 2), ("Z", 1, 3, 6), ("Z", 2, 3, 6), ("Z", 3, 4, 6),
                ("V", "M", 0, 4, 12), ("V", "R", 2, 5, 12), ("Z", 5, 0, 2)], 2, ref="App D 1.2 Ω, 9.6 V, 8 A")
# 4.62: b = ground, M = 1, a = 2, BL = 3, 4 = below ammeter ; io through 20 Ω (M -> b); vo = V2 - V1
print("4.62 Rtest", rtest(4, [("V", "am", 1, 4, 0), ("Z", 4, 0, 20), ("F", 1, 2, "am", 0.1), ("Z", 2, 1, 10),
                              ("Z", 1, 3, 40), ("E", "d", 3, 0, 2, 1, 2)], 2), "(even; Vth = 0)")
print("4.63 Rtest", rtest(2, [("Z", 1, 0, 20), ("Z", 1, 2, 10), ("G", 0, 2, 1, 0, 0.5)], 2), "(App D −3.333 Ω, 0 A)")
# 4.64: 1 = dep top, 2 = N, 3 = a ; ix = V2 / 2 ; V1 = 10 ix = 5 V2
print("4.64 Rtest", rtest(3, [("E", "d", 1, 0, 2, 0, 5), ("Z", 1, 2, 4), ("Z", 2, 0, 2), ("Z", 2, 3, 1)], 3), "(even)")
rep("4.65", 3, [("V", "s", 1, 0, 32), ("Z", 1, 2, 4), ("Z", 2, 0, 12), ("Z", 2, 3, 2)], 3, ref="App D Vo = 24 − 5Io")
