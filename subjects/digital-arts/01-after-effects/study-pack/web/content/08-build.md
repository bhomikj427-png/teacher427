@@ brief | The brief: a 15-second title sting | practice | A title that draws, reveals, pops and exports. Every chapter's skill used once.

[[fig:storyboard|Seven layers of work over 15 seconds. Rows 1–5 are the core; 6–7 are polish.|w=100]]

**Make:** a 1920 × 1080, 30 fps, 15 s piece showing a word or your name.

**Done means:** a file `title-sting-v1.mp4` on disk. Unfinished polish is fine.

**Rule for tonight:** try each step before opening its card's hints. Stuck for 5 minutes → open the chapter card named in the step.

Save with **Ctrl+Alt+Shift+S** after every step: each step gets its own file.

@@ b1 | Step 1: comp + background | practice | New comp, then a solid with a gradient.

[[fig:sb_0|Row 1 runs the whole 15 s.|w=100]]

:::q Try it first
Make the comp, then a background that isn't flat.
:::

:::reveal Hints (chapter 1, 2, 5)
**Ctrl+N** 1920 × 1080, 30 fps, 15 s → **Ctrl+Y** solid → **Ctrl+5**, search **Gradient Ramp**, double-click → set its two colours in **F3**. Rename the layer `BG` (Enter).
:::

@@ b2 | Step 2: a line that draws on | practice | Pen line + Trim Paths, 0.5 s → 2 s, eased.

[[fig:sb_1|Row 2: 0.5 s to 2 s.|w=100]]

:::q Try it first
A horizontal line under where the title will sit, drawing itself left to right.
:::

:::reveal Hints (chapter 4: Trim Paths)
**F2**, **G**, two clicks at the same height (watch the Info panel's y value). Stroke 6 px, Fill off. **Add ▸ Trim Paths**. End **0 %** at 0.5 s, **100 %** at 2 s. Select both keyframes, **F9**.
:::

@@ b3 | Step 3: the title reveal | practice | Text animator: letters fade and rise in, 1.5 s → 3.5 s.

[[fig:sb_2|Row 3: 1.5 s to 3.5 s, overlapping the end of the line.|w=100]]

:::q Try it first
Type the word. Make its letters appear one after another.
:::

:::reveal Hints (chapter 4: text animators)
**Ctrl+T**, type, **Ctrl+Enter**. Centre: Paragraph centre, **Ctrl+Alt+Home**, **Ctrl+Home**. **Animate ▸ Opacity** → 0 %. Add ▸ Property ▸ Position → y +60. **Range Selector ▸ Start** 0 % at 1.5 s → 100 % at 3.5 s. **F9**.
:::

@@ b4 | Step 4: accents pop in | practice | Two or three shapes scale from 0 to 100 %, eased, one with a Repeater.

[[fig:sb_3|Row 4: 3 s to 4.5 s.|w=100]]

:::q Try it first
Small circles or squares near the title that pop in after it.
:::

:::reveal Hints (chapters 2–4)
**F2**, **Q** ellipse with Shift. **Ctrl+Alt+Home** to centre its anchor. **Alt+Shift+S** at 3 s with Scale 0 %; at 3.4 s Scale 100 %; **F9**. Duplicate (**Ctrl+D**), move, slide later with **[**. One with **Add ▸ Repeater** for a row of dots.
:::

@@ b5 | Step 5: one control for everything | practice | Parent all elements to a null; slow push-in over 15 s.

[[fig:sb_4|Row 5: the whole duration, very slow.|w=100]]

:::q Try it first
Make everything drift slightly closer across the whole piece, by animating one layer.
:::

:::reveal Hints (chapter 2: parenting)
**Ctrl+Alt+Shift+Y** null, name it `CTRL`. **Shift+F4**, pick-whip line, text and shapes to it (not the background). CTRL **Scale** 100 % at 0 s → 105 % at 15 s. Leave it Linear so the push stays constant.
:::

@@ b6 | Step 6: polish | practice | Glow on an adjustment layer, a gentle wiggle, motion blur.

[[fig:sb_5|Row 6: optional, across the whole piece.|w=100]]

:::reveal Hints (chapter 5)
**Ctrl+Alt+Y**, drag it to the top of the stack, add **Glow** at a low intensity. On one accent: Alt-click Position stopwatch, `wiggle(1, 8)`. Motion blur switch on the moving layers **and** the comp's Enable Motion Blur.
:::

Optional: gradient inside the title with a **track matte** (chapter 4).

@@ b7 | Step 7: the ending | practice | Fade out in the last 2 s. Then preview the whole thing.

[[fig:sb_6|Row 7: 13 s to 15 s.|w=100]]

:::reveal Hints (chapters 3, 5, 6)
Pre-compose everything except BG (**Ctrl+Shift+C**, Move all attributes) and keyframe its **Opacity** 100 % at 13 s → 0 % at 15 s. Or keyframe each layer. Preview with **Space**; if slow, **Ctrl+Shift+J** (Half).
:::

@@ b-export | Export: the file | practice | Ctrl+M, H.264, name it, Render.

[[fig:render_queue|The only step that is not optional.|w=100]]

1. **Ctrl+M**.
2. Output Module → **H.264**.
3. Output To → `title-sting-v1.mp4`.
4. **Render**. Watch the file once it finishes.

Rendered before step 6 or 7? That still counts. v2 can come tomorrow.

@@ after-tonight | After tonight | idea | The night makes the file; spaced recall makes the skill last.

[[fig:storyboard|Tomorrow: rebuild rows 2–3 from nothing.|w=80]]

| When | Do | No notes? |
|---|---|---|
| Tomorrow | rebuild steps 2–3 in a new comp | yes |
| +3 days | shortcut drill (chapter 7), then a 5-minute logo animate-in | yes |
| +7 days | a different piece: a lower third or a logo sting | yes |

One night gives a result, not retention. The returns above are what keep it.
