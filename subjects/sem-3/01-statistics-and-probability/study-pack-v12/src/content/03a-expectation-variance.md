# 03a — Expectation and variance: the centre and the spread

<div class="sub">Gupta & Kapoor ch. 6 (§6.1–6.2) · blueprint row 1 "mathematical expectation and variance" · 4 real questions (MTE B2; Assignment 1 App 1, App 3, MCQ 4) · needs 02a (PMF step 4, reading a table step 8), 02b (PDF as area step 1, total area step 2)</div>

## Map

[[map:1 The long-run average > 2 The balance point > 3 The average of a function > 4 Variance: squared distance > 5 The shortcut formula > 6 Standard deviation > 7 A continuous X|here=1]]

02a and 02b gave a random variable a full table (or curve) of probabilities. A table is a lot to carry. This file boils it down to **two numbers**: where the values sit on average (the **expectation**), and how far they typically stray from that average (the **variance**, and its square root, the **standard deviation**). 03b then gives rules that combine these numbers without redoing the sums, and Chebyshev's inequality, which turns them into a guaranteed probability.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| X | a random variable: here, the number of defective sensors in one batch | 0, 1, 2 or 3 |
| p(x) | the PMF, as in 02a: P(X = x) | p(1) = 0.40 |
| E(X) or μ | the expectation (mean): the long-run average of X over many repeats | μ = 1.2 |
| E(X²) | the long-run average of X squared | 2.3 |
| Var(X) or σ² | the variance: the long-run average of (X − μ)², the squared distance from the mean | 0.86 |
| σ | the standard deviation: √Var(X), a typical distance from the mean, in X's own units | 0.927 |

**Running example.** A factory checks batches of sensors. X = number of defective sensors in a batch, with PMF (A1 App 1):

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| p(x) | 0.25 | 0.40 | 0.25 | 0.10 |

Steps 1–6 use it; the battery-life table of A1 App 3 is the second example.

## The questions this file answers

- <span class="tag">A1 App 1</span> The number of defective sensors X in a batch has P(X = 0, 1, 2, 3) = 0.25, 0.40, 0.25, 0.10. Verify it is a valid PMF; find the mean and variance and interpret them.
- <span class="tag">A1 App 3</span> The battery life X (years) is 2, 3, 4, 5 with probabilities 0.20, 0.30, 0.35, 0.15. Find the mean, variance and standard deviation, and interpret.
- <span class="tag">A1 MCQ 4</span> The expectation of a random variable represents: (a) the average value (b) the most likely value (c) the maximum value (d) the median.
- <span class="tag">MTE B2 · 4 marks</span> A continuous random variable X is distributed over (0, 1) with pdf f(x) = ax² + bx, where a and b are constants. If the mean of X is 0.5, find a and b.

---

## Build

### 1 · The long-run average

The table says what can happen in one batch. A manager wants one number: how many defectives to expect per batch.

:::q Predict
Imagine 100 batches that follow the table exactly: 25 have no defective, 40 have one, 25 have two, 10 have three. How many defective sensors are there in all 100 batches? How many per batch on average?
:::

:::guess Guess first
Write your two numbers before reading on.
:::

:::note Terms
**Expectation (mean) E(X)**, also written **μ** ("mu"): the average value of X over very many repeats of the experiment. It counts "how much X per repeat, in the long run". It is set entirely by the table: the values and their probabilities.
:::

Count the defectives in the 100 batches:

| x | batches (100 × p(x)) | defectives (x × batches) |
|---|---|---|
| 0 | 25 | 0 |
| 1 | 40 | 40 |
| 2 | 25 | 50 |
| 3 | 10 | 30 |
| total | 100 | **120** |

120 defectives over 100 batches is **1.2 per batch**. Dividing by 100 at the end is the same as multiplying each x by its probability at the start, which gives the formula:

$$E(X) = Σ x · p(x)$$

Read it as: "multiply each value by its probability, then add". For the sensors: 0(0.25) + 1(0.40) + 2(0.25) + 3(0.10) = 0 + 0.40 + 0.50 + 0.30 = **1.2**.

**Answer to the Predict.** **120** defectives in all, **1.2** per batch. That is E(X).

<span class="tag">A1 App 1</span> The PMF is valid (02a step 4): every p(x) ≥ 0 and 0.25 + 0.40 + 0.25 + 0.10 = 1. Mean **E(X) = 1.2** defective sensors per batch.

:::check Check 1
A fair die: X = 1, 2, …, 6, each with probability 1/6. Find E(X).
:::

### 2 · The balance point

E(X) = 1.2, yet no batch has 1.2 defective sensors. So what is this number, on the picture of the PMF?

:::q <span class="tag">A1 App 3</span>
The battery life X (years) of a device is 2, 3, 4, 5 with probabilities 0.20, 0.30, 0.35, 0.15. Find the mean battery life. Can a battery last exactly that long according to this table?
:::

:::guess Guess first
Without calculating: is the mean nearer 3 or nearer 4?
:::

[[fig:sens_balance|What this graph plots: the sensors' PMF as bars standing on a beam. Horizontal axis: x, the number of defectives. Bar height: p(x). Red triangle: the point where the beam balances, x = 1.2.|w=62]]

**Reading the figure.**

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| bar (weight) | 0.25 | 0.40 | 0.25 | 0.10 |
| distance from 1.2 | 1.2 left | 0.2 left | 0.8 right | 1.8 right |
| weight × distance | 0.30 left | 0.08 left | 0.20 right | 0.18 right |

Left side: 0.30 + 0.08 = 0.38. Right side: 0.20 + 0.18 = 0.38. Equal, so the beam balances at 1.2. **E(X) is the balance point of the bars.** A heavy bar pulls it towards itself; it need not sit on a bar.

**Answer.**

1. E(X) = 2(0.20) + 3(0.30) + 4(0.35) + 5(0.15).
2. = 0.40 + 0.90 + 1.40 + 0.75 = **3.45 years**.

No battery lasts exactly 3.45 years in this table (lives are 2, 3, 4 or 5): the mean is the balance point, not a possible value. It sits nearer 3 than 4 because the bars at 2 and 3 together (0.50) outweigh the bar at 5.

<span class="tag">A1 MCQ 4</span> The expectation represents the **average value**: (a). Not the most likely value (the sensors' most likely value is 1, the mean is 1.2).

:::check Check 2
X = 0 with probability 0.7 and X = 1 with probability 0.3 (one sensor: good or defective). Find E(X). Is it a value X can take?
:::

### 3 · The average of a function of X

The variance (next step) needs the average of X², not of X. Is that just (average of X)²?

:::q Predict
For the sensors, E(X) = 1.2, so [E(X)]² = 1.44. Predict E(X²), the long-run average of X². Bigger than 1.44, equal, or smaller?
:::

:::guess Guess first
Squaring stretches the big values (3² = 9) more than the small ones (1² = 1). Which way does that push the average?
:::

:::note Terms
**E(X²):** the long-run average of the **squares** of X. Same recipe as E(X): square each value, weight by its probability, add. More generally, **E(g(X)) = Σ g(x) p(x)** for any function g: transform the values, keep the probabilities.
:::

$$E(X^{2}) = Σ x^{2} · p(x)$$

| x | 0 | 1 | 2 | 3 | total |
|---|---|---|---|---|---|
| x² | 0 | 1 | 4 | 9 | |
| p(x) | 0.25 | 0.40 | 0.25 | 0.10 | 1 |
| x² p(x) | 0 | 0.40 | 1.00 | 0.90 | **2.3** |

**Answer to the Predict.** E(X²) = **2.3**, bigger than [E(X)]² = 1.44. In general **E(X²) ≠ [E(X)]²**: the average of the squares is not the square of the average. The gap between them (2.3 − 1.44 = 0.86) is the variance, as step 5 shows.

:::check Check 3
Battery table (step 2): find E(X²).
:::

### 4 · Variance: the average squared distance from the mean

Two tables can share a mean and still differ: values packed close to μ, or scattered far from it. One number should measure that spread.

:::q Predict
Sensors: μ = 1.2. Value 3 lies 1.8 above the mean; value 0 lies 1.2 below. If you just averaged the signed distances (x − μ), weighting by p(x), what would you get? Why is that useless as a spread measure?
:::

:::guess Guess first
Think of step 2's beam: what do the left and right pulls do?
:::

:::note Terms
**Deviation x − μ:** how far a value is from the mean, with a sign. **Variance Var(X)**, also written **σ²** ("sigma squared"): the long-run average of the **squared** deviation, E[(X − μ)²]. Squaring makes every distance positive and weights far values heavily. Its units are X's units squared (defectives²).
:::

$$Var(X) = E[(X − μ)^{2}] = Σ (x − μ)^{2} · p(x)$$

[[fig:sens_sqdist|What this graph plots: for each sensor value x, the squared distance (x − 1.2)² from the mean. Horizontal axis: x. Bar height: (x − 1.2)². Dashed line: the mean 1.2.|w=62]]

**Reading the figure, and the sum.**

| x | 0 | 1 | 2 | 3 | total |
|---|---|---|---|---|---|
| x − 1.2 | −1.2 | −0.2 | 0.8 | 1.8 | |
| (x − 1.2)² | 1.44 | 0.04 | 0.64 | 3.24 | |
| p(x) | 0.25 | 0.40 | 0.25 | 0.10 | |
| (x − 1.2)² p(x) | 0.36 | 0.016 | 0.16 | 0.324 | **0.86** |

The value 3 is rare (0.10), but its squared distance 3.24 is so large that it adds 0.324, more than a third of the total.

**Answer to the Predict.** The signed deviations average to **0** (step 2: the left and right pulls cancel), for every table. That is why the deviations are **squared** first. Var(X) = **0.86** defectives².

:::check Check 4
Two tables, both with mean 5: A takes 4, 5, 6 and B takes 0, 5, 10, each value with probability 1/3. Find Var for each from the definition. Which is more spread?
:::

### 5 · The shortcut: Var(X) = E(X²) − μ²

The definition needs every deviation. Exam answers use a shortcut that needs only the two averages already found.

:::q <span class="tag">A1 App 3 (cont.)</span>
For the battery table (E(X) = 3.45), find the variance.
:::

:::guess Guess first
Step 3 found E(X²) = 2.3 for the sensors, and step 4 found Var = 0.86. What did 2.3 − 1.2² give?
:::

$$Var(X) = E(X^{2}) − [E(X)]^{2}$$

Read it as: "the average of the squares minus the square of the average". Why it holds (expand the square; μ is a constant):

1. (X − μ)² = X² − 2μX + μ².
2. Average each term: E(X²) − 2μ E(X) + μ².
3. E(X) = μ, so this is E(X²) − 2μ² + μ² = **E(X²) − μ²**.

Sensors: 2.3 − 1.2² = 2.3 − 1.44 = **0.86**, the same as step 4's table.

**Answer.**

1. E(X²) = 4(0.20) + 9(0.30) + 16(0.35) + 25(0.15) = 0.80 + 2.70 + 5.60 + 3.75 = 12.85.
2. Var(X) = 12.85 − 3.45² = 12.85 − 11.9025 = **0.9475 ≈ 0.95** years².

:::check Check 5
Fair die: E(X) = 3.5. Find E(X²) and Var(X).
:::

### 6 · Standard deviation: spread in the original units

0.9475 "years squared" is hard to picture. Taking the square root brings the spread back to years.

:::q <span class="tag">A1 App 3 (cont.)</span>
Find the standard deviation of the battery life, and say in one sentence what the mean and SD tell a buyer.
:::

:::guess Guess first
Variance 0.9475: is the SD a little under 1 year, or about half a year?
:::

:::note Terms
**Standard deviation σ** = √Var(X): a typical distance of X from its mean, in X's own units (years, defectives). Small σ: values huddle near μ. Large σ: values scatter.
:::

**Answer.** σ = √0.9475 = **0.973 years**. Interpretation: a battery lasts **3.45 years on average, typically give or take about 1 year**.

:::note Key rounding
Assignment 1's key prints SD ≈ 0.98: that is √0.95, the variance rounded before the root. From the unrounded variance, σ = 0.973 ≈ 0.97. Round only at the last step.
:::

<span class="tag">A1 App 1 (interpretation)</span> Sensors: μ = 1.2, σ² = 0.86, σ = √0.86 = **0.927**. A batch has about 1.2 defectives on average, typically give or take about 1.

:::check Check 6
Fair die (Check 5): find σ to three decimals.
:::

### 7 · Expectation and variance for a continuous X

02b replaced bars with a curve and sums with areas. The same swap gives E and Var for a continuous X.

:::q <span class="tag">MTE B2 · 4 marks</span>
A continuous random variable X is distributed over (0, 1) with pdf f(x) = ax² + bx, where a, b are constants. If the mean of X is 0.5, find a and b.
:::

:::guess Guess first
Two unknowns need two equations. Which two facts about f give them?
:::

| | Discrete (steps 1–5) | Continuous (here) |
|---|---|---|
| E(X) | Σ x p(x) | ∫ x f(x) dx |
| E(X²) | Σ x² p(x) | ∫ x² f(x) dx |
| Var(X) | E(X²) − μ² | E(X²) − μ² (unchanged) |

The integrals run over the range of X. The balance-point picture still holds: E(X) is where the area under f would balance.

[[fig:cable_balance|What this graph plots: the PDF f(x) = 6x − 6x² on 0 to 1 (02b's cable). Horizontal axis: x. Height: f(x). Red triangle: the balance point E(X) = 0.5. The hump is symmetric, so it balances at its centre.|w=62]]

**Reading the figure.**

| x | 0.2 | 0.5 | 0.8 |
|---|---|---|---|
| f(x) | 0.96 | 1.5 | 0.96 |
| meaning | mirror of 0.8 | the peak and the balance point | mirror of 0.2 |

**Answer.**

1. *Total area = 1* (02b step 2): ∫₀¹ (ax² + bx) dx = a/3 + b/2 = 1. Multiply by 6: **2a + 3b = 6**.
2. *Mean = 0.5:* ∫₀¹ x(ax² + bx) dx = ∫₀¹ (ax³ + bx²) dx = a/4 + b/3 = ½. Multiply by 12: **3a + 4b = 6**.
3. Multiply equation 1 by 3 and equation 2 by 2: 6a + 9b = 18 and 6a + 8b = 12. Subtract: **b = 6**.
4. Then 2a = 6 − 3(6) = −12, so **a = −6**.
5. f(x) = −6x² + 6x = 6x(1 − x): 02b's cable PDF, symmetric about 0.5, so a mean of 0.5 is right ✓.

:::check Check 7
For f(x) = 6x(1 − x) on (0, 1): find E(X²), Var(X) and σ.
:::

---

## Exam form

**Definitions (one line each).** E(X) = Σ x p(x) or ∫ x f(x) dx: the long-run average, the balance point · E(g(X)) = Σ g(x) p(x) or ∫ g(x) f(x) dx · Var(X) = E[(X − μ)²], the average squared distance from μ · σ = √Var(X), in X's units.

**Working formula.** Var(X) = E(X²) − [E(X)]².

**Procedure: mean, variance, SD from a table.**

1. Check the PMF: all p(x) ≥ 0, Σ p(x) = 1.
2. μ = Σ x p(x).
3. E(X²) = Σ x² p(x) (a column x² p(x) in the table).
4. Var = E(X²) − μ²; σ = √Var. Round only at the end.
5. Interpret: "on average μ, typically give or take σ" (with units).

**Procedure: unknown constants in a PDF.** One equation per unknown: total area = 1, plus each given fact (mean, a probability).

## Traps

- Reading E(X) as a value X must take, or as the most likely value.
- Writing E(X²) = [E(X)]². The average of the squares is bigger (unless X never varies).
- Var = E(X²) − E(X) (forgot to square the mean).
- Rounding the variance before taking the root (the A1 App 3 key: 0.98 instead of 0.97).
- Giving σ² in the original units: variance is in units², σ is in units.
- In MTE B2, using only "mean = 0.5": total area = 1 is the second equation.

## Self-test

1. X = 0, 1, 2 with P = 0.3, 0.4, 0.3. Find E(X), E(X²), Var(X), σ.
2. X = 1, 2, 3 with P = 0.5, 0.3, 0.2. Find E(X) and Var(X).
3. Why must the deviations be squared before averaging?
4. f(x) = 2x on (0, 1). Find E(X) and Var(X).
5. f(x) = kx on (0, 2). Find k, then E(X).
6. Two tables have the same mean; table A has σ = 0.5, table B has σ = 3. Describe the difference in one sentence.
7. f(x) = a + bx on (0, 1) with mean 0.6. Find a and b.

<!--ANSWERS-->
## Answers

**Check 1.** (1 + 2 + 3 + 4 + 5 + 6)/6 = 21/6 = **3.5**.

**Check 2.** E(X) = 0(0.7) + 1(0.3) = **0.3**. Not a possible value: X is 0 or 1. It is the long-run share of defective sensors.

**Check 3.** 4(0.20) + 9(0.30) + 16(0.35) + 25(0.15) = **12.85**.

**Check 4.** A: (1 + 0 + 1)/3 = **2/3**. B: (25 + 0 + 25)/3 = **50/3 ≈ 16.67**. B is more spread.

**Check 5.** E(X²) = (1 + 4 + 9 + 16 + 25 + 36)/6 = 91/6 ≈ 15.17. Var = 91/6 − 12.25 = **35/12 ≈ 2.917**.

**Check 6.** σ = √(35/12) = **1.708**.

**Check 7.** E(X²) = ∫₀¹ 6x³(1 − x) dx = 6(¼ − ⅕) = **0.3**. Var = 0.3 − 0.5² = **0.05**. σ = √0.05 = **0.224**.

**Self-test.**

1. E = 0.4 + 0.6 = **1**; E(X²) = 0.4 + 1.2 = **1.6**; Var = 1.6 − 1 = **0.6**; σ = **0.775**.
2. E = 0.5 + 0.6 + 0.6 = **1.7**; E(X²) = 0.5 + 1.2 + 1.8 = 3.5; Var = 3.5 − 2.89 = **0.61**.
3. Signed deviations always average to 0 (the balance point), so they cannot measure spread; squares are all positive.
4. E = ∫₀¹ 2x² dx = **2/3**; E(X²) = ∫₀¹ 2x³ dx = ½; Var = ½ − 4/9 = **1/18 ≈ 0.0556**.
5. Area: k × 2²/2 = 2k = 1, **k = ½**. E = ∫₀² x²/2 dx = 8/6 = **4/3**.
6. Both centre on the same value, but B's values typically lie about 3 from it, A's only about 0.5.
7. Area: a + b/2 = 1. Mean: a/2 + b/3 = 0.6. From the first, a = 1 − b/2; then ½ − b/4 + b/3 = 0.6, b/12 = 0.1, **b = 1.2**, **a = 0.4**.
<!--/ANSWERS-->
