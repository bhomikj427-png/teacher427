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


UNITS = {"u0": u0}


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
