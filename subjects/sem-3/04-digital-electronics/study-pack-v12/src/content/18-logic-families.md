# 18 — Logic families

<div class="sub">Deck 14 (slides 4–25) · deck 05 slides 44–48 (tristate) · syllabus Unit 5 · needs 03 (NAND) and Electronic Devices 10 (the BJT as a switch)</div>

## Map

[[map:1 The yardsticks > 2 TTL NAND > 3 Tristate > 4 ECL and the comparison > 5 CMOS, interfacing|here=1]]

01–17 treated a gate as an ideal box. A real gate is a transistor circuit with real voltages, currents and delays. A **logic family** is a set of chips built on the same basic gate, so they share those numbers.

## The questions this file answers

- <span class="tag">Deck 14 slides 4–12</span> Define noise margin and fan-out; calculate both for standard TTL.
- <span class="tag">Deck 14 slides 24–25</span> Draw and explain a TTL NAND with totem-pole output; why must two totem-pole outputs not be joined?
- <span class="tag">Deck 05 slides 44–48</span> What is tristate logic and how is the third state made?
- <span class="tag">Deck 14 slide 14</span> Why is ECL fastest? Compare TTL, ECL and CMOS.
- <span class="tag">Deck 14 slides 19–22</span> CMOS inverter and NAND; why almost no static power; interfacing.

---

## Build

### 1 · The yardsticks: noise margin, fan-out, delay, power

:::q <span class="tag">Deck 14 slides 4–12</span>
Define noise margin and fan-out. For standard TTL (V_{OH(min)} = 2.4 V, V_{OL(max)} = 0.4 V, V_{IH(min)} = 2.0 V, V_{IL(max)} = 0.8 V; I_{OH} = 400 μA, I_{OL} = 16 mA, I_{IH} = 40 μA, I_{IL} = 1.6 mA) calculate both.
:::

:::guess Guess first
A gate promises its HIGH output is at least 2.4 V and accepts anything above 2.0 V as HIGH. Why the gap?
:::

:::note Terms
**V_{OH(min)}, V_{OL(max)}:** worst output levels guaranteed. **V_{IH(min)}, V_{IL(max)}:** input thresholds guaranteed. **I_{OH}, I_{OL}:** current an output supplies HIGH and sinks LOW. **I_{IH}, I_{IL}:** current one input takes.
:::

[[fig:noise_bands|Output and input voltage bands; the gaps are the noise margins.|w=60]]

$$NM_{H} = V_{OH(min)} − V_{IH(min)}      NM_{L} = V_{IL(max)} − V_{OL(max)}$$

[[fig:fanout_fig|Fan-out is limited by current in both states.|w=55]]

**Fan-out** = the smaller of I_{OL}/I_{IL} and I_{OH}/I_{IH}. **Fan-in** = number of inputs.

| Yardstick | Definition |
|---|---|
| Propagation delay t_{p} | input change to output change at 50% points; average of t_{PHL} and t_{PLH} |
| Rise, fall time | 10% → 90% and 90% → 10% of the swing |
| Power | V × average supply current; static + dynamic (grows with f) |
| Speed–power product | t_{p} × power: energy per switch, smaller is better |
| Integration | SSI &lt; 12 gates, MSI 12–99, LSI 100–9999, VLSI ≥ 10 000 |

**Answer.** NM_{H} = **0.4 V**, NM_{L} = **0.4 V**. Fan-out: 16/1.6 = 10 and 400/40 = 10: **10**. With t_{p} ≈ 10 ns and 10 mW, speed–power = 100 pJ.

:::check Check 1
(a) I_{OL} = 8 mA, I_{IL} = 0.4 mA, I_{OH} = 400 μA, I_{IH} = 20 μA: fan-out? (b) t_{PHL} = 8 ns, t_{PLH} = 12 ns: t_{p}?
:::

### 2 · The TTL NAND gate

:::q <span class="tag">Deck 14 slides 24–25</span>
Draw the circuit of a standard TTL NAND gate with totem-pole output and explain its operation. Why must two totem-pole outputs not be connected together?
:::

:::guess Guess first
The output stage has one transistor to pull up and one to pull down. What if both conduct at once?
:::

[[fig:ttl_nand|Standard TTL NAND: multi-emitter Q_{1}, phase splitter Q_{2}, totem pole Q_{3}–Q_{4}.|w=55]]

- **Q_{1}**, one emitter per input, does the AND.
- **Any input LOW:** Q_{1}'s base current leaves through that emitter, Q_{2} is OFF, Q_{4} OFF; Q_{3} gets base current and pulls the output **HIGH** through the diode.
- **All inputs HIGH:** Q_{1}'s base current flows through its collector into Q_{2}; Q_{2} ON drives Q_{4} into saturation: output **LOW**. The diode keeps Q_{3} OFF.
- **Totem pole:** active pull-up and pull-down: low output resistance both ways, fast.

A floating TTL input acts HIGH but picks up noise: tie unused inputs. Sub-families: 74, 74L, 74H, **74S** (Schottky clamp stops saturation: faster), **74LS** (the common one), 74AS, 74ALS.

**Answer.** Output = (AB)'. Join two totem poles with one HIGH and one LOW and Q_{3} of one and Q_{4} of the other short +5 V to ground: a large current, possible damage, invalid level. Shared lines use **open-collector** (no Q_{3}, external pull-up; joined outputs give wired-AND) or **tristate** outputs.

:::check Check 2
(a) Which transistors are ON when the output is LOW? (b) What does the "S" in 74LS do?
:::

### 3 · Tristate TTL

:::q <span class="tag">Deck 05 slides 44–48</span>
What is tristate logic? Explain how the third state is obtained in a TTL gate, and give one use.
:::

:::guess Guess first
How can an output be neither 0 nor 1?
:::

[[fig:tristate_bus|Tristate buffers sharing a bus.|w=60]]

The third state is **high impedance (Hi-Z)**: the output is disconnected, neither pulling up nor down. Many outputs can share a **bus** if only one is enabled. Circuit: the disable signal pulls an extra emitter of Q_{1} LOW (Q_{2}, Q_{4} OFF) and, through a diode, Q_{3}'s base LOW (Q_{3} OFF): both output transistors OFF.

| EN | IN | OUT |
|---|---|---|
| 0 | X | Hi-Z |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**Answer.** Three output states (0, 1, Hi-Z), made by turning both totem-pole transistors off; used on shared data buses. It keeps the fast active pull-up; but two enabled at once fight (bus contention), so enables are decoded.

:::check Check 3
Three tristate buffers drive one line. How many may be enabled at once, and what is the line's state if none is?
:::

### 4 · ECL and the family comparison

:::q <span class="tag">Deck 14 slide 14</span>
Why is ECL the fastest logic family? Compare TTL, ECL and CMOS.
:::

:::guess Guess first
A saturated transistor holds extra charge. What must happen to it before the transistor can switch off?
:::

[[fig:ecl_gate|ECL gate: a differential current switch.|w=55]]

R_{E} sets a nearly constant current, steered to whichever of Q_{1} (input) or Q_{2} (reference V_{BB}) has the higher base. Never switched off, **never saturated**, small swing: about **1 ns**. Costs: highest power (current always flows), small noise margin (1 ≈ −0.8 V, 0 ≈ −1.7 V), negative supply (−5.2 V). Gives **OR and NOR** outputs.

| | TTL (74, 74LS) | ECL | CMOS (74HC) |
|---|---|---|---|
| Device | BJT, saturating | BJT, non-saturating | n and p MOSFETs |
| Delay | ≈ 10 ns | ≈ 1 ns | ≈ 10 ns |
| Static power/gate | 10 mW (LS 2 mW) | highest | ≈ 0 |
| Noise margin | 0.4 V | ≈ 0.15 V | ≈ 30% of V_{DD} |
| Fan-out | 10 | 25 | 50+ |
| Supply | +5 V | −5.2 V | 2–6 V (4000: 3–15 V) |
| Basic gate | NAND | OR/NOR | inverter, NAND, NOR |

**Answer.** No saturation means no storage delay, and the swing is small. The table compares the three (typical textbook values).

:::check Check 4
(a) Which family for a battery-powered device, and why? (b) ECL: V_{OH(min)} = −0.98 V, V_{IH(min)} = −1.105 V. NM_{H}?
:::

### 5 · CMOS gates and interfacing

:::q <span class="tag">Deck 14 slides 19–22</span>
Draw a CMOS inverter and a 2-input CMOS NAND and explain them. Why does CMOS use almost no static power?
:::

:::guess Guess first
Is there any steady input for which both inverter transistors are ON?
:::

<div class="two">

[[fig:cmos_inv|CMOS inverter (Wikimedia Commons, public domain).]]

[[fig:cmos_nand|CMOS NAND (Wikimedia Commons, CC BY-SA 3.0).]]

</div>

**Inverter:** input LOW → pMOS ON, output V_{DD}; HIGH → nMOS ON, output 0. **NAND:** two nMOS in series to ground, two pMOS in parallel to V_{DD}; NOR is the reverse; n inputs, 2n transistors.

- Static power ≈ 0; **dynamic P = CV_{DD}^{2}f**. Full swing, large noise margin; input is a capacitor, so huge fan-out; wide supply range; dense.
- Weak points: static-sensitive oxide; slower with large loads. Never leave an input floating.

| Driving | Problem | Fix |
|---|---|---|
| TTL → CMOS (5 V) | TTL HIGH may be 2.4 V; 74HC needs ≈ 3.5 V | pull-up resistor, or 74HCT |
| CMOS → TTL | CMOS must sink I_{IL} = 1.6 mA per TTL input | CMOS buffer (4049, 4050), or LS TTL |
| Different supplies | levels differ | level shifter, or open collector with pull-up |

**Answer.** In either steady state one network is OFF, so there is no path from V_{DD} to ground: power is used only while switching.

:::check Check 5
(a) Clock doubled and V_{DD} halved: factor on dynamic power? (b) Transistors in a 3-input CMOS NAND?
:::

---

## Exam form

**Yardsticks.** Definitions; NM and fan-out formulas with a worked number; t_{p}, speed–power.

**TTL.** Circuit, operation for both input cases, totem pole, why outputs can't be joined, open collector, sub-families.

**Tristate.** Hi-Z, how made, bus use, contention.

**ECL.** Current switch, why fast, costs; the TTL/ECL/CMOS table.

**CMOS.** Inverter and NAND circuits and tables; P = CV^{2}f; interfacing table.

## Traps

- Fan-out from one state only: take the smaller of the two.
- NM_{L} = V_{IL} − V_{OL}, not V_{OL} − V_{IL}.
- Saying CMOS uses no power: dynamic power grows with f.
- Floating TTL input = HIGH; floating CMOS input = undefined.

## Self-test

1. V_{OH} = 4.9 V, V_{IH} = 3.5 V, V_{IL} = 1.5 V, V_{OL} = 0.1 V: noise margins?
2. I_{OL} = 4 mA, I_{IL} = 0.1 mA, I_{OH} = 0.4 mA, I_{IH} = 20 μA: fan-out?
3. t_{p} = 5 ns, 2 mW per gate: speed–power product?
4. CMOS gate with C = 20 pF, V_{DD} = 5 V, f = 10 MHz: dynamic power?
5. Open-collector vs totem-pole output: one advantage each.
6. How do you drive a 74HC input from a TTL output?

<!--ANSWERS-->

## Answers

**Check 1.** (a) 8/0.4 = 20, 400/20 = 20: **20**. (b) **10 ns**.

**Check 2.** (a) **Q_{2} and Q_{4}** (Q_{3} OFF). (b) A Schottky diode keeps the transistor out of saturation: no storage delay, **faster**.

**Check 3.** **One**. None enabled: **Hi-Z**, the line floats (a pull-up is normally added).

**Check 4.** (a) **CMOS**: almost zero static power. (b) −0.98 + 1.105 = **0.125 V**.

**Check 5.** (a) (½)^{2} × 2 = **½**. (b) **6**: three pMOS in parallel, three nMOS in series.

**Self-test.**

1. NM_{H} = **1.4 V**, NM_{L} = **1.4 V**.
2. 40 and 20: **20**.
3. **10 pJ**.
4. 20 pF × 25 × 10^{7} = **5 mW**.
5. Open collector: outputs can be joined (wired-AND) and pulled to another supply. Totem pole: fast active pull-up, low output resistance.
6. A pull-up resistor from the TTL output to +5 V, or use a 74HCT part.

<!--/ANSWERS-->
