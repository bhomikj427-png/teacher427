# 02b — Continuous random variables: PDF, CDF, median

<div class="sub">Gupta & Kapoor ch. 5 (§5.4) · blueprint row 1 "continuous random variables; PDF; CDF" · 3 real questions (Assignment 1 SA 2, SA 3, LA 1) · needs 01 (complement step 5, conditional probability step 7), 02a (random variable step 1, CDF step 7, reading F step 8)</div>

## Map

[[map:1 Probability is area > 2 Checking a PDF > 3 The smooth CDF > 4 The median > 5 A tail area > 6 Conditional with a PDF|here=1]]

02a counted: a discrete X has a list of values, and each value gets a probability. A **measured** quantity (a diameter, a lifetime, a day's power use) can take any value in an interval, so no list exists. This file replaces the PMF's bars with a smooth curve, the **PDF**, and replaces "add the bars" with "take the area". The CDF keeps its meaning from 02a, F(x) = P(X ≤ x); it becomes a smooth climb instead of a staircase. 03a then finds the average of such an X.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| X | a continuous random variable: a measurement that can take any value in an interval. Here, a cable's diameter | X between 0 and 1 |
| f(x) | the PDF (probability density function): the height of the curve at x. Not a probability; areas under it are | f(0.5) = 1.5 |
| ∫ₐᵇ f(x) dx | the area under f between a and b, which is P(a ≤ X ≤ b) | 0.396 for a = 0.2, b = 0.5 |
| F(x) | the CDF, as in 02a: P(X ≤ x), now the area under f to the left of x | F(0.5) = 0.5 |
| b | the median: the value with half the probability on each side, F(b) = ½ | b = 0.5 (cable) |

**Running example.** A cable's diameter X (in some unit) lies between 0 and 1, with PDF f(x) = 6x(1 − x) (A1 SA 3). The curve is a hump: low near the ends, highest in the middle. Steps 1–4 and Check 6 use it.

## The questions this file answers

- <span class="tag">A1 SA 3</span> The diameter of an electric cable X is a continuous random variable with pdf f(x) = 6x(1 − x), 0 ≤ x ≤ 1. (i) Check that it is a pdf. (ii) Determine b such that P(X < b) = P(X > b).
- <span class="tag">A1 SA 2</span> The daily consumption of electric power (in millions of kWh) is a random variable X with pdf f(x) = (1/9) x e^{−x/3}, x > 0. If the power plant has a daily capacity of 12 million kWh, what is the probability that the power supply will be inadequate on any given day?
- <span class="tag">A1 LA 1</span> The probability that a person will die between ages t₁ and t₂ is ∫ f(t) dt from t₁ to t₂, where f(t) = 3 × 10^{−9} t²(100 − t)² for 0 ≤ t ≤ 100 and 0 elsewhere. Find (i) the probability that a person will die between the ages 60 and 70; (ii) the probability that a person will die between those ages, assuming the individual lived up to 60.

---

## Build

### 1 · Probability is area under the curve

The cable's diameter can be 0.31, 0.3107, 0.31072…: too many values to list, so there are no bars to add.

:::q Predict
The cable's curve has height f(0.5) = 1.5. Can the probability that the diameter is exactly 0.5 be 1.5? What is a sensible answer?
:::

:::guess Guess first
A probability is never above 1. So what could the height 1.5 mean?
:::

:::note Terms
**Continuous random variable:** X can take any value in an interval (02a step 2: measurements). **PDF f(x)** (probability density function): a curve over the values of X. Its **height** at x tells how crowded the values are near x; it is not a probability. The **area** under the curve over an interval is the probability that X lands in that interval. It plays the role of the PMF's bars.
:::

$$P(a ≤ X ≤ b) = ∫_{a}^{b} f(x) dx$$

Read it as: "the chance X lands between a and b equals the area under f from a to b".

[[fig:cable_pdf|What this graph plots: the cable's PDF f(x) = 6x(1 − x). Horizontal axis: the diameter x. Height: f(x), how densely the diameters crowd near x. Shaded: the area from 0.2 to 0.5, which is P(0.2 ≤ X ≤ 0.5) = 0.396. Dots: the heights in the reading table.|w=62]]

**Reading the figure.**

| x | 0.2 | 0.5 | 0.8 |
|---|---|---|---|
| f(x) = 6x(1 − x) | 0.96 | 1.5 | 0.96 |
| meaning | diameters fairly common here | most crowded here | as common as at 0.2 (the hump is symmetric) |

The shaded area, worked out:

1. ∫ (6x − 6x²) dx = 3x² − 2x³.
2. At 0.5: 3(0.25) − 2(0.125) = 0.75 − 0.25 = 0.5.
3. At 0.2: 3(0.04) − 2(0.008) = 0.12 − 0.016 = 0.104.
4. Area = 0.5 − 0.104 = **0.396**.

- A single point has zero width, so **zero area**: P(X = 0.5) = 0 for a continuous X.
- So for a continuous X, **< and ≤ give the same answer**: P(X < 0.5) = P(X ≤ 0.5). (For a discrete X they differ: 02a step 8.)
- A height above 1 is fine. Only the total area must be 1.

**Answer to the Predict.** No. P(X = 0.5) = **0**, because a point has no width. The height 1.5 only says diameters near 0.5 are the most common; probabilities come from areas, such as P(0.2 ≤ X ≤ 0.5) = 0.396.

:::check Check 1
Cable: (a) P(X = 0.2). (b) P(0.5 < X < 0.8), using 3x² − 2x³. Does the answer match the hump's symmetry?
:::

### 2 · Checking that a curve is a PDF

02a step 4 had two rules for a PMF. A PDF has the same two, with the sum replaced by an area.

:::q <span class="tag">A1 SA 3 (i)</span>
The diameter of an electric cable X has pdf f(x) = 6x(1 − x), 0 ≤ x ≤ 1. Check that it is a pdf.
:::

:::guess Guess first
Which two things must hold? Think of 02a's "never negative" and "adds to 1".
:::

| Rule | PMF (02a) | PDF (here) |
|---|---|---|
| 1. never negative | p(x) ≥ 0 | f(x) ≥ 0 for every x |
| 2. everything adds to 1 | Σ p(x) = 1 | total area ∫ f(x) dx = 1 over all x |

Outside 0 ≤ x ≤ 1 the cable's f is 0, so the total area is the area from 0 to 1.

**Answer.**

1. On 0 ≤ x ≤ 1, both 6x and (1 − x) are ≥ 0, so **f(x) ≥ 0** ✓.
2. ∫₀¹ (6x − 6x²) dx = [3x² − 2x³]₀¹ = 3 − 2 = **1** ✓.

Both rules hold, so f is a pdf.

A PDF with an unknown constant k is found the same way as in 02a step 5: set the total area to 1 and solve for k.

:::check Check 2
f(x) = kx² for 0 ≤ x ≤ 3 (0 elsewhere). (a) Find k. (b) Find P(1 ≤ X ≤ 2).
:::

### 3 · The CDF: a smooth climb instead of a staircase

02a's F(x) = P(X ≤ x) added the bars to the left of x. For a continuous X it adds the **area** to the left of x.

:::q Predict
For the cable, guess F(0.5) without integrating. (Hint: the hump is symmetric about 0.5.)
:::

:::guess Guess first
What share of the total area of 1 lies left of the middle?
:::

:::note Terms
**CDF F(x):** the area under f from the far left up to x, F(x) = P(X ≤ x). Same meaning as 02a step 7; only the way it is added changes.
:::

$$F(x) = ∫_{−∞}^{x} f(t) dt$$

For the cable, f is 0 left of 0, so the area starts at 0:

1. For x < 0: F(x) = 0 (no area yet).
2. For 0 ≤ x ≤ 1: F(x) = ∫₀ˣ (6t − 6t²) dt = **3x² − 2x³**.
3. For x > 1: F(x) = 1 (all the area).

[[fig:cable_cdf|What this graph plots: the cable's CDF F(x) = 3x² − 2x³, the chance the diameter is at most x. It rises smoothly from 0 at x = 0 to 1 at x = 1, steepest where the PDF is highest (x = 0.5). Dashed: F(0.5) = 0.5.|w=62]]

**Reading the figure.**

| x | 0.2 | 0.5 | 0.8 |
|---|---|---|---|
| F(x) = 3x² − 2x³ | 0.104 | 0.5 | 0.896 |
| meaning | 10.4% of cables are thinner than 0.2 | half are thinner than 0.5 | 89.6% are thinner than 0.8 |

- No jumps: a continuous F climbs smoothly, because no single value holds any probability.
- The slope of F is f: **f(x) = F′(x)**. Check: d/dx (3x² − 2x³) = 6x − 6x² ✓. So the CDF is steepest where the PDF is tallest.
- 02a step 8's rules carry over unchanged: P(X > a) = 1 − F(a); P(a < X ≤ b) = F(b) − F(a). Step 1's area 0.396 is F(0.5) − F(0.2).

**Answer to the Predict.** F(0.5) = **0.5**: the hump is symmetric about 0.5, so half the area is on each side.

:::check Check 3
f(x) = 2x for 0 ≤ x ≤ 1. (a) Find F(x) on 0 ≤ x ≤ 1. (b) Find P(X > 0.5) from F.
:::

### 4 · The median: where F reaches one half

The last Predict found the point with half the area on each side. That point has a name, and the exam asks for it in disguise.

:::q <span class="tag">A1 SA 3 (ii)</span>
Determine b such that P(X < b) = P(X > b).
:::

:::guess Guess first
If both sides are equal and they add to 1, what must each be?
:::

:::note Terms
**Median b:** the value with half the probability below it and half above, P(X < b) = P(X > b) = ½, i.e. **F(b) = ½**.
:::

1. P(X < b) + P(X > b) = 1 (P(X = b) = 0), and the two are equal, so each is ½.
2. F(b) = ½: 3b² − 2b³ = ½.
3. Multiply by 2 and move everything to one side: 4b³ − 6b² + 1 = 0.
4. b = ½ is a root: 4/8 − 6/4 + 1 = 0.5 − 1.5 + 1 = 0 ✓. Factor it out: 4b³ − 6b² + 1 = (2b − 1)(2b² − 2b − 1).
5. The other roots, from 2b² − 2b − 1 = 0: b = (1 ± √3)/2 = 1.366 or −0.366. Both lie outside 0 ≤ x ≤ 1, where X never is, so reject them.

**Answer.** **b = ½** (0.5): the median diameter, as the symmetry already said.

:::check Check 4
f(x) = 2x for 0 ≤ x ≤ 1 (Check 3). Find the median b.
:::

### 5 · A tail area: "more than" with a curve that never ends

Some measurements have no upper end: power use can, in principle, be any positive amount. "More than c" is then the area from c out to infinity.

:::q <span class="tag">A1 SA 2</span>
Daily power consumption X (million kWh) has pdf f(x) = (1/9) x e^{−x/3}, x > 0. The plant's daily capacity is 12. Find the probability that the supply is inadequate on a given day.
:::

:::guess Guess first
"Inadequate" means which event about X? Will the answer be large or small?
:::

:::note Terms
**Tail area:** the area beyond a cut-off, here P(X > 12) = ∫ from 12 to ∞ of f. The **e^{−x/3}** factor makes the curve die away for large x, so this area is finite.
:::

[[fig:power_tail|What this graph plots: the PDF of daily power use, f(x) = (1/9) x e^(−x/3). It rises to a peak at x = 3, then falls away. Red: the area beyond x = 12, the days demand exceeds capacity.|w=66]]

**Reading the figure.**

| x | 3 | 12 | 20 |
|---|---|---|---|
| f(x) | 0.1226 | 0.0244 | 0.0028 |
| meaning | the peak: the most common use | the capacity line; few days reach it | almost no days |

Inadequate supply means **X > 12**. The integral needs integration by parts (∫ u dv = uv − ∫ v du):

1. Take u = x, dv = e^{−x/3} dx; then du = dx, v = −3e^{−x/3}.
2. ∫ x e^{−x/3} dx = −3x e^{−x/3} + 3 ∫ e^{−x/3} dx = −3x e^{−x/3} − 9e^{−x/3}.
3. As x → ∞ both terms go to 0 (the exponential wins over x).
4. At x = 12: −36e^{−4} − 9e^{−4} = −45e^{−4}.
5. ∫ from 12 to ∞ = 0 − (−45e^{−4}) = 45e^{−4}; times 1/9 gives **5e^{−4}**.

$$P(X > 12) = \frac{1}{9} × 45e^{−4} = 5e^{−4} = 5 × 0.018316 = 0.0916$$

The same steps from 0 give total area (1/9)(0 − (−9)) = 1 ✓, so f is a pdf.

**Answer.** P(supply inadequate) = 5e^{−4} = **0.0916**: about 1 day in 11. (The key's 0.0915 is the same value cut off, not rounded: 0.09158.)

:::check Check 5
f(x) = k e^{−2x} for x ≥ 0. (a) Find k. (b) Find P(X > 1).
:::

### 6 · Conditional probability with a PDF

01 step 7's rule, P(A | B) = P(A∩B)/P(B), works unchanged; each probability is now an area.

:::q <span class="tag">A1 LA 1</span>
f(t) = 3 × 10^{−9} t²(100 − t)² for 0 ≤ t ≤ 100 gives the age at death T. Find (i) P(death between 60 and 70); (ii) the same, given that the person lived to 60.
:::

:::guess Guess first
Will (ii) be larger or smaller than (i)? One line on why.
:::

[[fig:life_cond|What this graph plots: the PDF of age at death, f(t) = 3 × 10⁻⁹ t²(100 − t)². Dark: the area from 60 to 70, P(60 ≤ T ≤ 70) = 0.1544. Light + dark: all of T ≥ 60, area 0.3174. Given survival to 60, only the light + dark region is left, so the dark share grows.|w=66]]

**Reading the figure.**

| t | 50 | 60 | 70 |
|---|---|---|---|
| f(t) | 0.01875 | 0.01728 | 0.01323 |
| meaning | the peak: deaths most crowded near 50 | slightly fewer | fewer still |

The CDF first (step 3):

1. Expand: t²(100 − t)² = 10000t² − 200t³ + t⁴.
2. Integrate from 0 to t: 10000t³/3 − 50t⁴ + t⁵/5.
3. Multiply by 3 × 10^{−9}: F(t) = 10^{−5}t³ − 1.5 × 10^{−7}t⁴ + 6 × 10^{−10}t⁵. Check F(100) = 10 − 15 + 6 = 1 ✓.
4. F(70) = 3.43 − 3.6015 + 1.00842 = 0.83692.
5. F(60) = 2.16 − 1.944 + 0.46656 = 0.68256.

Then the two answers:

- (i) P(60 ≤ T ≤ 70) = F(70) − F(60) = 0.83692 − 0.68256 = **0.1544**.
- (ii) A = {60 ≤ T ≤ 70}, B = {T ≥ 60}. A lies inside B, so A∩B = A (01 step 8). P(B) = 1 − F(60) = 0.31744. P(A | B) = 0.15436/0.31744 = **0.4863**.

**Answer.** (i) **0.1544**; (ii) **0.4863**. Larger, because the people who died before 60 are removed from the denominator: the "given" shrinks the area we divide by, as the grid shrank in 01 step 7.

:::check Check 6
Cable: find P(X > 0.75 | X > 0.5).
:::

---

## Exam form

**Definitions (one line each).** Continuous X: any value in an interval (measurements) · PDF f(x): a density whose area over an interval is the probability of that interval · CDF F(x) = P(X ≤ x) = area under f to the left of x · median b: F(b) = ½.

| | Discrete X (02a) | Continuous X (02b) |
|---|---|---|
| Values | listable (counts) | an interval (measurements) |
| Function | PMF p(x) = P(X = x) | PDF f(x), a density |
| Valid if | p(x) ≥ 0, Σ p(x) = 1 | f(x) ≥ 0, ∫ f(x) dx = 1 |
| P(a ≤ X ≤ b) | Σ p(x) over a ≤ x ≤ b | ∫ₐᵇ f(x) dx = F(b) − F(a) |
| P(X = a) | p(a) | 0 |
| CDF | running sum (staircase) | area to the left (smooth); f = F′ |

**Procedure: show f is a pdf.** (1) f(x) ≥ 0 on its range; (2) total area = 1. State both.

**Procedure: median.** Write F(x); set F(b) = ½; solve; keep only the root inside the range of X.

**Procedure: P(X > c) with no upper end.** Integrate from c to ∞ (by parts for x e^{−x/k}); the terms at ∞ vanish.

## Traps

- Reading f(x) as a probability. A density can exceed 1 (cable: f(0.5) = 1.5); only areas are probabilities.
- Giving P(X = a) a non-zero value for a continuous X.
- Forgetting the "0 elsewhere" pieces of F: F = 0 left of the range, 1 right of it.
- Keeping a median root that lies outside the range of X.
- In SA 2, writing "inadequate" as X < 12 (that is the adequate side).
- In a conditional, dividing by 1 instead of by P(given event), or forgetting that A∩B = A when A lies inside B.

## Self-test

1. Why can f(0.5) = 1.5 for a PDF, but never P(X = 0.5) = 1.5?
2. f(x) = kx(2 − x) for 0 ≤ x ≤ 2. Find k.
3. f(x) = 3x² for 0 ≤ x ≤ 1. Find F(x) and P(0.5 < X ≤ 1).
4. For the f of question 3, find the median.
5. f(x) = (1/4) e^{−x/4} for x > 0. Find P(X > 4).
6. f(x) = x e^{−x} for x > 0. Find P(X > 1).
7. Cable: find P(X < 0.2 | X < 0.5).

<!--ANSWERS-->
## Answers

**Check 1.** (a) **0**: a single point has no area. (b) F(0.8) − F(0.5) = 0.896 − 0.5 = **0.396**, the same as P(0.2 ≤ X ≤ 0.5): the hump is symmetric about 0.5, so mirror intervals have equal areas.

**Check 2.** (a) k · 3³/3 = 9k = 1, **k = 1/9**. (b) (2³ − 1³)/27 = **7/27** ≈ 0.2593.

**Check 3.** (a) F(x) = ∫₀ˣ 2t dt = **x²**. (b) 1 − F(0.5) = 1 − 0.25 = **0.75**.

**Check 4.** b² = ½, **b = 1/√2 ≈ 0.7071** (the root −0.7071 lies outside the range).

**Check 5.** (a) ∫ from 0 to ∞ of k e^{−2x} dx = k/2 = 1, **k = 2**. (b) ∫ from 1 to ∞ of 2e^{−2x} dx = e^{−2} = **0.1353**.

**Check 6.** P(X > 0.5) = ½. P(X > 0.75) = 1 − F(0.75) = 1 − (3 × 0.5625 − 2 × 0.421875) = 1 − 0.84375 = 0.15625. {X > 0.75} lies inside {X > 0.5}, so the ratio is 0.15625/0.5 = **0.3125**.

**Self-test.**

1. f is a density: its height says how crowded values are near 0.5. A probability is an area, and a point has zero width, so P(X = 0.5) = 0; any probability is at most 1.
2. ∫₀² (2x − x²) dx = 4 − 8/3 = 4/3, so k × 4/3 = 1, **k = 3/4**.
3. F(x) = **x³** on 0 ≤ x ≤ 1 (0 before, 1 after). P(0.5 < X ≤ 1) = 1 − 0.125 = **0.875**.
4. b³ = ½, **b = 0.7937**.
5. ∫ from 4 to ∞ of (1/4) e^{−x/4} dx = e^{−1} = **0.3679**.
6. By parts: ∫ x e^{−x} dx = −x e^{−x} − e^{−x}. From 1 to ∞: 0 − (−e^{−1} − e^{−1}) = 2e^{−1} = **0.7358**.
7. {X < 0.2} lies inside {X < 0.5}: F(0.2)/F(0.5) = 0.104/0.5 = **0.208**.
<!--/ANSWERS-->
