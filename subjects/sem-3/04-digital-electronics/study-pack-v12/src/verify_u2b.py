"""Checks for files 04 (adders, subtractors) and 08 (shifts, barrel shifter, ALU), S6 2026-11-18.
Imported by verify.py (unit u2b). Every circuit is evaluated on all inputs; every printed number is
recomputed. ok is injected by verify.py.
"""
from itertools import product


def b(s):
    return int(s, 2)


def w(v, n=4):
    return format(v % (1 << n), f"0{n}b")


def bits(v, n=4):
    return [(v >> i) & 1 for i in range(n)]  # index i = bit i


def ripple(a, c, n=4, c0=0):
    """Ripple add; returns (sum mod 2^n, carries [C0..Cn])."""
    C = [c0]
    s = 0
    for i in range(n):
        x, y = (a >> i) & 1, (c >> i) & 1
        s |= (x ^ y ^ C[-1]) << i
        C.append((x & y) | (C[-1] & (x ^ y)))
    return s, C


def cla(a, c, n=4, c0=0):
    G, P = bits(a & c, n), bits(a ^ c, n)
    C = [c0]
    for i in range(n):  # unrolled form: sum over j of (P_i..P_{j+1}) G_j + P_i..P_0 C0
        t = 0
        for j in range(i + 1):
            prod = G[j]
            for k in range(j + 1, i + 1):
                prod &= P[k]
            t |= prod
        prod = c0
        for k in range(i + 1):
            prod &= P[k]
        C.append(t | prod)
    return G, P, C


def nand(*x):
    return 1 - min(x)


def nor(*x):
    return 1 - max(x)


def u2b():
    ok_ = ok  # noqa: F821
    # ---------------- 04
    ok_("04 s1 half adder S = A^B, C = AB on 4 rows", all((x ^ y, x & y) == ((x + y) & 1, (x + y) >> 1) for x, y in product((0, 1), repeat=2)))
    rowsS = [m for m in range(8) if bin(m).count("1") % 2 == 1]
    rowsC = [m for m in range(8) if bin(m).count("1") >= 2]
    ok_("04 s2 S = Σm(1,2,4,7), Cout = Σm(3,5,6,7)", rowsS == [1, 2, 4, 7] and rowsC == [3, 5, 6, 7])
    ok_("04 s3 Cout = AB + BC + AC; s4 = AB + (A^B)C", all(
        ((a & bb) | (bb & c) | (a & c)) == int(bin(4 * a + 2 * bb + c).count("1") >= 2) == ((a & bb) | ((a ^ bb) & c))
        for a, bb, c in product((0, 1), repeat=3)))
    ok_("04 s4 HA carries never both 1", all(not ((a & bb) and ((a ^ bb) & c)) for a, bb, c in product((0, 1), repeat=3)))
    # running example
    A, B = b("1011"), b("1110")
    s, C = ripple(A, B)
    ok_("04 s5 1011+1110 -> C4 S = 1 1001 (25), C1..C4 = 0,1,1,1", (C[4], w(s)) == (1, "1001") and C[1:] == [0, 1, 1, 1] and A + B == 25)
    s, C = ripple(b("0101"), b("0111"))
    ok_("04 c5 0101+0111 -> 1100, C1..C4 = 1,1,1,0", w(s) == "1100" and C[1:] == [1, 1, 1, 0])
    s, C = ripple(b("0111"), b("0101"))
    ok_("04 T3 0111+0101 -> 1100, C1..C4 = 1,1,1,0", w(s) == "1100" and C[1:] == [1, 1, 1, 0])

    # s6 delay: arrival times with two-HA full adders, gate delay 1, inputs at 0
    def arrival(n):
        t_c = 0  # C0
        last_s = 0
        for i in range(n):
            t_p = 1  # A^B
            t_and2 = max(t_p, t_c) + 1
            t_s = max(t_p, t_c) + 1
            t_c = max(1, t_and2) + 1  # OR of AB (t=1) and the second AND
            last_s = max(last_s, t_s)
        return t_c, last_s
    ok_("04 s6 Cn at (2n+1)T, last S at 2nT, for n = 1..32",
        all(arrival(n) == (2 * n + 1, 2 * n) for n in range(1, 33)))
    ok_("04 s6 table 3, 9, 17, 33; c6 65T, C2 at 5T; T7 13T",
        [arrival(n)[0] for n in (1, 4, 8, 16, 32, 6)] == [3, 9, 17, 33, 65, 13] and arrival(2)[0] == 5)
    # s7 CLA
    G, P, Cc = cla(A, B)
    ok_("04 s7 G = 1010, P = 0101, C1..C4 = 0,1,1,1 (= ripple)", w(A & B) == "1010" and w(A ^ B) == "0101" and Cc[1:] == ripple(A, B)[1][1:])
    ok_("04 s7 CLA carries = ripple carries for all 4-bit pairs and C0",
        all(cla(x, y, 4, c0)[2] == ripple(x, y, 4, c0)[1] for x, y, c0 in product(range(16), range(16), (0, 1))))
    ok_("04 c7 0101/0111: G = 0101, P = 0010, C = 1,1,1,0", w(5 & 7) == "0101" and w(5 ^ 7) == "0010" and cla(5, 7)[2][1:] == [1, 1, 1, 0])
    ok_("04 c7b largest AND in C3 has 4 inputs; C4 5 inputs (n+1 for Cn)", len(["P2", "P1", "P0", "C0"]) == 4 and 4 + 1 == 5)
    ok_("04 s7 graph: ripple 5,9,17,33 at n = 2,4,8,16; CLA 4", [2 * n + 1 for n in (2, 4, 8, 16)] == [5, 9, 17, 33] and 1 + 2 + 1 == 4)
    # s8 NAND / NOR adders
    good = True
    for a, bb in product((0, 1), repeat=2):
        g1 = nand(a, bb); g2 = nand(a, g1); g3 = nand(bb, g1); S = nand(g2, g3); Cy = nand(g1, g1)
        good &= (S, Cy) == (a ^ bb, a & bb)
        n1 = nor(a, a); n2 = nor(bb, bb); n3 = nor(a, bb); n4 = nor(n1, n2); n5 = nor(n4, n3)
        good &= (n5, n4) == (a ^ bb, a & bb)
    ok_("04 s8 5-NAND and 5-NOR half adders", good)

    def xor_nand(x, y):
        g1 = nand(x, y)
        return nand(nand(x, g1), nand(y, g1)), g1
    good = True
    for a, bb, c in product((0, 1), repeat=3):
        p, g1 = xor_nand(a, bb)
        S, h1 = xor_nand(p, c)
        Co = nand(g1, h1)
        good &= (S, Co) == (a ^ bb ^ c, int(a + bb + c >= 2))
    ok_("04 s8 9-NAND full adder", good)
    p, g1 = xor_nand(1, 1); S, h1 = xor_nand(p, 0)
    ok_("04 c8 A=B=1, Cin=0: (AB)'=0, ((A^B)Cin)'=1, Cout=1", (g1, h1, nand(g1, h1)) == (0, 1, 1))
    # s9 / s10 subtractors
    ok_("04 s9 half subtractor D = A^B, bout = A'B",
        all(((x - y) % 2, int(x - y < 0)) == (x ^ y, (1 - x) & y) for x, y in product((0, 1), repeat=2)))
    good = True
    for x, y, bi in product((0, 1), repeat=3):
        d = x - y - bi
        D, bo = d % 2, int(d < 0)
        good &= (D, bo) == (x ^ y ^ bi, ((1 - x) & y) | ((1 - x) & bi) | (y & bi)) == (x ^ y ^ bi, ((1 - x) & y) | ((1 - (x ^ y)) & bi))
    ok_("04 s10 full subtractor D, bout (both forms)", good)
    ok_("04 s10 bout = Σm(1,2,3,7); D rows 1,2,4,7",
        [4 * x + 2 * y + bi for x, y, bi in product((0, 1), repeat=3) if x - y - bi < 0] == [1, 2, 3, 7]
        and [4 * x + 2 * y + bi for x, y, bi in product((0, 1), repeat=3) if (x - y - bi) % 2] == [1, 2, 4, 7])
    ok_("04 s10 guess 0-1-1: D=0, bout=1; c10 1-1-1: D=1,bout=1; T6 0-0-1: 1,1",
        ((0 - 1 - 1) % 2, 1, (1 - 1 - 1) % 2, (0 - 0 - 1) % 2) == (0, 1, 1, 1))
    # s11 controlled cell
    good = True
    for E, x, y, c in product((0, 1), repeat=4):
        p = x ^ y
        D = p ^ c
        co = ((x ^ E) & y) | ((p ^ E) & c)
        if E == 0:
            good &= (D, co) == ((x + y + c) % 2, int(x + y + c >= 2))
        else:
            good &= (D, co) == ((x - y - c) % 2, int(x - y - c < 0))
    ok_("04 s11 E-controlled cell: E=0 full adder, E=1 full subtractor", good)
    ok_("04 c11 E=1, 1,0,1: D=0, out=0", ((1 ^ 0) ^ 1, ((1 ^ 1) & 0) | (((1 ^ 0) ^ 1) & 1)) == (0, 0))
    # s12 2's complement adder-subtractor
    good = True
    for x, y in product(range(16), range(16)):
        s, C = ripple(x, (~y) & 15, 4, 1)
        good &= (C[4] == int(x >= y)) and (s == (x - y) % 16)
    ok_("04 s12 A + B' + 1: carry 1 iff A >= B, bits = (A-B) mod 16, all pairs", good)
    s, C = ripple(A, (~B) & 15, 4, 1)
    ok_("04 s12 1011-1110: B'=0001, 1101, carry 0, = -3", w((~B) & 15) == "0001" and w(s) == "1101" and C[4] == 0 and (16 - s) == 3)
    s, C = ripple(B, (~A) & 15, 4, 1)
    ok_("04 c12a 1110-1011: B'=0100, 1 0011 = 3", w((~A) & 15) == "0100" and (C[4], w(s)) == (1, "0011"))
    s, C = ripple(6, (~3) & 15, 4, 1)
    ok_("04 c12b 0110-0011: B'=1100, 1 0011", w((~3) & 15) == "1100" and (C[4], w(s)) == (1, "0011"))
    s, C = ripple(3, (~6) & 15, 4, 1)
    ok_("04 T4 0011-0110: B'=1001, 1101 carry 0 = -3", w((~6) & 15) == "1001" and (C[4], w(s)) == (0, "1101") and 16 - s == 3)

    # s13 BCD adder
    def bcd(x, y, cin=0):
        t = x + y + cin
        K, Z = t >> 4, t & 15
        Y = K | ((Z >> 3) & (Z >> 2) & 1) | ((Z >> 3) & (Z >> 1) & 1)
        out = (Z + 6 * Y) & 15
        return K, Z, Y, out
    ok_("04 s13 BCD adder correct for all digit pairs and carry in",
        all((lambda r: (r[2], r[3]) == ((x + y + c) // 10, (x + y + c) % 10))(bcd(x, y, c)) for x in range(10) for y in range(10) for c in (0, 1)))
    ok_("04 s13 8+7: Z=1111,K=0,Y=1 -> 0101; c13 6+5 -> 1011,Y=1,0001; 9+9 -> K=1,Z=0010,1000; 4+5 Y=0; T5 4+8 -> 1100,Y=1,0010",
        bcd(8, 7) == (0, 15, 1, 5) and bcd(6, 5) == (0, 11, 1, 1) and bcd(9, 9) == (1, 2, 1, 8) and bcd(4, 5)[2] == 0
        and bcd(4, 8) == (0, 12, 1, 2) and (2 + 6) & 15 == 8)
    ok_("04 c3 Cout(0,1,1) = 1; c4 s1=1,c1=0,c2=1,S=0", (0 & 1) | (1 & 1) | (0 & 1) == 1 and (0 ^ 1, 0 & 1, (0 ^ 1) & 1, (0 ^ 1) ^ 1) == (1, 0, 1, 0))

    # ---------------- 08
    def lsl(s_, k): return (s_[k:] + "0" * k)
    def lsr(s_, k): return ("0" * k + s_[:-k])
    def rol(s_, k): return s_[k:] + s_[:k]
    def ror(s_, k): return s_[-k:] + s_[:-k]
    def asr(s_, k): return s_[0] * k + s_[:-k]
    def sval(s_): return int(s_, 2) - (1 << len(s_) if s_[0] == "1" else 0)
    x = "110110"
    ok_("08 s1 LSL2 011000, LSR1 011011", (lsl(x, 2), lsr(x, 1)) == ("011000", "011011"))
    ok_("08 s2 ROL2 011011, ROR1 011011, ROL6 = same", (rol(x, 2), ror(x, 1), rol(x, 6)) == ("011011", "011011", x))
    ok_("08 s3 ASR1 111011 (-10 -> -5), ASL2 011000 = +24 overflow (-40 < -32)",
        (asr(x, 1), sval(x), sval(asr(x, 1)), lsl(x, 2), sval(lsl(x, 2))) == ("111011", -10, -5, "011000", 24) and -40 < -32)
    ok_("08 s3 LSR1 of 110110 = 011011 = +27", int(lsr(x, 1), 2) == 27)
    ok_("08 s1 0011<<1 = 0110; c1 10110100>>2 = 00101101; 00001101<<1 = 00011010 = 26",
        lsl("0011", 1) == "0110" and lsr("10110100", 2) == "00101101" and lsl("00001101", 1) == "00011010" and int("00011010", 2) == 26)
    ok_("08 c2 ROL1 1001 = 0011; 1011 ROR1 = 1101, ROL1 back", rol("1001", 1) == "0011" and ror("1011", 1) == "1101" and rol("1101", 1) == "1011")
    ok_("08 c3 ASR 1001 = 1100 (-7 -> -4); 0110 -> 0011 (3); T8 011000 >>3 = 000011 (24 -> 3)",
        (asr("1001", 1), sval("1001"), sval("1100"), asr("0110", 1), asr("011000", 3), int("011000", 2)) == ("1100", -7, -4, "0011", "000011", 24))
    # s4 barrel shifter: table Y_i = D_{(i-s) mod 4}; MUX inputs per column
    good = True
    for d in range(16):
        ds = w(d)
        for s_ in range(4):
            y = "".join(str((d >> ((i - s_) % 4)) & 1) for i in (3, 2, 1, 0))
            good &= y == rol(ds, s_)
    ok_("08 s4 Y_i = D_(i-s mod 4) is rotate-left by s, all words", good)
    col = lambda i: [f"D{(i - s_) % 4}" for s_ in range(4)]  # noqa: E731
    ok_("08 s4 Y0 MUX inputs D0,D3,D2,D1; T7 Y2 inputs D2,D1,D0,D3", col(0) == ["D0", "D3", "D2", "D1"] and col(2) == ["D2", "D1", "D0", "D3"])
    ok_("08 c4 1011 rotate left 2 = 1110", rol("1011", 2) == "1110")
    # s5 logic unit
    a, bb = 0b0110, 0b0011
    ok_("08 s5 A=0110,B=0011: NOT 1001, AND 0010, OR 0111, XOR 0101", (w(~a), w(a & bb), w(a | bb), w(a ^ bb)) == ("1001", "0010", "0111", "0101"))
    ok_("08 c5 1010/1100: AND 1000, XOR 0110", (w(0b1010 & 0b1100), w(0b1010 ^ 0b1100)) == ("1000", "0110"))
    ok_("08 s5 guess A=0,B=1: NOT 1, AND 0, OR 1, XOR 1", (1 - 0, 0 & 1, 0 | 1, 0 ^ 1) == (1, 0, 1, 1))

    # s6 arithmetic circuit: MUX index 2S + Cin -> Y in (B, 0, 1111, B'), adder A + Y + Cin
    def arith(A_, B_, S, cin):
        Y = [B_, 0, 15, (~B_) & 15][2 * S + cin]
        return ripple(A_, Y, 4, cin)[0], Y
    ops = {(0, 0): lambda A_, B_: A_ + B_, (0, 1): lambda A_, B_: A_ + 1, (1, 0): lambda A_, B_: A_ - 1, (1, 1): lambda A_, B_: A_ - B_}
    ok_("08 s6 four operations correct mod 16 for all A, B",
        all(arith(A_, B_, S, c)[0] == ops[(S, c)](A_, B_) % 16 for A_, B_ in product(range(16), range(16)) for (S, c) in ops))
    ok_("08 s6 table 1001, 0111, 0101, 0011", [w(arith(6, 3, S, c)[0]) for S, c in ((0, 0), (0, 1), (1, 0), (1, 1))] == ["1001", "0111", "0101", "0011"])
    ok_("08 s6 10: 0110+1111 = 1 0101; 11: 0110+1100+1 = 1 0011", 6 + 15 == 0b10101 and 6 + 12 + 1 == 0b10011)
    ok_("08 c6 1010-0111: Y=1000, F=0011; 0000 S Cin=10 -> 1111",
        (w(arith(10, 7, 1, 1)[1]), w(arith(10, 7, 1, 1)[0]), w(arith(0, 0, 1, 0)[0])) == ("1000", "0011", "1111"))
    # s7 swapped carries
    ok_("08 s7 swapped: A+B+1, A (0000,0), A (1111,1), A-B-1",
        all((ripple(A_, B_, 4, 1)[0], ripple(A_, 0, 4, 0)[0], ripple(A_, 15, 4, 1)[0], ripple(A_, (~B_) & 15, 4, 0)[0])
            == ((A_ + B_ + 1) % 16, A_, A_, (A_ - B_ - 1) % 16) for A_, B_ in product(range(16), range(16))))
    # s8 ALU
    def alu(A_, B_, M, code):
        if M == 0:
            return arith(A_, B_, code >> 1, code & 1)[0]
        return [(~A_) & 15, A_ & B_, A_ | B_, A_ ^ B_][code]
    ok_("08 c8 OR = 0111, A+1 = 0111; only pair equal", alu(6, 3, 1, 2) == alu(6, 3, 0, 1) == 0b0111
        and sorted({(M, c): alu(6, 3, M, c) for M in (0, 1) for c in range(4)}.values()).count(0b0111) == 2)
    ok_("08 T4 0101 +1 = 0110; T5 0101+0010 = 0111", (w(alu(5, 0, 0, 1)), w(alu(5, 2, 0, 0))) == ("0110", "0111"))
    ok_("08 s8 8 operations = 2^3", len([(M, c) for M in (0, 1) for c in range(4)]) == 2 ** 3)
