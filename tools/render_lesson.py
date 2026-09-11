#!/usr/bin/env python3
"""
render_lesson.py — the browser lesson surface for the ece' Visual & Rendering subsystem.

Takes a declarative LESSON SPEC and emits ONE self-contained HTML file (CDN stack wired in,
clean typographic CSS), then auto-opens it. This is the *lesson surface*; the terminal stays the
*control channel* and stays plain ASCII (see ../rendering.md §2 — the two-surface rule). The two
never duplicate content: the terminal says "-> figure 2 in the lesson tab", the figure lives here.

THE SIX VISUAL PRIMITIVES (../rendering.md §3) and where each is rendered:
  1 Math / derivation .................. MathJax        (client-side CDN)   block "math"
  2 Relationship graph / concept map ... Mermaid        (client-side CDN)   block "map"
  3 Process / sequence / state ......... Mermaid        (client-side CDN)   block "process"
  4 Quantitative plot .................. matplotlib      (Python -> SVG)     block "plot"
  5 Tabular / comparison / truth grid .. HTML + CSS      (here)             block "table"
  6 Domain structural diagram .......... registry        (Python -> SVG)    block "structural"
                                          or WaveDrom     (client-side CDN)   block "timing"
  + "code"  -> highlight.js (client-side CDN)
  + "prose" -> minimal markdown
  + "check" -> a styled retrieval prompt (the CHECK lands here when it carries a figure; the
               dialogue itself still happens in the terminal)

Primitives 1,2,3,5,code are dependency-light client-side JS — zero Python. Primitives 4 and 6 need
real computation / schematic primitives, so they are pre-rendered to inline SVG by make_figure.py.
No network calls at lesson time except the CDN <script>/<link> tags.

LESSON SPEC
  {
    "title": str,
    "subject": str,                 # routes structural figures through the registry; informational
    "intro": str (optional markdown),
    "sections": [ {"heading": str, "blocks": [ <block>, ... ]}, ... ]
    # (a flat top-level "blocks" list is also accepted and wrapped in one untitled section)
  }
  Each <block> is one of the types above; figure-bearing blocks may carry a "caption" and are
  auto-numbered "Figure N" so the terminal can reference them.

USAGE
  As a library (the normal path — a lesson script builds the spec, computing any arrays, then):
    from render_lesson import render
    render(spec, "out.html")                      # writes + opens
  As a CLI:
    python tools/render_lesson.py <spec.json> <out.html> [--no-open]
"""
import os
import re
import sys
import json
import html
import datetime
import webbrowser

from make_figure import make_figure, NoStructuralRenderer


# ----------------------------------------------------------------------------- pinned CDN stack
# Major/minor pinned for determinism; all dependency-light, all client-side.
CDN = {
    "mathjax":      "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js",
    "mermaid":      "https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js",
    "hljs_js":      "https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11.9.0/highlight.min.js",
    "hljs_css":     "https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11.9.0/styles/github-dark.min.css",
    "wavedrom":     "https://cdn.jsdelivr.net/npm/wavedrom@3.5.0/wavedrom.min.js",
    "wavedrom_skin":"https://cdn.jsdelivr.net/npm/wavedrom@3.5.0/skins/default.js",
}


# ----------------------------------------------------------------------------- minimal markdown
def _inline(text):
    """Escape HTML, then apply a tiny safe inline subset: **bold** and `code`."""
    t = html.escape(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


def _markdown(md):
    """Blank-line-separated blocks. A block of '- ' lines becomes a <ul>; else a <p>. One idea per
    line is preserved (the learner's clean-scannable-UI preference)."""
    out = []
    for chunk in re.split(r"\n\s*\n", md.strip()):
        lines = [ln for ln in chunk.splitlines() if ln.strip()]
        if lines and all(ln.lstrip().startswith("- ") for ln in lines):
            items = "".join(f"<li>{_inline(ln.lstrip()[2:])}</li>" for ln in lines)
            out.append(f"<ul>{items}</ul>")
        else:
            out.append("<p>" + "<br>".join(_inline(ln) for ln in lines) + "</p>")
    return "\n".join(out)


# ----------------------------------------------------------------------------- block renderers
def _figure(inner, fignum, caption):
    cap = f"<figcaption>Figure {fignum}{' — ' + _inline(caption) if caption else ''}</figcaption>"
    return f'<figure class="fig">{inner}{cap}</figure>'


def _render_block(b, state):
    t = b.get("type")

    if t == "prose":
        return _markdown(b.get("md", ""))

    if t == "math":
        tex = b["tex"]
        return f'<div class="math">\\[{tex}\\]</div>' if b.get("display", True) \
            else f'<span class="math">\\({tex}\\)</span>'

    if t == "code":
        lang = b.get("lang", "")
        return (f'<pre class="code"><code class="language-{html.escape(lang)}">'
                f'{html.escape(b["code"])}</code></pre>')

    if t in ("map", "process"):
        state["fig"] += 1
        inner = f'<pre class="mermaid">{html.escape(b["mermaid"])}</pre>'
        return _figure(inner, state["fig"], b.get("caption"))

    if t == "table":
        state["fig"] += 1
        hi = b.get("highlight_row")
        head = "".join(f"<th>{_inline(str(h))}</th>" for h in b.get("headers", []))
        rows = ""
        for i, row in enumerate(b.get("rows", [])):
            cls = ' class="hi"' if hi is not None and i == hi else ""
            cells = "".join(f"<td>{_inline(str(c))}</td>" for c in row)
            rows += f"<tr{cls}>{cells}</tr>"
        tbl = f"<table class='grid'><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>"
        return _figure(tbl, state["fig"], b.get("caption"))

    if t == "timing":   # primitive 6, client-side WaveDrom
        state["fig"] += 1
        state["wavedrom"] = True
        payload = json.dumps(b["wavedrom"])
        inner = f'<script type="WaveDrom">{payload}</script>'
        return _figure(inner, state["fig"], b.get("caption"))

    if t == "plot":     # primitive 4, matplotlib -> inline SVG
        state["fig"] += 1
        svg = make_figure({"kind": "matplotlib", **b["figure"]}) \
            if b["figure"].get("kind") is None else make_figure(b["figure"])
        return _figure(f'<div class="svg">{svg}</div>', state["fig"], b.get("caption"))

    if t == "structural":   # primitive 6, registry -> inline SVG, with §3 fallback
        state["fig"] += 1
        try:
            svg = make_figure(b["figure"])
            return _figure(f'<div class="svg">{svg}</div>', state["fig"], b.get("caption"))
        except NoStructuralRenderer as e:
            note = (f'<p class="note">No structural renderer registered for subject '
                    f'<code>{html.escape(e.subject)}</code> — falling back (a domain renderer could '
                    f'be registered via <code>register_structural</code>).</p>')
            fb = b.get("fallback")
            if fb:
                state["fig"] -= 1   # let the fallback block claim the figure number
                return note + _render_block(fb, state)
            return _figure(f'<div class="svg missing">[no figure]</div>',
                           state["fig"], b.get("caption")) + note

    if t == "image":    # sourced image (whiteboard.md §5) — embedded as a data URI, citation required
        src_note = b.get("source")
        if not src_note or not str(src_note).strip():
            raise ValueError("image blocks require a non-empty 'source' (citation) — whiteboard.md §5")
        state["fig"] += 1
        import base64 as _b64
        ext = os.path.splitext(b["file"])[1].lower().lstrip(".") or "png"
        mime = {"jpg": "jpeg", "svg": "svg+xml"}.get(ext, ext)
        data = _b64.b64encode(open(b["file"], "rb").read()).decode("ascii")
        inner = (f'<div class="svg"><img src="data:image/{mime};base64,{data}" '
                 f'style="max-width:100%"></div>')
        srcline = f'<div class="note" style="text-align:center">source: {_inline(str(src_note))}</div>'
        return _figure(inner, state["fig"], b.get("caption")) + srcline

    if t == "check":    # retrieval prompt; answer hidden behind a disclosure
        ans = (f'<details class="answer"><summary>show answer</summary>'
               f'<div>{_markdown(b["answer"])}</div></details>') if b.get("answer") else ""
        return (f'<div class="check"><div class="check-tag">CHECK — retrieve before revealing</div>'
                f'<div class="check-q">{_markdown(b["q"])}</div>{ans}</div>')

    raise ValueError(f"render_lesson: unknown block type {t!r}")


# ----------------------------------------------------------------------------- page assembly
def _sections(spec, state):
    secs = spec.get("sections")
    if secs is None:
        secs = [{"heading": None, "blocks": spec.get("blocks", [])}]
    parts = []
    for s in secs:
        h = f"<h2>{_inline(s['heading'])}</h2>" if s.get("heading") else ""
        body = "\n".join(_render_block(b, state) for b in s.get("blocks", []))
        parts.append(f"<section>{h}{body}</section>")
    return "\n".join(parts)


def _html(spec):
    state = {"fig": 0, "wavedrom": False}
    body = _sections(spec, state)
    intro = f'<div class="intro">{_markdown(spec["intro"])}</div>' if spec.get("intro") else ""
    subject = spec.get("subject", "")
    badge = f'<span class="badge">{_inline(subject)}</span>' if subject else ""

    wavedrom_scripts = (
        f'<script src="{CDN["wavedrom_skin"]}"></script>'
        f'<script src="{CDN["wavedrom"]}"></script>'
        f'<script>window.addEventListener("load",function(){{'
        f'if(window.WaveDrom){{WaveDrom.ProcessAll();}}}});</script>'
    ) if state["wavedrom"] else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(spec.get("title", "Lesson"))}</title>
<link rel="stylesheet" href="{CDN['hljs_css']}">
<style>{_CSS}</style>
</head>
<body>
<main>
  <header class="lesson-head">
    {badge}
    <h1>{_inline(spec.get("title", "Lesson"))}</h1>
    <p class="surface-note">Lesson surface. The dialogue, retrieval prompts and CHECK answers
      happen in the terminal; this tab holds the figures, math and code.</p>
  </header>
  {intro}
  {body}
</main>

<script>
  window.MathJax = {{ tex: {{ inlineMath: [['\\\\(','\\\\)']], displayMath: [['\\\\[','\\\\]']] }},
                      svg: {{ fontCache: 'global' }} }};
</script>
<script id="MathJax-script" async src="{CDN['mathjax']}"></script>
<script src="{CDN['mermaid']}"></script>
<script>mermaid.initialize({{ startOnLoad: true, theme: 'neutral', securityLevel: 'loose' }});</script>
<script src="{CDN['hljs_js']}"></script>
<script>hljs.highlightAll();</script>
{wavedrom_scripts}
</body>
</html>
"""


# ----------------------------------------------------------------------------- clean typographic CSS
# Dark surface, single max-width reading column, generous whitespace, scannable headers, figures on
# light cards (matplotlib/schemdraw SVGs are black-on-white). Honors the clean-scannable-UI pref.
_CSS = """
:root{
  --bg:#15171c; --panel:#1d2027; --ink:#e6e8ee; --dim:#9aa3b2; --line:#2c313b;
  --accent:#6aa9ff; --accent-soft:#22304a; --check:#1e2a1e; --check-line:#3c5a3c;
  --max:50rem;
}
*{box-sizing:border-box}
html{font-size:17px}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;line-height:1.65;}
main{max-width:var(--max);margin:0 auto;padding:3rem 1.4rem 6rem;}
.lesson-head{border-bottom:1px solid var(--line);padding-bottom:1.2rem;margin-bottom:2rem;}
.badge{display:inline-block;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--accent);background:var(--accent-soft);padding:.2rem .6rem;border-radius:.4rem;}
h1{font-size:1.9rem;line-height:1.2;margin:.6rem 0 .2rem;}
h2{font-size:1.3rem;margin:2.6rem 0 .8rem;padding-top:.6rem;border-top:1px solid var(--line);}
.surface-note{color:var(--dim);font-size:.85rem;margin:.4rem 0 0;}
p{margin:.7rem 0;}
ul{margin:.6rem 0;padding-left:1.3rem;}
li{margin:.25rem 0;}
code{font-family:"JetBrains Mono",Consolas,Menlo,monospace;font-size:.9em;
  background:#0e1014;border:1px solid var(--line);border-radius:.3rem;padding:.05rem .35rem;}
pre.code{background:#0e1014;border:1px solid var(--line);border-radius:.6rem;
  padding:1rem 1.1rem;overflow:auto;margin:1.2rem 0;}
pre.code code{background:none;border:none;padding:0;font-size:.86rem;line-height:1.55;}
.intro{color:var(--dim);font-size:1.02rem;}
.math{overflow-x:auto;}
div.math{margin:1.4rem 0;}
figure.fig{margin:1.6rem 0;padding:0;}
.fig .svg, .fig pre.mermaid{background:#fff;border:1px solid var(--line);border-radius:.6rem;
  padding:1rem;text-align:center;overflow:auto;}
.fig .svg svg, .fig pre.mermaid svg{max-width:100%;height:auto;}
.fig pre.mermaid{color:#111;}
.fig .svg.missing{color:#b00;font-family:monospace;}
figcaption{color:var(--dim);font-size:.85rem;margin-top:.5rem;text-align:center;}
table.grid{border-collapse:collapse;width:100%;background:var(--panel);border-radius:.6rem;
  overflow:hidden;font-size:.92rem;}
table.grid th,table.grid td{border:1px solid var(--line);padding:.5rem .75rem;text-align:left;}
table.grid th{background:#222633;color:var(--ink);font-weight:600;}
table.grid tr.hi td{background:var(--accent-soft);}
.note{color:var(--dim);font-size:.85rem;font-style:italic;}
.check{background:var(--check);border:1px solid var(--check-line);border-left:4px solid #5fa85f;
  border-radius:.6rem;padding:1rem 1.2rem;margin:1.8rem 0;}
.check-tag{font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:#8fce8f;
  margin-bottom:.4rem;}
.check-q p{margin:.3rem 0;}
.answer{margin-top:.8rem;}
.answer summary{cursor:pointer;color:var(--accent);font-size:.85rem;}
.answer>div{margin-top:.6rem;padding-top:.6rem;border-top:1px dashed var(--check-line);}
"""


# ----------------------------------------------------------------------------- entry points
def render(spec, outpath, open_browser=True):
    """Render a lesson spec to a self-contained HTML file and (by default) open it in the browser.

    Low-level: writes to exactly `outpath`. For a real teaching lesson prefer save_lesson(), which
    routes to the permanent, dated, per-subject home so lessons are never lost to a temp dir."""
    outpath = os.path.abspath(outpath)
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(_html(spec))
    print(f"[done] lesson -> {outpath}")
    if open_browser:
        webbrowser.open("file:///" + outpath.replace("\\", "/"))
    return outpath


# --------------------------------------------------------------- permanent, per-subject lesson home
# The canonical, durable layout for a RENDERED teaching lesson (see rendering.md §8):
#     subjects/<subject>/lessons/[<unit-slug>/]<YYYY-MM-DD>-<concept-slug>.html
# Dated + slugged so re-rendering the same concept on a later day never clobbers the earlier copy,
# and a subject's lessons sit beside its knowledge-base/ and progress-log.md — never in a temp dir.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # tools/ -> repo root


def _slugify(text):
    """'RC Low-Pass Filter' -> 'rc-low-pass-filter'. Safe for a filename on any platform."""
    s = re.sub(r"[^a-z0-9]+", "-", str(text).strip().lower())
    return s.strip("-") or "lesson"


def lesson_path(subject, concept, unit=None, date=None, root=None):
    """Build the canonical permanent path for a rendered lesson. Does not write anything.

    `subject` may be nested (e.g. "sem-3/01-statistics-and-probability"): each `/`-separated
    segment is slugified separately so the path stays inside the real subject folder."""
    date = date or datetime.date.today().isoformat()
    subject_parts = [_slugify(seg) for seg in str(subject).replace("\\", "/").split("/") if seg.strip()]
    parts = [root or REPO_ROOT, "subjects", *subject_parts, "lessons"]
    if unit:
        parts.append(_slugify(unit))                       # optional per-unit subfolder arrangement
    parts.append(f"{date}-{_slugify(concept)}.html")
    return os.path.join(*parts)


def save_lesson(spec, subject=None, concept=None, unit=None, open_browser=True, date=None, root=None):
    """Render to the permanent per-subject lessons/ folder and return the saved path.

    subject / concept / unit default to spec['subject'] / spec['title'] / spec.get('unit'), so the
    normal call is just save_lesson(spec). This is the path a teaching session should use — the
    lesson lands next to the subject's knowledge base and persists across sessions."""
    subject = subject or spec.get("subject")
    concept = concept or spec.get("title")
    unit = unit if unit is not None else spec.get("unit")
    if not subject:
        raise ValueError("save_lesson needs a subject (set spec['subject'] or pass subject=...).")
    if not concept:
        raise ValueError("save_lesson needs a concept (set spec['title'] or pass concept=...).")
    return render(spec, lesson_path(subject, concept, unit, date, root), open_browser=open_browser)


def main():
    args = [a for a in sys.argv[1:] if a != "--no-open"]
    if len(args) != 2:
        print(__doc__)
        sys.exit(1)
    spec = json.load(open(args[0], encoding="utf-8"))
    render(spec, args[1], open_browser="--no-open" not in sys.argv)


if __name__ == "__main__":
    main()
