# 05 — Multiplexer and demultiplexer

<div class="sub">Deck 04 (slides 4–29) · mid-term 2025 Q5 (4 marks) · practice set 1 Q3, Q5, Q6 · syllabus Unit 2 · needs 01 (minterms)</div>

## Map

[[map:1 MUX as a truth table > 2 n variables on a smaller MUX > 3 MUX tree, demultiplexer|here=1]]

01–04 built circuits gate by gate. Some circuits are needed so often they are sold as single chips (MSI). The new skill here is building a function from a block without drawing its gates.

## The questions this file answers

- <span class="tag">MTE 2025 Q5 · 4 marks</span> Implement F(P, Q, R, S) = Σm(0, 1, 3, 4, 8, 9, 10, 11, 13, 15) with a single 8:1 MUX.
- <span class="tag">Set 1 Q3, Q5</span> Functions on 8:1 and on 4:1 MUXes only.
- <span class="tag">Deck 04 slides 26–29</span> Build a larger MUX from smaller ones; the demultiplexer.

---

## Build

### 1 · The MUX is a truth table in hardware

:::guess Predict
A 4:1 MUX has two select lines and four data inputs. If you put x and y on the selects and tie each data input to 0 or 1, what have you built?
:::

:::note Terms
**Multiplexer:** many data inputs I_{0}, I_{1}, …, one output. **Select lines:** a binary number that picks which input reaches the output. A 2^{n}:1 MUX has n select lines.
:::

$$4:1 MUX: Y = S_{1}'S_{0}'I_{0} + S_{1}'S_{0}I_{1} + S_{1}S_{0}'I_{2} + S_{1}S_{0}I_{3}$$

Each data input is one row: input I_{j} reaches the output exactly when the selects spell j.

**Answer.** Any function of x and y: tie I_{j} to F's value on row j. With n variables on a 2^{n}:1 MUX, each I_{j} is the constant from row j.

:::check Check 1
Implement F(x, y, z) = Σm(1, 2, 4, 7) on an 8:1 MUX.
:::

### 2 · n variables on a 2^{n−1}:1 MUX

:::q <span class="tag">MTE 2025 Q5 · 4 marks</span>
Implement the following function using single 8:1 Multiplexer. F(P, Q, R, S) = Σm(0, 1, 3, 4, 8, 9, 10, 11, 13, 15)
:::

:::guess Guess first
An 8:1 MUX has 3 select lines but the function has 4 variables. Where does the fourth go?
:::

Put n − 1 variables on the selects. Each select code now covers two rows (last variable = 0 and = 1). Compare F in those two rows with the last variable:

| F at S = 0, S = 1 | 0, 0 | 0, 1 | 1, 0 | 1, 1 |
|---|---|---|---|---|
| Connect | 0 | S | S' | 1 |

| Input | I_{0} | I_{1} | I_{2} | I_{3} | I_{4} | I_{5} | I_{6} | I_{7} |
|---|---|---|---|---|---|---|---|---|
| Minterms | 0, 1 | 2, 3 | 4, 5 | 6, 7 | 8, 9 | 10, 11 | 12, 13 | 14, 15 |
| F | 1, 1 | 0, 1 | 1, 0 | 0, 0 | 1, 1 | 1, 1 | 0, 1 | 0, 1 |
| Connect | 1 | S | S' | 0 | 1 | 1 | S | S |

[[fig:v1arg5|The finished circuit: P, Q, R on the selects (P most significant), one inverter for S'.|w=55]]

**Answer.** P, Q, R → selects. I_{0} = 1, I_{1} = S, I_{2} = S', I_{3} = 0, I_{4} = 1, I_{5} = 1, I_{6} = S, I_{7} = S.

:::check Check 2
(a) <span class="tag">Set 1 Q3</span> Implement F(a, b, c, d) = Σm(0, 1, 3, 5, 7, 9, 15) on an 8:1 MUX. (b) <span class="tag">Deck 04 slide 16</span> Implement F(x, y, z) = Σm(1, 2, 6, 7) on a 4:1 MUX.
:::

### 3 · MUX tree and the demultiplexer

:::q <span class="tag">Set 1 Q5</span>
Implement F(A, B, C, D) = Σm(0, 2, 7, 8, 9, 11, 13, 14, 15) using only 4:1 multiplexers. Take D as the input variable.
:::

:::guess Guess first
Three variables remain for selects, but a 4:1 MUX has only two select lines. How do you get a third?
:::

<div class="two">

[[fig:mux_tree|4:1 MUX from three 2:1 MUXes: S_{0} picks within each pair, S_{1} picks the pair.]]

[[fig:demux_fig|1:4 demultiplexer: D goes to the output chosen by the selects.]]

</div>

**MUX tree.** Small MUXes build a larger one: an 8:1 is two 4:1s (selects S_{1}S_{0}) and a 2:1 (select S_{2}) (deck 04 slides 26–29). **Demultiplexer:** the reverse: one data input D is routed to the selected output; the others stay 0. A decoder with an enable is a demultiplexer (06).

**Answer.** Three 4:1 MUXes. MUX 1 (A = 0) and MUX 2 (A = 1) use B, C as selects. MUX 1: **D', D', 0, D** (rows 0–1, 2–3, 4–5, 6–7). MUX 2: **1, D, D, 1** (rows 8–15). MUX 3: A on one select, the other grounded: I_{0} = MUX 1, I_{1} = MUX 2.

:::check Check 3
(a) How many 2:1 MUXes make an 8:1 MUX? (b) Write the four output equations of a 1:4 demultiplexer.
:::

---

## Exam form

**MUX.** Block, select table, 4:1 equation.

**Function on a MUX.** Selects ← n − 1 variables; the pair table (0, S, S', 1); draw the MUX with every input labelled.

**Tree, DEMUX.** 8:1 from 4:1s + 2:1; DEMUX equations Y_{j} = D·(select code j).

## Traps

- Putting the most significant variable on S_{0}: check which select is the MSB.
- Pairing rows wrongly: the pairs differ in the last variable only (0–1, 2–3, …).
- Forgetting the inverter that makes S'.

## Self-test

1. Implement F(x, y, z) = Σm(0, 3, 5, 6) on a 4:1 MUX (x, y on selects).
2. Implement F(A, B, C, D) = Σm(1, 3, 4, 11, 12, 13, 14, 15) on an 8:1 MUX (A, B, C on selects).
3. How many 4:1 MUXes make a 16:1 MUX?
4. Why is a MUX called a "universal" combinational block?
5. What is the difference between a demultiplexer and a decoder with enable?

<!--ANSWERS-->

## Answers

**Check 1.** I_{0}…I_{7} = **0, 1, 1, 0, 1, 0, 0, 1**.

**Check 2.** (a) Selects a, b, c: I_{0} = **1**, I_{1} = **d**, I_{2} = **d**, I_{3} = **d**, I_{4} = **d**, I_{5} = **0**, I_{6} = **0**, I_{7} = **d**. (b) Selects x, y: I_{0} = **z**, I_{1} = **z'**, I_{2} = **0**, I_{3} = **1**.

**Check 3.** (a) **Seven** (4 + 2 + 1). (b) Y_{0} = DS_{1}'S_{0}', Y_{1} = DS_{1}'S_{0}, Y_{2} = DS_{1}S_{0}', Y_{3} = DS_{1}S_{0}.

**Self-test.**

1. I_{0} = **z'**, I_{1} = **z**, I_{2} = **z**, I_{3} = **z'**.
2. I_{0} = **D**, I_{1} = **D**, I_{2} = **D'**, I_{3} = **0**, I_{4} = **0**, I_{5} = **D**, I_{6} = **1**, I_{7} = **1**.
3. **Five** (four, then one).
4. Any function of n variables fits on a 2^{n−1}:1 MUX with at most one inverter.
5. None in hardware: the decoder's enable is the DEMUX data input and its code inputs are the selects.

<!--/ANSWERS-->
