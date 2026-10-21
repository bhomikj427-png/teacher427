"""Build v2 of the theorems assignment: content-v2/*.md -> html/ + pdf/ (separate files; v1 untouched).

Same syntax as build.py, plus a step block:

  :::step
  @how
  $$ working $$          (the literal solution step)
  @what one line: what we did and where (e.g. "KCL at node X")
  @why the reasoning that transfers to other questions
  :::

Fading rule (learner-set 2026-10-21): the first questions carry How/What/Why on every step; after that,
What/Why appear only on steps that use an idea from the "What's new" box; plain working stays bare.

Run:  python build_v2.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402  (reuses render, CSS, page, to_pdf)
from pypdf import PdfReader  # noqa: E402

CONTENT = HERE / "content-v2"
OUT_NAME = "ECE2107-Theorems-v2-demo-superposition"

CSS_V2 = """
.st { border-left: 3px solid #cbd5e1; margin: 9pt 0; padding: 1pt 0 1pt 9pt; break-inside: avoid; }
.st .row { display: grid; grid-template-columns: 36pt 1fr; column-gap: 6pt; margin: 3pt 0; }
.st .lab { font-size: 7.6pt; font-weight: 800; letter-spacing: .6pt; padding-top: 3pt; }
.st .bd > p { margin: 1pt 0; }
.st .bd .eq { margin: 3pt 0; padding: 4pt; text-align: left; }
.st .how .lab { color: #374151; }
.st .what .lab { color: #1d4ed8; }
.st .what .bd { color: #1e3a8a; font-size: 9.8pt; }
.st .why .lab { color: #b45309; }
.st .why .bd { color: #78350f; font-size: 9.8pt; background: #fffbeb; border-radius: 4px; padding: 1pt 6pt; }
.howto { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 7px; padding: 7pt 11pt; margin: 9pt 0; }
.howto .bh { font-weight: 700; font-size: 9.5pt; text-transform: uppercase; letter-spacing: .4pt; color: #334155; }
"""

LABELS = {"how": "HOW", "what": "WHAT", "why": "WHY"}


def steps(text):
    """Turn each :::step block into How / What / Why rows (markdown kept inside each row)."""
    def rep(m):
        rows = re.split(r"^@(how|what|why)[ \t]*", m.group(1), flags=re.M)
        out = ['<div class="st" markdown="1">']
        for kind, body in zip(rows[1::2], rows[2::2]):
            out.append(f'<div class="row {kind}" markdown="1">\n<div class="lab">{LABELS[kind]}</div>\n'
                       f'<div class="bd" markdown="1">\n\n{body.strip()}\n\n</div>\n</div>')
        out.append("</div>")
        return "\n".join(out)
    return re.sub(r"^:::step[ \t]*\n(.*?)\n:::[ \t]*$", rep, text, flags=re.S | re.M)


def main():
    build.HTML.mkdir(exist_ok=True)
    build.PDF.mkdir(exist_ok=True)
    bodies = [build.render(steps(md.read_text(encoding="utf-8"))) for md in sorted(CONTENT.glob("*.md"))]
    body = '<div class="pb"></div>'.join(bodies)
    html = build.page("Theorems v2 demo", body).replace("</style>", CSS_V2 + "</style>", 1)
    html_path = build.HTML / f"{OUT_NAME}.html"
    html_path.write_text(html, encoding="utf-8")
    out = build.PDF / f"{OUT_NAME}.pdf"
    build.to_pdf(html_path, out)
    print("built:", out.name, len(PdfReader(str(out)).pages), "pages")


if __name__ == "__main__":
    main()
