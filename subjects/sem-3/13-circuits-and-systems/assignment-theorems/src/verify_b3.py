"""Batch 3 check: Chakraborty 5.35-5.44 (maximum power transfer).

For each circuit: V_th and Z_th from netlist solves (verify.solve), then the load power is maximised
by brute force (a fine sweep over the load, solving the FULL circuit with the load in place each
time), so the theorem's answer Z_L = Z_th* and P_max = |V_th|^2 / (4 R_th) is checked by a route
that never uses the theorem. Phasor magnitudes are treated as rms (the book's convention).
Run: python verify_b3.py
"""
import cmath
import numpy as np
from verify import solve, pol

j = 1j
d2r = np.radians


def thev(n, elems, a, b=0):
    V, _ = solve(n, elems)
    voc = V[a] - V[b]
    _, I = solve(n, elems + [("V", "_sc", a, b, 0)])
    return voc, voc / I["_sc"]


def load_power(n, elems, a, b, zl):
    V, _ = solve(n, elems + [("Z", a, b, zl)])
    i = (V[a] - V[b]) / zl
    return abs(i) ** 2 * zl.real


def sweep(n, elems, a, b=0, resistive=False, z0=None):
    """Brute-force maximum of load power. Complex load: coarse grid then refine around the best."""
    best = (-1, None)
    if resistive:
        for r in np.concatenate([np.linspace(1e-3, 50, 50001)]):
            p = load_power(n, elems, a, b, complex(r, 0))
            if p > best[0]:
                best = (p, r)
        return best
    cx, cy, span = z0.real, z0.imag, max(abs(z0), 1) * 2
    for _ in range(6):
        xs = np.linspace(max(cx - span, 1e-4), cx + span, 41)
        ys = np.linspace(cy - span, cy + span, 41)
        for x in xs:
            for y in ys:
                p = load_power(n, elems, a, b, complex(x, y))
                if p > best[0]:
                    best = (p, complex(x, y))
        cx, cy, span = best[1].real, best[1].imag, span / 8
    return best


def report(name, n, elems, a, b=0, resistive=False):
    voc, zth = thev(n, elems, a, b)
    if resistive and abs(zth.imag) > 1e-9:
        r_opt = abs(zth)
        p_th = abs(voc / (zth + r_opt)) ** 2 * r_opt
    else:
        r_opt = zth.conjugate() if not resistive else zth.real
        p_th = abs(voc) ** 2 / (4 * zth.real)
    p_bf, z_bf = sweep(n, elems, a, b, resistive=resistive, z0=zth.conjugate())
    print(f"{name:8s} Vth {pol(voc):22s} Zth {zth.real:+.4f}{zth.imag:+.4f}j  "
          f"theorem: ZL {r_opt:.4f}  Pmax {p_th:.4f} W | brute force: ZL {z_bf:.4f}  P {p_bf:.4f} W")
    return voc, zth


# 5.35 superposition of powers
for lab, P in (("a", (20, 80, 5)), ("b", (30, 270, 120))):
    r = [np.sqrt(p) for p in P]
    sums = [s1 * r[0] + s2 * r[1] + s3 * r[2] for s1 in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
    print(f"5.35({lab}) Pmax {max(s * s for s in sums):.4f} W  Pmin {min(s * s for s in sums):.4f} W")

# 5.36(a) 1 = 4V+, 2 = P, 3 = Q, 4 = top of the 6 V source (+ at bottom). Terminals Q-4.
report("5.36a", 4, [("V", "s1", 1, 0, 4), ("Z", 1, 2, 1), ("Z", 2, 0, 2), ("Z", 2, 3, 5), ("Z", 3, 0, 1),
                    ("V", "s2", 0, 4, 6)], 3, 4, resistive=True)
# 5.36(b) 1 = 5V+, 2 = P, 3 = top of R
report("5.36b", 3, [("V", "s", 1, 0, 5), ("Z", 1, 0, 2), ("Z", 1, 2, 3), ("Z", 2, 0, 1), ("I", 0, 2, 2),
                    ("Z", 2, 3, 1)], 3, resistive=True)
# 5.36(c) 1 = P (5 A source node), 2 = Q, 3 = 24 V +. R between P and Q.
report("5.36c", 3, [("I", 0, 1, 5), ("Z", 1, 0, 2), ("Z", 2, 0, 5), ("Z", 2, 3, 10), ("V", "s", 3, 0, 24)], 1, 2,
       resistive=True)
# 5.37
report("5.37", 3, [("V", "s", 1, 0, 5), ("Z", 1, 2, 3), ("Z", 2, 0, 3j), ("Z", 2, 3, 3), ("Z", 3, 0, -3j)], 3)
# 5.38(a)
report("5.38a", 2, [("V", "s", 1, 0, 10 * cmath.exp(-1j * d2r(30))), ("Z", 1, 2, 3 + 4j), ("Z", 2, 0, -5j)], 2)
# 5.38(b) 1 = src+, 2 = P, 3 = A
report("5.38b", 3, [("V", "s", 1, 0, 120 * cmath.exp(-1j * d2r(15))), ("Z", 1, 2, 5j), ("Z", 2, 0, 10 + 8j),
                    ("Z", 2, 3, 4 + 6j), ("I", 0, 3, 5), ("Z", 3, 0, 10)], 3)
# 5.39 resistive load across the lower inductor
report("5.39", 2, [("V", "s", 1, 0, 2), ("Z", 1, 2, 1j), ("Z", 2, 0, 1j)], 2, resistive=True)
# 5.40 1 = top of 10 A, 2 = M, 4 = below ammeter (6 Ω), 3 = terminal after 3 Ω. 2i1: V2 - V1 = 2 i1
report("5.40", 4, [("I", 0, 1, 10), ("Z", 1, 0, 4), ("H", "d", 2, 1, "am", 2), ("V", "am", 2, 4, 0), ("Z", 4, 0, 6),
                   ("Z", 2, 3, 3)], 3, resistive=True)
# 5.41
report("5.41", 3, [("V", "s", 1, 0, 100), ("Z", 1, 2, 2), ("Z", 2, 0, 3 + 5j), ("Z", 2, 3, 6j)], 3)
# 5.42
report("5.42", 3, [("V", "a", 1, 0, 50), ("Z", 1, 2, 5 + 5j), ("Z", 2, 3, 3 - 4j), ("V", "b", 3, 0, 25j)], 2)
# 5.43 check the found equivalent reproduces both measurements
Z = 12 + 5j
print(f"5.43     Isc {abs(260 / Z):.4f} A (20)   |I| with j11 {abs(260 / (Z + 11j)):.4f} A (13)   "
      f"Pmax {260 ** 2 / 48:.4f} W")
# 5.44 (sources set to their phasors; Z_L depends only on Z_th)
report("5.44", 3, [("V", "a", 1, 0, 5 * cmath.exp(1j * d2r(30))), ("Z", 1, 2, 3 + 2j), ("Z", 2, 3, 4 - 3j),
                   ("V", "b", 3, 0, 2)], 2)
