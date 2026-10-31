# Exp 5 · Magnitude comparator (1-bit and 7485) and odd-parity generator/checker (gates and 74180)

<div class="sub">Manual pp. 13–18 · ICs 7404, 7408, 7486, 7485, 74180</div>

[[map:3 NAND/NOR design > 4 Code converters > 5 Comparator & parity > 6–8 MUX, DEMUX, decoder|here=3]]

:::q <span class="tag">Manual Exp 5, aim</span>
Design and study 1-bit and 4-bit (7485) magnitude comparators, and a 3-bit odd-parity generator/checker, then the 74180. Viva form: "A lone 7485 lights both A>B and A<B when the inputs are equal. What did you forget?"
:::

:::guess Guess first
The 7485 has three *cascade inputs*. What must they be set to when only one chip is used?
:::

## 1-bit comparator

$$(A > B) = AB'          (A < B) = A'B          (A = B) = (A ⊕ B)'$$

**Wiring:**

- 7404: A → 1 → 2 (A'); B → 3 → 4 (B').
- 7408: A → 1, 7404-4 → 2 → **3 = (A > B)**; 7404-2 → 4, B → 5 → **6 = (A < B)**.
- 7486: A → 1, B → 2 → 3; 7404: 7486-3 → 5 → **6 = (A = B)**.

Only one output is HIGH at a time.

## 4-bit comparator, 7485

[[fig:pin7485|7485. The cascade inputs I(A>B), I(A=B), I(A<B) are on pins 4, 3, 2.|w=42]]

| Signal | A3 A2 A1 A0 | B3 B2 B1 B0 | I(A>B) | I(A=B) | I(A<B) | A>B, A=B, A<B out |
|---|---|---|---|---|---|---|
| pin | 15, 13, 12, 10 | 1, 14, 11, 9 | 4 → **GND** | 3 → **+5 V** | 2 → **GND** | 5, 6, 7 |

The chip compares from the MSB down. The first unequal bit decides the result. Only when all four bit pairs are equal does it pass the **cascade inputs** through. So a single chip needs I(A=B) = 1 (and the others 0) for "equal" to come out right.

**8-bit (exercise):**

- The **low** nibble's chip has cascade inputs 0, 1, 0.
- Its three outputs (pins 5, 6, 7) go into the **high** nibble chip's cascade inputs (pins 4, 3, 2).
- The final answer comes from the high chip.

## Odd parity generator and checker

**Odd parity** makes the total number of 1s (data + parity) **odd**.

- **Generator:** P = (X ⊕ Y ⊕ Z)'. Two XORs (7486) and an inverter (7404). The manual's Fig 5.4 feeds Y, Z into gate 1 and X with gate 1's output into gate 2.
- **Checker:** C = (X ⊕ Y ⊕ Z ⊕ P)'. Three XORs and an inverter. **C = 1 flags an error** (an even count arrived).

Manual Fig 5.5 puts inverters after the first two XORs. Those two inversions cancel inside the last XOR, so the result is the same.

| XYZ | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| P (odd) | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 0 |

## 74180: 9-bit parity generator/checker

[[fig:pin74180|74180. Data I0–I7; enables PE (pin 3) and PO (pin 4); outputs ΣE (pin 5) and ΣO (pin 6).|w=42]]

| Count of 1s in I0–I7 | PE | PO | ΣE | ΣO |
|---|---|---|---|---|
| even | 1 | 0 | 1 | 0 |
| odd | 1 | 0 | 0 | 1 |
| even | 0 | 1 | 0 | 1 |
| odd | 0 | 1 | 1 | 0 |
| any | 1 | 1 | 0 | 0 |
| any | 0 | 0 | 1 | 1 |

**The manual's observation table, filled** (checked):

| I7…I0 | PE PO | ΣE ΣO |
|---|---|---|
| 1111 0000 | 1 0 | **1 0** |
| 1111 0001 | 1 0 | **0 1** |
| 1010 1100 | 0 1 | **0 1** |
| 1010 1101 | 0 1 | **1 0** |
| 0000 0000 | 1 0 | **1 0** |
| 1111 1111 | 0 1 | **0 1** |

:::write Write in your record
**Result:** the 1-bit comparator and the 7485 4-bit comparator gave exactly one HIGH output per input pair. The 3-bit odd-parity generator/checker was verified (checker output 1 = error). The 74180 outputs matched the observation table.

**Theory for the record:** a magnitude comparator decides A > B, A = B or A < B. For one bit: AB', A'B and (A ⊕ B)'. The 7485 compares two 4-bit words from the MSB down. Its cascade inputs let chips be chained for longer words, and must be set to (0, 1, 0) for a single chip. A parity bit makes the number of 1s even or odd so that single-bit errors can be detected. Odd-parity generator: P = (X ⊕ Y ⊕ Z)'. The checker XORs all received bits. The 74180 generates/checks parity on 8 bits, with PE/PO selecting even/odd.
:::

:::check Check 1
(a) A = 1010, B = 1010 on a lone 7485 with I(A=B) left floating. What do you expect, and why is "floating" risky here? (b) Odd parity, data 101: give P, and the checker output if the received word is 1011. (c) How do you make a 9-bit odd-parity checker from one 74180 and an inverter?
:::

<!--ANSWERS-->

## Answers

**Opening question.** The cascade inputs: I(A=B) (pin 3) must be **HIGH**, and I(A>B), I(A<B) (pins 4, 2) **LOW**.

**Check 1.** (a) A floating TTL input usually acts HIGH, so it may happen to work. That relies on undefined behaviour, so tie pin 3 to +5 V. The datasheet's function table shows what wrong cascade settings do when A = B: all three at 0 gives A>B = A<B = **1** (the opening symptom); I(A>B) = I(A<B) = 1 with I(A=B) = 0 gives all three outputs **0**. (b) P = (1 ⊕ 0 ⊕ 1)' = **1**. The word 1011 has three 1s (odd) = valid, so the checker output is **0** (no error). (c) Feed 8 bits to I0–I7. Feed the 9th bit to PO, and its inverse (via the inverter) to PE. Then ΣO/ΣE give the odd-parity check of all 9 bits.

<!--/ANSWERS-->
