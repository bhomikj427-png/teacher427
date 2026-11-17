"""Unit 4 checks (files 15-16, S4 2026-11-17): detectors simulated, reductions recomputed. Imported by verify.py."""
from itertools import combinations, product

# ok, check_sop, detect, run_fsm, fn, run_sync are injected by verify.py's u4()


def refine(st, out, nxt, ins):
    blocks = {}
    for s in st:
        blocks.setdefault(out(s), []).append(s)
    P, hist = list(blocks.values()), []
    hist.append(P)
    while True:
        idx = {s: k for k, b in enumerate(P) for s in b}
        new = []
        for b in P:
            g = {}
            for s in b:
                g.setdefault(tuple(idx[nxt(s, i)] for i in ins), []).append(s)
            new.extend(g.values())
        if len(new) == len(P):
            return hist
        P = new
        hist.append(P)


def fmt(P):
    return "".join("(" + "".join(sorted(b)) + ")" for b in sorted(P, key=lambda b: sorted(b)[0]))


def mealy(T, ins=(0, 1)):
    return [fmt(P) for P in refine(sorted(T), lambda s: tuple(T[s][i][1] for i in ins), lambda s, i: T[s][i][0], ins)]


def moore(T, ins=(0, 1)):
    return [fmt(P) for P in refine(sorted(T), lambda s: T[s][1], lambda s, i: T[s][0][i], ins)]


def implication(T, ins=(0, 1)):
    st = sorted(T)
    pairs, cells, dead = list(combinations(st, 2)), {}, set()
    for a, b in pairs:
        imp = set()
        for i in ins:
            (na, oa), (nb, ob) = T[a][i], T[b][i]
            if oa is not None and ob is not None and oa != ob:
                dead.add((a, b))
            if na and nb and na != nb:
                imp.add(tuple(sorted((na, nb))))
        imp.discard((a, b))
        cells[(a, b)] = imp
    ch = True
    while ch:
        ch = False
        for p in pairs:
            if p not in dead and any(q in dead for q in cells[p]):
                dead.add(p)
                ch = True
    return cells, [p for p in pairs if p not in dead]


def maxcomp(st, cp):
    cp = set(cp)
    cl = [set(g) for r in range(len(st), 0, -1) for g in combinations(st, r) if all(p in cp for p in combinations(g, 2))]
    return sorted("".join(sorted(g)) for g in cl if not any(g < h for h in cl))


def closed(T, cover, ins=(0, 1)):
    for c in cover:
        for i in ins:
            ns = {T[s][i][0] for s in c if T[s][i][0]}
            if len(ns) > 1 and not any(ns <= set(d) for d in cover):
                return False
    return True


def wild(pat, xs, overlap=True):
    return [int(i + 1 >= len(pat) and all(p == "X" or int(p) == b for p, b in zip(pat, xs[i + 1 - len(pat):i + 1]))) for i in range(len(xs))]


def allseq(n=9):
    return [list(b) for k in range(1, n + 1) for b in product((0, 1), repeat=k)]


def mt(s):
    """'A:A/0,B/0 B:...' -> Mealy table; '-' = None."""
    T = {}
    for row in s.split():
        st, rest = row.split(":")
        T[st] = {}
        for i, e in enumerate(rest.split(",")):
            n, o = e.split("/")
            T[st][i] = (None if n == "-" else n, None if o == "-" else int(o))
    return T


def mo(s):
    """'A:A,B,0 ...' -> Moore {state: {x: next, 'z': out}} for run_fsm."""
    T = {}
    for row in s.split():
        st, rest = row.split(":")
        a, b, z = rest.split(",")
        T[st] = {0: a, 1: b, "z": int(z)}
    return T


def sim_eq(eqs, z, names, xs, start=0, nb=2):
    """D-flip-flop machine from printed equations (verify.fn); returns Z per bit (Mealy: Z with present state and x)."""
    fs, fz = [fn(e, names) for e in eqs], fn(z, names)
    s, out = start, []
    for x in xs:
        env = dict(zip(names, [int(c) for c in format(s, f"0{nb}b")] + [x]))
        out.append(fz(env))
        s = int("".join(str(f(env)) for f in fs), 2)
    return out


def u4():
    S = allseq()
    # ---- 15 detectors
    m1101 = mt("A:A/0,B/0 B:A/0,C/0 C:D/0,C/0 D:A/0,B/1")
    ok("15 s3 Mealy 1101 = overlapping detector on all strings <= 9", all(run_fsm(m1101, "A", x) == detect([1, 1, 0, 1], x) for x in S))
    ok("15 s2 1101101 -> Z 0001001", run_fsm(m1101, "A", [1, 1, 0, 1, 1, 0, 1]) == [0, 0, 0, 1, 0, 0, 1])
    ok("15 c3 1111101 -> 0000001", run_fsm(m1101, "A", [1, 1, 1, 1, 1, 0, 1]) == [0] * 6 + [1])
    m1101n = mt("A:A/0,B/0 B:A/0,C/0 C:D/0,C/0 D:A/0,A/1")
    ok("15 c4 non-overlap 1101 (D-1->A) = detector; 1101101 -> 0001000",
       all(run_fsm(m1101n, "A", x) == detect([1, 1, 0, 1], x, overlap=False) for x in S) and run_fsm(m1101n, "A", [1, 1, 0, 1, 1, 0, 1]) == [0, 0, 0, 1, 0, 0, 0])
    o1010 = mt("A:A/0,B/0 B:C/0,B/0 C:A/0,D/0 D:C/1,B/0")
    n1010 = mt("A:A/0,B/0 B:C/0,B/0 C:A/0,D/0 D:A/1,B/0")
    ok("15 s4 1010 overlapping (S3-0->S2) and non-overlapping (S3-0->S0) on all strings",
       all(run_fsm(o1010, "A", x) == detect([1, 0, 1, 0], x) and run_fsm(n1010, "A", x) == detect([1, 0, 1, 0], x, False) for x in S))
    ok("15 s4 101010 -> 000101 / 000100", run_fsm(o1010, "A", [1, 0, 1, 0, 1, 0]) == [0, 0, 0, 1, 0, 1] and run_fsm(n1010, "A", [1, 0, 1, 0, 1, 0]) == [0, 0, 0, 1, 0, 0])
    ok("15 s4 slip: 110 overlapping = non-overlapping", all(detect([1, 1, 0], x) == detect([1, 1, 0], x, False) for x in S))
    N3 = ["Y1", "Y2", "X"]
    check_sop("15 s6 count D1", "Y1Y2' + Y1'Y2X", [3, 4, 5], N3)
    check_sop("15 s6 count D2", "Y1'Y2'X + Y1Y2'X' + Y1Y2X", [1, 4, 7], N3)
    check_sop("15 s7 gray D1", "Y1Y2 + XY2", [3, 6, 7], N3)
    check_sop("15 s7 gray D2", "X", [1, 3, 5, 7], N3)
    check_sop("15 s7 gray Z", "XY1Y2'", [5], N3)
    check_sop("15 s8 T", "Y1Y2' + Y1'Y2X", [3, 4, 5], N3)
    check_sop("15 s8 J", "X", [1, 5], N3, [2, 3, 6, 7])
    check_sop("15 s8 K", "X'", [2, 6], N3, [0, 1, 4, 5])
    ok("15 s6-8 gate-input cost 7+12+3=22, 6+0+3=9, 7+0+3=10", (5 + 2) + (9 + 3) + 3 == 22 and (4 + 2) + 3 == 9 and 7 + 3 == 10)
    for lab, eq, zz in (("count", ["Y1Y2' + Y1'Y2X", "Y1'Y2'X + Y1Y2'X' + Y1Y2X"], "Y1Y2X"), ("gray", ["Y1Y2 + XY2", "X"], "XY1Y2'")):
        ok(f"15 s6/7 {lab} D circuit = 1101 detector on all strings", all(sim_eq(eq, zz, N3, x) == detect([1, 1, 0, 1], x) for x in S))
    ok("15 c7 gray 00 -1-> 01 -1-> 11 -0-> 10, Z on 4th bit", sim_eq(["Y1Y2 + XY2", "X"], "XY1Y2'", N3, [1, 1, 0, 1]) == [0, 0, 0, 1])
    N0 = ["Y1", "Y0", "X"]
    check_sop("15 s10 Mealy111 D1", "XY0", [3, 7], N0, [4, 5])
    check_sop("15 s10 Mealy111 D0", "X", [1, 3, 7], N0, [4, 5])
    check_sop("15 s10 Mealy111 Z", "XY1", [7], N0, [4, 5])
    check_sop("15 s10 Moore111 D1", "XY0 + XY1", [3, 7, 5], N0)
    check_sop("15 s10 Moore111 D0", "XY1'", [1, 3], N0)
    ok("15 s10 Mealy 111 circuit = detector", all(sim_eq(["XY0", "X"], "XY1", N0, x) == detect([1, 1, 1], x) for x in S))
    N4 = ["Y2", "Y1", "Y0", "X"]
    # Moore 1101: A000 B001 C010 D011 E100; next per (state, x)
    nx = {0: (0, 1), 1: (0, 2), 2: (3, 2), 3: (0, 4), 4: (0, 2)}
    dc = [m for m in range(16) if m >> 1 >= 5]
    for b, e in ((2, "Y1Y0X"), (1, "Y2X + Y1Y0' + Y1'Y0X"), (0, "Y1Y0'X' + Y2'Y1'Y0'X")):
        check_sop(f"15 s11 Moore1101 D{b}", e, [s * 2 + x for s in nx for x in (0, 1) if nx[s][x] >> b & 1], N4, dc)
    M = mo("A:A,B,0 B:A,C,0 C:D,C,0 D:A,E,0 E:A,C,1")
    ok("15 s11 Moore 1101 = detector (output of the state entered)", all(run_fsm(M, "A", x, mealy=False) == detect([1, 1, 0, 1], x) for x in S))
    ok("15 s11 / 16 Moore 1101 already minimal (5 blocks)", moore({k: ({0: v[0], 1: v[1]}, v["z"]) for k, v in M.items()})[-1] == "(A)(B)(C)(D)(E)")
    tabs = {
        "1011 Moore": (mo("S0:S0,S1,0 S1:S2,S1,0 S2:S0,S3,0 S3:S2,S4,0 S4:S2,S1,1"), "1011", False),
        "11011 Moore": (mo("S0:S0,S1,0 S1:S0,S2,0 S2:S3,S2,0 S3:S0,S4,0 S4:S0,S5,0 S5:S3,S2,1"), "11011", False),
        "10101 Mealy": (mt("S0:S0/0,S1/0 S1:S2/0,S1/0 S2:S0/0,S3/0 S3:S4/0,S1/0 S4:S0/0,S3/1"), "10101", True),
        "10101 Moore": (mo("S0:S0,S1,0 S1:S2,S1,0 S2:S0,S3,0 S3:S4,S1,0 S4:S0,S5,0 S5:S4,S1,1"), "10101", False),
        "1X1 Mealy": (mt("S0:S0/0,S1/0 S1:S2/0,S3/0 S2:S0/0,S1/1 S3:S2/0,S3/1"), "1X1", True),
        "101 Mealy": (mt("S0:S0/0,S1/0 S1:S2/0,S1/0 S2:S0/0,S1/1"), "101", True),
    }
    for k, (T, p, me) in tabs.items():
        ok(f"15 s12/st {k} table = overlapping detector on all strings <= 9", all(run_fsm(T, "S0", x, mealy=me) == wild(p, x) for x in S))
    # 1XX1 Mealy: state = last three bits
    T = {f"{s:03b}": {x: (f"{(s * 2 + x) & 7:03b}", int(s >> 2 & 1 and x)) for x in (0, 1)} for s in range(8)}
    ok("15 st 1XX1 Mealy, 8 states = last 3 bits, minimal", all(run_fsm(T, "000", x) == wild("1XX1", x) for x in S) and len(mealy(T)[-1].split(")(")) == 8)
    ok("15 s12 1X1 Mealy 4 states minimal", len(mealy(tabs["1X1 Mealy"][0])[-1].split(")(")) == 4)
    # ---- 16
    R = mt("A:C/1,B/0 B:C/1,E/0 C:B/1,E/0 D:D/0,B/1 E:E/0,A/1")
    resp = {s: ["".join(map(str, run_fsm(R, s, list(map(int, w))))) for w in ("00", "01", "10", "11", "110", "111")] for s in "ABCDE"}
    ok("16 s1 response table (00,01,10,11,110,111)", resp == {"A": ["11", "10", "01", "00", "000", "001"], "B": ["11", "10", "00", "01", "011", "010"],
       "C": ["11", "10", "00", "01", "011", "010"], "D": ["00", "01", "11", "10", "100", "101"], "E": ["00", "01", "11", "10", "101", "100"]}, resp)
    ok("16 s4 partition P1..P3 (ABC)(DE), (A)(BC)(DE), (A)(BC)(D)(E)", mealy(R) == ["(ABC)(DE)", "(A)(BC)(DE)", "(A)(BC)(D)(E)"], mealy(R))
    c, sv = implication(R)
    ok("16 s5 implication cells AB:BE, AC:BC+BE, BC:none, DE:AB; survivor BC",
       c[("A", "B")] == {("B", "E")} and c[("A", "C")] == {("B", "C"), ("B", "E")} and c[("B", "C")] == set() and c[("D", "E")] == {("A", "B")} and sv == [("B", "C")])
    ok("16 s2 inspection B=D (3 tables)", all(mealy(mt(t))[-1] == "(A)(BD)(C)" for t in (
        "A:B/0,C/1 B:C/0,A/1 C:D/1,B/0 D:C/0,A/1", "A:B/0,C/1 B:B/0,A/1 C:D/1,B/0 D:D/0,A/1", "A:B/0,C/1 B:D/0,A/1 C:D/1,B/0 D:B/0,A/1")))
    M7 = {k: ({0: v[0], 1: v[1]}, int(v[2])) for k, v in zip("ABCDEFG", ["BC1", "DF1", "FE0", "BG1", "FC0", "ED0", "FG0"])}
    ok("16 s3 Moore partition (ABD)(CEFG) -> (ABD)(CEG)(F) -> (AD)(B)(CEG)(F)", moore(M7) == ["(ABD)(CEFG)", "(ABD)(CEG)(F)", "(AD)(B)(CEG)(F)"], moore(M7))
    T8 = mt("A:E/0,D/0 B:A/1,F/0 C:C/0,A/1 D:B/0,A/0 E:D/1,C/0 F:C/0,D/1 G:H/1,G/1 H:C/1,B/1")
    c8, sv8 = implication(T8)
    ok("16 c4/s6 8-state -> (AD)(BE)(CF)(G)(H); GH implies BG, CH", mealy(T8)[-1] == "(AD)(BE)(CF)(G)(H)" and sv8 == [("A", "D"), ("B", "E"), ("C", "F")]
       and c8[("G", "H")] == {("B", "G"), ("C", "H")})
    T12 = mt("A:A/0,B/0 B:H/1,C/0 C:E/0,B/0 D:C/1,D/0 E:C/1,E/0 F:F/1,G/1 G:B/0,F/0 H:H/1,C/0")
    ok("16 st2 slide 12 -> (ACG)(BDEH)(F), (A)(BH)(C)(DE)(F)(G)", mealy(T12) == ["(ACG)(BDEH)(F)", "(A)(BH)(C)(DE)(F)(G)"], mealy(T12))
    I2 = ["00", "01", "11", "10"]
    T15 = {s: {k: (v[0], int(v[2])) for k, v in zip(I2, r.split())} for s, r in zip("ABCDEFGH", [
        "D/0 D/0 F/0 A/0", "C/1 D/0 E/1 F/0", "C/1 D/0 E/1 A/0", "D/0 B/0 A/0 F/0", "C/1 F/0 E/1 A/0", "D/0 D/0 A/0 F/0", "G/0 G/0 A/0 A/0", "B/1 D/0 E/1 A/0"])}
    ok("16 c6 slide 15/18 -> (AF)(BCH)(D)(E)(G); survivors AF, BC, BH, CH", mealy(T15, I2)[-1] == "(AF)(BCH)(D)(E)(G)"
       and implication(T15, I2)[1] == [("A", "F"), ("B", "C"), ("B", "H"), ("C", "H")])
    T24 = mt("A:A/-,-/- B:C/1,B/0 C:D/0,-/1 D:-/-,B/- E:A/0,C/1")
    c, sv = implication(T24)
    ok("16 s7 compatible pairs AB AC AD AE BD CD CE (DE dies via BC)", sv == [("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"), ("B", "D"), ("C", "D"), ("C", "E")])
    ok("16 s8 maximal compatibles (ABD)(ACD)(ACE); (ABD)(ACE) closed, (ABD)(CE) not",
       maxcomp("ABCDE", sv) == ["ABD", "ACD", "ACE"] and closed(T24, ["ABD", "ACE"]) and not closed(T24, ["ABD", "CE"]))
    T26 = mt("A:D/-,A/- B:E/0,A/- C:D/0,B/- D:C/-,C/- E:C/1,B/-")
    ok("16 c8 slide 26 maxcomp (ABC)(ACD)(ADE); (ABC)(DE) closed", maxcomp("ABCDE", implication(T26)[1]) == ["ABC", "ACD", "ADE"] and closed(T26, ["ABC", "DE"]))
    T25 = mt("A:B/1,D/0 B:-/-,B/0 C:E/0,D/- D:B/1,A/0 E:-/-,C/1 F:-/0,E/1")
    ok("16 st4 slide 25 cover (ABD)(BC)(E)(F) compatible and closed", closed(T25, ["ABD", "BC", "E", "F"])
       and all(p in implication(T25)[1] for p in [("A", "B"), ("A", "D"), ("B", "D"), ("B", "C")]))
    N2 = ["y1", "y0", "X"]
    ok("16 s10 ASM 1010: D0 = X, D1 = X'y0 + Xy1y0', Z = X'y1y0 = overlapping 1010 detector",
       all(sim_eq(["X'y0 + Xy1y0'", "X"], "X'y1y0", N2, x) == detect([1, 0, 1, 0], x) for x in S))
    ok("16 s10 slip: slide's D0 = Xy0', D1 = X'y0'... fails (101010)", sim_eq(["X'y0y1' + Xy1y0'", "Xy0'"], "X'y1y0", N2, [1, 0, 1, 0, 1, 0]) != [0, 0, 0, 1, 0, 1])
    ok("16 s11 counter E=1: 0,1,2,3,0; E=0 -> 00", run_sync("D", [{"D": "E"}, {"D": "E(y1⊕y0)"}, {"D": "Ey0'"}], 4, 4, ["E", "y1", "y0"]) == [4, 5, 6, 7, 4]
       and all(run_sync("D", [{"D": "E"}, {"D": "E(y1⊕y0)"}, {"D": "Ey0'"}], s, 1, ["E", "y1", "y0"])[1] == 0 for s in range(4)))
    ok("16 s11 MOD-6 hold: D0 = X xor y0 matches next bit 0 for states 0-5", all(((s + x) % 6 & 1) == (x ^ (s & 1)) for s in range(6) for x in (0, 1)))
    check_sop("16 s12 carry D", "AB + Ay + By", [3, 5, 6, 7], ["A", "B", "y"])
    ok("16 s12 sum Z = A xor B xor y = m(1,2,4,7)", [m for m in range(8) if bin(m).count("1") % 2] == [1, 2, 4, 7])

    def sadd(a, b, n=4):
        y, s, st = 0, [], []
        for k in range(n):
            ai, bi = a >> k & 1, b >> k & 1
            s.append(ai ^ bi ^ y)
            y = (ai & bi) | (ai & y) | (bi & y)
            st.append(y)
        return sum(v << k for k, v in enumerate(s)), st
    ok("16 s12 0110+0111 -> 1101, states after clocks G,H,H,G", sadd(6, 7) == (13, [0, 1, 1, 0]))
    ok("16 c12 0101+0011 -> 1000, H,H,H,G", sadd(5, 3) == (8, [1, 1, 1, 0]))
    ok("16 st7 1011+0110 -> 0001, ends in H", sadd(11, 6) == (1, [0, 1, 1, 1]))
