# Exp 12 · MOSFET inverter (resistive load)

<div class="sub">Manual pp. 34–35 · LTspice · CO4 · theory: ECE2101 unit 4 (MOSFETs) · links straight to the Digital Electronics lab (logic gates)</div>

[[map:9 JFET curves > 10 CS amplifier > 11 Oscillator > 12 MOSFET inverter|here=4]]

**What you already have:**

- From Exp 9, a FET's gate voltage controls its channel.
- From Exp 5, a transistor can be a switch: cut-off = open, saturation = closed.
- From digital electronics: NOT gate, logic 1 and logic 0.

**Three terms first:**

- **Enhancement nMOS:** a MOSFET whose gate is insulated by oxide (so it draws **no** gate current). It has **no** channel at V_{GS} = 0. A channel forms only when V_{GS} > **V_{TH}** (threshold voltage).
- **Inverter:** a NOT gate. Input high gives output low, and input low gives output high.
- **VTC (voltage transfer characteristic):** V_{out} plotted against V_{in}.

:::q <span class="tag">Manual Exp 12, aim</span>
Analyse an inverter circuit using a MOSFET. Viva form: "Explain the two states of the circuit, and mark V_{OH}, V_{OL}, V_{IL}, V_{IH} and V_{M} on the VTC."
:::

:::guess Guess first
When the input is 0 V, is the MOSFET on or off? What is the output then?
:::

## How it works

[[fig:exp12_circuit|Fig 12.1, redrawn: 1 kΩ from +5 V to the drain (output); input pulse on the gate; source to ground.|w=62]]

| Input | MOSFET | Current | Output |
|---|---|---|---|
| 0 V (logic 0), below V_{TH} | **off** (cut-off): no channel | I_{D} = 0, so no drop across the 1 kΩ | V_{out} = V_{DD} = **5 V (logic 1)** |
| 5 V (logic 1), above V_{TH} | **on**, fully (deep triode): the channel is a very low resistance (≈ 9 mΩ for this part) | I_{D} ≈ 5 V/1 kΩ = 5 mA | V_{out} ≈ 5 mA × 9 mΩ ≈ **0 V (logic 0)** |

**VTC terms:**

| Term | Meaning |
|---|---|
| V_{OH} / V_{OL} | output high / output low levels |
| V_{IL} | the highest input still read as 0. Where the VTC slope first reaches −1. |
| V_{IH} | the lowest input read as 1. Where the slope returns to −1. |
| V_{M} | switching threshold, where V_{out} = V_{in} |
| noise margins | NM_{L} = V_{IL} − V_{OL} and NM_{H} = V_{OH} − V_{IH}: how much noise an input can carry before the gate misreads it |

## Do it

:::do Do it (LTspice)
1. Draw Fig 12.1: M1: Pick New MOSFET → **FDR6580**; R1 = 1k; V1 = 5 V.
2. V2: **PULSE**: V1 = 0, V2 = 5, Tdelay = 0, Trise = 0, Tfall = 0, Ton = 1m, Tperiod = 2m, Ncycles = 10, which gives `PULSE(0 5 0 0 0 1m 2m 10)`.
3. Directive: `.tran 0 20m 0 1u`. The manual's bare `.tran 20m` works too, but its coarse steps show slanted edges and a false spike up to about 6.8 V.
4. Plot the input and output. Set the y-axis limits manually to −0.5 … 5.5 V. Read V_{min} and V_{max} of each.
5. **VTC (extra marks):** replace the pulse with a DC source, run `.dc V2 0 5 0.001`, and plot V(out) against V2.
:::

## What you should see

[[fig:exp12_tr|Transient: the output is the input upside-down: 5 V when the input is 0, about 0 V when the input is 5 V.|w=82]]

| Voltage | V_{min} | V_{max} |
|---|---|---|
| V_{in} | 0 V | 5 V |
| V_{out} | ≈ 0 V (0.04 mV) | 5.0 V |

[[fig:exp12_vtc|VTC from LTspice: a very sharp switch near 0.76 V (zoom inset).|w=80]]

| V_{OH} | V_{OL} | V_{IL} | V_{IH} | V_{M} | NM_{L} | NM_{H} |
|---|---|---|---|---|---|---|
| 5.00 V | ≈ 0 V | 0.53 V | 0.77 V | 0.76 V | 0.53 V | 4.23 V |

**Why it switches so low and so sharply:** the FDR6580 is a **power** MOSFET. It conducts amps from a tiny gate overdrive, so just past V_{TH} it already pulls the 5 mA that the 1 kΩ allows. The switch therefore happens right at V_{TH}, far below V_{DD}/2.

The manual's Fig 12.2 (with V_{IL} ≈ 0.9 V and V_{IH} ≈ 2.2 V) is a generic textbook VTC, not this part's.

:::trap Trap: V_{th} vs V_{M}
The manual says "V_{th} is the inverter threshold voltage, which is V_{dd}/2". These are two different quantities:

- **V_{TH}** is the MOSFET's own turn-on voltage.
- **V_{M}** is the inverter's switching point (where V_{out} = V_{in}).

V_{M} = V_{DD}/2 is the **design goal** of a symmetric CMOS inverter. In this resistor-load circuit, V_{M} ≈ 0.76 V.
:::

:::write Write in your record
**Result:** the output is inverted with respect to the input, with maximum voltage **5 V** as logic 1 and minimum voltage **≈ 0 V** as logic 0. (VTC: V_{IL} = 0.53 V, V_{IH} = 0.77 V, V_{M} = 0.76 V.)

**Theory for the record:** the inverter is the basic digital gate; NAND, NOR and larger logic are built from the same idea. In the resistive-load nMOS inverter, an enhancement nMOS pulls the output down and a resistor pulls it up to V_{DD}. For V_{in} < V_{TH} the MOSFET is cut off, no current flows, and V_{out} = V_{DD} (logic 1). For a high input the MOSFET conducts in the linear region and pulls the output close to 0 (logic 0). The VTC shows V_{OH}, V_{OL} and the transition region, with V_{IL} and V_{IH} at the unity-slope points and V_{M} where V_{out} = V_{in}. Noise margins are NM_{L} = V_{IL} − V_{OL} and NM_{H} = V_{OH} − V_{IH}. A drawback: current (and power) flows continuously when the output is low, which CMOS removes.
:::

:::check Check 1
(a) How much power does this inverter waste when its output is LOW? When HIGH? (b) Why does the MOSFET's gate draw no DC current? (c) What replaces the resistor in a CMOS inverter, and what does that fix?
:::

<!--ANSWERS-->

## Answers

**Opening question.** Input 0 V: the MOSFET is **off**, so no current flows and the output = **5 V**. Input 5 V: the MOSFET is **on** and the output ≈ 0 V. V_{OH} = 5 V, V_{OL} ≈ 0, V_{IL} = 0.53 V, V_{IH} = 0.77 V, V_{M} = 0.76 V.

**Check 1.** (a) LOW: 5 mA flows from the 5 V supply, so P = 5 V × 5 mA = **25 mW**, nearly all in the resistor. HIGH: no current, so ≈ 0 W. (b) The gate is insulated from the channel by a thin oxide layer: a capacitor, which passes no DC. (c) A **pMOS** transistor (pull-up). Only one transistor is on in each state, so no DC current flows from V_{DD} to ground. The static power becomes ≈ 0, and V_{OL} is exactly 0.

<!--/ANSWERS-->
