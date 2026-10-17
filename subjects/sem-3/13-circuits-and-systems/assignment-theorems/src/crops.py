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
    # batch 2 (Thevenin / Norton 5.15-5.34): boxes from figfind.py clusters, padded for labels, then trimmed
    "ck5_15": ("ck", 264, (140, 178, 395, 275), "trim"),
    "ck5_15s1": ("ck", 264, (280, 312, 490, 405), "trim"),
    "ck5_15s2": ("ck", 264, (75, 432, 450, 512), "trim"),
    "ck5_16": ("ck", 265, (160, 72, 365, 192), "trim"),
    "ck5_16s": ("ck", 265, (318, 190, 490, 428), "trim"),
    "ck5_17": ("ck", 265, (100, 505, 400, 595), "trim"),
    "ck5_17s1": ("ck", 266, (100, 368, 410, 452), "trim"),
    "ck5_17s2": ("ck", 266, (150, 538, 370, 631), "trim"),
    "ck5_17s3": ("ck", 267, (265, 72, 485, 172), "trim"),
    "ck5_18": ("ck", 267, (160, 205, 390, 325), "trim"),
    "ck5_18s": ("ck", 267, (262, 343, 490, 462), "trim"),
    "ck5_19": ("ck", 268, (180, 250, 365, 372), "trim"),
    "ck5_19s1": ("ck", 268, (312, 372, 490, 492), "trim"),
    "ck5_19s2": ("ck", 268, (312, 492, 490, 612), "trim"),
    "ck5_20": ("ck", 269, (85, 90, 440, 175), "trim"),
    "ck5_20s": ("ck", 269, (85, 182, 440, 266), "trim"),
    "ck5_21a": ("ck", 269, (85, 425, 320, 540), "trim"),
    "ck5_21b": ("ck", 269, (85, 540, 320, 640), "trim"),
    "ck5_21c": ("ck", 270, (85, 78, 345, 165), "trim"),
    "ck5_21d": ("ck", 270, (85, 165, 345, 252), "trim"),
    "ck5_21e": ("ck", 270, (85, 252, 345, 362), "trim"),
    "ck5_21as": ("ck", 270, (270, 380, 490, 506), "trim"),
    "ck5_21ds": ("ck", 272, (335, 75, 490, 165), "trim"),
    "ck5_21es1": ("ck", 272, (135, 215, 385, 330), "trim"),
    "ck5_21es2": ("ck", 272, (135, 415, 385, 505), "trim"),
    "ck5_22": ("ck", 273, (130, 92, 390, 202), "trim"),
    "ck5_22s1": ("ck", 273, (130, 360, 395, 460), "trim"),
    "ck5_22s2": ("ck", 274, (135, 117, 385, 210), "trim"),
    "ck5_23": ("ck", 274, (60, 522, 245, 602), "trim"),
    "ck5_23s": ("ck", 275, (295, 72, 490, 245), "trim"),
    "ck5_23s2": ("ck", 275, (105, 190, 230, 298), "trim"),
    "ck5_24": ("ck", 275, (390, 283, 488, 345), "trim"),
    "ck5_24s": ("ck", 275, (105, 470, 400, 592), "trim"),
    "ck5_25": ("ck", 276, (60, 72, 290, 156), "trim"),
    "ck5_25s1": ("ck", 276, (70, 188, 450, 272), "trim"),
    "ck5_25s2": ("ck", 276, (120, 316, 400, 400), "trim"),
    "ck5_25s3": ("ck", 276, (240, 412, 490, 496), "trim"),
    "ck5_25s4": ("ck", 276, (70, 511, 450, 597), "trim"),
    "ck5_25s5": ("ck", 277, (110, 156, 410, 250), "trim"),
    "ck5_26": ("ck", 277, (125, 262, 400, 350), "trim"),
    "ck5_26s": ("ck", 277, (118, 566, 412, 645), "trim"),
    "ck5_27": ("ck", 278, (140, 212, 380, 294), "trim"),
    "ck5_27s": ("ck", 278, (140, 436, 380, 515), "trim"),
    "ck5_28": ("ck", 279, (155, 113, 380, 193), "trim"),
    "ck5_28s1": ("ck", 279, (155, 215, 380, 292), "trim"),
    "ck5_28s2": ("ck", 279, (165, 312, 362, 402), "trim"),
    "ck5_29": ("ck", 280, (165, 412, 335, 500), "trim"),
    "ck5_29s": ("ck", 280, (85, 528, 410, 615), "trim"),
    "ck5_30": ("ck", 281, (170, 230, 360, 315), "auto"),
    "ck5_30s1": ("ck", 281, (190, 385, 336, 438), "auto"),
    "ck5_30s2": ("ck", 281, (130, 553, 394, 621), "auto"),
    "ck5_31": ("ck", 283, (168, 176, 362, 282), "trim"),
    "ck5_31s": ("ck", 283, (162, 438, 362, 546), "trim"),
    "ck5_32": ("ck", 284, (165, 255, 430, 368), "trim"),
    "ck5_33": ("ck", 285, (189, 325, 303, 383), "auto"),
    "ck5_33s1": ("ck", 285, (189, 451, 303, 509), "auto"),
    "ck5_33s2": ("ck", 286, (187, 128, 274, 186), "auto"),
    "ck5_34": ("ck", 286, (231, 480, 304, 530), "auto"),
    "ck5_34s": ("ck", 287, (204, 157, 333, 214), "auto"),
    # batch 3 (maximum power transfer 5.35-5.44): seeds from figfind.py, grown by auto()
    "ck5_35": ("ck", 287, (334, 404, 474, 435), "auto2"),
    "ck5_36a": ("ck", 288, (130, 295, 280, 340), "auto2", (60, 16, 45, 8)),
    "ck5_36b": ("ck", 288, (130, 362, 280, 415), "auto2", (60, 8, 45, 6)),
    "ck5_36c": ("ck", 288, (130, 437, 280, 495), "auto2", (60, 8, 45, 16)),
    "ck5_36as": ("ck", 288, (283, 534, 468, 613), "auto2"),
    "ck5_36as2": ("ck", 289, (190, 100, 332, 161), "auto2"),
    "ck5_36bs1": ("ck", 289, (93, 318, 474, 382), "auto2"),
    "ck5_36bs2": ("ck", 289, (95, 437, 465, 501), "auto2"),
    "ck5_36cs1": ("ck", 290, (305, 81, 450, 143), "auto2", (60, 10, 45, 16)),
    "ck5_36cs2": ("ck", 290, (296.5, 150, 485, 222), "trim"),
    "ck5_37": ("ck", 290, (146, 261, 376, 328), "auto2"),
    "ck5_38a": ("ck", 291, (140, 82, 370, 150), "auto2", (60, 10, 45, 6)),
    "ck5_38b": ("ck", 291, (140, 168, 370, 255), "auto2", (60, 8, 45, 16)),
    "ck5_40": ("ck", 292, (100, 178, 281, 254), "auto2"),
    "ck5_40s1": ("ck", 292, (292, 290, 468, 364), "auto2"),
    "ck5_40s2": ("ck", 292, (292, 393, 477, 469), "auto2"),
    "ck5_41": ("ck", 292, (209, 530, 329, 590), "auto2"),
    "ck5_41s": ("ck", 293, (244, 200, 298, 242), "auto2"),
    "ck5_42": ("ck", 293, (179, 394, 341, 451), "auto2"),
    "ck5_44": ("ck", 294, (185, 528, 362, 580), "auto2"),
    # Part B batch 4 (Sadiku 5e section 4.3 superposition): seeds read off the page renders, grown by auto2()
    "sd_pp4_4": ("sd", 158, (55, 90, 190, 150), "auto2"),
    "sd_pp4_5": ("sd", 159, (125, 390, 290, 455), "auto2"),
    "sd4_10": ("sd", 187, (105, 275, 280, 332), "auto2"),
    "sd4_11": ("sd", 187, (120, 435, 265, 478), "auto2"),
    "sd4_12": ("sd", 187, (100, 575, 278, 648), "auto2"),
    "sd4_13": ("sd", 187, (322, 84, 528, 165)),
    "sd4_14": ("sd", 187, (342, 242, 500, 334), "auto2"),
    "sd4_15": ("sd", 187, (335, 432, 500, 494), "auto2", (40, 5, 45, 16)),
    "sd4_16": ("sd", 187, (328, 573, 514, 652), "auto2"),
    "sd4_17": ("sd", 188, (55, 100, 270, 148), "auto2"),
    "sd4_18": ("sd", 188, (84, 248, 240, 335), "auto2"),
    "sd4_19": ("sd", 188, (84, 428, 240, 500), "auto2"),
    # Part B batch 5 (Sadiku 5e section 4.4 source transformation)
    "sd_pp4_6": ("sd", 161, (100, 570, 340, 622), "auto2"),
    "sd_pp4_7": ("sd", 162, (55, 612, 212, 662), "auto2"),
    "sd4_20": ("sd", 188, (80, 620, 234, 666), "auto2"),
    "sd4_21": ("sd", 188, (342, 104, 464, 151), "auto2"),
    "sd4_22": ("sd", 188, (322, 256, 486, 313), "auto2"),
    "sd4_23": ("sd", 188, (288, 411, 486, 468), "auto2"),
    "sd4_24": ("sd", 188, (300, 576, 493, 666), "auto2", (28, 16, 45, 16)),
    "sd4_25": ("sd", 189, (95, 104, 284, 205), "auto2"),
    "sd4_26": ("sd", 189, (95, 296, 284, 367), "auto2"),
    "sd4_27": ("sd", 189, (105, 468, 291, 522), "auto2"),
    "sd4_28": ("sd", 189, (105, 602, 291, 658), "auto2"),
    "sd4_29": ("sd", 189, (350, 104, 500, 180), "auto2"),
    "sd4_30": ("sd", 189, (314, 278, 514, 338), "auto2"),
    "sd4_31": ("sd", 189, (364, 436, 500, 493), "auto2"),
    "sd4_32": ("sd", 189, (335, 591, 514, 651), "auto2"),
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


def auto(page, seed, reach=24, pad=3):
    """Figure box from a rough seed: the vector drawings connected to the seed (wires have zero
    height, so every box is inflated by 1.5 pt before testing contact), plus every text line that sits
    wholly within `reach` of them (labels), but no paragraph lines (they run wider)."""
    seed = pymupdf.Rect(seed)
    rs = [dr["rect"] + (-1.5, -1.5, 1.5, 1.5) for dr in page.get_drawings() if dr["rect"].y1 > 70]
    box = None
    for r in rs:
        if r.intersects(seed):
            box = pymupdf.Rect(r) if box is None else box | r
    if box is None:
        return seed
    grown = True
    while grown:
        grown = False
        for r in rs:
            if r in box or not r.intersects(box):
                continue
            if (r | box).width > 440:  # page-wide rules are not part of a figure
                continue
            box |= r; grown = True
    zone = box + (-reach, -reach, reach, reach)
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            r = pymupdf.Rect(ln["bbox"])
            if r in zone:
                box |= r
    return (box + (-pad, -pad, pad, pad)) & page.rect


def auto2(page, seed, pad=(60, 16, 45, 16)):
    """Connected drawings from the seed (as auto), padded for labels, then pulled back so no body-text
    line (font >= 9.5 pt) is inside; the result is then ink-trimmed. Works whether the labels are
    text (about 7-8 pt) or vector glyphs."""
    seed = pymupdf.Rect(seed)
    rs = [dr["rect"] + (-1.5, -1.5, 1.5, 1.5) for dr in page.get_drawings()
          if dr["rect"].y1 > 70 and dr["rect"] in page.rect + (-2, -2, 2, 2)
          and not (dr["rect"].width > 300 and dr["rect"].height > 300)]
    box = None
    for r in rs:
        if r.intersects(seed):
            box = pymupdf.Rect(r) if box is None else box | r
    if box is None:
        return seed
    grown = True
    while grown:
        grown = False
        for r in rs:
            if r in box or not r.intersects(box) or (r | box).width > 440:
                continue
            box |= r; grown = True
    L, T, R, B = pad
    out = pymupdf.Rect(box.x0 - L, box.y0 - T, box.x1 + R, box.y1 + B)
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            for s in ln["spans"]:
                if s["size"] < 9.5 or not s["text"].strip():
                    continue
                r = pymupdf.Rect(s["bbox"])
                if not r.intersects(out) or r.intersects(box):
                    continue
                if r.y1 <= box.y0 + 2:
                    out.y0 = max(out.y0, r.y1 + 0.5)
                elif r.y0 >= box.y1 - 2:
                    out.y1 = min(out.y1, r.y0 - 0.5)
                elif r.x1 <= box.x0 + 2:
                    out.x0 = max(out.x0, r.x1 + 0.5)
                elif r.x0 >= box.x1 - 2:
                    out.x1 = min(out.x1, r.x0 - 0.5)
    return trim(page, out & page.rect, min_ink=8)


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
        elif mode and mode[0] == "auto":
            clip = auto(docs[book][page - 1], clip)
        elif mode and mode[0] == "auto2":
            clip = auto2(docs[book][page - 1], clip, *mode[1:])
        pix = docs[book][page - 1].get_pixmap(dpi=220, clip=clip)
        pix.save(out / f"{name}.png")
        print(name, pix.width, pix.height)

if __name__ == "__main__":
    main(sys.argv[1:] or None)
