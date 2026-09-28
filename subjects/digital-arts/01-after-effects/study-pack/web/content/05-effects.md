@@ warm-up-5 | Warm-up: guess first | practice | Three guesses about effects and structure.

:::q Guess first (write it down)
1. You want one glow on 12 layers. Add Glow 12 times, or something else?
2. A rotating logo has a drop shadow. Does the shadow keep pointing the same way?
3. Name something that keeps a shape spinning forever without keyframes.
:::

@@ effects | Applying effects | method | Ctrl+5, search, double-click. Settings in Effect Controls (F3).

[[fig:render_order|Effects run after masks and before the transform, top to bottom in Effect Controls.|w=100]]

- **Effects & Presets (Ctrl+5)**: type the name, **double-click** it (applies to selected layers) or drag it onto a layer.
- Adjust in **Effect Controls (F3)**. Effect properties have stopwatches: they animate like any property.
- **E** shows a layer's effects in the Timeline. **Ctrl+Shift+E** removes all effects.
- Start with: **Gradient Ramp**, **Fill**, **Glow**, **Drop Shadow**, **Gaussian Blur**, **Fractal Noise**.

@@ adjustment | Adjustment layers | method | Effects on an adjustment layer hit every layer below it.

[[fig:adjustment_layer|Glow on layer 2 reaches layers 3 and 4, not layer 1.|w=100]]

- **Ctrl+Alt+Y**. Put effects on it, not on each layer.
- It works on the combined image below, so it is also **faster** than the same effect on many layers.
- Draw a mask on it to limit the effect to an area.

:::reveal Quick check: warm-up question 1
One **adjustment layer** with Glow above the 12 layers.
:::

@@ render-order | The order a frame is built | idea | Bottom layer first. Inside a layer: masks → effects → transform.

[[fig:render_order|This one order explains most "why did it do that?" moments.|w=100]]

Because effects come **before** transform, a drop shadow is baked in and then rotated with the layer.

:::reveal Quick check: warm-up question 2
**No.** The shadow turns with the logo. Put the shadow on an adjustment layer above, or precompose the logo and shadow the precomp.
:::

@@ precompose | Pre-compose: many layers become one | method | Ctrl+Shift+C. Usually: Move all attributes into the new composition.

[[fig:precompose|Three layers become one precomp layer; double-click it to edit inside.|w=100]]

| Option | Use it when |
|---|---|
| **Move all attributes into the new composition** | grouping several layers (the normal case) |
| Leave all attributes | a single footage layer whose keyframes/effects should stay outside |

Why: one matte, effect or fade for a whole group; a tidy Timeline; a reusable piece. **Tab** jumps between nested comps.

:::reveal Quick check: fade five layers together
Pre-compose them (Move all attributes), then keyframe the precomp's **Opacity (T)**.
:::

@@ expr-basics | Expressions in one minute | idea | A short line of code that sets a property's value on every frame.

[[fig:expr_plots|Expressions are functions of time: here, a straight rotation and a looped bounce.|w=100]]

1. **Alt-click the stopwatch** of a property.
2. Type the expression in the field that opens.
3. Click outside it.

**EE** shows every expression in the comp. Delete the text (or Alt-click again) to remove it.

@@ expr-three | Three expressions worth knowing | method | wiggle, time, loopOut: drift, spin, repeat.

[[fig:expr_plots|Left: time * 90 turns 90° per second. Right: the keyframed bounce, repeated by loopOut.|w=100]]

| Expression | On | Does |
|---|---|---|
| `wiggle(2, 30)` | Position | drifts randomly, about 2 times a second, about 30 px |
| `time * 90` | Rotation | 90° per second, forever |
| `loopOut("cycle")` | any keyframed property | repeats the keyframed part until the layer ends |

:::reveal Quick check: warm-up question 3
`time * 90` on Rotation (any number sets the speed in degrees per second).
:::

@@ self-test-5 | Self-test: chapter 5 | practice | In the software, no notes.

1. Blur everything except the top layer, with one effect.
2. Group a line and a title so they fade out together.
3. A small shape that drifts gently forever.

:::reveal Answers
1. Adjustment layer (Ctrl+Alt+Y) under the top layer, Gaussian Blur on it. 2. Select both, Ctrl+Shift+C (Move all attributes), keyframe the precomp's Opacity. 3. Alt-click its Position stopwatch, `wiggle(1, 15)`.
:::
