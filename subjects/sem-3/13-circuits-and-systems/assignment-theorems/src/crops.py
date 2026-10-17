"""Crop question figures straight from the two textbooks (real figures, not redrawn).

Each entry: name -> (book, 1-based PDF page, (x0, y0, x1, y1) in PDF points).
Run: python crops.py   -> writes ../figs/<name>.png
"""
import sys
from pathlib import Path
import pymupdf

HERE = Path(__file__).resolve().parent
INBOX = HERE.parents[2] / "_inbox" / "_unsorted"
BOOKS = {
    "ck": INBOX / "circuit-theory-and-networks-fourth-edition-wbut-2014-9789339214265-9339214269_compress.pdf",
    "sd": INBOX / "file_17265317748jBDU.pdf",
}
CROPS = {
    "ck5_1": ("ck", 248, (72, 180, 312, 255)),
    "ck5_2": ("ck", 248, (150, 455, 385, 570)),
    "ck5_3": ("ck", 249, (145, 300, 356, 403)),
    "ck5_4": ("ck", 250, (192, 269, 335, 414)),
    "ck5_1s": ("ck", 248, (85, 281, 440, 356)),
    "ck5_2s": ("ck", 249, (113, 72, 430, 155)),
    "ck5_3s": ("ck", 249, (78, 432, 455, 523)),
    "ck5_4s": ("ck", 250, (132, 470, 420, 616)),
    # batch 1 (auto-trimmed: region between the question text and "Solution")
    "ck5_5": ("ck", 251, (60, 199, 470, 477), "trim"),
    "ck5_6": ("ck", 253, (60, 505, 470, 587), "trim"),
    "ck5_7": ("ck", 254, (60, 352, 470, 437), "trim"),
    "ck5_8": ("ck", 255, (60, 306, 470, 393), "trim"),
    "ck5_9": ("ck", 256, (60, 319, 470, 431), "trim"),
    "ck5_10": ("ck", 258, (60, 74, 470, 227), "trim"),
    "ck5_11": ("ck", 259, (60, 519, 470, 680), "trim"),
    "ck5_12": ("ck", 260, (60, 512, 470, 680), "trim"),
    "ck5_13": ("ck", 261, (60, 541, 470, 680), "trim"),
    "ck5_14": ("ck", 263, (60, 238, 470, 348), "trim"),
    # batch 1 sub-circuits (book's own "source acting alone" drawings)
    "ck5_5as": ("ck", 251, (60, 536, 470, 612), "trim"),
    "ck5_5bs": ("ck", 252, (60, 238, 470, 331), "trim"),
    "ck5_5cs1": ("ck", 252, (278, 540, 490, 603), "trim"),
    "ck5_5cs2": ("ck", 253, (60, 150, 490, 368), "trim"),
    "ck5_6s": ("ck", 254, (60, 74, 470, 148), "trim"),
    "ck5_7s": ("ck", 254, (60, 464, 470, 546), "trim"),
    "ck5_8s1": ("ck", 255, (60, 407, 470, 489), "trim"),
    "ck5_8s2": ("ck", 256, (60, 94, 470, 176), "trim"),
    "ck5_9s1": ("ck", 256, (60, 476, 470, 553), "trim"),
    "ck5_9s2": ("ck", 257, (60, 106, 470, 189), "trim"),
    "ck5_9s3": ("ck", 257, (60, 285, 470, 398), "trim"),
    "ck5_9s4": ("ck", 257, (60, 412, 470, 488), "trim"),
    "ck5_10s1": ("ck", 258, (60, 312, 470, 453), "trim"),
    "ck5_10s2": ("ck", 258, (60, 479, 470, 601), "trim"),
    "ck5_10s3": ("ck", 259, (60, 70, 470, 144), "trim"),
    "ck5_10s4": ("ck", 259, (60, 252, 470, 378), "trim"),
    "ck5_11s1": ("ck", 260, (60, 168, 470, 297), "trim"),
    "ck5_11s2": ("ck", 260, (325, 316, 490, 450), "trim"),
    "ck5_12s1": ("ck", 261, (60, 70, 470, 170), "trim"),
    "ck5_12s2": ("ck", 261, (60, 185, 470, 287), "trim"),
    "ck5_13s1": ("ck", 262, (60, 105, 470, 191), "trim"),
    "ck5_13s2": ("ck", 262, (60, 455, 470, 538), "trim"),
    "ck5_14s1": ("ck", 263, (60, 372, 470, 481), "trim"),
    "ck5_14s2": ("ck", 263, (300, 538, 490, 645), "trim"),
    "sd_pp4_3": ("sd", 156, (50, 345, 212, 411)),
    "sd4_8": ("sd", 186, (325, 590, 468, 660)),
    "sd4_9": ("sd", 187, (98, 104, 260, 165)),
}

def trim(page, clip, pad=4, gap=5, min_ink=30):
    """Shrink clip to the figure's ink: bands of rows/columns separated by >= gap blank lines are
    dropped when they hold < min_ink dark pixels (stray text fragments), then pad is added."""
    pix = page.get_pixmap(dpi=72, clip=clip)
    w, h, n = pix.width, pix.height, pix.n
    data = pix.samples
    dark = [[min(data[y * pix.stride + x * n:y * pix.stride + x * n + 3]) < 200 for x in range(w)]
            for y in range(h)]

    def keep_range(counts):
        bands, cur = [], None
        blank = 0
        for k, c in enumerate(counts):
            if c:
                if cur is None or blank >= gap:
                    cur = [k, k, 0]; bands.append(cur)
                cur[1] = k; cur[2] += c; blank = 0
            else:
                blank += 1
        bands = [b for b in bands if b[2] >= min_ink] or bands
        return (bands[0][0], bands[-1][1]) if bands else None

    rows = keep_range([sum(r) for r in dark])
    if not rows:
        return clip
    cols = keep_range([sum(dark[y][x] for y in range(rows[0], rows[1] + 1)) for x in range(w)])
    return pymupdf.Rect(clip.x0 + cols[0] - pad, clip.y0 + rows[0] - pad,
                        clip.x0 + cols[1] + pad, clip.y0 + rows[1] + pad) & clip


def main(names=None):
    out = HERE.parent / "figs"
    out.mkdir(exist_ok=True)
    docs = {k: pymupdf.open(v) for k, v in BOOKS.items()}
    for name, (book, page, rect, *mode) in CROPS.items():
        if names and name not in names:
            continue
        clip = pymupdf.Rect(*rect)
        if mode and mode[0] == "trim":
            clip = trim(docs[book][page - 1], clip)
        pix = docs[book][page - 1].get_pixmap(dpi=220, clip=clip)
        pix.save(out / f"{name}.png")
        print(name, pix.width, pix.height)

if __name__ == "__main__":
    main(sys.argv[1:] or None)
