# 05 — Multiplexer and demultiplexer

<div class="sub">Deck 04 (slides 3–39) · syllabus Unit 2 (multiplexer, demultiplexer, function generation) · 4 real questions: MTE 2025 Q5 (4 marks), practice set 1 Q3, Q5, Q6 · needs 01 step 7 (minterms, Σm), 02 (K-map pairs), 03 step 1 (gates)</div>

## Map

[[map:1 2:1 MUX > 2 4:1 MUX, select count > 3 n variables on 2ⁿ:1 > 4 n variables on 2ⁿ⁻¹:1 > 5 MTE Q5 on 8:1 > 6 Two variables left over > 7 MUX tree > 8 Only 4:1 MUXes > 9 Enable, 74LS151 > 10 Demultiplexer|here=1]]

Files 01–03 built every circuit gate by gate from a minimal expression. Some blocks are needed so often that they are sold as one chip (medium-scale integration, MSI). This file teaches the first of them, the **multiplexer (MUX)**: a switch that a binary number turns. It ends with the switch run backwards, the **demultiplexer**. File 06 builds the decoder, which is a demultiplexer seen from another side, and file 08 uses MUXes inside the shifter and ALU.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| I_{0}, I_{1}, … | data inputs: the signals the MUX chooses between; I_{j} is the one passed when the select code is j | 0, 1, a variable, or its complement |
| S, S_{1}, S_{0} | select lines: a binary number (S_{1} the more significant bit) that says which data input reaches the output | — |
| n | number of select lines; a MUX with n selects has 2^{n} data inputs (a 2^{n}:1 MUX) | 1, 2, 3 |
| Y, Z, F | the MUX output; F when the MUX realises a function | — |
| residue | what F does on the rows that share one select code, written in the variables left off the selects | 0, 1, D, D' |
| G' | active-low enable (strobe): 0 lets the MUX work, 1 forces its output Y to 0 | tied to 0 |
| D, Y_{j} | in a demultiplexer: the one data input D and the outputs Y_{0} … Y_{3} it is routed to | — |

## Running example

**MTE 2025 Q5: F(P, Q, R, S) = Σm(0, 1, 3, 4, 8, 9, 10, 11, 13, 15).** Step 5 puts it on one 8:1 MUX, step 6's Check on one 4:1 MUX, step 8's Check on 4:1 MUXes only.

## The questions this file answers

- <span class="tag">MTE 2025 Q5 · 4 marks</span> Implement the following function using single 8:1 Multiplexer. F(P, Q, R, S) = Σm(0, 1, 3, 4, 8, 9, 10, 11, 13, 15)
- <span class="tag">Practice set 1 Q3</span> Implement the following Boolean Function Using 8:1 Multiplexer. F(a, b, c, d) = Σm(0, 1, 3, 5, 7, 9, 15)
- <span class="tag">Practice set 1 Q5</span> Design a combinational circuit to implement the following Boolean function using only 4:1 Multiplexer. Take 'D' as input variable. F(A, B, C, D) = Σm(0, 2, 7, 8, 9, 11, 13, 14, 15)
- <span class="tag">Practice set 1 Q6</span> Implement the following Boolean Function Using 8:1 Multiplexer. F(P, Q, R, S) = Σm(0, 2, 5, 9, 11, 12, 14, 15)
- <span class="tag">Deck 04 slides 13–29</span> Function generation on 8:1 and 4:1 MUXes (EX 4.13–4.24); MUX trees; the 74LS151.

---

## Build

### 1 · The 2:1 MUX: a switch turned by one bit

A home cinema amplifier has one speaker output and a button that picks the source: the TV or the music player. The button does not carry sound; it only decides which source reaches the speaker.

:::q <span class="tag">Deck 04 slides 5–8</span>
Design a 2×1 MUX: block diagram, truth table, and the gate circuit.
:::

:::guess Guess first
The output equals I_{0} when S = 0 and I_{1} when S = 1. Write that sentence as one Boolean expression.
:::

:::note Terms
**Data input** I_{0}, I_{1}: the signals that can reach the output (the sources). **Select line** S: the one bit that decides which data input is passed; nothing else about it reaches the output. **Multiplexer (data selector):** the block that passes exactly the data input whose number the select lines spell.
:::

[[fig:u2_mux21|Left: the 2:1 MUX block (data inputs I0, I1, select S, output Z). Right: its gates. S' opens the lower AND for I0, S opens the upper AND for I1, and the OR passes whichever is open.|w=78]]

"Z = I_{0} when S = 0, Z = I_{1} when S = 1" becomes one SOP, one term per case:

$$Z = S'I_{0} + SI_{1}$$

Read it in words: the term S'I_{0} is "S is 0 **and** I_{0} is 1"; the term SI_{1} is "S is 1 **and** I_{1} is 1". Exactly one of S', S is 1, so exactly one AND gate is open at a time.

Slide 6's truth table lists all 8 rows of (S, D_{1}, D_{0}); the output is 1 on rows 1, 3, 6, 7: D_{0} where S = 0, D_{1} where S = 1.

:::note Slip in the slides
Deck 04 slide 7 draws the K-map of this table with 1s in cells 2, 3, 5, 7 (rows D_{0}, columns SD_{1}). The table on slide 6 and the formula O = S'D_{0} + SD_{1} put the 1s at rows 1, 3, 6, 7. The pack uses the table and the formula.
:::

**Answer.** Block: two data inputs, one select, one output. Equation **Z = S'I_{0} + SI_{1}**. Gates: an inverter for S', two 2-input ANDs (S'·I_{0} and S·I_{1}), one 2-input OR.

:::check Check 1
(a) Tie I_{0} = 0 and I_{1} = 1. What function of S is Z? (b) Tie I_{0} = 1 and I_{1} = 0. What is Z now?
:::

### 2 · The 4:1 MUX, and how many select lines

One select bit chooses between two inputs. More inputs need a longer select number.

:::guess Predict
A MUX has 16 data inputs. How many select lines does it need? And 32?
:::

:::note Terms
**n select lines** spell a number from 0 to 2^{n} − 1, so they can name 2^{n} data inputs: a **2^{n}:1 MUX**. **Minterm of the selects:** S_{1}'S_{0}' is 1 only for code 00, S_{1}'S_{0} only for 01, and so on (file 01 step 7).
:::

[[fig:u2_mux41|The 4:1 MUX: data inputs I0–I3, selects S1 (more significant) and S0, output Y.|w=40]]

Step 1's equation extends with one AND term per data input: data input I_{j} is ANDed with the select minterm m_{j}.

$$Y = S_{1}'S_{0}'I_{0} + S_{1}'S_{0}I_{1} + S_{1}S_{0}'I_{2} + S_{1}S_{0}I_{3}$$

Read it: "select code 00 opens I_{0}'s gate, 01 opens I_{1}'s, 10 opens I_{2}'s, 11 opens I_{3}'s". In the general form, Y = Σ m_{j}·I_{j}: every select minterm gates one input.

| Select code S_{1}S_{0} | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| Y | I_{0} | I_{1} | I_{2} | I_{3} |

Uses (slide 11): many computers sharing one line, choosing one radio channel, routing data inside a processor, and **function generation**, which is the rest of this file.

**Answer to the Predict.** 2^{n} = 16 gives **n = 4**; 2^{n} = 32 gives **n = 5**.

:::check Check 2
How many select lines do a 4:1, a 16:1 and a 32:1 MUX need?
:::

### 3 · n variables on a 2ⁿ:1 MUX: the truth table in hardware

Step 2's equation has one term per row of a table. If the function's variables drive the selects, each data input becomes one row of that function's truth table.

:::q <span class="tag">Deck 04 slide 15 (EX 4.15)</span>
Using an 8-to-1 multiplexer, design a logic circuit to realize the following Boolean function F(A, B, C) = Σm(2, 3, 5, 6, 7).
:::

:::guess Guess first
A, B, C go on the three selects (A most significant). For select code 010 = row 2, which data input is passed, and what must it be tied to?
:::

[[fig:u2_ex415|EX 4.15: selects A, B, C (A most significant); each data input is tied to F's value on its row: 0, 0, 1, 1, 0, 1, 1, 1.|w=46]]

1. With A, B, C on the selects, the select code **is** the row number: code ABC = 010 passes I_{2}.
2. On row 2 the output must equal F(row 2). So tie I_{2} to F(row 2) = 1.
3. Do this for all 8 rows: I_{j} = F(row j). The data inputs are the F column of the truth table, top to bottom.

| Row j | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| I_{j} = F | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 1 |

**Answer.** I_{0} … I_{7} = **0, 0, 1, 1, 0, 1, 1, 1** (1 for each minterm in the list, 0 otherwise). No gates and no minimisation are needed.

:::check Check 3
(a) <span class="tag">Deck 04 slide 24 (EX 4.24)</span> An 8:1 MUX has A, B, C on S_{2}, S_{1}, S_{0} and data inputs 0, 0, 1, 0, 0, 1, 1, 1. Find F as Σm and as a minimal SOP. (b) <span class="tag">Deck 04 slide 14 (EX 4.14)</span> Implement the half adder (sum and carry) on two 4:1 MUXes with A, B on the selects.
:::

### 4 · n variables on a 2ⁿ⁻¹:1 MUX: one variable becomes data

Step 3 spends one data input per row. Half the MUX does the job if one variable moves from the selects to the data inputs.

:::q <span class="tag">Deck 04 slide 16 (EX 4.16)</span>
Implement F(x, y, z) = Σm(1, 2, 6, 7) using a 4×1 mux.
:::

:::guess Guess first
x and y go on the selects; z is left over. On the two rows with xy = 00, F is 0 then 1. Which signal, built from z, has those two values?
:::

:::note Terms
**Pair of rows:** the two rows that share one select code; they differ only in the last variable (here z), which is 0 in the first row and 1 in the second. **Residue:** F on that pair, written as a function of the last variable: one of 0, 1, z, z'.
:::

For each pair, compare F with z. There are only four patterns:

| F on the pair (z = 0, z = 1) | 0, 0 | 0, 1 | 1, 0 | 1, 1 |
|---|---|---|---|---|
| Tie the data input to | 0 | z | z' | 1 |

[[fig:u2_ex416|EX 4.16: x and y on the selects; data inputs z, z', 0, 1 (the residues of the four pairs).|w=40]]

| Select xy | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| Rows | 0, 1 | 2, 3 | 4, 5 | 6, 7 |
| F on the pair | 0, 1 | 1, 0 | 0, 0 | 1, 1 |
| Data input | z | z' | 0 | 1 |

**Answer.** Selects x (S_{1}), y (S_{0}); **I_{0} = z, I_{1} = z', I_{2} = 0, I_{3} = 1**. The only extra part is one inverter for z'.

:::check Check 4
<span class="tag">Deck 04 slide 17 (EX 4.17)</span> Use a 4:1 MUX with A, B on the selects to generate F(A, B, C) = Σm(2, 5, 6, 7).
:::

### 5 · MTE Q5: four variables on one 8:1 MUX

Step 4's pairing works for any number of variables: the first n − 1 go on the selects, the last one becomes data.

:::q <span class="tag">MTE 2025 Q5 · 4 marks</span>
Implement the following function using single 8:1 Multiplexer. F(P, Q, R, S) = Σm(0, 1, 3, 4, 8, 9, 10, 11, 13, 15)
:::

:::guess Guess first
P, Q, R go on the selects. Select code 001 covers which two minterms? Is F 1 on both, one, or neither?
:::

Select code PQR = k covers minterms 2k and 2k + 1 (S = 0, then S = 1). Mark each minterm 1 if it is in the list:

| Data input | I_{0} | I_{1} | I_{2} | I_{3} | I_{4} | I_{5} | I_{6} | I_{7} |
|---|---|---|---|---|---|---|---|---|
| Minterms (S = 0, S = 1) | 0, 1 | 2, 3 | 4, 5 | 6, 7 | 8, 9 | 10, 11 | 12, 13 | 14, 15 |
| F on the pair | 1, 1 | 0, 1 | 1, 0 | 0, 0 | 1, 1 | 1, 1 | 0, 1 | 0, 1 |
| Tie to (step 4 table) | 1 | S | S' | 0 | 1 | 1 | S | S |

[[fig:u2_mte5|MTE Q5 finished: P, Q, R on the selects (P most significant); data inputs 1, S, S', 0, 1, 1, S, S.|w=46]]

**Answer.**

1. Selects: P → S_{2}, Q → S_{1}, R → S_{0}.
2. Pair table above (10 minterms → 8 pairs).
3. **I_{0} = 1, I_{1} = S, I_{2} = S', I_{3} = 0, I_{4} = 1, I_{5} = 1, I_{6} = S, I_{7} = S**; one inverter makes S'.
4. Check one row: PQRS = 0101 (m_{5}). Code PQR = 010 passes I_{2} = S' = 0, and 5 is not in the list. ✓

:::check Check 5
(a) <span class="tag">Practice set 1 Q6</span> Implement F(P, Q, R, S) = Σm(0, 2, 5, 9, 11, 12, 14, 15) on an 8:1 MUX (P, Q, R on the selects). (b) <span class="tag">Deck 04 slide 18 (EX 4.18)</span> Implement F(A, B, C, D) = Σm(1, 3, 4, 11, 12, 13, 14, 15) on an 8:1 MUX (A, B, C on the selects).
:::

### 6 · Two variables left over: one 4:1 MUX for a 4-variable function

Step 5 left one variable off the selects. Leave two off and each select code covers four rows; the residue is then a function of two variables, built with a gate or two.

:::q <span class="tag">Deck 04 slide 19 (EX 4.19)</span>
F(A, B, C, D) = Σm(1, 3, 4, 11, 12–15) using 4×1 mux. (The slide gives no solution.)
:::

:::guess Guess first
A, B go on the selects. For AB = 00, the four rows are CD = 00, 01, 10, 11, and F is 1 on rows 1 and 3. What function of C and D is that?
:::

[[fig:u2_ex419|EX 4.19 on one 4:1 MUX: A, B on the selects; data inputs D, C'D', CD, 1, each a residue in C and D.|w=40]]

| Select AB | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| Rows | 0–3 | 4–7 | 8–11 | 12–15 |
| Minterms of F there | 1, 3 | 4 | 11 | 12, 13, 14, 15 |
| CD values where F = 1 | 01, 11 | 00 | 11 | all |
| Residue | **D** | **C'D'** | **CD** | **1** |

Read each residue off the CD values: 01 and 11 share D = 1, so D; 00 alone is C'D'; 11 alone is CD; all four is 1.

**Answer.** Selects A, B; **I_{0} = D, I_{1} = C'D', I_{2} = CD, I_{3} = 1**. Cost: one 4:1 MUX, two AND gates and inverters for C', D'. Step 5's 8:1 version needed only one inverter: a smaller MUX moves the work into gates.

:::check Check 6
Put the running example, F(P, Q, R, S) = Σm(0, 1, 3, 4, 8, 9, 10, 11, 13, 15), on one 4:1 MUX with P, Q on the selects. Give the four residues.
:::

### 7 · A MUX tree: big MUXes from small ones

Steps 3–6 assumed one MUX of the right size. When only small MUXes are available, they are stacked in levels.

:::q <span class="tag">Deck 04 slides 26–28 (EX 4.26–4.28)</span>
Use three 2-1 MUX to make one 4-1 MUX. Construct an 8-to-1 multiplexer using 2-to-1 multiplexers; then using one 2-to-1 and two 4-to-1 multiplexers.
:::

:::guess Guess first
In a 4:1 MUX built from 2:1 MUXes, the first level picks within each pair (I_{0} or I_{1}, I_{2} or I_{3}). Which select bit drives the first level: S_{0} or S_{1}?
:::

:::note Terms
**MUX tree:** MUXes in levels; each level halves (or quarters) the number of signals. **Level:** all the MUXes that share one select bit; the **least** significant select bit drives the level nearest the data inputs.
:::

[[fig:mux_tree|A 4:1 MUX from three 2:1 MUXes: S0 picks within each pair (I0/I1, I2/I3), S1 picks between the two pair winners.|w=55]]

1. Data inputs I_{0}, I_{1} differ only in S_{0} (codes 00, 01); so do I_{2}, I_{3}. So **S_{0} drives the first level**: two 2:1 MUXes.
2. The two winners differ in S_{1}: **S_{1} drives the second level**: one 2:1 MUX. Total **3**.
3. 8:1 from 2:1: levels of 4, 2, 1 MUXes on S_{0}, S_{1}, S_{2}: **7**.
4. 8:1 from 4:1: two 4:1 MUXes on S_{1}S_{0} (one for I_{0}–I_{3}, one for I_{4}–I_{7}), then one 2:1 on S_{2}.

The count rule: divide the number of signals by the MUX size, level after level, until one signal is left; add the levels' MUX counts. If the last level has fewer signals than the MUX has inputs (8:1 from 4:1 leaves 2), use a smaller MUX there, or a 4:1 with its unused select tied to 0.

**Answer to the Guess.** **S_{0}**: it is the bit in which neighbouring inputs differ.

:::check Check 7
How many 2:1 MUXes make a 16:1 MUX? How many 4:1 MUXes?
:::

### 8 · Only 4:1 MUXes for a 4-variable function

Step 7's tree turns step 5's single 8:1 MUX into small parts. Practice set 1 Q5 asks for exactly that.

:::q <span class="tag">Practice set 1 Q5</span>
Design a combinational circuit to implement the following Boolean function using only 4:1 Multiplexer. Take 'D' as input variable. F(A, B, C, D) = Σm(0, 2, 7, 8, 9, 11, 13, 14, 15)
:::

:::guess Guess first
"D as input variable" means D goes on the data inputs, so A, B, C must all be selects. One 4:1 MUX has two select lines. How many 4:1 MUXes, and which variable drives the last one?
:::

1. Treat it first as one 8:1 MUX (step 5) with A, B, C on the selects; residues in D:

| Select ABC | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| Minterms (D = 0, D = 1) | 0, 1 | 2, 3 | 4, 5 | 6, 7 | 8, 9 | 10, 11 | 12, 13 | 14, 15 |
| F on the pair | 1, 0 | 1, 0 | 0, 0 | 0, 1 | 1, 1 | 0, 1 | 0, 1 | 1, 1 |
| Residue | D' | D' | 0 | D | 1 | D | D | 1 |

2. Build that 8:1 MUX the step-7 way: MUX 1 takes the first four residues (A = 0), MUX 2 the last four (A = 1); both use **B, C** as selects.
3. MUX 3 picks MUX 1 or MUX 2 by A. It is a 4:1 MUX used as a 2:1: S_{1} = 0, S_{0} = A, I_{0} = MUX 1, I_{1} = MUX 2, I_{2} = I_{3} = 0.

[[fig:u2_ps1q5|Practice set 1 Q5 with 4:1 MUXes only. MUX1 (A = 0 half): D', D', 0, D. MUX2 (A = 1 half): 1, D, D, 1. Both on selects B, C. MUX3 on selects 0, A picks one of them.|w=62]]

**Answer.** Three 4:1 MUXes: **MUX 1 = D', D', 0, D; MUX 2 = 1, D, D, 1** (selects B, C); **MUX 3: S_{1} = 0, S_{0} = A, I_{0} = MUX 1, I_{1} = MUX 2**. One inverter makes D'.

:::check Check 8
Build the running example (MTE Q5) the same way, from 4:1 MUXes only with S as the data variable. Give the data inputs of the two first-level MUXes.
:::

### 9 · Enable, and the 74LS151 chip

Step 8's third MUX did a 2:1 job. A chip with an **enable** pin does it with an OR gate instead.

:::q <span class="tag">Deck 04 slides 20–21, 29 (EX 4.20, 4.29)</span>
Exercise 1: Implement the logic circuit function specified in the table by using the 74LS151 8-input data selector/multiplexer (Y = 1 on rows 1, 3, 5, 6 of A_{2}A_{1}A_{0}). Then: construct an 8-to-1 multiplexer using only two 4-to-1 multiplexers and basic gates.
:::

:::guess Guess first
Two 4:1 MUXes both see S_{1}S_{0}. If the lower-half MUX could be switched off whenever S_{2} = 1 and the upper-half one whenever S_{2} = 0, what single gate combines their outputs?
:::

:::note Terms
**Enable (strobe) G':** a control pin; with the bar it is **active-low**: G' = 0 lets the MUX work, G' = 1 switches it off. **Disabled output:** what the output shows when switched off. For the '151 family a high strobe forces Y low (Y = 0) and its complement output W high (TI SN74ALS151 function table).
:::

[[fig:u2_ls151|Slide 21's answer: a 74LS151 with G' tied to 0 (enabled), selects A2, A1, A0, data inputs 0, 1, 0, 1, 0, 1, 1, 0: data input j is F on row j.|w=46]]

The 74LS151 is step 3's 8:1 MUX in one package: tie G' = 0 and wire the truth-table column to D_{0}–D_{7}. Its SOP, Y = A_{2}'A_{1}'A_{0} + A_{2}'A_{1}A_{0} + A_{2}A_{1}'A_{0} + A_{2}A_{1}A_{0}', is Σm(1, 3, 5, 6).

[[fig:u2_cascade_en|Slide 29 solved: two 4:1 MUXes share S1, S0; S2 drives the top MUX's G' and S2' the bottom one's, so only one is enabled; the OR passes the enabled output because the disabled one outputs 0.|w=50]]

1. S_{2} = 0: top MUX (I_{0}–I_{3}) enabled (G' = S_{2} = 0), bottom MUX disabled (G' = S_{2}' = 1), output 0.
2. OR(x, 0) = x: F = the top MUX's choice, I_{(S1S0)}.
3. S_{2} = 1: roles swap; F = I_{(4 + S1S0)}.

**Answer.** 74LS151: **G' = 0, D_{0}…D_{7} = 0, 1, 0, 1, 0, 1, 1, 0**. 8:1 from two 4:1: **S_{2} to one enable, S_{2}' to the other, one 2-input OR**. The OR works only because a disabled MUX outputs 0.

:::check Check 9
Which 8:1 data input reaches F when S_{2}S_{1}S_{0} = 110 in the two-MUX circuit? Which MUX is enabled?
:::

### 10 · The demultiplexer: the switch run backwards

A MUX gathers many sources onto one line. At the far end of that line, something must hand the signal back out to the right destination (slide 31: a MUX and a DEMUX sharing a one-bit bus).

:::q <span class="tag">Deck 04 slides 36–38</span>
Draw the 1-to-4 demultiplexer and write its output equations.
:::

:::guess Guess first
In a 1:4 DEMUX the selects say which output gets the data D. What value must the other three outputs hold?
:::

:::note Terms
**Demultiplexer (data distributor):** one data input D, 2^{n} outputs; the select code j routes D to output Y_{j}. Every other output stays 0.
:::

[[fig:demux_fig|The 1:4 demultiplexer: D enters four AND gates; each gate is also fed one select minterm, so only output Y(S1S0) can follow D.|w=55]]

Each output is D gated by its select minterm (step 2's minterms again):

$$Y_{0} = S_{1}'S_{0}'D      Y_{1} = S_{1}'S_{0}D      Y_{2} = S_{1}S_{0}'D      Y_{3} = S_{1}S_{0}D$$

Read it: "Y_{2} copies D when the select code is 10, and is 0 otherwise". A 1:8 DEMUX (slide 38) has eight such gates with 3-variable minterms.

**Answer to the Guess.** **0**. **Answer.** Four 3-input ANDs, each fed D and one minterm of S_{1}, S_{0} (two inverters make S_{1}', S_{0}'); equations above. File 06 step 3 shows the same circuit is a 2:4 decoder whose enable carries D.

:::check Check 10
A 1:4 DEMUX has S_{1}S_{0} = 10 and D = 1. Give Y_{0}, Y_{1}, Y_{2}, Y_{3}.
:::

---

## Exam form

**MUX (2:1, 4:1).** Block (data, selects, output) · truth table · Y = Σ m_{j}I_{j}, e.g. Y = S_{1}'S_{0}'I_{0} + S_{1}'S_{0}I_{1} + S_{1}S_{0}'I_{2} + S_{1}S_{0}I_{3} · gates: one AND per input, one OR.

**Function on a MUX** (MTE Q5 recipe, 4 marks):

1. Write which variables go on the selects, most significant first.
2. Draw the pair table: data input · minterms covered · F on the pair · residue.
3. Residues: (0, 0) → 0; (0, 1) → X; (1, 0) → X'; (1, 1) → 1 (X = the variable left over).
4. Draw the MUX with every data input labelled and the inverter for X'.
5. Check one row by hand.

**Smaller MUX** (two variables left over): four rows per code, residue a 2-variable function (EX 4.19).

**Tree:** first level on S_{0}; 8:1 = 7 × 2:1 or 2 × 4:1 + 1 × 2:1; with enables: 2 × 4:1 + OR, S_{2} to the enables.

**DEMUX:** Y_{j} = D·m_{j}(selects); others 0.

## Traps

- Putting the most significant variable on S_{0}: the select code must spell the row number, MSB on the highest select.
- Pairing the wrong rows: a pair differs only in the variable left over (0–1, 2–3, …), so that variable must be the **last** one in F's list.
- Swapping X and X': (0, 1) → X, (1, 0) → X'.
- Forgetting the inverter that makes X'.
- In a tree, putting S_{2} on the first level: the first level uses the least significant select.
- Combining two enabled MUXes with an OR while both are enabled: the enables must be opposite.

## Self-test

1. <span class="tag">Practice set 1 Q3</span> Implement F(a, b, c, d) = Σm(0, 1, 3, 5, 7, 9, 15) on an 8:1 MUX (a, b, c on the selects).
2. Implement F(A, B, C) = Σm(0, 2, 5, 7) on a 4:1 MUX with A, B on the selects.
3. Implement the same F with A, C on the selects and B as the data variable. What do the residues tell you about F?
4. Implement the full adder's sum S = Σm(1, 2, 4, 7) and carry C = Σm(3, 5, 6, 7) on two 4:1 MUXes with x, y on the selects (z = carry in).
5. Why can any function of n variables be built from one 2^{n−1}:1 MUX and at most one inverter?
6. What is the difference between a 1:4 DEMUX and a 2:4 decoder with an enable?

<!--ANSWERS-->

## Answers

**Check 1.** (a) Z = S'·0 + S·1 = **S**. (b) Z = S'·1 + S·0 = **S'** (a 2:1 MUX makes an inverter).

**Check 2.** **2, 4, 5** (2^{2} = 4, 2^{4} = 16, 2^{5} = 32).

**Check 3.** (a) Rows with data 1: 2, 5, 6, 7, so F = **Σm(2, 5, 6, 7)**. Map (file 02): pair m_{5}, m_{7} → AC and pair m_{2}, m_{6} → BC'; F = **AC + BC'**. (b) Sum S = Σm(1, 2): **I_{0}…I_{3} = 0, 1, 1, 0**. Carry C = Σm(3): **0, 0, 0, 1**.

**Check 4.** Pairs (C = 0, 1): AB = 00 → rows 0, 1 → 0, 0 → **0**; 01 → rows 2, 3 → 1, 0 → **C'**; 10 → rows 4, 5 → 0, 1 → **C**; 11 → rows 6, 7 → 1, 1 → **1**. Data inputs **0, C', C, 1**.

**Check 5.** (a) Pairs (S = 0, 1): (0, 1) 1, 0 → S'; (2, 3) 1, 0 → S'; (4, 5) 0, 1 → S; (6, 7) 0, 0 → 0; (8, 9) 0, 1 → S; (10, 11) 0, 1 → S; (12, 13) 1, 0 → S'; (14, 15) 1, 1 → 1. Data inputs **S', S', S, 0, S, S, S', 1**. (b) Pairs (D = 0, 1): (0, 1) 0, 1 → D; (2, 3) 0, 1 → D; (4, 5) 1, 0 → D'; (6, 7) → 0; (8, 9) → 0; (10, 11) 0, 1 → D; (12, 13) → 1; (14, 15) → 1. Data inputs **D, D, D', 0, 0, D, 1, 1**.

**Check 6.** PQ = 00: minterms 0, 1, 3 → RS = 00, 01, 11 → R'S' + R'S + RS = **R' + S**. PQ = 01: minterm 4 → RS = 00 → **R'S'**. PQ = 10: 8, 9, 10, 11 → **1**. PQ = 11: 13, 15 → RS = 01, 11 → **S**. Data inputs **R' + S, R'S', 1, S** (one OR, one AND, inverters).

**Check 7.** 2:1: 8 + 4 + 2 + 1 = **15**. 4:1: 4 + 1 = **5**.

**Check 8.** Step 5's residues split in two: first MUX (P = 0, selects Q, R) **1, S, S', 0**; second MUX (P = 1) **1, 1, S, S**. A third 4:1 MUX with S_{1} = 0, S_{0} = P picks between them.

**Check 9.** S_{2} = 1: the top MUX has G' = S_{2} = 1 (disabled, outputs 0); the **bottom MUX** has G' = S_{2}' = 0 (enabled). S_{1}S_{0} = 10 selects its third input: **I_{6}** (4 + 2).

**Check 10.** **Y_{0} = 0, Y_{1} = 0, Y_{2} = 1, Y_{3} = 0**.

**Self-test.**

1. Pairs (d = 0, 1): (0, 1) 1, 1 → 1; (2, 3) 0, 1 → d; (4, 5) 0, 1 → d; (6, 7) 0, 1 → d; (8, 9) 0, 1 → d; (10, 11) → 0; (12, 13) → 0; (14, 15) 0, 1 → d. Data inputs **1, d, d, d, d, 0, 0, d**.
2. AB = 00: rows 0, 1 → 1, 0 → C'; 01: rows 2, 3 → 1, 0 → C'; 10: rows 4, 5 → 0, 1 → C; 11: rows 6, 7 → 0, 1 → C. Data inputs **C', C', C, C** (F = A'C' + AC).
3. Selects A, C; each code covers B = 0, 1. AC = 00: rows 0, 2 → 1, 1 → **1**; 01: rows 1, 3 → **0**; 10: rows 4, 6 → **0**; 11: rows 5, 7 → **1**. Data inputs **1, 0, 0, 1**: all constants, so F does not depend on B at all: F = A'C' + AC (A XNOR C).
4. Sum: xy = 00 → rows 0, 1 → 0, 1 → z; 01 → 1, 0 → z'; 10 → 1, 0 → z'; 11 → 0, 1 → z: **z, z', z', z**. Carry: 00 → **0**; 01 → rows 2, 3 → 0, 1 → **z**; 10 → rows 4, 5 → **z**; 11 → **1**: **0, z, z, 1**.
5. With n − 1 variables on the selects, each select code covers two rows that differ only in the last variable X; F on those two rows is one of four patterns, so the data input is 0, 1, X or X'. Only X' needs a gate: one inverter.
6. None in hardware. The decoder's code inputs are the DEMUX selects, and its enable is the DEMUX data input D (file 06 step 3).

<!--/ANSWERS-->
