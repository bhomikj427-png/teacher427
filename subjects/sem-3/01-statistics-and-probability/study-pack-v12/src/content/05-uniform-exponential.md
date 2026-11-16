# 05 — Uniform and exponential distributions

<div class="sub">Gupta & Kapoor §8.1 (rectangular or uniform distribution), §8.6 (exponential; Example 8.40 "lacks memory"; ch. 8 exercise 7(a) = A2 B5) · blueprint row 2 "standard probability distributions: uniform, exponential" · 14 real questions (MTE B4; A2 B2, B5, B7, B8, C1, C4, D2, D4, MCQ 4, 5, 8, 10) · needs 01 (conditional probability, step 7), 02b (PDF as area step 1, CDF step 3), 03a (E(X) and Var for a continuous X, step 7), 04b (Poisson counts at a rate, step 1)</div>

## Map

[[map:1 Uniform: a flat density > 2 Probability = length ratio > 3 The bus word problem > 4 Absolute values > 5 Mean and variance > 6 Finding K > 7 Exponential: waiting for the next event > 8 Survival P(X > x) > 9 Memoryless > 10 A conditional that is not memoryless|here=1]]

File 02b turned probability into area under a density curve. This file takes the two simplest curves. The **uniform** is a flat rectangle, so every area is width × height (steps 1–6). The **exponential** is the waiting time until the next event of 04b's Poisson count (steps 7–10). File 06 then moves to the normal curve, where areas come from a table; file 09a uses both means to estimate parameters.

| Symbol | What it means in this file | Typical value |
|---|---|---|
| a, b | the two ends of the interval a uniform X can take (set by the question) | a = −3, b = 3 |
| U(a, b) | short name for "uniform on (a, b)" | U(−3, 3) |
| f(x) | the density: height of the curve at x; area under it = probability (02b step 1) | 1/6 |
| λ | for the exponential: the rate, events per unit time (as in 04b) | ½ per hour |
| 1/λ | the mean waiting time | 2 hours |
| Exp(λ) | short name for "exponential with rate λ" | Exp(½) |
| s, t | lengths of time already waited (s) and still to wait (t), step 9 | s = 8, t = 3 hours |

**Running examples.** Uniform: X ~ U(−3, 3), any value from −3 to 3 equally likely (A2 B8). Exponential: a waiting time with **mean 2**, so λ = ½ (A2 B5, B7).

## The questions this file answers

- <span class="tag">A2 B2</span> A random variable X is uniformly distributed between 10 and 20. Find the exact probability that X is greater than 16.
- <span class="tag">MTE B4 · 4 marks</span> Buses arrive at a specified stop at 15-minute intervals starting at 7 a.m. (7:00, 7:15, 7:30, …). A passenger arrives at a random time uniformly distributed between 7:00 and 7:30. Find the probability that he waits less than 5 minutes.
- <span class="tag">A2 B8</span> A random variable X has uniformly distributed over (−3, 3). Compute (i) P(X < 2), (ii) P(|X| < 2), (iii) P(|X − 2| < 2), and (iv) find K for which P(X > K) = 1/3.
- <span class="tag">A2 C4</span> When values are rounded to the nearest integer, the rounding error X is uniformly distributed between −0.5 and 0.5. Find the probability that a rounding error is greater than 0.2 in magnitude.
- <span class="tag">A2 D4</span> The lifespan of a particular species of plant in a controlled greenhouse is uniformly distributed between 15 and 35 weeks. Find the probability that the plant will live for at least 25 weeks but no more than 30 weeks.
- <span class="tag">A2 D2</span> The arrival time of buses at a university terminal follows an exponential distribution with an average rate of 4 buses per hour. What is the probability that a student will have to wait more than 30 minutes for the next bus?
- <span class="tag">A2 B7</span> The time (in hours) required to repair a watch is exponentially distributed with parameter λ = ½. (i) What is the probability that the repair time exceeds 2 hours? (ii) What is the probability that a repair takes more than 11 hours given that its duration exceeds 8 hours?
- <span class="tag">A2 C1</span> The time to failure of a hardware component (in hours) is exponential with a mean of 1000 hours. Find the probability that it will survive at least 1500 hours, given that it has already survived 500 hours.
- <span class="tag">A2 B5</span> If X has an exponential distribution with mean 2, find P(X < 1 | X < 2).
- <span class="tag">A2 MCQ 4, 5, 8, 10</span> Uniform variance; the memoryless distribution; the exponential's SD; P(c < X < d) when d lies beyond b.

---

## Build

### 1 · Uniform: a flat density

File 02b's rule "probability = area" is easiest on a rectangle.

:::q <span class="tag">A2 B2</span>
A random variable X is uniformly distributed between 10 and 20. Find the exact probability that X is greater than 16.
:::

:::guess Guess first
What fraction of the stretch from 10 to 20 lies above 16? Write it as a decimal.
:::

:::note Terms
**Uniform distribution U(a, b):** X can be any value between a and b, and equal-length pieces of (a, b) are equally likely (G&K §8.1; also called "rectangular" because its graph is a rectangle). **Height 1/(b − a):** the total area must be 1 (02b step 2), and the rectangle is b − a wide, so its height is 1/(b − a).
:::

$$f(x) = \frac{1}{b − a},  a < x < b;    f(x) = 0 \text{ elsewhere}$$

[[fig:unif_rect|What this graph plots: the density of U(10, 20). Horizontal axis: x. Vertical axis: f(x), the height. The rectangle is 10 wide and 0.1 high (area 1). Red strip: x from 16 to 20, the event X > 16; its area is the probability.|w=76]]

| x | f(x) |
|---|---|
| 9 | 0 (outside) |
| 12 | 0.1 |
| 16 | 0.1 |
| 21 | 0 (outside) |

**Answer to the question.** P(X > 16) = width × height = (20 − 16) × 0.1 = **0.4**.

:::check Check 1
For the running example U(−3, 3): (a) find the height f(x); (b) find P(X < 0).
:::

### 2 · Probability = length ratio

Step 1's area was width × 1/(b − a). That is a ratio of lengths, which makes every uniform question a length question.

:::q <span class="tag">A2 MCQ 10</span>
A continuous Uniform distribution defined over the interval [a, b]. What is P(c < X < d), where c ∈ (a, b) and d > b: a) (b − c)/(b − a) b) (d − c)/(b − a) c) (d − c)/(d − a) d) (b − c)/(d − a)
:::

:::guess Guess first
Draw the rectangle from a to b; mark c inside and d to the right of b. Which part of (c, d) has area?
:::

**Rule** (from step 1, for a ≤ c < d ≤ b):

$$P(c < X < d) = \frac{d − c}{b − a} = \frac{\text{length of the event's stretch}}{\text{length of the whole range}}$$

**Clip first.** If part of (c, d) lies outside (a, b), the height there is 0, so that part adds nothing: cut (c, d) back to (a, b) before taking the ratio.

| U(−3, 3), event | stretch inside (−3, 3) | probability |
|---|---|---|
| 0 < X < 2 | 0 to 2, length 2 | 2/6 = 1/3 |
| 1 < X < 5 | 1 to 3, length 2 | 2/6 = 1/3 |
| X > 4 | none | 0 |

**Answer to the question.** Only (c, b) lies under the rectangle: P(c < X < d) = **(b − c)/(b − a)**, option (a).

:::check Check 2
<span class="tag">A2 D4</span> The lifespan of a particular species of plant in a controlled greenhouse is uniformly distributed between 15 and 35 weeks. Find the probability that the plant will live for at least 25 weeks but no more than 30 weeks.
:::

### 3 · The bus word problem

The skill here is turning a story into stretches of X; the arithmetic is step 2's ratio.

:::q <span class="tag">MTE B4 · 4 marks</span>
Buses arrive at a specified stop at 15-minute intervals starting at 7 a.m. (7:00, 7:15, 7:30, …). A passenger arrives at a random time uniformly distributed between 7:00 and 7:30. Find the probability that he waits less than 5 minutes.
:::

:::guess Guess first
List the arrival times (minutes after 7:00) that give a wait under 5 minutes.
:::

**Terms.** Nothing new. X = arrival time in minutes after 7:00, so X ~ U(0, 30) and f(x) = 1/30.

[[fig:unif_bus|What this graph plots: the density of the arrival time X ~ U(0, 30). Horizontal axis: minutes after 7:00. Vertical axis: f(x) = 1/30. Dashed red lines: buses at 7:00, 7:15, 7:30. Green strips: arrival times with a wait under 5 minutes, the 5 minutes just before each bus.|w=80]]

**Derivation.**

1. A wait under 5 minutes means arriving in the 5 minutes before a bus.
2. The buses inside the window come at 15 and 30 minutes, so the good stretches are 10 < X < 15 and 25 < X < 30.
3. The stretches do not overlap, so their probabilities add (01 step 6): 5/30 + 5/30.

**Answer to the question.** P(wait < 5 min) = 10/30 = **1/3**.

:::check Check 3
Same buses, same arrival window. Find P(he waits more than 10 minutes).
:::

### 4 · Absolute values

"|X| < 2" and "greater than 0.2 in magnitude" are stretches written in a short code. Decode, clip, then take step 2's ratio.

:::q <span class="tag">A2 B8 (i)–(iii)</span>
X is uniformly distributed over (−3, 3). Compute (i) P(X < 2), (ii) P(|X| < 2), (iii) P(|X − 2| < 2).
:::

:::guess Guess first
Rewrite |X − 2| < 2 as "… < X < …".
:::

:::note Terms
**|X − m| < r:** X is within distance r of the point m, that is **m − r < X < m + r**. **|X| > r** (magnitude greater than r): X < −r **or** X > r, two stretches.
:::

[[fig:unif_abs|What this graph plots: the density of U(−3, 3), height 1/6. Horizontal axis: x. The arrow marks ∣x − 2∣ < 2, the stretch 0 < x < 4. Green: the part inside (−3, 3), 0 < x < 3. Red bar: 3 to 4, outside the range, so it adds nothing.|w=78]]

**Answer to the question.** f = 1/6 and the range has length 6.

| part | stretch | clipped to (−3, 3) | probability |
|---|---|---|---|
| (i) X < 2 | −3 < X < 2 | same | 5/6 |
| (ii) ∣X∣ < 2 | −2 < X < 2 | same | 4/6 = **2/3** |
| (iii) ∣X − 2∣ < 2 | 0 < X < 4 | 0 < X < 3 | 3/6 = **1/2** |

(i) = **5/6**.

:::check Check 4
<span class="tag">A2 C4</span> When values are rounded to the nearest integer, the rounding error X is uniformly distributed between −0.5 and 0.5. Find the probability that a rounding error is greater than 0.2 in magnitude.
:::

### 5 · Mean and variance of the uniform

Exam MCQs ask for the centre and spread of the rectangle. Both follow from 03a's formulas.

:::q <span class="tag">A2 MCQ 4</span>
If a continuous random variable X is uniformly distributed over the interval (a, b), its variance is given by: a) (a + b)/2 b) (b − a)²/12 c) (b − a)/2 d) (b − a)²/2
:::

:::guess Guess first
For U(−3, 3), where is the balance point (03a step 1)? Write the mean first, then pick the variance option.
:::

**Derivation** (continuous E and Var, 03a step 7):

1. E(X) = ∫ₐᵇ x × 1/(b − a) dx = (b² − a²)/(2(b − a)) = **(a + b)/2**: the midpoint.
2. E(X²) = ∫ₐᵇ x² × 1/(b − a) dx = (b³ − a³)/(3(b − a)) = (a² + ab + b²)/3.
3. Var(X) = E(X²) − (E(X))² (03a step 5) = (a² + ab + b²)/3 − (a + b)²/4.
4. Over the common denominator 12: (4a² + 4ab + 4b² − 3a² − 6ab − 3b²)/12 = (a² − 2ab + b²)/12 = **(b − a)²/12** (G&K §8.1).

| U(a, b) | mean (a + b)/2 | variance (b − a)²/12 | SD |
|---|---|---|---|
| U(−3, 3) | 0 | 36/12 = 3 | 1.732 |
| U(10, 20) | 15 | 100/12 = 8.33 | 2.887 |

Read back: the mean is the middle of the rectangle; the variance depends only on its width.

**Answer to the question.** **(b − a)²/12**, option (b). Option (a) is the mean.

:::check Check 5
X ~ U(0, 12). Find the mean, the variance and the SD.
:::

### 6 · Finding K from a probability

Steps 1–4 went from a stretch to a probability. Now the probability is given and an end of the stretch is unknown.

:::q <span class="tag">A2 B8 (iv)</span>
X is uniformly distributed over (−3, 3). Find K for which P(X > K) = 1/3.
:::

:::guess Guess first
A third of the width 6 is 2. Where must K sit so that the stretch above it is 2 long?
:::

**Derivation.**

1. The event X > K is the stretch from K to 3, length 3 − K (K inside the range).
2. Step 2's ratio: (3 − K)/6 = 1/3.
3. Multiply by 6: 3 − K = 2, so **K = 1**.

**Answer to the question.** **K = 1**.

:::check Check 6
X ~ U(−3, 3). Find K for which P(X < K) = 0.25.
:::

### 7 · Exponential: waiting for the next event

File 04b counted events in an interval. Now measure the other way: the **time until** the next event.

:::q <span class="tag">A2 MCQ 8</span>
If X is an exponentially distributed random variable with the rate parameter λ, what is the standard deviation of X? a) λ b) 1/λ c) 1/λ² d) λ²
:::

:::guess Guess first
Repairs finish at a rate of ½ per hour. On average, how many hours does one repair take?
:::

:::note Terms
**Exponential distribution Exp(λ):** X = the waiting time until the next event when events arrive as in 04b, at an average rate λ per unit time (G&K §8.6). **λ:** events per unit time. **1/λ:** the mean wait; a question that gives the mean m gives λ = 1/m.
:::

$$f(x) = λe^{−λx},  x ≥ 0;    E(X) = \frac{1}{λ},  Var(X) = \frac{1}{λ^{2}},  σ = \frac{1}{λ}$$

[[fig:expo_tail|What this graph plots: the density of the running example, Exp(½), mean 2. Horizontal axis: x, waiting time. Vertical axis: f(x) = ½e^(−x/2). Short waits are the most likely; the curve never reaches 0. Red: the area beyond 4, used in step 8.|w=78]]

| x | f(x) = ½e^{−x/2} |
|---|---|
| 0 | 0.5 |
| 2 | 0.1839 |
| 4 | 0.0677 |
| 6 | 0.0249 |

Read back: the mean wait is one over the rate (rate ½ per hour, mean 2 hours), and the SD equals the mean.

**Answer to the question.** σ = **1/λ**, option (b).

:::check Check 7
Buses arrive at 4 per hour (exponential gaps). Find the mean wait and the SD in minutes.
:::

### 8 · Survival: P(X > x) = e^{−λx}

Most exponential questions ask "more than x". One integral gives a formula that replaces every later integral.

:::q <span class="tag">A2 D2</span>
The arrival time of buses at a university terminal follows an exponential distribution with an average rate of 4 buses per hour. A student arrives at the terminal at a random time. What is the probability that they will have to wait more than 30 minutes for the next bus to arrive?
:::

:::guess Guess first
At 4 buses an hour, the mean wait is 15 minutes. Is a wait over 30 minutes rare (under 20%)? Write a guess.
:::

**Terms.** **Survival probability** P(X > x): the chance the wait is still going on at time x.

**Derivation.**

1. P(X > x) = the integral of λe^{−λu} du from u = x to ∞ (area to the right of x, 02b step 1).
2. = [−e^{−λu}] from x to ∞ = 0 − (−e^{−λx}).
3. **P(X > x) = e^{−λx}**; the CDF is F(x) = 1 − e^{−λx}.

Keep units matched: λ per hour needs x in hours. For the running example (λ = ½), P(X > 4) = e^{−2} = 0.1353: the red area in step 7's figure.

**Answer to the question.** λ = 4 per hour, x = 30 minutes = 0.5 hour: P(X > 0.5) = e^{−4 × 0.5} = e^{−2} = **0.1353**.

:::check Check 8
<span class="tag">A2 B7 (i)</span> The time (in hours) required to repair a watch is exponentially distributed with parameter λ = ½. What is the probability that the repair time exceeds 2 hours?
:::

### 9 · The memoryless property

"It has already taken 8 hours" sounds like it should change the answer. For the exponential it does not.

:::q <span class="tag">A2 B7 (ii)</span>
The repair time is exponential with λ = ½. What is the probability that a repair takes more than 11 hours given that its duration exceeds 8 hours?
:::

:::guess Guess first
Is it smaller than, equal to, or larger than P(more than 3 hours)?
:::

:::note Terms
**Memoryless:** P(X > s + t | X > s) = P(X > t) for all s, t ≥ 0. Having waited s already does not change the chance of waiting t more (G&K §8.6, Example 8.40: the exponential "lacks memory"). The exponential is the only continuous distribution with this property.
:::

[[fig:expo_memory|What this graph plots: the density of Exp(½) twice. Horizontal axis: repair time x (hours). Vertical axis: f(x). Left (0 to 16 hours): grey = all repairs, red = longer than 3 hours. Right (8 to 24 hours, vertical axis magnified e⁴ ≈ 55 times): grey = repairs already past 8 hours, red = past 11. The right panel is the left one shifted by 8 hours; red ÷ grey is e^(−1.5) in both.|w=92]]

**Derivation** (conditional probability, 01 step 7):

1. P(X > 11 | X > 8) = P(X > 11 and X > 8)/P(X > 8).
2. X > 11 already implies X > 8, so the top is P(X > 11).
3. Step 8: = e^{−11/2}/e^{−8/2} = e^{−(11 − 8)/2} = e^{−3/2}.
4. That is P(X > 3): only the extra 3 hours matter.

**Answer to the question.** P(X > 11 | X > 8) = e^{−1.5} = **0.2231** = P(X > 3).

<span class="tag">A2 MCQ 5</span> "The memoryless property is a defining characteristic of which continuous distribution?": (c) **exponential**.

:::check Check 9
<span class="tag">A2 C1</span> The time to failure of a specific hardware component (in hours) follows an exponential distribution with a mean of 1000 hours. Find the probability that the component will survive at least 1500 hours, given that it has already survived 500 hours without failing.
:::

### 10 · A conditional that is not memoryless

Step 9 covered "more than, given more than". Other conditionals have no shortcut: they need 01's ratio.

:::q <span class="tag">A2 B5</span>
If X has an exponential distribution with mean 2, find P(X < 1 | X < 2).
:::

:::guess Guess first
Is it the same as P(X < 1)? Write yes or no, with a reason.
:::

**Terms.** Nothing new: mean 2, so λ = ½, and P(X < x) = 1 − e^{−x/2} (step 8).

**Derivation.**

1. P(X < 1 | X < 2) = P(X < 1 and X < 2)/P(X < 2) (01 step 7).
2. X < 1 already implies X < 2, so the top is P(X < 1).
3. P(X < 1) = 1 − e^{−0.5} = 0.3935; P(X < 2) = 1 − e^{−1} = 0.6321.
4. Ratio: 0.3935/0.6321 = **0.6225**.

$$P(X < 1 | X < 2) = \frac{1 − e^{−0.5}}{1 − e^{−1}} = 0.6225$$

**Answer to the question.** **0.6225**, not P(X < 1) = 0.3935: knowing X < 2 removes the long right tail, so a short wait becomes likelier. G&K prints the same exercise (ch. 8, ex. 7(a)) with this answer, (1 − e^{−θ})/(1 − e^{−2θ}), θ = ½.

:::note Key slip
Assignment 2's key prints 0.5679 for B5. The textbook's printed answer and the numerical check both give 0.6225; the pack uses 0.6225.
:::

:::check Check 10
X ~ Exp(1). Find P(1 < X < 3 | X > 1).
:::

---

## Exam form

| | Uniform U(a, b) | Exponential Exp(λ) |
|---|---|---|
| Story | equally likely anywhere in (a, b) | waiting time to the next Poisson event, rate λ |
| f(x) | 1/(b − a), a < x < b | λe^{−λx}, x ≥ 0 |
| CDF F(x) | (x − a)/(b − a) | 1 − e^{−λx} |
| Mean | (a + b)/2 | 1/λ |
| Variance | (b − a)²/12 | 1/λ² |
| Key fact | probability = length of stretch/(b − a), clipped to (a, b) | P(X > x) = e^{−λx}; P(X > s + t ∣ X > s) = P(X > t) |

**Procedure (uniform):** turn the words into a stretch of X (decode |·|), clip it to (a, b), divide its length by b − a.

**Procedure (exponential):** get λ (λ = 1/mean; match the time units), use e^{−λx} for "more than x", 1 − e^{−λx} for "less than x"; for "more than s + t given more than s" use memorylessness; any other conditional uses the ratio P(A and B)/P(B).

**Proof of memorylessness** (when asked): step 9's derivation, lines 1–4, with s and t in place of 8 and 3.

## Traps

- Using the mean as λ: an exponential with **mean 2** has λ = ½.
- Mixing units: a rate per hour with a time in minutes.
- Forgetting to clip a stretch to (a, b) (A2 B8 (iii), A2 MCQ 10).
- Reading |X| > 0.2 as one stretch: it is two (X < −0.2 or X > 0.2).
- Using memorylessness for "less than, given less than" (A2 B5): it covers only "more than, given more than".
- Adding ±1 to x: for a continuous X, P(X ≥ x) = P(X > x).

## Self-test

1. Write the density, mean and variance of U(a, b) and of Exp(λ).
2. X ~ U(0, 10). Find P(3 < X < 8) and the variance.
3. A machine's life is exponential with mean 5 years. Find P(it lasts more than 5 years).
4. For the machine in Q3, find P(it lasts more than 8 years | it has already lasted 3).
5. State the memoryless property and name the continuous distribution that has it.
6. Calls arrive as a Poisson count at 2 per minute. What is the distribution of the time between calls, and its mean?
7. X ~ U(−1, 1). Find P(|X| > 0.5) and E(X²).

<!--ANSWERS-->
## Answers

**Check 1.** (a) 1/(3 − (−3)) = **1/6**. (b) stretch −3 to 0: 3/6 = **½**.

**Check 2.** (30 − 25)/(35 − 15) = 5/20 = **0.25**.

**Check 3.** Waits over 10 minutes: arrive 7:00–7:05 or 7:15–7:20: 10/30 = **1/3**.

**Check 4.** |X| ≤ 0.2 is −0.2 to 0.2, probability 0.4/1 = 0.4; so P(|X| > 0.2) = 1 − 0.4 = **0.6**.

**Check 5.** Mean **6**; variance 144/12 = **12**; SD √12 = **3.464**.

**Check 6.** (K − (−3))/6 = 0.25 ⇒ K + 3 = 1.5 ⇒ **K = −1.5**.

**Check 7.** λ = 4 per hour: mean = SD = 1/4 hour = **15 minutes**.

**Check 8.** e^{−½ × 2} = e^{−1} = **0.3679**.

**Check 9.** Memoryless: P(X > 1500 | X > 500) = P(X > 1000) = e^{−1000/1000} = e^{−1} = **0.3679**.

**Check 10.** (e^{−1} − e^{−3})/e^{−1} = 1 − e^{−2} = **0.8647** (by memorylessness, it equals P(X < 2)).

**Self-test.**

1. U: 1/(b − a), (a + b)/2, (b − a)²/12. Exp: λe^{−λx}, 1/λ, 1/λ².
2. 5/10 = **0.5**; 100/12 = **8.33**.
3. λ = 0.2 per year: e^{−0.2 × 5} = e^{−1} = **0.3679**.
4. Memoryless: P(X > 5) = **0.3679**.
5. P(X > s + t | X > s) = P(X > t) for all s, t ≥ 0; the exponential.
6. Exponential with λ = 2 per minute; mean **½ minute**.
7. Two stretches of length 0.5 each: 1/2 = **0.5**; E(X²) = Var + mean² = 4/12 + 0 = **1/3**.
<!--/ANSWERS-->
