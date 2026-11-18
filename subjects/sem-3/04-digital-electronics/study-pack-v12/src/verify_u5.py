"""Files 18 (logic families) and 19 (memories, PLDs), S8.

Called from verify.py (unit u5), which injects ok(), check_sop(), same() and minterms().
Device numbers are the ones the pack prints (TI SN7400, SN74HC00 data sheets; KB 05 S8 block).
"""
from itertools import combinations, product

NAMES3 = "ABC"
NAMES4 = "ABCD"


def close(a, b, tol=1e-9):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def cross(ts, vs, level):
    """Time a piecewise-linear waveform first crosses `level` (either direction)."""
    for (t0, v0), (t1, v1) in zip(zip(ts, vs), zip(ts[1:], vs[1:])):
        if v0 != v1 and min(v0, v1) <= level <= max(v0, v1):
            return t0 + (level - v0) * (t1 - t0) / (v1 - v0)


# ---------------------------------------------------------------- 18
def f18():
    # step 1: 50 % crossings
    tphl, tplh = 17 - 10, 51 - 40
    ok("18 st1 t_PHL = 17 - 10 = 7 ns, t_PLH = 51 - 40 = 11 ns, gap 4, t_pd = 11", (tphl, tplh, tplh - tphl, max(tphl, tplh)) == (7, 11, 4, 11))
    ok("18 c1 t_PLH 8 - 3 = 5 ns; t_pd = max(8, 12) = 12", (8 - 3, max(8, 12)) == (5, 12))
    # step 2: the figure's pulse (0 V at 10 ns, 5 V at 15 ns, 5 V at 40 ns, 0 V at 47.5 ns)
    r = ([0, 10, 15], [0, 0, 5])
    f = ([40, 47.5, 55], [5, 0, 0])
    pts = (cross(*r, 0.5), cross(*r, 4.5), cross(*f, 4.5), cross(*f, 0.5))
    ok(f"18 st2 crossings {pts} = 10.5, 14.5, 40.75, 46.75 ns", all(close(a, b) for a, b in zip(pts, (10.5, 14.5, 40.75, 46.75))))
    ok("18 st2 t_r = 4 ns, t_f = 6 ns", close(pts[1] - pts[0], 4) and close(pts[3] - pts[2], 6))
    ok("18 c2 0.3/2.7 V = 10/90 % of 3 V; t_r = 3 ns", close(0.1 * 3, 0.3) and close(0.9 * 3, 2.7) and 5 - 2 == 3)
    # step 3: power
    iavg = (4 + 12) / 2
    ok("18 st3 avg I_CC 8 mA, package 40 mW, gate 10 mW", (iavg, 5 * iavg, 5 * iavg / 4) == (8, 40, 10))
    pdyn = 20e-12 * 5 ** 2 * 1e6
    ok(f"18 st3 C V^2 f = 20 pF x 25 x 1 MHz = {pdyn * 1e3:.3f} mW", close(pdyn, 0.5e-3))
    ok("18 c3 20 pF x 25 x 10 MHz = 5 mW; 2 x (1/2)^2 = 1/2", close(20e-12 * 25 * 1e7, 5e-3) and close(2 * 0.5 ** 2, 0.5))
    # step 4: noise margins (guaranteed SN7400 levels)
    nmh, nml = 2.4 - 2.0, 0.8 - 0.4
    ok("18 st4 NM_H = NM_L = 0.4 V", close(nmh, 0.4) and close(nml, 0.4))
    ok("18 st4 0.4 + 0.5 = 0.9 V > V_IL(max) 0.8 V", close(0.4 + 0.5, 0.9) and 0.9 > 0.8)
    h, l = 4.4 - 3.15, 1.35 - 0.1
    ok(f"18 c4 74HC00 at 4.5 V: NM_H {h:.2f}, NM_L {l:.2f}, {100 * h / 4.5:.1f} % -> 28 %", close(h, 1.25) and close(l, 1.25) and round(100 * h / 4.5) == 28)
    # step 5: PDP
    p1, p2 = 11e-9 * 10e-3, 9e-9 * 0.5e-3
    ok(f"18 st5 PDP 7400 {p1 * 1e12:.0f} pJ, 74HC00 {p2 * 1e12:.1f} pJ, ratio {p1 / p2:.1f} ~ 24", close(p1, 110e-12) and close(p2, 4.5e-12) and round(p1 / p2) == 24)
    ok("18 c5 5 ns x 2 mW = 10 pJ; (1/2) x 4 = 2", close(5e-9 * 2e-3, 10e-12) and 0.5 * 4 == 2)
    # step 6: fan-out
    fo = lambda iol, iil, ioh, iih: min(iol / iil, ioh / iih)
    ok("18 st6 fan-out min(16/1.6, 0.4/0.04) = 10", close(16 / 1.6, 10) and close(0.4 / 0.04, 10) and round(fo(16, 1.6, 0.4, 0.04)) == 10)
    ok("18 c6 min(8/0.4, 0.4/0.02) = 20", close(8 / 0.4, 20) and close(0.4 / 0.02, 20))
    # steps 7-8: switch-level CMOS. pMOS on when gate 0, nMOS on when gate 1.
    def cmos(pull_up_on, pull_down_on):
        assert pull_up_on != pull_down_on, "both or neither network conducts"
        return 1 if pull_up_on else 0
    inv_ok = all(cmos(a == 0, a == 1) == 1 - a for a in (0, 1))
    nand_ok = all(cmos((a == 0) or (b == 0), (a == 1) and (b == 1)) == 1 - (a & b) for a, b in product((0, 1), repeat=2))
    nor_ok = all(cmos((a == 0) and (b == 0), (a == 1) or (b == 1)) == 1 - (a | b) for a, b in product((0, 1), repeat=2))
    ok("18 st7-8 inverter, NAND (n series / p parallel), NOR (dual): exactly one network on, right outputs", inv_ok and nand_ok and nor_ok)
    ok("18 st8 NAND A=1,B=0 -> 1; c8 NOR A=0,B=0 -> 1; 3-input NOR 6 transistors", 1 - (1 & 0) == 1 and 1 - (0 | 0) == 1 and 2 * 3 == 6)
    # step 9: TTL multi-emitter: output transistor on only if no emitter LOW (open = no path = HIGH)
    def ttl(*ins):  # ins: 0, 1 or None (open)
        stolen = any(x == 0 for x in ins)
        return 1 if stolen else 0
    ok("18 st9 TTL NAND model gives (AB)'; open input acts HIGH", all(ttl(a, b) == 1 - (a & b) for a, b in product((0, 1), repeat=2)) and ttl(None, 1) == ttl(1, 1) == 0)
    ok("18 c10 wired-AND 1.0.1 = 0", (1 & 0 & 1) == 0)
    ok("18 c12 Cambridge: 7/0.8 = 8.75 ~ 9 x faster; 160/7 = 22.9 ~ 23 x energy; 0.8 ns x 200 mW = 160 pJ", round(7 / 0.8) == 9 and round(160 / 7) == 23 and close(0.8e-9 * 200e-3, 160e-12) and close(3.4e-9 * 5e-3, 17e-12) and close(7e-9 * 1e-3, 7e-12))
    ok("18 st13 10 mW x 10^6 = 10 kW; c13 20 x 10 pF = 200 pF", close(10e-3 * 1e6, 1e4) and 20 * 10 == 200)
    # step 14: interfacing
    ok("18 st14 TTL->HC fails: 2.4 < 3.15; HC->TTL: 3.98 > 2.0, 0.26 < 0.8; 4/1.6 = 2.5 -> 2 inputs", 2.4 < 3.15 and 3.98 > 2.0 and 0.26 < 0.8 and close(4 / 1.6, 2.5) and int(4 / 1.6) == 2)
    ok("18 c14 five TTL inputs 5 x 1.6 = 8 mA > 4 mA", close(5 * 1.6, 8) and 8 > 4)
    # self-test
    ok("18 self 1: 4.9-3.5 = 1.4, 1.5-0.1 = 1.4", close(4.9 - 3.5, 1.4) and close(1.5 - 0.1, 1.4))
    ok("18 self 2: min(40, 20) = 20", close(fo(4, 0.1, 0.4, 0.02), 20))
    ok("18 self 3: t_pd 10 ns, PDP 20 pJ", max(6, 10) == 10 and close(10e-9 * 2e-3, 20e-12))
    ok("18 self 4: 50 pF x 25 x 2 MHz = 2.5 mW", close(50e-12 * 25 * 2e6, 2.5e-3))
    ok("18 self 5: NOR(0, 1) = 0", 1 - (0 | 1) == 0)


# ---------------------------------------------------------------- 19 helpers
def lits(names):
    """Every product term over `names` (each variable: absent, true, complemented), as dicts."""
    out = []
    for code in product((None, 1, 0), repeat=len(names)):
        out.append(tuple(code))
    return out


def tval(term, bits):
    return all(c is None or c == b for c, b in zip(term, bits))


def tstr(term, names):
    s = "".join(n + ("" if c else "'") for n, c in zip(names, term) if c is not None)
    return s or "1"


def onset(fun, n):
    return {m for m in range(2 ** n) if fun(m)}


def bits_of(m, n):
    return tuple((m >> (n - 1 - i)) & 1 for i in range(n))


def pla_min(funcs, n, kmax):
    """Smallest number of distinct product terms such that each output, in true or complement
    form, is the OR of the chosen terms that are its implicants. funcs: list of on-sets."""
    terms = lits("X" * n)
    cover = {}
    for t in terms:
        cover[t] = frozenset(m for m in range(2 ** n) if tval(t, bits_of(m, n)))
    full = frozenset(range(2 ** n))
    for k in range(1, kmax + 1):
        for chosen in combinations(terms, k):
            good = True
            for on in funcs:
                okf = False
                for tgt in (frozenset(on), full - frozenset(on)):
                    imps = [cover[t] for t in chosen if cover[t] <= tgt]
                    if imps and frozenset().union(*imps) == tgt:
                        okf = True
                        break
                if not okf:
                    good = False
                    break
            if good:
                return k, chosen
    return None, None


# ---------------------------------------------------------------- 19
def f19():
    # memory sizes
    ok("19 st1 1K x 8: 2^10 = 1024 -> 10 address, 8 data, 8192 bits", 2 ** 10 == 1024 and 1024 * 8 == 8192)
    ok("19 c1 16K x 4: 14 address lines, 65536 bits; 12 addr x 16 data = 4096 x 16 = 65536 bits = 8192 bytes",
       2 ** 14 == 16384 and 16384 * 4 == 65536 and 2 ** 12 * 16 == 65536 and 65536 // 8 == 8192)
    ok("19 st4 4K x 8 from 1K x 8: 4 chips, 12 lines, 2 decoder bits", 4096 // 1024 == 4 and 2 ** 12 == 4096 and 2 ** 2 == 4)
    ranges = [(c * 1024, c * 1024 + 1023) for c in range(4)]
    ok(f"19 st4 chip blocks {ranges}; hex 000-3FF, 400-7FF, 800-BFF, C00-FFF",
       [f"{a:03X}-{b:03X}" for a, b in ranges] == ["000-3FF", "400-7FF", "800-BFF", "C00-FFF"])
    ok("19 st4 1K x 16 from two 1K x 8 side by side", 16 // 8 == 2)
    ok("19 c4 64K x 8 from 16K x 4: 4 x 2 = 8 chips, 16 lines, A15 A14 decoded; 2K x 16 from 2K x 8: 2 chips",
       (65536 // 16384) * (8 // 4) == 8 and 2 ** 16 == 65536 and 16 // 8 == 2)
    ok("19 self 8K x 8: 13 lines; 32K x 8 / 8K x 8 = 4 chips, 15 lines (A14 A13 decoded)", 2 ** 13 == 8192 and 32768 // 8192 == 4 and 2 ** 15 == 32768)
    ok("19 self 4-bit x 4-bit: 8 address bits, 15 x 15 = 225 < 256 -> 256 x 8", 15 * 15 == 225 < 2 ** 8)
    ok("19 self PROM for 4 inputs, 2 outputs: 16 x 2; c7 4 inputs, 3 outputs: 16 x 3", 2 ** 4 == 16)

    # 8 x 4 ROM (deck 15 slides 20-21): X marks per output
    marks = {"F3": (2, 5, 7), "F2": (0, 7), "F1": (1, 4), "F0": (1, 5, 7)}
    word = lambda a: "".join("1" if a in marks[k] else "0" for k in ("F3", "F2", "F1", "F0"))
    ok(f"19 st6 words: 001 -> {word(1)}, 011 -> {word(3)}, 101 -> {word(5)}, 111 -> {word(7)}",
       (word(1), word(3), word(5), word(7)) == ("0011", "0000", "1001", "1101"))
    ok("19 st6 slide-21 slip: 0011 is the word at 001 only", [a for a in range(8) if word(a) == "0011"] == [1])
    for nm, expr in (("F3", "AC + A'BC'"), ("F2", "ABC + A'B'C'"), ("F1", "AB'C' + A'B'C"), ("F0", "AC + B'C")):
        ok(f"19 st6 {nm} = {expr} (A2 A1 A0 = A B C) on minterms {marks[nm]}", same(expr, set(marks[nm]), NAMES3))

    ok(f"19 c6 input 100 -> {word(4)}; A2 = D4..D7", word(4) == "0010" and [m for m in range(8) if m >> 2] == [4, 5, 6, 7])
    ok("19 c7 BCD to 7-seg PROM 16 x 7, 6 unused words; c10 PAL 3 + 2 = 5; c11 6 lines; trap 1K x 8 = 8192 bits = 2^13", 2 ** 4 - 10 == 6 and 3 + 2 == 5 and 2 ** 13 == 1024 * 8)
    # PROM EX 15.22 truth table
    f1 = [1, 1, 1, 0, 0, 1, 0, 1]
    f2 = [0, 1, 1, 0, 1, 0, 1, 0]
    ok("19 st7 EX 15.22: f1 = m(0,1,2,5,7), f2 = m(1,2,4,6)",
       [m for m in range(8) if f1[m]] == [0, 1, 2, 5, 7] and [m for m in range(8) if f2[m]] == [1, 2, 4, 6])

    # PAL EX 15.24
    F1 = "C' + A'B'"
    ok("19 st8 F3 = AD + BD + F1 = AD + BD + A'B' + C'", same("AD + BD + A'B' + C'", set(minterms("AD + BD + C' + A'B'", NAMES4)), NAMES4))
    f1on = set(minterms("C' + A'B'", "ABCD"))
    f4 = set(minterms("AB + CD", NAMES4)) | (set(range(16)) - f1on)
    ok("19 st8 F4 = AB + CD + F1' equals AB + CD + AC + BC; F1' = AC + BC",
       same("AB + CD + AC + BC", f4, NAMES4) and same("AC + BC", set(range(16)) - f1on, NAMES4))

    # PAL EX 15.25-27
    W, X, Y, Z = (2, 12, 13), (7, 8, 9, 10, 11, 12, 13, 14, 15), (0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 15), (1, 2, 8, 12, 13)
    check_sop("19 st9 w", "ABC' + A'B'CD'", W, NAMES4)
    check_sop("19 st9 x", "A + BCD", X, NAMES4)
    check_sop("19 st9 y", "A'B + CD + B'D'", Y, NAMES4)
    check_sop("19 st9 z (4 terms, too many for 3)", "ABC' + A'B'CD' + AC'D' + A'B'C'D", Z, NAMES4)
    ok("19 st9 z = w + AC'D' + A'B'C'D", set(W) | set(minterms("AC'D' + A'B'C'D", NAMES4)) == set(Z))

    # running example F1 = m(0,1,2,4), F2 = m(0,5,6,7)
    R1, R2 = (0, 1, 2, 4), (0, 5, 6, 7)
    check_sop("19 st9 F1 true", "A'B' + A'C' + B'C'", R1, NAMES3)
    check_sop("19 st9 F2 true", "AB + AC + A'B'C'", R2, NAMES3)
    check_sop("19 st11 F1' (0s of F1)", "AB + AC + BC", [m for m in range(8) if m not in R1], NAMES3)
    ok("19 st11 true forms share nothing: 6 distinct terms", len({"A'B'", "A'C'", "B'C'"} | {"AB", "AC", "A'B'C'"}) == 6)
    k, ch = pla_min([set(R1), set(R2)], 3, 4)
    ok(f"19 st11 PLA minimum {k} terms ({', '.join(tstr(t, NAMES3) for t in ch)})", k == 4)
    ok("19 st11 F1 = (AB + AC + BC)' by XOR with 1", all(((m in R1) ^ 0) == ((m in minterms("AB + AC + BC", NAMES3)) ^ 1) for m in range(8)))

    # EX 15.36: F1 = AB' + AC + A'BC', F2 = (AC + BC)': 4 product lines, AC shared
    ok("19 c10 EX 15.36 product lines {AB', AC, BC, A'BC'} = 4", len({"AB'", "AC", "A'BC'"} | {"AC", "BC"}) == 4)
    ok("19 c10 x xor 1 = x', x xor 0 = x", all((x ^ 1) == 1 - x and (x ^ 0) == x for x in (0, 1)))

    # EX 15.37
    E1, E2, E3 = (1, 2, 4, 6), (0, 1, 6, 7), (1, 2, 3, 5, 7)
    check_sop("19 st12 F1", "A'B'C + BC' + AC'", E1, NAMES3)
    check_sop("19 st12 F2", "A'B' + AB", E2, NAMES3)
    check_sop("19 st12 F3", "C + A'B", E3, NAMES3)
    check_sop("19 st12 F2' (0s of F2)", "A'B + AB'", [m for m in range(8) if m not in E2], NAMES3)
    ok("19 st12 PAL terms 3 + 2 + 2 = 7, each <= 3", 3 + 2 + 2 == 7)
    k, ch = pla_min([set(E1), set(E2), set(E3)], 3, 6)
    ok(f"19 st12 PLA minimum {k} terms ({', '.join(tstr(t, NAMES3) for t in ch)})", k == 5)
    ok("19 st12 minimal forms alone: 7 distinct terms (A'B'C, BC', AC', A'B', AB, C, A'B)",
       len({"A'B'C", "BC'", "AC'"} | {"A'B'", "AB"} | {"C", "A'B"}) == 7)
    ok("19 st12 the pack's 5-term PLA: F2 = AB + A'B'C + A'B'C' (true), F3' = A'B'C' + AC' (complemented)",
       same("AB + A'B'C + A'B'C'", set(E2), NAMES3)
       and same("A'B'C' + AC'", {m for m in range(8) if m not in E3}, NAMES3)
       and len({"A'B'C", "BC'", "AC'"} | {"AB", "A'B'C", "A'B'C'"} | {"A'B'C'", "AC'"}) == 5)
    ok("19 st12 PROM 8 x 3", 2 ** 3 == 8)

    # self-test 4
    check_sop("19 self F = m(1,3,5,7)", "C", (1, 3, 5, 7), NAMES3)
    check_sop("19 self G = m(3,7)", "BC", (3, 7), NAMES3)


def u5():
    f18()
    f19()
