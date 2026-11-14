# 07 — 7-segment display, comparator, parity

<div class="sub">Deck 06 (comparator slides 3–6, parity slide 13) · mid-term 2025 Q2 (2 marks) · practice set 1 Q9–Q10 · syllabus Unit 2 · needs 02 (K-maps with don't-cares)</div>

## Map

[[map:1 BCD to 7-segment > 2 Multiplexed display > 3 Magnitude comparator > 4 Parity|here=1]]

Three more MSI blocks, each a K-map exercise from 02 with a job attached: drive a display, compare two numbers, catch a transmission error.

## The questions this file answers

- <span class="tag">Set 1 Q10</span> Design a BCD to 7-segment decoder for a common-anode display.
- <span class="tag">Deck 06 slides 3–6</span> Design a 2-bit magnitude comparator.
- <span class="tag">MTE 2025 Q2 · 2 marks</span> 1011 is applied to an even parity generator. What is the output?

---

## Build

### 1 · BCD to 7-segment decoder

:::q <span class="tag">Set 1 Q10</span>
Design a BCD to 7-segment decoder circuit for a common anode display.
:::

:::guess Guess first
In a common-anode display all anodes are tied to +5 V. Does a segment light on a 1 or on a 0?
:::

:::note Terms
**7-segment display:** seven LED bars a–g. **Common cathode:** cathodes grounded; a segment lights on 1. **Common anode:** anodes at +V; a segment lights on 0. **Driver:** an output that supplies the 10–20 mA an LED needs, through a resistor.
:::

[[fig:seven_seg|Segment names and digit shapes.|w=60]]

For each segment list the digits that light it, with codes 10–15 as don't-cares (02):

| Seg. | Lit for | Minimal SOP (lit = 1) |
|---|---|---|
| a | 0 2 3 5 6 7 8 9 | A + C + BD + B'D' |
| b | 0 1 2 3 4 7 8 9 | B' + C'D' + CD |
| c | all except 2 | B + C' + D |
| d | 0 2 3 5 6 8 9 | A + B'D' + B'C + CD' + BC'D |
| e | 0 2 6 8 | B'D' + CD' |
| f | 0 4 5 6 8 9 | A + C'D' + BC' + BD' |
| g | 2 3 4 5 6 8 9 | A + B'C + BC' + CD' |

[[fig:v1arg6|K-map for segment e.|w=40]]

Shapes used: 6 with the top bar, 9 with the bottom bar (some chips omit them, changing a and d).

**Answer.** The equations light a segment with 1 (common cathode). For **common anode** each output must be **0** to light, so drive the complements (an inverter on each output, or minimise the 0s): e.g. **e' = (B'D' + CD')' = D + BC'**. Anodes to +5 V, a series resistor per segment.

:::check Check 1
(a) Which segments light for 4? (b) Write the active-low expression for segment c.
:::

### 2 · Multiplexed display

:::guess Predict
A 6-digit display with a decoder per digit needs 42 segment lines. How could one decoder serve all six?
:::

[[fig:mux_display|Multiplexed display: shared segment lines, digits enabled in turn.|w=70]]

Wire the segment lines of all digits together and enable one digit at a time with its own BCD value, faster than the eye follows (each digit refreshed more than about 50 times a second).

**Answer.** Time-share it: N digits need **7 + N** lines and one decoder.

:::check Check 2
Lines for a 6-digit display with and without multiplexing?
:::

### 3 · Magnitude comparator

:::q <span class="tag">Deck 06 slides 3–6</span>
Design a 2-bit magnitude comparator: outputs G (A &gt; B), E (A = B), L (A &lt; B) for A = A_{1}A_{0}, B = B_{1}B_{0}.
:::

:::guess Guess first
Comparing 5234 with 5199 by hand: which digit do you look at first, and when do you stop?
:::

[[fig:comparator_flow|Compare from the MSB; the first differing bit decides.|w=60]]

One bit: G = AB', L = A'B, E = A ⊙ B. Write **x_{i} = A_{i} ⊙ B_{i}**. The first position from the top where the bits differ decides; lower bits matter only while all higher ones are equal.

| | 2-bit | 4-bit (7485) |
|---|---|---|
| E | x_{1}x_{0} | x_{3}x_{2}x_{1}x_{0} |
| G | A_{1}B_{1}' + x_{1}A_{0}B_{0}' | A_{3}B_{3}' + x_{3}A_{2}B_{2}' + x_{3}x_{2}A_{1}B_{1}' + x_{3}x_{2}x_{1}A_{0}B_{0}' |
| L | A_{1}'B_{1} + x_{1}A_{0}'B_{0} | same with A', B swapped in; or (G + E)' |

**Answer.** K-maps of the 16-row table give G = A_{1}B_{1}' + A_{0}B_{1}'B_{0}' + A_{1}A_{0}B_{0}', L = A_{1}'B_{1} + A_{1}'A_{0}'B_{0} + A_{0}'B_{1}B_{0}, E = (A_{1} ⊙ B_{1})(A_{0} ⊙ B_{0}): the table's formulas multiplied out. The 7485's cascade inputs (A&gt;B, A=B, A&lt;B) take the result of the lower chip for 8 bits.

:::check Check 3
(a) A = 0101, B = 0100: where is it decided, and which output is 1? (b) Why can L be made from G and E with one gate?
:::

### 4 · Parity generator and checker

:::q <span class="tag">MTE 2025 Q2 · 2 marks</span>
The four-bit binary sequence 1011 is applied to an even parity generator circuit. What will be the output?
:::

:::guess Guess first
Count the 1s in 1011. Is the count already even?
:::

:::note Terms
**Parity bit:** one extra bit so the receiver can detect an error. **Even parity:** total 1s (data + parity) even. **Odd parity:** total odd.
:::

[[fig:parity_fig|Parity generator and checker from XOR gates.|w=70]]

XOR of several bits is 1 exactly when an odd number are 1, so **P_{even} = XOR of all data bits**; P_{odd} is its complement. Three bits: P_{even} = X ⊕ Y ⊕ Z. **Checker:** XOR everything received, parity included; with even parity E should be 0. One parity bit detects any odd number of errors, misses two, and cannot locate the error.

**Answer.** Three 1s (odd): P = 1 ⊕ 0 ⊕ 1 ⊕ 1 = **1**. The word sent, 1011 1, has four 1s.

:::check Check 4
(a) Odd parity bit for 1011? (b) Even parity, received data 1001 with parity 1: error?
:::

---

## Exam form

**7-segment.** Segment diagram; truth table 0–9 with 10–15 as X; K-map per segment; common anode = complement outputs; multiplexed display (7 + N lines).

**Comparator.** One-bit G, E, L; x_{i}; 2-bit and 4-bit equations; cascading.

**Parity.** XOR tree generator, checker, what one bit detects.

## Traps

- Common anode needs active-low outputs.
- Forgetting the don't-cares 10–15 in the segment maps.
- Comparing from the LSB.
- Mixing even and odd parity: even parity bit = XOR, odd = XNOR.

## Self-test

1. Which segments light for 7?
2. Odd parity bit for 1101001?
3. A 2-bit comparator gets A = 10, B = 11. Which output is 1?
4. An even-parity checker receives 10110 (parity included). Error?
5. A 4-digit multiplexed display needs how many lines?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **b, c, f, g**. (b) c' = **B'CD'**: 0 (lit) for every digit except 2.

**Check 2.** **13** with, **42** without.

**Check 3.** (a) Bit 0 decides (1 against 0): **G = 1**. (b) Exactly one of G, E, L is 1, so L = (G + E)': **one NOR**.

**Check 4.** (a) **0**: the count is already odd. (b) Three 1s: odd, **E = 1, error**.

**Self-test.**

1. **a, b, c**.
2. Four 1s (even): odd parity bit = **1**.
3. **L** (A &lt; B: 2 &lt; 3).
4. Three 1s: **error**.
5. 7 + 4 = **11**.

<!--/ANSWERS-->
