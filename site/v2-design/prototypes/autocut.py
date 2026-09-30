"""Automatic chaptering + trunk choice (SITE-V2-DRAFT §6). No learner input.

Input: concepts, flow edges. Output: ordered chapters, each within the load cap, such that
  * every prerequisite sits in the same or an earlier chapter (so the chapter graph flows one way),
  * few edges cross chapter boundaries (natural seams),
  * chapter 1 is the trunk: the base the subject starts from.

Algorithm
  1. validate: unique ids, edges reference real concepts, flow edges acyclic (Kahn).
  2. order: a topological sort that keeps KB topics together (the "textbook as tie-breaker" hint) and takes
     topics in flow order (shallowest first).
  3. split that order into chapters by dynamic programming: minimise edges crossing chapter boundaries + a
     penalty per mixed topic, with every chapter in [MIN, CAP]. Optimal for the given order.
  4. refine: move single concepts between chapters when that cuts fewer edges, keeping order validity and
     the size bounds.
  5. name each chapter from its dominant KB topics; colour it from its dominant stage.
"""
from collections import Counter, defaultdict

CAP = 9   # design parameter (draft §6.4), not an evidence claim: one L1 screen
MIN = 5

STAGE_OF_TOPIC = {
    "Numbers & codes": "found", "Gates": "found", "Boolean algebra": "found", "K-maps": "found",
    "Combinational design": "comb", "Adders": "comb", "Comparators": "comb", "MUX / DEMUX": "comb",
    "Decoder / encoder": "comb", "Display": "comb", "Shifter / ALU": "comb",
    "Latches": "seq", "Flip-flops": "seq", "Counters": "seq", "Shift registers": "seq", "Timing": "seq",
    "State machines": "seq",
    "Logic families": "phys", "Memories & PLDs": "phys",
}
STAGES = [
    {"id": "found", "title": "Foundations", "hue": "blue"},
    {"id": "comb", "title": "Building blocks", "hue": "green"},
    {"id": "seq", "title": "Memory", "hue": "violet"},
    {"id": "phys", "title": "Silicon", "hue": "amber"},
]


class GraphError(Exception):
    pass


def validate(concepts, edges):
    ids = [c["id"] for c in concepts]
    dup = [k for k, v in Counter(ids).items() if v > 1]
    if dup:
        raise GraphError(f"duplicate concept ids: {dup}")
    known = set(ids)
    for e in edges:
        for end in (e["from"], e["to"]):
            if end not in known:
                raise GraphError(f"edge {e['from']} → {e['to']}: unknown concept {end!r}")
        if not e.get("bridge"):
            raise GraphError(f"edge {e['from']} → {e['to']} has no bridge")
    pairs = Counter((e["from"], e["to"]) for e in edges)
    if any(v > 1 for v in pairs.values()):
        raise GraphError(f"duplicate edges: {[k for k, v in pairs.items() if v > 1]}")
    topo(ids, edges)  # raises on a cycle


def topo(ids, edges, prefer=None):
    """Kahn's algorithm. `prefer` (id → rank) breaks ties; raises GraphError on a cycle."""
    indeg = {i: 0 for i in ids}
    out = defaultdict(list)
    for e in edges:
        if e["from"] in indeg and e["to"] in indeg:
            indeg[e["to"]] += 1
            out[e["from"]].append(e["to"])
    rank = prefer or {i: k for k, i in enumerate(ids)}
    ready = sorted([i for i in ids if indeg[i] == 0], key=rank.get)
    order = []
    while ready:
        n = ready.pop(0)
        order.append(n)
        for m in out[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                ready.append(m)
        ready.sort(key=rank.get)
    if len(order) != len(ids):
        stuck = [i for i in ids if i not in order]
        raise GraphError(f"flow edges contain a cycle through: {stuck}")
    return order


def reach(ids, edges):
    """Number of concepts downstream of each concept (how much of the subject rests on it)."""
    out = defaultdict(set)
    for e in edges:
        out[e["from"]].add(e["to"])
    memo = {}

    def down(n):
        if n not in memo:
            s = set()
            for m in out[n]:
                s |= {m} | down(m)
            memo[n] = s
        return memo[n]
    return {i: len(down(i)) for i in ids}


def depth(ids, edges):
    """Longest path from any source: how far down the flow each concept sits."""
    preds = defaultdict(set)
    for e in edges:
        preds[e["to"]].add(e["from"])
    d = {}
    for i in topo(ids, edges):
        d[i] = 1 + max((d[p] for p in preds[i]), default=-1)
    return d


def flow_order(concepts, edges):
    """A topological order that keeps topics together (a locality-preserving sort).

    Stay inside the current topic while any of its concepts is ready; when it runs dry, switch to the ready
    topic that comes first in the syllabus unit order, then highest in the flow (smallest mean depth). Inside a topic, place first what the most of the
    subject rests on (downstream reach)."""
    ids = [c["id"] for c in concepts]
    topic = {c["id"]: c["topic"] for c in concepts}
    preds = defaultdict(set)
    for e in edges:
        preds[e["to"]].add(e["from"])
    d, down = depth(ids, edges), reach(ids, edges)
    members = defaultdict(list)
    for i in ids:
        members[topic[i]].append(i)
    tdepth = {t: sum(d[i] for i in m) / len(m) for t, m in members.items()}
    # syllabus unit of each topic (KB/official order): the teaching-order signal the edges alone can't carry,
    # e.g. U5 logic families only need gates, yet the KB puts them last on purpose (00-map.md).
    unit = {c["id"]: c.get("unit", 0) for c in concepts}
    tunit = {t: Counter(unit[i] for i in m).most_common(1)[0][0] for t, m in members.items()}
    placed, order, cur = set(), [], None
    while len(order) < len(ids):
        ready = [i for i in ids if i not in placed and preds[i] <= placed]
        same = [i for i in ready if topic[i] == cur]
        pool = same or ready
        best = min(pool, key=lambda i: ((0, 0) if same else (tunit[topic[i]], tdepth[topic[i]]),
                                        d[i], -down[i], ids.index(i)))
        cur = topic[best]
        order.append(best)
        placed.add(best)
    return order


def segment(order, edges, topic, cap, min_size, mix_penalty=1.5):
    """Split the linear order into chapters by dynamic programming.

    Cost of a chapter = edges with exactly one end inside it (so every crossing edge is paid twice, once per
    side) + mix_penalty per extra KB topic inside it. Sizes bounded by [min_size, cap]."""
    n = len(order)
    pos = {i: k for k, i in enumerate(order)}
    ends = [(pos[e["from"]], pos[e["to"]]) for e in edges]

    def cost(a, b):  # chapter = order[a:b]
        inside = lambda k: a <= k < b
        c = sum(1 for x, y in ends if inside(x) != inside(y))
        return c + mix_penalty * (len({topic[i] for i in order[a:b]}) - 1)
    INF = float("inf")
    best = [INF] * (n + 1)
    back = [0] * (n + 1)
    best[0] = 0
    for b in range(1, n + 1):
        for a in range(max(0, b - cap), b - min_size + 1):
            if best[a] < INF and best[a] + cost(a, b) < best[b]:
                best[b], back[b] = best[a] + cost(a, b), a
    if best[n] == INF:  # tail too short for min_size: allow it
        return segment(order, edges, topic, cap, 1, mix_penalty)
    cuts, b = [], n
    while b:
        cuts.append((back[b], b))
        b = back[b]
    return [order[a:b] for a, b in reversed(cuts)]


def cut(concepts, edges, cap=CAP, min_size=MIN):
    validate(concepts, edges)
    ids = [c["id"] for c in concepts]
    topic = {c["id"]: c["topic"] for c in concepts}
    preds, succs = defaultdict(set), defaultdict(set)
    for e in edges:
        preds[e["to"]].add(e["from"])
        succs[e["from"]].add(e["to"])

    order = flow_order(concepts, edges)
    chapters = segment(order, edges, topic, cap, min_size)

    # refinement: move single concepts where that cuts fewer edges (order validity + size bounds kept)
    where = {i: k for k, ch in enumerate(chapters) for i in ch}

    def crossing(i, k):
        return sum(1 for p in preds[i] if where[p] != k) + sum(1 for s in succs[i] if where[s] != k)
    improved, rounds = True, 0
    while improved and rounds < 50:
        improved, rounds = False, rounds + 1
        for i in order:
            k = where[i]
            if len(chapters[k]) <= min_size:
                continue
            lo = max([where[p] for p in preds[i]], default=0)
            hi = min([where[s] for s in succs[i]], default=len(chapters) - 1)
            here = crossing(i, k)
            for j in range(lo, hi + 1):
                if j != k and len(chapters[j]) < cap and crossing(i, j) < here:
                    chapters[k].remove(i)
                    chapters[j].append(i)
                    where[i] = j
                    improved = True
                    break

    grank = {i: k for k, i in enumerate(order)}
    out = []
    for n, ch in enumerate(chapters, 1):
        inner = [e for e in edges if e["from"] in ch and e["to"] in ch]
        ch = topo(sorted(ch, key=grank.get), inner, prefer=grank)
        tc = Counter(topic[i] for i in ch).most_common()
        title = tc[0][0]
        if len(tc) > 1 and tc[1][1] >= 2:
            title += " · " + tc[1][0]
        stage = Counter(STAGE_OF_TOPIC[topic[i]] for i in ch).most_common(1)[0][0]
        # hub = the concept with the most edges inside the chapter: names the chapter when topics repeat
        deg = Counter()
        for e in edges:
            if e["from"] in ch and e["to"] in ch:
                deg[e["from"]] += 1
                deg[e["to"]] += 1
        hub = max(ch, key=lambda i: (deg[i], -ch.index(i)))
        out.append({"id": f"ch{n}", "n": n, "title": title, "stage": stage, "concepts": ch, "trunk": n == 1,
                    "hub": hub})
    seen = Counter(c["title"] for c in out)
    title_of = {c["id"]: c["title"] for c in concepts}
    for c in out:
        if seen[c["title"]] > 1:
            c["title"] = f"{c['title']}: {title_of[c['hub']]}"
    return out


def check(chapters, edges, cap=CAP):
    """Draft §6.5 guards: every concept once, sizes within cap, chapter graph flows one way."""
    where = {}
    for ch in chapters:
        if len(ch["concepts"]) > cap:
            raise GraphError(f"{ch['id']} over cap: {len(ch['concepts'])}")
        for i in ch["concepts"]:
            if i in where:
                raise GraphError(f"{i} in two chapters")
            where[i] = ch["n"]
    for e in edges:
        if where[e["from"]] > where[e["to"]]:
            raise GraphError(f"edge {e['from']} → {e['to']} flows backwards across chapters")
    crossing = sum(1 for e in edges if where[e["from"]] != where[e["to"]])
    return {"chapters": len(chapters), "concepts": len(where), "edges": len(edges),
            "crossing": crossing, "sizes": [len(c["concepts"]) for c in chapters]}
