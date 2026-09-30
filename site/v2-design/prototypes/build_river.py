"""Build the session-2 rework prototype ("river"): DE graph + auto-cut + kinds + priming → out/river-data.js.

    python site/v2-design/prototypes/build_river.py
then open site/v2-design/prototypes/river.html (no server needed).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import autocut  # noqa: E402
import build_proto  # noqa: E402
import de_graph as g  # noqa: E402
import priming  # noqa: E402


def main():
    chapters = autocut.cut(g.CONCEPTS, g.EDGES)
    stats = autocut.check(chapters, g.EDGES)
    missing = [c["id"] for c in g.CONCEPTS if c["id"] not in priming.KIND]
    extra = set(priming.KIND) - {c["id"] for c in g.CONCEPTS}
    if missing or extra:
        raise SystemExit(f"kind map out of step with the graph: missing {missing}, unknown {sorted(extra)}")
    ids = [ch["id"] for ch in chapters]
    if sorted(ids) != sorted(priming.CHAPTERS) or sorted(i for u in priming.UNITS for i in u["chapters"]) != sorted(ids):
        raise SystemExit("priming chapters out of step with the auto-cut (re-key priming.CHAPTERS / UNITS)")
    for ch in chapters:
        p = priming.CHAPTERS[ch["id"]]
        ch["auto"] = ch["title"]
        ch.update(title=p["title"], q=p["q"], line=p["line"], terms=p["terms"])
        if len(p["terms"]) > 3:
            raise SystemExit(f"{ch['id']}: priming allows at most 3 terms")
    unit_of = {c: u["id"] for u in priming.UNITS for c in u["chapters"]}
    for ch in chapters:
        ch["unitId"] = unit_of[ch["id"]]

    bodies = build_proto.v1_bodies()
    concepts = []
    for c in g.CONCEPTS:
        d = dict(c, kind=priming.KIND[c["id"]], oldKind=c["kind"])
        d["body"] = bodies.get(c["v1"]) if c["v1"] else None
        concepts.append(d)
    data = {
        "subject": {"slug": "digital-electronics", "code": "ECE2102", "title": "Digital Electronics"},
        "kinds": priming.KINDS,
        "units": priming.UNITS,
        "chapters": chapters,
        "concepts": concepts,
        "edges": g.EDGES,
        "relates": g.RELATES,
        "order": [i for ch in chapters for i in ch["concepts"]],
        "chapterEdges": build_proto.chapter_edges(chapters, g.EDGES),
        "stats": stats,
    }
    out = HERE / "out"
    out.mkdir(exist_ok=True)
    (out / "river-data.js").write_text("window.DATA = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    kinds = {}
    for c in concepts:
        kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
    print(json.dumps(stats), kinds)


if __name__ == "__main__":
    main()
