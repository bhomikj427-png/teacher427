"""Build the v2 session-2 prototype data: DE graph → auto-cut chapters → out/data.js (+ v1 card bodies).

    python site/v2-design/prototypes/build_proto.py
then open site/v2-design/prototypes/proto.html (no server needed).
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parents[1]
ROOT = SITE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(SITE))

import autocut  # noqa: E402
import de_graph as g  # noqa: E402
import build as v1build  # noqa: E402  (site/build.py: its Markdown renderer draws the v1 card bodies)

DE_WEB = ROOT / "subjects/sem-3/04-digital-electronics/study-pack/web"


def v1_bodies():
    figs = v1build.load_figures(DE_WEB)
    text = (DE_WEB / "content/01-boolean-kmap.md").read_text(encoding="utf-8")
    return {cid: v1build.render(body, figs) for cid, _t, _k, _g, body in v1build.split_concepts(text)}


def chapter_edges(chapters, edges):
    """Chapter → chapter links (count of concept edges), plus the transitive reduction used for drawing."""
    where = {i: c["id"] for c in chapters for i in c["concepts"]}
    count = defaultdict(int)
    for e in edges:
        a, b = where[e["from"]], where[e["to"]]
        if a != b:
            count[(a, b)] += 1
    succ = defaultdict(set)
    for a, b in count:
        succ[a].add(b)

    def reachable(a, b, skip):
        stack, seen = [x for x in succ[a] if (a, x) != skip], set()
        while stack:
            x = stack.pop()
            if x == b:
                return True
            if x not in seen:
                seen.add(x)
                stack.extend(succ[x])
        return False
    out = []
    for (a, b), n in count.items():
        out.append({"from": a, "to": b, "n": n, "direct": not reachable(a, b, (a, b))})
    return out


def main():
    chapters = autocut.cut(g.CONCEPTS, g.EDGES)
    stats = autocut.check(chapters, g.EDGES)
    bodies = v1_bodies()
    concepts = []
    for c in g.CONCEPTS:
        d = dict(c)
        d["body"] = bodies.get(c["v1"]) if c["v1"] else None
        concepts.append(d)
    order = [i for ch in chapters for i in ch["concepts"]]
    data = {
        "subject": {"slug": "digital-electronics", "code": "ECE2102", "title": "Digital Electronics",
                    "line": "MTE + ETE scope · auto-cut from the knowledge base"},
        "stages": autocut.STAGES,
        "chapters": chapters,
        "concepts": concepts,
        "edges": g.EDGES,
        "relates": g.RELATES,
        "order": order,
        "chapterEdges": chapter_edges(chapters, g.EDGES),
        "stats": stats,
        "cut": {"cap": autocut.CAP, "min": autocut.MIN},
    }
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    (out / "data.js").write_text("window.DATA = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(json.dumps(stats))
    for ch in chapters:
        print(ch["n"], ch["stage"], ch["title"], len(ch["concepts"]))


if __name__ == "__main__":
    main()
