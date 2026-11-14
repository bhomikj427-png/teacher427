# 13 — Designing synchronous counters

<div class="sub">Deck 10 slides 18–37 · practice set 2 Q4–Q6 · 2025 mid-term Q8 (8 marks) · syllabus Unit 3 · needs 09 (flip-flops, excitation tables) and 12 (ripple counters)</div>

## Map

[[map:1 Why synchronous > 2 State table and excitation > 3 K-maps and circuit > 4 Other flip-flop types > 5 MOD-N, unused states > 6 Any sequence|here=1]]

12 built a counter by letting each flip-flop clock the next. This file gives every flip-flop the same clock and lets gates decide which ones change. The method is the same one 15 uses for every state machine.

## The questions this file answers

- <span class="tag">MTE 2025 Q8 · 8 marks</span> Design a synchronous counter that counts clock pulses from 0–7 using negative edge triggered T flip-flops.
- <span class="tag">Set 2 Q4</span> Design 2-bit synchronous up counter.
- <span class="tag">Set 2 Q5, Q6</span> 2-bit synchronous down counter using TFF; 3-bit synchronous down counter using DFF.
- <span class="tag">Deck 10 slides 34–37</span> MOD counters and a Gray-code counter with JK flip-flops.

---

## Build

### 1 · Why synchronous

:::guess Predict
A 3-bit ripple counter goes from 011 to 100. All three bits must change. Do they change at the same instant?
:::

[[fig:ripple_waves|A ripple counter (12): after the 4th edge the outputs pass through 010 and 000 before settling at 100 (shaded).]]

In a ripple counter each flip-flop waits for the one before it, so the outputs settle one flip-flop delay t_{pd} after another. For n bits the worst wait is **n·t_{pd}**, and anything reading the outputs sees false counts on the way.

:::note Terms
**Synchronous counter:** every flip-flop gets the same clock, so all outputs change together, one t_{pd} after the edge. **Flip-flop input logic:** the gates in front of each flip-flop that decide whether it changes at the next edge.
:::

**Answer.** No. Q0 changes first, then Q1, then Q2, so the counter briefly shows 010 and 000. A synchronous counter changes all three together.

:::check Check 1
(a) A 4-bit ripple counter uses flip-flops with t_{pd} = 25 ns. Find its worst settling time and its highest usable clock frequency. (b) Why can a decoder on a ripple counter's outputs give false pulses?
:::

### 2 · State table and excitation

All flip-flops now share the clock, so each one needs its own input logic. The design finds that logic from a table.

:::q <span class="tag">MTE 2025 Q8 · 8 marks</span>
Design a synchronous counter that counts clock pulses from 0–7 using negative edge triggered T flip-flops.
:::

:::guess Guess first
In the count 011 → 100 all three bits change. What do the lower bits look like every time the top bit has to change?
:::

**The design procedure** (the same for every counter, and for every state machine in 15):

1. Number of flip-flops: the smallest n with 2^{n} ≥ number of states.
2. State table: each present state and the next state.
3. For each flip-flop, write its inputs from the excitation table (09), row by row.
4. K-map each input as a function of the present state. Unused states are don't-cares.
5. Draw the circuit: one common clock, gates from step 4.
6. If there are unused states, check that each one leads back into the count.

A T flip-flop toggles when T = 1 and holds when T = 0, so its excitation is simple: **T = 1 exactly where the bit changes.**

| present Q2 Q1 Q0 | next Q2 Q1 Q0 | T2 T1 T0 |
|---|---|---|
| 0 0 0 | 0 0 1 | 0 0 1 |
| 0 0 1 | 0 1 0 | 0 1 1 |
| 0 1 0 | 0 1 1 | 0 0 1 |
| 0 1 1 | 1 0 0 | 1 1 1 |
| 1 0 0 | 1 0 1 | 0 0 1 |
| 1 0 1 | 1 1 0 | 0 1 1 |
| 1 1 0 | 1 1 1 | 0 0 1 |
| 1 1 1 | 0 0 0 | 1 1 1 |

8 states, so 3 flip-flops. Each T column is the next state XOR the present state.

:::check Check 2
(a) Give the T, D and JK inputs that take a flip-flop from Q = 1 to Q = 0. (b) How many flip-flops does a MOD-10 counter need?
:::

### 3 · K-maps and the circuit

The T columns are three functions of Q2 Q1 Q0. Each one goes on a K-map.

:::guess Guess first
Before drawing a map, read the table: when is T1 equal to 1? When is T2?
:::

<div class="two">

[[fig:km_T1|T1 is 1 in every row with Q0 = 1.]]

[[fig:km_T2|T2 is 1 only when Q1 = Q0 = 1.]]

</div>

T0 is 1 in every row, so it needs no map.

$$T0 = 1    T1 = Q0    T2 = Q1·Q0$$

[[fig:counter_T|The finished counter. The bubble on each clock input marks negative-edge triggering.]]

**Answer.** State table and T columns as in step 2; K-maps above; **T0 = 1, T1 = Q0, T2 = Q1·Q0**, one 2-input AND gate, one shared negative-edge clock. All 8 states are used, so there are no unused states to check. The pattern continues: each bit toggles when every lower bit is 1 (a 4-bit counter adds T3 = Q2Q1Q0).

:::check Check 3
<span class="tag">Set 2 Q5</span> Design a 2-bit synchronous down counter using T flip-flops.
:::

### 4 · Other flip-flop types

The procedure does not change with the flip-flop. Only step 3's excitation table does.

:::q <span class="tag">Set 2 Q4</span>
Design 2-bit synchronous up counter. (Use JK flip-flops, then repeat with D.)
:::

:::guess Guess first
A JK flip-flop with J = K = 1 toggles. What does that make J and K equal to, if you already know the T answer?
:::

| Flip-flop | Excitation rule | 2-bit up counter |
|---|---|---|
| **T** | T = 1 where the bit changes | T0 = 1, T1 = Q0 |
| **JK** | 0→0: 0X · 0→1: 1X · 1→0: X1 · 1→1: X0 | J0 = K0 = 1, J1 = K1 = Q0 |
| **D** | D = the next state | D0 = Q0', D1 = Q1 ⊕ Q0 |

**Answer.** States 00 → 01 → 10 → 11 → 00. JK excitation (J1 K1, J0 K0) per row: 00: 0X, 1X · 01: 1X, X1 · 10: X0, 1X · 11: X1, X1. The K-maps give **J0 = K0 = 1, J1 = K1 = Q0**. With D: **D0 = Q0', D1 = Q1 ⊕ Q0**. The X's in the JK table are why JK designs need the fewest gates; D designs need the most.

:::check Check 4
<span class="tag">Set 2 Q6</span> Design a 3-bit synchronous down counter using D flip-flops.
:::

### 5 · MOD-N counters and unused states

A counter with fewer than 2^{n} states leaves some codes unused. The design treats them as don't-cares, which leaves one question open.

:::q <span class="tag">Deck 10 slide 34</span>
Design a MOD-6 synchronous up counter (0 to 5) using JK flip-flops, and check whether it is self-starting.
:::

:::guess Guess first
The counter never visits 110 or 111. What happens if it powers up in one of them?
:::

3 flip-flops; states 6 and 7 are don't-cares in every K-map. The procedure gives:

$$J0 = K0 = 1    J1 = Q2'Q0,  K1 = Q0    J2 = Q1Q0,  K2 = Q0$$

**Self-starting** means every unused state leads back into the count. Check each one with the equations:

- From **110**: Q0 = 0, so J1 = K1 = 0 and J2 = K2 = 0; only FF0 toggles → **111**.
- From **111**: FF0 toggles to 0; J1 = 0, K1 = 1 resets FF1; J2 = K2 = 1 toggles FF2 to 0 → **000**.

**Answer.** Equations above. Both unused states return to the count (110 → 111 → 000), so the counter **is self-starting**. If one had led to a loop outside the count (a **lock-out**), the fix is to choose different values for that state's don't-cares and redo its K-maps.

:::check Check 5
Why must the unused states be checked in a MOD-6 counter but not in the 0–7 counter of steps 2–3?
:::

### 6 · Any sequence

Nothing in the procedure requires counting in binary. The state table can list any order.

:::q <span class="tag">Deck 10 slides 35–37</span>
Design a 3-bit Gray-code counter using JK flip-flops. (Sequence 000, 001, 011, 010, 110, 111, 101, 100.)
:::

:::guess Guess first
In a Gray sequence only one bit changes per step. How many flip-flops toggle at each clock?
:::

Same six steps, with the Gray order in the state table and the JK excitation table:

$$J2 = Q1Q0',  K2 = Q1'Q0'    J1 = Q2'Q0,  K1 = Q2Q0$$

$$J0 = (Q2 ⊕ Q1)',  K0 = Q2 ⊕ Q1$$

**Answer.** The equations above (deck 10 slide 36). Exactly one flip-flop toggles per clock, so a decoder on the outputs never sees two bits changing at once. The same method gives up/down counters: add the direction input X as one more K-map variable, e.g. a 2-bit up/down counter with D flip-flops has D0 = Q0', D1 = Q1 ⊕ Q0 ⊕ X (X = 0 up, X = 1 down; deck 10 slide 31).

:::check Check 6
In the Gray counter, which flip-flop toggles when the count goes from 110 to 111? Check it with the equations.
:::

---

## Exam form

**Procedure (write it as numbered steps).** 1. Flip-flops: smallest n with 2^{n} ≥ states. 2. State table. 3. Excitation for each flip-flop. 4. K-map each input (unused states = X). 5. Circuit with one common clock. 6. Self-start check of unused states.

**Excitation tables.** T: 1 where the bit changes. JK: 0→0 0X, 0→1 1X, 1→0 X1, 1→1 X0. D: the next state. SR: 0→0 0X, 0→1 10, 1→0 01, 1→1 X0.

**Results to remember.** 3-bit up (T): T0 = 1, T1 = Q0, T2 = Q1Q0. 3-bit up (JK): J = K = the same as T. 3-bit down (T): T0 = 1, T1 = Q0', T2 = Q1'Q0'. Decade (T): T0 = 1, T1 = Q3'Q0, T2 = Q1Q0, T3 = Q2Q1Q0 + Q3Q0.

**Ripple vs synchronous.** Clock to first flip-flop only vs to all · delay n·t_{pd} vs one t_{pd} · false states vs none · simplest vs extra gates · binary only vs any sequence.

## Traps

- Writing the next-state column in the T column: T is next XOR present, not the next state.
- Forgetting that unused states are don't-cares, which gives larger, wrong-looking equations.
- Skipping the self-start check for a MOD-N counter.
- Clocking the flip-flops from each other: that is a ripple counter, not a synchronous one.
- Drawing a positive-edge clock when the question says negative edge: put the bubble on every clock input.
- Reading a K-map row order as 00, 01, 10, 11: it is 00, 01, 11, 10.

## Self-test

1. Write the six steps of the design procedure from memory.
2. Design a 3-bit synchronous up counter with JK flip-flops.
3. Design a 3-bit synchronous down counter with T flip-flops.
4. A synchronous counter has t_{pd} = 10 ns, one 5 ns AND gate between flip-flops and setup time 5 ns. Find f_{max}.
5. Write D1 for a 2-bit up/down counter (X = 0 up, X = 1 down) using D flip-flops.
6. Give three differences between ripple and synchronous counters.

<!--ANSWERS-->

## Answers

**Check 1.** (a) 4 × 25 = **100 ns**; f_{max} = 1/100 ns = **10 MHz**. (b) While the ripple settles, the outputs pass through false codes for a few nanoseconds; a decoder reads them as real counts.

**Check 2.** (a) T = 1; D = 0; J K = X 1. (b) 2^{3} = 8 &lt; 10 ≤ 16, so **4**.

**Check 3.** States 11 → 10 → 01 → 00 → 11. Q0 changes every time: **T0 = 1**. Q1 changes when Q0 = 0: **T1 = Q0'**.

**Check 4.** D = next state. **D0 = Q0'**, **D1 = Q1'Q0' + Q1Q0** (= Q1 ⊙ Q0), **D2 = Q2Q1 + Q2Q0 + Q2'Q1'Q0'**.

**Check 5.** The MOD-6 counter has two unused states (6, 7) whose don't-cares were chosen by the K-maps, so where they lead is not known until checked. The 0–7 counter uses all 8 states.

**Check 6.** Present 110: Q2 = 1, Q1 = 1, Q0 = 0. J0 = (1 ⊕ 1)' = 1 and K0 = 0, so FF0 sets to 1; J1 = 0, K1 = 0 holds FF1; J2 = Q1Q0' = 1, K2 = 0 holds FF2 at 1. Only **FF0** changes: 110 → 111 ✓.

**Self-test.**

1. Flip-flops → state table → excitation → K-maps (unused = X) → circuit with one clock → self-start check.
2. **J0 = K0 = 1, J1 = K1 = Q0, J2 = K2 = Q1Q0.**
3. **T0 = 1, T1 = Q0', T2 = Q1'Q0'.**
4. T = 10 + 5 + 5 = 20 ns, so **f_{max} = 50 MHz**.
5. **D1 = Q1 ⊕ Q0 ⊕ X** (D0 = Q0').
6. Clock to one flip-flop vs to all; delay n·t_{pd} vs one t_{pd}; false states vs none; binary only vs any sequence; fewer gates vs extra gates (any three).

<!--/ANSWERS-->
