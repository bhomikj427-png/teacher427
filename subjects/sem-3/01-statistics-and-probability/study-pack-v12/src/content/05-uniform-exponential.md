# 05 — Uniform and exponential distributions

<div class="sub">Gupta & Kapoor ch. 8 (§8.1, §8.6) · blueprint row 2 "uniform, exponential" · 13 real questions (MTE, Assignment 2) · needs 02, 03, 04 (Poisson)</div>

## Map

[[map:1 Uniform: flat density > 2 Uniform in a word problem > 3 Absolute values and the mean > 4 Exponential: waiting times > 5 Memoryless property > 6 Conditionals that are not memoryless|here=1]]

## The questions this file answers

- <span class="tag">MTE B4 · 4 marks</span> Buses arrive every 15 minutes from 7 a.m. A passenger arrives at a time uniform between 7:00 and 7:30. P(waits less than 5 minutes).
- <span class="tag">A2 B2</span> X uniform between 10 and 20: P(X > 16).
- <span class="tag">A2 B8</span> X uniform on (−3, 3): P(X < 2), P(|X| < 2), P(|X − 2| < 2), and K with P(X > K) = 1/3.
- <span class="tag">A2 C4</span> Rounding error uniform on (−0.5, 0.5): P(error greater than 0.2 in magnitude).
- <span class="tag">A2 D4</span> Plant lifespan uniform on 15 to 35 weeks: P(25 ≤ X ≤ 30).
- <span class="tag">A2 D2</span> Buses arrive exponentially at 4 per hour: P(wait more than 30 minutes).
- <span class="tag">A2 B7</span> Repair time exponential with λ = ½: P(more than 2 h); P(more than 11 h given more than 8 h).
- <span class="tag">A2 C1</span> Lifetime exponential, mean 1000 h: P(survive 1500 h given it survived 500 h).
- <span class="tag">A2 B5</span> Exponential with mean 2: P(X < 1 | X < 2).
- <span class="tag">A2 MCQ 4, 5, 8, 10</span> Uniform variance; memoryless distribution; exponential SD; P(c < X < d) for d beyond b.

---

## Build

### 1 · Uniform: a flat density

File 02's rule P = area is easiest to see on a rectangle.

:::q <span class="tag">A2 B2</span>
A random variable X is uniformly distributed between 10 and 20. Find the exact probability that X is greater than 16.
:::

:::guess Guess first
What fraction of the interval 10–20 lies above 16?
:::

**Term.** **Uniform X ~ U(a, b)**: every value in (a, b) is equally likely (G&K §8.1). Total area 1 over width b − a forces the height:

$$f(x) = \frac{1}{b − a},  a < x < b;    P(c < X < d) = \frac{d − c}{b − a}  (for a ≤ c < d ≤ b)$$

**Answer.** P(X > 16) = (20 − 16)/(20 − 10) = **0.4**.

<span class="tag">A2 MCQ 10</span> On [a, b], with c inside and d > b: the density is 0 beyond b, so only (c, b) counts: P(c < X < d) = **(b − c)/(b − a)** (a).

:::check Check 1
<span class="tag">A2 D4</span> Plant lifespan is uniform between 15 and 35 weeks. Find P(25 ≤ X ≤ 30).
:::

### 2 · Uniform in a word problem

The skill is turning the story into an interval of X.

:::q <span class="tag">MTE B4 · 4 marks</span>
Buses arrive at a specified stop at 15-minute intervals starting at 7 a.m. (7:00, 7:15, 7:30, …). A passenger arrives at a random time uniformly distributed between 7:00 and 7:30. Find the probability that he waits less than 5 minutes.
:::

:::guess Guess first
List the arrival times (in minutes after 7:00) that give a wait under 5 minutes.
:::

X = minutes after 7:00, X ~ U(0, 30), f(x) = 1/30. A wait under 5 minutes means arriving in the 5 minutes before a bus: 7:10–7:15 or 7:25–7:30.

[[fig:uniform_bus|The two green strips are the good arrival times.|w=80]]

**Answer.** P(10 < X < 15) + P(25 < X < 30) = 5/30 + 5/30 = **1/3**.

:::check Check 2
Same buses, same arrival window. Find P(he waits more than 10 minutes).
:::

### 3 · Absolute values, and the uniform's mean and variance

Inequalities with absolute values are intervals in disguise.

:::q <span class="tag">A2 B8</span>
X is uniformly distributed over (−3, 3). Compute (i) P(X < 2) (ii) P(|X| < 2) (iii) P(|X − 2| < 2) (iv) K for which P(X > K) = 1/3.
:::

:::guess Guess first
Rewrite |X − 2| < 2 as "… < X < …".
:::

**Rule.** |X − m| < r ⇔ m − r < X < m + r. Then cut the interval to the range (a, b).

**Answer.** f = 1/6.
(i) (2 − (−3))/6 = **5/6**. (ii) −2 < X < 2: 4/6 = **2/3**. (iii) 0 < X < 4, cut to 0 < X < 3: 3/6 = **1/2**. (iv) (3 − K)/6 = 1/3 ⇒ **K = 1**.

**Mean and variance** (G&K §8.1):

$$E(X) = \frac{a + b}{2},    Var(X) = \frac{(b − a)^{2}}{12}$$

<span class="tag">A2 MCQ 4</span> The variance is **(b − a)^{2}/12** (b).

:::check Check 3
<span class="tag">A2 C4</span> Rounding error X ~ U(−0.5, 0.5). Find P(|X| > 0.2).
:::

### 4 · Exponential: the waiting time

File 04's Poisson counts events; the exponential measures the gap until the next one.

:::q <span class="tag">A2 D2</span>
The arrival of buses at a university terminal follows an exponential distribution with an average rate of 4 buses per hour. A student arrives at a random time. What is the probability that the student waits more than 30 minutes for the next bus?
:::

:::guess Guess first
At 4 per hour, what is the average gap between buses? Is a 30-minute wait likely?
:::

**Term.** **Exponential X ~ Exp(λ)**, rate λ > 0 (G&K §8.6):

$$f(x) = λe^{−λx},  x ≥ 0;    P(X > x) = e^{−λx}$$

$$E(X) = \frac{1}{λ},    Var(X) = \frac{1}{λ^{2}},    σ = \frac{1}{λ}$$

Keep the units matched: λ per hour with x in hours. If the question gives the **mean** m, then λ = 1/m.

**Answer.** λ = 4 per hour, x = 0.5 hour. P(X > 0.5) = e^{−4 × 0.5} = e^{−2} = **0.1353**.

<span class="tag">A2 MCQ 8</span> The SD of Exp(λ) is **1/λ** (b): equal to the mean.

:::check Check 4
<span class="tag">A2 B7 (i)</span> Repair time is exponential with λ = ½ per hour. Find P(repair takes more than 2 hours).
:::

### 5 · The memoryless property

Exponential questions often give "already waited" information. One property removes it.

:::q <span class="tag">A2 B7 (ii)</span>
Repair time is exponential with λ = ½. What is the probability that a repair takes more than 11 hours given that it has already exceeded 8 hours?
:::

:::guess Guess first
Is it smaller than, equal to, or larger than P(more than 3 hours)?
:::

**Memoryless property** (G&K §8.6): for s, t ≥ 0,

$$P(X > s + t | X > s) = \frac{e^{−λ(s + t)}}{e^{−λs}} = e^{−λt} = P(X > t)$$

Time already waited does not change the remaining wait. The exponential is the only continuous distribution with this property.

[[fig:expo_memoryless|Red over grey has the same ratio as P(X > 3) over the whole curve.|w=80]]

**Answer.** P(X > 11 | X > 8) = P(X > 3) = e^{−3/2} = **e^{−1.5} = 0.2231**.

<span class="tag">A2 MCQ 5</span> The memoryless continuous distribution: **exponential** (c).

:::check Check 5
<span class="tag">A2 C1</span> Time to failure is exponential with mean 1000 hours. Find P(it survives at least 1500 hours, given it has survived 500).
:::

### 6 · Conditionals that are not memoryless

Memorylessness is about "**more than**, given **more than**". Other conditionals need file 01's ratio.

:::q <span class="tag">A2 B5</span>
X has an exponential distribution with mean 2. Find P(X < 1 | X < 2).
:::

:::guess Guess first
Is this the same as P(X < 1)? Write yes or no and a reason.
:::

**Answer.** λ = 1/2. P(X < x) = 1 − e^{−x/2}.

$$P(X < 1 | X < 2) = \frac{P(X < 1)}{P(X < 2)} = \frac{1 − e^{−0.5}}{1 − e^{−1}} = \frac{0.3935}{0.6321} = 0.6225$$

Not P(X < 1) = 0.3935: knowing X < 2 removes the long right tail.

:::note Key slip
Assignment 2's key prints 0.5679. Neither λ = ½ nor λ = 2 gives that value; 0.6225 was checked by numerical integration.
:::

:::check Check 6
X ~ Exp(λ = 1). Find P(1 < X < 3 | X > 1).
:::

---

## Exam form

| | Uniform U(a, b) | Exponential Exp(λ) |
|---|---|---|
| Story | equally likely anywhere in (a, b) | waiting time between Poisson events |
| f(x) | 1/(b − a), a < x < b | λe^{−λx}, x ≥ 0 |
| CDF F(x) | (x − a)/(b − a) | 1 − e^{−λx} |
| Mean | (a + b)/2 | 1/λ |
| Variance | (b − a)^{2}/12 | 1/λ^{2} |
| Key fact | probability = length/(b − a) | P(X > s + t ∣ X > s) = P(X > t) |

**Link to file 04.** If counts are Poisson with rate λ per unit time, the gap between events is Exp(λ), mean 1/λ.

## Traps

- Using the mean as λ: an exponential with **mean 2** has λ = ½.
- Mixing units: rate per hour with time in minutes.
- Forgetting to cut an interval to (a, b) for a uniform (A2 B8 (iii)).
- Applying memorylessness to "less than, given less than" (A2 B5): it only covers "more than, given more than".
- P(X ≥ x) and P(X > x) are equal for continuous X; no ±1 correction.

## Self-test

1. Write the pdf, mean and variance of U(a, b) and Exp(λ).
2. X ~ U(0, 10). Find P(3 < X < 8) and the variance.
3. A machine's life is exponential with mean 5 years. Find P(it lasts more than 5 years).
4. For the machine in Q3, P(lasts more than 8 years | already lasted 3)?
5. State the memoryless property and say which distribution has it.
6. Calls arrive as a Poisson process at 2 per minute. What is the distribution of the time between calls, and its mean?
7. X ~ U(−1, 1). Find P(|X| > 0.5) and E(X^{2}).

<!--ANSWERS-->
## Answers

**Check 1.** (30 − 25)/20 = **0.25**.

**Check 2.** Waits over 10 minutes: arrive 7:00–7:05 or 7:15–7:20: 10/30 = **1/3**.

**Check 3.** 1 − 0.4/1 = **0.6**.

**Check 4.** e^{−1} = **0.3679**.

**Check 5.** P(X > 1000) = e^{−1} = **0.3679** (memoryless: 1500 − 500 = 1000).

**Check 6.** (e^{−1} − e^{−3})/e^{−1} = 1 − e^{−2} = **0.8647**.

**Self-test.**

1. U: 1/(b − a), (a + b)/2, (b − a)^{2}/12. Exp: λe^{−λx}, 1/λ, 1/λ^{2}.
2. **0.5**; 100/12 = **8.33**.
3. λ = 0.2: e^{−1} = **0.3679**.
4. P(X > 5) = **0.3679** (memoryless).
5. P(X > s + t | X > s) = P(X > t): the exponential.
6. Exponential with λ = 2 per minute; mean **½ minute**.
7. **0.5**; E(X^{2}) = Var + 0 = 4/12 = **1/3**.
<!--/ANSWERS-->
