@@ sc-files | Files and undo | method | New comp, settings, import, save, undo, render.

[[fig:kb_files|Blue = the letters; grey = modifiers held with them.|w=100]]

| Key | Does |
|---|---|
| Ctrl+N | new composition |
| Ctrl+K | composition settings |
| Ctrl+I | import a file |
| Ctrl+S | save project |
| Ctrl+Alt+Shift+S | increment and save |
| Ctrl+Z / Ctrl+Shift+Z | undo / redo |
| Ctrl+M | add comp to Render Queue |

:::reveal Quick check: cover the table. Which key opens the settings of the comp you are in?
**Ctrl+K**.
:::

@@ sc-tools | Tools | method | Single letters. Tap to switch; hold to borrow the tool and return.

[[fig:kb_tools|Green = tool keys. Holding Space borrows the Hand tool.|w=100]]

| Key | Does |
|---|---|
| V | Selection tool |
| H | Hand tool (Space = hold for Hand) |
| W | Rotation tool |
| Y | Pan Behind: move the anchor point |
| Q | shape tools (press again to cycle) |
| G | Pen tool |
| Ctrl+T | Type tool |

Holding a tool key switches only while held; a quick tap switches for good. Adobe documents this for the single-letter tools.

:::reveal Quick check: you are drawing with the Pen and need to move a point. Which key, held?
**Ctrl** (temporary Selection tool while a pen tool is active).
:::

@@ sc-props | Show one property | method | A P S R T for the transforms; U for animated; E effects; M masks.

[[fig:kb_props|Orange = property keys. Double letters: press twice quickly.|w=100]]

| Key | Does |
|---|---|
| A | show only Anchor Point |
| P | show only Position |
| S | show only Scale |
| R | show only Rotation |
| T | show only Opacity |
| U / UU | show keyframed / all modified properties |
| E / EE | show effects / expressions |
| M / MM | mask path / all mask properties |
| F | mask feather |

**Shift + key** adds to what is shown instead of replacing it.

:::reveal Quick check: Position and Opacity together?
**P**, then **Shift+T**.
:::

@@ sc-time | Moving through time | method | J/K jump keyframes, B/N set the work area, Page Down steps a frame.

[[fig:kb_time|Violet = time keys.|w=100]]

| Key | Does |
|---|---|
| J / K | previous / next keyframe or marker |
| B / N | work-area start / end at the current time |
| Home / End | start / end of the comp |
| Page Down / Page Up | one frame forward / back (Shift: 10) |
| I / O | layer In / Out point |
| Alt+Shift+J | go to a typed time |
| D | scroll the Timeline to the current time |
| = / - | zoom time in / out |
| ; | zoom to single frames |

:::trap Arrow keys
Arrows **nudge the selected layer** 1 px. They do not step time. Some cheat sheets get this wrong.
:::

@@ sc-keys | Keyframes | method | Alt+Shift+letter sets a keyframe; F9 eases; Shift+F3 opens the graphs.

[[fig:kb_keys|Red = keyframe keys, used with Alt+Shift or Ctrl.|w=100]]

| Key | Does |
|---|---|
| Alt+Shift+P | add or remove a Position keyframe at the current time |
| Alt+Shift+S | same for Scale |
| Alt+Shift+R | same for Rotation |
| Alt+Shift+T | same for Opacity |
| F9 | Easy Ease the selected keyframes |
| Shift+F9 / Ctrl+Shift+F9 | Easy Ease in / out |
| Shift+F3 | Graph Editor on/off |
| Ctrl+Alt+H | toggle Hold / Auto Bezier |
| Alt+→ / Alt+← | move selected keyframes 1 frame later / earlier |

:::reveal Quick check: cover the table. Keyframe Scale without touching the mouse?
**Alt+Shift+S**.
:::

@@ sc-layers | Layers | method | New solid/null/adjustment, split, trim, lock, switches.

[[fig:kb_layers|Blue = layer commands, violet = time-based ones.|w=100]]

| Key | Does |
|---|---|
| Ctrl+Y | new solid |
| Ctrl+Alt+Y | new adjustment layer |
| Ctrl+Alt+Shift+Y | new null object |
| Ctrl+D | duplicate |
| Ctrl+Shift+D | split layer at the current time |
| Alt+[ / Alt+] | trim In / Out point to the current time |
| [ / ] | move layer so its In / Out point is at the current time |
| Ctrl+Shift+C | pre-compose |
| Ctrl+L / Ctrl+Shift+L | lock layer / unlock all |
| Ctrl+Alt+Down / Up | move layer down / up the stack |
| F4 | show Switches / Modes columns |
| Shift+F4 | show Parent column |

@@ sc-views | Views and panels | method | Zoom the viewer, fit it, half resolution, maximize a panel.

[[fig:kb_views|Red = view keys.|w=100]]

| Key | Does |
|---|---|
| . / , | zoom viewer in / out |
| / | viewer to 100 % |
| Shift+/ | zoom viewer to fit |
| Ctrl+J / Ctrl+Shift+J | resolution Full / Half |
| ` | maximize / restore the panel under the pointer |
| \ | switch focus Composition ↔ Timeline |
| ' | safe zones |
| Ctrl+R | rulers |
| Shift+F5 / F5 | take / show snapshot |

@@ sc-export | Panels and export | method | Ctrl+number opens panels; Ctrl+M and Ctrl+Alt+M send to render.

[[fig:kb_export|Blue = panel and export keys.|w=100]]

| Key | Does |
|---|---|
| Ctrl+0 | Project panel |
| Ctrl+Alt+0 | Render Queue panel |
| Ctrl+3 | Preview panel |
| Ctrl+5 | Effects & Presets panel |
| F3 | Effect Controls |
| Ctrl+M | add comp to Render Queue |
| Ctrl+Alt+M | send comp to Adobe Media Encoder |
| Ctrl+Alt+S | add current frame to Render Queue |

Your install's live list: **Edit > Keyboard Shortcuts** (Ctrl+Alt+').

@@ sc-drill | Drill: keys from memory | practice | Say the key before you reveal it. Then do it in the software.

1. Show only Rotation.
2. Keyframe Opacity at the current time.
3. Next keyframe.
4. Ease the selected keyframes.
5. Split the layer here.
6. Trim the layer's end to here.
7. New null.
8. Set the work area to start here.
9. Pre-compose.
10. Add to Render Queue.

:::reveal Answers
1 **R** · 2 **Alt+Shift+T** · 3 **K** · 4 **F9** · 5 **Ctrl+Shift+D** · 6 **Alt+]** · 7 **Ctrl+Alt+Shift+Y** · 8 **B** · 9 **Ctrl+Shift+C** · 10 **Ctrl+M**
:::

Missed ones go on tomorrow's list. Recall tomorrow beats rereading tonight.
