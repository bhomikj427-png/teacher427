# 13 — Synchronous counters

<div class="sub">Deck 10 (slides 18–37) · syllabus Unit 3 (synchronous counters, up/down counters, MOD-N counters) · 4 real questions: MTE 2025 Q8 (8 marks), practice set 2 Q4, Q5, Q6 · needs 09 step 12 (excitation tables), 02 steps 1–5 and 7 (K-maps, don't-cares), 12 steps 5–7 (ripple delay, MOD-N, decade counter)</div>

## Map

[[map:1 Why one shared clock > 2 State diagram and state table > 3 D flip-flops > 4 T flip-flops > 5 JK flip-flops > 6 MTE Q8: the 3-bit table > 7 MTE Q8: K-maps and circuit > 8 Down counters > 9 MOD-N: the decade counter > 10 Unused states, self-starting > 11 Up/down counters > 12 Any sequence: Gray code|here=1]]

File 12 built counters by letting each flip-flop clock the next; they need no gates, but the outputs settle one stage after another and show false counts on the way. This file gives **every flip-flop the same clock** and puts gates in front of each flip-flop to decide whether it changes at the next edge. Finding those gates is a fixed procedure: state table → excitation table (09 step 12) → K-maps (02) → circuit. The procedure works for any count order and any flip-flop type, and file 15 reuses it unchanged for every state machine.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| CLK | the clock; in this file it goes to every flip-flop | 1 – 100 MHz |
| Q0, Q1, Q2, Q3 | flip-flop outputs; Q0 is the least significant bit; the count is read Q2 Q1 Q0 | 0 or 1 |
| Q⁺ (Q1⁺, …) | the value a Q takes after the next clock edge (next state) | 0 or 1 |
| present state | the count Q2 Q1 Q0 now, before the edge | 000 – 111 |
| D, T, J, K | flip-flop inputs (D0 = the D input of FF0, …) | 0 or 1 |
| X (in a table or K-map) | don't-care: either value gives the required result | — |
| Dn, Up | direction inputs of up/down counters: Dn = 1 counts down (deck 10 slides 29–32 call it X); Up = 1 counts up (slide 33) | 0 or 1 |
| t_{pd} | flip-flop delay, clock edge → Q | 10 ns |
| t_{su} | setup time: how long before the edge a flip-flop's input must be steady (file 14) | 5 ns |

## Running example

**MTE 2025 Q8's counter: 3 bits, counting 0 → 7 → 0, negative-edge T flip-flops.** Steps 2–5 practise the procedure on its 2-bit version (00 → 11); steps 6–7 solve Q8 in full (T0 = 1, T1 = Q0, T2 = Q1Q0); step 8 runs the same table backwards; steps 9–12 change only the state table.

## The questions this file answers

- <span class="tag">MTE 2025 Q8 · 8 marks</span> Design a synchronous counter that counts clock pulses from 0-7 using negative edge triggered T flipflop.
- <span class="tag">Practice set 2 Q4</span> Design 2-bit synchronous up counter.
- <span class="tag">Practice set 2 Q5</span> Design 2-bit synchronous down counter using TFF.
- <span class="tag">Practice set 2 Q6</span> Design 3-bit synchronous down counter using DFF.
- <span class="tag">Deck 10 slides 26–37</span> Synchronous decade counter; up/down counters; 3-bit Gray-code counter with JK flip-flops.

---

## Build

### 1 · Why one shared clock

12 step 5 timed the ripple counter: each stage waits t_{pd} for the one before, so a 4-bit chain needs 4 t_{pd} to settle and shows false counts meanwhile.

:::guess Predict
Flip-flops with t_{pd} = 10 ns. A 4-bit ripple counter needs 4 × 10 = 40 ns per count. A synchronous counter clocks all four flip-flops together but needs an AND gate (5 ns) in front of some of them, and each input must be steady 5 ns before the edge. Which one can run faster?
:::

:::note Terms
**Synchronous (parallel) counter:** every flip-flop is clocked by the same clock pulse at the same time (deck 10 slide 18). **Flip-flop input logic:** the gates in front of each flip-flop; they look at the present count and set each input so that the flip-flop changes at the next edge only if its bit must change.
:::

[[fig:counter_T|A synchronous counter (the answer to step 7): one CLK line reaches every flip-flop; the AND gate decides when FF2 toggles. Nothing is clocked by another flip-flop's output.|w=82]]

At the edge, every flip-flop that must change starts at the same instant and finishes one t_{pd} later: **no stage waits for another**, so there are no false counts. Before the next edge the input logic must recompute the inputs from the new count, and the inputs must then be steady for t_{su}. One clock period must hold all three:

$$T_{min} = t_{pd} + t_{gate} + t_{su}$$

*flip-flop delay, then the gates' delay, then the setup margin.* Unlike the ripple's n · t_{pd}, this does not grow with the number of bits (only the gate in front can get wider). File 14 treats this timing in full.

**Answer to the Predict.** Synchronous: T_{min} = 10 + 5 + 5 = 20 ns, f_{max} = 1 / 20 ns = **50 MHz**. Ripple: 40 ns, f_{max} = **25 MHz**. The synchronous counter is twice as fast here and never shows a false count.

:::check Check 1
(a) Give two drawbacks of a ripple counter that a synchronous counter does not have. (b) What does the synchronous counter pay instead?
:::

### 2 · State diagram and state table

Step 1 said the input logic decides which flip-flops change. To design it, first write down what the counter must do, edge by edge.

:::q <span class="tag">Practice set 2 Q4</span>
Design 2-bit synchronous up counter.
:::

:::guess Guess first
Write the four counts of a 2-bit up counter in order. For each one, what must the next count be?
:::

:::note Terms
**State:** the stored count Q1 Q0. **State diagram:** one circle per state and one arrow per clock edge, from the present state to the next. **State table:** the same information as rows: present state → next state (deck 10 slide 19).
:::

[[fig:u3c_sd2|What this graph plots: each circle is a state Q1 Q0; each arrow is one clock edge, from the present state to the next state (deck 10 slide 19).|w=46]]

| Present Q1 Q0 | Next Q1⁺ Q0⁺ |
|---|---|
| 0 0 | 0 1 |
| 0 1 | 1 0 |
| 1 0 | 1 1 |
| 1 1 | 0 0 |

This table is the whole specification. The rest of the design answers one question per flip-flop and per row: **what must its input be so that Q becomes Q⁺?** The steps, for every counter in this file:

1. Flip-flops: the smallest n with 2^{n} ≥ number of states (12 step 7).
2. State diagram and state table.
3. For each flip-flop, its input in each row, from its excitation table (09 step 12).
4. A K-map per input, variables = the present state; unused states are don't-cares (02 step 7).
5. Circuit: one common clock; gates from step 4.
6. If any state is unused, check where it leads (step 10).

**Answer** (first half; steps 3–5 finish it). 4 states, so **2 flip-flops**; state diagram and table above.

:::check Check 2
(a) How many flip-flops does a counter with 6 states need? With 10? (b) Write the state table of a 2-bit down counter.
:::

### 3 · D flip-flops: the input is the next state

The state table gives Q⁺. A D flip-flop copies D at the edge: Q⁺ = D.

:::q <span class="tag">Practice set 2 Q4 · deck 10 slide 19</span>
Design 2-bit synchronous up counter (with D flip-flops).
:::

:::guess Guess first
If Q⁺ = D, what is the D1 column of the table, and what is the D0 column?
:::

:::note Terms
**Excitation (input) column:** for one flip-flop, the input value needed in each row of the state table. **For D:** D = Q⁺, row by row (09 step 12).
:::

| Q1 Q0 | Q1⁺ Q0⁺ | D1 | D0 |
|---|---|---|---|
| 0 0 | 0 1 | 0 | 1 |
| 0 1 | 1 0 | 1 | 0 |
| 1 0 | 1 1 | 1 | 1 |
| 1 1 | 0 0 | 0 | 0 |

1. D0 = 1, 0, 1, 0: it is 1 exactly when Q0 = 0, so **D0 = Q0'**.
2. D1 = 0, 1, 1, 0: 1 when Q1 and Q0 differ, the XOR pattern (01 step 8): **D1 = Q1 ⊕ Q0**.
3. Read back: Q0 flips every edge; Q1 takes "Q1 with a carry from Q0 added", which is how a 2-bit binary number counts.

**Answer.** **D0 = Q0', D1 = Q1 ⊕ Q0**: two D flip-flops on one clock, Q0' wired to D0, an XOR of Q1 and Q0 into D1.

:::check Check 3
Using D flip-flops, give D1 and D0 for the 2-bit down counter of Check 2(b).
:::

### 4 · T flip-flops: T = 1 where the bit changes

The same counter with T flip-flops needs a different column: T does not say what Q becomes, only whether it changes.

:::q <span class="tag">Deck 10 slides 20–21</span>
2-bit synchronous binary counter using TFF.
:::

:::guess Guess first
In each row, which bits change between Q and Q⁺? Those are the rows where that flip-flop's T must be 1.
:::

:::note Terms
**T excitation:** T = 1 when Q must change, T = 0 when it must stay: **T = Q ⊕ Q⁺** (09 step 12: 0→0: 0, 0→1: 1, 1→0: 1, 1→1: 0).
:::

| Q1 Q0 | Q1⁺ Q0⁺ | T1 | T0 |
|---|---|---|---|
| 0 0 | 0 1 | 0 | 1 |
| 0 1 | 1 0 | 1 | 1 |
| 1 0 | 1 1 | 0 | 1 |
| 1 1 | 0 0 | 1 | 1 |

1. Q0 changes in every row: **T0 = 1**.
2. Q1 changes in the rows where Q0 = 1: **T1 = Q0**.

Read it back: *the low bit always toggles; the next bit toggles when the bit below it is 1*, exactly the carry rule of binary counting.

**Answer.** **T0 = 1, T1 = Q0** (deck 10 slide 21): T0 tied high, Q0 wired straight to T1, one clock for both. No gate at all.

:::check Check 4
<span class="tag">Practice set 2 Q5</span> Design a 2-bit synchronous down counter using T flip-flops: T0 and T1.
:::

### 5 · JK flip-flops: the don't-cares help

A JK flip-flop has two inputs, and for every wanted change one of them does not matter.

:::q <span class="tag">Deck 10 slide 22</span>
2-bit synchronous binary counter using JK flip-flops.
:::

:::guess Guess first
To take Q from 0 to 1, J must be 1. Does K matter? To take Q from 1 to 1, which input must be 0?
:::

:::note Terms
**JK excitation** (09 step 12): 0→0: J K = 0 X · 0→1: 1 X · 1→0: X 1 · 1→1: X 0. Each row fixes one input and leaves the other free.
:::

| Q1 Q0 | Q1⁺ Q0⁺ | J1 K1 | J0 K0 |
|---|---|---|---|
| 0 0 | 0 1 | 0 X | 1 X |
| 0 1 | 1 0 | 1 X | X 1 |
| 1 0 | 1 1 | X 0 | 1 X |
| 1 1 | 0 0 | X 1 | X 1 |

1. J0 = 1, X, 1, X: set every X to 1 → **J0 = 1**. K0 = X, 1, X, 1 → **K0 = 1**.
2. J1 = 0, 1, X, X: 1 where Q0 = 1, with the X's chosen to match → **J1 = Q0**. K1 = X, X, 0, 1 → **K1 = Q0**.

J = K = the T answer of step 4. That is no accident: a JK with J = K behaves as a T flip-flop (09 step 10).

| Flip-flop | Input rule | 2-bit up counter |
|---|---|---|
| D | D = Q⁺ | D0 = Q0', D1 = Q1 ⊕ Q0 |
| T | T = Q ⊕ Q⁺ | T0 = 1, T1 = Q0 |
| JK | table above, X's free | J0 = K0 = 1, J1 = K1 = Q0 |

**Answer.** **J0 = K0 = 1, J1 = K1 = Q0.** The X's let the K-map choose, which is why JK designs tend to need the fewest gates.

:::check Check 5
Give the J and K needed to (a) keep Q at 1, (b) take Q from 1 to 0.
:::

### 6 · MTE Q8, part 1: the 3-bit table

Steps 3–5 designed 2 bits. MTE Q8 asks for 3, with T flip-flops.

:::q <span class="tag">MTE 2025 Q8 · 8 marks</span>
Design a synchronous counter that counts clock pulses from 0-7 using negative edge triggered T flipflop.
:::

:::guess Guess first
In 011 → 100 all three bits change. Look at the lower bits whenever Q2 must change: what are they?
:::

:::note Terms
**Next-state column:** the count plus 1, with 111 → 000. **T column:** present XOR next, bit by bit (step 4).
:::

| Present Q2 Q1 Q0 | Next Q2⁺ Q1⁺ Q0⁺ | T2 | T1 | T0 |
|---|---|---|---|---|
| 0 0 0 | 0 0 1 | 0 | 0 | 1 |
| 0 0 1 | 0 1 0 | 0 | 1 | 1 |
| 0 1 0 | 0 1 1 | 0 | 0 | 1 |
| 0 1 1 | 1 0 0 | 1 | 1 | 1 |
| 1 0 0 | 1 0 1 | 0 | 0 | 1 |
| 1 0 1 | 1 1 0 | 0 | 1 | 1 |
| 1 1 0 | 1 1 1 | 0 | 0 | 1 |
| 1 1 1 | 0 0 0 | 1 | 1 | 1 |

1. 8 states (0–7): 2^{3} = 8, so **3 flip-flops**, and every code is used.
2. T0 is 1 in all 8 rows; T1 in 4 rows (where Q0 = 1); T2 in 2 rows (where Q1 = Q0 = 1).
3. Pattern: **a bit toggles when every bit below it is 1**, the binary carry rule again.

**Answer to the Guess.** Every time Q2 must change (rows 011 and 111), **Q1 = Q0 = 1**.

:::check Check 6
Write the T columns' rows for 101 → 110 and 110 → 111, and say which flip-flops toggle in each.
:::

### 7 · MTE Q8, part 2: K-maps and the circuit

The T columns are three functions of Q2 Q1 Q0. Each goes on a 3-variable K-map (02 step 3).

:::guess Guess first
Without a map: T1 is 1 in the rows 1, 3, 5, 7. Which single variable is 1 in exactly those rows?
:::

:::note Terms
**K-map cell:** one present state (row Q2, column Q1 Q0 in Gray order 00, 01, 11, 10); a 1 means the flip-flop must toggle from that state. **Group:** a block of 1s that gives one product term (02 step 2).
:::

<div class="two">

[[fig:km_T1|What this graph plots: one cell per present state (row Q2, columns Q1 Q0); 1 = FF1 must toggle. The four 1s form the column pair Q0 = 1: T1 = Q0.]]

[[fig:km_T2|Same map for FF2: 1 only in states 011 and 111, a pair: T2 = Q1 Q0.]]

</div>

$$T0 = 1  ·  T1 = Q0  ·  T2 = Q1·Q0$$

**Circuit** (figure in step 1): three T flip-flops, each with a **bubble on its clock input** (negative-edge triggered, as Q8 asks); one CLK line to all three; T0 tied to 1; Q0 wired to T1; one 2-input AND of Q1 and Q0 into T2.

1. All 8 states are in the count, so step 6 of the procedure (unused states) has nothing to check.
2. The pattern extends: a 4-bit counter adds **T3 = Q2 Q1 Q0** (deck 10 slide 25), one more AND input per bit.
3. Over one cycle of 8 edges FF0 toggles 8 times, FF1 4 times, FF2 2 times: Q1 runs at f_{CLK}/4, Q2 at f_{CLK}/8, the same divider as 12 step 3 but with all changes on the same edge.

**Answer (MTE Q8, 8 marks).** (i) 3 flip-flops; (ii) state table and T columns as in step 6; (iii) K-maps above; (iv) **T0 = 1, T1 = Q0, T2 = Q1 Q0**; (v) circuit: negative-edge T flip-flops, common clock, one AND gate.

:::check Check 7
(a) Design a 3-bit synchronous up counter with JK flip-flops: J and K of each stage. (b) Write T3 for a 4-bit counter.
:::

### 8 · Down counters

Steps 6–7 counted up. Counting down only changes the next-state column; the procedure is the same.

:::q <span class="tag">Practice set 2 Q6</span>
Design 3-bit synchronous down counter using DFF.
:::

:::guess Guess first
Counting down, a bit must change when every bit below it is 0 (the borrow rule). With D flip-flops, though, you need the next state, not the change. What is D0?
:::

:::note Terms
**Down count:** next = present − 1, with 000 → 111. **Borrow:** a bit changes when all lower bits are 0 (12 step 4).
:::

| Present Q2 Q1 Q0 | Next = D2 D1 D0 |
|---|---|
| 0 0 0 | 1 1 1 |
| 0 0 1 | 0 0 0 |
| 0 1 0 | 0 0 1 |
| 0 1 1 | 0 1 0 |
| 1 0 0 | 0 1 1 |
| 1 0 1 | 1 0 0 |
| 1 1 0 | 1 0 1 |
| 1 1 1 | 1 1 0 |

<div class="two">

[[fig:km_D1_down|What this graph plots: one cell per present state; 1 = D1 must be 1 (next Q1 = 1). Two pairs: Q1'Q0' and Q1Q0.]]

[[fig:km_D2_down|Same for D2: pairs Q2Q1 and Q2Q0, and the lone 1 at 000 (the wrap 000 → 111): Q2'Q1'Q0'.]]

</div>

1. D0 column = 1, 0, 1, 0, …: **D0 = Q0'** (no map needed).
2. D1 ones at 000, 011, 100, 111: **D1 = Q1'Q0' + Q1Q0** (= Q1 XNOR Q0).
3. D2 ones at 000, 101, 110, 111: **D2 = Q2Q1 + Q2Q0 + Q2'Q1'Q0'**.

With T flip-flops the same counter is shorter, because the borrow rule is the T rule: T0 = 1, **T1 = Q0'**, **T2 = Q1'Q0'**.

**Answer.** Three D flip-flops on one clock with **D0 = Q0', D1 = Q1'Q0' + Q1Q0, D2 = Q2Q1 + Q2Q0 + Q2'Q1'Q0'**; it counts 0, 7, 6, … 1, 0.

:::check Check 8
<span class="tag">Practice set 2 Q5</span> Write the T-column table of the 2-bit down counter and confirm T1 = Q0', T0 = 1.
:::

### 9 · MOD-N: the synchronous decade counter

A count of fewer than 2^{n} states leaves some codes unused. They never occur in the count, so their inputs can be anything.

:::q <span class="tag">Deck 10 slides 26–27 (EX 10.26–10.27)</span>
Synchronous decade/BCD counter (T flip-flops).
:::

:::guess Guess first
A decade counter uses 0000 – 1001. Which six codes are unused, and what goes in their K-map cells?
:::

:::note Terms
**Unused states:** codes the count never visits (1010 – 1111 here). **Don't-care cells:** their cells in every K-map are X, so groups may include them (02 step 7).
:::

| Present Q3 Q2 Q1 Q0 | Next | T3 | T2 | T1 | T0 |
|---|---|---|---|---|---|
| 0000 (0) | 0001 | 0 | 0 | 0 | 1 |
| 0001 (1) | 0010 | 0 | 0 | 1 | 1 |
| 0010 (2) | 0011 | 0 | 0 | 0 | 1 |
| 0011 (3) | 0100 | 0 | 1 | 1 | 1 |
| 0100 (4) | 0101 | 0 | 0 | 0 | 1 |
| 0101 (5) | 0110 | 0 | 0 | 1 | 1 |
| 0110 (6) | 0111 | 0 | 0 | 0 | 1 |
| 0111 (7) | 1000 | 1 | 1 | 1 | 1 |
| 1000 (8) | 1001 | 0 | 0 | 0 | 1 |
| 1001 (9) | 0000 | 1 | 0 | 0 | 1 |
| 1010 – 1111 | — | X | X | X | X |

1. **T0 = 1** (every row).
2. T1 is 1 in rows 1, 3, 5, 7 but **not 9**: Q0 = 1 and Q3 = 0. With 11, 13, 15 as X: **T1 = Q3'Q0**.
3. T2 is 1 in rows 3, 7: **T2 = Q1Q0** (the X at 11 and 15 allow the pair).
4. T3 is 1 in rows 7 and 9. Row 9 groups with the X's 11, 13, 15 into **Q3Q0**; row 7 groups with X 15 into **Q2Q1Q0**: **T3 = Q2Q1Q0 + Q3Q0**.

Compare the binary 4-bit counter (T1 = Q0, T3 = Q2Q1Q0): the extra Q3' in T1 stops Q1 at 1001 → 0000, and the extra Q3Q0 in T3 resets Q3 there.

**Answer.** **T0 = 1, T1 = Q3'Q0, T2 = Q1Q0, T3 = Q2Q1Q0 + Q3Q0** (deck 10 slides 26–27). Unlike 12 step 7, no clear pulse and no momentary 1010: 1001 goes straight to 0000 on one edge.

:::check Check 9
Why is T1 = Q0 (the binary answer) wrong for the decade counter? Name the row where it fails and what it would do there.
:::

### 10 · Unused states and self-starting

Step 9 let the K-maps fill the unused cells with whatever made the groups largest. At power-up a counter can wake in any code, including an unused one.

:::guess Predict
The decade counter of step 9 wakes up at 1010. Apply T0 = 1, T1 = Q3'Q0, T2 = Q1Q0, T3 = Q2Q1Q0 + Q3Q0. Where does it go, and does it ever reach the count?
:::

:::note Terms
**Self-starting:** every unused state leads into the main count within a few clocks. **Lock-out:** an unused state (or a loop of them) that never leads into the count; the counter is stuck there for ever.
:::

[[fig:u3c_sd_decade|What this graph plots: each circle is a state Q3 Q2 Q1 Q0, each arrow one clock edge. Solid ring: the count 0000 – 1001. Dashed: the six unused states and where the equations send them.|w=70]]

Apply the equations to each unused state (T = 1 flips that bit):

| From | T3 T2 T1 T0 | To |
|---|---|---|
| 1010 (10) | 0 0 0 1 | 1011 (11) |
| 1011 (11) | 1 1 0 1 | 0110 (6) |
| 1100 (12) | 0 0 0 1 | 1101 (13) |
| 1101 (13) | 1 0 0 1 | 0100 (4) |
| 1110 (14) | 0 0 0 1 | 1111 (15) |
| 1111 (15) | 1 1 0 1 | 0010 (2) |

Every unused state reaches the count within two clocks: the counter is **self-starting**. Had one led into a loop of unused states (lock-out), the fix is to choose that state's next state yourself (for example, send it to 0000), replace its X's with the matching inputs, and redo the K-maps.

**Answer to the Predict.** **1010 → 1011 → 0110 (6)**: two clocks, then it counts normally.

:::check Check 10
A MOD-6 synchronous counter (0–5) with JK flip-flops has J2 = Q1Q0, K2 = Q0, J1 = Q2'Q0, K1 = Q0, J0 = K0 = 1. Where do 110 and 111 go? Is it self-starting?
:::

### 11 · Up/down counters

So far the state table had one next state per row. An up/down counter has a direction input, and the input becomes one more K-map variable.

:::q <span class="tag">Deck 10 slides 29–32</span>
2-bit Up/Down counter: counter outputs 00, 01, 10, 11; a single input X (pack: Dn): Dn = 0 the counter counts up; Dn = 1 the counter counts down. Use D flip-flops.
:::

:::guess Guess first
D0 for both directions: does Q0 flip every clock whether counting up or down?
:::

:::note Terms
**Up/down (bidirectional) counter:** a counter with a control input that sets the direction (deck 10 slide 28). **Dn:** the direction input; Dn = 0 up, Dn = 1 down (the deck calls it X).
:::

| Dn | Q1 Q0 | Q1⁺ Q0⁺ = D1 D0 |
|---|---|---|
| 0 | 00 | 01 |
| 0 | 01 | 10 |
| 0 | 10 | 11 |
| 0 | 11 | 00 |
| 1 | 00 | 11 |
| 1 | 01 | 00 |
| 1 | 10 | 01 |
| 1 | 11 | 10 |

1. D0 = 1 whenever Q0 = 0, in both halves: **D0 = Q0'** (deck 10 slide 31 asks why: the low bit alternates in either direction).
2. D1 on a 3-variable map (Dn, Q1, Q0) is a checkerboard: 1 when an odd number of Dn, Q1, Q0 are 1: **D1 = Q1 ⊕ Q0 ⊕ Dn**.
3. Read back: Dn = 0 gives D1 = Q1 ⊕ Q0 (step 3's up counter); Dn = 1 inverts it, giving Q1 XNOR Q0 (step 8's down counter).

With T flip-flops and an Up input (Up = 1 counts up; deck 10 slide 33), the carry rule and the borrow rule are joined by OR: **T0 = 1, T1 = Q0·Up + Q0'·Up', T2 = Q0Q1·Up + Q0'Q1'·Up'**.

**Answer.** **D0 = Q0', D1 = Q1 ⊕ Q0 ⊕ Dn** (deck 10 slides 31–32): a 3-input XOR into D1, Q0' into D0, one clock.

:::check Check 11
In the 3-bit T up/down counter, Up = 0 and the count is 100. Find T2, T1, T0 and the next count.
:::

### 12 · Any sequence: the Gray-code counter

Nothing in the procedure needs the states to be in binary order. The state table can list any order.

:::q <span class="tag">Deck 10 slides 35–37 (EX 10.35–10.37)</span>
A 3-bit Gray code counter (using JK flip-flops): 000, 001, 011, 010, 110, 111, 101, 100.
:::

:::guess Guess first
In a Gray sequence only one bit changes per step. How many flip-flops change at each clock edge?
:::

:::note Terms
**Gray code:** an order of the codes in which neighbours differ in exactly one bit (01 step 1's code table). **Any-sequence counter:** the state table lists the wanted order; everything after it is the usual procedure (deck 10 slide 34).
:::

[[fig:u3c_sd_gray|What this graph plots: each circle is a state Q2 Q1 Q0, each arrow one clock edge (deck 10 slide 35). Exactly one bit differs across every arrow.|w=52]]

Rows in Gray order, JK inputs from 09 step 12 (only FF0 shown; FF1 and FF2 the same way):

| Q2 Q1 Q0 | Next | J0 K0 |
|---|---|---|
| 000 | 001 | 1 X |
| 001 | 011 | X 0 |
| 011 | 010 | X 1 |
| 010 | 110 | 0 X |
| 110 | 111 | 1 X |
| 111 | 101 | X 0 |
| 101 | 100 | X 1 |
| 100 | 000 | 0 X |

<div class="two">

[[fig:km_J0_gray|What this graph plots: one cell per present state; 1 = J0 must be 1, X = free (Q0 already 1). Pairs Q2'Q1' and Q2Q1.]]

[[fig:km_K0_gray|K0: 1 = FF0 must reset, X = free (Q0 = 0). Pairs Q2'Q1 and Q2Q1'.]]

</div>

$$J0 = Q2Q1 + Q2'Q1' = (Q2 ⊕ Q1)'  ·  K0 = Q2'Q1 + Q2Q1' = Q2 ⊕ Q1$$

$$J1 = Q2'Q0,  K1 = Q2Q0  ·  J2 = Q1Q0',  K2 = Q1'Q0'$$

:::note Slip in deck 10 slide 36 (as transcribed)
Slide 36's maps read J1 = Q2'Q0' and K1 = Q2Q0'. FF1 must set only in state 001 (→ 011) and reset only in 111 (→ 101), both with Q0 = 1, so the correct terms are **J1 = Q2'Q0, K1 = Q2Q0**, as slide 37's circuit has them. `uncertain`: the slide image was not re-viewed this session; the pack uses slide 37's equations, which verify.py checks by simulating the counter.
:::

**Answer.** The six equations above (deck 10 slide 37). Simulated from 000 the counter goes 001, 011, 010, 110, 111, 101, 100, 000, with **exactly one flip-flop toggling per clock**, so a decoder on the outputs never sees two bits changing at once.

:::check Check 12
The Gray counter is at 110. Use the equations to find which flip-flop changes at the next edge.
:::

---

## Exam form

**Design procedure (write it as numbered steps; MTE Q8 gives marks for each).**
1. Flip-flops: smallest n with 2^{n} ≥ number of states.
2. State diagram and state table (present → next).
3. Excitation columns from the flip-flop's table: D = Q⁺ · T = Q ⊕ Q⁺ · JK: 0→0 0X, 0→1 1X, 1→0 X1, 1→1 X0.
4. One K-map per input; unused states = X.
5. Circuit: one common clock to every flip-flop (bubble if negative-edge), gates from step 4.
6. Unused states: apply the equations; show each reaches the count (self-starting).

**Results to remember.**
- Binary up (T): T0 = 1, T1 = Q0, T2 = Q1Q0, T3 = Q2Q1Q0. JK: J = K = the same.
- Binary down (T): T0 = 1, T1 = Q0', T2 = Q1'Q0'. Down (D, 3-bit): D0 = Q0', D1 = Q1'Q0' + Q1Q0, D2 = Q2Q1 + Q2Q0 + Q2'Q1'Q0'.
- 2-bit up (D): D0 = Q0', D1 = Q1 ⊕ Q0. Up/down (D): D1 = Q1 ⊕ Q0 ⊕ Dn.
- Decade (T): T0 = 1, T1 = Q3'Q0, T2 = Q1Q0, T3 = Q2Q1Q0 + Q3Q0.

**Ripple vs synchronous.** Clock to FF0 only vs to all · settling n · t_{pd} vs t_{pd} + t_{gate} · false states vs none · no gates vs input logic · binary (or reset) counts only vs any sequence.

## Traps

- Copying the next-state column into the T column: T = Q ⊕ Q⁺, not Q⁺.
- Filling unused-state cells with 0 instead of X: larger, wrong-looking equations.
- Skipping the self-start check for a MOD-N counter.
- Clocking one flip-flop from another's output in a "synchronous" design: that is a ripple counter.
- Leaving out the clock bubbles when the question says negative edge.
- K-map columns in the order 00, 01, 10, 11 instead of 00, 01, 11, 10.

## Self-test

1. Write the six steps of the design procedure from memory.
2. Design a 3-bit synchronous down counter with T flip-flops.
3. A synchronous counter: t_{pd} = 10 ns, one AND gate of 5 ns, setup time 5 ns. f_{max}?
4. Design a MOD-6 synchronous up counter (0–5) with JK flip-flops and check it is self-starting.
5. Write D1 and D0 for a 2-bit up/down counter with D flip-flops (Dn = 1 down).
6. In the decade counter, why does T3 contain the term Q3Q0?
7. Give three differences between ripple and synchronous counters.

<!--ANSWERS-->

## Answers

**Check 1.** (a) Settling time grows with the number of bits (n · t_{pd}), and the outputs pass through false counts that a decoder can catch. (b) Gates in front of the flip-flops (the input logic), and a design procedure to find them.

**Check 2.** (a) 6 states: 2^{3} = 8 ≥ 6, **3**; 10 states: **4**. (b) 00 → 11, 01 → 00, 10 → 01, 11 → 10.

**Check 3.** D = next: D0 = 1, 0, 1, 0 → **D0 = Q0'**; D1 = 1, 0, 0, 1 → **D1 = Q1'Q0' + Q1Q0** (Q1 XNOR Q0).

**Check 4.** Down: 00 → 11 (both change), 01 → 00 (Q0), 10 → 01 (both), 11 → 10 (Q0). **T0 = 1**, T1 = 1 in rows 00 and 10, where Q0 = 0: **T1 = Q0'**.

**Check 5.** (a) **J K = X 0**. (b) **J K = X 1**.

**Check 6.** 101 → 110: T2 T1 T0 = **0 1 1**: FF1 and FF0 toggle. 110 → 111: **0 0 1**: FF0 only.

**Check 7.** (a) **J0 = K0 = 1, J1 = K1 = Q0, J2 = K2 = Q1Q0**. (b) **T3 = Q2Q1Q0**.

**Check 8.** 00 → 11: T1 T0 = 1 1; 01 → 00: 0 1; 10 → 01: 1 1; 11 → 10: 0 1. T0 = 1 everywhere; T1 = 1 where Q0 = 0: **T1 = Q0'** ✓.

**Check 9.** It fails in row **1001**: Q0 = 1, so T1 = Q0 = 1 would toggle Q1 to 1, and the next state could not be 0000. The decade count needs Q1 to stay 0 on 1001 → 0000; the factor Q3' makes T1 = 0 there.

**Check 10.** From **110**: Q0 = 0, so J2 = K2 = 0 and J1 = K1 = 0 (hold); J0 = K0 = 1 toggles FF0 → **111**. From **111**: K2 = 1, J2 = 1 → FF2 toggles to 0; J1 = 0, K1 = 1 → FF1 resets; FF0 toggles to 0 → **000**. Both reach the count: **self-starting**.

**Check 11.** Up = 0, Q2 Q1 Q0 = 1 0 0: T0 = 1; T1 = Q0·Up + Q0'·Up' = 0 + 1 = **1**; T2 = Q0Q1·Up + Q0'Q1'·Up' = 0 + 1 = **1**. All three toggle: **011** (4 → 3, counting down).

**Check 12.** Q2 Q1 Q0 = 1 1 0. J0 = (1 ⊕ 1)' = 1, K0 = 0 → FF0 sets to 1. J1 = Q2'Q0 = 0, K1 = Q2Q0 = 0 → FF1 holds. J2 = Q1Q0' = 1, K2 = 0 → FF2 stays 1. Only **FF0** changes: 110 → **111**.

**Self-test.**

1. Flip-flops → state table → excitation columns → K-maps (unused = X) → circuit with one clock → self-start check.
2. **T0 = 1, T1 = Q0', T2 = Q1'Q0'**; one clock; counts 0, 7, 6, … 1, 0.
3. 10 + 5 + 5 = 20 ns, **f_{max} = 50 MHz**.
4. 3 flip-flops; 110, 111 = X. **J0 = K0 = 1, J1 = Q2'Q0, K1 = Q0, J2 = Q1Q0, K2 = Q0.** Unused: 110 → 111 → 000: self-starting (Check 10).

[[fig:u3c_sd_mod6|What this graph plots: each circle is a state Q2 Q1 Q0, each arrow one clock edge. Solid: the MOD-6 count; dashed: the unused states 110 → 111 → 000.|w=46]]

5. **D0 = Q0', D1 = Q1 ⊕ Q0 ⊕ Dn.**
6. At 1001 Q3 must return to 0, so T3 must be 1 there; Q2Q1Q0 is 0 at 1001, so the extra term **Q3Q0** (1 at 1001, X at 1011, 1101, 1111) supplies it.
7. Clock to one flip-flop vs to all; settling n · t_{pd} vs t_{pd} + t_{gate}; false states vs none; no gates vs input logic; binary only vs any sequence (any three).

<!--/ANSWERS-->
