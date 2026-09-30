# Site v2 · session 2 prototypes (throwaway)

Judged by look, then rebuilt properly in session 3. Nothing here touches `site/build.py` or `site/static/`.

- **`compare.html`**: start here. Every variant side by side (desktop + phone screenshots), pros/cons, live links, and
  the decisions to make.
- **`proto.html`**: the live prototype. Routes: `#/` L0 · `#/ch/<ch>` L1 · `#/c/<ch>/<id>` L2 focus · `…/web` L3.
  Query: `l0=river|lanes|strata`, `l1=strict|ports|connected`, `growth=0`, `p=<concepts done>`, `chrome=0`,
  `theme=dark`, `selftest=1`. The prototype controls sit bottom-left.
- **`de_graph.py`**: Digital Electronics as a v2 graph: 117 concepts, 188 flow edges (each with a bridge,
  30 with a predict-first question), 18 relates-to links. Hand-extracted from the KB; this is the stand-in for the
  automatic graph-extraction step.
- **`autocut.py`**: automatic chaptering (SITE-V2-DRAFT §6). Validate → topic-coherent topological order →
  DP split (≤ 9 per chapter, min crossing edges + topic-mix penalty) → single-move refinement → auto names/stages.
- **`build_proto.py`**: graph → cut → `out/data.js` (renders the v1 K-map cards through `site/build.py` for focus).
- **`shoot.sh`** + **`phone.html`**: screenshots (Chrome headless; phone = 390px iframe, because headless won't go
  below ~500px wide).

Rebuild: `python site/v2-design/prototypes/build_proto.py`. Self-test: open `proto.html?selftest=1`, then read the
page title (last run: PASS, 576 renders, 0 errors).
