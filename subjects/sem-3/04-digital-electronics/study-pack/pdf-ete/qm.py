"""Shared logic helpers for verify.py: Quine-McCluskey minimiser, MUX tables, state reduction."""
from itertools import combinations


def primes(ones, dcs):
    terms = {(m, 0) for m in set(ones) | set(dcs)}
    allp = set()
    while terms:
        nxt, used = set(), set()
        for a, b in combinations(terms, 2):
            if a[1] == b[1]:
                d = a[0] ^ b[0]
                if d and d & (d - 1) == 0:
                    nxt.add((a[0] & ~d, a[1] | d)); used |= {a, b}
        allp |= terms - used
        terms = nxt
    return allp


def covers(t, m):
    return (m & ~t[1]) == t[0]


def minimal_all(ones, dcs, n):
    """Every minimum cover (fewest terms, then fewest literals) as tuples of (value, mask)."""
    P = [p for p in sorted(primes(ones, dcs)) if any(covers(p, m) for m in ones)]
    for k in range(0, len(P) + 1):
        best = [c for c in combinations(P, k) if all(any(covers(t, m) for t in c) for m in ones)]
        if best:
            cost = lambda c: sum(n - bin(t[1]).count("1") for t in c)
            mn = min(map(cost, best))
            return [c for c in best if cost(c) == mn]
    return [()]


def lit(t, names, pos=False):
    n = len(names)
    s = []
    for i, v in enumerate(names):
        bit = 1 << (n - 1 - i)
        if t[1] & bit:
            continue
        one = bool(t[0] & bit)
        s.append(v + ("" if one != pos else "'"))
    if pos:
        return "(" + " + ".join(s) + ")"
    return "".join(s) or "1"


def norm(expr):
    """Order-independent form of an SOP/POS string, for comparing with printed answers."""
    e = expr.replace(" ", "")
    if e.startswith("("):
        return frozenset(frozenset(_lits(t.replace("+", ""))) for t in e.strip("()").split(")("))
    return frozenset(frozenset(_lits(t)) for t in e.split("+"))


def _lits(t):
    out, i = [], 0
    while i < len(t):
        j = i + 1
        while j < len(t) and (t[j].isdigit() or t[j] == "'"):
            j += 1
        out.append(t[i:j]); i = j
    return out


def sop(ones, dcs, names):
    return [" + ".join(lit(t, names) for t in c) or "0" for c in minimal_all(ones, dcs, len(names))]


def pos(ones, dcs, names):
    n = len(names)
    zeros = [m for m in range(2 ** n) if m not in ones and m not in dcs]
    return ["".join(lit(t, names, pos=True) for t in c) for c in minimal_all(zeros, dcs, n)]


def mux(ones, n, nsel):
    """Data-input truth columns: for each select code, the tuple of F over the leftover variables."""
    rest = n - nsel
    return [tuple(int((i << rest | r) in ones) for r in range(2 ** rest)) for i in range(2 ** nsel)]


def mux1(ones, names):
    """n variables on a 2^(n-1):1 MUX; the last variable is the leftover."""
    x = names[-1]
    return [{(0, 0): "0", (1, 1): "1", (0, 1): x, (1, 0): x + "'"}[v] for v in mux(ones, len(names), len(names) - 1)]


def reduce_states(tbl):
    """tbl: {state: ((next, out) per input)} -> list of successive partitions."""
    blocks = {}
    for s, row in tbl.items():
        blocks.setdefault(tuple(o for _, o in row), []).append(s)
    part = sorted(blocks.values())
    hist = [part]
    while True:
        idx = {s: i for i, b in enumerate(part) for s in b}
        new = []
        for b in part:
            sub = {}
            for s in b:
                sub.setdefault(tuple(idx[n] for n, _ in tbl[s]), []).append(s)
            new += sorted(sub.values())
        new = sorted(new)
        if new == part:
            return hist
        part = new
        hist.append(part)


# ------------------------------------------------------------------ flip-flop waveform simulation
def level(pts, t):
    """Value at time t of a piecewise-constant signal given as [(time, value), ...]."""
    v = pts[0][1]
    for tt, vv in pts:
        if tt <= t:
            v = vv
    return v


def edge_ff(kind, ins, edges, q0=0):
    """Q breakpoints of an edge-triggered flip-flop. ins: dict of input signals; sampled just before each edge."""
    q, out = q0, [(0, q0)]
    for t in edges:
        s = {k: level(v, t - 1e-6) for k, v in ins.items()}
        if kind == "D":
            q = s["D"]
        elif kind == "T":
            q ^= s["T"]
        elif kind == "JK":
            q = (s["J"] & (1 - q)) | ((1 - s["K"]) & q)
        out.append((t, q))
    return out


def d_latch(d, highs, q0=0):
    """Q breakpoints of a D latch that is transparent during the [a, b) intervals in highs."""
    q, out = q0, [(0, q0)]
    for a, b in highs:
        times = sorted({a} | {t for t, _ in d if a < t < b})
        for t in times:
            q = level(d, t)
            out.append((t, q))
    return out


def compress(pts):
    out = [pts[0]]
    for t, v in pts[1:]:
        if v != out[-1][1]:
            out.append((t, v))
    return out
