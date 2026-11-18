"""Files 11 (registers, ring and Johnson counters) and 14 (timing analysis), S7.

Called from verify.py (unit u3r), which injects ok(). Bit lists are written Q0 Q1 Q2 Q3 (Q0 = the
stage the serial input enters, as in deck 09 slides 8, 11, 22).
"""


def s(bits):
    return "".join(str(b) for b in bits)


def shift_right(q, sin):
    """One clock of a right-shift register: sin enters Q0, every bit moves one stage on, Q(n-1) drops out."""
    return [sin] + q[:-1]


def run(q, nxt, n):
    out = [s(q)]
    for _ in range(n):
        q = nxt(q)
        out.append(s(q))
    return out


def cycle_from(q, nxt):
    seen = []
    while s(q) not in seen:
        seen.append(s(q))
        q = nxt(q)
    return seen, s(q)


def ring(q):
    return shift_right(q, q[-1])


def johnson(q):
    return shift_right(q, 1 - q[-1])


def lfsr(q):
    return shift_right(q, q[2] ^ q[3])


def u74194(q, s1, s0, dsr=0, dsl=0, d=None):
    """74HC194 function table (Nexperia data sheet Table 3), outputs Q0..Q3."""
    if (s1, s0) == (0, 0):
        return q[:]
    if (s1, s0) == (0, 1):  # shift right: DSR -> Q0, q0 -> Q1 ...
        return [dsr] + q[:-1]
    if (s1, s0) == (1, 0):  # shift left: q1 -> Q0 ..., DSL -> Q3
        return q[1:] + [dsl]
    return d[:]


def serial_add(a, b):
    """Deck 09 slides 25-26: A <- A + B; A, B written MSB..LSB, shift right, sum into A's MSB, carry FF Q."""
    a, b, qc, steps = a[:], b[:], 0, []
    for _ in range(len(a)):
        x, y = a[-1], b[-1]
        sm, c = x ^ y ^ qc, (x & y) | (x & qc) | (y & qc)
        a = [sm] + a[:-1]
        b = [0] + b[:-1]
        qc = c
        steps.append((sm, c, s(a)))
    return steps, s(a), qc


def u3r():
    # ---------------- file 11
    # step 1: parallel register Q(t+1) = D(t): one clock loads all four bits
    ok("11 st1 PIPO: D = 1011 at one edge -> Q0Q1Q2Q3 = 1011 after 1 clock", s([1, 0, 1, 1]) == "1011")
    # step 2: SISO delay
    q, outs, ins = [0, 0, 0, 0], [], [1, 1, 0, 1]
    for k in range(8):
        q = shift_right(q, ins[k] if k < 4 else 0)
        outs.append(q[3])
    ok("11 st2 SISO 0000, bits 1 1 0 1 enter on clocks 1-4: Q3 after clocks 1..8 = 0 0 0 1 1 0 1 0",
       outs == [0, 0, 0, 1, 1, 0, 1, 0], outs)
    ok("11 st2 4-stage SISO at 1 MHz delays by 4 clocks = 4 us; 8-stage at 2 MHz = 4 us", 4 / 1e6 == 4e-6 and 8 / 2e6 == 4e-6)
    # step 3: SIPO loading 1011, LSB first (deck 09 slide 12)
    q, trace = [0, 0, 0, 0], []
    for b in [1, 1, 0, 1]:
        q = shift_right(q, b)
        trace.append(s(q))
    ok("11 st3 SIPO 1011 LSB first: 1000 1100 0110 1011", trace == ["1000", "1100", "0110", "1011"], trace)
    q, trace2 = [0, 0, 0, 0], []
    for b in [1, 0, 1, 1]:
        q = shift_right(q, b)
        trace2.append(s(q))
    ok("11 c3 SIPO bits sent MSB first 1,0,1,1: 1000 0100 1010 1101 (Q0..Q3 reads 1101 = reversed)",
       trace2 == ["1000", "0100", "1010", "1101"], trace2)
    # step 4: PISO: load D0..D3 = 1011, then shift (0 enters Q0): Q3 = d3 after load, then d2, d1, d0
    q = [1, 0, 1, 1]
    sout = [q[3]]
    for _ in range(3):
        q = shift_right(q, 0)
        sout.append(q[3])
    ok("11 st4 PISO load 1011: Q3 after load, shift 1, 2, 3 = 1 1 0 1 (d3 d2 d1 d0)", sout == [1, 1, 0, 1], sout)
    ok("11 st4 PISO stage-2 D = SHIFT.Q1 + SHIFT'.D2: SHIFT=1 picks Q1, SHIFT=0 picks D2",
       all(((sh & q1) | ((1 - sh) & d2)) == (q1 if sh else d2) for sh in (0, 1) for q1 in (0, 1) for d2 in (0, 1)))
    # step 5: 74194 on the running word 1011
    w = [1, 0, 1, 1]
    ok("11 st5 74194 S1S0=00 hold 1011", s(u74194(w, 0, 0)) == "1011")
    ok("11 st5 74194 S1S0=01 shift right DSR=0: 1011 -> 0101", s(u74194(w, 0, 1, dsr=0)) == "0101")
    ok("11 st5 74194 S1S0=10 shift left DSL=0: 1011 -> 0110", s(u74194(w, 1, 0, dsl=0)) == "0110")
    ok("11 st5 74194 S1S0=11 load 0110", s(u74194(w, 1, 1, d=[0, 1, 1, 0])) == "0110")
    q = w
    for m in [(0, 1, 1, 0), (0, 1, 0, 0), (1, 0, 0, 1), (0, 0, 0, 0)]:
        q = u74194(q, m[0], m[1], dsr=m[2], dsl=m[3])
    ok("11 c5 1011: right(DSR=1) 1101, right(DSR=0) 0110, left(DSL=1) 1101, hold 1101", s(q) == "1101", s(q))
    ok("11 c5 trace values", s(u74194(w, 0, 1, dsr=1)) == "1101" and s(u74194([1, 1, 0, 1], 0, 1, dsr=0)) == "0110"
       and s(u74194([0, 1, 1, 0], 1, 0, dsl=1)) == "1101")
    # step 6: ring counters
    c4, back = cycle_from([1, 0, 0, 0], ring)
    ok("11 st6 4-bit ring from 1000: 1000 0100 0010 0001, MOD-4", c4 == ["1000", "0100", "0010", "0001"] and back == "1000", c4)
    c6, back6 = cycle_from([1, 0, 0, 0, 0, 0], ring)
    ok("11 st6 EX 9.20 6-bit ring from 100000: 6 states, MOD-6", len(c6) == 6 and back6 == "100000", c6)
    ok("11 st6 ring outputs one-hot: each state has exactly one 1", all(x.count("1") == 1 for x in c6))
    ok("11 st6 ring 0000 stays 0000", cycle_from([0, 0, 0, 0], ring)[0] == ["0000"])
    cc, _ = cycle_from([1, 1, 0, 0], ring)
    ok("11 c6 ring started at 1100: 1100 0110 0011 1001 (two 1s circulate)", cc == ["1100", "0110", "0011", "1001"], cc)
    ok("11 st6 6-bit ring at 600 kHz: each output 100 kHz (f/6)", 600e3 / 6 == 100e3)
    # step 7: Johnson
    j4, jb = cycle_from([0, 0, 0, 0], johnson)
    ok("11 st7 EX 9.22 4-bit Johnson: 0000 1000 1100 1110 1111 0111 0011 0001, MOD-8",
       j4 == ["0000", "1000", "1100", "1110", "1111", "0111", "0011", "0001"] and jb == "0000", j4)
    j3, _ = cycle_from([0, 0, 0], johnson)
    ok("11 st7 3-bit Johnson: 000 100 110 111 011 001, MOD-6", j3 == ["000", "100", "110", "111", "011", "001"], j3)
    j5, _ = cycle_from([0] * 5, johnson)
    ok("11 c7 MOD-10: Johnson 5 FF, ring 10 FF, binary 4 FF", len(j5) == 10 and 2 ** 4 >= 10 > 2 ** 3)
    terms = {"0000": (0, 0, 3, 0), "1000": (0, 1, 1, 0), "1100": (1, 1, 2, 0), "1110": (2, 1, 3, 0),
             "1111": (0, 1, 3, 1), "0111": (0, 0, 1, 1), "0011": (1, 0, 2, 1), "0001": (2, 0, 3, 1)}
    # term (i, vi, k, vk): Q_i = vi AND Q_k = vk
    uniq = all(sum(1 for st in j4 if int(st[i]) == vi and int(st[k]) == vk) == 1 and int(t[i]) == vi and int(t[k]) == vk
               for t, (i, vi, k, vk) in terms.items())
    ok("11 st7 each 2-input decode term is 1 in exactly one of the 8 Johnson states", uniq)
    ok("11 st7 Johnson outputs: each Q high 4 of 8 clocks (50 % duty, f/8)", all(sum(int(st[i]) for st in j4) == 4 for i in range(4)))
    # step 8: lock-out
    bad, bb = cycle_from([0, 1, 0, 0], johnson)
    ok("11 st8 Johnson from 0100: 8-state loop 0100 1010 1101 0110 1011 0101 0010 1001, never 0000",
       bad == ["0100", "1010", "1101", "0110", "1011", "0101", "0010", "1001"] and "0000" not in bad, bad)
    ok("11 st8 the 16 states split into the 8 good + 8 bad", sorted(bad + j4) == sorted(format(i, "04b") for i in range(16)))
    # step 9: XOR-feedback SIPO, EX 9.24 (deck 09 slide 24): feedback = Q2 xor Q3 into Q0
    x = run([0, 1, 1, 0], lfsr, 5)
    ok("11 st9 EX 9.24 0110 -> 1011 -> 0101 -> 1010 (-> 1101 -> 1110)", x == ["0110", "1011", "0101", "1010", "1101", "1110"], x)
    lc, lb = cycle_from([0, 1, 1, 0], lfsr)
    ok("11 st9 the XOR register visits all 15 non-zero states before repeating", len(lc) == 15 and "0000" not in lc and lb == "0110")
    ok("11 st9 0000 stays 0000 under XOR feedback", cycle_from([0, 0, 0, 0], lfsr)[0] == ["0000"])
    # step 10: serial adder EX 9.26
    steps, a_final, c_final = serial_add([0, 1, 0, 0], [0, 1, 1, 1])
    ok("11 st10 EX 9.26 0100 + 0111: (S,C) per clock (1,0) (1,0) (0,1) (1,0); A after: 1010 1101 0110 1011",
       steps == [(1, 0, "1010"), (1, 0, "1101"), (0, 1, "0110"), (1, 0, "1011")], steps)
    ok("11 st10 4 + 7 = 11 = 1011, carry FF 0 at the end", a_final == "1011" and c_final == 0 and 4 + 7 == 11)
    st2, a2, c2 = serial_add([0, 1, 1, 0], [0, 0, 1, 1])
    ok("11 c10 0110 + 0011 = 1001: (S,C) (1,0) (0,1) (0,1) (1,0)", a2 == "1001" and [(p[0], p[1]) for p in st2] == [(1, 0), (0, 1), (0, 1), (1, 0)], st2)
    # self-test
    ok("11 ST 5-bit ring MOD-5; 5-bit Johnson MOD-10; 8 FF Johnson MOD-16", len(cycle_from([1, 0, 0, 0, 0], ring)[0]) == 5
       and len(cycle_from([0] * 8, johnson)[0]) == 16)
    ok("11 ST Johnson state 1110 decode Q2 Q3'", terms["1110"] == (2, 1, 3, 0))
    ok("11 ST 8-bit SIPO at 9600 bit/s: 8 clocks = 0.833 ms", abs(8 / 9600 - 0.000833) < 1e-6)

    # ---------------- file 14 (t in ns)
    tpd, tsu, th, cmax, cmin = 8, 3, 2, 12, 1
    T = tpd + cmax + tsu
    ok("14 st5 running example T_min = 8 + 12 + 3 = 23 ns, f_max = 43.5 MHz", T == 23 and round(1e3 / T, 1) == 43.5)
    ok("14 st5 at 40 MHz (25 ns) data arrives 23 ns: 2 ns spare; at 50 MHz (20 ns) fails by 3 ns",
       25 - T == 2 and 20 - T == -3)
    ok("14 st6 hold: 8 + 1 = 9 ns >= 2 ns, 7 ns spare", tpd + cmin >= th and tpd + cmin - th == 7)
    ok("14 c5 longest path +4 ns: 27 ns, 37.0 MHz; hold unchanged", tpd + cmax + 4 + tsu == 27 and round(1e3 / 27, 1) == 37.0)
    ok("14 st1 50 MHz clock period 20 ns; Q valid 8 ns after the edge = 40 % of the period", 1e3 / 50 == 20 and 8 / 20 == 0.4)
    # skew: d = capture clock later than launch clock (ns)
    setup = lambda d, cm=cmax: tpd + cm + tsu - d
    hold_ok = lambda d, cn=cmin: tpd + cn >= th + d
    ok("14 st7 skew +3: T_min 20 ns (50 MHz); hold 9 >= 5 holds", setup(3) == 20 and round(1e3 / setup(3)) == 50 and hold_ok(3))
    ok("14 st7 skew -3 (capture early): T_min 26 ns, 38.5 MHz", setup(-3) == 26 and round(1e3 / 26, 1) == 38.5)
    ok("14 st7 skew +8: hold 9 >= 10 fails by 1 ns", not hold_ok(8) and (th + 8) - (tpd + cmin) == 1)
    ok("14 st7 fix: 2 ns buffer on the short path: 8 + 3 = 11 >= 10; long path unchanged (T_min 15 ns)",
       hold_ok(8, cmin + 2) and setup(8) == 15)
    ok("14 st7 hold with skew does not contain T: changing T leaves 9 >= 10 false", not hold_ok(8))
    ok("14 c7 skew +7: hold 9 >= 9 just met; T_min 16 ns, 62.5 MHz", hold_ok(7) and setup(7) == 16 and 1e3 / 16 == 62.5)
    # step 8: counters
    ok("14 st8 4-bit ripple t_pd 10 ns: 40 ns, 25 MHz; synchronous 10 + 5 + 5 = 20 ns, 50 MHz",
       4 * 10 == 40 and 1e3 / 40 == 25 and 10 + 5 + 5 == 20 and 1e3 / 20 == 50)
    ok("14 st8 8-bit ripple 80 ns, 12.5 MHz; 8-bit synchronous (one AND level) still 20 ns",
       8 * 10 == 80 and 1e3 / 80 == 12.5)
    # self-test
    ok("14 ST1 5 + 10 + 2 = 17 ns, 58.8 MHz", 5 + 10 + 2 == 17 and round(1e3 / 17, 1) == 58.8)
    ok("14 ST2 2 + 0.5 = 2.5 < 3: violated by 0.5 ns", 2 + 0.5 < 3 and 3 - 2.5 == 0.5)
    ok("14 ST4 t_pd 6, comb 9, su 2, skew +2: T_min 15 ns (66.7 MHz); hold: 6 + 1 = 7 >= 1 + 2", 6 + 9 + 2 - 2 == 15
       and round(1e3 / 15, 1) == 66.7 and 6 + 1 >= 1 + 2)
    ok("14 ST5 100 MHz needs T 10 ns: 4 + c + 2 <= 10 -> c <= 4 ns", 10 - 4 - 2 == 4)

    # ---------------- added after the text was written (S7)
    q = [1, 1, 0, 0]
    so = [q[3]]
    for _ in range(3):
        q = shift_right(q, 0)
        so.append(q[3])
    ok("11 c4 PISO load 1100: output after load, shifts 1-3 = 0 0 1 1", so == [0, 0, 1, 1], so)
    q = [1, 0, 1, 1]
    q = shift_right(q, 0); a1 = s(q); q = shift_right(q, 0); a2 = s(q); q = shift_right(q, 0); a3 = s(q)
    ok("11 st4 PISO register after shifts 1-3: 0101 0010 0001", (a1, a2, a3) == ("0101", "0010", "0001"))
    ok("11 c10 serial 0110 + 0011: A after clocks 1011 0101 0010 1001", [p[2] for p in serial_add([0, 1, 1, 0], [0, 0, 1, 1])[0]] == ["1011", "0101", "0010", "1001"])
    ok("11 ST2 8-FF Johnson: 16 used, 240 unused", 2 ** 8 - 16 == 240)
    ok("11 st8 unused counts 4 bits: ring 16 - 4 = 12, Johnson 16 - 8 = 8", 16 - 4 == 12 and 16 - 8 == 8)
    ok("11 c8 after 1101 in the unused loop: 0110 1011 0101", run([1, 1, 0, 1], johnson, 3)[1:] == ["0110", "1011", "0101"])
    ok("14 c1 100 MHz: T 10 ns, t_pd 8 ns = 80 %", 1e3 / 100 == 10 and 8 / 10 == 0.8)
    win = lambda e, tc: e - 3 < tc < e + 2   # inside setup+hold window, t_su 3, t_h 2 (boundaries safe)
    ok("14 c2 edge 40: change at 30 safe, 37 at the limit (safe), 38.5 inside", not win(40, 30) and not win(40, 37) and win(40, 38.5))
    ok("14 st3 edge 20: 15 safe, 18 setup broken, 21 hold broken, 23 safe; window 17-22, 5 ns",
       not win(20, 15) and win(20, 18) and win(20, 21) and not win(20, 23) and 3 + 2 == 5)
    ok("14 st7 table: d=-3 hold 9 >= -1; d=+8 T_min 15 ns 66.7 MHz", 9 >= 2 - 3 and 23 - 8 == 15 and round(1e3 / 15, 1) == 66.7)
    ok("14 c8 3-bit ripple 60 ns 16.7 MHz; synchronous 30 ns 33.3 MHz", 3 * 20 == 60 and round(1e3 / 60, 1) == 16.7
       and 20 + 5 + 5 == 30 and round(1e3 / 30, 1) == 33.3)
