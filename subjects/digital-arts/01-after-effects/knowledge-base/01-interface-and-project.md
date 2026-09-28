# 01 — Interface & project

> Stage 1. Truth = [UG] (`sources.md`). `settled` unless marked.

## The containers (big idea 1)
- **Project** = one `.aep` file. It stores compositions and **references** (links) to source files; it
  does not copy your footage into itself. Only one project is open at a time. [UG p.78–79]
  - Consequence: move or rename a source file and the project shows it as missing. **File > Dependencies >
    Collect Files** copies the project plus all footage into one folder, for moving or archiving. [UG p.549]
- **Composition (comp)** = "the framework for a movie": a frame (width × height), a frame rate, a duration,
  and its own timeline of layers. Similar to a sequence in Premiere Pro. [UG p.86]
- **Footage item** = an imported file listed in the Project panel. A **layer** is one use of a footage item
  inside a comp; editing the layer never changes the source. One footage item can feed many layers. [UG p.177]

## The default panels (what each is for)
| Panel | Job | Open/close |
|---|---|---|
| **Project** | the bin: every imported file and every comp | Ctrl+0 |
| **Composition** | the viewer: shows the current frame; you drag and draw here | double-click a comp |
| **Timeline** | layers (left: names, switches, properties) and time (right: layer bars, keyframes, the current-time indicator) | opens with the comp |
| **Tools** | selection, hand, zoom, rotation, camera, pan-behind, shape, pen, type, brush, puppet | Ctrl+1 |
| **Preview** | play settings per preview key | Ctrl+3 |
| **Effects & Presets** | search and apply effects and animation presets | Ctrl+5 |
| **Effect Controls** | the settings of effects on the selected layer | F3 |
| **Info** | pixel colour and coordinates under the pointer, keyframe info | Ctrl+2 |
| **Character / Paragraph** | type formatting | Ctrl+6 / Ctrl+7 |
| **Render Queue** | export | Ctrl+Alt+0 |
[UG p.14 shortcuts; p.41–52 panels]

- **Properties panel [version: 2024+]:** a central place to adjust layer transform properties without
  opening the Timeline outline (June 2024 feature summary). Useful, but the Timeline route below works in
  every version. `likely` (Q2 in the map).
- **Timeline anatomy:** current time display (top-left) · current-time indicator (CTI, the vertical line)
  · time ruler · work area bar (the range that previews and can render) · layer bars · keyframes.
  **Bottom layer renders first** and appears furthest back. [UG p.89]
- **\\** (backslash) toggles focus between the Composition and Timeline panels. **`** (accent grave) maximizes
  the panel under the pointer; press again to restore. [UG p.14–15]

## Workspaces
- A workspace is a saved arrangement of panels. Choose one from the workspace bar (right of the Tools
  panel) or Window > Workspace. **Window > Workspace > Reset "name" to Saved Layout** restores a layout you
  have wrecked — the standard fix when a panel disappears. [UG p.45–46]
- Panels dock (edge drop zones) or group (centre drop zones); drag by the tab's gripper. A closed panel
  comes back from the **Window** menu. [UG p.47–48]

## Making a composition
- **Composition > New Composition (Ctrl+N)**; change later with **Ctrl+K**. Settings: preset, width,
  height, pixel aspect ratio, frame rate, resolution, start timecode, duration, background colour. [UG p.88–91]
- Set frame size and aspect with the final output in mind: some calculations depend on them, so late
  changes can alter results. [UG p.88]
- A comp made by dragging footage onto the **Create a new Composition** button inherits that footage's size
  and frame rate. [UG p.88]
- Limits: 3 h duration, 30 000 × 30 000 px. [UG p.90]
- Background colour is not rendered when the comp is nested; it becomes transparent. For a real
  background, add a solid. [UG p.91]
- Tonight's default: **1920 × 1080, square pixels, 30 fps, 10–15 s** (the "Social Media Landscape HD" /
  HD 1080 presets give this; exact preset names vary by version) `[version]`.

## Import and save
- Import: **Ctrl+I** (one file / sequence), **Ctrl+Alt+I** (several), or drag files into the Project panel.
  **Ctrl+/** adds the selected item to the most recently active comp. [UG p.19]
- Save **Ctrl+S**; **Increment and Save Ctrl+Alt+Shift+S** saves a numbered copy next to the original
  (cheap version history). [UG p.81]
- Only the `.aep` is primary; `.aepx` is an XML copy for automation; `.aet` is a template. [UG p.78]

→ Stage 2: `stage-2/01-render-pipeline.md` (why nested background colour vanishes; comp vs layer space).
