# 06 — The normal distribution

<div class="sub">Gupta & Kapoor §8.2 (normal distribution; §8.2.1 as a limit of the binomial; §8.2.2 chief characteristics, areas 0·6826 / 0·9544 / 0·9973) · blueprint row 2 "standard probability distributions: normal" · 12 real questions (MTE C1(a); A2 B3, B4, B6, C2, D1, MCQ 1, 6, 11) · needs 02b (PDF as area, step 1), 03a (mean and SD, steps 1 and 6), 04a (binomial "at least one", step 5)</div>

## Map

[[map:1 The bell: μ and σ > 2 The standard normal Z > 3 Standardise: z = (x − μ)/σ > 4 Reading the table: area from 0 to z > 5 Tails > 6 Between two values > 7 68–95–99.7 > 8 Expected counts > 9 A normal inside a binomial > 10 Percentages back to μ and σ > 11 Two conditions and a percentile|here=1]]

File 05's curves were simple enough to integrate by hand (a rectangle, an exponential). The normal curve is not: nobody integrates it in an exam. Instead every normal curve is turned into **one** standard curve (steps 2–3), and its areas are read from **one** table (step 4). Steps 5–8 use that table forwards (value → probability → count); step 9 puts a normal probability inside 04a's binomial; steps 10–11 run the table backwards (percentage → value). File 07 then explains why averages are normal, and files 11–13 use this table for intervals and tests.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| X | one battery's life in hours (the running example) | 1660 |
| μ | the mean: where the bell's peak sits (03a step 1) | 1500 h |
| σ | the standard deviation: the typical distance from μ (03a step 6) | 100 h |
| N(μ, σ²) | short name for "normal with mean μ and variance σ²" | N(1500, 100²) |
| Z | the standard normal: a normal with mean 0 and SD 1 | — |
| z | a value of Z: how many SDs a value sits from the mean | 1.6 |
| φ(z) | in these assignments: the **area** under the Z curve from 0 to z (the table) | φ(1.6) = 0.4452 |

**Running example.** A2 B4: lithium-ion batteries whose life X is normal with **mean μ = 1500 hours and SD σ = 100 hours**; 5000 of them are tested.

## The questions this file answers

- <span class="tag">A2 MCQ 1</span> In a Normal distribution, the probability density curve is perfectly symmetric about the: a) Variance b) Standard Deviation c) Mean d) Origin
- <span class="tag">A2 MCQ 6</span> What is the variance for a Standard Normal distribution? a) 1 b) 3 c) 0 d) ∞
- <span class="tag">A2 MCQ 11</span> For a standard normal curve, what is the approximate area under the curve between z = −1 and z = 1? a) 95.45% b) 99.73% c) 50.00% d) 68.27%
- <span class="tag">A2 B3</span> Given a normal distribution with mean μ = 50 and standard deviation σ = 10, find the probability that X lies between 45 and 62. (Given φ(0.5) = 0.1915 and φ(1.2) = 0.3849.)
- <span class="tag">A2 B4</span> In a quality test on 5000 lithium-ion batteries, life was normal with mean 1500 h and SD 100 h. Estimate how many last (i) more than 1660 h (ii) less than 1380 h (iii) more than 1350 h but less than 1680 h. (φ(1.2) = 0.3849, φ(1.5) = 0.4332, φ(1.6) = 0.4452, φ(1.8) = 0.4641.)
- <span class="tag">A2 D1</span> Bulb life is normal with mean 3000 h and SD 400 h. Of 10,000 bulbs, how many last between 2500 and 3500 hours?
- <span class="tag">MTE C1(a) · 4 marks</span> The marks obtained by students in a subject are approximately normally distributed with mean 65 and SD 5. If 3 students are selected at random from this group, what is the probability that at least one of them scored above 75? (Given: the area between Z = 0 and Z = 2 under the standard normal curve is 0.4772.)
- <span class="tag">A2 B6</span> In a distribution exactly normal, 10% of the items are under 30 and 85% are under 65. What are the mean and standard deviation? (φ(1.04) = 0.35, φ(1.28) = 0.4.)
- <span class="tag">A2 C2</span> In an examination, 46% of candidates passed and 9% got distinctions; the minimum pass and distinction marks are 40 and 75. Assume marks are normal. Estimate the average mark and the SD. Also find the minimum qualifying mark for re-examination of failed candidates, if the best 25% of them are given another chance. (φ(0.1) = 0.04, φ(1.34) = 0.41, φ(0.24) = 0.095.)

---

## Build

### 1 · The bell: μ and σ

File 02b drew a density and read probabilities as areas. The normal is the density you will meet most: lives, marks, heights, measurement errors.

:::q <span class="tag">A2 MCQ 1</span>
In a Normal distribution, the probability density curve is perfectly symmetric about the: a) Variance b) Standard Deviation c) Mean d) Origin
:::

:::guess Guess first
Battery lives average 1500 hours. Is a battery that lasts 1400 hours as common as one that lasts 1600? Pick an option.
:::

:::note Terms
**Normal distribution N(μ, σ²):** a density shaped like a bell, high in the middle and falling away evenly on both sides (G&K §8.2). **μ:** sets where the peak sits (the mean). **σ:** sets how wide the bell is (the SD); one σ is the distance from the peak to where the curve changes from bending down to bending up.
:::

[[fig:norm_battery|What this graph plots: the density of the battery life X ~ N(1500, 100²). Horizontal axis: x, life in hours. Vertical axis: f(x), the height of the curve (an area under it is a probability). Red dashed line: the mean μ = 1500. Orange arrow: one SD, σ = 100. The four dots are the table below.|w=80]]

| x (hours) | distance from μ | f(x) |
|---|---|---|
| 1300 | 2σ below | 0.000540 |
| 1400 | 1σ below | 0.002420 |
| 1500 | at μ | 0.003989 |
| 1600 | 1σ above | 0.002420 |

The formula (G&K §8.2), read once and never integrated by hand:

$$f(x) = \frac{1}{σ√(2π)} e^{−(x − μ)²/(2σ²)},  −∞ < x < ∞;    E(X) = μ,  Var(X) = σ²$$

Read back: the height depends on x only through (x − μ)², the **squared distance** from the mean, so x = 1400 and x = 1600 (both 100 away) get the same height. That is the symmetry. Because the two halves match, the mean, the median and the mode are the same point μ, and half the area lies on each side.

**Answer to the question.** The table shows f(1400) = f(1600): the curve is a mirror image about the **mean**, option (c).

:::check Check 1
For the batteries: (a) which is larger, f(1450) or f(1550)? (b) What is P(X < 1500)?
:::

### 2 · The standard normal Z

Every (μ, σ) pair gives a different bell, and no exam can print a table for each. One bell is chosen as the reference.

:::q <span class="tag">A2 MCQ 6</span>
What is the variance for a Standard Normal distribution? a) 1 b) 3 c) 0 d) ∞
:::

:::guess Guess first
The reference bell should be as simple as possible. What mean and what SD would you choose for it?
:::

:::note Terms
**Standard normal Z:** the normal with mean 0 and SD 1, N(0, 1). Its horizontal axis counts **SDs from the mean** instead of hours or marks.
:::

The battery curve and the Z curve are the same shape: slide the battery curve left by 1500 so its peak sits at 0, then measure in units of 100 hours. Step 3's figure shows both scales on one curve.

**Answer to the question.** Z has SD 1, so its variance is 1² = **1**, option (a). (Its mean is 0.)

:::check Check 2
X ~ N(1500, 100²). Write the mean and variance of X, then the mean and variance of Z.
:::

### 3 · Standardise: z = (x − μ)/σ

Step 2 said "measure in SDs from the mean". This step makes that one subtraction and one division.

:::q Predict
A battery lasts 1660 hours. How many SDs above the mean is that?
:::

:::guess Guess first
1660 is 160 hours above 1500, and one SD is 100 hours. Write a number.
:::

:::note Terms
**Standardising:** turning a value x into z = (x − μ)/σ. **x − μ** counts how far x is from the mean (in hours); **dividing by σ** turns hours into SDs. A negative z means below the mean.
:::

[[fig:norm_xz|What this graph plots: the battery density once, with two scales. Bottom axis: x, hours. Top axis (orange): z = (x − 1500)/100, SDs from the mean. Each hour value sits directly under its z value; the red dashed line is 1660 h, which is z = 1.6.|w=80]]

| x (hours) | x − μ | z = (x − μ)/σ |
|---|---|---|
| 1350 | −150 | −1.5 |
| 1380 | −120 | −1.2 |
| 1500 | 0 | 0 |
| 1660 | 160 | 1.6 |
| 1680 | 180 | 1.8 |

Read back: z = (x − μ)/σ = "how many SDs, and which side". Because the two scales line up, any area between two x values equals the area between their two z values: **P(X > 1660) = P(Z > 1.6)**.

**Answer to the Predict.** z = (1660 − 1500)/100 = 160/100 = **1.6** SDs above the mean.

:::check Check 3
<span class="tag">MTE C1(a), first line</span> Marks are normal with mean 65 and SD 5. (a) Standardise a mark of 75. (b) Which mark has z = −1.4?
:::

### 4 · Reading the table: area from 0 to z

Step 3 moved every question onto Z. The table gives areas under Z, in one fixed form.

:::q Predict
What fraction of batteries last between 1500 and 1660 hours? (φ(1.6) = 0.4452.)
:::

:::guess Guess first
1500 is the mean and 1660 is 1.6 SDs above it. Is the fraction more or less than one half?
:::

:::note Terms
**φ(z)** (as the assignments use it): the area under the Z curve **from 0 to z**, for z ≥ 0 — the number the question prints or the table gives. Other books use other letters or tabulate the area from −∞; always read which area the question gives.
:::

[[fig:norm_table|What this graph plots: the standard normal density. Horizontal axis: z. Vertical axis: the height of the Z curve. Green: the area from 0 to 1.6, which is φ(1.6) = 0.4452. Each half of the curve holds area 0.5.|w=76]]

| z | 0.5 | 1 | 1.5 | 1.6 | 2 |
|---|---|---|---|---|---|
| φ(z) = area from 0 to z | 0.1915 | 0.3413 | 0.4332 | 0.4452 | 0.4772 |

Read back: φ grows with z but never passes 0.5, because the whole right half holds only 0.5. A negative z needs no new table: by symmetry the area from −1.6 to 0 equals the area from 0 to 1.6.

**Answer to the Predict.** 1500 → z = 0 and 1660 → z = 1.6, so P(1500 < X < 1660) = P(0 < Z < 1.6) = φ(1.6) = **0.4452**: less than one half (the half above the mean also holds the batteries beyond 1660).

:::check Check 4
Using the table above: (a) P(0 < Z < 1.5); (b) P(−1.5 < Z < 0); (c) P(1500 < X < 1700) for the batteries.
:::

### 5 · Tails

Step 4's table starts at 0. Most questions ask "more than" or "less than", which is a **tail**: everything beyond one value.

:::q <span class="tag">A2 B4 (i), (ii) as probabilities</span>
For the batteries, find the probability that one battery lasts (i) more than 1660 h; (ii) less than 1380 h. (φ(1.2) = 0.3849, φ(1.6) = 0.4452.)
:::

:::guess Guess first
Is P(X > 1660) about 5%, 15% or 45%?
:::

:::note Terms
**Upper tail** P(Z > z): the area to the right of z. **Lower tail** P(Z < −z): the area to the left of −z; by symmetry it equals the upper tail P(Z > z).
:::

[[fig:norm_tails|What this graph plots: the battery density. Horizontal axis: life in hours. Red right tail: lives above 1660 (z = 1.6). Red left tail: lives below 1380 (z = −1.2). Each tail = half the curve (0.5) minus the table area between the mean and the cut.|w=80]]

The rule, for z > 0:

1. The half beyond the mean holds 0.5.
2. The table area φ(z) is the part between the mean and z.
3. **P(Z > z) = 0.5 − φ(z)**, and the same number for P(Z < −z).

**Answer to the question.** (i) z = 1.6: P(X > 1660) = 0.5 − 0.4452 = **0.0548**, about 5%. (ii) z = (1380 − 1500)/100 = −1.2: P(X < 1380) = P(Z < −1.2) = 0.5 − 0.3849 = **0.1151**.

:::check Check 5
For the batteries: (a) P(X > 1700) (φ(2) = 0.4772); (b) P(X < 1350) (φ(1.5) = 0.4332).
:::

### 6 · Between two values

Step 5 cut once. Two cuts give two table areas; whether to **add** or **subtract** them depends on which sides of the mean the cuts fall.

:::q <span class="tag">A2 B3</span>
Given a normal distribution with mean μ = 50 and standard deviation σ = 10, find the probability that X lies between 45 and 62. (Given φ(0.5) = 0.1915 and φ(1.2) = 0.3849.)
:::

:::guess Guess first
45 and 62 are how many SDs from 50, and on which sides?
:::

[[fig:norm_between|What this graph plots: the density of X ~ N(50, 10²). Horizontal axis: x. Red dashed line: the mean 50. Green: 45 to 50, area φ(0.5) = 0.1915. Orange: 50 to 62, area φ(1.2) = 0.3849. The cuts are on opposite sides of the mean, so the two pieces add.|w=80]]

| Where the two cuts fall | Area between them |
|---|---|
| opposite sides of the mean (z₁ < 0 < z₂) | φ(∣z₁∣) + φ(z₂) |
| same side (0 < z₁ < z₂) | φ(z₂) − φ(z₁) |
| same side, both below (z₁ < z₂ < 0) | φ(∣z₁∣) − φ(∣z₂∣) |

Read back: draw the bell, mark the mean, shade; the picture tells you to add (the shading crosses the mean) or subtract (it does not).

**Answer to the question.** z₁ = (45 − 50)/10 = −0.5, z₂ = (62 − 50)/10 = 1.2: opposite sides, so add. P(45 < X < 62) = 0.1915 + 0.3849 = **0.5764**.

:::check Check 6
Same X ~ N(50, 10²). Find (a) P(X > 62); (b) P(55 < X < 62).
:::

### 7 · 68–95–99.7

Three areas come up so often that they are worth knowing without a table.

:::q <span class="tag">A2 MCQ 11</span>
For a standard normal curve, what is the approximate area under the curve between z = −1 and z = 1? a) 95.45% b) 99.73% c) 50.00% d) 68.27%
:::

:::guess Guess first
Pick an option, then check it with step 4's table: φ(1) = 0.3413.
:::

[[fig:normal_rule|What this graph plots: a normal density with the horizontal axis marked in SDs from the mean (μ − 3σ to μ + 3σ). Darkest band: within one SD of the mean; middle band: within two; palest: within three. The arrows give the area of each band.|w=78]]

| Band | Area | Battery lives in the band |
|---|---|---|
| μ ± σ | 2 × 0.3413 = 0.6827 (68.27%) | 1400 to 1600 h |
| μ ± 2σ | 2 × 0.4772 = 0.9545 (95.45%) | 1300 to 1700 h |
| μ ± 3σ | 0.9973 (99.73%) | 1200 to 1800 h |

Read back: about two-thirds of values lie within one SD of the mean, about 95% within two, and almost all within three. These hold for **every** normal curve, because steps 2–3 turn every curve into Z.

:::note Two printings of the same areas
G&K §8.2.2 prints these areas as 0·6826, 0·9544, 0·9973 (four places, cut short); the course writes 68.27%, 95.45%, 99.73% (rounded). Both describe the same areas; use the course's options in the exam.
:::

**Answer to the question.** P(−1 < Z < 1) = 2 × 0.3413 = 0.6827 = **68.27%**, option (d).

:::check Check 7
X ~ N(100, 15²). Without a table: (a) what percentage of values lie between 70 and 130? (b) between 85 and 115?
:::

### 8 · Expected counts: N × P

Steps 5–6 gave the chance for **one** item. "How many of 5000" multiplies that chance by the number of items.

:::q <span class="tag">A2 B4</span>
In a quality test on 5000 lithium-ion batteries, life was normal with mean 1500 h and SD 100 h. Estimate how many last (i) more than 1660 h (ii) less than 1380 h (iii) more than 1350 h but less than 1680 h. (φ(1.2) = 0.3849, φ(1.5) = 0.4332, φ(1.6) = 0.4452, φ(1.8) = 0.4641.)
:::

:::guess Guess first
Step 5 gave P(X > 1660) = 0.0548. About how many of 5000 is that?
:::

:::note Terms
**Expected count:** N × P, the number of items out of N expected in the event (the same N·P as 04a step 6's expected frequency). Round to a whole number at the end, not before.
:::

**Answer to the question.**

1. (i) P(X > 1660) = 0.0548 (step 5): 5000 × 0.0548 = **274** batteries.
2. (ii) P(X < 1380) = 0.1151 (step 5): 5000 × 0.1151 = 575.5 ≈ **576** batteries.
3. (iii) z = (1350 − 1500)/100 = −1.5 and z = (1680 − 1500)/100 = 1.8: opposite sides, so add: P = 0.4332 + 0.4641 = 0.8973; 5000 × 0.8973 = 4486.5 ≈ **4487** batteries.

:::check Check 8
<span class="tag">A2 D1</span> Bulb life is normal with mean 3000 h and SD 400 h. Of 10,000 bulbs, how many last between 2500 and 3500 hours? (φ(1.25) = 0.3944.)
:::

### 9 · A normal probability inside a binomial

The 4-mark MTE question chains two files: a normal probability for one student (steps 3–5), then 04a's binomial for three students.

:::q <span class="tag">MTE C1(a) · 4 marks</span>
The marks obtained by students in a subject are approximately normally distributed with mean 65 and SD 5. If 3 students are selected at random from this group, what is the probability that at least one of them scored above 75? (Given: the area between Z = 0 and Z = 2 under the standard normal curve is 0.4772.)
:::

:::guess Guess first
P(one student > 75) is small. Is P(at least one of three) about three times it, or exactly three times it?
:::

:::note Terms
**p:** the chance that **one** student scores above 75 (from the normal). **Y:** how many of the 3 chosen students score above 75; each student is one yes/no trial with chance p, so Y ~ B(3, p) (04a step 3).
:::

[[fig:normal_std|What this graph plots: left, the marks density N(65, 5²) with the marks above 75 in red; right, the standard normal Z with the area above z = 2 in red and the table area 0 to 2 (0.4772) in green. Standardising moves the red tail from the left curve to the right one without changing its area.|w=92]]

**Answer to the question.**

1. One student: z = (75 − 65)/5 = 2, so p = P(X > 75) = P(Z > 2) = 0.5 − 0.4772 = **0.0228** (step 5).
2. Three students: Y ~ B(3, 0.0228), q = 1 − p = 0.9772.
3. "At least one" = 1 − "none" (04a): P(Y ≥ 1) = 1 − P(Y = 0) = 1 − q³ = 1 − 0.9772³ = 1 − 0.93315 = **0.0668**.

So about three times p (3 × 0.0228 = 0.0684), slightly less: 3p counts twice the cases where two students both pass 75.

:::note Marking scheme
The MTE scheme gives marks for z and P(X > 75) = 0.0228, then for the binomial set-up and 1 − q³. Its final 0.0667 is the same value rounded differently.
:::

:::check Check 9
Same class. Five students are chosen. Find P(none of them scored above 75).
:::

### 10 · Percentages back to μ and σ

Steps 3–9 went value → z → area. Inverse questions give the areas and ask for μ and σ: read the table backwards.

:::q <span class="tag">A2 B6</span>
In a distribution exactly normal, 10% of the items are under 30 and 85% are under 65. What are the mean and standard deviation? (Given φ(1.04) = 0.35 and φ(1.28) = 0.4.)
:::

:::guess Guess first
Is the mean nearer 30 or 65? (Which side has the smaller tail?)
:::

[[fig:normal_inverse|What this graph plots: the fitted normal density. Horizontal axis: x. Red: the 10% below 30. Purple: the 15% above 65. Dashed lines: 30 sits 1.28 SDs below the mean, 65 sits 1.04 SDs above it.|w=78]]

The method, four lines:

1. Place each value: 10% below 30 is under one half, so 30 is **below** μ; 85% below 65 is over one half, so 65 is **above** μ.
2. Area between μ and each value: 0.5 − 0.10 = 0.40 for 30; 0.85 − 0.5 = 0.35 for 65.
3. Table backwards: φ(1.28) = 0.40, so 30 has z = −1.28; φ(1.04) = 0.35, so 65 has z = +1.04.
4. Each z gives one equation (x − μ)/σ = z; two equations, two unknowns.

**Answer to the question.**

1. (30 − μ)/σ = −1.28, so 30 = μ − 1.28σ.
2. (65 − μ)/σ = 1.04, so 65 = μ + 1.04σ.
3. Subtract line 1 from line 2: 35 = 2.32σ, so **σ = 15.09**.
4. μ = 30 + 1.28 × 15.09 = **49.31**.

:::check Check 10
A normal variable has 31% of values below 45 and 8% above 64. Find μ and σ. (φ(0.5) = 0.19, φ(1.4) = 0.42.)
:::

### 11 · Two conditions and a percentile

The 8-mark version of step 10 adds a second question about the fitted curve: a cut-off inside one group.

:::q <span class="tag">A2 C2</span>
In an examination, 46% of candidates passed and 9% got distinctions; the minimum pass and distinction marks are 40 and 75. Assume marks are normal. Estimate the average mark and the SD. Also find the minimum qualifying mark for re-examination of failed candidates, if the best 25% of them are given another chance. (φ(0.1) = 0.04, φ(1.34) = 0.41, φ(0.24) = 0.095.)
:::

:::guess Guess first
Only 46% passed. Is the pass mark 40 above or below the mean?
:::

:::note Terms
**Percentile mark:** the mark with a given percentage of candidates below it. "Best 25% of the failures" means the top quarter of those below 40, so the cut-off has the other three quarters of the failures below it.
:::

[[fig:norm_c2|What this graph plots: the fitted marks density N(37.18, 28.23²). Horizontal axis: mark. Red: distinctions above 75 (9%). Green-blue: passes without distinction, 40 to 75 (37%). Orange: the best quarter of the failures, 30.40 to 40 (13.5%). Grey: the rest of the failures, below 30.40 (40.5%).|w=86]]

**Answer to the question.** *Mean and SD* (step 10's method):

1. 46% are above 40, under one half, so 40 is **above** μ: area between μ and 40 = 0.5 − 0.46 = 0.04, φ(0.1) = 0.04, so (40 − μ)/σ = 0.1.
2. 9% are above 75: area between μ and 75 = 0.5 − 0.09 = 0.41, φ(1.34) = 0.41, so (75 − μ)/σ = 1.34.
3. Subtract: 35/σ = 1.34 − 0.1 = 1.24, so **σ = 28.23**; μ = 40 − 0.1 × 28.23 = **37.18**.

*Re-examination mark:*

4. Failed = below 40 = 54% of all candidates. The best quarter of them = 0.25 × 54% = 13.5%, just below 40.
5. So the cut-off x has 54% − 13.5% = 40.5% of candidates below it. 40.5% is under one half, so x is below μ, with 0.5 − 0.405 = 0.095 between them.
6. φ(0.24) = 0.095, so z = −0.24: x = 37.18 − 0.24 × 28.23 = **30.40** marks.

:::note Key slip
Assignment 2's key prints μ = 37.5 and a mark of 30.43. The two equations give μ = 37.18 (37.18 + 1.34 × 28.23 = 75.0 checks); the key's own 30.43 needs μ ≈ 37.2, so 37.5 is a typo. 30.43 vs 30.40 is rounding.
:::

:::check Check 11
With μ = 37.18 and σ = 28.23, what percentage of candidates score above 60? (φ(0.81) = 0.291.)
:::

---

## Exam form

**Statement** (G&K §8.2). X ~ N(μ, σ²): f(x) = \frac{1}{σ√(2π)} e^{−(x − μ)²/(2σ²)}, −∞ < x < ∞; mean μ, variance σ²; symmetric about μ; mean = median = mode.

**Standardising.** Z = (X − μ)/σ ~ N(0, 1); P(a < X < b) = P((a − μ)/σ < Z < (b − μ)/σ).

**Forward procedure (value → probability → count).**

1. Convert each limit: z = (x − μ)/σ.
2. Sketch the bell, mark 0, shade the event.
3. Areas from φ(z) (area 0 to z): tail = 0.5 − φ(z); opposite sides add; same side subtract.
4. Count = N × probability, rounded at the end.

**Inverse procedure (percentage → value).** Place each value left or right of μ → area between μ and the value → z from the table (negative below μ) → (x − μ)/σ = z → solve.

**Areas to remember.** μ ± σ: 68.27% · μ ± 2σ: 95.45% · μ ± 3σ: 99.73% · φ(1.645) = 0.45 · φ(1.96) = 0.475 · φ(2.576) = 0.495.

## Traps

- Subtracting two φ values when the limits are on **opposite** sides of μ: add them.
- Forgetting the 0.5 in a tail: P(Z > z) = 0.5 − φ(z), not φ(z).
- Dividing by σ² instead of σ when standardising.
- In inverse questions, a value below μ gets a **negative** z.
- Treating "at least one of 3" as 3p: use 1 − q³.
- Rounding a count before multiplying: round N × P at the end.

## Self-test

1. Write the normal density and say what μ and σ set.
2. X ~ N(60, 8²). Find P(X > 72). (φ(1.5) = 0.4332.)
3. X ~ N(60, 8²). Find P(52 < X < 68) without a table.
4. Heights are N(165, 6²) cm. In a group of 1000, about how many are taller than 177 cm? (φ(2) = 0.4772.)
5. The top 5% of a N(70, 10²) exam get an A. Find the cut-off mark. (φ(1.645) = 0.45.)
6. Why does the table only need z ≥ 0?

<!--ANSWERS-->
## Answers

**Check 1.** (a) Equal: 1450 and 1550 are both 50 hours from the mean. (b) **0.5**: half the area lies on each side of μ.

**Check 2.** X: mean 1500, variance 100² = 10,000. Z: mean **0**, variance **1**.

**Check 3.** (a) z = (75 − 65)/5 = **2**. (b) x = μ + zσ = 65 − 1.4 × 5 = **58**.

**Check 4.** (a) φ(1.5) = **0.4332**. (b) Same by symmetry: **0.4332**. (c) z = 0 and 2: φ(2) = **0.4772**.

**Check 5.** (a) z = 2: 0.5 − 0.4772 = **0.0228**. (b) z = −1.5: 0.5 − 0.4332 = **0.0668**.

**Check 6.** (a) z = 1.2: 0.5 − 0.3849 = **0.1151**. (b) z = 0.5 and 1.2, same side: 0.3849 − 0.1915 = **0.1934**.

**Check 7.** (a) 70 to 130 is μ ± 2σ: **95.45%**. (b) 85 to 115 is μ ± σ: **68.27%**.

**Check 8.** z = (2500 − 3000)/400 = −1.25 and +1.25: 2 × 0.3944 = 0.7888; 10,000 × 0.7888 = **7888 bulbs**.

**Check 9.** P(Y = 0) = q⁵ = 0.9772⁵ = **0.8911**.

**Check 10.** 45 below μ: area 0.5 − 0.31 = 0.19, z = −0.5. 64 above μ: area 0.5 − 0.08 = 0.42, z = 1.4. Subtract: 19 = 1.9σ, so σ = **10**; μ = 45 + 0.5 × 10 = **50**.

**Check 11.** z = (60 − 37.18)/28.23 = 0.81: 0.5 − 0.291 = 0.209, about **21%**.

**Self-test.**

1. f(x) = \frac{1}{σ√(2π)} e^{−(x − μ)²/(2σ²)}; μ sets where the peak is (the mean), σ sets the width (the SD).
2. z = (72 − 60)/8 = 1.5: 0.5 − 0.4332 = **0.0668**.
3. 52 to 68 is μ ± σ: **0.6827**.
4. z = (177 − 165)/6 = 2: 0.5 − 0.4772 = 0.0228; 1000 × 0.0228 = 22.8 ≈ **23**.
5. Area 0.45 between μ and the cut-off: z = 1.645, mark = 70 + 1.645 × 10 = **86.45**.
6. The curve is symmetric about 0, so the area from −z to 0 equals the area from 0 to z.
<!--/ANSWERS-->
