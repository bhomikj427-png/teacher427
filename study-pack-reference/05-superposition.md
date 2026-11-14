# 05 — Superposition theorem

<div class="sub">Class notes p.6–9, set 2 p.7–9 · MTE syllabus item 5 (DC and AC) · 2 board questions + 1 textbook · needs 01 (source internal resistances), 02 (dividers)</div>

## Map

[[map:1 The statement > 2 Switching a source off > 3 One source at a time > 4 Add with signs > 5 Where it fails > 6 AC sources|here=1]]

## The questions this file answers

- <span class="tag">Class p.7</span> Calculate the current I using the superposition theorem (10 V, 2 A, two resistors).
- <span class="tag">Class p.9 · set 2 p.9</span> Calculate the current I_{1} using superposition (two 5 V sources across 1 kΩ).
- <span class="tag">textbook</span> A DC and an AC source in one circuit: find i(t).

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

:::q <span class="tag">Class p.9 · set 2 p.9</span>
Calculate the value of current I_{1} using superposition.
:::

[[fig:sp_5v|Both sources have + at the top, as drawn in class. Both sit directly across the 1 kΩ.|w=55]]

:::guess Guess first
Apply superposition exactly by the rule: left source alone (right source → its internal resistance), then right source alone. Add. Now look at the circuit: what voltage is actually across the 1 kΩ?
:::

**The professor's working (set 2 p.9), by the rule:**

- **Case 1, left 5 V alone.** The right source is replaced by its internal resistance, 0 Ω: a **short**. That short sits directly across the 1 kΩ, so **I_{1} = 0**.
- **Case 2, right 5 V alone.** By symmetry the left source becomes a short across the 1 kΩ: **I_{1} = 0**.
- **Sum:** I_{total} = 0 + 0 = **0 A**, which the professor labels **LIMITATION**.

**The true answer.** Both ideal sources hold the top rail at 5 V, so the 1 kΩ has 5 V across it (KVL round either loop): **I_{1} = \frac{5}{1k} = 5 mA**. Superposition gave 0 A. It is wrong here, not slightly off.

**Why it fails.** In each case the short that replaces the idle source is also placed **across the active source**. An ideal 5 V source shorted by a wire would need infinite current, so each case sub-circuit is impossible, and the "0" it produces means nothing. This is the professor's limitation "sometimes gives false results in ideal circuits" (set 2 p.8): **ideal voltage sources in parallel** (or ideal current sources in series) cannot be switched off one at a time.

:::note Two versions in the notes
The first set of notes (class p.9) sketched case 1 with the idle source **removed** (an open) instead of shorted. That gives 5 + 5 = 10 mA, also wrong, and for a second reason: an idle voltage source must be shorted, never opened. The set 2 version applies the rule correctly and shows the real point: the rule itself breaks down here. Learn the set 2 version.
:::

**The limitations, complete:**

| Limitation | Why |
|---|---|
| **Linear circuits only** | the sum rule *is* linearity; a diode breaks it (set 2 p.8: forward / reverse bias, superposition fails; class p.7: non-linear, unilateral) |
| **Not for power** | P = I^{2}R is not linear in I. See below |
| **Dependent sources are never switched off** | their value is set by a circuit variable, not by an outside excitation |
| **Ideal sources that conflict** | parallel ideal V sources / series ideal I sources: each case gives 0, the truth is 5 mA (Q above) |

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

### 6 · Superposition with AC sources

:::q <span class="tag">textbook</span>
A 10 V DC source and a 10 cos(1000t) V source drive 1 kΩ and 1 H in series. Find the steady-state current i(t).
:::

[[fig:ac_sp||w=48]]

:::guess Guess first
Can you turn both sources into phasors and add them?
:::

No: a phasor only exists **at one frequency**. DC is ω = 0, the other source is ω = 1000 rad/s. The impedance of the inductor is different at each (Z_{L} = jωL), so the circuit must be solved **once per frequency**, and the answers added **in the time domain**. This is the one case where superposition is not a choice but the only way.

**Case 1: DC alone** (AC source → short). At DC the inductor is a short (01): i_{1} = \frac{10}{1k} = **10 mA**.

**Case 2: AC alone** (DC source → short). At ω = 1000: Z = R + jωL = 1000 + j1000 Ω = 1414∠45° Ω.

$$I_{2} = \frac{10∠0°}{1414∠45°} = 7.07∠−45° mA  ⇒  i_{2}(t) = 7.07 cos(1000t − 45°) mA$$

**Add in time:**

$$i(t) = 10 + 7.07 cos(1000t − 45°) mA$$

[[fig:ac_sp_plot|The AC part rides on the 10 mA DC level. A time simulation of the circuit gives the same curve.|w=80]]

**Same frequency?** If all sources share one ω, you may add their **phasors** directly, and the result is the same as adding in time. The rule for switching sources off does not change: V → short, I → open, dependent sources stay.

:::check Check 3
Would I_{2} change if the inductor were 2 H? Give the new phasor.
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

**AC.** Sources at different frequencies: solve each at its own ω (Z_{L} = jωL, Z_{C} = 1/jωC), convert each to a time function, add in time. Same frequency: phasors may be added.

## Traps

- Removing a voltage source (leaving an open) instead of **shorting** it. The class p.9 sketch does this; set 2 p.9 corrects it.
- Adding phasors of **different** frequencies.
- Switching off a dependent source.
- Adding powers.
- Losing the sign when a contribution flows opposite to the chosen direction.

## Self-test

1. State superposition in one sentence, including what happens to the other sources.
2. What is the internal resistance of an ideal current source, and what does it become when switched off?
3. In the step-1 circuit, find the voltage at node A from each source separately, then add.
4. Can superposition find the power in a resistor directly? What do you do instead?
5. A circuit has one independent source and one dependent source. How many superposition cases are there?
6. For the two-5 V circuit, what does superposition give, and what is the true I_{1}?

<!--ANSWERS-->
## Answers

**Check 1.** (a) Shorting the 10 V source connects the 4 Ω's left end to the bottom rail, so both resistors now join node A to the bottom rail: parallel. (b) I_{2} = −4/3 A, so I = 5/3 − 4/3 = **1/3 A**.

**Check 2.** (I_{1} + I_{2})^{2} = I_{1}^{2} + I_{2}^{2} + 2I_{1}I_{2}. Adding the separate powers loses the 2I_{1}I_{2} cross term.

**Check 3.** Z = 1000 + j2000 = 2236∠63.4° Ω ⇒ I_{2} = **4.47∠−63.4° mA**.

**Self-test.**

1. Response = algebraic sum of each independent source's response acting alone; the other independent sources are replaced by their internal resistances; dependent sources stay.
2. ∞; it becomes an **open** circuit.
3. 10 V alone: V_{A} = 10/3 V. 2 A alone: V_{A} = 2 × (4 ∥ 2) = 2 × 4/3 = 8/3 V. Sum = **6 V** ✓ (matches the node equation).
4. No. Superpose the current (or voltage), then compute P = I^{2}R.
5. **One**: only independent sources get their own case.
6. Superposition: 0 + 0 = **0 A**. True: **5 mA**. Parallel ideal voltage sources cannot be switched off one at a time.
<!--/ANSWERS-->
