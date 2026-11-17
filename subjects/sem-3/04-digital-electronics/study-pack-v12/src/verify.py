"""Independent re-computation of every number and expression printed in the ECE2102 v1.3 study pack.

    python verify.py            -> runs the v1 checks, then every unit's checks; exit 1 on any failure
    python verify.py u1 u3      -> v1 checks + only the named units

Method (spec v1.3 §7.4): every printed Boolean expression is compared with the function it claims
to equal on every input row (exhaustive truth table; don't-care rows skipped); a printed minimum is
also compared with the Quine-McCluskey cost (terms, literals) from the v1 `qm.py`. Counters, flip-flop
waveforms and state machines are simulated clock edge by clock edge. Logic-family numbers are
recomputed from the level/current table the pack prints.

Part 0 runs the v1 pack's own checks (`../../study-pack/pdf-ete/verify.py`, ~500 lines, 0 failures
expected): the v1.2 files still print those answers until each one is rebuilt.
Units are added by the sprint that builds their files (S1: u1, S2: u3 flip-flops, ...).
"""
import subprocess
import sys
from itertools import product
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
HERE = Path(__file__).resolve().parent
V1 = HERE.parents[1] / "study-pack" / "pdf-ete"
sys.path.insert(0, str(V1))
import qm  # noqa: E402  (v1 Quine-McCluskey; used for the minimum-cost comparison)

FAILS, N = [], [0]


def ok(label, cond, detail=""):
    N[0] += 1
    if not cond:
        FAILS.append(label)
    print(f"{'ok  ' if cond else 'FAIL'} {label}{'' if cond else '  ' + str(detail)}")


# ---------------------------------------------------------------- Boolean expressions
class _P:
    """Recursive-descent parser: + (OR), ⊕ or ^ (XOR), juxtaposition or · (AND), postfix ' (NOT),
    ( ), constants 0/1. Variable names are given explicitly (longest match first), e.g. "ABCD" or
    ["Q2", "Q1", "Q0"]."""

    def __init__(self, s, names):
        self.s = s.replace(" ", "").replace("·", "").replace("’", "'").replace("‾", "'")
        self.names = sorted(names, key=len, reverse=True)
        self.i = 0

    def peek(self):
        return self.s[self.i] if self.i < len(self.s) else ""

    def expr(self):
        t = self.xor()
        while self.peek() == "+":
            self.i += 1
            a, b = t, self.xor()
            t = (lambda a, b: lambda e: a(e) | b(e))(a, b)
        return t

    def xor(self):
        t = self.term()
        while self.peek() in ("⊕", "^"):
            self.i += 1
            a, b = t, self.term()
            t = (lambda a, b: lambda e: a(e) ^ b(e))(a, b)
        return t

    def term(self):
        t = self.fact()
        while self.peek() and self.peek() not in "+)⊕^":
            a, b = t, self.fact()
            t = (lambda a, b: lambda e: a(e) & b(e))(a, b)
        return t

    def fact(self):
        c = self.peek()
        if c == "(":
            self.i += 1
            t = self.expr()
            assert self.peek() == ")", f"missing ) in {self.s}"
            self.i += 1
        elif c in "01":
            self.i += 1
            t = (lambda v: lambda e: v)(int(c))
        else:
            for v in self.names:
                if self.s.startswith(v, self.i):
                    self.i += len(v)
                    t = (lambda v: lambda e: e[v])(v)
                    break
            else:
                raise ValueError(f"bad token at {self.s[self.i:]!r} in {self.s!r}")
        while self.peek() == "'":
            self.i += 1
            t = (lambda a: lambda e: 1 - a(e))(t)
        return t


def fn(expr, names):
    p = _P(expr, names)
    f = p.expr()
    assert p.i == len(p.s), f"trailing text in {expr!r}"
    return f


def rows(names):
    """(minterm index, env) for every row; the first name is the MSB."""
    names = list(names)
    for bits in product((0, 1), repeat=len(names)):
        yield int("".join(map(str, bits)), 2), dict(zip(names, bits))


def minterms(expr, names):
    f = fn(expr, names)
    return [m for m, e in rows(names) if f(e)]


def same(expr, ones, names, dcs=()):
    """True if expr is 1 exactly on `ones` (rows in `dcs` are free)."""
    f = fn(expr, names)
    return all(f(e) == (m in ones) for m, e in rows(names) if m not in dcs)


def cost(expr):
    """(terms, literals) of a flat SOP string."""
    ts = [t for t in expr.replace(" ", "").split("+") if t]
    return len(ts), sum(sum(ch.isalpha() for ch in t) for t in ts)


def check_sop(label, expr, ones, names, dcs=(), minimal=True):
    ok(f"{label}: {expr} on all {2 ** len(list(names))} rows", same(expr, ones, names, dcs), minterms(expr, names))
    if minimal:
        sols = qm.sop(list(ones), list(dcs), list(names))  # every minimum cover, as SOP strings
        best = min(cost(s) for s in sols)
        ok(f"{label}: cost {cost(expr)} = QM minimum {best}", cost(expr) == best, sols)


def check_pos(label, expr, zeros, names, dcs=()):
    ones = [m for m, _ in rows(names) if m not in zeros and m not in dcs]
    ok(f"{label}: {expr} is 0 exactly on {list(zeros)}", same(expr, ones, names, dcs))


# ---------------------------------------------------------------- flip-flops, counters, FSMs
def ff_next(kind, q, **x):
    """Characteristic equations: D: Q+=D · T: Q+=T⊕Q · JK: Q+=JQ'+K'Q · SR: Q+=S+R'Q (S=R=1 invalid)."""
    if kind == "D":
        return x["D"]
    if kind == "T":
        return x["T"] ^ q
    if kind == "JK":
        return (x["J"] & (1 - q)) | ((1 - x["K"]) & q)
    if kind == "SR":
        assert not (x["S"] and x["R"]), "S=R=1 is not allowed"
        return x["S"] | ((1 - x["R"]) & q)
    raise ValueError(kind)


def run_sync(kind, inputs, state, steps, names):
    """Synchronous circuit: `inputs[i]` maps flip-flop i (MSB first, named names[i]) to a dict of its
    input expressions (e.g. {"T": "Q1Q0"}). Returns the state sequence as integers."""
    fs = [{k: fn(v, names) for k, v in inputs[i].items()} for i in range(len(names))]
    seq = [state]
    for _ in range(steps):
        e = dict(zip(names, (int(b) for b in format(state, f"0{len(names)}b"))))
        nxt = [ff_next(kind, e[n], **{k: f(e) for k, f in fs[i].items()}) for i, n in enumerate(names)]
        state = int("".join(map(str, nxt)), 2)
        seq.append(state)
    return seq


def run_ripple(n, up=True, start=0, steps=8):
    """n T=1 flip-flops, each clocked by the previous stage (negative-edge, Q drives the next clock for
    an up counter, Q' for a down counter). Settled count after each input clock edge."""
    q, seq = [(start >> i) & 1 for i in range(n)], [start]
    for _ in range(steps):
        i = 0
        while i < n:
            old = q[i]
            q[i] ^= 1
            fell = (old == 1 and q[i] == 0) if up else (old == 0 and q[i] == 1)
            if not fell:
                break
            i += 1
        seq.append(sum(b << i for i, b in enumerate(q)))
    return seq


def run_fsm(table, start, xs, mealy=True):
    """table[state][x] = (next_state, output) for Mealy; for Moore the output is table[state]["z"]."""
    s, out = start, []
    for x in xs:
        if mealy:
            s, z = table[s][x]
            out.append(z)
        else:
            s = table[s][x]
            out.append(table[s]["z"])
    return out


def detect(pattern, xs, overlap=True):
    """Reference detector output for a bit string: 1 at each position where `pattern` ends."""
    out, last = [], -len(pattern)
    for i in range(len(xs)):
        hit = xs[max(0, i - len(pattern) + 1):i + 1] == pattern and (overlap or i - last >= len(pattern))
        out.append(int(hit))
        if hit:
            last = i
    return out


# ---------------------------------------------------------------- units (filled by S1 onward)
def u0():
    """Self-test of the helpers against facts any build relies on."""
    check_sop("helper: De Morgan (x+y)' = x'y'", "x'y'", minterms("(x+y)'", "xy"), "xy", minimal=False)
    check_sop("helper: v1 K-map (v1figs km abcd)", "b'c' + bc + a'c'", [0, 4, 5, 7, 8, 9, 15], "abcd", dcs=[1, 3, 6, 14])
    ok("helper: consensus xy + x'z + yz = xy + x'z", same("xy + x'z", minterms("xy+x'z+yz", "xyz"), "xyz"))
    ok("helper: 3-bit T counter T0=1, T1=Q0, T2=Q1Q0 counts 0..7,0",
       run_sync("T", [{"T": "Q1Q0"}, {"T": "Q0"}, {"T": "1"}], 0, 8, ["Q2", "Q1", "Q0"]) == [0, 1, 2, 3, 4, 5, 6, 7, 0])
    ok("helper: 3-bit ripple up counts 0..7,0", run_ripple(3, True, 0, 8) == [0, 1, 2, 3, 4, 5, 6, 7, 0])
    ok("helper: 3-bit ripple down counts 0,7..0", run_ripple(3, False, 0, 8) == [0, 7, 6, 5, 4, 3, 2, 1, 0])
    ok("helper: JK toggles at J=K=1", ff_next("JK", 0, J=1, K=1) == 1 and ff_next("JK", 1, J=1, K=1) == 0)
    ok("helper: overlapping 1101 detector", detect([1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1]) == [0, 0, 0, 1, 0, 0, 1])
    # Standard-TTL table (KB 05 §1, `settled`): the numbers file 18 prints.
    VOH, VOL, VIH, VIL = 2.4, 0.4, 2.0, 0.8
    IOH, IOL, IIH, IIL = 400e-6, 16e-3, 40e-6, 1.6e-3
    ok("KB05 TTL NM_H = 0.4 V, NM_L = 0.4 V", abs(VOH - VIH - 0.4) < 1e-9 and abs(VIL - VOL - 0.4) < 1e-9)
    ok("KB05 TTL fan-out = min(16/1.6, 400/40) = 10", min(round(IOL / IIL, 9), round(IOH / IIH, 9)) == 10)


def eq(label, e1, e2, names, dcs=()):
    """Two printed expressions agree on every row (don't-care rows skipped)."""
    ok(f"{label}: {e1} = {e2}", same(e1, minterms(e2, names), names, dcs))


def rows_of(label, expr, want, names):
    ok(f"{label}: {expr} is 1 on rows {want}", minterms(expr, names) == list(want), minterms(expr, names))


def pos_min(label, expr, ones, names, dcs=()):
    """A printed POS is 0 exactly on the 0-rows and has the QM-minimum literal count."""
    zeros = [m for m in range(2 ** len(names)) if m not in ones and m not in dcs]
    check_pos(label, expr, zeros, names, dcs)
    lits = lambda s: sum(ch.isalpha() for ch in s)
    best = min(lits(p) for p in qm.pos(list(ones), list(dcs), list(names)))
    ok(f"{label}: {lits(expr)} literals = QM POS minimum {best}", lits(expr) == best)


def nbrs(m, n):
    return sorted(m ^ (1 << i) for i in range(n))


def u1():
    """Files 01-03 (S1): every expression, list and gate network printed in 01, 02, 03."""
    # ---- 01 Boolean algebra
    X3 = "xyz"
    eq("01 run: as written = Σm(2,3,5,7)", "x'yz + x'yz' + xz", "x'yz'+x'yz+xy'z+xyz", X3)
    check_sop("01 s6 running example", "x'y + xz", [2, 3, 5, 7], X3)
    ok("01 s3 running example as written costs 3 terms, 8 literals", cost("x'yz + x'yz' + xz") == (3, 8))
    check_pos("01 s8 ΠM(0,1,4,6)", "(x+y+z)(x+y+z')(x'+y+z)(x'+y'+z)", [0, 1, 4, 6], X3)
    check_pos("01 s10 short POS", "(x+y)(x'+z)", [0, 1, 4, 6], X3)
    ok("01 c1 1+1+0 = 1", fn("1+1+0", "")({}) == 1)
    ok("01 s2 rows: 2^3 = 8, 2^5 = 32, 2^4 = 16", (2 ** 3, 2 ** 5, 2 ** 4) == (8, 32, 16))
    rows_of("01 c2 xz", "xz", [5, 7], X3)
    eq("01 s3 XOR", "A'B + AB'", "A⊕B", "AB")
    eq("01 s3 XNOR", "A'B' + AB", "(A⊕B)'", "AB")
    for e1, e2 in (("X + YZ", "(X+Y)(X+Z)"), ("X + X'Y", "X+Y"), ("X(X+Y)", "X"), ("X + XY", "X"),
                   ("XY + X'Z + YZ", "XY + X'Z"), ("(X+Y)'", "X'Y'"), ("(XY)'", "X'+Y'")):
        eq("01 s4-5 law", e1, e2, "XYZ")
    eq("01 s5 answer", "(A + B'C)'", "A'(B + C')", "ABC")
    eq("01 c5a", "(xyz)'", "x'+y'+z'", X3)
    eq("01 c5b", "((A+B)C')'", "A'B' + C", "ABC")
    eq("01 c5c F'", "(x'y + xz)'", "xz' + x'y'", X3)
    eq("01 c5c product form", "(x+y')(x'+z')", "xz' + x'y'", X3)
    check_sop("01 c6a slide 19", "x'z' + yz'", minterms("x'y'z' + x'yz' + xyz'", X3), X3)
    eq("01 c6b", "xy + xy'z", "xy + xz", X3)
    rows_of("01 s7 m3", "A'BC", [3], "ABC")
    rows_of("01 c7a m5", "AB'C", [5], "ABC")
    rows_of("01 c7b AB + C'", "AB + C'", [0, 2, 4, 6, 7], "ABC")
    check_pos("01 s8 M3", "(A + B' + C')", [3], "ABC")
    check_pos("01 c8a M5", "(A' + B + C')", [5], "ABC")
    check_pos("01 c8b a+b'+c", "(a + b' + c)", [2], "abc")
    rows_of("01 s9 f1 SOP", "a'b'c + a'bc' + ab'c' + abc'", [1, 2, 4, 6], "abc")
    check_pos("01 s9 f1 ΠM(0,3,5,7)", "(a + b + c)(a + b' + c')(a' + b + c')(a' + b' + c')", [0, 3, 5, 7], "abc")
    ok("01 c9 Σm(0,2,5) -> ΠM(1,3,4,6,7)", [m for m in range(8) if m not in (0, 2, 5)] == [1, 3, 4, 6, 7])
    rows_of("01 s10 slide 31 standard SOP", "a'b'c + bc' + ac'", [1, 2, 4, 6], "abc")
    rows_of("01 c10a A + B'C", "A + B'C", [1, 4, 5, 6, 7], "ABC")
    check_pos("01 c10b (a+b')(b+c)", "(a+b')(b+c)", [0, 2, 3, 4], "abc")
    eq("01 st1", "AB + AB' + A'B", "A + B", "AB")
    check_pos("01 st3 Σm(1,3,6,7)", "(A+B+C)(A+B'+C)(A'+B+C)(A'+B+C')", [0, 2, 4, 5], "ABC")
    check_pos("01 st5 A + B'C as ΠM(0,2,3)", "A + B'C", [0, 2, 3], "ABC")
    rows_of("01 st7 m9", "AB'C'D", [9], "ABCD")
    check_pos("01 st7 M9", "(A' + B + C + D')", [9], "ABCD")

    # ---- 02 K-maps
    check_sop("02 s1 Z = AB' + AB", "A", [2, 3], "AB")
    check_sop("02 c1a OR", "A + B", [1, 2, 3], "AB")
    ok("02 c2a neighbours of 5 = 1, 4, 7", nbrs(5, 3) == [1, 4, 7])
    ok("02 st6 neighbours of 6 = 2, 4, 7", nbrs(6, 3) == [2, 4, 7])
    rows_of("02 c3b y'z'", "y'z'", [0, 4], X3)
    check_sop("02 s4 slide 27", "b", [2, 3, 6, 7], "abc")
    eq("02 s4 two pairs", "a'b + ab", "b", "abc")
    rows_of("02 s4 checkerboard a⊕b⊕c", "a⊕b⊕c", [1, 2, 4, 7], "abc")
    check_sop("02 s5 slide 44", "a'b + ab' + bc'", [2, 3, 4, 5, 6], "abc")
    check_sop("02 s5 alternative", "a'b + ab' + ac'", [2, 3, 4, 5, 6], "abc")
    check_sop("02 c5 slides 27-32", "a'b + ab'", [2, 3, 4, 5], "abc")
    rows_of("02 s6 corners b'd'", "b'd'", [0, 2, 8, 10], "abcd")
    MTE = [0, 4, 5, 7, 8, 9, 15]
    for e in ("b'c'd' + a'bc' + bcd + ab'c'", "a'c'd' + a'bc' + bcd + ab'c'", "a'c'd' + a'bd + bcd + ab'c'"):
        check_sop("02 s6 MTE Q4 without don't-cares", e, MTE, "abcd")
    for e in ("b'c' + bc + a'c'", "b'c' + bc + a'b"):
        check_sop("02 s7 MTE Q4", e, MTE, "abcd", dcs=[1, 3, 6, 14])
    for e in ("a'b'd' + a'b'c + a'cd' + ac'd' + abd", "b'c'd' + a'b'c + a'cd' + ac'd' + abd",
              "b'c'd' + a'b'c + a'cd' + abc' + abd"):
        check_sop("02 c6 slide 51", e, [0, 2, 3, 6, 8, 12, 13, 15], "abcd")
    for e in ("a'd' + c'd' + abd", "a'd' + ac' + abd"):
        check_sop("02 c7 slide 69", e, [0, 2, 6, 8, 12, 13, 15], "abcd", dcs=[3, 4, 9])
    S63 = [0, 1, 2, 5, 8, 9, 10]
    check_sop("02 s8 slide 63 SOP", "X'Y' + X'Z' + W'Y'Z", S63, "WXYZ")
    pos_min("02 s8 slide 63 POS", "(W' + X')(Y' + Z')(X' + Z)", S63, "WXYZ")
    check_sop("02 c8a slide 64", "W + XYZ + X'Y'Z", [m for m in range(16) if m not in (0, 2, 3, 4, 5, 6)], "WXYZ")
    pos_min("02 c8b MTE Q4 POS", "(b + c')(a' + b' + c)", MTE, "abcd", dcs=[1, 3, 6, 14])
    check_sop("02 s9 slide 58", "ce", [5, 7, 13, 15, 21, 23, 29, 31], "abcde")
    P1 = [0, 2, 5, 8, 10, 13, 15, 17, 19, 21, 26, 28, 29, 30, 31]
    check_sop("02 s9 PS1 Q1", "xz + wz' + v'x'z' + vw'z", P1, "vwxyz", dcs=[7, 12, 14, 23, 24])
    ok("02 s9 PS1 Q1 cost (4, 10)", cost("xz + wz' + v'x'z' + vw'z") == (4, 10))
    S62 = [0, 1, 4, 5, 6, 11, 12, 14, 16, 20, 22, 28, 30, 31]
    check_sop("02 c9 slide 62", "XZ' + V'W'Y' + W'Y'Z' + V'WX'YZ + VWXY", S62, "VWXYZ")
    ok("02 c9 cost (5, 17)", cost("XZ' + V'W'Y' + W'Y'Z' + V'WX'YZ + VWXY") == (5, 17))
    ok("02 c9 cell 11 has no 1-neighbour", not set(nbrs(11, 5)) & set(S62))
    pair = [m for m in range(16) if any((m >> i) & 3 == 3 for i in range(3))]
    ok("02 s10 PS1 Q4 rows = 3,6,7,11,12,13,14,15", pair == [3, 6, 7, 11, 12, 13, 14, 15])
    check_sop("02 s10 PS1 Q4", "AB + BC + CD", pair, "ABCD")
    three = [m for m in range(16) if any((m >> i) & 7 == 7 for i in range(2))]
    eq("02 c10 three consecutive", "ABC + BCD", "+".join(qm.lit((m, 0), "ABCD") for m in three), "ABCD")
    check_sop("02 st1", "a' + bc", [0, 1, 2, 3, 7], "abc")
    check_sop("02 st2", "B'C' + CD' + A'BD", [0, 1, 2, 5, 6, 7, 8, 9, 10, 14], "ABCD")
    for e in ("CD + A'B'", "CD + A'D"):
        check_sop("02 st3", e, [1, 3, 7, 11, 15], "ABCD", dcs=[0, 2, 5])
    pos_min("02 st4", "(A + B + C')(A' + B' + C)", [0, 2, 3, 4, 5, 7], "ABC")

    # ---- 03 NAND / NOR (every gate network evaluated row by row)
    eq("03 s2 MTE Q1", "P'Q' + P'", "P'", "PQ")
    eq("03 s2 NOR(P,P)", "(P+P)'", "P'", "PQ")
    for e1, e2 in (("(XX)'", "X'"), ("((XY)')'", "XY"), ("(X'Y')'", "X+Y"),
                   ("((X+Y)')'", "X+Y"), ("(X'+Y')'", "XY")):
        eq("03 s1-2 universal", e1, e2, "XY")
    eq("03 s3 slide 41 NAND-NAND", "((X'Y'Z')'(XYZ')')'", "X'Y'Z' + XYZ'", "XYZ")
    n3, n4 = "((AB')'(A'B)')'", "(C'D)'"
    n5 = f"({n3}E{n4})'"
    eq("03 s4 slide 42 N3", n3, "AB' + A'B", "ABCDE")
    eq("03 s4 slide 42 N4", n4, "C + D'", "ABCDE")
    eq("03 s4 slide 42 six NANDs", f"({n5}{n5})'", "(AB' + A'B)E(C + D')", "ABCDE")
    eq("03 s5 slide 45 NOR-NOR", "((X'+Y)' + (X+Y')' + Z)'", "(X'+Y)(X+Y')Z'", "XYZ")
    check_sop("03 s6 PS1 Q2", "w'x' + w'z + x'y", [0, 1, 3, 5, 7, 10, 11], "wxyz", dcs=[2, 6, 13])
    eq("03 s6 PS1 Q2 NAND-NAND", "((w'x')'(w'z)'(x'y)')'", "w'x' + w'z + x'y", "wxyz")
    eq("03 s6 PS1 Q1 NAND-NAND", "((v'x'z')'(xz)'(wz')'(vw'z)')'", "xz + wz' + v'x'z' + vw'z", "vwxyz")
    eq("03 c2a NOR AND", "((A+A)' + (B+B)')'", "AB", "AB")
    eq("03 c2b P' + Q' via NOR", "((((P+P)' + (Q+Q)')')+(((P+P)' + (Q+Q)')'))'", "P' + Q'", "PQ")
    eq("03 c3a MTE Q4 NAND", "((b'c')'(bc)'(a'c')')'", "b'c' + bc + a'c'", "abcd")
    eq("03 c3b running 01 NAND", "((x'y)'(xz)')'", "x'y + xz", X3)
    eq("03 c4a A + BC", "(A'(BC)')'", "A + BC", "ABC")
    eq("03 c4b (A+B)(C+D) NAND", "((((A'B')'(C'D')')')((A'B')'(C'D')')')'", "(A+B)(C+D)", "ABCD")
    eq("03 c5a NOR-NOR", "((A+B)' + (C+D)')'", "(A+B)(C+D)", "ABCD")
    eq("03 c5b NOR-NOR", "((A+B)' + (C+C)')'", "(A+B)C", "ABC")
    eq("03 c6 MTE Q4 NOR-NOR", "((b+c')' + (a'+b'+c)')'", "b'c' + bc + a'c'", "abcd", dcs=[1, 3, 6, 14])
    x1 = "(AB)'"
    xor = f"((A{x1})'(B{x1})')'"
    eq("03 s7 XOR from 4 NANDs", xor, "A⊕B", "AB")
    e11 = {"A": 1, "B": 1}
    ok("03 c7a A=B=1: N1=0, N2=1, N3=1, F=0",
       [fn(s, "AB")(e11) for s in (x1, f"(A{x1})'", f"(B{x1})'", xor)] == [0, 1, 1, 0])
    eq("03 st4", "A'B + A'B' + AB'", "(AB)'", "AB")
    eq("03 st5 NOR from POS", "((x+y)' + (x'+z)')'", "x'y + xz", X3)


def nor(*a):
    return int(not any(a))


def nand(*a):
    return int(not all(a))


def settle(f, q, qb, n=8):
    """Iterate a cross-coupled pair (q, qb) = f(q, qb) to a fixed point (gate-level latch model)."""
    for _ in range(n):
        q, qb = f(q, qb)
    return q, qb


def edge_seq(kind, q, rows):
    """Q after each edge for a list of input dicts (characteristic equation, file 09)."""
    out = []
    for x in rows:
        q = ff_next(kind, q, **x)
        out.append(q)
    return out


def lvl(sig, t):
    v = sig[0][1]
    for tt, vv in sig:
        if tt <= t:
            v = vv
    return v


def u3():
    """Files 09-10 (S2): latch tables at gate level, characteristic/excitation tables, conversions,
    clock numbers, and every waveform answer re-simulated from the question data."""
    sys.path.insert(0, str(HERE))
    import figs_u3 as W  # question data only (inputs read from the exam images)
    # ---- 09 step 1: inverter ring holds both values
    ok("09 s1 inverter ring: Q=1 and Q=0 both stable", all(settle(lambda q, qb: (1 - qb, 1 - q), v, 1 - v) == (v, 1 - v) for v in (0, 1)))
    # ---- 09 step 2: NOR latch table (Q = NOR(R, Q'), Q' = NOR(S, Q)), rows S R Q0 -> Q Q'
    nor_tab = {(0, 0, 0): (0, 1), (0, 0, 1): (1, 0), (0, 1, 0): (0, 1), (0, 1, 1): (0, 1),
               (1, 0, 0): (1, 0), (1, 0, 1): (1, 0), (1, 1, 0): (0, 0), (1, 1, 1): (0, 0)}
    for (s, r, q0), want in nor_tab.items():
        got = settle(lambda q, qb: (nor(r, qb), nor(s, q)), q0, 1 - q0)
        ok(f"09 s2 NOR latch S={s} R={r} Q0={q0} -> Q,Q'={want}", got == want, got)
    seq, q = [], 0
    for s, r in ((1, 0), (0, 0)):
        q, _ = settle(lambda a, b: (nor(r, b), nor(s, a)), q, 1 - q); seq.append(q)
    ok("09 c2a NOR latch Q=0, SR=10,00 -> 1,1", seq == [1, 1])
    seq, q, qb = [], 0, 1
    for s, r in ((1, 0), (0, 0), (0, 1), (0, 0)):
        q, qb = settle(lambda a, b: (nor(r, b), nor(s, a)), q, qb); seq.append(q)
    ok("09 st1 NOR latch SR=10,00,01,00 -> 1,1,0,0", seq == [1, 1, 0, 0], seq)
    # ---- 09 step 3: NAND latch (Q = NAND(S', Q'), Q' = NAND(R', Q))
    nand_tab = {(1, 1): "hold", (1, 0): (0, 1), (0, 1): (1, 0), (0, 0): (1, 1)}
    for (sp, rp), want in nand_tab.items():
        res = {q0: settle(lambda q, qb: (nand(sp, qb), nand(rp, q)), q0, 1 - q0) for q0 in (0, 1)}
        cond = all(res[q0] == (q0, 1 - q0) for q0 in (0, 1)) if want == "hold" else all(v == want for v in res.values())
        ok(f"09 s3 NAND latch S'={sp} R'={rp} -> {want}", cond, res)
    # ---- 09 step 4: gated SR latch from 4 NANDs
    def gated(en, s, r, q0):
        sp, rp = nand(s, en), nand(r, en)
        return settle(lambda q, qb: (nand(sp, qb), nand(rp, q)), q0, 1 - q0)[0]
    ok("09 s4 gated SR: EN=0 holds for all S,R,Q0", all(gated(0, s, r, q0) == q0 for s in (0, 1) for r in (0, 1) for q0 in (0, 1)))
    ok("09 s4 gated SR: EN=1 SR=00 hold, 01 reset, 10 set",
       all(gated(1, 0, 0, q0) == q0 and gated(1, 0, 1, q0) == 0 and gated(1, 1, 0, q0) == 1 for q0 in (0, 1)))
    q = 0; seq = []
    for en, s, r in ((0, 1, 0), (1, 1, 0), (0, 0, 1)):
        q = gated(en, s, r, q); seq.append(q)
    ok("09 c4 gated SR Q=0: (EN,S,R)=010,110,001 -> 0,1,1", seq == [0, 1, 1], seq)
    # ---- 09 step 5: D latch = gated with S=D, R=D'
    dl = lambda en, d, q0: gated(en, d, 1 - d, q0)
    ok("09 s5 D latch: EN=1 Q=D, EN=0 hold", all(dl(1, d, q0) == d and dl(0, d, q0) == q0 for d in (0, 1) for q0 in (0, 1)))
    q = 0; seq = []
    for en, d in ((1, 1), (1, 0), (1, 1), (0, 0)):
        q = dl(en, d, q); seq.append(q)
    ok("09 c5 D latch Q=0: EN=1 D=1,0,1 then EN=0 D=0 -> 1,0,1,1", seq == [1, 0, 1, 1], seq)
    # ---- 09 step 6: clock numbers
    close = lambda a, b: abs(a - b) <= 1e-9 * max(1, abs(b))
    ok("09 s6 guess: 2 µs high in 8 µs -> 25 %, 125 kHz", close(2 / 8, 0.25) and close(1 / 8e-6, 125e3))
    ok("09 s6 1 kHz -> T = 1 ms", close(1 / 1e3, 1e-3))
    ok("09 c6a 50 MHz -> 20 ns", close(1 / 50e6, 20e-9))
    ok("09 c6b 40 ns, 30 ns high -> 25 MHz, 75 %", close(1 / 40e-9, 25e6) and close(30 / 40, 0.75))
    ok("09 st2 40 ns, 10 ns high -> 25 MHz, 25 %", close(1 / 40e-9, 25e6) and close(10 / 40, 0.25))
    # ---- 09 step 7: latch vs flip-flop on figs2 data (8 vs 2 changes)
    import figs2
    lat = qm.compress(qm.d_latch(figs2.W_D, figs2.HIGHS))
    ffq = qm.compress(qm.edge_ff("D", {"D": figs2.W_D}, figs2.RISE))
    ok("09 s7 latch Q changes 8 times, flip-flop 2", (len(lat) - 1, len(ffq) - 1) == (8, 2), (len(lat) - 1, len(ffq) - 1))
    ok("09 s7 the 5.35-5.7 dip lies in the 3rd high time (5,6)", figs2.HIGHS[2] == (5, 6))
    # ---- 09 step 8-10: characteristic tables and equations
    for q0 in (0, 1):
        ok(f"09 s8 SR Q={q0}: 00 hold, 01 reset, 10 set", [ff_next("SR", q0, S=s, R=r) for s, r in ((0, 0), (0, 1), (1, 0))] == [q0, 0, 1])
    eq("09 c8b S=R=0 in S+R'Q", "0 + 1Q", "Q", "Q")
    ok("09 c8a SR Q=1, SR=01 -> 0", ff_next("SR", 1, S=0, R=1) == 0)
    ok("09 c8c D=1,1,0,1 -> 1,1,0,1", edge_seq("D", 0, [{"D": d} for d in (1, 1, 0, 1)]) == [1, 1, 0, 1])
    jk_rows = [m for m in range(8) if ff_next("JK", m & 1, J=m >> 2, K=(m >> 1) & 1)]
    ok("09 s9 JK Q+ = Σm(1,4,5,6) over JKQ", jk_rows == [1, 4, 5, 6], jk_rows)
    check_sop("09 s9 JK Q+ = JQ' + K'Q minimal", "JQ' + K'Q", [1, 4, 5, 6], "JKQ")
    run = [{"J": j, "K": k} for j, k in ((1, 0), (0, 0), (0, 1), (1, 1), (1, 1))]
    ok("09 running example JK Q=0 -> 1,1,0,1,0", edge_seq("JK", 0, run) == [1, 1, 0, 1, 0])
    ok("09 c9a J=K=Q=1 -> 0", ff_next("JK", 1, J=1, K=1) == 0)
    ok("09 c9b Q=1, JK=01,10,11,00 -> 0,1,0,0", edge_seq("JK", 1, [{"J": a, "K": b} for a, b in ((0, 1), (1, 0), (1, 1), (0, 0))]) == [0, 1, 0, 0])
    ok("09 st3 Q=1, JK=11,00,10,01 -> 0,0,1,0", edge_seq("JK", 1, [{"J": a, "K": b} for a, b in ((1, 1), (0, 0), (1, 0), (0, 1))]) == [0, 0, 1, 0])
    eq("09 s10 T: T'Q + TQ' = T⊕Q", "T'Q + TQ'", "T⊕Q", "TQ")
    eq("09 s10 JK with J=K=T gives TQ' + T'Q", "TQ' + (T')Q", "T⊕Q", "TQ")
    ok("09 s10 MTE Q3: T=1 toggles from both states", all(ff_next("T", q0, T=1) == 1 - q0 for q0 in (0, 1)))
    ok("09 c10c Q=0, T=1,0,1,1 -> 1,1,0,1", edge_seq("T", 0, [{"T": t} for t in (1, 0, 1, 1)]) == [1, 1, 0, 1])
    clk = [(0, 0)] + [p for k in range(8) for p in ((2 * k + 1, 1), (2 * k + 2, 0))]
    qa = qm.compress(qm.edge_ff("T", {"T": [(0, 1)]}, [2 * k + 1 for k in range(8)]))
    ok("09 s10 tdiv: Q_A toggles at every ↑ (period = 2 clock periods)", [t for t, _ in qa[1:]] == [1, 3, 5, 7, 9, 11, 13, 15])
    ok("09 s10 1 kHz -> 500 Hz, 250 Hz; c10a 10 kHz -> 5 kHz; c10b 16 kHz /8 -> 2 kHz; 10 st5 8 kHz -> 4 kHz",
       (1000 / 2, 1000 / 4, 10e3 / 2, 16e3 / 2 ** 3, 8e3 / 2) == (500, 250, 5e3, 2e3, 4e3))
    ok("09 s11 1 µs / 20 ns = 50 toggles", round(1e-6 / 20e-9) == 50)
    # ---- 09 step 12: excitation table derived from the characteristic equations
    def excite(kind, q0, q1):
        names = {"SR": "SR", "JK": "JK", "D": "D", "T": "T"}[kind]
        good = [c for c in product((0, 1), repeat=len(names))
                if not (kind == "SR" and c == (1, 1)) and ff_next(kind, q0, **dict(zip(names, c))) == q1]
        return "".join("X" if len({c[i] for c in good}) == 2 else str(good[0][i]) for i in range(len(names)))
    printed = {(0, 0): ("0X", "0X", "0", "0"), (0, 1): ("10", "1X", "1", "1"),
               (1, 0): ("01", "X1", "0", "1"), (1, 1): ("X0", "X0", "1", "0")}
    for (q0, q1), want in printed.items():
        got = tuple(excite(k, q0, q1) for k in ("SR", "JK", "D", "T"))
        ok(f"09 s12 excitation {q0}->{q1}: SR JK D T = {want}", got == want, got)
    # ---- 09 step 13: every conversion, exhaustively
    def conv(label, want, have, logic, ins):
        good = True
        for q0 in (0, 1):
            for c in product((0, 1), repeat=len(ins)):
                e = dict(zip(ins, c)); e["Q"] = q0
                if want == "SR" and e["S"] and e["R"]:
                    continue
                drive = {k: fn(v, list(ins) + ["Q"])(e) for k, v in logic.items()}
                if have == "SR" and drive["S"] and drive["R"]:
                    good = False; continue
                good &= ff_next(have, q0, **drive) == ff_next(want, q0, **{k: e[k] for k in ins})
        ok(f"09 s13 {label}", good)
    conv("SR -> D: S = D, R = D'", "D", "SR", {"S": "D", "R": "D'"}, "D")
    conv("JK -> D: J = D, K = D'", "D", "JK", {"J": "D", "K": "D'"}, "D")
    conv("T -> D: T = D⊕Q", "D", "T", {"T": "D⊕Q"}, "D")
    conv("SR -> JK: S = JQ', R = KQ", "JK", "SR", {"S": "JQ'", "R": "KQ"}, "JK")
    conv("D -> SR: D = S + R'Q", "SR", "D", {"D": "S + R'Q"}, "SR")
    conv("D -> T: D = T⊕Q", "T", "D", {"D": "T⊕Q"}, "T")
    conv("D -> JK: D = JQ' + K'Q", "JK", "D", {"D": "JQ' + K'Q"}, "JK")
    conv("JK -> T: J = K = T", "T", "JK", {"J": "T", "K": "T"}, "T")
    conv("T -> JK: T = JQ' + KQ", "JK", "T", {"T": "JQ' + KQ"}, "JK")
    check_sop("09 s13 J map (DQ): ones m2, X m1,m3 -> J = D", "D", [2], "DQ", dcs=[1, 3])
    check_sop("09 s13 K map (DQ): ones m1, X m0,m2 -> K = D'", "D'", [1], "DQ", dcs=[0, 2])
    check_sop("09 s13 T map (DQ): ones m1,m2 -> D'Q + DQ'", "D'Q + DQ'", [1, 2], "DQ")
    check_sop("09 s13 S map (DQ): ones m2, X m3 -> S = D", "D", [2], "DQ", dcs=[3])
    ok("09 c13b SR->JK at J=K=Q=1: S=0, R=1, Q+=0", (fn("JQ'", "JKQ")({"J": 1, "K": 1, "Q": 1}), fn("KQ", "JKQ")({"J": 1, "K": 1, "Q": 1})) == (0, 1))
    # ---- 10: every waveform answer, own sampler (inputs just before the edge)
    def edges_jk(edges, eps):
        q, out = 0, []
        for t in edges:
            q = ff_next("JK", q, J=lvl(W.J7, t + eps), K=lvl(W.K7, t + eps)); out.append(q)
        return out
    ok("10 s3 MTE Q7 positive edge, just-before: 0,0,0,0,1,0,1", edges_jk(W.RISE7, -1e-6) == [0, 0, 0, 0, 1, 0, 1], edges_jk(W.RISE7, -1e-6))
    ok("10 s2 note MTE Q7 after-edge reading: 1,1,1,1,1,0,1", edges_jk(W.RISE7, 1e-6) == [1, 1, 1, 1, 1, 0, 1], edges_jk(W.RISE7, 1e-6))
    ok("10 s3 JK before ↑1..↑7 = 00,01,00,00,10,01,11",
       [(lvl(W.J7, t - 1e-6), lvl(W.K7, t - 1e-6)) for t in W.RISE7] == [(0, 0), (0, 1), (0, 0), (0, 0), (1, 0), (0, 1), (1, 1)])
    ok("10 s2 coincident: J rises at ↑1, ↑3; K falls at ↑2", (1, 1) in W.J7 and (5, 1) in W.J7 and (3, 0) in W.K7)
    q, st6 = 1, []
    for t in W.RISE7:
        q = ff_next("JK", q, J=lvl(W.J7, t - 1e-6), K=lvl(W.K7, t - 1e-6)); st6.append(q)
    ok("10 c3b / st6 Q0=1: 1,0,0,0,1,0,1", st6 == [1, 0, 0, 0, 1, 0, 1], st6)
    ok("10 s4 PS2 Q3a negative edge: 1,0,1,1,0,0,1", edges_jk(W.FALL7, -1e-6) == [1, 0, 1, 1, 0, 0, 1], edges_jk(W.FALL7, -1e-6))
    ok("10 s4 JK before ↓1..↓7 = 10,01,10,10,11,01,11",
       [(lvl(W.J7, t - 1e-6), lvl(W.K7, t - 1e-6)) for t in W.FALL7] == [(1, 0), (0, 1), (1, 0), (1, 0), (1, 1), (0, 1), (1, 1)])
    # step 7: async (own event loop)
    q, after, ev = 0, [], sorted(set(W.FALL7) | {t for t, _ in W.CLR3B + W.PR3B})
    for t in ev:
        if t in W.FALL7:
            q = ff_next("JK", q, J=lvl(W.J7, t - 1e-6), K=lvl(W.K7, t - 1e-6))
        if lvl(W.CLR3B, t) == 0:
            q = 0
        elif lvl(W.PR3B, t) == 0:
            q = 1
        if t in W.FALL7:
            after.append(q)
    ok("10 s7 PS2 Q3b: 1,0,1,1,0,0,1", after == [1, 0, 1, 1, 0, 0, 1], after)
    ok("10 s7 PR' pulse inside pulse-4 high (7,8); CLR' pulse spans ↑6 (t=11)", 7 < 7.25 < 7.5 < 8 and 10.8 < 11 < 11.5)
    # step 5: D latch, original grid (shift back by 2), Q0 = 1
    qd, tl = 1, []
    for k in range(26):
        t = k + 2 + 0.5  # middle of square k+1
        if lvl(W.EN_D, t):
            qd = lvl(W.D_D, t)
        tl.append(qd)
    want = [0, 0, 1, 1, 0] + [1] * 3 + [0] * 8 + [1] * 10
    ok("10 s5 D latch Q per square: 0 in 1-2, 1 in 3-4, 0 in 5, 1 in 6-8, 0 in 9-16, 1 in 17-26", tl == want, tl)
    ok("10 c5a D flip-flop on EN ↑ (squares 1,9,13,23): 0,0,0,1",
       [lvl(W.D_D, t - 1e-6) for t, v in W.EN_D if v == 1] == [0, 0, 0, 1])
    # step 6: JK latch per square, race when J=K=1 inside a window
    qj, tj = 1, []
    for k in range(26):
        t = k + 2 + 0.5
        if lvl(W.EN_JK, t):
            j, kk = lvl(W.J_JK, t), lvl(W.K_JK, t)
            qj = "race" if j and kk else ff_next("JK", qj if qj != "race" else 0, J=j, K=kk)
        tj.append(qj)
    want = [1] * 3 + [0] * 11 + [1] * 8 + [0] * 2 + ["race"] * 2
    ok("10 s6 JK latch per square: 1 in 1-3, 0 in 4-14, 1 in 15-22, 0 in 23-24, race 25-26", tj == want, tj)
    ok("10 c6b JK flip-flop at last window ↑ (t=22 orig): JK=01 -> 0",
       ff_next("JK", 1, J=lvl(W.J_JK, 24 - 1e-6), K=lvl(W.K_JK, 24 - 1e-6)) == 0)
    # step 1: D flip-flop figure (figs2 data)
    ok("10 s1 D before ↑1..↑6 = 0,0,1,0,0,0", [lvl(figs2.W_D, t - 1e-6) for t in figs2.RISE] == [0, 0, 1, 0, 0, 0])
    ok("10 c1a D before ↓1..↓6 = 1,0,1,0,1,0", [lvl(figs2.W_D, t - 1e-6) for t in figs2.FALL] == [1, 0, 1, 0, 1, 0])
    ok("10 st1 D 1,0,0,1 -> 1,0,0,1; st2 T neg Q0=1 1,1,0,1 -> 0,1,1,0; st3 SR 10,00,01,00 -> 1,1,0,0",
       edge_seq("D", 0, [{"D": d} for d in (1, 0, 0, 1)]) == [1, 0, 0, 1]
       and edge_seq("T", 1, [{"T": t} for t in (1, 1, 0, 1)]) == [0, 1, 1, 0]
       and edge_seq("SR", 0, [{"S": s, "R": r} for s, r in ((1, 0), (0, 0), (0, 1), (0, 0))]) == [1, 1, 0, 0])


UNITS = {"u0": u0, "u1": u1, "u3": u3}


def main(argv):
    print("== Part 0: v1 checks (study-pack/pdf-ete/verify.py)")
    r = subprocess.run([sys.executable, "verify.py"], cwd=V1, capture_output=True, text=True, encoding="utf-8")
    n_ok = sum(1 for line in r.stdout.splitlines() if line.startswith("ok"))
    ok(f"v1 verify.py exits 0 ({n_ok} v1 checks pass)", r.returncode == 0, (r.stdout + r.stderr)[-600:])
    for name in (argv or list(UNITS)):
        print(f"== {name}")
        UNITS[name]()
    print(f"\n{N[0]} checks, {len(FAILS)} failures" + ("" if not FAILS else ": " + "; ".join(FAILS)))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
