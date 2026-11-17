# 16 — State reduction and ASM charts

<div class="sub">Deck 12 (slides 2–26) · deck 13 (slides 2–19) · syllabus Unit 4 (state reduction; algorithmic state machines) · real questions: the decks' worked examples and reduction problems; none on the MTE or the practice sets · needs 15 steps 5–9 (state tables, Mealy/Moore, assignment and equations)</div>

## Map

[[map:1 Equivalent states > 2 Reduction by inspection > 3 Partitioning a Moore table > 4 Partitioning a Mealy table > 5 The implication table > 6 Implications that loop > 7 Don't-cares: compatible states > 8 Maximal compatibles, closed cover > 9 ASM chart elements > 10 ASM chart of the 1010 detector > 11 Moore outputs: a counter > 12 Serial adder|here=1]]

File 15 built state tables from words. Nothing in that process guarantees the fewest states: two states may behave identically and only cost flip-flops and gates. Steps 1–8 find such states and merge them; this is step 3 of the design procedure ("state reduction"), done before state assignment. Steps 9–12 redraw state machines as **ASM charts**, flowcharts in which each state box lasts one clock period, and read the next-state and output equations straight off them. File 17 uses both for timing generators and asynchronous circuits.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| x, w, X, E, A, B | inputs (deck letters kept); one bit per clock period | 0 or 1 |
| z, Z | output | 0 or 1 |
| A … H, S1 … S9 | state names in a state table | 5–9 states |
| C/1 in a table | Mealy entry: next state C, output 1 | — |
| – | unspecified entry (don't-care next state or output) | — |
| P1, P2, … | partitions: the states split into blocks, refined one step at a time | — |
| (BC) | a block / class: states B and C taken as one | — |
| A', B', … | states of the reduced table | 2–6 states |
| y, y1, y0 | state bits in an ASM chart (code written beside the state box) | 0 or 1 |
| m0, m1, … | minterms of the state bits (m2 = y1y0' = state code 10) | — |

## Running example

**Deck 12's five-state Mealy machine** (slides 4, 10 and 16), reduced three ways: by its response tables (step 1), by partitioning (step 4) and by an implication table (step 5). Every method gives **B ≡ C**, 5 states → 4.

| State | x = 0 | x = 1 |
|---|---|---|
| A | C/1 | B/0 |
| B | C/1 | E/0 |
| C | B/1 | E/0 |
| D | D/0 | B/1 |
| E | E/0 | A/1 |

## The questions this file answers

- <span class="tag">Deck 12 slides 3–4</span> Define equivalent states; find the equivalent states of the five-state machine from its responses.
- <span class="tag">Deck 12 slides 7–15</span> Find equivalent states by inspection and by partitioning (Moore and Mealy tables, one and two inputs) and give the minimized state table.
- <span class="tag">Deck 12 slides 16–18</span> Find equivalent states with an implication table.
- <span class="tag">Deck 12 slides 19–26</span> Incompletely specified circuits: compatible states, maximal compatibles, merger diagrams, a complete, consistent and minimal cover.
- <span class="tag">Deck 13 slides 3–19</span> The three ASM elements; ASM charts of the 1010 detector, a MOD-6 counter, a serial adder and a 2-bit counter; equations from a chart.

---

## Build

### 1 · Equivalent states

Two buttons on a remote that do exactly the same thing in every situation are, for every purpose, one button. Two states are the same in that sense when no experiment on the inputs and outputs can tell them apart.

:::q <span class="tag">Deck 12 slides 3–4 (EX 12.4)</span>
For the machine of the running example, the output sequences for every input sequence of length 2 and 3 are listed below. Which states are equivalent?
:::

:::guess Guess first
In the length-2 table, D and E give identical outputs. Are they equivalent?
:::

:::note Terms
**Equivalent states** (completely specified circuit): states that produce the same output sequence for **every** input sequence (slide 3). Test that works one clock at a time: Si and Sj are equivalent if and only if, for every input, (1) their outputs are the same and (2) their next states are equivalent. **Completely specified:** every next state and output in the table is given.
:::

| Start in | 00 | 01 | 10 | 11 | 110 | 111 |
|---|---|---|---|---|---|---|
| A | 11 | 10 | 01 | 00 | 000 | 001 |
| B | 11 | 10 | 00 | 01 | 011 | 010 |
| C | 11 | 10 | 00 | 01 | 011 | 010 |
| D | 00 | 01 | 11 | 10 | 100 | 101 |
| E | 00 | 01 | 11 | 10 | 101 | 100 |

*Each entry is the output sequence produced from that start state; the input sequence heads the column, first bit on the left.* B and C agree everywhere (here, and in the full length-3 table of slide 4). D and E agree on every length-2 input but differ on 110 and 111.

Removing equivalent states matters because (slide 2): the number of flip-flops grows with the number of states; more states make the design more complex; and test routines assume no redundant states.

**Answer to the Guess:** no. D and E are told apart by 110 (100 vs 101): agreeing on short sequences is not enough. **B ≡ C** only, so the machine needs 4 states.

:::check Check 1
(a) Which inputs of length 2 tell A from B? Trace one of them through the state table. (b) Why does a table of all inputs of length 3 still not prove that B ≡ C?
:::

### 2 · Reduction by inspection

Trying every input sequence never ends. The one-clock test of step 1 gives a quick first method: compare rows.

:::q <span class="tag">Deck 12 slide 7 (EX 12.7)</span>
Find equivalent states by inspection: A: B/0, C/1 · B: C/0, A/1 · C: D/1, B/0 · D: C/0, A/1 (next/output for x = 0; for x = 1).
:::

:::guess Guess first
Which two rows are identical?
:::

:::note Terms
**Identical rows:** same next state and same output for every input. They pass the one-clock test with nothing left to check, so they are equivalent.
:::

| State | x = 0 | x = 1 | | Reduced | x = 0 | x = 1 |
|---|---|---|---|---|---|---|
| A | B/0 | C/1 | | A | B/0 | C/1 |
| B | C/0 | A/1 | | B | C/0 | A/1 |
| C | D/1 | B/0 | | C | **B**/1 | B/0 |
| D | C/0 | A/1 | | | | |

Merge: delete row D and write B wherever D appeared (C's x = 0 entry).

Inspection also catches two disguised cases (slide 7, bottom): rows that differ only because each **goes to itself** (B: B/0, A/1 and D: D/0, A/1), and rows that differ only because they **go to each other** (B: D/0, A/1 and D: B/0, A/1). In both, assuming B ≡ D makes the rows identical.

**Answer to the Guess:** rows **B and D** (both C/0, A/1): B ≡ D, and the machine needs 3 states.

:::check Check 2
Reduce by inspection: A: B/0, C/1 · B: B/0, A/1 · C: D/1, B/0 · D: D/0, A/1.
:::

### 3 · Partitioning a Moore table

Inspection misses equivalences that need a chain of reasoning. Partitioning is systematic: it splits states apart until nothing more splits.

:::q <span class="tag">Deck 12 slides 8–9 (EX 12.8–12.9)</span>
Minimize the Moore machine: A: B, C, z = 1 · B: D, F, 1 · C: F, E, 0 · D: B, G, 1 · E: F, C, 0 · F: E, D, 0 · G: F, G, 0 (next for w = 0, w = 1; output).
:::

:::guess Guess first
Which states can certainly **not** be equivalent to A, just from the outputs?
:::

:::note Terms
**Partition:** the states divided into blocks; states in one block are "not yet told apart". **Refinement:** a block splits when, for some input, its states' next states fall in **different blocks** of the current partition.
:::

1. P1 = (ABCDEFG): all states together.
2. P2, split by output: z = 1 for A, B, D; z = 0 for C, E, F, G → **(ABD)(CEFG)**.
3. P3: on w = 1, C → E, E → C, G → G (all in CEFG) but F → D (in ABD): F splits off → **(ABD)(CEG)(F)**.
4. P4: on w = 1, A → C and D → G (in CEG) but B → F (in F): B splits off → **(AD)(B)(CEG)(F)**.
5. P5: A, D go to B, B (w = 0) and C, G (w = 1), same blocks; C, E, G go to F, F, F and E, C, G, same blocks. **P5 = P4: stop.**

| State | w = 0 | w = 1 | z |
|---|---|---|---|
| A = (AD) | B | C | 1 |
| B | A | F | 1 |
| C = (CEG) | F | C | 0 |
| F | C | A | 0 |

**Answer to the Guess:** **C, E, F and G** (output 0, A's is 1). In a Moore machine the output belongs to the state, so P2 splits by the single output column.

:::check Check 3
(a) Flip-flops before and after this reduction? (b) Why does C stay with E and G although C → F on w = 0 and F is alone?
:::

### 4 · Partitioning a Mealy table

In a Mealy table each state has one output per input, so P1 splits by the **whole output row**.

:::q <span class="tag">Deck 12 slide 10 (EX 12.10)</span>
Find the equivalent states of the running example by partitioning.
:::

:::guess Guess first
List each state's output row (x = 0, x = 1). How many different rows are there?
:::

:::note Terms
**Output row:** the outputs of one state for each input value, read as a pattern (A: 1, 0). States with different output rows are told apart in one clock.
:::

| Partition | Blocks | What splits, and why |
|---|---|---|
| P0 | (ABCDE) | start |
| P1 | (ABC)(DE) | output rows: A, B, C give 1, 0; D, E give 0, 1 |
| P2 | (A)(BC)(DE) | x = 1: A → B (in ABC) but B, C → E (in DE) |
| P3 | (A)(BC)(D)(E) | x = 1: D → B (in BC) but E → A (in A) |
| P4 = P3 | (A)(BC)(D)(E) | B, C → C, B (same block) and E, E: nothing splits |

Reduced table (C replaced by B): A: B/1, B/0 · B: B/1, E/0 · D: D/0, B/1 · E: E/0, A/1.

**Answer to the Guess:** **two** output rows, (1, 0) and (0, 1): P1 = (ABC)(DE). Partitioning ends with **B ≡ C**, as the response table of step 1 suggested, and now proved.

:::check Check 4
<span class="tag">Deck 12 slide 11</span> Reduce by partitioning (next/z for x = 0; for x = 1): A E/0, D/0 · B A/1, F/0 · C C/0, A/1 · D B/0, A/0 · E D/1, C/0 · F C/0, D/1 · G H/1, G/1 · H C/1, B/1.
:::

### 5 · The implication table

Partitioning works on all states at once. The implication table tests **pairs**, which is what the incompletely specified tables of steps 7–8 need.

:::q <span class="tag">Deck 12 slide 16 (EX 12.16)</span>
Find the equivalent states of the running example with an implication table.
:::

:::guess Guess first
The cell for (A, B) lists the pair BE. What does that mean, and is (A, B) equivalent?
:::

:::note Terms
**Implication table:** a staircase grid with one cell per pair of states. **Implied pair:** a pair of next states that must be equivalent for the cell's pair to be equivalent (A and B go to C, C on x = 0 and to B, E on x = 1, so (A, B) implies BE).
:::

[[fig:implication_chart|What this graph plots: one cell per pair of states (row = later state, column = earlier); × = outputs differ; a listed pair = what must also be equivalent; a slash = struck out because an implied pair was struck out.|w=48]]

1. Cross out (×) every pair whose outputs differ: all six pairs between {A, B, C} and {D, E}.
2. In each remaining cell write the implied pairs: (A, B): BE · (A, C): BC, BE · (B, C): only CB and EE, which hold already (✓) · (D, E): AB.
3. Cross out every cell that implies a crossed-out pair: BE is ×, so (A, B) and (A, C) go; then AB is crossed, so (D, E) goes.
4. Repeat step 3 until nothing changes. The uncrossed cells are the equivalent pairs: **(B, C)**.

**Answer to the Guess:** (A, B) is equivalent only if B and E are. (B, E) is crossed out (different outputs), so **(A, B) is not**. Result: (A)(BC)(D)(E), the same as step 4.

:::check Check 5
(A, C) lists BC and BE, and BC survives. Why is (A, C) still crossed out?
:::

### 6 · Implications that loop

In step 5 every chain of implications ended at a crossed cell or at ✓. In bigger tables the chains can form a loop.

:::q <span class="tag">Deck 12 slide 17 (EX 12.17)</span>
Use an implication table to find the equivalent states of the 8-state machine of step 4's Check (A E/0, D/0 · … · H C/1, B/1).
:::

:::guess Guess first
(A, D) needs BE; (B, E) needs AD and CF; (C, F) needs AD. None of them is crossed. Are they equivalent?
:::

:::note Terms
**Loop of implications:** cells that only imply each other. Nothing in the loop can ever be crossed out, so all its pairs are equivalent.
:::

[[fig:u4_impl8|What this graph plots: the implication table of the 8-state machine. Every pair whose outputs differ is ×. (G, H) is struck out because it needs BG and CH, both ×. The three shaded cells imply only each other.|w=62]]

- Outputs split the states into (AD)(BE)(CF)(GH); every pair across these blocks is ×.
- (G, H) implies BG and CH, both crossed: (G, H) is crossed.
- (A, D) → BE → AD, CF → AD: a closed loop with no crossed cell. All three survive.

**Answer to the Guess:** yes: **A ≡ D, B ≡ E, C ≡ F**, and G, H stay separate: (AD)(BE)(CF)(G)(H), 8 states → 5, the same result as partitioning.

:::check Check 6
<span class="tag">Deck 12 slide 18</span> For the two-input machine of slide 15, the uncrossed pairs are (A, F), (B, C), (B, H) and (C, H). Write the reduced set of states and say why B, C and H can become one state.
:::

### 7 · Don't-cares: compatible states

All tables so far were completely specified. Real specifications often leave entries open (–), as don't-cares did in K-maps (02 step 7).

:::q <span class="tag">Deck 12 slides 19–20, 24 (EX 12.24)</span>
Find the compatible pairs of the incompletely specified machine: A: A/–, –/– · B: C/1, B/0 · C: D/0, –/1 · D: –/–, B/– · E: A/0, C/1.
:::

:::guess Guess first
A is compatible with B, and A is compatible with C. Must B be compatible with C?
:::

:::note Terms
**Incompletely specified circuit:** some next states or outputs are unspecified (–). **Compatible states:** for every input, the outputs agree **where both are specified**, and the next states are compatible **where both are specified** (slide 19). **Not transitive:** compatibility is reflexive and symmetric but not transitive, so compatible groups may overlap (slide 20).
:::

Implication table, same steps as step 5, ignoring every – :

| Pair | Outputs | Implied | Result |
|---|---|---|---|
| (B, C), (B, E) | differ (x = 0: 1 vs 0) | — | × |
| (D, E) | agree | BC | crossed (BC is ×) |
| (A, B) | agree | AC | compatible |
| (A, C), (C, E) | agree | AD | compatible |
| (A, D), (A, E), (B, D), (C, D) | agree | none | compatible ✓ |

**Answer to the Guess:** no. **B and C are incompatible** (their x = 0 outputs are 1 and 0) although each is compatible with A. A can merge with B or with C, but not with both in one state.

:::check Check 7
(a) Why is (A, D) compatible with no conditions at all? (b) Is (ABD) a compatible class (every pair inside compatible)?
:::

### 8 · Maximal compatibles and a closed cover

Step 7 gave the compatible pairs. The reduced machine needs groups of states, chosen so that the reduced table still works.

:::q <span class="tag">Deck 12 slides 21–24 (EX 12.24)</span>
Find the maximal compatibles of step 7's machine with a merger diagram, and choose a set of compatibility classes that is complete, consistent and minimal. Give the reduced table.
:::

:::guess Guess first
The three largest compatible groups are (ABD), (ACD) and (ACE). Can two of them do the job?
:::

:::note Terms
**Maximal compatible:** a compatible group that no further state can join (every pair inside compatible). **Merger diagram:** states as points, a line for each compatible pair; maximal compatibles are the largest fully connected groups (slide 21). **Closed (consistent) cover:** a set of classes that contains every state (**complete**), and in which, for each class and each input, the class's next states all fall inside **one** chosen class (**consistent**); with the fewest classes (**minimal**) (slide 22).
:::

[[fig:u4_merger5|What this graph plots: merger diagram of step 7's machine: one point per state, a solid line per compatible pair, dashed red lines for incompatible pairs. The shaded triangles are the maximal compatibles.|w=52]]

| Class | Next states, x = 0 | Next states, x = 1 |
|---|---|---|
| (ABD) | AC | B |
| (ACD) | AD | B |
| (ACE) | AD | C |

Choose (ABD) and (ACE):

1. Complete: A, B, D, C, E all appear.
2. Consistent: (ABD) on x = 0 needs AC → inside (ACE); on x = 1, B → inside (ABD). (ACE) on x = 0 needs AD → inside (ABD); on x = 1, C → inside (ACE).
3. Minimal: B and C are incompatible, so at least 2 states are needed; 2 are used.

| State | x = 0 | x = 1 |
|---|---|---|
| A' = (ABD) | B'/1 | A'/0 |
| B' = (ACE) | A'/0 | B'/1 |

*Outputs: the specified ones in the class (A' on x = 0: B gives 1, A and D give –, so 1).*

**Answer to the Guess:** yes: **(ABD)(ACE)** covers all five states and is closed: **5 states → 2**, one flip-flop. Not every pair of classes works: (ABD) with (CE) also covers all states, but (ABD) on x = 0 needs A and C together, and no chosen class holds both.

:::check Check 8
<span class="tag">Deck 12 slide 26</span> A machine has maximal compatibles (ABC), (ACD), (ADE), with implied next states (ABC): DE on x = 0, AB on x = 1; for (DE): C on x = 0, BC on x = 1. Show that (ABC)(DE) is a closed cover.
:::

### 9 · ASM chart elements

State tables and diagrams do not show **when** within a clock period each output is valid. ASM charts are flowcharts built to show that (deck 13 slide 2).

:::q <span class="tag">Deck 13 slides 3–6</span>
Name the three basic elements of an ASM chart and state the timing rule of each.
:::

:::guess Guess first
In a flowchart of a clocked machine, which box should take exactly one clock period?
:::

:::note Terms
**ASM chart (algorithmic state machine chart):** a flowchart of a state machine in which each **state box** stands for one clock period. **ASM block:** one state box together with the decision and conditional output boxes reached from it before the next state box; all of it happens in that state's clock period.
:::

[[fig:u4_asm_boxes|The three ASM elements (deck 13 slides 4–6): state box (name, code, Moore outputs), decision box (tests an input, one exit per value), conditional output box (a Mealy output on one path).|w=86]]

| Element | Shape | Rules (deck 13) |
|---|---|---|
| State box | rectangle; name at the corner, state code beside it | one state; takes one clock period; one entry, one exit; outputs listed inside (Moore outputs) are asserted during that period |
| Decision box | diamond | tests one or more inputs; two or more exits; always follows a state box and is decided in the same clock period, so inputs must be valid at the start of the period |
| Conditional output box | rounded box | must follow a decision box; its outputs are asserted in the same period as the state box it hangs from, only on that path (Mealy outputs) |

**Answer to the Guess:** the **state box**: one state box = one clock period. Decision and conditional boxes take no extra time; they belong to the period of the state box above them.

:::check Check 9
(a) Why can a conditional output box never follow a state box directly? (b) In a Moore machine, which of the three elements does the chart never use?
:::

### 10 · ASM chart of the 1010 detector

Step 9 gave the parts. Converting a state diagram is mechanical: circle → state box, arrows out of it → decision box on the input, Mealy output → conditional box on that exit.

:::q <span class="tag">Deck 13 slides 7–8 (EX 13.7–13.8)</span>
Draw the ASM chart of the overlapping 1010 sequence detector (15 step 4; S0 = 00, S1 = 01, S2 = 10, S3 = 11) and derive the next-state and output equations from it.
:::

:::guess Guess first
Every path that enters S1 or S3 (codes ending in 1) has X = 1 on it. What is D0?
:::

:::note Terms
**Reading equations off a chart:** each path from a state box into a state box is one term: (minterm of the source state) · (input condition on the path). D_i = the OR of the terms of every path entering a state whose code has bit i = 1; an output = the OR of the terms of the paths through its conditional box.
:::

[[fig:u4_asm_1010|What this graph plots: the ASM chart of the overlapping 1010 detector; each state box is one clock period, codes y1y0 beside the boxes. The only output, Z = 1, is a conditional box on S3's X = 0 exit.|w=60]]

| Path | Term | Enters | Adds to |
|---|---|---|---|
| S0, X = 1 | Xm0 | S1 (01) | D0 |
| S1, X = 1 | Xm1 | S1 (01) | D0 |
| S1, X = 0 | X'm1 | S2 (10) | D1 |
| S2, X = 1 | Xm2 | S3 (11) | D1, D0 |
| S3, X = 1 | Xm3 | S1 (01) | D0 |
| S3, X = 0 | X'm3 | S2 (10), through Z = 1 | D1, Z |

$$D0 = X(m0 + m1 + m2 + m3) = X     D1 = X'm1 + Xm2 + X'm3 = X'y0 + Xy1y0'     Z = X'm3 = X'y1y0$$

:::note Slip in deck 13 slide 8
The slide prints D0 = Xm0 + Xm2 = X(y0)' and D1 = X'm1 + Xm2. Its own chart has two more paths ending in a state with y0 = 1 (S1 → S1 and S3 → S1, both on X = 1) and one more into S2 (S3 on X = 0). The full sums above are used here; they reproduce the detector (input 101010 → Z = 000101).
:::

**Answer to the Guess:** **D0 = X**: every 1 moves the machine into a state ending in 1, every 0 into a state ending in 0.

:::check Check 10
(a) In which state, and on which input, is Z = 1? Is Z a Mealy or a Moore output? (b) Evaluate D1 for S3 with X = 0 from D1 = X'y0 + Xy1y0'.
:::

### 11 · Moore outputs: a counter

The 1010 chart had only a conditional (Mealy) output. A counter's output is its state, written inside the state boxes.

:::q <span class="tag">Deck 13 slide 18 (EX 13.18)</span>
2-bit binary up counter with input E: for E = 1 it counts S0 → S1 → S2 → S3 → S0; for E = 0 it returns to S0. The output is the count. Draw the ASM chart and give the D equations.
:::

:::guess Guess first
S3 goes to S0 for both E = 0 and E = 1. Does S3 need a decision box?
:::

:::note Terms
**Moore output in a state box:** "Out = 01" inside S1's box means the output is 01 for the whole clock period spent in S1, whatever the input does.
:::

[[fig:u4_asm_count2|What this graph plots: ASM chart of the 2-bit counter with enable E; outputs inside the state boxes (Moore); a decision on E after S0, S1, S2. S3 has a single exit to S0.|w=56]]

| Present y1y0 | Next, E = 0 | Next, E = 1 | Output |
|---|---|---|---|
| S0 = 00 | 00 | 01 | 00 |
| S1 = 01 | 00 | 10 | 01 |
| S2 = 10 | 00 | 11 | 10 |
| S3 = 11 | 00 | 00 | 11 |

$$D1 = E(y1 ⊕ y0)     D0 = Ey0'$$

*With E = 1, D1 D0 is the count plus one (13 step 3: D1 = Q1 ⊕ Q0, D0 = Q0'); E = 0 forces 00.*

:::note Slips in deck 13 slides 9 and 18
Slide 18 draws a decision box on E after S3 whose two exits both go to S0: a decision that decides nothing (left out here). Slide 9 (MOD-6 counter with enable X) prints D0 = X[Σm(0, 2, 4)] + d(6, 7) and similar for D1, D2: these contain only the X = 1 paths, so for X = 0 every flip-flop would load 0 and the counter would fall to 000 instead of holding, as its chart's X = 0 self-loops require. With the hold paths included, D0 = Xy0' + X'y0 = X ⊕ y0.
:::

**Answer to the Guess:** no. Both values of E lead to S0, so S3's box has a **single exit** to S0.

:::check Check 11
<span class="tag">Deck 13 slide 9</span> MOD-6 counter with enable X (holds when X = 0, Z = 1 on the step from S5 to S0): (a) how many state boxes and flip-flops? (b) Where is Z = 1 drawn: in a state box or a conditional box?
:::

### 12 · Serial adder

The last chart is a machine that computes: it adds two binary numbers one bit per clock, least significant bit first.

:::q <span class="tag">Deck 13 slides 13–16 (EX 13.13–13.16)</span>
A serial adder takes bits a and b from two shift registers and puts the sum bit s into a third. Give its state diagram, explain what the state remembers, and derive the flip-flop and output equations.
:::

:::guess Guess first
To add the next column, what single fact about the earlier columns must the machine remember?
:::

:::note Terms
**Serial addition:** one column per clock period, starting with the least significant bits. **Carry state:** G = carry into this column is 0, H = carry is 1; one flip-flop y holds it.
:::

[[fig:u4_serial_adder|What this graph plots: left, the serial adder's data path (shift registers A and B feed one bit each per clock into the adder FSM, whose sum bit goes into the sum register); right, its 2-state Mealy diagram, arrows labelled ab/s.|w=92]]

Each column is a full-adder step (file 04): the sum bit is 1 when an odd number of a, b, y are 1; the next carry is 1 when at least two are.

$$D = AB + Ay + By  (= Σm(3, 5, 6, 7) in ABy)     Z = A ⊕ B ⊕ y  (= Σm(1, 2, 4, 7))$$

*D is the carry out, which becomes the next state; Z is the sum bit, a Mealy output (it depends on the inputs A, B).* The circuit (slide 14) is one full adder and one D flip-flop with reset to G.

Worked: 0110 + 0111 (6 + 7), bits fed LSB first:

| Clock | a b | y (state) | s | next y |
|---|---|---|---|---|
| 1 | 0 1 | 0 (G) | 1 | 0 |
| 2 | 1 1 | 0 (G) | 0 | 1 |
| 3 | 1 1 | 1 (H) | 1 | 1 |
| 4 | 0 0 | 1 (H) | 1 | 0 |

Sum bits LSB first 1, 0, 1, 1 → **1101 = 13**.

**Answer to the Guess:** only the **carry** (0 or 1): two states, one flip-flop, however long the numbers are.

:::check Check 12
Add 0101 + 0011 serially from state G: give s and the state for each of the 4 clocks, and the sum.
:::

---

## Exam form

**Equivalent states:** same output sequence for every input sequence; one-clock test: same outputs for every input, and equivalent next states.

**Partitioning:**
1. P1 by output (Moore: the output; Mealy: the whole output row).
2. Refine: split a block when, for some input, its states' next states lie in different blocks.
3. Repeat until P(k+1) = P(k); each block becomes one state; rewrite the table.

**Implication table:**
1. Staircase grid, one cell per pair.
2. × every pair with different outputs.
3. Write implied next-state pairs in the others (✓ if none).
4. Cross every cell that implies a crossed pair; repeat until no change; survivors are equivalent (loops survive).

**Incompletely specified:** compatible pairs by the same table ignoring –; maximal compatibles from the merger diagram; choose a cover that is complete, closed (consistent) and minimal; write the reduced table.

**ASM chart:** state box (one clock period, Moore outputs), decision box (input test), conditional output box (Mealy output, after a decision box). Equations: each path = source minterm · input condition; D_i = OR of paths into states with bit i = 1.

## Traps

- Stopping when two states agree on short input sequences (D and E in step 1).
- Splitting on next states before splitting on outputs; comparing next states by name instead of by block.
- Treating compatibility as transitive: (AB) and (AC) compatible does not make (ABC) a class.
- Choosing a cover that covers every state but is not closed.
- Putting a Mealy output inside a state box, or a conditional box straight after a state box.
- Copying deck 13 slide 8's D0 = X(y0)' or slide 9's equations without hold terms.

## Self-test

1. Define equivalent states (deck 12 slide 3).
2. <span class="tag">Deck 12 slide 12</span> Reduce by partitioning: A A/0, B/0 · B H/1, C/0 · C E/0, B/0 · D C/1, D/0 · E C/1, E/0 · F F/1, G/1 · G B/0, F/0 · H H/1, C/0.
3. Why does a loop of implications in an implication table mean equivalence?
4. <span class="tag">Deck 12 slide 25</span> A 6-state incompletely specified machine has compatible classes (ABD), (BC), (E), (F). Why is the reduced machine allowed to list "A' or B'" as one next state?
5. What is an ASM block, and how long does it take?
6. <span class="tag">Deck 13 slide 11</span> Draw the ASM chart of a D flip-flop as a Moore machine (state A: Z = 0, state B: Z = 1).
7. A serial adder adds 1011 + 0110. Which state is it in after the fourth clock, and what does that state mean?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **10 and 11** (A: 01, 00; B: 00, 01). Input 11: A —1/0→ B —1/0→ E gives 00; B —1/0→ E —1/1→ A gives 01. The first outputs agree; the second differ because A has moved to B but B has moved to E. (b) Equivalence is about **every** sequence, of any length; a finite table only shows no difference has been found yet. The one-clock test (steps 3–5) proves it.

**Check 2.** B: B/0, A/1 and D: D/0, A/1 differ only because each goes to itself: **B ≡ D**. Reduced: A: B/0, C/1 · B: B/0, A/1 · C: B/1, B/0.

**Check 3.** (a) 7 states → **3** flip-flops; 4 states → **2**. (b) F is a block of its own, and C, E, G **all** go to F on w = 0: same block, so no split.

**Check 4.** P1 by output rows: (AD) give 0, 0; (BE) 1, 0; (CF) 0, 1; (GH) 1, 1. P2: on x = 0, G → H but H → C (different blocks): G, H split; the other pairs go to matching blocks (A, D → E, B and D, A; B, E → A, D and F, C; C, F → C, C and A, D). P3 = P2 = **(AD)(BE)(CF)(G)(H)**: 8 states → **5**.

**Check 5.** A cell survives only if **every** pair it implies survives. BE is crossed, so (A, C) is crossed whatever BC does.

**Check 6.** **(AF)(BCH)(D)(E)(G)**: 8 states → 5. Equivalence is transitive (slide 5): B ≡ C and C ≡ H give B ≡ H, so the three are one class.

**Check 7.** (a) A's outputs are all –, D's are all –, and their next states are never both specified for the same input (A: A, –; D: –, B): nothing can conflict. (b) **Yes**: (A, B), (A, D), (B, D) are all compatible.

**Check 8.** Complete: A, B, C in (ABC), D, E in (DE). Closed: (ABC) needs DE on x = 0 → inside (DE); AB on x = 1 → inside (ABC). (DE) needs C on x = 0 → inside (ABC); BC on x = 1 → inside (ABC). ✓ Two states, one flip-flop.

**Check 9.** (a) A conditional output depends on an input, so an input must be tested first, by a decision box. (b) The **conditional output box**: a Moore machine has no outputs that depend on the input.

**Check 10.** (a) In **S3 with X = 0**: the arrival of the final 0 of 1010. A **Mealy** output (conditional box, depends on X). (b) S3: y1y0 = 11, X = 0: X'y0 = 1 → **D1 = 1**: the next state S2 = 10 has y1 = 1 ✓.

**Check 11.** (a) **6** state boxes (S0–S5), **3** flip-flops. (b) In a **conditional output box** on S5's X = 1 exit: Z depends on X, a Mealy output.

**Check 12.** Bits LSB first: a = 1, 0, 1, 0; b = 1, 1, 0, 0. Clock 1: y 0 (G), s 0, carry 1 → H. Clock 2: y 1, s 0, → H. Clock 3: y 1, s 0, → H. Clock 4: y 1, a b = 0 0, s 1, → G. Sum bits 0, 0, 0, 1 → **1000 = 8**.

**Self-test.**

1. States are equivalent when, for every possible input sequence, the circuit produces the same output sequence whichever of them it starts in.
2. P1 by output rows: (ACG) 0, 0; (BDEH) 1, 0; (F) 1, 1. P2: in (ACG), the next-state blocks (x = 0; x = 1) are A: ACG, BDEH · C: BDEH, BDEH · G: BDEH, F: all three split. In (BDEH): B: BDEH, ACG · D: ACG, BDEH · E: ACG, BDEH · H: BDEH, ACG: (BH)(DE). P2 = **(A)(BH)(C)(DE)(F)(G)**; P3 = P2 (B, H → H, H and C, C; D, E → C, C and D, E). 8 → **6** states.
3. Every pair in the loop needs only pairs in the loop; none of them can ever be crossed, so each pair passes the one-clock test with assumptions that are themselves consistent: no input sequence can separate them.
4. B lies in both (ABD) and (BC). A next state B may be represented by either class, so either choice keeps the table correct (slide 25).
5. One state box plus the decision and conditional output boxes reached from it before the next state box; it lasts **one clock period**.
6. State box A (Z = 0) → decision D: 0 → A, 1 → B. State box B (Z = 1) → decision D: 0 → A, 1 → B. Next state = D (slide 11: D = Y'D + YD = D).
7. 1011 + 0110 = 11 + 6 = 17 = 10001: the 4-bit sum is 0001 and the final carry is 1, so the machine is in **H (carry 1)**: the fifth sum bit (1) is still owed.

<!--/ANSWERS-->
