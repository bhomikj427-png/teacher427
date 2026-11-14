"""Pull rendered figures out of the v1 HTML (DE-ETE-v1.html) for placeholders whose source
functions no longer exist. Output: v1figs.json {placeholder: svg/img html}. Run once."""
import json, re
from pathlib import Path
V1 = Path(__file__).resolve().parents[2] / "study-pack" / "pdf-ete"
W = lambda s: re.sub(r"\s+", " ", s)
A = lambda s: "".join(c if ord(c) < 128 else "?" for c in s)
html = W((V1 / "DE-ETE-v1.html").read_text(encoding="utf-8")); htmlA = A(html)
PH = re.compile(r"\{\{(.*?)\}\}")
def texts(seg):  # plain-text runs of the segment, in order
    return [t.strip() for t in re.split(r"<[^>]*>", seg) if len(t.strip()) >= 12]
out = {}
for part in sorted((V1 / "parts").glob("[A-H].html")):
    segs = PH.split(A(W(part.read_text(encoding="utf-8"))))
    cur, k = 0, 1
    while k < len(segs):
        group = [segs[k].strip()]
        while k + 2 < len(segs) and not texts(segs[k + 1]):
            k += 2; group.append(segs[k].strip())
        prev = [t for j in range(0, k, 2) for t in texts(segs[j])]
        nxt = texts(segs[k + 1]) if k + 1 < len(segs) else []
        a = htmlA.find(prev[-1][-40:], cur) + len(prev[-1][-40:]) if prev else cur
        b = htmlA.find(nxt[0][:40], a) if nxt else len(html)
        assert a >= 0 and b > a, (part.name, group)
        sl = html[a:b]
        s = min([i for i in (sl.find("<svg"), sl.find("<img")) if i >= 0])
        ends = [sl.rfind("</svg>") + 6] if "</svg>" in sl else []
        if "<img" in sl:
            ends.append(sl.find(">", sl.rfind("<img")) + 1)
        e = max(ends)
        out[" + ".join(group)] = sl[s:e]
        cur, k = b, k + 2
(Path(__file__).parent / "v1figs.json").write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
for k, v in out.items(): print(len(v), v.count("<svg"), k[:80])
