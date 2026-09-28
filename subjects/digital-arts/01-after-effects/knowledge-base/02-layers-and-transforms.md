# 02 — Layers & transforms

> Stage 1. Truth = [UG]. `settled` unless marked.

## Layer types [UG p.177–181, 20]
| Type | Made with | Source | Typical use |
|---|---|---|---|
| Footage (video, image, audio) | import, drag in | a footage item | the material |
| **Solid** | Layer > New > Solid (**Ctrl+Y**) | a solid-colour footage item (kept in the Solids folder) | backgrounds, matte sources |
| **Text** | Type tool (**Ctrl+T**) or Ctrl+Alt+Shift+T | none (synthetic, vector) | titles |
| **Shape** | shape tools (**Q**) or Pen (**G**), drawn with no layer selected | none (synthetic, vector) | graphics, lines, icons |
| **Null object** | **Ctrl+Alt+Shift+Y** | none; invisible in render | a controller to parent other layers to |
| **Adjustment** | **Ctrl+Alt+Y** | none | its effects apply to the composite of **all layers below it** |
| Camera, light | Ctrl+Alt+Shift+C / L | — | 3D (out of scope tonight) |
| Precomp | precompose or drag a comp in | a composition | nesting (unit 05) |

- Layers are numbered by stacking position; the number changes when you reorder. **Numpad digits** select
  a layer by number. [UG p.177, 20]
- An adjustment layer at the bottom of the stack has no visible result (nothing below it). [UG p.180]

## The five transform properties (and their keys)
Twirl a layer open, or press the key with the layer selected. [UG p.22–24]

| Key | Property | Measured in |
|---|---|---|
| **A** | Anchor Point | **layer** space — the pivot |
| **P** | Position | **composition** space — where the anchor point sits in the frame |
| **S** | Scale | % around the anchor point |
| **R** | Rotation (and Orientation in 3D) | degrees around the anchor point |
| **T** | Opacity | % |

- **Shift + key** adds a property to what is shown (P, then Shift+S shows both). **U** shows only
  properties with keyframes; **UU** shows every property changed from default. [UG p.22]
- Position is where the anchor point is; the anchor point is the pivot inside the layer. [UG p.183]
- **Pan Behind tool (Y)** moves the anchor point without moving the layer on screen. **Ctrl+Alt+Home**
  centres the anchor point in the layer's visible content. [UG p.15, 23]
- Drag a value to scrub it; **Shift-drag** = 10× steps; **Ctrl-drag** = 1/10 steps. [UG p.18]
- Double-click the Selection tool resets Scale to 100 %; double-click the Rotation tool resets Rotation.

## Parenting [UG p.205–207]
- Pick-whip the child's **Parent** column onto the parent (or pick from its menu). **Shift+F4**
  shows/hides the Parent column.
- The child's Position, Scale, Rotation (and 3D Orientation) become **relative to the parent**. **Opacity
  is not inherited.**
- One parent per layer; a parent can have many children. Parenting cannot be animated on/off.
- **Nulls** exist for this: parent many layers to one invisible null, animate the null, and everything
  moves together.

## Switches [UG p.193]
| Switch | Does |
|---|---|
| Video (eye) | show or hide the layer |
| **Solo** | only soloed layers preview and render (use to isolate) |
| **Lock** | no edits possible (Ctrl+L; unlock all Ctrl+Shift+L) |
| **Shy** | hides the layer *in the Timeline* when the comp's Hide Shy Layers switch is on; still renders |
| Collapse / Continuously Rasterize | for precomps: collapse; for vector layers: re-rasterize every frame so scaling above 100 % stays sharp |
| Quality | Best / Draft |
| fx | render the layer's effects or not |
| **Motion Blur** | per layer; needs the comp's Enable Motion Blur switch as well |
| 3D | make the layer 3D |
**F4** toggles the Switches / Modes columns (Modes holds blending mode and track matte).

## Arranging in time [UG p.16–21]
- **[ / ]** move the layer so its In / Out point is at the CTI.
- **Alt+[ / Alt+]** trim the In / Out point to the CTI.
- **Ctrl+Shift+D** splits the layer at the CTI into two layers.
- **Ctrl+D** duplicates. **Ctrl+Alt+Down/Up** moves a layer down/up the stack.
- **I / O** jump the CTI to the layer's In / Out point.

## Blending modes [UG p.21, 208]
- Set per layer in the Modes column; **Shift+- / Shift+=** cycles through them. Screen and Add brighten
  (good for glows over dark), Multiply darkens. Beginners need Normal, Add, Screen, Multiply, Overlay.

→ Stage 2: `stage-2/01-render-pipeline.md` (layer space vs comp space; why parenting skips opacity).
