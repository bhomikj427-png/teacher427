# 04c — Polar vs rectangular: why two forms?

<div class="sub">Follows 04b · a maths doubt that AC circuits force on you · textbook: Sadiku ch. 9 §9.3 + App. B (complex numbers) · every number checked by script (`verify_polar.py`)</div>

## Map

[[map:04b: phasor = size∠angle > 1 Same arrow, two addresses > 2 Adding: rectangular wins > 3 Multiplying: polar wins > 4 Why angles add > 5 Why AC needs both > 6 Could rectangular do everything?|here=2]]

**You already have (04b):** a phasor is an arrow. **a + jb** says "a across, b up". **M∠θ** says "length M, turned θ from the right". This sheet answers why you keep switching between them.

:::q Sadiku, Practice Problem 10.5 (assignment B81)
Find current I_{o} in the circuit of Fig. 10.8 using the superposition theorem.
:::

Superposition gave the two pieces: **I_{o}′ = 2.808∠81.84° A** (voltage source alone) and **I_{o}″ = 3.370∠51.84° A** (current source alone). The last step is I_{o} = I_{o}′ + I_{o}″.

:::guess Guess first
Is the answer 6.178∠133.68° (add the sizes, add the angles)? If not, roughly how big is it, and roughly what angle?
:::

---

### 1 · The same arrow, two addresses

Two ways to give directions to the same spot: "walk 3 m east, then 4 m north", or "walk 5 m, facing 53.1° left of east". Same spot. Neither carries more information.

[[fig:two_addresses|3 + j4 and 5∠53.1° are the same arrow. Conversion (04b): M = √(a² + b²), θ = tan⁻¹(b/a); back: a = M cos θ, b = M sin θ.|w=88]]

So the question is never "which form is correct". It is **"which form makes this step short"**. Each form has one operation it makes trivial.

**Bridge:** the two operations a circuit needs are **adding** (KVL, KCL, series Z) and **multiplying/dividing** (V = IZ). Take them one at a time.

### 2 · Adding: rectangular wins

**Adding two arrows** means walking one, then the other from where you stopped (head-to-tail). The "across" moves and the "up" moves don't affect each other, so they add separately:

$$(a + jb) + (c + jd) = (a + c) + j(b + d)$$

**Polar has no such rule.** Two arrows of sizes 3 and 4 can add to anything from 1 to 7. It depends on the angle between them:

[[fig:add_angle_matters|Same sizes, three different answers. In polar you'd need the cosine rule every time.|w=95]]

"Add the sizes" is only true when the angles are equal (left panel). That's the mistake the guess tempted you into.

**The anchor, solved.** Convert each piece to rectangular, add, convert back:

$$I_{o}′ = 2.808∠81.84° = 0.399 + j2.780        I_{o}″ = 3.370∠51.84° = 2.082 + j2.650$$

$$I_{o} = 2.481 + j5.429 = 5.97∠65.4° A$$

[[fig:rect_add_pp105|The sum's size, 5.97, is less than 2.808 + 3.370 = 6.18, because the two arrows point in different directions. (Book: 5.97∠65.45°, from unrounded pieces.)|w=56]]

:::check Check 1 (answers at the end)
(a) Add 10∠30° + 10∠−30°. Is the result's size 20? (b) Which form did you have to go through?
:::

**Bridge:** adding is "move". The other thing a circuit does to an arrow is "stretch and turn" (§3).

### 3 · Multiplying: polar wins

**Multiplying by a complex number** does two things to an arrow: it **stretches** the length and **turns** the angle.

[[fig:multiply_turn|(5∠53.1°) × (2∠30°): length 5 × 2 = 10, angle 53.1° + 30° = 83.1°.|w=44]]

Polar stores exactly those two things, so the rule is one line each:

$$multiply: sizes ×, angles +        divide: sizes ÷, angles −$$

Rectangular has to expand brackets and use j² = −1:

| | Rectangular | Polar |
|---|---|---|
| (3 + j4)(1 + j1) | 3 + j3 + j4 + j²4 = **−1 + j7** (4 products, then regroup) | 5∠53.1° × 1.414∠45° = **7.07∠98.1°** |
| \frac{10}{3 + j4} | multiply top and bottom by the conjugate 3 − j4: \frac{30 − j40}{25} = **1.2 − j1.6** | \frac{10∠0°}{5∠53.1°} = **2∠−53.1°** |

Same answers (convert to check). Polar took one step each; rectangular took several, and division needs the **conjugate trick** (flip the sign of the j part to clear j from the bottom).

**Multiplying by j** is the cleanest case: j = 1∠90°, so it turns an arrow 90° and leaves its length alone. In rectangular: j(3 + j4) = −4 + j3, which is 3 + j4 turned a quarter-turn.

:::check Check 2
Find \frac{6∠0°}{2∠−90°} in polar, then in rectangular.
:::

**Bridge:** "angles add when you multiply" looks like a convenient rule. It's a consequence of something you already know (§4).

### 4 · Why angles add: they are exponents

Euler's formula says the polar form is really an exponential:

$$M∠θ  is shorthand for  M e^{jθ}        (e^{jθ} = cos θ + j sin θ)$$

**Exponents add when you multiply:** 10² × 10³ = 10⁵. In the same way:

$$M_{1}e^{jα} × M_{2}e^{jβ} = M_{1}M_{2} e^{j(α + β)}$$

So polar is the **exponent form** of a complex number, and rectangular is the **sum form**. Exponent form makes × and ÷ easy (same reason logarithms turned multiplication into addition on old slide rules). Sum form makes + and − easy. No single form makes both easy. That's a property of the numbers, not a choice of notation.

**Bridge:** that explains the maths. AC is where you need both operations at once (§5).

### 5 · Why AC needs both

An inductor's voltage is L·\frac{di}{dt}. Differentiate a sinusoid and look at what happens:

[[fig:deriv_shift|The slope of a cosine is the same cosine, scaled by ω and shifted 90° earlier. Scale + turn is multiplication by ω∠90° = jω.|w=88]]

That's where Z_{L} = jωL comes from. Every R, L and C does a **stretch-and-turn** to a sinusoid. That's **multiplication**, polar's job. Kirchhoff's laws **add** voltages and currents. That's rectangular's job. A circuit has both, so one problem uses both:

| Step in an AC problem | Operation | Use |
|---|---|---|
| Source V_{m} cos(ωt + θ) → V_{m}∠θ | read off size and angle | **polar** (comes that way) |
| R, jωL, −j/(ωC) | they're given as a + jb | **rectangular** (comes that way) |
| Series: Z_{1} + Z_{2} | add | **rectangular** |
| V = IZ, I = V/Z, dividers | multiply / divide | **polar** |
| Parallel: \frac{Z_{1}Z_{2}}{Z_{1} + Z_{2}} | top ×, bottom + | **both, in one formula** |
| KVL, KCL, superposition sum | add | **rectangular** |
| Answer → M cos(ωt + θ) | need size and angle | **polar** |

In PP 10.5, the 10 A piece needs the divider I_{o}″ = 10 × \frac{Z}{(8 − j2) + Z} with Z = j4 ∥ 6. Mixed form: Z = \frac{24∠90°}{7.211∠33.69°} = 3.328∠56.31° = 1.846 + j2.769; bottom = 9.846 + j0.769 = 9.876∠4.47°; then I_{o}″ = \frac{10 × 3.328}{9.876}∠(56.31° − 4.47°) = **3.370∠51.84°**. Each step is in the form where it is one line.

### 6 · So could rectangular do everything?

**Yes. Every step can be done in a + jb and gives the identical answer.** Nothing is ever *wrong* in rectangular. It costs:

- **More arithmetic, more slips.** The same I_{o}″ in rectangular only: two conjugate divisions and about ten multiplications. You get 2.082 + j2.650 = the same 3.370∠51.84°.
- **A conversion at the end anyway.** The time answer is M cos(ωt + θ), which needs size and angle. Rectangular can't skip polar; it postpones it.
- **Less meaning on the page.** 3.370∠51.84° tells you "3.37 A peak, 51.84° ahead of the reference". 2.082 + j2.650 tells you neither until converted.

Polar-only is worse: it has no shortcut for adding, so every KVL or KCL step would need the cosine rule.

:::key The rule
**Add or subtract → rectangular. Multiply or divide → polar. Convert whenever the next operation changes.** "Better" means fewer steps and fewer slips, never "more correct".
:::

:::trap Quadrant trap (from 04b)
Converting to polar with tan⁻¹(b/a) is wrong when a is negative: add 180°. −1 + j7 is 7.07∠98.1°, not 7.07∠−81.9°. Sketch the arrow first.
:::

---

## Summary card

| Form | Stores | Easy | Hard |
|---|---|---|---|
| **a + jb** (sum form) | across, up | +, − (parts add separately) | ×, ÷ (brackets, conjugate) |
| **M∠θ = Me^{jθ}** (exponent form) | stretch, turn | ×, ÷ (sizes ×÷, angles ±) | +, − (no rule; cosine rule) |

**Where you use it next:** every Sadiku ch. 10–11 problem in the assignment (B80–B127).

## Self-test

1. Add (4 + j3) + (4 − j3). Both have size 5: why is the sum's size not 10?
2. Find (2∠30°)(3∠60°) in polar, then in rectangular.
3. Find (4 + j3) ∥ (−j5) using \frac{Z_{1}Z_{2}}{Z_{1} + Z_{2}}. Say which form you use for the top, the bottom, and the division.
4. Show in rectangular that multiplying 3 + j4 by j keeps its size 5.
5. For each, which form: (a) series impedances, (b) I = V/Z, (c) the KCL sum at a node, (d) writing i(t)?
6. In one sentence: why does multiplying complex numbers add their angles?

<!--ANSWERS-->
## Answers

**Guess.** No. Sizes add only when angles are equal, and angles never add when you *add* arrows. The real answer is **5.97∠65.4° A**: a bit less than 6.18, with an angle between the two pieces' angles (51.84° and 81.84°).

**Check 1.** (a) 10∠30° = 8.660 + j5, 10∠−30° = 8.660 − j5. Sum = **17.32 + j0 = 17.32∠0°**. Not 20: the arrows are 60° apart. (b) Rectangular.

**Check 2.** Polar: \frac{6}{2} = 3, 0° − (−90°) = 90° ⇒ **3∠90°**. Rectangular: **0 + j3** (straight up).

**Self-test.**

1. **8 + j0 = 8.** The j parts cancel (one points up, one down). Sizes add only for arrows pointing the same way.
2. 2 × 3 = 6, 30° + 60° = 90° ⇒ **6∠90° = 0 + j6**.
3. Top (multiply, polar): (5∠36.87°)(5∠−90°) = 25∠−53.13°. Bottom (add, rectangular): 4 + j3 − j5 = 4 − j2 = 4.472∠−26.57°. Divide (polar): \frac{25}{4.472}∠(−53.13° + 26.57°) = **5.590∠−26.57° = 5 − j2.5 Ω**.
4. j(3 + j4) = j3 + j²4 = **−4 + j3**. Size √(16 + 9) = **5**. Same length, turned 90°.
5. (a) **rectangular** (add), (b) **polar** (divide), (c) **rectangular** (add), (d) **polar** (need M and θ).
6. Polar form is Me^{jθ}, and **exponents add when you multiply** powers of the same base.
<!--/ANSWERS-->
