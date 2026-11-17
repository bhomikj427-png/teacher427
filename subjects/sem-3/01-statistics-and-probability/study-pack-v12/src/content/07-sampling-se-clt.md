# 07 — Sampling, standard error and the Central Limit Theorem

<div class="sub">Professor's LMS slides "Sampling Concepts & Limit Theorems" p.2–18 · Gupta & Kapoor §8.10 (Central Limit Theorem), §12.3 (parameter, statistic, sampling distribution, standard error) · blueprint row 2 "population and sample; standard error; Central Limit Theorem" · 6 real questions (slides p.5, p.11–12, p.13–14, p.15–16, p.17–18; A4 MCQ 8) · needs 03b (shift and scale, step 1; mean of a sum, step 2; variance of a sum, step 3), 06 (standardise, step 3; tails, step 5; between two values, step 6)</div>

## Map

[[map:1 Population and sample > 2 Parameter and statistic > 3 The sampling distribution > 4 Standard error: its spread > 5 SE = σ/√n > 6 Four times the sample, half the SE > 7 The Central Limit Theorem > 8 When the CLT may be used > 9 z for an average > 10 An average between two values > 11 A lower tail > 12 Normal population, small sample|here=1]]

File 06 found probabilities for **one** value drawn from a normal curve. This file asks about the **average** of many values. Steps 1–4 set up the idea that an average changes from sample to sample and has its own spread, the standard error; steps 5–6 give its formula σ/√n; steps 7–8 say when the average follows a normal curve (the Central Limit Theorem); steps 9–12 then use file 06's table on averages, one slide example each. File 08 judges formulas that guess a population's numbers from a sample, and file 11 builds intervals from the standard error.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| N | population size: how many units there are in all | 500,000 bulbs |
| n | sample size: how many units are measured | 36 customers |
| μ | population mean: the average over every unit (fixed) | 4 min |
| σ | population SD: the typical distance of one unit from μ (fixed) | 2 min |
| x̄ | sample mean: the average of the n measured values; a new sample gives a new x̄ | 4.5 min |
| s | sample SD: the SD of the n measured values | 5 |
| SE | standard error: the SD of x̄ over all possible samples | 2/√36 = 0.333 min |
| z | how many SEs an average sits from μ: (x̄ − μ)/SE | 1.5 |
| φ(z) | the area under the Z curve from 0 to z (06 step 4) | φ(1.5) = 0.4332 |

**Running example.** Slides p.11–12: waits at a bank ATM are right-skewed (most people finish fast, a few take very long), with **μ = 4 min and σ = 2 min**; a sample is **n = 36** customers. Steps 5–9 and their Checks use it.

## The questions this file answers

- <span class="tag">Slides p.5</span> A factory produces light bulbs with a known population SD σ = 100 hours. An inspector pulls a random sample of 25 bulbs. Find the standard error of the mean, and see what happens if n increases to 100.
- <span class="tag">A4 MCQ 8 · 1 mark</span> A sample has mean 40, SD 5, size 25. The standard error is: 5 / 2 / 1 / 0.2.
- <span class="tag">Slides p.11–12</span> Wait times at a bank ATM are heavily right-skewed. μ = 4 min, σ = 2 min. For a random sample of 36 customers, what is the probability that their average wait is greater than 4.5 minutes?
- <span class="tag">Slides p.13–14</span> The amount of impurity in a batch of a chemical product is a random variable with mean 4.0 g and SD 1.5 g. If 50 batches are prepared independently, what is the approximate probability that the average impurity of these 50 batches is between 3.5 g and 3.8 g?
- <span class="tag">Slides p.15–16</span> LED bulb lifespan is heavily skewed with mean 50,000 h and SD 8,000 h. For a sample of 64 bulbs, find the probability that the average lifespan is less than 48,000 h.
- <span class="tag">Slides p.17–18</span> The average life of a machine is 7 years with SD 1 year, and lives follow a normal distribution. Find the probability that the average life of 9 random machines falls between 6.4 and 7.2 years.

Blueprint row 2 (20 marks) carries one of the two 8-mark Part C questions; a CLT problem like steps 9–12 is a likely candidate.

---

## Build

### 1 · Population and sample

A factory makes 500,000 bulbs a month (slides p.2). Testing a bulb's life burns it out, so nobody can test them all.

:::q Predict
An inspector tests 100 of the 500,000 bulbs and finds an average life of 1480 hours. Is 1480 hours the average life of all 500,000 bulbs?
:::

:::guess Guess first
Yes or no? And would a second set of 100 bulbs give exactly 1480 again?
:::

:::note Terms
**Population:** every unit we want a conclusion about; its size is **N** (here 500,000 bulbs). **Sample:** the units actually measured, picked at random so that every unit has the same chance; its size is **n** (here 100).
:::

[[fig:ball_samples|What this figure shows: slide p.3's small population, 10 balls a to j, of which 4 (a, d, g, i) are black. Below it, three random samples of 4 balls each, drawn without putting a ball back. Right-hand column: the share of black balls in each row.|w=88]]

The figure is the bulb factory in miniature: the top row is the whole population (N = 10), each lower row is one sample (n = 4). The population's share of black balls is 4/10 = 0.4. The three samples give 0.25, 0.25 and 0.5: none of them is 0.4, and they disagree with each other.

**Answer to the Predict.** No. 1480 hours describes only the 100 bulbs tested. It is a guess at the average of all 500,000, and a second random 100 would give a slightly different number, just as the three ball samples gave 0.25, 0.25 and 0.5.

:::check Check 1
A university with 8,000 students asks 200 of them, chosen at random, how many hours they sleep. Name the population and the sample, and give N and n.
:::

### 2 · Parameter and statistic

Step 1 found two kinds of number: one that describes the whole population, and one computed from a sample. They get different names because they behave differently.

:::q Predict
In the ball figure, which number stays the same however many samples you draw: 0.4, or the share of black in a sample?
:::

:::guess Guess first
Pick one, and say why the other one moves.
:::

:::note Terms
**Parameter:** a number describing the population, such as μ (its mean) or σ (its SD). It is **fixed**; it is unknown only because we cannot measure every unit (G&K §12.3). **Statistic:** a number computed from the sample alone, such as x̄ (the sample mean) or s (the sample SD). It **changes from sample to sample**.
:::

| | Parameter | Statistic |
|---|---|---|
| describes | the population (all N units) | one sample (n units) |
| symbols | μ, σ | x̄, s |
| changes with the sample? | no | yes |
| balls | 0.4 black | 0.25, 0.25, 0.5 in the three samples |
| bulbs | average life of all 500,000 | 1480 h for the 100 tested |

**Answer to the Predict.** 0.4 stays fixed: it is a **parameter**, set by the 10 balls themselves. The share of black in a sample is a **statistic**: it depends on which 4 balls were drawn, so it moves.

:::check Check 2
Parameter or statistic? (a) The mean height of all students at the university. (b) The share of defective chips in a box of 50 chips that were inspected, used to judge the whole day's output. (c) The average of 60 marks, where the 60 students are the whole class being described.
:::

### 3 · The sampling distribution

Step 2 said a statistic changes from sample to sample. To see **how** it changes, list every sample.

:::q Predict
From 10 balls there are 210 different samples of 4. Over all 210, what share of black is the most common, and what is the average share?
:::

:::guess Guess first
Write one number for the most common share and one for the average.
:::

:::note Terms
**Score:** call a black ball 1 and a white ball 0. Then the share of black in a sample is the average of its four scores: it **is** the sample mean x̄. **Sampling distribution of x̄:** the list of every value x̄ can take, with how often each one happens, over **all** possible samples of size n (G&K §12.3).
:::

[[fig:ball_sampling|What this graph plots: all 210 samples of 4 from the 10 balls, sorted by their share of black. Horizontal axis: the share of black in the sample (x̄ of the 0/1 scores). Vertical axis: how many of the 210 samples have that share. Red dashed line: the population's share, 0.4.|w=78]]

| share of black (x̄) | 0 | 0.25 | 0.5 | 0.75 | 1 |
|---|---|---|---|---|---|
| black balls in the sample | 0 | 1 | 2 | 3 | 4 |
| samples (of 210) | 15 | 80 | 90 | 24 | 1 |

Read back: each count is (ways to pick the black balls) × (ways to pick the white ones), as in 01's counting; for 2 black, 6 × 15 = 90. The bars pile up around 0.4 and thin out at both ends.

**Answer to the Predict.** The most common share is **0.5** (90 samples). The average over all 210 samples is (0 × 15 + 0.25 × 80 + 0.5 × 90 + 0.75 × 24 + 1 × 1)/210 = 84/210 = **0.4**: exactly the population's share. Single samples miss, but on average x̄ hits the parameter.

:::check Check 3
Pick one of the 210 samples at random. (a) What is the chance its share of black is 0.5? (b) What is the chance it holds no black ball at all?
:::

### 4 · Standard error: the spread of the sampling distribution

Step 3's bars centre on 0.4 but are spread out. One number measures that spread.

:::q Predict
A typical sample's share of black misses 0.4 by about how much: 0.02, 0.2 or 0.5?
:::

:::guess Guess first
Look at the bar chart and pick one.
:::

:::note Terms
**Standard error (SE):** the standard deviation of the sampling distribution: how far x̄ typically lands from the centre, over all possible samples. G&K §12.3: "the standard deviation of the sampling distribution of a statistic is known as its standard error". It is an SD (03a step 6), with the 210 samples playing the part of the values.
:::

The figure is step 3's bar chart; the SE is computed from its table, as 03a computed a variance from a PMF:

1. Each sample's distance from the centre, squared: (0 − 0.4)² = 0.16, (0.25 − 0.4)² = 0.0225, (0.5 − 0.4)² = 0.01, (0.75 − 0.4)² = 0.1225, (1 − 0.4)² = 0.36.
2. Average over the 210 samples: (0.16 × 15 + 0.0225 × 80 + 0.01 × 90 + 0.1225 × 24 + 0.36 × 1)/210 = 8.4/210 = 0.04. This is the variance of x̄.
3. SE = √0.04 = **0.2**.

**Answer to the Predict.** About **0.2**: the SE of the share of black is 0.2. A typical sample lands about 0.2 away from 0.4, which is why the three samples in step 1 gave 0.25 and 0.5.

:::check Check 4
How many of the 210 samples have a share of black within 0.2 of 0.4 (that is, within one SE)? What fraction of all samples is that?
:::

### 5 · SE = σ/√n

Listing every sample worked for 10 balls. For 500,000 bulbs it is impossible, so the SE needs a formula.

:::q <span class="tag">Slides p.5</span>
A factory produces light bulbs with a known population SD σ = 100 hours. An inspector pulls a random sample of 25 bulbs. Find the standard error of the mean, and see what happens if n increases to 100.
:::

:::guess Guess first
One bulb varies by about 100 hours. Does the average of 25 bulbs vary by more than 100 hours, by exactly 100, or by less?
:::

:::note Terms
**σ:** the SD of **one** unit (one bulb's life), set by the population. **n:** how many independent units are averaged. **SE of x̄:** the SD of the average of n of them.
:::

The derivation uses only 03b's rules. Write X₁, …, Xₙ for the n values, drawn independently, each with mean μ and SD σ:

1. x̄ = (X₁ + X₂ + … + Xₙ)/n.
2. Mean of the sum: μ + μ + … + μ = nμ (03b step 2). Dividing by n: the mean of x̄ is **μ**.
3. Variance of the sum: σ² + σ² + … + σ² = nσ²; adding variances needs the draws to be **independent** (03b step 3).
4. Dividing by n divides the variance by n² (03b step 1): Var(x̄) = nσ²/n² = σ²/n.
5. SE = √(σ²/n) = **σ/√n**.

$$SE = \frac{σ}{\sqrt{n}}$$

Read back: σ = how much one unit varies; √n = how much averaging n units calms that down. Highs and lows in the sample partly cancel, so the average varies less than one unit does.

| n | 1 | 4 | 25 | 100 |
|---|---|---|---|---|
| SE = 100/√n (hours) | 100 | 50 | 20 | 10 |

**Answer to the question.** n = 25: SE = 100/√25 = 100/5 = **20 hours**. n = 100: SE = 100/√100 = 100/10 = **10 hours**. The average of 25 bulbs varies far less than one bulb does.

:::note Why the balls gave 0.2, not the formula's 0.245
One ball's score (1 or 0) has σ = √(0.4 × 0.6) = 0.49, so σ/√4 = 0.245, not step 4's 0.2. Line 3 needs independent draws; drawing 4 of only 10 balls without putting them back is not independent (each draw changes what is left), and it makes the SE smaller. With 500,000 bulbs, removing 25 changes almost nothing, so σ/√n holds.
:::

:::check Check 5
(a) <span class="tag">A4 MCQ 8</span> A sample has mean 40, SD 5, size 25. The standard error is: 5 / 2 / 1 / 0.2. (Use the sample SD s in place of σ.) (b) For the ATM (σ = 2 min, n = 36), find the SE of the average wait.
:::

### 6 · Four times the sample, half the SE

Step 5's n sits under a square root. That root decides how much a bigger sample buys.

:::q Predict
The bulbs' SE is 20 hours with n = 25. How many bulbs are needed to bring the SE down to 5 hours?
:::

:::guess Guess first
Is it 100 bulbs (four times the SE cut, four times the bulbs), or more?
:::

[[fig:se_n|What this graph plots: the SE of the average bulb life against the sample size, for σ = 100 hours. Horizontal axis: n, the number of bulbs averaged. Vertical axis: SE = 100/√n, in hours. Dots: n = 4, 25 and 100. From n = 25 to n = 100 (four times the bulbs) the SE only halves.|w=80]]

| n | 25 | 100 | 400 |
|---|---|---|---|
| √n | 5 | 10 | 20 |
| SE (hours) | 20 | 10 | 5 |

Read back: multiplying n by 4 multiplies √n by 2, so SE = σ/√n is divided by 2 (slides p.5: "quadrupling n halves SE"). To divide the SE by k, multiply n by k². The curve falls steeply at first and then flattens: each extra bulb buys less.

**Answer to the Predict.** SE = 100/√n = 5 needs √n = 20, so **n = 400**: cutting the SE to a quarter (20 → 5) takes 4² = 16 times the bulbs, not 4 times.

:::check Check 6
ATM waits, σ = 2 min. (a) Find the SE for n = 9 and for n = 144. (b) What sample size gives SE = 0.25 min?
:::

### 7 · The Central Limit Theorem

Steps 3–6 gave the centre (μ) and the spread (SE) of x̄. A probability also needs its **shape**, and the ATM waits are not normal.

:::q Predict
Single ATM waits are right-skewed: a long tail of slow customers. Draw the shape you expect for the average wait of 36 customers.
:::

:::guess Guess first
Skewed like the single waits, flat, or bell-shaped?
:::

:::note Terms
**Independent and identically distributed:** every value in the sample is drawn the same way from the same population, and no value affects another. **Approximately normal:** close enough to a normal curve that file 06's table gives the probabilities to about two decimal places.
:::

[[fig:clt_shapes|What this figure shows: four populations (columns: normal, flat, skewed, two humps), each sampled 20,000 times. Top row: histograms of single values. Middle row: histograms of the average of 10 values. Bottom row: the average of 30 values. Horizontal axis in every panel: the value, 0 to 10; the height is how often it occurs.|w=96]]

Read the columns top to bottom: whatever the top shape, the averages pile up in the middle, and by n = 30 every column is a narrow bell. The skewed column keeps a slight lean at n = 10 and has lost it by n = 30 (slide p.10 shows the same grid).

**Central Limit Theorem** (G&K §8.10; slides p.7). If X₁, …, Xₙ are independent and identically distributed with mean μ and finite SD σ, then for large n:

1. **Centre:** x̄ is centred on μ (step 5, line 2).
2. **Spread:** its SD is the SE, σ/√n (step 5, line 5).
3. **Shape:** it is approximately **normal**, whatever the population's shape.

$$Z = \frac{x̄ − μ}{σ/\sqrt{n}} ≈ N(0, 1)$$

Read back: subtract the centre and divide by the spread (06 step 3, with σ/√n in place of σ), and the result can be read off the Z table.

**Answer to the Predict.** A **bell**, centred on 4 min, with SD 2/√36 = 0.333 min. The single waits stay skewed; only their average becomes normal.

:::check Check 7
For the ATM (μ = 4, σ = 2, n = 36), give the centre, the spread and the shape of the average wait x̄.
:::

### 8 · When the CLT may be used

Step 7 said "for large n". The slides turn "large" into a rule, and add the case where no CLT is needed.

:::q <span class="tag">Slides p.8</span> (Predict)
Three situations: (i) skewed population, n = 64; (ii) normal population, n = 9; (iii) skewed population, n = 10. For which can the average be treated as normal?
:::

:::guess Guess first
Answer yes or no for each of the three.
:::

| Population | n | Shape of x̄ | Why |
|---|---|---|---|
| any shape | n ≥ 30 | approximately N(μ, σ²/n) | the CLT |
| normal | any n, even small | exactly N(μ, σ²/n) | a sum of normals is normal; no CLT needed |
| not normal | n < 30 | unknown | the CLT cannot be used yet |

:::note Slides p.7 and p.8 disagree slightly
Slide p.7 writes "n ≥ 30", slide p.8 writes "n > 30". The pack uses **n ≥ 30**. The number 30 is a rule of thumb for the course: G&K §8.10 states the theorem for n → ∞ and gives no cut-off.
:::

**Answer to the Predict.** (i) **Yes**: n = 64 ≥ 30, the CLT applies (this is the LED example, step 11). (ii) **Yes**, and exactly: the population is normal (the machine example, step 12). (iii) **No**: skewed and only 10 values.

:::check Check 8
Delivery times are strongly skewed, μ = 30 min, σ = 12 min. Can the normal table be used for the average of (a) n = 10 deliveries; (b) n = 64 deliveries? For (b), find the SE.
:::

### 9 · z for an average

Steps 5–8 give everything: x̄ is approximately normal with centre μ and SD σ/√n. Now file 06's method runs on averages.

:::q <span class="tag">Slides p.11–12</span>
Wait times at a bank ATM are heavily right-skewed. μ = 4 min, σ = 2 min. For a random sample of 36 customers, what is the probability that their average wait is greater than 4.5 minutes?
:::

:::guess Guess first
4.5 min is only half a minute above the mean. Is P(x̄ > 4.5) about 5%, 25% or 45%?
:::

:::note Terms
**z for an average:** z = (x̄ − μ)/SE: how many **SEs** (not σ's) the average sits from μ.
:::

[[fig:atm_tail|What this graph plots: the curve of the average wait of 36 customers, N(4, 0.333²). Horizontal axis: x̄, the average wait in minutes. Vertical axis: the height of the curve (areas are probabilities). Dotted line: μ = 4. Red: the averages above 4.5 min.|w=80]]

| x̄ (min) | 3.5 | 4 | 4.5 | 5 |
|---|---|---|---|---|
| z = (x̄ − 4)/0.333 | −1.5 | 0 | 1.5 | 3 |

Read back: 4.5 min is 1.5 SEs above the mean. For one customer, 4.5 min would be only 0.25 σ above; the average of 36 rarely strays that far.

**Answer to the question.**

1. Conditions: n = 36 ≥ 30, so x̄ is approximately normal (step 8), even though the waits are skewed.
2. SE = σ/√n = 2/√36 = 2/6 = 0.333 min.
3. z = (4.5 − 4)/0.333 = 1.5.
4. Upper tail (06 step 5): P(x̄ > 4.5) = 0.5 − φ(1.5) = 0.5 − 0.4332 = **0.0668**, about 6.7%.

:::check Check 9
ATM, n = 36. Find (a) P(x̄ < 3.5); (b) P(x̄ > 4.2). (φ(0.6) = 0.2257.)
:::

### 10 · An average between two values

Step 9 cut once. Two cuts on the same side of μ need a subtraction (06 step 6).

:::q <span class="tag">Slides p.13–14</span>
The amount of impurity in a batch of a chemical product is a random variable with mean 4.0 g and SD 1.5 g. If 50 batches are prepared independently, what is the approximate probability that the average impurity of these 50 batches is between 3.5 g and 3.8 g?
:::

:::guess Guess first
Both limits are below the mean 4.0. Will you add the two table areas or subtract them?
:::

[[fig:impur_band|What this graph plots: the curve of the average impurity of 50 batches, N(4, 0.2121²). Horizontal axis: x̄ in grams. Vertical axis: the height of the curve. Dotted line: μ = 4. Red: averages between 3.5 g and 3.8 g, both below the mean.|w=80]]

| x̄ (g) | 3.5 | 3.8 | 4.0 |
|---|---|---|---|
| z = (x̄ − 4)/0.2121 | −2.36 | −0.94 | 0 |
| φ(∣z∣): area from the mean to x̄ | 0.4909 | 0.3264 | 0 |

**Answer to the question.**

1. Conditions: n = 50 ≥ 30, so x̄ is approximately normal (the impurity's own shape is not given).
2. SE = 1.5/√50 = 1.5/7.071 = 0.2121 g.
3. z₁ = (3.5 − 4)/0.2121 = −2.36; z₂ = (3.8 − 4)/0.2121 = −0.94.
4. Both cuts are below the mean, so subtract: P = φ(2.36) − φ(0.94) = 0.4909 − 0.3264 = **0.1645**.

:::note Slide slip (p.14)
Slide p.14 prints the second limit as z = −0.4. The correct value is (3.8 − 4)/0.2121 = −0.94, and the slide's own next line uses φ(0.94) = 0.3264, so its answer 0.1644 is right to rounding (0.1645 here).
:::

:::check Check 10
Same batches. Find P(average impurity exceeds 4.3 g). (φ(1.41) = 0.4207.)
:::

### 11 · A lower tail

Step 9 was an upper tail. A "less than" question is the mirror image (06 step 5).

:::q <span class="tag">Slides p.15–16</span>
LED bulb lifespan is heavily skewed with mean 50,000 h and SD 8,000 h. For a sample of 64 bulbs, find the probability that the average lifespan is less than 48,000 h.
:::

:::guess Guess first
48,000 is 2,000 h below the mean. How many SEs is that?
:::

[[fig:led_tail|What this graph plots: the curve of the average life of 64 LED bulbs, N(50,000, 1,000²). Horizontal axis: x̄ in hours. Vertical axis: the height of the curve. Dotted line: μ = 50,000. Red: averages below 48,000 h.|w=80]]

| x̄ (h) | 48,000 | 49,000 | 50,000 | 51,000 |
|---|---|---|---|---|
| z = (x̄ − 50,000)/1,000 | −2 | −1 | 0 | 1 |

**Answer to the question.**

1. Conditions: skewed, but n = 64 ≥ 30: the CLT applies.
2. SE = 8,000/√64 = 8,000/8 = 1,000 h.
3. z = (48,000 − 50,000)/1,000 = −2.
4. Lower tail = upper tail by symmetry: P(x̄ < 48,000) = 0.5 − φ(2) = 0.5 − 0.4772 = **0.0228**.

:::check Check 11
Same bulbs. Find P(48,000 < x̄ < 51,000). (φ(1) = 0.3413, φ(2) = 0.4772.)
:::

### 12 · Normal population, small sample

Steps 9–11 all had n ≥ 30. The last slide example has n = 9, which step 8 allows only for a normal population.

:::q <span class="tag">Slides p.17–18</span>
The average life of a machine is 7 years with SD 1 year, and lives follow a normal distribution. Find the probability that the average life of 9 random machines falls between 6.4 and 7.2 years.
:::

:::guess Guess first
n = 9 is far below 30. Can the normal table still be used? Why?
:::

[[fig:machine_two|What this graph plots: two curves on one axis. Horizontal axis: life in years. Vertical axis: the height of each curve. Grey: the life of one machine, N(7, 1²). Blue: the average life of 9 machines, N(7, (1/3)²), three times narrower. Red: averages between 6.4 and 7.2 years.|w=80]]

| x̄ (years) | 6.4 | 7 | 7.2 |
|---|---|---|---|
| z = (x̄ − 7)/(1/3) | −1.8 | 0 | 0.6 |
| φ(∣z∣) | 0.4641 | 0 | 0.2257 |

**Answer to the question.**

1. Conditions: n = 9 < 30, but the population is normal, so x̄ is **exactly** normal (step 8, row 2): no CLT is needed.
2. SE = 1/√9 = 1/3 year.
3. z₁ = (6.4 − 7)/(1/3) = −1.8; z₂ = (7.2 − 7)/(1/3) = 0.6.
4. The cuts are on opposite sides of the mean, so add: P = φ(1.8) + φ(0.6) = 0.4641 + 0.2257 = **0.6898**.

:::check Check 12
(a) Same machines, n = 9: find P(x̄ > 7.5). (φ(1.5) = 0.4332.) (b) Why could the same method not be used for the LED bulbs of step 11 with n = 9?
:::

---

## Exam form

**Definitions** (G&K §12.3). Population: all the units of interest (size N). Sample: the units measured, chosen at random (size n). Parameter: a fixed number describing the population (μ, σ). Statistic: a number computed from the sample alone (x̄, s); it varies from sample to sample. Sampling distribution: the values of a statistic over all possible samples of size n. Standard error: the SD of a statistic's sampling distribution.

**Standard error of the mean.** For n independent values with mean μ and SD σ: E(x̄) = μ, Var(x̄) = σ²/n, **SE = σ/√n** (s in place of σ when σ is not given). Quadrupling n halves the SE.

**Central Limit Theorem** (G&K §8.10, Lindeberg–Lévy form). If X₁, …, Xₙ are independent and identically distributed with mean μ and finite variance σ², then as n → ∞, P(a ≤ (x̄ − μ)/(σ/√n) ≤ b) → Φ(b) − Φ(a): the sample mean is approximately N(μ, σ²/n) whatever the population's distribution. Course rule: n ≥ 30 is large enough. If the population is normal, x̄ is exactly N(μ, σ²/n) for every n.

**Procedure for a probability about x̄.**

1. Conditions: n ≥ 30, or a normal population. (Neither: the CLT cannot be used.)
2. SE = σ/√n.
3. z = (x̄ − μ)/SE for each limit.
4. Area from the table (06 steps 5–6): tail = 0.5 − φ(z); opposite sides add; same side subtract.
5. One line of conclusion in words.

## Traps

- Dividing by σ instead of σ/√n in the z for an average.
- "The CLT makes the data normal": only the **average** (or sum) becomes normal; single values keep their shape.
- Using the CLT for a skewed population with n < 30.
- Expecting 4 times the sample to give a quarter of the SE: it gives half (16 times the sample for a quarter).
- Calling a sample's x̄ a parameter: it changes with the sample, so it is a statistic.
- Two limits on the same side of μ: subtract the table areas, do not add.

## Self-test

1. Give one example of a parameter and one of a statistic for the ATM waits.
2. State the Central Limit Theorem with its three parts (centre, spread, shape) and its condition.
3. σ = 12 and n = 36. Find the SE. What n gives SE = 1?
4. A population has μ = 80, σ = 15. For n = 100, find P(77 < x̄ < 83). (φ(2) = 0.4772.)
5. Why does the machine example (step 12) need no CLT?
6. For the ATM data, what sample size makes P(x̄ > 4.5) = 0.0228? (φ(2) = 0.4772.)
7. A population has σ = 20. A sample of 25 gives SE = 4. How many times larger must the sample be to make SE = 1?

<!--ANSWERS-->
## Answers

**Check 1.** Population: all 8,000 students, N = 8,000. Sample: the 200 asked, n = 200.

**Check 2.** (a) **Parameter**: it describes every student. (b) **Statistic**: computed from the 50 inspected chips, used to judge the day's output. (c) **Parameter**: the 60 students are the whole population being described.

**Check 3.** (a) 90/210 = **3/7 ≈ 0.4286**. (b) 15/210 = **1/14 ≈ 0.0714**.

**Check 4.** Shares 0.25 and 0.5 lie within 0.2 of 0.4: 80 + 90 = **170 samples**, 170/210 ≈ **81%**.

**Check 5.** (a) SE = 5/√25 = 5/5 = **1**. (b) SE = 2/√36 = 2/6 = **0.333 min**.

**Check 6.** (a) n = 9: 2/3 = **0.667 min**; n = 144: 2/12 = **0.167 min**. (b) 2/√n = 0.25 gives √n = 8, so **n = 64**.

**Check 7.** Centre μ = **4 min**; spread SE = **0.333 min**; shape **approximately normal** (n = 36 ≥ 30).

**Check 8.** (a) **No**: skewed and n = 10 < 30. (b) **Yes**: n = 64 ≥ 30; SE = 12/√64 = 12/8 = **1.5 min**.

**Check 9.** (a) z = (3.5 − 4)/0.333 = −1.5: P = 0.5 − 0.4332 = **0.0668**. (b) z = (4.2 − 4)/0.333 = 0.6: P = 0.5 − 0.2257 = **0.2743**.

**Check 10.** z = (4.3 − 4)/0.2121 = 1.41: P = 0.5 − 0.4207 = **0.0793**.

**Check 11.** z = −2 and z = 1, opposite sides, so add: 0.4772 + 0.3413 = **0.8185**.

**Check 12.** (a) z = (7.5 − 7)/(1/3) = 1.5: P = 0.5 − 0.4332 = **0.0668**. (b) The LED lives are skewed, and n = 9 < 30: x̄'s shape is unknown, so the CLT cannot be used (step 8, row 3).

**Self-test.**

1. Parameter: μ = 4 min, the mean wait of all customers. Statistic: x̄, the average wait of the 36 customers sampled.
2. If X₁, …, Xₙ are independent and identically distributed with mean μ and finite SD σ, then for large n (course rule n ≥ 30) the sample mean x̄ is centred on μ, has SD σ/√n, and is approximately normal whatever the population's shape.
3. SE = 12/√36 = 12/6 = **2**; 12/√n = 1 gives **n = 144**.
4. SE = 15/10 = 1.5; z = (77 − 80)/1.5 = −2 and (83 − 80)/1.5 = 2; P = 2 × 0.4772 = **0.9544**.
5. The machine lives are normal, so x̄ is exactly normal for any n (step 8, row 2).
6. Need (4.5 − 4)/(2/√n) = 2, so √n = 2 × 2/0.5 = 8: **n = 64**.
7. SE = 20/√n = 1 needs √n = 20, n = 400 = **16 times** 25.
<!--/ANSWERS-->
