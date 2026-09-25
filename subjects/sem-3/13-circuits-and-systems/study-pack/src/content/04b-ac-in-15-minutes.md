# 04b — AC in 15 minutes: phasors, j and angles

<div class="sub">Read before 05 §6, 06 §6 and 07 §4 · no new syllabus item: it's the tool those AC parts use · textbook: Hayt ch. 10 · every number checked by script (`verify_ac.py`)</div>

## Map

[[map:1 An AC source is just a cosine > 2 Keep only size and angle (the phasor) > 3 j = "turn 90°" > 4 R, L, C become impedances Z > 5 Solve like DC|here=1]]

**The whole idea in one line:** turn the AC circuit into a DC-style circuit with complex numbers, solve it with the rules you already know (Ohm, dividers, KVL, Thévenin), then turn the answer back into a cosine.

---

### 1 · An AC source is just a cosine

$$v(t) = V_{m} cos(ωt + θ)$$

- **V_{m}** = size (peak value).
- **ω** = how fast it wiggles (rad/s). It is given in the question and **never changes** anywhere in the circuit.
- **θ** = angle: how far the wave is shifted left or right.

In a circuit of R, L and C with one source, **every voltage and current is a cosine at the same ω**. They differ in only two things: **size** and **angle**.

[[fig:ac_wave|The source and the voltage across the resistor in the example of §5. Same ω; different size, different angle.|w=80]]

So you only need to track two numbers per quantity. That pair is the **phasor**.

### 2 · The phasor: write size∠angle

$$10 cos(1000t − 45°)  ⇒  10∠−45°      (drop the "cos(ωt ...)", keep size and angle)$$

Going back is the reverse: 7.07∠−45° mA at ω = 1000 means i(t) = 7.07 cos(1000t − 45°) mA.

:::note sin instead of cos?
If the question gives sin (like 02's 10 sin(2000t + 30°)), just use sin both ways: 10∠30°, and the answer goes back into sin(…). Don't mix sin and cos in one problem.
:::

### 3 · What j is

A phasor is an **arrow**: length = size, direction = angle. You can write the same arrow two ways:

| Form | Looks like | Means | Best for |
|---|---|---|---|
| **Polar** | M∠θ | length M, angle θ | multiplying, dividing |
| **Rectangular** | a + jb | a across, b up | adding, subtracting |

**j** marks the "up" part. That's all it is. (Maths writes i; circuits use j because i is current.)

[[fig:phasor_plane|3 + j4: go 3 right, 4 up. The arrow has length 5 and angle 53.1°.|w=52]]

**Converting (the only formulas you need):**

$$Rectangular → polar:  M = \sqrt{a^{2} + b^{2}}    θ = tan^{−1}(b/a)$$

$$Polar → rectangular:  a = M cos θ    b = M sin θ$$

So 3 + j4 = \sqrt{9 + 16}∠tan^{−1}(4/3) = **5∠53.1°**, and 10∠30° = 8.66 + j5.

:::trap Quadrant trap
If a is negative, the arrow points left, and tan^{−1} gives the wrong angle. Add 180°. Example: −3 + j4 = 5∠**126.9°**, not 5∠−53.1°. A quick sketch of the arrow catches this.
:::

**Two rules for arithmetic:**

- **Add/subtract → rectangular.** Add the real parts, add the j parts: (5 − j5) + (5 + j5) = 10.
- **Multiply/divide → polar.** Multiply → **multiply sizes, add angles**. Divide → **divide sizes, subtract angles**.

$$(2∠30°)(3∠20°) = 6∠50°      \frac{10∠0°}{5∠−90°} = 2∠90°$$

**j itself:** j = 1∠90°, so multiplying by j turns an arrow 90° anticlockwise. Also j^{2} = −1, and **\frac{1}{j} = −j** (it turns by −90°). You'll use that last one for capacitors.

:::check Check 1 (answers at the end)
(a) Write 20 cos(500t + 60°) V as a phasor. (b) Convert 6 − j8 to polar. (c) Divide 10∠0° by 2∠45°.
:::

### 4 · R, L and C become impedances

Impedance **Z** is "AC resistance": V = I·Z, just like V = IR. It's complex, because L and C shift the angle.

| Element | Impedance Z | Angle | In words |
|---|---|---|---|
| R | **R** | 0° | no shift |
| L | **jωL** | +90° | current lags the voltage by 90° |
| C | \frac{1}{jωC} = **−j\frac{1}{ωC}** | −90° | current leads the voltage by 90° |

[[fig:z_plane|R points right, L points up, C points down. Series elements add as arrows.|w=44]]

Example at ω = 1000 rad/s: a 1 H inductor is j·1000·1 = **j1000 Ω**. A 1 µF capacitor is \frac{1}{j·1000·10^{−6}} = \frac{1000}{j} = **−j1000 Ω**.

**Everything from DC still works with Z in place of R:** series Z's add, parallel is \frac{Z_{1}Z_{2}}{Z_{1} + Z_{2}}, voltage/current dividers, KVL, KCL, nodal, mesh, superposition, Thévenin. Nothing new to learn: only the numbers are complex.

### 5 · The recipe, on the circuit from 05 §6

:::q
10 cos(1000t) V drives 1 kΩ in series with 1 H. Find the current i(t).
:::

:::guess Guess first
Will the current's angle be positive or negative? (Hint: which way does an inductor's Z point?)
:::

[[fig:ac_rl_domains|Step 1 and 2: the source becomes a phasor, each element becomes its impedance.|w=90]]

**Step 1. Source → phasor.** 10 cos(1000t) ⇒ **10∠0° V**.

**Step 2. Elements → Z** (ω = 1000). R = 1000 Ω, L: jωL = **j1000 Ω**.

**Step 3. Solve like DC.** Series, so add (rectangular), then divide (polar):

$$Z = 1000 + j1000 = 1414∠45° Ω      I = \frac{V}{Z} = \frac{10∠0°}{1414∠45°} = 7.07∠−45° mA$$

**Step 4. Back to time.** i(t) = **7.07 cos(1000t − 45°) mA**.

A time simulation of the circuit gives exactly this: peak 7.071 mA, 45° behind the source. The current **lags** (negative angle), because the inductor pulled the angle of Z up to +45°, and dividing subtracts it.

**KVL still works, but as arrows.** V_{R} = I·1000 = 7.07∠−45° V, and V_{L} = I·j1000 = 7.07∠+45° V.

[[fig:kvl_phasor|The two element voltages add head-to-tail to the source. Their sizes do not add up to 10.|w=50]]

:::trap Size trap
7.07 + 7.07 = 14.1 V, more than the 10 V source! Sizes of phasors don't add. Add in rectangular: (5 − j5) + (5 + j5) = 10 ✓.
:::

:::check Check 2
Replace the inductor with a **1 µF capacitor** (same source, same 1 kΩ). Find I as a phasor and i(t). Does the current lead or lag?
:::

### 6 · Peak vs rms (only for power)

A phasor's size is usually the **peak**. Power formulas use **rms**:

$$rms = \frac{peak}{√2}      (for a sinusoid)$$

That's why 07 §4 says P_{max} = \frac{|V_{Th}|^{2}}{4R_{Th}} with rms, or \frac{|V_{Th}|^{2}}{8R_{Th}} with peak.

---

## Summary card

| Step | Do |
|---|---|
| 1 | Source V_{m} cos(ωt + θ) → **V_{m}∠θ** |
| 2 | R → R, L → **jωL**, C → **−j/(ωC)** |
| 3 | Solve with DC rules. **Add in a + jb, multiply/divide in M∠θ.** |
| 4 | Answer M∠θ → **M cos(ωt + θ)** (same ω) |

**Where you use it next:** 05 §6 (AC superposition), 06 §6 (AC Thévenin/Norton), 07 §4 (conjugate match), mock B11.

## Self-test

1. What is the impedance of 0.2 H at ω = 500 rad/s? Of 10 µF at ω = 500 rad/s?
2. 10 cos(500t) V drives 100 Ω in series with 0.2 H. Find i(t).
3. Convert −3 + j4 to polar. Why is tan^{−1}(4/−3) not enough?
4. A current phasor is 5∠0° mA (peak). What is its rms value?
5. Why can you add phasors only when all sources have the same ω? (Look at 05 §6.)

<!--ANSWERS-->
## Answers

**Guess (§5).** Negative: the inductor makes Z's angle positive (+45°), and I = V/Z subtracts it.

**Check 1.** (a) **20∠60° V**. (b) \sqrt{36 + 64} = 10, tan^{−1}(−8/6) = −53.1° ⇒ **10∠−53.1°** (a is positive, so no correction). (c) 10/2 = 5, 0° − 45° ⇒ **5∠−45°**.

**Check 2.** Z_{C} = −j1000 Ω. Z = 1000 − j1000 = 1414∠−45° Ω. I = \frac{10∠0°}{1414∠−45°} = **7.07∠+45° mA**, so i(t) = **7.07 cos(1000t + 45°) mA**. The current **leads**: a capacitor pulls the angle the opposite way to an inductor.

**Self-test.**

1. jωL = j·500·0.2 = **j100 Ω**. \frac{1}{jωC} = \frac{1}{j·500·10^{−5}} = \frac{200}{j} = **−j200 Ω**.
2. Z = 100 + j100 = 141.4∠45° Ω; I = \frac{10∠0°}{141.4∠45°} = 70.7∠−45° mA ⇒ **i(t) = 70.7 cos(500t − 45°) mA**.
3. **5∠126.9°**. tan^{−1}(4/−3) gives −53.1°, an arrow pointing right and down; but −3 + j4 points left and up, so add 180°.
4. 5/√2 = **3.54 mA rms**.
5. A phasor only means something at one ω (Z_{L} = jωL changes with ω). Different ω's: solve each separately, turn each answer into a cosine, then add in time.
<!--/ANSWERS-->
