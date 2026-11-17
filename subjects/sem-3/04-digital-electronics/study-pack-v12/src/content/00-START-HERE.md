# Digital Electronics — Study Pack (ETE)

<div class="sub">ECE2102 (ECE 2105 on the decks) · B.Tech ECE Sem 3 · all 5 units of the syllabus on slide 2 of the professor's first deck · built from the 2025 mid-term paper, decks 01–15 and two practice sets · every answer checked by computer</div>

## Priority order: if time is short, study in this order

Ranked by the professor's own material: the 2025 mid-term paper (30 marks: 2-mark recall, 4-mark method, one 8-mark design), the two practice sets, and the decks. There is **no end-term paper yet**, so this is an estimate. The mid-term covered Units 1–3 up to counters; the end-term covers all five units, so Units 3–5 weigh more than the mid-term suggests.

| Rank | Study | Why it ranks here | Do first | Rough time |
|---|---|---|---|---|
| 1 | **13 Synchronous counters** | The mid-term's only 8-mark question; practice set 2 Q4–Q6; deck 10 | 13 §2–§3 | 60 min |
| 2 | **15 FSM design** | Deck 11, with five practice detectors on its last slide; Unit 4 is not yet examined | 15 the 1101 detector | 60 min |
| 3 | **02 K-map** | Mid-term Q4 (4 marks); practice set 1 Q1, Q4 | 02 §7 don't-cares (MTE Q4) | 60 min |
| 4 | **05 MUX, DEMUX** | Mid-term Q5 (4 marks); practice set 1 Q3, Q5, Q6 | 05 n variables on a smaller MUX | 40 min |
| 5 | **06 Decoder, encoder** | Mid-term Q6 (4 marks); practice set 1 Q7, Q8 | 06 function from a decoder | 30 min |
| 6 | **09, 10 Flip-flops and waveforms** | Mid-term Q3 (2) and Q7 (4); practice set 2 Q1–Q3 | 10 the waveform procedure | 50 min |
| 7 | **16 State reduction, ASM** | Decks 12–13, worked tables | 16 partitioning | 45 min |
| 8 | **11, 12 Registers, ripple counters** | Decks 09–10 | 12 MOD-N reset | 40 min |
| 9 | **19 Memories, PLDs** | Deck 15, with PAL and PLA design examples | 19 PLA table | 40 min |
| 10 | **18 Logic families** | Deck 14 | 18 noise margin, fan-out | 35 min |
| 11 | **04 Adders, subtractors** | Deck 03; mid-term Q6 used the full adder | 04 full adder | 30 min |
| 12 | **01, 03 Boolean algebra, NAND/NOR** | Mid-term Q1 (2 marks); practice set 1 Q2 and Q1's circuit | 03 §2 (MTE Q1), §6 (map → NAND) | 60 min |
| 13 | **07, 08 Display, comparator, parity, shifter, ALU** | Mid-term Q2 (2 marks); decks 06–07 | 07 parity | 30 min |
| 14 | **14, 17 Timing; generators, asynchronous circuits** | Syllabus items with no deck coverage | 17 hazards | 40 min |
| last | **20 Mock paper** | Closed book, after the rest | all | 3 h |

Two rules for using the ranking:

- **Short on time:** do only the "Do first" column, top to bottom, then the matching mock-paper questions.
- **Stuck in 13 or 15:** both rest on 09 (the excitation tables) and 02 (K-maps). Go back one step and don't skip ahead.

## The path through this pack

The order is the syllabus, unit by unit.

**Unit 1 — combinational logic design**

[[map:01 Boolean algebra > 02 K-map > 03 NAND, NOR > 04 Adders, subtractors]]

**Unit 2 — MSI devices**

[[map:05 MUX, DEMUX > 06 Decoder, encoder > 07 Display, comparator, parity > 08 Shifter, ALU]]

**Unit 3 — sequential logic**

[[map:09 Latches, flip-flops > 10 Waveforms > 11 Registers, ring, Johnson > 12 Ripple counters > 13 Synchronous counters > 14 Timing analysis|here=5]]

**Units 4–5 — state machines, families, memories**

[[map:15 FSM design > 16 Reduction, ASM > 17 Generators, async > 18 Logic families > 19 Memories, PLDs > 20 Mock paper]]

Each file needs the ones before it. 02 is Boolean algebra drawn as a grid. 05–06 build functions from blocks instead of gates. 13 uses 09's excitation tables and 02's K-maps. 15 is 13 with an input added. 19's PLA is two levels of 01's gates, made programmable.

| File | Syllabus item | What it teaches | Real Qs |
|---|---|---|---|
| 01 | U1 | gates, Boolean laws, minterms, maxterms, Σm and ΠM | deck 01 |
| 02 | U1 | K-maps (2–5 variables), prime and essential implicants, don't-cares, POS, word problem | MTE Q4, set 1 Q1, Q4 |
| 03 | U1 | universal gates, NAND–NAND, multi-level NAND, NOR–NOR, XOR from NAND | MTE Q1, set 1 Q1–Q2 |
| 04 | U1 | half/full adder and subtractor, parallel, look-ahead, serial, BCD | deck 03 |
| 05 | U2 | multiplexer, function generation, MUX tree, demultiplexer | MTE Q5, set 1 Q3, Q5, Q6 |
| 06 | U2 | decoder, decoder-based design, encoder, priority encoder | MTE Q6, set 1 Q7–Q8 |
| 07 | U2 | 7-segment driver, multiplexed display, comparator, parity | MTE Q2, set 1 Q9–Q10 |
| 08 | U2 | logical, circular, arithmetic shifts, barrel shifter, ALU | deck 07 |
| 09 | U3 | SR latch, D latch, SR/D/JK/T flip-flops, master–slave, excitation, conversion | MTE Q3, set 2 Q1 |
| 10 | U3 | drawing flip-flop and latch waveforms | MTE Q7, set 2 Q2–Q3 |
| 11 | U3 | SISO, SIPO, PISO, PIPO, universal register, ring, Johnson | deck 09 |
| 12 | U3 | ripple up/down, MOD-N by reset, cascading | deck 10 |
| 13 | U3 | synchronous counter design with T, JK, D; MOD-N; any sequence | MTE Q8, set 2 Q4–Q6 |
| 14 | U3 | setup, hold, propagation delay, f_{max} | practice |
| 15 | U4 | Moore and Mealy, sequence detectors, state assignment | deck 11 |
| 16 | U4 | partitioning, implication tables, compatibles, ASM charts | decks 12–13 |
| 17 | U4 | skew, metastability, LFSR, pulse train, clocks, races, hazards | practice |
| 18 | U5 | noise margin, fan-out, TTL NAND, tristate, ECL, CMOS, interfacing | deck 14 |
| 19 | U5 | RAM, ROM, memory decoding, PROM, PAL, PLA | deck 15 |
| 20 | all | one closed-book paper with a key | sets 1–2, decks |

## Where the questions come from

A step opens with a **real question, quoted**, wherever the professor's material has one, tagged with its source: <span class="tag">MTE 2025 Q8</span> = the mid-term paper of 25 Sep 2025, <span class="tag">Set 2 Q5</span> = practice set 2, <span class="tag">Deck 10 slide 34</span> = a worked example on a slide. Where there is none, the step opens with a **Predict** prompt instead, or a problem tagged <span class="tag">practice</span>.

All eight mid-term questions are worked in the pack. Mid-term Q7's waveform image is missing from our copy of the paper, so 10 uses a practice waveform in the same form.

## How each file runs

| Part | What happens |
|---|---|
| **Map** | the file's steps, in order |
| **Build** | each step opens with a real question or a Predict → you guess → the answer teaches the idea → a Check |
| **Exam form** | what to reproduce in the exam: statements, procedures, equations |
| **Traps** | the mistakes that cost marks |
| **Self-test, Answers** | answers to every Check and the Self-test are on the last page(s) of each file |

:::key The one rule that makes this work
When you reach a **Guess first** box, write a guess on paper **before** reading on: one line, however wrong. A wrong guess that gets corrected sticks better than a right answer you only read.
:::

## Units and symbols used everywhere

- **A'** = NOT A (complement). **·** or nothing = AND, **+** = OR, **⊕** = XOR, **⊙** = XNOR.
- **Σm(…)** lists the rows where F = 1; **ΠM(…)** lists the rows where F = 0; **d(…)** lists don't-cares.
- **Q⁺** = Q after the clock edge. **Q0** is the least significant bit of a counter.
- K-map rows and columns run **00, 01, 11, 10**, so neighbouring cells differ in one bit.

## Where the professor's material disagrees with the pack

| Where | Slide says | Pack says | Why |
|---|---|---|---|
| Deck 01 slide 31 (01) | last term a'bc | a'bc' | the expansion of bc' gives a'bc' (row 2); a'bc is row 3, where f = 0 |
| Deck 02 slide 28 (02) | F(a, b, c) = Σm(2, 4, 5, 7) under the map | Σm(2, 3, 6, 7) | the map and slide 27 both use 2, 3, 6, 7 |
| Deck 01 slide 41 (03) | circuit output labelled Z | F | Z is already an input of the circuit |
| Deck 15 slide 28 (19) | F_{2}(A, B, C), F_{3}(A, B, C) with minterms up to 15 | functions of A, B, C, D | three variables have only minterms 0–7 |
| Deck header vs paper | ECE 2105 | ECE2102 | same syllabus; the deck code is stale |

## How this pack was checked

- Facts: the subject knowledge base (Anand Kumar, Jain, Brown & Vranesic, Mano).
- Answers: every minimised expression was compared with a computer minimiser (Quine–McCluskey) and with its truth table; every counter and sequence detector was simulated; every state reduction was redone by partitioning (the v1 `verify.py`, 192 checks, plus `src/verify.py`: 153 checks, every expression in 01–03 included).
- Where a slide has a slip, the pack uses the corrected version and says so in a Note.
