"""Merge the three sem-3 lab packs (ED, DE, DSA) into one bookmarked PDF with a contents page.

Run:  python merge.py      (rebuild each lab pack first with its own src/build.py)
"""
import subprocess
from pathlib import Path

from pypdf import PdfReader, PdfWriter

HERE = Path(__file__).resolve().parent
SEM3 = HERE.parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PACKS = [
    ("ECE2130 Electronic Devices Lab", SEM3 / "08-electronic-devices-lab-1/study-pack/pdf/ECE2130-ED-Lab-pack.pdf",
     "LTspice from zero, Exp 0–12, design problem, revision set"),
    ("ECE2131 Digital Electronics Lab", SEM3 / "09-digital-electronics-lab/study-pack/pdf/ECE2131-DE-Lab-pack.pdf",
     "Pin-to-pin wiring for every experiment, designs checked, revision set"),
    ("ECE2132 Data Structures & Algorithms Lab", SEM3 / "15-data-structures-and-algorithms-lab/study-pack/pdf/ECE2132-DSA-Lab-pack.pdf",
     "C++ from zero, Exp 1–12 (corrected, tested code), exam day, revision set"),
]
OUT = HERE / "Sem3-Lab-ETE-pack.pdf"


def cover(starts):
    rows = "".join(
        f"<tr><td class='p'>{s}</td><td><b>{name}</b><br><span>{what}</span></td><td class='n'>{n} pp.</td></tr>"
        for (name, _, what), (s, n) in zip(PACKS, starts))
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 22mm 20mm; }}
body {{ font-family: 'Segoe UI', Arial, sans-serif; color: #1f2937; }}
h1 {{ font-size: 26pt; margin: 40mm 0 4pt; }} .sub {{ color: #6b7280; margin-bottom: 18mm; }}
table {{ border-collapse: collapse; width: 100%; font-size: 11pt; }}
td {{ padding: 9pt 8pt; border-bottom: 1px solid #e5e7eb; vertical-align: top; }}
td span {{ color: #6b7280; font-size: 9.5pt; }} .p {{ width: 18mm; color: #1d4ed8; font-weight: 700; font-size: 14pt; }}
.n {{ width: 20mm; text-align: right; color: #6b7280; }}
.how {{ margin-top: 14mm; font-size: 10pt; color: #374151; line-height: 1.5; }}
</style></head><body>
<h1>Semester 3 — Lab ETE pack</h1><div class="sub">Three labs in one file. Page numbers below are PDF pages; use the bookmarks panel to jump.</div>
<table>{rows}</table>
<div class="how"><b>Same method in every pack:</b> guess first, then read; type or build it yourself; check boxes close each
chapter with answers at its end; the revision set at the end of each lab is the re-test to do on a later day.</div>
</body></html>"""
    h = HERE / "cover.html"
    h.write_text(html, encoding="utf-8")
    pdf = HERE / "cover.pdf"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", h.as_uri()], check=True, capture_output=True, timeout=120)
    return pdf


def copy_outline(writer, items, reader, offset, parent):
    last = None
    for it in items:
        if isinstance(it, list):
            if last is not None:
                copy_outline(writer, it, reader, offset, last)
            continue
        page = reader.get_destination_page_number(it)
        last = writer.add_outline_item(it.title, page + offset, parent=parent)


def main():
    readers = [PdfReader(str(p)) for _, p, _ in PACKS]
    starts, page = [], 2                                     # page 1 = contents
    for r in readers:
        starts.append((page, len(r.pages)))
        page += len(r.pages)
    w = PdfWriter()
    w.append(str(cover(starts)))
    w.add_outline_item("Contents", 0)
    for (name, _, _), r, (s, _) in zip(PACKS, readers, starts):
        off = len(w.pages)
        for pg in r.pages:
            w.add_page(pg)
        top = w.add_outline_item(name, off)
        copy_outline(w, r.outline, r, off, top)
    with open(OUT, "wb") as f:
        w.write(f)
    print(OUT.name, len(w.pages), "pages;", ", ".join(f"{n.split()[0]} p.{s}" for (n, _, _), (s, _) in zip(PACKS, starts)))


if __name__ == "__main__":
    main()
