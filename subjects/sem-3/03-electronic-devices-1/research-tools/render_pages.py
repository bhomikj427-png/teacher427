"""Render PDF pages to PNG so they can be looked at with the Read tool.

Usage:  python -I render_pages.py <file.pdf> <out_dir> [first] [last] [dpi]

Pages are 1-based; default = every page at 90 dpi (enough to spot label overlaps; use 130
for small print). Used for (a) viewing every page of a built pack file (spec §7) and
(b) reading scanned or picture-only PDFs (numerical sheets, the WSU logic deck).
"""
import sys
from pathlib import Path

import pymupdf


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    pdf, out = Path(sys.argv[1]), Path(sys.argv[2])
    doc = pymupdf.open(pdf)
    first = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    last = int(sys.argv[4]) if len(sys.argv) > 4 else doc.page_count
    dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 90
    out.mkdir(parents=True, exist_ok=True)
    for i in range(first - 1, min(last, doc.page_count)):
        dst = out / ("%s-p%03d.png" % (pdf.stem, i + 1))
        doc[i].get_pixmap(dpi=dpi).save(dst)
    print("%s: pages %d-%d of %d -> %s" % (pdf.name, first, min(last, doc.page_count), doc.page_count, out))


if __name__ == "__main__":
    main()
