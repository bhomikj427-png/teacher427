# 18 — Logic families

<div class="sub">Deck 14 (slides 4–25) · deck 05 slides 44–48 (tristate) · syllabus Unit 5 (TTL NAND specifications, noise margin, propagation delay, fan-in and fan-out; tristate TTL; ECL; CMOS and interfacing) · no worked questions in the decks (Predict prompts throughout) · needs 03 step 1 (NAND), 14 step 1 (clock-to-Q delay) and the switch idea of a transistor (on = closed, off = open)</div>

## Map

[[map:1 Propagation delay > 2 Rise and fall time > 3 Power > 4 Noise margin > 5 Speed–power product > 6 Fan-out > 7 CMOS inverter > 8 CMOS NAND and NOR > 9 TTL NAND > 10 Totem pole, open collector > 11 Tristate > 12 ECL > 13 Families compared > 14 Interfacing|here=1]]

Files 01–17 treated a gate as a perfect box: the output is the function of the inputs, at once, at exactly 0 or 1. A real gate is a transistor circuit. Its output takes nanoseconds to change, sits at some voltage near 0 or near the supply, draws current and gives off heat. A **logic family** is a set of chips built round the same basic gate circuit, so they share these numbers (deck 14 slide 4). This file first learns to read the numbers (steps 1–6), then looks inside the gates that produce them (7–12), and ends by comparing and connecting families (13–14). File 19 builds memories and programmable logic out of the same gates.

## Symbols

| Symbol | What it means in this file | Typical value (7400) |
|---|---|---|
| V_{CC}, V_{DD} | supply voltage (TTL: V_{CC}; CMOS: V_{DD}) | 5 V |
| V_{OH(min)} | lowest voltage a HIGH output is guaranteed to give | 2.4 V |
| V_{OL(max)} | highest voltage a LOW output is guaranteed to give | 0.4 V |
| V_{IH(min)} | lowest input voltage guaranteed to be read as 1 | 2.0 V |
| V_{IL(max)} | highest input voltage guaranteed to be read as 0 | 0.8 V |
| I_{OH}, I_{OL} | most current a HIGH output can source, a LOW output can sink, while keeping its level | 0.4 mA, 16 mA |
| I_{IH}, I_{IL} | current one input draws when HIGH, gives out when LOW | 40 µA, 1.6 mA |
| t_{PLH}, t_{PHL} | delay from input change to output change, output going LOW→HIGH and HIGH→LOW | 11 ns, 7 ns |
| t_{r}, t_{f} | time an edge takes from 10 % to 90 % of its swing (rise) and back (fall) | a few ns |
| NM_{H}, NM_{L} | noise margins: how much noise a HIGH and a LOW can take and still be read right | 0.4 V, 0.4 V |
| P | power one gate takes from the supply | 10 mW |
| C, f | capacitance charged at each switch; switching frequency | 20 pF; 1 MHz |

## Running example

**One gate of a 7400**, the standard-TTL quad 2-input NAND, with the numbers from TI's SN7400 data sheet (typical delays, guaranteed levels and currents). Steps 1–6 read every yardstick off it; step 9 opens it up; steps 13–14 set it beside the CMOS 74HC00 (TI SN74HC00 data sheet).

## The questions this file answers

The decks hold no worked questions for this file: deck 14 is definitions and circuits. Each step opens on a **Predict** prompt instead. The syllabus asks for exactly these items: TTL NAND specifications, noise margin, propagation delay, fan-in and fan-out, tristate TTL, ECL, CMOS and interfacing.

---

## Build

### 1 · Propagation delay: t_{PLH} and t_{PHL}

A gate's truth table says *what* the output becomes. A real gate also takes time to get there, and file 14's speed limits were built from exactly this time.

:::guess Predict
A 7400 NAND is used as an inverter (both inputs joined). Its input rises through the half-way voltage at 10 ns and falls through it at 40 ns. The output falls through half-way at 17 ns and rises through it at 51 ns. Which delay is longer, the one for the output going down or going up, and by how much?
:::

:::note Terms
**t_{PHL}:** the time from the input crossing half-way to the output crossing half-way, when the output goes **H**igh → **L**ow. **t_{PLH}:** the same, when the output goes **L**ow → **H**igh. Each is set by how fast the gate's transistors can move charge on and off the output; the two differ because different transistors do the pulling up and the pulling down.
:::

[[fig:u5_tpd|What this graph plots: time across (ns), one row per signal (input IN, output OUT of an inverting gate), voltage up. The dotted line in each row is the 50 % level; each delay is measured between two 50 % crossings.|w=70]]

Deck 14 slide 5: both delays are measured **between the 50 % points** of the input and output edges. Measuring at the middle of each edge means the slope of the edge does not change the answer much.

| Edge pair (figure) | Input 50 % | Output 50 % | Delay |
|---|---|---|---|
| input rises, output falls | 10 ns | 17 ns | t_{PHL} = 7 ns |
| input falls, output rises | 40 ns | 51 ns | t_{PLH} = 11 ns |

These are the SN7400's typical values (data sheet: t_{PLH} 11 ns typ, 22 ns max; t_{PHL} 7 ns typ, 15 ns max, with a 400 Ω, 15 pF load). TI measures standard TTL at 1.5 V rather than at 50 %; 1.5 V is close to the point where a TTL input switches. CMOS data sheets (74HC00) use 50 % of V_{CC}, as the deck does.

One number for "the delay": TI's 74HC00 data sheet takes **t_{pd} = the larger of t_{PLH} and t_{PHL}**, because a signal path has to wait for whichever edge is slower. That is the value file 14's timing sums need. For the 7400: t_{pd} = 11 ns.

**Answer to the Predict.** t_{PHL} = 17 − 10 = **7 ns**; t_{PLH} = 51 − 40 = **11 ns**. The output going up is slower by **4 ns**, so the gate's t_{pd} = 11 ns.

:::check Check 1
(a) An input crosses 50 % at 3 ns and the inverted output crosses 50 % at 8 ns while rising. Which delay is this, and how long? (b) A gate has t_{PHL} = 8 ns and t_{PLH} = 12 ns. What t_{pd} goes into a timing check?
:::

### 2 · Rise and fall time: 10 % to 90 %

Step 1 timed the gap *between* two edges. An edge itself is not vertical either; how long it takes matters when the next gate must see a clean change.

:::guess Predict
An edge goes from 0 V to 5 V. You want one number for "how long it took". Why not measure from the moment it leaves 0 V to the moment it reaches 5 V?
:::

:::note Terms
**Rise time t_{r}:** the time the signal takes to go from **10 % to 90 %** of its swing, low to high. **Fall time t_{f}:** from 90 % down to 10 %. Both are set by how much capacitance the output drives and how much current it can push.
:::

[[fig:u5_rise_fall|What this graph plots: voltage (V) up, time (ns) across, for one pulse with sloped edges. The dashed lines are 10 % and 90 % of the 5 V swing; t_r and t_f are read between the dots where the edges cross them.|w=62]]

Deck 14 slide 6 defines t_{r} and t_{f} this way, and TI's 74HC00 data sheet draws them the same way (its Figure 7-3). For a 0 → 5 V swing, 10 % is 0.5 V and 90 % is 4.5 V.

| Point read on the figure | Time |
|---|---|
| rising edge crosses 0.5 V | 10.5 ns |
| rising edge crosses 4.5 V | 14.5 ns |
| falling edge crosses 4.5 V | 40.75 ns |
| falling edge crosses 0.5 V | 46.75 ns |

So t_{r} = 14.5 − 10.5 = 4 ns and t_{f} = 46.75 − 40.75 = 6 ns.

**Answer to the Predict.** A real edge creeps away from 0 V and creeps up to 5 V, so the exact "start" and "end" are hard to see. Between 10 % and 90 % the edge is moving fast and its crossing times are sharp; that is why the definition cuts off the two ends.

:::check Check 2
(a) A 0 → 3 V edge crosses 0.3 V at 2 ns and 2.7 V at 5 ns. What is t_{r}? (b) Which is measured at the 50 % points, t_{r} or t_{PLH}?
:::

### 3 · Power: static and dynamic

Steps 1–2 measured speed. The supply pays for every gate, all the time; a chip of thousands of gates is limited by the heat.

:::guess Predict
A 7400 package (four gates) draws 4 mA from 5 V when all outputs are HIGH and 12 mA when all are LOW. Its outputs spend half the time in each state. How much power does one gate take?
:::

:::note Terms
**Static power:** power drawn while the inputs sit still: current flowing through resistors and on transistors (deck 14 slide 7: "I²R losses ... no input signal"). **Dynamic power:** power drawn only when the output switches: each switch charges or discharges the capacitance C on the output through a resistance. It grows with the switching rate f.
:::

Static power is supply voltage × average supply current. The SN7400 data sheet gives, per package of four gates, I_{CCH} = 4 mA (outputs HIGH) and I_{CCL} = 12 mA (outputs LOW), typical.

1. Average current, assuming a 50 % duty cycle (the approximation enters here): (4 + 12)/2 = 8 mA.
2. Package power: 5 V × 8 mA = 40 mW.
3. Per gate: 40/4 = **10 mW**.

Dynamic power: each full cycle charges C to V and empties it again, which costs C·V² of energy; at f cycles per second,

$$P_{dyn} = C V^{2} f$$

Read it: *capacitance charged × supply squared × switches per second*. Doubling V quadruples the power. For one 74HC00 CMOS gate the data sheet's "power dissipation capacitance" is C = 20 pF; at 5 V and 1 MHz: 20 pF × 25 V² × 10⁶ /s = 0.5 mW. Its static current is at most 2 µA for the whole package (25 °C), so almost all CMOS power is dynamic (step 7 shows why).

**Answer to the Predict.** 5 V × 8 mA = 40 mW per package, **10 mW per gate**, drawn even when nothing switches.

:::check Check 3
(a) A CMOS gate with C = 20 pF runs at 5 V and 10 MHz. P_{dyn}? (b) The same gate's clock is doubled and its supply halved. By what factor does P_{dyn} change?
:::

### 4 · Noise margin

Step 3 counted current; now the voltages. A wire picks up noise, so the voltage that arrives is not the voltage that was sent.

:::guess Predict
A 7400 output is LOW, guaranteed at most 0.4 V. A 7400 input reads anything up to 0.8 V as LOW. Noise adds a 0.5 V spike to the wire. Is the bit still safe?
:::

:::note Terms
**Noise margin:** how far a guaranteed output level is from the input threshold it must clear. It counts the volts of noise a signal can pick up and still be read right. Set by the family's guaranteed levels.
:::

[[fig:u5_noise_ttl|What this graph plots: voltage (V) up. Left bar: the bands a standard-TTL output is guaranteed to stay in. Right bar: the bands a TTL input is guaranteed to read. The two gaps between the bars are the noise margins.|w=60]]

Deck 14 slide 8:

$$NM_{H} = V_{OH(min)} - V_{IH(min)}    NM_{L} = V_{IL(max)} - V_{OL(max)}$$

Read them: *the worst HIGH sent, minus the least HIGH accepted*; *the most LOW accepted, minus the worst LOW sent*. Both are differences of **guaranteed** numbers, so the margin holds for every chip of the family. With the SN7400's guaranteed levels: NM_{H} = 2.4 − 2.0 = **0.4 V** and NM_{L} = 0.8 − 0.4 = **0.4 V**. A family's noise margin is the smaller of the two.

:::note Slide slips
Deck 14 slide 21 gives TTL a "typical noise immunity about 1–1.6 V". That uses *typical* output levels (the SN7400's typical V_{OH} is 3.4 V, V_{OL} 0.2 V), not the guaranteed ones; the slide's range itself is not checked in a data sheet here. Exam answers use the guaranteed 0.4 V.
:::

**Answer to the Predict.** 0.4 + 0.5 = 0.9 V, above V_{IL(max)} = 0.8 V: the bit is **not** safe. Any spike over NM_{L} = 0.4 V can be misread.

:::check Check 4
(a) A CMOS 74HC00 at V_{CC} = 4.5 V: V_{OH(min)} = 4.4 V, V_{IH(min)} = 3.15 V, V_{IL(max)} = 1.35 V, V_{OL(max)} = 0.1 V. Find NM_{H} and NM_{L}. (b) What fraction of the 4.5 V supply is that?
:::

### 5 · Speed–power product

Steps 1 and 3 gave two numbers, delay and power, and a family can buy one with the other. One figure of merit puts them together.

:::guess Predict
Gate X: 11 ns, 10 mW. Gate Y: 9 ns, 0.5 mW. Which is better, and by what one number would you compare them?
:::

:::note Terms
**Speed–power product (power–delay product, PDP):** t_{pd} × P. Delay in seconds times power in joules per second gives joules: the **energy one switching event costs**. Smaller is better (deck 14 slide 9).
:::

$$PDP = t_{pd} × P$$

Read it: *how long one switch takes × how fast energy is used* = *energy per switch*. Within one technology, a faster gate usually costs more power, so the product stays roughly constant (UMBC CMPE 315 notes); a better technology lowers the product itself.

1. 7400: 11 ns × 10 mW = 110 × 10⁻¹² J = **110 pJ**.
2. 74HC00 at 1 MHz: about 9 ns (typical, 4.5 V) × 0.5 mW (5 V) ≈ **4.5 pJ** (approximation: the two figures are read at slightly different supplies).

For CMOS the product depends on how fast the gate is clocked, because its power is dynamic (step 3).

**Answer to the Predict.** Compare **t_{pd} × P**: X costs 110 pJ per switch, Y about 4.5 pJ. **Y is better** on both counts, by a factor of about 24 in energy.

:::check Check 5
(a) A gate has t_{pd} = 5 ns and P = 2 mW. PDP? (b) A gate twice as fast at four times the power: does its PDP go up or down, and by what factor?
:::

### 6 · Fan-out (and fan-in)

Steps 4 and 5 judged one gate on its own. In a circuit one output drives several inputs, and each input draws current from it.

:::guess Predict
A 7400 output can sink 16 mA when LOW and source 0.4 mA when HIGH. Each 7400 input pushes out 1.6 mA when LOW and draws 40 µA when HIGH. How many inputs can one output drive?
:::

:::note Terms
**Fan-out:** the largest number of inputs of the same family one output can drive while still holding its guaranteed levels. Set by the output's current limits divided by one input's current. **Fan-in:** the number of inputs a gate has (deck 14 slide 10: a NAND with 8 inputs has fan-in 8); it is fixed when the chip is made, not an electrical limit.
:::

[[fig:u5_fanout|One driver feeding N loads in each output state. Left: output LOW, every load input pushes I_IL into the driver, which must sink them all. Right: output HIGH, the driver must source I_IH to every load.|w=72]]

Deck 14 slide 12:

$$fan-out = min(\frac{I_{OL}}{I_{IL}}, \frac{I_{OH}}{I_{IH}})$$

Read it: *how many inputs' worth of current the output can take in the LOW state, and in the HIGH state; the smaller one wins*, because the output must work in both.

1. LOW: 16 mA / 1.6 mA = 10.
2. HIGH: 0.4 mA / 40 µA = 10.
3. Fan-out = min(10, 10) = **10**.

Past the fan-out a LOW output sinks too much current and rises above V_{OL(max)} = 0.4 V, eating the noise margin of step 4.

**Answer to the Predict.** **10** inputs; here both states give 10.

:::check Check 6
(a) A gate has I_{OL} = 8 mA, I_{IL} = 0.4 mA, I_{OH} = 0.4 mA, I_{IH} = 20 µA. Fan-out? (b) What is the fan-in of a 3-input NAND, and why is fan-in not computed from currents?
:::

### 7 · The CMOS inverter: why static power is almost zero

Steps 1–6 measured gates from the outside. Step 3's puzzle was why a CMOS gate draws almost no current when it sits still; the answer is inside.

:::guess Predict
A CMOS inverter is one switch from V_{DD} to the output and one switch from the output to 0 V; the input drives both. For a steady input of 0 or 1, can there ever be a path from V_{DD} straight to 0 V?
:::

:::note Terms
**pMOS transistor:** a switch that is closed (on) when its gate is LOW. **nMOS transistor:** closed when its gate is HIGH. **Complementary:** one pMOS network pulling up and one nMOS network pulling down, built so exactly one of them is on for every input.
:::

[[fig:u5_cmos_sw|The CMOS inverter drawn as two switches (deck 14 slide 22b). Left, A = 0: the pMOS is on, the nMOS off, X = V_DD. Right, A = 1: the reverse, X = 0 V.|w=62]]

[[fig:cmos_inv|The CMOS inverter at transistor level (deck 14 slide 22a): pMOS from V_DD to the output, nMOS from the output to ground, gates joined (Wikimedia Commons, public domain).|w=30]]

| A | pMOS | nMOS | X |
|---|---|---|---|
| 0 | on | off | V_{DD} (1) |
| 1 | off | on | 0 V (0) |

In each row one switch is open, so no current flows from V_{DD} to 0 V; the only static current is leakage (74HC00: at most 2 µA for four gates at 25 °C). The output reaches the rail itself, V_{DD} or 0 V ("full swing", deck 14 slide 19). Current flows only while the output switches: to charge or empty the load capacitance (step 3), plus a brief moment mid-edge when both transistors conduct.

**Answer to the Predict.** **No.** For A = 0 the nMOS is open; for A = 1 the pMOS is open. A path exists only during a transition.

:::check Check 7
(a) Which transistor connects the output to V_{DD} when A = 0? (b) Why must an unused CMOS input never be left unconnected? (Hint: what if it floats near V_{DD}/2?)
:::

### 8 · CMOS NAND and NOR: series and parallel switches

Step 7 built NOT from one pull-up and one pull-down switch. Two inputs need two switches in each network; how they are joined decides the function.

:::guess Predict
You want X = 0 only when A = 1 **and** B = 1. Should the two nMOS switches (on when their input is 1) be in series or in parallel between X and 0 V?
:::

:::note Terms
**Series:** switches one after another; the path conducts only if **all** are on (AND). **Parallel:** switches side by side; the path conducts if **any** is on (OR).
:::

[[fig:u5_cmos_nand_nor|Switch-level CMOS gates (deck 14 slide 23). (a) NAND: pMOS A and B in parallel to V_DD, nMOS A and B in series to 0 V. (b) NOR: pMOS in series, nMOS in parallel.|w=66]]

| Gate | pull-down (nMOS) | pull-up (pMOS) | X = 0 when |
|---|---|---|---|
| NAND | A, B in series | A, B in parallel | A = 1 and B = 1 |
| NOR | A, B in parallel | A, B in series | A = 1 or B = 1 |

The pull-up is always the **dual** of the pull-down: series ↔ parallel. That keeps the rule of step 7: for every input, exactly one network conducts. A CMOS gate with n inputs uses n pMOS + n nMOS = **2n transistors**.

Check NAND, A = 1, B = 0: nMOS B is off, so the series path is broken; pMOS B is on, so X = V_{DD}: output **1** = (1·0)'. ✓

**Answer to the Predict.** **In series**: the path to 0 V conducts only when both are on. Then the pMOS pair must be in parallel, so X is pulled up whenever A or B is 0. That is NAND.

:::check Check 8
(a) How many transistors does a 3-input CMOS NOR use, and how are its nMOS joined? (b) In the NOR of the figure, A = 0, B = 0: which switches are on, and what is X?
:::

### 9 · The TTL NAND gate: the multi-emitter input

Steps 7–8 were CMOS, built from MOSFETs. TTL is built from bipolar transistors (deck 14 slide 18), and the 7400 of the running example does its AND inside one transistor.

:::guess Predict
In deck 14 slide 25, inputs A and B are two emitters of one transistor Q₁, whose base is pulled up through a resistor R to V_{CC}. If A is held at 0 V, where does the current from R go: into the next transistor, or out through A?
:::

:::note Terms
**Multi-emitter transistor:** one BJT with several emitters sharing one base and collector (deck 14 slide 25b); each emitter is one gate input. **Saturated:** a BJT switched fully on, collector close to its emitter voltage, like a closed switch.
:::

[[fig:ttl_nand|A standard TTL NAND gate: multi-emitter input transistor, a phase-splitter transistor, and a two-transistor (totem-pole) output stage.|w=55]]

Deck 14 slide 25 draws the simplest version: Q₁ (multi-emitter) drives one output transistor whose collector goes through R_{C} to V_{CC} and is the output X.

| Inputs | Current from R | Output transistor | X |
|---|---|---|---|
| any input LOW | flows out of Q₁ through that emitter | off (no base current) | HIGH, pulled up through R_{C} |
| all inputs HIGH | no emitter can take it; it flows out of Q₁'s collector into the next base | on, saturated | LOW, near 0 V |

The current takes the easiest way out: one LOW emitter is enough to steal it. So the output is LOW only when every input is HIGH: **X = (AB)'**. The input side is an AND (all emitters must be HIGH), the output transistor inverts it.

**Answer to the Predict.** **Out through A**: a LOW emitter gives the current an easy path to 0 V, so the output transistor gets none and switches off; X is HIGH.

:::check Check 9
(a) For A = 1, B = 1, is the output transistor on or off, and what is X? (b) Why does a TTL input that is left open act like a HIGH? (Which way can the base current go?)
:::

### 10 · Totem-pole and open-collector outputs

Step 9's output pulls up through a resistor, which is slow to charge a load. The 7400 replaces the resistor with a second transistor; that speeds it up but forbids one thing.

:::guess Predict
Two 7400 outputs are wired together. Gate 1 drives HIGH (its upper transistor on), gate 2 drives LOW (its lower transistor on). What flows, and what voltage does the shared wire show?
:::

:::note Terms
**Totem-pole output:** an upper transistor that pulls the output to V_{CC} stacked on a lower one that pulls it to 0 V; one of them is on. Both directions are driven actively, so edges are fast. **Open-collector output:** the upper transistor removed; the output can only pull LOW, and an external **pull-up resistor** supplies the HIGH. **Wired-AND:** open-collector outputs joined on one pulled-up wire: the wire is HIGH only if no output pulls it LOW.
:::

[[fig:u5_totem_oc|(a) Two totem-pole outputs joined, one HIGH and one LOW: a low-resistance path from +5 V to ground through both gates. (b) Open-collector outputs share one pull-up resistor; any gate turning on pulls Y low.|w=72]]

The SN7400 has totem-pole outputs (its data sheet tests them as "2-state totem-pole outputs"). Joined outputs at opposite levels make the path in figure (a): a large current through two on-transistors, a wire voltage that is neither a valid 0 nor a valid 1, and possible damage. Open-collector parts (figure b) can be joined: each can only pull down, so the shared line Y obeys

$$Y = Y_{1} · Y_{2}$$

*Y is 1 only if every output lets go* (AND, done by the wire). The price: the pull-up resistor charges the line slowly, so open-collector edges are slower than totem-pole ones.

**Answer to the Predict.** A large current flows from +5 V through gate 1's upper transistor and gate 2's lower transistor to ground; the wire sits at an **undefined** level between the bands of step 4, and the chips can be damaged. Totem-pole outputs are never joined.

:::check Check 10
(a) Three open-collector outputs on one pulled-up line give 1, 0, 1. What is the line? (b) Give one advantage of the totem-pole output and one of the open-collector output.
:::

### 11 · Tristate outputs and the bus

Step 10 left a problem: open collector shares a wire but is slow; totem pole is fast but cannot share. A third output state solves both.

:::q <span class="tag">Deck 05 slide 48</span>
The 3-state buffer: if EN = 0 then OUT = Hi-Z regardless of IN; if EN = 1 then OUT = IN. Complete its truth table.
:::

:::guess Guess first
What could an output be that is neither 0 nor 1, and why would that let several outputs share one wire?
:::

:::note Terms
**High impedance (Hi-Z, Z):** the output is disconnected: both totem-pole transistors are off, so it neither pulls up nor pulls down (deck 05 slide 47: it "behaves as an open circuit"). **Enable (EN):** the input that chooses between driving (EN = 1) and Z (EN = 0). **Bus:** one wire (or set of wires) shared by several outputs, only one of which drives at a time.
:::

[[fig:tristate_bus|Several tristate buffers on one bus line: the enabled buffer drives the line; the others are in Hi-Z and are, in effect, not connected.|w=60]]

| EN | IN | OUT |
|---|---|---|
| 0 | 0 | Z |
| 0 | 1 | Z |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Deck 05 slide 47: gates without a Z state "cannot have their outputs connected together"; Hi-Z gates "can". When enabled, a tristate output is a normal fast totem pole; when disabled, it is out of the circuit. So the enables must be arranged (usually by a decoder, file 06) so that **exactly one** buffer on a bus is enabled. Two enabled with different data is step 10's fight again (**bus contention**). Slide 46 adds variations: active-low EN, inverted OUT.

**Answer to the question.** EN = 0: OUT = **Z** for IN = 0 and 1; EN = 1: OUT = **IN** (0 → 0, 1 → 1).

:::check Check 11
(a) Four tristate buffers drive one bus line. At most how many may be enabled at once? What does the line do if none is? (b) Which file-06 circuit gives "exactly one of four" enables from 2 select bits?
:::

### 12 · ECL: the bipolar gate that never saturates

Steps 9–11 used saturating transistors. Deck 14 slide 14 names ECL the "fastest available logic family"; the reason is what ECL refuses to do.

:::guess Predict
A saturated BJT has extra charge stored in its base. Before it can switch off, that charge must be removed. What would a gate designer do to avoid waiting for it?
:::

:::note Terms
**Emitter-coupled logic (ECL):** a bipolar family whose gate is a **differential pair**: two transistors share one emitter resistor that sets a nearly constant current, and the input decides which transistor carries it. **Current steering:** the current is never switched off, only moved from one transistor to the other.
:::

[[fig:ecl_gate|An ECL gate: input transistor and reference transistor share one emitter current; the higher base takes it. Outputs come out through emitter followers as OR and NOR.|w=55]]

Neither transistor of the pair is driven into saturation, so no stored base charge has to be cleared: switching is limited only by moving a small voltage across small capacitances. That makes ECL the fastest family, at a price:

| Gain | Cost |
|---|---|
| fastest switching (deck 14 slide 14) | the steering current flows all the time: highest static power |
| true and complement outputs (OR and NOR) at once | small voltage swing, so a small noise margin |
| | needs careful wiring (slide 14: "requires extreme care") |

A 1985 comparison of 7400-format quad NAND gates (University of Cambridge notes): ECL 0.8 ns at 200 mW = 160 pJ; TTL 74F00 3.4 ns at 5 mW = 17 pJ; CMOS 74HC00 7 ns at 1 mW = 7 pJ. ECL wins on speed and loses on energy.

:::note Not yet checked
Deck 14 slide 14 lists ECL's supply as "±5 V". Lecture leads give V_{EE} = −5.2 V and levels near −0.9 V (1) and −1.7 V (0) for the 10K series, with a noise margin of about 0.1–0.15 V. None of these was read in a data sheet or textbook this session `uncertain`: do not quote them as exact values.
:::

**Answer to the Predict.** **Never let the transistor saturate.** ECL steers a constant current between two transistors that both stay out of saturation, so there is no stored charge to wait for.

:::check Check 12
(a) Why does an ECL gate draw power even when its inputs never change? (b) From the Cambridge figures, how many times faster is the ECL gate than the 74HC00, and how many times more energy does it spend per switch?
:::

### 13 · The families compared

Steps 7–12 opened the three families the deck names. Deck 14 slides 13–21 set them side by side; this step builds the table from the numbers checked in this file.

:::guess Predict
Rank TTL, ECL and CMOS for: (a) speed, (b) static power, (c) noise margin. Which would you put in a battery-powered device?
:::

| | Standard TTL (7400) | CMOS (74HC00, V_{CC} = 4.5–5 V) | ECL |
|---|---|---|---|
| transistor | BJT, saturating | pMOS + nMOS | BJT, non-saturating |
| t_{pd} | 11 ns (t_{PLH} typ) | 9 ns typ | under 1 ns (0.8 ns, 1985 part) |
| static power per gate | 10 mW | about 0 (2 µA per package) | highest (200 mW, 1985 part) |
| power while switching | 10 mW + switching | C V² f: 0.5 mW at 1 MHz | about the same as static |
| noise margin | 0.4 V | 1.25 V at 4.5 V (28 % of V_{CC}) | small `uncertain` |
| fan-out | 10 | not a current limit (see below) | — |
| supply | 5 V | 2–6 V | negative supply `uncertain` |

**Families in the deck (slide 13):** DL, RTL, DTL (obsolete), TTL, ECL, MOS, CMOS. Slide 14 rings CMOS and TTL as "the most important to understand". **Integration levels (slide 15):** SSI < 12 gates per chip, MSI < 100, LSI about 1 000, VLSI about 10 000, ULSI about 100 000, GSI about 1 000 000; the slide's own scale, with boundaries that books draw differently. Slide 17: a VLSI chip built from TTL gates "would melt" (10 mW × 10⁶ gates = 10 kW), which is why every large chip is CMOS.

**CMOS fan-out.** A CMOS input draws almost no steady current, so I_{OL}/I_{IL} is huge. What each input does add is capacitance (74HC00: 3 pF typical, 10 pF max), and more load capacitance means slower edges (step 2). CMOS fan-out is therefore set by the speed you need, not by DC current; slide 20's "about 50" is that kind of practical figure and is not checked here.

:::note Slide slips
Slide 20 gives CMOS "a single supply of 5–15 V" and slide 14 "3–15 V": those fit the older 4000 series (rated up to about 15–18 V, not checked here), not the 74HC series (2–6 V, data sheet). Slide 20's "noise immunity about 30 % of supply" agrees with the 74HC00 numbers above (1.25 V of 4.5 V = 28 %).
:::

**Answer to the Predict.** (a) Speed: ECL fastest, then CMOS and TTL close together. (b) Static power: CMOS lowest (almost 0), then TTL, ECL highest. (c) Noise margin: CMOS largest (1.25 V), TTL 0.4 V, ECL smallest. Battery device: **CMOS**, because it draws power only when it switches.

:::check Check 13
(a) Why is every VLSI chip CMOS, in one line with a number? (b) A CMOS gate drives 20 inputs of 10 pF each. What load capacitance is that, and what happens to its rise time compared with one input?
:::

### 14 · Interfacing TTL and CMOS

Step 13 showed the families use different levels. When one family's output drives another's input, both of its numbers must be checked.

:::guess Predict
A 7400 output drives a 74HC00 input, both on 5 V. The 7400's HIGH is guaranteed only down to 2.4 V. A 74HC00 at 4.5 V needs at least 3.15 V to read a 1. Does the link work?
:::

:::note Terms
**Interfacing:** connecting an output of one family to an input of another. It works only if (1) the output's guaranteed levels clear the input's thresholds (step 4) **and** (2) the output can supply the current the inputs draw (step 6). **Pull-up resistor:** a resistor from the line to V_{CC} that lifts a weak HIGH to near the supply.
:::

| Direction | Levels | Current | Verdict |
|---|---|---|---|
| TTL 7400 → CMOS 74HC00 | V_{OH(min)} 2.4 V < V_{IH(min)} 3.15 V: **fails** | CMOS input takes almost none: fine | fix the HIGH |
| CMOS 74HC00 → TTL 7400 | V_{OH} ≥ 3.98 V > 2.0 V; V_{OL} ≤ 0.26 V < 0.8 V (at 4 mA, 25 °C): pass | 4 mA sink / 1.6 mA per input = 2.5 | drives **2** TTL inputs |

Fixes for TTL → CMOS (KB 05 §4): a **pull-up resistor** from the TTL output to +5 V, which lifts the HIGH towards 5 V; or a **74HCT** part, a CMOS chip whose input thresholds are made TTL-compatible. For CMOS → TTL beyond 2 inputs, a buffer with stronger drive.

Every unused CMOS input is tied to V_{CC} or ground: the 74HC00 data sheet requires it. A floating CMOS input drifts, can sit near the middle where both transistors conduct (step 7), and wastes power or oscillates. A floating TTL input reads as HIGH (Check 9b) but picks up noise; tie it too.

**Answer to the Predict.** **No.** The 7400 guarantees only 2.4 V, which is below the 3.15 V the 74HC00 needs: a HIGH may be misread. Add a pull-up resistor or use a 74HCT part.

:::check Check 14
(a) One 74HC00 output must drive five 7400 inputs. What fails, and what do you add? (b) Why does a 74HC00 driving 7400 inputs not need a level check on the HIGH?
:::

---

## Exam form

**Yardsticks (steps 1–6).**
1. t_{PHL}, t_{PLH}: input 50 % to output 50 %, output falling / rising; sketch the two waveforms. t_{pd} for timing = the larger.
2. t_{r}: 10 % → 90 %; t_{f}: 90 % → 10 %.
3. Static power = V_{CC} × average I_{CC}; dynamic P = C V² f.
4. NM_{H} = V_{OH(min)} − V_{IH(min)}, NM_{L} = V_{IL(max)} − V_{OL(max)}; sketch the two voltage-band bars.
5. PDP = t_{pd} × P, in joules (pJ); smaller is better.
6. Fan-out = min(I_{OL}/I_{IL}, I_{OH}/I_{IH}); fan-in = number of inputs.
7. Standard TTL: 2.4/0.4/2.0/0.8 V; 0.4/16 mA out, 40 µA/1.6 mA in → NM 0.4 V, fan-out 10.

**Circuits (steps 7–12).** CMOS inverter with its two-row switch table; NAND (nMOS series, pMOS parallel) and NOR (the dual); why static power ≈ 0. TTL NAND: multi-emitter input, both input cases. Totem pole vs open collector (wired-AND, pull-up). Tristate: symbol, EN/IN/OUT table, bus, contention. ECL: current steering, no saturation → fastest; highest power, small swing.

**Comparison and interfacing (13–14).** The three-family table; integration levels; TTL → CMOS fails on V_{OH} (fix: pull-up or HCT); CMOS → TTL limited by sink current; tie unused inputs.

## Traps

- Fan-out from one state only: compute both ratios and take the smaller.
- NM_{L} = V_{IL(max)} − V_{OL(max)}, not the other way round; and use guaranteed values, not typical.
- Rise time from 0 % to 100 %: it is 10 % to 90 %.
- "CMOS uses no power": its static power is near 0, its dynamic power C V² f grows with frequency.
- Joining totem-pole outputs: never; open collector (with a pull-up) or tristate (one enabled) instead.
- Fan-in is the number of inputs, not a current ratio.
- Writing PDP in watts: delay × power is energy (J, usually pJ).

## Self-test

1. V_{OH(min)} = 4.9 V, V_{IH(min)} = 3.5 V, V_{IL(max)} = 1.5 V, V_{OL(max)} = 0.1 V. Find both noise margins.
2. I_{OL} = 4 mA, I_{IL} = 0.1 mA, I_{OH} = 0.4 mA, I_{IH} = 20 µA. Fan-out?
3. A gate has t_{PHL} = 6 ns, t_{PLH} = 10 ns and draws 2 mW. Its t_{pd} for a timing check, and its PDP?
4. A CMOS gate with C = 50 pF switches at 2 MHz from 5 V. Dynamic power?
5. Draw a 2-input CMOS NOR at switch level and give its output for A = 0, B = 1.
6. Why can two 7400 outputs not be joined, and name two output types that can share a line.
7. A 7400 must drive a 74HC00 input on 5 V. What goes wrong and give two fixes.
8. Why is ECL faster than TTL, and what does it pay for it?

<!--ANSWERS-->

## Answers

**Check 1.** (a) The output is rising, so this is **t_{PLH} = 8 − 3 = 5 ns**. (b) **12 ns**, the larger of the two.

**Check 2.** (a) 0.3 V and 2.7 V are 10 % and 90 % of 3 V: **t_{r} = 5 − 2 = 3 ns**. (b) **t_{PLH}**; t_{r} uses 10 % and 90 %.

**Check 3.** (a) 20 pF × 25 V² × 10⁷ /s = **5 mW**. (b) 2 × (½)² = **½**: the power halves.

**Check 4.** (a) NM_{H} = 4.4 − 3.15 = **1.25 V**; NM_{L} = 1.35 − 0.1 = **1.25 V**. (b) 1.25/4.5 = **28 %** (deck 14 slide 20: "about 30 %").

**Check 5.** (a) 5 ns × 2 mW = **10 pJ**. (b) ½ × 4 = 2: the PDP **doubles** (it gets worse).

**Check 6.** (a) LOW: 8/0.4 = 20; HIGH: 0.4 mA/20 µA = 20: **fan-out 20**. (b) **3**; it counts input pins, fixed when the gate is made, so no current enters into it.

**Check 7.** (a) The **pMOS** (on when its gate is LOW). (b) A floating input can drift to about V_{DD}/2, where both transistors are partly on: current flows straight through, and the output is undefined or oscillates. Tie it to V_{DD} or 0 V.

**Check 8.** (a) **6** transistors; the three nMOS are **in parallel** (any input 1 pulls X low). (b) Both pMOS (series, both on) are **on**, both nMOS off: **X = V_{DD} = 1** = (0 + 0)'.

**Check 9.** (a) **On** (saturated): Q₁'s base current goes out of its collector into the output transistor's base; **X = 0**. (b) An open emitter cannot carry current, just like an emitter held HIGH, so the base current goes on into the next transistor, exactly as for a HIGH input.

**Check 10.** (a) One output pulls LOW: the line is **0** (1·0·1 = 0). (b) Totem pole: **fast edges both ways** (active pull-up). Open collector: outputs **can be joined** (wired-AND), and the pull-up can go to a different supply.

**Check 11.** (a) **One**; with none enabled, every output is Z and the line **floats** (undefined) unless a pull-up resistor holds it. (b) A **2-to-4 decoder**: exactly one output is active for each select code.

**Check 12.** (a) Its steering current flows all the time; the input only moves it from one transistor to the other. (b) 7/0.8 ≈ **9 times faster**; 160/7 ≈ **23 times more energy** per switch.

**Check 13.** (a) At 10 mW per gate, a million TTL gates would take **10 kW**; CMOS gates take almost nothing while still. (b) 20 × 10 pF = **200 pF**, 20 times one input's 10 pF, so the edges take about 20 times longer to charge: **slower rise time**.

**Check 14.** (a) LOW state: five inputs push 5 × 1.6 = 8 mA into the output, but it is specified only to 4 mA at V_{OL} ≤ 0.26 V; its LOW may rise past V_{IL(max)} = 0.8 V. Add a **buffer** with more sink current (or split the load). (b) Its HIGH is at least 3.98 V, far above TTL's V_{IH(min)} = 2.0 V.

**Self-test.**

1. NM_{H} = 4.9 − 3.5 = **1.4 V**; NM_{L} = 1.5 − 0.1 = **1.4 V**.
2. 4/0.1 = 40, 0.4 mA/20 µA = 20: **fan-out 20**.
3. t_{pd} = **10 ns** (the larger); PDP = 10 ns × 2 mW = **20 pJ**.
4. 50 pF × 25 × 2 × 10⁶ = **2.5 mW**.
5. Two pMOS in series from V_{DD}, two nMOS in parallel to 0 V. A = 0, B = 1: nMOS B is on, so **X = 0** (pMOS B is off, the series pull-up is broken).
6. One HIGH and one LOW would short +5 V to ground through the two totem poles: large current, undefined level. **Open-collector** (with a pull-up resistor: wired-AND) and **tristate** (one enabled at a time).
7. Its HIGH is guaranteed only to 2.4 V, below the 74HC00's V_{IH(min)} (3.15 V at 4.5 V). Fix: a **pull-up resistor** to +5 V, or a **74HCT** part with TTL-level inputs.
8. Its transistors **never saturate** (current steering), so no stored charge delays switch-off. It pays with **the highest static power** (the current always flows) and a **small noise margin** (small swing).

<!--/ANSWERS-->
