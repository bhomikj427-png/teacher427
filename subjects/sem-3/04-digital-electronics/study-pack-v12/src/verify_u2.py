"""Unit 2 checks for files 05-06 (MUX/DEMUX, decoder/encoder), S5 2026-11-17. Imported by verify.py.

Every MUX realisation is evaluated row by row against the function's minterm list; every decoder
circuit is built from minterm outputs and compared; encoders are compared with "index of the
(highest) active input". The data lists below are the ones the pack prints.
"""
from itertools import product

# ok, fn are injected by verify.py's u2()


def val(expr, names, env):
    """Evaluate a data-input label: '0', '1', or an expression over names."""
    if expr in ("0", "1"):
        return int(expr)
    return int(bool(fn(expr, names)(env)))


def rows(names):
    for bits in product((0, 1), repeat=len(names)):
        yield int("".join(map(str, bits)), 2), dict(zip(names, bits))


def mux_out(data, sel, names, env):
    """data[i] is selected when the select bits (first = MSB) spell i."""
    i = int("".join(str(env[s]) for s in sel), 2)
    return val(data[i], names, env)


def check_mux(label, ones, names, sel, data):
    bad = [m for m, e in rows(names) if mux_out(data, sel, names, e) != (m in ones)]
    ok(f"{label}: MUX selects {''.join(sel)}, data {data} gives Σm{tuple(ones)}", not bad, bad)


def residues(ones, names, sel):
    """Shannon residues: for each select code, the function of the remaining variables (as minterm set)."""
    rest = [n for n in names if n not in sel]
    out = []
    for code in range(2 ** len(sel)):
        sb = dict(zip(sel, map(int, format(code, f"0{len(sel)}b"))))
        out.append([int("".join(map(str, rb)), 2) for rb in product((0, 1), repeat=len(rest))
                    if int("".join(str({**sb, **dict(zip(rest, rb))}[n]) for n in names), 2) in ones])
    return out


def u2():
    # ---------------- 05 MUX/DEMUX
    N3, N4 = ["A", "B", "C"], ["A", "B", "C", "D"]
    # step 1: 2:1 MUX Z = S'I0 + SI1 (slide 5/7) against the 8-row table of slide 6 (S, D1, D0)
    t = [(s, d1, d0, (d0 if s == 0 else d1)) for s, d1, d0 in product((0, 1), repeat=3)]
    ok("05 s1: O = S'D0 + SD1 matches slide 6 table", all(((1 - s) & d0 | s & d1) == o for s, d1, d0, o in t))
    ok("05 s1: slide-6 table has O = 1 on rows 1, 3, 6, 7", [i for i, r in enumerate(t) if r[3]] == [1, 3, 6, 7])
    # slide 7's K-map (1s at m2, m3, m5, m7 by its own D0 rows / SD1 cols) vs the table
    slide7 = {2, 3, 5, 7}
    ok("05 s1: slide 7 K-map differs from the table (slip)", slide7 != {1, 3, 6, 7})
    # Check 1: I0=0,I1=1 -> S ; I0=1,I1=0 -> S'
    ok("05 c1: 2:1 MUX with 0,1 gives S; with 1,0 gives S'",
       all(mux_out(["0", "1"], ["S"], ["S"], {"S": s}) == s and mux_out(["1", "0"], ["S"], ["S"], {"S": s}) == 1 - s for s in (0, 1)))
    # step 2: 4:1 has 2 selects; 16:1 -> 4, 32:1 -> 5
    ok("05 c2: selects for 4:1, 16:1, 32:1 = 2, 4, 5", [n.bit_length() - 1 for n in (4, 16, 32)] == [2, 4, 5])
    # step 3: EX 4.15 F = Σm(2,3,5,6,7) on 8:1 -> data = truth column
    check_mux("05 s3 EX4.15", [2, 3, 5, 6, 7], N3, N3, ["0", "0", "1", "1", "0", "1", "1", "1"])
    # EX 4.13 / 4.24 (reverse): data 0,0,1,0,0,1,1,1 -> Σm(2,5,6,7) = AC + BC'
    check_mux("05 c3 EX4.24", [2, 5, 6, 7], N3, N3, ["0", "0", "1", "0", "0", "1", "1", "1"])
    ok("05 c3: AC + BC' = Σm(2,5,6,7)", [m for m, e in rows(N3) if fn("AC + BC'", N3)(e)] == [2, 5, 6, 7])
    # EX 4.14 half adder on two 4:1 (A, B selects)
    check_mux("05 c3 EX4.14 sum", [1, 2], ["A", "B"], ["A", "B"], ["0", "1", "1", "0"])
    check_mux("05 c3 EX4.14 carry", [3], ["A", "B"], ["A", "B"], ["0", "0", "0", "1"])
    # step 4: EX 4.16 F(x,y,z) = Σm(1,2,6,7) on 4:1, selects x y -> z, z', 0, 1
    check_mux("05 s4 EX4.16", [1, 2, 6, 7], ["x", "y", "z"], ["x", "y"], ["z", "z'", "0", "1"])
    # Check 4: EX 4.17 F = Σm(2,5,6,7) on 4:1, selects A B -> 0, C', C, 1
    check_mux("05 c4 EX4.17", [2, 5, 6, 7], N3, ["A", "B"], ["0", "C'", "C", "1"])
    # step 5 (running example): MTE Q5 F(P,Q,R,S) = Σm(0,1,3,4,8,9,10,11,13,15), 8:1 selects PQR
    NP = ["P", "Q", "R", "S"]
    MTE5 = [0, 1, 3, 4, 8, 9, 10, 11, 13, 15]
    D5 = ["1", "S", "S'", "0", "1", "1", "S", "S"]
    check_mux("05 s5 MTE Q5", MTE5, NP, ["P", "Q", "R"], D5)
    ok("05 s5: MTE Q5 residues (pairs) = [both, S, S', none, both, both, S, S]",
       residues(MTE5, NP, ["P", "Q", "R"]) == [[0, 1], [1], [0], [], [0, 1], [0, 1], [1], [1]])
    # Check 5: PS1 Q6 F(P,Q,R,S) = Σm(0,2,5,9,11,12,14,15)
    check_mux("05 c5 PS1 Q6", [0, 2, 5, 9, 11, 12, 14, 15], NP, ["P", "Q", "R"], ["S'", "S'", "S", "0", "S", "S", "S'", "1"])
    # EX 4.18 F(A,B,C,D) = Σm(1,3,4,11,12-15) on 8:1 -> D, D, D', 0, 0, D, 1, 1
    E18 = [1, 3, 4, 11, 12, 13, 14, 15]
    check_mux("05 s5 EX4.18", E18, N4, N3, ["D", "D", "D'", "0", "0", "D", "1", "1"])
    # step 6: EX 4.19 same function on ONE 4:1 (selects A B) -> D, C'D', CD, 1
    check_mux("05 s6 EX4.19", E18, N4, ["A", "B"], ["D", "C'D'", "CD", "1"])
    # Check 6: MTE Q5 on one 4:1 (selects P Q) -> R' + S, R'S', 1, S
    check_mux("05 c6 MTE Q5 on 4:1", MTE5, NP, ["P", "Q"], ["R' + S", "R'S'", "1", "S"])
    # step 7: trees. 4:1 from three 2:1; 8:1 from seven 2:1; 8:1 from two 4:1 + one 2:1
    def tree21(I, s):  # s = [S2, S1, S0] bits (MSB first); first level uses S0
        lvl = list(I)
        for b in reversed(s):
            lvl = [lvl[2 * k + b] for k in range(len(lvl) // 2)]
        return lvl[0]
    ok("05 s7: three 2:1 = 4:1 (S0 first level, S1 last)",
       all(tree21(list(range(4)), [s1, s0]) == 2 * s1 + s0 for s1, s0 in product((0, 1), repeat=2)))
    ok("05 s7: seven 2:1 = 8:1",
       all(tree21(list(range(8)), list(b)) == int("".join(map(str, b)), 2) for b in product((0, 1), repeat=3)))
    ok("05 s7: two 4:1 (S1 S0) + one 2:1 (S2) = 8:1",
       all([[0, 1, 2, 3], [4, 5, 6, 7]][s2][2 * s1 + s0] == 4 * s2 + 2 * s1 + s0 for s2, s1, s0 in product((0, 1), repeat=3)))
    ok("05 c7: 2:1 count for 16:1 = 15; 4:1 count for 16:1 = 5", (8 + 4 + 2 + 1, 4 + 1) == (15, 5))
    # step 8: PS1 Q5 only 4:1, D as data: F(A,B,C,D) = Σm(0,2,7,8,9,11,13,14,15)
    P5 = [0, 2, 7, 8, 9, 11, 13, 14, 15]
    D8 = ["D'", "D'", "0", "D", "1", "D", "D", "1"]
    check_mux("05 s8 PS1 Q5 (as one 8:1, ABC)", P5, N4, N3, D8)
    # built: MUX1 = D8[0:4], MUX2 = D8[4:8] on selects B C; MUX3 4:1 with S1 = 0, S0 = A, I0 = MUX1, I1 = MUX2, I2 = I3 = 0
    def three41(e):
        m1 = val(D8[2 * e["B"] + e["C"]], N4, e)
        m2 = val(D8[4 + 2 * e["B"] + e["C"]], N4, e)
        return [m1, m2, 0, 0][2 * 0 + e["A"]]
    ok("05 s8: three 4:1 MUXes realise PS1 Q5", all(three41(e) == (m in P5) for m, e in rows(N4)))
    # Check 8: MTE Q5 halves for the two first-level 4:1 MUXes
    ok("05 c8: MTE Q5 halves = (1,S,S',0) and (1,1,S,S)", (D5[:4], D5[4:]) == (["1", "S", "S'", "0"], ["1", "1", "S", "S"]))
    # step 9: 74LS151 exercise (slides 20-21): Y = Σm(1,3,5,6) on A2 A1 A0
    NA = ["A2", "A1", "A0"]
    check_mux("05 s9 slide 21", [1, 3, 5, 6], NA, NA, ["0", "1", "0", "1", "0", "1", "1", "0"])
    ok("05 s9: slide 21's SOP = Σm(1,3,5,6)",
       [m for m, e in rows(NA) if fn("A2'A1'A0 + A2'A1A0 + A2A1'A0 + A2A1A0'", NA)(e)] == [1, 3, 5, 6])
    # 8:1 from two 4:1 with active-low enables + OR (slide 29): G1' = S2, G2' = S2'; disabled output = 0
    def mux41_en(I, s1, s0, gbar):
        return 0 if gbar else I[2 * s1 + s0]
    ok("05 s9: two enabled 4:1 + OR = 8:1",
       all((mux41_en([0, 1, 2, 3], s1, s0, s2) or 0) + (mux41_en([4, 5, 6, 7], s1, s0, 1 - s2) or 0)
           - (0 if (s2 == 0 and s1 == 0 and s0 == 0) else 0) == 4 * s2 + 2 * s1 + s0 for s2, s1, s0 in product((0, 1), repeat=3)))
    # (the OR of two numbers is checked bitwise with one-hot data below)
    ok("05 s9: OR of the two 4:1 outputs selects exactly one data bit",
       all(sum([mux41_en([int(k == j) for j in range(4)], s1, s0, s2), mux41_en([int(k == j + 4) for j in range(4)], s1, s0, 1 - s2)]) == int(k == 4 * s2 + 2 * s1 + s0)
           for k in range(8) for s2, s1, s0 in product((0, 1), repeat=3)))
    # step 10: 1:4 DEMUX: Yi = D·mi (S1 S0)
    ok("05 s10: 1:4 DEMUX puts D on Y(2S1+S0) only",
       all([d * int(i == 2 * s1 + s0) for i in range(4)] == [d if i == 2 * s1 + s0 else 0 for i in range(4)]
           for d, s1, s0 in product((0, 1), repeat=3)))
    # Check 10: S1 S0 = 10, D = 1 -> Y2 = 1, others 0
    ok("05 c10: S1S0 = 10, D = 1 -> Y = (0,0,1,0)", [int(i == 2) for i in range(4)] == [0, 0, 1, 0])
    # Self-test: PS1 Q3 F(a,b,c,d) = Σm(0,1,3,5,7,9,15), 8:1 selects a b c
    check_mux("05 T1 PS1 Q3", [0, 1, 3, 5, 7, 9, 15], ["a", "b", "c", "d"], ["a", "b", "c"], ["1", "d", "d", "d", "d", "0", "0", "d"])
    # Self-test: F(A,B,C) = Σm(0,2,5,7) on 4:1 (A B selects) -> C', C', C, C ; = A'C' + AC
    check_mux("05 T2", [0, 2, 5, 7], N3, ["A", "B"], ["C'", "C'", "C", "C"])
    # Self-test: same function with C, A on the selects... (B as data): selects A C -> pairs over B
    check_mux("05 T3 (selects A C)", [0, 2, 5, 7], N3, ["A", "C"], ["1", "0", "0", "1"])
    # Self-test: full adder sum on 4:1 (x y selects) -> z, z', z', z ; carry -> 0, z, z, 1
    NF = ["x", "y", "z"]
    check_mux("05 T4 FA sum", [1, 2, 4, 7], NF, ["x", "y"], ["z", "z'", "z'", "z"])
    check_mux("05 T4 FA carry", [3, 5, 6, 7], NF, ["x", "y"], ["0", "z", "z", "1"])

    # ---------------- 06 decoder/encoder
    def dec(n, code, en=1):
        return [int(en and i == code) for i in range(2 ** n)]
    def or_of(outs, idx):
        return int(any(outs[i] for i in idx))
    # step 1-2: 2:4 and 3:8 decoder outputs are the minterms
    ok("06 s1: 2:4 outputs W,X,Y,Z = A'B', A'B, AB', AB",
       all(dec(2, 2 * a + b) == [int(fn(t, ["A", "B"])({"A": a, "B": b})) for t in ("A'B'", "A'B", "AB'", "AB")]
           for a, b in product((0, 1), repeat=2)))
    ok("06 s2: 3:8 output Di = mi (x MSB)",
       all(dec(3, m)[i] == int(fn(["x'y'z'", "x'y'z", "x'yz'", "x'yz", "xy'z'", "xy'z", "xyz'", "xyz"][i], NF)(e)) for m, e in rows(NF) for i in range(8)))
    # step 3: enable: high-level (slide 11) and active-low outputs with active-low enable (slide 13)
    ok("06 s3: En = 0 -> all outputs 0 (slide 11)", all(dec(2, c, en=0) == [0] * 4 for c in range(4)))
    sl13 = {(1, a, b): [1, 1, 1, 1] for a in (0, 1) for b in (0, 1)}
    sl13.update({(0, a, b): [0 if i == 2 * a + b else 1 for i in range(4)] for a in (0, 1) for b in (0, 1)})
    ok("06 s3: slide 13 = NAND(E', A^, B^) table",
       all(sl13[(e, a, b)] == [1 - int((1 - e) and i == 2 * a + b) for i in range(4)] for e, a, b in product((0, 1), repeat=3)))
    # step 4: 4:16 from two 3:8 (w MSB: top EN = w', bottom EN = w) and from five 2:4
    ok("06 s4: two 3:8 + w enable = 4:16",
       all(dec(3, m & 7, en=1 - (m >> 3)) + dec(3, m & 7, en=m >> 3) == dec(4, m) for m in range(16)))
    ok("06 s4: five 2:4 = 4:16 (first stage on w3 w2 drives enables)",
       all(sum((dec(2, m & 3, en=dec(2, m >> 2)[k]) for k in range(4)), []) == dec(4, m) for m in range(16)))
    ok("06 c4: 2:4 count for 4:16 = 5; 3:8 count for 5:32 = 4 (+ one 2:4)", (1 + 4, 32 // 8) == (5, 4))
    # step 5: decoder + OR. slide 18 F = Σm(0,2) with 2:4 (A MSB) = B'
    ok("06 s5: OR(0,2) of 2:4 = B'", all(or_of(dec(2, 2 * a + b), [0, 2]) == 1 - b for a, b in product((0, 1), repeat=2)))
    ok("06 s5: slide 20 F = OR(1,2,5,7) on 3:8 = Σm(1,2,5,7)",
       [m for m in range(8) if or_of(dec(3, m), [1, 2, 5, 7])] == [1, 2, 5, 7])
    # Check 5: slide 26 with two 2:4, Z on the enables: dec A (EN = Z') on X Y, dec B (EN = Z) on X Y
    def two24(x, y, z):
        a, b = dec(2, 2 * x + y, en=1 - z), dec(2, 2 * x + y, en=z)
        return int(a[1] or b[0] or b[2] or b[3])
    ok("06 c5: two 2:4 with Z enables: F = A1 + B0 + B2 + B3 = Σm(1,2,5,7)",
       [4 * x + 2 * y + z for x, y, z in product((0, 1), repeat=3) if two24(x, y, z)] == [1, 2, 5, 7])
    ok("06 c5: half adder from 2:4: S = OR(1,2), C = out 3",
       all((or_of(dec(2, 2 * a + b), [1, 2]), dec(2, 2 * a + b)[3]) == ((a + b) & 1, (a + b) >> 1) for a, b in product((0, 1), repeat=2)))
    # step 6: MTE Q6 full adder, x y z (z = carry in)
    ok("06 s6 MTE Q6: S = OR(1,2,4,7), C = OR(3,5,6,7) = full adder",
       all((or_of(dec(3, 4 * x + 2 * y + z), [1, 2, 4, 7]), or_of(dec(3, 4 * x + 2 * y + z), [3, 5, 6, 7])) == ((x + y + z) & 1, (x + y + z) >> 1)
           for x, y, z in product((0, 1), repeat=3)))
    ok("06 s6: full adder from two 2:4 (A2 on enables) uses D1,2,4,7 / D3,5,6,7",
       all((or_of(dec(2, m & 3, en=1 - (m >> 2)) + dec(2, m & 3, en=m >> 2), [1, 2, 4, 7]),
            or_of(dec(2, m & 3, en=1 - (m >> 2)) + dec(2, m & 3, en=m >> 2), [3, 5, 6, 7])) == (bin(m).count("1") & 1, int(bin(m).count("1") >= 2))
           for m in range(8)))
    # step 7: PS1 Q7 Y = ΠM(0,3,5,6,7) with NOR(D0,D3,D5,D6,D7) = Σm(1,2,4)
    ok("06 s7 PS1 Q7: NOR of 0,3,5,6,7 = Σm(1,2,4)", [m for m in range(8) if not or_of(dec(3, m), [0, 3, 5, 6, 7])] == [1, 2, 4])
    # slide 25: active-low outputs + AND: f1 = ΠM(0,3,5), f2 = ΠM(2,3,4)
    def lowdec(m):
        return [1 - v for v in dec(3, m)]
    ok("06 s7 slide 25: AND of active-low 0,3,5 = ΠM(0,3,5)", [m for m in range(8) if not all(lowdec(m)[i] for i in (0, 3, 5))] == [0, 3, 5])
    ok("06 s7 slide 25: AND of active-low 2,3,4 = ΠM(2,3,4)", [m for m in range(8) if not all(lowdec(m)[i] for i in (2, 3, 4))] == [2, 3, 4])
    # the four-way table: NAND of active-low ones-outputs = OR of active-high ones-outputs
    ok("06 s7: NAND(active-low 1,2,4) = OR(active-high 1,2,4)",
       all(int(not all(lowdec(m)[i] for i in (1, 2, 4))) == or_of(dec(3, m), [1, 2, 4]) for m in range(8)))
    # step 8: PS1 Q8 F(a,b,c,d) = Σm(0,1,2,5,6,8,9,15) from two 3:8 (a on enables) + OR
    P8 = [0, 1, 2, 5, 6, 8, 9, 15]
    ok("06 s8 PS1 Q8: OR of 4:16 outputs 0,1,2,5,6,8,9,15",
       [m for m in range(16) if or_of(dec(3, m & 7, en=1 - (m >> 3)) + dec(3, m & 7, en=m >> 3), P8)] == P8)
    ok("06 s8: F has 8 ones and 8 zeros (OR and NOR both need 8 inputs)", (len(P8), 16 - len(P8)) == (8, 8))
    # step 9: encoders
    ok("06 s9: 4:2 encoder y1 = w2 + w3, y0 = w1 + w3",
       all(((k >> 1) & 1, k & 1) == (int(k in (2, 3)), int(k in (1, 3))) for k in range(4)))
    def enc83(D):
        return (int(D[4] or D[5] or D[6] or D[7]), int(D[2] or D[3] or D[6] or D[7]), int(D[1] or D[3] or D[5] or D[7]))
    ok("06 s9: 8:3 encoder x,y,z = binary of the active input",
       all(enc83([int(i == k) for i in range(8)]) == tuple(int(c) for c in format(k, "03b")) for k in range(8)))
    ok("06 s9: D3 and D6 together -> xyz = 111 (7, wrong)", enc83([0, 0, 0, 1, 0, 0, 1, 0]) == (1, 1, 1))
    ok("06 s9: no input -> 000 (same as D0)", enc83([0] * 8) == enc83([1, 0, 0, 0, 0, 0, 0, 0]) == (0, 0, 0))
    # step 10: 4:2 priority encoder x = D2 + D3, y = D3 + D1D2', V = D0+D1+D2+D3
    good = True
    for D in product((0, 1), repeat=4):
        act = [i for i in range(4) if D[i]]
        x, y, V = int(D[2] or D[3]), int(D[3] or (D[1] and not D[2])), int(any(D))
        if act:
            good &= (2 * x + y == max(act)) and V == 1
        else:
            good &= V == 0
    ok("06 s10: priority encoder equations on all 16 inputs", good)
    # Check 10: D0 = D1 = D2 = 1, D3 = 0 -> xy = 10, V = 1
    ok("06 c10: D0..D3 = 1110 -> x y V = 1 0 1", (1, 0, 1) == (int(1 or 0), int(0 or (1 and not 1)), 1))
    # Self-test: 8:3 priority encoder equations
    g8 = True
    for D in product((0, 1), repeat=8):
        a = [i for i in range(8) if D[i]]
        y2 = D[4] | D[5] | D[6] | D[7]
        y1 = D[7] | D[6] | ((1 - D[5]) & (1 - D[4]) & (D[3] | D[2]))
        y0 = D[7] | ((1 - D[6]) & D[5]) | ((1 - D[6]) & (1 - D[4]) & D[3]) | ((1 - D[6]) & (1 - D[4]) & (1 - D[2]) & D[1])
        if a:
            g8 &= 4 * y2 + 2 * y1 + y0 == max(a)
    ok("06 T: 8:3 priority encoder equations on all 256 inputs", g8)
    # Self-test: F = Σm(0,2) from slide 18 written with A0 = Y, A1 = X: outputs 0, 2 -> X'Y' + XY' = Y'
    ok("06 T: 2:4 with A1 = X, A0 = Y, OR(0,2) = Y'", all(or_of(dec(2, 2 * X + Y), [0, 2]) == 1 - Y for X, Y in product((0, 1), repeat=2)))
