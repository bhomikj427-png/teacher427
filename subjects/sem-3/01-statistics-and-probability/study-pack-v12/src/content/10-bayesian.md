# 10 — Introduction to Bayesian estimation

<div class="sub">Professor's LMS slides "MLE and Bayesian Estimation" (p.10–15, Example 15) · Walpole et al. ch. 18 (via the knowledge base) · blueprint row 3 "introduction of Bayesian estimation" · 1 slide example + slide definitions · needs 01 (Bayes' theorem), 04 (binomial), 09</div>

## Map

[[map:1 Parameters as random variables > 2 Prior → posterior > 3 The full posterior table > 4 A Bayes point estimate|here=1]]

## The questions this file answers

- <span class="tag">Slides p.10–12</span> What is the key difference between the Bayesian and the classical (frequentist) approach? What are subjective probability, the conditional perspective and the prior distribution?
- <span class="tag">Slides Ex. 15</span> The prior distribution for the proportion of defectives p produced by a machine is P(p = 0.1) = 0.6, P(p = 0.2) = 0.4. Let x be the number of defectives in a random sample of size 2. Find the posterior distribution of p, given that x is observed.

The blueprint says "introduction of", inside the 22-mark estimation row: expect definitions (2 marks) or one posterior calculation like Example 15 (6 marks).

---

## Build

### 1 · Parameters as random variables

Files 08–09 treated θ as a fixed unknown number. The Bayesian approach does not.

:::q <span class="tag">Slides p.10</span>
What is the key difference between the Bayesian approach and the classical (frequentist) approach?
:::

:::guess Guess first
"What is the probability that it rains tomorrow?" Can that be a long-run frequency of repeated tomorrows? What kind of probability is it?
:::

**Terms** (slides p.10–12):

- **Subjective probability**: a probability that expresses a person's degree of belief (rain tomorrow, a stock rising, a merger). Different people may give different values.
- **Prior distribution π(θ)**: a probability distribution placed on the parameter **before** seeing data, usually from subjective probability or past records. It reflects the experimenter's prior belief.
- **Conditional perspective**: inference is based on the data actually observed; all knowledge about θ is in the observed data **plus** the prior.

**Answer.** In the Bayesian approach the **parameter is treated as a random variable**, with its own distribution; in the classical approach it is a fixed unknown constant and only the data are random.

:::check Check 1
Write two applications the slides list for Bayesian methods, and one reason a prior is useful when data are scarce.
:::

### 2 · Prior → posterior

File 01's Bayes' theorem updated the probability of a cause after seeing an effect. Here the "cause" is the value of θ.

:::q Predict
A machine's defect rate is either 0.1 or 0.2, with prior belief 0.6 and 0.4. You test 2 items and **both are good**. Does your belief in p = 0.1 go up or down? Roughly to what?
:::

:::guess Guess first
Write "up" or "down" and a number.
:::

**Posterior distribution** (slides p.13): with prior π(θ) and sample x = (x₁, …, xₙ),

$$π(θ | x) = \frac{f(x | θ) π(θ)}{g(x)}$$

$$g(x) = Σ_{θ} f(x | θ)π(θ)  (θ discrete),    g(x) = ∫ f(x | θ)π(θ) dθ  (θ continuous)$$

f(x | θ) is the likelihood of file 09; g(x) is the marginal probability of the data, which makes the posterior add to 1. In words: **posterior ∝ likelihood × prior**.

**Answer.** x = 0 defectives in 2. Likelihoods: f(0 | 0.1) = 0.9^{2} = 0.81, f(0 | 0.2) = 0.8^{2} = 0.64.
Products: 0.81 × 0.6 = 0.486; 0.64 × 0.4 = 0.256; g(0) = 0.742.
π(0.1 | 0) = 0.486/0.742 = **0.6550**: **up** from 0.6. Two good items favour the lower defect rate.

:::check Check 2
Same prior. One item is tested and it is defective. Find π(0.1 | x = 1) for n = 1.
:::

### 3 · The full posterior table

:::q <span class="tag">Slides Ex. 15</span>
Assume that the prior distribution for the proportion of defectives produced by a machine is p = 0.1 with π = 0.6, p = 0.2 with π = 0.4. Denote by x the number of defectives among a random sample of size 2. Find the posterior probability distribution of p, given that x is observed.
:::

:::guess Guess first
For x = 2 (both defective), which value of p will the posterior favour?
:::

**Answer.** X | p ~ B(2, p): f(x | p) = C(2, x)p^{x}(1 − p)^{2−x}.
g(x) = C(2, x)[(0.1)^{x}(0.9)^{2−x}(0.6) + (0.2)^{x}(0.8)^{2−x}(0.4)].

| x | f(x ∣ 0.1)·0.6 | f(x ∣ 0.2)·0.4 | g(x) | π(0.1 ∣ x) | π(0.2 ∣ x) |
|---|---|---|---|---|---|
| 0 | 0.81 × 0.6 = 0.486 | 0.64 × 0.4 = 0.256 | 0.742 | **0.6550** | **0.3450** |
| 1 | 0.18 × 0.6 = 0.108 | 0.32 × 0.4 = 0.128 | 0.236 | **0.4576** | **0.5424** |
| 2 | 0.01 × 0.6 = 0.006 | 0.04 × 0.4 = 0.016 | 0.022 | **0.2727** | **0.7273** |

Check: g(0) + g(1) + g(2) = 1.000 ✓; each row of the posterior adds to 1.

[[fig:prior_posterior|Each defective found shifts belief toward p = 0.2.|w=78]]

:::check Check 3
Same machine, prior changed to P(p = 0.1) = P(p = 0.2) = 0.5. Find π(0.2 | x = 1) for a sample of 2.
:::

### 4 · A Bayes point estimate

The posterior is a whole distribution. When one number is wanted, summarise it.

:::q Predict
After observing x = 0 in Example 15, give a single estimate of p.
:::

:::guess Guess first
Should it be 0.1, 0.2, or something in between?
:::

**Bayes estimate.** Under squared-error loss the Bayes estimate is the **posterior mean** E(θ | x) (Walpole et al. ch. 18). The posterior mode (most probable value) is another summary.

**Answer.** E(p | x = 0) = 0.1 × 0.6550 + 0.2 × 0.3450 = 0.0655 + 0.0690 = **0.1345**. Compare the prior mean 0.1 × 0.6 + 0.2 × 0.4 = 0.14: the data pulled the estimate down a little.

**Contrast with file 09.** The MLE from x = 0 defectives in 2 is p̂ = 0/2 = 0, which ignores the prior knowledge that p is 0.1 or 0.2. The Bayes estimate combines both.

:::check Check 4
Find the Bayes estimate (posterior mean) of p after x = 2 in Example 15.
:::

---

## Exam form

**Definitions.**

- **Bayesian approach**: parameters are random variables; inference combines a prior distribution with the observed data.
- **Prior π(θ)**: distribution of θ before data, reflecting prior belief (subjective probability).
- **Posterior π(θ | x)**: distribution of θ after data.
- **Conditional perspective**: inference is conditional on the data actually observed.

**Posterior.** π(θ | x) = f(x | θ)π(θ)/g(x), g(x) = Σ_{θ} f(x | θ)π(θ) or ∫ f(x | θ)π(θ)dθ.

**Procedure (discrete prior).**

1. List the θ values and prior weights.
2. Likelihood f(x | θ) for the observed x.
3. Products f(x | θ)π(θ); sum them for g(x).
4. Posterior = each product ÷ g(x). Check the posterior adds to 1.
5. If asked for an estimate: posterior mean Σθ π(θ | x).

| | Classical (MoM, MLE) | Bayesian |
|---|---|---|
| θ is | a fixed unknown constant | a random variable |
| Uses | data only | data + prior |
| Answer | a point/interval for θ | a posterior distribution of θ |

## Traps

- Forgetting to divide by g(x): the products are not yet probabilities.
- Using the binomial coefficient in one product but not the other (it cancels only if used consistently).
- Calling the prior "the data": the prior is fixed before the sample is seen.

## Self-test

1. State the key difference between Bayesian and classical estimation.
2. Define prior and posterior distributions.
3. Write Bayes' formula for the posterior and say what g(x) is.
4. A coin is fair (p = 0.5) or biased (p = 0.8), prior 0.7 and 0.3. One toss gives a head. Find the posterior P(p = 0.8 | head).
5. For Q4, find the posterior mean of p.

<!--ANSWERS-->
## Answers

**Check 1.** Any two of: statistical modelling and data analysis, bioinformatics, biology, business, engineering, environmental science, health, medicine. With few data the prior supplies information the sample cannot.

**Check 2.** Products: 0.1 × 0.6 = 0.06, 0.2 × 0.4 = 0.08; g = 0.14. π(0.1 | 1) = 0.06/0.14 = **0.4286**.

**Check 3.** Products: 0.18 × 0.5 = 0.09, 0.32 × 0.5 = 0.16; g = 0.25. π(0.2 | 1) = 0.16/0.25 = **0.64**.

**Check 4.** 0.1 × 0.2727 + 0.2 × 0.7273 = 0.02727 + 0.14546 = **0.1727**.

**Self-test.**

1. Bayesian: θ is random with a prior distribution; classical: θ is a fixed constant.
2. Prior: belief about θ before data. Posterior: distribution of θ given the data.
3. π(θ | x) = f(x | θ)π(θ)/g(x); g(x) = Σ f(x | θ)π(θ), the marginal probability of the data.
4. Products 0.5 × 0.7 = 0.35, 0.8 × 0.3 = 0.24; g = 0.59. P(0.8 | H) = 0.24/0.59 = **0.4068**.
5. 0.5 × 0.5932 + 0.8 × 0.4068 = **0.6220**.
<!--/ANSWERS-->
