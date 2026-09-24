# 01 — Circuit elements and sources

<div class="sub">Class notes p.1–3 · needed by every other file · no board question yet: the openers here are Predict prompts, not exam questions</div>

## Map

[[map:1 Active vs passive > 2 Independent sources > 3 Dependent sources > 4 R, L, C laws > 5 What can't jump|here=1]]

The professor's classification (class p.1):

| Element | Kind | Examples |
|---|---|---|
| **Active** · independent | fixed value | voltage source, current source |
| **Active** · dependent | value set by another circuit quantity | VCVS, VCCS, CCVS, CCCS |
| **Passive** | cannot deliver net energy | R, L, C |

---

## Build

### 1 · Active vs passive

:::guess Predict
A phone charger's transistor amplifies a signal. Does the transistor create energy, or take it from somewhere?
:::

An **active element can deliver net energy** to the rest of the circuit. A **passive element cannot**:

- R turns energy into heat.
- L and C store energy and give it back, but never more than they took.

An amplifier (transistor, op-amp) is **active**. It does not create energy: it draws it from its DC supply and uses it to make a bigger copy of the input signal.

:::note Wording in the class notes
Class p.2 says an active element "doesn't require any external energy source". Read that as: *the element is the thing that supplies energy to the circuit*. It does not mean an amplifier runs without a supply. It doesn't.
:::

:::check Check 1
(a) Is a battery being charged acting as active or passive at that moment? (b) Why is an op-amp called active even though it needs ±15 V to work?
:::

### 2 · Independent sources

:::guess Predict
An ideal 10 V source is connected to 1 Ω, then to 1 MΩ. What happens to its voltage and to its current in each case?
:::

- **Ideal voltage source**: keeps its voltage **fixed whatever current flows**. Internal resistance = **0**.
- **Ideal current source**: keeps its current **fixed whatever voltage appears**. Internal resistance = **∞**.

Those two internal resistances return in 03: "switching off" a source means replacing it with its internal resistance, so a V source becomes a **short** and an I source becomes an **open**.

[[fig:sources|Circle = independent source. Diamond = dependent source. + / − inside = voltage source; arrow inside = current source.|w=95]]

### 3 · Dependent (controlled) sources

:::guess Predict
A transistor's collector current is about 100 times its base current. What kind of source would you draw to model that?
:::

A **dependent source** outputs a value set by a voltage or current **somewhere else in the circuit** (class p.2: "value depends on another parameter; it is not constant").

| Name | Output | Controlled by | Law | Unit of the constant |
|---|---|---|---|---|
| **VCVS** | voltage | a voltage V_{x} | V = μ·V_{x} | none |
| **CCVS** | voltage | a current I_{x} | V = r·I_{x} | Ω |
| **VCCS** | current | a voltage V_{x} | I = g·V_{x} | S (siemens) |
| **CCCS** | current | a current I_{x} | I = β·I_{x} | none |

The notes link each one to real hardware: **op-amp (741) → VCVS** and **BJT (BC547) → CCCS**, because I_{C} = β·I_{B}.

:::trap Units of a CCVS
In 04 the source is marked **2I**. A voltage equal to "2 × a current" only makes sense if 2 carries units of Ω. With kΩ and mA, 2I means **2 kΩ × I**: I = 1.5 mA gives 3 V.
:::

:::check Check 2
(a) Draw the symbol for a CCCS with value 3I_{1}. (b) Which of the four is the op-amp model, and what is μ called for an op-amp?
:::

### 4 · The R, L, C laws

:::guess Predict
If the current in an inductor is constant, what voltage appears across it?
:::

| | Resistor R | Inductor L | Capacitor C |
|---|---|---|---|
| Law | v = iR | v = L·\frac{di}{dt} | i = C·\frac{dv}{dt} |
| Where it comes from | Ohm: V ∝ I | ψ = Nφ = Li, and v = \frac{dψ}{dt} | q = Cv; differentiate: \frac{dq}{dt} = i |
| Energy | dissipated as heat | stored in the **magnetic** field: ½Li^{2} | stored in the **electric** field: ½Cv^{2} |
| DC steady state | resistor | **short circuit** (di/dt = 0 ⇒ v = 0) | **open circuit** (dv/dt = 0 ⇒ i = 0) |

:::note Slip in the class notes
Class p.3 writes the inductor law as "d/dt (CI) = C dI/dt". It is **L**: v = d(Li)/dt = **L di/dt**. The side box on the same page (ψ = Li) confirms it.
:::

### 5 · What can't jump

:::guess Predict
A switch connects 10 V to an R–L circuit at t = 0. Just after the switch closes, which one can jump instantly, the inductor's current or its voltage?
:::

- **Inductor current cannot change instantly.** A jump would need di/dt = ∞, so v = L·di/dt = ∞.
- **Capacitor voltage cannot change instantly.** A jump would need i = C·dv/dt = ∞.
- A **resistor** has no memory: its current and voltage can jump (class p.20).

[[fig:continuity_plot|The inductor current rises smoothly from 0. The inductor voltage jumps from 0 to 10 V at the instant of switching.|w=80]]

:::check Check 3
(a) Which quantity of a capacitor may jump at t = 0: its voltage or its current? (b) Why does a large spark appear when you open a switch in series with a motor coil?
:::

---

## Exam form

- **Active element**: can deliver net energy to the circuit (sources; amplifiers, which draw from a supply). **Passive**: cannot (R, L, C).
- **Dependent source**: its value depends on another circuit variable. Four types: VCVS, VCCS, CCVS, CCCS (table in step 3, with symbols).
- **Laws**: v = iR · v = L di/dt · i = C dv/dt.
- **Continuity**: i_{L}(0⁺) = i_{L}(0⁻) and v_{C}(0⁺) = v_{C}(0⁻).
- **DC steady state**: L → short, C → open.

## Traps

- "An inductor stores current" and "a capacitor stores voltage" (class-note wording) → the exam answer is **energy in a magnetic / electric field**.
- Writing C for L in v = L di/dt.
- A dependent source's value is **not** a fixed number: it changes whenever its controlling variable changes.

## Self-test

1. Name the four dependent sources and give the unit of each constant.
2. Derive v = L di/dt starting from ψ = Nφ.
3. Why is an inductor a short circuit at DC steady state?
4. Energy stored in 1 mH carrying 10 mA?
5. True or false: a resistor's current cannot change suddenly.

<!--ANSWERS-->
## Answers

**Check 1.** (a) Passive: it is absorbing energy at that moment. (b) It delivers more signal power to the load than the input provides; the extra comes from its supply.

**Check 2.** (a) A diamond with an arrow inside, labelled 3I_{1}. (b) VCVS; μ is the open-loop (voltage) gain.

**Check 3.** (a) Its current (i = C dv/dt can jump; v cannot). (b) The coil current cannot stop instantly, so v = L di/dt becomes huge and arcs across the opening contacts.

**Self-test.**

1. VCVS (μ, no unit) · CCVS (r, Ω) · VCCS (g, S) · CCCS (β, no unit).
2. ψ = Nφ ∝ i ⇒ ψ = Li; v = dψ/dt = d(Li)/dt = L di/dt.
3. At steady state di/dt = 0, so v = L·0 = 0 whatever the current: that is a short.
4. ½ × 1×10^{−3} × (10×10^{−3})^{2} = **50 nJ**.
5. False: a resistor has no memory.
<!--/ANSWERS-->
