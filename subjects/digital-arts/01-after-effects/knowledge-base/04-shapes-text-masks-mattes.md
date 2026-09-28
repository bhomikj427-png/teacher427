# 04 — Shapes, text, masks, mattes

> Stage 1. Truth = [UG], plus [AE23] for track mattes. `settled` unless marked.

## Paths (shared by shapes, masks, motion paths) [UG p.405–406]
- A path = **vertices** joined by **segments**; each vertex has direction handles. **Corner points**
  break direction; **smooth points** keep one tangent line.
- A path has no look of its own. A **stroke** draws along it; a **fill** paints inside it.
- Open path (a line) vs closed path (a circle).

## Shape layers [UG p.406–409, 413–414, 434–441]
- Draw with a shape tool (**Q** cycles Rectangle, Rounded Rectangle, Ellipse, Polygon, Star) or the **Pen
  (G)** in the Composition panel **with no layer selected** → a new shape layer. With a shape layer
  selected, drawing adds a shape to *that* layer. With any other layer selected, drawing makes a **mask**
  on it (trap T6).
- Default shape = **Path + Stroke + Fill** inside a **Group**, and each group has its own Transform.
  While dragging a shape: **Shift** constrains (square, circle), **Space** repositions, **↑/↓** changes
  star/polygon points or corner roundness. [UG p.29]
- **Parametric** paths (from shape tools) keep numeric Size / Roundness properties you can animate.
  **Bezier** paths (from the Pen) are edited vertex by vertex.
- **Order inside a layer matters:** a Fill or Stroke applies to all paths **above** it in the same group;
  path operations act on paths above them.
- **Add** menu (Timeline or Tools) adds attributes. The beginner set:
  - **Trim Paths** — animate **Start / End** (0–100 %) to draw a line on or off; **Offset** slides it.
  - **Repeater** — copies the shape N times, each with an extra transform (offset, rotation, scale).
  - **Round Corners**, **Offset Paths**, **Wiggle Paths**, **Merge Paths**.
- Group / ungroup shapes: **Ctrl+G / Ctrl+Shift+G**.

## Text [UG p.445–449, 470–476]
- **Ctrl+T** Type tool (cycles horizontal/vertical); click for point text, drag for paragraph text.
  **Ctrl+Alt+Shift+T** makes an empty text layer. Format in Character (Ctrl+6) and Paragraph (Ctrl+7).
- Four ways to animate text: (1) the layer's Transform, (2) **text animation presets** (Effects & Presets
  > Animation Presets > Text), (3) Source Text (the characters themselves change, Hold keyframes),
  (4) **animators + selectors**.
- **Animators** (Timeline: **Animate ▸** menu on the text layer):
  1. Add an animator property (e.g. Opacity, Position, Scale, Blur).
  2. Set that property to the **"away" value** (e.g. Opacity 0 %, Position y +100).
  3. Keyframe the **Range Selector's Start or End** (or Offset) from 0 → 100 %.
  The selector sweeps across the characters, so letters change one after another. Usually only the
  selector is keyframed; the animator property holds a single value. [UG p.470–471]
- Units can be switched from % to character **Index** in Range Selector > Advanced.
- Presets are a fast way to learn animators: apply one, then press **UU** to see exactly what it changed.
  Text presets were built at 720 × 480, so offscreen values may need adjusting in a 1080p comp. [UG p.470]

## Masks [UG p.27, 443]
- A mask = a path on a layer that cuts its visibility. Draw with a shape tool or Pen **with the layer
  selected**. **Ctrl+Shift+N** new mask. **M** shows Mask Path; **MM** all mask properties; **F** Mask
  Feather. Mask modes: Add, Subtract, Intersect, Difference, None. **Ctrl+Shift+I** inverts.
- Mask Path, Feather, Opacity and Expansion are all keyframeable → animated reveals.

## Track mattes [UG p.499–501; AE23]
- A track matte lets one layer (the **fill**) show only through the shapes of another (the **matte**).
- Two kinds: **Alpha** (opaque parts of the matte show the fill) and **Luma** (bright parts show the
  fill); each has an Inverted version.
- **[version: 23.0+]** Any layer can be chosen as the matte, via the **Track Matte** column's pick whip or
  menu (Modes column, **F4**). The matte layer's video is switched off automatically. Before 23.0 the
  matte had to be the layer directly above the fill. (The 2019-era guide still describes the old rule;
  see `CHANGELOG.md` entry 1.)
- Classic use: text layer as the matte, a video or gradient as the fill → footage inside letters. A
  moving matte is a **traveling matte**.

→ Stage 2: `stage-2/01-render-pipeline.md` (vector vs raster, continuous rasterization, matte order).
