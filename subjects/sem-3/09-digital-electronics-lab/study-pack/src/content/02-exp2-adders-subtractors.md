# Exp 2 · Half/full adder and subtractor; 7483 adder, 2's-complement subtractor, BCD adder

<div class="sub">Manual pp. 5–9 · ICs 7486, 7408, 7432, 7404, 7483 · all expressions checked over every input</div>

[[map:1 Gates & universality > 2 Adders/subtractors > 3 NAND/NOR design > 4 Code converters|here=2]]

:::q <span class="tag">Manual Exp 2, aim</span>
Design and test a half adder/half subtractor and a full adder/full subtractor; study the 7483. Viva form: "How does a single 7483 subtract, and what does C_{out} tell you after a subtraction?"
:::

:::guess Guess first
Subtraction A − B = A + (2's complement of B). How would you get B's 2's complement using XOR gates and the carry-in?
:::

## Designs

| Circuit | Outputs |
|---|---|
| half adder | S = A ⊕ B, C = AB |
| half subtractor (A − B) | D = A ⊕ B, B_{o} = A'B |
| full adder | S = A ⊕ B ⊕ C_{in}, C_{out} = AB + BC_{in} + AC_{in} (= AB + C_{in}(A ⊕ B)) |
| full subtractor | D = A ⊕ B ⊕ B_{i}, B_{o} = A'B + (A ⊕ B)'B_{i} |

| A B C_{in} | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| full adder S C_{out} | 0 0 | 1 0 | 1 0 | 0 1 | 1 0 | 0 1 | 0 1 | 1 1 |
| full subtractor D B_{o} (third input = B_{i}) | 0 0 | 1 1 | 1 1 | 0 1 | 1 0 | 0 0 | 0 0 | 1 1 |

## Wiring

| Circuit | Wires (7486/7408/7432: gate 1 = pins 1, 2 → 3; gate 2 = 4, 5 → 6; gate 3 = 9, 10 → 8; gate 4 = 12, 13 → 11) |
|---|---|
| half adder | A → 7486-1 and 7408-1; B → 7486-2 and 7408-2. **S = 7486-3, C = 7408-3** |
| half subtractor | D = 7486 (A → 1, B → 2 → 3). A → 7404-1 (pin 2 = A'); 7404-2 → 7408-1, B → 7408-2; **B_{o} = 7408-3** |
| full adder: sum | 7486 gate 1: A, B → 3; gate 2: pin 3 → 4, C_{in} → 5; **S = 7486-6** |
| full adder: carry (Fig 2.3) | 7408: A, B → 3 (AB); B → 4, C_{in} → 5 → 6 (BC_{in}); A → 9, C_{in} → 10 → 8 (AC_{in}). 7432: 7408-3 → 1, 7408-6 → 2 → 3; 7432-3 → 4, 7408-8 → 5; **C_{out} = 7432-6** |
| full subtractor: borrow | 7404: A → 1 → 2 (A'); 7486-3 (A ⊕ B) → 3 → 4. 7408: 7404-2 → 1, B → 2 → 3 (A'B); 7404-4 → 4, B_{i} → 5 → 6. 7432: 3 → 1, 6 → 2; **B_{o} = 7432-3** |

## The 7483: 4-bit adder (note the odd power pins)

[[fig:pin7483|VCC is pin 5 and GND is pin 12, not 16/8. Wiring power to 16 and 8 is the classic mistake with this chip.|w=42]]

| Signal | A3 A2 A1 A0 | B3 B2 B1 B0 | C_{in} | S3 S2 S1 S0 | C_{out} |
|---|---|---|---|---|---|
| pin | 1, 3, 8, 10 | 16, 4, 7, 11 | 13 | 15, 2, 6, 9 | 14 |

## 4-bit adder / 2's-complement subtractor (Fig 2.6)

- Feed each B bit through an XOR whose other input is the control **M** (7486), and also send **M to C_{in}** (pin 13).
- **M = 0:** B passes unchanged, C_{in} = 0, so the 7483 computes **A + B**.
- **M = 1:** each B bit is inverted (1's complement) and C_{in} = 1 adds the 1, giving 2's complement. So the 7483 computes **A − B**.

| Wire | |
|---|---|
| b0 → 7486-1, M → 2 → pin 3 → 7483-11 | b1 → 7486-4, M → 5 → pin 6 → 7483-7 |
| b2 → 7486-9, M → 10 → pin 8 → 7483-4 | b3 → 7486-12, M → 13 → pin 11 → 7483-16 |
| M → 7483-13 (C_{in}) | A3..A0 → pins 1, 3, 8, 10 |

| Try | Inputs | S3..S0 | C_{out} | Meaning |
|---|---|---|---|---|
| 7 + 5 | M = 0, A = 0111, B = 0101 | 1100 | 0 | 12 |
| 7 − 5 | M = 1, A = 0111, B = 0101 | **0010** | **1** | +2. C_{out} = 1 means no borrow, result positive. |
| 5 − 7 | M = 1, A = 0101, B = 0111 | **1110** | **0** | C_{out} = 0 means negative: 1110 is −2 in 2's complement |

## BCD adder (Fig 2.7)

- Add the two BCD digits in 7483 #1.
- If the sum is more than 9, or produced a carry, add 6 (0110) in 7483 #2.

The correction signal is:

$$K = C_{4} + S_{3}S_{2} + S_{3}S_{1}$$

Make S3S2 and S3S1 with two 7408 gates, then OR all three with two 7432 gates. Feed **0 K K 0** into B3 B2 B1 B0 of 7483 #2, with the first sum on its A inputs and C_{in} = 0. **K is the decimal carry.**

Example: 7 + 5. 7483 #1 gives 1100 (12 > 9), so K = 1. Then 1100 + 0110 = (1)0010. Output: carry **1**, digit **0010**, which reads as 12 ✓.

:::write Write in your record
**Result:** the truth tables of the half/full adder and half/full subtractor were verified. The 7483 added two 4-bit numbers; with the XOR/M arrangement it subtracted in 2's complement (7 − 5 = 0010, C_{out} = 1; 5 − 7 = 1110, C_{out} = 0). The BCD adder gave 7 + 5 = 1 0010.

**Theory for the record:** a half adder adds two bits (S = A ⊕ B, C = AB). A full adder adds three, including the carry-in (S = A ⊕ B ⊕ C_{in}, C_{out} = AB + BC_{in} + AC_{in}), and can be built from two half adders and an OR. Subtractors produce a difference and a borrow (half: D = A ⊕ B, B_{o} = A'B). The 7483 is a 4-bit binary adder with fast carry. Subtraction uses A − B = A + B' + 1, made by XOR-ing B with a control M and feeding M to C_{in}. For BCD addition, 6 is added when the binary sum exceeds 9 or produces a carry.
:::

:::check Check 1
(a) In the subtractor, why does C_{out} = 1 mean "no borrow"? (b) BCD 8 + 9: give 7483 #1's output, K, and the final output. (c) A student powers the 7483 on pins 16 and 8. What happens?
:::

<!--ANSWERS-->

## Answers

**Opening question.** XOR each B bit with M (M = 1 inverts it) and feed M into C_{in} (+1). Together that adds the 2's complement of B, so the adder subtracts. After a subtraction, C_{out} = 1 means A ≥ B (positive result); C_{out} = 0 means the result is negative, in 2's-complement form.

**Check 1.** (a) A + (2⁴ − B) = 2⁴ + (A − B). When A ≥ B this overflows 4 bits, so carry = 1. When A < B it doesn't. (b) 8 + 9 = 17: #1 gives C_{4} = 1, S = 0001, so K = 1. 0001 + 0110 = **0111**, carry 1, i.e. **1 0111** = 17 ✓. (c) Pin 16 is B3 and pin 8 is A1, so the chip gets no power. If the real VCC/GND pins (5, 12) are left floating while inputs are driven, it misbehaves and can be damaged. The outputs are garbage.

<!--/ANSWERS-->
