# 04 — Thévenin's and Norton's theorems

<div class="sub">Class notes p.10–11, p.15 · 1 board question (with a dependent source) · needs 01, 02, 03</div>

## Map

[[map:1 The idea > 2 V_{Th}: open-circuit voltage > 3 R_{Th} with a dependent source > 4 Load current > 5 Norton: the same, as a current source|here=1]]

## The question this file answers

- <span class="tag">Class p.11</span> Determine the load current using Thévenin's theorem (10 V source, dependent source 2I, R_{L} = 1 kΩ).

---

## Build

:::q <span class="tag">Class p.11</span>
Determine the load current I_{L} using Thévenin's theorem.
:::

[[fig:th_q|The board circuit. I is the current in the left 2 kΩ, flowing right. The dependent source is a CCVS of value 2I, with + at the top.|w=65]]

:::note Units
With kΩ and mA, "2I" means 2 kΩ × I (01, step 3): I = 1 mA gives 2 V. The notes stop after setting up Step 1; the rest below is the standard method, with every number confirmed by computer.
:::

:::guess Guess first
Without solving: if R_{L} changed from 1 kΩ to 5 kΩ, would you want to re-solve the whole circuit? What would you rather have?
:::

### 1 · The idea

Any **linear** two-terminal network, however complicated, behaves at its terminals **exactly like one voltage source V_{Th} in series with one resistance R_{Th}**. Replace the whole network with that pair and the load is easy, for any R_{L}.

[[fig:th_eq|The Thévenin equivalent: I_{L} = V_{Th} / (R_{Th} + R_{L}).|w=40]]

**Procedure** (class p.10):
1. Remove the load R_{L} (or Z_{L}).
2. Find V_{Th}, the **open-circuit** voltage across the load terminals.
3. Find R_{Th} across the same terminals.
4. Put R_{L} back on the equivalent: I_{L} = V_{Th} / (R_{Th} + R_{L}).

### 2 · V_{Th}: the open-circuit voltage

[[fig:th_voc|Load removed. No current flows in the right 2 kΩ (it leads to an open end), so V_{Th} = V_{A}.|w=60]]

Units: V, mA, kΩ. Take I in the left 2 kΩ:

- Left resistor: I = \frac{10 − V_{A}}{2}
- Middle branch, flowing down: \frac{V_{A} − 2I}{2}. It is the only other path out of A, so it carries all of I.
- KCL at A: I = \frac{V_{A} − 2I}{2} ⇒ **V_{A} = 4I**
- Substitute: I = \frac{10 − 4I}{2} ⇒ I = \frac{5}{3} mA ⇒ V_{A} = \frac{20}{3} V

$$V_{Th} = 20/3 ≈ 6.67 V$$

:::check Check 1
Why does no current flow in the right-hand 2 kΩ here, and why does that make V_{Th} = V_{A}?
:::

### 3 · R_{Th} when there is a dependent source

:::guess Guess first
Switch off the 10 V source and "look in" from B: 2 kΩ in series with (2 kΩ ∥ 2 kΩ) = 3 kΩ. What is wrong with doing that here?
:::

The dependent source **stays on** (03), and it changes how current flows. So resistors alone don't give R_{Th}. Two correct methods; both give the same answer.

**Method A: R_{Th} = V_{oc} / I_{sc}.** Short the terminals and find the short-circuit current:

[[fig:th_isc|B shorted to the bottom rail. Now the right 2 kΩ carries current too.|w=60]]

KCL at A: I = \frac{V_{A} − 2I}{2} + \frac{V_{A}}{2} ⇒ V_{A} = 2I. With I = \frac{10 − 2I}{2}: I = 2.5 mA, V_{A} = 5 V, so I_{sc} = \frac{5}{2} = **2.5 mA**.

$$R_{Th} = \frac{V_{oc}}{I_{sc}} = \frac{20/3}{2.5} = 8/3 ≈ 2.67 kΩ$$

**Method B: test source** (the professor's method, class p.10: R_{Th} = V_{dc} / I_{dc}). Switch off the **independent** source only, keep 2I, apply a test voltage V_{t} at the terminals and find the current I_{t} it drives:

[[fig:th_test|10 V replaced by a short; the dependent source is still on; the test source V_{t} is at B.|w=60]]

With the 10 V shorted, the left 2 kΩ runs from ground to A, so I = \frac{0 − V_{A}}{2} = −\frac{V_{A}}{2}. Currents leaving A downwards:

- through the left 2 kΩ: \frac{V_{A}}{2}
- through the middle branch: \frac{V_{A} − 2I}{2} = \frac{V_{A} + V_{A}}{2} = V_{A}

Total = 1.5 V_{A}, so A looks like \frac{1}{1.5} = \frac{2}{3} kΩ to ground. Then R_{Th} = 2 + \frac{2}{3} = **8/3 kΩ** ✓, the same as method A.

The 3 kΩ from the Guess box is **wrong**: it ignores that the dependent source doubles the middle branch's current.

:::check Check 2
(a) In method B, why is I negative? (b) If the circuit had **no** independent source at all, which method would still work, and why?
:::

### 4 · The load current

[[fig:th_eq_num|The whole left side, replaced by its Thévenin equivalent.|w=40]]

$$I_{L} = \frac{V_{Th}}{R_{Th} + R_{L}} = \frac{20/3}{8/3 + 1} = \frac{20}{11} ≈ 1.82 mA$$

Confirmed by solving the full original circuit with R_{L} in place: **1.818 mA**. For R_{L} = 5 kΩ it is now one line: 6.67 / 7.67 = 0.87 mA.

### 5 · Norton: the same network as a current source

Norton's equivalent is a **current source I_{N} in parallel with R_{N}** (class p.15). By source transformation (02, step 4):

$$I_{N} = I_{sc} = \frac{V_{Th}}{R_{Th}}      R_{N} = R_{Th}$$

[[fig:no_eq_num|Norton equivalent of the same network: 2.5 mA in parallel with 2.67 kΩ.|w=60]]

Current division: I_{L} = 2.5 × \frac{8/3}{8/3 + 1} = **20/11 mA** ✓. Same answer.

**Norton procedure** (class p.15): (i) remove the load; (ii) find R_{N}, exactly as for R_{Th}; (iii) short the load terminals and find the short-circuit current I_{N}; (iv) draw I_{N} ∥ R_{N} with the load.

:::check Check 3
A network has V_{Th} = 12 V and R_{Th} = 4 kΩ. Give its Norton equivalent.
:::

---

## Exam form

**Thévenin's theorem.** Any linear bilateral network seen from two terminals can be replaced by a voltage source V_{Th} (the open-circuit voltage at those terminals) in series with R_{Th} (the resistance seen at the terminals with all independent sources switched off).

**Norton's theorem.** The same network can be replaced by a current source I_{N} (the short-circuit current) in parallel with R_{N} = R_{Th}.

**Link:** V_{Th} = I_{N}·R_{Th}.

**R_{Th} with dependent sources:** keep them on; use V_{oc}/I_{sc}, or apply a test source: R_{Th} = V_{t}/I_{t}.

## Traps

- Switching off the dependent source when finding R_{Th}.
- Using the test-source method but forgetting to switch off the **independent** sources (the class p.10 sketch still shows V_{in}; it must be zeroed).
- Measuring V_{Th} with the load still connected.
- Norton: I_{N} is the **short-circuit** current, not the current in the original load.

## Self-test

1. State Thévenin's theorem in two lines.
2. Which two measurements, both at the terminals, give V_{Th} and R_{Th} for any linear network?
3. For the board circuit, what would R_{Th} be if the dependent source were replaced by a plain wire?
4. Find I_{L} for the board circuit if R_{L} = 8/3 kΩ. What is special about that value? (Hint: 05.)
5. Convert V_{Th} = 6 V, R_{Th} = 3 kΩ into Norton form.

<!--ANSWERS-->
## Answers

**Check 1.** The right 2 kΩ ends at an open terminal, so there is no path: I = 0, voltage drop = 0, so V_{B} = V_{A}.

**Check 2.** (a) With the 10 V shorted, current flows from ground *into* A through the left resistor, which is opposite to the defined direction of I. (b) Only the test-source method: V_{oc} = 0 and I_{sc} = 0, so V_{oc}/I_{sc} is 0/0.

**Check 3.** I_{N} = 12/4 = **3 mA** in parallel with **4 kΩ**.

**Self-test.**

1. See Exam form.
2. The open-circuit voltage (= V_{Th}) and the short-circuit current (I_{sc}); R_{Th} = V_{oc}/I_{sc}.
3. The middle branch becomes a plain 2 kΩ: R_{Th} = 2 + (2 ∥ 2) = **3 kΩ**.
4. \frac{20/3}{16/3} = **1.25 mA**. R_{L} = R_{Th}: this load receives the maximum possible power.
5. **2 mA in parallel with 3 kΩ**.
<!--/ANSWERS-->
