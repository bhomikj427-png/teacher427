"""List figure regions on book pages by clustering vector drawings (helper for choosing crop boxes).
Run: python figfind.py ck 264 287"""
import sys
import pymupdf
from crops import BOOKS


def clusters(page, gap=14):
    rs = [d["rect"] for d in page.get_drawings() if d["rect"].width < 450 or d["rect"].height > 3]
    rs = [r for r in rs if not (r.y1 < 70)]  # running header
    boxes = []
    for r in rs:
        r = pymupdf.Rect(r)
        merged = True
        while merged:
            merged = False
            for b in boxes:
                if (r.x0 - gap < b.x1 and b.x0 - gap < r.x1 and r.y0 - gap < b.y1 and b.y0 - gap < r.y1):
                    r |= b; boxes.remove(b); merged = True; break
        boxes.append(r)
    return sorted([b for b in boxes if b.width > 40 and b.height > 25], key=lambda b: (b.y0, b.x0))


if __name__ == "__main__":
    book, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    d = pymupdf.open(BOOKS[book])
    for p in range(a, b + 1):
        for k, c in enumerate(clusters(d[p - 1])):
            print(p, k, tuple(round(v) for v in c))
