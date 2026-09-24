# 03 — Superposition theorem

<div class="sub">Class notes p.6–9 · 2 board questions · needs 01 (source internal resistances), 02 (dividers)</div>

## Map

[[map:1 The statement > 2 Switching a source off > 3 One source at a time > 4 Add with signs > 5 Where it fails|here=1]]

## The questions this file answers

- <span class="tag">Class p.7</span> Calculate the current I using the superposition theorem (10 V, 2 A, two resistors).
- <span class="tag">Class p.9</span> Calculate the current I_{1} using superposition (two 5 V sources across 1 kΩ).

---

## Build

### 1–3 · The method

:::q <span class="tag">Class p.7</span>
Calculate the value of current I using the superposition theorem.
:::

[[fig:sp_q|The board circuit. I is the current down through the 2 Ω resistor.|w=55]]

:::note Units on the board
The board labels read "4k" and "2k", but the professor's working (10 × 2/6 = 10/3 V, then 5/3 A) treats them as **4 Ω and 2 Ω**. The pack uses ohms, so every number stays consistent. A full computer solve of this circuit gives exactly the professor's answer, **3 A**.
:::

:::guess Guess first
Two sources push current into the 2 Ω. Would you try solving for both at once, or one at a time? If one at a time, what do you do with the other source?
:::

**Statement** (class p.6): in a **linear** circuit with several independent sources, the response in any element (a current or a voltage) is the **algebraic sum** of the responses produced by **each source acting alone**.

It works because a linear circuit's response is a weighted sum of its source values, so each source's share can be found separately.

**Switching a source off** = replacing it with its **internal resistance** (class p.7, and 01 step 2):

[[fig:deactivate|Only independent sources are switched off. A dependent source always stays in the circuit.|w=90]]

**Case 1: 10 V alone** (2 A source → open):

[[fig:sp_c1||w=50]]

4 Ω and 2 Ω are in series across 10 V. By voltage division, V_{2Ω} = 10 × \frac{2}{6} = \frac{10}{3} V, so **I_{1} = \frac{10/3}{2} = \frac{5}{3} A ↓**.

**Case 2: 2 A alone** (10 V source → short):

[[fig:sp_c2||w=50]]

With the 10 V shorted, the 4 Ω runs from A to the bottom rail, so it is now **in parallel** with the 2 Ω. The 2 A splits by current division: **I_{2} = 2 × \frac{4}{4 + 2} = \frac{4}{3} A ↓**.

**Step 3: add, with signs.** Both cases push current **down** through the 2 Ω, so they add:

$$I = I_{1} + I_{2} = \frac{5}{3} + \frac{4}{3} = 3 A$$

**Cross-check without superposition.** One node equation at A: \frac{10 − V_{A}}{4} + 2 = \frac{V_{A}}{2}, so V_{A} = 6 V and I = 6/2 = **3 A** ✓.

:::check Check 1
(a) In case 2, why is the 4 Ω in *parallel* with the 2 Ω, when it was in *series* in case 1? (b) If the 2 A source pointed downwards instead, what would I be?
:::

### 4 · Signs matter

Pick a reference direction for the answer **once**, before the cases. In each case, a current that flows **against** that direction enters the sum as **negative**. The class example happened to have both cases in the same direction.

### 5 · Where superposition fails

:::q <span class="tag">Class p.9</span>
Calculate the value of current I_{1} using superposition.
:::

[[fig:sp_5v|Both sources have + at the top, as drawn in class. Both sit directly across the 1 kΩ.|w=55]]

:::guess Guess first
Apply superposition mechanically: left source alone, then right source alone. Add. Now look at the circuit: what voltage is actually across the 1 kΩ?
:::

- Mechanically: left 5 V alone gives 5 mA, right 5 V alone gives 5 mA, so the "sum" is **10 mA** ✗.
- Actually: both ideal sources hold the 1 kΩ at **5 V**, so **I_{1} = 5 mA** ✅.

The mechanical method went wrong because "switching off" the right source means **shorting** it, and that short sits across the left source and the resistor. The case-1 sub-circuit is impossible (a 5 V source shorted), so superposition cannot even start. This is the professor's **limitation 3**: "sometimes gives false results in ideal circuits". Ideal voltage sources in **parallel** (or ideal current sources in **series**) cannot be switched off one at a time.

**The limitations, complete:**

| Limitation | Why |
|---|---|
| **Linear circuits only** | the sum rule *is* linearity; a diode or transistor switch breaks it (class p.7: non-linear, unilateral) |
| **Not for power** | P = I^{2}R is not linear in I. See below |
| **Dependent sources are never switched off** | their value is set by a circuit variable, not by an outside excitation |
| **Ideal sources that conflict** | parallel ideal V sources / series ideal I sources: the "off" sub-circuit is impossible (Q above) |

**Why power can't be superposed**, using the Q from step 1:

| | Current in 2 Ω | Power in 2 Ω |
|---|---|---|
| 10 V alone | 5/3 A | (5/3)^{2} × 2 = 5.56 W |
| 2 A alone | 4/3 A | (4/3)^{2} × 2 = 3.56 W |
| "sum of powers" | | 9.11 W ✗ |
| **actual** (I = 3 A) | 3 A | 3^{2} × 2 = **18 W** ✅ |

Superpose the **currents**, then square.

:::check Check 2
Why does squaring break superposition? Give the one-line algebra reason.
:::

---

## Exam form

**Statement.** In a linear, bilateral network containing more than one independent source, the response in any element equals the algebraic sum of the responses caused by each independent source acting alone, with all other independent sources replaced by their internal resistances (V source → short, I source → open). Dependent sources remain active.

**Procedure.**
1. Choose the reference direction of the unknown.
2. Keep one independent source; switch off the others (V → short, I → open). Keep dependent sources.
3. Find that source's contribution with dividers or series–parallel reduction.
4. Repeat for every independent source.
5. Add the contributions algebraically (with signs).

**Limitations.** Not for non-linear or unilateral elements · not for power · dependent sources stay on · fails for conflicting ideal sources.

## Traps

- Removing a voltage source (leaving an open) instead of **shorting** it. The class p.9 Step 1 sketch does this.
- Switching off a dependent source.
- Adding powers.
- Losing the sign when a contribution flows opposite to the chosen direction.

## Self-test

1. State superposition in one sentence, including what happens to the other sources.
2. What is the internal resistance of an ideal current source, and what does it become when switched off?
3. In the step-1 circuit, find the voltage at node A from each source separately, then add.
4. Can superposition find the power in a resistor directly? What do you do instead?
5. A circuit has one independent source and one dependent source. How many superposition cases are there?

<!--ANSWERS-->
## Answers

**Check 1.** (a) Shorting the 10 V source connects the 4 Ω's left end to the bottom rail, so both resistors now join node A to the bottom rail: parallel. (b) I_{2} = −4/3 A, so I = 5/3 − 4/3 = **1/3 A**.

**Check 2.** (I_{1} + I_{2})^{2} = I_{1}^{2} + I_{2}^{2} + 2I_{1}I_{2}. Adding the separate powers loses the 2I_{1}I_{2} cross term.

**Self-test.**

1. Response = algebraic sum of each independent source's response acting alone; the other independent sources are replaced by their internal resistances; dependent sources stay.
2. ∞; it becomes an **open** circuit.
3. 10 V alone: V_{A} = 10/3 V. 2 A alone: V_{A} = 2 × (4 ∥ 2) = 2 × 4/3 = 8/3 V. Sum = **6 V** ✓ (matches the node equation).
4. No. Superpose the current (or voltage), then compute P = I^{2}R.
5. **One**: only independent sources get their own case.
<!--/ANSWERS-->
