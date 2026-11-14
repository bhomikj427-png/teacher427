# 09 — Method of moments and maximum likelihood

<div class="sub">Professor's LMS slides "MLE and Bayesian Estimation" (Examples 11–14) · Gupta & Kapoor §15.10–15.13 · blueprint row 3 "methods of estimation: MoM and MLE" · 4 slide examples + 3 Gupta & Kapoor exercises · needs 03, 04, 05, 08</div>

## Map

[[map:1 MoM: match one moment > 2 MoM: two parameters > 3 MLE: the five steps > 4 MLE from data > 5 MLE for the normal > 6 MLE with a product of powers > 7 Both methods, same data|here=1]]

## The questions this file answers

- <span class="tag">G&K ch. 15 ex. 20(b)</span> Random sample from f(x, α) = αe^{−αx}, x > 0. Estimate α by the method of moments.
- <span class="tag">G&K ch. 15 ex. 21</span> Random sample from f(x; a, b) = 1/(b − a), a < x < b. Find estimates of a and b by the method of moments.
- <span class="tag">Slides Ex. 12</span> Poisson pmf f(x | μ) = e^{−μ}μ^{x}/x!. What is the maximum likelihood estimate of μ?
- <span class="tag">Slides Ex. 13</span> Survival times of 10 rats (months): 14, 17, 27, 18, 12, 8, 22, 13, 19, 12. Assuming an exponential distribution, give the MLE of the mean survival time.
- <span class="tag">Slides Ex. 11</span> Normal population: MLE of the mean when the variance is known, and of the variance when the mean is known.
- <span class="tag">Slides Ex. 14</span> Sample 12, 11.2, 13.5, 12.3, 13.8, 11.9 from f(x; θ) = θ/x^{θ+1}, x > 1. Find the MLE of θ.
- <span class="tag">G&K ch. 15 ex. 23(b)</span> Sample 0.46, 0.38, 0.61, 0.82, 0.59, 0.53, 0.72, 0.44, 0.59, 0.60 from f(x) = (1 + θ)x^{θ}, 0 < x < 1. Estimate θ by (i) the method of moments (ii) maximum likelihood.

Estimation is 22 of the ETE's 80 marks. A 6- or 8-mark derivation of an MLE or MoM estimator is the most likely long question in that row.

---

## Build

### 1 · Method of moments: match one moment

File 08 judged estimators. Now two ways to **build** one. The first is the simplest.

:::q <span class="tag">G&K ch. 15 ex. 20(b)</span>
Let X₁, …, Xₙ be a random sample from f(x, α) = αe^{−αx}, 0 < x < ∞, α > 0. Estimate α using the method of moments.
:::

:::guess Guess first
The population mean of this exponential is 1/α (file 05). The sample has mean x̄. What would you set equal?
:::

**Terms.**

- **r-th population moment** μ′ᵣ = E(X^{r}): a function of the parameters.
- **r-th sample moment** m′ᵣ = (1/n)Σxᵢ^{r}: computed from the data.

**Method of moments** (Karl Pearson; G&K §15.13): with k unknown parameters, set the first k population moments equal to the sample moments and solve.

**Answer.** One parameter, one equation: E(X) = 1/α = x̄ ⇒ **α̂ = 1/x̄**.

:::check Check 1
A sample 2, 5, 7, 10 comes from U(0, θ). Find the method-of-moments estimate of θ.
:::

### 2 · Method of moments: two parameters

Two unknowns need two moments.

:::q <span class="tag">G&K ch. 15 ex. 21</span>
X₁, …, Xₙ is a random sample from f(x; a, b) = 1/(b − a), a < x < b. Find estimates of a and b by the method of moments.
:::

:::guess Guess first
Which two facts about U(a, b) involve both a and b? (File 05's table.)
:::

**Answer.** Use the mean and the variance (equivalent to the first two moments, since Var = μ′₂ − μ′₁^{2}):
(a + b)/2 = x̄ and (b − a)^{2}/12 = m₂, where m₂ = (1/n)Σ(xᵢ − x̄)^{2}.
So b + a = 2x̄ and b − a = √(12m₂) = 2√(3m₂). Adding and subtracting:

$$â = x̄ − √(3m_{2}),    b̂ = x̄ + √(3m_{2})$$

:::note Properties (G&K §15.13, remarks)
MoM estimators are consistent but in general less efficient than MLEs. The two methods give the same estimator when the MLE is a linear function of the sample moments (Poisson λ, exponential mean, normal μ).
:::

:::check Check 2
A sample has x̄ = 10 and m₂ = 3. Find â and b̂ for U(a, b).
:::

### 3 · Maximum likelihood: the five steps

MoM matches averages. MLE asks a different question: which parameter value makes the observed data most probable?

:::q <span class="tag">Slides Ex. 12</span>
Consider a Poisson distribution with pmf f(x | μ) = e^{−μ}μ^{x}/x!, x = 0, 1, 2, … . A random sample x₁, …, xₙ is taken. What is the maximum likelihood estimate of μ?
:::

:::guess Guess first
Your guess for the answer (it is a familiar statistic).
:::

**Term.** **Likelihood** L(θ) = Π f(xᵢ; θ): the joint probability of the observed sample, read as a function of θ. **MLE** θ̂ = the θ that maximises L (slides p.2; G&K §15.11).

**The professor's five steps** (slides p.2):

1. Write the distribution f(x; θ).
2. Likelihood L(θ) = Π f(xᵢ; θ).
3. Log-likelihood ℓ(θ) = ln L(θ) (turns the product into a sum; same maximiser).
4. Solve dℓ/dθ = 0 for θ̂.
5. Check d^{2}ℓ/dθ^{2} < 0 (a maximum).

**Answer.**
L(μ) = Π e^{−μ}μ^{xᵢ}/xᵢ! = e^{−nμ}μ^{Σxᵢ}/Πxᵢ!.
ℓ(μ) = −nμ + (Σxᵢ) ln μ − ln Π xᵢ!.
dℓ/dμ = −n + Σxᵢ/μ = 0 ⇒ **μ̂ = Σxᵢ/n = x̄**.
d^{2}ℓ/dμ^{2} = −Σxᵢ/μ^{2} < 0 ✓.

:::check Check 3
A binomial B(m, p) with m known gives the sample x₁, …, xₙ. Find the MLE of p.
:::

### 4 · MLE from data

With numbers, the same steps end in a value.

:::q <span class="tag">Slides Ex. 13</span>
Ten rats are injected with cancer cells and given a drug designed to increase survival. Survival times (months): 14, 17, 27, 18, 12, 8, 22, 13, 19, 12. Assume the exponential distribution applies. Give the maximum likelihood estimate of the mean survival time.
:::

:::guess Guess first
Guess the answer, then check it against step 3's pattern.
:::

**Answer.** Parametrise by the mean β: f(x; β) = (1/β)e^{−x/β}, x > 0.
ℓ(β) = −10 ln β − (1/β)Σxᵢ.
dℓ/dβ = −10/β + Σxᵢ/β^{2} = 0 ⇒ β̂ = Σxᵢ/10 = x̄.
Σxᵢ = 162, so **β̂ = 16.2 months**. The second derivative at β̂ is negative, so this is a maximum.

[[fig:likelihood_curve|The log-likelihood of the rat data peaks at the sample mean.|w=70]]

:::check Check 4
For the rat data, what is the MLE of the **rate** λ = 1/β? (MLEs carry over: the MLE of g(θ) is g(θ̂).)
:::

### 5 · MLE for the normal

Two parameters: differentiate with respect to each.

:::q <span class="tag">Slides Ex. 11</span>
For random sampling from a normal population, find the MLE of (a) the population mean when the variance is known; (b) the population variance when the mean is known.
:::

:::guess Guess first
(a) is familiar. For (b), will the divisor be n or n − 1?
:::

**Answer.** ℓ(μ, σ^{2}) = −(n/2) ln(2π) − (n/2) ln σ^{2} − \frac{1}{2σ^{2}}Σ(xᵢ − μ)^{2}.
(a) ∂ℓ/∂μ = Σ(xᵢ − μ)/σ^{2} = 0 ⇒ Σxᵢ − nμ = 0 ⇒ **μ̂ = x̄**.
(b) ∂ℓ/∂σ^{2} = −\frac{n}{2σ^{2}} + \frac{1}{2σ^{4}}Σ(xᵢ − μ)^{2} = 0 ⇒ **σ̂^{2} = (1/n)Σ(xᵢ − μ)^{2}**.

If μ is also unknown it is replaced by x̄, giving σ̂^{2} = (1/n)Σ(xᵢ − x̄)^{2}: the n-divisor, which file 08 showed is **biased**. MLEs are consistent but need not be unbiased.

:::check Check 5
Data 4, 6, 8 from a normal population with both parameters unknown. Find μ̂ and σ̂^{2} by maximum likelihood.
:::

### 6 · MLE with a product of powers

When f contains x^{θ}, the log turns the product into a sum of ln xᵢ.

:::q <span class="tag">Slides Ex. 14</span>
A sample of the values 12, 11.2, 13.5, 12.3, 13.8 and 11.9 comes from a population with density f(x; θ) = θ/x^{θ+1}, x > 1, θ > 0. Find the maximum likelihood estimate of θ.
:::

:::guess Guess first
After taking logs, where will θ appear: next to Σxᵢ or next to Σ ln xᵢ?
:::

**Answer.** L(θ) = Π θ/xᵢ^{θ+1} = θ^{n}/(Πxᵢ)^{θ+1}.
ℓ(θ) = n ln θ − (θ + 1)Σ ln xᵢ.
dℓ/dθ = n/θ − Σ ln xᵢ = 0 ⇒ θ̂ = n/Σ ln xᵢ.
Σ ln xᵢ = ln 12 + ln 11.2 + ln 13.5 + ln 12.3 + ln 13.8 + ln 11.9 = 15.114.
**θ̂ = 6/15.114 = 0.3970**. d^{2}ℓ/dθ^{2} = −n/θ^{2} < 0 ✓.

:::note Slide label
The slide writes the likelihood as L(x₁, …, x₁₀; θ) although the sample has six values; n = 6 is used in its final line and here.
:::

:::check Check 6
Same density, a sample of 4 values with Σ ln xᵢ = 2. Find θ̂.
:::

### 7 · Both methods on the same data

The two methods need not agree. This question asks for both.

:::q <span class="tag">G&K ch. 15 ex. 23(b)</span>
The sample values from a population with pdf f(x) = (1 + θ)x^{θ}, 0 < x < 1, θ > 0, are 0.46, 0.38, 0.61, 0.82, 0.59, 0.53, 0.72, 0.44, 0.59, 0.60. Find the estimate of θ by (i) the method of moments (ii) maximum likelihood.
:::

:::guess Guess first
Will the two estimates be equal? (Step 2's note says when they are.)
:::

**(i) MoM.** E(X) = ∫₀¹ x(1 + θ)x^{θ} dx = \frac{1 + θ}{θ + 2}. Set equal to x̄ and solve:
x̄(θ + 2) = 1 + θ ⇒ θ̂ = \frac{2x̄ − 1}{1 − x̄}. Here x̄ = 5.74/10 = 0.574:
**θ̂ = (1.148 − 1)/0.426 = 0.3474**.

**(ii) MLE.** ℓ(θ) = n ln(1 + θ) + θ Σ ln xᵢ; dℓ/dθ = n/(1 + θ) + Σ ln xᵢ = 0 ⇒ θ̂ = −1 − n/Σ ln xᵢ.
Σ ln xᵢ = −5.7873, so **θ̂ = −1 + 10/5.7873 = 0.7279**.

The estimates differ (0.35 and 0.73): the MLE is not a linear function of x̄ here. The MLE is the more efficient of the two.

:::check Check 7
For f(x) = (1 + θ)x^{θ}, which statistic is sufficient for θ? (Look at where θ meets the data in ℓ.)
:::

---

## Exam form

**Method of moments.** Equate μ′ᵣ = E(X^{r}) to m′ᵣ = (1/n)Σxᵢ^{r} for r = 1, …, k; solve for the k parameters.

**Maximum likelihood.**

1. f(x; θ). 2. L(θ) = Πf(xᵢ; θ). 3. ℓ = ln L. 4. dℓ/dθ = 0 ⇒ θ̂. 5. d^{2}ℓ/dθ^{2} < 0.

**Standard MLEs** (memorise):

| Distribution | MLE |
|---|---|
| Poisson(λ) | λ̂ = x̄ |
| Binomial(m, p), m known | p̂ = x̄/m |
| Exponential, mean β (rate λ) | β̂ = x̄ (λ̂ = 1/x̄) |
| Normal μ (σ known) | μ̂ = x̄ |
| Normal σ^{2} (μ known / unknown) | (1/n)Σ(xᵢ − μ)^{2} / (1/n)Σ(xᵢ − x̄)^{2} |
| θ/x^{θ+1}, x > 1 | n/Σ ln xᵢ |
| (1 + θ)x^{θ}, 0 < x < 1 | −1 − n/Σ ln xᵢ |

**Properties of MLE** (slides p.3): consistent; most efficient (for large n); a function of a sufficient statistic when one exists; invariant: the MLE of g(θ) is g(θ̂). Not always unbiased.

## Traps

- Differentiating L instead of ln L: legal but much harder.
- Dropping the n in front of ln θ (there is one factor of θ per observation).
- Forgetting the second-derivative check in a long answer: it carries a mark.
- Writing σ̂^{2} with n − 1: the MLE divides by n.
- Mixing the exponential's mean β and rate λ: β̂ = x̄ but λ̂ = 1/x̄.

## Self-test

1. State the principle of maximum likelihood and the five steps.
2. Find the MLE of p for a Bernoulli sample x₁, …, xₙ (each 0 or 1).
3. Find the MoM estimator of λ for a Poisson sample. Does it equal the MLE?
4. A sample from Exp(rate λ) has values 2, 3, 5, 6. Find λ̂ by both methods.
5. Why is ln L maximised instead of L?
6. Give one property MLEs have and one they need not have.

<!--ANSWERS-->
## Answers

**Check 1.** E(X) = θ/2 = x̄ = 6 ⇒ **θ̂ = 12**. (The MLE here is the largest value, 10, found by inspection, not by differentiating.)

**Check 2.** â = 10 − √9 = **7**, b̂ = 10 + 3 = **13**.

**Check 3.** ℓ = const + (Σxᵢ) ln p + (nm − Σxᵢ) ln(1 − p); Σxᵢ/p = (nm − Σxᵢ)/(1 − p) ⇒ **p̂ = x̄/m**.

**Check 4.** λ̂ = 1/16.2 = **0.0617 per month**.

**Check 5.** μ̂ = **6**; σ̂^{2} = (4 + 0 + 4)/3 = **8/3 ≈ 2.67**.

**Check 6.** θ̂ = 4/2 = **2**.

**Check 7.** θ multiplies **Σ ln xᵢ** (equivalently Π xᵢ): that statistic is sufficient.

**Self-test.**

1. Choose θ to maximise the likelihood of the observed sample; steps as in Exam form.
2. ℓ = Σxᵢ ln p + (n − Σxᵢ) ln(1 − p) ⇒ **p̂ = x̄**.
3. E(X) = λ = x̄ ⇒ λ̂ = x̄: **yes**, the same as the MLE.
4. x̄ = 4: MoM 1/λ = 4 ⇒ λ̂ = **0.25**; MLE λ̂ = 1/x̄ = **0.25**.
5. ln is increasing, so the maximiser is the same, and the product becomes a sum that is easy to differentiate.
6. Has: consistency (or invariance, efficiency for large n). Need not have: unbiasedness.
<!--/ANSWERS-->
