"""Build the DSA lab "to-write" file (record write-up): to-write.md -> ../../pdf/ECE2132-DSA-Lab-to-write.pdf

Run:  python build_record.py      (after ../verify.py, which produces the outputs quoted here)
Reuses ../build.py's renderer. Extra syntax: ```mermaid ... ``` blocks become flowcharts (Mermaid 10.9.1, CDN).
Programs come from ../code/ with the pack-only "FIX:" comments removed (the code itself is unchanged).
"""
import html
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import build  # noqa: E402

MERMAID = "https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"
OUT_HTML = build.HTML / "to-write.html"
OUT_PDF = build.PDF / "ECE2132-DSA-Lab-to-write.pdf"

_orig_src = build._src


def clean_src(name):
    src = _orig_src(name)
    src = re.sub(r"[ \t]*// FIX:.*$", "", src, flags=re.M)        # drop pack-only fix notes
    return re.sub(r"\n{3,}", "\n\n", src)


build._src = clean_src

EXTRA_CSS = """
h1 { font-size: 19pt; }
h2.exp { break-before: page; font-size: 15pt; color: #111827; border-bottom: 2px solid #1d4ed8; margin-top: 0; }
h3 { color: #1d4ed8; font-size: 11pt; margin: 10pt 0 3pt; text-transform: uppercase; letter-spacing: .5pt; }
.flows { display: flex; flex-wrap: wrap; gap: 6pt 14pt; justify-content: space-around; align-items: flex-start; break-inside: avoid; }
.flows pre.mermaid { margin: 0; }
pre.mermaid { background: none; text-align: center; margin: 6pt 0; break-inside: avoid; }
pre.mermaid svg { max-height: 235mm; max-width: 100%; height: auto; }
.code pre { font-size: 8.6pt; }
"""


def main():
    text = (HERE / "to-write.md").read_text(encoding="utf-8")
    flows = []

    def keep(m):
        src = re.sub(r'"[^"]*"', lambda q: q.group(0).replace("&", "#amp;").replace("<", "#lt;")
                     .replace(">", "#gt;"), m.group(1).strip())         # Mermaid's own entity codes
        flows.append(f'<pre class="mermaid">{src}</pre>')
        return f"\n\nMERMAIDTOKEN{len(flows) - 1}X\n\n"
    text = re.sub(r"```mermaid\n(.*?)```", keep, text, flags=re.S)
    body = build.render(text)
    for k, f in enumerate(flows):
        body = body.replace(f"<p>MERMAIDTOKEN{k}X</p>", f).replace(f"MERMAIDTOKEN{k}X", f)
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>DSA Lab to-write</title>
<style>{build.CSS}{EXTRA_CSS}</style>
<script src="{MERMAID}"></script>
<script>mermaid.initialize({{ startOnLoad: true, theme: 'neutral', flowchart: {{ useMaxWidth: true, htmlLabels: true }},
  themeVariables: {{ fontSize: '13px' }} }});</script></head><body>{body}</body></html>"""
    page = page.replace(build.PACK, "ECE2132 DSA Lab · To-write (record)")
    OUT_HTML.write_text(page, encoding="utf-8")
    subprocess.run([build.CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=20000", f"--print-to-pdf={OUT_PDF}", OUT_HTML.as_uri()],
                   check=True, capture_output=True, timeout=180)
    from pypdf import PdfReader, PdfWriter
    r = PdfReader(str(OUT_PDF))
    w = PdfWriter()
    for p in r.pages:
        w.add_page(p)
    # bookmark each experiment: find the page where its heading text appears
    for title in re.findall(r"^## (Experiment .*?)\s*\{\.exp\}", text, flags=re.M):
        key = title.split("—")[0].strip()
        for i, p in enumerate(r.pages):
            if key + " " in (p.extract_text() or "") or key + "\n" in (p.extract_text() or ""):
                w.add_outline_item(title.replace("*", ""), i)
                break
    with open(OUT_PDF, "wb") as f:
        w.write(f)
    print(OUT_PDF.name, len(r.pages), "pages")


if __name__ == "__main__":
    main()
