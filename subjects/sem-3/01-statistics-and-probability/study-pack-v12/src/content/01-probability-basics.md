# 01 — Probability: the basic terms

<div class="sub">Gupta & Kapoor ch. 4 (§4.3, 4.7, 4.8) · blueprint row 1 "basic terminology and concepts of probability theory" · 4 real questions (Assignment 1) · needs nothing earlier</div>

## Map

[[map:1 Outcomes and events > 2 Classical probability > 3 Addition and complement > 4 Conditional probability > 5 Independence > 6 Bayes' theorem|here=1]]

## The questions this file answers

- <span class="tag">A1 MCQ 7</span> A box contains 4 red and 6 blue balls. One ball is selected randomly. The probability of selecting a red ball is: 0.2 / 0.4 / 0.6 / 0.8.
- <span class="tag">A1 MCQ 9</span> A card is drawn from a standard deck of 52 cards. The probability of drawing an Ace is: 1/13 / 1/4 / 4/13 / 1/52.
- <span class="tag">A1 MCQ 6</span> The conditional probability of A given B is defined as: P(B)/P(A) / P(A∩B)/P(B) / P(A) + P(B) / P(A∩B)/P(A).
- <span class="tag">A1 MCQ 8</span> If P(A | B) = 1, then: A is impossible whenever B occurs / A always occurs whenever B occurs / A and B are mutually exclusive / none of these.

Row 1 of the ETE blueprint is 10 marks: two 2-mark items and one 6-mark item. Every later file uses the words defined here.

---

## Build

### 1 · Outcomes, sample space, events

:::q Predict
You throw one die. Write down every result that can happen. Then write down the results that count as "an even number".
:::

:::guess Guess first
Write both lists on paper before reading on.
:::

**Terms.**

- **Random experiment**: an action whose result is not known in advance (throwing a die, drawing a card).
- **Sample space S**: the list of every possible result (outcome). For one die, S = {1, 2, 3, 4, 5, 6}.
- **Event**: a group of outcomes, written as a set. "Even" = A = {2, 4, 6}.

[[fig:venn|Events are regions inside S. A∩B ("A and B") is the overlap; A∪B ("A or B") is everything in either circle.|w=55]]

Two events are **mutually exclusive** if they cannot happen together: their overlap is empty, A∩B = ∅. "Even" and "odd" on one die are mutually exclusive. The **complement** Aᶜ is "A does not happen": everything in S outside A.

**Answer.** S = {1, 2, 3, 4, 5, 6}; even = {2, 4, 6}.

:::check Check 1
(a) Two coins are tossed. Write S. (b) Are "at least one head" and "no head" mutually exclusive? Are they complements?
:::

### 2 · Classical probability: count and divide

The list of outcomes is in place; now give each event a number.

:::q <span class="tag">A1 MCQ 7 · 2 marks</span>
A box contains 4 red and 6 blue balls. One ball is selected randomly. The probability of selecting a red ball is: (a) 0.2 (b) 0.4 (c) 0.6 (d) 0.8
:::

:::guess Guess first
Pick an option and write one line saying why.
:::

**Classical definition** (G&K §4.3): if the experiment has n **equally likely** outcomes and m of them are favourable to A, then

$$P(A) = \frac{m}{n} = \frac{favourable outcomes}{total outcomes}$$

"Selected randomly" is the phrase that makes every ball equally likely. Every probability lies between 0 (impossible) and 1 (certain), and P(S) = 1.

**Answer.** n = 4 + 6 = 10 balls, m = 4 red. P(red) = 4/10 = **0.4**, option (b).

:::q <span class="tag">A1 MCQ 9 · 2 marks</span>
A card is drawn from a standard deck of 52 cards. The probability of drawing an Ace is: (a) 1/13 (b) 1/4 (c) 4/13 (d) 1/52
:::

**Answer.** A deck has 4 aces among 52 cards: P = 4/52 = **1/13**, option (a).

:::check Check 2
A bag has 3 white, 5 black and 2 green balls. One ball is drawn at random. Find P(not black).
:::

### 3 · Addition rule and complement

Single events are done; exam questions combine them with "or" and "not".

:::q Predict
One card is drawn from 52. Find P(Ace or Heart).
:::

:::guess Guess first
Is it 4/52 + 13/52? Write your answer and check whether any card was counted twice.
:::

**Terms.** P(A∪B) = probability that A or B (or both) happens.

**Addition rule** (G&K §4.6):

$$P(A ∪ B) = P(A) + P(B) − P(A ∩ B)$$

The overlap is subtracted because it was counted once inside P(A) and again inside P(B). For **mutually exclusive** events the overlap is empty, so P(A∪B) = P(A) + P(B).

**Complement rule**: P(Aᶜ) = 1 − P(A). Use it whenever "at least one" appears: P(at least one) = 1 − P(none).

**Answer.** 4 aces + 13 hearts − 1 (the ace of hearts, counted twice) = 16 cards. P = 4/52 + 13/52 − 1/52 = **16/52 = 4/13**.

:::check Check 3
P(A) = 0.5, P(B) = 0.3, P(A∩B) = 0.1. Find (a) P(A∪B) (b) P(neither A nor B).
:::

### 4 · Conditional probability

The next step is what happens to a probability once you **know** something has already happened.

:::q <span class="tag">A1 MCQ 6 · 2 marks</span>
The conditional probability of A given B is defined as: (a) P(B)/P(A) (b) P(A∩B)/P(B) (c) P(A) + P(B) (d) P(A∩B)/P(A)
:::

:::guess Guess first
A die shows an even number. What is the chance it is a 6? Answer that, then pick the formula that gives the same number.
:::

**Term.** **P(A | B)**, read "probability of A given B": the probability of A when we already know B happened.

Knowing B shrinks the sample space to B. Inside that smaller space, A can only happen through the overlap A∩B:

$$P(A | B) = \frac{P(A ∩ B)}{P(B)},  P(B) > 0$$

**Concrete.** B = even = {2, 4, 6}, A = six = {6}. A∩B = {6}. P(A|B) = (1/6)/(3/6) = **1/3**: one of the three even faces.

**Answer.** Option **(b)**. Option (d) is P(B | A), the conditioning the other way round.

**Multiplication rule** (rearranged): P(A∩B) = P(B) · P(A | B). A probability tree multiplies along each branch:

[[fig:cond_tree|Each path's probability = product of the branch probabilities on it.|w=72]]

:::q <span class="tag">A1 MCQ 8 · 2 marks</span>
If P(A | B) = 1, then: (a) A is impossible whenever B occurs (b) A always occurs whenever B occurs (c) A and B are mutually exclusive (d) none of these.
:::

**Answer.** P(A|B) = 1 means P(A∩B) = P(B): every outcome in B is also in A. So A always happens when B does, option **(b)**. Mutually exclusive would give P(A|B) = 0, the opposite.

:::check Check 4
Two cards are drawn one after the other without replacement. Find P(both are aces).
:::

### 5 · Independence

Conditional probability gives the exact meaning of "one event does not affect the other".

:::q Predict
A coin is tossed and a die is thrown. Is P(head and six) = (1/2)(1/6)? Why can you multiply here but not for two aces drawn without replacement?
:::

:::guess Guess first
Write one sentence on what makes the two situations different.
:::

**Term.** A and B are **independent** if knowing B does not change the probability of A: P(A | B) = P(A). Substituting into the multiplication rule:

$$A, B independent ⇔ P(A ∩ B) = P(A) · P(B)$$

**Answer.** The coin cannot influence the die, so P(head and six) = 1/2 × 1/6 = **1/12**. Drawing a first ace without replacement removes an ace, so P(second ace) changes from 4/52 to 3/51: the draws are **dependent**.

:::trap Independent is not mutually exclusive
Mutually exclusive events (with non-zero probabilities) are always **dependent**: if one happens, the other's probability drops to 0.
:::

:::check Check 5
P(A) = 0.4 and P(B) = 0.5. Find P(A∩B) if (a) A and B are independent (b) A and B are mutually exclusive.
:::

### 6 · Bayes' theorem

The last tool turns a conditional probability around: from P(B | A) to P(A | B). File 10 (Bayesian estimation) is built on it.

:::q Predict
Machine M₁ makes 60% of a factory's bolts and machine M₂ makes 40%. 2% of M₁'s bolts and 5% of M₂'s bolts are defective. A bolt picked at random is defective. Which machine is more likely to have made it?
:::

:::guess Guess first
M₂ makes fewer bolts but a higher share of them are bad. Write which machine you would bet on.
:::

**Total probability**: a defective bolt comes from M₁ or from M₂, so add the two tree paths:

$$P(D) = P(M_{1})P(D | M_{1}) + P(M_{2})P(D | M_{2}) = 0.6 × 0.02 + 0.4 × 0.05 = 0.012 + 0.020 = 0.032$$

**Bayes' theorem** (G&K §4.8): the share of that total coming through each path is

$$P(M_{i} | D) = \frac{P(M_{i}) P(D | M_{i})}{Σ_{j} P(M_{j}) P(D | M_{j})}$$

**Answer.** P(M₁ | D) = 0.012/0.032 = **0.375**. P(M₂ | D) = 0.020/0.032 = **0.625**. M₂ is the more likely source: its higher defect rate outweighs its smaller output.

**Terms used again in file 10:** P(Mᵢ) is the **prior** (before seeing the bolt); P(Mᵢ | D) is the **posterior** (after seeing it is defective).

:::check Check 6
In the same factory, a bolt is found **good**. Find P(M₁ | good).
:::

---

## Exam form

**Definitions.** Random experiment · sample space S (all outcomes) · event (a subset of S) · mutually exclusive (A∩B = ∅) · complement Aᶜ · equally likely outcomes.

**Formulas.**

1. Classical: P(A) = m/n (equally likely outcomes), 0 ≤ P(A) ≤ 1, P(S) = 1.
2. Addition: P(A∪B) = P(A) + P(B) − P(A∩B); mutually exclusive: P(A∪B) = P(A) + P(B).
3. Complement: P(Aᶜ) = 1 − P(A); P(at least one) = 1 − P(none).
4. Conditional: P(A | B) = P(A∩B)/P(B).
5. Multiplication: P(A∩B) = P(B)P(A | B); independent: P(A∩B) = P(A)P(B).
6. Bayes: P(Aᵢ | B) = P(Aᵢ)P(B | Aᵢ) / Σⱼ P(Aⱼ)P(B | Aⱼ).

**Procedure for a Bayes question.** (1) Name the causes A₁, A₂, … and the observed event B. (2) Write the priors P(Aᵢ) and the likelihoods P(B | Aᵢ). (3) Total probability P(B) = Σ P(Aᵢ)P(B | Aᵢ). (4) Divide each path by P(B).

## Traps

- Adding P(A) + P(B) for events that overlap: subtract P(A∩B).
- Swapping P(A | B) and P(B | A): the given event goes in the denominator.
- Treating "mutually exclusive" as "independent".
- Multiplying probabilities for draws **without** replacement as if they were independent.

## Self-test

1. Define sample space and event, with a one-die example.
2. Two dice are thrown. Find P(sum = 7).
3. P(A) = 0.6, P(B) = 0.5, P(A∪B) = 0.8. Find P(A∩B) and P(A | B).
4. Are the A and B of question 3 independent? Show the test.
5. A family has two children. Given that at least one is a boy, find P(both are boys).
6. Urn I has 2 white and 3 black balls; urn II has 4 white and 1 black. An urn is chosen at random and a ball drawn from it is white. Find P(it came from urn I).

<!--ANSWERS-->
## Answers

**Check 1.** (a) S = {HH, HT, TH, TT}. (b) Yes, they cannot both happen; and yes, together they cover S, so "no head" is the complement of "at least one head".

**Check 2.** P(not black) = 1 − 5/10 = **0.5**.

**Check 3.** (a) 0.5 + 0.3 − 0.1 = **0.7**. (b) 1 − 0.7 = **0.3**.

**Check 4.** (4/52)(3/51) = 12/2652 = **1/221**.

**Check 5.** (a) 0.4 × 0.5 = **0.2**. (b) **0**.

**Check 6.** P(good) = 0.6 × 0.98 + 0.4 × 0.95 = 0.588 + 0.380 = 0.968. P(M₁ | good) = 0.588/0.968 = **0.6074**.

**Self-test.**

1. S = set of all outcomes, {1, …, 6}; event = subset, e.g. even = {2, 4, 6}.
2. Six pairs (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) of 36: **1/6**.
3. P(A∩B) = 0.6 + 0.5 − 0.8 = **0.3**; P(A | B) = 0.3/0.5 = **0.6**.
4. P(A)P(B) = 0.30 = P(A∩B), so **yes, independent** (also P(A | B) = 0.6 = P(A)).
5. Outcomes with at least one boy: BB, BG, GB. P(BB | at least one boy) = **1/3**.
6. P(W) = ½(2/5) + ½(4/5) = 0.2 + 0.4 = 0.6. P(I | W) = 0.2/0.6 = **1/3**.
<!--/ANSWERS-->
