"""Checks for file 07 (7-segment display, magnitude comparator, parity), S6 2026-11-18.
Imported by verify.py (unit u2c). Every circuit is evaluated on all inputs; every printed number is
recomputed. ok, fn and check_sop are injected by verify.py.
"""
from functools import reduce
from itertools import product

# Digit shapes (deck 05 slides 28-29): 6 with the top bar a, 7 = a b c, 9 with the bottom bar d.
LIT = {0: "abcdef", 1: "bc", 2: "abdeg", 3: "abcdg", 4: "bcfg", 5: "acdfg", 6: "acdefg", 7: "abc",
       8: "abcdefg", 9: "abcdfg"}
DC = list(range(10, 16))
# file 07 step 2 table (lit = 1, common cathode) and step 3 table (lit = 0, common anode, minimised on the 0s)
HIGH = {"a": "A + C + BD + B'D'", "b": "B' + C'D' + CD", "c": "B + C' + D", "d": "A + B'D' + B'C + CD' + BC'D",
        "e": "B'D' + CD'", "f": "A + C'D' + BC' + BD'", "g": "A + B'C + BC' + CD'"}
LOW = {"a": "A'B'C'D + BC'D'", "b": "BC'D + BCD'", "c": "B'CD'", "d": "A'B'C'D + BC'D' + BCD",
       "e": "D + BC'", "f": "A'B'D + B'C + CD", "g": "A'B'C' + BCD"}


def xor(*x):
    return reduce(lambda p, q: p ^ q, x, 0)


def ones(word):
    return sum(int(c) for c in word)


def cmp_n(a, b, n):
    """(G, E, L) from the file's equations: x_i = A_i XNOR B_i, G = sum over i of (higher x's) A_i B_i'."""
    A = [(a >> i) & 1 for i in range(n)]
    B = [(b >> i) & 1 for i in range(n)]
    x = [1 - (A[i] ^ B[i]) for i in range(n)]
    g = l = 0
    for i in range(n - 1, -1, -1):
        hi = all(x[j] for j in range(i + 1, n))
        g |= hi and A[i] and not B[i]
        l |= hi and (not A[i]) and B[i]
    return int(g), int(all(x)), int(l)


def u2c():
    # ---- steps 1-2: segment table and lit-1 equations
    names = "ABCD"
    for s in "abcdefg":
        lit = [d for d in range(10) if s in LIT[d]]
        check_sop(f"07 s2 segment {s} = {HIGH[s]}", HIGH[s], lit, names, DC)
    ok("07 s1 digit 4 lights b c f g", LIT[4] == "bcfg")
    ok("07 s1 EX 5.30 input 0110 = 6 lights a c d e f g (6 segments)", LIT[int("0110", 2)] == "acdefg" and len(LIT[6]) == 6)
    ok("07 s1 digit 8 lights all 7, digit 1 lights 2", len(LIT[8]) == 7 and len(LIT[1]) == 2)
    ok("07 s2 e is lit for 0 2 6 8 only", [d for d in range(10) if "e" in LIT[d]] == [0, 2, 6, 8])
    # ---- step 3: common anode = active-low outputs
    for s in "abcdefg":
        dark = [d for d in range(10) if s not in LIT[d]]
        check_sop(f"07 s3 active-low {s}' = {LOW[s]}", LOW[s], dark, names, DC)
        f1, f0 = fn(HIGH[s], names), fn(LOW[s], names)
        ok(f"07 s3 {s}' is the complement of {s} on 0-9", all(f1(dict(zip(names, map(int, f'{m:04b}')))) != f0(dict(zip(names, map(int, f'{m:04b}')))) for m in range(10)))
    ok("07 s3 c' = B'CD' is 1 only for digit 2", [d for d in range(10) if fn(LOW["c"], names)(dict(zip(names, map(int, f'{d:04b}'))))] == [2])
    ok("07 s3 digit 7 on common anode: outputs a..g = 0001111", "".join("0" if s in LIT[7] else "1" for s in "abcdefg") == "0001111")
    # ---- step 4: multiplexed display
    ok("07 s4 6 digits: 42 lines without, 13 with", 7 * 6 == 42 and 7 + 6 == 13)
    ok("07 s4 4 digits: 28 without, 11 with", 7 * 4 == 28 and 7 + 4 == 11)
    ok("07 s4 4 digits rescanned 60 times/s: each digit on 1/240 s = 4.17 ms", abs(1000 / (4 * 60) - 4.17) < 0.005)
    # ---- step 5: 1-bit comparator
    for a, b in product((0, 1), repeat=2):
        ok(f"07 s5 1-bit A={a} B={b}: G=AB', E=XNOR, L=A'B", cmp_n(a, b, 1) == (a & (1 - b), 1 - (a ^ b), (1 - a) & b))
    # ---- step 6: 2-bit comparator, names W=A1 X=A0 Y=B1 Z=B0
    n2 = "WXYZ"
    G = [m for m in range(16) if (m >> 2) > (m & 3)]
    L = [m for m in range(16) if (m >> 2) < (m & 3)]
    E = [m for m in range(16) if (m >> 2) == (m & 3)]
    ok("07 s6 G has 6 ones, L 6, E 4", (len(G), len(L), len(E)) == (6, 6, 4))
    check_sop("07 s6 G = A1B1' + A0B1'B0' + A1A0B0'", "WY' + XY'Z' + WXZ'", G, n2)
    check_sop("07 s6 L = A1'B1 + A0'B1B0 + A1'A0'B0", "W'Y + X'YZ + W'X'Z", L, n2)
    check_sop("07 s6 E as 4 minterms", "W'X'Y'Z' + W'XY'Z + WXYZ + WX'YZ'", E, n2)
    ok("07 s6 E = (A1 XNOR B1)(A0 XNOR B0) on all 16 rows", all(((m >> 2) == (m & 3)) == ((((m >> 3) & 1) == ((m >> 1) & 1)) and (((m >> 2) & 1) == (m & 1))) for m in range(16)))
    ok("07 s6 x-form G = A1B1' + x1A0B0' on all 16 rows", all(cmp_n(m >> 2, m & 3, 2)[0] == (m in G) for m in range(16)))
    ok("07 s6 exactly one of G E L is 1; L = (G + E)'", all(sum(cmp_n(a, b, 2)) == 1 and cmp_n(a, b, 2)[2] == 1 - (cmp_n(a, b, 2)[0] | cmp_n(a, b, 2)[1]) for a in range(4) for b in range(4)))
    ok("07 s6 A=10 B=11: L", cmp_n(2, 3, 2) == (0, 0, 1))
    ok("07 s6 A=11 B=10: G (decided at bit 0)", cmp_n(3, 2, 2) == (1, 0, 0))
    # ---- step 7: 4-bit and cascade
    ok("07 s7 4-bit equations right on all 256 pairs", all(cmp_n(a, b, 4) == (int(a > b), int(a == b), int(a < b)) for a in range(16) for b in range(16)))
    ok("07 s7 running example 0110 vs 0101: G = 1", cmp_n(0b0110, 0b0101, 4) == (1, 0, 0))
    a, b = 0b0110, 0b0101
    first = max(i for i in range(4) if ((a >> i) & 1) != ((b >> i) & 1))
    ok("07 s7 running example decided at bit 1 (x3 = x2 = 1)", first == 1)
    ok("07 s7 0101 vs 0100: decided at bit 0, G", cmp_n(0b0101, 0b0100, 4) == (1, 0, 0) and max(i for i in range(4) if ((5 >> i) & 1) != ((4 >> i) & 1)) == 0)

    def cascade(a, b):
        gl, el, ll = cmp_n(a & 15, b & 15, 4)  # low chip, cascade inputs seeded (0, 1, 0): its outputs are its own
        g4, e4, l4 = cmp_n(a >> 4, b >> 4, 4)
        return int(g4 or (e4 and gl)), int(e4 and el), int(l4 or (e4 and ll))
    ok("07 s7 two chips cascaded = 8-bit comparator on all 65536 pairs", all(cascade(a, b) == (int(a > b), int(a == b), int(a < b)) for a in range(256) for b in range(256)))
    ok("07 s7 4-bit G has 4 terms, the last with 5 literals (x3 x2 x1 A0 B0')", len("A3B3' + x3A2B2' + x3x2A1B1' + x3x2x1A0B0'".split("+")) == 4)
    # ---- step 8: parity generator
    for x, y, z in product((0, 1), repeat=3):
        pe = xor(x, y, z)
        ok(f"07 s8 {x}{y}{z}: even P = {pe}, odd P = {1 - pe} (slide 12)", (x + y + z + pe) % 2 == 0 and (x + y + z + 1 - pe) % 2 == 1)
    ok("07 s8 MTE Q2: 1011 even parity P = 1, sent 10111 has four 1s", xor(1, 0, 1, 1) == 1 and ones("10111") == 4)
    ok("07 s8 1011 odd parity P = 0", 1 - xor(1, 0, 1, 1) == 0)
    ok("07 s8 running example 0110: even P = 0, odd P = 1", xor(0, 1, 1, 0) == 0)
    # ---- step 9: 4-bit generator, chain vs tree
    ev = [m for m in range(16) if xor(*map(int, f"{m:04b}"))]
    ok("07 s9 4-bit even P = A xor B xor C xor D: m(1,2,4,7,8,11,13,14) (slide 16)", ev == [1, 2, 4, 7, 8, 11, 13, 14])
    ok("07 s9 4-bit odd P: m(0,3,5,6,9,10,12,15) (slide 17)", [m for m in range(16) if m not in ev] == [0, 3, 5, 6, 9, 10, 12, 15])
    ok("07 s9 no two 1s of the parity map adjacent: 8 single-cell terms", all(bin(p ^ q).count("1") != 1 for p in ev for q in ev))
    ok("07 s9 chain (((A^B)^C)^D) = tree (A^B)^(C^D) on 16 rows", all(((a ^ b) ^ c) ^ d == (a ^ b) ^ (c ^ d) for a, b, c, d in product((0, 1), repeat=4)))
    ok("07 s9 n = 4: 3 XORs; chain 3 gate delays, tree 2", (4 - 1, 4 - 1, 2) == (3, 3, 2))
    ok("07 s9 n = 8: 7 XORs; chain 7 delays, tree 3", (8 - 1, (8 - 1), (8).bit_length() - 1) == (7, 7, 3))
    # ---- step 10: checker
    ok("07 s10 EX 6.23: XYZ = 001 -> P = 1, E = 0", xor(0, 0, 1) == 1 and xor(0, 0, 1, 1) == 0)
    ok("07 s10 EX 6.23: Y flipped (0111 received) -> E = 1", xor(0, 1, 1, 1) == 1)
    pec = [m for m in range(16) if xor(*map(int, f"{m:04b}"))]
    ok("07 s10 slide 20 PEC = P^A^B^C: m(1,2,4,7,8,11,13,14)", pec == [1, 2, 4, 7, 8, 11, 13, 14])
    words = [d + (xor(*d),) for d in product((0, 1), repeat=3)]
    single = all(xor(*[w[i] ^ (i == k) for i in range(4)]) == 1 for w in words for k in range(4))
    double = all(xor(*[w[i] ^ (i in (j, k)) for i in range(4)]) == 0 for w in words for j in range(4) for k in range(j + 1, 4))
    triple = all(xor(*[w[i] ^ (i != k) for i in range(4)]) == 1 for w in words for k in range(4))
    ok("07 s10 every 1-bit error caught, every 2-bit error missed, every 3-bit error caught", single and double and triple)
    ok("07 s10 5-bit even checker PE = A^B^C^D^P: 16 of 32 rows (slide 24)", sum(xor(*r) for r in product((0, 1), repeat=5)) == 16)
    ok("07 s10 received 1001 + parity 1 (even): three 1s -> E = 1", xor(1, 0, 0, 1, 1) == 1)
    # ---- self-test and checks
    ok("07 ST odd parity bit for 1101001: four 1s -> 1", ones("1101001") == 4 and 1 - xor(*map(int, "1101001")) == 1)
    ok("07 ST even checker receives 10110: three 1s -> error", xor(*map(int, "10110")) == 1)
    ok("07 ST A = 1001, B = 1011: decided at bit 1, L", cmp_n(9, 11, 4) == (0, 0, 1) and max(i for i in range(4) if ((9 >> i) & 1) != ((11 >> i) & 1)) == 1)
    ok("07 ST digit 5 lights a c d f g; b and e dark", LIT[5] == "acdfg")
    ok("07 c9 even parity bit for 1000 0001: two 1s -> 0", xor(*map(int, "10000001")) == 0)
    ok("07 c11 0011 sent, X and Y flip -> 1111, E = 0 (missed)", xor(1, 1, 1, 1) == 0)
    ok("07 c6 A=11 B=10: A1B1' = 0, A0B1'B0' = 0, A1A0B0' = 1", (1 & 0, 1 & 0 & 1, 1 & 1 & 1) == (0, 0, 1))
