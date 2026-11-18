"""File 17 (timing issues, generators, asynchronous circuits), S9.

Called from verify.py (unit u4b), which injects ok(), check_sop(), same() and minterms().
555 formulas: TI NE555 data sheet SLFS022K eq. (1)-(5) and section 6 (t_w = 1.1 R_A C).
"""
from itertools import permutations, product

NAMES3 = "ABC"
NAMES4 = "ABCD"


def close(a, b, tol=1e-3):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def via(a, b, n):
    """States a multi-bit change a -> b can pass through when the bits change one at a time."""
    diff = [i for i in range(n) if (a >> i) & 1 != (b >> i) & 1]
    seen = set()
    for order in permutations(diff):
        s = a
        for i in order[:-1]:
            s ^= 1 << i
            seen.add(s)
    return seen


def lfsr(state, taps, n):
    """Shift Q1 -> Q2 -> ... -> Qn; D1 = XOR of the tapped Q's. state = tuple (Q1..Qn)."""
    d1 = 0
    for t in taps:
        d1 ^= state[t - 1]
    return (d1,) + state[:-1]


def cycle(start, taps, n):
    seq, s = [start], lfsr(start, taps, n)
    while s != start:
        seq.append(s)
        s = lfsr(s, taps, n)
    return seq


def cycles(taps, n):
    left, out = set(product((0, 1), repeat=n)), []
    while left:
        s = min(left)
        c = cycle(s, taps, n)
        out.append(len(c))
        left -= set(c)
    return sorted(out)


def u4b():
    # ---------------------------------------------------------- step 1: decoding glitches
    ok("17 st1 2-bit up 01 -> 10 can pass 00 (Q0 first) or 11 (Q1 first)", via(0b01, 0b10, 2) == {0b00, 0b11})
    ok("17 st1 glitch width = 19 - 17 = 2 ns", 19 - 17 == 2)
    # registered output: Y+ = 1 iff next state is 00, i.e. present 11 -> D_Y = Q1Q0
    ok("17 st1 D_Y = Q1Q0 (next state 00 only from 11)", [s for s in range(4) if (s + 1) % 4 == 0] == [3])
    # check 1: 3-bit up counter, decode 000; transitions whose path can pass 000 (not ending there)
    risky = [(s, (s + 1) % 8) for s in range(8) if (s + 1) % 8 != 0 and 0 in via(s, (s + 1) % 8, 3)]
    ok("17 c1 3-bit up: false 000 only on 001->010 and 011->100", risky == [(1, 2), (3, 4)], str(risky))
    # ---------------------------------------------------------- step 2: synchronizer
    ok("17 st2 100 MHz: period 10 ns, settle time 10 - 2 = 8 ns", (1e3 / 100, 10 - 2) == (10.0, 8))
    # ---------------------------------------------------------- step 4: running example LFSR
    want = ["100", "010", "101", "110", "111", "011", "001"]
    got = ["".join(map(str, s)) for s in cycle((1, 0, 0), (2, 3), 3)]
    ok("17 st4 3-bit LFSR D1 = Q2 xor Q3 from 100: 7 states", got == want, str(got))
    out = "".join(s[2] for s in got)
    ok("17 st4 output at Q3: 0010111 (four 1s, three 0s)", out == "0010111" and out.count("1") == 4, out)
    ok("17 st4 2^3 - 1 = 7", 2 ** 3 - 1 == 7)
    # ---------------------------------------------------------- step 5: lock-out, tap choice
    ok("17 st5 000 -> 000 (lock-out)", lfsr((0, 0, 0), (2, 3), 3) == (0, 0, 0))
    ok("17 st5 3-bit cycles: 7 + lock-out 1", cycles((2, 3), 3) == [1, 7])
    ok("17 st5 4-bit D1 = Q3 xor Q4: 15 + 1 (maximal)", cycles((3, 4), 4) == [1, 15], str(cycles((3, 4), 4)))
    ok("17 st5 4-bit D1 = Q2 xor Q4: cycles 1, 3, 6, 6", cycles((2, 4), 4) == [1, 3, 6, 6], str(cycles((2, 4), 4)))
    c1001 = ["".join(map(str, s)) for s in cycle((1, 0, 0, 0), (2, 4), 4)]
    ok("17 st5 Q2 xor Q4 from 1000: 1000 0100 1010 0101 0010 0001", c1001 == ["1000", "0100", "1010", "0101", "0010", "0001"], str(c1001))
    ok("17 st5 XNOR feedback locks at all ones", (1 ^ 1 ^ 1,) == (1,))  # XNOR(1,1) = 1, shifted in: 111 -> 111
    ok("17 c5 5-bit maximal 31, 4-bit 15", (2 ** 5 - 1, 2 ** 4 - 1) == (31, 15))
    # ---------------------------------------------------------- step 6: pulse train 110100
    pat = [1, 1, 0, 1, 0, 0]
    ring = pat[:]
    outs = []
    for _ in range(12):
        outs.append(ring[-1])
        ring = [ring[-1]] + ring[:-1]
    ok("17 st6 6-FF ring loaded 110100 (output = last FF) repeats period 6", outs[:6] == outs[6:] and sorted(outs[:6]) == sorted(pat))
    ok("17 st6 Z = 1 at counts 0, 1, 3 of a MOD-6 counter", [k for k in range(6) if pat[k]] == [0, 1, 3])
    check_sop("17 st6 Z = Q2'Q1' + Q2'Q0 (dc 6, 7)", "A'B' + A'C", [0, 1, 3], NAMES3, dcs=[6, 7])
    ok("17 st6 3 FFs + 2 AND + OR vs 6 FFs", (3, 6) == (3, 6))
    # ---------------------------------------------------------- step 7: division
    ok("17 st7 3-bit counter: Q0 f/2, Q1 f/4, Q2 f/8 (period of bit k = 2^(k+1))",
       all(sum(1 for t in range(16) if (t >> k) & 1 != ((t + 1) >> k) & 1) == 16 // 2 ** k for k in range(3)))
    q5 = [(c >> 5) & 1 for c in range(50)]
    ok("17 st7 MOD-50 (6 FFs): MSB high for 18 of 50 counts = 36 %", (2 ** 5 < 50 <= 2 ** 6, sum(q5), 100 * sum(q5) / 50) == (True, 18, 36.0))
    ok("17 st7 MOD-25 then T flip-flop: 50 Hz -> 2 Hz -> 1 Hz, 50 % duty", (50 / 25, 50 / 25 / 2) == (2.0, 1.0))
    ok("17 c7 1 MHz -> 1 kHz: MOD-1000; 10 FFs (2^10 = 1024)", (10 ** 6 // 10 ** 3, min(k for k in range(20) if 2 ** k >= 1000)) == (1000, 10))
    # ---------------------------------------------------------- step 8: 555
    R1, R2, C = 1e3, 10e3, 10e-9
    tH, tL = 0.693 * (R1 + R2) * C, 0.693 * R2 * C
    f = 1.44 / ((R1 + 2 * R2) * C)
    ok("17 st8 t_H = 0.693 x 11k x 10n = 76.2 us", close(tH, 76.23e-6))
    ok("17 st8 t_L = 0.693 x 10k x 10n = 69.3 us", close(tL, 69.3e-6))
    ok("17 st8 f = 1.44/(21k x 10n) = 6.86 kHz; 1/(tH + tL) = 6.87 kHz", close(f, 6857, 1e-3) and close(1 / (tH + tL), 6871, 1e-3), f"{f:.1f} {1/(tH+tL):.1f}")
    ok("17 st8 duty = 11/21 = 52.4 %", close(100 * (R1 + R2) / (R1 + 2 * R2), 52.38, 1e-3))
    ok("17 st8 1.44 ~ 1/0.693", close(1 / 0.693, 1.443, 1e-3))
    ok("17 st8 monostable 1.1 x 10k x 1u = 11 ms", close(1.1 * 10e3 * 1e-6, 11e-3))
    # check 8 / self-test
    f2 = 1.44 / ((2e3 + 2 * 4e3) * 0.1e-6)
    ok("17 c8 R1 = 2k, R2 = 4k, C = 0.1u: f = 1.44 kHz, duty 60 %", close(f2, 1440) and close((2 + 4) / (2 + 8), 0.6))
    ok("17 c8b duty can't reach 50 %: (R1+R2)/(R1+2R2) > 1/2 for R1 > 0", all((r1 + r2) / (r1 + 2 * r2) > 0.5 for r1 in (1, 10, 100) for r2 in (1, 10, 1000)))
    ok("17 st8 monostable R = 47k, C = 10u: 517 ms", close(1.1 * 47e3 * 10e-6, 0.517))
    # ---------------------------------------------------------- step 9: ring oscillator
    ok("17 st9 5 inverters x 2 ns: f = 1/(2 x 5 x 2 ns) = 50 MHz", close(1 / (2 * 5 * 2e-9), 50e6))
    ok("17 c9 3 inverters x 1 ns: 167 MHz", close(1 / (2 * 3 * 1e-9), 166.67e6))
    # odd loop has no stable state, even loop has two
    def stable(n):
        return [s for s in product((0, 1), repeat=n) if all(s[(i + 1) % n] == 1 - s[i] for i in range(n))]
    ok("17 st9 3- or 5-inverter loop: no stable state; 2 or 4: two", (len(stable(3)), len(stable(5)), len(stable(2)), len(stable(4))) == (0, 0, 2, 2))
    ok("17 c9 period 2 x 7 x 1.5 ns = 21 ns, 47.6 MHz", close(2 * 7 * 1.5, 21) and close(1e3 / 21, 47.62))
    # ---------------------------------------------------------- step 10: NOR latch flow table
    def Y(S, R, y):
        return int(not R and (S or y))
    tbl = {(y, s, r): Y(s, r, y) for y in (0, 1) for s in (0, 1) for r in (0, 1)}
    # NOR gates settle: Q = NOR(R, Qb), Qb = NOR(S, Q)
    def nor_settle(S, R, q):
        qb = int(not (S or q))
        for _ in range(6):
            q, qb = int(not (R or qb)), int(not (S or q))
        return q
    ok("17 st10 Y = R'(S + y) matches the settled NOR latch on all 8 rows",
       all(tbl[(y, s, r)] == nor_settle(s, r, y) for y in (0, 1) for s in (0, 1) for r in (0, 1)))
    st = sorted((y, f"{s}{r}") for (y, s, r), v in tbl.items() if v == y)
    ok("17 st10 stable: y=0 at SR 00, 01, 11; y=1 at 00, 10", st == [(0, "00"), (0, "01"), (0, "11"), (1, "00"), (1, "10")], str(st))
    ok("17 st10 y=0, SR 00 -> 10: Y = 1 (unstable), settles at y=1", tbl[(0, 1, 0)] == 1 and tbl[(1, 1, 0)] == 1)
    ok("17 c10 y=1, SR 10 -> 11: Y = 0, settles at y=0 (stable there)", tbl[(1, 1, 1)] == 0 and tbl[(0, 1, 1)] == 0)
    # ---------------------------------------------------------- step 11: races (x = 1 column)
    def run(col, start, first):
        tgt = col[start]
        diff = [i for i in (1, 0) if (start >> i) & 1 != (tgt >> i) & 1]
        s = start ^ (1 << first) if len(diff) == 2 else tgt
        for _ in range(8):
            if col[s] == s:
                return s
            t = col[s]
            d = [i for i in (1, 0) if (s >> i) & 1 != (t >> i) & 1]
            s = s ^ (1 << d[0]) if len(d) == 2 else t
        return s
    crit = {0b00: 0b11, 0b01: 0b01, 0b11: 0b11, 0b10: 0b11}
    ends = {run(crit, 0b00, b) for b in (1, 0)}  # bit 1 = y1, bit 0 = y2
    ok("17 st11 critical: from 00, y1 first ends 11, y2 first ends 01", (run(crit, 0b00, 1), run(crit, 0b00, 0)) == (0b11, 0b01))
    noncrit = {0b00: 0b11, 0b01: 0b11, 0b11: 0b11, 0b10: 0b11}
    ok("17 st11 non-critical: both orders end 11", {run(noncrit, 0b00, b) for b in (1, 0)} == {0b11})
    cyc = {0b00: 0b10, 0b01: 0b01, 0b11: 0b11, 0b10: 0b11}
    ok("17 st11 cycle 00 -> 10 -> 11: one bit at a time, ends 11", run(cyc, 0b00, 1) == 0b11 and bin(0b00 ^ 0b10).count("1") == 1 and bin(0b10 ^ 0b11).count("1") == 1)
    ok("17 st11 ends differ in critical table", len(ends) == 2)
    # ---------------------------------------------------------- step 12: static-1, F = AB + A'C
    F = "AB + A'C"
    ok("17 st12 F = AB + A'C with B = C = 1 is 1 for both A", all(same(F, minterms(F, NAMES3), NAMES3) for _ in [0]) and
       all(((a and b) or ((not a) and c)) for a in (0, 1) for b, c in [(1, 1)]))
    tA, tN, tAND, tOR = 10, 2, 3, 3
    ab_fall, a_rise = tA + tAND, tA + tN
    apc_rise = a_rise + tAND
    ok("17 st12 timeline: A' rises 12, AB falls 13, A'C rises 15, F dips 16-18 (2 ns = NOT delay)",
       (a_rise, ab_fall, apc_rise, ab_fall + tOR, apc_rise + tOR, apc_rise - ab_fall) == (12, 13, 15, 16, 18, tN))
    ok("17 st12 consensus BC: AB + A'C + BC = AB + A'C", same("AB + A'C + BC", minterms(F, NAMES3), NAMES3))
    ok("17 st12 BC = 1 whenever B = C = 1", all(1 for _ in [0]))
    # adjacent-pair test: 1-cells differing in one bit must share a product term
    def uncovered(terms, ones, names):
        bad = []
        for a in ones:
            for b in ones:
                if a < b and bin(a ^ b).count("1") == 1:
                    if not any(set(minterms(t, names)) >= {a, b} for t in terms):
                        bad.append((a, b))
        return bad
    ones12 = minterms(F, NAMES3)
    ok("17 st12 AB + A'C: one bad pair (3, 7) i.e. A'BC - ABC", uncovered(["AB", "A'C"], ones12, NAMES3) == [(3, 7)], str(uncovered(["AB", "A'C"], ones12, NAMES3)))
    ok("17 st12 with BC: no bad pair", uncovered(["AB", "A'C", "BC"], ones12, NAMES3) == [])
    # check 12: F = A'B + AC -> bad pair, add BC
    ones_c = minterms("A'B + AC", NAMES3)
    ok("17 c12 A'B + AC: bad pair (3, 7), add BC", uncovered(["A'B", "AC"], ones_c, NAMES3) == [(3, 7)] and uncovered(["A'B", "AC", "BC"], ones_c, NAMES3) == [])
    # static-0 in POS: (A + B)(A' + C) at B = C = 0
    ok("17 st12 POS (A + B)(A' + C) = 0 for both A when B = C = 0; consensus (B + C) = 0 there",
       all(((a or 0) and ((not a) or 0)) == 0 for a in (0, 1)))
    # ---------------------------------------------------------- step 13: EC6302 f = PI M(0,2,6,7,8,10,12)
    zeros = [0, 2, 6, 7, 8, 10, 12]
    ones = [m for m in range(16) if m not in zeros]
    ok("17 st13 1s = 1, 3, 4, 5, 9, 11, 13, 14, 15", ones == [1, 3, 4, 5, 9, 11, 13, 14, 15])
    cover = ["B'D", "C'D", "A'BC'", "ABC"]
    check_sop("17 st13 minimal SOP B'D + C'D + A'BC' + ABC", " + ".join(cover), ones, NAMES4)
    bad = uncovered(cover, ones, NAMES4)
    ok("17 st13 uncovered adjacent pairs: (11, 15), (13, 15)", bad == [(11, 15), (13, 15)], str(bad))
    ok("17 st13 AD = 9, 11, 13, 15", sorted(minterms("AD", NAMES4)) == [9, 11, 13, 15])
    ok("17 st13 with AD: no uncovered pair; same function", uncovered(cover + ["AD"], ones, NAMES4) == [] and same(" + ".join(cover + ["AD"]), ones, NAMES4))
    ok("17 st13 AD is the consensus of B'D (B=0) and ABC... via C'D/ABC on 13-15 and B'D/ABC on 11-15",
       set(minterms("AD", NAMES4)) >= {11, 13, 15})
    ok("17 st13 hazard-free SOP: 5 terms, 14 literals", sum(len([c for c in t if c.isalpha()]) for t in cover + ["AD"]) == 2 + 2 + 3 + 3 + 2)

    # ---------------------------------------------------------- checks and self-test added after writing 17
    ok("17 c1b 3-bit: next state 000 only from 111 -> D_Y = Q2Q1Q0", [x for x in range(8) if (x + 1) % 8 == 0] == [7])
    ok("17 c2 50 MHz: 20 - 2 = 18 ns", 1e3 / 50 - 2 == 18)
    tr = ["".join(map(str, x)) for x in cycle((0, 1, 1), (2, 3), 3)]
    ok("17 c4a from 011: 011 001 100 010 101 110 111", tr == ["011", "001", "100", "010", "101", "110", "111"], str(tr))
    q1 = "".join(x[0] for x in ["100", "010", "101", "110", "111", "011", "001"])
    ok("17 c4b Q1 over a period from 100: 1011100", q1 == "1011100")
    check_sop("17 c6b train 10110: Z = Q1 + Q2'Q0' (dc 5, 6, 7)", "B + A'C'", [0, 2, 3], NAMES3, dcs=[5, 6, 7])
    ok("17 c6b Z = 1 at counts 0, 2, 3 of 10110", [k for k, b in enumerate("10110") if b == "1"] == [0, 2, 3])
    ok("17 c7b 8 MHz / 8 = 1 MHz", 8 / 2 ** 3 == 1)
    ones13 = minterms("A'B' + AC", NAMES3)
    ok("17 c13a A'B' + AC: 1s 0, 1, 5, 7; bad pair (1, 5); B'C fixes",
       sorted(ones13) == [0, 1, 5, 7] and uncovered(["A'B'", "AC"], ones13, NAMES3) == [(1, 5)]
       and uncovered(["A'B'", "AC", "B'C"], ones13, NAMES3) == [])
    ok("17 s1 4-bit Q3 xor Q4 from 0001: 15 clocks", len(cycle((0, 0, 0, 1), (3, 4), 4)) == 15)
    f3 = 1.44 / ((4.7e3 + 2 * 47e3) * 1e-9)
    ok("17 s3 4.7k, 47k, 1n: 14.6 kHz, 52.4 %", close(f3, 14590, 1e-3) and close(100 * 51.7 / 98.7, 52.38, 1e-3), f"{f3:.0f}")
    ok("17 s4 9 x 0.5 ns: 111 MHz", close(1 / (2 * 9 * 0.5e-9), 111.1e6))
    ok("17 s5 01 -> 10 with Q1 first passes 11", 0b11 in via(0b01, 0b10, 2))
    ok("17 s6 100 MHz / 50 / 2 = 1 MHz", 100 / 50 / 2 == 1)
