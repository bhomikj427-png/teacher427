"""Batch 8 check: Sadiku 5e ch. 10 §10.4-10.5 (AC superposition, source transformation).
Each frequency is solved as its own phasor circuit (full netlist, every source at that frequency on);
DC parts with inductors as near-shorts and capacitors as near-opens. Run: python verify_b8.py"""
import cmath
import numpy as np
from verify import solve, pol

j = 1j
ang = lambda m, d: m * cmath.exp(1j * np.radians(d))
SH, OP = 1e-9, 1e12   # short / open for DC
def show(k, v): print(f"{k:28s} {pol(complex(v))}   ({complex(v).real:+.4f}{complex(v).imag:+.4f}j)")

V, _ = solve(4, [("V", "s", 1, 0, 60), ("Z", 1, 2, 10), ("Z", 2, 3, -4j), ("Z", 2, 4, 8j), ("Z", 3, 0, 5), ("Z", 4, 0, -6j),
                 ("I", 3, 4, 2.4)]); show("PP10.4 Io (6.089∠5.94)", (V[1] - V[2]) / 10)
V, _ = solve(3, [("Z", 1, 0, 8), ("Z", 1, 2, -2j), ("Z", 2, 0, 4j), ("Z", 2, 3, 6), ("I", 3, 2, 10), ("V", "s", 3, 0, ang(50, 30))])
show("PP10.5 Io (5.97∠65.45)", V[1] / 8)
V, _ = solve(2, [("V", "s", 1, 0, 75), ("Z", 1, 2, 8), ("Z", 2, 0, -1j), ("Z", 2, 0, 5j)]); show("PP10.6 w=5 sin", V[2])
V, _ = solve(1, [("Z", 1, 0, 8), ("Z", 1, 0, -0.5j), ("Z", 1, 0, 10j), ("I", 0, 1, 6)]); show("PP10.6 w=10 cos", V[1])
V, _ = solve(2, [("I", 0, 1, ang(12, 90)), ("Z", 1, 0, 4 - 3j), ("Z", 1, 2, 2 + 1j), ("Z", 2, 0, 5j), ("Z", 2, 0, 1 - 2j)])
show("PP10.7 Io (9.863∠99.46)", V[2] / (1 - 2j))
# 10.40
V, _ = solve(3, [("V", "a", 1, 0, 0), ("Z", 1, 2, 4), ("Z", 2, 0, SH), ("Z", 2, 3, 2), ("V", "b", 3, 0, 8)]); show("10.40 DC io", V[2] / SH)
V, _ = solve(3, [("V", "a", 1, 0, 10), ("Z", 1, 2, 4), ("Z", 2, 0, 4j), ("Z", 2, 3, 2), ("V", "b", 3, 0, 0)]); show("10.40 w=4 io", V[2] / 4j)
# 10.41
for w, a, lab in ((2, 6, "cos"), (4, 4, "sin")):
    show(f"10.41 w={w} {lab}", a * 2 / (2 + 1 / (j * w * 0.25)))
# 10.43 ix = current right->left in 3 Ω (w = 2)
V, _ = solve(3, [("I", 0, 1, ang(5, 10)), ("Z", 1, 0, 8j), ("Z", 1, 2, -4j), ("Z", 2, 3, 3), ("V", "s", 3, 0, ang(10, -60))])
show("10.43 ix (9.902∠-129.17)", (V[3] - V[2]) / 3)
# 10.44
V, _ = solve(2, [("Z", 1, 0, 16), ("Z", 1, 2, 20 + 10j), ("V", "s", 2, 0, 50)]); show("10.44 w=2 sin vx", V[1])
V, _ = solve(2, [("I", 0, 1, ang(12, 10)), ("Z", 1, 0, 16), ("Z", 1, 2, 20 + 30j), ("V", "s", 2, 0, 0)]); show("10.44 w=6 cos vx", V[1])
# 10.45
show("10.45 w=10 cos i (791.1∠21.47 mA)", ang(16, 30) / (20 + 3j))
show("10.45 w=4 sin i (299.5∠176.6 mA)", -6 / (20 + 1.2j))
# 10.46 vo: DC (10 V), w=3 (12 V cos), w=2 (4 A sin)
V, _ = solve(3, [("V", "a", 1, 0, 0), ("Z", 1, 2, 6), ("Z", 2, 0, OP), ("Z", 2, 3, SH), ("V", "b", 3, 0, 10)]); show("10.46 DC", V[2])
V, _ = solve(3, [("V", "a", 1, 0, 12), ("Z", 1, 2, 6), ("Z", 2, 0, -4j), ("Z", 2, 3, 6j), ("V", "b", 3, 0, 0)]); show("10.46 w=3 cos", V[2])
V, _ = solve(3, [("V", "a", 1, 0, 0), ("Z", 1, 2, 6), ("Z", 2, 0, -6j), ("Z", 2, 3, 4j), ("I", 0, 2, 4), ("V", "b", 3, 0, 0)]); show("10.46 w=2 sin", V[2])
# 10.47 io down 4 Ω. nodes 1 src+, 2 between 1 Ω and cap, 3 A, 4 B, 5 C
def c47(w, vs, is_, vdc, ZL, ZC):
    V, _ = solve(5, [("V", "s", 1, 0, vs), ("Z", 1, 2, 1), ("Z", 2, 3, ZC), ("Z", 3, 0, 2), ("V", "e", 4, 3, vdc),
                     ("I", 0, 4, is_), ("Z", 4, 5, ZL), ("Z", 5, 0, 4)]); return V[5] / 4
show("10.47 DC", c47(0, 0, 0, 24, SH, OP)); show("10.47 w=1 sin(ref)", c47(1, ang(10, -30), 0, 0, 2j, -6j))
show("10.47 w=3 cos", c47(3, 0, 2, 0, 6j, -2j))
# 10.48 io up through 100 Ω (R -> T2). nodes T1 1, M1 2, T2 3, M2 4, R 5
def c48(vs, is_, vdc, ZL, ZC):
    V, _ = solve(5, [("V", "s", 1, 2, vs), ("I", 0, 2, is_), ("Z", 2, 4, ZL), ("Z", 1, 3, ZC), ("Z", 3, 4, 80), ("Z", 4, 0, 60),
                     ("Z", 3, 5, 100), ("V", "e", 5, 0, vdc)]); return (V[5] - V[3]) / 100
show("10.48 DC", c48(0, 0, 24, SH, OP)); show("10.48 w=2000 cos", c48(50, 0, 0, 80j, -25j)); show("10.48 w=4000 sin", c48(0, 2, 0, 160j, -12.5j))
show("10.49 i (4.472∠56.56 sin)", ang(8, 30) * 5 / (8 + 1j - 5j))
V, _ = solve(3, [("V", "s", 1, 0, 60), ("Z", 1, 2, 2 + 4j), ("Z", 2, 0, 6), ("Z", 2, 3, -2j), ("Z", 3, 0, 4 - 3j), ("I", 0, 3, 5j)])
show("10.52 Ix", V[3] / (4 - 3j))
V, _ = solve(4, [("V", "s", 1, 0, 20), ("Z", 1, 2, 4), ("Z", 2, 0, 2j), ("Z", 2, 3, -3j), ("Z", 3, 0, 2), ("Z", 3, 4, 4j), ("Z", 4, 0, -2j)])
show("10.53 Vo (3.529-j5.883)", V[4])
# 10.42/10.51 sample design: V1 = 10∠0°, V2 = 5∠0°, X_L = 2, R1 = 4, X_C = 4, R2 = 2 (Ω); Io = current in −jX_C... see write-up
V, _ = solve(3, [("V", "a", 1, 0, 10), ("Z", 1, 2, 2j), ("Z", 2, 0, 4), ("Z", 2, 3, 0.0), ("Z", 3, 0, -4j), ("Z", 3, 4, 2),
                 ("V", "b", 4, 0, 5)][:0] or [("V", "a", 1, 0, 10), ("Z", 1, 2, 2j), ("Z", 2, 0, 4), ("Z", 2, 0, -4j),
                 ("Z", 2, 3, 2), ("V", "b", 3, 0, 5)])
show("10.42 design: node V", V[2]); show("10.42 design: Io = (V - 0)/(-j4)", V[2] / -4j)
