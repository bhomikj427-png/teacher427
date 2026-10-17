"""Batch 10 check: Sadiku 5e §11.2-11.3 (PP 11.4-11.5, Probs. 11.12-11.21). Phasors are amplitudes
(Sadiku's ch. 11 convention for these figures): P = ½ Re(V I*), P_max = |V_th|² / (8 R_th).
Thevenin by netlist; each maximum also checked by sweeping the load on the full circuit."""
import cmath
import numpy as np
from verify import solve, pol

a_ = lambda m, d: m * cmath.exp(1j * np.radians(d))


def thev(n, e, a, b=0):
    V, _ = solve(n, e); voc = V[a] - V[b]
    _, I = solve(n, e + [("V", "_sc", a, b, 0)]); return voc, voc / I["_sc"]


def pl(n, e, a, b, z):
    V, _ = solve(n, e + [("Z", a, b, z)]); v = V[a] - V[b]; return 0.5 * (abs(v) ** 2 / abs(z) ** 2) * z.real


def rep(name, n, e, a, b=0, resistive=False, ref=""):
    vth, zth = thev(n, e, a, b)
    if resistive:
        zl = abs(zth); pm = 0.5 * abs(vth / (zth + zl)) ** 2 * zl
        rs = np.linspace(max(zl * 0.5, 1e-3), zl * 1.5, 20001); ps = [pl(n, e, a, b, complex(r, 0)) for r in rs]
        k = int(np.argmax(ps)); chk = f"sweep R {rs[k]:.4f} P {ps[k]:.4f}"
    else:
        zl = zth.conjugate(); pm = abs(vth) ** 2 / (8 * zth.real)
        best = max(((pl(n, e, a, b, complex(x, y)), x, y) for x in np.linspace(zl.real * 0.8, zl.real * 1.2, 81)
                    for y in np.linspace(zl.imag - abs(zl) * 0.2, zl.imag + abs(zl) * 0.2, 81)))
        chk = f"grid ZL {best[1]:.4f}{best[2]:+.4f}j P {best[0]:.4f}"
    print(f"{name:7s} Vth {pol(vth):20s} Zth {zth.real:+.4f}{zth.imag:+.4f}j  ZL {zl:.4f}  Pmax {pm:.4f} W | {chk}   {ref}")


# PP 11.4 element powers: 1 = 40 V+, 2 = M, 3 = 20∠90 top
V, I = solve(3, [("V", "a", 1, 0, 40), ("Z", 1, 2, 8), ("Z", 2, 0, -2j), ("Z", 2, 3, 4j), ("V", "b", 3, 0, 20j)])
i8 = (V[1] - V[2]) / 8; i4 = (V[2] - V[3]) / 4j
print("PP11.4 P8", 0.5 * abs(i8) ** 2 * 8, " P40V absorbed", 0.5 * (40 * (-i8).conjugate()).real,
      " P20jV absorbed", 0.5 * (20j * i4.conjugate()).real, "  (book −60, −40, 100)")
rep("PP11.5", 3, [("Z", 1, 0, 8), ("Z", 1, 2, -4j), ("I", 0, 2, 12), ("Z", 2, 3, 10j), ("Z", 3, 0, 5)], 3,
    ref="book 3.415−j0.7317, 51.47 W")
rep("11.12", 3, [("V", "s", 1, 0, 165), ("Z", 1, 3, 2j), ("Z", 1, 2, 4), ("Z", 2, 3, -3j), ("Z", 3, 0, 5)], 2, ref="even")
print("11.13 Pmax", 165 ** 2 / (8 * 120), "(App D 28.36 W)")
rep("11.14d", 2, [("I", 0, 1, 10), ("Z", 1, 0, 10j), ("Z", 1, 0, 10), ("Z", 1, 2, 5 - 5j)], 2, ref="design")
rep("11.15", 2, [("V", "s", 1, 0, 12), ("Z", 1, 0, 1), ("Z", 0, 0, 1)][:0] or None, 0) if False else None
rep("11.15", 3, [("V", "s", 1, 0, 12), ("Z", 1, 2, 1), ("Z", 2, 0, 1j), ("Z", 2, 3, -1j), ("G", 0, 3, 2, 0, 2)], 3,
    ref="App D 90 W")
rep("11.16", 3, [("V", "s", 1, 0, 10), ("Z", 1, 2, 2), ("Z", 2, 0, -5j), ("Z", 2, 3, 4), ("G", 2, 3, 2, 0, 0.5),
                 ("Z", 3, 0, 4j)], 3, ref="even")
# 11.17: T 1, L 2, R 3, Bt ground ; 5∠90 from Bt up into T
rep("11.17", 3, [("Z", 1, 2, -10j), ("Z", 1, 3, 30), ("Z", 2, 0, 40), ("Z", 3, 0, 20j), ("I", 0, 1, 5j)], 2, 3,
    ref="App D 20 Ω?, 31.25 W")
# 11.18: T 1, ML 2, MM 3, MR 4 ; 60 V with + at bottom (MM): V3 - V1 = 60
rep("11.18", 4, [("Z", 1, 2, 40), ("Z", 2, 0, 30j), ("V", "s", 3, 1, 60), ("Z", 2, 3, 40), ("Z", 3, 4, 80),
                 ("I", 0, 3, 5), ("Z", 1, 4, -10j)], 4, ref="even")
rep("11.19", 3, [("Z", 1, 0, 1j), ("Z", 1, 2, 3), ("I", 0, 2, 33), ("Z", 2, 0, 6), ("Z", 2, 3, -2j)], 3, resistive=True,
    ref="App D 258.5 W")
# 11.20: 1 src+, 4 after ammeter, A 2, B 3 ; V_A - V_B = 4 Io
rep("11.20", 4, [("V", "s", 1, 0, 165), ("V", "am", 1, 4, 0), ("Z", 4, 2, 40), ("Z", 2, 0, 20j), ("Z", 2, 0, -10j),
                 ("H", "d", 2, 3, "am", 4), ("Z", 3, 0, -10j)], 3, resistive=True, ref="even")
rep("11.21", 2, [("V", "s", 3, 0, a_(120, 60)), ("Z", 3, 1, 100), ("Z", 1, 0, 40 + 30j), ("Z", 1, 2, -10j), ("Z", 2, 0, 50),
                 ("I", 0, 2, 2j)][:0] or [("Z", 1, 0, 1)], 1, resistive=True) if False else None
rep("11.21", 3, [("V", "s", 3, 0, a_(120, 60)), ("Z", 3, 1, 100), ("Z", 1, 0, 40 + 30j), ("Z", 1, 2, -10j),
                 ("Z", 2, 0, 50), ("I", 0, 2, 2j)], 2, resistive=True, ref="App D 19.58 Ω")
