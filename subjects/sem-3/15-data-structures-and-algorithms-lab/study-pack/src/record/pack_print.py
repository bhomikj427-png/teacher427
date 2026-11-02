"""Build the cut-and-paste print sheet: ../../pdf/ECE2132-DSA-Lab-to-print.pdf

Every flowchart, program part and output is one piece with a dashed cut border and a small label,
packed onto A4 pages (bottom-left first fit, only on the last two pages so pieces stay near their
experiment).
- Flowcharts: the manual's own images (flowcharts/expNN.*). Exp 1, 2, 9 have none in the manual,
  so their Mermaid charts from to-write.md are used.
- Programs: the verified files in ../code/ (pack-only "FIX:" and trailing notes removed), split at
  blank lines into parts that fit a page.
- Outputs: ../out/ from verify.py (menus shown once).
Run:  python pack_print.py      (after ../verify.py)
"""
import re
import subprocess
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import build  # noqa: E402

MM = 72 / 25.4
PAGE_W, PAGE_H = 210 * MM, 297 * MM
MARGIN, GAP, PAD, LABEL_H = 7 * MM, 3 * MM, 2 * MM, 4 * MM
MONO = r"C:\Windows\Fonts\consola.ttf"
SANS = r"C:\Windows\Fonts\segoeui.ttf"
CODE_PT, LINE = 8.2, 8.2 * 1.17
MAX_LINES = 48                                   # one program part fits a page
TALL_FIRST = False
WINDOW = 4                                       # later pieces may fill gaps on the last 3 pages
OUT_PDF = build.PDF / "ECE2132-DSA-Lab-to-print.pdf"
MERMAID = "https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"
TMP = build.HTML / "_print_tmp"

# Display width (mm) of each manual flowchart: dense charts stay near page width so text stays readable.
FLOW_W = {3: 112, 4: 112, 5: 168, 6: 160, 7: 146, 8: 192, 10: 192, 11: 128, 12: 125}

EXPS = [  # (n, title, program file, output cases)
    (1, "Pointers", "e01_pointers.cpp", ["e01"]),
    (2, "Pointer arithmetic", "e02_pointer_arithmetic.cpp", ["e02"]),
    (3, "Array insertion", "e03_array_insert.cpp", ["e03_begin", "e03_pos", "e03_end"]),
    (4, "Array deletion", "e04_array_delete.cpp", ["e04_begin", "e04_pos", "e04_end"]),
    (5, "Matrix multiplication", "e05_matrix_multiply.cpp", ["e05"]),
    (6, "Matrix transpose", "e06_matrix_transpose.cpp", ["e06"]),
    (7, "Insertion sort", "e07_insertion_sort.cpp", ["e07"]),
    (8, "Quick sort + comparison", "e08_sort_compare.cpp", ["e08_compare"]),
    (9, "Stack (probable)", "e09_stack.cpp", ["e09"]),
    (10, "Queue", "e10_queue.cpp", ["e10"]),
    (11, "Singly linked list", "e11_singly_linked_list.cpp", ["e11"]),
    (12, "Circular linked list", "e12_circular_linked_list.cpp", ["e12"]),
]


# ------------------------------------------------------------------ text helpers
def strip_trailing_comment(line):
    """Drop a // note after code (not inside a string); keep full-line comments."""
    if line.strip().startswith("//"):
        return line
    k = line.find("//")
    while k != -1:
        if line[:k].count('"') % 2 == 0:
            return line[:k].rstrip()
        k = line.find("//", k + 2)
    return line


def program_lines(name):
    src = (build.CODE / name).read_text(encoding="utf-8")
    src = re.sub(r"[ \t]*// FIX:.*$", "", src, flags=re.M)
    lines = [strip_trailing_comment(l).rstrip() for l in src.strip("\n").split("\n")]
    out = []
    for l in lines:                                # collapse double blank lines
        if l == "" and out and out[-1] == "":
            continue
        out.append(l)
    return out


def split_parts(lines):
    """Split into equal-ish parts (each <= MAX_LINES), cutting at the blank line nearest each target."""
    import math
    n = math.ceil(len(lines) / MAX_LINES)
    if n == 1:
        return [lines]
    parts, start = [], 0
    for k in range(1, n):
        target = round(len(lines) * k / n)
        blanks = [i for i in range(start + 10, len(lines) - 10) if lines[i] == "" and i - start <= MAX_LINES]
        cut = min(blanks, key=lambda i: abs(i - target)) if blanks else target
        parts.append(lines[start:cut])
        start = cut + 1
    parts.append(lines[start:])
    return parts


def output_lines(case):
    txt = (build.OUT / f"{case}.txt").read_text(encoding="utf-8").strip("\n")
    txt, _ = build.collapse_menus(txt)
    return txt.split("\n")


# ------------------------------------------------------------------ mermaid charts (Exp 1, 2, 9)
def mermaid_sources(n):
    md = (HERE / "to-write.md").read_text(encoding="utf-8")
    sec = re.search(rf"## Experiment {n} —.*?(?=\n## Experiment |\Z)", md, re.S).group(0)
    flow = re.search(r"### Flowchart\n(.*?)### Program", sec, re.S).group(1)
    return re.findall(r"```mermaid\n(.*?)```", flow, re.S)


def render_mermaid(src, path):
    src = re.sub(r'"[^"]*"', lambda q: q.group(0).replace("&", "#amp;").replace("<", "#lt;").replace(">", "#gt;"),
                 src.strip())
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>@page {{ size: 400mm 600mm; margin: 5mm; }}
body {{ margin: 0; background: #fff; }}</style><script src="{MERMAID}"></script>
<script>mermaid.initialize({{ startOnLoad: true, theme: 'neutral', flowchart: {{ useMaxWidth: false, htmlLabels: true }},
themeVariables: {{ fontSize: '14px' }} }});</script></head><body><pre class="mermaid">{src}</pre></body></html>"""
    h = path.with_suffix(".html")
    h.write_text(html, encoding="utf-8")
    subprocess.run([build.CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=20000", f"--print-to-pdf={path}", h.as_uri()],
                   check=True, capture_output=True, timeout=180)
    d = pymupdf.open(str(path))
    p = d[0]
    box = pymupdf.Rect()
    for _, r in p.get_bboxlog():
        r = pymupdf.Rect(r)
        if r.width < p.rect.width * 0.95 and r.is_valid and not r.is_empty:
            box |= r
    return d, box


# ------------------------------------------------------------------ pieces
class Piece:
    def __init__(self, label, w, h, draw):
        self.label, self.w, self.h, self.draw = label, w + 2 * PAD, h + 2 * PAD + LABEL_H, draw


def text_piece(label, lines, boxed=False):
    font = pymupdf.Font(fontfile=MONO)
    width = max((font.text_length(l, fontsize=CODE_PT) for l in lines), default=10) + (4 if boxed else 0)
    height = len(lines) * LINE + (3 if boxed else 0)

    def draw(page, x, y):
        if boxed:
            page.draw_rect(pymupdf.Rect(x, y, x + width, y + height), color=(0.55, 0.55, 0.55), width=0.5)
        tw = pymupdf.TextWriter(page.rect)
        for i, l in enumerate(lines):
            tw.append((x + (2 if boxed else 0), y + (1.5 if boxed else 0) + (i + 0.8) * LINE), l,
                      font=font, fontsize=CODE_PT)
        tw.write_text(page, color=(0.07, 0.09, 0.15))
    return Piece(label, width, height, draw)


def image_piece(label, path, width_mm):
    pix = pymupdf.Pixmap(str(path))
    w = width_mm * MM
    h = w * pix.height / pix.width
    h_max = PAGE_H - 2 * MARGIN - 2 * PAD - LABEL_H
    if h > h_max:
        w, h = w * h_max / h, h_max

    def draw(page, x, y):
        page.insert_image(pymupdf.Rect(x, y, x + w, y + h), filename=str(path))
    return Piece(label, w, h, draw)


def pdf_piece(label, doc, clip, scale):
    w, h = clip.width * scale, clip.height * scale

    def draw(page, x, y):
        page.show_pdf_page(pymupdf.Rect(x, y, x + w, y + h), doc, 0, clip=clip)
    return Piece(label, w, h, draw)


# ------------------------------------------------------------------ packing
def fits(rects, r):
    if r.x1 > PAGE_W - MARGIN + 0.01 or r.y1 > PAGE_H - MARGIN + 0.01:
        return False
    return all(not (r.x0 < q.x1 + GAP - 0.01 and q.x0 < r.x1 + GAP - 0.01 and
                    r.y0 < q.y1 + GAP - 0.01 and q.y0 < r.y1 + GAP - 0.01) for q in rects)


def place(pages, piece):
    for page_rects in pages[-WINDOW:]:
        xs = sorted({MARGIN} | {q.x1 + GAP for q in page_rects})
        ys = sorted({MARGIN} | {q.y1 + GAP for q in page_rects})
        for y in ys:
            for x in xs:
                r = pymupdf.Rect(x, y, x + piece.w, y + piece.h)
                if fits(page_rects, r):
                    page_rects.append(r)
                    return pages.index(page_rects), r
    pages.append([])
    r = pymupdf.Rect(MARGIN, MARGIN, MARGIN + piece.w, MARGIN + piece.h)
    pages[-1].append(r)
    return len(pages) - 1, r


def main():
    TMP.mkdir(parents=True, exist_ok=True)
    pieces, keep = [], []
    for n, title, prog, cases in EXPS:
        exp_start = len(pieces)
        tag = f"Exp {n} · {title}"
        if n in FLOW_W:
            img = next(HERE.glob(f"flowcharts/exp{n:02d}.*"))
            pieces.append(image_piece(f"{tag} · Flowchart (manual)", img, FLOW_W[n]))
        else:
            for k, src in enumerate(mermaid_sources(n)):
                doc, clip = render_mermaid(src, TMP / f"flow{n:02d}_{k}.pdf")
                keep.append(doc)
                pieces.append(pdf_piece(f"{tag} · Flowchart" + (f" ({k + 1})" if n == 9 else ""), doc, clip, 0.75))
        parts = split_parts(program_lines(prog))
        for k, part in enumerate(parts):
            suffix = f" (part {k + 1}/{len(parts)})" if len(parts) > 1 else ""
            pieces.append(text_piece(f"{tag} · Program{suffix}", part))
        for k, case in enumerate(cases):
            suffix = f" ({k + 1}/{len(cases)})" if len(cases) > 1 else ""
            pieces.append(text_piece(f"{tag} · Output{suffix}", output_lines(case), boxed=True))
        if TALL_FIRST:                               # tall pieces first, small ones fill around them
            pieces[exp_start:] = sorted(pieces[exp_start:], key=lambda pc: -pc.h)

    pages, placed = [], []
    for pc in pieces:
        pi, r = place(pages, pc)
        placed.append((pi, r, pc))

    out = pymupdf.open()
    for _ in pages:
        out.new_page(width=PAGE_W, height=PAGE_H)
    label_font = pymupdf.Font(fontfile=SANS)
    for pi, r, pc in placed:
        page = out[pi]
        page.draw_rect(r, color=(0.45, 0.45, 0.45), width=0.6, dashes="[3 2] 0")
        tw = pymupdf.TextWriter(page.rect)
        tw.append((r.x0 + PAD, r.y0 + PAD + 2.6 * MM), pc.label, font=label_font, fontsize=6.8)
        tw.write_text(page, color=(0.35, 0.35, 0.4))
        pc.draw(page, r.x0 + PAD, r.y0 + PAD + LABEL_H)
    for i, page in enumerate(out):
        tw = pymupdf.TextWriter(page.rect)
        tw.append((PAGE_W - MARGIN - 40 * MM, PAGE_H - 3 * MM), f"ECE2132 DSA Lab · to-print · {i + 1}",
                  font=label_font, fontsize=6)
        tw.write_text(page, color=(0.6, 0.6, 0.6))
    used = sum(r.width * r.height for _, r, _ in placed)
    total = len(pages) * (PAGE_W - 2 * MARGIN) * (PAGE_H - 2 * MARGIN)
    out.save(str(OUT_PDF), garbage=3, deflate=True)
    print(f"{OUT_PDF.name}: {len(pages)} pages, {len(pieces)} pieces, {100 * used / total:.0f}% of printable area used")


if __name__ == "__main__":
    main()
