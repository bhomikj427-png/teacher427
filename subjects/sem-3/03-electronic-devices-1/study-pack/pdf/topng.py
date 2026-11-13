"""usage: topng.py file.pdf first last [dpi]  -> scratch PNGs (page numbers 1-based)"""
import sys, pymupdf
from pathlib import Path
pdf, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); dpi = int(sys.argv[4]) if len(sys.argv) > 4 else 70
out = Path(sys.argv[5]) if len(sys.argv) > 5 else Path(pdf).parent
d = pymupdf.open(pdf); print(d.page_count, "pages")
for i in range(a - 1, min(b, d.page_count)):
    d[i].get_pixmap(dpi=dpi).save(str(out / f"{Path(pdf).stem}-p{i+1:02d}.png"))
