# 16 — State reduction and ASM charts

<div class="sub">Deck 12 (slides 10–26) · deck 13 (slides 3–8) · syllabus Unit 4 · needs 15 (state tables)</div>

## Map

[[map:1 Partitioning > 2 Implication table, compatibles > 3 ASM charts|here=1]]

15 built a state table by hand; it may have more states than needed. Fewer states can mean fewer flip-flops and simpler logic. An ASM chart is the same machine drawn as a flowchart with timing.

## The questions this file answers

- <span class="tag">Deck 12 slides 10, 16</span> Find the equivalent states of a 5-state machine and give the reduced table.
- <span class="tag">Deck 12 slide 17</span> Reduce an 8-state machine by partitioning.
- <span class="tag">Deck 13 slides 3–8</span> Name the three elements of an ASM chart; draw the chart of the 1101 detector.

---

## Build

### 1 · Partitioning

:::q <span class="tag">Deck 12 slides 10 and 16</span>
Find the equivalent states of the machine below and give the reduced state table.
:::

| Present | x = 0 | x = 1 |
|---|---|---|
| A | C/1 | B/0 |
| B | C/1 | E/0 |
| C | B/1 | E/0 |
| D | D/0 | B/1 |
| E | E/0 | A/1 |

:::guess Guess first
Which rows give the same outputs? Only those can possibly merge.
:::

:::note Terms
**Equivalent states:** for every input they give the same output and go to equivalent next states. No input sequence can tell them apart, so they merge.
:::

1. **P_{0}** = (ABCDE).
2. **P_{1}**, split by outputs: A, B, C give (1, 0); D, E give (0, 1) → (ABC)(DE).
3. **P_{2}**, split by the block each next state falls in. On x = 1: A → B (in ABC), but B, C → E (in DE): A separates → (A)(BC)(DE).
4. **P_{3}**: on x = 1, D → B (in BC) but E → A (in A): D and E separate → (A)(BC)(D)(E).
5. **P_{4} = P_{3}**: B, C go to C, B (same block) and E, E. Stop.

**Answer.** **B ≡ C.** Five states become four, so 2 flip-flops instead of 3. Replace C by B: A: B/1, B/0 · B: B/1, E/0 · D: D/0, B/1 · E: E/0, A/1.

:::check Check 1
<span class="tag">Deck 12 slide 17</span> Reduce by partitioning (next/z for x = 0; for x = 1): A E/0, D/0 · B A/1, F/0 · C C/0, A/1 · D B/0, A/0 · E D/1, C/0 · F C/0, D/1 · G H/1, G/1 · H C/1, B/1.
:::

### 2 · Implication table and compatibles

:::guess Predict
Partitioning works top-down. Could you instead test every pair of states once?
:::

[[fig:implication_chart|Implication table for step 1's machine.|w=45]]

1. One cell per pair. Cross out (×) every pair whose outputs differ.
2. In each remaining cell write the next-state pairs that would have to be equivalent.
3. Cross out any cell that depends on a crossed pair. Repeat until nothing changes.
4. Uncrossed cells are the equivalent pairs.

Here A–B needs B–E (crossed), so it goes; D–E needs A–B, so it goes; **B–C** needs only C–B and E–E: it survives.

**Incompletely specified machines** (deck 12 slides 19–26): with don't-care entries, equivalence becomes **compatibility**: specified outputs never conflict and next states are compatible. It is **not transitive**, so states are grouped into maximal compatibles with a merger diagram; the chosen set must **cover** every state and be **closed** (each group's next states fall inside one chosen group).

**Answer.** Yes: the implication table tests every pair, and gives the same B ≡ C.

:::check Check 2
Why can't you merge A, B, C just because A–B and B–C are compatible?
:::

### 3 · ASM charts

:::q <span class="tag">Deck 13 slides 3–8</span>
Name the three elements of an ASM chart and draw the ASM chart of the Mealy 1101 detector of 15.
:::

:::guess Guess first
In a flowchart of the machine, which shape should take exactly one clock period?
:::

[[fig:asm_1101|ASM chart of the Mealy 1101 detector.|w=55]]

An **ASM chart** is a flowchart with timing: each state box lasts one clock period.

- **State box** (rectangle): one state; Moore outputs inside. One entry, one exit.
- **Decision box** (diamond): tests an input; exits for 0 and 1.
- **Conditional output box** (oval): an output produced only on that path; always after a decision box. A Mealy output.

An **ASM block** is one state box with the decision and conditional boxes reached before the next state box: everything in it happens in one clock period. Circle → state box; arrows → decision on the input; Mealy output → oval on that exit. Back to a circuit: each path between state boxes is one state-table row. The deck also charts a MOD-6 counter, D and JK flip-flops, a serial adder (carry 0 / carry 1) and 2-bit up and up/down counters.

**Answer.** State box, decision box, conditional output box. Four state boxes A–D, a decision on x after each, and one oval (z = 1) on the x = 1 exit of D.

:::check Check 3
(a) In the Moore 1101 detector, where is z = 1 written? (b) How many state boxes for a MOD-6 counter? (c) Why can a conditional output box never follow a state box directly?
:::

---

## Exam form

**Partitioning.** P_{0} → P_{1} by outputs → refine by next-state blocks until stable; the reduced table.

**Implication table.** Four steps; equivalent pairs; compatibility, merger diagram, cover and closure.

**ASM.** Three elements with shapes; ASM block; chart for a given machine.

## Traps

- Splitting on next states before splitting on outputs.
- Comparing next states by name instead of by block.
- Treating compatibility as transitive.
- Putting a Mealy output in a state box.

## Self-test

1. Define equivalent states.
2. Reduce: A: B/0, C/1 · B: A/0, D/1 · C: C/1, A/0 · D: D/1, B/0 (next/z for x = 0; x = 1).
3. How many flip-flops before and after reduction in Q2?
4. What is an ASM block?
5. Draw the ASM chart of a 2-bit up counter.

<!--ANSWERS-->

## Answers

**Check 1.** P_{1} by outputs: (AD)(BE)(CF)(GH). P_{2}: on x = 1, G → G but H → B: G, H separate; A, D go to E, B and D, A (same blocks); B, E go to A, D and F, C; C, F go to C, C and A, D. → **(AD)(BE)(CF)(G)(H)**, P_{3} = P_{2}. 8 states become **5**.

**Check 2.** Compatibility is not transitive: A–C may conflict even though both are compatible with B.

**Check 3.** (a) **Inside E's state box**. (b) **Six**. (c) A conditional output depends on an input, so an input must be tested first: a decision box.

**Self-test.**

1. Same output for every input, and equivalent next states, for every input sequence.
2. P_{1}: (AB)(CD). A → B, C and B → A, D: same blocks; C → C, A and D → D, B: same blocks. **A ≡ B, C ≡ D**: two states.
3. **2 → 1**.
4. One state box with the decision and conditional output boxes reached from it before the next state box: one clock period.
5. Four state boxes 00 → 01 → 10 → 11 → 00, no decision boxes (no input).

<!--/ANSWERS-->
