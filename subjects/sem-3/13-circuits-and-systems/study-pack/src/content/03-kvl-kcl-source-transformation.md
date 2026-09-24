# 03 — KVL, KCL and source transformation

<div class="sub">Class notes p.4–5, set 2 p.4, p.11 · MTE syllabus item 3 · 1 board question + 1 textbook problem · needs 02</div>

## Map

[[map:1 KCL: currents at a node > 2 KVL: voltages round a loop > 3 Power check > 4 Source transformation > 5 Using it on a class circuit|here=1]]

## The questions this file answers

- <span class="tag">textbook</span> A loop with 12 V, 2 kΩ, an opposing 4 V source and 4 kΩ: find i, each voltage, and each element's power.
- <span class="tag">Class p.4</span> Source transformation: V in series with R ⇔ V/R in parallel with R.
- <span class="tag">Class p.7 · set 2 p.8</span> The superposition circuit again, solved in three lines by source transformation.

The professor used both laws inside other methods (KCL in the nodal working on set 2 p.11; KVL in every divider). This file states them on their own, as the syllabus asks.

---

## Build

### 1 · KCL: what goes into a node comes out

:::guess Predict
5 mA and 3 mA flow into a node. 2 mA flows out along a third wire. What flows in the fourth wire, and which way?
:::

[[fig:kcl_node|One node, four wires.|w=40]]

**Kirchhoff's current law (KCL):** the algebraic sum of the currents at any node is zero. Equivalently, **total current in = total current out**.

$$Σ i_{in} = Σ i_{out}$$

Why it holds: charge cannot pile up at a node (a node stores no charge). So every coulomb that arrives per second must leave.

For the Predict: 5 + 3 = 2 + i_{x}, so **i_{x} = 6 mA, out**. If you had drawn i_{x} pointing in, you would get i_{x} = −6 mA: the same answer. A minus sign only means the real current flows against your arrow.

You already used KCL in 02: the three branch currents of the class p.5 question add back to the source, 5.33 + 2.67 + 4 = 12 A.

:::check Check 1
Currents into a node: 4 mA, −1 mA, i. Out of it: 7 mA. Find i.
:::

### 2 · KVL: round a loop, the voltages add to zero

:::q <span class="tag">textbook</span>
Find the loop current i, the voltage across each resistor, and the power of every element.
:::

[[fig:kvl_loop|The 4 V source has + at the top, so it pushes against the 12 V source.|w=55]]

:::guess Guess first
Which source "wins", and is the current in the direction of the arrow shown?
:::

**Kirchhoff's voltage law (KVL):** the algebraic sum of the voltages around any closed loop is zero.

$$Σ v_{rises} = Σ v_{drops}   (round any closed loop)$$

Why it holds: voltage is energy per unit charge. A charge that travels round a loop and returns to its start has the same energy it began with.

**Method.** Go round the loop in the direction of i (clockwise). A source traversed from − to + is a **rise**. A resistor traversed along i is a **drop** of iR. A source traversed from + to − is a **drop**.

- 12 V source, bottom to top (− to +): rise of 12 V.
- 2 kΩ: drop 2i. 4 V source, top to bottom (+ to −): drop 4 V. 4 kΩ: drop 4i.

$$12 = 2i + 4 + 4i  ⇒  i = \frac{8}{6} = \frac{4}{3} mA ≈ 1.33 mA$$

Voltages: v_{2kΩ} = 2 × \frac{4}{3} = **2.67 V**, v_{4kΩ} = **5.33 V**. Check round the loop: 12 = 2.67 + 4 + 5.33 ✓.

The Guess answer: the 12 V source wins, and i > 0 means the current does flow clockwise.

:::check Check 2
Swap the 4 V source (+ at the bottom, so it now helps). Find i.
:::

### 3 · The power check (02 §4, in use)

Sign rule from 02: current **entering +** means the element absorbs p = vi.

| Element | Current enters its… | Absorbed power |
|---|---|---|
| 12 V source | − terminal (current leaves +) | −12 × \frac{4}{3} = **−16 mW** (delivers 16 mW) |
| 4 V source | + terminal | +4 × \frac{4}{3} = **+5.33 mW** (it is being charged) |
| 2 kΩ | + (always, for a resistor) | (\frac{4}{3})^{2} × 2 = **+3.56 mW** |
| 4 kΩ | + | (\frac{4}{3})^{2} × 4 = **+7.11 mW** |
| **Sum** | | −16 + 5.33 + 3.56 + 7.11 = **0** ✓ |

Delivered = absorbed. Use this as the last line of any loop or node answer: if the powers do not add to zero, something upstream is wrong.

### 4 · Source transformation

:::guess Predict
A 10 V source with 2 kΩ in series. Short its terminals: what current flows? Leave them open: what voltage appears? Could a current source with a resistor in parallel give the same two answers?
:::

[[fig:srctx|Both give the same open-circuit voltage (V) and the same short-circuit current (V/R), so no outside circuit can tell them apart.|w=75]]

A **voltage source V in series with R** is equivalent to a **current source I = V/R in parallel with the same R** (class p.4; set 2 p.4 writes I = V/R under the current source), as seen from the terminals a–b.

For the Predict: short-circuit current = 10/2k = **5 mA**; open-circuit voltage = **10 V**. So it is equivalent to 5 mA ∥ 2 kΩ, and 5 mA × 2 kΩ = 10 V, the same terminal behaviour.

It is the bridge between Thévenin and Norton in 06: I_{N} = V_{Th} / R_{Th}.

:::trap Only works with a resistor
An **ideal** voltage source (no series R) has no current-source equivalent: V/0 is undefined. Same for an ideal current source with no parallel R.
:::

### 5 · Using it on a class circuit

:::q <span class="tag">Class p.7 · set 2 p.8</span>
Find I in the superposition circuit (10 V, 4 Ω, 2 Ω, 2 A) without superposition.
:::

[[fig:sp_q|The class circuit (05 §1).|w=50]]

Transform 10 V in series with 4 Ω into \frac{10}{4} = **2.5 A in parallel with 4 Ω**:

[[fig:sp_srctx|Now everything is in parallel between node A and the bottom rail.|w=62]]

Both current sources push up into A: 2.5 + 2 = 4.5 A. It flows into 4 Ω ∥ 2 Ω = \frac{4}{3} Ω, so V_{A} = 4.5 × \frac{4}{3} = **6 V** and **I = \frac{6}{2} = 3 A**, the professor's answer (05 §1) in three lines.

:::check Check 3
Convert 3 mA in parallel with 4 kΩ into a voltage-source form.
:::

---

## Exam form

- **KCL**: Σ currents into a node = Σ currents out (charge is conserved; a node stores no charge).
- **KVL**: Σ voltage rises = Σ voltage drops round any closed loop (energy is conserved).
- **Sign rule**: a negative answer means the real direction is opposite to the arrow you drew. Keep your arrow; report the sign.
- **Power balance**: Σ absorbed power = 0 over the whole circuit.
- **Source transformation**: V in series with R ⇔ V/R in parallel with R. Not for ideal sources.

## Traps

- Changing sign conventions half-way round a loop. Fix the direction once and apply the rise/drop rule to every element.
- Source transformation keeps R **the same size**. It changes from series to parallel, not in value.
- Transforming a source whose resistor is the one you are asked about: that resistor disappears into the equivalent. Keep the element you need outside the transformation.

## Self-test

1. State KCL and KVL, each with the conservation law behind it.
2. A node has 10 mA in and three outputs: 2 mA, 5 mA, i. Find i.
3. A loop has 9 V, 1 kΩ and 2 kΩ. Find i and check the power balance.
4. Transform 12 V in series with 3 kΩ.
5. Why is a negative answer from KCL not a mistake?

<!--ANSWERS-->
## Answers

**Check 1.** 4 + (−1) + i = 7 ⇒ **i = 4 mA** into the node.

**Check 2.** 12 + 4 = 6i ⇒ **i = 8/3 ≈ 2.67 mA**.

**Check 3.** 3 mA × 4 kΩ = **12 V in series with 4 kΩ**.

**Self-test.**

1. KCL: Σ i_{in} = Σ i_{out} at a node (conservation of charge). KVL: Σ v round a closed loop = 0 (conservation of energy).
2. 10 = 2 + 5 + i ⇒ **i = 3 mA**.
3. i = 9/3k = **3 mA**. Source delivers 9 × 3 = 27 mW; resistors absorb 9 + 18 = 27 mW ✓.
4. **4 mA in parallel with 3 kΩ**.
5. It only means the current flows opposite to the arrow you chose; the magnitude is still right.
<!--/ANSWERS-->
