@@ warm-up-2 | Warm-up: guess first | practice | Three guesses about layers and movement.

:::q Guess first (write it down)
1. You rotate a rectangle and it swings around its corner instead of spinning in place. What is set wrong?
2. Ten shapes must move together as one. Name a way that doesn't mean animating ten layers.
3. A layer is dimmed to 50 % opacity. Is a layer "attached" to it also dimmed?
:::

@@ layer-types | Layer types | idea | Four you will make tonight: solid, shape, text, null.

[[fig:layer_stack|A background solid, a shape and a text layer, stacked.|w=90]]

| Layer | Make it | Use |
|---|---|---|
| **Solid** | **Ctrl+Y** | backgrounds, colour fields |
| **Shape** | **Q** or **G**, drawn with nothing selected | graphics, lines |
| **Text** | **Ctrl+T** then click | titles |
| **Null** | **Ctrl+Alt+Shift+Y** | invisible controller |
| **Adjustment** | **Ctrl+Alt+Y** | effects on everything below |
| Footage | drag in from Project | video, images, audio |

@@ stack | Stacking order | idea | Layer 1 is in front. The bottom layer is drawn first.

[[fig:layer_stack|Bottom renders first; each layer is drawn over the result so far.|w=100]]

- Drag layers up and down in the Timeline, or **Ctrl+Alt+↑ / ↓**.
- Layers are numbered by position; the numbers change as you reorder.
- A numpad digit selects a layer by its number.

:::reveal Quick check: text is hidden behind a solid. Fix?
Drag the text **above** the solid (smaller number), or select it and press **Ctrl+Alt+↑**.
:::

@@ transform-keys | Five properties, five keys | idea | A P S R T open one property each. U shows what is animated.

[[fig:transform_keys|Select a layer and press the letter. Shift + letter adds another property to the view.|w=100]]

:::q Try it
Make a solid. Press **P**, then **Shift+S**, then **Shift+R**. What did each press add?
:::

Drag a number to scrub it. **Shift-drag** = 10× steps, **Ctrl-drag** = fine steps.

:::reveal Quick check: which key shows only what you have animated?
**U.** **UU** shows every property you changed, animated or not. Opening a template and pressing UU shows how it was built.
:::

@@ anchor | The anchor point is the pivot | idea | Scale and rotation happen around the anchor point. Position places the anchor point in the frame.

[[fig:anchor_rotation|Same 35° rotation. Only the anchor point (orange) differs.|w=100]]

- **Pan Behind tool (Y):** drag the anchor point without moving the layer on screen.
- **Ctrl+Alt+Home:** anchor point to the centre of the layer's content.
- A shape that orbits instead of spinning has its anchor point away from the shape. **Ctrl+Alt+Home**, then rotate.

:::reveal Quick check: warm-up question 1
The **anchor point** sits at the corner. Move it to the centre (**Y** or **Ctrl+Alt+Home**).
:::

@@ parenting | Parenting and nulls | method | Children follow their parent's position, scale and rotation. Not its opacity.

[[fig:parenting|Move or rotate the null; every child moves with it.|w=100]]

1. **Ctrl+Alt+Shift+Y** makes a null.
2. **Shift+F4** shows the Parent column.
3. Drag each child's **pick whip** onto the null.
4. Animate the null only.

:::trap Opacity is not inherited
Fading the parent does not fade the children. Fade each child, or precompose the group and fade the precomp (chapter 5).
:::

:::reveal Quick check: warm-up questions 2 and 3
2: parent all ten to **one null** and animate the null. 3: **no**, opacity is not passed to children.
:::

@@ switches | Switches worth knowing | idea | Eye, solo, lock, shy, motion blur. F4 swaps switches and modes.

[[fig:timeline_anatomy|Switches sit in the columns left of the layer names (area 2).|w=70]]

| Switch | Does |
|---|---|
| **Eye** | show/hide the layer |
| **Solo** | only soloed layers show: isolate what you are fixing |
| **Lock** | no edits (Ctrl+L; Ctrl+Shift+L unlocks all) |
| **Shy** | hides the layer from the Timeline list (still renders) when Hide Shy is on |
| **Motion Blur** | blur fast motion; needs the comp's motion-blur switch too |

**F4** toggles the Switches / Modes columns. Modes holds blending mode and track matte.

@@ time-edit | Cutting and sliding layers in time | method | Alt+[ and Alt+] trim; Ctrl+Shift+D splits; [ and ] slide.

[[fig:timeline_anatomy|All of these act at the CTI (the red line).|w=70]]

| Key | Does |
|---|---|
| **Alt+[** / **Alt+]** | trim the layer's start / end to the CTI |
| **[** / **]** | slide the layer so it starts / ends at the CTI |
| **Ctrl+Shift+D** | split the layer at the CTI |
| **Ctrl+D** | duplicate |
| **I** / **O** | jump to the layer's start / end |

:::reveal Quick check: make a text appear at 2 s instead of 0 s
Select it, CTI to 2 s, press **[** (slide) or **Alt+[** (trim). Slide keeps its full length; trim cuts the start off.
:::

@@ self-test-2 | Self-test: chapter 2 | practice | In the software, no notes.

1. Make a blue solid, a star shape and a text layer; put the text on top.
2. Make the star spin in place around its own centre when you change Rotation.
3. Parent the star and the text to a null; move the null.
4. Make the text start at 1 s.

:::reveal Answers
1. Ctrl+Y; Q (cycle to Star), draw with nothing selected; Ctrl+T; drag text to layer 1. 2. Select star, **Ctrl+Alt+Home**, then R. 3. Ctrl+Alt+Shift+Y, Shift+F4, pick-whip both to the null. 4. CTI 1 s, select text, **[**.
:::
