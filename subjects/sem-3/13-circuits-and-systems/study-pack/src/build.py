"""Build the ECE2107 study pack: content/*.md + figures.py -> html/*.html -> pdf/*.pdf (+ one combined PDF).

Run:  python build.py
Needs: markdown, schemdraw, ziamath, matplotlib, pypdf, Google Chrome (headless print).

Content syntax on top of Markdown:
  [[fig:name|caption|w=60]]      figure from figures.py (w = max width in %, optional)
  [[map:A > B > C|here=2]]       horizontal flow map (here = 1-based node to highlight)
  :::q Title ... :::             boxes: q (question), guess, check, trap, note, key
  $$ ... $$                      display equation (one line)
  \\frac{a}{b}  x_{sub}  x^{sup}  stacked fraction / subscript / superscript
  \\sqrt{x}                     √(x)
"""
import re
import subprocess
import sys
import warnings
from pathlib import Path

import markdown
from pypdf import PdfWriter, PdfReader

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import figures  # noqa: E402

ROOT = HERE.parent
CONTENT = HERE / "content"
HTML = ROOT / "html"
PDF = ROOT / "pdf"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PACK = "ECE2107 Circuits & Systems · MTE Study Pack"

CSS = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm;
  @bottom-left { content: "%(pack)s"; font: 8pt 'Segoe UI', Arial; color: #9ca3af; }
  @bottom-right { content: counter(page); font: 8pt 'Segoe UI', Arial; color: #9ca3af; } }
:root { --ink:#1f2937; --muted:#6b7280; --accent:#1d4ed8; --line:#e5e7eb; }
* { box-sizing: border-box; }
body { font-family: 'Segoe UI', Arial, sans-serif; color: var(--ink); font-size: 10.5pt;
  line-height: 1.5; margin: 0; background: #fff; }
h1 { font-size: 21pt; margin: 0 0 2pt; letter-spacing: -0.3pt; }
.sub { color: var(--muted); font-size: 9.5pt; margin-bottom: 12pt; }
h2 { font-size: 13.5pt; color: var(--accent); border-bottom: 1.5px solid var(--line);
  padding-bottom: 3pt; margin: 18pt 0 8pt; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 14pt 0 5pt; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
code { font-family: Consolas, monospace; font-size: 9.5pt; background: #f3f4f6; padding: 0 3px; border-radius: 3px; }
ol, ul { break-inside: avoid; }
table { border-collapse: collapse; margin: 8pt 0; width: 100%%; font-size: 9.8pt; break-inside: avoid; }
th { background: #eff6ff; color: #1e3a8a; text-align: left; }
th, td { border: 1px solid #dbe2ea; padding: 4pt 7pt; vertical-align: top; }
figure { margin: 10pt auto; text-align: center; break-inside: avoid; }
figure svg { max-width: 100%%; height: auto; }
figcaption { font-size: 9pt; color: var(--muted); margin-top: 3pt; }
.eq { text-align: center; font-size: 12pt; margin: 8pt 0; padding: 6pt; background: #f8fafc;
  border-radius: 6px; break-inside: avoid; }
.frac { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center;
  margin: 0 2px; font-size: 95%%; }
.frac > span:first-child { border-bottom: 1px solid currentColor; padding: 0 3px; }
.frac > span:last-child { padding: 0 3px; }
.box { border-radius: 7px; padding: 7pt 11pt; margin: 9pt 0; break-inside: avoid; border-left: 4px solid; }
.box > .bh { font-weight: 700; font-size: 9.5pt; text-transform: uppercase; letter-spacing: .4pt; margin-bottom: 2pt; }
.box p:first-of-type { margin-top: 2pt; } .box p:last-child { margin-bottom: 2pt; }
.q { background: #eff6ff; border-color: #1d4ed8; } .q > .bh { color: #1d4ed8; }
.guess { background: #fefce8; border-color: #ca8a04; } .guess > .bh { color: #a16207; }
.check { background: #f0fdf4; border-color: #16a34a; } .check > .bh { color: #15803d; }
.trap { background: #fef2f2; border-color: #dc2626; } .trap > .bh { color: #b91c1c; }
.note { background: #f9fafb; border-color: #9ca3af; } .note > .bh { color: #4b5563; }
.key { background: #f5f3ff; border-color: #7c3aed; } .key > .bh { color: #6d28d9; }
.map { display: flex; flex-wrap: wrap; align-items: center; gap: 4pt; margin: 8pt 0 12pt; break-inside: avoid; }
.map .n { border: 1.5px solid #cbd5e1; border-radius: 6px; padding: 4pt 8pt; font-size: 9.3pt; background: #fff; }
.map .n.here { border-color: var(--accent); background: #eff6ff; color: #1e3a8a; font-weight: 600; }
.map .a { color: #94a3b8; font-size: 12pt; }
.answers { break-before: page; }
.answers h2 { color: #15803d; }
.tag { display: inline-block; font-size: 8.5pt; color: #1e3a8a; background: #dbeafe; border-radius: 4px;
  padding: 0 5px; font-weight: 600; }
hr { border: 0; border-top: 1px solid var(--line); margin: 14pt 0; }
""" % {"pack": PACK}


def fig(m):
    parts = m.group(1).split("|")
    name = parts[0].strip()
    cap = parts[1].strip() if len(parts) > 1 else ""
    w = 100
    for p in parts[2:]:
        if p.strip().startswith("w="):
            w = int(p.strip()[2:])
    svg = figures.ALL[name]()
    svg = re.sub(r'<\?xml[^>]*\?>', "", svg)
    cap_html = f"<figcaption>{inline(cap)}</figcaption>" if cap else ""
    return f'\n<figure style="max-width:{w}%">{svg}{cap_html}</figure>\n'


def fmap(m):
    body, *opts = m.group(1).split("|")
    here = 0
    for o in opts:
        if o.strip().startswith("here="):
            here = int(o.strip()[5:])
    nodes = [n.strip() for n in body.split(">")]
    out = []
    for k, n in enumerate(nodes, 1):
        cls = "n here" if k == here else "n"
        out.append(f'<span class="{cls}">{inline(n)}</span>')
    return '\n<div class="map">' + '<span class="a">→</span>'.join(out) + "</div>\n"


def inline(t):
    # sub/sup first, so a fraction's braces no longer contain nested braces
    t = re.sub(r"_\{([^{}]*)\}", r"<sub>\1</sub>", t)
    t = re.sub(r"\^\{([^{}]*)\}", r"<sup>\1</sup>", t)
    for _ in range(3):
        t = re.sub(r"\\sqrt\{([^{}]*)\}", r"√(\1)", t)
        t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}",
                   r'<span class="frac"><span>\1</span><span>\2</span></span>', t)
    return t


BOX_TITLES = {"q": "Question", "guess": "Guess first", "check": "Check", "trap": "Trap",
              "note": "Note", "key": "Key idea"}


def boxes(text):
    def rep(m):
        kind, title = m.group(1), m.group(2).strip()
        head = title or BOX_TITLES[kind]
        return f'<div class="box {kind}" markdown="1">\n<div class="bh">{inline(head)}</div>\n\n{m.group(3)}\n\n</div>'
    return re.sub(r"^:::(\w+)[ \t]*(.*?)\n(.*?)\n:::[ \t]*$", rep, text, flags=re.S | re.M)


def render(md_text):
    t = md_text
    stash = []

    def keep(m):
        stash.append(fig(m))
        return f"\n\nFIGTOKEN{len(stash) - 1}X\n\n"
    t = re.sub(r"\[\[fig:(.*?)\]\]", keep, t)
    t = re.sub(r"\[\[map:(.*?)\]\]", fmap, t)
    t = re.sub(r"^\$\$(.*?)\$\$[ \t]*$",
               lambda m: '<div class="eq">' + re.sub(r" {2,}", "&emsp;&emsp;&emsp;",
                                                     inline(m.group(1).strip())) + "</div>",
               t, flags=re.M)
    t = boxes(t)
    t = inline(t)
    t = t.replace("<!--ANSWERS-->", '<div class="answers" markdown="1">').replace("<!--/ANSWERS-->", "</div>")
    h = markdown.markdown(t, extensions=["tables", "md_in_html", "attr_list", "sane_lists"])
    for k, f in enumerate(stash):
        h = h.replace(f"<p>FIGTOKEN{k}X</p>", f).replace(f"FIGTOKEN{k}X", f)
    return h


def page(title, body):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{CSS}</style></head><body>{body}</body></html>"""


def to_pdf(html_path, pdf_path):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", html_path.as_uri()],
                   check=True, capture_output=True, timeout=120)


def main():
    HTML.mkdir(exist_ok=True)
    PDF.mkdir(exist_ok=True)
    merged = PdfWriter()
    for md in sorted(CONTENT.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip()
        html_path = HTML / (md.stem + ".html")
        html_path.write_text(page(title, render(text)), encoding="utf-8")
        pdf_path = PDF / (md.stem + ".pdf")
        to_pdf(html_path, pdf_path)
        n = len(PdfReader(str(pdf_path)).pages)
        start = len(merged.pages)
        merged.append(str(pdf_path))
        merged.add_outline_item(title, start)
        print(f"{md.stem}: {n} pages")
    out = PDF / "ECE2107-Circuits-and-Systems-study-pack.pdf"
    with open(out, "wb") as f:
        merged.write(f)
    print("combined:", out.name, len(merged.pages), "pages")


if __name__ == "__main__":
    main()
