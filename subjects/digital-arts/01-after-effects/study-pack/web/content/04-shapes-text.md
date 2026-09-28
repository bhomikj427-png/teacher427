@@ warm-up-4 | Warm-up: guess first | practice | Three guesses about shapes and text.

:::q Guess first (write it down)
1. How would you make a line look like it is being drawn, left to right?
2. How do you make letters of a word appear one after another, without making one layer per letter?
3. You draw a rectangle while your video layer is selected. What do you get?
:::

@@ shape-layers | Inside a shape layer | idea | A shape = a path, plus a stroke along it and a fill inside it, in a group.

[[fig:shape_anatomy|Twirl open a shape layer (Contents) to see this. Stroke and Fill act on the paths above them in the same group.|w=100]]

- Draw with **Q** (Rectangle → Rounded → Ellipse → Polygon → Star) or the **Pen (G)**, with **nothing selected** → new shape layer.
- While dragging: **Shift** = square/circle · **Space** = reposition · **↑ / ↓** = more / fewer star points.
- **Ctrl+G** groups shapes; each group has its own Transform.
- Shape-tool paths keep live **Size** and **Roundness** you can animate.

@@ trim-paths | Trim Paths: lines that draw themselves | method | Add ▸ Trim Paths, then keyframe End from 0 % to 100 %.

[[fig:trim_paths|Step through: End 35 %, 70 %, 100 %.|w=100|steps=3]]

:::q Try it
Pen (**G**), click-click-click an open zig-zag (nothing selected). In the Timeline: **Add ▸ Trim Paths**. Guess which property draws the line on, then keyframe it.
:::

1. Twirl open **Trim Paths 1**.
2. CTI 0 s: **End 0 %**, stopwatch on. CTI 1 s: **End 100 %**.
3. Select both keyframes, **F9**.

Turn off Fill if the open path shows a filled wedge. **Offset** slides the drawn part along the path.

:::reveal Quick check: warm-up question 1
A stroked path with **Trim Paths**, End keyframed 0 → 100 %.
:::

@@ repeater | Repeater: many from one | method | One shape, N copies, each shifted, rotated or scaled a bit more.

[[fig:shape_anatomy|Repeater is another item in the Add menu, placed below the path it copies.|w=70]]

- **Add ▸ Repeater** copies every path, stroke and fill **above it**. **Copies** = how many. Its **Transform** group = what is added per copy, applied n times to copy n.
- Row: Copies 5, Transform Position x 60 → shapes at 0, 60, 120, 180, 240.
- Ring: small circle whose group Transform Position is (0, −150), i.e. away from the layer's centre. Select the **layer**, Add ▸ Repeater, Copies 12, Position 0, **Rotation 30°**.
- Animate **Offset** to make the copies travel.

:::reveal Quick check: 8 petals around a centre, which Repeater rotation?
**360 / 8 = 45°** per copy.
:::

@@ mask-or-shape | Trap: mask or shape? | trap | Same tool, different result. It depends on what is selected.

[[fig:mask_or_shape|The shape tools and the Pen draw a mask on a selected non-shape layer.|w=100]]

:::trap The fix
Press **F2** (deselect all) before drawing a new shape.
:::

:::reveal Quick check: warm-up question 3
A **mask** on the video layer: the video is cut to the rectangle.
:::

Masks are useful too: **M** shows Mask Path, **F** feather, **Ctrl+Shift+I** inverts, and Mask Path can be keyframed for reveals.

@@ text-layers | Text layers | method | Ctrl+T, click, type. Format in Character (Ctrl+6) and Paragraph (Ctrl+7).

[[fig:layer_stack|Text is its own layer, vector like shapes: sharp at any scale.|w=70]]

- **Ctrl+T**, click in the frame (point text), type, then **Ctrl+Enter** (or Enter on the numpad) to finish.
- Font, size, tracking, colour: **Character** panel (**Ctrl+6**).
- Centre it: Paragraph (**Ctrl+7**) centre-align, then **Ctrl+Alt+Home** for the anchor, then **Ctrl+Home** to centre the layer in view.

:::reveal Quick check: fastest way to try a text animation?
Effects & Presets (**Ctrl+5**) → search **Animation Presets > Text** → drag one onto the layer. Then **UU** to see what it changed.
:::

@@ text-animators | Text animators: one letter at a time | method | Set the "away" value once; keyframe the range selector sweep.

[[fig:text_animator|Opacity 0 % applies inside the selection. Moving Start from 0 % to 100 % releases the letters in order.|w=100|steps=3]]

1. Text layer → Timeline **Animate ▸ Opacity**.
2. Set the animator's **Opacity 0 %** (the whole word vanishes).
3. **Range Selector 1 ▸ Start**: 0 % at 0 s → **100 %** at 1 s. F9.
4. From the animator's **Add** menu choose **Property ▸ Position**, set y **+60**: letters rise in as they appear (same selector).

Only the selector is keyframed. The animator values stay fixed.

:::reveal Quick check: warm-up question 2
One text layer, **an animator** (Opacity 0 %) and a **Range Selector** whose Start is keyframed 0 → 100 %.
:::

@@ track-matte | Track matte: video inside text | method | One layer's alpha (or brightness) decides where another layer shows.

[[fig:track_matte|Alpha matte: the text's shape, the gradient's colour.|w=100]]

1. Text layer (the **matte**) + a gradient or video (the **fill**) in the comp.
2. **F4** until the Modes columns show **Track Matte**.
3. On the **fill** layer, pick-whip or choose the text layer; mode **Alpha**.

The matte layer is hidden automatically. **Luma** uses brightness instead of alpha. Since version 23.0 the matte can be any layer; older tutorials show the old "matte directly above" rule.

:::reveal Quick check: which layer gets the Track Matte setting?
The **fill** layer (the one being cut), pointing at the matte.
:::

@@ self-test-4 | Self-test: chapter 4 | practice | In the software, no notes.

1. A horizontal line that draws on over 1 s with a soft stop.
2. A ring of 10 dots.
3. The word `HELLO` whose letters fade and rise in, one by one.
4. A gradient visible only inside `HELLO`.

:::reveal Answers
1. Pen with nothing selected, 2 clicks; Add ▸ Trim Paths; End 0 → 100 %; F9. 2. Ellipse, its group Transform Position (0, −150); select the layer, Add ▸ Repeater, Copies 10, Position 0, Rotation 36°. 3. Animate ▸ Opacity 0 %, add Position y +60, Start 0 → 100 %. 4. Solid + Gradient Ramp under the text; Track Matte on the solid → the text, Alpha.
:::
