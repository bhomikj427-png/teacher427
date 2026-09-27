"""Build the study website: every subjects/**/study-pack/web/ pack -> site/public/.

Run:   python site/build.py            (from the repo root, or anywhere)
Open:  site/public/index.html          (all links are relative, so it works from disk and on GitHub Pages)

A pack is a folder `study-pack/web/` holding:
  meta.json      subject title, exam shape, chapter list + learning-path edges
  figures.py     functions returning SVG strings (ALL = {name: fn})
  content/*.md   one file per chapter; only chapters with a file get a page

Content syntax on top of Markdown:
  [[fig:name|caption|w=60|steps=3]]   figure from figures.py; steps = click-through groups
  [[map:A > B > C|here=2]]            small flow map, `here` = 1-based highlighted node
  :::kind Title ... :::               boxes: q, trap, check, note, key
  :::reveal Title ... :::             collapsed answer (attempt first, then open)
  $$ ... $$                           display equation (one line, Unicode math)
"""
import html
import importlib.util
import json
import re
import shutil
import sys
from pathlib import Path

import markdown

SITE = Path(__file__).resolve().parent
ROOT = SITE.parent
OUT = SITE / "public"
SITE_NAME = "ece' study"


# ------------------------------------------------------------------ markdown extensions
def load_figures(web):
    spec = importlib.util.spec_from_file_location(f"figs_{abs(hash(str(web)))}", web / "figures.py")
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(web))
    spec.loader.exec_module(mod)
    sys.path.pop(0)
    return mod


def inline(t):
    t = re.sub(r"_\{([^{}]*)\}", r"<sub>\1</sub>", t)
    return re.sub(r"\^\{([^{}]*)\}", r"<sup>\1</sup>", t)


def cap_md(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", t)


def render(md_text, figs):
    stash = []

    def fig(m):
        name, *rest = [p.strip() for p in m.group(1).split("|")]
        cap = rest[0] if rest and "=" not in rest[0][:6] else ""
        opts = dict(p.split("=", 1) for p in rest if re.match(r"^(w|steps)=", p))
        svg = figs.ALL[name]()
        w = opts.get("w", "100")
        steps = int(opts.get("steps", 0))
        ctrl = ""
        attrs = ""
        if steps:
            attrs = f' data-steps="{steps}" data-step="0"'
            ctrl = ('<div class="stepper"><button type="button" data-act="prev" aria-label="Previous step">◀</button>'
                    f'<span class="step-n">step 0 / {steps}</span>'
                    '<button type="button" data-act="next" aria-label="Next step">▶</button>'
                    '<button type="button" data-act="all">show all</button></div>')
        cap_html = f"<figcaption>{cap_md(cap)}</figcaption>" if cap else ""
        stash.append(f'<figure class="fig" style="--w:{w}%"{attrs}><div class="fig-body">{svg}</div>{ctrl}{cap_html}</figure>')
        return f"\n\nFIGTOKEN{len(stash) - 1}X\n\n"

    def fmap(m):
        body, *opts = m.group(1).split("|")
        here = next((int(o.split("=")[1]) for o in opts if o.strip().startswith("here=")), 0)
        nodes = [n.strip() for n in body.split(">")]
        out = [f'<span class="n{" here" if k == here else ""}"><b>{k}</b>{html.escape(n)}</span>'
               for k, n in enumerate(nodes, 1)]
        return '\n<div class="flow">' + '<span class="arr" aria-hidden="true">→</span>'.join(out) + "</div>\n"

    def box(m):
        kind, title, body = m.group(1), m.group(2).strip(), m.group(3)
        if kind == "reveal":
            return (f'<details class="reveal" markdown="1">\n<summary>{html.escape(title or "Answer")}</summary>\n\n'
                    f'{body}\n\n</details>')
        head = title or {"q": "Question", "trap": "Trap", "check": "Check", "note": "Note", "key": "Key idea"}[kind]
        return f'<div class="box {kind}" markdown="1">\n<div class="bh">{html.escape(head)}</div>\n\n{body}\n\n</div>'

    t = re.sub(r"\[\[fig:(.*?)\]\]", fig, md_text)
    t = re.sub(r"\[\[map:(.*?)\]\]", fmap, t)
    t = re.sub(r"^\$\$(.*?)\$\$[ \t]*$", lambda m: f'<div class="eq">{inline(m.group(1).strip())}</div>', t, flags=re.M)
    t = re.sub(r"^:::(\w+)[ \t]*(.*?)\n(.*?)\n:::[ \t]*$", box, t, flags=re.S | re.M)
    t = inline(t)
    md = markdown.Markdown(extensions=["tables", "md_in_html", "attr_list", "sane_lists", "toc"],
                           extension_configs={"toc": {"toc_depth": "2-2"}})
    h = md.convert(t)
    for k, f in enumerate(stash):
        h = h.replace(f"<p>FIGTOKEN{k}X</p>", f).replace(f"FIGTOKEN{k}X", f)
    return h, md.toc_tokens


# ------------------------------------------------------------------ page shell
def page(title, body, depth, crumbs=(), toc=None, desc=""):
    up = "../" * depth
    crumb = "".join(f'<a href="{up}{href}">{html.escape(t)}</a><span>/</span>' for t, href in crumbs)
    side = ""
    if toc:
        side = ('<nav class="toc" aria-label="On this page"><div class="toc-h">On this page</div>'
                + "".join(f'<a href="#{t["id"]}">{t["name"]}</a>' for t in toc) + "</nav>")
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · {SITE_NAME}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}static/style.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head><body>
<header class="top"><div class="top-in">
<a class="brand" href="{up}index.html"><span class="logo" aria-hidden="true">◧</span>{SITE_NAME}</a>
<div class="crumbs">{crumb}</div>
<button class="theme" type="button" aria-label="Toggle dark mode">◐</button>
</div></header>
<div class="layout{' has-toc' if toc else ''}">{side}<main>{body}</main></div>
<footer class="foot">Figures are generated from code; every K-map answer is machine-checked.</footer>
<script src="{up}static/app.js"></script>
</body></html>"""


# ------------------------------------------------------------------ subject page figures
def exam_bar(exam):
    total = exam["marks"]
    W, x, parts = 760, 0, []
    for k, s in enumerate(exam["sections"]):
        m = s["count"] * s["each"]
        w = W * m / total
        parts.append(f'<rect class="eb c{k}" x="{x}" y="0" width="{w - 4}" height="70" rx="10"/>'
                     f'<text class="eb-t" x="{x + 12}" y="22">{html.escape(s["label"])}</text>'
                     f'<text class="eb-m" x="{x + 12}" y="44">{m} marks</text>'
                     f'<text class="eb-s" x="{x + 12}" y="61">{s["count"]} × {s["each"]} · {round(100 * m / total)}%</text>')
        x += w
    return (f'<svg class="fig-svg" viewBox="0 0 {W} 70" style="max-width:{W}px" role="img" '
            f'aria-label="Exam split">' + "".join(parts) + "</svg>")


def learning_path(meta, built):
    rows = {}
    for c in meta["chapters"]:
        rows.setdefault(c["row"], []).append(c)
    W, nh, nw, gy = 800, 56, 248, 34
    pos = {}
    for r, cs in rows.items():
        n = len(cs)
        gap = (W - n * nw) / (n + 1)
        for i, c in enumerate(cs):
            pos[c["n"]] = (gap + i * (nw + gap), r * (nh + gy))
    H = (max(rows) + 1) * (nh + gy) - gy
    p = ['<defs><marker id="lp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
         '<path d="M0,0 L10,5 L0,10 z" class="lp-head"/></marker></defs>']
    for a, b in meta["edges"]:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        sx, sy, ex, ey = x1 + nw / 2, y1 + nh, x2 + nw / 2, y2 - 2
        p.append(f'<path class="lp-edge" d="M{sx},{sy} C{sx},{sy + gy * 0.7} {ex},{ey - gy * 0.7} {ex},{ey}" marker-end="url(#lp)"/>')
    for c in meta["chapters"]:
        x, y = pos[c["n"]]
        live = c["id"] in built
        cls = "lp-node live" if live else "lp-node"
        node = (f'<rect class="{cls}" x="{x}" y="{y}" width="{nw}" height="{nh}" rx="12"/>'
                f'<circle class="lp-num{" live" if live else ""}" cx="{x + 24}" cy="{y + nh / 2}" r="13"/>'
                f'<text class="lp-num-t" x="{x + 24}" y="{y + nh / 2 + 4.5}" text-anchor="middle">{c["n"]}</text>'
                f'<text class="lp-t" x="{x + 46}" y="{y + 23}">{html.escape(c["title"])}</text>'
                f'<text class="lp-s" x="{x + 46}" y="{y + 41}">{html.escape(c.get("note") or ("ready" if live else "coming soon"))}</text>')
        p.append(f'<a href="{c["id"]}.html">{node}</a>' if live else f"<g>{node}</g>")
    return (f'<svg class="fig-svg lp" viewBox="-4 -4 {W + 8} {H + 8}" style="max-width:{W}px" role="img" '
            f'aria-label="Learning path">' + "".join(p) + "</svg>")


# ------------------------------------------------------------------ build
def build_pack(web):
    meta = json.loads((web / "meta.json").read_text(encoding="utf-8"))
    figs = load_figures(web)
    slug = meta["slug"]
    out = OUT / slug
    out.mkdir(parents=True, exist_ok=True)
    built = {p.stem: p for p in sorted((web / "content").glob("*.md"))}
    order = [c for c in meta["chapters"] if c["id"] in built]
    crumbs = [(meta["title"], f"{slug}/index.html")]
    for k, c in enumerate(order):
        body, toc = render(built[c["id"]].read_text(encoding="utf-8"), figs)
        prev_ = order[k - 1] if k else None
        next_ = order[k + 1] if k + 1 < len(order) else None
        nav = '<nav class="pn">'
        nav += f'<a class="prev" href="{prev_["id"]}.html">← {html.escape(prev_["title"])}</a>' if prev_ else "<span></span>"
        nav += f'<a class="next" href="{next_["id"]}.html">{html.escape(next_["title"])} →</a>' if next_ else f'<a class="next" href="index.html">Back to the path →</a>'
        nav += "</nav>"
        (out / f"{c['id']}.html").write_text(
            page(c["title"], f'<article class="chapter">{body}</article>{nav}', 1, crumbs, toc,
                 f"{meta['title']}: {c['title']}"), encoding="utf-8")
    ex = meta["exam"]
    cards = "".join(
        (f'<a class="ch live" href="{c["id"]}.html">' if c["id"] in built else '<div class="ch">')
        + f'<span class="ch-n">{c["n"]}</span><span class="ch-t">{html.escape(c["title"])}</span>'
        + f'<span class="ch-w">{html.escape(c["weight"])}</span>'
        + f'<span class="ch-s">{"ready" if c["id"] in built else "coming soon"}</span>'
        + ("</a>" if c["id"] in built else "</div>")
        for c in meta["chapters"])
    body = f"""<section class="hero"><div class="code">{meta['code']}</div><h1>{html.escape(meta['title'])}</h1>
<p class="lede">{html.escape(meta['blurb'])}</p></section>
<h2>The exam</h2><p class="muted">{ex['name']} · {ex['marks']} marks · {ex['minutes']} min · ≈{ex['minutes'] // ex['marks']} min per mark</p>
<figure class="fig" style="--w:100%"><div class="fig-body">{exam_bar(ex)}</div></figure>
<h2>The learning path</h2><p class="muted">Start at 1. Chapters 3, 4 and 5 can go in any order. Click a ready chapter.</p>
<figure class="fig" style="--w:100%"><div class="fig-body">{learning_path(meta, built)}</div></figure>
<h2>Chapters</h2><div class="chapters">{cards}</div>"""
    (out / "index.html").write_text(page(meta["title"], body, 1, [], None, meta["blurb"]), encoding="utf-8")
    return meta, len(order)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(SITE / "static", OUT / "static")
    (OUT / ".nojekyll").write_text("")
    packs = []
    for m in sorted(ROOT.glob("subjects/**/study-pack/web/meta.json")):
        meta, n = build_pack(m.parent)
        packs.append((meta, n))
        print(f"{meta['slug']}: {n} chapter page(s)")
    cards = "".join(
        f'<a class="subj" href="{m["slug"]}/index.html"><span class="code">{m["code"]}</span>'
        f'<span class="subj-t">{html.escape(m["title"])}</span><span class="subj-b">{html.escape(m["blurb"])}</span>'
        f'<span class="subj-p"><span class="bar"><span style="width:{100 * n / len(m["chapters"]):.0f}%"></span></span>'
        f'{n} / {len(m["chapters"])} chapters</span></a>'
        for m, n in packs)
    body = f"""<section class="hero"><h1>Study packs, drawn.</h1>
<p class="lede">Every idea opens with a picture. Every answer stays hidden until you've tried.</p></section>
<div class="subjects">{cards}</div>"""
    (OUT / "index.html").write_text(page("Home", body, 0, desc="Pictorial study packs"), encoding="utf-8")
    print("site ->", OUT)


if __name__ == "__main__":
    main()
