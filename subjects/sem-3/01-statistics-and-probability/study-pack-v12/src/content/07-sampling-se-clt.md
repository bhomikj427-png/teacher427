# 07 — Sampling, standard error and the Central Limit Theorem

<div class="sub">Professor's LMS slides "Sampling Concepts & Limit Theorems" (19 slides) · Gupta & Kapoor §8.10, §12.1–12.3, §12.12 · blueprint row 2 "population and sample; standard error; Central Limit Theorem" · 6 real questions · needs 03, 06</div>

## Map

[[map:1 Population, sample, parameter, statistic > 2 Standard error > 3 The Central Limit Theorem > 4 CLT between two values > 5 Small samples: when the CLT is not needed, and when it fails|here=1]]

## The questions this file answers

- <span class="tag">Slides p.4</span> Bulb lifespans have σ = 100 h. Find the standard error of the mean for n = 25, and for n = 100.
- <span class="tag">A4 MCQ 8 · 1 mark</span> A sample has mean 40, SD 5, size 25. The standard error is: 5 / 2 / 1 / 0.2.
- <span class="tag">Slides p.8–9</span> ATM wait times are right-skewed with μ = 4 min, σ = 2 min. For a sample of 36 customers, P(average wait > 4.5 min)?
- <span class="tag">Slides p.10–11</span> Impurity per batch has mean 4.0 g, SD 1.5 g. For 50 batches, P(3.5 g < average < 3.8 g)?
- <span class="tag">Slides p.12–13</span> LED bulb lifespan is skewed, mean 50,000 h, SD 8,000 h. For 64 bulbs, P(average < 48,000 h)?
- <span class="tag">Slides p.14–15</span> Machine life is normal, mean 7 years, SD 1 year. For 9 machines, P(6.4 < average < 7.2)?

Blueprint row 2 (20 marks) carries one of the two 8-mark Part C questions; a CLT problem is a likely candidate.

---

## Build

### 1 · Population, sample, parameter, statistic

Files 02–06 described one random variable. Statistics starts when we only see part of the data.

:::q Predict
A factory makes 500,000 bulbs a month. An inspector tests 100 of them and finds an average life of 1480 hours. Is 1480 the true average life of all the bulbs?
:::

:::guess Guess first
Yes or no, and would a second batch of 100 give exactly 1480 again?
:::

**Terms** (slides p.2; G&K §12.3):

| | Population (size N) | Sample (size n) |
|---|---|---|
| What | every unit we want conclusions about | the units we actually measure, chosen at random |
| Its numbers are | **parameters**: μ, σ (fixed, unknown) | **statistics**: x̄, s (computed, vary from sample to sample) |
| Example | all 500,000 bulbs | 100 bulbs tested |

**Answer.** No. 1480 is a **statistic**: an estimate of the parameter μ. Another random 100 bulbs would give a slightly different x̄. That variation is the subject of this file.

:::check Check 1
Classify each as parameter or statistic: (a) the mean height of all students at MUJ; (b) the proportion of defectives in a box of 50 inspected chips; (c) the SD of marks in a class of 60 used to describe that class only.
:::

### 2 · Standard error: how much x̄ varies

Since x̄ changes from sample to sample, it has its own spread.

:::q <span class="tag">Slides p.4</span>
A factory produces lightbulbs with a known population SD σ = 100 hours. An inspector pulls a random sample of 25 bulbs. Find the standard error of the mean, and see what happens if n increases to 100.
:::

:::guess Guess first
Will the spread of x̄ be more or less than 100 hours? By how much for n = 25?
:::

**Terms.**

- **Sampling distribution of X̄**: the distribution of x̄ over all possible samples of size n.
- **Standard error (SE)**: the SD of that sampling distribution (slides p.3; G&K §12.12).

For independent observations (03b step 3: variances add, and Var(X̄) = Var(ΣXᵢ)/n^{2} = nσ^{2}/n^{2}):

$$E(X̄) = μ,    SE(X̄) = \frac{σ}{√n}$$

If σ is unknown, the sample SD s replaces it: SE ≈ s/√n.

[[fig:se_shrink|SE falls with √n: 4 times the sample halves the SE.|w=72]]

**Answer.** n = 25: SE = 100/√25 = 100/5 = **20 h**. n = 100: SE = 100/10 = **10 h**. Quadrupling n halves the SE.

<span class="tag">A4 MCQ 8</span> s = 5, n = 25: SE = 5/√25 = **1** (c).

:::check Check 2
How large must n be for the bulbs' SE to be 5 hours?
:::

### 3 · The Central Limit Theorem

SE gives the spread of x̄. The CLT gives its **shape**: normal, so file 06's table applies.

:::q <span class="tag">Slides p.8–9</span>
Wait times at a bank ATM are heavily right-skewed: most people finish fast, a few take a very long time. μ = 4 min, σ = 2 min. For a random sample of 36 customers, what is the probability that their average wait is greater than 4.5 minutes?
:::

:::guess Guess first
The individual times are skewed, not normal. Can file 06 still be used for the average of 36?
:::

**Central Limit Theorem** (slides p.6; G&K §8.10). If X₁, …, Xₙ are independent with the same distribution, mean μ and finite variance σ^{2}, then for large n

$$X̄ ≈ N(μ, σ^{2}/n),    Z = \frac{X̄ − μ}{σ/√n} ≈ N(0, 1)$$

whatever the shape of the population. The professor's three rules:

1. **Centre**: the mean of the sample means is μ.
2. **Spread**: their SD is the SE, σ/√n.
3. **Shape**: as n grows the shape becomes normal; n ≥ 30 is taken as large enough.

[[fig:clt_hist|A skewed population (left). Its sample means (centre, right) become a narrow bell as n grows.|w=95]]

**Answer.** n = 36 ≥ 30, so X̄ ≈ N(4, (2/6)^{2}). SE = 2/√36 = 0.333.
z = (4.5 − 4)/0.333 = 1.50. P(X̄ > 4.5) = 0.5 − φ(1.5) = 0.5 − 0.4332 = **0.0668**: about a 6.7% chance.

:::check Check 3
<span class="tag">Slides p.12–13</span> LED lifespan is heavily skewed: mean 50,000 h, SD 8,000 h. For a sample of 64 bulbs, find P(average lifespan < 48,000 h). (φ(2) = 0.4772.)
:::

### 4 · CLT between two values

Same method, two limits.

:::q <span class="tag">Slides p.10–11</span>
The amount of impurity in a batch of a chemical product is a random variable with mean 4.0 g and SD 1.5 g. If 50 batches are prepared independently, what is the approximate probability that the average impurity of these 50 batches is between 3.5 g and 3.8 g?
:::

:::guess Guess first
Both limits are below the mean. Will you add or subtract the two table areas?
:::

**Answer.** SE = 1.5/√50 = 0.2121.
z₁ = (3.5 − 4)/0.2121 = −2.36; z₂ = (3.8 − 4)/0.2121 = −0.94. Both negative, same side, so subtract:
P = φ(2.36) − φ(0.94) = 0.4909 − 0.3264 = **0.1645**.

:::note Slide typo
Slide 11 prints the second limit as z = −0.4, but its next line uses φ(0.94) = 0.3264, which is the correct z = −0.94. The slide's final 0.1644 is right to rounding.
:::

:::check Check 4
Same batches. Find P(average impurity exceeds 4.3 g). (φ(1.41) = 0.4207.)
:::

### 5 · Small samples: when the CLT is not needed, and when it fails

The n ≥ 30 rule is about the population's shape. A normal population needs no CLT.

:::q <span class="tag">Slides p.14–15</span>
The average life of a machine is 7 years with SD 1 year, and lives follow a normal distribution. Find the probability that the average life of 9 random machines falls between 6.4 and 7.2 years.
:::

:::guess Guess first
n = 9 is far below 30. Is the answer still a normal-table calculation? Why?
:::

**The professor's three cases** (slides p.7):

| Population | n | Distribution of X̄ |
|---|---|---|
| any shape | > 30 | approximately N(μ, σ^{2}/n): the CLT |
| normal | any n (even ≤ 30) | exactly N(μ, σ^{2}/n) |
| not normal | ≤ 30 | unknown: the CLT cannot be applied |

**Answer.** The population is normal, so X̄ ~ N(7, (1/3)^{2}) exactly. SE = 1/√9 = 1/3.
z₁ = (6.4 − 7)/(1/3) = −1.8; z₂ = (7.2 − 7)/(1/3) = 0.6. Opposite sides, so add:
P = φ(1.8) + φ(0.6) = 0.4641 + 0.2257 = **0.6898**.

:::check Check 5
Delivery times are strongly skewed with μ = 30 min, σ = 12 min. Can the CLT give P(X̄ > 33) for (a) n = 10 deliveries? (b) n = 64 deliveries? For (b), find it. (φ(2) = 0.4772.)
:::

---

## Exam form

**Definitions.** Population: all units of interest; parameter: a number describing it (μ, σ). Sample: units observed, chosen at random; statistic: a number computed from it (x̄, s). Standard error: the SD of a statistic's sampling distribution; for x̄, SE = σ/√n.

**CLT statement.** If X₁, …, Xₙ are i.i.d. with mean μ and finite variance σ^{2}, then for large n the sample mean X̄ is approximately N(μ, σ^{2}/n), i.e. Z = (X̄ − μ)/(σ/√n) ≈ N(0, 1), regardless of the population's distribution. (For a sum: ΣXᵢ ≈ N(nμ, nσ^{2}).)

**Procedure.**

1. Check the conditions: n ≥ 30, or the population is normal.
2. SE = σ/√n.
3. z = (x̄ − μ)/SE for each limit.
4. Area from the table (file 06's rules).
5. One line of conclusion in words.

## Traps

- Using σ instead of σ/√n in the z for a sample mean.
- Saying "the CLT makes the data normal": it is the **mean** (or sum) that becomes normal; the data keep their shape.
- Applying the CLT to a skewed population with small n.
- Forgetting that quadrupling n only halves the SE.

## Self-test

1. Distinguish parameter and statistic with one example each.
2. State the Central Limit Theorem.
3. σ = 12 and n = 36. Find the SE. What n gives SE = 1?
4. A population has μ = 80, σ = 15. For n = 100, find P(77 < X̄ < 83). (φ(2) = 0.4772.)
5. Why does the machine example need no CLT?
6. For the ATM data, what sample size makes P(X̄ > 4.5) about 0.0228? (φ(2) = 0.4772.)

<!--ANSWERS-->
## Answers

**Check 1.** (a) parameter (b) statistic (c) parameter (the class is the whole population being described).

**Check 2.** 100/√n = 5 ⇒ √n = 20 ⇒ **n = 400**.

**Check 3.** SE = 8000/8 = 1000; z = (48000 − 50000)/1000 = −2; P = 0.5 − 0.4772 = **0.0228**.

**Check 4.** z = (4.3 − 4)/0.2121 = 1.41; P = 0.5 − 0.4207 = **0.0793**.

**Check 5.** (a) No: skewed and n < 30. (b) Yes: SE = 12/8 = 1.5, z = 2, P = 0.5 − 0.4772 = **0.0228**.

**Self-test.**

1. Parameter: the true mean life μ of all bulbs. Statistic: the mean x̄ of 100 tested bulbs.
2. See Exam form.
3. SE = 12/6 = **2**; 12/√n = 1 ⇒ **n = 144**.
4. SE = 1.5; z = ±2; P = 2 × 0.4772 = **0.9544**.
5. The population is normal, so X̄ is exactly normal for any n.
6. Need (4.5 − 4)/(2/√n) = 2 ⇒ √n = 8 ⇒ **n = 64**.
<!--/ANSWERS-->
