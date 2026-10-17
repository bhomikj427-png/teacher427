"""Batch 2 check: Chakraborty 5.15-5.34 (Thevenin / Norton).

Every circuit is entered as a netlist from the book figure. For each one:
  Voc  = open-circuit voltage (load removed)
  Isc  = short-circuit current through a 0 V "ammeter" source placed across the terminals
  Zth  = Voc / Isc, cross-checked by a test-source solve (independent sources off) where useful
  plus the full circuit solved with the load in place (no theorem at all).
Transient problems (5.28, 5.30) are checked by integrating the circuit ODEs (RK4) against the
Laplace answer. Run: python verify_b2.py
"""
import cmath
import numpy as np
from verify import solve, pol

j = 1j
OUT = []


def show(k, v):
    v = complex(v)
    OUT.append((k, v))
    print(f"{k:40s} {v.real:+.5f}{v.imag:+.5f}j   {pol(v)}")


def thev(n, elems, a, b=0, extra_nodes=1):
    """Voc, Isc (a->b through the short), Zth for terminals a-b of the netlist (load removed)."""
    V, _ = solve(n, elems)
    voc = V[a] - V[b]
    _, I = solve(n, elems + [("V", "_sc", a, b, 0)])
    isc = I["_sc"]
    return voc, isc, (voc / isc if abs(isc) > 1e-15 else float("inf"))


def ztest(n, elems_off, a, b=0):
    """Zth by a 1 A test source into a (independent sources already switched off)."""
    V, _ = solve(n, elems_off + [("I", b, a, 1)])
    return V[a] - V[b]


# 5.15  1 = between 10V(-) and 1Ω, 2 = TL, 3 = middle, 4 = right top, 5 = between 5V(-) and 2Ω
e = [("Z", 1, 0, 1), ("V", "s1", 2, 1, 10), ("Z", 2, 3, 1), ("Z", 3, 0, 1), ("Z", 3, 4, 1),
     ("V", "s2", 4, 5, 5), ("Z", 5, 0, 2)]
voc, isc, zth = thev(5, e, 4)
show("5.15 Voc (45/11=4.0909)", voc); show("5.15 Rth (10/11=0.9091)", zth)
V, _ = solve(5, e + [("Z", 4, 0, 2)]); show("5.15 i full solve (45/32)", V[4] / 2)

# 5.16  1 = TL(10V+), 2 = a, 3 = x.  V0 = V2 - V1;  dep: V2 - V3 = 3 V0
e = [("V", "s", 1, 0, 10), ("Z", 1, 2, 1), ("I", 0, 2, 1), ("E", "d", 2, 3, 2, 1, 3)]
voc, isc, zth = thev(3, e, 3)
show("5.16 Voc", voc); show("5.16 Isc (x->y)", isc); show("5.16 Rth", zth)
show("5.16 Rth test source", ztest(3, [("V", "s", 1, 0, 0), ("Z", 1, 2, 1), ("E", "d", 2, 3, 2, 1, 3)], 3))
try:
    V, _ = solve(3, e + [("Z", 3, 0, 2)])
    show("5.16 I full solve", V[3] / 2)
except np.linalg.LinAlgError:
    print("5.16 full solve with 2 Ω load: SINGULAR (no solution)")
V, _ = solve(3, e + [("Z", 3, 0, 2.001)]); show("5.16 I with 2.001 Ω (blows up)", V[3] / 2.001)

# 5.17 ladder
e = [("V", "s", 1, 0, 100), ("Z", 1, 2, 90), ("Z", 2, 3, 10), ("Z", 3, 0, 1000), ("Z", 3, 4, 100),
     ("Z", 4, 0, 10), ("Z", 4, 5, 100), ("Z", 5, 0, 100), ("Z", 5, 6, 1000)]
voc, isc, zth = thev(6, e, 6)
show("5.17 Vth (1000/463=2.15983)", voc); show("5.17 Rth (487200/463=1052.27)", zth)
V, _ = solve(6, e + [("Z", 6, 0, 10)]); show("5.17 I full solve", V[6] / 10)

# 5.18 op-amp: 1 = 12V, 2 = e1, 3 = e2 (inverting), 4 = V0; ideal op-amp as gain 1e9
e = [("V", "s", 1, 0, 12), ("Z", 1, 2, 2000), ("Z", 2, 3, 8000), ("Z", 2, 4, 4000), ("Z", 3, 4, 12000),
     ("E", "oa", 4, 0, 0, 3, 1e9)]
voc, isc, zth = thev(4, e, 2)
show("5.18 Vth (4.8)", voc); show("5.18 Rth (800)", zth)
V, _ = solve(4, e + [("Z", 2, 0, 4000)]); show("5.18 I full solve (1 mA)", V[2] / 4000)

# 5.19 1 = TL, 2 = M, 3 = A, 4 = between 2Ω and dep source. Vs = V1 - V2; dep 4Vs up into 4
e = [("V", "s", 1, 0, 10), ("Z", 1, 2, 2), ("Z", 2, 4, 2), ("G", 0, 4, 1, 2, 4), ("Z", 2, 3, 4)]
voc, isc, zth = thev(4, e, 3)
show("5.19 Voc (10)", voc); show("5.19 Isc (45/19=2.3684)", isc); show("5.19 Rth (38/9=4.2222)", zth)
show("5.19 Rth test source", ztest(4, [("V", "s", 1, 0, 0), ("Z", 1, 2, 2), ("Z", 2, 4, 2), ("G", 0, 4, 1, 2, 4),
                                      ("Z", 2, 3, 4)], 3))

# 5.20
e = [("V", "s1", 1, 0, 100), ("Z", 1, 2, 4j), ("Z", 2, 0, -8j), ("Z", 3, 0, -6j), ("Z", 3, 4, 4j),
     ("V", "s2", 4, 0, 100 * cmath.exp(1j * np.radians(60)))]
voc, isc, zth = thev(4, e, 2, 3)
show("5.20 Vth (50-j259.81)", voc); show("5.20 Zth (j20)", zth)
V, _ = solve(4, e + [("Z", 2, 3, 8j)]); show("5.20 i a->b full solve (9.45∠-169.1)", (V[2] - V[3]) / 8j)

# 5.21(a) 1 = T, 2 = P, 3 = A
e = [("I", 2, 1, 10), ("Z", 1, 2, 15j), ("Z", 2, 0, 3), ("Z", 1, 3, 2), ("Z", 3, 0, -5j)]
voc, isc, zth = thev(3, e, 3)
show("5.21a Vth (67.08∠-63.4)", voc); show("5.21a Zth (7.07∠-81.86)", zth)
# (b)
e = [("V", "s", 1, 0, 20j), ("Z", 1, 2, 5 + 10j), ("Z", 2, 0, 3 - 4j)]
voc, isc, zth = thev(2, e, 2)
show("5.21b Vth (10∠0)", voc); show("5.21b Zth (5.59∠-26.56)", zth)
# (c) 4 Ω across AB treated as the load
e = [("V", "s", 1, 0, 100), ("Z", 1, 2, 10), ("Z", 2, 0, -5j), ("Z", 2, 3, 5), ("Z", 3, 0, 8 + 6j)]
voc, isc, zth = thev(3, e, 3)
show("5.21c Vth (29.553∠-34.16)", voc); show("5.21c Zth (5.33∠-0.5)", zth)
V, _ = solve(3, e + [("Z", 3, 0, 4)]); show("5.21c V_AB with 4 Ω in place", V[3])
show("5.21c   same via Thevenin", voc * 4 / (zth + 4))
# (d) s-domain at sample s values
for s in (1.0, 0.5 + 2j, 3j):
    vs = 2 * s / (s * s + 4)
    e = [("V", "s", 1, 0, vs), ("Z", 1, 2, 1), ("Z", 2, 3, s / 2), ("Z", 3, 4, 1), ("Z", 4, 0, 4 / s),
         ("Z", 4, 0, 4 / s)]
    voc, isc, zth = thev(4, e, 3)
    show(f"5.21d s={s}: Vth - 4s/((s²+4)(s+2))", voc - 4 * s / ((s * s + 4) * (s + 2)))
    show(f"5.21d s={s}: Zth (1)", zth)
# (e) 1 = src+, 4 = after ammeter, 2 = P, 3 = A; dep 5I pushed from A to P
e = [("V", "s", 1, 0, 10), ("V", "am", 1, 4, 0), ("Z", 4, 2, 100), ("Z", 2, 0, 10j), ("Z", 2, 3, -5j),
     ("F", 3, 2, "am", 5)]
voc, isc, zth = thev(4, e, 3)
show("5.21e Vth (3.48∠84.3)", voc); show("5.21e IN (0.6∠31)", isc); show("5.21e Zth (5.8∠53.3)", zth)
show("5.21e Zth test source", ztest(4, [("V", "s", 1, 0, 0), ("V", "am", 1, 4, 0), ("Z", 4, 2, 100),
                                       ("Z", 2, 0, 10j), ("Z", 2, 3, -5j), ("F", 3, 2, "am", 5)], 3))

# 5.22 ω = 1. 1 = source top (−), 4 = after ammeter, 2 = P, 3 = Q. + of source at bottom
e = [("V", "s", 0, 1, 12), ("V", "am", 1, 4, 0), ("Z", 4, 2, 4), ("Z", 2, 0, -4j), ("Z", 2, 3, 2j),
     ("F", 2, 3, "am", 3), ("Z", 3, 0, -8j)]
voc, isc, zth = thev(4, e, 3)
show("5.22 Vth (book 4.8∠-36.87)", voc); show("5.22 IN (book 1.341∠63.435)", isc)
show("5.22 Zth (book 3.58∠-100.3)", zth)
V, _ = solve(4, e + [("Z", 3, 0, 2)]); show("5.22 V0 full solve (book 1.27∠32)", V[3])
show("5.22   same via Thevenin", voc * 2 / (zth + 2))
# book's Vth if the −j4 is dropped from mesh 2 (reproduces its slip)
I1, I2 = np.linalg.solve(np.array([[4 - 4j, 4j], [-2j, -6j]]), np.array([-12, 0]))
show("5.22 book's slip reproduced: I2(-j8)", I2 * -8j)

# 5.23
e = [("V", "a", 1, 0, 10), ("Z", 1, 2, 5), ("Z", 2, 3, 15), ("V", "b", 3, 0, 20)]
voc, isc, zth = thev(3, e, 2)
show("5.23 Vth (12.5)", voc); show("5.23 IN (10/3)", isc); show("5.23 RN (3.75)", zth)

# 5.25 1 = 5V+, 2 = middle, 3 = A
e = [("V", "s", 1, 0, 5), ("Z", 1, 0, 2), ("Z", 1, 0, 2), ("Z", 1, 2, 2), ("Z", 2, 0, 1), ("I", 0, 2, 2),
     ("Z", 2, 3, 1)]
voc, isc, zth = thev(3, e, 3)
show("5.25 Vth (3)", voc); show("5.25 IN (9/5)", isc); show("5.25 Rth (5/3)", zth)
_, I = solve(3, [("V", "s", 1, 0, 5), ("Z", 1, 0, 2), ("Z", 1, 0, 2), ("Z", 1, 2, 2), ("Z", 2, 0, 1),
                 ("I", 0, 2, 0), ("Z", 2, 3, 1), ("V", "_sc", 3, 0, 0)])
show("5.25 Isc' (5 V alone, 1)", I["_sc"])

# 5.26 (the book's SOLUTION circuit: 10 mV, 1 kΩ, VCVS 1e-4·V0, CCCS 75 I down, 30 kΩ)
e = [("V", "s", 1, 0, 0.01), ("V", "am", 1, 4, 0), ("Z", 4, 2, 1000), ("E", "h", 2, 0, 3, 0, 1e-4),
     ("F", 3, 0, "am", 75), ("Z", 3, 0, 30000)]
voc, isc, zth = thev(4, e, 3)
show("5.26 Voc (book -29)", voc); show("5.26 Isc (book -7.5e-4)", isc); show("5.26 Rth (book 38.67k)", zth)
show("5.26 Rth test source", ztest(4, [("V", "s", 1, 0, 0), ("V", "am", 1, 4, 0), ("Z", 4, 2, 1000),
                                      ("E", "h", 2, 0, 3, 0, 1e-4), ("F", 3, 0, "am", 75), ("Z", 3, 0, 30000)], 3))

# 5.27 1 = 3V+, 4 = after ammeter, 2 = top of 2Vx, 3 = a
for R in (50e3, 50):
    e = [("V", "s", 1, 0, 3), ("V", "am", 1, 4, 0), ("Z", 4, 2, 1000), ("E", "d", 2, 0, 3, 0, 2),
         ("F", 3, 0, "am", 40), ("Z", 3, 0, R)]
    voc, isc, zth = thev(4, e, 3)
    show(f"5.27 R={R:g}: Voc", voc); show(f"5.27 R={R:g}: Isc a->b", isc); show(f"5.27 R={R:g}: Rth", zth)
    off = [("V", "s", 1, 0, 0)] + e[1:]
    show(f"5.27 R={R:g}: Rth test source", ztest(4, off, 3))

# 5.29 1 = top node T, 2 = a. Dep current v1/100 up into T (v1 = V2), 100 V with + at T
e = [("G", 0, 1, 2, 0, 0.01), ("Z", 1, 0, 20), ("V", "s", 1, 2, 100)]
voc, isc, zth = thev(2, e, 2)
show("5.29 Voc (-125)", voc); show("5.29 Isc (-5)", isc); show("5.29 Rth (25)", zth)

# 5.31 random a, b, V1 vs the formulas
for (a, bb, v1) in ((0.3, 0.7, 5.0), (2.0, -1.5, 3.0)):
    e = [("V", "s", 1, 0, v1), ("V", "am", 1, 5, 0), ("Z", 5, 2, 1), ("Z", 2, 3, 1), ("E", "a", 3, 0, 1, 0, a),
         ("H", "b", 4, 2, "am", bb), ("Z", 4, 6, 1)]
    voc, isc, zth = thev(6, e, 6)
    show(f"5.31 a={a},b={bb}: Vth - formula", voc - v1 / 2 * (1 + a + bb - a * bb))
    show(f"5.31 a={a},b={bb}: Zth - (3-b)/2", zth - (3 - bb) / 2)

# 5.32
e = [("I", 0, 1, 5 * cmath.exp(1j * np.radians(30))), ("Z", 1, 0, 50 + 50j), ("Z", 1, 2, 100), ("Z", 2, 0, 50 + 50j)]
voc, isc, zth = thev(2, e, 2)
show("5.32 Vth (111.8∠93.43)", voc); show("5.32 Zth (50∠36.87)", zth)

# 5.33 1 = 12V+, 3 = after ammeter, 2 = A
e = [("V", "s", 1, 0, 12), ("V", "am", 1, 3, 0), ("Z", 3, 2, 10), ("F", 0, 2, "am", 2), ("Z", 2, 0, 5)]
voc, isc, zth = thev(3, e, 2)
show("5.33 Vth (7.2)", voc); show("5.33 Isc (3.6)", isc); show("5.33 Rth (2)", zth)

# 5.34 1 = top of 20 Ω (v0), 2 = x
show("5.34 Zth (-10/3)", ztest(2, [("Z", 1, 0, 20), ("Z", 1, 2, 10), ("G", 0, 2, 1, 0, 0.5)], 2))
V, _ = solve(2, [("Z", 1, 0, 20), ("Z", 1, 2, 10), ("G", 0, 2, 1, 0, 0.5)])
show("5.34 Voc (0)", V[2])


# ---- transients by direct ODE integration ----
def rk4(f, x0, T, n=200000):
    h = T / n
    x = np.array(x0, float)
    for _ in range(n):
        k1 = f(x); k2 = f(x + h / 2 * k1); k3 = f(x + h / 2 * k2); k4 = f(x + h * k3)
        x = x + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return x


# 5.28 state [iL1, vC, iL2]; figure C = 2 F (book's Laplace network uses 1/s, i.e. C = 1 F)
for C in (2, 1):
    f = lambda x: np.array([(3 - 2 * x[0] - x[1]) / 1, (x[0] - x[2]) / C, (x[1] - 2 * x[2]) / 1])
    for T in (0.5, 1.0, 3.0):
        sim = rk4(f, [0, 0, 0], T, 20000)[2]
        ours = 0.75 - 0.75 * np.exp(-2 * T) - 1.5 * T * np.exp(-T)
        book = 0.75 - 0.75 * np.exp(-2 * T) - 1.5 * np.exp(-T) * np.sin(T)
        print(f"5.28 C={C} F i_L2({T}) ODE {sim:.6f}  ours(C=2) {ours:.6f}  book {book:.6f}")

# 5.30 state [iL1, iL2], vP = 10 (iL1 - iL2)
f = lambda x: np.array([100 - 10 * x[0] - 10 * (x[0] - x[1]), 10 * (x[0] - x[1]) - 10 * x[1]])
for T in (0.02, 0.05, 0.2):
    sim = rk4(f, [4, 2], T, 20000)[1]
    lap = 10 / 3 - 2 * np.exp(-10 * T) + 2 / 3 * np.exp(-30 * T)
    print(f"5.30 i_R({T}) ODE {sim:.6f}  Laplace {lap:.6f}")
