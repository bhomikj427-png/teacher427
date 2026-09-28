@@ warm-up-3 | Warm-up: guess first | practice | Three guesses about motion.

:::q Guess first (write it down)
1. What is the smallest number of keyframes that makes something move?
2. A ball moves left to right at constant speed. Why might it look robotic?
3. You click the stopwatch next to Position a second time. What happens?
:::

@@ stopwatch | The stopwatch | idea | Click it once to start recording that property. Click it again and every keyframe is deleted.

[[fig:timeline_anatomy|The stopwatch (⏱) sits left of each property name; keyframes (◆) appear on its row.|w=80]]

- Stopwatch **on**: changing the value at any time creates or updates a keyframe at the CTI.
- Stopwatch **off**: the property has one value for the whole layer.

:::trap Clicking an active stopwatch
It **deletes all keyframes** of that property and keeps the current value. Ctrl+Z if it happens.
:::

:::reveal Quick check: warm-up question 3
All Position keyframes are deleted.
:::

@@ add-keys | Two keyframes = motion | method | Start state at one time, end state at another. After Effects fills the frames between.

[[fig:interp_graphs|Two keyframes (◆). The frames in between are computed: that is interpolation.|w=100]]

:::q Try it
Solid, **P**, CTI at 0 s, click the stopwatch, drag the layer left. CTI to 2 s, drag it right. Space. Predict: does it move at constant speed?
:::

| Key | Does |
|---|---|
| **Alt+Shift+P** | keyframe Position at the CTI, no mouse (S, R, T, A: Scale, Rotation, Opacity, Anchor) |
| **J** / **K** | previous / next keyframe |
| **Alt+→** / **Alt+←** | nudge selected keyframes one frame |

Click a property's name to select all its keyframes; drag to retime.

@@ interpolation | Interpolation: how the gap is filled | idea | Linear is constant speed. Bezier types curve. Hold jumps.

[[fig:interp_graphs|Top: value over time. Dots: where the layer is on each frame. Even dots = constant speed.|w=100]]

- **Linear**: constant speed, instant start and stop. Mechanical.
- **Bezier family** (Auto, Continuous, Bezier): smooth curves you can shape.
- **Hold**: the value stays, then jumps at the next keyframe. For pops and cuts.
- Change it: right-click a keyframe > Keyframe Interpolation (**Ctrl+Alt+K**).

:::reveal Quick check: warm-up question 1
**Two**: a start and an end.
:::

@@ easy-ease | Easy Ease: F9 | method | Speed 0 at each keyframe, 33.33 % influence. Slow in, slow out.

[[fig:interp_graphs|The middle graph is Easy Ease: dots bunch up near the keyframes (slow) and spread in the middle (fast).|w=100]]

Select keyframes → **F9**. Only arriving: **Shift+F9**. Only leaving: **Ctrl+Shift+F9**.

Real things speed up and slow down. Animators call it *slow in and slow out* (Thomas & Johnston, 1981). This single key is the biggest quality jump tonight.

:::reveal Quick check: warm-up question 2
Real objects accelerate and decelerate. Constant speed with instant stops reads as mechanical. **F9** on both keyframes.
:::

@@ graph-editor | The Graph Editor | method | Shift+F3. The speed graph shows the ease; drag handles to shape it.

[[fig:speed_graphs|Same move, two speed graphs. The shaded area is the distance, so it stays equal when you reshape the curve.|w=100]]

- **Shift+F3** toggles the Graph Editor. Position shows the **speed** graph; most other properties show the **value** graph.
- Drag a keyframe handle **up** = faster there; **sideways** = influence (how long the ease lasts).
- Try: drag the **end** keyframe's handle far left for a longer, softer landing (more influence).

:::reveal Quick check: raise the start speed. What happens to the middle?
The middle slows. The distance (area) is fixed, so extra speed early is paid back later.
:::

@@ motion-path | The motion path | idea | Animated Position draws a path in the frame. Dot spacing = speed.

[[fig:interp_graphs|The dot rows under each graph are what the motion path shows: one dot per frame.|w=100]]

- Boxes on the path are keyframes; drag their handles to bend the path.
- **Pen (G)** on the path adds a keyframe there.
- Tight dots = slow; wide dots = fast.

@@ boomerang | Trap: the boomerang drift | trap | Two equal Position keyframes can drift apart and back. Use Hold or Linear.

[[fig:boomerang|Keyframes 2 and 3 hold the same position, but the default Auto Bezier path bulges out and back.|w=100]]

:::trap Why it happens
Position uses **Auto Bezier** by default, which draws a smooth curve through neighbouring keyframes, even between two equal ones.
:::

Fix: right-click keyframe 2 > **Toggle Hold Keyframe** (Ctrl+Alt+H), or set both to Linear.

@@ self-test-3 | Self-test: chapter 3 | practice | In the software, no notes.

1. Make a circle travel across the frame in 1.5 s and stop softly.
2. Make it pause 1 s at the end of the move, then fly off the right edge.
3. Show only the animated properties.
4. Open the speed graph and make the stop even softer.

:::reveal Answers
1. Alt+Shift+P at 0 s, move CTI to 1.5 s, drag; select both keyframes, **F9**. 2. At 2.5 s press Alt+Shift+P (same value → a hold); at 3 s move it off-frame; if it drifts, Hold on the 1.5 s keyframe. 3. **U**. 4. **Shift+F3**, drag the last keyframe's handle further left.
:::
