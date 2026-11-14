# Electronic Devices & Circuits — Study Pack (ETE)

<div class="sub">ECE2106 · B.Tech ECE Sem 3 · all 7 units of the syllabus on slide 2 of the professor's first deck · built from the professor's decks and solved-numerical sheets · every answer checked by computer</div>

## Priority order: if time is short, study in this order

Ranked by how much the professor's material stresses each topic: solved numerical sheets, a flagged mark value, and the size of the deck. There is **no past paper yet**, so this is an estimate. Every topic on the syllabus can come up.

| Rank | Study | Why it ranks here | Do first | Rough time |
|---|---|---|---|---|
| 1 | **07 JFET** | A classmate relayed "8 marks" for the JFET parameters; the professor's numericals sheet spends Q1–Q19 on JFETs | 07 §3 (parameters), then §2 and §4 | 70 min |
| 2 | **08 MOSFET** | The same sheet, Q20–Q31: D-MOSFET and E-MOSFET bias and gain | 08 bias steps | 60 min |
| 3 | **11 BJT biasing and stability** | 53-slide deck, the longest in Unit 5; stability factor is derived in full | 11 voltage-divider bias, S | 60 min |
| 4 | **12 h-parameters, multistage** | A whole problem sheet (book pp. 131–145, Problems 3–16) | 12 the four formulas | 50 min |
| 5 | **04 Diode circuits and rectifiers** | Two decks of worked examples (L08, L09) | 04 rectifier table | 40 min |
| 6 | **05 Clippers, clampers, Zener** | Deck L10 with worked examples | 05 clamper rule, Zener regulator | 40 min |
| 7 | **13 Feedback** | 51-slide deck, four topologies | 13 gain with feedback | 40 min |
| 8 | **14 Oscillators** | Deck with RC, Wien, LC, crystal | 14 Barkhausen, RC phase-shift | 35 min |
| 9 | **03 pn junction and diode** | Second half of the 100-slide Unit 1–2 deck | 03 built-in voltage, diode equation | 40 min |
| 10 | **01, 02 Semiconductors and current flow** | First half of the same deck; mostly definitions and short derivations | 02 drift and diffusion | 50 min |
| 11 | **10 BJT operation** | Short decks L20–L25 | 10 α, β | 25 min |
| 12 | **06 Special diodes, 09 CMOS and FinFET** | Extra decks beyond the syllabus text | 09 CMOS gate | 30 min |
| last | **15 Mock paper** | Closed book, after the rest | all | 3 h |

Two rules for using the ranking:

- **Short on time:** do only the "Do first" column, top to bottom, then the matching mock-paper questions.
- **Stuck in 07 or 08:** both lean on 03 (the reverse-biased pn junction). Go back one step and don't skip ahead.

## The path through this pack

The order is the syllabus, unit by unit.

**Unit 1 — semiconductors**

[[map:01 Semiconductors, carriers > 02 Drift, diffusion, continuity]]

**Unit 2 — the diode**

[[map:03 pn junction, diode > 04 Diode circuits, rectifiers > 05 Clippers, clampers, Zener > 06 Special diodes]]

**Units 3–4 — field-effect transistors**

[[map:07 JFET|here=1]]

[[map:08 MOSFET > 09 CMOS, FinFET]]

**Units 5–7 — BJT, feedback, oscillators**

[[map:10 BJT operation > 11 BJT biasing > 12 h-parameters > 13 Feedback > 14 Oscillators > 15 Mock paper]]

Each file needs the ones before it. 07 uses 03's depletion region. 08 reuses 07's biasing method. 11 uses 10's α and β. 13 and 14 use 12's amplifier gain. 14 is 13 with the feedback made positive.

| File | Syllabus item | What it teaches | Real Qs |
|---|---|---|---|
| 01 | U1 | energy bands, electrons and holes, doping, mass-action law, Fermi level | deck |
| 02 | U1 | drift, mobility, conductivity, diffusion, Einstein relation, continuity | deck |
| 03 | U2 | junction, depletion region, built-in voltage, diode equation, resistances, capacitances | deck |
| 04 | U2 | load line, series/parallel diode circuits, half- and full-wave rectifiers | L08, L09 |
| 05 | U2 | clippers, clampers, voltage multipliers, Zener regulator, Schottky | L10 |
| 06 | U2 extra | LED, photodiode, tunnel diode | deck |
| 07 | U3 | JFET operation, Shockley's equation, g_{m}, r_{d}, μ, biasing, CS and CD amplifiers | sheet Q1–Q19 |
| 08 | U4 | E- and D-MOSFET, regions, current equations, biasing, amplifiers | sheet Q20–Q31 |
| 09 | U4 extra | MOSFET as a switch, CMOS gates, FinFET | deck |
| 10 | U5 | BJT construction, operation, α, β, the three connections | L20–L25 |
| 11 | U5 | load line, Q-point, fixed / emitter / voltage-divider bias, stability factor | L26–L27 |
| 12 | U5 | h-parameter model, CE and CC analysis, multistage, Darlington | book Problems 3–16 |
| 13 | U6 | feedback, the four topologies, effects of negative feedback | deck |
| 14 | U7 | Barkhausen, RC phase-shift, Wien bridge, Hartley, Colpitts, crystal | deck |
| 15 | all | one closed-book paper with a key | sheet extras |

## Where the questions come from

A step opens with a **real question, quoted**, wherever the professor's material has one, tagged with its source: <span class="tag">Sheet Q17</span> = the JFET/MOSFET solved-numericals sheet, <span class="tag">Book P3</span> = the h-parameter problem pages, <span class="tag">Deck</span> = a worked example on a slide. Where there is none, the step opens with a **Predict** prompt instead, or a problem tagged <span class="tag">practice</span>.

Marks per question: **not known**, except the relayed "8 marks" for the JFET parameters.

## How each file runs

| Part | What happens |
|---|---|
| **Map** | the file's steps, in order |
| **Build** | each step opens with a real question or a Predict → you guess → the answer teaches the idea → a Check |
| **Exam form** | what to reproduce in the exam: statements, derivations, procedures, formulas |
| **Traps** | the mistakes that cost marks |
| **Self-test, Answers** | answers to every Check and the Self-test are on the last page(s) of each file |

:::key The one rule that makes this work
When you reach a **Guess first** box, write a guess on paper **before** reading on: one line, however wrong. A wrong guess that gets corrected sticks better than a right answer you only read.
:::

## Units and symbols used everywhere

- Uppercase **V, I** with uppercase subscripts = DC values (V_{GS}, I_{D}). Lowercase **v, i** = small AC signals (v_{gs}, i_{d}).
- Resistances in **kΩ** with currents in **mA** give voltages in **V** directly: 3.3 kΩ × 1.52 mA = 5 V.
- n-channel devices throughout unless a step says p-channel. For a p-channel device every voltage and current reverses.

## Where the professor's material disagrees with the pack

| Where | Slide says | Pack says | Why |
|---|---|---|---|
| L08 slide 5 (04) | V_{R} = 18.5 V | 9.25 V | R is 0.5 kΩ; 18.5 V cannot come from a 10 V source |
| Feedback slide 32 (13) | 98.3 for A = 5000 | 98.0 | 5000/51 = 98.0; the table's other entries are right |

## How this pack was checked

- Facts: the subject knowledge base (Boylestad & Nashelsky, Sedra & Smith, Streetman, Neamen). Units 6–7 and the deck extras are not in the knowledge base yet; their formulas are the standard textbook results, each re-derived or simulated.
- Numbers: every number in the pack was computed a second time by `verify.py` (211 checks), including numerical simulation of the oscillator networks.
- Where a slide has a slip, the pack uses the corrected value and says so in a Note.
