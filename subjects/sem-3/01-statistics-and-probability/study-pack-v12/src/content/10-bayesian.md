# 10 — Introduction to Bayesian estimation

<div class="sub">Professor's LMS slides "MLE and Bayesian Estimation" p.11–15 (Example 15) · Gupta & Kapoor §4·9 (Bayes' theorem; remarks 1–3 name the a priori probabilities, the likelihoods and the posterior probabilities) and exercise 4(d) Q3(f) · posterior and Bayes estimate: S. Balakrishnan, CMU 36-705 lecture 16, and S. H. Chan, Rutgers Math 170S notes §6.8 (G&K has no Bayesian estimation) · blueprint row 3 "introduction of Bayesian estimation" · 1 slide example + slide definitions + 1 textbook exercise · needs 01 steps 11–12 (total probability, Bayes' theorem), 02a step 4 (the PMF rules), 04a step 3 (binomial formula), 09b step 1 (likelihood)</div>

## Map

[[map:1 Two views of an unknown parameter > 2 The prior: belief before the data > 3 The likelihood of what you saw > 4 The marginal g(x): the total chance of the data > 5 The posterior: the prior updated by the data > 6 The full posterior table > 7 One number: the posterior mean|here=1]]

Files 08–09b estimated a parameter as **one fixed unknown number**, from the data alone. A factory manager rarely starts from nothing: experience says the machine's defect rate is 0.1 or 0.2, and more likely 0.1. Bayesian estimation writes that belief as a probability distribution for the parameter, then updates it with the sample using Bayes' theorem from file 01. The result is a new distribution for the parameter, the **posterior**. No new mathematics is needed: this is file 01 step 12 with "machine M₁ or M₂" replaced by "p = 0.1 or p = 0.2", and file 01 even used the same weights 0.6 and 0.4.

| Symbol | What it means in this file | Typical value (Ex. 15) |
|---|---|---|
| θ (here p) | the parameter; in Ex. 15, p = the proportion of defective items the machine produces | 0.1 or 0.2 |
| π(θ) | the prior: the probability given to each value of θ before any data are seen | π(0.1) = 0.6, π(0.2) = 0.4 |
| x | the data; in Ex. 15, the number of defectives in a sample of n = 2 items | 0, 1 or 2 |
| f(x ∣ θ) | the likelihood: the chance of the data x if θ were the true value | f(0 ∣ 0.1) = 0.81 |
| g(x) | the marginal: the total chance of the data, adding over every value of θ | g(0) = 0.742 |
| π(θ ∣ x) | the posterior: the probability of each value of θ after x is seen | π(0.1 ∣ 0) = 0.6550 |

**Running example.** Slides Ex. 15: a machine's proportion of defectives p is either 0.1 or 0.2, with prior probabilities 0.6 and 0.4. Two items are tested. Steps 2–5 and 7 use the outcome "both good" (x = 0); step 6 works all three outcomes, as the slide does.

## The questions this file answers

- <span class="tag">Slides p.11</span> What is the key difference between the Bayesian approach and the classical (frequentist) approach?
- <span class="tag">Slides p.11–12</span> What are subjective probability, the conditional perspective and the prior distribution?
- <span class="tag">Slides p.13</span> Write the posterior distribution of θ and the marginal distribution of the data, for θ discrete and continuous.
- <span class="tag">Slides Ex. 15</span> The prior distribution for the proportion of defectives p produced by a machine is P(p = 0.1) = 0.6, P(p = 0.2) = 0.4. Let x be the number of defectives in a random sample of size 2. Find the posterior distribution of p, given that x is observed.
- <span class="tag">G&K ex. 4(d) Q3(f)</span> Two shipments of parts: one has 10% defectives, the other 5%. One shipment is selected at random and two parts are tested and found good. Find the (posterior) probability that they came from the first shipment. (Step 5, Check 5.)

The blueprint says "introduction of", inside the 22-mark estimation row: expect definitions (2 marks) or one posterior calculation like Example 15 (6 marks).

---

## Build

### 1 · Two views of an unknown parameter

Files 08–09b treated θ as one fixed unknown number. This file changes that one assumption and nothing else.

:::q <span class="tag">Slides p.11</span>
What is the key difference between the Bayesian approach and the classical (frequentist) approach?
:::

:::guess Guess first
The machine's defect rate p is 0.1 or 0.2. Does the sentence "there is a 60% chance that p = 0.1" make sense? Write yes or no, and why.
:::

:::note Terms
**Classical (frequentist) view:** p is one fixed number. It is unknown, but it does not vary, so no probability is put on its values; only the sample is random. **Bayesian view:** p is treated as a **random variable**: each possible value gets a probability that measures how strongly it is believed.
:::

[[fig:two_views|What this graph plots: the same unknown defect rate p in the two views. Horizontal axis: possible values of p. Left: the classical view, one fixed value whose position is not known (the question mark), with no probability attached. Right: the Bayesian view, one bar for each possible value; its height is the probability given to that value (0.6 at p = 0.1, 0.4 at p = 0.2).|w=86]]

The classical methods (MoM, MLE) ask: "which single value of p do the data point to?" They use the data only. The Bayesian method asks: "how likely is each value of p, now that I have seen the data?" It uses the data **plus** a distribution for p chosen beforehand.

**Answer.** In the Bayesian approach the **parameter is treated as a random variable** with its own probability distribution; in the classical approach it is a fixed unknown constant and only the data are random. So "a 60% chance that p = 0.1" is a meaningful sentence to a Bayesian and a meaningless one to a classical statistician.

:::check Check 1
Which of these are Bayesian statements? (a) "From these data, p̂ = 0.15." (b) "Given past months, I would bet 3 to 2 that p = 0.1." (c) "The parameter p has a probability distribution."
:::

### 2 · The prior: belief before the data

If p is random, it needs a distribution before any item is tested. Step 1's right panel showed one; this step says where it comes from.

:::q <span class="tag">Slides p.11–12</span>
What is subjective probability? What is the prior distribution? What is meant by the conditional perspective?
:::

:::guess Guess first
"The probability that it rains tomorrow": can that be the long-run fraction of many repeated tomorrows? If not, what does the number measure?
:::

:::note Terms
**Subjective probability:** a number from 0 to 1 that measures one person's degree of belief in a statement (rain tomorrow, a share price rising). It is set by what that person knows, so two people may give different values. **Prior distribution π(θ):** a probability for each possible value of θ, fixed **before** the sample is seen; it is the experimenter's prior belief, usually a subjective probability. **Conditional perspective:** inference rests on the data actually observed; after the sample, what is known about θ is the data plus the prior.
:::

| p | 0.1 | 0.2 | total |
|---|---|---|---|
| π(p) | 0.6 | 0.4 | 1 |

A prior is a probability distribution like the PMFs of file 02a, so it obeys the same two rules (02a step 4): each value lies between 0 and 1, and the values add to 1. The Ex. 15 prior says "p = 0.1 is more likely than p = 0.2, by 3 to 2". G&K §4·9 remark 1 calls such probabilities "a priori" because they exist before any information from the experiment.

**Answer.** Subjective probability is a degree of belief held by a person, not a long-run frequency. The prior distribution is the distribution placed on the parameter before the data are seen; it expresses the experimenter's prior belief. The conditional perspective: conclusions are drawn from the data actually observed, combined with the prior. "Rain tomorrow" cannot be repeated, so its probability is a belief: a subjective probability.

:::check Check 2
A colleague writes the prior P(p = 0.1) = 0.7, P(p = 0.2) = 0.4. (a) Why is this not a prior? (b) Rescale it so that the ratio 7 : 4 stays and it becomes one.
:::

### 3 · The likelihood of what you saw

The prior is belief before the data. To update it, each value of p must be scored by how well it explains the data, as in 09b step 1.

:::q Predict
Two items are tested and **both are good** (x = 0). Under which value, p = 0.1 or p = 0.2, is this result more likely, and by roughly how many times?
:::

:::guess Guess first
Write 0.1 or 0.2, and a ratio.
:::

:::note Terms
**Likelihood f(x ∣ θ):** the probability of the observed data if θ were the true value. It is set by the model (here the binomial) and by the data. G&K §4·9 remark 2 uses the same word: likelihoods show how likely the observed event is under each a priori value.
:::

[[fig:bayes_tree|What this graph plots: a probability tree. First branches: the two possible values of p, with their prior probabilities 0.6 and 0.4. Second branches: the result of testing two items, "both good" (x = 0) or "at least one defective", with its chance under that value of p. At the right: prior × likelihood for the two "both good" paths; they add to g(0) = 0.742 (step 4).|w=88]]

Given p, the number of defectives among 2 items is binomial, X ∣ p ~ B(2, p) (file 04a step 3):

$$f(x | p) = C(2, x) p^{x} (1 − p)^{2 − x}$$

For x = 0 the formula leaves only (1 − p)^{2}:

1. f(0 ∣ 0.1) = (0.9)^{2} = 0.81
2. f(0 ∣ 0.2) = (0.8)^{2} = 0.64

Read back: if the defect rate were 0.1, two good items would turn up 81% of the time; if it were 0.2, 64% of the time.

**Answer to the Predict.** p = 0.1: 0.81/0.64 = **1.27 times** as likely. The likelihood alone is not yet the probability that p = 0.1: that also needs the prior (step 5).

:::check Check 3
For x = 1 (one defective among the two), find f(1 ∣ 0.1) and f(1 ∣ 0.2). Which value of p does this result favour, and by how many times?
:::

### 4 · The marginal g(x): the total chance of the data

In file 01 step 11 the chance of a defective bolt added the paths through the two machines. The tree of step 3 has the same shape, so the same sum gives the chance of the data.

:::q Predict
Before any item is tested, and without knowing p, what is the probability that both items will be good?
:::

:::guess Guess first
Will the answer lie between 0.64 and 0.81, or outside them? Write a number.
:::

:::note Terms
**Marginal g(x):** the probability of the data x when θ is not known, found by adding prior × likelihood over every possible value of θ. It is set by the prior and the model together, not by any single value of θ.
:::

The slides (p.13) write it for both kinds of parameter:

$$g(x) = Σ_{θ} f(x | θ) π(θ)    (θ discrete)$$

$$g(x) = ∫ f(x | θ) π(θ) dθ    (θ continuous)$$

Read back: weight each value's likelihood by how much that value was believed, and add. It is the total-probability rule of file 01 step 11 (G&K eq. 4·12a), with the values of θ as the paths. Balakrishnan (CMU l.16, eq. 16.10) calls it the **marginal** distribution of the data.

**Answer to the Predict.**

1. Path p = 0.1: 0.6 × 0.81 = 0.486
2. Path p = 0.2: 0.4 × 0.64 = 0.256
3. g(0) = 0.486 + 0.256 = **0.742**

It lies between 0.64 and 0.81, nearer 0.81: g(0) is an average of the two likelihoods, weighted 0.6 and 0.4 by the prior.

:::check Check 4
Find g(1) and g(2) for Ex. 15 (Check 3 gives the likelihoods for x = 1). Do g(0), g(1) and g(2) add to 1? Why must they?
:::

### 5 · The posterior: the prior updated by the data

Step 4 added the two paths that end in "both good". The posterior asks what share of that total came through each value of p, exactly as file 01 step 12 split the defective bolts by machine.

:::q Predict
The prior gave p = 0.1 a probability of 0.6. Both tested items are good. Does the belief in p = 0.1 go up or down, and to roughly what?
:::

:::guess Guess first
Write "up" or "down", and a number.
:::

:::note Terms
**Posterior distribution π(θ ∣ x):** the probability of each value of θ after the data x are seen. It is set by the prior and the likelihood together. G&K §4·9 remark 3: posterior probabilities are "determined after the results of the experiment are known".
:::

[[fig:bayes_update0|What this graph plots: for each possible value of p (horizontal axis), two bars: the prior probability (grey) and the posterior probability after two good items (blue). Vertical axis: probability. The grey bars add to 1, and so do the blue bars.|w=70]]

| p | prior π(p) | prior × likelihood | posterior π(p ∣ x = 0) |
|---|---|---|---|
| 0.1 | 0.6 | 0.486 | 0.6550 |
| 0.2 | 0.4 | 0.256 | 0.3450 |
| total | 1 | 0.742 = g(0) | 1 |

The slides (p.13) give the rule:

$$π(θ | x) = \frac{f(x | θ) π(θ)}{g(x)}$$

Read back: posterior = (likelihood × prior) ÷ (the same product added over all θ). Dividing by g(x) only rescales the products so they add to 1; it does not change their ratio. In short: **posterior ∝ likelihood × prior**. This is G&K's Bayes' theorem (§4·9) with the values of θ as the events Eᵢ.

**Answer to the Predict.**

1. π(0.1 ∣ 0) = 0.486/0.742 = **0.6550**
2. π(0.2 ∣ 0) = 0.256/0.742 = **0.3450**

**Up**, from 0.6 to 0.6550. Two good items favour the lower defect rate (step 3), but two items are little evidence, so the belief moves only a little.

:::check Check 5
(a) Same prior. One item is tested (n = 1) and it is defective. Find π(0.1 ∣ x = 1).
(b) <span class="tag">G&K ex. 4(d) Q3(f)</span> Two shipments of parts are received. The first contains 1000 parts with 10% defectives and the second 2000 parts with 5% defectives. One shipment is selected at random. Two parts are tested and found good. Find the probability (a posterior) that the tested parts were selected from the first shipment. (Hint: "selected at random" sets the prior.)
:::

### 6 · The full posterior table

Step 5 handled one outcome. Ex. 15 asks for the posterior "given that x is observed": every possible x, in one table.

:::q <span class="tag">Slides Ex. 15</span>
Assume that the prior distribution for the proportion of defectives produced by a machine is p = 0.1 with π = 0.6, p = 0.2 with π = 0.4. Denote by x the number of defectives among a random sample of size 2. Find the posterior probability distribution of p, given that x is observed.
:::

:::guess Guess first
For x = 2 (both defective), which value of p will the posterior favour? Will it be more or less one-sided than the x = 0 case (0.6550 for p = 0.1)?
:::

The slide's solution in three lines:

1. X ∣ p ~ B(2, p): f(x ∣ p) = C(2, x)p^{x}(1 − p)^{2−x}.
2. g(x) = C(2, x)[(0.1)^{x}(0.9)^{2−x}(0.6) + (0.2)^{x}(0.8)^{2−x}(0.4)].
3. π(0.1 ∣ x) = C(2, x)(0.1)^{x}(0.9)^{2−x}(0.6)/g(x), and π(0.2 ∣ x) = 1 − π(0.1 ∣ x).

C(2, x) is in the top of line 3 and inside g(x), so it cancels; it must be used in both or in neither.

| x | f(x ∣ 0.1) × 0.6 | f(x ∣ 0.2) × 0.4 | g(x) | π(0.1 ∣ x) | π(0.2 ∣ x) |
|---|---|---|---|---|---|
| 0 | 0.81 × 0.6 = 0.486 | 0.64 × 0.4 = 0.256 | 0.742 | **0.6550** | **0.3450** |
| 1 | 0.18 × 0.6 = 0.108 | 0.32 × 0.4 = 0.128 | 0.236 | **0.4576** | **0.5424** |
| 2 | 0.01 × 0.6 = 0.006 | 0.04 × 0.4 = 0.016 | 0.022 | **0.2727** | **0.7273** |

Checks on the table: g(0) + g(1) + g(2) = 0.742 + 0.236 + 0.022 = 1.000, and each row's posterior adds to 1.

[[fig:prior_posterior|What this graph plots: four pairs of bars, the prior and the posterior after x = 0, 1 and 2 defectives. In each pair, blue = probability that p = 0.1, red = probability that p = 0.2; each pair adds to 1. Labels are rounded to three decimals.|w=78]]

Reading the figure: each defective found moves belief toward p = 0.2: from the prior 0.4 to 0.3450 (x = 0), 0.5424 (x = 1) and 0.7273 (x = 2).

**Answer.** The posterior distribution of p is the table's last two columns, one row for each observed x. For x = 2 the posterior favours **p = 0.2 (0.7273)**, more one-sided than the x = 0 case. Two defectives are 0.04/0.01 = 4 times as likely under p = 0.2, while two good items are only 1.27 times as likely under p = 0.1: a defective is rare, so seeing one says more.

:::check Check 6
Same machine and sample of 2, but the prior is P(p = 0.1) = P(p = 0.2) = 0.5. (a) Find π(0.2 ∣ x = 1). (b) With equal prior weights, what is the posterior proportional to?
:::

### 7 · One number: the posterior mean

The posterior is a whole distribution. When a question asks for "an estimate of p", one number is wanted.

:::q Predict
After x = 0 in Ex. 15, give a single estimate of p.
:::

:::guess Guess first
Should it be 0.1, 0.2, or something between them?
:::

:::note Terms
**Bayes estimate (posterior mean):** E(θ ∣ x) = Σ θ π(θ ∣ x), the balance point of the posterior (file 03a step 2). It is the best single number when an error of size e costs e^{2} (squared-error loss): Balakrishnan (CMU l.16, Thm 16.5) and Chan (§6.8). If the cost is the size of the error itself, the best number is the posterior **median** instead.
:::

[[fig:bayes_means|What this graph plots: a number line of estimates of p. The two possible values 0.1 and 0.2 are marked. Dots: the prior mean 0.14 and the posterior means after x = 0, 1 and 2 defectives (0.1345, 0.1542, 0.1727).|w=86]]

| | weight on 0.1 | weight on 0.2 | mean |
|---|---|---|---|
| prior | 0.6 | 0.4 | 0.14 |
| after x = 0 | 0.6550 | 0.3450 | 0.1345 |
| after x = 1 | 0.4576 | 0.5424 | 0.1542 |
| after x = 2 | 0.2727 | 0.7273 | 0.1727 |

Reading the table: every mean lies between 0.1 and 0.2, and it moves toward 0.2 as more defectives are found. The mean need not be a possible value of p: it is a balance point, not a choice between 0.1 and 0.2.

**Answer to the Predict.** E(p ∣ x = 0) = 0.1 × 0.6550 + 0.2 × 0.3450 = 0.0655 + 0.0690 = **0.1345**: between the two, a little below the prior mean 0.1 × 0.6 + 0.2 × 0.4 = 0.14. The two good items pulled the estimate down.

**Compare 09b.** The MLE from 0 defectives in 2 is p̂ = x/n = 0/2 = 0: a value the prior says is impossible, since p is 0.1 or 0.2. The Bayes estimate combines the prior with the data; the MLE uses the data only.

:::check Check 7
(a) Find the Bayes estimate (posterior mean) of p after x = 2 in Ex. 15, and compare it with the MLE x/n.
(b) Twenty items are tested and all are good. Find π(0.1 ∣ x = 0) with the Ex. 15 prior and with a 0.5/0.5 prior. Compare the gap between the two answers with the same gap for 2 items (0.6550 against 0.5586).
:::

---

## Exam form

**Definitions.**

- **Bayesian approach**: the parameter is a random variable; inference combines a prior distribution with the observed data. **Classical approach**: the parameter is a fixed unknown constant; inference uses the data only.
- **Subjective probability**: a person's degree of belief in a statement; different people may give different values.
- **Prior π(θ)**: the distribution of θ before the data, reflecting the experimenter's prior belief.
- **Posterior π(θ ∣ x)**: the distribution of θ after the data x are observed.
- **Conditional perspective**: inference is conditional on the data actually observed; knowledge of θ after sampling = data + prior.

**Posterior.** π(θ | x) = f(x | θ)π(θ)/g(x), with g(x) = Σ_{θ} f(x | θ)π(θ) (θ discrete) or ∫ f(x | θ)π(θ) dθ (θ continuous).

**Procedure (discrete prior, as in Ex. 15).**

1. List the values of θ and their prior probabilities.
2. Write the likelihood f(x ∣ θ) for the observed x (binomial, Poisson, …).
3. Multiply: f(x ∣ θ)π(θ) for each θ; add the products to get g(x).
4. Posterior = each product ÷ g(x). Check that the posterior adds to 1.
5. If an estimate is asked: posterior mean Σ θ π(θ ∣ x).

| | Classical (MoM, MLE) | Bayesian |
|---|---|---|
| θ is | a fixed unknown constant | a random variable |
| Uses | the data only | the data + a prior |
| Answer | a value (or an interval) for θ | a posterior distribution of θ; its mean if one number is needed |

## Traps

- Stopping at the products: f(x ∣ θ)π(θ) are not yet probabilities until divided by g(x).
- Using C(n, x) in one product and not the other: it cancels only when used in both.
- Calling the prior "the data": the prior is fixed before the sample is seen.
- Reporting the MLE when a Bayes estimate is asked: the Bayes estimate is the posterior mean, not x/n.
- Expecting the posterior mean to be one of the possible values of θ: 0.1345 is neither 0.1 nor 0.2.

## Self-test

1. State the key difference between Bayesian and classical estimation.
2. Define the prior and the posterior distributions, and say what g(x) is.
3. A coin is either fair (p = 0.5) or biased (p = 0.8), with prior probabilities 0.7 and 0.3. One toss gives a head. Find the posterior P(p = 0.8 ∣ head).
4. For Q3, find the posterior mean of p.
5. Ex. 15's machine and prior, but a sample of 3 items gives 1 defective. Find the posterior distribution of p and the Bayes estimate.

<!--ANSWERS-->
## Answers

**Check 1.** (b) and (c). (b) puts a probability (3 to 2, i.e. 0.6) on a value of the parameter; (c) is the Bayesian view itself. (a) is a classical point estimate from the data alone.

**Check 2.** (a) 0.7 + 0.4 = 1.1: the probabilities add to more than 1. (b) Divide each by 1.1: P(p = 0.1) = 0.7/1.1 = **0.6364**, P(p = 0.2) = 0.4/1.1 = **0.3636**. (Dividing by the total is what g(x) does in step 5.)

**Check 3.** f(1 ∣ 0.1) = 2(0.1)(0.9) = **0.18**; f(1 ∣ 0.2) = 2(0.2)(0.8) = **0.32**. It favours **p = 0.2**, 0.32/0.18 = **1.78 times**.

**Check 4.** g(1) = 0.6 × 0.18 + 0.4 × 0.32 = 0.108 + 0.128 = **0.236**. f(2 ∣ 0.1) = 0.01, f(2 ∣ 0.2) = 0.04, so g(2) = 0.006 + 0.016 = **0.022**. Total 0.742 + 0.236 + 0.022 = **1**: the sample must show 0, 1 or 2 defectives, so g is a PMF of x.

**Check 5.** (a) Likelihoods for one defective in one item: 0.1 and 0.2. Products 0.1 × 0.6 = 0.06, 0.2 × 0.4 = 0.08; g = 0.14. π(0.1 ∣ 1) = 0.06/0.14 = **0.4286**.
(b) Prior ½ and ½ (one shipment picked at random, whatever its size). Likelihoods of two good parts: 0.9^{2} = 0.81 and 0.95^{2} = 0.9025. Products 0.405 and 0.45125; g = 0.85625. P(first ∣ two good) = 0.405/0.85625 = **0.4730**. (This treats the two draws as independent; drawing without replacement from 1000 and 2000 parts gives the same 0.4730 to four decimals.)

**Check 6.** (a) Products 0.18 × 0.5 = 0.09 and 0.32 × 0.5 = 0.16; g = 0.25. π(0.2 ∣ 1) = 0.16/0.25 = **0.64**. (b) With equal prior weights the prior cancels: the posterior is proportional to the **likelihood** alone (0.64 = 0.32/(0.18 + 0.32)).

**Check 7.** (a) E(p ∣ x = 2) = 0.1 × 0.2727 + 0.2 × 0.7273 = 0.02727 + 0.14546 = **0.1727**. The MLE is 2/2 = **1**: every item defective, a value far outside what the prior allows.
(b) Likelihoods 0.9^{20} = 0.12158 and 0.8^{20} = 0.011529. Ex. 15 prior: products 0.072946 and 0.0046117, so π(0.1 ∣ 0) = 0.072946/0.077558 = **0.9405**. Prior 0.5/0.5: 0.12158/(0.12158 + 0.011529) = **0.9134**. Gap **0.027**, against 0.6550 − 0.5586 = **0.096** for 2 items: with more data the posterior depends less on the prior.

**Self-test.**

1. Bayesian: θ is a random variable with a prior distribution, and inference uses data + prior. Classical: θ is a fixed unknown constant, and inference uses the data only.
2. Prior: the distribution of θ before the data (prior belief). Posterior: the distribution of θ given the observed data. g(x) = Σ f(x | θ)π(θ) (or the integral): the total probability of the data, which makes the posterior add to 1.
3. Products 0.5 × 0.7 = 0.35 and 0.8 × 0.3 = 0.24; g = 0.59. P(p = 0.8 ∣ H) = 0.24/0.59 = **0.4068**.
4. 0.5 × 0.5932 + 0.8 × 0.4068 = **0.6220**.
5. f(1 ∣ 0.1) = 3(0.1)(0.9)^{2} = 0.243 and f(1 ∣ 0.2) = 3(0.2)(0.8)^{2} = 0.384. Products 0.243 × 0.6 = 0.1458 and 0.384 × 0.4 = 0.1536; g(1) = 0.2994. Posterior π(0.1 ∣ 1) = **0.4870**, π(0.2 ∣ 1) = **0.5130**. Bayes estimate 0.1 × 0.4870 + 0.2 × 0.5130 = **0.1513**.
<!--/ANSWERS-->
