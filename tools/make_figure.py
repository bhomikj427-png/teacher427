#!/usr/bin/env python3
"""
make_figure.py — Python figure renderer for the ece' Visual & Rendering subsystem.

A DISPATCHER over a renderer REGISTRY, not a fixed switch (see ../rendering.md §3, §5). It turns a
declarative figure spec into one self-contained, inline **SVG string** that render_lesson.py embeds
into the browser lesson surface. Sharp, small, deterministic — and never a network call at lesson
time.

WHICH PRIMITIVES LIVE HERE
  Only the two that need real Python/computation (the rest are client-side CDN JS in render_lesson):
    - primitive 4  "Quantitative plot"        -> kind="matplotlib"  (matplotlib + numpy/scipy)
    - primitive 6  "Domain structural diagram" -> kind="structural"  (the subject->renderer REGISTRY)

THE REGISTRY (subject-agnostic by construction)
  Primitive 6 is the ONLY subject-specific slot, and it is an EXTENSIBLE registry, never a fixed
  list. A subject adds a structural renderer by calling register_structural("<subject>", handler) —
  NO edits to this dispatcher. We ship one first entry, "ece" -> schemdraw. If a subject has no
  registered renderer, _structural() raises NoStructuralRenderer; render_lesson catches it and
  applies the §3 fallback (Mermaid/plot best-effort + a one-line note). A lesson is never blocked on
  a missing renderer.

DETERMINISM
  Fixed fonts, sizes, figure size, colors, dpi -> a given spec renders byte-stable across runs.

USAGE
  As a library (the normal path; render_lesson imports this):
    from make_figure import make_figure, register_structural, NoStructuralRenderer
    svg = make_figure({"kind": "matplotlib", "series": [...], ...})
  As a CLI (smoke test): reads a JSON spec, writes an .svg
    python tools/make_figure.py <spec.json> <out.svg>

DEPS: matplotlib, numpy, scipy (primitive 4); schemdraw (the shipped primitive-6 entry). Pinned in
../requirements.txt. schemdraw is imported lazily INSIDE its handler, so a subject that never uses a
structural figure (and never installs schemdraw) still renders fine — the universal path has no
domain dependency.
"""
import io
import sys
import json


# ----------------------------------------------------------------------------- determinism
# One place for every visual constant, so figures look identical run-to-run and subject-to-subject.
FIG_FONT = "DejaVu Sans"          # ships with matplotlib; guaranteed present -> stable text metrics
FIG_FONT_SIZE = 11
FIG_SIZE = (6.2, 3.7)             # inches; a readable card inside the max-width reading column
FIG_DPI = 100
# A fixed, colour-blind-friendly cycle (Okabe-Ito subset) — never rely on matplotlib's default,
# which can shift between versions.
FIG_COLORS = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9"]


def _strip_xml_preamble(svg):
    """Drop the <?xml?> / <!DOCTYPE> preamble so the <svg> embeds inline cleanly in HTML."""
    i = svg.find("<svg")
    return svg[i:] if i != -1 else svg


# ----------------------------------------------------------------------------- primitive 4: matplotlib
def _matplotlib(spec):
    """
    Declarative quantitative plot -> inline SVG. The spec carries DATA, not code (the lesson script
    does any numpy/scipy computation and passes arrays in), keeping this handler pure and reusable.

    spec = {
      "kind": "matplotlib",
      "series": [ {"x": [...], "y": [...], "label": "...", "style": "-"|"--"|":"|"o"} , ... ],
      "xlabel": str, "ylabel": str, "title": str,
      "xscale": "linear"|"log",  "yscale": "linear"|"log",   # optional
      "grid": bool (default True),
      "vlines": [ {"x": float, "label": str} ],              # optional reference lines
      "hlines": [ {"y": float, "label": str} ],              # optional
    }
    """
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({
        "font.family": FIG_FONT,
        "font.size": FIG_FONT_SIZE,
        "svg.fonttype": "none",        # keep text as selectable text, crisp + small
        "axes.prop_cycle": plt.cycler(color=FIG_COLORS),
        "axes.grid": spec.get("grid", True),
        "grid.alpha": 0.3,
        "axes.spines.top": False,
        "axes.spines.right": False,
    })

    fig, ax = plt.subplots(figsize=FIG_SIZE, dpi=FIG_DPI)
    for s in spec.get("series", []):
        ax.plot(s["x"], s["y"], s.get("style", "-"), label=s.get("label"))

    if spec.get("xscale"):
        ax.set_xscale(spec["xscale"])
    if spec.get("yscale"):
        ax.set_yscale(spec["yscale"])
    if spec.get("xlabel"):
        ax.set_xlabel(spec["xlabel"])
    if spec.get("ylabel"):
        ax.set_ylabel(spec["ylabel"])
    if spec.get("title"):
        ax.set_title(spec["title"])

    for v in spec.get("vlines", []):
        ax.axvline(v["x"], color="#888", ls="--", lw=1)
        if v.get("label"):
            ax.annotate(v["label"], xy=(v["x"], 0.02), xycoords=("data", "axes fraction"),
                        rotation=90, va="bottom", ha="right", color="#555", fontsize=9)
    for h in spec.get("hlines", []):
        ax.axhline(h["y"], color="#888", ls="--", lw=1)
        if h.get("label"):
            ax.annotate(h["label"], xy=(0.99, h["y"]), xycoords=("axes fraction", "data"),
                        va="bottom", ha="right", color="#555", fontsize=9)

    if any(s.get("label") for s in spec.get("series", [])):
        ax.legend(frameon=False)

    fig.tight_layout()
    buf = io.StringIO()
    fig.savefig(buf, format="svg", facecolor="white")
    plt.close(fig)
    return _strip_xml_preamble(buf.getvalue())


# ----------------------------------------------------------------------------- primitive 6: registry
class NoStructuralRenderer(Exception):
    """Raised when a structural figure is requested for a subject with no registered renderer.
    render_lesson catches this and applies the §3 fallback (Mermaid/plot + one-line note)."""
    def __init__(self, subject):
        self.subject = subject
        super().__init__(
            f"No structural renderer registered for subject '{subject}'. "
            f"Register one with register_structural('{subject}', handler), or use a Mermaid/plot block."
        )


_STRUCTURAL_REGISTRY = {}   # subject (str) -> handler(spec) -> svg string


def register_structural(subject, handler):
    """Add a subject's structural (primitive-6) renderer. The whole point of the registry: adding a
    domain renderer touches THIS call only, never the dispatcher. Subject-agnostic by construction."""
    _STRUCTURAL_REGISTRY[subject] = handler


def has_structural(subject):
    return subject in _STRUCTURAL_REGISTRY


def _structural(spec):
    subject = spec.get("subject", "")
    handler = _STRUCTURAL_REGISTRY.get(subject)
    if handler is None:
        raise NoStructuralRenderer(subject)
    return handler(spec)


# ---- shipped first entry: ECE -> schemdraw (circuits / op-amps / gates) ----------------------
def _schemdraw_handler(spec):
    """
    First registry entry (ECE). schemdraw is imported HERE, lazily, so subjects that never draw a
    schematic carry no dependency on it.

    Declarative schematic spec — a small element-sequence interpreter (enough for series/ladder
    circuits like an RC filter; extend the directive set as needed):

    spec = {
      "kind": "structural", "subject": "ece",
      "elements": [
        {"e": "SourceV", "d": "up",   "label": "Vin"},
        {"e": "Line",    "d": "right"},
        {"e": "Dot",     "push": true},            # remember this node
        {"e": "Resistor","d": "right","label": "R"},
        {"e": "Dot",     "push": true},
        {"e": "Capacitor","d":"down", "label": "C"},
        {"e": "Ground"},
        {"pop": true},                              # back to the remembered node
        ...
      ]
    }
    Each step: "e"=element class in schemdraw.elements; "d"=direction (right/left/up/down);
    "label"=text; "length"=float; "args"={ctor kwargs}; "push"/"pop"=save/restore drawing position.
    """
    import schemdraw
    import schemdraw.elements as elm

    schemdraw.config(font=FIG_FONT, fontsize=12, color="black", lw=1.6)
    d = schemdraw.Drawing(show=False)
    for step in spec.get("elements", []):
        if step.get("pop"):
            d.pop()
            continue
        E = getattr(elm, step["e"])(**step.get("args", {}))
        if step.get("d"):
            getattr(E, step["d"])()
        if "length" in step:
            E.length(step["length"])
        if "label" in step:
            E.label(step["label"])
        d += E
        if step.get("push"):
            d.push()
    return _strip_xml_preamble(d.get_imagedata("svg").decode("utf-8"))


register_structural("ece", _schemdraw_handler)


# ----------------------------------------------------------------------------- dispatcher
def make_figure(spec):
    """Spec -> inline SVG string. Dispatch is by figure KIND (the primitive family), never by
    subject; subject only matters inside the primitive-6 structural registry."""
    kind = spec.get("kind")
    if kind == "matplotlib":
        return _matplotlib(spec)
    if kind == "structural":
        return _structural(spec)
    raise ValueError(
        f"make_figure: unknown kind {kind!r}. This renderer handles 'matplotlib' (primitive 4) and "
        f"'structural' (primitive 6). MathJax/Mermaid/WaveDrom/code are client-side in render_lesson."
    )


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    svg = make_figure(spec)
    open(sys.argv[2], "w", encoding="utf-8").write(svg)
    print(f"[done] {spec.get('kind')} figure -> {sys.argv[2]}  ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
