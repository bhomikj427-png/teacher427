# 06 — The normal distribution

<div class="sub">Gupta & Kapoor ch. 8 (§8.2) · blueprint row 2 "normal" · 9 real questions (MTE, Assignment 2) · needs 02b, 03, 04a (binomial)</div>

## Map

[[map:1 The curve and its two parameters > 2 Standardise, then read the table > 3 Tails and expected counts > 4 Normal inside a binomial > 5 From percentages back to μ and σ > 6 A two-condition inverse problem|here=1]]

## The questions this file answers

- <span class="tag">MTE C1(a) · 4 marks</span> Marks are normal with mean 65 and SD 5. If 3 students are selected at random, P(at least one scored above 75)? (Area from Z = 0 to Z = 2 is 0.4772.)
- <span class="tag">A2 B3</span> μ = 50, σ = 10: P(45 < X < 62). (φ(0.5) = 0.1915, φ(1.2) = 0.3849.)
- <span class="tag">A2 B4</span> 5000 batteries, life normal with mean 1500 h, SD 100 h: how many last more than 1660 h, less than 1380 h, between 1350 and 1680 h?
- <span class="tag">A2 D1</span> Bulb life normal, mean 3000 h, SD 400 h: of 10,000 bulbs, how many last between 2500 and 3500 h?
- <span class="tag">A2 B6</span> 10% of items are under 30 and 85% under 65: find the mean and SD.
- <span class="tag">A2 C2</span> 46% pass (40 marks) and 9% get distinction (75 marks): estimate the mean and SD; find the re-examination mark for the best 25% of failures.
- <span class="tag">A2 MCQ 1, 6, 11</span> Centre of symmetry; variance of the standard normal; area between z = −1 and 1.

---

## Build

### 1 · The curve and its two parameters

Files 04–05 each had a story. The normal's story is "many small independent effects added together" (file 07 explains why).

:::q <span class="tag">A2 MCQ 11 · 1 mark</span>
For a standard normal curve, what is the approximate area between z = −1 and z = 1? (a) 95.45% (b) 99.73% (c) 50.00% (d) 68.27%
:::

:::guess Guess first
Pick an option before looking at the figure.
:::

**Term.** **Normal X ~ N(μ, σ^{2})** (G&K §8.2): a bell-shaped density

$$f(x) = \frac{1}{σ√(2π)} e^{−(x − μ)²/(2σ²)},  −∞ < x < ∞;    E(X) = μ,  Var(X) = σ^{2}$$

μ sets the centre, σ the width. The curve is symmetric about μ, so mean = median = mode, and half the area lies on each side.

[[fig:normal_rule|The same three percentages hold for every normal curve.|w=78]]

**Answer.** **68.27%** (d). <span class="tag">A2 MCQ 1</span> The curve is symmetric about the **mean** (c). <span class="tag">A2 MCQ 6</span> The standard normal has variance **1** (a).

:::check Check 1
X ~ N(100, 15^{2}). Without a table, what percentage of values lie between 70 and 130?
:::

### 2 · Standardise, then read the table

There are infinitely many normal curves but only one table. Standardising moves any of them onto it.

:::q <span class="tag">A2 B3</span>
Given a normal distribution with mean μ = 50 and standard deviation σ = 10, find the probability that X lies between 45 and 62. (Given φ(0.5) = 0.1915 and φ(1.2) = 0.3849.)
:::

:::guess Guess first
45 and 62 are how many SDs from 50, and on which sides?
:::

**Terms.**

- **Standard normal Z**: N(0, 1).
- **Standardising**: Z = (X − μ)/σ counts how many SDs X is from the mean.
- **φ(z)** in these questions = area from 0 to z under the standard curve (the table the professor gives).

**Using the 0-to-z table.** Symmetry gives everything else:

| Wanted | Area |
|---|---|
| P(0 < Z < z) | φ(z) |
| P(Z > z), z > 0 | 0.5 − φ(z) |
| P(−z₁ < Z < z₂) | φ(z₁) + φ(z₂) |
| P(z₁ < Z < z₂), both positive | φ(z₂) − φ(z₁) |

**Answer.** z₁ = (45 − 50)/10 = −0.5, z₂ = (62 − 50)/10 = 1.2. Opposite sides of 0, so add: P = 0.1915 + 0.3849 = **0.5764**.

:::check Check 2
Same X. Find P(X > 62) and P(55 < X < 62).
:::

### 3 · Tails and expected counts

"How many items" = N × probability.

:::q <span class="tag">A2 B4</span>
In a quality test on 5000 lithium-ion batteries, life was normal with mean 1500 h and SD 100 h. Estimate how many last (i) more than 1660 h (ii) less than 1380 h (iii) more than 1350 h but less than 1680 h. Given φ(1.2) = 0.3849, φ(1.5) = 0.4332, φ(1.6) = 0.4452, φ(1.8) = 0.4641.
:::

:::guess Guess first
For (i): about what percentage of batteries are more than 1.6 SD above the mean?
:::

**Answer.**
(i) z = (1660 − 1500)/100 = 1.6: P = 0.5 − 0.4452 = 0.0548; 5000 × 0.0548 = **274**.
(ii) z = (1380 − 1500)/100 = −1.2: P = 0.5 − 0.3849 = 0.1151; 5000 × 0.1151 = 575.5 ≈ **576**.
(iii) z = −1.5 and 1.8: P = 0.4332 + 0.4641 = 0.8973; 5000 × 0.8973 = 4486.5 ≈ **4487**.

:::check Check 3
<span class="tag">A2 D1</span> Bulb life is normal with mean 3000 h and SD 400 h. Of 10,000 bulbs, how many last between 2500 and 3500 hours? (φ(1.25) = 0.3944.)
:::

### 4 · A normal probability inside a binomial

The 4-mark MTE question chains two files: a normal probability for one student, then file 04a's binomial for three.

:::q <span class="tag">MTE C1(a) · 4 marks</span>
The marks obtained by students in a subject are approximately normally distributed with mean 65 and SD 5. If 3 students are selected at random from this group, what is the probability that at least one of them scored above 75? (Given: the area between Z = 0 and Z = 2 under the standard normal curve is 0.4772.)
:::

:::guess Guess first
P(one student > 75) is small. Is P(at least one of three) roughly three times it?
:::

[[fig:normal_std|Standardising moves the red tail onto the Z table.|w=92]]

**Answer.** *One student:* z = (75 − 65)/5 = 2. p = P(X > 75) = P(Z > 2) = 0.5 − 0.4772 = **0.0228**.
*Three students:* Y = number above 75, Y ~ B(3, 0.0228), q = 0.9772.
P(Y ≥ 1) = 1 − P(Y = 0) = 1 − (0.9772)^{3} = 1 − 0.93315 = **0.0668**. (≈ 3 × 0.0228 = 0.0684, as guessed, slightly less.)

:::note Marking scheme
The professor's scheme splits this as: z-value and P(X > 75) = 0.0228, then the binomial set-up and 1 − q^{3}. Its final 0.0667 is the same value with (0.9772)^{3} rounded differently.
:::

:::check Check 4
Same class. Five students are chosen. Find P(none scored above 75).
:::

### 5 · From percentages back to μ and σ

Inverse questions give areas and ask for parameters: read the table backwards.

:::q <span class="tag">A2 B6</span>
In a distribution exactly normal, 10% of the items are under 30 and 85% are under 65. What are the mean and standard deviation? Given φ(1.04) = 0.35 and φ(1.28) = 0.4.
:::

:::guess Guess first
Is the mean nearer 30 or 65? (Which side has the smaller tail?)
:::

**Method.** (1) Sketch; mark each given value left or right of μ. (2) Turn each percentage into an area from 0 to z. (3) Write (x − μ)/σ = ±z for each. (4) Solve the two equations.

[[fig:normal_inverse|10% below 30 puts 30 left of μ; 15% above 65 puts 65 right of μ.|w=78]]

**Answer.** Below 30 is 10%: area from 30 to μ = 0.4, so z = −1.28: (30 − μ)/σ = −1.28.
Below 65 is 85%: area from μ to 65 = 0.35, so z = 1.04: (65 − μ)/σ = 1.04.
Subtract: 35/σ = 2.32 ⇒ **σ = 15.09**; μ = 30 + 1.28 × 15.09 = **49.31**.

:::check Check 5
A normal variable has 31% of values below 45 and 8% above 64. Find μ and σ. (φ(0.5) = 0.19, φ(1.4) = 0.42.)
:::

### 6 · A two-condition inverse problem

The 8-mark version adds a second question about the fitted curve.

:::q <span class="tag">A2 C2</span>
In an examination, 46% of candidates passed and 9% got distinctions; the minimum pass and distinction marks are 40 and 75. Assume marks are normal. Estimate the average mark and the SD. Also find the minimum qualifying mark for re-examination of failed candidates, if the best 25% of them are given another chance. (φ(0.1) = 0.04, φ(1.34) = 0.41, φ(0.24) = 0.095.)
:::

:::guess Guess first
46% passed, so is 40 above or below the mean?
:::

**Answer.** P(X ≥ 40) = 0.46 < 0.5, so 40 is above μ: area from μ to 40 = 0.04, z = 0.1: (40 − μ)/σ = 0.1.
P(X ≥ 75) = 0.09: area from μ to 75 = 0.41, z = 1.34: (75 − μ)/σ = 1.34.
Subtract: 35/σ = 1.24 ⇒ **σ = 28.23**; μ = 40 − 0.1 × 28.23 = **37.18**.

*Re-examination.* Failed = 54% (marks below 40). Best 25% of them = 0.25 × 54% = 13.5% of all candidates, lying just below 40. So the qualifying mark x has P(X < x) = 0.54 − 0.135 = 0.405: x is below μ with area 0.5 − 0.405 = 0.095 between them, z = −0.24.
x = 37.18 − 0.24 × 28.23 = **30.40** marks.

:::note Key slip
Assignment 2's key prints μ = 37.5. The two equations give 37.18 (the key's own 30.43 needs μ ≈ 37.2, so 37.5 is a typo).
:::

:::check Check 6
With μ = 37.18 and σ = 28.23, what percentage of candidates score above 60? (φ(0.81) = 0.291.)
:::

---

## Exam form

**Statement.** X ~ N(μ, σ^{2}): f(x) = \frac{1}{σ√(2π)} e^{−(x − μ)²/(2σ²)}; mean μ, variance σ^{2}; symmetric about μ; mean = median = mode.

**Standardisation.** Z = (X − μ)/σ ~ N(0, 1).

**Procedure (forward).**

1. Write the event in X; convert each limit to z = (x − μ)/σ.
2. Sketch the curve; shade the area.
3. Use φ(z) (area 0 to z) with the symmetry table of step 2.
4. For counts: N × probability, rounded to a whole number.

**Procedure (inverse).** Sketch → place each value left/right of μ → area from μ → z from the table → (x − μ)/σ = ±z → solve.

**Areas to remember.** μ ± σ: 68.27% · μ ± 2σ: 95.45% · μ ± 3σ: 99.73% · φ(1.96) = 0.475 · φ(1.645) = 0.45 · φ(2.576) = 0.495.

## Traps

- Subtracting φ values when the limits are on **opposite** sides of μ (add them).
- Forgetting the 0.5 when finding a tail: P(Z > z) = 0.5 − φ(z).
- Dividing by σ^{2} instead of σ when standardising.
- In inverse questions, giving z the wrong sign: values below μ have negative z.
- Treating "at least one of 3" as 3p: use 1 − q^{3}.

## Self-test

1. Write the normal pdf and name its parameters.
2. X ~ N(60, 8^{2}). Find P(X > 72). (φ(1.5) = 0.4332.)
3. X ~ N(60, 8^{2}). Find P(52 < X < 68) without a table.
4. Heights are N(165, 6^{2}) cm. In a group of 1000, how many are taller than 177 cm? (φ(2) = 0.4772.)
5. The top 5% of a N(70, 10^{2}) exam get an A. Find the cut-off mark. (φ(1.645) = 0.45.)
6. Why does the normal table only need z ≥ 0?

<!--ANSWERS-->
## Answers

**Check 1.** 70 to 130 is μ ± 2σ: **95.45%**.

**Check 2.** P(X > 62) = 0.5 − 0.3849 = **0.1151**. z = 0.5 and 1.2, same side: 0.3849 − 0.1915 = **0.1934**.

**Check 3.** z = ±1.25: 2 × 0.3944 = 0.7888; 10,000 × 0.7888 = **7888 bulbs**.

**Check 4.** (0.9772)^{5} = **0.8911**.

**Check 5.** 45 below μ: area 0.19, z = −0.5. 64 above μ: area 0.42, z = 1.4. (64 − 45)/σ = 1.9 ⇒ σ = **10**, μ = 45 + 5 = **50**.

**Check 6.** z = (60 − 37.18)/28.23 = 0.81: 0.5 − 0.291 = 0.209, about **21%**.

**Self-test.**

1. f(x) = (1/(σ√(2π)))e^{−(x − μ)²/(2σ²)}; μ = mean, σ = SD.
2. z = 1.5: 0.5 − 0.4332 = **0.0668**.
3. μ ± σ: **0.6827**.
4. z = 2: 0.0228 × 1000 ≈ **23**.
5. Area 0.45 from μ: z = 1.645: 70 + 16.45 = **86.45**.
6. The curve is symmetric about 0, so the area from −z to 0 equals the area from 0 to z.
<!--/ANSWERS-->
