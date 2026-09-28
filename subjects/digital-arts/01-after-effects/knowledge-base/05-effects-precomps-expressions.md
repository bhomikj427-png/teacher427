# 05 — Effects, precomps, expressions

> Stage 1. Truth = [UG]. `settled` unless marked.

## Effects [UG p.20, 180]
- **Effects & Presets panel (Ctrl+5):** type in its search box, then **double-click** an effect (applies to
  the selected layers) or drag it onto a layer.
- Settings live in **Effect Controls (F3)** and in the layer's **Effects** group in the Timeline (**E**).
  Effect properties have stopwatches and animate like any other.
- **Ctrl+Shift+E** removes all effects from the selected layers; **Ctrl+Alt+Shift+E** re-applies the last
  effect used.
- Stacked effects run **top to bottom** in Effect Controls; reordering them changes the result.
- **Adjustment layer:** its effects apply to the composite of every layer below it → one colour grade or
  blur for a whole scene, cheaper than applying it per layer. A mask on the adjustment layer limits the
  effect to an area. [UG p.180]
- Beginner-useful effects: **Fill** (recolour), **Gradient Ramp**, **Drop Shadow**, **Glow**, **Gaussian
  Blur**, **Fractal Noise** (textures), **Turbulent Displace**, **Venetian Blinds / Linear Wipe** (wipes),
  **CC Particle World** (particles, in the bundled Cycore set). `likely` for exact availability [version].

## Precomposing & nesting (threshold T4) [UG p.96–100; options p.97]
- **Ctrl+Shift+C** = Layer > Pre-compose: selected layers move into a new composition, which replaces
  them as a single layer.
- Two options:
  - **Leave all attributes in "comp"** — only for a single layer (not text or shape). The layer's
    keyframes, effects and masks stay *outside* on the precomp layer; the new comp matches the layer's size.
  - **Move all attributes into the new composition** — everything goes inside; the new comp matches the
    original comp's size. The normal choice for a group of layers.
- Why precompose: group layers so one effect/matte/transform applies to all; tidy a long timeline; reuse
  a piece (a logo animation) in several places; change the render order (unit stage-2).
- Double-click a precomp layer to open it; **Tab** opens the mini-flowchart to jump up and down the nest.

## Render order (threshold T3) [UG p.100]
- The comp is built **bottom layer first**.
- Inside each raster layer: **masks → effects → transform → layer styles**. (Continuously rasterized
  vector layers: masks → transform → effects.)
- Consequences: a Drop Shadow on a layer is computed *before* the layer rotates, so the shadow **rotates
  with it** (the light source seems to spin). Put the shadow on an adjustment layer above, or precompose
  the layer first, to keep the shadow direction fixed.

## Expressions (starter kit) [UG p.580, 597, 614–616]
- An expression = a short JavaScript-based line that computes a property's value every frame.
  **Alt-click the stopwatch** (or Alt+Shift+=) to add one; type it; click outside to apply. **EE** shows
  every expression in the comp.
- The three worth knowing tonight:

| Expression | Put it on | Does |
|---|---|---|
| `wiggle(2, 30)` | Position (or Rotation, Scale) | random drift: about 2 wiggles per second, average size about 30 units (px, °, %) around the keyframed value |
| `time * 90` | Rotation | 90° per second forever (`time` = comp time in seconds) |
| `loopOut("cycle")` | any keyframed property | after the last keyframe, repeats the keyframed section until the layer ends |

- `wiggle(freq, amp, octaves=1, amp_mult=.5, t=time)` — freq in wiggles/s, amp in the property's units.
- `loopOut(type="cycle", numKeyframes=0)` — loops from the last keyframe back; other types include
  "pingpong". [UG p.616]
- **Pick whip** in the expression field links one property to another (e.g. a shape's rotation to a
  slider) — the base of all rigging.

→ Stage 2: `stage-2/01-render-pipeline.md` (precompose vs collapse transformations; why adjustment layers
are cheaper).
