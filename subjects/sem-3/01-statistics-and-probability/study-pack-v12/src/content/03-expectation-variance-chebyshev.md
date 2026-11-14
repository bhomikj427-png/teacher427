# 03 — Expectation, variance and Chebyshev's inequality

<div class="sub">Gupta & Kapoor ch. 6 (§6.1–6.7, §6.13) · blueprint row 1 "mathematical expectation and variance, Chebyshev's inequality" · 13 real questions (MTE, Assignment 1) · needs 02</div>

## Map

[[map:1 Expectation > 2 Variance and SD > 3 Continuous X > 4 Rules for sums and constants > 5 Chebyshev's inequality > 6 Chebyshev on a given distribution|here=1]]

## The questions this file answers

- <span class="tag">MTE B1 · 3 marks</span> X takes −1, 1, 3, 5 with probabilities 1/6, 1/6, 1/6, 1/2. By Chebyshev's inequality find the upper bound of P(|X − 3| ≥ 1).
- <span class="tag">MTE B2 · 4 marks</span> f(x) = ax^{2} + bx on (0, 1), mean 0.5: find a and b.
- <span class="tag">MTE A1(a) · 2 marks</span> If X₁ and X₂ are independent, E(X₁X₂) = E(X₁)E(X₂): correct or not?
- <span class="tag">A1 App 1, 3</span> Sensors (0–3 defectives) and battery life (2–5 years): mean, variance, SD, interpretation.
- <span class="tag">A1 App 4</span> Marks with μ = 70, σ^{2} = 25: by Chebyshev, the minimum proportion between 60 and 80.
- <span class="tag">A1 SA 4–6</span> Expected tosses until a head · two dice, prove P(|X − 7| ≥ 3) ≤ 35/54 · 600 throws, lower bound for 80 to 120 sixes.
- <span class="tag">A1 LA 3</span> 25 items, 5 defective, sample of 4: expected number of defectives with and without replacement.
- <span class="tag">A1 MCQ 4, 5, 10</span> What expectation represents · which inequality bounds deviation from the mean · where Chebyshev applies.

---

## Build

### 1 · Expectation: the balance point

File 02 gave each value a probability. One number now summarises where the distribution sits.

:::q <span class="tag">A1 App 3</span>
Battery life X (years) = 2, 3, 4, 5 with P(X) = 0.20, 0.30, 0.35, 0.15. Find the mean battery life.
:::

:::guess Guess first
Without calculating: is the mean nearer 3 or nearer 4?
:::

**Term.** **Expectation (mean)** E(X) = μ (G&K §6.1):

$$E(X) = Σ x · p(x)  (discrete)        E(X) = ∫ x f(x) dx  (continuous)$$

Each value is weighted by how often it occurs. E(X) is the long-run average of many repetitions, and the point where the PMF bars would balance.

[[fig:balance|E(X) need not be a value X can take.|w=62]]

**Answer.** E(X) = 2(0.20) + 3(0.30) + 4(0.35) + 5(0.15) = 0.40 + 0.90 + 1.40 + 0.75 = **3.45 years**. <span class="tag">A1 MCQ 4</span>: expectation represents the **average value** (a).

**An infinite sum.** <span class="tag">A1 SA 4</span> A coin is tossed until a head appears. X = number of tosses: P(X = x) = (½)^{x}, x = 1, 2, … . E(X) = Σ x(½)^{x} = ½/(1 − ½)^{2} = **2** (using Σ x q^{x} = q/(1 − q)^{2}).

:::check Check 1
<span class="tag">A1 App 1</span> Defective sensors X = 0, 1, 2, 3 with P = 0.25, 0.40, 0.25, 0.10. Verify it is a PMF and find E(X).
:::

### 2 · Variance and standard deviation: the spread

Two distributions can share a mean and still differ in how far values stray from it.

:::q <span class="tag">A1 App 3 (cont.)</span>
For the battery data, find the variance and the standard deviation.
:::

:::guess Guess first
Values run from 2 to 5 around a mean of 3.45. Guess the SD to one decimal.
:::

**Terms.**

- **Variance** Var(X) = σ^{2} = E[(X − μ)^{2}]: the mean squared distance from μ.
- **Standard deviation** σ = √Var(X), in the same units as X.

The working formula (G&K §6.2):

$$Var(X) = E(X^{2}) − [E(X)]^{2},    E(X^{2}) = Σ x^{2} p(x)$$

**Answer.** E(X^{2}) = 4(0.20) + 9(0.30) + 16(0.35) + 25(0.15) = 0.80 + 2.70 + 5.60 + 3.75 = 12.85.
Var(X) = 12.85 − 3.45^{2} = 12.85 − 11.9025 = **0.9475 ≈ 0.95**. σ = √0.9475 = **0.973 years**.
Interpretation: a typical battery lasts 3.45 years, give or take about one year.

:::note Key rounding
The key prints SD ≈ 0.98: that is √0.95, the variance rounded first. From the unrounded variance the SD is 0.973 ≈ 0.97.
:::

:::check Check 2
<span class="tag">A1 App 1</span> For the sensors, find Var(X). (Key: 0.86.)
:::

### 3 · Expectation for a continuous X

The same two definitions, with Σ replaced by ∫. Here they are used to find unknown constants.

:::q <span class="tag">MTE B2 · 4 marks</span>
A continuous random variable X is distributed over (0, 1) with pdf f(x) = ax^{2} + bx, where a, b are constants. If the mean of X is 0.5, find a and b.
:::

:::guess Guess first
Two unknowns need two equations. Which two facts about f give them?
:::

**Answer.** *Equation 1, total area = 1:* ∫₀¹ (ax^{2} + bx) dx = a/3 + b/2 = 1 ⇒ **2a + 3b = 6**.
*Equation 2, mean = 0.5:* ∫₀¹ x(ax^{2} + bx) dx = a/4 + b/3 = ½ ⇒ **3a + 4b = 6**.
Solve: multiply the first by 3 and the second by 2: 6a + 9b = 18 and 6a + 8b = 12, so b = 6, then 2a = 6 − 18, **a = −6, b = 6**. f(x) = 6x − 6x^{2} = 6x(1 − x): the cable pdf of file 02, symmetric about 0.5 ✓.

:::check Check 3
For f(x) = 6x(1 − x) on (0, 1), find E(X^{2}) and Var(X).
:::

### 4 · Rules for constants and sums

Exam questions often combine random variables. These rules save integrating again.

:::q <span class="tag">MTE A1(a)</span>
If X₁ and X₂ are independent random variables, then E(X₁ · X₂) = E(X₁) · E(X₂). Correct or not?
:::

:::guess Guess first
Is E(X + Y) = E(X) + E(Y) always true? Is E(XY) = E(X)E(Y) always true? Write yes/no for each.
:::

**Rules** (G&K §6.3–6.7), a, b constants:

| Rule | Needs independence? |
|---|---|
| E(aX + b) = aE(X) + b | no |
| E(X + Y) = E(X) + E(Y) | **no**: always true |
| E(XY) = E(X)E(Y) | **yes** |
| Var(aX + b) = a^{2}Var(X) | no: adding b shifts, does not spread |
| Var(X ± Y) = Var(X) + Var(Y) | **yes**; note + for X − Y too |

**Answer.** **Correct** for independent X₁, X₂ (the multiplication theorem of expectation). So in MTE A1 the incorrect statement is (b), as found in file 02.

**Sums without counting every case.** <span class="tag">A1 LA 3</span> 25 items, 5 defective; sample 4. Let Xᵢ = 1 if the i-th item drawn is defective. Each draw, with or without replacement, has P(defective) = 5/25 = 0.2. By the sum rule E(X) = 4 × 0.2 = **0.8 in both cases**.

:::note Key slip
Assignment 1's key gives 0.808 for "without replacement". The sum rule needs no independence, so the expectation is 0.8 either way; only the variance changes.
:::

:::check Check 4
E(X) = 3, Var(X) = 4. Find E(2X − 5) and Var(2X − 5). If Y is independent of X with Var(Y) = 1, find Var(X − Y).
:::

### 5 · Chebyshev's inequality: a bound from μ and σ alone

The variance measures spread; Chebyshev turns it into a guaranteed probability, whatever the shape of the distribution.

:::q <span class="tag">A1 App 4</span>
Marks of engineering students have mean μ = 70 and variance σ^{2} = 25. Use Chebyshev's inequality to estimate the minimum proportion of students scoring between 60 and 80.
:::

:::guess Guess first
60 to 80 is μ ± 10, which is μ ± how many σ? Guess the minimum percentage.
:::

**Chebyshev's inequality** (G&K §6.13). For any X with mean μ and finite variance σ^{2}, and any k > 0:

$$P(|X − μ| ≥ kσ) ≤ \frac{1}{k^{2}}    equivalently    P(|X − μ| < kσ) ≥ 1 − \frac{1}{k^{2}}$$

With a distance c instead of kσ (c = kσ): P(|X − μ| ≥ c) ≤ σ^{2}/c^{2}.

[[fig:chebyshev|Three shapes with μ = 70, σ = 5. Chebyshev's 75% holds for all of them.|w=80]]

**Answer.** σ = 5, so 60 to 80 is μ ± 2σ: k = 2. P(60 < X < 80) ≥ 1 − 1/4 = **0.75**. At least **75%** of students score between 60 and 80.

<span class="tag">A1 MCQ 5</span> The inequality bounding deviation from the mean: **Chebyshev's** (d). <span class="tag">A1 MCQ 10</span> It applies to **any distribution with finite mean and variance** (b).

:::check Check 5
A random variable has μ = 50, σ = 4. Give a lower bound for P(38 < X < 62).
:::

### 6 · Chebyshev on a given distribution

When the distribution is given, find μ and σ^{2} first, then compare the bound with the exact probability.

:::q <span class="tag">MTE B1 · 3 marks</span>
A random variable takes values −1, 1, 3 and 5 with probabilities 1/6, 1/6, 1/6 and 1/2. By Chebyshev's inequality find the upper bound of P(|X − 3| ≥ 1).
:::

:::guess Guess first
Find μ. Then guess: will Chebyshev's bound be useful here?
:::

**Answer.** μ = (−1 + 1 + 3)/6 + 5/2 = 3/6 + 15/6 = **3**. E(X^{2}) = (1 + 1 + 9)/6 + 25/2 = 11/6 + 75/6 = 86/6 = **43/3**. σ^{2} = 43/3 − 9 = **16/3**.
Chebyshev with c = 1: P(|X − 3| ≥ 1) ≤ σ^{2}/1^{2} = **16/3**. (Professor's key: 16/3.)

:::note What the 16/3 means
Every probability is at most 1, so a bound of 16/3 says nothing new. Chebyshev only bites when c is larger than σ (here σ = 2.31). The exact value is P(|X − 3| ≥ 1) = 1 − P(X = 3) = **5/6**. Write the key's answer, then add this one line: it shows you know what the bound means.
:::

:::q <span class="tag">A1 SA 5</span>
Two unbiased dice are thrown; X is the sum. Prove that P(|X − 7| ≥ 3) ≤ 35/54 and compare with the actual probability.
:::

**Answer.** For one die, μ = 3.5 and σ^{2} = 91/6 − 3.5^{2} = 35/12. The dice are independent, so for the sum μ = 7, σ^{2} = 2 × 35/12 = **35/6**. Chebyshev with c = 3: P(|X − 7| ≥ 3) ≤ (35/6)/9 = **35/54** ≈ 0.648 ✓.
Actual: |X − 7| ≥ 3 means sum ≤ 4 or ≥ 10: (1 + 2 + 3) + (3 + 2 + 1) = 12 of 36 outcomes, **1/3**. The bound holds but is loose.

:::q <span class="tag">A1 SA 6</span>
A symmetric die is thrown 600 times. Find a lower bound for the probability of getting 80 to 120 sixes.
:::

**Answer.** X = number of sixes is binomial (file 04) with n = 600, p = 1/6: μ = np = 100, σ^{2} = np(1 − p) = 600 × (1/6)(5/6) = 250/3. 80 to 120 is |X − 100| ≤ 20:
P(|X − 100| < 20) ≥ 1 − σ^{2}/20^{2} = 1 − (250/3)/400 = 1 − 5/24 = **19/24** ≈ 0.79.

:::check Check 6
X takes 1, 2, 3 with probabilities ¼, ½, ¼. Find the Chebyshev bound for P(|X − 2| ≥ 1) and the exact value.
:::

---

## Exam form

**Definitions.** E(X) = Σx p(x) or ∫x f(x)dx. Var(X) = E(X − μ)^{2} = E(X^{2}) − [E(X)]^{2}. σ = √Var(X).

**Rules.** E(aX + b) = aE(X) + b · Var(aX + b) = a^{2}Var(X) · E(X + Y) = E(X) + E(Y) always · E(XY) = E(X)E(Y) and Var(X ± Y) = Var(X) + Var(Y) when X, Y are independent.

**Chebyshev's inequality.** For any X with mean μ and finite variance σ^{2}:
P(|X − μ| ≥ kσ) ≤ 1/k^{2}, P(|X − μ| < kσ) ≥ 1 − 1/k^{2}; with distance c: P(|X − μ| ≥ c) ≤ σ^{2}/c^{2}.

**Procedure (Chebyshev on a table).**

1. μ = Σx p(x); E(X^{2}) = Σx^{2}p(x); σ^{2} = E(X^{2}) − μ^{2}.
2. Write the event as |X − μ| ≥ c (or < c); read off c.
3. Bound = σ^{2}/c^{2} (upper) or 1 − σ^{2}/c^{2} (lower).
4. If asked, compute the exact probability from the table and compare.

## Traps

- Var(X) = E(X^{2}) − [E(X)]^{2}, not E(X^{2}) − E(X).
- Var(X − Y) = Var(X) + Var(Y) for independent X, Y: the variances **add**.
- Var(aX + b) = a^{2}Var(X): the constant b disappears and a is squared.
- In Chebyshev, using σ^{2} where kσ is needed, or c where c^{2} is needed.
- Writing E(XY) = E(X)E(Y) without independence.

## Self-test

1. State Chebyshev's inequality in both forms.
2. X = 0, 1, 2 with P = 0.3, 0.4, 0.3. Find E(X), Var(X) and σ.
3. f(x) = 2x on (0, 1). Find E(X) and Var(X).
4. E(X) = 10, Var(X) = 9. Find E(3X + 2) and Var(3X + 2).
5. μ = 100, σ = 10. What does Chebyshev say about P(70 < X < 130)?
6. A fair coin is tossed 400 times; X = heads. Use Chebyshev to bound P(180 < X < 220).
7. Why can Chebyshev's bound be larger than 1? What does that tell you?

<!--ANSWERS-->
## Answers

**Check 1.** Sum = 1.00 and all ≥ 0, so valid. E(X) = 0.40 + 0.50 + 0.30 = **1.2**.

**Check 2.** E(X^{2}) = 0.40 + 1.00 + 0.90 = 2.3; Var = 2.3 − 1.44 = **0.86**.

**Check 3.** E(X^{2}) = ∫₀¹ 6x^{3}(1 − x) dx = 6(¼ − ⅕) = **0.3**; Var = 0.3 − 0.25 = **0.05**.

**Check 4.** E = 2(3) − 5 = **1**; Var(2X − 5) = 4 × 4 = **16**; Var(X − Y) = 4 + 1 = **5**.

**Check 5.** 38 to 62 is μ ± 12 = μ ± 3σ: P ≥ 1 − 1/9 = **8/9 ≈ 0.889**.

**Check 6.** μ = 2; E(X^{2}) = ¼ + 2 + 9/4 = 4.5; σ^{2} = 0.5. Bound: P ≤ 0.5/1 = **0.5**. Exact: P(X = 1 or 3) = **0.5**: here the bound is attained.

**Self-test.**

1. P(|X − μ| ≥ kσ) ≤ 1/k^{2}; P(|X − μ| < kσ) ≥ 1 − 1/k^{2}.
2. E = 0.4 + 0.6 = **1**; E(X^{2}) = 0.4 + 1.2 = 1.6; Var = **0.6**; σ = **0.775**.
3. E = 2/3; E(X^{2}) = ½; Var = ½ − 4/9 = **1/18**.
4. **32** and **81**.
5. 70 to 130 is μ ± 3σ: P ≥ **8/9**.
6. μ = 200, σ^{2} = 100. |X − 200| < 20: P ≥ 1 − 100/400 = **0.75**.
7. σ^{2}/c^{2} > 1 when c < σ. The bound is then true but gives no information.
<!--/ANSWERS-->
