# 02 — Dividers, source transformation, ladders

<div class="sub">Class notes p.1, p.4–5 · 4 board questions · needs 01</div>

## Map

[[map:1 Voltage division > 2 Current division > 3 Division with AC > 4 Source transformation > 5 Ladder reduction|here=1]]

## The questions this file answers

- <span class="tag">Class p.4</span> 15 V across 3 kΩ and 6 kΩ in series. Find V_{1} and V_{2}.
- <span class="tag">Class p.5</span> A 12 A source feeds 3 kΩ ∥ 6 kΩ ∥ 4 kΩ. Find the current in each.
- <span class="tag">Class p.5</span> v = 10 sin(2000t + 30°) V across 3 kΩ and 7 kΩ in series. Find v_{1} and v_{2}.
- <span class="tag">Class p.1</span> An infinite ladder: 3 kΩ shunt, 5 kΩ series, 7 kΩ shunt, 11 kΩ series, 13 kΩ shunt, … Find R_{eq}.

---

## Build

### 1 · Voltage division

:::q <span class="tag">Class p.4</span>
15 V is applied across 3 kΩ and 6 kΩ in series. Find the voltage across each.
:::

[[fig:vdr|Series resistors carry the same current, so each one's voltage is proportional to its resistance.|w=55]]

:::guess Guess first
Which resistor gets more voltage, and roughly how much?
:::

Series means **one current**: I = \frac{V}{R_{1} + R_{2}}. Each voltage is that current times its own resistance:

$$V_{1} = V·\frac{R_{1}}{R_{1} + R_{2}}      V_{2} = V·\frac{R_{2}}{R_{1} + R_{2}}$$

V_{1} = 15 × \frac{3}{9} = **5 V**, V_{2} = 15 × \frac{6}{9} = **10 V**. They add back to 15 V (KVL).

:::check Check 1
12 V across 1 kΩ, 2 kΩ, 3 kΩ in series. Voltage across the 2 kΩ?
:::

### 2 · Current division

:::q <span class="tag">Class p.5</span>
A 12 A current source feeds 3 kΩ, 6 kΩ and 4 kΩ in parallel. Find I_{1}, I_{2}, I_{3}.
:::

[[fig:cdr12|Parallel branches share one voltage, so the current splits in inverse proportion to resistance.|w=60]]

:::guess Guess first
Which branch carries the most current? Rank the three before calculating.
:::

Parallel means **one voltage**. For two branches that gives the class rule, where **each branch gets the *other* resistor on top**:

$$I_{1} = I·\frac{R_{2}}{R_{1} + R_{2}}      I_{2} = I·\frac{R_{1}}{R_{1} + R_{2}}$$

For three branches, the professor's method is to merge the other two branches into one, then apply the two-branch rule:

| Branch | The other two, merged | Current |
|---|---|---|
| 3 kΩ | 6 ∥ 4 = 2.4 kΩ | 12 × \frac{2.4}{2.4 + 3} = **5.33 A** |
| 6 kΩ | 3 ∥ 4 = \frac{12}{7} kΩ | 12 × \frac{12/7}{12/7 + 6} = **2.67 A** |
| 4 kΩ | 3 ∥ 6 = 2 kΩ | 12 × \frac{2}{2 + 4} = **4 A** |

Check: 5.33 + 2.67 + 4 = 12 A (KCL). Faster in one line: the current in each branch is proportional to its **conductance** 1/R, i.e. to 1/3 : 1/6 : 1/4 = 4 : 2 : 3, so 12 A splits as 12 × \frac{4}{9}, 12 × \frac{2}{9}, 12 × \frac{3}{9}.

:::note Label in the class notes
The side note "I_{2} + I_{3} = 6×4/10 = 2.4" is the **resistance** 6 ∥ 4 = 2.4 kΩ, not a current.
:::

:::check Check 2
(a) 10 mA into 1 kΩ ∥ 4 kΩ: current in the 1 kΩ? (b) Why does the *smaller* resistor take the *larger* current?
:::

### 3 · Division works for AC too

:::q <span class="tag">Class p.5</span>
v = 10 sin(2000t + 30°) V is applied across 3 kΩ and 7 kΩ in series. Find v_{1} and v_{2}.
:::

[[fig:acvdr||w=50]]

:::guess Guess first
Does v_{1} have the same phase angle as the source, or a different one?
:::

A resistor's v = iR holds **at every instant**, so the divider ratio applies to the whole waveform. Resistors do not shift phase:

$$v_{1} = 0.3 × 10 sin(2000t + 30°) = 3 sin(2000t + 30°) V      v_{2} = 7 sin(2000t + 30°) V$$

[[fig:acplot|All three waves cross zero together: same frequency, same phase. Only the amplitude is divided.|w=80]]

This holds only because both elements are **resistors**. With an L or C in the divider, the ratio becomes complex and shifts the phase. That case uses impedances (05, conjugate matching).

### 4 · Source transformation

:::guess Predict
A 10 V source with 2 kΩ in series. Short its terminals: what current flows? Leave them open: what voltage appears? Could a current source with a resistor in parallel give the same two answers?
:::

[[fig:srctx|Both give the same open-circuit voltage (V) and the same short-circuit current (V/R), so no outside circuit can tell them apart.|w=75]]

A **voltage source V in series with R** is equivalent to a **current source I = V/R in parallel with the same R** (class p.4), as seen from the terminals a–b.

For the Predict: short-circuit current = 10/2k = **5 mA**; open-circuit voltage = **10 V**. So it is equivalent to 5 mA ∥ 2 kΩ, and 5 mA × 2 kΩ = 10 V, the same terminal behaviour.

It is the bridge between Thévenin and Norton in 04: I_{N} = V_{Th} / R_{Th}.

:::check Check 3
Convert 3 mA in parallel with 4 kΩ into a voltage-source form.
:::

### 5 · Series–parallel reduction: the infinite ladder

:::q <span class="tag">Class p.1 · the first question of the course</span>
Find R_{eq} of the infinite ladder: 3 kΩ shunt, 5 kΩ series, 7 kΩ shunt, 11 kΩ series, 13 kΩ shunt, … ∞.
:::

[[fig:ladder|Read from the far end: each shunt sits in parallel with everything to its right; each series resistor adds.|w=80]]

:::guess Guess first
The first resistor is 3 kΩ, directly across a–b. Can R_{eq} be more than 3 kΩ?
:::

**Rule: reduce from the far end towards the terminals.** Written out, the ladder is:

$$R_{eq} = 3 ∥ (5 + 7 ∥ (11 + 13 ∥ (…)))  kΩ$$

The Guess answer: the 3 kΩ is in parallel with everything else, so **R_{eq} < 3 kΩ**, always.

The values 3, 5, 7, 11, 13 are the **prime numbers**. Assuming that pattern continues (the notes stop at 13), cut the ladder off after more and more resistors:

[[fig:ladder_plot|3 resistors give 2.400 kΩ, 5 give 2.329, 9 give 2.318. The far sections are huge resistors hidden behind parallel paths, so they barely change the answer.|w=80]]

**R_{eq} ≈ 2.318 kΩ** (converged; confirmed by computer). The professor may intend a different continuation, so ask.

:::key The standard trick, and why it fails here
For a ladder whose sections are **all identical** (series R, shunt R, repeated forever), cutting off the first section leaves the **same** infinite ladder. So R_{eq} = R + (R ∥ R_{eq}). Solving the quadratic gives R_{eq} = R(1 + √5)/2 ≈ 1.618 R.

Here every section is different, so the rest of the ladder never looks like the whole, and you must truncate.
:::

---

## Exam form

- **VDR**: V_{k} = V·\frac{R_{k}}{R_{total}}. **CDR (two branches)**: I_{1} = I·\frac{R_{2}}{R_{1}+R_{2}}.
- Division holds for any waveform when every element is a resistor. Phase is unchanged.
- **Source transformation**: V in series with R ⇔ V/R in parallel with R.
- **Ladder**: reduce from the far end. Identical infinite ladder: R_{eq} = R + R ∥ R_{eq}.

## Traps

- CDR with the **same** resistor on top (I·R_{1}/(R_{1}+R_{2}) for I_{1}) is the most common slip: the answer comes out swapped.
- Source transformation keeps R **the same size**. It changes from series to parallel, not in value.
- Forgetting that R_{eq} of a network with a shunt resistor across the terminals must be smaller than that resistor.

## Self-test

1. 20 V across 2 kΩ and 8 kΩ in series. Both voltages?
2. 9 mA into 3 kΩ ∥ 6 kΩ. Both currents?
3. v = 6 sin(100t) V across 1 kΩ and 2 kΩ in series. v across the 2 kΩ?
4. Transform 12 V in series with 3 kΩ.
5. An infinite ladder of identical 1 kΩ sections (series then shunt). R_{eq}?

<!--ANSWERS-->
## Answers

**Check 1.** 12 × 2/6 = **4 V**.

**Check 2.** (a) 10 × 4/5 = **8 mA**. (b) Same voltage across both, and I = V/R, so the smaller R takes more current.

**Check 3.** 3 mA × 4 kΩ = **12 V in series with 4 kΩ**.

**Self-test.**

1. **4 V** and **16 V**.
2. 3 kΩ: 9 × 6/9 = **6 mA**; 6 kΩ: **3 mA**.
3. \frac{2}{3} × 6 sin(100t) = **4 sin(100t) V**.
4. **4 mA in parallel with 3 kΩ**.
5. R(1 + √5)/2 = **1.618 kΩ**.
<!--/ANSWERS-->
