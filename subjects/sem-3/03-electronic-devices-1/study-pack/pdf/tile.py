"""usage: tile.py file.pdf first last outdir [cols]  -> one PNG per `cols*2` pages (2 rows), for quick visual review"""
import sys, pymupdf
from pathlib import Path
pdf, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), Path(sys.argv[4]); cols = int(sys.argv[5]) if len(sys.argv) > 5 else 3
d = pymupdf.open(pdf); b = min(b, d.page_count); print(d.page_count, "pages")
pw, ph = 595, 842; per = cols * 2
for k, s0 in enumerate(range(a - 1, b, per)):
    doc = pymupdf.open(); pg = doc.new_page(width=pw * cols, height=ph * 2)
    for j, i in enumerate(range(s0, min(s0 + per, b))):
        r = pymupdf.Rect((j % cols) * pw, (j // cols) * ph, (j % cols + 1) * pw, (j // cols + 1) * ph)
        pg.show_pdf_page(r, d, i); pg.draw_rect(r, color=(0.6, 0.6, 0.6)); pg.insert_text((r.x0 + 6, r.y0 + 12), f"p{i+1}", fontsize=11, color=(1, 0, 0))
    pg.get_pixmap(dpi=82).save(str(out / f"{Path(pdf).stem}-t{a + k * per:02d}.png"))
