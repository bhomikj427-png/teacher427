"""Figures for the After Effects web study pack. Every function returns an SVG string.

All figures are generated (never hand-drawn) and styled with the site's CSS variables, so they follow the
light/dark theme. Curves are computed: Easy Ease is the cubic Bezier Adobe describes (speed 0, influence
33.33 %), rotations are real rotations about the anchor point. verify.py checks the maths and that every
figure is well-formed XML.

Schematic figures (the window layout, the Timeline) show the default arrangement in outline only; the real
layout varies with workspace and version, and the captions say so.
"""
import math
from html import escape

INK, MUTED, LINE, SOFT, CARD = "var(--ink)", "var(--muted)", "var(--line)", "var(--soft)", "var(--card)"
ACC, ORG, GRN, VIO, RED = "var(--accent)", "var(--g1)", "var(--g2)", "var(--g3)", "var(--bad)"
MONO = 'font-family="JetBrains Mono, Consolas, monospace"'
_uid = [0]


def _id(p):
    _uid[0] += 1
    return f"{p}{_uid[0]}"


def svg(w, h, body, label=""):
    return (f'<svg class="fig-svg" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" '
            f'xmlns="http://www.w3.org/2000/svg">{body}</svg>')


def T(x, y, s, size=13, fill=INK, anchor="start", weight=400, mono=False, extra=""):
    fam = MONO if mono else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}" {fam} {extra}>{escape(str(s))}</text>')


def R(x, y, w, h, fill=CARD, stroke=LINE, sw=1.2, rx=6, extra=""):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}" {extra}/>')


def L(x1, y1, x2, y2, stroke=LINE, sw=1.2, extra=""):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def arrow(x1, y1, x2, y2, color=MUTED, sw=1.4):
    a = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 8 * math.cos(a), y2 - 8 * math.sin(a)
    p1 = (hx + 4 * math.sin(a), hy - 4 * math.cos(a))
    p2 = (hx - 4 * math.sin(a), hy + 4 * math.cos(a))
    return (L(x1, y1, hx, hy, color, sw) +
            f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')


def badge(x, y, n, color=ACC):
    return (f'<circle cx="{x}" cy="{y}" r="10" fill="{color}"/>'
            + T(x, y + 4.5, n, 12, "var(--card)", "middle", 700))


def diamond(x, y, r=6, fill=INK):
    return f'<polygon points="{x},{y - r} {x + r},{y} {x},{y + r} {x - r},{y}" fill="{fill}"/>'


def step(n, body):
    """A click-through group: hidden until the stepper reaches n (site/static/app.js)."""
    return f'<g class="kg" data-step="{n}" style="transition:opacity .25s">{body}</g>'


# ------------------------------------------------------------------ maths (verify.py imports these)
def bezier(p0, p1, p2, p3, u):
    a = (1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0] + 3 * (1 - u) * u ** 2 * p2[0] + u ** 3 * p3[0]
    b = (1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1] + 3 * (1 - u) * u ** 2 * p2[1] + u ** 3 * p3[1]
    return a, b


def ease_value(t, influence=1 / 3):
    """Normalized value (0..1) at normalized time t for Easy Ease on both keyframes.

    Adobe: after Easy Ease each keyframe has speed 0 and influence 33.33 % (UG p.321). As a temporal Bezier
    that is control points (0,0), (influence,0), (1-influence,1), (1,1). Solve x(u) = t by bisection.
    """
    p0, p1, p2, p3 = (0, 0), (influence, 0), (1 - influence, 1), (1, 1)
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if bezier(p0, p1, p2, p3, mid)[0] < t:
            lo = mid
        else:
            hi = mid
    return bezier(p0, p1, p2, p3, (lo + hi) / 2)[1]


def linear_value(t):
    return t


def hold_value(t):
    return 0.0 if t < 1 else 1.0


def rotate(pt, pivot, deg):
    a = math.radians(deg)
    x, y = pt[0] - pivot[0], pt[1] - pivot[1]
    return (pivot[0] + x * math.cos(a) - y * math.sin(a), pivot[1] + x * math.sin(a) + y * math.cos(a))


def rect_corners(pos, anchor, w, h, deg):
    """Corners of a w×h layer whose anchor point (layer space) sits at Position (comp space), rotated deg."""
    tl = (pos[0] - anchor[0], pos[1] - anchor[1])
    pts = [tl, (tl[0] + w, tl[1]), (tl[0] + w, tl[1] + h), (tl[0], tl[1] + h)]
    return [rotate(p, pos, deg) for p in pts]


def loop_cycle(t, period=1.0):
    """loopOut('cycle') of a 0→1 s keyframed bounce: value repeats every period (UG p.616)."""
    u = (t % period) / period
    return math.sin(math.pi * u)  # the keyframed shape: up and back down within the period


def selector_opacity(i, n, start):
    """Range Selector with an Opacity 0 % animator; selection = [start, 1]. Character i's opacity (0..1)."""
    a, b = i / n, (i + 1) / n
    overlap = max(0.0, min(b, 1.0) - max(a, start))
    return 1 - overlap / (b - a)


# ------------------------------------------------------------------ chapter 1
def ui_layout():
    W, H = 700, 430
    b = [R(4, 4, W - 8, H - 8, SOFT, LINE, 1.2, 10)]
    b.append(R(14, 14, W - 28, 34, CARD))
    b.append(T(26, 36, "Tools   V  H  Z  W  C  Y  Q  G  Ctrl+T …", 12.5, MUTED, mono=True))
    b.append(T(W - 26, 36, "workspaces ▸ Default  Learn  Standard …", 12, MUTED, "end"))
    panels = [
        (14, 56, 160, 222, "1", "Project", "your files + comps", ACC),
        (182, 56, 336, 222, "2", "Composition", "the frame you see and drag in", ACC),
        (526, 56, 160, 50, "3", "Info", "colour, x/y", MUTED),
        (526, 112, 160, 50, "4", "Preview", "play settings", MUTED),
        (526, 168, 160, 50, "5", "Effects & Presets", "search, double-click", MUTED),
        (526, 224, 160, 54, "6", "Properties", "transforms (2024+)", MUTED),
    ]
    for x, y, w, h, n, name, job, c in panels:
        b.append(R(x, y, w, h))
        b.append(badge(x + 16, y + 17, n, c))
        b.append(T(x + 32, y + 22, name, 13.5, INK, weight=650))
        b.append(T(x + 12, y + 40, job, 12, MUTED))
    # composition frame inside panel 2
    b.append(R(222, 110, 256, 144, "var(--accent-soft)", ACC, 1.2, 2))
    b.append(T(350, 186, "1920 × 1080 frame", 12, ACC, "middle", 600))
    # timeline
    b.append(R(14, 286, W - 28, 130))
    b.append(badge(30, 303, "7", ACC))
    b.append(T(46, 308, "Timeline", 13.5, INK, weight=650))
    b.append(T(120, 308, "layers + properties (left) · time, bars, keyframes (right)", 12, MUTED))
    b.append(L(250, 318, 250, 408, LINE))
    for i, (nm, x1, x2) in enumerate([("Title", 300, 560), ("Shape", 270, 640), ("Background", 256, 676)]):
        y = 326 + i * 28
        b.append(T(30, y + 13, f"{i + 1}  {nm}", 12.5, INK, mono=True))
        b.append(R(x1, y, x2 - x1, 18, "var(--accent-soft)", ACC, 1, 4))
    b.append(L(430, 316, 430, 410, RED, 1.8))
    b.append(T(434, 326, "CTI", 11.5, RED, weight=700))
    return svg(W, H, "".join(b), "After Effects window: Project, Composition, side panels, Timeline")


def containers():
    W, H = 640, 250
    boxes = [("Project  (.aep file)", "links to your source files", 10, 10, 620, 230, MUTED),
             ("Composition", "frame + frame rate + duration + its own timeline", 30, 44, 580, 186, ACC),
             ("Layer", "one use of a footage item, or a shape / text / solid / null", 50, 84, 540, 136, GRN),
             ("Property", "Position, Scale, Opacity, an effect setting…", 70, 124, 500, 86, ORG),
             ("Keyframe", "the value of one property at one time", 90, 164, 460, 36, VIO)]
    b = []
    for name, note, x, y, w, h, c in boxes:
        b.append(R(x, y, w, h, CARD if c != VIO else "var(--soft)", c, 1.4, 8))
        b.append(T(x + 12, y + 22, name, 14, c, weight=700))
        b.append(T(x + w - 12, y + 22, note, 12, MUTED, "end"))
    return svg(W, H, "".join(b), "Containers: project, composition, layer, property, keyframe")


def timeline_anatomy():
    W, H = 700, 260
    b = [R(4, 4, W - 8, H - 8, CARD, LINE, 1.2, 10)]
    b.append(T(18, 32, "0;00;02;00", 16, ACC, weight=700, mono=True))
    b.append(L(250, 12, 250, 250))
    x0, x1 = 262, 684
    sec = (x1 - x0) / 6
    for s in range(7):
        x = x0 + s * sec
        b.append(L(x, 40, x, 48, MUTED))
        b.append(T(x, 36, f"{s}s", 11, MUTED, "middle", mono=True))
    b.append(R(x0 + 0.5 * sec, 52, 4 * sec, 8, "var(--zero)", "none", 0, 3))
    rows = [("1", "Title", 1.0, 5.5), ("2", "Shape", 0, 6), ("  Position", None, 0, 0), ("3", "Background", 0, 6)]
    y = 72
    for n, nm, a, z in rows:
        if nm is None:
            b.append(T(40, y + 13, n.strip(), 12.5, INK, mono=True))
            b.append(T(22, y + 13, "⏱", 12, ORG))
            for k in (0.5, 2.0, 3.5):
                b.append(diamond(x0 + k * sec, y + 9, 6, ORG))
        else:
            b.append(R(18, y + 1, 14, 14, SOFT, LINE, 1, 3))
            b.append(T(40, y + 13, f"{n}  {nm}", 12.5, INK, mono=True))
            b.append(R(x0 + a * sec, y, (z - a) * sec, 18, "var(--accent-soft)", ACC, 1, 4))
        y += 30
    cti = x0 + 2 * sec
    b.append(L(cti, 40, cti, 196, RED, 1.8))
    b.append(f'<polygon points="{cti - 6},{40} {cti + 6},{40} {cti},{48}" fill="{RED}"/>')
    notes = [(18, 222, "1 current time"), (150, 222, "2 switches + layer names"), (300, 222, "3 work area (grey bar)"),
             (470, 222, "4 CTI"), (560, 222, "5 keyframes ◆")]
    for x, yy, s in notes:
        b.append(T(x, yy + 14, s, 12, MUTED))
    return svg(W, H, "".join(b), "Timeline anatomy")


# ------------------------------------------------------------------ chapter 2
def layer_stack():
    W, H = 640, 230
    b = []
    layers = [("3  Background (solid)", SOFT), ("2  Circle (shape)", "var(--accent-soft)"), ("1  TITLE (text)", CARD)]
    for i, (nm, f) in enumerate(reversed(layers)):
        y = 30 + i * 52
        b.append(R(20, y, 260, 40, f, LINE if i else INK, 1.2, 6))
        b.append(T(34, y + 25, nm, 13.5, INK, mono=True))
    b.append(arrow(300, 170, 300, 40, ORG, 2))
    b.append(T(312, 110, "renders", 12.5, ORG, weight=600))
    b.append(T(312, 126, "bottom → top", 12.5, ORG, weight=600))
    b.append(R(420, 30, 200, 144, SOFT, LINE, 1.2, 4))
    b.append(f'<circle cx="520" cy="102" r="46" fill="{ACC}" fill-opacity=".55"/>')
    b.append(T(520, 110, "TITLE", 24, INK, "middle", 800))
    b.append(T(520, 200, "result: top layer in front", 12.5, MUTED, "middle"))
    return svg(W, H, "".join(b), "Layer stacking order")


def anchor_rotation():
    W, H = 660, 250
    b = []
    for k, (title, anchor) in enumerate([("anchor at centre", (60, 30)), ("anchor at top-left corner", (0, 0))]):
        ox = 40 + k * 330
        pos = (ox + 130, 125)
        ghost = rect_corners(pos, anchor, 120, 60, 0)
        rot = rect_corners(pos, anchor, 120, 60, 35)
        b.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in ghost)
                 + f'" fill="none" stroke="{MUTED}" stroke-dasharray="5 4" stroke-width="1.3"/>')
        b.append('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in rot)
                 + f'" fill="{ACC}" fill-opacity=".22" stroke="{ACC}" stroke-width="1.6"/>')
        px, py = pos
        b.append(f'<circle cx="{px}" cy="{py}" r="7" fill="none" stroke="{ORG}" stroke-width="2"/>')
        b.append(L(px - 11, py, px + 11, py, ORG, 2) + L(px, py - 11, px, py + 11, ORG, 2))
        b.append(T(ox + 130, 232, title, 13.5, INK, "middle", 650))
        b.append(T(ox + 130, 30, "Rotation 0° → 35°", 12, MUTED, "middle"))
    return svg(W, H, "".join(b), "Rotation happens around the anchor point")


def transform_keys():
    W, H = 640, 170
    keys = [("A", "Anchor Point", "pivot"), ("P", "Position", "where"), ("S", "Scale", "size"),
            ("R", "Rotation", "turn"), ("T", "Opacity", "see-through")]
    b = []
    for i, (k, name, gist) in enumerate(keys):
        x = 20 + i * 124
        b.append(R(x + 30, 16, 52, 52, CARD, INK, 1.6, 9))
        b.append(T(x + 56, 51, k, 24, INK, "middle", 800, mono=True))
        b.append(T(x + 56, 92, name, 13.5, INK, "middle", 650))
        b.append(T(x + 56, 110, gist, 12, MUTED, "middle"))
    b.append(T(320, 150, "U = only animated properties     UU = everything you changed", 13, ACC, "middle", 600, mono=True))
    return svg(W, H, "".join(b), "Transform property keys A P S R T")


def parenting():
    W, H = 660, 230
    b = []
    kids = [(-70, -40, "text"), (80, -20, "shape"), (0, 60, "shape")]
    for k, (title, npos, ang) in enumerate([("null at rest", (150, 115), 0), ("move + rotate the null", (190, 120), 25)]):
        ox = k * 330
        nx, ny = ox + npos[0], npos[1]
        b.append(R(nx - 12, ny - 12, 24, 24, "none", MUTED, 1.4, 2, 'stroke-dasharray="4 3"'))
        for dx, dy, kind in kids:
            cx, cy = rotate((nx + dx, ny + dy), (nx, ny), ang)
            b.append(L(nx, ny, cx, cy, LINE, 1.1, 'stroke-dasharray="3 3"'))
            if kind == "text":
                b.append(T(cx, cy + 6, "Aa", 18, INK, "middle", 800, extra=f'transform="rotate({ang} {cx:.1f} {cy:.1f})"'))
            else:
                b.append(f'<rect x="{cx - 13:.1f}" y="{cy - 13:.1f}" width="26" height="26" rx="4" fill="{ACC}" fill-opacity=".45" '
                         f'transform="rotate({ang} {cx:.1f} {cy:.1f})"/>')
        b.append(T(ox + 165, 218, title, 13.5, INK, "middle", 650))
    b.append(arrow(300, 115, 350, 115, ORG, 2))
    return svg(W, H, "".join(b), "Children follow their parent null")


# ------------------------------------------------------------------ chapter 3
def _graph(x, y, w, h, fn, title, color, frames=15):
    b = [R(x, y, w, h, CARD, LINE, 1.1, 6)]
    pts = [(x + 14 + (w - 28) * i / 200, y + h - 40 - (h - 72) * fn(i / 200)) for i in range(201)]
    if fn is hold_value:
        pts = [(x + 14, y + h - 40), (x + w - 14, y + h - 40), (x + w - 14, y + 32)]
    b.append('<polyline points="' + " ".join(f"{a:.1f},{c:.1f}" for a, c in pts)
             + f'" fill="none" stroke="{color}" stroke-width="2.2"/>')
    b.append(diamond(x + 14, y + h - 40, 6, INK) + diamond(x + w - 14, y + 32, 6, INK))
    b.append(T(x + w / 2, y + 20, title, 13.5, INK, "middle", 700))
    # frame dots = where the layer is on each frame (motion-path spacing)
    for i in range(frames + 1):
        v = fn(i / frames) if fn is not hold_value else (1.0 if i == frames else 0.0)
        b.append(f'<circle cx="{x + 14 + (w - 28) * v:.1f}" cy="{y + h - 16}" r="3" fill="{color}"/>')
    return "".join(b)


def interp_graphs():
    W, H, w = 660, 210, 206
    b = [_graph(10, 8, w, 190, linear_value, "Linear", MUTED),
         _graph(227, 8, w, 190, ease_value, "Easy Ease (F9)", ACC),
         _graph(444, 8, w, 190, hold_value, "Hold", ORG)]
    return svg(W, H, "".join(b), "Value over time for linear, eased and hold keyframes, with one dot per frame")


def speed_graphs():
    W, H = 640, 220
    b = []
    n = 200
    for k, (title, fn, c) in enumerate([("Linear: constant speed", linear_value, MUTED), ("Easy Ease: 0 → peak → 0", ease_value, ACC)]):
        x, y, w, h = 10 + k * 320, 10, 300, 190
        b.append(R(x, y, w, h, CARD, LINE, 1.1, 6))
        sp = [(fn(min(1, (i + 1) / n)) - fn(max(0, (i - 1) / n))) / (2 / n) for i in range(n + 1)]
        sp[0], sp[-1] = (fn(1 / n) - fn(0)) * n, (fn(1) - fn(1 - 1 / n)) * n
        base, scale = y + h - 30, (h - 70) / 1.6
        pts = [(x + 16 + (w - 32) * i / n, base - scale * s) for i, s in enumerate(sp)]
        area = f"{x + 16},{base} " + " ".join(f"{a:.1f},{c2:.1f}" for a, c2 in pts) + f" {x + w - 16},{base}"
        b.append(f'<polygon points="{area}" fill="{c}" fill-opacity=".15"/>')
        b.append('<polyline points="' + " ".join(f"{a:.1f},{c2:.1f}" for a, c2 in pts) + f'" fill="none" stroke="{c}" stroke-width="2.2"/>')
        b.append(L(x + 16, base, x + w - 16, base, LINE))
        b.append(T(x + w / 2, y + 22, title, 13.5, INK, "middle", 700))
        b.append(T(x + w / 2, base + 20, "shaded area = distance travelled (same in both)", 11.5, MUTED, "middle"))
    return svg(W, H, "".join(b), "Speed graphs: linear vs eased")


def boomerang():
    W, H = 620, 200
    A, B, C = (70, 140), (310, 140), (550, 60)
    b = [T(310, 24, "schematic · keyframes 2 and 3 have the same value", 12, MUTED, "middle")]
    b.append(f'<path d="M{A[0]},{A[1]} C 190,140 250,150 {B[0]},{B[1]} C 360,132 380,190 330,176 '
             f'C 290,165 300,138 {B[0]},{B[1]} C 380,140 470,70 {C[0]},{C[1]}" fill="none" stroke="{RED}" stroke-width="2"/>')
    b.append(f'<path d="M{A[0]},{A[1]} L{B[0]},{B[1]} L{C[0]},{C[1]}" fill="none" stroke="{GRN}" stroke-width="2" stroke-dasharray="6 5"/>')
    for p, lab in [(A, "1"), (B, "2 = 3"), (C, "4")]:
        b.append(R(p[0] - 6, p[1] - 6, 12, 12, INK, "none", 0, 1))
        b.append(T(p[0], p[1] - 14, lab, 12.5, INK, "middle", 700))
    b.append(T(360, 196, "red: Auto Bezier drifts out and back", 12.5, RED, "start", 600))
    b.append(T(70, 196, "green dashed: Linear / Hold stays put", 12.5, GRN, "start", 600))
    return svg(W, H, "".join(b), "Boomerang drift between equal keyframes")


# ------------------------------------------------------------------ chapter 4
def shape_anatomy():
    W, H = 660, 250
    rows = [(0, "▾ Shape Layer 1", INK, 700), (1, "▾ Contents", INK, 600), (2, "▾ Rectangle 1   (group)", ACC, 650),
            (3, "Rectangle Path 1   ← the path (Size, Roundness)", INK, 400), (3, "Stroke 1   ← line along the path", ORG, 400),
            (3, "Fill 1   ← colour inside", GRN, 400), (3, "Transform: Rectangle 1", MUTED, 400),
            (2, "Add ▸  Trim Paths, Repeater, Round Corners…", VIO, 600), (1, "▸ Transform   (the layer's A P S R T)", MUTED, 400)]
    b = []
    for i, (ind, s, c, wgt) in enumerate(rows):
        b.append(T(14 + ind * 22, 26 + i * 25, s, 13, c, weight=wgt, mono=True))
    b.append(R(498, 60, 140, 96, GRN, ORG, 6, 12, 'fill-opacity=".35"'))
    b.append(T(568, 184, "result", 12.5, MUTED, "middle"))
    return svg(W, H, "".join(b), "Inside a shape layer")


def trim_paths():
    W, H = 640, 250
    path = "M40,170 C120,40 200,40 260,120 S400,220 470,110 S580,40 600,70"
    b = []
    pid = _id("tp")
    b.append(f'<path id="{pid}" d="{path}" fill="none" stroke="{LINE}" stroke-width="10" stroke-linecap="round"/>')
    stages = [(0.35, "End 35 %"), (0.7, "End 70 %"), (1.0, "End 100 %")]
    b.append(T(320, 230, "Trim Paths: keyframe End 0 % → 100 % and the line draws itself on", 12.5, MUTED, "middle"))
    for k, (e, lab) in enumerate(stages, 1):
        b.append(step(k, f'<path d="{path}" fill="none" stroke="{ACC}" stroke-width="10" stroke-linecap="round" '
                         f'pathLength="100" stroke-dasharray="{e * 100:.0f} 200"/>'
                         + T(40 + 190 * (k - 1), 24, lab, 13.5, ACC, weight=700, mono=True)))
    return svg(W, H, "".join(b), "Trim Paths end percentage drawing a line on")


def text_animator():
    W, H = 640, 280
    word, n = "MOTION", 6
    b = [T(320, 22, "Animator: Opacity 0 %   ·   keyframe Range Selector Start 0 % → 100 %", 12.5, MUTED, "middle")]
    for k, start in enumerate([0.0, 1 / 3, 2 / 3, 1.0]):
        y = 70 + k * 56
        body = T(70, y - 4, f"Start {start * 100:.0f} %", 12.5, ORG, "end", 700, mono=True)
        bx = 90 + 460 * start
        body += R(bx, y - 38, 550 - bx, 46, "var(--g1)", "none", 0, 4, 'fill-opacity=".10"')
        for i, ch in enumerate(word):
            op = selector_opacity(i, n, start)
            body += T(110 + i * 76, y, ch, 34, INK, "middle", 800, extra=f'fill-opacity="{max(op, .06):.2f}"')
        b.append(step(k, body) if k else body)
    return svg(W, H, "".join(b), "Range selector sweeping across characters")


def track_matte():
    W, H = 660, 210
    g, c = _id("tmg"), _id("tmc")
    b = [f'<defs><linearGradient id="{g}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#2f5bea"/>'
         f'<stop offset=".5" stop-color="#b23fbf"/><stop offset="1" stop-color="#e0661b"/></linearGradient>'
         f'<clipPath id="{c}"><text x="550" y="120" font-size="74" font-weight="900" text-anchor="middle">GO</text></clipPath></defs>']
    for i, (title, note) in enumerate([("matte: text layer", "alpha = where to show"), ("fill: gradient layer", "what shows"),
                                       ("result", "fill seen through the matte")]):
        x = 20 + i * 215
        b.append(R(x, 20, 190, 140, SOFT, LINE, 1.1, 6))
        b.append(T(x + 95, 184, title, 13.5, INK, "middle", 650))
        b.append(T(x + 95, 202, note, 12, MUTED, "middle"))
    b.append(T(115, 120, "GO", 74, INK, "middle", 900))
    b.append(f'<rect x="235" y="20" width="190" height="140" rx="6" fill="url(#{g})"/>')
    b.append(f'<rect x="450" y="20" width="190" height="140" fill="url(#{g})" clip-path="url(#{c})"/>')
    b.append(T(210, 96, "+", 26, MUTED, "middle") + T(437, 96, "=", 26, MUTED, "middle"))
    return svg(W, H, "".join(b), "Alpha track matte: text shows a gradient")


def mask_or_shape():
    W, H = 640, 220
    b = [R(20, 86, 150, 48, CARD, INK, 1.4, 8), T(95, 107, "draw with", 12.5, MUTED, "middle"),
         T(95, 124, "Q or G", 14, INK, "middle", 700, mono=True)]
    b.append(R(215, 86, 150, 48, CARD, ORG, 1.4, 24) + T(290, 115, "layer selected?", 13, ORG, "middle", 700))
    b.append(arrow(170, 110, 213, 110))
    outs = [(30, "nothing selected", "→ NEW shape layer", GRN), (100, "a shape layer", "→ shape added to it", ACC),
            (170, "any other layer", "→ a MASK on it", RED)]
    for y, cond, res, col in outs:
        b.append(arrow(365, 110, 420, y + 16))
        b.append(R(422, y, 200, 40, CARD, col, 1.4, 8))
        b.append(T(432, y + 16, cond, 12, MUTED) + T(432, y + 33, res, 13, col, weight=700))
    return svg(W, H, "".join(b), "What a shape tool draws depends on the selection")


# ------------------------------------------------------------------ chapter 5
def render_order():
    W, H = 660, 230
    stepsx = [("source", MUTED), ("masks", ORG), ("effects", VIO), ("transform", ACC), ("layer styles", GRN)]
    b = [T(20, 26, "inside ONE layer", 13, INK, weight=700)]
    for i, (s, c) in enumerate(stepsx):
        x = 20 + i * 126
        b.append(R(x, 40, 104, 44, CARD, c, 1.6, 8) + T(x + 52, 67, s, 13.5, c, "middle", 700))
        if i:
            b.append(arrow(x - 22, 62, x - 2, 62))
    b.append(T(20, 124, "then the comp, layer by layer", 13, INK, weight=700))
    for i, nm in enumerate(["layer 3 (bottom)", "layer 2", "layer 1 (top)"]):
        x = 20 + i * 214
        b.append(R(x, 138, 180, 40, SOFT, LINE, 1.2, 6) + T(x + 90, 163, nm, 13, INK, "middle", 600))
        if i:
            b.append(arrow(x - 32, 158, x - 4, 158, ORG, 1.8))
    b.append(T(330, 212, "each finished layer is the input the next one is drawn over", 12.5, MUTED, "middle"))
    return svg(W, H, "".join(b), "Render order: masks, effects, transform, styles; bottom layer first")


def adjustment_layer():
    W, H = 620, 230
    rows = [("1  Title", False), ("2  Adjustment Layer  ·  Glow", True), ("3  Shapes", False), ("4  Background", False)]
    b = []
    for i, (nm, adj) in enumerate(rows):
        y = 20 + i * 48
        b.append(R(20, y, 330, 38, "var(--g3)" if adj else CARD, VIO if adj else LINE, 1.4, 6,
                   'fill-opacity=".14"' if adj else ""))
        b.append(T(34, y + 24, nm, 13.5, VIO if adj else INK, weight=700 if adj else 400, mono=True))
    b.append(f'<path d="M370,120 h18 v90 h-18" fill="none" stroke="{VIO}" stroke-width="2"/>')
    b.append(T(398, 162, "Glow applies to", 13, VIO, weight=650) + T(398, 180, "everything below", 13, VIO, weight=650))
    b.append(T(398, 44, "not affected", 13, MUTED, weight=600))
    return svg(W, H, "".join(b), "An adjustment layer affects the layers beneath it")


def precompose_fig():
    W, H = 660, 220
    b = [T(110, 22, "before", 13.5, INK, "middle", 700), T(510, 22, "after Ctrl+Shift+C", 13.5, INK, "middle", 700)]
    for i, nm in enumerate(["Title", "Line", "Circle"]):
        b.append(R(20, 36 + i * 44, 180, 34, CARD, LINE) + T(34, 58 + i * 44, f"{i + 1}  {nm}", 13, INK, mono=True))
    b.append(R(20, 168, 180, 34, SOFT, LINE) + T(34, 190, "4  Background", 13, INK, mono=True))
    b.append(arrow(215, 100, 290, 100, ORG, 2))
    b.append(R(310, 36, 180, 34, "var(--accent-soft)", ACC, 1.6) + T(324, 58, "1  Logo  (precomp)", 13, ACC, weight=700, mono=True))
    b.append(R(310, 80, 180, 34, SOFT, LINE) + T(324, 102, "2  Background", 13, INK, mono=True))
    b.append(R(512, 36, 136, 150, CARD, ACC, 1.2, 8, 'stroke-dasharray="5 4"'))
    b.append(T(580, 58, "inside Logo:", 12, ACC, "middle", 600))
    for i, nm in enumerate(["Title", "Line", "Circle"]):
        b.append(T(530, 86 + i * 26, nm, 12.5, INK, mono=True))
    b.append(L(490, 53, 512, 53, ACC, 1.2, 'stroke-dasharray="3 3"'))
    return svg(W, H, "".join(b), "Pre-composing three layers into one")


def expr_plots():
    W, H = 660, 220
    b = []
    # time * 90
    x, y, w, h = 10, 10, 310, 196
    b.append(R(x, y, w, h, CARD, LINE, 1.1, 6) + T(x + w / 2, y + 22, "time * 90  (on Rotation)", 13.5, INK, "middle", 700, mono=True))
    x0, yb, sx, sy = x + 30, y + h - 30, (w - 50) / 4, (h - 70) / 360
    b.append(L(x0, yb, x0 + 4 * sx, yb) + L(x0, yb, x0, y + 34))
    b.append('<polyline points="' + " ".join(f"{x0 + t * sx:.1f},{yb - (90 * t) * sy:.1f}" for t in (0, 4))
             + f'" fill="none" stroke="{ACC}" stroke-width="2.2"/>')
    for t in range(5):
        b.append(T(x0 + t * sx, yb + 15, f"{t}s", 11, MUTED, "middle", mono=True))
    b.append(T(x0 + 4 * sx - 4, yb - 360 * sy + 14, "360°", 11.5, ACC, "end", mono=True))
    # loopOut
    x = 340
    b.append(R(x, y, w, h, CARD, LINE, 1.1, 6) + T(x + w / 2, y + 22, 'loopOut("cycle")', 13.5, INK, "middle", 700, mono=True))
    x0, sy2 = x + 30, (h - 80)
    b.append(L(x0, yb, x0 + 4 * sx, yb))
    kf = [(x0 + t / 100 * sx, yb - loop_cycle(t / 100) * sy2) for t in range(0, 101)]
    lp = [(x0 + t / 100 * sx, yb - loop_cycle(t / 100) * sy2) for t in range(100, 401)]
    b.append('<polyline points="' + " ".join(f"{a:.1f},{c:.1f}" for a, c in kf) + f'" fill="none" stroke="{ACC}" stroke-width="2.4"/>')
    b.append('<polyline points="' + " ".join(f"{a:.1f},{c:.1f}" for a, c in lp)
             + f'" fill="none" stroke="{ORG}" stroke-width="2" stroke-dasharray="6 4"/>')
    for t in range(5):
        b.append(T(x0 + t * sx, yb + 15, f"{t}s", 11, MUTED, "middle", mono=True))
    b.append(T(x0 + 0.5 * sx, y + 44, "keyframed", 11.5, ACC, "middle", 600) + T(x0 + 2.5 * sx, y + 44, "repeated by the expression", 11.5, ORG, "middle", 600))
    return svg(W, H, "".join(b), "Expressions as graphs over time")


# ------------------------------------------------------------------ chapter 6
def preview_cache():
    W, H = 660, 130
    x0, x1 = 30, 630
    b = [L(x0, 60, x1, 60, LINE, 1.2)]
    for s in range(11):
        x = x0 + (x1 - x0) * s / 10
        b.append(L(x, 54, x, 66, MUTED) + T(x, 46, f"{s}s", 11, MUTED, "middle", mono=True))
    b.append(R(x0 + 60, 74, 480, 8, "var(--zero)", "none", 0, 3))
    b.append(R(x0 + 60, 88, 300, 8, GRN, "none", 0, 3))
    b.append(L(x0 + 360, 30, x0 + 360, 104, RED, 1.8))
    b.append(T(x0 + 60, 118, "grey = work area   ·   green = cached in RAM: plays in real time   ·   red = CTI", 12, MUTED))
    return svg(W, H, "".join(b), "Work area and green cache bar")


def render_queue():
    W, H = 680, 150
    stages = [("Composition", "select it", MUTED), ("Ctrl+M", "Add to Render Queue", INK), ("Render Settings", "Best Settings", ACC),
              ("Output Module", "H.264  (not Lossless)", ORG), ("Output To", "name + folder", GRN), ("Render", "→ file.mp4", VIO)]
    b = []
    for i, (s, sub, c) in enumerate(stages):
        x = 8 + i * 113
        b.append(R(x, 34, 100, 58, CARD, c, 1.6, 8))
        b.append(T(x + 50, 58, s, 12.5, c, "middle", 700))
        b.append(T(x + 50, 78, sub, 10.5, MUTED, "middle"))
        if i:
            b.append(arrow(x - 13, 63, x - 1, 63))
    b.append(T(340, 126, "render settings = how frames are computed · output module = how they are encoded", 12, MUTED, "middle"))
    return svg(W, H, "".join(b), "Render Queue steps")


# ------------------------------------------------------------------ chapter 7: keyboard map
_ROWS = [
    [("Esc", 1)] + [(f"F{i}", 1) for i in range(1, 13)],
    [("`", 1)] + [(c, 1) for c in "1234567890"] + [("-", 1), ("=", 1), ("⌫", 2)],
    [("Tab", 1.5)] + [(c, 1) for c in "QWERTYUIOP"] + [("[", 1), ("]", 1), ("\\", 1.5)],
    [("Caps", 1.75)] + [(c, 1) for c in "ASDFGHJKL"] + [(";", 1), ("'", 1), ("Enter", 2.25)],
    [("Shift", 2.25)] + [(c, 1) for c in "ZXCVBNM"] + [(",", 1), (".", 1), ("/", 1), ("Shift ", 2.75)],
    [("Ctrl", 1.5), ("Win", 1.25), ("Alt", 1.25), ("Space", 6.25), ("Alt ", 1.25), ("Ctrl ", 1.5)],
]
_NAV = [("Home", 0, 1), ("PgUp", 1, 1), ("End", 0, 2), ("PgDn", 1, 2), ("↑", 0.5, 4), ("←", -0.5, 5), ("↓", 0.5, 5), ("→", 1.5, 5)]
CAT = {"file": ACC, "tool": GRN, "prop": ORG, "time": VIO, "key": RED, "mod": MUTED}


def keyboard(hl):
    """hl: {key label: category}. Unhighlighted keys stay faint so the pattern reads at a glance."""
    u, g = 38, 4
    W, H = 15.5 * u + 4 * u, 6 * u + 20
    b = []

    def cap(x, y, w, lab):
        cat = hl.get(lab.strip())
        if cat:
            c = CAT[cat]
            return (R(x, y, w - g, u - g, c, c, 1.4, 5, 'fill-opacity=".18"')
                    + T(x + (w - g) / 2, y + u / 2 + 3, lab.strip(), 12 if len(lab.strip()) < 4 else 10, c, "middle", 800, mono=True))
        return (R(x, y, w - g, u - g, CARD, LINE, 1, 5)
                + T(x + (w - g) / 2, y + u / 2 + 3, lab.strip(), 10.5 if len(lab.strip()) < 4 else 9, "var(--zero)", "middle", 500, mono=True))

    for r, row in enumerate(_ROWS):
        x, y = 4, 4 + r * u + (6 if r else 0)
        for lab, w in row:
            if r == 0 and lab in ("F1", "F5", "F9"):
                x += 0.35 * u
            b.append(cap(x, y, w * u, lab))
            x += w * u
    nx = 4 + 15.4 * u
    for lab, cx, cy in _NAV:
        b.append(cap(nx + (cx + 0.6) * u, 4 + cy * u + 6, u, lab))
    return svg(W, H, "".join(b), "Keyboard map of highlighted shortcuts")


KB = {
    "files": {"N": "file", "K": "file", "I": "file", "S": "file", "Z": "file", "M": "file", "Ctrl": "mod", "Shift": "mod", "Alt": "mod"},
    "tools": {"V": "tool", "Y": "tool", "Q": "tool", "G": "tool", "T": "tool", "H": "tool", "W": "tool", "Space": "tool", "Ctrl": "mod"},
    "props": {"A": "prop", "P": "prop", "S": "prop", "R": "prop", "T": "prop", "U": "prop", "E": "prop", "M": "prop", "F": "prop"},
    "time": {"J": "time", "K": "time", "B": "time", "N": "time", "I": "time", "O": "time", "Home": "time", "End": "time",
             "PgUp": "time", "PgDn": "time", "D": "time", "=": "time", "-": "time", ";": "time"},
    "keys": {"F9": "key", "F3": "key", "Alt": "mod", "Shift": "mod", "P": "prop", "S": "prop", "R": "prop", "T": "prop",
             "Ctrl": "mod", "K": "key", "H": "key", "→": "key", "←": "key"},
    "layers": {"Y": "file", "D": "file", "C": "file", "[": "time", "]": "time", "L": "file", "F4": "key", "Ctrl": "mod",
               "Alt": "mod", "Shift": "mod", "↑": "file", "↓": "file"},
    "views": {"\\": "key", "`": "key", ".": "key", ",": "key", "/": "key", "J": "key", "'": "key", "R": "key", "F5": "key",
              "Shift": "mod", "Ctrl": "mod"},
    "export": {"M": "file", "S": "file", "0": "file", "3": "file", "5": "file", "Ctrl": "mod", "Alt": "mod", "Shift": "mod"},
}


def _kb(name):
    return lambda: keyboard(KB[name])


# ------------------------------------------------------------------ chapter 8: the build
BUILD = [("Background (solid + Gradient Ramp)", 0, 15, MUTED), ("Line draws on (Trim Paths)", 0.5, 2.0, ACC),
         ("Title reveal (text animator)", 1.5, 3.5, ORG), ("Accents pop (Scale + F9)", 3.0, 4.5, GRN),
         ("Null push-in (Scale 100 → 105 %)", 0, 15, VIO), ("Glow + wiggle (polish)", 0, 15, MUTED),
         ("Fade out (Opacity)", 13, 15, RED)]


def storyboard(hl=None):
    W, H = 680, 44 + 30 * len(BUILD) + 20
    x0, x1 = 250, 668
    sx = (x1 - x0) / 15
    b = []
    for s in range(0, 16, 1):
        x = x0 + s * sx
        b.append(L(x, 30, x, H - 16, LINE, 0.8) + (T(x, 22, f"{s}", 11, MUTED, "middle", mono=True) if s % 5 == 0 or s in (1, 2, 3, 4) else ""))
    for i, (nm, a, z, c) in enumerate(BUILD):
        y = 40 + i * 30
        on = hl is None or hl == i
        b.append(T(10, y + 14, f"{i + 1}. {nm}", 12, INK if on else MUTED, weight=650 if hl == i else 400))
        b.append(R(x0 + a * sx, y, (z - a) * sx, 18, c, c, 1, 4, f'fill-opacity="{".45" if on else ".10"}"'))
    b.append(T(x1, H - 2, "seconds", 11, MUTED, "end"))
    return svg(W, H, "".join(b), "Storyboard of the 15-second title sting")


def _sb(i):
    return lambda: storyboard(i)


ALL = {
    "ui_layout": ui_layout, "containers": containers, "timeline_anatomy": timeline_anatomy,
    "layer_stack": layer_stack, "anchor_rotation": anchor_rotation, "transform_keys": transform_keys, "parenting": parenting,
    "interp_graphs": interp_graphs, "speed_graphs": speed_graphs, "boomerang": boomerang,
    "shape_anatomy": shape_anatomy, "trim_paths": trim_paths, "text_animator": text_animator, "track_matte": track_matte,
    "mask_or_shape": mask_or_shape,
    "render_order": render_order, "adjustment_layer": adjustment_layer, "precompose": precompose_fig, "expr_plots": expr_plots,
    "preview_cache": preview_cache, "render_queue": render_queue,
    "storyboard": storyboard,
    **{f"kb_{k}": _kb(k) for k in KB},
    **{f"sb_{i}": _sb(i) for i in range(len(BUILD))},
}
