# 06 — Decoder and encoder

<div class="sub">Deck 05 (slides 2–43) · syllabus Unit 2 (decoder, encoder, priority encoder, function realisation) · 3 real questions: MTE 2025 Q6 (4 marks), practice set 1 Q7, Q8 · needs 01 step 7 (minterms, Σm and ΠM), 03 step 1 (NAND/NOR), 05 steps 2, 9, 10 (select minterms, enable, demultiplexer)</div>

## Map

[[map:1 2:4 decoder > 2 3:8 decoder > 3 Enable, active-low > 4 Bigger decoders > 5 Decoder + OR > 6 MTE Q6 full adder > 7 Zeros: NOR, AND > 8 Four variables > 9 Encoder > 10 Priority encoder|here=1]]

File 05's demultiplexer sent one data bit to the output named by the select code. Drop the data bit and keep only the naming: a **decoder** turns an n-bit code into one active line out of 2^{n}. Each line is one minterm, so a decoder plus an OR gate realises any function, which is how MTE Q6 builds a full adder. The file ends with the **encoder**, the decoder run backwards. Decoders return in file 07 (BCD to 7-segment) and in file 19 (memory address decoding).

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| A, B / x, y, z / w | decoder code inputs (the binary number); the first listed is the most significant bit | — |
| D_{j} (or W, X, Y, Z) | decoder output j: 1 only when the input code is j; it is minterm m_{j} | one of 2^{n} is 1 |
| En, E | enable: when inactive, no output is active | high or low level |
| active-low | a signal whose "on" value is 0; drawn with a bubble, written with a bar or a prime | 74138 outputs |
| D_{0} … D_{7} (encoder) | encoder inputs: the lines, one of which is expected to be 1 | — |
| x, y, z / y_{1}, y_{0} | encoder outputs: the binary number of the active input | — |
| V | valid output: 1 when at least one encoder input is 1 | 0 or 1 |

## Running example

**MTE 2025 Q6: the full adder** (inputs x, y and carry-in z; sum S = Σm(1, 2, 4, 7), carry C = Σm(3, 5, 6, 7), file 04). Step 6 builds it from a 3:8 decoder, then from two 2:4 decoders; step 6's Check reads it on one input row.

## The questions this file answers

- <span class="tag">MTE 2025 Q6 · 4 marks</span> Design Full Adder using suitable decoder.
- <span class="tag">Practice set 1 Q7</span> Realize the Boolean function Y = ΠM(0, 3, 5, 6, 7) with a Decoder and one NOR gate.
- <span class="tag">Practice set 1 Q8</span> Implement the following function using suitable decoder. F(a, b, c, d) = Σm(0, 1, 2, 5, 6, 8, 9, 15)
- <span class="tag">Deck 05 slides 14–26, 36–43</span> Decoder cascading (EX 5.14–5.16), decoder function realisation (EX 5.18–5.26), the 4-to-2 priority encoder.

---

## Build

### 1 · The 2:4 decoder: a code lights one line

A lift has four floors and a 2-bit floor code. Above the doors, four lamps; exactly the lamp whose number the code spells is lit.

:::q <span class="tag">Deck 05 slides 6–7</span>
Draw the 2-to-4 active-high decoder: block, truth table and output equations.
:::

:::guess Guess first
Inputs A (most significant) and B. Write the condition "the code is 10" as one AND term in A and B.
:::

:::note Terms
**Decoder (n-to-2^{n}):** n code inputs, 2^{n} outputs; output j is 1 exactly when the input code equals j, all others 0. **Active-high output:** the selected output is the one at 1 (the others at 0).
:::

| A B | W = D_{0} | X = D_{1} | Y = D_{2} | Z = D_{3} |
|---|---|---|---|---|
| 0 0 | 1 | 0 | 0 | 0 |
| 0 1 | 0 | 1 | 0 | 0 |
| 1 0 | 0 | 0 | 1 | 0 |
| 1 1 | 0 | 0 | 0 | 1 |

Each output is 1 on one row only, so each is one minterm (file 01 step 7):

$$W = A'B'      X = A'B      Y = AB'      Z = AB$$

Read it: "Y is 1 when A is 1 **and** B is 0, that is, when the code is 10". Gates: two inverters and four 2-input ANDs.

**Answer to the Guess.** **AB'** (output Y = D_{2}).

:::check Check 1
Inputs A = 0, B = 1. Which output is 1, and what are the other three?
:::

### 2 · The 3:8 decoder: every output is a minterm

Step 1 used 2 bits. With 3 bits the same idea gives 8 outputs, and the claim "output j = minterm m_{j}" becomes the tool for the rest of the file.

:::guess Predict
A 3:8 decoder has inputs x, y, z (x most significant). Which output is 1 for xyz = 101, and what is its equation?
:::

| Output | D_{0} | D_{1} | D_{2} | D_{3} | D_{4} | D_{5} | D_{6} | D_{7} |
|---|---|---|---|---|---|---|---|---|
| Equation (slide 9) | x'y'z' | x'y'z | x'yz' | x'yz | xy'z' | xy'z | xyz' | xyz |
| 1 only on row | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

Gates: three inverters and eight 3-input ANDs, one per minterm. In general an n-to-2^{n} decoder is **every minterm of n variables at once**: D_{j} = m_{j}.

Slide 4 shows why the block exists: an 8:3 encoder at the sender squeezes 8 lines into 3 wires, and a 3:8 decoder at the receiver opens them back into 8.

**Answer to the Predict.** 101 = 5: **D_{5} = xy'z** is 1, all others 0.

:::check Check 2
Which 3:8 output is 1 for xyz = 011? Write its equation.
:::

### 3 · Enable and active-low outputs

Step 2's decoder always lights one line. Cascading decoders (step 4) and using one as a demultiplexer (file 05 step 10) need a pin that switches all lines off.

:::q <span class="tag">Deck 05 slides 10–13</span>
Draw the 2-to-4 decoder with an enable, first with a high-level enable, then with active-low outputs and an active-low enable (NAND version).
:::

:::guess Guess first
In the NAND version the selected output is the one at **0**. With the enable switched off, what do all four outputs show?
:::

:::note Terms
**Enable En:** a control input; while it is inactive no output is active. **High-level (active-high) enable:** works when En = 1. **Low-level (active-low) enable E':** works when E' = 0. **Active-low output:** the selected output is 0 and the rest are 1.
:::

1. **High-level enable (slide 11).** Each AND gets En as one more input: W = En·A'B', …, Z = En·AB. En = 0 → all outputs 0.
2. **Active-low outputs, active-low enable (slide 13).** Each output is a NAND of E (inverted), and the code literals: D_{0} = (E'A'B')', …. With E = 1 every NAND sees a 0 and outputs 1: all off. With E = 0, only the NAND whose code matches outputs 0.

| E | A B | D_{0} D_{1} D_{2} D_{3} |
|---|---|---|
| 1 | X X | 1 1 1 1 |
| 0 | 0 0 | 0 1 1 1 |
| 0 | 0 1 | 1 0 1 1 |
| 0 | 1 0 | 1 1 0 1 |
| 0 | 1 1 | 1 1 1 0 |

An X on the input side means "either value".

**The decoder with enable is a demultiplexer.** Feed the data bit D into En: the output named by A B copies D, the others stay off. That is file 05 step 10's Y_{j} = D·m_{j}.

**Answer to the Guess.** **1 1 1 1**: "off" for an active-low output is 1.

:::note Note
Deck 05 slides 44–48 (the tri-state buffer: output = input when enabled, disconnected, "high impedance", when not) are taught with the logic families in file 18.
:::

:::check Check 3
The slide-13 decoder has E = 0, A = 1, B = 0. Give D_{0}, D_{1}, D_{2}, D_{3}.
:::

### 4 · Bigger decoders from smaller ones

Step 3's enable is what makes this work: the extra input bit decides which small decoder is allowed to light a line.

:::q <span class="tag">Deck 05 slides 14–15 (EX 5.14, 5.15)</span>
Build a 4×16 decoder using 3×8 decoders; then using 2×4 decoders.
:::

:::guess Guess first
Two 3:8 decoders share x, y, z. The fourth bit w (most significant) must enable exactly one of them. What goes to each enable?
:::

[[fig:u2_dec416|4:16 decoder from two 3:8 decoders: x, y, z go to both; w' enables the top decoder (outputs D0–D7), w enables the bottom one (D8–D15).|w=52]]

1. Codes 0–7 have w = 0; codes 8–15 have w = 1. The low three bits xyz are the position inside each half.
2. Top decoder: EN = **w'** (one inverter), so it works for codes 0–7.
3. Bottom decoder: EN = **w**, so it works for codes 8–15; its output j is overall output 8 + j.
4. **With 2:4 decoders (slide 15):** a first 2:4 on the two most significant bits w_{3}w_{2} drives the enables of four second-stage 2:4 decoders, each fed w_{1}w_{0}: **five** 2:4 decoders, no inverter.

**Answer to the Guess.** Top: **w'**; bottom: **w**.

:::check Check 4
(a) How many 2:4 decoders does a 4:16 decoder take in the slide-15 layout? (b) How many 3:8 decoders make a 5:32 decoder, and what drives their enables?
:::

### 5 · Decoder + OR: any function from its minterm list

Step 2 said output j is minterm m_{j}. A function in Σm form is an OR of minterms, so it is an OR of decoder outputs.

:::q <span class="tag">Deck 05 slides 18, 20 (EX 5.18, 5.20)</span>
Realise F = Σm(0, 2) with a 2:4 decoder. Then: design a circuit, using a 3-to-8 Decoder to realize F(X, Y, Z) = Σm(1, 2, 5, 7).
:::

:::guess Guess first
F = Σm(0, 2) with inputs A, B. Which two decoder outputs go into the OR gate? Simplify the result.
:::

[[fig:u2_sl18|Slide 18 solved: a 2:4 decoder on A (MSB) and B; outputs 0 and 2 go into an OR gate, so F = A'B' + AB' = B'.|w=48]]

**Recipe.**

1. Decoder with one input per variable, the most significant variable on the most significant input.
2. One OR gate per output function; its inputs are the decoder outputs numbered in that function's Σm list.
3. Several functions of the same variables share **one** decoder; each gets its own OR.

**Answer.** Σm(0, 2): **OR of D_{0}, D_{2}** = A'B' + AB' = **B'**. Σm(1, 2, 5, 7): **3:8 decoder (X MSB), 4-input OR of D_{1}, D_{2}, D_{5}, D_{7}**.

:::note Slip in the slides
Slide 18's block diagram wires A_{0} = Y and A_{1} = X, while its table names the inputs A, B. The pack uses the table (A most significant). With the slide's wiring the same OR gives Y'.
:::

:::check Check 5
(a) <span class="tag">Deck 05 slide 26 (EX 5.26)</span> Realise F(X, Y, Z) = Σm(1, 2, 5, 7) with two 2:4 decoders, X, Y on their code inputs and Z on the enables (decoder A enabled by Z', decoder B by Z). Which outputs go into the OR? (b) <span class="tag">Deck 05 slide 21</span> Design a half adder with one 2:4 decoder.
:::

### 6 · MTE Q6: the full adder from a decoder

Step 5's recipe with two functions of the same three variables.

:::q <span class="tag">MTE 2025 Q6 · 4 marks</span>
Design Full Adder using suitable decoder.
:::

:::guess Guess first
A full adder has three inputs and two outputs. Which decoder size, and how many OR gates?
:::

1. Inputs x, y, z (z = carry in): three variables → **3:8 decoder**, x on the most significant input.
2. Truth table (file 04): S = 1 when an odd number of inputs is 1 → **S = Σm(1, 2, 4, 7)**; C = 1 when two or more are 1 → **C = Σm(3, 5, 6, 7)**.
3. One 4-input OR per output (step 5's recipe); D_{7} feeds both. D_{0} is unused.

[[fig:u2_fa_dec|MTE Q6 / deck 05 slide 22: a 3:8 decoder on x, y, z; outputs 1, 2, 4, 7 into the OR that makes S; outputs 3, 5, 6, 7 into the OR that makes C.|w=62]]

**With two 2:4 decoders (slide 23).** The most significant bit A_{2} goes to the enables (A_{2}' on the first, A_{2} on the second), as in step 4; together they are one 3:8 decoder (D_{0}–D_{3} and D_{4}–D_{7}), and the same two ORs follow.

**Answer.** **3:8 decoder; S = D_{1} + D_{2} + D_{4} + D_{7}; C = D_{3} + D_{5} + D_{6} + D_{7}** (two 4-input ORs). For full marks: the truth table, both Σm lists, and the circuit.

:::check Check 6
On the row x y z = 1 1 0: which decoder output is 1, and what are S and C?
:::

### 7 · Using the zeros: NOR, and active-low outputs with AND

Step 6 ORed the rows where F = 1. A function given as ΠM lists its rows where F = 0; the decoder handles it without converting.

:::q <span class="tag">Practice set 1 Q7</span>
Realize the Boolean function Y = ΠM(0, 3, 5, 6, 7) with a Decoder and one NOR gate.
:::

:::guess Guess first
The OR of D_{0}, D_{3}, D_{5}, D_{6}, D_{7} is 1 exactly where Y = 0. What does a NOR of the same five outputs give?
:::

[[fig:u2_ps1q7|Practice set 1 Q7: a 3:8 decoder on A, B, C; outputs 0, 3, 5, 6, 7 (the maxterm rows) into one NOR gate.|w=60]]

1. OR(D_{0}, D_{3}, D_{5}, D_{6}, D_{7}) = 1 on rows 0, 3, 5, 6, 7 = **Y'**.
2. NOR = NOT of that OR = **Y**.
3. Y is 1 on the remaining rows: Y = ΠM(0, 3, 5, 6, 7) = **Σm(1, 2, 4)**.

The four ways to finish a decoder circuit:

| Decoder outputs | Feed the rows where F = 1 into | Feed the rows where F = 0 into |
|---|---|---|
| active-high | OR | NOR |
| active-low (74138) | NAND | AND |

Active-low outputs are complemented minterms m_{j}'; NAND(m_{1}', m_{2}', m_{4}') = m_{1} + m_{2} + m_{4} by De Morgan (file 01 step 5), so NAND plays the OR's role. Pick the column with fewer rows: it gives the smaller gate.

**Answer.** **3:8 decoder (A MSB) and one 5-input NOR of D_{0}, D_{3}, D_{5}, D_{6}, D_{7}**; Y = Σm(1, 2, 4).

:::check Check 7
<span class="tag">Deck 05 slides 24–25 (EX 5.24)</span> Realise f_{1}(x_{2}, x_{1}, x_{0}) = ΠM(0, 3, 5) and f_{2} = ΠM(2, 3, 4) with one 3:8 decoder with active-low outputs and two AND gates. Which outputs feed each AND?
:::

### 8 · A four-variable function: build the decoder first

Practice set 1 Q8 has four variables, so it needs a 4:16 decoder, which step 4 builds from two 3:8s.

:::q <span class="tag">Practice set 1 Q8</span>
Implement the following function using suitable decoder. F(a, b, c, d) = Σm(0, 1, 2, 5, 6, 8, 9, 15)
:::

:::guess Guess first
F has 8 ones out of 16 rows. Is an OR of the 1-rows cheaper than a NOR of the 0-rows here?
:::

1. Four variables → **4:16 decoder**: two 3:8 decoders, b c d on both, **a' on the first enable, a on the second** (step 4's figure with w = a).
2. Outputs 0–7 come from the first decoder, 8–15 from the second (output j of the second is overall 8 + j).
3. OR the outputs in the list: **0, 1, 2, 5, 6** (first decoder) and **8, 9, 15** (second decoder's 0, 1, 7).

**Answer.** Two 3:8 decoders (enables a', a) and **one 8-input OR of outputs 0, 1, 2, 5, 6, 8, 9, 15**. Answer to the Guess: neither: 8 ones and 8 zeros, so the OR and the NOR both need 8 inputs.

:::check Check 8
How many ones and zeros does F have, and how many inputs would the NOR version's gate need?
:::

### 9 · The encoder: the decoder run backwards

A keypad has ten keys but sends a 4-bit code (slide 35). The block that turns "which line is on" into a binary number is an encoder.

:::q <span class="tag">Deck 05 slides 36–37</span>
Draw the 4-to-2 encoder; write the output equations of the 8-to-3 (octal-to-binary) encoder.
:::

:::guess Guess first
In a 4:2 encoder, output y_{1} is the high bit of the active input's number. For which inputs (w_{0} … w_{3}) is it 1?
:::

:::note Terms
**Encoder (2^{n}-to-n):** 2^{n} inputs, of which exactly **one** is assumed to be 1; the n outputs give that input's number in binary.
:::

[[fig:u2_enc42|The 4:2 encoder: y1 = w3 + w2, y0 = w3 + w1. w0 is not wired: its code is 00, the same as "no input".|w=52]]

Each output bit is 1 for the inputs whose number has a 1 in that position, so each is an OR:

| Encoder | Outputs |
|---|---|
| 4:2 | y_{1} = w_{2} + w_{3} · y_{0} = w_{1} + w_{3} |
| 8:3 | x = D_{4} + D_{5} + D_{6} + D_{7} · y = D_{2} + D_{3} + D_{6} + D_{7} · z = D_{1} + D_{3} + D_{5} + D_{7} |

**The two faults (slide 33's questions).**

1. **Two inputs on.** D_{3} and D_{6} together: x = 1, y = 1, z = 1 → **111 = 7**, a key nobody pressed.
2. **No input on.** All ORs give **000**, the same as D_{0} alone.

**Answer to the Guess.** w_{2} and w_{3} (numbers 10 and 11): **y_{1} = w_{2} + w_{3}**.

:::check Check 9
An 8:3 encoder has only D_{5} active. Give x y z, and say which three ORs produced the 1s.
:::

### 10 · The priority encoder and the valid bit

Step 9's two faults are fixed by two rules: the highest active input wins, and a separate output says whether any input is active.

:::q <span class="tag">Deck 05 slides 38–43</span>
Design a 4-to-2 priority encoder with a valid output: truth table, K-maps, circuit.
:::

:::guess Guess first
D_{1} and D_{2} are both 1 (D_{3} = 0). Which number must come out, and how must the equation for the low bit y stop D_{1} from setting it?
:::

:::note Terms
**Priority encoder:** when several inputs are 1, outputs the number of the **highest** one. **Valid bit V:** 1 when at least one input is 1; V = 0 marks the output as meaningless (no input).
:::

| D_{3} D_{2} D_{1} D_{0} | x y | V |
|---|---|---|
| 0 0 0 0 | X X | 0 |
| 0 0 0 1 | 0 0 | 1 |
| 0 0 1 X | 0 1 | 1 |
| 0 1 X X | 1 0 | 1 |
| 1 X X X | 1 1 | 1 |

Each X row stands for several rows: once D_{3} = 1 the lower inputs do not matter. The output X X with V = 0 is a don't-care, since V already says "ignore x y".

[[fig:u2_prio_km|What these maps plot: x (left) and y (right) of the priority encoder. Rows D3 D2, columns D1 D0; a cell is one input combination; X at cell 0 is the don't-care (no input). Groups: x = D2 + D3; y = D3 + D1D2'.|w=70]]

1. x = 1 when D_{2} or D_{3} wins: **x = D_{2} + D_{3}**.
2. y = 1 when D_{3} wins, or D_{1} wins (D_{1} = 1 and D_{2} = 0, D_{3} = 0): y = D_{3} + D_{1}D_{2}'D_{3}'; the map drops D_{3}' (D_{3} + D_{3}'P = D_{3} + P): **y = D_{3} + D_{1}D_{2}'**.
3. **V = D_{0} + D_{1} + D_{2} + D_{3}**.

The D_{2}' in y is the priority: D_{1} counts only when D_{2} is off.

:::note Slip in the slides
Slide 39 names the valid bit **d**; slides 40–43 call it **V**. The pack uses V. Slide 42's maps put D_{0}D_{1} on the rows and D_{2}D_{3} on the columns; the pack's maps put the most significant inputs D_{3}D_{2} on the rows. Same groups, same equations.
:::

**Answer to the Guess.** D_{2} wins: **x y = 1 0**. The term D_{1}D_{2}' is 0 because D_{2} = 1, so y stays 0.

:::check Check 10
D_{0} = D_{1} = D_{2} = 1, D_{3} = 0. Give x, y, V.
:::

---

## Exam form

**Decoder.** Block · truth table · D_{j} = m_{j} (2:4: W = A'B', X = A'B, Y = AB', Z = AB) · gates: inverters + 2^{n} ANDs (NANDs for active-low).

**Function from a decoder** (MTE Q6 recipe, 4 marks):

1. Truth table → Σm list for each output (full adder: S = Σm(1, 2, 4, 7), C = Σm(3, 5, 6, 7)).
2. Decoder size = number of variables; MSB on the top input.
3. One OR per output on its Σm outputs (NOR on ΠM rows; NAND / AND for active-low outputs).
4. Draw it, label every output number.

**Expansion.** 4:16 = two 3:8 + enables w', w (or five 2:4: first stage on the two MSBs drives the enables).

**Priority encoder (4:2).** Table with X rows · x = D_{2} + D_{3} · y = D_{3} + D_{1}D_{2}' · V = D_{0} + D_{1} + D_{2} + D_{3} · why priority and V.

## Traps

- ORing active-low outputs: active-low needs NAND (rows where F = 1) or AND (rows where F = 0).
- ΠM with a NOR: NOR the **maxterm** rows (F = 0), not the Σm rows.
- Putting the least significant variable on the decoder's MSB input: the output numbers no longer match the minterm numbers.
- Building 4:16 with both enables tied to w: one needs w'.
- Plain encoder with two inputs active: the output is the OR of both codes, not either one.
- Forgetting V: without it, "D_{0} only" and "nothing" both give 00.

## Self-test

1. Write y_{2}, y_{1}, y_{0} of an 8-to-3 priority encoder (D_{7} highest).
2. Slide 18's wiring: A_{1} = X, A_{0} = Y on a 2:4 decoder, OR of outputs 0 and 2. What is F?
3. Realise practice set 1 Q7's Y = ΠM(0, 3, 5, 6, 7) with an active-low 3:8 decoder and one NAND gate.
4. A 4:2 priority encoder has only D_{0} active. Give x, y, V. What changes if no input is active?
5. A full adder from a 3:8 decoder: why is output D_{0} not connected?
6. Why does a priority encoder need the V output? Answer in one line.

<!--ANSWERS-->

## Answers

**Check 1.** Code 01: **X = D_{1} = 1**; W, Y, Z = **0**.

**Check 2.** 011 = 3: **D_{3} = x'yz**.

**Check 3.** Selected code 10 → D_{2} = 0: **D_{0} D_{1} D_{2} D_{3} = 1 1 0 1**.

**Check 4.** (a) **Five** (one first stage, four second stage). (b) **Four** 3:8 decoders; their enables come from a **2:4 decoder** on the two most significant bits (each 2:4 output enables one 3:8).

**Check 5.** (a) Minterm number = 4X + 2Y + Z. m_{1} = 001 → Z = 1, XY = 00 → **B0**; m_{2} = 010 → Z = 0, XY = 01 → **A1**; m_{5} = 101 → **B2**; m_{7} = 111 → **B3**. F = **A1 + B0 + B2 + B3** (one 4-input OR). (b) Inputs A, B: sum S = Σm(1, 2) → **OR of D_{1}, D_{2}**; carry C = Σm(3) → **D_{3} directly**, no gate.

**Check 6.** 110 = 6: **D_{6} = 1**. 6 is not in S's list (1, 2, 4, 7): **S = 0**; 6 is in C's list (3, 5, 6, 7): **C = 1**. (1 + 1 + 0 = 10 in binary.)

**Check 7.** Active-low outputs + AND uses the rows where f = 0: **f_{1} = AND of outputs 0, 3, 5**; **f_{2} = AND of outputs 2, 3, 4**.

**Check 8.** **8 ones, 8 zeros**; the NOR would also need **8 inputs** (outputs 3, 4, 7, 10, 11, 12, 13, 14).

**Check 9.** 5 = 101: **x y z = 1 0 1**. x's OR (D_{4} + D_{5} + D_{6} + D_{7}) and z's OR (D_{1} + D_{3} + D_{5} + D_{7}) contain D_{5}; y's does not.

**Check 10.** Highest active is D_{2}: **x = 1, y = 0, V = 1** (y: D_{3} = 0 and D_{1}D_{2}' = 1·0 = 0).

**Self-test.**

1. **y_{2} = D_{4} + D_{5} + D_{6} + D_{7}**; **y_{1} = D_{7} + D_{6} + D_{5}'D_{4}'(D_{3} + D_{2})**; **y_{0} = D_{7} + D_{6}'D_{5} + D_{6}'D_{4}'D_{3} + D_{6}'D_{4}'D_{2}'D_{1}**. (Each lower input counts only when every higher input that would change that bit is off.)
2. Outputs 0, 2 are codes XY = 00, 10: X'Y' + XY' = **Y'**.
3. Y is 1 on rows 1, 2, 4: **one 3-input NAND of active-low outputs 1, 2, 4** (NAND of m_{1}', m_{2}', m_{4}' = m_{1} + m_{2} + m_{4}).
4. D_{0} only: **x = 0, y = 0, V = 1**. No input: x y = 0 0 too, but **V = 0**, so the output is marked invalid.
5. Row 0 (x = y = z = 0) has S = 0 and C = 0: minterm 0 is in neither list.
6. Without V, "only D_{0} active" and "no input active" give the same output 00.

<!--/ANSWERS-->
