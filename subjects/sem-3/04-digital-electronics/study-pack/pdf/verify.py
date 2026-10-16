"""Machine-checks every worked answer in DE-v1.pdf. Run: python verify.py"""
from itertools import combinations, product

def primes(ones, dcs, n):
    terms = {(m, 0) for m in ones | dcs}           # (value, mask of eliminated bits)
    allp = set()
    while terms:
        nxt, used = set(), set()
        for a, b in combinations(terms, 2):
            if a[1] == b[1]:
                d = a[0] ^ b[0]
                if d and d & (d - 1) == 0:
                    nxt.add((a[0] & ~d, a[1] | d)); used |= {a, b}
        allp |= terms - used; terms = nxt
    return allp

def covers(t, m): return (m & ~t[1]) == t[0]

def minimal(ones, dcs, n):
    P = sorted(primes(set(ones), set(dcs), n))
    for k in range(1, len(P) + 1):
        best = [c for c in combinations(P, k) if all(any(covers(t, m) for t in c) for m in ones)]
        if best:
            return min(best, key=lambda c: sum(n - bin(t[1]).count('1') for t in c)), P
    return (), P

def lit(t, names):
    n = len(names); s = ''
    for i, v in enumerate(names):
        bit = 1 << (n - 1 - i)
        if t[1] & bit: continue
        s += v + ('' if t[0] & bit else "'")
    return s or '1'

def sop(c, names): return ' + '.join(lit(t, names) for t in c) or '0'

out = []
def show(label, ones, dcs, names):
    c, P = minimal(ones, dcs, len(names)); out.append(f"{label} = {sop(c, names)}"); return c, P

# ---- 010 overlapping detector, Mealy: S0=00 S1=01 S2=10 ; inputs (A,B,x)
mealy = {(0,0):{0:((0,1),0),1:((0,0),0)}, (0,1):{0:((0,1),0),1:((1,0),0)}, (1,0):{0:((0,1),1),1:((0,0),0)}}
def tables(fsm, mealy_out=True):
    DA, DB, Z, dc = set(), set(), set(), set()
    for A, B, x in product((0,1), repeat=3):
        m = A<<2 | B<<1 | x
        if (A, B) not in fsm: dc.add(m); continue
        (na, nb), z = fsm[(A, B)][x]
        if na: DA.add(m)
        if nb: DB.add(m)
        if z: Z.add(m)
    return DA, DB, Z, dc
DA, DB, Z, dc = tables(mealy)
show("Mealy DA", DA, dc, "ABx"); show("Mealy DB", DB, dc, "ABx"); show("Mealy z", Z, dc, "ABx")
# simulate
def run_mealy(bits):
    s, zs = (0,0), []
    for b in bits:
        (s, z) = mealy[s][b]; zs.append(z)
    return zs
seq = [0,1,0,1,0,0,1,0,1,1,0,1,0]
ref = [1 if i>=2 and seq[i-2:i+1]==[0,1,0] else 0 for i in range(len(seq))]
assert run_mealy(seq) == ref, (run_mealy(seq), ref)
out.append(f"Mealy sim x={''.join(map(str,seq))} z={''.join(map(str,run_mealy(seq)))} OK")
# Moore: S0=00 S1=01 S2=10 S3=11 (z=1)
moore = {(0,0):{0:((0,1),0),1:((0,0),0)}, (0,1):{0:((0,1),0),1:((1,0),0)},
         (1,0):{0:((1,1),0),1:((0,0),0)}, (1,1):{0:((0,1),0),1:((1,0),0)}}
DA, DB, _, dc = tables(moore)
show("Moore DA", DA, dc, "ABx"); show("Moore DB", DB, dc, "ABx")
def run_moore(bits):
    s, zs = (0,0), []
    for b in bits:
        s = moore[s][b][0]; zs.append(int(s == (1,1)))
    return zs
assert run_moore(seq) == ref
out.append("Moore sim OK (z = AB, appears after the edge that completes 010)")

# ---- Anna-2021 15(b): f = ΠM(0,2,6,7,8,10,12) -> hazard-free SOP
zeros = {0,2,6,7,8,10,12}; ones = set(range(16)) - zeros
c, P = show("f minimal", ones, set(), "ABCD")
out.append("f primes: " + ', '.join(lit(t, "ABCD") for t in P))
# hazard check: every adjacent pair of 1s inside one product of the cover
def hazards(cover):
    bad = []
    for m in ones:
        for b in range(4):
            n = m ^ (1 << b)
            if n in ones and m < n and not any(covers(t, m) and covers(t, n) for t in cover):
                bad.append((m, n))
    return bad
out.append(f"static-1 hazards in minimal cover: {hazards(c)}")
fix = list(c)
for m, n in hazards(c):
    t = next(t for t in P if covers(t, m) and covers(t, n))
    if t not in fix: fix.append(t)
assert not hazards(fix)
out.append("hazard-free f = " + sop(fix, "ABCD"))

# ---- LFSR 3-bit, x^3 + x + 1 (Fibonacci: shift right, new Q1 = Q2 xor Q3)
s = (1,0,0); seen = []
while s not in seen:
    seen.append(s); s = (s[1] ^ s[2], s[0], s[1])
out.append("LFSR states Q1Q2Q3: " + ' '.join(''.join(map(str,x)) for x in seen) + f"  period={len(seen)}")
assert len(seen) == 7
# 4-bit Johnson
s = (0,0,0,0); seen = []
while s not in seen:
    seen.append(s); s = (1 - s[3], s[0], s[1], s[2])
out.append("Johnson-4: " + ' '.join(''.join(map(str,x)) for x in seen) + f"  mod={len(seen)}")
assert len(seen) == 8

# ---- state reduction example (partition refinement)
T = {'a':('a','b',0,0), 'b':('c','d',0,0), 'c':('a','d',0,0), 'd':('e','f',0,1),
     'e':('a','f',0,1), 'f':('g','f',0,1), 'g':('a','f',0,1)}   # next(x=0), next(x=1), z(x=0), z(x=1)
blocks = {}
for s_, v in T.items(): blocks.setdefault((v[2], v[3]), []).append(s_)
part = list(blocks.values())
while True:
    idx = {s_: i for i, b in enumerate(part) for s_ in b}
    new = []
    for b in part:
        g = {}
        for s_ in b: g.setdefault((idx[T[s_][0]], idx[T[s_][1]]), []).append(s_)
        new += list(g.values())
    if len(new) == len(part): break
    part = new
out.append("reduction partition: " + ' '.join('(' + ''.join(sorted(b)) + ')' for b in part))

# ---- PLA example: F1 = Σm(4,5,7), F2 = Σm(3,5,7) -> share AC
for nm, mts in (("F1", {4,5,7}), ("F2", {3,5,7})):
    show(f"PLA {nm}", mts, set(), "ABC")
# mod-60 FF count
import math; out.append(f"mod-60 FFs = {math.ceil(math.log2(60))}")
# timing
out.append(f"fmax(8+12+3 ns) = {1e3/23:.1f} MHz")
out.append(f"TTL fan-out = {min(16/1.6, 400/40):.0f}; NM_H={2.4-2.0:.1f} V NM_L={0.8-0.4:.1f} V")
out.append(f"ECL NM_H={-0.98+1.105:.3f} NM_L={-1.475+1.63:.3f}")
out.append(f"555 f(R1=1k,R2=10k,C=10nF) = {1.44/((1e3+2*10e3)*10e-9):.0f} Hz, duty={(11e3)/(21e3):.3f}")
out.append(f"ring osc N=5 tpd=2ns: f = {1/(2*5*2e-9)/1e6:.0f} MHz")
print('\n'.join(out))

# ---- EC1201 (Nov/Dec 2021) 14(a)(i): synchronous counter 1,0,2,3,4,8,7,6,5 (repeat), D flip-flops
seqc = [1, 0, 2, 3, 4, 8, 7, 6, 5]
nxt = {s: seqc[(i + 1) % len(seqc)] for i, s in enumerate(seqc)}
dcs = set(range(16)) - set(seqc)
res = []
for b, nm in ((3, "D3"), (2, "D2"), (1, "D1"), (0, "D0")):
    ones = {s for s in seqc if nxt[s] >> b & 1}
    c, _ = minimal(ones, dcs, 4); res.append(f"{nm} = {sop(c, ['Q3','Q2','Q1','Q0'])}")
    # check
    for s in seqc:
        assert any(covers(t, s) for t in c) == bool(nxt[s] >> b & 1)
print("counter 1,0,2,3,4,8,7,6,5:", "; ".join(res))
def nx(s):
    q3, q2, q1, q0 = (s >> 3) & 1, (s >> 2) & 1, (s >> 1) & 1, s & 1
    d3 = q2 & (1 - q1) & (1 - q0); d2 = (q1 & q0) | (q2 & q1) | q3
    d1 = ((1 - q2) & (1 - q0)) | (q2 & q1 & q0); d0 = (q1 & (1 - q0)) | (q2 & (1 - q1) & q0) | q3
    return d3 << 3 | d2 << 2 | d1 << 1 | d0
for s in seqc: assert nx(s) == nxt[s]
print("unused states ->", {u: nx(u) for u in range(9, 16)})
