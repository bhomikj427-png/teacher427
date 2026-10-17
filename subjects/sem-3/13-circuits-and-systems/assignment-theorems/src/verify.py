"""Independent numeric check of every marathon answer (modified nodal analysis, complex phasors).

Each problem is entered as a netlist straight from the book figure and solved with ALL sources on
(no superposition), so it checks the superposition answer by a different route.
Run: python verify.py
"""
import cmath
import numpy as np


def solve(n_nodes, elems):
    """n_nodes excludes ground (node 0). elems:
    ('Z', a, b, z)            impedance a-b
    ('I', a, b, i)            current source pushing i from a to b through itself (out of b)
    ('V', name, p, m, v)      voltage source, V(p)-V(m)=v; its current (p->m inside) is unknown
    ('E', name, p, m, cp, cm, k)   VCVS: V(p)-V(m)=k*(V(cp)-V(cm))
    ('H', name, p, m, vname, k)    CCVS: V(p)-V(m)=k*I(vname)  (I through source vname, p->m inside)
    Returns (node voltages dict, source currents dict)."""
    vs = [e for e in elems if e[0] in "VEH"]
    N = n_nodes + len(vs)
    A = np.zeros((N, N), complex)
    b = np.zeros(N, complex)
    idx = {e[1]: n_nodes + k for k, e in enumerate(vs)}

    def add(r, c, val):
        if r > 0 and c > 0:
            A[r - 1, c - 1] += val

    for e in elems:
        if e[0] == "Z":
            _, a, bb, z = e
            y = 1 / z
            add(a, a, y); add(bb, bb, y); add(a, bb, -y); add(bb, a, -y)
        elif e[0] == "I":
            _, a, bb, i = e
            if a > 0: b[a - 1] -= i
            if bb > 0: b[bb - 1] += i
    for e in vs:
        k = idx[e[1]]
        p, m = e[2], e[3]
        if p > 0: A[p - 1, k] += 1; A[k, p - 1] += 1
        if m > 0: A[m - 1, k] -= 1; A[k, m - 1] -= 1
        if e[0] == "V":
            b[k] = e[4]
        elif e[0] == "E":
            cp, cm, g = e[4], e[5], e[6]
            if cp > 0: A[k, cp - 1] -= g
            if cm > 0: A[k, cm - 1] += g
        elif e[0] == "H":
            A[k, idx[e[4]]] -= e[5]
    x = np.linalg.solve(A, b)
    V = {0: 0}
    V.update({i + 1: x[i] for i in range(n_nodes)})
    return V, {name: x[k] for name, k in idx.items()}


def pol(z):
    return f"{abs(z):.4f}∠{np.degrees(cmath.phase(z)):.2f}°"


R = {}
j = 1j

# 5.1  nodes: 1=left of series 1Ω (top of 1A src), 2=A, 3=B(1V)
V, _ = solve(3, [("I", 0, 1, 1), ("Z", 1, 2, 1), ("Z", 2, 0, 1), ("Z", 2, 3, 2), ("Z", 3, 0, 3), ("V", "s", 3, 0, 1)])
R["5.1 I"] = (V[2] - V[3]) / 2

# 5.2  1=top node (R), 2=B
V, _ = solve(2, [("I", 0, 1, 1), ("Z", 1, 0, 1), ("Z", 1, 2, j), ("Z", 2, 0, -5j + 4j), ("V", "s", 2, 0, 1)])
R["5.2 V"] = V[1]

# 5.3  1=src top, 2=between 5Ω and dep(−), 3=X. Vx = V(0)-V(3) (+ at bottom)
V, I = solve(3, [("V", "s", 1, 0, 10), ("Z", 1, 2, 5), ("E", "d", 3, 2, 0, 3, 2), ("Z", 3, 0, 2), ("I", 0, 3, 2)])
R["5.3 I"] = (V[1] - V[2]) / 5

# 5.4  1=src + (left), 2=right node(src −), 3=left node below j4
V, _ = solve(3, [("V", "s", 1, 2, 4), ("Z", 1, 3, 3 + 4j), ("Z", 3, 2, 3 - 4j), ("I", 2, 3, 2j)])
R["5.4 I"] = (V[3] - V[2]) / (3 - 4j)

# 5.5(a) 1=src, 2=A, 3=B
V, _ = solve(3, [("V", "s", 1, 0, 5), ("Z", 1, 2, 4), ("Z", 2, 0, -2j), ("Z", 2, 3, 5j), ("I", 0, 3, 2)])
R["5.5a i0"] = V[2] / (-2j)

# 5.5(b) DC part: inductor = short (tiny Z), AC part at w=4
V, _ = solve(3, [("V", "s", 1, 0, 0), ("Z", 1, 2, 4), ("Z", 2, 0, 1e-12), ("Z", 2, 3, 2), ("V", "d", 3, 0, 8)])
R["5.5b i0 DC"] = V[2] / 1e-12
V, _ = solve(3, [("V", "s", 1, 0, 10), ("Z", 1, 2, 4), ("Z", 2, 0, 4j), ("Z", 2, 3, 2), ("V", "d", 3, 0, 0)])
R["5.5b i0 AC"] = V[2] / 4j

# 5.5(c) 1=left top (8Ω top), 2=M, 3=R(V src +). 2A source from R into M (parallel with 6Ω)
V, _ = solve(3, [("Z", 1, 0, 8), ("Z", 1, 2, -2j), ("Z", 2, 0, 4j), ("Z", 2, 3, 6), ("I", 3, 2, 2),
                 ("V", "s", 3, 0, 10 * cmath.exp(1j * np.radians(30)))])
R["5.5c i0"] = V[1] / 8

# 5.6 w=5 part and w=10 part (figure value 20 A; book solution uses 2 A)
V, _ = solve(2, [("V", "s", 1, 0, 30), ("Z", 1, 2, 8), ("Z", 2, 0, -1j), ("Z", 2, 0, 5j)])
R["5.6 v0 (w=5, sin ref)"] = V[2]
V, _ = solve(2, [("V", "s", 1, 0, 0), ("Z", 1, 2, 8), ("Z", 2, 0, -0.5j), ("Z", 2, 0, 10j), ("I", 0, 2, 20)])
R["5.6 v0 (w=10, cos ref, 20 A)"] = V[2]

# 5.7 1=6V top, 2=N, 3=dep top. i0 via ammeter source "a" in series with 1Ω
V, I = solve(4, [("V", "s", 1, 0, 6), ("V", "a", 1, 4, 0), ("Z", 4, 2, 1), ("I", 0, 2, 1), ("Z", 2, 3, 5),
                 ("H", "d", 3, 0, "a", 2)])
R["5.7 i0"] = I["a"]
R["5.7 i"] = (V[2] - V[3]) / 5

# 5.8 1=30V top, 2=A, 3=B, 4=20V top
V, _ = solve(4, [("V", "s1", 1, 0, 30), ("Z", 1, 2, 5), ("Z", 2, 0, 5j), ("Z", 2, 3, 2 + 3j), ("Z", 3, 0, 6),
                 ("Z", 3, 4, 4), ("V", "s2", 4, 0, 20)])
R["5.8 i (A->B)"] = (V[2] - V[3]) / (2 + 3j)

# 5.9 B=0. 1=A, 2=C, 3=D, 4=x (between 6Ω and 4V)
V, _ = solve(4, [("Z", 1, 2, 4), ("Z", 2, 3, 2), ("V", "s2", 3, 0, 2), ("Z", 1, 4, 6), ("V", "s4", 0, 4, 4),
                 ("I", 1, 2, 2)])
R["5.9 VAB"] = V[1]

# 5.10 BM=0. 1=TL, 2=TM, 3=BL. i = V(TM)/3
V, _ = solve(3, [("E", "d", 2, 1, 2, 0, 4 / 3), ("Z", 1, 3, 2), ("Z", 2, 0, 3), ("V", "s", 3, 0, 10),
                 ("I", 3, 2, 2), ("I", 1, 0, 8)])
R["5.10 i"] = V[2] / 3

# 5.11 bottom=0. 1=T, 2=ML, 3=X. i=(V1-V3)/3 ; dep V(T)-V(ML)=4i
V, _ = solve(3, [("E", "d", 1, 2, 1, 3, 4 / 3), ("Z", 2, 0, 2), ("Z", 1, 3, 3), ("I", 2, 3, 8),
                 ("V", "s", 0, 3, 10), ("I", 0, 1, 2)])
R["5.11 V1"] = V[1] - V[3]

# 5.12 1=left src, 2=A, 3=right src
V, _ = solve(3, [("V", "a", 1, 0, 10j), ("Z", 1, 2, 5), ("Z", 2, 0, 3 + 4j), ("Z", 2, 3, 5j), ("V", "b", 3, 0, 10)])
R["5.12 I"] = V[2] / (3 + 4j)

# 5.13 1=A, 2=B, 3=C
V, _ = solve(3, [("I", 0, 1, 20), ("Z", 1, 0, 5), ("Z", 1, 0, 2j), ("Z", 1, 2, 4), ("Z", 2, 0, -2j),
                 ("Z", 2, 3, 2), ("V", "s", 3, 0, 100j)])
R["5.13 I (A->B)"] = (V[1] - V[2]) / 4

# 5.14 bottom=0. 1=TL(Vx), 2=TM, 3=TR, 4=between 1Ω and 2A
V, _ = solve(4, [("Z", 1, 0, 2), ("V", "s", 2, 1, 4), ("Z", 2, 3, 3), ("Z", 4, 2, 1), ("I", 0, 4, 2),
                 ("E", "d", 3, 0, 1, 0, 5)])
R["5.14 I"] = (V[2] - V[3]) / 3

if __name__ == "__main__":
    for k, v in R.items():
        print(f"{k:32s} {v.real:+.4f}{v.imag:+.4f}j   {pol(v)}")


# ---- per-source partials (other independent sources switched off) ----
def partials():
    P = {}
    # 5.9 : (s2, s4, Isrc)
    for name, (a, c, d) in {"5.9 V' (2V)": (2, 0, 0), "5.9 V'' (4V)": (0, 4, 0), "5.9 V''' (2A)": (0, 0, 2)}.items():
        V, _ = solve(4, [("Z", 1, 2, 4), ("Z", 2, 3, 2), ("V", "s2", 3, 0, a), ("Z", 1, 4, 6), ("V", "s4", 0, 4, c),
                         ("I", 1, 2, d)])
        P[name] = V[1]
    # 5.10 : (10V, 2A, 8A)
    for name, (a, c, d) in {"5.10 i' (10V)": (10, 0, 0), "5.10 i'' (2A)": (0, 2, 0), "5.10 i''' (8A)": (0, 0, 8)}.items():
        V, _ = solve(3, [("E", "d", 2, 1, 2, 0, 4 / 3), ("Z", 1, 3, 2), ("Z", 2, 0, 3), ("V", "s", 3, 0, a),
                         ("I", 3, 2, c), ("I", 1, 0, d)])
        P[name] = V[2] / 3
    # 5.11 : (8A, 2A, 10V)
    for name, (a, c, d) in {"5.11 V1' (8A)": (8, 0, 0), "5.11 V1'' (2A)": (0, 2, 0), "5.11 V1''' (10V)": (0, 0, 10)}.items():
        V, _ = solve(3, [("E", "d", 1, 2, 1, 3, 4 / 3), ("Z", 2, 0, 2), ("Z", 1, 3, 3), ("I", 2, 3, a),
                         ("V", "s", 0, 3, d), ("I", 0, 1, c)])
        P[name] = V[1] - V[3]
    # 5.14 : (4V, 2A)
    for name, (a, c) in {"5.14 I' (4V)": (4, 0), "5.14 I'' (2A)": (0, 2)}.items():
        V, _ = solve(4, [("Z", 1, 0, 2), ("V", "s", 2, 1, a), ("Z", 2, 3, 3), ("Z", 4, 2, 1), ("I", 0, 4, c),
                         ("E", "d", 3, 0, 1, 0, 5)])
        P[name] = (V[2] - V[3]) / 3
    # 5.3 : (10V, 2A)
    for name, (a, c) in {"5.3 I' (10V)": (10, 0), "5.3 I'' (2A)": (0, 2)}.items():
        V, _ = solve(3, [("V", "s", 1, 0, a), ("Z", 1, 2, 5), ("E", "d", 3, 2, 0, 3, 2), ("Z", 3, 0, 2), ("I", 0, 3, c)])
        P[name] = (V[1] - V[2]) / 5
    # 5.7 : (6V, 1A)
    for name, (a, c) in {"5.7 (6V)": (6, 0), "5.7 (1A)": (0, 1)}.items():
        V, I = solve(4, [("V", "s", 1, 0, a), ("V", "a", 1, 4, 0), ("Z", 4, 2, 1), ("I", 0, 2, c), ("Z", 2, 3, 5),
                         ("H", "d", 3, 0, "a", 2)])
        P[name + " i0"] = I["a"]; P[name + " i"] = (V[2] - V[3]) / 5
    return P


if __name__ == "__main__":
    print("--- partials ---")
    for k, v in partials().items():
        print(f"{k:32s} {v.real:+.4f}{v.imag:+.4f}j")
