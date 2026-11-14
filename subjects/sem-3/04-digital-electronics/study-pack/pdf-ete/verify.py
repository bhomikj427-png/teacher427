"""Re-derives every worked answer printed in DE-ETE-v1.pdf. Run: python verify.py  (exit 0 = all pass).

Each printed expression is checked two ways: it must equal the function on every specified input row
(truth-table comparison), and it must be as cheap as the Quine-McCluskey minimum (same number of terms and
literals). Counters and sequence detectors are simulated; state reductions are re-partitioned.
"""
import random
import re
import sys
from itertools import product

import qm

sys.stdout.reconfigure(encoding="utf-8")
N = [0]


def ok(label, cond, detail=""):
    N[0] += 1
    assert cond, f"FAIL {label} {detail}"
    print(f"ok  {label}")


def lits(term, names):
    out, t = [], term.replace(" ", "").replace("·", "")
    order = sorted(names, key=len, reverse=True)
    while t:
        for v in order:
            if t.startswith(v):
                t = t[len(v):]
                neg = t.startswith("'")
                if neg:
                    t = t[1:]
                out.append((v, neg))
                break
        else:
            raise ValueError(f"cannot parse {term!r} at {t!r}")
    return out


def sop_fn(expr, names):
    terms = [lits(t, names) for t in expr.split("+")] if expr.strip() not in ("0", "1") else None
    def f(env):
        if terms is None:
            return int(expr.strip())
        return int(any(all(env[v] != neg for v, neg in t) for t in terms))
    return f, terms


def pos_fn(expr, names):
    sums = [lits(s.replace("+", ""), names) for s in re.findall(r"\(([^)]*)\)", expr)]
    return (lambda env: int(all(any(env[v] != neg for v, neg in s) for s in sums))), sums


def envs(names):
    n = len(names)
    for m in range(2 ** n):
        yield m, {v: (m >> (n - 1 - i)) & 1 for i, v in enumerate(names)}


def check_sop(label, expr, ones, dcs, names, minimal=True):
    f, terms = sop_fn(expr, names)
    for m, env in envs(names):
        if m in dcs:
            continue
        assert f(env) == int(m in ones), f"FAIL {label}: {expr} wrong at row {m}"
    if minimal:
        best = qm.minimal_all(ones, dcs, len(names))[0]
        cost = (len(best), sum(len(names) - bin(t[1]).count("1") for t in best))
        mine = (len(terms), sum(len(t) for t in terms)) if terms else (0, 0)
        assert mine == cost, f"FAIL {label}: {expr} costs {mine}, minimum is {cost}"
    ok(f"{label}: {expr}", True)


def check_pos(label, expr, ones, dcs, names):
    f, sums = pos_fn(expr, names)
    n = len(names)
    for m, env in envs(names):
        if m in dcs:
            continue
        assert f(env) == int(m in ones), f"FAIL {label}: {expr} wrong at row {m}"
    zeros = [m for m in range(2 ** n) if m not in ones and m not in dcs]
    best = qm.minimal_all(zeros, dcs, n)[0]
    assert (len(sums), sum(len(s) for s in sums)) == (len(best), sum(n - bin(t[1]).count("1") for t in best)), f"FAIL {label} not minimal"
    ok(f"{label}: {expr}", True)


R = lambda a, b: list(range(a, b + 1))

# ================================================================= Part A
f1, _ = sop_fn("x'yz + x'yz' + xz", "xyz"); f2, _ = sop_fn("x'y + xz", "xyz")
ok("A1 slide 18: x'yz + x'yz' + xz = x'y + xz", all(f1(e) == f2(e) for _, e in envs("xyz")))
f1, _ = sop_fn("x'y'z' + x'yz' + xyz'", "xyz"); f2, _ = sop_fn("x'z' + yz'", "xyz")
ok("A1 check a (slide 19)", all(f1(e) == f2(e) for _, e in envs("xyz")))
ok("A1 check b: A + A'B = A + B", all((a | ((1 - a) & b)) == (a | b) for a, b in product((0, 1), repeat=2)))
ok("A1 check c: (A + B'C)' = A'(B + C')", all((1 - (a | ((1 - b) & c))) == ((1 - a) & (b | (1 - c))) for a, b, c in product((0, 1), repeat=3)))
ok("A1 consensus", all(((x & y) | ((1 - x) & z) | (y & z)) == ((x & y) | ((1 - x) & z)) for x, y, z in product((0, 1), repeat=3)))
ok("A1 X + YZ = (X + Y)(X + Z)", all((x | (y & z)) == ((x | y) & (x | z)) for x, y, z in product((0, 1), repeat=3)))
check_sop("A2 f1 = Σm(1,2,4,6)", "a'b'c + a'bc' + ab'c' + abc'", [1, 2, 4, 6], [], "abc", minimal=False)
fp, _ = pos_fn("(a + b + c)(a + b' + c')(a' + b + c')(a' + b' + c')", "abc")
ok("A2 ΠM(0,3,5,7) expansion", all(fp(e) == int(m in (1, 2, 4, 6)) for m, e in envs("abc")))
check_sop("A2 standard form a'b'c + bc' + ac'", "a'b'c + bc' + ac'", [1, 2, 4, 6], [], "abc")
ok("A2 check a: Σm(0,2,5) = ΠM(1,3,4,6,7)", sorted(set(range(8)) - {0, 2, 5}) == [1, 3, 4, 6, 7])
ok("A2 slide-31 slip: a'bc is row 3", int("011", 2) == 3 and 3 not in (1, 2, 4, 6))
MTE4 = ([0, 4, 5, 7, 8, 9, 15], [1, 3, 6, 14])
check_sop("A3 MTE Q4", "b'c' + bc + a'c'", *MTE4, "abcd")
check_sop("A3 MTE Q4 alternative", "b'c' + bc + a'b", *MTE4, "abcd")
check_sop("A3 check a (slide 69)", "a'd' + c'd' + abd", [0, 2, 6, 8, 12, 13, 15], [3, 4, 9], "abcd")
check_sop("A3 check a alternative", "a'd' + ac' + abd", [0, 2, 6, 8, 12, 13, 15], [3, 4, 9], "abcd")
check_sop("A3 check b (slide 27)", "b", [2, 3, 6, 7], [], "abc")
D63 = [0, 1, 2, 5, 8, 9, 10]
check_sop("A4 slide 63 SOP", "X'Y' + X'Z' + W'Y'Z", D63, [], "WXYZ")
check_pos("A4 slide 63 POS", "(W' + X')(Y' + Z')(X' + Z)", D63, [], "WXYZ")
check_sop("A4 slide 58 five-variable", "ce", [5, 7, 13, 15, 21, 23, 29, 31], [], "abcde")
ok("A4 check a: ΠM(0,2,3,4,5,6) ones", sorted(set(range(16)) - {0, 2, 3, 4, 5, 6}) == [1, 7] + R(8, 15))
check_sop("A4 check a (slide 64)", "W + XYZ + X'Y'Z", [1, 7] + R(8, 15), [], "WXYZ")
check_sop("A4 check b (practice set 1 Q1)", "xz + wz' + v'x'z' + vw'z", [0, 2, 5, 8, 10, 13, 15, 17, 19, 21, 26, 28, 29, 30, 31], [7, 12, 14, 23, 24], "vwxyz")
ok("A5 MTE Q1: P'Q' + P' = P'", all((((1 - p) & (1 - q)) | (1 - p)) == (1 - p) for p, q in product((0, 1), repeat=2)))
nand = lambda *a: 1 - int(all(a)); nor = lambda *a: 1 - int(any(a))
ok("A5 NOR inverter", all(nor(p, p) == 1 - p for p in (0, 1)))
ok("A5 NAND builds NOT, AND, OR", all(nand(x, x) == 1 - x and nand(nand(x, y), nand(x, y)) == (x & y) and nand(nand(x, x), nand(y, y)) == (x | y) for x, y in product((0, 1), repeat=2)))
ok("A5 XOR from 4 NANDs", all(nand(nand(a, nand(a, b)), nand(b, nand(a, b))) == (a ^ b) for a, b in product((0, 1), repeat=2)))
ok("A5 NAND-NAND of A3's answer", all(nand(nand(1 - e["b"], 1 - e["c"]), nand(e["b"], e["c"]), nand(1 - e["a"], 1 - e["c"])) == int(m in MTE4[0]) for m, e in envs("abcd") if m not in MTE4[1]))
check_sop("A5 check a (practice set 1 Q2)", "w'x' + w'z + x'y", [0, 1, 3, 5, 7, 10, 11], [2, 6, 13], "wxyz")
ok("A5 check c: AND from 3 NORs", all(nor(nor(a, a), nor(b, b)) == (a & b) for a, b in product((0, 1), repeat=2)))
FA = {(a, b, c): ((a + b + c) >> 1, (a + b + c) & 1) for a, b, c in product((0, 1), repeat=3)}
ok("A6 FA: S = A⊕B⊕Cin, Cout = AB + Cin(A⊕B)", all(FA[k] == ((k[0] & k[1]) | (k[2] & (k[0] ^ k[1])), k[0] ^ k[1] ^ k[2]) for k in FA))
check_sop("A6 FA carry", "AB + BC + AC", [3, 5, 6, 7], [], "ABC")
ok("A6 S = Σm(1,2,4,7)", [m for m in range(8) if bin(m).count("1") % 2] == [1, 2, 4, 7])
ok("A6 two half adders", all(((k[0] ^ k[1]) ^ k[2], (k[0] & k[1]) | ((k[0] ^ k[1]) & k[2])) == (FA[k][1], FA[k][0]) for k in FA))
FS = {(a, b, c): (int(a - b - c < 0), (a - b - c) & 1) for a, b, c in product((0, 1), repeat=3)}
ok("A6 FS: D, Bout = A'B + Bin(A⊕B)'", all(FS[k] == (((1 - k[0]) & k[1]) | (k[2] & (1 - (k[0] ^ k[1]))), k[0] ^ k[1] ^ k[2]) for k in FS))
check_sop("A6 FS borrow", "A'B + A'C + BC", [m for m in range(8) if FS[tuple((m >> i) & 1 for i in (2, 1, 0))][0]], [], "ABC")
ok("A6 check a: 1+0+1", FA[(1, 0, 1)] == (1, 0))
A, B = 0b1011, 0b1110
c, carries, s = 0, [], 0
for i in range(4):
    a, b = (A >> i) & 1, (B >> i) & 1
    cy, sm = FA[(a, b, c)]; s |= sm << i; c = cy; carries.append(c)
ok("A7 1011 + 1110: carries 0,1,1,1, sum 1 1001 = 25", carries == [0, 1, 1, 1] and (c << 4 | s) == 0b11001 == 25)
G, P = A & B, A ^ B
ok("A7 check a: G = 1010, P = 0101", (G, P) == (0b1010, 0b0101))
c, cl = 0, []
for i in range(4):
    c = ((G >> i) & 1) | (((P >> i) & 1) & c); cl.append(c)
ok("A7 look-ahead carries equal ripple carries", cl == carries)
g, p = [1, 0, 1, 1], [0, 1, 1, 0]
ok("A7 expanded C3 formula", all((gg[2] | (pp[2] & gg[1]) | (pp[2] & pp[1] & gg[0]) | (pp[2] & pp[1] & pp[0] & c0)) ==
   (gg[2] | (pp[2] & (gg[1] | (pp[1] & (gg[0] | (pp[0] & c0)))))) for gg in product((0, 1), repeat=3) for pp in product((0, 1), repeat=3) for c0 in (0, 1)))
ok("A7 delay 4-bit = 9T, 8-bit = 17T", (2 * 4 + 1, 2 * 8 + 1) == (9, 17))
ok("A7 check c: 0110 - 0011", 0b0110 + (0b0011 ^ 0b1111) + 1 == 0b10011)
ok("A7 adder-subtractor for all 4-bit pairs", all(((a + (b ^ (15 * m)) + m) & 15) == ((a + b) & 15 if m == 0 else (a - b) & 15) for a in range(16) for b in range(16) for m in (0, 1)))
ra, rb, cy, trace = [0, 1, 0, 0], [0, 1, 1, 1], 0, []
for _ in range(4):
    cy2, sm = FA[(ra[-1], rb[-1], cy)]
    ra = [sm] + ra[:-1]; rb = [0] + rb[:-1]; cy = cy2
    trace.append(("".join(map(str, ra)), sm, cy))
ok("A8 serial adder trace", trace == [("1010", 1, 0), ("1101", 1, 0), ("0110", 0, 1), ("1011", 1, 0)])


def bcd(x, y):
    z = x + y; k, z4 = z >> 4, z & 15
    yy = k | ((z4 >> 3) & (z4 >> 2) & 1) | ((z4 >> 3) & (z4 >> 1) & 1)
    s = z4 + (6 if yy else 0)
    return yy, s & 15, z4, k


ok("A8 BCD adder correct for all digit pairs", all(bcd(x, y)[0] * 10 + bcd(x, y)[1] == x + y for x in range(10) for y in range(10)))
check_sop("A8 Z ≥ 10", "Z3Z2 + Z3Z1", R(10, 15), [], ["Z3", "Z2", "Z1", "Z0"])
ok("A8 8 + 7", bcd(8, 7) == (1, 5, 0b1111, 0)); ok("A8 check a: 6 + 5", bcd(6, 5) == (1, 1, 0b1011, 0)); ok("A8 check b: 9 + 9", bcd(9, 9) == (1, 8, 0b0010, 1))

# ================================================================= Part B
MTE5 = [0, 1, 3, 4, 8, 9, 10, 11, 13, 15]
ok("B1 MTE Q5 MUX inputs", qm.mux1(MTE5, "PQRS") == ["1", "S", "S'", "0", "1", "1", "S", "S"])
ok("B1 MTE Q5 row pairs", qm.mux(MTE5, 4, 3) == [(1, 1), (0, 1), (1, 0), (0, 0), (1, 1), (1, 1), (0, 1), (0, 1)])
ok("B1 check a (practice set 1 Q3)", qm.mux1([0, 1, 3, 5, 7, 9, 15], "abcd") == ["1", "d", "d", "d", "d", "0", "0", "d"])
ok("B1 check b (slide 16)", qm.mux1([1, 2, 6, 7], "xyz") == ["z", "z'", "0", "1"])
PS5 = [0, 2, 7, 8, 9, 11, 13, 14, 15]
m1 = {0: "D'", 1: "D'", 2: "0", 3: "D"}; m2 = {0: "1", 1: "D", 2: "D", 3: "1"}
val = lambda s, d: {"0": 0, "1": 1, "D": d, "D'": 1 - d}[s]
ok("B1 check c (practice set 1 Q5) three 4:1 MUXes", all(val((m2 if a else m1)[b << 1 | c], d) == int((a << 3 | b << 2 | c << 1 | d) in PS5) for a, b, c, d in product((0, 1), repeat=4)))
ok("B1 4:1 from three 2:1", all((lambda lo, hi: hi if s1 else lo)(i[1] if s0 else i[0], i[3] if s0 else i[2]) == i[s1 << 1 | s0] for i in product((0, 1), repeat=4) for s1 in (0, 1) for s0 in (0, 1)))
ok("B2 MTE Q6: S = Σm(1,2,4,7), Cout = Σm(3,5,6,7)", [m for m in range(8) if FA[((m >> 2) & 1, (m >> 1) & 1, m & 1)][1]] == [1, 2, 4, 7] and [m for m in range(8) if FA[((m >> 2) & 1, (m >> 1) & 1, m & 1)][0]] == [3, 5, 6, 7])
ok("B2 active-low decoder + NAND", all(nand(*[int(m != j) for j in (1, 2, 5, 7)]) == int(m in (1, 2, 5, 7)) for m in range(8)))
ok("B2 check a: NOR of outputs 0,3,5,6,7 = ΠM(0,3,5,6,7) = Σm(1,2,4)", all(nor(*[int(m == j) for j in (0, 3, 5, 6, 7)]) == int(m in (1, 2, 4)) for m in range(8)))
W = ["w3", "w2", "w1", "w0"]
pe = {m: (3 if m & 8 else 2 if m & 4 else 1 if m & 2 else 0) for m in range(1, 16)}
check_sop("B3 priority y1", "w3 + w2", [m for m in pe if pe[m] & 2], [0], W)
check_sop("B3 priority y0", "w3 + w2'w1", [m for m in pe if pe[m] & 1], [0], W)
ok("B3 check a: 0110 → 10", pe[0b0110] == 2)
ok("B3 plain encoder fails on w1 + w2", ((1 | 0) << 1 | (1 | 0)) == 3)
SEG = {0: "abcdef", 1: "bc", 2: "abged", 3: "abgcd", 4: "fgbc", 5: "afgcd", 6: "afgedc", 7: "abc", 8: "abcdefg", 9: "abcdfg"}
EQ = {"a": "A + C + BD + B'D'", "b": "B' + C'D' + CD", "c": "B + C' + D", "d": "A + B'D' + B'C + CD' + BC'D", "e": "B'D' + CD'",
      "f": "A + C'D' + BC' + BD'", "g": "A + B'C + BC' + CD'"}
LIT = {"a": "0 2 3 5 6 7 8 9", "b": "0 1 2 3 4 7 8 9", "d": "0 2 3 5 6 8 9", "e": "0 2 6 8", "f": "0 4 5 6 8 9", "g": "2 3 4 5 6 8 9"}
for s_, e_ in EQ.items():
    on = [d for d in range(10) if s_ in SEG[d]]
    if s_ in LIT:
        assert " ".join(map(str, on)) == LIT[s_], s_
    check_sop(f"B4 segment {s_}", e_, on, R(10, 15), "ABCD")
ok("B4 segment c lit for all except 2", [d for d in range(10) if "c" not in SEG[d]] == [2])
fe, _ = sop_fn("B'D' + CD'", "ABCD"); fe2, _ = sop_fn("D + BC'", "ABCD")
ok("B4 e' = D + BC'", all(fe(e) == 1 - fe2(e) for _, e in envs("ABCD")))
fc, _ = sop_fn("B + C' + D", "ABCD"); fc2, _ = sop_fn("B'CD'", "ABCD")
ok("B4 check b: c' = B'CD'", all(fc(e) == 1 - fc2(e) for _, e in envs("ABCD")))
ok("B4 check a: digit 4 = b c f g", sorted(SEG[4]) == list("bcfg")); ok("B4 check c: 13 and 42 lines", (7 + 6, 7 * 6) == (13, 42))
C4 = ["A1", "A0", "B1", "B0"]
gt = [m for m in range(16) if (m >> 2) > (m & 3)]; lt = [m for m in range(16) if (m >> 2) < (m & 3)]
check_sop("B5 2-bit G", "A1B1' + A0B1'B0' + A1A0B0'", gt, [], C4)
check_sop("B5 2-bit L", "A1'B1 + A1'A0'B0 + A0'B1B0", lt, [], C4)
xn = lambda a, b: 1 - (a ^ b)
ok("B5 2-bit formulas with x1", all(((a1 & (1 - b1)) | (xn(a1, b1) & a0 & (1 - b0))) == int((a1 << 1 | a0) > (b1 << 1 | b0)) and (xn(a1, b1) & xn(a0, b0)) == int((a1, a0) == (b1, b0))
   for a1, a0, b1, b0 in product((0, 1), repeat=4)))


def g4(a, b):
    x = [xn((a >> i) & 1, (b >> i) & 1) for i in range(4)]; A_ = [(a >> i) & 1 for i in range(4)]; B_ = [1 - ((b >> i) & 1) for i in range(4)]
    return (A_[3] & B_[3]) | (x[3] & A_[2] & B_[2]) | (x[3] & x[2] & A_[1] & B_[1]) | (x[3] & x[2] & x[1] & A_[0] & B_[0])


ok("B5 4-bit G formula", all(g4(a, b) == int(a > b) for a in range(16) for b in range(16)))
ok("B5 check a: 0101 vs 0100 decided at bit 0", (0b0101 ^ 0b0100) == 1 and 0b0101 > 0b0100)
par = lambda w: bin(w).count("1") % 2
ok("B6 MTE Q2: even parity bit of 1011 = 1", par(0b1011) == 1); ok("B6 check a: odd parity bit of 1011 = 0", 1 - par(0b1011) == 0)
ok("B6 check b: 1001 + parity 1 → error", par(0b10011) == 1)
w = "110110"
ok("B7 logical left 2", w[2:] + "00" == "011000"); ok("B7 logical right 1", "0" + w[:-1] == "011011"); ok("B7 circular left 2", w[2:] + w[:2] == "011011")
ok("B7 circular right 1", w[-1] + w[:-1] == "011011"); ok("B7 arithmetic right 1", w[0] + w[:-1] == "111011")
ok("B7 check a: 1001 → 1100 (−7 → −4)", "1" + "1001"[:-1] == "1100" and (0b1001 - 16, 0b1100 - 16) == (-7, -4))
rot = {0: "3210", 1: "2103", 2: "1032", 3: "0321"}
ok("B7 barrel table: rotate left by s", all(rot[s_] == "".join(str((i - s_) % 4) for i in (3, 2, 1, 0)) for s_ in range(4)))
ok("B7 MUX for Y0", [rot[s_][3] for s_ in range(4)] == ["0", "3", "2", "1"])


def alu(a, b, s1, s0, cin):
    y = sum((((b >> i) & 1 & s0) | ((1 - ((b >> i) & 1)) & s1)) << i for i in range(4))
    return (a + y + cin) & 15


ok("B8 arithmetic circuit table", all(alu(a, b, 0, 0, 0) == a and alu(a, b, 0, 0, 1) == (a + 1) & 15 and alu(a, b, 0, 1, 0) == (a + b) & 15 and alu(a, b, 0, 1, 1) == (a + b + 1) & 15
   and alu(a, b, 1, 0, 0) == (a + (b ^ 15)) & 15 and alu(a, b, 1, 0, 1) == (a - b) & 15 and alu(a, b, 1, 1, 0) == (a - 1) & 15 and alu(a, b, 1, 1, 1) == a for a in range(16) for b in range(16)))
ok("B8 check a, b", alu(0b0110, 0b0011, 1, 0, 1) == 0b0011 and alu(0b0110, 0, 1, 1, 0) == 0b0101)

# ================================================================= Part C
def nor_latch(s, r, q, qb):
    for _ in range(6):
        q, qb = nor(r, qb), nor(s, q)
    return q, qb


ok("C1 NOR latch table", nor_latch(0, 1, 1, 0) == (0, 1) and nor_latch(1, 0, 0, 1) == (1, 0) and nor_latch(0, 0, 1, 0) == (1, 0) and nor_latch(0, 0, 0, 1) == (0, 1) and nor_latch(1, 1, 0, 1) == (0, 0))
jk = lambda j, k, q: (j & (1 - q)) | ((1 - k) & q)
ok("C2 JK table = JQ' + K'Q", all(jk(j, k, q) == [q, 0, 1, 1 - q][j << 1 | k] for j, k, q in product((0, 1), repeat=3)))
ok("C2 SR: Q+ = S + R'Q", all((s_ | ((1 - r) & q)) == [q, 0, 1][s_ << 1 | r] for s_, r, q in product((0, 1), repeat=3) if not (s_ and r)))
ok("C2 T = JK with J = K = T; D = JK with J = D, K = D'", all(jk(t, t, q) == t ^ q and jk(t, 1 - t, q) == t for t, q in product((0, 1), repeat=2)))
EXC = {(0, 0): ("0X", "0X", 0, 0), (0, 1): ("10", "1X", 1, 1), (1, 0): ("01", "X1", 0, 1), (1, 1): ("X0", "X0", 1, 0)}
for (q, qn), (sr, jk_, d, t) in EXC.items():
    for s_ in ((0, 1) if sr[0] == "X" else (int(sr[0]),)):
        for r in ((0, 1) if sr[1] == "X" else (int(sr[1]),)):
            if not (s_ and r):
                assert (s_ | ((1 - r) & q)) == qn
    for j in ((0, 1) if jk_[0] == "X" else (int(jk_[0]),)):
        for k in ((0, 1) if jk_[1] == "X" else (int(jk_[1]),)):
            assert jk(j, k, q) == qn
    assert d == qn and t == q ^ qn
ok("C3 excitation table", True)
ok("C3 D from SR, JK, T", all((d | ((1 - (1 - d)) & q)) == d and jk(d, 1 - d, q) == d and ((d ^ q) ^ q) == d for d, q in product((0, 1), repeat=2)))
ok("C3 conversions", all(((j & (1 - q)) | ((1 - (k & q)) & q)) == jk(j, k, q) and (((j & (1 - q)) | (k & q)) ^ q) == jk(j, k, q) for j, k, q in product((0, 1), repeat=3)))
import figs2  # noqa: E402  (the waveform data drawn in C2 and C4)
qpos = [v for _, v in qm.edge_ff("JK", {"J": figs2.W_J, "K": figs2.W_K}, figs2.RISE)[1:]]
ok("C4 JK positive edge: Q = 1 0 1 1 0 0", qpos == [1, 0, 1, 1, 0, 0])
ok("C4 inputs before rising edges", [(qm.level(figs2.W_J, t - 1e-6), qm.level(figs2.W_K, t - 1e-6)) for t in figs2.RISE] == [(1, 0), (0, 1), (1, 1), (1, 0), (0, 1), (0, 0)])
ok("C4 check a: negative edge", [v for _, v in qm.edge_ff("JK", {"J": figs2.W_J, "K": figs2.W_K}, figs2.FALL)[1:]] == [1, 0, 1, 1, 0, 0]
   and [(qm.level(figs2.W_J, t - 1e-6), qm.level(figs2.W_K, t - 1e-6)) for t in figs2.FALL] == [(1, 0), (0, 1), (1, 1), (1, 0), (0, 1), (0, 0)])
q, out = 0, []
for t in (1, 0, 0, 1, 1, 0):
    q ^= t; out.append(q)
ok("C4 check b: T flip-flop", out == [1, 1, 1, 0, 1, 1])
reg, seq = [0, 1, 1, 0], []
for _ in range(5):
    reg = [reg[2] ^ reg[3]] + reg[:3]; seq.append("".join(map(str, reg)))
ok("C5 slide 24: 0110 → 1011 → 0101 → 1010 (→ 1101 → 1110)", seq == ["1011", "0101", "1010", "1101", "1110"])
reg, seq = [0] * 4, []
for b in (1, 1, 0, 1):
    reg = [b] + reg[:3]; seq.append("".join(map(str, reg)))
ok("C5 SIPO loading 1011", seq == ["1000", "1100", "0110", "1011"])
reg, seq = [0] * 4, []
for _ in range(8):
    seq.append("".join(map(str, reg))); reg = [1 - reg[3]] + reg[:3]
ok("C6 Johnson sequence, MOD-8", seq == ["0000", "1000", "1100", "1110", "1111", "0111", "0011", "0001"] and reg == [0] * 4)
dec = ["Q0'Q3'", "Q0Q1'", "Q1Q2'", "Q2Q3'", "Q0Q3", "Q0'Q1", "Q1'Q2", "Q2'Q3"]
QN = ["Q0", "Q1", "Q2", "Q3"]
ok("C6 Johnson decode terms", all(sop_fn(dec[i], QN)[0](dict(zip(QN, map(int, s2)))) == int(i == j) for i in range(8) for j, s2 in enumerate(seq)))
reg, st = [0, 1, 0, 0], set()
for _ in range(8):
    st.add(tuple(reg)); reg = [1 - reg[3]] + reg[:3]
ok("C6 Johnson lock-out loop from 0100", not (st & {tuple(map(int, s2)) for s2 in seq}) and len(st) == 8)
ok("C7 decade: 1010 is the first state with Q3 = Q1 = 1", [n for n in range(16) if n & 8 and n & 2][0] == 10)
ok("C7 check b: MOD-7 uses Q2Q1Q0, MOD-12 uses Q3Q2", [n for n in range(8) if n & 7 == 7][0] == 7 and [n for n in range(16) if n & 12 == 12][0] == 12)
ok("C7 flip-flop counts", all((2 ** (n - 1) < m <= 2 ** n) for m, n in ((10, 4), (60, 6), (12, 4), (6, 3))))
ok("C7 check a: 100 ns, 10 MHz", (4 * 25, 1e3 / 100) == (100, 10.0))


def run_counter(eqs, names, kind, start, steps):
    """eqs: {bit name: expr or (J expr, K expr)}; returns the list of visited states."""
    s, seq = start, []
    n = len(names)
    for _ in range(steps):
        seq.append(s)
        env = {v: (s >> (n - 1 - i)) & 1 for i, v in enumerate(names) if v[0] == "Q"}
        env.update({v: x for v, x in extra.items()})
        nxt = 0
        for i, v in enumerate(q for q in names if q[0] == "Q"):
            q = env[v]
            if kind == "T":
                q ^= sop_fn(eqs[v], list(env))[0](env)
            elif kind == "D":
                q = sop_fn(eqs[v], list(env))[0](env)
            else:
                q = jk(sop_fn(eqs[v][0], list(env))[0](env), sop_fn(eqs[v][1], list(env))[0](env), q)
            nxt = nxt << 1 | q
        s = nxt
    return seq


extra = {}
Q3 = ["Q2", "Q1", "Q0"]
ok("C8 MTE Q8: T0 = 1, T1 = Q0, T2 = Q1Q0 counts 0–7", run_counter({"Q2": "Q1Q0", "Q1": "Q0", "Q0": "1"}, Q3, "T", 0, 9) == [0, 1, 2, 3, 4, 5, 6, 7, 0])
tt = [(s, (s + 1) % 8, s ^ ((s + 1) % 8)) for s in range(8)]
ok("C8 T table rows", [format(t, "03b") for _, _, t in tt] == ["001", "011", "001", "111", "001", "011", "001", "111"])
ok("C8 Gray counter (JK)", run_counter({"Q2": ("Q1Q0'", "Q1'Q0'"), "Q1": ("Q2'Q0", "Q2Q0"), "Q0": ("Q2'Q1' + Q2Q1", "Q2'Q1 + Q2Q1'")}, Q3, "JK", 0, 9) == [0, 1, 3, 2, 6, 7, 5, 4, 0])
ok("C8 3-bit down (T)", run_counter({"Q2": "Q1'Q0'", "Q1": "Q0'", "Q0": "1"}, Q3, "T", 0, 9) == [0, 7, 6, 5, 4, 3, 2, 1, 0])
Q4 = ["Q3", "Q2", "Q1", "Q0"]
ok("C8 decade (T)", run_counter({"Q3": "Q2Q1Q0 + Q3Q0", "Q2": "Q1Q0", "Q1": "Q3'Q0", "Q0": "1"}, Q4, "T", 0, 11) == list(range(10)) + [0])
M6 = {"Q2": ("Q1Q0", "Q0"), "Q1": ("Q2'Q0", "Q0"), "Q0": ("1", "1")}
ok("C8 MOD-6 (JK)", run_counter(M6, Q3, "JK", 0, 7) == [0, 1, 2, 3, 4, 5, 0])
ok("C8 MOD-6 unused states: 6 → 7 → 0", run_counter(M6, Q3, "JK", 6, 3) == [6, 7, 0])
for x_, want in ((0, [0, 1, 2, 3, 0]), (1, [0, 3, 2, 1, 0])):
    extra = {"X": x_}
    assert run_counter({"Q1": "Q1'Q0'X + Q1'Q0X' + Q1Q0'X' + Q1Q0X", "Q0": "Q0'"}, ["Q1", "Q0"], "D", 0, 5) == want
ok("C8 2-bit up/down (D): D1 = Q1 ⊕ Q0 ⊕ X", all((q1 ^ q0 ^ x) == sop_fn("Q1'Q0'X + Q1'Q0X' + Q1Q0'X' + Q1Q0X", ["Q1", "Q0", "X"])[0]({"Q1": q1, "Q0": q0, "X": x}) for q1, q0, x in product((0, 1), repeat=3)))
for u, want in ((1, list(range(8)) + [0]), (0, [0, 7, 6, 5, 4, 3, 2, 1, 0])):
    extra = {"U": u}
    assert run_counter({"Q2": "Q1Q0U + Q1'Q0'U'", "Q1": "Q0U + Q0'U'", "Q0": "1"}, Q3, "T", 0, 9) == want
ok("C8 3-bit up/down (T, slide 33)", True)
extra = {}
ok("C8 check a: 2-bit down (T)", run_counter({"Q1": "Q0'", "Q0": "1"}, ["Q1", "Q0"], "T", 3, 5) == [3, 2, 1, 0, 3])
ok("C8 check b: 3-bit down (D)", run_counter({"Q2": "Q2Q1 + Q2Q0 + Q2'Q1'Q0'", "Q1": "Q1'Q0' + Q1Q0", "Q0": "Q0'"}, Q3, "D", 0, 9) == [0, 7, 6, 5, 4, 3, 2, 1, 0])
ok("mock Q14: 2-bit up (JK, T, D)", run_counter({"Q1": ("Q0", "Q0"), "Q0": ("1", "1")}, ["Q1", "Q0"], "JK", 0, 5) == [0, 1, 2, 3, 0]
   and run_counter({"Q1": "Q0", "Q0": "1"}, ["Q1", "Q0"], "T", 0, 5) == [0, 1, 2, 3, 0] and run_counter({"Q1": "Q1'Q0 + Q1Q0'", "Q0": "Q0'"}, ["Q1", "Q0"], "D", 0, 5) == [0, 1, 2, 3, 0])
ok("C9 fmax = 43.5 MHz, hold 9 ≥ 2", abs(1e3 / (8 + 12 + 3) - 43.5) < 0.05 and 8 + 1 >= 2)
ok("C9 checks: 37.0 MHz, 50 MHz", abs(1e3 / 27 - 37.0) < 0.05 and 1e3 / 20 == 50)

# ================================================================= Part D
MEALY = {"A": (("A", 0), ("B", 0)), "B": (("A", 0), ("C", 0)), "C": (("D", 0), ("C", 0)), "D": (("A", 0), ("B", 1))}
MOORE = {"A": ("A", "B", 0), "B": ("A", "C", 0), "C": ("D", "C", 0), "D": ("A", "E", 0), "E": ("A", "C", 1)}


def run_mealy(bits):
    s, z = "A", []
    for b in bits:
        s, o = MEALY[s][b]; z.append(o)
    return z


def run_moore(tm, bits):
    s, z = next(iter(tm)), []
    for b in bits:
        s = tm[s][b]; z.append(tm[s][2])
    return z


ref = lambda bits, pat: [int(i >= len(pat) - 1 and bits[i - len(pat) + 1:i + 1] == pat) for i in range(len(bits))]
ok("D2 1101101 → 0001001", run_mealy([1, 1, 0, 1, 1, 0, 1]) == [0, 0, 0, 1, 0, 0, 1])
random.seed(7)
streams = [[random.randint(0, 1) for _ in range(60)] for _ in range(300)]
ok("D2 Mealy 1101 detector on 300 random streams", all(run_mealy(b) == ref(b, [1, 1, 0, 1]) for b in streams))
ok("D2 Moore 1101 detector on 300 random streams", all(run_moore(MOORE, b) == ref(b, [1, 1, 0, 1]) for b in streams))
M1011 = {"S0": ("S0", "S1", 0), "S1": ("S2", "S1", 0), "S2": ("S0", "S3", 0), "S3": ("S2", "S4", 0), "S4": ("S2", "S1", 1)}
ok("D2 check a / mock Q17: Moore 1011 on 300 random streams", all(run_moore(M1011, b) == ref(b, [1, 0, 1, 1]) for b in streams))


def fsm_eqs(label, table, codes, eqs, names, zexpr, znames, mealy=False):
    nb = len(names) - 1
    D = [[] for _ in range(nb)]; Z = []
    for s, row in table.items():
        for x in (0, 1):
            ns = row[x][0] if mealy else row[x]
            m = codes[s] << 1 | x
            for b in range(nb):
                if (codes[ns] >> (nb - 1 - b)) & 1:
                    D[b].append(m)
            if mealy and row[x][1]:
                Z.append(m)
    used = {codes[s] << 1 | x for s in table for x in (0, 1)}
    dc = [m for m in range(2 ** len(names)) if m not in used]
    for b in range(nb):
        check_sop(f"{label} D for {names[b]}", eqs[b], D[b], dc, names)
    if mealy:
        check_sop(f"{label} Z", zexpr, Z, dc, names)
    else:
        check_sop(f"{label} z", zexpr, [codes[s] for s in table if table[s][2]], [c for c in range(2 ** nb) if c not in codes.values()], znames)


Y = ["Y1", "Y2", "X"]
fsm_eqs("D2 Gray", MEALY, {"A": 0, "B": 1, "C": 3, "D": 2}, ["Y1Y2 + XY2", "X"], Y, "XY1Y2'", None, mealy=True)
fsm_eqs("D2 counting", MEALY, {"A": 0, "B": 1, "C": 2, "D": 3}, ["Y1Y2' + XY1'Y2", "XY1'Y2' + X'Y1Y2' + XY1Y2"], Y, "XY1Y2", None, mealy=True)
Y3 = ["Y2", "Y1", "Y0", "X"]
fsm_eqs("D2 Moore 1101", MOORE, {s: i for i, s in enumerate("ABCDE")}, ["Y1Y0X", "Y2X + Y1Y0' + Y1'Y0X", "Y1Y0'X' + Y2'Y1'Y0'X"], Y3, "Y2", ["Y2", "Y1", "Y0"])
fsm_eqs("mock Q17 Moore 1011", M1011, {s: i for i, s in enumerate(M1011)}, ["Y1Y0X", "Y0X' + Y1Y0'X + Y2X'", "Y1'X + Y0'X"], Y3, "Y2", ["Y2", "Y1", "Y0"])
NO = dict(MEALY); NO["D"] = (("A", 0), ("A", 1))
def nonoverlap(bits):
    s, z = "A", []
    for b in bits:
        s, o = NO[s][b]; z.append(o)
    return z
def ref_no(bits, pat):
    out, i, last = [0] * len(bits), 0, -1
    for i in range(len(bits)):
        if i - len(pat) + 1 > last and bits[i - len(pat) + 1:i + 1] == pat and i >= len(pat) - 1:
            out[i] = 1; last = i
    return out
ok("D2 check b: non-overlapping version (D —1/1→ A)", all(nonoverlap(b) == ref_no(b, [1, 1, 0, 1]) for b in streams))
M111 = {"A": (("A", 0), ("B", 0)), "B": (("A", 0), ("C", 0)), "C": (("A", 0), ("C", 1))}
def run111(bits):
    s, z = "A", []
    for b in bits:
        s, o = M111[s][b]; z.append(o)
    return z
ok("D2 check c: 3-state Mealy 111 detector", all(run111(b) == ref(b, [1, 1, 1]) for b in streams))
tb = lambda c0, c1: {s: ((a[0], int(a[2])), (b[0], int(b[2]))) for s, a, b in zip("ABCDEFGH", c0.split(), c1.split())}
P = lambda parts: [list(p) for p in parts.split()]
t5 = tb("C/1 C/1 B/1 D/0 E/0", "B/0 E/0 E/0 B/1 A/1")
ok("D3 partitions (ABC)(DE) → (A)(BC)(DE) → (A)(BC)(D)(E)", qm.reduce_states(t5) == [P("ABC DE"), P("A BC DE"), P("A BC D E")])
red = {"A": "B/1 B/0", "B": "B/1 E/0", "D": "D/0 B/1", "E": "E/0 A/1"}
ok("D3 reduced table", all(red[s] == " ".join(f"{'B' if n == 'C' else n}/{o}" for n, o in t5[s]) for s in red))
imp = {("A", "B"): [("B", "E")], ("A", "C"): [("B", "C"), ("B", "E")], ("D", "E"): [("A", "B")]}
for (a, b), need in imp.items():
    got = sorted({tuple(sorted((t5[a][x][0], t5[b][x][0]))) for x in (0, 1)} - {(a, b)} - {(s, s) for s in "ABCDE"})
    assert got == sorted(need), (a, b, got)
ok("D3 implication-table cells", {tuple(sorted((t5["B"][x][0], t5["C"][x][0]))) for x in (0, 1)} <= {("B", "C"), ("E", "E")})
ok("D3 check (slide 17): (AD)(BE)(CF)(G)(H)", qm.reduce_states(tb("E/0 A/1 C/0 B/0 D/1 C/0 H/1 C/1", "D/0 F/0 A/1 A/0 C/0 D/1 G/1 B/1")) == [P("AD BE CF GH"), P("AD BE CF G H")])
ok("mock Q15 (slide 18): (AF)(BCH)(D)(E)(G)", qm.reduce_states(tb("D/0 C/1 C/1 D/0 C/1 D/0 G/0 B/1", "D/0 D/0 D/0 B/0 F/0 D/0 G/0 D/0")) == [P("ADFG BCEH"), P("AFG BCEH D"), P("AF BCH D E G")])
s, seq = (1, 0, 0), []
for _ in range(8):
    seq.append("".join(map(str, s))); s = (s[1] ^ s[2], s[0], s[1])
ok("D6 LFSR: 7 states", seq == ["100", "010", "101", "110", "111", "011", "001", "100"] and [int(x[2]) for x in seq[:7]] == [0, 0, 1, 0, 1, 1, 1])
f555 = 1.44 / ((1e3 + 2 * 10e3) * 10e-9)
ok("D6 555: 6.86 kHz, 52%", abs(f555 - 6857) < 5 and abs(11 / 21 - 0.52) < 0.005)
ok("D6 ring oscillator 50 MHz", 1 / (2 * 5 * 2e-9) == 50e6)
HZ = [1, 3, 4, 5, 9, 11, 13, 14, 15]
ok("D7 ΠM → Σm", sorted(set(range(16)) - {0, 2, 6, 7, 8, 10, 12}) == HZ)
check_sop("D7 minimal cover", "B'D + C'D + A'BC' + ABC", HZ, [], "ABCD")
check_sop("D7 hazard-free cover", "B'D + C'D + A'BC' + ABC + AD", HZ, [], "ABCD", minimal=False)


def uncovered_pairs(expr):
    _, terms = sop_fn(expr, "ABCD")
    cov = lambda m, t: all(((m >> (3 - "ABCD".index(v))) & 1) != neg for v, neg in t)
    return sorted((a, b) for a in HZ for b in HZ if a < b and bin(a ^ b).count("1") == 1 and not any(cov(a, t) and cov(b, t) for t in terms))


ok("D7 hazards at 11–15 and 13–15 only", uncovered_pairs("B'D + C'D + A'BC' + ABC") == [(11, 15), (13, 15)])
ok("D7 none left with AD", uncovered_pairs("B'D + C'D + A'BC' + ABC + AD") == [])

# ================================================================= Part E
ok("E1 TTL noise margins 0.4 V, fan-out 10", abs((2.4 - 2.0) - 0.4) < 1e-9 and abs((0.8 - 0.4) - 0.4) < 1e-9 and min(16 / 1.6, 400 / 40) == 10)
ok("E1 speed-power 100 pJ", abs(10e-9 * 10e-3 - 100e-12) < 1e-15)
ok("E1 checks: 20; 0.9 V, 1.4 V; 10 ns", min(8 / 0.4, 400 / 20) == 20 and abs(4.4 - 3.5 - 0.9) < 1e-9 and abs(1.5 - 0.1 - 1.4) < 1e-9 and (8 + 12) / 2 == 10)
ok("E4 check b: 0.125 V", abs(-0.98 + 1.105 - 0.125) < 1e-9)
ok("E5 check b: power halves", 0.5 ** 2 * 2 == 0.5)
ok("E5 CMOS NAND", all((0 if (a and b) else 1) == nand(a, b) for a, b in product((0, 1), repeat=2)))
ok("E6 1K × 8: 10 lines, 8192 bits; 4 chips, 12 lines", (2 ** 10, 1024 * 8, 4096 // 1024, 2 ** 12) == (1024, 8192, 4, 4096))
ok("E6 check a: 14 lines, 8 chips", 2 ** 14 == 16 * 1024 and (64 // 16) * (8 // 4) == 8)
check_sop("E7 F1 direct", "A'B' + A'C' + B'C'", [0, 1, 2, 4], [], "ABC")
check_sop("E7 F1'", "AB + AC + BC", [3, 5, 6, 7], [], "ABC")
check_sop("E7 F2", "AB + AC + A'B'C'", [0, 5, 6, 7], [], "ABC")
check_pos("E7 F1 K-map groups", "(B' + C')(A' + C')(A' + B')", [0, 1, 2, 4], [], "ABC")
PAL = {"w": ("ABC' + A'B'CD'", [2, 12, 13]), "x": ("A + BCD", R(7, 15)), "y": ("A'B + CD + B'D'", [0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 15]),
       "z": ("ABC' + A'B'CD' + AC'D' + A'B'C'D", [1, 2, 8, 12, 13])}
for k_, (e_, on) in PAL.items():
    check_sop(f"E7 PAL {k_}", e_, on, [], "ABCD")
fz, _ = sop_fn("AC'D' + A'B'C'D", "ABCD"); fw, _ = sop_fn(PAL["w"][0], "ABCD")
ok("E7 z = w + AC'D' + A'B'C'D", all((fw(e) | fz(e)) == int(m in PAL["z"][1]) for m, e in envs("ABCD")))
check_sop("E7 check b F1", "A'B'C + BC' + AC'", [1, 2, 4, 6], [], "ABC"); check_sop("E7 check b F2", "A'B' + AB", [0, 1, 6, 7], [], "ABC"); check_sop("E7 check b F3", "C + A'B", [1, 2, 3, 5, 7], [], "ABC")
ok("E7 check c: 256 × 8 ROM", 2 ** 8 == 256 and 15 * 15 < 2 ** 8)

# ================================================================= Mock paper
ok("mock 2: ΠM(0,2,4,5,7)", sorted(set(range(8)) - {1, 3, 6}) == [0, 2, 4, 5, 7])
ok("mock 5: odd parity of 1101001 = 1", 1 - par(0b1101001) == 1); ok("mock 7: 4 flip-flops, 4 unused", 16 - 12 == 4)
ok("mock 9: 0.7 V, 0.3 V", abs(2.7 - 2.0 - 0.7) < 1e-9 and abs(0.8 - 0.5 - 0.3) < 1e-9)
cons = [m for m in range(16) if any((m >> i) & 3 == 3 for i in range(3))]
ok("mock 11 minterms", cons == [3, 6, 7, 11, 12, 13, 14, 15]); check_sop("mock 11", "AB + BC + CD", cons, [], "ABCD")
ok("mock 12 (practice set 1 Q6)", qm.mux1([0, 2, 5, 9, 11, 12, 14, 15], "PQRS") == ["S'", "S'", "S", "0", "S", "S", "S'", "1"])
P1 = [1] + R(4, 7) + R(10, 13); P2 = R(4, 7) + [10, 11]; P3 = R(4, 7) + R(9, 15)
check_sop("mock 18 F1", "A'B + BC' + AB'C + A'C'D", P1, [], "ABCD"); check_sop("mock 18 F2", "A'B + AB'C", P2, [], "ABCD"); check_sop("mock 18 F3", "B + AC + AD", P3, [], "ABCD")
f2_, _ = sop_fn("A'B + AB'C", "ABCD"); fr, _ = sop_fn("BC' + A'C'D", "ABCD")
ok("mock 18: F1 = F2 + BC' + A'C'D", all((f2_(e) | fr(e)) == int(m in P1) for m, e in envs("ABCD")))
ok("mock 19b: MOD-6 clears at 110", [n for n in range(8) if n & 6 == 6][0] == 6)

print(f"\nALL {N[0]} CHECKS PASS")
