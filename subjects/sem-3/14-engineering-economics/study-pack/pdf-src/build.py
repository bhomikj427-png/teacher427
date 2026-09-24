"""Build the MEE2003 study pack PDF: ../*.md (source, unchanged) -> html/ -> pdf/ + one combined PDF.

Run: python build.py      Needs: markdown, matplotlib, pypdf, Google Chrome.
- The first ``` block under "## Map" (00: under "## The path") is replaced by a Mermaid flowchart (MAPS).
- Concept figures (figures.py) are inserted at the END of the named section (FIGS), so the question
  and the guess still come before the picture.
"""
import re
import subprocess
from pathlib import Path

import markdown
from pypdf import PdfReader, PdfWriter

import figures

HERE = Path(__file__).resolve().parent
PACK = HERE.parent
HTML, PDF = HERE / "html", PACK / "pdf"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
MERMAID = (HERE / "mermaid.min.js").read_text(encoding="utf-8")

MAPS = {
    "00-START-HERE": """flowchart TB
  subgraph R1[" "]
    direction LR
    A["01 Basics · demand · supply<br/>L1–3"] --> B["02 Equilibrium · tax<br/>L4–5 ✎"] --> C["03 Elasticity<br/>L6–7 ✎"] --> D["04 Decision making<br/>L8–9"] --> E["05 Estimates<br/>L10–12"]
  end
  subgraph R2[" "]
    direction LR
    F["06 EOQ<br/>L13 ✎"] --> G["07 Payback + ROR<br/>L14 ✎"] --> H["08 TVM + NPV<br/>L15–17 ★"] --> I["09 IRR<br/>L18–19 ✎"] --> J["10 Mock MTE"]
  end
  R1 --> R2
  K["L20–24 cost · LCC · break-even — ⚠ not uploaded yet"]:::miss
  R2 -.- K
  classDef miss fill:#fef2f2,stroke:#dc2626,color:#991b1b
  style H fill:#dbeafe,stroke:#1d4ed8
  style R1 fill:#ffffff,stroke:#ffffff
  style R2 fill:#ffffff,stroke:#ffffff""",
    "01-economics-basics-and-demand-supply": """flowchart LR
  S["Scarcity"] --> E["Economics =<br/>choice under scarcity"]
  E --> M["Micro vs Macro"]
  E --> G["Economic goals"]
  E --> Y["Systems: capitalist ·<br/>socialist · mixed"]
  S --> P["PPC"]
  S --> EE["Engineering economics:<br/>technical vs economic efficiency"]
  S --> D["Demand"] --> DD["Determinants"] --> L["Law of demand<br/>(SE + IE)"] --> C["Δ demand vs<br/>Δ quantity demanded"]
  S --> SU["Supply"] --> LS["Law of supply"] --> SD["Determinants"]""",
    "02-equilibrium-tax-subsidy": """flowchart LR
  A["Demand eqn +<br/>supply eqn"] --> B["Qd = Qs →<br/>P* then Q*"]
  B --> T["TAX T: supply uses (P − T)"] --> T2["P′, Q′ · revenue = T·Q′<br/>seller gets P′ − T"]
  B --> S["SUBSIDY S: demand uses (P − S)"] --> S2["P′, Q′ · subsidy = S·Q′<br/>buyer pays P′ − S"]
  B --> F["Factor cost changes"] --> F2["supply curve shifts →<br/>re-solve"]""",
    "03-elasticity-of-demand": """flowchart LR
  E["E = %ΔQ / %ΔX<br/>= (ΔQ/ΔX)·(X/Q)"] --> P["Price Eₚ<br/>5 degrees"]
  E --> I["Income Eᵧ<br/>luxury / necessity / inferior"]
  E --> C["Cross Eₓᵧ<br/>substitute / complement"]
  E --> A["Promotional Eₐ<br/>is advertising worth it?"]""",
    "04-economic-decision-making": """flowchart LR
  D["Economic decision:<br/>best alternative under constraints"] --> P["Process<br/>5-step · 9-step rational"]
  D --> K["Key elements<br/>scarcity · opportunity cost · marginal ·<br/>incentives · trade-offs · rationality"]
  D --> T["Types<br/>programmed vs non-programmed"]
  D --> I["Importance in projects<br/>+ influencing factors"]
  D --> N["Numericals<br/>car (total cost) · cloud (EAC)"]""",
    "05-types-of-estimates": """flowchart LR
  E["Estimate: predict cost/time<br/>before the project"] --> R["ROM<br/>−50%…+100%"] --> B["Budget"] --> DF["Definitive<br/>−5%…+10%"]
  E --> T["Techniques"]
  T --> PA["Parametric<br/>rate × quantity"]
  T --> AN["Analogous<br/>old × new/old size"]
  T --> BU["Bottom-up<br/>Σ tasks + contingency"]""",
    "06-EOQ-inventory": """flowchart TB
  I["Inventory"] --> D["Demand:<br/>dependent / independent"]
  I --> C["Costs: ordering S ·<br/>holding H · shortage"]
  I --> S["Control: continuous<br/>vs periodic"]
  I --> E["EOQ model"] --> TC["TC = DC + (D/Q)S + (Q/2)H"] --> Q["Q* = √(2DS/H)"]
  Q --> O["orders = D/Q* · cycle = Q*/D<br/>ROP = demand rate × lead time"]""",
    "07-payback-and-ROR": """flowchart LR
  P["Payback = time to<br/>recover investment"] --> E["Even flow:<br/>investment / annual inflow"]
  P --> U["Uneven flow: cumulative table<br/>years before + unrecovered/next flow"]
  P --> DC["Decision:<br/>PB ≤ target → accept"]
  P --> PC["Pros/cons: simple ·<br/>ignores TVM & later flows"]
  P --> R["ROR = saving/investment = 1/PB"]""",
    "08-TVM-and-NPV": """flowchart TB
  T["₹1 today > ₹1 tomorrow"] --> F["F = P(1+i)ⁿ"] --> P["P = F/(1+i)ⁿ"]
  P --> A["Annuity: P = A·[1 − (1+i)⁻ⁿ]/i"]
  A --> N["NPV = Σ Fₙ/(1+i)ⁿ − F₀"]
  N --> D1[">0 accept · <0 reject"]
  N --> D2["projects:<br/>higher NPV"]
  N --> D3["costs only:<br/>lower PV"]
  N --> D4["effect of<br/>discount rate"]""",
    "09-IRR": """flowchart TB
  I["IRR = rate where NPV = 0"] --> T["Trial rates:<br/>one NPV +, one NPV −"] --> X["Interpolate<br/>i₁ + (i₂−i₁)·y₁/(y₁−y₂)"]
  X --> D["IRR > required rate → accept"]
  I --> V["NPV (₹) vs IRR (%)"]""",
}

FIGS = {  # file stem -> [(section heading prefix, figure, caption)]
    "01-economics-basics-and-demand-supply": [
        ("## 2.", "ppc", "PPC: growth shifts it out, lost resources shift it in, a point inside means idle resources."),
        ("## 6.", "demand_shift", "Left: a movement along the curve (own price). Right: shifts of the whole curve (any other factor)."),
    ],
    "02-equilibrium-tax-subsidy": [("## 4.", "tax_p1", "Problem 1 drawn to scale: the tax shifts supply up by ₹1.20, but the price rises only ₹0.96.")],
    "03-elasticity-of-demand": [("## 2.", "elasticity_degrees", "The five degrees of price elasticity.")],
    "04-economic-decision-making": [("## 6.", "cloud_eac", "Cloud hosting at 10%: B's upfront cost, annualized, makes B dearer than A.")],
    "05-types-of-estimates": [("## 3.", "estimate_accuracy", "Accuracy ranges from the slides: ROM vs definitive.")],
    "06-EOQ-inventory": [("## 2.", "eoq_curve", "The EOQ trade-off, drawn with the battery problem's numbers (§5).")],
    "07-payback-and-ROR": [("## 3.", "payback_cumulative", "The cumulative inflow crosses the $200k investment during year 4.")],
    "08-TVM-and-NPV": [
        ("## 2.", "discounting", "$1000 received n years from now, valued today at 10%."),
        ("## 7.", "furnace_rate", "The furnace decision flips as the discount rate rises (the crossover is ≈ 15%)."),
    ],
    "09-IRR": [("## 3.", "npv_irr", "The machine's NPV against the discount rate. IRR is where the curve crosses zero, and the chord gives the interpolated value.")],
}

CSS = """
@page { size: A4; margin: 15mm 14mm; }
body { font-family: 'Segoe UI', Arial, sans-serif; color: #1f2937; font-size: 10.3pt; line-height: 1.5; margin: 0; }
h1 { font-size: 20pt; margin: 0 0 8pt; color: #111827; border-bottom: 3px solid #1d4ed8; padding-bottom: 4pt; }
h2 { font-size: 13.5pt; color: #1d4ed8; border-bottom: 1.5px solid #e5e7eb; padding-bottom: 3pt; margin: 16pt 0 7pt; break-after: avoid; }
h3 { font-size: 11.5pt; margin: 12pt 0 5pt; break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 7pt 0; font-size: 9.6pt; }
tr { break-inside: avoid; }
th { background: #eff6ff; color: #1e3a8a; text-align: left; }
th, td { border: 1px solid #dbe2ea; padding: 3.5pt 6pt; vertical-align: top; }
pre { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 7pt 10pt; font-size: 8.3pt;
      line-height: 1.4; break-inside: avoid; white-space: pre-wrap; }
code { font-family: Consolas, monospace; font-size: 9.2pt; background: #f3f4f6; padding: 0 3px; border-radius: 3px; }
pre code { background: none; padding: 0; }
blockquote { background: #eff6ff; border-left: 4px solid #1d4ed8; margin: 8pt 0; padding: 5pt 11pt; border-radius: 6px; break-inside: avoid; }
blockquote p { margin: 3pt 0; }
p.q { background: #fefce8; border-left: 4px solid #ca8a04; padding: 5pt 10pt; border-radius: 6px; break-inside: avoid; }
figure { margin: 10pt auto; text-align: center; break-inside: avoid; }
figure svg { max-width: 100%; height: auto; }
figcaption { font-size: 8.8pt; color: #6b7280; margin-top: 2pt; }
.mermaid { text-align: center; margin: 8pt 0 12pt; break-inside: avoid; }
.answers { break-before: page; }
h2.ans { color: #15803d; }
hr { border: 0; border-top: 1px solid #e5e7eb; margin: 12pt 0; }
"""


def tidy(text):
    """Join hard-wrapped quote lines (nl2br would keep them) and escape the * in Q*, i*."""
    out, fence = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            fence = not fence
        if not fence:
            line = re.sub(r"(?<=[A-Za-z])\*(?=[ ,.)=/²])", r"\\*", line)
            prev = out[-1] if out else ""
            if (line.startswith("> ") and prev.startswith("> ") and not line.startswith("> |")
                    and not prev.startswith("> |") and prev.strip() != ">" and not re.match(r"> \(?[ivx]+\)|> \([a-z]\)", line)):
                out[-1] = prev + " " + line[2:]
                continue
            # join prose that was hard-wrapped (long previous line); keep short, deliberate breaks
            block = re.match(r"\s*([#|>`]|[-*] |\d+\. |<)", line)
            pblock = re.match(r"\s*([#|`]|<)", prev)
            if line.strip() and prev.strip() and not block and not pblock and len(prev) >= 95:
                out[-1] = prev + " " + line.strip()
                continue
        out.append(line)
    return "\n".join(out)


def build_md(stem, text):
    text = tidy(text)
    anchor = "## The path" if stem == "00-START-HERE" else "## Map"
    if stem in MAPS and anchor in text:
        i = text.index(anchor)
        j = text.index("```", i)
        k = text.index("```", j + 3) + 3
        text = text[:j] + f'<div class="mermaid">\n{MAPS[stem]}\n</div>' + text[k:]
    for head, name, cap in FIGS.get(stem, []):
        i = text.index("\n" + head) + 1
        nxt = re.search(r"\n## |\n---\n", text[i + 3:])
        pos = i + 3 + nxt.start() if nxt else len(text)
        tok = f"\n\nFIG::{name}::{cap}\n\n"
        text = text[:pos] + tok + text[pos:]
    return text


def to_html(stem, text):
    stash = {}

    def keep_mermaid(m):
        stash[f"MERMAID{len(stash)}"] = m.group(0)
        return f"\n\nMERMAID{len(stash) - 1}\n\n"
    text = re.sub(r'<div class="mermaid">.*?</div>', keep_mermaid, text, flags=re.S)
    h = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "nl2br"])
    for k, v in stash.items():
        h = h.replace(f"<p>{k}</p>", v)
    h = re.sub(r"<p>FIG::(\w+)::(.*?)</p>",
               lambda m: f'<figure>{figures.ALL[m.group(1)]()}<figcaption>{m.group(2)}</figcaption></figure>', h)
    h = h.replace("<p><strong>Q ▸</strong>", '<p class="q"><strong>Q ▸</strong>')
    h = re.sub(r"<h2>(Answers)</h2>", r'<div class="answers"></div><h2 class="ans">\1</h2>', h)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style>
<script>{MERMAID}</script>
<script>mermaid.initialize({{startOnLoad:true, theme:'base', flowchart:{{useMaxWidth:true, htmlLabels:true}},
themeVariables:{{fontFamily:'Segoe UI, Arial', fontSize:'13px', primaryColor:'#f8fafc', primaryBorderColor:'#94a3b8',
lineColor:'#64748b', primaryTextColor:'#1f2937'}}}});</script></head><body>{h}</body></html>"""


def main():
    HTML.mkdir(exist_ok=True)
    PDF.mkdir(exist_ok=True)
    merged = PdfWriter()
    for md in sorted(PACK.glob("[0-9][0-9]-*.md")):
        text = md.read_text(encoding="utf-8")
        title = text.splitlines()[0].lstrip("# ").strip()
        hp = HTML / f"{md.stem}.html"
        hp.write_text(to_html(md.stem, build_md(md.stem, text)), encoding="utf-8")
        pp = HTML / f"{md.stem}.pdf"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--run-all-compositor-stages-before-draw", "--virtual-time-budget=15000",
                        f"--print-to-pdf={pp}", hp.as_uri()], check=True, capture_output=True, timeout=180)
        start = len(merged.pages)
        merged.append(str(pp))
        merged.add_outline_item(title, start)
        print(md.stem, len(PdfReader(str(pp)).pages), "pages")
    out = PDF / "MEE2003-Engineering-Economics-study-pack.pdf"
    with open(out, "wb") as f:
        merged.write(f)
    print("combined:", out, len(merged.pages), "pages")


if __name__ == "__main__":
    main()
