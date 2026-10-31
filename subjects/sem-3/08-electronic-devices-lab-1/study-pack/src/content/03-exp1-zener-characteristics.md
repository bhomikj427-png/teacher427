# Exp 1 · Zener diode characteristics and dynamic resistance

<div class="sub">Manual pp. 7–8 · hands-on · CO1, CO2 · theory: ECE2101 unit 2 (pn junctions)</div>

[[map:0 Instruments > 1 Zener curve > 2 Regulator > 3 Clipper > 4 Clamper|here=2]]

**What you already have:** Ohm's law, and the meters from Exp 0.

**Three terms first:**

- **Diode:** a p-type and an n-type piece of silicon joined together (a *pn junction*). The p side is the **anode** and the n side is the **cathode** (the bar on the symbol). Current flows easily from anode to cathode.
- **Forward / reverse bias:** anode more positive than cathode = forward. The reverse = reverse.
- **Breakdown:** under enough reverse voltage, a junction suddenly conducts heavily.

:::q <span class="tag">Manual Exp 1, aim</span>
To plot the characteristics of a zener diode and find its dynamic resistance under reverse-biased condition. Viva form: "Why does a zener's reverse current rise sharply at one voltage, and what is its *dynamic* resistance?"
:::

:::guess Guess first
Sketch I against V for an ordinary diode, both directions, before reading on. Where does it conduct?
:::

## The idea: a diode that is meant to break down

[[fig:diode_iv|One curve, three regions. A zener is built so the left-hand breakdown happens at a chosen, sharp voltage V_{Z}.|w=80]]

1. **Forward:** almost no current until about 0.6–0.7 V (silicon), then current rises steeply. This is the same as any diode.
2. **Reverse, below V_{Z}:** only a tiny leakage current (µA). The diode is close to an open circuit.
3. **Reverse, at V_{Z}:** the junction **breaks down**. The current can rise from 1 mA to 10 mA while the voltage barely moves from V_{Z}.

Region 3 is what makes a zener useful: **a voltage that stays put while the current changes**, which is a voltage reference. Exp 2 uses exactly that.

**Why breakdown happens** (viva staple; from ECE2101 unit 2):

| | Zener breakdown | Avalanche breakdown |
|---|---|---|
| doping | heavy, so the junction is thin | light, so the junction is wide |
| mechanism | the field pulls electrons straight across (tunnelling) | fast carriers knock out new ones (chain reaction) |
| V_{Z} | below about 5 V | above about 6 V |
| temperature coefficient | negative | positive |

A 6.2 V zener is near the crossover and uses both mechanisms. That is why ~5–6 V zeners drift least with temperature. "Zener diode" is the trade name for any breakdown diode, whichever mechanism it uses.

**Dynamic resistance r_{z}:** in breakdown, how much the voltage moves per unit change of current:

$$r_{z} = \frac{ΔV_{Z}}{ΔI_{Z}}$$

A small r_{z} (tens of ohms or less) means a better voltage reference. It is called *dynamic* because it is the slope of the curve, not V/I at one point. V_{Z}/I_{Z} would be a static resistance, and a meaningless one here.

**Limits:**

- **I_{Z(min)}:** the least current that keeps the zener in breakdown.
- **I_{Z(max)} = P_{Z}/V_{Z}:** the largest current before it overheats. A 0.5 W, 6.2 V zener allows I_{Z(max)} = 0.5/6.2 = 81 mA.

The series 1 kΩ resistor in the circuit limits the current.

## The circuit

[[fig:exp01_circuit|Fig 1.1, redrawn. The zener's cathode faces the + side, so it is reverse-biased. The ammeter is in series; the voltmeter (or DSO) is across the zener.|w=72]]

:::trap Trap: the manual's parts list
It lists a **1N4007**. That is an ordinary rectifier with a breakdown near 1000 V, so it will never break down on a 0–30 V supply. Ask for a **zener** (e.g. 6.2 V). A 1N4007 placed reverse-biased just shows µA leakage at every V_{S}.
:::

:::do Do it (hands-on, breadboard)
1. Supply **off**, voltage knob at 0, current limit low.
2. Wire the 1 kΩ from supply + to the ammeter. Ammeter (DMM on mA DC, red lead in the mA port) to the zener's **cathode** (the banded end). Zener's anode to supply −.
3. Put the voltmeter (DMM on DC V, or the DSO) across the zener.
4. Switch on. Raise V_{S} in **1 V steps from 0 to 15 V**, reading V_{Z} and I_{Z} at each step.
5. Plot I_{Z} (y) against V_{Z} (x). Mark the knee: that is V_{Z}.
6. Take two points well into breakdown, read ΔV_{Z} and ΔI_{Z}, and calculate r_{z}.
:::

## What you should see

Simulated with a 6.2 V zener (BZX84C6V2L, the part Exp 2 uses). A different zener shifts the knee to its own V_{Z}, but the shape is identical.

[[fig:exp01_plot|LTspice, 1 kΩ series, V_{S} 0–15 V. Flat (open) until about 6 V, then nearly vertical. The zoom shows the r_{z} triangle.|w=85]]

| V_{S} (V) | 0–5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V_{Z} (V) | = V_{S} | 5.957 | 6.185 | 6.245 | 6.279 | 6.303 | 6.322 | 6.337 | 6.350 | 6.362 | 6.372 |
| I_{Z} (mA) | ≈ 0 (µA) | 0.04 | 0.82 | 1.76 | 2.72 | 3.70 | 4.68 | 5.66 | 6.65 | 7.64 | 8.63 |

Below breakdown, the zener takes almost no current, so no voltage drops across the 1 kΩ and V_{Z} = V_{S}. In breakdown, V_{Z} is pinned and the rest of V_{S} drops across the resistor: I_{Z} = (V_{S} − V_{Z})/1 kΩ. Check: V_{S} = 15 gives (15 − 6.372)/1000 = 8.63 mA ✓.

## Calculation

Using the 10 V and 15 V rows (both well into breakdown):

$$r_{z} = \frac{6.372 − 6.303}{8.63 − 3.70 mA} = \frac{0.069 V}{4.93 mA} ≈ 14 Ω$$

The zoom figure uses 2 → 8 mA and gives 0.111 V / 6 mA = 18 Ω. r_{z} shrinks as the current grows, so always **state the current range used**.

:::write Write in your record
**Result:** breakdown voltage V_{Z} ≈ **6.2 V** (at I_{Z} ≈ 1 mA); dynamic resistance r_{z} ≈ **14 Ω** (between 3.7 and 8.6 mA). Use your own readings in the lab.

**Theory for the record:** a zener is a heavily doped pn diode designed to operate in reverse breakdown. Forward, it behaves like a normal diode (about 0.7 V). Reverse, only leakage flows until V_{Z}, where the current rises sharply while the voltage stays nearly constant. Breakdown is by tunnelling (below ~5 V) or avalanche (above ~6 V). Operation must stay between I_{Z(min)} and I_{Z(max)} = P_{Z}/V_{Z}. The slope ΔV_{Z}/ΔI_{Z} in breakdown is the dynamic resistance; a small value means good regulation, which Exp 2 uses.
:::

:::trap Trap: no series resistor
Without the 1 kΩ (or with it shorted), the current in breakdown is limited only by the supply, and the zener burns out. Never connect a zener directly across a supply.
:::

:::check Check 1
(a) At V_{S} = 12 V, a student reads V_{Z} = 6.34 V. Predict I_{Z} without the ammeter. (b) Why is r_{z} not simply V_{Z}/I_{Z}? (c) A 3.3 V zener and a 12 V zener: which mechanism does each use, and which way does each one's V_{Z} move when heated?
:::

<!--ANSWERS-->

## Answers

**Opening question.** Reverse current rises sharply at V_{Z} because the junction breaks down (tunnelling or avalanche), producing many carriers. Dynamic resistance = ΔV_{Z}/ΔI_{Z}, the slope in breakdown. It is small (≈ 14–18 Ω here).

**Check 1.** (a) I_{Z} = (12 − 6.34)/1 kΩ = **5.66 mA**. (b) r_{z} describes how V changes when I changes (the slope), which is what matters for regulation. V_{Z}/I_{Z} at one point is a large, current-dependent number with no use here. (c) 3.3 V: Zener (tunnelling) mechanism, V_{Z} falls with heat (negative coefficient). 12 V: avalanche, V_{Z} rises with heat (positive coefficient).

<!--/ANSWERS-->
