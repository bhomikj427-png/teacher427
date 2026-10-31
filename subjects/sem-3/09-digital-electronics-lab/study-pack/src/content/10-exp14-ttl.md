# Exp 14 · TTL NAND and NOR gates (inside the chip)

<div class="sub">In the experiment list, but the manual gives no pages for it · the circuit below is the standard 7400-type TTL NAND, simulated in LTspice (src/sim/ttl.py) with discrete transistors · theory: ECE2102 logic families</div>

[[map:12 Shift registers > 13 FSM > 14 TTL|here=3]]

:::q <span class="tag">Experiment list, item 14</span>
Implement TTL logic for a NAND and a NOR gate. Viva form: "What does Q1's multi-emitter do, why is the output stage called a totem pole, and what is TTL's noise margin?"
:::

:::guess Guess first
If any input is LOW, which way does Q1's base current go?
:::

## The TTL NAND

[[fig:ttl_nand_circuit|Standard TTL NAND: multi-emitter input (Q1), phase splitter (Q2), totem-pole output (Q4 on top, Q3 below). Build Q1 as two transistors with shared base and shared collector.|w=78]]

| Inputs | What happens | Output |
|---|---|---|
| **any input LOW** | Q1's base current flows out through that emitter, so Q1 pulls Q2's base low. Q2 and Q3 are off; Q4 (via R2) and D conduct. | **HIGH** ≈ 5 − V_{BE4} − V_{D} ≈ 3.6 V when loaded (≈ 4 V lightly loaded) |
| **all inputs HIGH** | Q1's emitters are reverse-biased. R1's current flows through Q1's base–collector junction into Q2's base: Q2 and Q3 saturate. D keeps Q4 off. | **LOW** ≈ V_{CE(sat)} ≈ 0.2 V |

**Totem pole:** Q4 actively pulls the output up and Q3 actively pulls it down, stacked one above the other. That gives fast switching both ways. The 130 Ω resistor and the diode stop both transistors conducting hard at once.

**TTL NOR:** each input gets its own Q1 + Q2 pair. The two Q2s sit **in parallel** (shared collector and emitter), so **any** HIGH input turns Q3 on and pulls the output LOW. The totem pole is the same.

## Results (LTspice, 2N2222 transistors, 1N4148 diode, 100 kΩ load)

| A B | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| NAND V_{Y} | 3.99 V | 3.99 V | 3.99 V | **0.01 V** |
| NOR V_{Y} | **3.99 V** | 0.01 V | 0.01 V | 0.01 V |

[[fig:ttl_vtc|Transfer characteristic: the output switches near 1.37 V (NAND) / 1.39 V (NOR), inside TTL's undefined band of 0.8–2.0 V.|w=78]]

**Standard TTL levels (74 series):**

| Parameter | Value |
|---|---|
| V_{IL(max)} | 0.8 V |
| V_{IH(min)} | 2.0 V |
| V_{OL(max)} | 0.4 V |
| V_{OH(min)} | 2.4 V |
| noise margins | NM_{L} = 0.8 − 0.4 = **0.4 V**; NM_{H} = 2.4 − 2.0 = **0.4 V** |
| fan-out | 10 |
| propagation delay | ≈ 10 ns per gate |

:::do Do it
**LTspice** (if done as simulation):

1. Draw the circuit with two NPNs for Q1 (bases tied, collectors tied, one emitter per input). Q2–Q4 = 2N2222; D = 1N4148. VCC = 5 V.
2. Inputs are DC sources of 0 or 5 V. Run `.op` for each of the four input pairs.
3. For the VTC, hold B high (NAND) or low (NOR) and run `.dc VA 0 5 0.01`.

**Breadboard:** the same circuit with BC547s and a 5 V supply. Inputs to 0 V / 5 V through the switches; output to an LED through about 330 Ω, or to the DMM.
:::

:::write Write in your record
**Result:** the TTL NAND gave a HIGH output (≈ 4 V) for any LOW input and a LOW output (≈ 0 V) only when both inputs were HIGH. The TTL NOR gave a HIGH output only for 00. Both switched at ≈ 1.4 V.

**Theory for the record:** transistor-transistor logic uses a multi-emitter input transistor that performs the AND function. A phase-splitter transistor drives a totem-pole output: an active pull-up transistor with a diode, and an active pull-down transistor. Any LOW input diverts Q1's base current, turning off the phase splitter and the pull-down, so the output is HIGH. With all inputs HIGH, current flows through Q1's base–collector junction into the phase splitter, saturating the pull-down, so the output is LOW. A NOR uses parallel phase splitters. TTL works from 5 V, with V_{IL} ≤ 0.8 V, V_{IH} ≥ 2.0 V, noise margin 0.4 V and fan-out 10. A floating input behaves as HIGH.
:::

:::check Check 1
(a) Why does a floating TTL input act as HIGH? (b) What would happen without the diode D? (c) Why can't two totem-pole outputs be wired together?
:::

<!--ANSWERS-->

## Answers

**Opening question.** A LOW input lets Q1's base current flow **out through that emitter** into the input source, which starves Q2. The output stage is a totem pole because Q4 and Q3 are stacked between VCC and ground. The noise margin is **0.4 V** each way.

**Check 1.** (a) With nothing pulling the emitter down, Q1's base–emitter junction has no path, just as if the input were HIGH. R1's current goes to Q2. (b) With the output LOW, Q4's base (Q2's collector at about 0.9 V) could still forward-bias Q4. Both Q4 and Q3 would conduct, wasting current and raising V_{OL}. D adds the extra voltage drop that keeps Q4 off. (c) If one output is HIGH and the other LOW, Q4 of one and Q3 of the other form a low-resistance path from VCC to ground. A large current flows and can damage them. Use open-collector gates for wired logic.

<!--/ANSWERS-->
