# 10 — Drawing flip-flop waveforms

<div class="sub">Mid-term 2025 Q7 (4 marks; its waveform is missing from our copy, so the question below is a practice one in the same form) · practice set 2 Q2–Q3 · syllabus Unit 3 · needs 09 (characteristic tables)</div>

## Map

[[map:1 The edge-by-edge procedure > 2 T, D and asynchronous inputs|here=1]]

A 4-mark question with one method. Mark the edges, read the inputs just before each, apply the table, hold flat between edges.

## The questions this file answers

- <span class="tag">MTE 2025 Q7 form · 4 marks</span> Draw Q for a positive-edge JK flip-flop, Q initially 0.
- <span class="tag">Set 2 Q2–Q3</span> The same for T and D flip-flops, and for negative edges.

---

## Build

### 1 · The edge-by-edge procedure

:::q <span class="tag">MTE 2025 Q7 form · practice waveform</span>
Draw the output waveform for the following input waveform, assuming the flip-flop (JK) to be positive edge triggered and the output Q is initially at logic zero.
:::

[[fig:jk_wave_noq|Clock, J and K.|w=75]]

:::guess Guess first
At how many instants can Q change in this picture?
:::

1. Mark every **active edge** with a dotted line (rising for positive-edge, falling for negative).
2. Start Q at the given value.
3. At each edge read the inputs **just before** it and apply the characteristic table (09).
4. **Between edges Q is flat**, whatever the inputs do.
5. PRESET or CLEAR override at once, mid-cycle if necessary.

| Rising edge | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| J K before | 1 0 | 0 1 | 1 1 | 1 0 | 0 1 | 0 0 |
| Action | set | reset | toggle | set | reset | hold |
| Q after | 1 | 0 | 1 | 1 | 0 | 0 |

[[fig:jk_wave|The answer: Q changes only at the six rising edges.|w=75]]

**Answer.** Six instants at most (the six rising edges); Q = 1, 0, 1, 1, 0, 0 after them. Write the edge table beside the drawing in the exam: it shows the method even if a line is slightly off.

:::check Check 1
Redo the question for a **negative**-edge JK: give Q after each of the six falling edges.
:::

### 2 · T, D, and asynchronous inputs

:::guess Predict
A T flip-flop holds T = 1 for three edges in a row. What does Q look like?
:::

[[fig:t_wave|T flip-flop waveform: Q toggles at each active edge where T = 1.|w=75]]

- **T:** toggle where T = 1, hold where T = 0. With T = 1 throughout, Q is the clock divided by 2.
- **D:** Q after each edge is D just before it. Between edges, D can wiggle freely.
- **D latch** (not flip-flop): Q follows D for the whole time EN = 1; draw it transparent, not edge-sampled.
- **CLEAR/PRESET:** draw Q jumping the moment they go active, and staying forced while they are active.

**Answer.** A square wave: Q toggles at each of the three edges.

:::check Check 2
A negative-edge T flip-flop starts at Q = 0. At six falling edges T is 1, 0, 0, 1, 1, 0. Q after each edge?
:::

---

## Exam form

Mark edges → table of inputs just before each edge → action → Q after → draw Q flat between edges. State edge type and initial Q.

## Traps

- Reading the inputs after the edge instead of before.
- Letting Q change between edges for a flip-flop (only a latch does).
- Using rising edges for a bubble (negative-edge) clock.
- Ignoring an asynchronous CLEAR that is active mid-cycle.

## Self-test

1. Positive-edge D flip-flop: D just before four edges is 1, 0, 0, 1. Q after each?
2. Negative-edge T flip-flop, Q starts at 1, T = 1, 1, 0, 1. Q after each edge?
3. Positive-edge SR flip-flop, Q = 0, SR before edges = 10, 00, 01, 00. Q after each?
4. How does a D latch's waveform differ from a D flip-flop's for the same D and clock?
5. A JK flip-flop with J = K = 1 is clocked at 8 kHz. What is the frequency of Q?

<!--ANSWERS-->

## Answers

**Check 1.** J K before the falling edges: 10, 01, 11, 10, 01, 00, so **Q = 1, 0, 1, 1, 0, 0**: the same values, but every change comes half a clock period later.

**Check 2.** **Q = 1, 1, 1, 0, 1, 1**.

**Self-test.**

1. **1, 0, 0, 1**.
2. **0, 1, 1, 0**.
3. **1, 1, 0, 0**.
4. The latch follows every change of D while the enable is high; the flip-flop changes only at edges.
5. **4 kHz**.

<!--/ANSWERS-->
