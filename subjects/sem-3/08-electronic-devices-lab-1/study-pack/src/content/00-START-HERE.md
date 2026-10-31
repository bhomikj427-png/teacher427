# 00 · Start here: the whole lab on one page

<div class="sub">ECE2130 / VDT2130 Electronic Devices Lab-I · source: the lab manual (session 2025-26), 39 pp. · every expected number in this pack comes from running the manual's own circuits in LTspice</div>

## The lab as one path

[[map:Instruments (Exp 0) > Diodes: 1 zener curve · 2 regulator · 3 clipper · 4 clamper > BJT: 5 curves · 6 CE amp · 7 follower · 8 feedback > JFET: 9 curves · 10 CS amp > 11 oscillator > 12 MOSFET inverter > Extra: two-stage amp + design problem|here=1]]

Each block builds on the one before it:

- **Diodes first.** A diode is one junction. Exp 1 measures it, and Exps 2–4 use it in three circuits.
- **Then the BJT.** A transistor is two junctions. Exp 5 measures its curves, and Exps 6–8 turn it into amplifiers.
- **Then FETs.** The same "measure the curve, then build the amplifier" pattern, with a field-controlled device.
- **Exp 11 and Exp 12** take an amplifier somewhere new: positive feedback makes an oscillator, and a transistor used as a switch makes a logic gate.

## How each experiment is run and marked

| Exp | Topic | Done in | Marked by |
|---|---|---|---|
| 0 | DC and AC measurement | hands-on | not assessed |
| 1 | Zener characteristics, dynamic resistance | hands-on | viva, ETE |
| 2 | Zener line and load regulation | LTspice / Virtual Lab | viva, ETE |
| 3 | Clipper | hands-on | viva, ETE |
| 4 | Clamper | LTspice | viva, ETE |
| 5 | BJT CE characteristics, h-parameters | LTspice / Virtual Lab | viva, ETE |
| 6 | CE amplifier frequency response | hands-on | viva, ETE |
| 7 | Emitter follower gain | hands-on | viva, ETE |
| 8 | Negative feedback (bypass capacitor) | LTspice | viva, ETE |
| 9 | JFET drain and transfer characteristics | LTspice | viva, ETE |
| 10 | CS amplifier frequency response | LTspice | viva, ETE |
| 11 | RC phase-shift oscillator | LTspice | viva, ETE |
| 12 | MOSFET inverter | LTspice | viva, ETE |

The manual does not give this lab's marks split. The Digital Electronics lab manual gives 100 = internal 60 + external 40, with a 3-hour exam. Expect the same shape here, but it is not confirmed.

**ETE** (end-term exam) for a lab usually means: you are given one experiment, you build or simulate it, you show the result, and you answer **viva** (oral) questions on it. So for every experiment you need to be able to:

1. draw the circuit from memory,
2. build or simulate it without help,
3. get the expected readings and calculate the result,
4. answer "why" questions about it.

Each chapter below gives you those four things, in that order.

## What goes in the record (lab file)

The manual (p. 3) asks for six headings per experiment:

| Heading | What to write |
|---|---|
| Aim | as in the list above |
| Circuit diagram | the circuit, labelled with values |
| Theory | about 15 lines. Each chapter has a ready "Theory for the record" block. |
| Observations | the table or a well-labelled waveform |
| Calculations | if any, with the formula first |
| Result | the parameters, **with % error** |

$$\% error = \frac{|theoretical − observed|}{theoretical} × 100$$

## How a chapter works

:::q The question
Each chapter opens with the experiment's aim, quoted from the manual, plus a real viva-style question.
:::

:::guess Guess first
Answer it on paper before reading on, even if your answer is a wild guess. Guessing first makes the explanation stick better than reading cold. This line is the reason the pack works, not decoration.
:::

Then come **the ideas needed**, **the circuit**, a **Do it** box with the exact steps, **what you should see** (simulated curves and numbers), the worked **calculation**, a **Write in your record** box, **traps**, and **checks**. The answers to the checks are on the last page of each chapter.

## Errors in the manual (know these for the viva)

| Where | The manual says | Correct |
|---|---|---|
| Exp 0 | V_{rms} = V_{p}/√2, with V_{p} read as peak-to-peak | For a sine, V_{rms} = V_{peak}/√2 = V_{pp}/(2√2) |
| Exp 1 | Requirement: diode 1N4007 | The experiment needs a **zener** diode. A 1N4007 is an ordinary rectifier and will not show a sharp breakdown below about 1000 V. |
| Exp 5 | h_{21} = output admittance, h_{22} = forward current gain | Swapped. h_{21} = h_{fe} (forward current gain), h_{22} = h_{oe} (output admittance). |
| Exp 5 | 1/h_{oe} = ΔI_{C}/ΔV_{CE} | h_{oe} = ΔI_{C}/ΔV_{CE}. The ratio is a conductance, so 1/h_{oe} is the output resistance. |
| Exp 5 | "Keep emitter current I_{b} = 20 A" | **Base** current I_{B} = 20 **µA** |
| Exp 5 | Fig 5.1 with 62 kΩ in the collector | With 62 kΩ, I_{C} can never exceed 10 V / 62 kΩ = 0.16 mA, so the I_{B} = 20/40 µA table cannot be filled. See Exp 5. |
| Exp 6 | Input 500 mV | This clips the output badly. Use about 20 mV (Exp 6 shows both). |
| Exp 7 | Input impedance "of the order of hundred ohms" | Input impedance is **high**: about 3 kΩ here (set by the bias resistors), and about 600 kΩ looking into the base alone. The **output** impedance is the low one (about 70 Ω). |
| Exp 9 | r_{d} = (7 − 6)/(0.1183 − 0.1180) = 3.3 kΩ | Decimal slip. The manual's own data (11.83 − 11.80 mA) gives 1 V / 0.03 mA = **33 kΩ**. LTspice gives 38 kΩ. |
| Exp 12 | "V_{th} is the inverter threshold voltage, which is V_{dd}/2" | Two different things. V_{TH} is the MOSFET's turn-on voltage. V_{M} is where V_{out} = V_{in}. V_{M} = V_{DD}/2 only for a symmetric CMOS inverter, not for this resistor-load circuit (V_{M} ≈ 0.76 V here). |
