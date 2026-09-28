# 03 — Keyframes & motion

> Stage 1. Truth = [UG]. `settled` unless marked.

## Keyframes (big idea 2) [UG p.232]
- Animation = change over time. Any property with a **stopwatch** can be animated.
- **Click the stopwatch** → a keyframe at the current time; from then on, changing the value at another
  time creates or updates a keyframe there.
- **Clicking an active stopwatch again deletes every keyframe** of that property and keeps the current
  value as a constant. (Adobe's own warning.)
- Keyframe at the CTI without touching the mouse: **Alt+Shift + property key** (Alt+Shift+P for Position,
  Alt+Shift+S Scale, Alt+Shift+R Rotation, Alt+Shift+T Opacity, Alt+Shift+A Anchor). [UG p.22, 25]
- **J / K** jump to the previous / next keyframe (or marker, or work-area edge). [UG p.17]
- Move keyframes: drag; **Alt+← / Alt+→** nudges selected keyframes one frame. Copy/paste works; pasted
  keyframes land at the CTI. Click a property name to select all its keyframes.
- A minimum useful animation is **two keyframes**: a start state and an end state. The values between are
  **interpolated** ("tweening"). [UG p.232, 309]

## Interpolation [UG p.309–313]
- **Temporal** interpolation = how the value moves through *time* (seen in the value graph).
  **Spatial** interpolation = the *shape* of a motion path in the frame (Position, Anchor Point only).
- Methods (all are constrained versions of Bezier):
  - **Linear:** constant rate, instant start and stop → mechanical. Diamond icon. Straight line in the
    value graph.
  - **Auto Bezier:** smooth through the keyframe, handles set automatically. **Default spatial**
    interpolation. Dragging a handle converts it to Continuous Bezier.
  - **Continuous Bezier:** smooth, handles set by you.
  - **Bezier:** handles independent; can make a corner in a curved path.
  - **Hold:** temporal only; value jumps at the next keyframe (flat line then a step) → strobes, pops,
    cuts.
- Change: right-click a keyframe > Keyframe Interpolation (**Ctrl+Alt+K**); Ctrl+Alt+H toggles Hold.
- **Boomerang trap:** two Position keyframes with the **same value** and Auto Bezier spatial
  interpolation can drift back and forth between them. Fix: Hold on the first, or Linear on both.
  [UG p.310]

## Easy Ease [UG p.25, 321]
- **F9** = Easy Ease (in and out); **Shift+F9** = ease in; **Ctrl+Shift+F9** = ease out.
- Mechanism: each eased keyframe gets **speed 0** with **33.33 % influence** on the eased side(s): the
  layer slows into the keyframe and accelerates out. Icons change to hourglass shapes.
- Why it matters: real objects accelerate and decelerate. Linear motion reads as robotic; eased motion
  reads as physical. This one key is the biggest quality jump a beginner can make.

## Graph Editor [UG p.233–235]
- **Shift+F3** toggles between layer-bar mode and Graph Editor mode.
- Two graphs: **value graph** (property value vs time) and **speed graph** (rate of change vs time).
  Auto-select shows the speed graph for spatial properties (Position) and the value graph for the rest.
- In the speed graph, dragging a keyframe's handle **up = faster**, down = slower, and **sideways =
  influence** (how far the ease reaches). Bigger influence → longer, more dramatic ease. [UG p.318]
- **Separate Dimensions** splits Position into X and Y so each can be keyframed and eased on its own.
- Reading the value graph: the **slope** is the speed. Flat = still. Steep = fast. An S-curve = eased.

## Motion paths [UG p.292–293]
- Animating Position draws a **motion path** in the Composition panel: dots = one per frame, boxes =
  keyframes. **Dot spacing shows speed** (tight dots = slow, wide = fast).
- Bend the path by dragging keyframe handles; add a keyframe on the path with the Pen tool.

## Time helpers
- **B / N** set the work-area start / end to the CTI; previews and (by default) renders use the work area.
- **Alt+Shift+J** go to a typed time. **Home / End** comp start / end. **Page Up / Page Down** (or
  Ctrl+← / Ctrl+→) step one frame; add Shift for 10 frames. **Plain arrows nudge the selected layer 1 px —
  they do not step time.** [UG p.16–19, 23]
- **= / -** zoom the timeline in time; **;** zooms to single frames.

→ Stage 2: `stage-2/02-motion-and-time.md` (value vs speed graph maths; frame rate, motion blur, the
12-principles link).
