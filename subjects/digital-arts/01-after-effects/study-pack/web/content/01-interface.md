@@ warm-up | Warm-up: guess before you open anything | practice | Four guesses. Wrong ones are useful; they mark what to watch for.

:::q Guess first (write it down)
1. After Effects saves a project as one file. Does that file contain your video clips?
2. What is the difference between a *composition* and a *layer*?
3. You set the composition's background colour to blue. Will the exported video be blue behind everything?
4. Which panel do you think you will spend most time in?
:::

Each one is answered on a card in this chapter. Keep your guesses and compare.

@@ panels | The window: seven panels | idea | Project holds files, Composition shows the frame, Timeline holds time. The rest are helpers.

[[fig:ui_layout|The Default workspace in outline. Positions change with workspace and version; the **jobs** do not.|w=100]]

| # | Panel | Job |
|---|---|---|
| 1 | **Project** | every imported file and every composition |
| 2 | **Composition** | the current frame; drag and draw here |
| 3–6 | Info · Preview · Effects & Presets · Properties | helpers (colour/x-y, play settings, effect search, quick transforms) |
| 7 | **Timeline** | layers on the left, time on the right |

**`** (under Esc) maximizes the panel under the mouse. Press again to restore.

:::reveal Quick check: where does an imported video appear first?
In the **Project** panel. It only appears in the frame once you drag it into a composition (then it is a layer).
:::

@@ workspaces | Workspaces: saved layouts | idea | A lost panel is one menu away. Reset beats hunting.

[[fig:ui_layout|Same panels, rearranged. A workspace is just a saved arrangement.|w=60]]

- Switch layouts in the **workspace bar** at the right of the Tools row, or Window > Workspace.
- Closed a panel by mistake? **Window** menu → the panel name.
- Layout wrecked? **Window > Workspace > Reset "Default" to Saved Layout.**
- Drag a panel by its tab onto another panel's **edge** to dock it beside, onto its **middle** to stack it as a tab.

:::reveal Quick check: the Timeline vanished. Two ways back?
Double-click the composition in the **Project** panel (each comp opens in its own Timeline), or **reset the workspace**.
:::

@@ containers | Project ⊃ comp ⊃ layer ⊃ property ⊃ keyframe | idea | Every "where is it?" question is answered by which box owns it.

[[fig:containers|Five nested boxes. Keyframes live inside properties, properties inside layers, layers inside compositions.|w=100]]

- The **project** (.aep) stores compositions and **links** to your files, not copies. Move a source file and it goes missing.
- A **composition** = a frame size + frame rate + duration + its own timeline. Like a sequence in Premiere.
- A **layer** is one *use* of a file. Editing it never changes the file.

:::reveal Quick check: warm-up question 1
**No.** The .aep only links to your clips. To move a project with its clips, use File > Dependencies > **Collect Files**.
:::

@@ new-comp | Make the composition first | method | Ctrl+N. For tonight: 1920 × 1080, 30 fps, 15 s.

[[fig:containers|The composition is the box everything else goes in.|w=60]]

:::q Try it: predict, then do
Press **Ctrl+N**. Before looking at the dialog, guess which three settings matter most.
:::

| Setting | Tonight | Why |
|---|---|---|
| Width × Height | **1920 × 1080** | full HD; set it now, late changes shift things |
| Frame rate | **30** | smooth, standard for screens |
| Duration | **0;00;15;00** | 15 s |
| Background | any | a viewing aid only (next card) |

**Ctrl+K** reopens these settings later.

@@ import-save | Import and save | method | Ctrl+I brings files in. Ctrl+S, and Increment and Save for free versions.

[[fig:ui_layout|Imports land in panel 1 (Project). Drag from there onto the Timeline.|w=60]]

- **Ctrl+I** import one file · **Ctrl+Alt+I** several · or drag files from Explorer into the Project panel.
- **Ctrl+/** drops the selected file into the active composition.
- **Ctrl+S** save. **Ctrl+Alt+Shift+S** = Increment and Save: a numbered copy beside the original. Use it before anything risky.

:::reveal Quick check: why use Increment and Save instead of Save As?
It keeps working in the new numbered file **and** leaves the old one untouched, in one key press. A cheap undo across sessions.
:::

@@ timeline | Reading the Timeline | idea | Left = what (layers, properties). Right = when (bars, keyframes, the red CTI line).

[[fig:timeline_anatomy|1 current time · 2 switches and layer names · 3 work area · 4 current-time indicator (CTI) · 5 keyframes.|w=100]]

- The **CTI** is "now". Every edit to a value happens at the CTI.
- The **work area** (grey bar) is the range that previews, and by default renders. Set its ends with **B** and **N**.
- **\\** jumps between the Composition and Timeline panels.
- **Layer 1 is on top.** The bottom layer is drawn first.

:::reveal Quick check: what does dragging the CTI do?
It **scrubs**: shows the frame at that time without playing. Space plays.
:::

@@ traps-1 | Traps in the first hour | trap | The background colour lies, the project links, and panels close.

:::trap Background colour
The composition's background colour is a viewing aid. Nested inside another comp it becomes **transparent**. For a real background, add a **solid** (Ctrl+Y).
:::

:::trap Moving files
The .aep links to files. Rename or move a clip and it shows as missing. Keep a project folder; use **Collect Files** to move it.
:::

:::trap A panel disappeared
Nothing is deleted. **Window** menu or **reset the workspace**.
:::

@@ self-test-1 | Self-test: chapter 1 | practice | Do it in the software, no notes. Then reveal.

1. Make a 1920 × 1080, 30 fps, 12 s composition named `test`.
2. Import any image and put it in the comp.
3. Maximize the Timeline, then restore it.
4. Set the work area to 2 s – 6 s.
5. Save a numbered copy.

:::reveal Answers
1. Ctrl+N, set values, name it. 2. Ctrl+I, then drag into the Timeline (or Ctrl+/). 3. Mouse over it, **`**, again **`**. 4. CTI to 2 s, **B**; CTI to 6 s, **N**. 5. **Ctrl+Alt+Shift+S**.
:::
