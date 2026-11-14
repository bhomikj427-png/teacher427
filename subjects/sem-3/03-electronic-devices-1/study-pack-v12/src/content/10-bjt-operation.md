# 10 — BJT operation

<div class="sub">Decks L20–L25 · syllabus Unit 5 ("BJT characteristics and comparison with MOSFETs") · needs 03 (forward and reverse bias of a pn junction)</div>

## Map

[[map:1 Structure, operation > 2 CB, CE, CC and α, β, γ > 3 BJT vs MOSFET|here=1]]

The FETs (07, 08) use a voltage to control a channel. The bipolar junction transistor is two pn junctions back to back, and a small current into the thin middle layer controls a large current through the device.

## The questions this file answers

- <span class="tag">Deck L20</span> Why is the base thin and lightly doped, and the emitter heavily doped?
- <span class="tag">Deck L22</span> Compare the CB, CE and CC connections; derive the relations among α, β and γ.
- <span class="tag">practice</span> β = 100 and I_{CBO} = 20 nA: find α and I_{CEO}.
- <span class="tag">Syllabus</span> Compare the BJT with the MOSFET.

---

## Build

### 1 · Construction and operation

:::q <span class="tag">Deck L20</span>
Why is the base of a transistor made very thin and lightly doped, while the emitter is heavily doped?
:::

:::guess Guess first
What should happen to the electrons the emitter sends into the base?
:::

:::note Terms
**Emitter (E):** supplies (emits) the carriers. **Base (B):** the thin middle layer that controls them. **Collector (C):** collects them.
:::

[[fig:bjt_struct|npn BJT in the active region: EB forward, CB reverse.|w=70]]

- Three layers, n–p–n or p–n–p, so two junctions: emitter–base and collector–base. "Bipolar": both electrons and holes take part.
- **Active region (npn):** EB forward biased, so the emitter injects electrons into the base. Only about 1% recombine there; that needs a small **I_{B}**. The other 99% diffuse across and are swept into the collector by the reverse-biased CB junction: **I_{C}**.
- A small I_{B} controls a large I_{C}: the BJT is **current-controlled**. For pnp, swap n and p and reverse everything.

$$I_{E} = I_{C} + I_{B}$$

[[fig:bjt_symbols|npn and pnp symbols; the arrow is on the emitter and shows conventional current.|w=45]]

| Region | EB | CB | Behaviour · use |
|---|---|---|---|
| **Active** | forward | reverse | I_{C} = βI_{B}, V_{BE} ≈ 0.7 V. Amplifier |
| Saturation | forward | forward | I_{C} &lt; βI_{B}, set by the circuit; V_{CE(sat)} ≈ 0.2 V. Closed switch |
| Cutoff | reverse | reverse | I_{C} ≈ 0. Open switch |

**Answer.** Almost every carrier from the emitter should reach the collector. A thin, lightly doped base has few holes and gives electrons little time to meet one, so few recombine: I_{B} is small and I_{C}/I_{B} large. The heavy emitter doping makes the EB current almost all electrons into the base, not holes back into the emitter. The collector is the largest region because it dissipates the most heat.

:::check Check 1
(a) State the bias of each junction in the active region. (b) I_{E} = 5 mA, I_{B} = 50 μA. Find I_{C}. (c) Which regions does a switch use?
:::

### 2 · The three connections and α, β, γ

:::q <span class="tag">practice · decks L22–L25</span>
A transistor has β = 100 and I_{CBO} = 20 nA. Find α and I_{CEO}.
:::

:::guess Guess first
Is α slightly below 1 or slightly above?
:::

An amplifier needs two input and two output wires, so one terminal is shared ("common"):

| | Common base (CB) | Common emitter (CE) | Common collector (CC) |
|---|---|---|---|
| In · out | emitter · collector | base · collector | base · emitter |
| Current gain | α = I_{C}/I_{E}, 0.95–0.995 | β = I_{C}/I_{B}, 50–400 | γ = I_{E}/I_{B} = 1 + β |
| Voltage gain | high | high | just under 1 |
| R_{in} | very low (tens of Ω) | medium (≈ 1 kΩ) | very high |
| R_{out} | very high | medium–high | very low |
| Phase | 0° | 180° | 0° |
| Use | high frequency; low-R source | general: highest power gain | buffer, matching |

**Relations.** Substitute I_{E} = I_{C} + I_{B} into the definitions:

$$β = α/(1 − α)      α = β/(1 + β)      γ = 1 + β = 1/(1 − α)$$

**Leakage.** I_{CBO} (I_{CO}) is the CB leakage with the emitter open. In CE the transistor amplifies its own leakage: **I_{CEO} = (1 + β)I_{CBO}**, the collector current with the base open. Complete expressions: I_{C} = αI_{E} + I_{CBO}; I_{C} = βI_{B} + (1 + β)I_{CBO}.

**Characteristics.** Input curves (I_{B} against V_{BE}) look like a forward diode. Output curves (I_{C} against V_{CE}, one per I_{B}) are nearly flat in the active region (11 §1).

**Answer.** α = 100/101 = **0.990**. I_{CEO} = 101 × 20 nA = **2.02 μA**.

:::check Check 2
(a) α = 0.98. Find β and γ. (b) Derive β = α/(1 − α). (c) Which connection drives an 8 Ω loudspeaker from a high-resistance stage, and why?
:::

### 3 · BJT compared with the MOSFET

:::q <span class="tag">Syllabus Unit 5</span>
Compare the BJT and the MOSFET.
:::

:::guess Guess first
Write five rows from memory before reading the table.
:::

| Point | BJT | MOSFET |
|---|---|---|
| Controlled by | base current | gate voltage |
| Carriers | both (bipolar) | one type (unipolar) |
| Input resistance | ≈ 1 kΩ (CE); draws input current | 10^{10} Ω and above; no DC input current |
| Transfer law | exponential: I_{C} ∝ e^{V_{BE}/V_{T}} | square: K(V_{GS} − V_{T})^{2} |
| g_{m} | high: I_{C}/V_{T} (38 mS at 1 mA) | lower: 2√(KI_{D}) |
| Gain per stage | higher | lower |
| Temperature | I_{C} rises: thermal runaway risk | I_{D} falls (mobility drops): self-limiting |
| Switching | slowed by stored charge in saturation | no stored minority charge |
| Power in logic | base current flows continuously | CMOS ≈ 0 when idle |
| Density | larger | tiny: billions per chip |
| Noise · handling | more noise; robust | less noise; oxide damaged by static |
| Best at | high-gain analog amplifiers | digital ICs, switches, high-Z_{in} stages |

**Answer.** The table: any eight rows, each with both columns.

:::check Check 3
(a) Two reasons MOSFETs replaced BJTs in digital ICs. (b) Which gives more voltage gain per stage, and which parameter explains it? (c) Why is a MOSFET thermally more stable?
:::

---

## Exam form

**Operation.** Sketch npn with biases; electron flow: injection, ~1% recombination (I_{B}), collection (I_{C}); I_{E} = I_{C} + I_{B}; doping and width reasons. Region table.

**Connections.** The CB/CE/CC table. Derive β = α/(1 − α), γ = 1 + β. I_{CEO} = (1 + β)I_{CBO}.

**Comparison.** BJT vs MOSFET table, at least eight rows.

## Traps

- Writing V_{BE} ≈ 0.7 V in cutoff: it is below that.
- Swapping α and β: α &lt; 1 is CB; β ≫ 1 is CE.
- Forgetting the (1 + β) when leakage flows in CE.
- Saying CC has voltage gain: it has current gain only (γ), voltage gain just under 1.

## Self-test

1. I_{E} = 10 mA, α = 0.99. Find I_{C} and I_{B}.
2. β = 150. Find α.
3. I_{CBO} = 10 nA, β = 100. Find I_{CEO}.
4. Draw the CB/CE/CC table from memory (gains, resistances, phase).
5. Why is CE the most used connection?
6. Explain why the collector current hardly depends on V_{CE} in the active region.

<!--ANSWERS-->

## Answers

**Check 1.** (a) EB forward, CB reverse. (b) I_{C} = 5 − 0.05 = **4.95 mA**. (c) Cutoff (open) and saturation (closed).

**Check 2.** (a) β = 0.98/0.02 = **49**; γ = **50**. (b) β = I_{C}/I_{B} = I_{C}/(I_{E} − I_{C}); divide by I_{E}: α/(1 − α). (c) **Common collector**: high R_{in}, very low R_{out}, so it drives a low-resistance load without loading the stage before.

**Check 3.** (a) Near-zero static power in CMOS; far smaller, so higher density (also simpler fabrication). (b) The BJT: g_{m} = I_{C}/V_{T} is higher at the same current. (c) Its current falls as temperature rises, because mobility falls.

**Self-test.**

1. **I_{C} = 9.9 mA**, **I_{B} = 0.1 mA**.
2. α = 150/151 = **0.9934**.
3. 101 × 10 nA = **1.01 μA**.
4. See step 2.
5. It is the only connection with both current gain and voltage gain, so it has the highest power gain; its R_{in} and R_{out} are moderate.
6. The CB junction is reverse biased; its field sweeps across every electron that reaches it. I_{C} is set by how many electrons the emitter injects (by V_{BE}, I_{B}), not by how hard they are pulled.

<!--/ANSWERS-->
