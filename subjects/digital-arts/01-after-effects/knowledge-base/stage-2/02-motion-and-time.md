# Stage 2 · 02 — Motion and time (why motion feels right)

> Depth for unit 03. Truth = [UG] for the software; [TJ81]/[WLV06] (`sources.md` in this folder) for the
> animation principle.

## 1. Value graph vs speed graph: one curve and its slope [UG p.233, 309, 318]
- The **value graph** plots the property value v(t). The **speed graph** plots how fast it changes, the
  slope dv/dt. (For Position, speed is the length of the velocity vector, in px/s.)
- So: a straight value line ↔ a flat speed line (constant speed = Linear). An S-shaped value curve ↔ a
  hill-shaped speed curve that starts and ends at 0 (Easy Ease). A Hold ↔ a flat value line with a step.
- **The area under the speed curve between two keyframes is fixed** — it equals the distance travelled
  (the change in value). *Derived:* pulling one handle up (faster at a keyframe) must lower speed elsewhere
  in that segment to keep the same total, which is why dragging speed handles reshapes the whole segment.
- **Influence** = how far in time a keyframe's handle reaches into the segment (Easy Ease default 33.33 %).
  More influence = a longer, softer ease and a sharper speed peak in the middle. [UG p.321]
- Temporal and spatial interpolation are independent: the motion **path shape** (spatial) and the
  **timing along it** (temporal) are set separately. Dot spacing on the path is the temporal part drawn in
  space. [UG p.292–293, 309]

## 2. Why easing reads as "real" [TJ81 via WLV06]
- Thomas & Johnston's *Slow in and slow out* principle: physical objects rarely change speed instantly;
  action slows around the key poses. In hand animation that meant more drawings near the extremes. Easy
  Ease produces the same spacing automatically (tight dots near keyframes, wide in the middle).
- Their caution, quoted by White, Loken & van de Panne (2006): overuse gives "a mechanical feel to the
  action", proper use "a very spirited result". *So:* F9 everywhere looks samey; strong ease-out +
  softer ease-in (tuned in the speed graph) is the usual next step.

## 3. Frames, frame rate, motion blur [UG p.91–92, 193]
- Everything happens on frames: at 30 fps one frame = 1/30 s. Keyframes can sit only on frames unless
  "Allow keyframes between frames" is on in the Graph Editor options. [UG p.235]
- **Motion blur** simulates a camera shutter. **Shutter angle** sets exposure as a fraction of the frame:
  exposure = (angle / 360) × frame duration. Adobe's example: 90° at 24 fps → 1/96 s. The common 180° at
  30 fps → 1/60 s. [UG p.91]
- It needs both the layer switch and the comp's **Enable Motion Blur** switch (trap T15). It costs render
  time; turn the comp switch on for final checks and renders.
- **Posterize Time / Preserve frame rate** deliberately lower the frame rate for a stop-motion look. [UG p.91]

## 4. Expressions as functions of time [UG p.597, 614–616]
- An expression is evaluated fresh on every frame; `time` is the comp time in seconds. So `time * 90`
  is a straight line in the value graph with slope 90 °/s.
- `wiggle(freq, amp)` adds smooth noise to the keyframed value (octaves add finer detail; amp_mult scales
  each octave). Adobe's example: `position.wiggle(5, 20, 3, .5)` ≈ 5 wiggles/s of about 20 px, plus finer
  layers at 10 and 20 wiggles/s of about 10 and 5 px. [UG p.615]
- `loopOut("cycle")` maps any time after the last keyframe back into the keyframed range, so a 1 s
  bounce repeats until the layer ends. `"pingpong"` alternates forward and backward.
