"""Checker for every tree / heap / expression / graph answer in dsa-instrV2.md.
Run: python verify_dsa.py   (prints all traces the chat file quotes)."""
import heapq

# ---------------- BST ----------------
class N:
    def __init__(s, k): s.k, s.l, s.r, s.h, s.red = k, None, None, 1, True

def bst_insert(t, k):
    if t is None: return N(k)
    if k < t.k: t.l = bst_insert(t.l, k)
    else: t.r = bst_insert(t.r, k)
    return t

def pre(t):  return [] if t is None else [t.k] + pre(t.l) + pre(t.r)
def ino(t):  return [] if t is None else ino(t.l) + [t.k] + ino(t.r)
def post(t): return [] if t is None else post(t.l) + post(t.r) + [t.k]
def size(t): return 0 if t is None else 1 + size(t.l) + size(t.r)
def height(t): return 0 if t is None else 1 + max(height(t.l), height(t.r))  # nodes on longest path

def levels(t):
    out, q = [], [(t, 0)]
    while q:
        n, d = q.pop(0)
        if n is None: continue
        while len(out) <= d: out.append([])
        out[d].append(n.k)
        q += [(n.l, d + 1), (n.r, d + 1)]
    return out

def shape(t):  # parent -> (left, right)
    if t is None: return {}
    d = {t.k: (t.l.k if t.l else '-', t.r.k if t.r else '-')}
    d.update(shape(t.l)); d.update(shape(t.r)); return d

def bst_delete(t, k):
    if t is None: return None
    if k < t.k: t.l = bst_delete(t.l, k)
    elif k > t.k: t.r = bst_delete(t.r, k)
    else:
        if t.l is None: return t.r
        if t.r is None: return t.l
        s = t.r
        while s.l: s = s.l
        t.k = s.k; t.r = bst_delete(t.r, s.k)
    return t

# ---------------- AVL ----------------
def h(n): return n.h if n else 0
def upd(n): n.h = 1 + max(h(n.l), h(n.r))
def bf(n): return h(n.l) - h(n.r)
def rr(y):  # right rotation
    x = y.l; y.l = x.r; x.r = y; upd(y); upd(x); return x
def lr(x):  # left rotation
    y = x.r; x.r = y.l; y.l = x; upd(x); upd(y); return y

LOG = []
def avl_insert(t, k):
    if t is None: return N(k)
    if k < t.k: t.l = avl_insert(t.l, k)
    else: t.r = avl_insert(t.r, k)
    upd(t); b = bf(t)
    if b > 1 and k < t.l.k: LOG.append(f"LL at {t.k} -> right rotate {t.k}"); return rr(t)
    if b < -1 and k > t.r.k: LOG.append(f"RR at {t.k} -> left rotate {t.k}"); return lr(t)
    if b > 1: LOG.append(f"LR at {t.k} -> left rotate {t.l.k}, then right rotate {t.k}"); t.l = lr(t.l); return rr(t)
    if b < -1: LOG.append(f"RL at {t.k} -> right rotate {t.r.k}, then left rotate {t.k}"); t.r = rr(t.r); return lr(t)
    return t

def bfs_all(t):
    out, q = {}, [t]
    while q:
        n = q.pop(0)
        if n: out[n.k] = bf(n); q += [n.l, n.r]
    return out

def avl_run(keys, title):
    print(f"\n=== AVL {title}: {keys}")
    t = None
    for k in keys:
        LOG.clear(); t = avl_insert(t, k)
        print(f"  +{k}: {'; '.join(LOG) if LOG else 'no rotation'} | levels {levels(t)}")
    print("  final shape", shape(t)); print("  BF", bfs_all(t))
    print("  pre", pre(t), "in", ino(t), "post", post(t))
    return t

# ---------------- Red-Black (CLRS insert) ----------------
class RB:
    def __init__(s): s.root = None
    def rot_l(s, x):
        y = x.r; x.r = y.l
        if y.l: y.l.p = x
        y.p = x.p
        if x.p is None: s.root = y
        elif x is x.p.l: x.p.l = y
        else: x.p.r = y
        y.l = x; x.p = y
    def rot_r(s, x):
        y = x.l; x.l = y.r
        if y.r: y.r.p = x
        y.p = x.p
        if x.p is None: s.root = y
        elif x is x.p.r: x.p.r = y
        else: x.p.l = y
        y.r = x; x.p = y
    def insert(s, k):
        z = N(k); z.p = None; y = None; x = s.root
        while x: y = x; x = x.l if k < x.k else x.r
        z.p = y
        if y is None: s.root = z
        elif k < y.k: y.l = z
        else: y.r = z
        ev = []
        while z.p and z.p.red:
            g = z.p.p
            if z.p is g.l:
                u = g.r
                if u and u.red:
                    ev.append(f"uncle {u.k} red -> recolour {z.p.k},{u.k} black, {g.k} red"); z.p.red = u.red = False; g.red = True; z = g
                else:
                    if z is z.p.r: ev.append(f"triangle -> left rotate {z.p.k}"); z = z.p; s.rot_l(z)
                    ev.append(f"line -> right rotate {g.k}, swap colours"); z.p.red = False; g.red = True; s.rot_r(g)
            else:
                u = g.l
                if u and u.red:
                    ev.append(f"uncle {u.k} red -> recolour {z.p.k},{u.k} black, {g.k} red"); z.p.red = u.red = False; g.red = True; z = g
                else:
                    if z is z.p.l: ev.append(f"triangle -> right rotate {z.p.k}"); z = z.p; s.rot_r(z)
                    ev.append(f"line -> left rotate {g.k}, swap colours"); z.p.red = False; g.red = True; s.rot_l(g)
        if s.root.red: ev.append("root red -> black")
        s.root.red = False
        return ev

def rb_levels(t):
    out, q = [], [(t, 0)]
    while q:
        n, d = q.pop(0)
        if n is None: continue
        while len(out) <= d: out.append([])
        out[d].append(f"{n.k}{'R' if n.red else 'B'}")
        q += [(n.l, d + 1), (n.r, d + 1)]
    return out

def rb_run(keys, title):
    print(f"\n=== RB {title}: {keys}")
    T = RB()
    for k in keys:
        ev = T.insert(k)
        print(f"  +{k}: {'; '.join(ev) if ev else 'parent black, done'} | {rb_levels(T.root)}")

# ---------------- Heap ----------------
def heap_delete_max(a):
    a = a[:]; steps = []
    top = a[0]; a[0] = a.pop(); i = 0; steps.append(f"move last ({a[0]}) to root: {a}")
    while True:
        l, r, big = 2 * i + 1, 2 * i + 2, i
        if l < len(a) and a[l] > a[big]: big = l
        if r < len(a) and a[r] > a[big]: big = r
        if big == i: break
        steps.append(f"swap {a[i]} with larger child {a[big]}")
        a[i], a[big] = a[big], a[i]; i = big
        steps[-1] += f": {a}"
    return top, a, steps

def heap_insert_max(a, k):
    a = a[:] + [k]; i = len(a) - 1; steps = [f"append {k}: {a}"]
    while i and a[(i - 1) // 2] < a[i]:
        p = (i - 1) // 2; a[i], a[p] = a[p], a[i]; steps.append(f"swap with parent: {a}"); i = p
    return a, steps

# ---------------- Expressions ----------------
PREC = {'!': 5, '^': 4, '*': 3, '/': 3, '<': 2, '>': 2, '+': 2.5, '-': 2.5, '&&': 1, '||': 0}
RIGHT = {'^', '!'}
def tok(s):
    s = s.replace(' ', '').replace('×', '*').replace('−', '-'); out = []; i = 0
    while i < len(s):
        if s[i:i + 2] in ('&&', '||'): out.append(s[i:i + 2]); i += 2
        else: out.append(s[i]); i += 1
    # implicit multiplication: ")(" or ")X"
    fixed = []
    for t in out:
        if fixed and (fixed[-1] == ')' or fixed[-1].isalnum()) and (t == '(' or t.isalnum()):
            fixed.append('*')
        fixed.append(t)
    return fixed

def to_postfix(s, show=False):
    out, st, rows = [], [], []
    for t in tok(s):
        if t.isalnum(): out.append(t)
        elif t == '(': st.append(t)
        elif t == ')':
            while st[-1] != '(': out.append(st.pop())
            st.pop()
        else:
            while st and st[-1] != '(' and (PREC[st[-1]] > PREC[t] or (PREC[st[-1]] == PREC[t] and t not in RIGHT)):
                out.append(st.pop())
            st.append(t)
        rows.append((t, ''.join(st), ' '.join(out)))
    while st: out.append(st.pop())
    rows.append(('end', '', ' '.join(out)))
    if show:
        for r in rows: print(f"    {r[0]:>3} | stack {r[1]:<8} | out {r[2]}")
    return out

def postfix_to_tree(pf):
    st = []
    for t in pf:
        if t.isalnum(): st.append(t)
        elif t == '!': st.append((t, st.pop()))
        else: b = st.pop(); a = st.pop(); st.append((t, a, b))
    assert len(st) == 1, f"invalid: leftover {st}"
    return st[0]

def prefix_of(n):
    if isinstance(n, str): return [n]
    return [n[0]] + sum((prefix_of(c) for c in n[1:]), [])

def eval_postfix(pf):
    st = []
    for t in pf.split():
        if t.lstrip('-').isdigit(): st.append(int(t))
        else:
            b = st.pop(); a = st.pop()
            st.append({'+': a + b, '-': a - b, '*': a * b, '/': a / b}[t])
        print(f"    {t:>2} -> {st}")
    return st[0]

def check_postfix_valid(s):
    depth = 0
    for i, c in enumerate(s):
        if c.isalpha(): depth += 1
        else:
            if depth < 2: return f"INVALID at symbol {i+1} '{c}': stack holds {depth} operand(s)"
            depth -= 1
    return "valid" if depth == 1 else f"INVALID: {depth} operands left at end"

def check_prefix_valid(s):
    need = 1
    for i, c in enumerate(s):
        if need == 0: return f"INVALID: expression complete after {i} symbols, '{s[i:]}' left over"
        need += 1 if not c.isalpha() else -1
    return "valid" if need == 0 else f"INVALID: needs {need} more operands"

# ---------------- Graphs ----------------
def graph(edges):
    g = {}
    for u, v, w in edges:
        g.setdefault(u, []).append((v, w)); g.setdefault(v, []).append((u, w))
    for u in g: g[u].sort()
    return g

def dijkstra(g, s):
    dist = {v: float('inf') for v in g}; par = {v: '-' for v in g}; dist[s] = 0; done = []
    print(f"  {'pick':>4} | " + ' '.join(f"{v:>5}" for v in sorted(g)))
    while len(done) < len(g):
        u = min((v for v in g if v not in done), key=lambda v: (dist[v], v)); done.append(u)
        for v, w in g[u]:
            if v not in done and dist[u] + w < dist[v]: dist[v] = dist[u] + w; par[v] = u
        print(f"  {u:>4} | " + ' '.join(f"{(str(dist[v]) if dist[v] < 1e9 else 'inf') + ('*' if v in done else ''):>5}" for v in sorted(g)))
    print("  parents", par); return dist, par

def prim(g, s):
    key = {v: float('inf') for v in g}; par = {v: '-' for v in g}; key[s] = 0; inn = []; tot = 0
    while len(inn) < len(g):
        u = min((v for v in g if v not in inn), key=lambda v: (key[v], v)); inn.append(u); tot += key[u]
        if par[u] != '-': print(f"  add {par[u]}-{u} ({key[u]})")
        for v, w in g[u]:
            if v not in inn and w < key[v]: key[v] = w; par[v] = u
        print(f"     in={inn} key=" + str({v: key[v] if key[v] < 1e9 else 'inf' for v in sorted(g) if v not in inn}))
    print("  Prim total", tot)

def kruskal(edges):
    p = {}
    def f(x):
        p.setdefault(x, x)
        while p[x] != x: x = p[x]
        return x
    tot = 0; n = len({x for e in edges for x in e[:2]}); k = 0
    for u, v, w in sorted(edges, key=lambda e: (e[2], e[0], e[1])):
        if k == n - 1: print(f"  {u}-{v} {w}: not needed (MST complete)"); continue
        if f(u) != f(v): p[f(u)] = f(v); tot += w; k += 1; print(f"  {u}-{v} {w}: ACCEPT")
        else: print(f"  {u}-{v} {w}: REJECT (cycle)")
    print("  Kruskal total", tot)

def bfs(g, s):
    seen, q, order, tree = {s}, [s], [], []
    print("  BFS queue states:")
    while q:
        u = q.pop(0); order.append(u)
        for v, _ in g[u]:
            if v not in seen: seen.add(v); q.append(v); tree.append(f"{u}-{v}")
        print(f"    visit {u}: queue {q}")
    print("  BFS order", order, "tree", tree)

def dfs(g, s):
    seen, order, tree, st = {s}, [s], [], [s]
    print("  DFS stack states:")
    print(f"    visit {s}: stack {st}")
    while st:
        u = st[-1]
        nxt = [v for v, _ in g[u] if v not in seen]
        if nxt:
            v = nxt[0]; seen.add(v); order.append(v); tree.append(f"{u}-{v}"); st.append(v); print(f"    visit {v}: stack {st}")
        else:
            st.pop(); print(f"    backtrack from {u}: stack {st}")
    print("  DFS order", order, "tree", tree)

# ---------------- run everything ----------------
if __name__ == '__main__':
    print("=== BST ETE26 Q11")
    t = None
    for k in [45, 36, 76, 23, 89, 115, 98, 39, 41, 56, 69, 48]: t = bst_insert(t, k)
    print(" levels", levels(t)); print(" shape", shape(t))
    print(" pre", pre(t)); print(" in ", ino(t)); print(" post", post(t)); print(" height(nodes)", height(t))

    print("\n=== BST ETE25 Q7-9")
    t = None
    for k in [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]: t = bst_insert(t, k)
    print(" levels", levels(t)); print(" shape", shape(t))
    print(" pre", pre(t)); print(" in ", ino(t)); print(" post", post(t))
    print(" left subtree", size(t.l), "right subtree", size(t.r), "total", size(t))
    print(" delete 15 (two children):"); t = bst_delete(t, 15); print("  levels", levels(t))

    print("\n=== BST 50Q-35 deletes")
    t = None
    for k in [60, 40, 80, 20, 50, 70, 90, 10, 30, 45, 55, 65, 75, 85, 95]: t = bst_insert(t, k)
    t = bst_delete(t, 10); print(" -10", levels(t))
    t = bst_delete(t, 20); print(" -20", levels(t))
    t = bst_delete(t, 60); print(" -60", levels(t))

    avl_run([9, 27, 50, 15, 2, 21, 36], "ETE26 Q9")
    avl_run([1, 2, 3], "try RR")
    avl_run([30, 10, 20], "try LR")
    avl_run([24, 12, 36, 8, 16, 30, 42, 4, 10, 14, 20, 28, 34], "booklet Q44")
    avl_run([50, 25, 75, 15, 35, 60, 90, 10, 20, 30, 40, 55, 65], "booklet Q45")
    avl_run([10, 20, 30, 40, 50, 25], "classic")

    rb_run([10, 20, 30, 15, 25, 5], "short")
    rb_run([22, 11, 33, 5, 17, 27, 44, 3, 8, 14, 19, 38, 50], "booklet Q54")
    rb_run([1, 2, 3, 4, 5], "deck sorted")

    print("\n=== Heap ETE26 Q10")
    H = [90, 89, 70, 36, 85, 63, 65, 21, 18, 15, 75]
    top, a, st = heap_delete_max(H)
    for s in st: print("  ", s)
    print("  final", a)
    print("  insert 95 into original:")
    for s in heap_insert_max(H, 95)[1]: print("  ", s)

    print("\n=== Expressions")
    e = "((A + B × C)(D − E / (F + G))) × (H + I / (J − K × L))"
    pf = to_postfix(e); print(" ETE26 Q12 postfix:", ' '.join(pf)); print(" prefix:", ' '.join(prefix_of(postfix_to_tree(pf))))
    e = "((!(A && !((B < C) || (C > D))) || (C < E)) && (F && G || H || I))"
    pf = to_postfix(e); print(" ETE25 Q10 postfix:", ' '.join(pf)); print(" prefix:", ' '.join(prefix_of(postfix_to_tree(pf))))
    s = "+AB^CD*EF+GH*I/J+KL-MN+OP/"
    print(" ETE25 Q11 as postfix:", check_postfix_valid(s)); print("            as prefix:", check_prefix_valid(s))
    print(" 50Q-26 (A+B)*(C-D)/E:"); pf = to_postfix("(A+B)*(C-D)/E", show=True)
    print("   prefix:", ' '.join(prefix_of(postfix_to_tree(pf))))
    print(" A+B*C-D:"); pf = to_postfix("A+B*C-D", show=True); print("   prefix", ' '.join(prefix_of(postfix_to_tree(pf))))
    print(" A1 ((A+B)/C)(D-E):", ' '.join(to_postfix("((A+B)/C)(D-E)")))
    print(" 50Q-27 eval 8 3 2 * + 5 1 - /:"); print("  =", eval_postfix("8 3 2 * + 5 1 - /"))
    print(" A1 eval 12 3 4 * + 6 2 / -:"); print("  =", eval_postfix("12 3 4 * + 6 2 / -"))
    print("\n=== Graph G1 (booklet Q103)")
    G1 = [('A','B',5),('A','C',2),('B','C',1),('B','D',6),('C','D',4),('C','E',8),('D','E',2),('D','F',7),('E','F',3),('E','G',6),('F','G',1)]
    g = graph(G1); dijkstra(g, 'A'); bfs(g, 'A'); dfs(g, 'A')
    print("\n=== Graph G2 (booklet Q77)")
    G2 = [('A','B',16),('A','C',9),('B','F',10),('B','C',7),('B','D',25),('C','F',8),('E','F',5),('C','E',15),('C','D',14)]
    g2 = graph(G2); prim(g2, 'A'); kruskal(G2)
    print("  Prim from E:"); prim(g2, 'E')
    print("\n=== Huffman a5 b9 c12 d13 e16 f45 / hashing mod 10")
    f = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    hq = [(w, i, k) for i, (k, w) in enumerate(f.items())]; heapq.heapify(hq); cnt = len(hq)
    codes = {k: '' for k in f}; grp = {k: [k] for k in f}
    while len(hq) > 1:
        w1, _, a = heapq.heappop(hq); w2, _, b = heapq.heappop(hq)
        for x in grp[a]: codes[x] = '0' + codes[x]
        for x in grp[b]: codes[x] = '1' + codes[x]
        grp[a + b] = grp[a] + grp[b]; heapq.heappush(hq, (w1 + w2, cnt, a + b)); cnt += 1
    print(" ", codes, "total bits", sum(f[k] * len(codes[k]) for k in f))
    T = [None] * 10
    for k in [23, 43, 13, 27, 37]:
        i = k % 10
        while T[i] is not None: i = (i + 1) % 10
        T[i] = k
    print("  table", T)

# ---------------- assignment / booklet keys ----------------
def build(keys):
    t = None
    for k in keys: t = bst_insert(t, k)
    return t

def rebuild(preo, ino_):
    if not preo: return None
    r = N(preo[0]); i = ino_.index(preo[0])
    r.l = rebuild(preo[1:i + 1], ino_[:i]); r.r = rebuild(preo[i + 1:], ino_[i + 1:]); return r

def search_path(t, k):
    p = []
    while t:
        p.append(t.k)
        if k == t.k: return p, True
        t = t.l if k < t.k else t.r
    return p, False

def keys_section():
    print("\n=== 50Q-32 letters"); t = build(list("MGTDJPWBFHKNRUY"))
    print(" levels", levels(t)); print(" pre", ''.join(pre(t)), "in", ''.join(ino(t)), "post", ''.join(post(t)))
    print("=== 50Q-33"); t = build([45, 25, 65, 15, 35, 55, 75, 10, 20, 30, 40, 50, 60, 70, 80, 5, 18])
    print(" levels", levels(t), "min", ino(t)[0], "max", ino(t)[-1], "height(edges)", height(t) - 1)
    print("=== 50Q-34"); t = build(list("CAFBEHDGI")); print(" levels", levels(t), "G", search_path(t, 'G'), "Z", search_path(t, 'Z'))
    print("=== 50Q-36"); t = rebuild(list("ABDECFG"), list("DBEAFCG")); print(" levels", levels(t), "post", ''.join(post(t)))
    print("=== 50Q-44"); t = rebuild(list("RKDFMPZX"), list("DKFRMPXZ")); print(" shape", shape(t), "post", ''.join(post(t)))
    print("=== 50Q-46"); t = build(list("SKWDNUZAFMPTVXYCEGLO")); print(" levels", levels(t))
    print(" pre", ''.join(pre(t)), "in", ''.join(ino(t)), "post", ''.join(post(t)), "V", search_path(t, 'V'))
    for k in "DSW": t = bst_delete(t, k); print(f" -{k}", levels(t))
    avl_run([40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35, 45, 55, 65, 75, 1, 8], "50Q-37")
    avl_run(list("HDLBFJNACEGIKMO"), "50Q-38")
    avl_run(list("ACEGIKMOQSUWYBDFHJLN"), "50Q-49")
    rb_run([10, 20, 30, 15, 25, 5, 1, 8, 12, 18, 22, 28, 35, 40, 32], "50Q-41")
    print("\n=== booklet 34-43 (prefix / postfix / value)")
    for e in ["(20+5*(8-3))/(6+2)", "50/(10-2*(3+1))+7", "100/5*(4+2)-(8/2+3)", "(15-(3+2)*4)/(7-(6/3))",
              "40-(12/(3+1)*2)+(8-5*2)", "25+(8*(6-2))/(4+2)", "(18+6)/(4-2)*(7+3)", "(20-(8+2))*(15/(3+2))",
              "50-(10+5*(8-3))/(6-2)", "100/5*(2+3)-8*(4-1)"]:
        import re
        names = {}; s = re.sub(r'\d+', lambda m: names.setdefault(m.group(), chr(ord('a') + len(names))), e)
        back = {v: k for k, v in names.items()}
        pf = to_postfix(s); tree = postfix_to_tree(pf)
        print(f" {e}\n   postfix: {' '.join(back.get(x, x) for x in pf)}\n   prefix:  {' '.join(back.get(x, x) for x in prefix_of(tree))}\n   value:   {eval(e)}")

keys_section()
