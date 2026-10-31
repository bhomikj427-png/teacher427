# Exp 1 · Logic gates, and NAND/NOR as universal gates

<div class="sub">Manual pp. 1–4 · ICs 7400, 7402, 7404, 7408, 7432, 7486 · trainer kit</div>

[[map:1 Gates & universality > 2 Adders/subtractors > 3 NAND/NOR design > 4 Code converters|here=1]]

:::q <span class="tag">Manual Exp 1, aim</span>
Verify the truth tables of AND, OR, NOT, NAND, NOR and XOR; realise NOT, AND and OR using only NAND gates, then only NOR gates. Viva form: "Why are NAND and NOR called universal? Show OR from NANDs only."
:::

:::guess Guess first
How many 2-input NANDs make an OR? Sketch it before reading on.
:::

## The six ICs

[[fig:pin7400|7408 (AND), 7432 (OR) and 7486 (XOR) use exactly this layout. Only the gate inside changes.|w=42]]

[[fig:pin7402|The 7402 is different: each output comes FIRST (pins 1, 4, 10, 13).|w=42]]

[[fig:pin7404|Six inverters.|w=42]]

**Testing a gate IC** (e.g. the 7408): connect A → pin 1, B → pin 2, LED ← pin 3, VCC 14, GND 7. Walk 00, 01, 10, 11. Repeat for gates 2–4 if you have time: a chip can have one dead gate.

| A B | AND | OR | NAND | NOR | XOR | NOT A |
|---|---|---|---|---|---|---|
| 0 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| 0 1 | 0 | 1 | 1 | 0 | 1 | 1 |
| 1 0 | 0 | 1 | 1 | 0 | 1 | 0 |
| 1 1 | 1 | 1 | 0 | 0 | 0 | 0 |

## Universality

A gate is **universal** if NOT, AND and OR (and so any function) can be built from it alone.

| Make | From NAND (7400) | From NOR (7402) |
|---|---|---|
| NOT A | NAND(A, A) | NOR(A, A) |
| AND | NAND, then a NAND-inverter: ((AB)')' | invert both inputs, then NOR: (A' + B')' = AB (De Morgan) |
| OR | invert both inputs, then NAND: (A'B')' = A + B (De Morgan) | NOR, then a NOR-inverter: ((A + B)')' |
| gates needed | NOT 1, AND 2, OR 3 | NOT 1, OR 2, AND 3 |

## Wiring (the manual's pin numbers)

| Circuit | Wires |
|---|---|
| NOT (NAND) | A → 7400 pins 1 and 2; Y = pin 3 |
| AND (NAND) | A → 1, B → 2; pin 3 → pins 4 and 5; Y = pin 6 |
| OR (NAND) | A → 1 and 2 (pin 3 = A'); B → 4 and 5 (pin 6 = B'); pin 3 → 9, pin 6 → 10; Y = pin 8 |
| NOT (NOR) | A → 7402 pins 2 and 3; Y = pin 1 |
| OR (NOR) | A → 2, B → 3; pin 1 → pins 5 and 6; Y = pin 4 |
| AND (NOR) | A → 2 and 3 (pin 1 = A'); B → 5 and 6 (pin 4 = B'); pin 1 → 8, pin 4 → 9; Y = pin 10 |

:::write Write in your record
**Result:** the truth tables of AND, OR, NOT, NAND, NOR and XOR were verified. NOT, AND and OR were realised using only NAND gates (1, 2, 3 gates) and using only NOR gates (1, 3, 2 gates), and their truth tables verified.

**Theory for the record:** logic gates implement Boolean operations: AND (Y = AB), OR (Y = A + B), NOT (Y = A'), NAND (Y = (AB)'), NOR (Y = (A + B)'), XOR (Y = AB' + A'B). TTL ICs of the 74 series contain several gates in a 14-pin DIP, with VCC on pin 14 and GND on pin 7. NAND and NOR are universal gates: NOT, AND and OR, and therefore any Boolean function, can be built using only one of them. By De Morgan's theorems, (A'B')' = A + B and (A' + B')' = AB.
:::

:::check Check 1
(a) Make XOR from 2-input NANDs only: how many gates? (b) Why does a floating input on a 7402 NOR give a stuck-at-0 output? (c) Which pin is the output of gate 3 on the 7400, and on the 7402?
:::

<!--ANSWERS-->

## Answers

**Opening question.** Each of them alone can make NOT, AND and OR, and so any function. OR = NAND(NAND(A,A), NAND(B,B)): **3 NANDs**.

**Check 1.** (a) **4 NANDs**: n1 = (AB)', then A ⊕ B = NAND(NAND(A, n1), NAND(B, n1)). (b) A floating TTL input behaves as logic 1, and a NOR with any input at 1 outputs 0. (c) 7400 gate 3: inputs 9, 10 → output **8**. 7402 gate 3: inputs 8, 9 → output **10**.

<!--/ANSWERS-->
