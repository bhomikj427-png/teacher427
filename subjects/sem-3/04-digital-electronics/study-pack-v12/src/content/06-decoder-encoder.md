# 06 — Decoder and encoder

<div class="sub">Deck 05 (slides 4–43) · mid-term 2025 Q6 (4 marks) · practice set 1 Q7–Q8 · syllabus Unit 2 · needs 01 (minterms) and 04 (full adder)</div>

## Map

[[map:1 Decoder-based design > 2 Bigger decoders > 3 Priority encoder|here=1]]

05's MUX picks one input. A decoder does the opposite job: it turns a code into one active line out of many. Each line is a minterm, so a decoder plus an OR gate is any function.

## The questions this file answers

- <span class="tag">MTE 2025 Q6 · 4 marks</span> Design a full adder using a suitable decoder.
- <span class="tag">Set 1 Q7</span> Realise Y = ΠM(0, 3, 5, 6, 7) with a decoder and one NOR gate.
- <span class="tag">Deck 05 slides 36–43</span> Design a 4-to-2 priority encoder with a valid output.

---

## Build

### 1 · Decoder-based design

:::q <span class="tag">MTE 2025 Q6 · 4 marks</span>
Design Full Adder using suitable decoder.
:::

:::guess Guess first
A full adder has 3 inputs. How many outputs must the decoder have, and what is each output in the language of 01?
:::

:::note Terms
**Decoder (n to 2^{n}):** exactly one output is active, the one numbered by the input code; output j is minterm m_{j}. **Enable:** switches all outputs off when inactive. **Active-low:** the selected output goes to 0 (drawn with a bubble).
:::

[[fig:decoder_fig|3:8 decoder with two OR gates: the full adder.|w=65]]

Any function = decoder + one OR per output, ORing the minterms in its Σm list. With active-low outputs (74138), each output is m_{j}', so use a **NAND**: NAND(m_{1}', m_{2}') = m_{1} + m_{2}.

**Answer.** 3:8 decoder, inputs A, B, C_{in} (A MSB). From 04: S = Σm(1, 2, 4, 7), C_{out} = Σm(3, 5, 6, 7). **OR outputs 1, 2, 4, 7 for S; OR outputs 3, 5, 6, 7 for C_{out}.** Active-low decoder: two 4-input NANDs.

:::check Check 1
(a) <span class="tag">Set 1 Q7</span> Realise Y = ΠM(0, 3, 5, 6, 7) with a decoder and one NOR gate. (b) <span class="tag">Deck 05 slide 20</span> Realise F(X, Y, Z) = Σm(1, 2, 5, 7) with an active-low 3:8 decoder.
:::

### 2 · Bigger decoders from smaller ones

:::guess Predict
You have two 3:8 decoders with enables. How would you make a 4:16 decoder?
:::

**Deck 05 slide 14.** The low three bits go to both decoders; the top bit enables one directly and the other through an inverter. A decoder with enable is also a **demultiplexer** (05): the code inputs are the selects and the data drives the enable.

**Answer.** Two 3:8 decoders and one inverter: w_{3} = 0 enables the low decoder (outputs 0–7), w_{3} = 1 the high one (8–15).

:::check Check 2
How many 2:4 decoders with enables, and what else, make a 3:8 decoder?
:::

### 3 · Encoder and priority encoder

:::q <span class="tag">Deck 05 slides 36–43</span>
Design a 4-to-2 priority encoder with a valid output.
:::

:::guess Guess first
A plain encoder assumes only one input is 1. What should happen if two are 1 at once?
:::

:::note Terms
**Encoder (2^{n} to n):** outputs the active input's number in binary. **Priority encoder:** with several active, outputs the highest-numbered. **Valid V:** 1 when at least one input is active.
:::

| w_{3} w_{2} w_{1} w_{0} | y_{1} y_{0} | V |
|---|---|---|
| 0 0 0 0 | X X | 0 |
| 0 0 0 1 | 0 0 | 1 |
| 0 0 1 X | 0 1 | 1 |
| 0 1 X X | 1 0 | 1 |
| 1 X X X | 1 1 | 1 |

An X on the input side means "whatever": once w_{3} = 1 the lower inputs are ignored. A plain encoder (y_{1} = w_{2} + w_{3}, y_{0} = w_{1} + w_{3}) gives 11 for w_{1} and w_{2} together, and 00 for both "w_{0}" and "nothing". Priority and V fix both.

**Answer.**

$$y_{1} = w_{3} + w_{2}      y_{0} = w_{3} + w_{2}'w_{1}      V = w_{3} + w_{2} + w_{1} + w_{0}$$

The w_{2}' in y_{0} is the priority: w_{1} counts only if w_{2} is off. Uses: keyboard encoding (decimal-to-BCD), interrupt handling.

:::check Check 3
(a) Inputs 0110: y_{1}y_{0} and V? (b) Write y_{0} for a plain 8-to-3 encoder. (c) Why is V needed?
:::

---

## Exam form

**Decoder.** Block and truth table; output j = m_{j}; function = OR of its minterms (NAND for active-low; NOR for the ΠM rows).

**Expansion.** 4:16 from two 3:8s and an inverter.

**Priority encoder.** Table with Xs; y_{1}, y_{0}, V; why priority and V are needed.

## Traps

- Using OR with active-low outputs: it needs NAND.
- ΠM with a NOR: NOR the rows where F = 0 (the maxterm rows), not the Σm rows.
- Forgetting the X rows in the priority table stand for many rows.

## Self-test

1. Realise F(A, B, C) = Σm(0, 3, 5) with a 3:8 decoder and one gate.
2. Design a full subtractor with a 3:8 decoder.
3. Priority encoder input w_{3}w_{2}w_{1}w_{0} = 1011: y_{1}y_{0} and V?
4. Write y_{2} of an 8-to-3 priority encoder.
5. Give one use each for a decoder and a priority encoder.

<!--ANSWERS-->

## Answers

**Check 1.** (a) Y = 0 on rows 0, 3, 5, 6, 7: **NOR outputs 0, 3, 5, 6, 7** (= Σm(1, 2, 4)). (b) A **4-input NAND** on outputs 1, 2, 5, 7.

**Check 2.** **Two 2:4 decoders** with enables and **one inverter** for the top bit.

**Check 3.** (a) w_{2} is highest: **10, V = 1**. (b) y_{0} = **w_{1} + w_{3} + w_{5} + w_{7}**. (c) 00 could mean "input 0" or "nothing"; V tells them apart.

**Self-test.**

1. OR of outputs **0, 3, 5**.
2. D = Σm(1, 2, 4, 7), B_{out} = Σm(1, 2, 3, 7): **OR outputs 1, 2, 4, 7** and **OR outputs 1, 2, 3, 7**.
3. **11, V = 1** (w_{3} wins).
4. y_{2} = **w_{4} + w_{5} + w_{6} + w_{7}**.
5. Decoder: memory address decoding, or a function generator. Priority encoder: interrupt priority, keyboard encoding.

<!--/ANSWERS-->
