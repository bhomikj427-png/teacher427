# 11 — Confidence interval for the mean

<div class="sub">Gupta & Kapoor §15.15 · blueprint row 3 "point and interval estimation; confidence interval for mean" · 7 real questions (Assignments 4 and 5) · needs 06, 07, 08</div>

## Map

[[map:1 What a 95% interval means > 2 σ known: the z-interval > 3 Changing the confidence level > 4 An interval for a function of μ > 5 σ unknown: the t-interval > 6 A t-interval from raw data|here=1]]

## The questions this file answers

- <span class="tag">A4 B3</span> 100 patients, mean haemoglobin 12.5 g/dL, population SD 2 g/dL: a 95% CI for the mean. (Table value 1.96.)
- <span class="tag">A4 B1</span> 20 rental cars, mean 85.5 miles/day, population SD 19.3 miles: a 99% CI for μ. (Table value 2.576.)
- <span class="tag">A4 B2</span> N(μ, σ^{2}) with variance 9; n = 25, x̄ = 30: a 95% CI for r(θ) = 2μ + 7. (Table value 1.96.)
- <span class="tag">A4 B4</span> 10 components, mean breaking strength 250 N, sample SD 20 N, normal population: a 95% CI for the mean. (Table value 2.262.)
- <span class="tag">A4 B5</span> 20 trials, mean 85 °C, sample SD 4 °C, normal: a 90% CI. (Table value 1.729.)
- <span class="tag">A5 D2</span> 20 part weights (24.8, 25.1, …): 95% confidence limits for the mean weight. (t₀.₀₅ = 2.093 for 19 df.)
- <span class="tag">A5 A1(v)</span> Define confidence interval and confidence limits.

---

## Build

### 1 · What a 95% interval means

File 08's estimators give one number. An interval adds how far off that number could be.

:::q <span class="tag">A5 A1(v)</span>
Define confidence interval and confidence limits.
:::

:::guess Guess first
"We are 95% confident μ is between 12.1 and 12.9." Write what the 95% refers to.
:::

From file 07, Z = (X̄ − μ)/(σ/√n) ~ N(0, 1), and P(−1.96 < Z < 1.96) = 0.95. Rearranging the inequality for μ:

$$P(X̄ − 1.96 \frac{σ}{√n} < μ < X̄ + 1.96 \frac{σ}{√n}) = 0.95$$

**Terms** (G&K §15.15):

- **Confidence interval**: the random interval (X̄ − 1.96σ/√n, X̄ + 1.96σ/√n), which contains μ with probability 0.95.
- **Confidence limits**: its two end points (lower and upper).
- **Confidence coefficient** 1 − α: here 0.95.

[[fig:ci_coverage|25 samples, 25 intervals. About 95% of them cover the fixed μ.|w=80]]

**Answer.** A 95% confidence interval is an interval computed from the sample by a rule that captures μ in 95% of repeated samples; its end points are the confidence limits. For one computed interval, μ is either inside or not: the 95% belongs to the method.

:::check Check 1
A student says "there is a 95% probability that μ lies in (12.1, 12.9)". What is the correct wording?
:::

### 2 · σ known: the z-interval

:::q <span class="tag">A4 B3</span>
A hospital wants to estimate the average haemoglobin level of adult patients. A random sample of 100 patients has mean 12.5 g/dL. The population standard deviation is known to be 2 g/dL. Construct a 95% confidence interval for the population mean. (Tabulated value 1.96.)
:::

:::guess Guess first
Compute the SE, then guess the half-width.
:::

**Formula** (σ known; normal population or n large):

$$x̄ ± z_{α/2} \frac{σ}{√n}    (z = 1.645, 1.96, 2.576 for 90%, 95%, 99%)$$

The **margin of error** is z_{α/2} σ/√n: the half-width.

**Answer.** SE = 2/√100 = 0.2. Margin = 1.96 × 0.2 = 0.392.
CI = 12.5 ± 0.392 = **(12.108, 12.892) g/dL**.

:::check Check 2
Same data but n = 400. Find the new interval. What happened to its width?
:::

### 3 · Changing the confidence level

More confidence costs width.

:::q <span class="tag">A4 B1</span>
A car rental firm wants the average miles travelled per day by its cars rented in California. A random sample of 20 cars gives a sample mean of 85.5 miles, with a population standard deviation of 19.3 miles. Compute a 99% confidence interval for μ. (Tabulated value 2.576.)
:::

:::guess Guess first
Will the 99% interval be wider or narrower than a 95% one from the same data?
:::

**Answer.** σ is known, so z applies even though n = 20 (the population is taken as normal).
SE = 19.3/√20 = 19.3/4.4721 = 4.3156. Margin = 2.576 × 4.3156 = 11.117.
CI = 85.5 ± 11.117 = **(74.38, 96.62) miles**.

| Confidence | z | Margin | Interval |
|---|---|---|---|
| 90% | 1.645 | 7.10 | (78.40, 92.60) |
| 95% | 1.96 | 8.46 | (77.04, 93.96) |
| 99% | 2.576 | 11.12 | (74.38, 96.62) |

:::check Check 3
What sample size would give a 95% margin of error of 5 miles for the rental cars?
:::

### 4 · An interval for a function of μ

If you have an interval for μ, a linear function of μ gets its interval by applying the function to both limits.

:::q <span class="tag">A4 B2</span>
For an N(μ, σ^{2}) population with variance 9, construct a 95% confidence interval for the parametric function r(θ) = 2μ + 7, based on a random sample of size 25 giving a sample mean of 30. (Tabulated value 1.96.)
:::

:::guess Guess first
Find the interval for μ first. What do you do to its two ends?
:::

**Answer.** σ = 3, SE = 3/5 = 0.6, margin = 1.96 × 0.6 = 1.176.
CI for μ: (28.824, 31.176). Since 2μ + 7 increases with μ:
CI for 2μ + 7: (2 × 28.824 + 7, 2 × 31.176 + 7) = **(64.648, 69.352)**.
Equivalently: (2x̄ + 7) ± 2 × 1.176 = 67 ± 2.352.

:::check Check 4
Same data: give a 95% CI for 10 − μ. (Careful with the order of the limits.)
:::

### 5 · σ unknown: the t-interval

Usually σ is unknown and must be replaced by s. With a small sample that adds extra uncertainty.

:::q <span class="tag">A4 B4</span>
An engineer tests 10 components. The sample mean breaking strength is 250 N and the sample standard deviation is 20 N. Assuming the population is normally distributed, construct a 95% confidence interval for the population mean breaking strength. (Tabulated value 2.262.)
:::

:::guess Guess first
Why is the table value 2.262 rather than 1.96?
:::

**Terms.**

- **Student's t-distribution** with ν degrees of freedom: the distribution of (X̄ − μ)/(s/√n) for a normal population, ν = n − 1 (G&K §14.2). Bell-shaped like Z but with fatter tails; it approaches Z as n grows.
- **t_{α/2, n−1}**: the table value leaving α/2 in each tail.

[[fig:z_vs_t|Fewer degrees of freedom, fatter tails, larger table value.|w=66]]

**Formula** (σ unknown, normal population, small n):

$$x̄ ± t_{α/2, n−1} \frac{s}{√n}$$

**Answer.** df = 9, t = 2.262. SE = 20/√10 = 6.3246. Margin = 2.262 × 6.3246 = 14.306.
CI = 250 ± 14.306 = **(235.69, 264.31) N**.

**Choosing z or t.** σ known → z. σ unknown and n small (< 30) with a normal population → t. σ unknown and n large → z with s (t and z are almost equal).

:::check Check 5
<span class="tag">A4 B5</span> 20 trials: mean 85 °C, sample SD 4 °C, normal population. Find the 90% CI. (Table value 1.729.)
:::

### 6 · A t-interval from raw data

The 8-mark version gives the data, so x̄ and s must be computed first.

:::q <span class="tag">A5 D2 (CI part)</span>
A company aims for a part weight of 25.0 g. A sample of 20 parts gives: 24.8, 25.1, 24.9, 25.0, 25.2, 24.7, 25.0, 25.1, 25.3, 24.9, 25.0, 24.8, 25.1, 24.9, 25.2, 25.0, 25.1, 24.8, 25.0, 25.2. Provide the 95% confidence limits for the average weight. (t₀.₀₅ = 2.093 for 19 df.)
:::

:::guess Guess first
Does 25.0 g lie inside the interval?
:::

**Shortcut for s.** Work with d = (x − 25.0) × 10 to avoid decimals: d = −2, 1, −1, 0, 2, −3, 0, 1, 3, −1, 0, −2, 1, −1, 2, 0, 1, −2, 0, 2.
Σd = 1, Σd^{2} = 49. So d̄ = 0.05 ⇒ x̄ = 25.0 + 0.005 = **25.005 g**.
Σ(d − d̄)^{2} = 49 − 1^{2}/20 = 48.95; s_{d}^{2} = 48.95/19 = 2.5763, s_{d} = 1.6051 ⇒ **s = 0.16051 g**.

**Answer.** SE = 0.16051/√20 = 0.035891. Margin = 2.093 × 0.035891 = 0.0751.
CI = 25.005 ± 0.0751 = **(24.930, 25.080) g**. 25.0 lies inside (file 13 finishes the test).

:::note Key slip
Assignment 5 prints (24.945, 25.075). Those limits have a half-width of 0.065, which corresponds to s ≈ 0.139, not the data's 0.1605. The limits here were recomputed from the 20 values two ways (by hand and with a library t-interval).
:::

:::check Check 6
Using the same data, find the 99% confidence limits. (t₀.₀₁ = 2.861 for 19 df.)
:::

---

## Exam form

**Definition.** A 100(1 − α)% confidence interval for μ is a random interval (L, U), computed from the sample, with P(L < μ < U) = 1 − α. L and U are the confidence limits; 1 − α is the confidence coefficient.

| Case | Interval | df |
|---|---|---|
| σ known (normal, or n large) | x̄ ± z_{α/2} σ/√n | — |
| σ unknown, n large | x̄ ± z_{α/2} s/√n | — |
| σ unknown, n small, normal population | x̄ ± t_{α/2, n−1} s/√n | n − 1 |

z_{α/2}: 1.645 (90%), 1.96 (95%), 2.576 (99%). s^{2} = Σ(x − x̄)^{2}/(n − 1).

**Procedure.** (1) Identify x̄, σ or s, n and the level. (2) Choose z or t. (3) SE. (4) Margin = table value × SE. (5) x̄ ± margin, with units. (6) One line of interpretation.

## Traps

- Using z when σ is unknown and n is small.
- Using df = n instead of n − 1.
- Dividing by n instead of √n.
- Saying "95% probability that μ is in this interval".
- Computing s with the n-divisor when the data are raw.

## Self-test

1. Define a confidence interval and its limits.
2. n = 64, x̄ = 52, σ = 8: give the 95% and 99% intervals.
3. n = 16, x̄ = 20, s = 4, normal population: the 95% interval (t₀.₀₅,₁₅ = 2.131).
4. Why is a t-interval wider than the z-interval from the same numbers?
5. What happens to the width when n is multiplied by 4?
6. From A4 B3, can the hospital say the mean is above 12? Explain using the interval.

<!--ANSWERS-->
## Answers

**Check 1.** "We are 95% confident": the method used produces intervals that contain μ in 95% of samples.

**Check 2.** SE = 2/20 = 0.1; 12.5 ± 0.196 = **(12.304, 12.696)**: half as wide (n × 4 ⇒ width ÷ 2).

**Check 3.** 1.96 × 19.3/√n = 5 ⇒ √n = 7.5656 ⇒ n = 57.2 ⇒ **n = 58** (round up).

**Check 4.** 10 − μ decreases as μ increases, so the limits swap: (10 − 31.176, 10 − 28.824) = **(−21.176, −18.824)**.

**Check 5.** SE = 4/√20 = 0.8944; margin = 1.729 × 0.8944 = 1.5465; **(83.45, 86.55) °C**.

**Check 6.** Margin = 2.861 × 0.035891 = 0.1027; **(24.902, 25.108) g**.

**Self-test.**

1. See Exam form.
2. SE = 1: 95% **(50.04, 53.96)**; 99% **(49.42, 54.58)**.
3. SE = 1; margin 2.131: **(17.869, 22.131)**.
4. Estimating σ by s adds uncertainty; the t-distribution's fatter tails give a larger table value.
5. The width halves (SE ∝ 1/√n).
6. Yes: the whole interval (12.108, 12.892) lies above 12.
<!--/ANSWERS-->
