# 15 — FSM design: Mealy, Moore, sequence detectors

<div class="sub">Deck 11 (slides 2–43) · syllabus Unit 4 (finite state machines; design of synchronous FSM) · real questions: deck 11's worked examples (1101, 1010, 110, 111) and the five practice detectors on slide 43; none on the MTE or the practice sets · needs 13 steps 2–7 (state table → excitation → K-maps → circuit), 09 step 12 (excitation tables), 02 steps 5–7 (K-maps with don't-cares)</div>

## Map

[[map:1 What a state remembers > 2 Words to states: the 1101 chain > 3 Every state, every input > 4 Overlapping or not > 5 The state table > 6 State assignment: counting order > 7 Gray assignment and the circuit > 8 Other flip-flops: T and JK > 9 Mealy and Moore > 10 The 111 detector both ways > 11 Moore 1101: the extra state > 12 The five practice detectors|here=1]]

File 13 designed counters: circuits that walk a fixed list of states, one step per clock. Here an **input** decides which state comes next, and an **output** reports something about the inputs seen so far. That is a **finite state machine (FSM)**, the general synchronous circuit. The design procedure is 13's (state table → excitation → K-maps → circuit) with one new first step: turning a sentence ("detect 1101") into a state diagram. File 16 then shrinks state tables that have more states than they need and draws the same machines as ASM charts.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| X (or x) | the serial input: one bit per clock period, sampled at the clock edge | 0 or 1 |
| Z (or z, y) | the output: 1 when the pattern has just arrived | 0 or 1 |
| A, B, C, D, E · S0, S1, … | state names; each stands for "how much of the pattern has arrived" | 3–6 states |
| Y1, Y2 (Y1, Y0 in steps 10–11) | the flip-flop outputs that hold the state code; Y2 Y1 Y0 when 3 bits are needed | 0 or 1 |
| D1, D2 · T · J, K | flip-flop inputs (D1 = the D input of the flip-flop holding Y1) | 0 or 1 |
| 1/0 on an arrow | Mealy label: input / output on that transition | — |
| A/0 in a circle | Moore label: state / output while in that state | — |
| X in a K-map or table | don't-care (an unused code, or a JK input either value satisfies) | — |

## Running example

**The 1101 detector of deck 11, overlap allowed** (slides 7–34): input 1101101 must give Z = 0001001 (two matches, the middle 1 shared). Steps 2–5 build its state diagram and table; steps 6–8 turn it into a circuit three ways (D with counting order, D with Gray order, T + JK); step 11 builds its Moore version. Every equation is checked by running 1101101 through it.

## The questions this file answers

- <span class="tag">Deck 11 slides 7–25</span> Recognize the sequence 1101 (1101101 contains it twice); state diagram, state table, state assignment, D flip-flop equations, circuit.
- <span class="tag">Deck 11 slides 32–34</span> The same detector with a T flip-flop for Y1 and a JK flip-flop for Y2.
- <span class="tag">Deck 11 slides 26–27</span> Sequence recognizers 1010 and 110: non-overlapping and overlapping.
- <span class="tag">Deck 11 slides 35–42</span> Mealy and Moore circuits; the 111 detector both ways; the Moore 1101 detector.
- <span class="tag">Deck 11 slide 43</span> Design a Moore circuit for x = 1011; Moore for 11011; Moore/Mealy for 10101; Moore/Mealy for 1X1; Mealy for 1XX1 (z = 1 when the sequence occurs, else 0).

---

## Build

### 1 · What a state remembers

A door keypad with the code 1101 does not store every key ever pressed. It keeps one thing: **how far into the code you are**. Press 1, 1, 0 and it is "three in"; press a wrong key and it falls back. A sequence detector works the same way.

:::guess Predict
Bits arrive one per clock. Z must be 1 when the last four bits are 1101. Must the circuit store the last four bits (16 possibilities, 4 flip-flops), or less?
:::

:::note Terms
**State:** what the circuit remembers about the inputs so far, held in its flip-flops; it is chosen to be exactly what is needed to decide future outputs (deck 11 slides 4–5). n flip-flops hold up to 2ⁿ states. **Sequence recognizer (detector):** a sequential circuit whose output is 1 each time a given pattern has just arrived at its input (slide 5).
:::

| State | What has arrived (the useful tail of the input) | If the next bit is 1 | If the next bit is 0 |
|---|---|---|---|
| A | nothing useful | "1" | still nothing |
| B | "1" | "11" | nothing |
| C | "11" | still "11" | "110" |
| D | "110" | 1101 complete: Z = 1 | nothing |

The table is the keypad: four situations, each one "how far into 1101". Each situation is a state; the clock moves the machine from one to the next.

**Answer to the Predict:** less. Only four situations matter, so **2 flip-flops** (2² = 4) are enough, not 4. Storing the last four bits would also work, but would need 16 states where 4 do.

:::check Check 1
(a) How many states can 3 flip-flops hold? (b) A machine has 5 states. How many flip-flops does it need? (c) What does state C mean in the table above?
:::

### 2 · Words to states: the 1101 chain

Step 1 listed the four situations. A **state diagram** draws them as circles with arrows, one arrow per input value.

:::q <span class="tag">Deck 11 slides 7–11 (EX 11.8–11.11)</span>
Recognize the sequence 1101. The sequence 1101101 contains 1101 twice; the 1 in the middle belongs to both. The sequence must be recognized each time it occurs.
:::

:::guess Guess first
After 1101 has arrived and Z = 1, where should the arrow go: back to the start A, or somewhere else?
:::

:::note Terms
**Arrow label x/z (Mealy):** "on input x, go along this arrow, and the output is z during this clock period". **Reset state:** the state the machine starts in, where none of the pattern has arrived (slide 6).
:::

[[fig:u4_chain_1101|What this graph plots: one circle per state; each arrow is one clock period with input/output written on it. The chain A → B → C → D follows 1, 1, 0; the green arrow is the final 1, with output 1.|w=78]]

Deck 11's procedure (slide 6), applied:

1. Start in A, where none of 1101 has arrived.
2. Add a state for each new symbol of the pattern: B after "1", C after "11", D after "110".
3. The arrow out of D on a 1 completes 1101: label it **1/1**.
4. Where does it go? The final 1 of 1101 is also the **first 1** of the next possible 1101 (1101**1**01). So after it the machine has "1", which is exactly state **B** (slide 10).

**Answer to the Guess:** to **B**, not A. Going to A would forget the 1 that just arrived and miss the second match in 1101101.

:::check Check 2
Run 1101101 through the chain (start in A). After which input bits is the machine in state B, and after which bits is Z = 1?
:::

### 3 · Every state, every input

The chain covers only the bits that fit the pattern. A circuit receives 0s and 1s in any order, so every state needs an arrow for **both** input values.

:::q <span class="tag">Deck 11 slides 12–13 (EX 11.12–11.13)</span>
The other arcs are added to each state for inputs not yet listed. Which arcs are missing?
:::

:::guess Guess first
List them: which states lack a 0 arrow, and which lack a 1 arrow?
:::

:::note Terms
**Fall-back rule:** on a bit that breaks the pattern, go to the state for the **longest tail of what has arrived that is still a beginning of the pattern**. (Slide 6: "add other arcs which transition to states that represent the input subsequence that has occurred.")
:::

[[fig:u4_mealy_1101|What this graph plots: the complete Mealy 1101 detector: 4 states, 8 arrows (two per state), each labelled input/output. Only D's 1-arrow has output 1.|w=78]]

| State | Missing arrow | What has arrived | Longest tail that begins 1101 | Goes to |
|---|---|---|---|---|
| A | 0 | "0" | none | A (0/0) |
| B | 0 | "10" | none ("0" does not begin 1101) | A (0/0) |
| C | 1 | "111" | "11" | C (1/0) |
| D | 0 | "1100" | none | A (0/0) |

C's self-loop means "two or more 1s have arrived" (slide 13): extra 1s keep the last two bits at 11.

**Answer to the Guess:** four arrows were missing: **0 from A, 0 from B, 1 from C, 0 from D**. The finished diagram has 4 × 2 = 8 arrows.

:::check Check 3
<span class="tag">Deck 11 slide 7</span> Run 1111101 through the complete diagram from A. Give the state after each bit and the output Z for each bit.
:::

### 4 · Overlapping or not

Step 2's D → B arrow let the last 1 start a new match. Some problems forbid that: after a match the next match must use fresh bits.

:::q <span class="tag">Deck 11 slide 26 (EX 11.26)</span>
Sequence recognizer 1010: draw the non-overlapping and the overlapping state diagrams.
:::

:::guess Guess first
In the overlapping version, 1010 has just arrived. Which tail of it begins a new 1010: "0", "10", or "010"?
:::

:::note Terms
**Overlapping detector:** bits of one match may also be bits of the next (1010**10** gives two matches). **Non-overlapping:** after a match the machine starts again from the reset state, as if nothing had arrived.
:::

[[fig:u4_1010|What this graph plots: two Mealy 1010 detectors that differ in one arrow (green): after the match, non-overlapping returns to S0, overlapping goes to S2 ("10" already arrived).|w=92]]

- States: S0 nothing, S1 "1", S2 "10", S3 "101". Both diagrams share every arrow except S3's 0-arrow.
- **Non-overlapping:** S3 —0/1→ **S0**: the match is used up.
- **Overlapping:** S3 —0/1→ **S2**: the last two bits "10" are the first two bits of the next 1010.

The rule for the completing arrow: overlapping → go to the state of the longest tail of the pattern that is also its beginning; non-overlapping → go to the reset state.

:::note Slip in deck 11 slide 27
Slide 27 ("Sequence Detector 110") has an **"Overlapping"** heading with an empty panel. The panel can stay empty for a reason: no tail of 110 ("0" or "10") is a beginning of 110, so the overlapping and non-overlapping 110 detectors are **the same diagram** (S2 —0/1→ S0 in both).
:::

**Answer to the Guess:** "10". The overlapping 1010 detector sends S3's 0-arrow to S2. Input 101010 gives Z = 000101 overlapping and Z = 000100 non-overlapping.

:::check Check 4
(a) Which one arrow changes to make step 3's 1101 detector non-overlapping? (b) Run 1101101 through the non-overlapping version: write Z.
:::

### 5 · The state table

The diagram is complete; the circuit needs the same facts as a table, one row per present state.

:::q <span class="tag">Deck 11 slides 14–16 (EX 11.14–11.16)</span>
From the state diagram, fill in the state table: 4 states, one input, one output. What is the minimum number of bits to code 4 states?
:::

:::guess Guess first
How many entries does the table hold (next state and output, for every state and every input)?
:::

:::note Terms
**State table:** one row per present state; for each input value, the next state and the output. It is the state diagram written as a table: one arrow = one (next, output) entry.
:::

| Present state | Next, x = 0 | Next, x = 1 | Z, x = 0 | Z, x = 1 |
|---|---|---|---|---|
| A | A | B | 0 | 0 |
| B | A | C | 0 | 0 |
| C | D | C | 0 | 0 |
| D | A | B | 0 | 1 |

Number of flip-flops: the smallest n with 2ⁿ ≥ number of states. Four states: 2² = 4, so **2 bits, 2 flip-flops** (slide 16), and every 2-bit code 00, 01, 10, 11 is used once.

**Answer to the Guess:** 4 states × 2 inputs = **8 next-state entries and 8 output entries**, one pair per arrow of step 3's diagram. Minimum bits: **2**.

:::check Check 5
Write the state table of the overlapping 1010 detector of step 4 (states S0–S3).
:::

### 6 · State assignment: counting order

The table names states with letters; flip-flops hold bits. Giving each state a code is **state assignment**.

:::q <span class="tag">Deck 11 slides 17–21 (EX 11.17–11.21)</span>
Use counting order A = 00, B = 01, C = 10, D = 11 and D flip-flops. Obtain the K-maps for D1, D2 and Z and minimise them.
:::

:::guess Guess first
With D flip-flops, what is D1 in row B for x = 1 (B goes to C)?
:::

:::note Terms
**Coded state table:** the state table with each letter replaced by its code Y1 Y2. **D flip-flop design:** the D input must equal the next value of its bit (D = Q⁺, 13 step 3), so each D column of the K-map is copied straight from the next-state column. **Gate-input cost:** the number of gate inputs the equations need: every literal entering an AND, plus one OR input per product term (a term that is a single literal needs no AND).
:::

| Y1 Y2 | Next, x = 0 | Next, x = 1 | Z, x = 0 | Z, x = 1 |
|---|---|---|---|---|
| A = 00 | 00 | 01 | 0 | 0 |
| B = 01 | 00 | 10 | 0 | 0 |
| C = 10 | 11 | 10 | 0 | 0 |
| D = 11 | 00 | 01 | 0 | 1 |

<div class="two">

[[fig:km_cnt_D1|What this graph plots: one cell per (present state, input); row Y1, columns Y2 X; 1 = the next Y1 is 1. Groups: the pair Y1Y2' (state C, both inputs) and the single cell Y1'Y2X (B with x = 1).]]

[[fig:km_cnt_D2|Same layout for the next Y2. Three 1s, no two adjacent: three 3-literal terms.]]

</div>

$$D1 = Y1Y2' + Y1'Y2X     D2 = Y1'Y2'X + Y1Y2'X' + Y1Y2X     Z = Y1Y2X$$

*D1: in C (either input), or in B when x = 1. D2: three separate cells, none adjacent.* Gate-input cost: D1 = 5 literals + 2 OR inputs = 7; D2 = 9 + 3 = 12; Z = 3 (one AND, no OR). **Total 22.**

**Answer to the Guess:** row B, x = 1: next state C = **10**, so **D1 = 1** (and D2 = 0). That is the cell Y1Y2X = 011 in the D1 map.

:::check Check 6
(a) In the counting-order table, which entry puts the 1 in D2's cell Y1Y2X = 100? (b) Check D2 = Y1'Y2'X + Y1Y2'X' + Y1Y2X in row D, x = 1.
:::

### 7 · Gray assignment and the circuit

Step 6 works but costs 22 gate inputs. The same table with other codes can cost much less.

:::q <span class="tag">Deck 11 slides 22–25 (EX 11.22–11.25)</span>
Another possible assignment is Gray code: A = 00, B = 01, C = 11, D = 10. Obtain the K-maps for D1, D2 and Z, minimise, and draw the circuit with D flip-flops that have a reset input.
:::

:::guess Guess first
Look at the next-state column for x = 1 in the table below. What do you notice about its second bit?
:::

:::note Terms
**Reset input:** an asynchronous input on every flip-flop that forces the state code to the reset state's code (00 = A) when the circuit is switched on (slide 25).
:::

| Y1 Y2 | Next, x = 0 | Next, x = 1 | Z, x = 0 | Z, x = 1 |
|---|---|---|---|---|
| A = 00 | 00 | 01 | 0 | 0 |
| B = 01 | 00 | 11 | 0 | 0 |
| C = 11 | 10 | 11 | 0 | 0 |
| D = 10 | 00 | 01 | 0 | 1 |

<div class="two">

[[fig:km_gray_D1|What this graph plots: next Y1 for each (Y1Y2, X) under the Gray codes. Two overlapping pairs: Y1Y2 (state C) and Y2X.]]

[[fig:km_gray_D2|Next Y2: 1 in every cell with X = 1 and nowhere else, so D2 = X.]]

</div>

$$D1 = Y1Y2 + XY2     D2 = X     Z = XY1Y2'$$

*D2 = X: under these codes, the second bit of every next state simply records the bit that just arrived. Z: in D (10) with x = 1.* Gate-input cost: D1 = 4 + 2 = 6, D2 = 0 (a wire), Z = 3: **total 9, against 22** for counting order. Deck 11 completes the design with this assignment (slide 24).

[[fig:u4_gray_circuit|The 1101 detector (deck 11 slide 25): two D flip-flops on one clock, reset to 00 = A; D1 from two ANDs and an OR, D2 a plain wire from X, Z one 3-input AND.|w=86]]

Checking the circuit with the running example, 1101101 from 00: Y1Y2 goes 01, 11, 10, 01, 11, 10, 01 and Z = 0, 0, 0, 1, 0, 0, 1: **Z = 0001001**, both matches.

**Answer to the Guess:** for x = 1 every next state ends in 1; for x = 0 every one ends in 0. The second bit is the input itself, so **D2 = X** with no gates. The codes do not change what the machine does, only how many gates it needs: **9 gate inputs instead of 22**.

:::check Check 7
Start the Gray-coded circuit at 00 and apply x = 1, 1, 0, 1. Give Y1 Y2 after each clock edge, and Z during the last bit.
:::

### 8 · Other flip-flops: T and JK

Steps 6–7 used D flip-flops, where the input is the next state. With T or JK flip-flops the input says how to **change**, and comes from the excitation tables of 09 step 12.

:::q <span class="tag">Deck 11 slides 32–34 (EX 11.32–11.34)</span>
Use a T flip-flop for Y1 and a JK flip-flop for Y2, with the Gray code assignment. Obtain the excitation table for the T and JK inputs, optimise the equations, and give the total gate-input cost.
:::

:::guess Guess first
Row B = 01 with x = 0 goes to 00. What must T (for Y1) and J, K (for Y2) be?
:::

:::note Terms
**Excitation table** (09 step 12): for each change Q → Q⁺, the input that causes it. T: T = 1 exactly when the bit changes. JK: 0→0 needs J = 0, K = X; 0→1 needs J = 1, K = X; 1→0 needs J = X, K = 1; 1→1 needs J = X, K = 0.
:::

| Y1 Y2 | Next (x = 0, x = 1) | T for Y1 (x = 0, 1) | J K for Y2, x = 0 | J K for Y2, x = 1 | Z (x = 0, 1) |
|---|---|---|---|---|---|
| A = 00 | 00, 01 | 0, 0 | 0 X | 1 X | 0, 0 |
| B = 01 | 00, 11 | 0, 1 | X 1 | X 0 | 0, 0 |
| C = 11 | 10, 11 | 0, 0 | X 1 | X 0 | 0, 0 |
| D = 10 | 00, 01 | 1, 1 | 0 X | 1 X | 0, 1 |

<div class="two">

[[fig:km_T_1101|What this graph plots: T for Y1 per (Y1Y2, X): 1 where Y1 must change (B with x = 1; D with either input). Groups Y1Y2' and Y1'Y2X.]]

[[fig:km_J_1101|J for Y2: 1 in A and D with x = 1; the Y2 = 1 cells are don't-cares (X). The whole X = 1 column groups: J = X.]]

</div>

$$T = Y1Y2' + Y1'Y2X     J = X     K = X'     Z = XY1Y2'$$

*K is 1 in B and C with x = 0, don't-care where Y2 = 0: the whole x = 0 column, K = X'.* Gate-input cost: T = 5 + 2 = 7, J and K = 0 (a wire and an inverter), Z = 3: **10** (slide 33). The JK flip-flop still records the input: J = X, K = X' makes Y2⁺ = X, as D2 = X did.

**Answer to the Guess:** Y1 stays 0 → **T = 0**. Y2 goes 1 → 0 → **J = X (don't-care), K = 1**.

:::check Check 8
(a) Row D = 10, x = 1, goes to 01. Give T, J, K. (b) Rank the three designs (counting-order D, Gray D, T + JK) by gate-input cost.
:::

### 9 · Mealy and Moore

Every output so far was written on an arrow and used the input: Z = XY1Y2'. That is one of two ways to build the output.

:::q <span class="tag">Deck 11 slides 35–36</span>
Two ways to design clocked sequential circuits: Mealy and Moore type. Differentiate them.
:::

:::guess Guess first
Find the one wire that differs between the two block diagrams below.
:::

:::note Terms
**Mealy machine:** the output is a function of the present state **and the present input**. **Moore machine:** the output is a function of the present state **only**; the logic splits into next-state logic and output logic (slide 36).
:::

[[fig:fsm_blocks|Moore (output logic fed by the state only) and Mealy (output logic fed by the state and the input). The memory elements and next-state logic are the same in both.]]

| | Mealy | Moore |
|---|---|---|
| Output depends on | present state and present input | present state only |
| Written in the diagram | on the arrow (x/z) | inside the circle (S/z) |
| When the output changes | whenever the input changes, even between clock edges | only after a clock edge; steady for the whole period |
| Number of states for a detector | fewer | usually one more (slide 40) |
| Detector output appears | in the same clock period as the last bit | in the period after the last bit's edge |

**Answer to the Guess:** the wire from the **input X to the output logic**. Mealy has it; Moore does not. The 1101 detector so far is **Mealy** (Z = XY1Y2' contains X).

:::check Check 9
(a) Is Z = Y1Y0' a Mealy or a Moore output? (b) Why does a Moore circle carry its output, but a Mealy arrow carries its output?
:::

### 10 · The 111 detector both ways

Step 9 listed the differences; the 111 detector shows them on one problem, including the drawback of Mealy (slide 37).

:::q <span class="tag">Deck 11 slides 37–39 (EX 11.37–11.39)</span>
Design a 111 sequence detector as a Mealy machine and as a Moore machine (Gray code assignment, D flip-flops). Compare their timing.
:::

:::guess Guess first
The Moore machine needs one more state than the Mealy one. What does that extra state mean?
:::

:::note Terms
**False output:** a Mealy output pulse caused by the input changing between clock edges, when the pattern is not actually completed at the edge (slide 39).
:::

[[fig:u4_111|What this graph plots: the 111 detector as Mealy (3 states, output on the arrows) and Moore (4 states, output in the circles: D/1 = "111 has arrived").|w=92]]

| | Codes Y1 Y0 | Next-state and output equations (slide 38) |
|---|---|---|
| Mealy | A 00, B 01, C 11 (10 unused) | D1 = XY0 · D0 = X · Z = XY1 |
| Moore | A 00, B 01, C 11, D 10 | D1 = X(Y0 + Y1) · D0 = XY1' · Z = Y1Y0' |

[[fig:u4_111_timing|What this graph plots: time across, one row per signal; state rows show the state in each clock period. X = 1, 1, 0, 1, 1, 1, 1 at the rising edges, but X is also 1 for part of period 3. Mealy Z follows X inside state C (red pulse: false output); Moore Z rises only at the edge that enters D.|w=92]]

Reading the timing diagram:

1. Edges 1 and 2 sample X = 1: both machines reach C ("11").
2. During period 3 X is 1 for a while, then 0 before edge 3. Mealy Z = XY1 is 1 while X is 1 in state C: a pulse, although edge 3 samples X = 0 and no 111 occurred. **False output.**
3. Moore Z = Y1Y0' depends on the state only, which changes only at edges: no pulse.
4. Edges 4–6 sample 1, 1, 1. Mealy Z is 1 during period 6 (state C, X = 1); Moore Z goes high at edge 6, when the machine enters D, and stays high for whole periods.

**Answer to the Guess:** D means **"111 has just arrived"**. A Moore output belongs to a state, so the "match" needs its own state; in Mealy the match is an arrow out of C.

:::check Check 10
(a) Check the Mealy D1 = XY0 in row B, x = 1. (b) From reset, x = 1, 1, 1: in which clock period is Mealy Z first 1, and in which is Moore Z first 1?
:::

### 11 · Moore 1101: the extra state

The running example was Mealy. Its Moore version follows step 10's rule: the match gets its own state.

:::q <span class="tag">Deck 11 slides 40–42 (EX 11.40–11.42)</span>
For the Moore model, outputs depend on states. Add a state E with output 1 for the final 1 of the recognized sequence, and give the state and output tables.
:::

:::guess Guess first
E is entered on the final 1 of 1101. Where should E go on the next 1, and on the next 0?
:::

:::note Terms
**E:** "1101 has just arrived", output 1. It plays B's role for the future (one useful 1 has arrived) but differs from B in its output, so it cannot be B (slide 41).
:::

[[fig:moore_1101|What this graph plots: the Moore 1101 detector: five circles labelled state/output; arrows carry the input only. E/1 is the only state with output 1.|w=82]]

| Present state | Next, x = 0 | Next, x = 1 | Output y |
|---|---|---|---|
| A | A | B | 0 |
| B | A | C | 0 |
| C | D | C | 0 |
| D | A | E | 0 |
| E | A | C | 1 |

Five states need **3 flip-flops** (2³ = 8 ≥ 5). With codes A = 000, B = 001, C = 010, D = 011, E = 100 (Y2 Y1 Y0) and the three unused codes 101–111 as don't-cares, D flip-flops give:

$$D2 = Y1Y0X     D1 = Y2X + Y1Y0' + Y1'Y0X     D0 = Y1Y0'X' + Y2'Y1'Y0'X     y = Y2$$

*y = Y2: only E has Y2 = 1, so the output is a wire from one flip-flop.* Run 1101101: states B, C, D, E, C, D, E; y is 1 in the periods after edges 4 and 7: the same two matches, each one clock period later than Mealy's Z.

**Answer to the Guess:** on a 1, E goes to **C**: the last two bits are "11" (as from B). On a 0, E goes to **A**: "10" begins no 1101. E's row is B's row with the output changed from 0 to 1.

:::check Check 11
(a) Why can't E and B be merged into one state? (b) Check D2 = Y1Y0X: which transition is the only one that enters E?
:::

### 12 · The five practice detectors

Steps 2–11 used patterns of fixed bits. Slide 43's practice list adds patterns with **X** (any bit), which need a different kind of state.

:::q <span class="tag">Deck 11 slide 43 Q1</span>
Design a Moore circuit to detect a sequence: if the input x = 1011 then output z = 1, otherwise z = 0.
:::

:::guess Guess first
After 1011 has arrived (overlap allowed), which tail of it begins a new 1011? Where does each arrow out of the match state go?
:::

:::note Terms
**Wildcard pattern (1X1, 1XX1):** X matches either bit. The machine can no longer track "how far into the pattern": a 0 in the X position must not break the match. Instead it **remembers the last n − 1 bits** (n = pattern length), because each of them may matter later.
:::

[[fig:u4_1011_moore|What this graph plots: the Moore 1011 detector, overlap allowed: S0 nothing, S1 "1", S2 "10", S3 "101", S4 "1011" (output 1). Arrows carry the input only.|w=86]]

| State (what has arrived) | Next, x = 0 | Next, x = 1 | z |
|---|---|---|---|
| S0 (nothing) | S0 | S1 | 0 |
| S1 ("1") | S2 | S1 | 0 |
| S2 ("10") | S0 | S3 | 0 |
| S3 ("101") | S2 | S4 | 0 |
| S4 ("1011") | S2 | S1 | 1 |

From S4 the useful tail is "1" (a 1 → "11", whose tail "1" is S1; a 0 → "10" = S2). Five states → 3 flip-flops; the circuit follows steps 6–7.

**Wildcards.** For **1X1** (Q4) the output on the next bit depends on the bit **two back**, so the Mealy machine remembers the last two bits: **4 states** (00, 01, 10, 11), with z = 1 on an input 1 from states 10 and 11. For **1XX1** (Q5) it remembers the last three bits: **8 states**. These are minimal: state reduction (file 16) merges none of them.

| Practice detector (slide 43, overlap allowed) | Mealy states | Moore states |
|---|---|---|
| Q1 1011 | 4 | **5** |
| Q2 11011 | 5 | **6** |
| Q3 10101 | **5** | **6** |
| Q4 1X1 | **4** | **6** |
| Q5 1XX1 | **8** | 12 |

(Bold = the version slide 43 asks for.)

**Answer to the Guess:** the tail "1" begins 1011, so the match state S4 acts like S1: on 1 → **S1**, on 0 → **S2** ("10").

:::check Check 12
<span class="tag">Deck 11 slide 43 Q4</span> Write the Mealy state table for 1X1 with states S0 = last two bits 00 (or reset), S1 = 01, S2 = 10, S3 = 11.
:::

---

## Exam form

**Mealy vs Moore** (5 marks): the two block diagrams (step 9) and the table: output from state + input vs state only; on the arrow vs in the circle; changes with the input (can give false outputs) vs only at edges; fewer states vs usually one more; same period vs one period later.

**Sequence detector design** (the full procedure, deck 11 slide 3):
1. Specification: the pattern; overlapping or not; Mealy or Moore.
2. States: reset state, then one state per symbol of the pattern ("1", "11", "110").
3. Completing arrow: Mealy 1/1 (or Moore: a match state with output 1); overlapping → to the longest tail that begins the pattern, non-overlapping → to reset.
4. Every state gets an arrow for x = 0 and x = 1 (fall-back rule).
5. State table → number of flip-flops (2ⁿ ≥ states) → state assignment (try Gray order).
6. Flip-flop inputs: D = next state; T, JK from the excitation table; unused codes are don't-cares.
7. K-maps → equations → circuit with a common clock and a reset to the start state.
8. Verify: run a test string with two overlapping matches (1101101 → 0001001).

## Traps

- Sending an overlapping detector's completing arrow to the reset state.
- A state with only one outgoing arrow.
- Writing a Mealy output inside the circle, or using the input in a Moore output equation.
- Forgetting that a Moore detector needs the extra match state (and its row in the table).
- Treating a wildcard X in 1X1 as "the pattern must contain the letter X": it means either bit.
- Copying deck 11's slide 27 "Overlapping" panel as missing: for 110 it is the same diagram.
- Leaving out the reset to the start state's code.

## Self-test

1. Give three differences between Mealy and Moore machines.
2. <span class="tag">Deck 11 slide 43 Q2</span> Moore circuit for 11011 (overlap allowed): state meanings and state table.
3. <span class="tag">Deck 11 slide 43 Q3</span> Mealy state table for 10101 (overlap allowed). What changes for Moore?
4. <span class="tag">Deck 11 slide 43 Q5</span> Mealy detector for 1XX1: how many states, and what does each one remember?
5. Draw the Mealy 101 detector, overlap allowed.
6. Why can the state assignment change the cost of the circuit but not its behaviour? Give the numbers for the 1101 detector.
7. How many flip-flops for a 6-state machine, and how many unused codes become don't-cares?

<!--ANSWERS-->

## Answers

**Check 1.** (a) 2³ = **8**. (b) **3** (2² = 4 < 5 ≤ 8). (c) "11 has arrived" (two or more 1s in a row, the last bits).

**Check 2.** States A → B → C → D → B → C → D → B. In **B after bits 1, 4 and 7**; **Z = 1 on bits 4 and 7** (Z = 0001001).

**Check 3.** States after each bit: B, C, C, C, C, D, B. **Z = 0000001**: the 1101 at the end is found although five 1s came first.

**Check 4.** (a) D —1/1→ B becomes **D —1/1→ A**. (b) **Z = 0001000**: the second 1101 shares the middle 1 with the first, which non-overlapping forbids.

**Check 5.**

| Present | Next, x = 0 | Next, x = 1 | Z, x = 0 | Z, x = 1 |
|---|---|---|---|---|
| S0 | S0 | S1 | 0 | 0 |
| S1 | S2 | S1 | 0 | 0 |
| S2 | S0 | S3 | 0 | 0 |
| S3 | S2 | S1 | 1 | 0 |

**Check 6.** (a) Row C = 10, x = 0: next D = 11, so D2 = 1 at Y1Y2X = 100. (b) Row D: Y1Y2X = 111: the term Y1Y2X = 1, so D2 = 1; the table gives next 01, D2 = 1. ✓

**Check 7.** 00 → **01 → 11 → 10 → 01**. During the last bit the machine is in 10 (D) with x = 1: **Z = XY1Y2' = 1**.

**Check 8.** (a) Y1: 1 → 0, **T = 1**. Y2: 0 → 1, **J = 1, K = X**. (b) **Gray D: 9 < T + JK: 10 < counting-order D: 22.**

**Check 9.** (a) **Moore**: it uses only state bits. (b) A Moore output is fixed for the whole time the machine is in a state, so it belongs to the state; a Mealy output also depends on the input, so it belongs to a (state, input) pair, which is an arrow.

**Check 10.** (a) B = 01, x = 1: next C = 11, Y1⁺ = 1; XY0 = 1 · 1 = **1** ✓. (b) **Mealy: period 3** (in C, the third 1 present, before edge 3). **Moore: period 4** (after edge 3 enters D).

**Check 11.** (a) Their outputs differ (B: 0, E: 1): equivalent states must give the same output (file 16 step 1). (b) Only **D (011) with x = 1** goes to E (100); D2 = Y1Y0X is 1 exactly there (Y2 = 1 with Y1Y0 = 11 is unused).

**Check 12.**

| Present (last two bits) | Next, x = 0 | Next, x = 1 | z, x = 0 | z, x = 1 |
|---|---|---|---|---|
| S0 (00) | S0 | S1 | 0 | 0 |
| S1 (01) | S2 | S3 | 0 | 0 |
| S2 (10) | S0 | S1 | 0 | **1** |
| S3 (11) | S2 | S3 | 0 | **1** |

z = 1 when x = 1 and the bit two back was 1 (states 10 and 11).

**Self-test.**

1. Output from state + input vs state only; on the arrow vs in the circle; Mealy can give false outputs between edges, Moore changes only at edges; Moore usually needs one more state; Mealy responds in the same period, Moore one period later.
2. S0 nothing, S1 "1", S2 "11", S3 "110", S4 "1101", S5 "11011" (z = 1). Next (x = 0, x = 1): S0 → S0, S1 · S1 → S0, S2 · S2 → S3, S2 · S3 → S0, S4 · S4 → S0, S5 · S5 → S3, S2. Six states, 3 flip-flops.
3. S0 nothing, S1 "1", S2 "10", S3 "101", S4 "1010". Next/z (x = 0; x = 1): S0 S0/0; S1/0 · S1 S2/0; S1/0 · S2 S0/0; S3/0 · S3 S4/0; S1/0 · S4 S0/0; **S3/1**. Moore: add S5 "10101" (z = 1): S4 —1→ S5, and S5 → S4 on 0, S1 on 1. Five Mealy states, six Moore states.
4. **8 states**, one per value of the last three bits (000 … 111). z = 1 on input 1 when the oldest of the three bits is 1 (states 100–111).
5. S0: 0/0 → S0, 1/0 → S1. S1 ("1"): 0/0 → S2, 1/0 → S1. S2 ("10"): 0/0 → S0, **1/1 → S1**.
6. The codes change the next-state and output equations, not the state table; codes that put related states in adjacent cells give bigger K-map groups. 1101 detector: counting order **22** gate inputs, Gray order **9**.
7. **3 flip-flops** (2² = 4 < 6 ≤ 8); **2 unused codes**, don't-cares in every K-map.

<!--/ANSWERS-->
