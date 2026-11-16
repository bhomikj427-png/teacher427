# 09a — Method of moments

<div class="sub">Gupta & Kapoor §15.13 (method of moments and its remarks) · blueprint row 3 "methods of estimation: MoM and MLE" · 3 real questions (G&K ch. 15 ex. 20(b), 21, 23(b)(i)) · needs 03a (E(X) step 1, E(X²) step 3, shortcut variance step 5), 05 (exponential and uniform means), 08 (estimator and estimate, step 1)</div>

## Map

[[map:1 Population and sample moments > 2 One parameter: match the mean > 3 When the estimate is impossible > 4 Two parameters: match two moments > 5 MoM on a new density|here=1]]

File 08 judged estimators that were handed to you (x̄, the larger throw, T₁). This file **builds** one from scratch by the oldest recipe: the population's averages are formulas in the unknown parameter; the sample's averages are numbers; set them equal and solve. File 09b builds estimators the other way (maximum likelihood) and compares the two on the same data.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| θ | the unknown parameter of the population ("theta"); here the exponential's rate | θ̂ = 1/3 per minute |
| μ′ᵣ | r-th population moment E(X^{r}): the long-run average of X^{r}; a formula in θ | μ′₁ = 1/θ |
| m′ᵣ | r-th sample moment (1/n)Σxᵢ^{r}: the average of xᵢ^{r} over the data; a number | m′₁ = x̄ = 3 |
| m₂ | the sample variance with divisor n: m′₂ − (m′₁)^{2} = (1/n)Σ(xᵢ − x̄)^{2} | 2.5 |
| θ̂ | the estimate: the θ that makes the population moment equal the sample moment ("theta hat") | 1/3 |
| a, b | the ends of a uniform distribution U(a, b) (step 4) | 7.26, 12.74 |

**Running example.** Waiting times at a bus stop (minutes): 2, 5, 1, 4. The model is exponential with rate θ (05): f(x, θ) = θe^{−θx}, x > 0, whose mean is 1/θ. The data average x̄ = 12/4 = **3** minutes. Steps 2 and 3 use it; step 1 starts from the die of 08.

## The questions this file answers

- <span class="tag">G&K ch. 15 ex. 20(b)</span> Let X₁, X₂, …, Xₙ be a random sample from f(x, θ) = θe^{−θx}, 0 < x < ∞, θ > 0. Estimate θ using the method of moments.
- <span class="tag">G&K ch. 15 ex. 21</span> X₁, X₂, …, Xₙ is a random sample from f(x; a, b) = 1/(b − a), a < x < b. Find estimates of a and b by the method of moments.
- <span class="tag">G&K ch. 15 ex. 23(b)(i)</span> The sample values from a population with pdf f(x) = (1 + θ)x^{θ}, 0 < x < 1, θ > 0, are 0.46, 0.38, 0.61, 0.82, 0.59, 0.53, 0.72, 0.44, 0.59, 0.60. Find the estimate of θ by the method of moments.

Estimation is 22 of the ETE's 80 marks (blueprint row 3); "find the estimator by the method of moments" is a standard 4–6 mark part.

---

## Build

### 1 · Population moments and sample moments

Start from the die of 08: a population you know completely, and a sample of four throws: 2, 6, 5, 3.

:::q Predict
For the die, the average face is 3.5. What is the average of the **squared** face, 1² to 6²? For the four throws, what are the average throw and the average squared throw?
:::

:::guess Guess first
Write the four numbers: die average, die average square, sample average, sample average square.
:::

:::note Terms
**r-th population moment** μ′ᵣ = E(X^{r}): the long-run average of X^{r} (03a steps 1 and 3). It is set by the population, so it is a formula in the parameters. **r-th sample moment** m′ᵣ = (1/n)Σxᵢ^{r}: the plain average of xᵢ^{r} over the n data values. It is set by the data, so it is a number. (G&K §15.13.)
:::

| r | population (die) μ′ᵣ | sample 2, 6, 5, 3: m′ᵣ |
|---|---|---|
| 1 | (1 + 2 + … + 6)/6 = **3.5** | (2 + 6 + 5 + 3)/4 = **4** |
| 2 | (1 + 4 + 9 + 16 + 25 + 36)/6 = 91/6 = **15.17** | (4 + 36 + 25 + 9)/4 = 74/4 = **18.5** |

**Answer to the Predict.** Die: 3.5 and 15.17. Sample: 4 and 18.5. The sample moments are close to the population ones but not equal: four throws do not reproduce the die exactly. With more throws they get closer (08 step 6, consistency).

The two kinds of moment are the two sides of every method-of-moments equation: **formula in θ = number from data**.

:::check Check 1
Three throws give 1, 4, 4. Find m′₁ and m′₂.
:::

### 2 · One parameter: match the mean

The die's moments were known. Now the population has an unknown θ, so its mean is a formula in θ; the data's mean is still a number.

:::q <span class="tag">G&K ch. 15 ex. 20(b)</span>
Let X₁, X₂, …, Xₙ be a random sample from f(x, θ) = θe^{−θx}, 0 < x < ∞, θ > 0. Estimate θ using the method of moments.
:::

:::guess Guess first
The bus waits 2, 5, 1, 4 minutes average 3. If the model's mean is 1/θ, which θ makes the model's mean 3?
:::

:::note Terms
**Method of moments (MoM):** with k unknown parameters, set the first k population moments equal to the first k sample moments, μ′ᵣ = m′ᵣ for r = 1, …, k, and solve for the parameters (G&K §15.13). One parameter needs one equation: the mean.
:::

[[fig:mom_match|What this graph plots: the model's mean 1/θ (curve) against the rate θ. Horizontal axis: θ (per minute). Vertical axis: mean waiting time (minutes). Dashed line: the sample mean x̄ = 3. The method of moments picks the θ where the curve crosses the dashed line.|w=78]]

**Reading the figure.**

| θ (per minute) | model mean 1/θ (minutes) | compared with x̄ = 3 |
|---|---|---|
| 0.20 | 5 | too long |
| 0.25 | 4 | too long |
| **1/3** | **3** | **equal: the estimate** |
| 0.50 | 2 | too short |

**Derivation** (each line from the one before):

1. Population mean of the exponential (05): μ′₁ = E(X) = 1/θ.
2. Sample mean: m′₁ = x̄.
3. Match them: 1/θ = x̄.
4. Solve: **θ̂ = 1/x̄**.

**Answer to the question.** θ̂ = 1/x̄: the rate is estimated by one over the average waiting time. For the bus data, θ̂ = 1/3 ≈ **0.333 per minute**: on average one bus every 3 minutes.

:::note Letter
G&K prints the parameter as θ in this exercise; the v1.2 pack wrote α. The answer is the same whatever the letter.
:::

:::check Check 2
Waiting times 0.5, 1.5, 2.0, 4.0 minutes, same model. Find θ̂ by the method of moments.
:::

### 3 · When the estimate is impossible

Matching the mean always gives a number. That number need not fit the data.

:::q Predict
A sample 2, 5, 7, 10 comes from U(0, θ): every value between 0 and θ equally likely. Find θ̂ by matching the mean. Then do the same for the sample 1, 1, 10. Is the second estimate possible?
:::

:::guess Guess first
The mean of U(0, θ) is the midpoint θ/2 (05). Write both estimates, and "possible / impossible" for the second.
:::

**Derivation.**

1. μ′₁ = θ/2 (midpoint of 0 to θ).
2. Match: θ/2 = x̄.
3. Solve: θ̂ = 2x̄.

**Answer to the Predict.** First sample: x̄ = 24/4 = 6, so θ̂ = **12**. Every value (largest 10) lies below 12: possible. Second sample: x̄ = 12/3 = 4, so θ̂ = **8**. But a value of 10 was observed, and U(0, 8) cannot produce 10: the estimate is **impossible**.

The method of moments uses only the averages, so it can ignore what single values say. 09b step 9 shows that maximum likelihood here gives the largest value instead, which is never impossible.

:::check Check 3
A sample 1, 2, 9 comes from U(0, θ). Find θ̂ by the method of moments and say whether it is possible.
:::

### 4 · Two parameters: match two moments

U(0, θ) had one unknown end. If both ends a and b are unknown, one equation cannot fix two numbers.

:::q <span class="tag">G&K ch. 15 ex. 21</span>
X₁, X₂, …, Xₙ is a random sample from f(x; a, b) = 1/(b − a), a < x < b. Find estimates of a and b by the method of moments.
:::

:::guess Guess first
The mean of U(a, b) is (a + b)/2 and its variance is (b − a)²/12 (05). How many equations do you need, and which two would you use?
:::

:::note Terms
**m₂** (the second sample moment about the mean) = (1/n)Σ(xᵢ − x̄)^{2} = m′₂ − (m′₁)^{2}: the data's variance with divisor n. It plays the part of the population variance μ′₂ − (μ′₁)^{2} (03a step 5). Matching mean and variance is the same as matching the first two moments.
:::

[[fig:mom_uniform|What this graph plots: the four data values 8, 9, 11, 12 (dots on the axis) and the fitted uniform density (rectangle) from â = 7.26 to b̂ = 12.74, height 1/(b̂ − â). Horizontal axis: x. Vertical axis: density f(x).|w=72]]

**Derivation.**

1. Match the means: (a + b)/2 = x̄, so b + a = 2x̄.
2. Match the variances: (b − a)^{2}/12 = m₂, so b − a = √(12m₂) = 2√(3m₂) (b > a, so the positive root).
3. Add lines 1 and 2 and halve: b̂ = x̄ + √(3m₂).
4. Subtract and halve: â = x̄ − √(3m₂).

$$â = x̄ − √(3m_{2}),    b̂ = x̄ + √(3m_{2})$$

Read in words: the ends sit √(3m₂) either side of the data's centre; a wider spread of data gives a wider rectangle.

**Answer to the question**, on the data 8, 9, 11, 12: x̄ = 40/4 = **10**; m′₂ = (64 + 81 + 121 + 144)/4 = 102.5; m₂ = 102.5 − 10² = **2.5**; √(3 × 2.5) = √7.5 = **2.739**. So â = 10 − 2.739 = **7.26** and b̂ = 10 + 2.739 = **12.74**.

:::check Check 4
A sample has x̄ = 10 and m₂ = 3. Find â and b̂ for U(a, b).
:::

### 5 · Method of moments on a new density

The densities so far had means you could look up in 05. For an unfamiliar density, first find the mean by integrating (02b, 03a step 7), then match.

:::q <span class="tag">G&K ch. 15 ex. 23(b)(i)</span>
The sample values from a population with pdf f(x) = (1 + θ)x^{θ}, 0 < x < 1, θ > 0, are 0.46, 0.38, 0.61, 0.82, 0.59, 0.53, 0.72, 0.44, 0.59, 0.60. Find the estimate of θ by the method of moments.
:::

:::guess Guess first
Larger θ pushes the density towards x = 1. Will the data's mean (about 0.57) give a small θ or a large one?
:::

**Derivation.**

1. E(X) = ∫₀¹ x · (1 + θ)x^{θ} dx = (1 + θ)∫₀¹ x^{θ+1} dx.
2. = (1 + θ) · \frac{1}{θ + 2} = \frac{1 + θ}{θ + 2}.
3. Match to the sample mean: \frac{1 + θ}{θ + 2} = x̄.
4. Multiply out: x̄θ + 2x̄ = 1 + θ.
5. Collect θ: θ(x̄ − 1) = 1 − 2x̄, so θ̂ = \frac{2x̄ − 1}{1 − x̄}.

**Answer to the question.** Σxᵢ = 5.74, so x̄ = **0.574**. θ̂ = (2 × 0.574 − 1)/(1 − 0.574) = 0.148/0.426 = **0.3474**: a small θ, as the mean is only a little above ½ (θ = 0 gives the flat density, mean ½).

:::note How good is a MoM estimator? (G&K §15.13, remarks)
MoM estimators are consistent and, for large n, approximately normal. They are **generally less efficient** than maximum-likelihood estimators (larger spread, 08 step 7); the two methods coincide only for special densities. 09b step 11 finds the MLE on these same ten values: 0.7279, not 0.3474.
:::

:::check Check 5
Same density, a different sample with x̄ = 0.6. Find θ̂ by the method of moments.
:::

---

## Exam form

**Method of moments** (G&K §15.13).

1. Count the unknown parameters: k.
2. Write the population moments μ′ᵣ = E(X^{r}) for r = 1, …, k as formulas in the parameters (look them up, or integrate).
3. Write the sample moments m′ᵣ = (1/n)Σxᵢ^{r} (or use x̄ and m₂ = (1/n)Σ(xᵢ − x̄)^{2}).
4. Set μ′ᵣ = m′ᵣ and solve; put hats on the answers.

**Standard results.**

| Population | MoM estimator |
|---|---|
| Exponential f = θe^{−θx} (rate θ) | θ̂ = 1/x̄ |
| Exponential with mean β | β̂ = x̄ |
| Poisson(λ) | λ̂ = x̄ |
| U(0, θ) | θ̂ = 2x̄ |
| U(a, b) | â = x̄ − √(3m₂), b̂ = x̄ + √(3m₂) |
| Normal (μ, σ²) | μ̂ = x̄, σ̂² = m₂ (divisor n) |
| (1 + θ)x^{θ}, 0 < x < 1 | θ̂ = (2x̄ − 1)/(1 − x̄) |

## Traps

- Matching the variance with divisor n − 1: the method of moments uses m₂ with divisor n.
- Setting the rate equal to x̄: the exponential's **mean** is 1/θ, so θ̂ = 1/x̄.
- Forgetting the positive root in b − a = √(12m₂).
- Using one equation for two unknowns: k parameters need k moments.
- Not checking the estimate against the data: U(0, θ) can give θ̂ below the largest value.

## Self-test

1. Define the r-th population moment and the r-th sample moment, and say which one depends on the parameter.
2. Find the MoM estimator of λ for a Poisson sample, and the estimate for the data 2, 0, 3, 1, 4.
3. Find the MoM estimator of β for f(x) = (1/β)e^{−x/β}, x > 0.
4. A sample 3, 5, 10 comes from U(0, θ). Find θ̂ by the method of moments.
5. A normal sample 4, 6, 8 has both parameters unknown. Find μ̂ and σ̂² by the method of moments.
6. f(x) = θx^{θ−1}, 0 < x < 1, θ > 0, has mean θ/(θ + 1). Find the MoM estimator of θ, and its value when x̄ = 0.75.

<!--ANSWERS-->
## Answers

**Check 1.** m′₁ = (1 + 4 + 4)/3 = **3**; m′₂ = (1 + 16 + 16)/3 = **11**.

**Check 2.** x̄ = 8/4 = 2, so θ̂ = 1/2 = **0.5 per minute**.

**Check 3.** x̄ = 12/3 = 4, θ̂ = 2 × 4 = **8**. **Impossible**: the value 9 was observed and U(0, 8) cannot produce it.

**Check 4.** √(3 × 3) = 3: â = 10 − 3 = **7**, b̂ = 10 + 3 = **13**.

**Check 5.** θ̂ = (1.2 − 1)/(1 − 0.6) = 0.2/0.4 = **0.5**.

**Self-test.**

1. μ′ᵣ = E(X^{r}), set by the population, so it depends on the parameter; m′ᵣ = (1/n)Σxᵢ^{r}, a number from the data.
2. E(X) = λ = x̄, so **λ̂ = x̄**; data: x̄ = 10/5 = **2**.
3. E(X) = β = x̄, so **β̂ = x̄**.
4. x̄ = 18/3 = 6, θ̂ = **12** (possible: 10 < 12).
5. μ̂ = x̄ = **6**; σ̂² = m₂ = (4 + 0 + 4)/3 = **8/3 ≈ 2.67**.
6. θ/(θ + 1) = x̄ ⇒ θ = x̄θ + x̄ ⇒ **θ̂ = x̄/(1 − x̄)**; x̄ = 0.75 gives θ̂ = 0.75/0.25 = **3**.
<!--/ANSWERS-->
