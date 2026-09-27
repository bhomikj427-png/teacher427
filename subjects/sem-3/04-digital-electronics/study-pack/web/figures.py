"""Figures for the Digital Electronics web study pack. Every function returns an SVG string.

K-maps, strips and Venns are hand-built SVG styled by the site's CSS classes (so they follow the
light/dark theme). Gate circuits are schemdraw, recoloured to currentColor.
Every K-map grouping here is checked by verify.py (python verify.py).
"""
import re

import schemdraw
import schemdraw.logic as lg

schemdraw.use("svg")

GRAY = {1: [0, 1], 2: [0, 1, 3, 2]}
_uid = [0]


def _id(prefix):
    _uid[0] += 1
    return f"{prefix}{_uid[0]}"


def _bits(v, n):
    return format(v, f"0{n}b")


# ------------------------------------------------------------------ K-map core
def _segments(pos, n):
    """Cyclic positions -> list of (start, end, open_lo, open_hi) runs."""
    pos = sorted(set(pos))
    if len(pos) == n:
        return [(0, n - 1, False, False)]
    runs, cur = [], [pos[0]]
    for p in pos[1:]:
        if p == cur[-1] + 1:
            cur.append(p)
        else:
            runs.append(cur)
            cur = [p]
    runs.append(cur)
    if len(runs) == 2 and runs[0][0] == 0 and runs[1][-1] == n - 1:
        return [(runs[1][0], runs[1][-1], False, True), (runs[0][0], runs[0][-1], True, False)]
    assert len(runs) == 1, f"not a K-map rectangle: {pos}"
    return [(runs[0][0], runs[0][-1], False, False)]


def _kmap_body(cells, groups, rv, cv, x0, y0, cs, show_idx, hl, title, labels=True, offset=0, emph0=False):
    """Return (svg_parts, width, height) for one map drawn at (x0, y0)."""
    nr, nc = len(rv), len(cv)
    rows, cols = GRAY[nr], GRAY[nc]
    R, C = len(rows), len(cols)
    lm = 66 if labels else 6
    tm = 60 if labels else 6
    gx, gy = x0 + lm, y0 + tm
    out = []
    if title:
        out.append(f'<text class="k-title" x="{gx + C * cs / 2}" y="{y0 + 12}" text-anchor="middle">{title}</text>')
    if labels:
        out.append(f'<text class="k-var" x="{gx - 16}" y="{gy - 34}" text-anchor="end">{rv}</text>')
        out.append(f'<text class="k-var" x="{gx - 4}" y="{gy - 34}">{cv}</text>')
        out.append(f'<line class="k-diag" x1="{gx - 44}" y1="{gy - 48}" x2="{gx - 4}" y2="{gy - 4}"/>')
        for j, c in enumerate(cols):
            out.append(f'<text class="k-lab" x="{gx + j * cs + cs / 2}" y="{gy - 16}" text-anchor="middle">{_bits(c, nc)}</text>')
        for i, r in enumerate(rows):
            out.append(f'<text class="k-lab" x="{gx - 16}" y="{gy + i * cs + cs / 2 + 5}" text-anchor="end">{_bits(r, nr)}</text>')
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            idx = (r << nc) | c
            x, y = gx + j * cs, gy + i * cs
            cls = "k-cell" + (f" {hl[idx + offset]}" if hl and idx + offset in hl else "")
            out.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{cs}" height="{cs}"/>')
            v = cells.get(idx + offset, "0") if cells is not None else None
            if v is None:
                out.append(f'<text class="k-idx-big" x="{x + cs / 2}" y="{y + cs / 2 + 5}" text-anchor="middle">m{idx + offset}</text>')
                continue
            vcls = {"1": "k-one", "0": "k-zero-em" if emph0 else "k-zero", "X": "k-x"}[v]
            fs = cs * 0.42
            out.append(f'<text class="{vcls}" x="{x + cs / 2}" y="{y + cs / 2 + fs * 0.36}" text-anchor="middle" style="font-size:{fs:.0f}px">{v}</text>')
            if show_idx:
                out.append(f'<text class="k-idx" x="{x + 4}" y="{y + 11}">{idx + offset}</text>')
    # groups
    pad_out = max(5, cs * 0.17)
    for k, g in enumerate(groups):
        members = [m - offset for m in g["cells"] if offset <= m < offset + R * C]
        if not members:
            continue
        rpos = {rows.index(m >> nc) for m in members}
        cpos = {cols.index(m & ((1 << nc) - 1)) for m in members}
        ins = 5 + 4 * (g.get("layer", k) % 4)
        parts = []
        for (r0, r1, rlo, rhi) in _segments(rpos, R):
            for (c0, c1, clo, chi) in _segments(cpos, C):
                x1 = gx + c0 * cs + ins - (pad_out + ins if clo else 0)
                x2 = gx + (c1 + 1) * cs - ins + (pad_out + ins if chi else 0)
                y1 = gy + r0 * cs + ins - (pad_out + ins if rlo else 0)
                y2 = gy + (r1 + 1) * cs - ins + (pad_out + ins if rhi else 0)
                parts.append(f'<rect class="k-grp" x="{x1}" y="{y1}" width="{x2 - x1}" height="{y2 - y1}" rx="{cs * 0.28:.0f}"/>')
        step = f' data-step="{g["step"]}"' if "step" in g else ""
        kind = " k-grp-0s" if g.get("zeros") else ""
        out.append(f'<g class="kg c{g.get("color", k)}{kind}"{step}>' + "".join(parts) + "</g>")
    w = lm + C * cs + 16
    h = tm + R * cs + 16
    return out, w, h


def _legend(groups, x, y, width):
    out, cx, cy = [], x, y
    for k, g in enumerate(groups):
        label = g.get("term")
        if not label:
            continue
        step = f' data-step="{g["step"]}"' if "step" in g else ""
        wlen = 34 + 9.2 * len(label)
        if cx + wlen > x + width and cx > x:
            cx, cy = x, cy + 28
        out.append(f'<g class="kg c{g.get("color", k)}"{step}><rect class="k-chip" x="{cx}" y="{cy}" width="{wlen}" height="22" rx="11"/>'
                   f'<text class="k-chip-t" x="{cx + 12}" y="{cy + 15.5}">{label}</text></g>')
        cx += wlen + 8
    return out, cy + 28 - y if out else 0


def kmap(cells, groups=(), rv="ab", cv="cd", cs=54, show_idx=False, hl=None, legend=True,
         title=None, labels=True, arrows=(), emph0=False):
    parts, w, h = _kmap_body(cells, list(groups), rv, cv, 0, 0 if not title else 18, cs, show_idx, hl,
                             title, labels, emph0=emph0)
    if title:
        h += 18
    lh = 0
    if legend:
        lp, lh = _legend(list(groups), 8, h, max(w, 260) - 8)
        parts += lp
    parts += list(arrows)
    W = max(w, 260) if legend and lh else w
    return _wrap(parts, W, h + lh + 4)


def kmap5(cells, groups, cs=40):
    """Two 4-variable maps: v=0 (0-15) and v=1 (16-31)."""
    gl = list(groups)
    a, w1, h1 = _kmap_body(cells, gl, "wx", "yz", 0, 18, cs, False, None, "v = 0", offset=0)
    b, w2, h2 = _kmap_body(cells, gl, "wx", "yz", w1 + 20, 18, cs, False, None, "v = 1", offset=16)
    W = w1 + 20 + w2
    lp, lh = _legend(gl, 8, h1 + 18, W - 8)
    return _wrap(a + b + lp, W, h1 + 18 + lh + 4)


def _wrap(parts, w, h, cls="fig-svg"):
    return (f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="-14 -14 {w + 28:.0f} {h + 28:.0f}" '
            f'style="max-width:{w + 28:.0f}px">' + "".join(parts) + "</svg>")


# ------------------------------------------------------------------ 01 figures
ARROW_DEF = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
             'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="k-arrowhead"/></marker></defs>')


def kmap_layout():
    """Index layout of a 4-variable map, m0 and its four neighbours highlighted, wrap arcs drawn."""
    cs = 58
    gx, gy = 66, 60
    hl = {0: "hl-a", 1: "hl-b", 4: "hl-b", 2: "hl-c", 8: "hl-c"}
    arrows = [ARROW_DEF,
              # m0 (row0,col0) <-> m2 (row0,col3): arc above the grid
              f'<path class="k-arrow" d="M{gx + cs * 0.5},{gy - 26} C{gx + cs * 0.9},{gy - 70} {gx + cs * 3.1},{gy - 70} {gx + cs * 3.5},{gy - 26}" marker-end="url(#ah)" marker-start="url(#ah)"/>',
              # m0 <-> m8 (row3,col0): arc to the left
              f'<path class="k-arrow" d="M{gx - 34},{gy + cs * 0.5} C{gx - 84},{gy + cs * 0.9} {gx - 84},{gy + cs * 3.1} {gx - 34},{gy + cs * 3.5}" marker-end="url(#ah)" marker-start="url(#ah)"/>',
              ]
    parts, w, h = _kmap_body(None, [], "ab", "cd", 0, 0, cs, False, hl, None)
    key = [
        f'<rect class="k-cell hl-a" x="0" y="{h + 6}" width="16" height="16"/><text class="k-note" x="22" y="{h + 19}">m0</text>',
        f'<rect class="k-cell hl-b" x="70" y="{h + 6}" width="16" height="16"/><text class="k-note" x="92" y="{h + 19}">next door</text>',
        f'<rect class="k-cell hl-c" x="182" y="{h + 6}" width="16" height="16"/><text class="k-note" x="204" y="{h + 19}">next door by wrap-around</text>',
    ]
    return (f'<svg class="fig-svg" xmlns="http://www.w3.org/2000/svg" viewBox="-66 -66 {w + 96} {h + 98}" '
            f'style="max-width:{w + 96}px">' + "".join(arrows + parts + key) + "</svg>")


def strip_sm_pm():
    """F(a,b,c) = Σm(1,3,5): the 1-rows are the Σm list, the 0-rows are the ΠM list."""
    ones = {1, 3, 5}
    cw, x0, y0 = 58, 20, 58
    p = []
    p.append(f'<text class="s-head one" x="{x0}" y="18">Σm lists the rows where F = 1</text>')
    for i in range(8):
        x = x0 + i * cw
        one = i in ones
        cls = "s-cell one" if one else "s-cell zero"
        p.append(f'<rect class="{cls}" x="{x}" y="{y0}" width="{cw - 6}" height="{cw - 6}" rx="8"/>')
        p.append(f'<text class="s-val" x="{x + (cw - 6) / 2}" y="{y0 + 34}" text-anchor="middle">{1 if one else 0}</text>')
        p.append(f'<text class="s-idx" x="{x + (cw - 6) / 2}" y="{y0 - 8}" text-anchor="middle">{i}</text>')
        p.append(f'<text class="s-bin" x="{x + (cw - 6) / 2}" y="{y0 + cw + 10}" text-anchor="middle">{_bits(i, 3)}</text>')
        if one:
            p.append(f'<line class="s-tick one" x1="{x + (cw - 6) / 2}" y1="{y0 - 22}" x2="{x + (cw - 6) / 2}" y2="{y0 - 34}"/>')
        else:
            p.append(f'<line class="s-tick zero" x1="{x + (cw - 6) / 2}" y1="{y0 + cw + 18}" x2="{x + (cw - 6) / 2}" y2="{y0 + cw + 30}"/>')
    p.append(f'<text class="s-lab" x="{x0 - 8}" y="{y0 - 8}" text-anchor="end">row</text>')
    p.append(f'<text class="s-lab" x="{x0 - 8}" y="{y0 + 34}" text-anchor="end">F</text>')
    p.append(f'<text class="s-lab" x="{x0 - 8}" y="{y0 + cw + 10}" text-anchor="end">abc</text>')
    p.append(f'<text class="s-head one" x="{x0 + 8 * cw}" y="18" text-anchor="end">Σm(1, 3, 5)</text>')
    p.append(f'<text class="s-head zero" x="{x0}" y="{y0 + cw + 52}">ΠM lists the rows where F = 0</text>')
    p.append(f'<text class="s-head zero" x="{x0 + 8 * cw}" y="{y0 + cw + 52}" text-anchor="end">ΠM(0, 2, 4, 6, 7)</text>')
    W = x0 + 8 * cw
    return (f'<svg class="fig-svg" xmlns="http://www.w3.org/2000/svg" viewBox="-30 0 {W + 44} {y0 + cw + 64}" '
            f'style="max-width:{W + 44}px">' + "".join(p) + "</svg>")


def _venn_panel(x, shade, label):
    """One Venn panel; shade in {'A', 'AB', 'B-A', 'AuB'}."""
    r, ax, bx, cy = 46, x + 62, x + 112, 70
    cid, mid = _id("vc"), _id("vm")
    defs = (f'<defs><clipPath id="{cid}"><circle cx="{ax}" cy="{cy}" r="{r}"/></clipPath>'
            f'<mask id="{mid}"><rect x="{x}" y="0" width="180" height="140" fill="white"/>'
            f'<circle cx="{ax}" cy="{cy}" r="{r}" fill="black"/></mask></defs>')
    fill = ""
    if shade == "A":
        fill = f'<circle class="v-fill" cx="{ax}" cy="{cy}" r="{r}"/>'
    elif shade == "AB":
        fill = f'<circle class="v-fill" cx="{bx}" cy="{cy}" r="{r}" clip-path="url(#{cid})"/>'
    elif shade == "B-A":
        fill = f'<circle class="v-fill" cx="{bx}" cy="{cy}" r="{r}" mask="url(#{mid})"/>'
    elif shade == "AuB":
        fill = f'<circle class="v-fill" cx="{ax}" cy="{cy}" r="{r}"/><circle class="v-fill" cx="{bx}" cy="{cy}" r="{r}" mask="url(#{mid})"/>'
    rings = (f'<circle class="v-ring" cx="{ax}" cy="{cy}" r="{r}"/><circle class="v-ring" cx="{bx}" cy="{cy}" r="{r}"/>'
             f'<text class="v-set" x="{ax - r + 2}" y="{cy - r + 6}" text-anchor="end">A</text><text class="v-set" x="{bx + r - 2}" y="{cy - r + 6}">B</text>')
    lab = f'<text class="v-lab" x="{x + 87}" y="148" text-anchor="middle">{label}</text>'
    return defs + fill + rings + lab


def _venn_eq(panels):
    p, x = [], 0
    for k, item in enumerate(panels):
        if isinstance(item, str):
            p.append(f'<text class="v-op" x="{x + 14}" y="80" text-anchor="middle">{item}</text>')
            x += 30
        else:
            p.append(_venn_panel(x, *item))
            x += 178
    return (f'<svg class="fig-svg" xmlns="http://www.w3.org/2000/svg" viewBox="-6 10 {x + 12} 150" '
            f'style="max-width:{x + 12}px">' + "".join(p) + "</svg>")


def venn_absorption():
    return _venn_eq([("A", "A"), "+", ("AB", "AB"), "=", ("A", "A")])


def venn_absorption2():
    return _venn_eq([("A", "A"), "+", ("B-A", "A'B"), "=", ("AuB", "A + B")])


def group_sizes():
    """Same map, groups of 1, 2, 4, 8 around m5: each doubling deletes one letter."""
    specs = [([5], "a'bc'd", "1 cell · 4 letters"),
             ([5, 7], "a'bd", "2 cells · 3 letters"),
             ([5, 7, 13, 15], "bd", "4 cells · 2 letters"),
             ([1, 3, 5, 7, 13, 15, 9, 11], "d", "8 cells · 1 letter")]
    cs, gap, parts, x = 26, 34, [], 0
    for k, (cells, term, note) in enumerate(specs):
        mp, w, h = _kmap_body({c: "1" for c in cells}, [{"cells": cells, "color": k}], "ab", "cd", x, 0, cs,
                              False, None, None, labels=False)
        parts += mp
        parts.append(f'<text class="g-term c{k}" x="{x + 6 + 2 * cs}" y="{h + 14}" text-anchor="middle">{term}</text>')
        parts.append(f'<text class="k-note" x="{x + 6 + 2 * cs}" y="{h + 34}" text-anchor="middle">{note}</text>')
        x += w + gap
    return _wrap(parts, x - gap, 4 * cs + 58)


def legal_illegal():
    """Three illegal shapes beside three legal ones."""
    cs, gap = 24, 30
    bad = [([0, 1, 3], "size 3: not a power of 2"),
           ([0, 5], "diagonal"),
           ([0, 1, 4], "L-shape")]
    good = [([0, 2, 8, 10], "four corners (wrap)"),
            ([4, 6], "left + right edge"),
            ([0, 1, 3, 2, 8, 9, 11, 10], "top + bottom rows")]
    parts, x = [], 0
    for row, (items, ok) in enumerate([(bad, False), (good, True)]):
        x = 0
        y = row * (4 * cs + 70)
        for cells, note in items:
            cellv = {c: "1" for c in cells}
            mp, w, h = _kmap_body(cellv, [] if not ok else [{"cells": cells, "color": 2}], "ab", "cd", x, y, cs,
                                  False, None, None, labels=False)
            parts += mp
            if not ok:
                # draw the would-be blob outline in red, cell by cell
                for c in cells:
                    rr, cc = GRAY[2].index(c >> 2), GRAY[2].index(c & 3)
                    parts.append(f'<rect class="k-bad" x="{x + 6 + cc * cs + 3}" y="{y + 6 + rr * cs + 3}" width="{cs - 6}" height="{cs - 6}" rx="5"/>')
            mark = "✗" if not ok else "✓"
            parts.append(f'<text class="{"mk-bad" if not ok else "mk-good"}" x="{x + 6 + 2 * cs}" y="{y + h + 12}" text-anchor="middle">{mark} {note}</text>')
            x += w + gap
    return _wrap(parts, x - gap, 2 * (4 * cs + 70) - 30)


def dontcare_effect():
    """m7, m15 alone make a pair (3 letters); with the don't-cares m6, m14 they make a quad (2 letters)."""
    cs = 32
    a, w, h = _kmap_body({7: "1", 15: "1", 6: "0", 14: "0"}, [{"cells": [7, 15], "color": 3}], "ab", "cd", 0, 18, cs,
                         False, None, "X read as 0")
    b, w2, _ = _kmap_body({7: "1", 15: "1", 6: "X", 14: "X"}, [{"cells": [6, 7, 14, 15], "color": 2}], "ab", "cd",
                          w + 30, 18, cs, False, None, "X used as 1")
    notes = [f'<text class="g-term c3" x="{58 + 2 * cs}" y="{h + 34}" text-anchor="middle">bcd · 3 letters</text>',
             f'<text class="g-term c2" x="{w + 30 + 58 + 2 * cs}" y="{h + 34}" text-anchor="middle">bc · 2 letters</text>']
    return _wrap(a + b + notes, w + 30 + w2, h + 44)


# ------------------------------------------------------------------ worked Q4 and answers
Q4_CELLS = {**{m: "1" for m in (0, 4, 5, 7, 8, 9, 15)}, **{m: "X" for m in (1, 3, 6, 14)}}


def q4_plot():
    return kmap(Q4_CELLS, show_idx=True, legend=False)


def q4_steps():
    groups = [{"cells": [0, 1, 8, 9], "term": "b'c'  essential (m8, m9)", "step": 1},
              {"cells": [6, 7, 14, 15], "term": "bc  essential (m15)", "step": 2},
              {"cells": [4, 5, 6, 7], "term": "a'b  covers m4, m5", "step": 3}]
    return kmap(Q4_CELLS, groups, show_idx=True)


def q4_alt():
    groups = [{"cells": [0, 1, 8, 9], "term": "b'c'"},
              {"cells": [6, 7, 14, 15], "term": "bc"},
              {"cells": [0, 1, 4, 5], "term": "a'c'", "color": 3}]
    return kmap(Q4_CELLS, groups, show_idx=True)


def pos_example():
    """F(a,b,c) = Σm(0,1,2,3,7): group the 0s (m4, m5, m6)."""
    cells = {m: "1" for m in (0, 1, 2, 3, 7)}
    groups = [{"cells": [4, 5], "term": "ab'  →  (a' + b)", "zeros": True, "color": 1},
              {"cells": [4, 6], "term": "ac'  →  (a' + c)", "zeros": True, "color": 4}]
    return kmap(cells, groups, rv="a", cv="bc", cs=56, emph0=True)


def ans2():
    return kmap({1: "1", 2: "1", 4: "1"}, rv="a", cv="bc", cs=50, show_idx=True, legend=False)


def ans3():
    cells = {**{m: "1" for m in (0, 1, 3, 5, 7, 10, 11)}, **{m: "X" for m in (2, 6, 13)}}
    groups = [{"cells": [0, 1, 3, 2], "term": "w'x'"},
              {"cells": [1, 3, 5, 7], "term": "w'z"},
              {"cells": [3, 2, 11, 10], "term": "x'y"}]
    return kmap(cells, groups, rv="wx", cv="yz", show_idx=True)


def ans4():
    cells = {m: "1" for m in (0, 2, 8, 10)}
    return kmap(cells, [{"cells": [0, 2, 8, 10], "term": "B'D'", "color": 2}], rv="AB", cv="CD", show_idx=True)


Q6_ONES = (0, 2, 5, 8, 10, 13, 15, 17, 19, 21, 26, 28, 29, 30, 31)
Q6_DC = (7, 12, 14, 23, 24)


def ans6():
    cells = {**{m: "1" for m in Q6_ONES}, **{m: "X" for m in Q6_DC}}
    groups = [{"cells": [5, 7, 13, 15, 21, 23, 29, 31], "term": "xz"},
              {"cells": [8, 10, 12, 14, 24, 26, 28, 30], "term": "wz'"},
              {"cells": [17, 19, 21, 23], "term": "vw'z"},
              {"cells": [0, 2, 8, 10], "term": "v'x'z'"}]
    return kmap5(cells, groups, cs=40)


# ------------------------------------------------------------------ circuits (schemdraw)
def _sd():
    d = schemdraw.Drawing(show=False)
    d.config(unit=1.6, fontsize=15, font="Arial", lw=1.8)
    return d


def _svg(d):
    s = d.get_imagedata("svg").decode()
    s = re.sub(r"<\?xml[^>]*\?>", "", s)
    s = s.replace("stroke:black", "stroke:currentColor").replace("fill:black", "fill:currentColor")
    s = s.replace('fill="black"', 'fill="currentColor"').replace('stroke="black"', 'stroke="currentColor"')
    m = re.search(r'width="([\d.]+)pt"', s)
    w = float(m.group(1)) * 1.33 if m else 400
    s = re.sub(r'\s(height|width)="[\d.]+pt"', "", s, count=2)
    return s.replace("<svg ", f'<svg class="fig-svg circuit" style="max-width:{w:.0f}px" ', 1)


def nor_inverter():
    d = _sd()
    g = d.add(lg.Nor().label("NOR", "bottom", fontsize=11))
    d.add(lg.Line().at(g.in1).left(0.6))
    d.add(lg.Line().down(g.in1.y - g.in2.y))
    d.add(lg.Line().right(0.6))
    d.add(lg.Dot().at((g.in1.x - 0.6, (g.in1.y + g.in2.y) / 2)))
    d.add(lg.Line().left(1.1).label("P", "left"))
    d.add(lg.Line().at(g.out).right(1).label("F = P'", "right"))
    return _svg(d)


def q4_circuit():
    """F = b'c' + bc + a'b. Input bubbles stand for the NOT gates."""
    d = _sd()
    o = d.add(lg.Or(inputs=3).at((6, 0)).anchor("in2"))
    a1 = d.add(lg.And(inputnots=[1, 2]).at((2.2, 1.6)).anchor("out"))
    a2 = d.add(lg.And().at((2.2, 0)).anchor("out"))
    a3 = d.add(lg.And(inputnots=[1]).at((2.2, -1.6)).anchor("out"))
    for gate, pin in ((a1, o.in1), (a2, o.in2), (a3, o.in3)):
        d.add(lg.Wire("-|").at(gate.out).to(pin))
    for gate, (l1, l2) in ((a1, ("b", "c")), (a2, ("b", "c")), (a3, ("a", "b"))):
        d.add(lg.Line().at(gate.in1).left(0.7).label(l1, "left"))
        d.add(lg.Line().at(gate.in2).left(0.7).label(l2, "left"))
    d.add(lg.Line().at(o.out).right(0.8).label("F", "right"))
    d.add(lg.Line().at(a1.out).right(0.001).label("b'c'", "top", fontsize=12, ofst=0.25))
    d.add(lg.Line().at(a2.out).right(0.001).label("bc", "top", fontsize=12, ofst=0.25))
    d.add(lg.Line().at(a3.out).right(0.001).label("a'b", "bottom", fontsize=12, ofst=0.25))
    return _svg(d)


def demorgan_gates():
    """NOR = AND with both inputs inverted (De Morgan, drawn)."""
    d = _sd()
    g1 = d.add(lg.Nor())
    d.add(lg.Line().at(g1.in1).left(0.5).label("A", "left"))
    d.add(lg.Line().at(g1.in2).left(0.5).label("B", "left"))
    d.add(lg.Line().at(g1.out).right(0.5).label("(A + B)'", "right"))
    g2 = d.add(lg.And(inputnots=[1, 2]).at((g1.out.x + 7.4, g1.out.y)).anchor("out"))
    d.add(lg.Line().at(g2.in1).left(0.5).label("A", "left"))
    d.add(lg.Line().at(g2.in2).left(0.5).label("B", "left"))
    d.add(lg.Line().at(g2.out).right(0.5).label("A'B'", "right"))
    d.add(lg.Line().at((g1.out.x + 3.3, g1.out.y)).right(0.001).label("≡", "center", fontsize=24))
    return _svg(d)


ALL = {name: fn for name, fn in globals().items()
       if callable(fn) and not name.startswith("_") and fn.__module__ == __name__
       and name not in ("kmap", "kmap5")}
