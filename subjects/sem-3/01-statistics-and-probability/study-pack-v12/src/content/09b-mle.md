# 09b — Maximum likelihood

<div class="sub">Professor's LMS slides "MLE and Bayesian Estimation" p.2–10 (five steps, properties, Examples 11–14) · Gupta & Kapoor §15.11 (eq. 15·53; Theorems 15.11, 15.13–15.15, 15.17), ch. 15 ex. 23(b)(ii) · blueprint row 3 "methods of estimation: MoM and MLE" · 5 real questions (slides Ex. 11–14, G&K 23(b)) · needs 02a (pmf step 2), 02b (pdf), 04 (Poisson), 05 (exponential), 06 (normal pdf), 08 (unbiased step 3, n − 1 step 5, consistent/efficient/sufficient steps 6–8), 09a (MoM, steps 2, 3, 5)</div>

## Map

[[map:1 Likelihood: a product > 2 The log keeps the peak > 3 The five steps > 4 Poisson > 5 Exponential from data > 6 Normal mean > 7 Normal variance > 8 Product of powers > 9 Second-derivative check > 10 Properties > 11 MoM against MLE|here=1]]

09a built an estimator by matching averages. Maximum likelihood asks a sharper question: **of all the values the parameter could take, which one makes the data we actually saw most probable?** That value is the estimate. The professor's slides teach it as five fixed steps, and every long MLE answer follows them. File 10 then treats the parameter itself as random (Bayesian estimation).

| Symbol | What it means in this file | Typical value |
|---|---|---|
| θ | the unknown parameter ("theta"); in the coin, p | p = 2/3 |
| f(x; θ) | the pmf or pdf of one observation, with θ written in (02a, 02b) | p for a head |
| L(θ) | likelihood: the probability (or density) of the whole observed sample, read as a function of θ | 0.148 at p = 2/3 |
| ℓ(θ) | log-likelihood ln L(θ) ("ell") | −1.910 |
| dℓ/dθ | slope of ℓ: zero at the peak | 0 at θ̂ |
| θ̂ | MLE: the θ where L (and ℓ) is greatest | β̂ = 16.2 |
| Σxᵢ, Σ ln xᵢ | totals of the data, or of their logs: the only way the data enter ℓ | 162; 15.114 |

**Running example.** Slides Ex. 13: survival times of 10 rats (months) 14, 17, 27, 18, 12, 8, 22, 13, 19, 12; Σxᵢ = 162, x̄ = **16.2**. Steps 5, 9 and 10 use it. Steps 1–2 open on a coin.

## The questions this file answers

- <span class="tag">Slides Ex. 12</span> Consider a Poisson distribution with pmf f(x | μ) = e^{−μ}μ^{x}/x!, x = 0, 1, 2, … . A random sample x₁, …, xₙ is taken. What is the maximum likelihood estimate of μ?
- <span class="tag">Slides Ex. 13</span> Ten rats are injected with cancer cells and given a drug designed to increase survival. Survival times (months): 14, 17, 27, 18, 12, 8, 22, 13, 19, 12. Assume the exponential distribution applies. Give the maximum likelihood estimate of the mean survival time.
- <span class="tag">Slides Ex. 11</span> For random sampling from a normal population, find the maximum likelihood estimators for (a) the population mean when the population variance is known; (b) the population variance when the population mean is known.
- <span class="tag">Slides Ex. 14</span> A sample of the values 12, 11.2, 13.5, 12.3, 13.8 and 11.9 comes from a population with density f(x; θ) = θ/x^{θ+1}, x > 1, θ > 0. Find the maximum likelihood estimate of θ.
- <span class="tag">G&K ch. 15 ex. 23(b)(ii)</span> The sample values from f(x) = (1 + θ)x^{θ}, 0 < x < 1, θ > 0, are 0.46, 0.38, 0.61, 0.82, 0.59, 0.53, 0.72, 0.44, 0.59, 0.60. Find the estimate of θ by maximum likelihood (and compare with the method of moments, 09a step 5).

The MLE derivation is rank 1 in START-HERE: the most likely long question in blueprint row 3 (22 of 80 marks).

---

## Build

### 1 · Likelihood: the probability of what you saw

A coin may be bent: P(head) = p is unknown. You toss it three times and see **H, H, T**.

:::q Predict
If p = 0.5, what is the probability of exactly the sequence H, H, T? If p = 0.8? Which value of p would you pick as your estimate, and why?
:::

:::guess Guess first
Write the two probabilities and your estimate of p.
:::

:::note Terms
**Likelihood** L(p): the probability of the observed data, worked out for a trial value of p. The tosses are independent, so it is a **product**: L(p) = p · p · (1 − p) = p^{2}(1 − p). The data are fixed; p is what varies. **Maximum likelihood estimate (MLE)** p̂: the value of p that makes L greatest (slides p.2; G&K §15.11).
:::

[[fig:coin_like|What this graph plots: the likelihood L(p) = p²(1 − p) of seeing H, H, T, for every trial value of p from 0 to 1. Horizontal axis: p. Vertical axis: L(p). One point = how probable H, H, T is if the coin's head probability were p. Dashed line: the peak.|w=74]]

**Reading the figure.**

| p | L(p) = p^{2}(1 − p) |
|---|---|
| 0.3 | 0.063 |
| 0.5 | 0.125 |
| **2/3** | **0.148 (the peak)** |
| 0.8 | 0.128 |

**Answer to the Predict.** p = 0.5: 0.5 × 0.5 × 0.5 = **0.125**. p = 0.8: 0.8 × 0.8 × 0.2 = **0.128**. The highest point of the curve is at **p̂ = 2/3**, L = 4/27 = 0.148: two heads in three tosses, so the head rate that best explains them is 2/3.

:::check Check 1
Tosses H, T, T. Write L(p) and find its value at p = 1/3 and at p = 1/2. Which is larger?
:::

### 2 · The log keeps the peak and turns the product into a sum

A product of n factors is hard to differentiate. Logs turn products into sums.

:::q Predict
ℓ(p) = ln L(p). Will ℓ peak at the same p as L, or somewhere else?
:::

:::guess Guess first
One word: same or different.
:::

:::note Terms
**Log-likelihood** ℓ(θ) = ln L(θ). ln is increasing (a bigger number has a bigger log), so ℓ is greatest exactly where L is greatest. ln(ab) = ln a + ln b turns the product into a sum, and ln(a^{k}) = k ln a brings powers down.
:::

[[fig:coin_L_lnL|What this graph plots: left, the likelihood L(p) = p²(1 − p); right, the log-likelihood ℓ(p) = 2 ln p + ln(1 − p), both for the tosses H, H, T. Horizontal axes: p. Dashed lines: the peak of each, both at p = 2/3.|w=88]]

**Reading the figure.**

| p | L(p) | ℓ(p) = ln L(p) |
|---|---|---|
| 0.5 | 0.125 | −2.079 |
| **2/3** | **0.148** | **−1.910** |
| 0.8 | 0.128 | −2.056 |
| 0.9 | 0.081 | −2.513 |

**Derivation** (the peak by calculus):

1. ℓ(p) = ln(p^{2}(1 − p)) = 2 ln p + ln(1 − p).
2. dℓ/dp = 2/p − 1/(1 − p).
3. At the peak the slope is zero: 2/p = 1/(1 − p).
4. Cross-multiply: 2(1 − p) = p, so 2 = 3p and **p̂ = 2/3**.

**Answer to the Predict.** **Same.** Both peak at p = 2/3; the log only changes the height scale.

:::check Check 2
For H, T, T, write ℓ(p), differentiate, and find p̂.
:::

### 3 · The five steps

The coin used every piece of the method. The professor's slides fix the order, and marks follow it.

:::q Predict
Each of n tosses gives xᵢ = 1 (head) or 0 (tail), with f(x; p) = p^{x}(1 − p)^{1−x}. Guess the MLE of p before working it.
:::

:::guess Guess first
Your formula for p̂ in terms of the data.
:::

**The five steps** (slides p.2; G&K §15.11, eq. 15·53):

1. Write the distribution of one observation, f(x; θ).
2. Likelihood: L(θ) = Π f(xᵢ; θ) (Π = multiply over i = 1 to n).
3. Log-likelihood: ℓ(θ) = ln L(θ).
4. Solve dℓ/dθ = 0 for θ: the solution is θ̂.
5. Check d^{2}ℓ/dθ^{2} < 0 at θ̂ (a peak, not a dip; step 9).

**Answer to the Predict**, by the five steps:

1. f(x; p) = p^{x}(1 − p)^{1−x}.
2. L(p) = p^{Σxᵢ}(1 − p)^{n−Σxᵢ} (powers add when factors multiply).
3. ℓ(p) = (Σxᵢ) ln p + (n − Σxᵢ) ln(1 − p).
4. dℓ/dp = Σxᵢ/p − (n − Σxᵢ)/(1 − p) = 0 ⇒ (1 − p)Σxᵢ = p(n − Σxᵢ) ⇒ Σxᵢ = np ⇒ **p̂ = Σxᵢ/n = x̄**, the fraction of heads.
5. d^{2}ℓ/dp^{2} = −Σxᵢ/p^{2} − (n − Σxᵢ)/(1 − p)^{2} < 0 ✓.

With n = 3, Σxᵢ = 2 this is step 1's 2/3.

:::check Check 3
20 tosses give 7 heads. Find p̂.
:::

### 4 · Poisson

Now a count model from 04: the same five steps, a different f.

:::q <span class="tag">Slides Ex. 12</span>
Consider a Poisson distribution with pmf f(x | μ) = e^{−μ}μ^{x}/x!, x = 0, 1, 2, … . A random sample x₁, …, xₙ is taken. What is the maximum likelihood estimate of μ?
:::

:::guess Guess first
μ is the Poisson mean (04). Which statistic would you expect?
:::

**Answer**, by the five steps (slides p.5–6):

1. f(x; μ) = e^{−μ}μ^{x}/x!.
2. L(μ) = Π e^{−μ}μ^{xᵢ}/xᵢ! = e^{−nμ}μ^{Σxᵢ}/Πxᵢ! (n factors of e^{−μ}; the powers of μ add).
3. ℓ(μ) = −nμ + (Σxᵢ) ln μ − ln Πxᵢ!. The last term has no μ in it.
4. dℓ/dμ = −n + Σxᵢ/μ = 0 ⇒ **μ̂ = Σxᵢ/n = x̄**.
5. d^{2}ℓ/dμ^{2} = −Σxᵢ/μ^{2} < 0 ✓.

Read in words: the best Poisson mean is the sample mean. ln Πxᵢ! drops out when differentiating, so it never needs computing.

:::check Check 4
Counts 2, 0, 3, 1, 4 from a Poisson population. Find μ̂.
:::

### 5 · Exponential, from data to a number

With numbers, the same steps end in a value.

:::q <span class="tag">Slides Ex. 13</span>
Ten rats are injected with cancer cells and given a drug designed to increase survival. Survival times (months): 14, 17, 27, 18, 12, 8, 22, 13, 19, 12. Assume the exponential distribution applies. Give the maximum likelihood estimate of the mean survival time.
:::

:::guess Guess first
After steps 3 and 4, guess the number.
:::

:::note Which parameter?
The slide writes the exponential with its **mean** β: f(x; β) = (1/β)e^{−x/β}, x > 0, not with the rate λ = 1/β of 05. The question asks for the mean, so β is the right parameter.
:::

[[fig:rats_loglik|What this graph plots: the log-likelihood ℓ(β) = −10 ln β − 162/β of the rat data, for trial mean survival times β from 6 to 40 months. Horizontal axis: β (months). Vertical axis: ℓ(β). Dashed line: the peak at β = 16.2.|w=78]]

**Reading the figure.**

| β (months) | ℓ(β) |
|---|---|
| 10 | −39.23 |
| **16.2** | **−37.85 (peak)** |
| 25 | −38.67 |
| 40 | −40.94 |

**Answer**, by the five steps (slides p.7–8):

1. f(x; β) = (1/β)e^{−x/β}.
2. L(β) = (1/β^{10}) e^{−Σxᵢ/β}.
3. ℓ(β) = −10 ln β − (1/β)Σxᵢ.
4. dℓ/dβ = −10/β + Σxᵢ/β^{2} = 0 ⇒ 10β = Σxᵢ ⇒ β̂ = Σxᵢ/10 = x̄.
5. Σxᵢ = 162, so **β̂ = 16.2 months**; the second derivative there is negative (step 9).

:::check Check 5
Five light bulbs last 900, 1100, 1000, 1300, 700 hours (exponential, mean β). Find β̂.
:::

### 6 · Normal mean, variance known

Two parameters μ and σ² appear in the normal pdf (06). Take them one at a time: first μ, with σ² a known number.

:::q <span class="tag">Slides Ex. 11(a)</span>
For random sampling from a normal population, find the maximum likelihood estimator for the population mean when the population variance is known.
:::

:::guess Guess first
Which statistic? (Steps 3–5 have shown a pattern.)
:::

**Answer** (slides p.4):

1. f(x; μ) = \frac{1}{σ√(2π)} e^{−(x − μ)^{2}/(2σ^{2})}.
2. L(μ) = (2π)^{−n/2}(σ^{2})^{−n/2} exp[−\frac{1}{2σ^{2}}Σ(xᵢ − μ)^{2}].
3. ℓ(μ) = −(n/2) ln 2π − (n/2) ln σ^{2} − \frac{1}{2σ^{2}}Σ(xᵢ − μ)^{2}. Only the last term holds μ.
4. dℓ/dμ = \frac{1}{σ^{2}}Σ(xᵢ − μ) = 0 ⇒ Σxᵢ − nμ = 0 ⇒ **μ̂ = x̄**.
5. d^{2}ℓ/dμ^{2} = −n/σ^{2} < 0 ✓.

Read in words: maximising ℓ means making Σ(xᵢ − μ)^{2} smallest, and the number closest to all the data in this squared sense is their mean.

:::check Check 6
Data 4, 6, 8 from a normal population with σ² = 4. Find μ̂.
:::

### 7 · Normal variance, mean known

Now the other parameter: μ is a known number, σ² is unknown. Treat σ² as one symbol (call it v if that helps).

:::q <span class="tag">Slides Ex. 11(b)</span>
For random sampling from a normal population, find the maximum likelihood estimator for the population variance when the population mean is known.
:::

:::guess Guess first
08 step 5 showed that s² divides by n − 1 to be unbiased. Will the MLE divide by n or by n − 1?
:::

**Answer** (same ℓ as step 6, now differentiated with respect to σ²):

1. ℓ = −(n/2) ln 2π − (n/2) ln σ^{2} − \frac{1}{2σ^{2}}Σ(xᵢ − μ)^{2}.
2. ∂ℓ/∂σ^{2} = −\frac{n}{2σ^{2}} + \frac{1}{2σ^{4}}Σ(xᵢ − μ)^{2}.
3. Set to zero and multiply by 2σ^{4}: −nσ^{2} + Σ(xᵢ − μ)^{2} = 0.
4. **σ̂^{2} = (1/n)Σ(xᵢ − μ)^{2}**: divisor **n**.

When μ is also unknown, it is replaced by its own MLE x̄, giving σ̂^{2} = (1/n)Σ(xᵢ − x̄)^{2}. 08 step 5 showed this is **biased** (it averages (n − 1)/n × σ²): the MLE need not be unbiased (G&K Thm 15.11, remark).

:::note Slide p.4
Ex. 11 asks two separate cases, but the slide differentiates with respect to μ and σ² together and writes only μ̂ = x̄. Its own line nσ² = Σ(xᵢ − μ)² gives σ̂² = (1/n)Σ(xᵢ − μ)², used here as part (b).
:::

:::check Check 7
(a) Data 4, 6, 8, μ known to be 5. Find σ̂². (b) Same data, μ unknown. Find μ̂ and σ̂².
:::

### 8 · A product of powers

When x appears as a power base, ln brings down Σ ln xᵢ instead of Σxᵢ.

:::q <span class="tag">Slides Ex. 14</span>
A sample of the values 12, 11.2, 13.5, 12.3, 13.8 and 11.9 comes from a population with density f(x; θ) = θ/x^{θ+1}, x > 1, θ > 0. Find the maximum likelihood estimate of θ.
:::

:::guess Guess first
After taking logs, will θ multiply Σxᵢ or Σ ln xᵢ?
:::

[[fig:ex14_loglik|What this graph plots: the log-likelihood ℓ(θ) = 6 ln θ − 15.114(θ + 1) of the slide's six values, for θ from 0.05 to 1.2. Horizontal axis: θ. Vertical axis: ℓ(θ). Dashed line: the peak at θ = 0.397.|w=78]]

**Reading the figure.**

| θ | ℓ(θ) |
|---|---|
| 0.2 | −27.79 |
| **0.397** | **−26.66 (peak)** |
| 0.6 | −27.25 |
| 1.0 | −30.23 |

**Answer** (slides p.9–10):

1. f(x; θ) = θ/x^{θ+1} = θ x^{−(θ+1)}.
2. L(θ) = Π θ/xᵢ^{θ+1} = θ^{n}/(Πxᵢ)^{θ+1}.
3. ℓ(θ) = n ln θ − (θ + 1)Σ ln xᵢ.
4. dℓ/dθ = n/θ − Σ ln xᵢ = 0 ⇒ θ̂ = n/Σ ln xᵢ.
5. Σ ln xᵢ = ln 12 + ln 11.2 + ln 13.5 + ln 12.3 + ln 13.8 + ln 11.9 = 15.114; **θ̂ = 6/15.114 = 0.3970**.

:::note Slide p.9
The slide writes the likelihood as L(x₁, …, x₁₀; θ) although the sample has six values; it uses n = 6 in its final line, as here.
:::

:::check Check 8
Same density, a sample of 4 values with Σ ln xᵢ = 2. Find θ̂.
:::

### 9 · The second-derivative check

Step 4 of the recipe finds where the slope is zero. A zero slope can be a peak or a dip; the fifth step tells which.

:::q Predict
For Ex. 14, d^{2}ℓ/dθ^{2} = −n/θ^{2}. Find its value at θ̂ = 0.3970. What would a positive value have meant?
:::

:::guess Guess first
Sign of the number, and "peak" or "dip" for a positive value.
:::

:::note Terms
**Second derivative** d^{2}ℓ/dθ^{2}: how the slope changes. Negative means the slope falls from + to − as θ grows: the curve bends down, a **peak** (maximum). Positive means a dip (minimum).
:::

| Example | d^{2}ℓ/dθ^{2} | at θ̂ |
|---|---|---|
| Poisson (step 4) | −Σxᵢ/μ^{2} | negative for any data with Σxᵢ > 0 |
| Rats (step 5) | 10/β^{2} − 2Σxᵢ/β^{3} | 10/16.2² − 324/16.2³ = −10/16.2² = **−0.0381** |
| Normal μ (step 6) | −n/σ^{2} | negative |
| Ex. 14 (step 8) | −n/θ^{2} | −6/0.3970² = **−38.07** |

**Answer to the Predict.** −6/0.3970^{2} = **−38.07 < 0**: a peak, so 0.3970 is the maximum. A positive value would have meant a **dip** (a minimum of the likelihood), not an estimate.

:::check Check 9
U(0, θ) with data 2, 5, 7, 10: L(θ) = 1/θ⁴ for θ ≥ 10 (each value has density 1/θ) and 0 for θ < 10. Does dℓ/dθ = 0 have a solution? Where is L greatest? Compare with 09a step 3.
:::

### 10 · Properties of the MLE

Why prefer the MLE? The slides list its properties; G&K proves them.

:::q Predict
For the rats, β̂ = 16.2 months is the MLE of the mean. What is the MLE of the **death rate** λ = 1/β? Do you need to redo the five steps?
:::

:::guess Guess first
A number, and yes or no.
:::

**Properties** (slides p.3; G&K §15.11):

| Property | What it says | G&K |
|---|---|---|
| Consistent | θ̂ → θ as n grows (08 step 6) | Thm 15.11 |
| Asymptotically normal | for large n, θ̂ is approximately normal around θ | Thm 15.13 |
| Most efficient | if a most efficient estimator exists, the likelihood equation gives it (08 step 7) | Thm 15.14 |
| Function of a sufficient statistic | if a sufficient estimator exists, θ̂ is a function of it (08 step 8) | Thm 15.15 |
| Invariant | if θ̂ is the MLE of θ, then g(θ̂) is the MLE of g(θ) | Thm 15.17 |
| **Not** always unbiased | σ̂² = (1/n)Σ(xᵢ − x̄)^{2} is biased (step 7) | Thm 15.11, remark |

**Answer to the Predict.** By invariance, λ̂ = 1/β̂ = 1/16.2 = **0.0617 per month**. No: the five steps need not be redone.

:::check Check 10
Using step 7(b)'s data 4, 6, 8, find the MLE of the standard deviation σ. Which property did you use?
:::

### 11 · MoM against MLE on the same data

09a step 5 estimated θ by moments on G&K's ten values: 0.3474. Now maximum likelihood on the same data.

:::q <span class="tag">G&K ch. 15 ex. 23(b)(ii)</span>
The sample values from f(x) = (1 + θ)x^{θ}, 0 < x < 1, θ > 0, are 0.46, 0.38, 0.61, 0.82, 0.59, 0.53, 0.72, 0.44, 0.59, 0.60. Find the estimate of θ by maximum likelihood.
:::

:::guess Guess first
Will it equal 09a's 0.3474?
:::

**Answer**, by the five steps:

1. f(x; θ) = (1 + θ)x^{θ}.
2. L(θ) = (1 + θ)^{n}(Πxᵢ)^{θ}.
3. ℓ(θ) = n ln(1 + θ) + θ Σ ln xᵢ.
4. dℓ/dθ = n/(1 + θ) + Σ ln xᵢ = 0 ⇒ θ̂ = −1 − n/Σ ln xᵢ.
5. Σ ln xᵢ = −5.7873 (every xᵢ < 1, so every log is negative); θ̂ = −1 + 10/5.7873 = **0.7279**. d^{2}ℓ/dθ^{2} = −n/(1 + θ)^{2} < 0 ✓.

| Method | uses | estimate |
|---|---|---|
| Moments (09a step 5) | x̄ = 0.574 | 0.3474 |
| Maximum likelihood | Σ ln xᵢ = −5.7873 | **0.7279** |

**Answer to the guess.** **No.** The two methods use different summaries of the data (x̄ against Σ ln xᵢ), so they give different numbers. The MLE is the one to prefer: MoM estimators are generally less efficient than MLEs (G&K §15.13, remarks).

:::check Check 11
For f(x) = (1 + θ)x^{θ}, which statistic is sufficient for θ? (Look at where θ meets the data in ℓ.)
:::

---

## Exam form

**Maximum likelihood** (slides p.2):

1. f(x; θ).
2. L(θ) = Π f(xᵢ; θ).
3. ℓ(θ) = ln L(θ).
4. dℓ/dθ = 0 ⇒ θ̂.
5. d^{2}ℓ/dθ^{2} < 0 at θ̂.

**Standard MLEs.**

| Distribution | MLE |
|---|---|
| Bernoulli(p) | p̂ = x̄ |
| Binomial(m, p), m known | p̂ = x̄/m |
| Poisson(μ) | μ̂ = x̄ |
| Exponential, mean β (rate λ) | β̂ = x̄ (λ̂ = 1/x̄) |
| Normal μ (σ² known) | μ̂ = x̄ |
| Normal σ² (μ known / unknown) | (1/n)Σ(xᵢ − μ)^{2} / (1/n)Σ(xᵢ − x̄)^{2} |
| θ/x^{θ+1}, x > 1 | n/Σ ln xᵢ |
| (1 + θ)x^{θ}, 0 < x < 1 | −1 − n/Σ ln xᵢ |
| U(0, θ) | the largest value (no zero-slope point) |

**Properties** (slides p.3; G&K Thms 15.11–15.17): consistent; asymptotically normal; most efficient when a most efficient estimator exists; a function of a sufficient statistic; invariant (MLE of g(θ) is g(θ̂)). Not always unbiased.

## Traps

- Differentiating L instead of ℓ: legal, but the product rule over n factors is long and error-prone.
- Dropping the n: there is one factor of θ (or 1/β) per observation, so ln gives n ln θ.
- Leaving out step 5 (second derivative) in a long answer: it carries a mark.
- Writing σ̂² with n − 1: the MLE divides by n.
- Mixing the exponential's mean β and rate λ: β̂ = x̄ but λ̂ = 1/x̄.
- Σ ln xᵢ is not ln Σxᵢ: take the log of each value, then add.

## Self-test

1. State the principle of maximum likelihood and the five steps.
2. Why is ℓ = ln L maximised instead of L, and why does it give the same θ̂?
3. Find the MLE of λ for a sample from f(x) = λe^{−λx}, x > 0, and its value for the data 2, 3, 5, 6.
4. A binomial B(m, p) with m known gives the sample x₁, …, xₙ. Find the MLE of p.
5. The MLE of a normal variance (μ unknown) is σ̂² = 8/3 for some data. Is it unbiased? Which property does the MLE have instead?
6. For f(x; θ) = θx^{θ−1}, 0 < x < 1, find the MLE of θ, and its value when Σ ln xᵢ = −4 for n = 8.
7. Give one advantage of the MLE over the method-of-moments estimator.

<!--ANSWERS-->
## Answers

**Check 1.** L(p) = p(1 − p)^{2}. L(1/3) = (1/3)(2/3)² = 4/27 = **0.148**; L(1/2) = 1/8 = **0.125**. **p = 1/3** gives the larger value.

**Check 2.** ℓ = ln p + 2 ln(1 − p); dℓ/dp = 1/p − 2/(1 − p) = 0 ⇒ 1 − p = 2p ⇒ **p̂ = 1/3**.

**Check 3.** p̂ = 7/20 = **0.35**.

**Check 4.** μ̂ = x̄ = 10/5 = **2**.

**Check 5.** β̂ = x̄ = 5000/5 = **1000 hours**.

**Check 6.** μ̂ = x̄ = **6** (σ² = 4 does not enter the answer).

**Check 7.** (a) σ̂² = (1 + 1 + 9)/3 = 11/3 = **3.67**. (b) μ̂ = **6**; σ̂² = (4 + 0 + 4)/3 = **8/3 ≈ 2.67**.

**Check 8.** θ̂ = 4/2 = **2**.

**Check 9.** ℓ = −4 ln θ for θ ≥ 10; dℓ/dθ = −4/θ is never zero, so the recipe's step 4 fails. L = 1/θ⁴ falls as θ grows, so L is greatest at the smallest allowed θ: **θ̂ = 10**, the largest value. MoM gave 12; the MLE is never below the largest value, so it is never impossible.

**Check 10.** σ̂ = √(8/3) = **1.633**, by **invariance** (g(σ²) = √σ²).

**Check 11.** θ multiplies **Σ ln xᵢ** (equivalently Πxᵢ): that statistic is sufficient, and the MLE is a function of it (Thm 15.15).

**Self-test.**

1. Choose the θ that makes the observed sample most probable; steps as in Exam form.
2. The product becomes a sum, easy to differentiate; ln is increasing, so the highest L is also the highest ℓ.
3. ℓ = n ln λ − λΣxᵢ; n/λ − Σxᵢ = 0 ⇒ **λ̂ = 1/x̄**; x̄ = 16/4 = 4, λ̂ = **0.25**.
4. ℓ = const + (Σxᵢ) ln p + (nm − Σxᵢ) ln(1 − p); Σxᵢ/p = (nm − Σxᵢ)/(1 − p) ⇒ **p̂ = x̄/m**.
5. **No**: divisor n makes it biased (it averages (n − 1)σ²/n). It is **consistent** (and invariant, asymptotically normal).
6. ℓ = n ln θ + (θ − 1)Σ ln xᵢ; n/θ + Σ ln xᵢ = 0 ⇒ **θ̂ = −n/Σ ln xᵢ**; = 8/4 = **2**.
7. It is generally more efficient (smaller spread), and invariant; it never gives an estimate the data rule out (Check 9).
<!--/ANSWERS-->
