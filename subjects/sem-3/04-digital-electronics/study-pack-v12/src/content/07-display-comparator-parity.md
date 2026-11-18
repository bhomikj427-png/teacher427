# 07 — 7-segment display, comparator, parity

<div class="sub">Deck 05 slides 27–30 (BCD to 7-segment) · deck 06 (comparator slides 1–7, parity slides 8–26) · MTE 2025 Q2 (2 marks) · practice set 1 Q9, Q10 · syllabus Unit 2 (driver and multiplexed display, comparators) · needs 01 step 3 (XOR, XNOR), 02 (four-variable K-maps, don't-cares), 06 steps 1–3 (decoders, active-low outputs)</div>

## Map

[[map:1 Segment table > 2 Segment K-maps > 3 Common anode > 4 Multiplexed display > 5 1-bit comparator > 6 2-bit comparator > 7 n-bit comparator > 8 Cascading > 9 Parity bit > 10 4-bit generator > 11 Parity checker|here=1]]

File 06 built decoders: circuits that turn a binary code into "which output is on". This file builds three more blocks of the same kind, each one a K-map job from file 02 with a purpose attached. A **BCD to 7-segment decoder** turns a 4-bit digit into the bars that draw it on a display. A **magnitude comparator** says whether one number is bigger, equal or smaller than another. A **parity generator and checker** add one bit to a word so that the receiver can tell when a bit was corrupted on the way. The deck order is kept: display (deck 05) first, then comparator and parity (deck 06).

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| A B C D | the four BCD input bits, **A the MSB** (worth 8), D the LSB (worth 1); deck 05 slide 28 names them the other way round (D the MSB) | 0 or 1 |
| a … g | the seven segments (bars) of the display: a top, b top-right, c bottom-right, d bottom, e bottom-left, f top-left, g middle | 1 = lit (common cathode) |
| a' … g' | active-low segment outputs: 0 lights the segment (common anode) | 0 = lit |
| N | number of digits on a multiplexed display | 4–8 |
| A = A_{3}A_{2}A_{1}A_{0}, B = B_{3}B_{2}B_{1}B_{0} | the two numbers a comparator compares; index 3 is the MSB | 0–15 |
| G, E, L | comparator outputs: G = 1 when A &gt; B, E = 1 when A = B, L = 1 when A &lt; B | exactly one is 1 |
| x_{i} | bit-equality: x_{i} = A_{i} ⊙ B_{i}, 1 when bit i of A equals bit i of B | 0 or 1 |
| P | parity bit added to the data word | 0 or 1 |
| E (parity) | checker output: 1 = error found (deck 06 slide 19 calls it PEC, slide 24 PE) | 0 or 1 |

## Running example

**The word 0110 (six, deck 05 slide 30, EX 5.30).** Step 1 shows it on a display, step 7 compares it with 0101 (five), step 9 adds its parity bit. Every step that needs a 4-bit word uses it.

## The questions this file answers

- <span class="tag">Deck 05 slide 30 (EX 5.30)</span> BCD input 0110: what decimal digit appears on the 7-segment display?
- <span class="tag">Practice set 1 Q10</span> Design a BCD to 7-segment decoder circuit for a common anode display.
- <span class="tag">Deck 06 slides 2–6</span> Design a 1-bit and a 2-bit magnitude comparator.
- <span class="tag">MTE 2025 Q2 · 2 marks</span> The 4-bit sequence 1011 is applied to an even parity generator. What is the output?
- <span class="tag">Practice set 1 Q9</span> Draw the logic diagram of a 4-bit odd/even parity generator.

---

## Build

### 1 · What the display needs: the segment table

A calculator or a lift shows each digit with seven bars. The bars are LEDs; the circuit's job is to decide, for each digit, which of the seven to switch on.

:::q <span class="tag">Deck 05 slide 30 (EX 5.30)</span>
The BCD input 0110 enters a BCD-to-7-segment decoder/driver that drives an LED display. What decimal digit appears?
:::

:::guess Guess first
0110 in binary is which number? Before looking at the table: how many of the seven bars does that digit need?
:::

:::note Terms
**7-segment display:** seven LED bars named a to g, arranged as an "8". **BCD (binary-coded decimal):** one decimal digit 0–9 written as its 4-bit binary number; codes 1010–1111 (10–15) are never sent. **Decoder/driver:** the circuit with 4 inputs and 7 outputs that picks the bars, and supplies the current the LEDs need (deck 05 slide 27). It is a decoder in file 06's sense: one code in, a pattern of outputs on.
:::

[[fig:seven_seg|The seven segments a–g and the digits 0–9 they draw (deck 05 slides 27–29). The 6 is drawn with its top bar a, the 9 with its bottom bar d, the 7 with three bars a, b, c.|w=70]]

Read each digit off the figure and write which bars it lights. One row per digit; a 1 means "this bar is lit".

| Digit | A B C D | a | b | c | d | e | f | g | bars lit |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 0000 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 6 |
| 1 | 0001 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 2 |
| 2 | 0010 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 5 |
| 3 | 0011 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 5 |
| 4 | 0100 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 4 |
| 5 | 0101 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 5 |
| 6 | 0110 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 6 |
| 7 | 0111 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 3 |
| 8 | 1000 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 7 |
| 9 | 1001 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 6 |
| 10–15 | 1010–1111 | X | X | X | X | X | X | X | — |

The last row matters for step 2: codes 10–15 never arrive, so each segment's output there is a **don't-care X** (file 02).

**Answer to the Guess.** 0110 = 4 + 2 = **6**. Its row lights **a, c, d, e, f, g**: six bars, all except b (top right). The display shows **6** (deck 05 slide 30's answer).

:::check Check 1
(a) Which bars light for 4? (b) Which digit lights only two bars, and which ones?
:::

### 2 · One K-map per segment

Step 1's table has seven output columns. Each column is a function of A, B, C, D on its own, so the decoder is seven separate four-variable K-map problems.

:::guess Predict
Segment a is lit for 8 of the 10 digits. Will its minimal expression be long or short? (Hint: a K-map groups the 1s, and the six don't-cares can join groups.)
:::

:::note Terms
**Lit = 1 (active-high):** the output is 1 when its segment should light. This suits a **common-cathode** display: all LED cathodes are joined to ground, so a segment lights when its anode is driven high.
:::

[[fig:seg_kmap_a|What this graph plots: the K-map of segment a. A B down the side and C D across, both in Gray order 00, 01, 11, 10. One cell = one input code; the number in the corner is the code's decimal value. 1 = the digit lights a, X = codes 10–15 (never sent). Each loop is one product term: the bottom two rows (A), the right-hand two columns (C), the middle square (BD), the four corners (B'D').|w=45]]

Segment a's 1s are digits 0, 2, 3, 5, 6, 7, 8, 9; its 0s are only 1 and 4. Loop the 1s, using X cells to make the loops as big as possible:

1. The rows A B = 11 and 10 hold 8, 9 and the X's 10–15: one 8-cell loop, **A**.
2. The columns C D = 11 and 10 hold 2, 3, 6, 7 and X's: one 8-cell loop, **C**.
3. 5 (0101) is left. With 7, 13, 15 it forms the middle square **BD**.
4. 0 (0000) is left. With 2, 8, 10 it forms the four corners **B'D'**.

So **a = A + C + BD + B'D'**. Doing the same for all seven segments gives:

| Segment | Lit for digits | Minimal SOP (lit = 1) |
|---|---|---|
| a | 0 2 3 5 6 7 8 9 | A + C + BD + B'D' |
| b | 0 1 2 3 4 7 8 9 | B' + C'D' + CD |
| c | 0 1 3 4 5 6 7 8 9 | B + C' + D |
| d | 0 2 3 5 6 8 9 | A + B'D' + B'C + CD' + BC'D |
| e | 0 2 6 8 | B'D' + CD' |
| f | 0 4 5 6 8 9 | A + C'D' + BC' + BD' |
| g | 2 3 4 5 6 8 9 | A + B'C + BC' + CD' |

Each line is checked against the table on all ten digits and is the smallest possible (verify compares it with a Quine–McCluskey minimum). Segment g has a second answer of the same size, A + B'C + BC' + BD': either is correct.

**Answer to the Predict.** **Short.** A segment lit for most digits has few 0s, and the don't-cares fill the gaps, so big loops form: a needs four terms with at most two letters each.

:::check Check 2
(a) Segment c's expression B + C' + D is 1 for the code 1110 (14). Why is that not a mistake? (b) From the table, list the digits that light segment e.
:::

### 3 · Common anode: light on 0

Step 2's outputs light a segment with a 1. Practice set 1 Q10 asks for the other kind of display.

:::q <span class="tag">Practice set 1 Q10</span>
Design a BCD to 7-segment decoder circuit for a common anode display.
:::

:::guess Guess first
In a common-anode display all the LED anodes are tied together to +5 V. To make current flow through one segment, must its cathode be pulled high or low?
:::

:::note Terms
**Common anode:** all anodes joined to the supply; a segment lights when its own line is driven **low (0)**. **Active-low output:** an output whose "on" value is 0 (file 06 step 3). **Series resistor:** one per segment line, limiting the LED current (the seven resistors on deck 05 slide 27).
:::

An LED conducts from anode to cathode. With the anode held at +5 V, current flows only when the cathode line is at 0; at 1 there is no voltage across the LED and it stays dark. So each output must now be the **complement** of step 2's: a' = 1 exactly where a = 0.

Two ways to build it:

1. **Invert step 2's outputs:** seven NOT gates after the common-cathode decoder.
2. **Minimise the 0s directly:** loop the 0s of each segment's K-map (with the same X's). This often gives a smaller circuit, because most segments have few 0s.

| Segment | Dark for digits | Active-low output (lights on 0) |
|---|---|---|
| a' | 1 4 | A'B'C'D + BC'D' |
| b' | 5 6 | BC'D + BCD' |
| c' | 2 | B'CD' |
| d' | 1 4 7 | A'B'C'D + BC'D' + BCD |
| e' | 1 3 4 5 7 9 | D + BC' |
| f' | 1 2 3 7 | A'B'D + B'C + CD |
| g' | 0 1 7 | A'B'C' + BCD |

Read one line back: **e' = D + BC'** says "drive e's line high (dark) for every odd digit (D = 1) and for 4 and 5 (B = 1, C = 0)"; everywhere else it is 0 and e lights. Each line is checked to be the exact complement of step 2's on digits 0–9, and minimal.

Ready-made chips do this job: the **7447** is a BCD-to-7-segment decoder/driver with active-low outputs for common-anode displays, the **7448** the active-high version for common cathode (KB 02 §4).

**Answer to the Guess.** **Low.** The anode is already at +5 V, so the segment lights when its line is 0. Every decoder output must be active-low: the complement of the common-cathode equations, built by inverting them or by looping the 0s (table above), with a resistor in each line.

:::check Check 3
(a) Write the seven common-anode outputs a … g for the digit 7. (b) c' = B'CD' is 1 for which digit only?
:::

### 4 · Many digits, one decoder: the multiplexed display

A clock shows 4 digits, a meter 6. Giving each digit its own decoder and seven wires multiplies the wiring.

:::guess Predict
A 6-digit display with one decoder per digit needs 6 × 7 = 42 segment lines. How could a single decoder serve all six digits?
:::

:::note Terms
**Digit enable:** one line per digit that switches that digit's common terminal on. **Multiplexed (time-shared) display:** all digits share the same seven segment lines; only one digit is enabled at a time. **Persistence of vision:** the eye blends light that flickers fast enough into a steady image.
:::

[[fig:mux_display|Multiplexed display: one BCD-to-7-segment decoder drives segment lines a–g shared by every digit; a separate enable line switches on one digit at a time.|w=70]]

The sequence repeats over and over:

1. Put digit 1's BCD code into the decoder; enable digit 1 only. Digit 1 shows its pattern; the others are dark.
2. Put digit 2's code in; enable digit 2 only. And so on to digit N, then back to digit 1.

Each digit is lit only 1/N of the time, but the scan runs fast enough that the eye sees all digits lit at once (KB 02 §4). For example, a 4-digit display rescanned 60 times a second keeps each digit on for 1/(4 × 60) s ≈ 4.17 ms per scan.

Line count: 7 shared segment lines + N enable lines.

$$lines = 7 + N   (instead of 7N)$$

Read it: seven lines carry the pattern, one extra line per digit says whose pattern it is.

**Answer to the Predict.** **Time-share it:** connect the segment lines of all six digits together, and enable the digits one at a time while the decoder is fed each digit's code in turn. 7 + 6 = **13** lines and one decoder, instead of 42 lines and six decoders.

:::check Check 4
A 4-digit display: how many lines with and without multiplexing?
:::

### 5 · Comparing one bit

The display steps took one number in. A comparator takes two numbers and answers one question: which is bigger? Start with one bit each.

:::q <span class="tag">Deck 06 slides 1–2</span>
Design a 1-bit magnitude comparator: inputs A and B (one bit each), outputs G (A &gt; B), E (A = B), L (A &lt; B).
:::

:::guess Guess first
With one bit each, A &gt; B can happen in only one way. Which?
:::

:::note Terms
**Magnitude comparator:** a circuit with two n-bit inputs A, B and three outputs G, E, L; exactly one of them is 1 for every input (KB 02 §1). **XNOR (equivalence, ⊙):** 1 when its inputs are equal (file 01 step 3).
:::

| A | B | L (A &lt; B) | E (A = B) | G (A &gt; B) |
|---|---|---|---|---|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 |

Each output column has a single 1 or two 1s, so each is one gate:

$$G = AB'      L = A'B      E = A'B' + AB = A ⊙ B$$

Read them: G says "A is 1 and B is 0"; L the reverse; E says "both 0 or both 1", which is exactly XNOR.

[[fig:comp1|1-bit comparator (deck 06 slide 2): A and B with their complements; an AND of A' and B gives L, an XNOR of A and B gives E, an AND of A and B' gives G.|w=60]]

**Answer to the Guess.** **A = 1, B = 0.** That is the only row of the table with A &gt; B, so G = AB'.

:::check Check 5
(a) A = 1, B = 1: give G, E, L. (b) Why does E need only one gate, an XNOR?
:::

### 6 · The 2-bit comparator from its truth table

Two bits each give 4 × 4 = 16 input rows. Deck 06 solves it the long way, with K-maps; step 7 shows the short way that also works for 4 bits.

:::q <span class="tag">Deck 06 slides 3–6</span>
Design a 2-bit magnitude comparator for A = A_{1}A_{0} and B = B_{1}B_{0}: truth table, K-maps and minimal G, E, L.
:::

:::guess Guess first
Of the 16 input pairs, how many give A = B? And how many give A &gt; B?
:::

The 16 rows of deck 06 slide 4 fit in one grid: A (as a number 0–3) down the side, B across, and the cell says which output is 1.

| A \ B | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | E | L | L | L |
| 1 | G | E | L | L |
| 2 | G | G | E | L |
| 3 | G | G | G | E |

E sits on the diagonal (4 cells), G below it (6 cells), L above it (6 cells).

[[fig:comp2_kmaps|What this graph plots: two 4-variable K-maps, A_{1}A_{0} down the side and B_{1}B_{0} across in Gray order. One cell = one input pair (A, B); 1 = that output is on. Left, G: three loops, A_{1}B_{1}' (a quad), A_{0}B_{1}'B_{0}' and A_{1}A_{0}B_{0}' (pairs). Right, L: the mirror image, A_{1}'B_{1}, A_{0}'B_{1}B_{0}, A_{1}'A_{0}'B_{0}.|w=82]]

Looping the maps (deck 06 slide 5):

$$G = A_{1}B_{1}' + A_{0}B_{1}'B_{0}' + A_{1}A_{0}B_{0}'$$

$$L = A_{1}'B_{1} + A_{0}'B_{1}B_{0} + A_{1}'A_{0}'B_{0}$$

Read G's terms: "A_{1} = 1 while B_{1} = 0" (the top bit already decides); "A_{0} = 1 while B is 00"; "A is 11 while B_{0} = 0". E's map has four 1s on the diagonal, none adjacent, so no loop forms:

$$E = A_{1}'A_{0}'B_{1}'B_{0}' + A_{1}'A_{0}B_{1}'B_{0} + A_{1}A_{0}B_{1}B_{0} + A_{1}A_{0}'B_{1}B_{0}'$$

The four terms say "the bits agree in both places", so they factor into two XNORs: **E = (A_{1} ⊙ B_{1})(A_{0} ⊙ B_{0})**, two XNORs and one AND (deck 06 slide 6's circuit). Deck 06 slide 5 prints "G = A&gt;B:" with a colon where "=" is meant.

Since exactly one output is 1, the third can always be made from the other two: **L = (G + E)'**, one NOR gate.

**Answer to the Guess.** **4** pairs are equal (the diagonal: 00 00, 01 01, 10 10, 11 11) and **6** have A &gt; B; the other 6 have A &lt; B.

:::check Check 6
(a) A = 11, B = 10: which output is 1, and which of G's three terms is 1? (b) How many gates does L need if G and E are already built?
:::

### 7 · Any number of bits: compare from the top

Step 6's K-maps had 16 cells; a 4-bit comparator would need 256-cell maps. The way you compare numbers by hand avoids them.

:::guess Predict
Comparing 5234 with 5199 by hand: which digit do you look at first, and when do you stop?
:::

:::note Terms
**Bit-equality x_{i} = A_{i} ⊙ B_{i}:** 1 when bit i of A equals bit i of B. **7485:** the standard 4-bit magnitude comparator chip (KB 02 §1).
:::

[[fig:comparator_flow|Comparison from the MSB down: while a bit pair is equal (x_{i} = 1) move one place right; the first pair that differs decides G or L; if all four are equal, E = 1.|w=70]]

The rule: look at the MSBs first. If they differ, they decide and the lower bits do not matter. If they are equal (x_{3} = 1), move to the next bit, and so on. Written as logic:

1. **E:** every bit pair is equal: **E = x_{3}x_{2}x_{1}x_{0}**.
2. **G:** A_{3} = 1, B_{3} = 0; **or** the MSBs are equal and A_{2} = 1, B_{2} = 0; **or** the top two pairs are equal and bit 1 decides; **or** the top three are equal and bit 0 decides:

$$G = A_{3}B_{3}' + x_{3}A_{2}B_{2}' + x_{3}x_{2}A_{1}B_{1}' + x_{3}x_{2}x_{1}A_{0}B_{0}'$$

3. **L:** the same with A and B swapped in each pair:

$$L = A_{3}'B_{3} + x_{3}A_{2}'B_{2} + x_{3}x_{2}A_{1}'B_{1} + x_{3}x_{2}x_{1}A_{0}'B_{0}$$

Read G back: each term is "everything above bit i is equal, and at bit i A has the 1". These are the 7485's equations (KB 02 §1, checked by verify on all 256 pairs). For n = 2 they give G = A_{1}B_{1}' + x_{1}A_{0}B_{0}', which multiplies out to step 6's K-map answer.

**Running example.** A = 0110 (six), B = 0101 (five):

| Bit | A_{i} | B_{i} | x_{i} | |
|---|---|---|---|---|
| 3 | 0 | 0 | 1 | equal: go on |
| 2 | 1 | 1 | 1 | equal: go on |
| 1 | 1 | 0 | 0 | differ, A has the 1: **G = 1** (term x_{3}x_{2}A_{1}B_{1}') |
| 0 | 0 | 1 | — | not looked at |

**Answer to the Predict.** Look at the **most significant digit first** and stop at the **first place where the digits differ**: 5 = 5, then 2 &gt; 1 decides, 5234 &gt; 5199. The 34 and 99 never matter. The comparator does the same, bit by bit.

:::check Check 7
(a) A = 0101, B = 0100: at which bit is it decided, and which output is 1? (b) A = 1001, B = 1011?
:::

### 8 · Wider words: cascading comparators

A 7485 compares 4 bits. Comparing two 8-bit numbers needs two of them, and step 7's rule says how to join them: the low half matters only when the high halves are equal.

:::guess Predict
Two 4-bit comparators compare the high halves and the low halves. When does the low comparator's answer decide the 8-bit result?
:::

:::note Terms
**Cascade inputs I(A&gt;B), I(A=B), I(A&lt;B):** three extra inputs of the 7485 that carry the result of a less significant stage (KB 02 §1).
:::

[[fig:comp_cascade|Two 7485s comparing 8-bit numbers: the right chip compares bits 3–0, its cascade inputs tied to I(A&gt;B) = 0, I(A=B) = 1, I(A&lt;B) = 0; its three outputs feed the cascade inputs of the left chip, which compares bits 7–4 and gives the final result.|w=80]]

Each chip computes its own G, E, L as in step 7 and then:

1. if its own bits differ, its own G or L is the answer (the higher bits decide);
2. if its own bits are all equal, it passes on what its cascade inputs say: G = G_{own} + E_{own}·I(A&gt;B), E = E_{own}·I(A=B), L = L_{own} + E_{own}·I(A&lt;B).

The lowest chip has nothing below it, so its cascade inputs are tied to "equal": **I(A=B) = 1, the other two 0**. Then its outputs are just its own comparison. Verify checks the two-chip circuit on all 65 536 pairs of 8-bit numbers.

**Answer to the Predict.** **Only when the high halves are equal.** Then the high chip passes on the low chip's G, E or L; otherwise the high chip's own result stands.

:::check Check 8
Why must the lowest chip's I(A=B) be 1 and not 0? (What would E be for two equal 8-bit numbers otherwise?)
:::

### 9 · One extra bit: the parity bit

Data sent down a wire or stored in memory can have a bit flipped by noise. The receiver cannot know the right value, but one extra bit lets it notice that something changed.

:::q <span class="tag">MTE 2025 Q2 · 2 marks</span>
The four-bit binary sequence 1011 is applied to an even parity generator circuit. What will be the output?
:::

:::guess Guess first
Count the 1s in 1011. Is the count even already? What bit would you add to make it even?
:::

:::note Terms
**Parity bit P:** one extra bit sent with the data (deck 06 slides 9–10). **Even parity:** P is chosen so that the total number of 1s, data plus P, is even. **Odd parity:** the total is odd (slide 11). **Parity generator:** the circuit that makes P at the sender.
:::

Deck 06 slide 12's table for three data bits X, Y, Z:

| X Y Z | 1s in data | even P | odd P |
|---|---|---|---|
| 000 | 0 | 0 | 1 |
| 001 | 1 | 1 | 0 |
| 010 | 1 | 1 | 0 |
| 011 | 2 | 0 | 1 |
| 100 | 1 | 1 | 0 |
| 101 | 2 | 0 | 1 |
| 110 | 2 | 0 | 1 |
| 111 | 3 | 1 | 0 |

Even P is 1 exactly when the data has an **odd** number of 1s (it adds the missing 1). An XOR chain gives 1 for an odd count of 1s (file 04 step 2 used this for the sum bit), so:

$$P_{even} = X ⊕ Y ⊕ Z      P_{odd} = (X ⊕ Y ⊕ Z)' = X ⊙ (Y ⊕ Z)$$

Read them: the even parity bit is the XOR of all data bits; the odd parity bit is its complement (deck 06 slide 13). Slide 14 calls P = X ⊕ Y ⊕ Z "a 3-input even function"; by slide 18's own definition it is an **odd** function (its 1s are the inputs with an odd number of 1s). Slide 22 states the rule correctly: **the even parity bit is generated by an odd function (XOR), the odd parity bit by an even function (XNOR).**

**Running example.** 0110 has two 1s, already even: P_{even} = 0 ⊕ 1 ⊕ 1 ⊕ 0 = **0**, P_{odd} = **1**.

**Answer to the Guess.** 1011 has **three** 1s, an odd count. The even parity generator adds **P = 1 ⊕ 0 ⊕ 1 ⊕ 1 = 1**, so the word sent, 1011 1, has four 1s: even.

:::check Check 9
(a) Odd parity bit for 1011? (b) Even parity bit for 1000 0001?
:::

### 10 · The 4-bit odd/even generator: chain or tree

Step 9 found P from a table of 8 rows. Practice set 1 Q9 asks for the 4-bit circuit; deck 06 slides 15–17 draw it two ways.

:::q <span class="tag">Practice set 1 Q9</span>
Draw the logic diagram of a 4-bit odd/even parity generator.
:::

:::guess Predict
The K-map of the 4-bit even parity bit has 8 ones. Can any two of them be looped together?
:::

:::note Terms
**Daisy chain:** XOR gates in a line, each adding one more input to the previous result. **Tree:** XOR gates in pairs, then pairs of pairs (slide 15). **Gate delay:** the time one gate takes to respond (file 04 step 6).
:::

The 4-bit even parity bit is 1 for the 8 codes with an odd number of 1s: **m(1, 2, 4, 7, 8, 11, 13, 14)** (deck 06 slide 16). On the K-map these 8 cells form a **checkerboard**: neighbouring cells differ in one bit, so they differ by one in the count of 1s, and one of them is odd, the other even. No two 1s touch, so no loop forms and the SOP has 8 four-letter terms. Slide 16 factors them instead:

$$P_{even} = A ⊕ B ⊕ C ⊕ D      P_{odd} = (A ⊕ B ⊕ C ⊕ D)'$$

Both need **three** 2-input XOR gates (n − 1 for n bits); the odd one adds an inverter at the end, or makes the last gate an XNOR (slide 17).

[[fig:parity_chain_tree|4-bit parity generator two ways (deck 06 slide 15). Top, daisy chain: A ⊕ B, then ⊕ C, then ⊕ D gives P_{even}; an inverter gives P_{odd}; 3 gate delays. Bottom, tree: A ⊕ B and C ⊕ D side by side, then one XOR of the two; 2 gate delays.|w=72]]

The two circuits give the same P (XOR can be regrouped freely), but the signals pass through different numbers of gates:

| | XOR gates | gate delays, 4 bits | gate delays, 8 bits |
|---|---|---|---|
| daisy chain | n − 1 | 3 | 7 |
| tree | n − 1 | 2 | 3 |

The tree's depth grows as log₂ n (each level halves the number of signals), the chain's as n − 1. Same gates, faster circuit.

**Answer to the Predict.** **No.** The 1s sit on a checkerboard, no two adjacent, which is why parity is built from XOR gates and never from a K-map loop.

:::check Check 10
An 8-bit even parity generator built as a tree: how many 2-input XOR gates, and how many gate delays?
:::

### 11 · The parity checker at the receiver

The generator added P. At the far end, the receiver must decide whether the word still has the right parity.

:::q <span class="tag">Deck 06 slide 23 (EX 6.23)</span>
Design an even parity generator and checker for 3-bit codes. (X, Y, Z) = (0, 0, 1) is sent; then Y changes from 0 to 1 on the way. What does the checker output in each case?
:::

:::guess Guess first
The received word should have an even number of 1s. Which single gate function tells "the count of 1s is odd" for all four received bits?
:::

:::note Terms
**Parity checker:** the receiver's circuit; its output E (deck 06 slide 19: PEC, parity error check) is **1 when the parity is wrong**, 0 when it is right.
:::

[[fig:parity_system|EX 6.23 as a system (deck 06 slides 9, 23). Sender: X ⊕ Y, then ⊕ Z, makes P. The four lines X, Y, Z, P cross the link. Receiver: (X ⊕ Y) ⊕ (Z ⊕ P) gives E, 1 when the four received bits hold an odd number of 1s.|w=78]]

With even parity, a correct word has an even count of 1s, so the XOR of **all received bits, P included** is 0. Any odd count gives 1:

$$E = X ⊕ Y ⊕ Z ⊕ P$$

It is the 4-input odd function (slide 22: "to check even parity, use an odd function on the n + 1 bits"); deck 06 slide 21 builds the same thing for P, A, B, C, and slides 24–25 for five bits (E = A ⊕ B ⊕ C ⊕ D ⊕ P). For odd parity the checker uses the complement (an even function, slide 26).

What one parity bit can and cannot do (verify flips every choice of bits in every 3-bit code word):

1. **One bit flipped:** the count of 1s changes by one, from even to odd: **E = 1, caught.**
2. **Two bits flipped:** the count changes by 0 or 2 and stays even: **E = 0, missed.**
3. Three flipped: caught again. Any odd number of errors is caught, any even number missed.
4. Even when E = 1, the checker cannot say **which** bit is wrong. Locating it needs more check bits (Hamming codes, beyond this course).

**Answer to the Guess.** **XOR of all four bits.** (0, 0, 1) gives P = 0 ⊕ 0 ⊕ 1 = 1; the word 0011 arrives with two 1s and **E = 0 ⊕ 0 ⊕ 1 ⊕ 1 = 0**: no error. With Y flipped, 0111 arrives with three 1s: **E = 1**, error detected (slide 23).

:::check Check 11
(a) Even parity: data 1001 arrives with parity bit 1. Is there an error? (b) The word 0011 is sent and both X and Y flip. What does the checker say?
:::

---

## Exam form

**BCD to 7-segment (PS1 Q10).** Segment diagram with names a–g. Truth table for 0–9 with codes 10–15 as X. One K-map per segment (seven maps), minimal SOPs (step 2 table). Common anode: outputs active-low, either invert the seven outputs or loop the 0s (step 3 table); a resistor in each segment line. Say which shapes you used for 6, 7, 9.

**Multiplexed display.** Shared segment lines, one enable per digit, digits lit in turn faster than the eye follows; 7 + N lines.

**Comparator (deck 06).** 1-bit: G = AB', L = A'B, E = A ⊙ B, circuit with two ANDs and an XNOR. 2-bit: 16-row table, K-maps for G and L, E = (A_{1} ⊙ B_{1})(A_{0} ⊙ B_{0}), circuit. n-bit: x_{i}, the four-term G and L, E = product of x's; cascading with the lowest stage's I(A=B) = 1.

**Parity (MTE Q2, PS1 Q9).** Count the 1s; P_{even} = XOR of the data bits, P_{odd} its complement. 4-bit generator: three XORs (chain or tree), inverter for odd. Checker: XOR of data and P; E = 1 means error; detects odd numbers of errors only, cannot locate them.

## Traps

- Deck 05 slide 28 calls the MSB D and the LSB A; this file (and file 02) calls the MSB A. Translate before reusing slide equations.
- Forgetting the don't-cares 10–15 in the segment maps (much longer equations).
- Common anode lights on **0**: the step 2 equations are for common cathode.
- Comparing from the LSB: the MSB decides first.
- Tying the lowest cascade stage's I(A=B) to 0: then E is never 1.
- Even parity **bit** = XOR (an odd function); odd parity bit = XNOR. Slide 14's wording mixes them up.
- A parity checker that gives E = 0 does not prove the word is right: two flipped bits pass unseen.

## Self-test

1. Which segments light for 5?
2. Odd parity bit for 1101001?
3. A 2-bit comparator gets A = 10, B = 11. Which output is 1?
4. An even-parity checker receives 10110 (parity bit included). Error?
5. A 4-digit multiplexed display needs how many lines?
6. Write the common-anode (active-low) expression for segment e, and say which digits it keeps dark.

<!--ANSWERS-->

## Answers

**Check 1.** (a) **b, c, f, g** (four bars). (b) **1**: bars **b and c**.

**Check 2.** (a) Code 14 is never sent to a BCD decoder; it is a don't-care, and the K-map used it to make the loop B bigger. (b) **0, 2, 6, 8**.

**Check 3.** (a) 7 lights a, b, c: a … g = **0 0 0 1 1 1 1** (0 = lit). (b) Only **2**: the one digit with c dark.

**Check 4.** **11** with multiplexing (7 + 4), **28** without (4 × 7).

**Check 5.** (a) **E = 1**, G = L = 0. (b) E is 1 when the bits agree, which is the XNOR's definition: one gate.

**Check 6.** (a) **G = 1**. A_{1} = B_{1} = 1, so A_{1}B_{1}' = 0 and A_{0}B_{1}'B_{0}' = 0; **A_{1}A_{0}B_{0}' = 1·1·1 = 1**: bit 0 decides. (b) **One NOR**: L = (G + E)'.

**Check 7.** (a) Bits 3–1 are equal; **bit 0** decides (A_{0} = 1, B_{0} = 0): **G = 1**. (b) Bits 3 and 2 equal; **bit 1** decides (A_{1} = 0, B_{1} = 1): **L = 1** (nine &lt; eleven).

**Check 8.** For two equal 8-bit numbers both chips see equal bits, so each passes on its cascade E. If the lowest I(A=B) were 0, E = E_{own}·0 = 0 all the way up and **no output would be 1**. Tied to 1, E = 1 as it should be.

**Check 9.** (a) **0**: three 1s, already odd. (b) Two 1s, already even: **P = 0**.

**Check 10.** **7** XOR gates (n − 1), **3** gate delays (8 → 4 → 2 → 1 signals).

**Check 11.** (a) Four received bits 1, 0, 0, 1 plus P = 1: three 1s, odd: **E = 1, error**. (b) 1111 arrives: four 1s, even: **E = 0**, the two errors are **missed**.

**Self-test.**

1. **a, c, d, f, g** (b and e dark).
2. Four 1s, already even: odd parity bit **1**.
3. **L** (A = 2 &lt; B = 3; bit 1 equal, bit 0 decides).
4. Three 1s: odd, **E = 1, error**.
5. 7 + 4 = **11** (28 without multiplexing).
6. **e' = D + BC'**: dark for every odd digit (D = 1: 1, 3, 5, 7, 9) and for 4 (B = 1, C = 0); lit for 0, 2, 6, 8.

<!--/ANSWERS-->
