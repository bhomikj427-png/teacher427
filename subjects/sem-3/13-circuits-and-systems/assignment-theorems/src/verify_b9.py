"""Batch 9 check: Sadiku 5e §10.6 AC Thevenin/Norton (PP 10.8-10.10, Probs. 10.55-10.68).
V_oc, I_sc (a->b), Z_th = V_oc/I_sc and a test-source Z_th, all by phasor netlist solves."""
import cmath
import numpy as np
from verify import solve, pol

a_ = lambda m, d: m * cmath.exp(1j * np.radians(d))


def thev(n, e, a, b=0):
    V, _ = solve(n, e); voc = V[a] - V[b]
    _, I = solve(n, e + [("V", "_sc", a, b, 0)]); isc = I["_sc"]
    return voc, isc, (voc / isc if abs(isc) > 1e-12 else None)


def ztest(n, e, a, b=0):
    off = [(x[:4] + (0,)) if (x[0] == "V" and not x[1].startswith(("am", "_"))) else (x[:3] + (0,)) if x[0] == "I" else x
           for x in e]
    V, _ = solve(n, off + [("I", b, a, 1)]); return V[a] - V[b]


def rep(name, n, e, a, b=0, ref=""):
    if isinstance(b, str):
        b, ref = 0, b
    voc, isc, z = thev(n, e, a, b)
    zt = ztest(n, e, a, b)
    print(f"{name:8s} Vth {pol(voc):22s} IN {pol(isc):22s} Zth {zt.real:+.4f}{zt.imag:+.4f}j ({pol(zt)})   {ref}")
    return voc, isc, zt


rep("PP10.8", 3, [("V", "s", 1, 0, a_(100, 20)), ("Z", 1, 2, 6 + 2j), ("Z", 2, 0, -4j), ("Z", 3, 0, 10)], 2, 3,
    "book 12.4-j3.2, 63.24∠-51.57")
# PP10.9: L 1, R 2(a), 3 between 8 and j4 not needed: Vo = V1 - V2
rep("PP10.9", 2, [("Z", 1, 2, 8 + 4j), ("I", 1, 2, 5), ("G", 0, 2, 1, 2, 0.2), ("Z", 1, 0, 4 - 2j)], 2, 0,
    "book Zth 4.473∠-7.64, Vth 7.35∠72.9")
e = [("V", "s", 1, 0, 20), ("Z", 1, 2, 4 + 2j), ("Z", 1, 3, 8), ("I", 0, 3, a_(4, -90)), ("Z", 3, 2, 1 - 3j)]
voc, isc, zt = rep("PP10.10", 3, e, 2, 0, "book ZN 3.176+j0.706, IN 8.396∠-32.68")
print("   Io", pol(isc * zt / (zt + 10 - 5j)), "(book 1.9714∠-2.10)")
rep("10.55a", 3, [("V", "s", 1, 0, a_(50, 30)), ("Z", 1, 2, 20j), ("Z", 2, 0, -10j), ("Z", 2, 3, 10)], 3,
    "AppD 22.63∠-63.43, 50∠-150, 2.236∠-86.6")
rep("10.55b", 2, [("I", 0, 1, 4), ("Z", 1, 0, 8), ("Z", 1, 2, -5j), ("Z", 2, 0, 10j)], 2, 0, "AppD 10∠26, 33.92∠58, 3.392∠32")
rep("10.56a", 2, [("Z", 0, 1, 6), ("Z", 1, 2, (4j * -2j) / (4j - 2j)), ("I", 0, 2, 2)], 2, 0, "even")
rep("10.56b", 3, [("V", "s", 1, 0, a_(120, 45)), ("Z", 1, 2, 30), ("Z", 2, 0, 60), ("Z", 2, 3, 10j), ("Z", 3, 0, -5j)], 3,
    "even")
rep("10.57d", 3, [("V", "s", 1, 0, 10), ("Z", 1, 2, 2 - 2j), ("Z", 2, 0, 2j), ("Z", 2, 3, 1)], 3, 0, "design")
rep("10.58", 1, [("I", 0, 1, a_(5, 45)), ("Z", 1, 0, 8 - 6j), ("Z", 1, 0, 10j)], 1, 0, "even")
# 10.59: T 1, X 2 (between -j2 and 10), O 3. Vo = V1 - V2
print("10.59  Zout", pol(ztest(3, [("G", 0, 1, 1, 2, 0.2), ("Z", 1, 0, 40j), ("Z", 1, 2, -2j), ("Z", 2, 3, 10)], 3)),
      "AppD -6+j38")
e60 = [("V", "s", 1, 0, 20), ("Z", 1, 2, 10), ("Z", 2, 0, 5j), ("Z", 2, 3, -4j), ("I", 0, 3, 4), ("Z", 3, 0, 4)]
rep("10.60ab", 3, e60, 3, 0, "even"); rep("10.60cd", 3, e60, 2, 3, "even")
# 10.61: L 1 (via ammeter to -j3), a 2
rep("10.61", 3, [("I", 0, 1, 2), ("V", "am", 1, 3, 0), ("Z", 3, 0, -3j), ("Z", 1, 2, 4), ("F", 0, 2, "am", 1.5)], 2,
    "AppD -24+j12, -8+j6")
# 10.62 (w=1): 1 src+, 4 after ammeter, A 2, B 3 ; Thevenin across 2 Ω (B to ground)
e62 = [("V", "s", 1, 0, 12), ("V", "am", 1, 4, 0), ("Z", 4, 2, 4), ("Z", 2, 0, -4j), ("Z", 2, 3, 2j), ("Z", 3, 0, -8j),
       ("F", 2, 3, "am", 3)]
voc, isc, zt = rep("10.62", 4, e62, 3, 0, "even (seen by 2 Ω)")
print("   vo", pol(voc * 2 / (zt + 2)))
V, _ = solve(4, e62 + [("Z", 3, 0, 2)]); print("   vo full", pol(V[3]))
rep("10.63", 2, [("I", 0, 1, a_(4, 30)), ("Z", 1, 0, 2000j), ("Z", 1, 0, 2000), ("Z", 1, 2, -1000j)], 2, 0,
    "AppD 1 kΩ, 5.657∠75")
rep("10.64", 3, [("I", 0, 1, a_(3, 60)), ("Z", 1, 2, 60), ("Z", 2, 0, 80j), ("Z", 1, 3, 40), ("Z", 3, 0, -30j)], 2, 3,
    "even")
# 10.65 design: vs = 10∠0 (+ left), R = 5, C1 -> -j10, L -> j5, C2 -> -j5 ; Norton seen by L (node 2 to ground)
voc, isc, zt = rep("10.65d", 3, [("Z", 1, 0, -10j), ("Z", 1, 2, 5), ("V", "s", 2, 3, 10), ("Z", 3, 0, -5j)], 2, 0, "design")
print("   io", pol(isc * zt / (zt + 5j)))
V, _ = solve(3, [("Z", 1, 0, -10j), ("Z", 1, 2, 5), ("V", "s", 2, 3, 10), ("Z", 3, 0, -5j), ("Z", 2, 0, 5j)])
print("   io full", pol(V[2] / 5j))
# 10.66 (w=10, cos ref; 2 sin = 2∠-90): L 1 (vo), X 2, A 3
rep("10.66", 3, [("I", 0, 1, a_(2, -90)), ("Z", 1, 0, 10), ("Z", 1, 2, -10j), ("V", "s", 3, 2, 12), ("Z", 3, 0, 5j),
                 ("G", 0, 3, 1, 0, 2)], 3, "even")
rep("10.67", 3, [("V", "s", 1, 0, a_(60, 45)), ("Z", 1, 2, 13 - 5j), ("Z", 1, 3, 12), ("Z", 2, 0, 10), ("Z", 3, 0, 8 + 6j)],
    2, 3, "AppD 4.945∠-69.76, 0.4378∠-75.24, 11.243+j1.079")
# 10.68 (w=10): 1 src+, 4 after ammeter, M 2, a 3 ; V_M = V_a/3 ; 4 io into a
rep("10.68", 4, [("V", "s", 1, 0, 6), ("V", "am", 1, 4, 0), ("Z", 4, 2, 4), ("E", "d", 2, 0, 3, 0, 1 / 3),
                 ("F", 0, 3, "am", 4), ("Z", 3, 0, -2j), ("Z", 3, 0, 10j)], 3, "even (sin ref)")
