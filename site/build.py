"""Build the study website: every subjects/**/study-pack/web/ pack -> site/public/.

Run:   python site/build.py
Open:  site/public/index.html   (relative links: works from disk and on GitHub Pages)

Each subject is ONE page: a zoomable map of every chapter and concept. Click a chapter to zoom in;
click a concept to open its card (one concept at a time, ◀ ▶ to walk the order, Esc to zoom out).

A pack is a folder `study-pack/web/` holding:
  meta.json      subject, exam shape, stages (colour groups), chapters (+ outline concepts for
                 chapters without content yet), learning-path edges
  figures.py     functions returning SVG strings (ALL = {name: fn})
  content/NN-*.md   one file per chapter, split into concepts by header lines:
                 @@ id | Title | kind | one-line gist      (kind: idea, method, exam, trap, practice)

Content syntax on top of Markdown:
  [[fig:name|caption|w=60|steps=3]]   figure from figures.py; steps = click-through groups
  :::q / trap / check / note / key    boxes          :::reveal Title   hidden until clicked
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
KINDS = {"idea", "method", "exam", "trap", "practice"}


# ------------------------------------------------------------------ markdown
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
        cap = rest[0] if rest and not re.match(r"^(w|steps)=", rest[0]) else ""
        opts = dict(p.split("=", 1) for p in rest if re.match(r"^(w|steps)=", p))
        svg = figs.ALL[name]()
        steps = int(opts.get("steps", 0))
        attrs = ctrl = ""
        if steps:
            attrs = f' data-steps="{steps}" data-step="0"'
            ctrl = ('<div class="stepper"><button type="button" data-act="prev" aria-label="Previous step">◀</button>'
                    f'<span class="step-n">step 0 / {steps}</span>'
                    '<button type="button" data-act="next" aria-label="Next step">▶</button>'
                    '<button type="button" data-act="all">show all</button></div>')
        cap_html = f"<figcaption>{cap_md(cap)}</figcaption>" if cap else ""
        stash.append(f'<figure class="fig" style="--w:{opts.get("w", "100")}%"{attrs}>'
                     f'<div class="fig-body">{svg}</div>{ctrl}{cap_html}</figure>')
        return f"\n\nFIGTOKEN{len(stash) - 1}X\n\n"

    def box(m):
        kind, title, body = m.group(1), m.group(2).strip(), m.group(3)
        if kind == "reveal":
            return (f'<details class="reveal" markdown="1">\n<summary>{html.escape(title or "Answer")}</summary>\n\n'
                    f'{body}\n\n</details>')
        head = title or {"q": "Question", "trap": "Trap", "check": "Check", "note": "Note", "key": "Key idea"}[kind]
        return f'<div class="box {kind}" markdown="1">\n<div class="bh">{html.escape(head)}</div>\n\n{body}\n\n</div>'

    t = re.sub(r"\[\[fig:(.*?)\]\]", fig, md_text)
    t = re.sub(r"^\$\$(.*?)\$\$[ \t]*$",
               lambda m: '<div class="eq">' + re.sub(r" {3,}", "&emsp;&emsp;", inline(m.group(1).strip())) + "</div>",
               t, flags=re.M)
    t = re.sub(r"^:::(\w+)[ \t]*(.*?)\n(.*?)\n:::[ \t]*$", box, t, flags=re.S | re.M)
    t = inline(t)
    h = markdown.markdown(t, extensions=["tables", "md_in_html", "attr_list", "sane_lists"])
    for k, f in enumerate(stash):
        h = h.replace(f"<p>FIGTOKEN{k}X</p>", f).replace(f"FIGTOKEN{k}X", f)
    return h


def split_concepts(text):
    """'@@ id | Title | kind | gist' headers -> [(id, title, kind, gist, body_md)]."""
    parts = re.split(r"^@@[ \t]+(.+)$", text, flags=re.M)
    out = []
    for head, body in zip(parts[1::2], parts[2::2]):
        f = [x.strip() for x in head.split("|")] + [""] * 4
        cid, title, kind, gist = f[:4]
        assert kind in KINDS, f"unknown kind {kind!r} in {head!r}"
        out.append((cid, title, kind, gist, body))
    return out


# ------------------------------------------------------------------ shell
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">')
THEME_BOOT = "<script>try{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}catch(e){}</script>"


def head(title, up, desc, extra_css=""):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            f'<title>{html.escape(title)} · {SITE_NAME}</title><meta name="description" content="{html.escape(desc)}">'
            f'{FONTS}<link rel="stylesheet" href="{up}static/style.css">{extra_css}{THEME_BOOT}</head>')


def exam_mini(ex):
    total, out = ex["marks"], []
    for k, s in enumerate(ex["sections"]):
        m = s["count"] * s["each"]
        out.append(f'<span class="xm c{k}" style="flex:{m}" title="{html.escape(s["label"])}: {s["count"]} × {s["each"]} = {m} marks">'
                   f'{html.escape(s["label"].split("·")[0].strip())} {m}</span>')
    return (f'<div class="exam-chip" title="{ex["name"]}: {ex["marks"]} marks, {ex["minutes"]} min">'
            f'<span class="xl">{ex["name"]} · {ex["marks"]} marks · {ex["minutes"]} min</span>'
            f'<span class="xbar">{"".join(out)}</span></div>')


# ------------------------------------------------------------------ build
def build_pack(web):
    meta = json.loads((web / "meta.json").read_text(encoding="utf-8"))
    figs = load_figures(web)
    slug = meta["slug"]
    out = OUT / slug
    out.mkdir(parents=True, exist_ok=True)
    files = {p.stem: p for p in (web / "content").glob("*.md")}
    templates, chapters, n_concepts, n_ready = [], [], 0, 0
    for c in meta["chapters"]:
        ch = {k: c[k] for k in ("id", "n", "title", "stage", "weight")}
        ch["note"] = c.get("note", "")
        if c["id"] in files:
            concepts = []
            for cid, title, kind, gist, body in split_concepts(files[c["id"]].read_text(encoding="utf-8")):
                tid = f"t-{c['id']}--{cid}"
                templates.append(f'<template id="{tid}">{render(body, figs)}</template>')
                concepts.append({"id": cid, "title": title, "kind": kind, "gist": gist, "ready": True})
            ch["ready"] = True
        else:
            concepts = [{"id": f"c{k}", "title": t, "kind": kd, "gist": "", "ready": False}
                        for k, (t, kd) in enumerate(c.get("concepts", []), 1)]
            ch["ready"] = False
        ch["concepts"] = concepts
        n_concepts += len(concepts)
        n_ready += sum(x["ready"] for x in concepts)
        chapters.append(ch)
    data = {"slug": slug, "code": meta["code"], "title": meta["title"], "stages": meta["stages"],
            "chapters": chapters, "edges": meta["edges"]}
    stage_legend = "".join(f'<span class="lg-st h-{s["hue"]}"><i></i>{html.escape(s["title"])}</span>' for s in meta["stages"])
    kind_legend = "".join(f'<span class="lg-k k-{k}"><i></i>{lbl}</span>' for k, lbl in
                          (("idea", "idea"), ("method", "method"), ("exam", "exam question"), ("trap", "trap"),
                           ("practice", "practice")))
    body = f"""<body class="mapmode">
<header class="mbar">
  <a class="brand" href="../index.html" title="All subjects"><span class="logo">◧</span></a>
  <button class="crumb" type="button" data-go="">
    <span class="code">{meta['code']}</span><span class="st">{html.escape(meta['title'])}</span></button>
  <span class="crumb-ch" hidden></span>
  <span class="grow"></span>
  {exam_mini(meta['exam'])}
  <button class="theme" type="button" aria-label="Toggle dark mode">◐</button>
</header>
<div id="viewport" aria-label="Concept map"><svg id="map" xmlns="http://www.w3.org/2000/svg"><g id="cam"></g></svg></div>
<div class="legend" id="legend"><button type="button" class="lg-toggle" aria-expanded="true">Key</button>
  <div class="lg-body"><div class="lg-row">{stage_legend}</div><div class="lg-row">{kind_legend}</div>
  <div class="lg-row lg-count">{len(chapters)} chapters · {n_concepts} concepts · {n_ready} drawn so far</div></div></div>
<div class="zoom"><button type="button" data-z="in" aria-label="Zoom in">+</button><button type="button" data-z="out" aria-label="Zoom out">−</button><button type="button" data-z="fit" aria-label="Show everything">⤢</button></div>
<div class="hint" id="hint">Click a chapter to zoom in · scroll or pinch to zoom · drag to move</div>
<nav class="chsheet" id="chsheet" aria-label="Concepts in this chapter" hidden></nav>
<div class="toast" id="toast" role="status"></div>
<div class="scrim" id="scrim"></div>
<article class="card" id="card" role="dialog" aria-modal="true" aria-labelledby="card-title" hidden>
  <header class="card-h"><div class="card-meta"><span class="card-ch"></span><span class="card-kind"></span></div>
    <h2 id="card-title"></h2><p class="card-gist"></p>
    <button class="card-x" type="button" aria-label="Back to the map">✕</button></header>
  <div class="card-b"></div>
  <footer class="card-f"><button type="button" class="nav prev">◀ <span></span></button><div class="pips"></div>
    <button type="button" class="nav next"><span></span> ▶</button></footer>
</article>
{''.join(templates)}
<script id="map-data" type="application/json">{json.dumps(data, ensure_ascii=False)}</script>
<script src="../static/app.js"></script><script src="../static/map.js"></script>
</body></html>"""
    (out / "index.html").write_text(head(meta["title"], "../", meta["blurb"], '<link rel="stylesheet" href="../static/map.css">')
                                    + body, encoding="utf-8")
    return meta, n_concepts, n_ready


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(SITE / "static", OUT / "static")
    (OUT / ".nojekyll").write_text("")
    packs = []
    for m in sorted(ROOT.glob("subjects/**/study-pack/web/meta.json")):
        meta, n, r = build_pack(m.parent)
        packs.append((meta, n, r))
        print(f"{meta['slug']}: map page, {n} concepts ({r} drawn)")
    cards = "".join(
        f'<a class="subj" href="{m["slug"]}/index.html"><span class="code">{m["code"]}</span>'
        f'<span class="subj-t">{html.escape(m["title"])}</span><span class="subj-b">{html.escape(m["blurb"])}</span>'
        f'<span class="subj-p"><span class="bar"><span style="width:{100 * r / n:.0f}%"></span></span>{r} / {n} concepts drawn</span></a>'
        for m, n, r in packs)
    body = f"""<body><header class="top"><div class="top-in"><a class="brand" href="index.html"><span class="logo">◧</span>{SITE_NAME}</a>
<span class="grow"></span><button class="theme" type="button" aria-label="Toggle dark mode">◐</button></div></header>
<main class="home"><section class="hero"><h1>Study packs, as maps.</h1>
<p class="lede">Each subject is one map. Zoom into a chapter, open one concept at a time, and try before you reveal.</p></section>
<div class="subjects">{cards}</div></main><script src="static/app.js"></script></body></html>"""
    (OUT / "index.html").write_text(head("Home", "", "Pictorial study maps") + body, encoding="utf-8")
    print("site ->", OUT)


if __name__ == "__main__":
    main()
