# 11 — Confidence interval for the mean

<div class="sub">Gupta & Kapoor §15.15 (confidence interval and confidence limits; σ known, and the t remark for small n) · blueprint row 3 "point and interval estimation; confidence interval for mean" · 7 real questions (A4 B1–B5, A5 A1(v), A5 D2) · needs 06 (reading the table, step 4), 07 (SE = σ/√n, step 5; the CLT, step 7; when it applies, step 8), 08 (point and interval estimation, step 2; why s divides by n − 1, step 5)</div>

## Map

[[map:1 How far off can x̄ be? > 2 The 95% interval x̄ ± 1.96 SE > 3 What "95%" means > 4 Other confidence levels > 5 Width and sample size > 6 An interval for 2μ + 7 > 7 σ unknown: the t-interval > 8 A t-interval from raw data|here=1]]

File 07 showed that the average x̄ of n values lands near μ, with a spread of SE = σ/√n. File 08 step 2 named two kinds of estimate: one number (a point estimate) or a range (an interval estimate). This file builds the range. Steps 1–3 turn "x̄ lands within 1.96 SE of μ, 95% of the time" into the interval x̄ ± 1.96 SE and say what its 95% means; steps 4–6 change the level, the sample size and the quantity estimated; steps 7–8 replace the unknown σ by s, which needs the t table. File 12 uses the same areas to decide between two claims, and file 13 tests a mean with the t of step 7.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| μ | population mean: the average over every unit; fixed, unknown, the thing we want | haemoglobin of all adult patients |
| σ | population SD, when the question gives it | 2 g/dL |
| n | sample size | 100 patients |
| x̄ | sample mean: the one average we measured | 12.5 g/dL |
| SE | standard error of x̄: σ/√n (07 step 5) | 2/√100 = 0.2 g/dL |
| z_{α/2} | the z that leaves the middle 95% (or 90%, 99%) of the Z curve between −z and +z | 1.96 for 95% |
| E | margin of error: z_{α/2} × SE, the half-width of the interval | 0.392 g/dL |
| 1 − α | confidence coefficient: the share of samples whose interval catches μ | 0.95 |
| s | sample SD (divides by n − 1, 08 step 5), used when σ is not given | 20 N |
| t_{α/2, n−1} | the t-table value that takes the place of z when s replaces σ | 2.262 for n = 10 |

**Running example.** A4 B3: **100 patients, x̄ = 12.5 g/dL, σ = 2 g/dL**, so SE = 0.2 g/dL. Steps 1–3 and 5 use it.

## The questions this file answers

- <span class="tag">A5 A1(v)</span> Define confidence interval and confidence limits.
- <span class="tag">A4 B3</span> A hospital wants to estimate the average haemoglobin level of adult patients. A random sample of 100 patients has a mean haemoglobin level of 12.5 g/dL. The population standard deviation is known to be 2 g/dL. Construct a 95% confidence interval for the population mean haemoglobin level. (Tabulated value 1.96.)
- <span class="tag">A4 B1</span> A car rental firm wants to estimate the average number of miles travelled per day by each of its cars rented in California. A random sample of 20 cars gives a sample mean of 85.5 miles, with a population standard deviation of 19.3 miles. Compute a 99% confidence interval to estimate μ. (Tabulated value 2.576.)
- <span class="tag">A4 B2</span> For an N(μ, σ²) population with variance 9, construct a 95% confidence interval for the parametric function r(θ) = 2μ + 7, based on a random sample of size 25 giving a sample mean of 30. (Tabulated value 1.96.)
- <span class="tag">A4 B4</span> An engineer tests 10 components. The sample mean breaking strength is 250 N and the sample standard deviation is 20 N. Assuming the population is normal, construct a 95% confidence interval for the population mean breaking strength. (Tabulated value 2.262.)
- <span class="tag">A4 B5</span> 20 trials of a machine: sample mean temperature 85 °C, sample SD 4 °C, normal population. Find the 90% confidence interval for the mean operating temperature. (Tabulated value 1.729.)
- <span class="tag">A5 D2 (CI part)</span> 20 part weights (24.8, 25.1, …): provide the 95% confidence limits for the average weight. (t₀.₀₅ = 2.093 for 19 df.)

Blueprint row 3 includes "confidence interval for mean": the A4 B-questions are its 4-mark form, A5 A1(v) its 2-mark definition.

---

## Build

### 1 · How far off can x̄ be?

A weather forecast says "28 °C" or "between 27 and 30 °C". The second is less precise but far more likely to be right. A mean from a sample has the same choice.

:::q Predict
The 100 patients of A4 B3 average 12.5 g/dL. Is μ, the average over **all** adult patients, exactly 12.5? Using SE = 2/√100 = 0.2 g/dL from file 07, how far from μ does x̄ usually land?
:::

:::guess Guess first
Write a distance d such that x̄ lands within d of μ in 95 samples out of 100.
:::

:::note Terms
**Point estimate:** one number used as the guess for μ; here x̄ = 12.5 (08 step 2). **Interval estimate:** a range of values, with a stated chance that the method catches μ. **Margin of error E:** the distance either side of x̄ that the range covers.
:::

[[fig:ci_band|What this graph plots: across: x̄ − μ, how far one sample's average lands from the true mean, in g/dL; up: how often each distance happens over all samples of 100 patients (a normal curve with SD = SE = 0.2, by the CLT of 07 step 7). Blue: the middle 95%, between −0.392 and +0.392. Red: the two 2.5% tails.|w=82]]

| x̄ − μ (g/dL) | in SEs | share of samples landing farther out than this (both sides) |
|---|---|---|
| 0.2 | 1 | 31.7% |
| 0.392 | 1.96 | 5% |
| 0.6 | 3 | 0.27% |

The 1.96 comes from 06 step 4's table: the area from 0 to 1.96 is 0.4750, so the area from −1.96 to 1.96 is 2 × 0.4750 = 0.95.

**Answer to the Predict.** No: 12.5 is one sample's average, and another 100 patients would give a different one. x̄ lands within **1.96 × SE = 1.96 × 0.2 = 0.392 g/dL** of μ in 95% of samples. Step 2 turns this round: if x̄ is usually within 0.392 of μ, then μ is usually within 0.392 of x̄.

:::check Check 1
A sample of 25 patients (same σ = 2) is used instead. (a) What is the SE? (b) Within what distance of μ does x̄ land in 95% of samples?
:::

### 2 · The 95% interval x̄ ± 1.96 SE

Step 1 measured from μ, which nobody knows. The interval measures from x̄, which we have.

:::q <span class="tag">A4 B3</span>
A hospital wants to estimate the average haemoglobin level of adult patients. A random sample of 100 patients has a mean haemoglobin level of 12.5 g/dL. The population standard deviation is known to be 2 g/dL. Construct a 95% confidence interval for the population mean haemoglobin level. (Tabulated value 1.96.)
:::

:::guess Guess first
Write the two ends of the interval before reading the derivation.
:::

:::note Terms
**Confidence interval:** the range from x̄ − E to x̄ + E. **Confidence limits:** its two ends, lower and upper. **Confidence coefficient 1 − α:** the share of samples whose interval catches μ; here 0.95 (G&K §15.15).
:::

**Derivation** (G&K §15.15; the population is normal, or n is large enough for the CLT, 07 step 8):

1. Z = (x̄ − μ)/SE follows the standard normal curve (07 step 7).
2. P(−1.96 < Z < 1.96) = 0.95 (step 1).
3. So P(−1.96 SE < x̄ − μ < 1.96 SE) = 0.95 (line 2, multiplied through by SE).
4. Subtract x̄ from every part and multiply by −1, which flips both signs: P(x̄ − 1.96 SE < μ < x̄ + 1.96 SE) = 0.95.

$$x̄ − 1.96 \frac{σ}{√n} < μ < x̄ + 1.96 \frac{σ}{√n}$$

In words: start at the sample average, go 1.96 standard errors down and 1.96 up. Line 4 holds **before** the sample is drawn, while x̄ is still unknown; step 3 says what that means once x̄ = 12.5 is in.

**Answer to A4 B3.**

1. SE = σ/√n = 2/√100 = 2/10 = 0.2 g/dL.
2. E = 1.96 × 0.2 = 0.392 g/dL.
3. Lower limit 12.5 − 0.392 = 12.108; upper limit 12.5 + 0.392 = 12.892.
4. The 95% confidence interval for μ is **(12.108, 12.892) g/dL**.

:::check Check 2
A sample of 64 bulbs has mean life 1480 h; σ = 120 h. Find the 95% confidence interval for the mean life of all bulbs.
:::

### 3 · What "95%" means

Step 2's line 4 was a statement about x̄ before it was drawn. Once the interval is (12.108, 12.892), μ is either inside it or not.

:::q <span class="tag">A5 A1(v)</span>
Define confidence interval and confidence limits.
:::

:::guess Guess first
"There is a 95% chance that μ lies between 12.108 and 12.892." True or false? Write why.
:::

[[fig:ci_coverage|What this graph plots: 20 imagined hospitals, each taking its own 100 patients from a population whose true mean is set at 12.5 g/dL for the picture. Each horizontal line is one hospital's interval x̄ ± 0.392; its dot is that hospital's x̄. Blue lines contain the true μ (black vertical line); the red one misses it.|w=82]]

The figure is the 95% made visible: the rule "x̄ ± 0.392" is used 20 times, and 19 of the 20 lines cross μ. In real life there is only one line, and nobody can see the vertical line to know whether it is one of the 19 or the red one.

**Answer to the Predict.** False as worded. μ is a fixed number, not a random one: for the computed interval (12.108, 12.892) the probability is 1 (inside) or 0 (outside). The 95% belongs to the **method**: intervals built this way catch μ in 95% of samples. The definition (G&K §15.15):

- **Confidence interval:** an interval (T₁, T₂) computed from the sample such that P(T₁ < μ < T₂) = 1 − α; for the mean with σ known, T₁ = x̄ − z_{α/2} σ/√n and T₂ = x̄ + z_{α/2} σ/√n.
- **Confidence limits:** its end points T₁ (lower) and T₂ (upper).
- **Confidence coefficient:** 1 − α, the probability in the definition (0.95 for a 95% interval).

:::check Check 3
A news report says: "95% of patients have haemoglobin between 12.108 and 12.892 g/dL." What has it confused? (Hint: is the interval about one patient or about μ?)
:::

### 4 · Other confidence levels

Step 2 used 1.96 because it leaves the middle 95%. A different level needs a different z.

:::q <span class="tag">A4 B1</span>
A car rental firm wants to estimate the average number of miles travelled per day by each of its cars rented in California. A random sample of 20 cars gives a sample mean of 85.5 miles, with a population standard deviation of 19.3 miles. Compute a 99% confidence interval to estimate μ. (Tabulated value 2.576.)
:::

:::guess Guess first
Will the 99% interval be wider or narrower than a 95% interval from the same cars?
:::

:::note Terms
**z_{α/2}:** the z with area 1 − α between −z and +z, so α/2 is left in each tail. For 95%, α = 0.05 and each tail holds 0.025.
:::

| Level 1 − α | Each tail α/2 | Area from 0 to z (06 step 4) | z_{α/2} |
|---|---|---|---|
| 90% | 0.05 | 0.45 | 1.645 |
| 95% | 0.025 | 0.475 | 1.96 |
| 99% | 0.005 | 0.495 | 2.576 (G&K prints 2.58) |

[[fig:ci_levels|What this graph plots: the car-rental data (x̄ = 85.5 miles, SE = 4.3156) with three intervals on one miles-per-day scale: 90% on top, 95% in the middle, 99% at the bottom. The dot is x̄ in every row; the printed numbers are the limits.|w=82]]

**Answer to A4 B1.** σ is given, so z is used, although n = 20 is small (the question treats the population as normal).

1. SE = 19.3/√20 = 19.3/4.4721 = 4.3156 miles.
2. E = 2.576 × 4.3156 = 11.117 miles.
3. 85.5 − 11.117 = 74.383; 85.5 + 11.117 = 96.617.
4. The 99% interval is **(74.38, 96.62) miles per day**.

| Level | z | E (miles) | Interval |
|---|---|---|---|
| 90% | 1.645 | 7.10 | (78.40, 92.60) |
| 95% | 1.96 | 8.46 | (77.04, 93.96) |
| 99% | 2.576 | 11.12 | (74.38, 96.62) |

Wider, as guessed: to catch μ more often, the net must be bigger.

:::check Check 4
From the running example (x̄ = 12.5, SE = 0.2), give (a) the 90% and (b) the 99% intervals.
:::

### 5 · Width and sample size

Step 4 widened the interval by asking for more confidence. The other dial is n: it sits under a square root in SE.

:::q Predict
The hospital wants a narrower 95% interval: margin E = 0.196 instead of 0.392. How many patients does it need instead of 100?
:::

:::guess Guess first
Twice as many? Four times? Write a number.
:::

[[fig:ci_width_n|What this graph plots: across: the sample size n; up: the 95% margin of error E = 1.96 × 2/√n in g/dL for the haemoglobin data. The three dots are n = 25, 100 and 400.|w=78]]

| n | SE = 2/√n | E = 1.96 SE |
|---|---|---|
| 25 | 0.4 | 0.784 |
| 100 | 0.2 | 0.392 |
| 400 | 0.1 | 0.196 |

Each step down the table multiplies n by 4 and halves E (07 step 6: √4 = 2).

**Solving for n.** E = z σ/√n, so:

1. √n = z σ / E.
2. n = (z σ / E)².
3. Round **up** to the next whole number: rounding down would leave E above the target.

**Answer to the Predict.** n = (1.96 × 2 / 0.196)² = 20² = **400 patients**, four times as many, not twice: halving E needs four times the data.

:::check Check 5
(a) The rental firm (σ = 19.3 miles) wants a 95% margin of error of 5 miles. How many cars? (b) The hospital wants E = 0.1 g/dL at 95%. How many patients?
:::

### 6 · An interval for 2μ + 7

Steps 2–5 gave intervals for μ itself. A question can ask for a quantity built from μ.

:::q <span class="tag">A4 B2</span>
For an N(μ, σ²) population with variance equal to 9, construct a 95% confidence interval for the parametric function r(θ) = 2μ + 7, based on a random sample of size 25 giving a sample mean of 30. (Tabulated value 1.96.)
:::

:::guess Guess first
Find the interval for μ first. What do you then do to its two ends?
:::

:::note Terms
**Parametric function r(θ):** a number computed from the parameter; here θ is μ and r = 2μ + 7. If a < μ < b, then 2a + 7 < 2μ + 7 < 2b + 7, because doubling and adding 7 keeps the order.
:::

**Answer to A4 B2.**

1. Variance 9, so σ = √9 = 3. SE = 3/√25 = 3/5 = 0.6.
2. E = 1.96 × 0.6 = 1.176.
3. Interval for μ: 30 − 1.176 = 28.824 to 30 + 1.176 = 31.176.
4. Apply r to both ends: 2 × 28.824 + 7 = 64.648; 2 × 31.176 + 7 = 69.352.
5. The 95% interval for 2μ + 7 is **(64.648, 69.352)**.

The same in one line: centre 2x̄ + 7 = 67, half-width 2 × 1.176 = 2.352, so 67 ± 2.352. The 7 shifts the interval; the 2 doubles its width (03b step 1: shift and scale).

| r(μ) | Lower | Upper |
|---|---|---|
| μ | 28.824 | 31.176 |
| 2μ + 7 | 64.648 | 69.352 |
| 10 − μ (Check 6) | ? | ? |

:::check Check 6
Same data: give the 95% interval for 10 − μ. (A minus sign reverses the order: which end becomes the lower limit?)
:::

### 7 · σ unknown: the t-interval

Steps 2–6 had σ in the question. Usually only the sample is available, so σ is replaced by the sample SD s, and a small sample makes s itself a rough guess.

:::q <span class="tag">A4 B4</span>
An engineer tests 10 components manufactured for a machine. The sample mean breaking strength is 250 N, and the sample standard deviation is 20 N. Assuming that the population is normally distributed, construct a 95% confidence interval for the population mean breaking strength. (Tabulated value 2.262.)
:::

:::guess Guess first
The question gives 2.262, not 1.96. Will the interval be wider or narrower than x̄ ± 1.96 s/√n? Why?
:::

:::note Terms
**t statistic:** t = (x̄ − μ)/(s/√n), the Z of step 2 with s in place of σ. **Degrees of freedom ν = n − 1:** how many of the n deviations from x̄ are free to vary (they must add to 0); it picks the row of the t table. **t_{α/2, n−1}:** the t-table value leaving α/2 in each tail (G&K §15.15, remark; the t-distribution itself: file 13).
:::

[[fig:z_vs_t|What this graph plots: across: the value of the statistic; up: how often it happens. Blue: the Z curve. Red: t with 4 df. Amber dashed: t with 9 df. The t curves are lower in the middle and fatter in the tails.|w=72]]

| Curve | Cut-off with 2.5% in each tail |
|---|---|
| t, 4 df (n = 5) | 2.776 |
| t, 9 df (n = 10) | 2.262 |
| t, 19 df (n = 20) | 2.093 |
| Z (n very large) | 1.96 |

Fatter tails put the 2.5% cut-off farther out, so the multiplier is larger; as n grows, s settles near σ and t approaches Z.

$$x̄ ± t_{α/2, n−1} \frac{s}{√n}$$

Read it as step 2's interval with two swaps: s for σ (we do not know σ), and t for z (paying for that with a wider net).

**Answer to A4 B4.** Wider than 1.96 would give, because 2.262 > 1.96.

1. df = 10 − 1 = 9; t₀.₀₂₅,₉ = 2.262.
2. SE = 20/√10 = 20/3.1623 = 6.3246 N.
3. E = 2.262 × 6.3246 = 14.306 N (with 1.96 it would be 12.396 N).
4. 250 − 14.306 = 235.694; 250 + 14.306 = 264.306.
5. The 95% interval is **(235.69, 264.31) N**.

**z or t?**

| What the question gives | Use |
|---|---|
| σ | z (normal population, or n large) |
| only s, n small (under 30), normal population | t with n − 1 df |
| only s, n large | z with s (t and z almost agree) |

:::check Check 7
(a) <span class="tag">A4 B5</span> An engineer records the operating temperature of a machine during 20 trials: sample mean 85 °C, sample SD 4 °C, normal population. Find the 90% confidence interval. (Tabulated value 1.729.)
(b) <span class="tag">A4 MCQ 3</span> When σ is unknown and a small sample is drawn from a normal population, which test is generally appropriate: z-test, Student's t-test, χ²-test, F-test?
:::

### 8 · A t-interval from raw data

Step 7 was given x̄ and s. The 8-mark version gives the data, so both must be computed first.

:::q <span class="tag">A5 D2 (CI part)</span>
A company aims for a part weight of 25.0 g. A sample of 20 parts gives: 24.8, 25.1, 24.9, 25.0, 25.2, 24.7, 25.0, 25.1, 25.3, 24.9, 25.0, 24.8, 25.1, 24.9, 25.2, 25.0, 25.1, 24.8, 25.0, 25.2. Provide the 95% confidence limits for the average weight. (t₀.₀₅ = 2.093 for 19 df.)
:::

:::guess Guess first
Does 25.0 g lie inside the interval?
:::

:::note Terms
**Coded value d:** d = (x − 25.0) × 10, the weight measured in tenths of a gram above 25.0. It turns 24.8 into −2 and 25.3 into 3, so the sums are whole numbers. Shifting changes the mean but not the SD; scaling by 10 multiplies both by 10 (03b step 1).
:::

[[fig:d2_weights|What this graph plots: each dot is one of the 20 part weights in grams (equal weights stacked). The blue bar below is the 95% confidence interval for the mean weight, with x̄ = 25.005 g as its dot; the red dashed line is the 25.0 g target.|w=80]]

**Answer to A5 D2 (CI part).**

1. d = −2, 1, −1, 0, 2, −3, 0, 1, 3, −1, 0, −2, 1, −1, 2, 0, 1, −2, 0, 2.
2. Σd = 1 and Σd² = 49.
3. d̄ = 1/20 = 0.05, so x̄ = 25.0 + 0.05/10 = **25.005 g**.
4. Σ(d − d̄)² = Σd² − (Σd)²/n = 49 − 1/20 = 48.95.
5. s_{d}² = 48.95/19 = 2.5763, s_{d} = 1.6051, so s = 1.6051/10 = **0.16051 g**.
6. SE = 0.16051/√20 = 0.16051/4.4721 = 0.035891 g.
7. E = 2.093 × 0.035891 = 0.0751 g.
8. 95% confidence limits: 25.005 − 0.0751 = **24.930 g** and 25.005 + 0.0751 = **25.080 g**.

25.0 g lies inside, so the data agree with the target (file 13 turns this into a formal test).

:::note Answer-key slip (A5 D2)
Assignment 5's key prints the limits (24.945, 25.075). Their half-width, 0.065, needs s ≈ 0.139 g; the 20 printed weights give s = 0.1605 g. The limits (24.930, 25.080) here were recomputed from the 20 values in `verify.py`, by hand and with a library t-interval.
:::

:::check Check 8
Same data: find the 99% confidence limits. (t₀.₀₁ = 2.861 for 19 df.)
:::

---

## Exam form

**Definitions** (G&K §15.15). A 100(1 − α)% **confidence interval** for μ is an interval (T₁, T₂) computed from the sample with P(T₁ < μ < T₂) = 1 − α. T₁ and T₂ are the **confidence limits**; 1 − α is the **confidence coefficient**. Meaning: intervals built this way contain μ in 100(1 − α)% of samples; a computed interval either contains μ or does not.

**Derivation (σ known).** Z = (x̄ − μ)/(σ/√n) ~ N(0, 1) ⇒ P(−1.96 < Z < 1.96) = 0.95 ⇒ P(x̄ − 1.96 σ/√n < μ < x̄ + 1.96 σ/√n) = 0.95.

| Case | Interval | Table value |
|---|---|---|
| σ known (normal population, or n large) | x̄ ± z_{α/2} σ/√n | z: 1.645 (90%), 1.96 (95%), 2.576 (99%) |
| σ unknown, n large | x̄ ± z_{α/2} s/√n | z |
| σ unknown, n small, normal population | x̄ ± t_{α/2, n−1} s/√n | t with n − 1 df |
| a + bμ | (a + b × lower, a + b × upper); swap the ends if b < 0 | as for μ |

**Sample size** for margin E: n = (z_{α/2} σ/E)², rounded up.

**Procedure.** (1) Write x̄, σ or s, n, the level. (2) Choose z or t (and df). (3) SE = σ/√n or s/√n. (4) E = table value × SE. (5) x̄ − E, x̄ + E, with units. (6) One sentence of meaning.

## Traps

- Saying "95% probability that μ is in (12.108, 12.892)": the 95% belongs to the method.
- Using z when only s is given and n is small.
- Using n instead of n − 1 for the t table's df, or dividing s² by n instead of n − 1.
- Dividing σ by n instead of √n.
- Halving the width by doubling n: it takes four times n.
- Rounding the sample size down.
- For 10 − μ or −μ, forgetting to swap the limits.

## Self-test

1. Define confidence interval, confidence limits and confidence coefficient.
2. n = 64, x̄ = 52, σ = 8: give the 95% and 99% intervals.
3. n = 16, x̄ = 20, s = 4, normal population: the 95% interval (t₀.₀₂₅,₁₅ = 2.131).
4. Why is a t-interval wider than the z-interval from the same x̄, s and n?
5. What happens to the width of a confidence interval when n is multiplied by 9?
6. From A4 B3's interval, can the hospital say the mean haemoglobin is above 12 g/dL? Explain.
7. Same sample as A4 B2 (σ = 3, n = 25, x̄ = 30): the 95% interval for 3μ.

<!--ANSWERS-->
## Answers

**Check 1.** (a) SE = 2/√25 = 2/5 = **0.4 g/dL**. (b) 1.96 × 0.4 = **0.784 g/dL**.

**Check 2.** SE = 120/√64 = 120/8 = 15 h; E = 1.96 × 15 = 29.4 h; **(1450.6, 1509.4) h**.

**Check 3.** It reads the interval as a range for **individual patients**. The interval is about **μ**, the average of all patients. Individual values spread with σ = 2 g/dL: about 95% of patients lie within 1.96 × 2 = 3.92 g/dL of μ, a range far wider than 0.784.

**Check 4.** (a) E = 1.645 × 0.2 = 0.329; **(12.171, 12.829) g/dL**. (b) E = 2.576 × 0.2 = 0.5152; **(11.985, 13.015) g/dL**.

**Check 5.** (a) n = (1.96 × 19.3/5)² = 7.5656² = 57.24, so **n = 58 cars** (round up). (b) n = (1.96 × 2/0.1)² = 39.2² = 1536.64, so **n = 1537 patients**.

**Check 6.** 10 − μ falls as μ rises, so the upper limit of μ gives the lower limit: 10 − 31.176 = −21.176 and 10 − 28.824 = −18.824; **(−21.176, −18.824)**.

**Check 7.** (a) df = 19; SE = 4/√20 = 0.8944 °C; E = 1.729 × 0.8944 = 1.5465 °C; **(83.45, 86.55) °C**. (b) **Student's t-test** (B).

**Check 8.** E = 2.861 × 0.035891 = 0.1027 g; **(24.902, 25.108) g**. Wider than the 95% limits, as step 4 predicts.

**Self-test.**

1. See Exam form.
2. SE = 8/8 = 1. 95%: 52 ± 1.96 = **(50.04, 53.96)**. 99%: 52 ± 2.576 = **(49.424, 54.576)**.
3. SE = 4/4 = 1; E = 2.131; **(17.869, 22.131)**.
4. s is itself estimated from the small sample; the t curve's fatter tails put the cut-off farther out (2.262 for 9 df against 1.96), so E is larger.
5. SE = σ/√n is divided by √9 = 3, so the width becomes **one third**.
6. **Yes**: the whole interval (12.108, 12.892) lies above 12, so every value of μ the interval allows is above 12 (at 95% confidence).
7. Interval for μ: (28.824, 31.176); multiply both ends by 3: **(86.472, 93.528)**.
<!--/ANSWERS-->
