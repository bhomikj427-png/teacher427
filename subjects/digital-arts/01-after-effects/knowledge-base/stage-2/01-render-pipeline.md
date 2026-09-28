# Stage 2 · 01 — The render pipeline (why things happen)

> Depth for units 01, 02, 04, 05, 06. Truth = [UG]. Every claim here is either quoted mechanism from the
> guide or *derived* from it (marked). Stage-1 files stay the quick set; this file explains them.

## 1. The full order a frame is built in [UG p.100–101]
1. Nested compositions render **first** (a precomp is computed completely before its container uses it).
2. Layers render **bottom to top**. Each finished layer is the input for the one above (that is how a
   blending mode or an adjustment layer "sees" what is below).
3. Inside one raster layer: **masks → effects (top to bottom in Effect Controls) → transform → layer
   styles**. Continuously rasterized vector layers: masks → transform → effects.
4. What the Layer panel shows = the layer **before** transforms.

**Derived consequences** (each explains a Stage-1 rule):
- An effect that looks like it has a direction (Drop Shadow, Linear Wipe, Motion Tile) turns when the layer
  rotates, because rotation happens after it (trap T9).
- An adjustment layer is **cheaper** than the same effect on N layers: it runs once on the composite
  instead of N times. Adobe says this directly. [UG p.180]
- Some effects ignore masks on their own layer; the fix is to precompose the masked layer and put the
  effect on the precomp, which forces "mask first, effect second" in two separate stages. [UG p.101]
- The **Transform effect** is a way to transform *before* later effects: reorder it inside the effect stack
  when you need rotation to happen before the shadow. [UG p.101]

## 2. Precomposing changes the order (the real reason to precompose)
- A precomp is a layer whose "footage" is another comp's finished result. Anything applied to the
  precomp layer (mask, effect, matte, transform) acts on **the whole group at once, after** everything
  inside is done. That is why one track matte or one glow can cover many layers only after precomposing.
- **Collapse Transformations** (switch on a precomp layer): the nested comp's transforms are *not* baked
  in first; they are combined with the container's transforms. Result: vector content (text, shapes) stays
  sharp when scaled up in the container, and the nested layers can sit in the container's 3D space. Cost:
  the precomp behaves less like a flat picture (masks/effects on it interact differently). [UG p.101]
- Nested comp **background colour** is dropped (transparent) because the container needs the precomp
  as an image with alpha, not a filled rectangle. [UG p.91] (*why* = derived.)
- **Preserve frame rate when nested** lets a precomp keep a choppy look (e.g. 12 fps) inside a 30 fps
  container. [UG p.91]

## 3. Two coordinate spaces (why anchor point matters) [UG p.183]
- **Layer space:** origin at the layer's own top-left; anchor point, mask vertices and effect points
  live here.
- **Composition space:** origin at the comp's top-left; Position lives here.
- Position = "put the layer's anchor point at this comp coordinate". Scale and rotation are applied
  around the anchor point, in that order of reasoning: the anchor is the fixed point of both. Moving the
  anchor with Pan Behind changes both Anchor Point and Position so the layer does not jump.
- **Parenting** composes the child's transform with the parent's (child's Position is expressed in the
  parent's space). Opacity is not a spatial transform, so it is not composed (trap T14). *(Why opacity is
  excluded = derived from the list in UG p.205.)*

## 4. Vector vs raster, and sharpness [UG p.405, 193, 197]
- Text and shape layers are vector: they are re-drawn at the needed size, so they stay sharp when scaled.
- Imported vector files (Illustrator, PDF, EPS) are rasterized once at import size; only **Continuously
  Rasterize** makes them re-rasterize per frame.
- Values are fractional, so layers can sit between pixels (subpixel positioning). Odd-sized layers have a
  half-pixel anchor point and can look soft when still; set whole-number positions for static crisp
  graphics. [UG p.197]

## 5. Two stages of export [UG p.541–543]
- **Render settings** answer "which frames, at what quality/resolution/time span" → pixels.
- **Output module** answers "how are those pixels encoded into a file" (format, codec, channels, audio).
- Because they are separate, one render can feed several output modules (mp4 + PNG sequence) without
  recomputing. The Render Queue uses an embedded Media Encoder for encoding; the standalone AME adds
  presets and background rendering. [UG p.541]

## 6. Colour depth [UG p.360]
- Project bit depth: **8, 16 or 32 bpc**. 8-bpc channels hold 0–255; 16-bpc 0–32 768; 32-bpc is
  floating point and can hold values below 0 and above 1 (over-bright light), which some glows and blurs
  use for more natural results. Higher depth = smoother gradients, fewer banding steps, slower renders.
  Click the bpc label at the bottom of the Project panel to change it (Alt-click cycles). [UG p.13]
- For tonight's piece 8 bpc is enough; if a gradient bands, try 16 bpc.
