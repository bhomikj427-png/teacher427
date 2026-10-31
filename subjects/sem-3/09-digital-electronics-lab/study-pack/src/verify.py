"""Brute-force check of every design used in the ECE2131 lab pack. Prints PASS/FAIL per design.

Run: python verify.py   (all must PASS before the pack is built)
"""
from itertools import product

ok = True


def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok &= bool(cond)


N = lambda x: 1 - x
XOR = lambda *a: sum(a) % 2
NAND = lambda *a: N(all(a))
NOR = lambda *a: N(any(a))

# Exp 1: universal gates
for a, b in product((0, 1), repeat=2):
    pass
check("NAND-only NOT/AND/OR", all(
    NAND(a, a) == N(a) and NAND(NAND(a, b), NAND(a, b)) == (a & b) and NAND(NAND(a, a), NAND(b, b)) == (a | b)
    for a, b in product((0, 1), repeat=2)))
check("NOR-only NOT/OR/AND", all(
    NOR(a, a) == N(a) and NOR(NOR(a, b), NOR(a, b)) == (a | b) and NOR(NOR(a, a), NOR(b, b)) == (a & b)
    for a, b in product((0, 1), repeat=2)))

# Exp 2: adders / subtractors
check("half adder", all((XOR(a, b), a & b) == ((a + b) % 2, (a + b) // 2) for a, b in product((0, 1), repeat=2)))
check("half subtractor D=A^B, B=A'B", all((XOR(a, b), N(a) & b) == ((a - b) % 2, int(a < b)) for a, b in product((0, 1), repeat=2)))
check("full adder S, Cout=AB+BC+AC", all(
    (XOR(a, b, c), (a & b) | (b & c) | (a & c)) == ((a + b + c) % 2, (a + b + c) // 2) for a, b, c in product((0, 1), repeat=3)))
check("full subtractor D=A^B^Bi, Bo=A'B+(A^B)'Bi", all(
    (XOR(a, b, bi), (N(a) & b) | (N(XOR(a, b)) & bi)) == ((a - b - bi) % 2, int(a - b - bi < 0))
    for a, b, bi in product((0, 1), repeat=3)))
check("full adder from 2 HA + OR", all(
    (XOR(XOR(a, b), c), (a & b) | (XOR(a, b) & c)) == ((a + b + c) % 2, (a + b + c) // 2) for a, b, c in product((0, 1), repeat=3)))


def add4(a, b, c0):
    s = a + b + c0
    return s & 15, s >> 4


check("7483 add/sub with XOR on B, M to C0 (A-B, no borrow -> Cout=1)", all(
    (add4(a, (b ^ 15) if m else b, m)[0] == ((a - b) & 15 if m else (a + b) & 15)) and
    (not m or add4(a, b ^ 15, 1)[1] == int(a >= b))
    for a, b, m in product(range(16), range(16), (0, 1))))


def bcd_add(x, y, cin=0):
    s, c = add4(x, y, cin)
    corr = c | ((s >> 3) & (s >> 2) & 1) | ((s >> 3) & (s >> 1) & 1)
    s2, _ = add4(s, 6 if corr else 0, 0)
    return corr, s2


check("BCD adder (correction = C4 + S3S2 + S3S1)", all(
    bcd_add(x, y, c) == ((x + y + c) // 10, (x + y + c) % 10) for x, y, c in product(range(10), range(10), (0, 1))))

# Exp 3: f = Sum m(1,3,5,7,8,12,14)
M3 = {1, 3, 5, 7, 8, 12, 14}
for w, x, y, z in product((0, 1), repeat=4):
    pass
f_sop = lambda w, x, y, z: (N(w) & z) | (w & N(y) & N(z)) | (w & x & N(z))
f_pos = lambda w, x, y, z: (w | z) & (N(w) | N(z)) & (N(w) | x | N(y))
f_nand = lambda w, x, y, z: NAND(NAND(N(w), z), NAND(w, N(y), N(z)), NAND(w, x, N(z)))
f_nor = lambda w, x, y, z: NOR(NOR(w, z), NOR(N(w), N(z)), NOR(N(w), x, N(y)))
for nm, fn in [("SOP", f_sop), ("POS", f_pos), ("NAND-NAND", f_nand), ("NOR-NOR", f_nor)]:
    check(f"Exp3 {nm}", all(fn(*bits) == int(8 * bits[0] + 4 * bits[1] + 2 * bits[2] + bits[3] in M3)
                            for bits in product((0, 1), repeat=4)))

# Exp 4: code converters
gray = lambda b: b ^ (b >> 1)
check("binary->gray G3=B3, Gi=Bi+1^Bi", all(
    gray(b) == ((b >> 3 & 1) << 3 | (XOR(b >> 3 & 1, b >> 2 & 1)) << 2 | (XOR(b >> 2 & 1, b >> 1 & 1)) << 1 | XOR(b >> 1 & 1, b & 1))
    for b in range(16)))


def g2b(g):
    b3 = g >> 3 & 1; b2 = b3 ^ (g >> 2 & 1); b1 = b2 ^ (g >> 1 & 1); b0 = b1 ^ (g & 1)
    return b3 << 3 | b2 << 2 | b1 << 1 | b0


check("gray->binary Bi = Bi+1 ^ Gi", all(g2b(gray(b)) == b for b in range(16)))


def xs3(n):
    A, B, C, D = n >> 3 & 1, n >> 2 & 1, n >> 1 & 1, n & 1
    W = A | (B & C) | (B & D)
    X = (N(B) & C) | (N(B) & D) | (B & N(C) & N(D))
    Y = (N(C) & N(D)) | (C & D)
    Z = N(D)
    return W << 3 | X << 2 | Y << 1 | Z


check("BCD->XS3 W=A+BC+BD, X=B'C+B'D+BC'D', Y=CD+C'D', Z=D'", all(xs3(n) == n + 3 for n in range(10)))

# Exp 5: comparator, parity
check("1-bit comparator", all(
    ((a & N(b)), (N(a) & b), N(XOR(a, b))) == (int(a > b), int(a < b), int(a == b)) for a, b in product((0, 1), repeat=2)))
check("odd parity generator P = (X^Y^Z)'", all(
    (sum((x, y, z)) + N(XOR(x, y, z))) % 2 == 1 for x, y, z in product((0, 1), repeat=3)))
check("odd parity checker C = (X^Y^Z^P)' flags error", all(
    N(XOR(x, y, z, p)) == int((x + y + z + p) % 2 == 0) for x, y, z, p in product((0, 1), repeat=4)))


def p74180(bits, pe, po):
    even = sum(bits) % 2 == 0
    if pe and not po:
        return (1, 0) if even else (0, 1)
    if po and not pe:
        return (0, 1) if even else (1, 0)
    return (0, 0) if pe and po else (1, 1)


rows180 = ["11110000 1 0", "11110001 1 0", "10101100 0 1", "10101101 0 1", "00000000 1 0", "11111111 0 1"]
tab180 = [p74180([int(c) for c in r.split()[0]], int(r.split()[1]), int(r.split()[2])) for r in rows180]
print("74180 observation table (SigmaE, SigmaO):", tab180)
check("74180 table as printed in pack", tab180 == [(1, 0), (0, 1), (0, 1), (1, 0), (1, 0), (0, 1)])

# Exp 6: MUX f = Sum m(0,3,5,7,8,10,14)
M6 = {0, 3, 5, 7, 8, 10, 14}
I8 = {0: "D'", 1: "D", 2: "D", 3: "D", 4: "D'", 5: "D'", 6: "0", 7: "D'"}
val = lambda e, D: {"D": D, "D'": N(D), "0": 0, "1": 1}[e]
check("8:1 MUX data inputs (S2S1S0 = ABC)", all(
    val(I8[(n >> 1)], n & 1) == int(n in M6) for n in range(16)))
I4 = {0: lambda C, D: N(XOR(C, D)), 1: lambda C, D: D, 2: lambda C, D: N(D), 3: lambda C, D: C & N(D)}
check("4:1 MUX data inputs (S1S0 = AB)", all(I4[n >> 2](n >> 1 & 1, n & 1) == int(n in M6) for n in range(16)))

# Exp 7/8: demux/decoder
check("1:4 demux Yi = D.minterm(S1S0)", all(
    [d & (s == i) for i in range(4)] == [d if s == i else 0 for i in range(4)] for d in (0, 1) for s in range(4)))
check("74138 as 1:8 demux: data on E1' (E2'=0, E3=1), selected output = D, others 1", all(
    [1 if (d or s != i) else 0 for i in range(8)] == [d if i == s else 1 for i in range(8)] for d in (0, 1) for s in range(8)))
check("NAND 2:4 decoder with enable, active-low", all(
    [NAND(e, N(a) if not (i >> 1) else a, N(b) if not (i & 1) else b) for i in range(4)] ==
    [0 if (e and (2 * a + b) == i) else 1 for i in range(4)] for e, a, b in product((0, 1), repeat=3)))

# Exp 10: conversions
check("D->SR: D = S + R'Q (S=R=1 excluded)", all(
    (s | (N(r) & q)) == (1 if s else (0 if r else q)) for s, r, q in product((0, 1), repeat=3) if not (s and r)))

# Exp 11: synchronous counter J=K=1, Q0, Q0Q1, Q0Q1Q2 (negative edge, 7473)
q = [0, 0, 0, 0]
seq = []
for _ in range(17):
    seq.append(q[3] * 8 + q[2] * 4 + q[1] * 2 + q[0])
    t = [1, q[0], q[0] & q[1], q[0] & q[1] & q[2]]
    q = [qi ^ ti for qi, ti in zip(q, t)]
check("4-bit sync up counter 0..15 then 0", seq == list(range(16)) + [0])
r = [1, 0, 0, 0]
ring = []
for _ in range(5):
    ring.append("".join(map(str, r)))
    r = [r[3]] + r[:3]
check("ring counter 1000,0100,0010,0001,1000", ring == ["1000", "0100", "0010", "0001", "1000"])
j = [0, 0, 0, 0]
john = []
for _ in range(9):
    john.append("".join(map(str, j)))
    j = [N(j[3])] + j[:3]
check("Johnson counter 8 states", john == ["0000", "1000", "1100", "1110", "1111", "0111", "0011", "0001", "0000"])

# Exp 12: SISO/SIPO enter 1,1,0,1 (Q3 first stage)
sr = [0, 0, 0, 0]
for bit in (1, 1, 0, 1):
    sr = [bit] + sr[:3]
check("SIPO after entering 1,1,0,1: Q3Q2Q1Q0 = 1011", "".join(map(str, sr)) == "1011")

# Exp 13: 1010 overlapping Mealy, manual equations
def step_jk(Q, J, K):
    return (J & N(Q)) | (N(K) & Q)


def detect(bits, eq):
    A = B = 0
    out = []
    for x in bits:
        z, JA, KA, JB, KB = eq(A, B, x)
        out.append(z)
        A, B = step_jk(A, JA, KA), step_jk(B, JB, KB)
    return out


eq1010 = lambda A, B, x: (A & N(B) & N(x), B & N(x), (B & N(x)) | (N(B) & x), x | A, A)
import random
random.seed(1)
okk = True
for _ in range(300):
    bits = [random.randint(0, 1) for _ in range(30)]
    want = [int(i >= 3 and bits[i - 3:i + 1] == [1, 0, 1, 0]) for i in range(len(bits))]
    okk &= detect(bits, eq1010) == want
check("1010 overlapping detector, manual's JK equations", okk)
# 101 version (the list of experiments): D1 = Q0 X', D0 = X, Z = Q1 X
def det101(bits):
    q1 = q0 = 0
    out = []
    for x in bits:
        out.append(q1 & x)
        q1, q0 = q0 & N(x), x
    return out


okk = True
for _ in range(300):
    bits = [random.randint(0, 1) for _ in range(30)]
    want = [int(i >= 2 and bits[i - 2:i + 1] == [1, 0, 1]) for i in range(len(bits))]
    okk &= det101(bits) == want
check("101 overlapping detector D1=Q0X', D0=X, Z=Q1X", okk)
# JK form of the same: J1=Q0X', K1=1, J0=X, K0=X'
okk = True
for _ in range(300):
    bits = [random.randint(0, 1) for _ in range(30)]
    q1 = q0 = 0
    out = []
    for x in bits:
        out.append(q1 & x)
        q1, q0 = step_jk(q1, q0 & N(x), 1), step_jk(q0, x, N(x))
    okk &= out == det101(bits)
check("101 detector JK form J1=Q0X', K1=1, J0=X, K0=X'", okk)

# Exp 13 ii: F+ = XY + FY'
check("async latch F+ = XY + FY'", all(
    ((x & y) | (f & N(y))) == (x if y else f) for x, y, f in product((0, 1), repeat=3)))

check("async latch hazard-free form F+ = XY + FY' + XF (same function)", all(
    ((x & y) | (f & N(y)) | (x & f)) == (x if y else f) for x, y, f in product((0, 1), repeat=3)))


# factored BCD->XS3 used in the wiring table
def xs3f(n):
    A, B, C, D = n >> 3 & 1, n >> 2 & 1, n >> 1 & 1, n & 1
    cd = C | D
    return (A | (B & cd)) << 3 | XOR(B, cd) << 2 | N(XOR(C, D)) << 1 | N(D)


check("BCD->XS3 factored W=A+B(C+D), X=B^(C+D), Y=(C^D)', Z=D'", all(xs3f(n) == n + 3 for n in range(10)))
# full adder on MUXes (exercise)
S8 = {1, 2, 4, 7}; C8 = {3, 5, 6, 7}
check("full adder on 8:1 MUX (S2S1S0 = A B Cin)", all(
    (int(n in S8), int(n in C8)) == ((bin(n).count("1")) % 2, int(bin(n).count("1") >= 2)) for n in range(8)))
check("full adder on 4:1 MUX (S1S0 = AB): S = Cin,Cin',Cin',Cin ; Cout = 0,Cin,Cin,1", all(
    ([c, N(c), N(c), c][2 * a + b], [0, c, c, 1][2 * a + b]) == ((a + b + c) % 2, (a + b + c) // 2)
    for a, b, c in product((0, 1), repeat=3)))
# conversions (exercise answers)
check("T from JK: T = JQ' + KQ", all(
    XOR(q, (j & N(q)) | (k & q)) == ((j & N(q)) | (N(k) & q)) for j, k, q in product((0, 1), repeat=3)))
check("T from D: D = T ^ Q", all(XOR(t, q) == (N(q) if t else q) for t, q in product((0, 1), repeat=2)))
# SISO serial-out order after loading 1,1,0,1 then shifting in 0s
sr = [0, 0, 0, 0]
for bit in (1, 1, 0, 1):
    sr = [bit] + sr[:3]
outs = [sr[3]]
for _ in range(3):
    sr = [0] + sr[:3]
    outs.append(sr[3])
check("SISO serial out (Q0) after 4th..7th clock = 1,1,0,1 (first-in first-out)", outs == [1, 1, 0, 1])
# 7483 subtract examples used in the pack
check("7 - 5 on 7483: S = 0010, Cout = 1", add4(7, 5 ^ 15, 1) == (2, 1))
check("5 - 7 on 7483: S = 1110 (-2), Cout = 0", add4(5, 7 ^ 15, 1) == (14, 0))
check("BCD 7 + 5 -> carry 1, digit 0010", bcd_add(7, 5) == (1, 2))
# 1010 detector example stream
check("1010 detector on 1,0,1,0,1,0 -> Z = 0,0,0,1,0,1", detect([1, 0, 1, 0, 1, 0], eq1010) == [0, 0, 0, 1, 0, 1])
check("101 detector on 1,0,1,0,1 -> Z = 0,0,1,0,1", det101([1, 0, 1, 0, 1]) == [0, 0, 1, 0, 1])

print("\nALL PASS" if ok else "\nSOME FAILED")
