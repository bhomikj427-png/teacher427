# 15 — FSM design: Moore, Mealy, sequence detectors

<div class="sub">Deck 11 (slides 3–43; five practice detectors on slide 43) · syllabus Unit 4 · needs 13 (the six-step counter procedure) and 09 (excitation tables)</div>

## Map

[[map:1 Moore and Mealy > 2 Words to a state diagram > 3 State table to circuit > 4 The Moore version|here=1]]

A counter (13) walks a fixed list of states. Add an input that decides which state comes next and an output, and you have a **finite state machine**: the general form of every synchronous circuit. The design steps are 13's six, with "words → state diagram" in front.

## The questions this file answers

- <span class="tag">Deck 11 slides 35–36</span> Differentiate Mealy and Moore circuits.
- <span class="tag">Deck 11 slides 7–25</span> Design a recogniser for 1101, overlap allowed (1101101 contains it twice).
- <span class="tag">Deck 11 slide 43</span> Practice detectors: 1011 Moore, and others.

---

## Build

### 1 · Moore and Mealy

:::q <span class="tag">Deck 11 slides 35–36</span>
Differentiate between Mealy and Moore sequential circuits.
:::

:::guess Guess first
In the two block diagrams below, find the one wire that is different.
:::

:::note Terms
**State:** what the circuit remembers about past inputs, held in its flip-flops; n flip-flops give up to 2^{n} states. **Next-state logic:** works out where to go. **Output logic:** produces z.
:::

[[fig:fsm_blocks|Moore (output from the state only) and Mealy (output from state and input).]]

| | Moore | Mealy |
|---|---|---|
| Output depends on | present state only | present state and present input |
| In the diagram | inside the circle (S/z) | on the arrow (x/z) |
| Output changes | only after a clock edge; steady all cycle | as soon as the input changes; can glitch |
| States | usually one more | fewer |
| Response | one clock later | same clock cycle |

**Answer.** The table. In one line: a Moore output is a function of the state; a Mealy output, of the state and the input.

:::check Check 1
<span class="tag">Deck 11 slide 37</span> How many states does a 111 detector need as a Mealy machine, and as a Moore machine?
:::

### 2 · From words to a state diagram

:::q <span class="tag">Deck 11 slides 7–25</span>
Design a sequence recognizer for 1101. The output is 1 each time the sequence occurs in the input, and overlap is allowed.
:::

:::guess Guess first
After receiving 110, what must the machine remember? After 1101, if the next pattern may reuse the last 1?
:::

**Give each state a meaning:** how much of the pattern has arrived. A = nothing useful, B = "1", C = "11", D = "110". Arrows are labelled input/output.

[[fig:mealy_1101|Mealy 1101 detector, overlap allowed.|w=60]]

- From D, a 1 completes 1101: output 1. That 1 can start a new pattern, so the arrow goes to **B**, not A (the overlap).
- From C, another 1 stays in C ("two or more 1s").
- Every state needs an arrow for x = 0 and for x = 1.

**Answer.** Four states, as drawn. The machine remembers the longest tail of the input that is also a head of 1101.

:::check Check 2
For a **non-overlapping** 1101 detector, which one arrow changes?
:::

### 3 · State table to circuit

:::guess Predict
Four states need two flip-flops. Does it matter which two-bit code each state gets?
:::

| Present | x = 0: next, z | x = 1: next, z |
|---|---|---|
| A = 00 | A, 0 | B, 0 |
| B = 01 | A, 0 | C, 0 |
| C = 11 | D, 0 | C, 0 |
| D = 10 | A, 0 | B, 1 |

**Procedure** (deck 11 slide 3): specification → state diagram → state table → state reduction (16) → **state assignment** → flip-flops and excitation → K-maps → circuit. With D flip-flops, D = next state, so the maps come straight from the table.

| Assignment | Equations |
|---|---|
| Gray order (A 00, B 01, C 11, D 10) | D_{1} = Y_{1}Y_{2} + XY_{2} · D_{2} = X · Z = XY_{1}Y_{2}' |
| Counting order (A 00, B 01, C 10, D 11) | D_{1} = Y_{1}Y_{2}' + XY_{1}'Y_{2} · D_{2} = XY_{1}'Y_{2}' + X'Y_{1}Y_{2}' + XY_{1}Y_{2} · Z = XY_{1}Y_{2} |

**Answer.** Yes for cost, no for behaviour. The Gray assignment needs far fewer gates, so the deck finishes with it: **D_{1} = Y_{1}Y_{2} + XY_{2}, D_{2} = X, Z = XY_{1}Y_{2}'**, with a reset to 00. Test 1101101 → Z = **0001001**.

:::check Check 3
Run 110110110 through the Mealy detector. Write Z.
:::

### 4 · The Moore version

:::q <span class="tag">Deck 11 slides 40–42</span>
Convert the 1101 detector to a Moore machine.
:::

:::guess Guess first
In Moore the output belongs to a state. Which new state is needed?
:::

[[fig:moore_1101|Moore 1101 detector: E = "1101 just seen", output 1.|w=60]]

Add **E = "1101 just seen"** with output 1. E behaves like B (a 1 has arrived) but outputs 1. Five states → 3 flip-flops. Codes A 000, B 001, C 010, D 011, E 100, D flip-flops, 101–111 don't-care:

$$D_{2} = Y_{1}Y_{0}X      D_{1} = Y_{2}X + Y_{1}Y_{0}' + Y_{1}'Y_{0}X      D_{0} = Y_{1}Y_{0}'X' + Y_{2}'Y_{1}'Y_{0}'X      z = Y_{2}$$

**Answer.** The output appears one clock after the last bit, and cannot glitch.

:::check Check 4
<span class="tag">Deck 11 slide 43 Q1</span> Design a Moore circuit that detects 1011 (overlap allowed). Give each state's meaning and the state table.
:::

---

## Exam form

**Moore vs Mealy.** Block diagrams and the five-row table.

**Detector design.** State meanings → diagram (both arrows from every state; overlap arrows) → state table → assignment → excitation (D: D = next state) → K-maps → equations → circuit with reset. Verify with a test string.

**Moore conversion.** Extra "pattern seen" state; output in the circle.

## Traps

- Sending the completion arrow to the start state in an overlapping detector.
- A state with only one outgoing arrow.
- Writing a Mealy output inside the circle.
- Forgetting the reset to the initial state.

## Self-test

1. Give three differences between Moore and Mealy machines.
2. Draw a Mealy 101 detector, overlap allowed.
3. Draw the Moore version of Q2.
4. How many flip-flops for a 5-state machine?
5. Why can a state assignment change the cost of the circuit?

<!--ANSWERS-->

## Answers

**Check 1.** Mealy **3** (nothing, "1", "11"); Moore **4** (one more to hold the output).

**Check 2.** D —1/1→ B becomes **D —1/1→ A**: after a match it starts from nothing.

**Check 3.** **000100100** (matches complete at bits 4 and 7).

**Check 4.** S0 nothing; S1 "1"; S2 "10"; S3 "101"; S4 "1011", output 1. Next (x = 0, x = 1): S0 → S0, S1 · S1 → S2, S1 · S2 → S0, S3 · S3 → S2, S4 · S4 → S2, S1. From S4 a 1 goes to S1 and a 0 to S2, because the final 1 can start a new pattern.

**Self-test.**

1. Output depends on state only vs state and input; output in circle vs on arrow; Moore usually needs one more state; Mealy responds in the same cycle and can glitch.
2. A (nothing): 0/0 → A, 1/0 → B. B ("1"): 0/0 → C, 1/0 → B. C ("10"): 0/0 → A, 1/1 → B.
3. A, B, C as above with outputs 0, plus D = "101" (output 1): A —1→ B, B —0→ C, C —1→ D, C —0→ A, D —0→ C, D —1→ B, B —1→ B, A —0→ A.
4. **3**.
5. The next-state and output equations depend on the codes; codes that keep related states adjacent give larger K-map groups.

<!--/ANSWERS-->
