# 03 — NAND-only and NOR-only circuits

<div class="sub">Deck 01 slides 40–47 · mid-term 2025 Q1 (2 marks) · practice set 1 Q2 · syllabus Unit 1 · needs 02 (minimal SOP and POS)</div>

## Map

[[map:1 Universal gates > 2 Two-level NAND–NAND and NOR–NOR|here=1]]

A chip is cheapest when it uses one kind of gate. NAND and NOR can each build everything, so any minimal SOP or POS from 02 turns into a one-gate-type circuit.

## The questions this file answers

- <span class="tag">MTE 2025 Q1 · 2 marks</span> Optimise F = P'Q' + P' and implement it with 2-input NOR gates.
- <span class="tag">Set 1 Q2</span> Minimise F(w, x, y, z) = Σm(0, 1, 3, 5, 7, 10, 11) + d(2, 6, 13) and realise it with NAND gates only.

---

## Build

### 1 · Universal gates

:::q <span class="tag">MTE 2025 Q1 · 2 marks</span>
Optimized the following expression and implement using 2-input NOR gate. F = P'Q' + P'
:::

:::guess Guess first
Can the answer still depend on Q?
:::

:::note Terms
**Universal gate:** a gate type that can build NOT, AND and OR on its own, and so any circuit. NAND and NOR are both universal.
:::

[[fig:universal_nand|NOT, AND and OR from NAND gates.|w=75]]

**NAND:** inputs tied → NOT; NAND + inverter → AND; invert both inputs first → OR, since (X'Y')' = X + Y. **NOR** is the dual: tied → NOT; NOR + inverter → OR; NOR of inverted inputs → AND.

**Answer.** F = P'(Q' + 1) = **P'** (absorption): Q drops out. One NOR with both inputs tied to P gives (P + P)' = P':

[[fig:nor_inverter|A NOR gate as an inverter.|w=35]]

:::check Check 1
(a) Build a 2-input AND from NOR gates only. How many gates? (b) Show that a NAND with inputs X' and Y' gives X + Y.
:::

### 2 · Two-level NAND–NAND and NOR–NOR

:::q <span class="tag">Set 1 Q2</span>
Minimise F(w, x, y, z) = Σm(0, 1, 3, 5, 7, 10, 11) + d(2, 6, 13) and realise it using NAND gates only.
:::

:::guess Guess first
Start from an AND–OR circuit. If you replace every gate by a NAND, what do the double bubbles on each internal wire do?
:::

| To build with | Start from | Then | Why |
|---|---|---|---|
| NAND only | minimal **SOP** | every AND and the OR → NAND | ((AB)'(CD)')' = AB + CD |
| NOR only | minimal **POS** | every OR and the AND → NOR | ((A + B)' + (C + D)')' = (A + B)(C + D) |

A single-literal term goes straight into the output gate, **complemented** (F = A + BC with NAND: the output NAND gets A' and (BC)').

<div class="two">

[[fig:v1arg4|02's mid-term answer with NAND gates only.]]

[[fig:xor_nand|XOR from four NAND gates (deck 01 slide 47).]]

</div>

**Answer.** K-map: **F = w'x' + w'z + x'y**. NAND–NAND: three 2-input NANDs (w', x' · w', z · x', y) into one 3-input NAND.

:::check Check 2
(a) How many 2-input NOR gates realise F = (A + B)(C + D)? (b) Realise F = A + BC with NAND gates only.
:::

---

## Exam form

**Universality.** Draw NOT, AND, OR from NAND (and from NOR) with the De Morgan line for each.

**Conversion.** Minimal SOP → NAND–NAND; minimal POS → NOR–NOR; single literals enter the output gate complemented.

## Traps

- Building NOR–NOR from an SOP: it gives the wrong function.
- Forgetting to complement a single-literal term at the output gate.
- Not simplifying first (the mid-term's F = P' needs one gate, not five).

## Self-test

1. Prove NOR is universal.
2. Realise F = AB + CD with NAND gates only. How many gates?
3. Realise F = (A + B)C with NOR gates only.
4. Build XOR from NAND gates. How many?
5. Simplify F = A'B + A'B' + AB' and implement it with one gate.

<!--ANSWERS-->

## Answers

**Check 1.** (a) AB = (A' + B')'. Two tied NORs make A' and B'; a third NOR gives AB: **3 gates**. (b) (X'·Y')' = X + Y by De Morgan.

**Check 2.** (a) **Three**: one for each sum and one output gate. (b) Output NAND with inputs A' and (BC)': F = (A'·(BC)')' = A + BC; gates: NAND(B, C), NAND(A, A) for A', output NAND: **3**.

**Self-test.**

1. NOT: NOR with tied inputs. OR: NOR then NOT. AND: NOR of A' and B' = (A' + B')' = AB.
2. NAND(A, B), NAND(C, D), NAND of those two: **3 gates**.
3. POS terms (A + B) and C: NOR(A, B), NOR(C, C) = C', output NOR of (A + B)' and C' = (A + B)C: **3 gates**.
4. **Four** NAND gates (figure in step 2).
5. A'B + A'B' = A'; A' + AB' = A' + B' = (AB)': **one NAND**.

<!--/ANSWERS-->
