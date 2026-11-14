"""Build DE-ETE-v1.pdf: parts/*.html + figs*.py -> DE-ETE-v1.html -> headless Chrome -> DE-ETE-v1.pdf.

Run:  python verify.py && python build.py          (build.py [prefix...] builds only parts whose name starts so)
Same format as ../../../03-electronic-devices-1/study-pack/pdf (EDC-ETE-v1): Q -> guess -> figure -> answer -> Check.
"""
import importlib
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAME = "DE-ETE-v1"
SITE_CSS = HERE.parents[4] / "site" / "static" / "style.css"
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]

# K-map classes from the site stylesheet (the K-map renderer is shared with the site), light theme only.
KCSS = "\n".join(l for l in SITE_CSS.read_text(encoding="utf-8").splitlines()
                 if l.lstrip().startswith((".k-", ".c0", ".c1", ".c2", ".c3", ".c4", ".fig-svg")))

CSS = KCSS + """
:root { --bg:#fff; --card:#fff; --ink:#1c1f24; --muted:#6a707a; --line:#e3e3de; --soft:#f4f4f0; --accent:#2f5bea; --accent-soft:#eef2fe;
  --g0:#2f5bea; --g1:#e0661b; --g2:#12925a; --g3:#b23fbf; --g4:#c2410c; --one:#1c1f24; --zero:#b7bac0; --x:#d97706; --bad:#d92d20; --good:#12925a; }
@page { size: A4; margin: 15mm 15mm 16mm 15mm; }
* { box-sizing: border-box; }
body { margin: 0; color: var(--ink); background: #fff; font: 10.4pt/1.5 "Segoe UI", Inter, system-ui, sans-serif;
  -webkit-print-color-adjust: exact; print-color-adjust: exact; }
h1 { font-size: 21pt; line-height: 1.15; margin: 0 0 8px; letter-spacing: -.01em; }
h2 { font-size: 14pt; margin: 2px 0 8px; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 14px 0 6px; color: var(--accent); break-after: avoid; }
p { margin: 6px 0; }
code { font: 9pt Consolas, monospace; background: var(--soft); padding: 0 4px; border-radius: 4px; }
sub, sup { font-size: 72%; line-height: 0; }
.cover { min-height: 255mm; display: flex; flex-direction: column; justify-content: center; break-after: page; }
.kicker { color: var(--muted); font-size: 10pt; letter-spacing: .04em; text-transform: uppercase; margin-bottom: 6px; }
.cover h1 { font-size: 30pt; } .sub { font-size: 12pt; color: var(--muted); max-width: 160mm; margin-bottom: 14px; }
.cover .fig { width: 100%; }
.head { break-inside: avoid; break-after: avoid; }
.legend { border-collapse: collapse; margin: 14px 0 8px; } .legend td { padding: 4px 10px 4px 0; vertical-align: top; }
.tag { display: inline-block; font-size: 8pt; font-weight: 700; padding: 1px 8px; border-radius: 99px; color: #fff; }
.tag.q { background: var(--accent); } .tag.g { background: var(--g1); } .tag.c { background: var(--g2); }
.fine { font-size: 8.8pt; color: var(--muted); }
.part { break-before: page; border-left: 5px solid var(--accent); padding: 4px 0 4px 16px; margin: 0 0 14px; }
.part-no { color: var(--accent); font-weight: 700; text-transform: uppercase; letter-spacing: .08em; font-size: 9.5pt; }
.lead { color: var(--muted); }
.concept { margin: 0 0 16px; padding-top: 4px; border-top: 1px solid var(--line); }
.path { color: var(--muted); font-size: 8.5pt; text-transform: uppercase; letter-spacing: .06em; margin-top: 8px; }
.q { background: var(--accent-soft); border-left: 3px solid var(--accent); padding: 8px 12px; border-radius: 0 8px 8px 0;
  margin: 8px 0 4px; font-size: 10.6pt; break-inside: avoid; }
.src { display: block; font-size: 8pt; color: var(--accent); font-weight: 600; letter-spacing: .02em; margin-bottom: 2px; }
.mock .src { display: inline; margin-left: 6px; font-weight: 500; }
.guess { color: var(--g1); font-weight: 700; font-size: 9.5pt; margin: 2px 0 10px; }
.guess::before { content: "✎ "; }
.terms { background: var(--soft); border-radius: 8px; padding: 6px 12px; margin: 8px 0; font-size: 9.8pt; break-inside: avoid; }
.terms b { color: var(--accent); }
.ans { background: #f2faf6; border-left: 3px solid var(--g2); padding: 8px 12px; border-radius: 0 8px 8px 0; margin: 10px 0;
  break-inside: avoid; }
.warn { background: #fff4f2; border-left: 3px solid var(--bad); padding: 6px 12px; border-radius: 0 8px 8px 0; margin: 8px 0;
  font-size: 9.8pt; break-inside: avoid; }
.check { border: 1.5px dashed var(--g2); padding: 7px 12px; border-radius: 8px; margin: 10px 0; font-size: 10pt; break-inside: avoid; }
.eq { font-weight: 600; font-size: 11pt; text-align: center; margin: 6px 0; }
.fig { margin: 8px auto; text-align: center; break-inside: avoid; }
.fig svg { max-width: 100%; height: auto; }
.fig svg.mpl { width: 100%; max-height: 92mm; }
.fig.small svg.mpl { max-height: 62mm; } .fig.tall svg.mpl { max-height: 150mm; }
.fig .fig-svg, .two .fig-svg { margin: 0 auto; }
.img { display: block; margin: 0 auto; width: 100%; }
.prov { font-size: 7.8pt; color: var(--muted); margin-top: 3px; text-align: center; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; align-items: center; break-inside: avoid; }
.two.top { align-items: start; }
.two > *, .three > * { min-width: 0; }
.two > .fig, .three > .fig { margin: 0; }
.two.asm { grid-template-columns: 1fr 1.15fr; }
.two.w31 { grid-template-columns: 1.6fr 1fr; } .two.w13 { grid-template-columns: 1fr 1.6fr; }
.three { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; align-items: center; break-inside: avoid; }
.two svg, .three svg { max-width: 100%; height: auto; } .two svg.mpl { width: 100%; max-height: 80mm; } .three svg.mpl { width: 100%; max-height: 60mm; }
.two.asm svg.mpl { max-height: 150mm; }
table.data, table.recall { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.6pt; break-inside: avoid; }
table.data th, table.data td, table.recall th, table.recall td { border-bottom: 1px solid var(--line); padding: 4px 8px; text-align: left; vertical-align: top; }
table.data th, table.recall th { background: var(--soft); font-weight: 600; }
table.recall td:first-child { width: 30%; font-weight: 600; }
table.recall { break-inside: auto; } table.recall tr { break-inside: avoid; }
table.mono td { font-family: Consolas, monospace; font-size: 9.4pt; }
table.tt { width: auto; margin: 8px auto; } table.tt td, table.tt th { text-align: center; padding: 2px 10px; }
.two table.data { margin-top: 0; }
ol.steps li, ul.tight li { margin: 3px 0; }
ol.steps, ul.tight { margin: 6px 0; padding-left: 22px; }
.answers { background: var(--soft); border-radius: 10px; padding: 6px 16px 8px; margin: 18px 0; }
.answers h3 { color: var(--g2); }
.answers li { margin: 4px 0; }
.sources { font-size: 9pt; color: var(--muted); border-top: 1px solid var(--line); margin-top: 20px; }
.sources li { margin: 3px 0; }
"""


def namespace():
    ns = {}
    for mod in sorted(p.stem for p in HERE.glob("figs*.py")):
        m = importlib.import_module(mod)
        ns.update({k: getattr(m, k) for k in dir(m) if not k.startswith("_")})
    return ns


def render(prefixes=()):
    ns = namespace()
    parts = sorted((HERE / "parts").glob("*.html"))
    if prefixes:
        parts = [p for p in parts if p.name.startswith(tuple(prefixes))]
    src = "\n".join(p.read_text(encoding="utf-8") for p in parts)

    def sub(m):
        try:
            return eval(m.group(1).strip(), ns)
        except Exception as e:
            raise RuntimeError(f"figure {m.group(1).strip()!r} failed: {e!r}") from e
    src = re.sub(r'(<div class="path">.*?<div class="guess">.*?</div>)', r'<div class="head">\1</div>', src, flags=re.S)
    body = re.sub(r"\{\{(.+?)\}\}", sub, src, flags=re.S)
    html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Digital Electronics: ETE pack v1</title>'
            f"<style>{CSS}</style></head><body>{body}</body></html>")
    out = HERE / (NAME + ("" if not prefixes else "-partial") + ".html")
    out.write_text(html, encoding="utf-8")
    return out


def pdf(html):
    exe = next(c for c in CHROME if Path(c).exists())
    target = html.with_suffix(".pdf")
    subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={target}", html.as_uri()], check=True, capture_output=True)
    return target


if __name__ == "__main__":
    sys.path.insert(0, str(HERE))
    print(pdf(render(sys.argv[1:])))
