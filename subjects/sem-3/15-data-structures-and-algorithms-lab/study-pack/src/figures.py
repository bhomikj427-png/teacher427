"""Figures for the ECE2132 DSA lab pack. Every function returns an SVG string (hand-built, no libraries).

Each figure draws the manual's own example data (Exp 1-12), so the picture matches the program's sample run.
"""
INK, ACCENT, MUTED = "#1f2937", "#1d4ed8", "#6b7280"
FILL, HI, GOOD, BAD, SOFT = "#eff6ff", "#fde68a", "#dcfce7", "#fee2e2", "#f3f4f6"
FONT = "font-family='Segoe UI, Arial, sans-serif'"
MONO = "font-family='Consolas, monospace'"


class S:
    """Tiny SVG builder."""

    def __init__(self, w, h):
        self.w, self.h, self.p = w, h, []

    def box(self, x, y, w, h, txt="", fill=FILL, stroke=INK, size=14, mono=True, bold=False, r=3):
        self.p.append(f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='{r}' fill='{fill}' "
                      f"stroke='{stroke}' stroke-width='1.4'/>")
        if txt != "":
            self.text(x + w / 2, y + h / 2 + size * 0.36, txt, size=size, mono=mono, bold=bold)
        return self

    def text(self, x, y, t, size=12, color=INK, anchor="middle", mono=False, bold=False, italic=False):
        f = MONO if mono else FONT
        wgt = " font-weight='700'" if bold else ""
        it = " font-style='italic'" if italic else ""
        t = str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        self.p.append(f"<text x='{x}' y='{y}' {f} font-size='{size}' fill='{color}' "
                      f"text-anchor='{anchor}'{wgt}{it}>{t}</text>")
        return self

    def arrow(self, x1, y1, x2, y2, color=INK, w=1.5, dash=False):
        d = " stroke-dasharray='4 3'" if dash else ""
        mid = "a" + color[1:]
        self.p.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' stroke-width='{w}'{d} "
                      f"marker-end='url(#{mid})'/>")
        return self

    def path(self, d, color=INK, w=1.5, arrow=True, dash=False):
        m = f" marker-end='url(#a{color[1:]})'" if arrow else ""
        da = " stroke-dasharray='4 3'" if dash else ""
        self.p.append(f"<path d='{d}' fill='none' stroke='{color}' stroke-width='{w}'{da}{m}/>")
        return self

    def svg(self):
        cols = {INK, ACCENT, MUTED, "#b91c1c", "#15803d", "#a16207"}
        defs = "".join(
            f"<marker id='a{c[1:]}' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='7' markerHeight='7' "
            f"orient='auto-start-reverse'><path d='M0,0 L10,5 L0,10 z' fill='{c}'/></marker>" for c in cols)
        return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {self.w} {self.h}' width='{self.w}'>"
                f"<defs>{defs}</defs>{''.join(self.p)}</svg>")


RED, GREEN, AMBER = "#b91c1c", "#15803d", "#a16207"


def row(s, x, y, vals, cw=46, ch=34, fills=None, idx=True, idx_base=0, label=None, size=14):
    for k, v in enumerate(vals):
        f = (fills or {}).get(k, FILL if v != "" else SOFT)
        s.box(x + k * cw, y, cw, ch, v, fill=f, size=size)
        if idx:
            s.text(x + k * cw + cw / 2, y + ch + 14, f"[{k + idx_base}]", size=10, color=MUTED, mono=True)
    if label:
        s.text(x - 10, y + ch / 2 + 5, label, size=12, anchor="end", bold=True)


# ---------------------------------------------------------------- Exp 1-2: pointers
def pointer_basic():
    s = S(560, 170)
    s.text(140, 22, "int number = 25;", size=13, mono=True)
    s.box(80, 40, 120, 50, "25", size=20, bold=True)
    s.text(140, 110, "number", size=13, bold=True)
    s.text(140, 128, "lives at address 0x61FF08", size=11, color=MUTED)
    s.text(420, 22, "int *ptr = &number;", size=13, mono=True)
    s.box(360, 40, 120, 50, "0x61FF08", size=15, fill=HI)
    s.text(420, 110, "ptr", size=13, bold=True)
    s.text(420, 128, "stores an ADDRESS, not 25", size=11, color=MUTED)
    s.path("M360,65 C300,65 260,65 202,65", color=ACCENT, w=2)
    s.text(280, 56, "points to", size=11, color=ACCENT)
    s.text(280, 160, "*ptr  =  \"go to the address in ptr, read what is there\"  =  25", size=12, color=ACCENT)
    return s.svg()


def pointer_arith():
    s = S(600, 205)
    vals = ["10", "20", "30", "40", "50"]
    x0, cw = 70, 92
    for k, v in enumerate(vals):
        s.box(x0 + k * cw, 60, cw, 40, v, size=16, fill=HI if k in (0, 1, 2) else FILL)
        s.text(x0 + k * cw + cw / 2, 118, f"0x61FF{0 + 4 * k:02X}", size=11, color=MUTED, mono=True)
        s.text(x0 + k * cw + cw / 2, 134, f"arr[{k}]", size=11, color=MUTED, mono=True)
    s.text(x0 - 8, 85, "arr", size=13, bold=True, anchor="end")
    labels = [(0, "ptr  (start)", ACCENT), (1, "ptr++", GREEN), (0, "ptr--", AMBER), (2, "ptr = ptr + 2", RED)]
    ys = [30, 30, 168, 30]
    used = set()
    for k, (i, lab, c) in enumerate(labels):
        cx = x0 + i * cw + cw / 2
        if ys[k] < 60:
            s.arrow(cx, 38, cx, 58, color=c)
            s.text(cx, 30, lab, size=12, color=c, bold=True, mono=True)
        else:
            s.arrow(cx, 158, cx, 140, color=c)
            s.text(cx, 176, lab, size=12, color=c, bold=True, mono=True)
        used.add(i)
    s.text(300, 200, "+1 on an int pointer = +4 bytes (sizeof(int)), i.e. the NEXT element", size=12, color=INK)
    return s.svg()


# ---------------------------------------------------------------- Exp 3-4: arrays
def array_insert():
    s = S(620, 272)
    s.text(20, 16, "Insert 25 at position 3 (index 2), n = 5", size=13, anchor="start", bold=True)
    row(s, 110, 62, ["10", "20", "30", "40", "50", ""], fills={2: HI, 3: HI, 4: HI}, label="before")
    # shift arrows, last first
    for k, (a, b) in enumerate([(4, 5), (3, 4), (2, 3)]):
        x1 = 110 + a * 46 + 23
        x2 = 110 + b * 46 + 23
        s.path(f"M{x1},62 C{x1},40 {x2},40 {x2},60", color=ACCENT)
        s.text((x1 + x2) / 2, 40, f"{k + 1}", size=11, color=ACCENT, bold=True)
    s.text(430, 84, "shift right, starting", size=11, anchor="start", color=ACCENT)
    s.text(430, 98, "from the LAST element", size=11, anchor="start", color=ACCENT)
    row(s, 110, 142, ["10", "20", "30", "30", "40", "50"], fills={2: SOFT}, label="after shift")
    s.text(430, 164, "index 2 is now free", size=11, anchor="start", color=MUTED)
    row(s, 110, 217, ["10", "20", "25", "30", "40", "50"], fills={2: GOOD}, label="arr[2] = 25")
    s.text(430, 239, "n = n + 1  (now 6)", size=11, anchor="start", color=GREEN, bold=True)
    return s.svg()


def array_delete():
    s = S(620, 185)
    s.text(20, 22, "Delete position 3 (index 2), n = 5", size=13, anchor="start", bold=True)
    row(s, 110, 50, ["10", "20", "30", "40", "50"], fills={2: BAD}, label="before")
    for k, (a, b) in enumerate([(3, 2), (4, 3)]):
        x1 = 110 + a * 46 + 23
        x2 = 110 + b * 46 + 23
        s.path(f"M{x1},50 C{x1},28 {x2},28 {x2},48", color=ACCENT)
        s.text((x1 + x2) / 2, 30, f"{k + 1}", size=11, color=ACCENT, bold=True)
    s.text(370, 64, "shift left, starting just", size=11, anchor="start", color=ACCENT)
    s.text(370, 78, "AFTER the deleted one", size=11, anchor="start", color=ACCENT)
    row(s, 110, 125, ["10", "20", "40", "50", "50"], fills={4: SOFT}, label="after")
    s.text(370, 140, "n = n - 1 (now 4): the old copy", size=11, anchor="start", color=GREEN, bold=True)
    s.text(370, 154, "in [4] is simply never printed", size=11, anchor="start", color=GREEN)
    return s.svg()


# ---------------------------------------------------------------- Exp 5-6: matrices
def _grid(s, x, y, M, cw=40, hi_row=None, hi_col=None, hi_cell=None, name=""):
    for i, r in enumerate(M):
        for j, v in enumerate(r):
            f = FILL
            if hi_row == i or hi_col == j:
                f = HI
            if hi_cell == (i, j):
                f = GOOD
            s.box(x + j * cw, y + i * cw, cw, cw, v, fill=f, size=15)
    if name:
        s.text(x + len(M[0]) * cw / 2, y - 10, name, size=13, bold=True)


def matmul():
    s = S(700, 190)
    _grid(s, 30, 40, [["1", "2"], ["3", "4"]], hi_row=0, name="A (2 x 2)")
    s.text(130, 85, "x", size=20)
    _grid(s, 160, 40, [["5", "6"], ["7", "8"]], hi_col=1, name="B (2 x 2)")
    s.text(262, 85, "=", size=20)
    _grid(s, 290, 40, [["19", "22"], ["43", "50"]], hi_cell=(0, 1), name="C (2 x 2)")
    s.text(390, 62, "C[0][1] = row 0 of A · column 1 of B", size=12, anchor="start", color=INK, bold=True)
    s.text(390, 84, "= A[0][0]·B[0][1] + A[0][1]·B[1][1]", size=12, anchor="start", mono=True)
    s.text(390, 104, "= 1·6 + 2·8 = 6 + 16 = 22", size=12, anchor="start", mono=True)
    s.text(390, 128, "k walks along the row AND", size=11, anchor="start", color=MUTED)
    s.text(390, 142, "down the column together", size=11, anchor="start", color=MUTED)
    s.text(350, 180, "Rule: (m x n) times (n x p) gives (m x p). The two inner numbers must match: c1 == r2.",
           size=12, color=ACCENT)
    return s.svg()


def transpose():
    s = S(560, 200)
    cols = [HI, GOOD, BAD]
    A = [["1", "2", "3"], ["4", "5", "6"]]
    for i in range(2):
        for j in range(3):
            s.box(40 + j * 42, 50 + i * 42, 42, 42, A[i][j], fill=cols[j], size=15)
    s.text(103, 38, "A  (2 x 3)", size=13, bold=True)
    T = [["1", "4"], ["2", "5"], ["3", "6"]]
    for i in range(3):
        for j in range(2):
            s.box(330 + j * 42, 40 + i * 42, 42, 42, T[i][j], fill=cols[i], size=15)
    s.text(372, 28, "T  (3 x 2)", size=13, bold=True)
    s.arrow(200, 90, 315, 90, color=ACCENT, w=2)
    s.text(258, 80, "T[j][i] = A[i][j]", size=12, color=ACCENT, mono=True)
    s.text(280, 190, "Column j of A becomes row j of T  (each colour = one column of A → one row of T)",
           size=12, color=INK)
    return s.svg()


# ---------------------------------------------------------------- Exp 7: insertion sort
def insertion_passes():
    rows = [("start", [5, 2, 4, 6, 1, 3], 1, None),
            ("pass 1  key=2", [2, 5, 4, 6, 1, 3], 2, 0),
            ("pass 2  key=4", [2, 4, 5, 6, 1, 3], 3, 1),
            ("pass 3  key=6", [2, 4, 5, 6, 1, 3], 4, 3),
            ("pass 4  key=1", [1, 2, 4, 5, 6, 3], 5, 0),
            ("pass 5  key=3", [1, 2, 3, 4, 5, 6], 6, 2)]
    s = S(560, 52 + 44 * len(rows))
    s.text(160, 20, "sorted part", size=11, color=GREEN, bold=True)
    s.text(330, 20, "unsorted part", size=11, color=MUTED, bold=True)
    s.text(470, 20, "shifts", size=11, color=MUTED, bold=True)
    shifts = ["", "1", "1", "0", "4", "3"]
    for r, (lab, vals, sorted_len, placed) in enumerate(rows):
        y = 34 + r * 44
        s.text(120, y + 22, lab, size=12, anchor="end", mono=True)
        for k, v in enumerate(vals):
            f = GOOD if k < sorted_len else SOFT
            if placed is not None and k == placed:
                f = HI
            s.box(135 + k * 46, y, 46, 32, v, fill=f, size=15)
        s.text(480, y + 22, shifts[r], size=13, mono=True)
    s.text(280, 52 + 44 * len(rows) - 6, "yellow = where the key landed;  total shifts = 9", size=11, color=MUTED)
    return s.svg()


# ---------------------------------------------------------------- Exp 8: quick sort
def partition_trace():
    # Lomuto on 10 7 8 9 1 5, pivot 5
    steps = [("pivot = 5, i = -1", [10, 7, 8, 9, 1, 5], None, None, "j = 0..3: 10, 7, 8, 9 are not < 5 → skip"),
             ("j = 4: 1 < 5", [10, 7, 8, 9, 1, 5], 0, 4, "i++ → i = 0; swap arr[0], arr[4]"),
             ("after swap", [1, 7, 8, 9, 10, 5], 1, 5, "loop over; swap arr[i+1], arr[high] (pivot in)"),
             ("result", [1, 5, 8, 9, 10, 7], None, None, "return 1: pivot 5 is in its FINAL place")]
    s = S(640, 40 + 52 * len(steps))
    for r, (lab, vals, a, b, note) in enumerate(steps):
        y = 20 + r * 52
        s.text(105, y + 22, lab, size=11, anchor="end", mono=True)
        for k, v in enumerate(vals):
            f = FILL
            if k == 5 and r < 3:
                f = HI
            if r == 3 and k == 1:
                f = GOOD
            if k in (a, b) and r in (1, 2):
                f = BAD
            s.box(115 + k * 44, y, 44, 32, v, fill=f, size=14)
        s.text(395, y + 21, note, size=11, anchor="start")
    s.text(320, 40 + 52 * len(steps) - 10, "yellow = pivot, red = the two cells being swapped, green = pivot placed",
           size=11, color=MUTED)
    return s.svg()


def quick_tree():
    s = S(660, 260)
    nodes = {  # id: (x, y, text, pivot)
        "a": (300, 30, "10 7 8 9 1 5", "5"),
        "b": (130, 105, "1", None),
        "c": (420, 105, "8 9 10 7", "7"),
        "d": (330, 175, "(empty)", None),
        "e": (500, 175, "9 10 8", "8"),
        "f": (430, 235, "(empty)", None),
        "g": (560, 235, "10 9", "9"),
    }
    edges = [("a", "b"), ("a", "c"), ("c", "d"), ("c", "e"), ("e", "f"), ("e", "g")]
    for u, v in edges:
        x1, y1 = nodes[u][0], nodes[u][1] + 14
        x2, y2 = nodes[v][0], nodes[v][1] - 16
        s.p.append(f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{MUTED}' stroke-width='1.2'/>")
    for k, (x, y, t, pv) in nodes.items():
        w = 9 * len(t) + 16
        s.box(x - w / 2, y - 14, w, 26, t, size=12, fill=SOFT if pv is None else FILL)
        if pv:
            s.text(x + w / 2 + 6, y + 4, f"pivot {pv}", size=10, color=AMBER, anchor="start", bold=True)
    s.text(20, 160, "left part:", size=11, anchor="start", color=MUTED)
    s.text(20, 174, "smaller than pivot", size=11, anchor="start", color=MUTED)
    s.text(20, 215, "Sorted: 1 5 7 8 9 10", size=13, anchor="start", color=GREEN, bold=True)
    return s.svg()


# ---------------------------------------------------------------- Exp 9-10: stack, queue
def stack_fig():
    s = S(520, 230)
    vals = ["10", "20", "30"]
    for k, v in enumerate(vals):
        s.box(60, 170 - k * 40, 90, 36, v, fill=HI if k == 2 else FILL, size=15)
        s.text(50, 193 - k * 40, f"[{k}]", size=10, color=MUTED, mono=True, anchor="end")
    s.box(60, 50, 90, 36, "", fill=SOFT)
    s.box(60, 10, 90, 36, "", fill=SOFT)
    s.text(105, 222, "stackArr (MAX = 5)", size=11, color=MUTED)
    s.arrow(250, 108, 155, 108, color=ACCENT, w=2)
    s.text(260, 112, "top = 2", size=13, color=ACCENT, anchor="start", bold=True, mono=True)
    s.text(260, 40, "push: top++, then store", size=12, anchor="start")
    s.text(260, 60, "pop: read stackArr[top], then top--", size=12, anchor="start")
    s.text(260, 80, "LIFO: last in (30) is first out", size=12, anchor="start", color=GREEN, bold=True)
    s.text(260, 150, "empty: top == -1  → Underflow", size=12, anchor="start", mono=True)
    s.text(260, 170, "full:  top == MAX-1 → Overflow", size=12, anchor="start", mono=True)
    return s.svg()


def queue_fig():
    s = S(620, 236)
    s.text(20, 20, "After enqueue 10, 20, 30 (MAX = 5)", size=13, anchor="start", bold=True)
    row(s, 120, 50, ["10", "20", "30", "", ""], cw=56)
    s.arrow(148, 132, 148, 104, color=GREEN, w=2)
    s.text(148, 148, "front = 0", size=12, color=GREEN, mono=True, bold=True)
    s.arrow(260, 132, 260, 104, color=RED, w=2)
    s.text(260, 148, "rear = 2", size=12, color=RED, mono=True, bold=True)
    s.text(420, 62, "enqueue → at rear", size=12, anchor="start", color=RED)
    s.text(420, 80, "dequeue → from front", size=12, anchor="start", color=GREEN)
    s.text(20, 178, "After 1 dequeue:", size=13, anchor="start", bold=True)
    row(s, 120, 186, ["", "20", "30", "", ""], cw=56, idx=False)
    s.text(420, 202, "front = 1, rear = 2", size=12, anchor="start", mono=True)
    s.text(420, 220, "slot [0] is never reused", size=11, anchor="start", color=MUTED)
    return s.svg()


def queue_waste():
    s = S(620, 150)
    s.text(20, 20, "Linear queue flaw: enqueue 1..5, dequeue twice, enqueue 7", size=13, anchor="start", bold=True)
    row(s, 120, 40, ["", "", "3", "4", "5"], cw=56, fills={0: BAD, 1: BAD})
    s.text(176, 112, "2 free slots ...", size=12, color=RED)
    s.text(372, 112, "... but rear == MAX-1", size=12, color=RED)
    s.text(310, 138, "so the program prints \"Queue Overflow!\" (verified run). The circular queue fixes this.",
           size=12, color=INK)
    return s.svg()


def circular_queue():
    import math
    s = S(560, 270)
    cx, cy, R = 140, 140, 85
    vals = ["6", "7", "3", "4", "5"]
    for k in range(5):
        a = -math.pi / 2 + k * 2 * math.pi / 5
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        f = GOOD if k in (0, 1) else FILL
        s.box(x - 22, y - 18, 44, 36, vals[k], fill=f, size=15)
        s.text(cx + (R + 38) * math.cos(a), cy + (R + 38) * math.sin(a) + 4, f"[{k}]", size=10, color=MUTED,
               mono=True)
    s.path(f"M{cx + 30},{cy - 30} A40,40 0 1,1 {cx - 30},{cy - 30}", color=ACCENT)
    s.text(cx, cy + 5, "wraps", size=11, color=ACCENT)
    s.text(300, 50, "front = 2 (value 3)", size=12, anchor="start", mono=True, color=GREEN)
    s.text(300, 70, "rear  = 1 (value 7)", size=12, anchor="start", mono=True, color=RED)
    s.text(300, 105, "rear = (rear + 1) % MAX", size=13, anchor="start", mono=True, bold=True)
    s.text(300, 125, "4 → (4+1) % 5 = 0", size=12, anchor="start", mono=True)
    s.text(300, 160, "full when (rear+1) % MAX == front", size=12, anchor="start", mono=True)
    s.text(300, 185, "green = new values stored in the", size=11, anchor="start", color=MUTED)
    s.text(300, 199, "slots the linear queue wasted", size=11, anchor="start", color=MUTED)
    return s.svg()


# ---------------------------------------------------------------- Exp 11-12: linked lists
def _node(s, x, y, v, fill=FILL):
    s.box(x, y, 50, 34, v, fill=fill, size=15)
    s.box(x + 50, y, 30, 34, "", fill=SOFT)
    s.p.append(f"<circle cx='{x + 65}' cy='{y + 17}' r='3' fill='{INK}'/>")


def sll_fig():
    s = S(620, 250)
    s.text(20, 22, "HEAD → 10 → 20 → 30 → NULL", size=13, anchor="start", bold=True)
    s.text(40, 64, "head", size=12, mono=True, bold=True)
    s.arrow(60, 60, 88, 60, color=ACCENT, w=2)
    xs = [90, 220, 350]
    for k, v in enumerate(["10", "20", "30"]):
        _node(s, xs[k], 43, v)
        if k < 2:
            s.arrow(xs[k] + 65, 60, xs[k + 1] - 2, 60)
    s.arrow(415, 60, 470, 60)
    s.text(500, 65, "NULL", size=13, mono=True, color=RED, bold=True)
    s.text(115, 95, "data", size=10, color=MUTED)
    s.text(155, 95, "next", size=10, color=MUTED)
    # insert at end
    s.text(20, 130, "Insert 40 at end: walk temp to the node whose next is NULL, then", size=12, anchor="start")
    s.text(40, 148, "temp->next = newNode;", size=12, anchor="start", mono=True, color=GREEN)
    # delete from beginning
    s.text(20, 182, "Delete from beginning:", size=12, anchor="start")
    s.text(40, 200, "temp = head;  head = head->next;  delete temp;", size=12, anchor="start", mono=True,
           color=RED)
    s.text(20, 232, "Order matters: move head BEFORE delete, or the rest of the list is lost.", size=12,
           anchor="start", color=MUTED)
    return s.svg()


def cll_fig():
    s = S(620, 196)
    s.text(20, 22, "Circular: the last node points back to head (never NULL)", size=13, anchor="start", bold=True)
    s.text(40, 74, "head", size=12, mono=True, bold=True)
    s.arrow(60, 70, 88, 70, color=ACCENT, w=2)
    xs = [90, 230, 370]
    for k, v in enumerate(["10", "20", "30"]):
        _node(s, xs[k], 53, v)
        if k < 2:
            s.arrow(xs[k] + 65, 70, xs[k + 1] - 2, 70)
    s.path("M435,70 L480,70 L480,125 L115,125 L115,90", color=RED, w=1.8)
    s.text(300, 142, "last->next == head", size=12, color=RED, mono=True, bold=True)
    s.text(20, 172, "Traverse with do { ... } while (temp != head);  - a plain while (temp != head) would stop "
                    "before printing anything.", size=11, anchor="start")
    return s.svg()


def one_node_circle():
    s = S(360, 110)
    s.text(40, 52, "head", size=12, mono=True, bold=True)
    s.arrow(60, 48, 88, 48, color=ACCENT, w=2)
    _node(s, 90, 31, "7")
    s.path("M155,48 L200,48 L200,92 L115,92 L115,67", color=RED, w=1.8)
    s.text(215, 52, "head->next == head", size=11, color=RED, mono=True, anchor="start")
    return s.svg()


ALL = {k: v for k, v in globals().items() if callable(v) and not k.startswith("_")
       and k not in ("S", "row")}
