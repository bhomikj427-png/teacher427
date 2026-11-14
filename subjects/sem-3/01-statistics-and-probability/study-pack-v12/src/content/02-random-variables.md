# 02 — Random variables: PMF, PDF, CDF

<div class="sub">Gupta & Kapoor ch. 5 (§5.1–5.4) · blueprint row 1 "discrete and continuous random variables; PMF; PDF; CDF" · 11 real questions (MTE, Assignment 1) · needs 01</div>

## Map

[[map:1 Random variable > 2 PMF > 3 Building a PMF by counting > 4 CDF > 5 PDF and area > 6 Conditional probability with a PDF|here=1]]

## The questions this file answers

- <span class="tag">MTE A1 · 2 marks</span> Which statement is not correct: the number of calls received during a definite time-period is a continuous random variable / the number of kings drawn from a pack is discrete / the life of a bulb is continuous / (independence statement, file 03).
- <span class="tag">A1 MCQ 1–3</span> Which is a discrete random variable? · The CDF of a random variable is? · Which is true about a PMF?
- <span class="tag">A1 SA 1</span> Find the probability distribution of boys and girls in families with 3 children, assuming equal probabilities. Also give the distribution function.
- <span class="tag">A1 LA 4</span> Four bad oranges are mixed with 16 good ones. Find the distribution of the number of bad oranges in a draw of two.
- <span class="tag">A1 LA 2</span> Table with k, 2k, …, 7k² + k: find k, probabilities, the distribution function, the minimum c with P(X ≤ c) > ½, and P(1.5 < X < 4.5 | X > 2).
- <span class="tag">A1 App 2</span> Calls per hour X = 0, 1, 2, 3 with P = 0.15, 0.35, 0.30, 0.20: CDF, P(X ≤ 2), P(X > 1).
- <span class="tag">A1 SA 3</span> Cable diameter f(x) = 6x(1 − x), 0 ≤ x ≤ 1: check it is a pdf; find b with P(X < b) = P(X > b).
- <span class="tag">A1 SA 2</span> Power consumption f(x) = (1/9)x e^{−x/3}, x > 0; capacity 12: P(supply inadequate).
- <span class="tag">A1 LA 1</span> f(t) = 3 × 10^{−9} t^{2}(100 − t)^{2}, 0 ≤ t ≤ 100: P(death between 60 and 70), and the same given survival to 60.

---

## Build

### 1 · A random variable turns outcomes into numbers

:::q <span class="tag">MTE A1 · 2 marks</span>
Which one of the following statements is **not** correct? (b) The number of calls received during a definite time-period is a continuous random variable. (c) The number of kings drawn from a pack of cards is a discrete random variable. (d) The life of an electric bulb is an example of a continuous random variable. *(Option (a), on independence, is in file 03.)*
:::

:::guess Guess first
For each of (b), (c), (d): can you list the possible values one by one (0, 1, 2, …)? Write "list" or "interval" next to each.
:::

**Terms.**

- **Random variable X**: a rule that gives a number to each outcome. Toss 3 coins, X = number of heads: the outcome HTH gets X = 2.
- **Discrete**: X takes separate values you can list (0, 1, 2, …). Counts are discrete.
- **Continuous**: X takes any value in an interval. Measurements (time, length, weight) are continuous.

**Answer.** Calls are **counted** (0, 1, 2, …), so the number of calls is **discrete**. Statement **(b)** is the incorrect one. Kings drawn (0–4) are discrete, bulb life (any time ≥ 0) is continuous, so (c) and (d) are correct.

:::check Check 1
<span class="tag">A1 MCQ 1</span> Which is discrete: height of students / time to complete an exam / number of defective bulbs in a box / temperature of a city?
:::

### 2 · The PMF: a probability for each value

A discrete X needs a probability for each of its values.

:::q <span class="tag">A1 MCQ 3 · 1 mark</span>
Which of the following is true about a PMF? (a) It can take negative values. (b) Its sum over all values equals 1. (c) It is decreasing. (d) It is defined only for continuous variables.
:::

:::guess Guess first
What must the probabilities of "0 heads, 1 head, 2 heads, 3 heads" add up to? Pick the option.
:::

**Term.** **PMF** (probability mass function) p(x) = P(X = x), for a discrete X. Two conditions make a table a valid PMF (G&K §5.3):

$$p(x) ≥ 0 for every x    and    Σ p(x) = 1$$

**Answer.** **(b)**. Probabilities are never negative and the values of X cover every outcome once, so they add to 1.

The "sum to 1" condition finds an unknown constant:

:::q <span class="tag">A1 LA 2 (i)</span>
X takes 0, 1, …, 7 with probabilities 0, k, 2k, 2k, 3k, k^{2}, 2k^{2}, 7k^{2} + k. Find k.
:::

**Answer.** Σp = 10k^{2} + 9k = 1, so 10k^{2} + 9k − 1 = 0, (10k − 1)(k + 1) = 0. k = −1 is rejected (p(1) = k would be negative), so **k = 1/10**.

:::note The assignment's table has a slip
Assignment 1 prints P(X = 0) = **k**, not 0. With that table Σp = 10k^{2} + 12k = 1 gives k = (−6 + √46)/10 ≈ 0.0782, and none of the key's answers (k = 1/10, 81/100, 4/5, 5/7) follow. The key matches the Gupta & Kapoor version, where **P(X = 0) = 0**. The pack uses that version.
:::

:::check Check 2
X = 1, 2, 3, 4 with P(X = x) = cx. Find c.
:::

### 3 · Building a PMF by counting

Most questions give the experiment, not the table. The PMF is then built by counting.

:::q <span class="tag">A1 SA 1</span>
Find the probability distribution of boys and girls in families with 3 children, assuming equal probabilities of boys and girls. Also give the distribution function.
:::

:::guess Guess first
List the 8 families (BBB, BBG, …). How many have exactly 2 boys?
:::

**Method.** (1) List the outcomes. (2) Give each its value of X. (3) Add the probabilities of outcomes with the same value.

| X = boys | Families | P(X = x) |
|---|---|---|
| 0 | GGG | 1/8 |
| 1 | BGG, GBG, GGB | 3/8 |
| 2 | BBG, BGB, GBB | 3/8 |
| 3 | BBB | 1/8 |

[[fig:pmf_cdf|Left: the PMF just found. Right: its CDF, which step 4 builds.|w=95]]

**Answer.** PMF 1/8, 3/8, 3/8, 1/8 for x = 0, 1, 2, 3 (sum 8/8 ✓). The distribution function is in step 4: **1/8, 4/8, 7/8, 1**.

When the items are drawn **without replacement**, count with combinations C(n, r):

:::q <span class="tag">A1 LA 4</span>
Four bad oranges are mixed accidentally with 16 good oranges. Find the probability distribution of the number of bad oranges in a draw of two oranges.
:::

**Answer.** Ways to draw 2 of 20: C(20, 2) = 190.
P(X = 0) = C(16, 2)/190 = 120/190 = **12/19**; P(X = 1) = 4 × 16/190 = 64/190 = **32/95**; P(X = 2) = C(4, 2)/190 = 6/190 = **3/95**. Sum = (120 + 64 + 6)/190 = 1 ✓.

:::check Check 3
Two dice are thrown; X = the larger of the two numbers. Find P(X = 1) and P(X = 6).
:::

### 4 · The CDF: probability accumulated up to x

The PMF gives one value at a time; most questions ask "at most" or "more than", which is a running total.

:::q <span class="tag">A1 MCQ 2 · 1 mark</span>
The cumulative distribution function (CDF) of a random variable is: (a) P(X = x) (b) P(X ≤ x) (c) P(X ≥ x) (d) P(X > x)
:::

:::guess Guess first
"Cumulative" means "running total". Of which probabilities? Pick the option.
:::

**Term.** **CDF** (distribution function) F(x) = P(X ≤ x) (G&K §5.2). For a discrete X it is the running sum of the PMF: a staircase that rises from 0 to 1 and never goes down.

**Answer.** **(b)**.

:::q <span class="tag">A1 App 2</span>
Calls per hour X = 0, 1, 2, 3 with P(X) = 0.15, 0.35, 0.30, 0.20. Find the CDF, P(X ≤ 2) and P(X > 1).
:::

**Answer.** Running sums: F(0) = 0.15, F(1) = 0.15 + 0.35 = 0.50, F(2) = 0.80, F(3) = 1.00.
P(X ≤ 2) = F(2) = **0.80**. P(X > 1) = 1 − F(1) = **0.50**. (Staffing: half of all hours bring 2 or more calls.)

**Two CDF uses from A1 LA 2** (k = 1/10, so p = 0, 0.1, 0.2, 0.2, 0.3, 0.01, 0.02, 0.17):

| x | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| F(x) | 0 | 1/10 | 3/10 | 5/10 | 8/10 | 81/100 | 83/100 | 1 |

- **Smallest c with P(X ≤ c) > ½:** F(3) = 0.5 is not greater than ½; F(4) = 0.8 is. **c = 4**.
- **P(1.5 < X < 4.5 | X > 2)** = P(X = 3 or 4)/P(X > 2) = (0.2 + 0.3)/(1 − 0.3) = 0.5/0.7 = **5/7**.

:::note The assignment's wording
A1 LA 2 (ii) asks P(X > 6) and P(X ≥ 6); its key prints 81/100, which is **P(X < 6)**. The correct values: P(X > 6) = P(7) = 0.17 = **17/100**, P(X ≥ 6) = 0.02 + 0.17 = **19/100**, P(X < 6) = **81/100**, P(0 < X < 5) = **4/5**.
:::

:::check Check 4
From the calls table: find P(1 ≤ X ≤ 2) using F only.
:::

### 5 · The PDF: probability is area

For a continuous X, a single value has probability 0. Probability lives in intervals, as area.

:::q <span class="tag">A1 SA 3</span>
The diameter of an electric cable X is a continuous random variable with pdf f(x) = 6x(1 − x), 0 ≤ x ≤ 1. (i) Check that it is a pdf. (ii) Determine b such that P(X < b) = P(X > b).
:::

:::guess Guess first
The curve 6x(1 − x) is symmetric about x = ½. Guess b before integrating.
:::

**Term.** **PDF** (probability density function) f(x), for a continuous X (G&K §5.4):

$$f(x) ≥ 0,    ∫ f(x) dx = 1 (over all x),    P(a ≤ X ≤ b) = ∫_{a}^{b} f(x) dx$$

[[fig:pdf_area|The height f(x) is not a probability; the area under it is.|w=62]]

So P(X = a) = 0, and < or ≤ give the same answer for a continuous X. The CDF is F(x) = ∫ f from the left end up to x, and f(x) = F′(x).

**Answer.** (i) f ≥ 0 on [0, 1], and ∫₀¹ (6x − 6x^{2}) dx = [3x^{2} − 2x^{3}]₀¹ = 3 − 2 = 1 ✓.
(ii) P(X < b) = ½: 3b^{2} − 2b^{3} = ½, i.e. 6b^{2} − 4b^{3} − 1 = 0. b = ½ gives 6/4 − 4/8 − 1 = 0 ✓, so **b = ½** (the median).

:::q <span class="tag">A1 SA 2</span>
Daily power consumption X (million kWh) has pdf f(x) = (1/9)x e^{−x/3}, x > 0. The plant's daily capacity is 12. Find the probability that supply is inadequate on a given day.
:::

**Answer.** Inadequate means X > 12. Integrate by parts: ∫ x e^{−x/3} dx = −3x e^{−x/3} − 9e^{−x/3}.

$$P(X > 12) = \frac{1}{9}[−3x e^{−x/3} − 9e^{−x/3}]_{12}^{∞} = \frac{1}{9}(36e^{−4} + 9e^{−4}) = 5e^{−4} = 0.0916$$

(The key's 0.0915 is the same value cut off at four places.)

:::check Check 5
f(x) = kx^{2} on 0 ≤ x ≤ 3. Find k and P(1 ≤ X ≤ 2).
:::

### 6 · Conditional probability with a PDF

File 01's P(A | B) = P(A∩B)/P(B) works unchanged; each probability is now an area.

:::q <span class="tag">A1 LA 1</span>
The probability that a person dies between ages t₁ and t₂ is ∫ f(t) dt from t₁ to t₂, with f(t) = 3 × 10^{−9} t^{2}(100 − t)^{2} for 0 ≤ t ≤ 100. Find (i) P(death between 60 and 70); (ii) the same, given that the person lived to 60.
:::

:::guess Guess first
Will (ii) be larger or smaller than (i)? One line on why.
:::

**Answer.** Expand: t^{2}(100 − t)^{2} = 10000t^{2} − 200t^{3} + t^{4}. Integrate and multiply by 3 × 10^{−9}:

$$F(t) = 10^{−5}t^{3} − 1.5 × 10^{−7}t^{4} + 6 × 10^{−10}t^{5}    (F(100) = 10 − 15 + 6 = 1 ✓)$$

F(70) = 3.43 − 3.6015 + 1.00842 = 0.83692. F(60) = 2.16 − 1.944 + 0.46656 = 0.68256.

(i) P(60 ≤ T ≤ 70) = 0.83692 − 0.68256 = **0.1544**.
(ii) P(T ≥ 60) = 1 − 0.68256 = 0.31744. P(60 ≤ T ≤ 70 | T ≥ 60) = 0.1544/0.31744 = **0.4863**. Larger, because the people who died before 60 are removed from the denominator.

:::check Check 6
For the cable pdf 6x(1 − x), find P(X > 0.75 | X > 0.5).
:::

---

## Exam form

| | Discrete X | Continuous X |
|---|---|---|
| Values | listable (counts) | an interval (measurements) |
| Function | PMF p(x) = P(X = x) | PDF f(x), a density |
| Valid if | p(x) ≥ 0, Σp(x) = 1 | f(x) ≥ 0, ∫f(x)dx = 1 |
| P(a ≤ X ≤ b) | Σ p(x) over a ≤ x ≤ b | ∫ₐᵇ f(x) dx |
| P(X = a) | p(a) | 0 |
| CDF F(x) = P(X ≤ x) | running sum (staircase) | ∫ f up to x (smooth); f = F′ |

**CDF properties.** 0 ≤ F(x) ≤ 1; non-decreasing; F(−∞) = 0, F(∞) = 1; P(a < X ≤ b) = F(b) − F(a).

**Procedure: find a constant.** Set Σp = 1 (or ∫f = 1), solve, reject any root that makes a probability negative.

## Traps

- Calling a **count** of calls or arrivals continuous: counts are discrete even when they come in time.
- Reading f(x) as a probability. A density can exceed 1; only areas are probabilities.
- For discrete X, "<" and "≤" differ: P(X < 2) = F(1), P(X ≤ 2) = F(2).
- Forgetting to reject the negative root when solving for k.
- In a conditional with a pdf, dividing by 1 instead of by the probability of the given event.

## Self-test

1. Define PMF, PDF and CDF in one line each.
2. Why is P(X = 2) = 0 for a continuous X but not for a discrete one?
3. X = number of heads in 2 tosses of a fair coin. Write the PMF and CDF.
4. f(x) = 2x on 0 ≤ x ≤ 1. Find F(x) and P(X > 0.5).
5. A box has 3 defective and 7 good items; 2 are drawn without replacement. Find the PMF of the number of defectives.
6. For A1 LA 2 (k = 1/10), find P(X ≥ 6) and P(2 ≤ X ≤ 4).
7. f(x) = k e^{−2x}, x ≥ 0. Find k and P(X > 1).

<!--ANSWERS-->
## Answers

**Check 1.** Number of defective bulbs in a box (a count).

**Check 2.** c(1 + 2 + 3 + 4) = 10c = 1 ⇒ **c = 1/10**.

**Check 3.** P(X = 1) = 1/36 (only (1, 1)). P(X = 6) = 1 − (5/6)^{2} = 11/36.

**Check 4.** F(2) − F(0) = 0.80 − 0.15 = **0.65**.

**Check 5.** k·27/3 = 9k = 1 ⇒ **k = 1/9**. P(1 ≤ X ≤ 2) = (8 − 1)/27 = **7/27**.

**Check 6.** P(X > 0.5) = ½. P(X > 0.75) = 1 − F(0.75) = 1 − (3(0.5625) − 2(0.421875)) = 1 − 0.84375 = 0.15625. Ratio = 0.15625/0.5 = **0.3125**.

**Self-test.**

1. PMF p(x) = P(X = x) (discrete); PDF f(x): density whose area gives probability (continuous); CDF F(x) = P(X ≤ x) (both).
2. A single point has zero width, so zero area under f. A discrete X puts a finite mass on each listed value.
3. p(0) = ¼, p(1) = ½, p(2) = ¼; F = ¼, ¾, 1 at x = 0, 1, 2.
4. F(x) = x^{2} for 0 ≤ x ≤ 1; P(X > 0.5) = 1 − 0.25 = **0.75**.
5. C(10, 2) = 45: p(0) = 21/45 = 7/15, p(1) = 21/45 = 7/15, p(2) = 3/45 = 1/15.
6. P(X ≥ 6) = 0.02 + 0.17 = **0.19**; P(2 ≤ X ≤ 4) = 0.2 + 0.2 + 0.3 = **0.7**.
7. k/2 = 1 ⇒ **k = 2**; P(X > 1) = e^{−2} = **0.1353**.
<!--/ANSWERS-->
