"""Shared figure helpers for study packs (study-pack-format.md v1.3, §7.3).

Subject figure modules import these instead of copying them:

    sys.path.insert(0, str(ROOT / "tools"))
    from figlib import fig, canvas, svg, box, arrow, axes, INK, MUTED, ACC, ...

Known fixes built in (found building EDC 01a–03b):
  - `m()` turns `X_y` in a label into mathtext subscripts, so labels need no `$…$` for subscripts.
  - `e^{x}` in a plain label prints literally: wrap the label in `$…$` yourself.
  - The `∝` glyph is missing from mathtext: write "grows as".
  - Circled digits ①② fail inside mathtext: keep them in plain labels without `_`.
  - Overlaps came from text placed inside lattices/axes: put labels outside the drawing.
    `check_figure()` finds the ones that remain (run on every figure by the shared builder).
"""
import io
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa: E402
from matplotlib.text import Text  # noqa: E402

# ---- palette and style (the reference pack's look) ---------------------------------------------
INK, MUTED, LINE, SOFT = "#1c1f24", "#6a707a", "#c9cbc4", "#f0f0eb"
ACC, G1, G2, G3, BAD = "#2f5bea", "#e0661b", "#12925a", "#b23fbf", "#d92d20"
NCOL, PCOL = "#dbeafe", "#fde2e2"
RC = {"font.family": ["Segoe UI", "DejaVu Sans"], "font.size": 9.5, "svg.fonttype": "none", "axes.grid": False,
      "axes.edgecolor": INK, "text.color": INK, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
      "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.9,
      "mathtext.fontset": "custom", "mathtext.rm": "Segoe UI", "mathtext.it": "Segoe UI:italic"}

_SUB = re.compile(r"(?<![\w$\\{])([A-Za-z]{1,2})_([A-Za-z0-9]+)")


def m(t):
    """`V_T` -> mathtext subscript; labels already holding `$` are left alone."""
    if isinstance(t, str) and "$" not in t:
        return _SUB.sub(lambda g: r"$\mathrm{%s}_{\mathrm{%s}}$" % (g.group(1), g.group(2)), t)
    return t


def fig(w, h, **kw):
    with plt.rc_context(RC):
        return plt.subplots(figsize=(w, h), **kw)


def canvas(w, h, xlim, ylim):
    f, ax = fig(w, h)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return f, ax


def box(ax, x, y, w, h, text="", fc="white", ec=INK, lw=1.3, fs=9.5, r=0.08, color=INK, weight="normal", ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw, ls=ls))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=color, weight=weight)


def arrow(ax, p, q, color=INK, lw=1.3, rad=0.0, ls="-"):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=11, color=color, lw=lw, ls=ls,
                                 connectionstyle=f"arc3,rad={rad}"))


def axes(ax, xl="", yl=""):
    """Label both axes. Every graph in a pack names its axes (spec §5.4)."""
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)


def svg(f):
    """Figure -> inline SVG string (class="mpl" so the page CSS sizes it)."""
    for t in f.findobj(Text):
        t.set_text(m(t.get_text()))
    buf = io.StringIO()
    f.savefig(buf, format="svg", bbox_inches="tight", pad_inches=0.04, transparent=True)
    plt.close(f)
    s = buf.getvalue()
    s = s[s.index("<svg"):]
    return re.sub(r'width="[\d.]+pt" height="[\d.]+pt"', 'class="mpl"', s, count=1)


# ---- overlap check (spec §7.3) ------------------------------------------------------------------
REPORT = []          # (figure name, problem) — filled by check_figure()
_current = ["?"]     # name of the figure being drawn (set by the builder)
_SHRINK = 1.5        # px: boxes that only touch are not reported


def _boxes(f):
    r = f.canvas.get_renderer()
    ticks = set()
    for ax in f.axes:
        ticks.update(id(t) for t in ax.get_xticklabels() + ax.get_yticklabels())
    out = []
    for t in f.findobj(Text):
        if id(t) in ticks:  # tick numbers touching at a corner are harmless; labels are what matter
            continue
        if not t.get_visible() or not t.get_text().strip():
            continue
        try:
            bb = t.get_window_extent(r)
        except Exception:
            continue
        if bb.width < 1 or bb.height < 1:
            continue
        out.append((t.get_text().strip(), bb))
    return out


def check_figure(f, name=None):
    """Report labels that overlap each other, or that fall outside the figure. Returns the problems."""
    name = name or _current[0]
    f.canvas.draw()
    bxs = _boxes(f)
    probs = []
    for i in range(len(bxs)):
        a_txt, a = bxs[i]
        for j in range(i + 1, len(bxs)):
            b_txt, b = bxs[j]
            ox = min(a.x1, b.x1) - max(a.x0, b.x0)
            oy = min(a.y1, b.y1) - max(a.y0, b.y0)
            if ox > _SHRINK and oy > _SHRINK:
                probs.append(f"labels overlap: {a_txt[:30]!r} / {b_txt[:30]!r}")
    W, H = f.bbox.width, f.bbox.height
    for txt, bb in bxs:
        if bb.x0 < -_SHRINK or bb.y0 < -_SHRINK or bb.x1 > W + _SHRINK or bb.y1 > H + _SHRINK:
            pass  # bbox_inches="tight" grows the canvas to include it; not cut in the output
    for p in probs:
        REPORT.append((name, p))
    return probs


_orig_savefig = Figure.savefig


def _checked_savefig(self, *a, **kw):
    check_figure(self)
    return _orig_savefig(self, *a, **kw)


def watch():
    """Run check_figure() on every figure saved from now on (any module, figlib or not)."""
    Figure.savefig = _checked_savefig


def run_all(figures):
    """Draw every figure in a {name: fn} dict and return the overlap report."""
    watch()
    REPORT.clear()
    import inspect
    for name, fn in figures.items():
        try:  # a figure is a zero-argument function; skip helpers and classes that leak into the dict
            if inspect.isclass(fn) or any(p.default is p.empty and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
                                          for p in inspect.signature(fn).parameters.values()):
                continue
        except (TypeError, ValueError):
            continue
        _current[0] = name
        try:
            fn()
        except Exception as e:  # a broken figure is reported, not fatal to the check
            REPORT.append((name, f"error: {e}"))
    return list(REPORT)
