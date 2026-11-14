# 08 — Estimators and the four properties of a good one

<div class="sub">Gupta & Kapoor ch. 15 (§15.1–15.6), §12.11 · blueprint row 3 "parameter and statistic, point and interval estimation; characteristics of a good estimator" · 2 real questions (MTE) + Gupta & Kapoor exercises · needs 03, 07</div>

## Map

[[map:1 Estimator, point and interval > 2 Unbiased > 3 Why s² divides by n − 1 > 4 Consistent > 5 Efficient > 6 Sufficient|here=1]]

## The questions this file answers

- <span class="tag">MTE C1(b) · 3 marks</span> X₁, X₂, X₃ is a random sample from a population with mean μ and variance σ^{2}. T₁ = X₁ + X₂ − X₃ and T₂ = 3X₁ + 2X₃ − 3X₂. Which is an unbiased estimator of μ? Justify.
- <span class="tag">MTE A3 · 2 marks</span> If an estimator t contains all the information of the sample regarding the parameter θ, it is called: efficient / sufficient / consistent / unbiased.
- <span class="tag">G&K ch. 15 objective Q1</span> True or false: "an unbiased estimator is necessarily consistent"; "a maximum likelihood estimator is always unbiased"; "an unbiased estimator whose variance tends to zero as the sample size increases is consistent".

Blueprint row 3 (estimation) is the heaviest row: 22 of 80 marks, with one 2-mark, two 6-mark and one 8-mark question.

---

## Build

### 1 · Estimator; point and interval estimation

File 07 showed that x̄ varies around μ. Estimation asks how to choose such a statistic well.

:::q Predict
To estimate the mean lifetime μ of all bulbs, you could use the sample mean, the sample median, or (largest + smallest)/2. How would you decide which is best?
:::

:::guess Guess first
Write one property you would want the chosen rule to have.
:::

**Terms** (G&K §15.1):

- **Estimator**: a statistic T (a formula in X₁, …, Xₙ) used to estimate a parameter θ. Its value for one sample is an **estimate**.
- **Point estimation**: one number for θ (x̄ = 1480 h).
- **Interval estimation**: a range with a stated confidence (1450 to 1510 h, 95% confidence): file 11.

**Answer.** Judge a rule by how its estimates behave over many samples: centred on θ (**unbiased**), closing in on θ as n grows (**consistent**), with small spread (**efficient**), and using all the information in the data (**sufficient**).

[[fig:targets|Each dot is the estimate from one sample. Unbiased: centred on θ. Efficient: tightly packed.|w=92]]

:::check Check 1
Point or interval? (a) "The mean is 12.5 g/dL." (b) "The mean is between 12.1 and 12.9 g/dL with 95% confidence."
:::

### 2 · Unbiased

:::q <span class="tag">MTE C1(b) · 3 marks</span>
Let X₁, X₂, X₃ be a random sample of size 3 from a population with mean μ and variance σ^{2}. T₁ = X₁ + X₂ − X₃ and T₂ = 3X₁ + 2X₃ − 3X₂ are used to estimate μ. Which of T₁, T₂ is unbiased? Justify your answer.
:::

:::guess Guess first
Add up the coefficients in each formula. What do you notice?
:::

**Term.** T is an **unbiased** estimator of θ if E(T) = θ for every θ (G&K §15.4). Otherwise E(T) − θ is the **bias**.

Each Xᵢ has E(Xᵢ) = μ; expectation is linear (file 03), so E(Σcᵢ Xᵢ) = (Σcᵢ)μ. A linear estimator is unbiased for μ exactly when its coefficients add to 1.

**Answer.**
E(T₁) = E(X₁) + E(X₂) − E(X₃) = μ + μ − μ = μ ⇒ **T₁ is unbiased**.
E(T₂) = 3μ + 2μ − 3μ = 2μ ≠ μ ⇒ **T₂ is biased** (bias = μ).

:::check Check 2
For the same sample, find λ so that T₃ = (λX₁ + X₂ + X₃)/3 is unbiased for μ.
:::

### 3 · Why the sample variance divides by n − 1

The most-used unbiased estimator in the course is s^{2}. Its divisor is the reason the t, F and χ² formulas use n − 1.

:::q Predict
For a normal population with σ^{2} = 4, many samples of size 3 are drawn. For each, compute Σ(xᵢ − x̄)^{2}/3. Will the average of these values be 4, more than 4, or less than 4?
:::

:::guess Guess first
x̄ is the centre of the sample itself. Are values closer to x̄ or to μ?
:::

**Answer.** **Less than 4**: about 8/3 ≈ 2.67. Deviations are measured from x̄, which sits inside the sample, so they are smaller than deviations from μ. The exact result (G&K §12.11):

$$E[Σ(Xᵢ − X̄)^{2}] = (n − 1)σ^{2}  ⇒  s^{2} = \frac{1}{n − 1} Σ(xᵢ − x̄)^{2}  is unbiased for σ^{2}$$

Dividing by n gives a biased estimator with E = \frac{n − 1}{n}σ^{2}. **n − 1 = degrees of freedom**: once x̄ is fixed, only n − 1 of the deviations are free.

:::note Notation in this pack
Gupta & Kapoor sometimes write s^{2} for the n-divisor and S^{2} for the (n − 1)-divisor. This pack writes **s^{2} with n − 1** throughout, and says so wherever a question's data could be read either way.
:::

:::check Check 3
Data 4, 6, 8. Compute Σ(x − x̄)^{2}/n and s^{2}.
:::

### 4 · Consistent

Unbiased is about the centre at one n. Consistency is about what happens as n grows.

:::q <span class="tag">G&K ch. 15 objective Q1 (iv), (vi)</span>
True or false: (iv) an unbiased estimator is necessarily consistent; (vi) an unbiased estimator whose variance tends to zero as the sample size increases is consistent.
:::

:::guess Guess first
T₁ = X₁ + X₂ − X₃ uses three observations however large the sample. Does it get better with n?
:::

**Term.** Tₙ is **consistent** for θ if Tₙ gets arbitrarily close to θ with probability → 1 as n → ∞ (G&K §15.3).

**Sufficient condition** (G&K Theorem 15.2): E(Tₙ) → θ **and** Var(Tₙ) → 0.

**Answer.** (iv) **False**: T₁ is unbiased but its variance stays 3σ^{2} for every n, so it never closes in on μ. (vi) **True**: that is the sufficient condition. Example: x̄ has E = μ and Var = σ^{2}/n → 0, so x̄ is consistent. File 07's LLN (G&K §6.15) is the same fact.

:::check Check 4
X is the number of successes in n trials with probability p. Is X/n a consistent estimator of p? Use the condition.
:::

### 5 · Efficient

Two unbiased estimators: prefer the one with less spread.

:::q Predict
For the MTE sample of size 3, both T₁ = X₁ + X₂ − X₃ and X̄ = (X₁ + X₂ + X₃)/3 are unbiased for μ. Which would you use?
:::

:::guess Guess first
Compute or guess each variance in terms of σ^{2}.
:::

**Term.** Of two unbiased estimators, T is **more efficient** than T′ if Var(T) < Var(T′). The **efficiency** of T′ relative to T is Var(T)/Var(T′) (G&K §15.5). The most efficient one is the minimum-variance unbiased estimator.

**Answer.** By file 03 (independent Xᵢ, variances add with squared coefficients):
Var(T₁) = (1 + 1 + 1)σ^{2} = **3σ^{2}**. Var(X̄) = (1/9)(3σ^{2}) = **σ^{2}/3**.
X̄ is 9 times more efficient (efficiency of T₁ relative to X̄ = (σ^{2}/3)/(3σ^{2}) = 1/9). Use **X̄**.

:::check Check 5
T₄ = (X₁ + 2X₂ + X₃)/4. Is it unbiased? Find Var(T₄) and its efficiency relative to X̄.
:::

### 6 · Sufficient

The last property is about information, not centre or spread.

:::q <span class="tag">MTE A3 · 2 marks</span>
If an estimator t contains all the information of the sample regarding the population parameter θ, it is called: (a) efficient (b) sufficient (c) consistent (d) unbiased
:::

:::guess Guess first
Pick from the definitions you now have.
:::

**Term.** T is **sufficient** for θ if, once T is known, the rest of the sample carries no further information about θ (G&K §15.6). **Factorisation test:** the likelihood L (file 09) splits as L = g(T, θ) · h(x), where h does not contain θ.

**Example.** Poisson sample: L = e^{−nλ}λ^{Σxᵢ}/Πxᵢ!. θ = λ appears only through Σxᵢ, so **Σxᵢ (and x̄) is sufficient** for λ.

**Answer.** **Sufficient** (b).

:::check Check 6
<span class="tag">G&K ch. 15 objective Q1 (iii)</span> True or false: "a maximum likelihood estimator is always unbiased." (Hint: file 09 shows that the MLE of σ^{2} divides by n.)
:::

---

## Exam form

**Definitions** (write all four when asked for "characteristics of a good estimator"):

1. **Unbiased**: E(T) = θ.
2. **Consistent**: T → θ in probability as n → ∞; sufficient condition E(T) → θ and Var(T) → 0.
3. **Efficient**: among unbiased estimators, the smallest variance; efficiency of T′ relative to T = Var(T)/Var(T′).
4. **Sufficient**: uses all the sample's information about θ; L = g(T, θ)h(x).

**Standard results.** x̄ is unbiased, consistent and (normal population) efficient for μ. s^{2} = Σ(x − x̄)^{2}/(n − 1) is unbiased for σ^{2}; the n-divisor version is biased but consistent.

**Procedure (is T unbiased?).** Take E of each term (E(Xᵢ) = μ), add, compare with θ, state "unbiased" or "biased, bias = …".

## Traps

- Calling an estimator unbiased because it "looks like" the mean: check the coefficients add to 1.
- Unbiased does not imply consistent, and consistent does not imply unbiased.
- Var(aX₁ − bX₂) = (a^{2} + b^{2})σ^{2}: the minus sign does not subtract variances.
- Swapping "efficient" (small variance) and "sufficient" (all the information).

## Self-test

1. Define unbiased, consistent, efficient and sufficient estimators.
2. X₁, X₂ from a population with mean μ. Is (2X₁ + 3X₂)/5 unbiased? Is (X₁ + X₂)/3?
3. Find the variances of the two estimators in Q2 (variance σ^{2}).
4. Why is s^{2} divided by n − 1?
5. Give an estimator that is unbiased but not consistent.
6. For a Poisson sample, which statistic is sufficient for λ?

<!--ANSWERS-->
## Answers

**Check 1.** (a) point (b) interval.

**Check 2.** E(T₃) = (λ + 2)μ/3 = μ ⇒ **λ = 1**.

**Check 3.** x̄ = 6; Σ(x − x̄)^{2} = 4 + 0 + 4 = 8. n-divisor: 8/3 = **2.67**; s^{2} = 8/2 = **4**.

**Check 4.** E(X/n) = np/n = p and Var(X/n) = npq/n^{2} = pq/n → 0: **consistent**.

**Check 5.** E = (1 + 2 + 1)μ/4 = μ: **unbiased**. Var = (1 + 4 + 1)σ^{2}/16 = **3σ^{2}/8**. Efficiency relative to X̄ = (σ^{2}/3)/(3σ^{2}/8) = **8/9**.

**Check 6.** **False**: the MLE of σ^{2} is Σ(x − x̄)^{2}/n, which is biased.

**Self-test.**

1. See Exam form.
2. Coefficients 2/5 + 3/5 = 1: **unbiased**. 1/3 + 1/3 = 2/3: **biased** (E = 2μ/3).
3. (4 + 9)σ^{2}/25 = **13σ^{2}/25**; (1 + 1)σ^{2}/9 = **2σ^{2}/9**.
4. E[Σ(X − X̄)^{2}] = (n − 1)σ^{2}, so dividing by n − 1 makes the estimator unbiased.
5. T = X₁ (the first observation alone): E = μ, but Var = σ^{2} for every n.
6. **Σxᵢ** (equivalently x̄).
<!--/ANSWERS-->
