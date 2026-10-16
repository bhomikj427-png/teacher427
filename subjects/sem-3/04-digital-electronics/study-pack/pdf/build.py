"""Build DE-v1.pdf: content.html + figs.py -> DE-v1.html -> headless Chrome -> DE-v1.pdf.

Run:  python verify.py && python build.py
"""
import re
import subprocess
from pathlib import Path

import figs

HERE = Path(__file__).resolve().parent
SITE_CSS = HERE.parents[4] / "site" / "static" / "style.css"
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]

# K-map classes from the site stylesheet (the renderer is shared), light theme only.
kcss = "\n".join(l for l in SITE_CSS.read_text(encoding="utf-8").splitlines()
                 if l.lstrip().startswith((".k-", ".c0", ".c1", ".c2", ".c3", ".c4", ".fig-svg")))

CSS = """
:root { --bg:#ffffff; --card:#ffffff; --ink:#1c1f24; --muted:#6a707a; --line:#e3e3de; --soft:#f4f4f0;
  --accent:#2f5bea; --accent-soft:#eef2fe; --g0:#2f5bea; --g1:#e0661b; --g2:#12925a; --g3:#b23fbf; --g4:#c2410c;
  --one:#1c1f24; --zero:#b7bac0; --x:#d97706; --bad:#d92d20; --good:#12925a; }
@page { size: A4; margin: 15mm 15mm 16mm 15mm; }
* { box-sizing: border-box; }
body { margin: 0; color: var(--ink); background: #fff; font: 10.4pt/1.5 "Segoe UI", Inter, system-ui, sans-serif;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1 { font-size: 21pt; line-height: 1.15; margin: 0 0 8px; letter-spacing: -.01em; }
h2 { font-size: 14pt; margin: 2px 0 8px; color: var(--ink); break-after: avoid; }
h3 { font-size: 11.5pt; margin: 14px 0 6px; color: var(--accent); break-after: avoid; }
p { margin: 6px 0; }
code { font: 9pt Consolas, monospace; background: var(--soft); padding: 0 4px; border-radius: 4px; }
sub { font-size: 72%; }
.cover { min-height: 255mm; display: flex; flex-direction: column; justify-content: center; break-after: page; }
.kicker { color: var(--muted); font-size: 10pt; letter-spacing: .04em; text-transform: uppercase; margin-bottom: 6px; }
.cover h1 { font-size: 30pt; } .sub { font-size: 12pt; color: var(--muted); max-width: 150mm; margin-bottom: 18px; }
.cover .fig { width: 100%; } .cover .fig svg.mpl { max-height: none; }
.two.asm { grid-template-columns: 1.1fr 1fr; } .two.asm svg.mpl { max-height: 150mm; }
.two.hz { display: block; } .two.hz svg.mpl { max-height: 55mm; width: 75%; } .two.hz .fig-svg { max-width: 300px !important; }
.legend { border-collapse: collapse; margin: 18px 0 10px; } .legend td { padding: 4px 10px 4px 0; vertical-align: top; }
.tag { display: inline-block; font-size: 8pt; font-weight: 700; padding: 1px 8px; border-radius: 99px; color: #fff; }
.tag.q { background: var(--accent); } .tag.g { background: var(--g1); } .tag.c { background: var(--g2); }
.fine { font-size: 8.8pt; color: var(--muted); }
.part { break-before: page; border-left: 5px solid var(--accent); padding: 4px 0 4px 16px; margin: 0 0 14px; }
.part-no { color: var(--accent); font-weight: 700; text-transform: uppercase; letter-spacing: .08em; font-size: 9.5pt; }
.lead { color: var(--muted); }
.concept { margin: 0 0 18px; padding-top: 4px; border-top: 1px solid var(--line); }
.concept + .concept { break-before: auto; }
.path { color: var(--muted); font-size: 8.5pt; text-transform: uppercase; letter-spacing: .06em; margin-top: 8px; }
.q { background: var(--accent-soft); border-left: 3px solid var(--accent); padding: 8px 12px; border-radius: 0 8px 8px 0;
  margin: 8px 0 4px; font-size: 10.6pt; break-inside: avoid; }
.src { display: block; font-size: 8pt; color: var(--accent); font-weight: 600; letter-spacing: .02em; margin-bottom: 2px; }
.mock .src { display: inline; margin-left: 6px; font-weight: 500; }
.guess { color: var(--g1); font-weight: 700; font-size: 9.5pt; margin: 2px 0 10px; }
.guess::before { content: "✎ "; }
.ans { background: #f2faf6; border-left: 3px solid var(--g2); padding: 8px 12px; border-radius: 0 8px 8px 0; margin: 10px 0;
  break-inside: avoid; }
.check { border: 1.5px dashed var(--g2); padding: 7px 12px; border-radius: 8px; margin: 10px 0; font-size: 10pt; break-inside: avoid; }
.eq { font-weight: 600; font-size: 11pt; }
.fig { margin: 8px auto; text-align: center; break-inside: avoid; }
.fig svg { max-width: 100%; height: auto; }
.fig svg.mpl { width: 100%; max-height: 92mm; }
.fig.narrow svg.mpl { max-height: 140mm; }
.fig.center { display: flex; flex-direction: column; align-items: center; }
.img { display: block; margin: 0 auto; width: 100%; }
.prov { font-size: 7.8pt; color: var(--muted); margin-top: 3px; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; align-items: start; break-inside: avoid; }
table.data, table.recall { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.6pt; break-inside: avoid; }
table.data th, table.data td, table.recall th, table.recall td { border-bottom: 1px solid var(--line); padding: 4px 8px; text-align: left; vertical-align: top; }
table.data th, table.recall th { background: var(--soft); font-weight: 600; }
table.recall td:first-child { width: 30%; font-weight: 600; }
table.recall td:last-child { color: var(--ink); }
table.mono td { font-family: Consolas, "JetBrains Mono", monospace; font-size: 9.4pt; }
.two table.data { margin-top: 0; }
ol.steps li, ul.tight li { margin: 3px 0; }
.answers { background: var(--soft); border-radius: 10px; padding: 6px 16px 8px; margin: 18px 0; break-inside: avoid; }
.answers h3 { color: var(--g2); }
.answers li { margin: 4px 0; }
.sources { font-size: 9pt; color: var(--muted); border-top: 1px solid var(--line); margin-top: 20px; }
.sources li { margin: 3px 0; }
"""


def render():
    src = (HERE / "content.html").read_text(encoding="utf-8")
    ns = {k: getattr(figs, k) for k in dir(figs) if not k.startswith("_")}
    body = re.sub(r"\{\{(.+?)\}\}", lambda m: eval(m.group(1).strip(), ns), src, flags=re.S)
    html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Digital Electronics ETE pack v1</title>'
            f"<style>{kcss}\n{CSS}</style></head><body>{body}</body></html>")
    out = HERE / "DE-v1.html"
    out.write_text(html, encoding="utf-8")
    return out


def pdf(html):
    exe = next(c for c in CHROME if Path(c).exists())
    target = HERE / "DE-v1.pdf"
    subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={target}", html.as_uri()], check=True, capture_output=True)
    return target


if __name__ == "__main__":
    print(pdf(render()))
