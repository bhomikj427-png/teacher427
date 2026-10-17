"""Batch 6a check: Sadiku 5e Thevenin/Norton, PP 4.8-4.12 and Probs. 4.33-4.48.

V_oc and I_sc by netlist solves (I_sc through a 0 V source a->b), R_th = V_oc/I_sc, plus a test-source
R_th with independent sources off, plus the loaded circuit where the question asks for a load quantity.
Run: python verify_b6a.py
"""
from verify import solve


def thev(n, e, a, b=0):
    V, _ = solve(n, e)
    voc = (V[a] - V[b]).real
    _, I = solve(n, e + [("V", "_sc", a, b, 0)])
    isc = I["_sc"].real
    return voc, isc, (voc / isc if abs(isc) > 1e-12 else float("inf"))


def rtest(n, e, a, b=0):
    off = [(x[:4] + (0,)) if (x[0] == "V" and not x[1].startswith(("am", "_"))) else
           (x[:3] + (0,)) if x[0] == "I" else x for x in e]
    V, _ = solve(n, off + [("I", b, a, 1)])
    return (V[a] - V[b]).real


def rep(name, n, e, a, b=0, ref=""):
    voc, isc, r = thev(n, e, a, b)
    print(f"{name:8s} Voc {voc:+.5f}  Isc {isc:+.5f}  Rth {r:+.5f}  Rtest {rtest(n, e, a, b):+.5f}   {ref}")
    return voc, isc, r


rep("PP4.8", 3, [("V", "s", 1, 0, 12), ("Z", 1, 2, 6), ("I", 0, 2, 2), ("Z", 2, 3, 6), ("Z", 3, 0, 4)], 3,
    ref="book 6 V, 3 Ω, I = 1.5 A")
V, _ = solve(3, [("V", "s", 1, 0, 12), ("Z", 1, 2, 6), ("I", 0, 2, 2), ("Z", 2, 3, 6), ("Z", 3, 0, 4), ("Z", 3, 0, 1)])
print("   PP4.8 I", V[3].real)
# PP4.9: 1 = 6V+, 2 = M, 4 = after ammeter (Ix), 3 = a
rep("PP4.9", 4, [("V", "s", 1, 0, 6), ("Z", 1, 2, 5), ("V", "am", 2, 4, 0), ("Z", 4, 3, 3), ("F", 0, 2, "am", 1.5),
                 ("Z", 3, 0, 4)], 3, ref="book 5.333 V, 444.4 mΩ")
# PP4.10: 1 = top of 5 Ω (vx), 2 = between 10 Ω and dep, 3 = a ; dep V2 - V3 = 4 vx
rep("PP4.10", 3, [("Z", 1, 0, 5), ("Z", 1, 2, 10), ("E", "d", 2, 3, 1, 0, 4), ("Z", 3, 0, 15)], 3,
    ref="book 0 V, −7.5 Ω (test source only)")
rep("PP4.11", 3, [("V", "s", 1, 0, 15), ("Z", 1, 2, 3), ("I", 0, 2, 4), ("Z", 2, 3, 3), ("Z", 3, 0, 6)], 3,
    ref="book RN 3 Ω, IN 4.5 A")
# PP4.12: 1 = left top, 2 = a ; dep V1 - V2 = 2 vx, vx = V2
rep("PP4.12", 2, [("Z", 1, 0, 6), ("I", 0, 1, 10), ("E", "d", 1, 2, 2, 0, 2), ("Z", 2, 0, 2)], 2,
    ref="book RN 1 Ω, IN 10 A")
rep("4.33", 2, [("I", 0, 1, 4), ("Z", 1, 0, 10), ("Z", 1, 2, 10)], 2, ref="App D 40 V, 20 Ω, 1.6 A")
rep("4.34", 3, [("V", "s", 1, 0, 12), ("Z", 1, 2, 6), ("Z", 2, 0, 3), ("Z", 2, 3, 2), ("I", 2, 3, 1)], 3,
    ref="design: 6 V, 4 Ω")
# 4.35 = 4.12 circuit, 5 Ω removed, terminals A(2)-B(3)
rep("4.35", 4, [("V", "s12", 1, 0, 12), ("Z", 1, 2, 6), ("Z", 2, 0, 3), ("Z", 3, 0, 12), ("Z", 3, 4, 4),
                ("V", "s19", 4, 0, 19), ("I", 3, 2, 2)], 2, 3, ref="App D −125 mV (vo = Vth·5/(Rth+5))")
# 4.36: terminals = top node (1) and node 2 (top of 30 V, bottom of 12 Ω)
rep("4.36", 3, [("Z", 1, 3, 10), ("V", "s50", 3, 0, 50), ("Z", 1, 0, 40), ("V", "s30", 2, 0, 30)], 1, 2,
    ref="even; i = (Vth)/(Rth+12)")
# 4.37: 1 = 120V+, 2 = P, 3 = a; 2 A pushes from a into P
rep("4.37", 3, [("V", "s", 1, 0, 120), ("Z", 1, 2, 20), ("Z", 2, 3, 40), ("I", 3, 2, 2), ("Z", 3, 0, 12)], 3,
    ref="App D 10 Ω, 666.7 mA")
# 4.38: 1 = left top, 2 = M, 3 = 12V+ (below 5 Ω), 4 = output node
voc, isc, r = rep("4.38", 4, [("I", 0, 1, 3), ("Z", 1, 0, 16), ("Z", 1, 2, 4), ("Z", 2, 3, 5), ("V", "s", 3, 0, 12),
                              ("Z", 2, 4, 1)], 4, ref="even")
print("   4.38 Vo", voc * 10 / (r + 10))
# 4.39: 1 = 24V+, 2 = TL, 3 = M, 4 = a ; 3 A from a into TL
rep("4.39", 4, [("V", "s", 1, 0, 24), ("Z", 1, 2, 10), ("Z", 2, 3, 10), ("Z", 3, 0, 5), ("Z", 3, 4, 16), ("I", 4, 2, 3)],
    4, ref="App D 20 Ω, −49.2 V")
# 4.40: 1 = 70V+, 2 = a, 3 = dep top ; Vo = V1 - V2 ; V3 = 4 Vo
rep("4.40", 3, [("V", "s", 1, 0, 70), ("Z", 1, 2, 10e3), ("Z", 2, 3, 20e3), ("E", "d", 3, 0, 1, 2, 4)], 2, ref="even")
# 4.41: 1 = left top, 2 = between 14 V and 14 Ω, 3 = a. 14 V: + on right
rep("4.41", 3, [("I", 0, 1, 1), ("Z", 1, 0, 6), ("V", "s", 2, 1, 14), ("Z", 2, 3, 14), ("I", 3, 0, 3), ("Z", 3, 0, 5)],
    3, ref="App D 4 Ω, −8 V, −2 A")
# 4.42: 1 = a, 2 = 30V+, 3 = M, 4 = B(b), 5 = U (top of 20 V source, − at top)
rep("4.42", 5, [("Z", 1, 2, 10), ("V", "s30", 2, 0, 30), ("Z", 1, 3, 10), ("I", 0, 3, 5), ("Z", 3, 0, 10),
                ("Z", 3, 4, 20), ("Z", 3, 5, 20), ("V", "s20", 4, 5, 20), ("Z", 4, 0, 10)], 1, 4, ref="even")
# 4.43: 1 = 20V+, 2 = a, 3 = b
voc, isc, r = rep("4.43", 3, [("V", "s", 1, 0, 20), ("Z", 1, 2, 10), ("Z", 2, 0, 10), ("Z", 3, 0, 5), ("I", 0, 3, 2)],
                  2, 3, ref="App D 10 Ω, 0 V")
V, _ = solve(3, [("V", "s", 1, 0, 20), ("Z", 1, 2, 10), ("Z", 2, 0, 10), ("Z", 3, 0, 5), ("I", 0, 3, 2), ("Z", 3, 2, 6)])
print("   4.43 ix (b->a)", ((V[3] - V[2]) / 6).real)
# 4.44: 1 = 24V+, 5 = between 24V− and 2 Ω, 2 = N, 3 = a, 4 = b, c = ground
e44 = [("V", "s", 1, 5, 24), ("Z", 5, 0, 2), ("Z", 1, 2, 3), ("Z", 2, 3, 1), ("Z", 2, 4, 4), ("Z", 4, 0, 5), ("I", 0, 4, 2)]
rep("4.44ab", 5, e44, 3, 4, ref="even")
rep("4.44bc", 5, e44, 4, 0, ref="even")
rep("4.45", 2, [("I", 0, 1, 4), ("Z", 1, 0, 6), ("Z", 1, 2, 6), ("Z", 2, 0, 4)], 2, ref="App D 3 Ω, 2 A")
rep("4.46", 2, [("I", 0, 1, 6), ("Z", 1, 0, 4), ("Z", 1, 2, 4), ("Z", 2, 0, 8)], 2, ref="design: 3 A, 4 Ω")
# 4.47: 1 = 30V+, 2 = a ; dep 2Vx down, Vx = V2
rep("4.47", 2, [("V", "s", 1, 0, 30), ("Z", 1, 2, 12), ("Z", 2, 0, 60), ("G", 2, 0, 2, 0, 2)], 2,
    ref="App D 1.1905 V, 476.2 mΩ, 2.5 A")
# 4.48: 1 = N, 4 = below ammeter (io through 4 Ω), 2 = right of dep, 3 = a ; dep V1 - V2 = 10 io
rep("4.48", 4, [("I", 0, 1, 2), ("V", "am", 1, 4, 0), ("Z", 4, 0, 4), ("H", "d", 1, 2, "am", 10), ("Z", 2, 3, 2)], 3,
    ref="even")
