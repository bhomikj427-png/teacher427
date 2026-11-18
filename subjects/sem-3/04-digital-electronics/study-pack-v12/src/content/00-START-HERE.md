# Digital Electronics — Study Pack (ETE)

<div class="sub">ECE2102 (ECE 2105 on the decks) · B.Tech ECE Sem 3 · all 5 units of the syllabus on slide 2 of the professor's first deck · built from the 2025 mid-term paper, decks 01–15 and two practice sets · every answer checked by computer</div>

## Priority order: if time is short, study in this order

Ranked by the professor's own material: the 2025 mid-term paper (30 marks: 2-mark recall, 4-mark method, one 8-mark design), the two practice sets, and the decks. There is **no end-term paper yet**, so this is an estimate. The mid-term covered Units 1–3 up to counters; the end-term covers all five units, so Units 3–5 weigh more than the mid-term suggests.

| Rank | Study | Why it ranks here | Do first | Rough time |
|---|---|---|---|---|
| 1 | **13 Synchronous counters** | The mid-term's only 8-mark question; practice set 2 Q4–Q6; deck 10 | 13 steps 6–7 (MTE Q8) | 75 min |
| 2 | **15 FSM design** | Deck 11, with five practice detectors on its last slide; Unit 4 is not yet examined | 15 steps 2–7 (the 1101 detector, word to circuit) | 75 min |
| 3 | **02 K-map** | Mid-term Q4 (4 marks); practice set 1 Q1, Q4 | 02 §7 don't-cares (MTE Q4) | 60 min |
| 4 | **05 MUX, DEMUX** | Mid-term Q5 (4 marks); practice set 1 Q3, Q5, Q6 | 05 steps 4–6 (n variables on a smaller MUX, MTE Q5) | 50 min |
| 5 | **06 Decoder, encoder** | Mid-term Q6 (4 marks); practice set 1 Q7, Q8 | 06 steps 5–7 (decoder + OR, MTE Q6 full adder) | 45 min |
| 6 | **09, 10 Flip-flops and waveforms** | Mid-term Q3 (2) and Q7 (4); practice set 2 Q1–Q3 | 10 the waveform procedure | 50 min |
| 7 | **16 State reduction, ASM** | Decks 12–13, worked tables | 16 steps 3–5 (partitioning, implication table) | 60 min |
| 8 | **11, 12 Registers, ripple counters** | Decks 09–10 | 11 steps 6–7 (ring, Johnson), 12 steps 6–7 (MOD-N by reset) | 60 min |
| 9 | **19 Memories, PLDs** | Deck 15, with PAL and PLA design examples | 19 steps 9 and 11 (PAL with feedback, PLA table), step 4 (memory expansion) | 55 min |
| 10 | **18 Logic families** | Deck 14 | 18 steps 4 and 6 (noise margin, fan-out), step 14 (TTL–CMOS interfacing) | 55 min |
| 11 | **04 Adders, subtractors** | Deck 03; mid-term Q6 used the full adder | 04 steps 2–5 (full adder, ripple adder), step 12 (2's-complement subtract) | 50 min |
| 12 | **01, 03 Boolean algebra, NAND/NOR** | Mid-term Q1 (2 marks); practice set 1 Q2 and Q1's circuit | 03 §2 (MTE Q1), §6 (map → NAND) | 60 min |
| 13 | **07, 08 Display, comparator, parity, shifter, ALU** | Mid-term Q2 (2 marks); practice set 1 Q9, Q10; decks 05–07 | 07 steps 9–11 (parity, MTE Q2), steps 2–3 (common-anode segments), 08 steps 6–8 (ALU) | 70 min |
| 14 | **14, 17 Timing; generators, asynchronous circuits** | Syllabus items with no deck coverage | 14 steps 5–6 (f_{max}, hold check), 17 steps 12–13 (hazards, EC6302) and 4 (LFSR trace) | 60 min |
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
| 07 | U2 | BCD to 7-segment decoder (common cathode and anode), multiplexed display, 1-, 2- and n-bit comparator, cascading, parity generator (chain, tree) and checker | MTE Q2, set 1 Q9–Q10 |
| 08 | U2 | logical, circular, arithmetic shifts, barrel shifter, ALU | deck 07 |
| 09 | U3 | SR latch, D latch, SR/D/JK/T flip-flops, master–slave, excitation, conversion | MTE Q3, set 2 Q1 |
| 10 | U3 | drawing flip-flop and latch waveforms | MTE Q7, set 2 Q2–Q3 |
| 11 | U3 | register, SISO delay, SIPO, PISO (SHIFT/LOAD'), universal 74194, ring, Johnson, lock-out, XOR feedback, serial adder | deck 09 slides 1–26 |
| 12 | U3 | ripple up and down counters, frequency division, ripple delay, MOD-N by reset, decade, cascading | deck 10 slide 14 |
| 13 | U3 | synchronous counter design with D, T, JK; down; decade; unused states; up/down; Gray | MTE Q8, set 2 Q4–Q6 |
| 14 | U3 | clock-to-Q delay, setup, hold, metastability, f_{max} (longest path), hold check (shortest path), clock skew, ripple vs synchronous counters | KB 03 (no deck) |
| 15 | U4 | states as memory, sequence detectors (overlap or not), state table, assignment (counting, Gray), D/T/JK circuits, Mealy vs Moore, wildcard detectors | deck 11 slides 4–43 |
| 16 | U4 | equivalent states, inspection, partitioning (Moore, Mealy), implication tables, compatibles and closed covers, ASM charts, serial adder | decks 12–13 |
| 17 | U4 | decoding glitches, metastability and the synchronizer, debouncing, LFSR (lock-out, taps), pulse trains, clock division, 555 astable/monostable, ring oscillator, flow tables, races and state assignment, static hazards, hazard-free design | practice; EC6302 Nov 2021 Q15(b) |
| 18 | U5 | t_{PLH}/t_{PHL}, rise/fall, power, noise margin, PDP, fan-out, CMOS inverter/NAND/NOR, TTL NAND, totem pole and open collector, tristate bus, ECL, families compared, interfacing | deck 14 slides 4–25, deck 05 slides 44–48 |
| 19 | U5 | 2^{k} × m organisation, SRAM/DRAM, ROM types, memory expansion, AND–OR array, ROM as a table, PROM design, PAL (feedback), PLA (output XOR, shared terms), PROM/PAL/PLA compared | deck 15 slides 2–37 |
| 20 | all | one closed-book paper with a key | sets 1–2, decks |

## Where the questions come from

A step opens with a **real question, quoted**, wherever the professor's material has one, tagged with its source: <span class="tag">MTE 2025 Q8</span> = the mid-term paper of 25 Sep 2025, <span class="tag">Set 2 Q5</span> = practice set 2, <span class="tag">Deck 10 slide 34</span> = a worked example on a slide. Where there is none, the step opens with a **Predict** prompt instead, or a problem tagged <span class="tag">practice</span>.

All eight mid-term questions are worked in the pack. Mid-term Q7's waveform is redrawn from the paper in 10 step 2 and worked in step 3.

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
| Deck 04 slide 7 (05) | 2:1 MUX K-map with 1s in cells 2, 3, 5, 7 | 1s at rows 1, 3, 6, 7 | slide 6's table and O = S'D0 + SD1 both give 1, 3, 6, 7 |
| Deck 05 slide 18 (06) | block wires A0 = Y, A1 = X; table names inputs A, B | A most significant | the table's order; with the slide's wiring the OR gives Y' |
| Deck 05 slide 39 (06) | valid bit named d | V | slides 40–43 call it V |
| Deck 01 slide 41 (03) | circuit output labelled Z | F | Z is already an input of the circuit |
| Deck 15 slide 28 (19) | F_{2}(A, B, C), F_{3}(A, B, C) with minterms up to 15 | functions of A, B, C, D | three variables have only minterms 0–7 |
| Deck 10 slide 6 (12) | "3-bit down counter" clocked from Q0, Q1 (negative edge) | clock from Q0', Q1' | negative-edge stages clocked from Q count up; slide 15 has the right circuit |
| Deck 10 slides 12–13 (12) | flip-flops D, C, B, A with D the LSB; slide 12's NAND wire runs over D | Q0–Q3, NAND on Q3, Q1 | same circuit, usual bit order; slide 13 draws the wire from C |
| Deck 11 slide 27 (15) | "Overlapping" panel for 110 left empty | same diagram as non-overlapping | no tail of 110 ("0", "10") begins 110 |
| Deck 13 slide 8 (16) | D0 = X(y0)', D1 = X'm1 + Xm2 | D0 = X, D1 = X'm1 + Xm2 + X'm3 | the chart has more paths into y0 = 1 and into S2; checked by simulation |
| Deck 13 slide 9 (16) | D0 = X[Σm(0, 2, 4)] + d(6, 7) (no hold terms) | D0 = X ⊕ y0 | with X = 0 the counter must hold, not fall to 000 |
| Deck 13 slide 18 (16) | decision box on E after S3, both exits to S0 | box left out | a decision with one outcome decides nothing |
| Deck 06 slide 5 (07) | G = A&gt;B: A1B1' + … (colon) | G = A_{1}B_{1}' + … | the colon stands for "=" |
| Deck 06 slide 14 (07) | P = X ⊕ Y ⊕ Z is "a 3-input even function" | an odd function | slide 18: an odd function's 1s are the inputs with an odd number of 1s; slide 22 agrees |
| Deck 07 slide 8 (08) | titled "1-bit ALU design" | 1-bit logic unit | the circuit has no adder; slides 9–10 add the arithmetic half |
| Deck 09 slide 2 (11) | "Simple registers": a new 4-bit data loaded every clock | the drawing is a shift register: 4 clocks for 4 bits | a parallel register (slides 3–4) loads in one clock |
| Deck 09 slide 13 (11) | parallel-in parallel-out listed as a shift register | a plain register | no wire runs from one stage to the next |
| Deck 09 slide 15 (11) | callout SHIFT·Q₀ + SHIFT'·D₁ pointing at stage 2 | SHIFT·Q₁ + SHIFT'·D₂ at stage 2 | the callout is stage 1's expression |
| Deck 09 slide 17 (11) | loop 0001 → 0010 → 0100 → 1000, timing diagram shifts Q_{A} → Q_{D} | 1000 → 0100 → 0010 → 0001 (Q_{0} first) | same counter, opposite bit order; slide 18 agrees |
| Deck 14 slide 21 (18) | TTL "typical noise immunity about 1–1.6 V" | NM = 0.4 V both ways | that range uses typical output levels (3.4 V, 0.2 V); exam answers use the guaranteed SN7400 levels |
| Deck 14 slides 14, 20 (18) | CMOS supply "3–15 V" and "5–15 V" | 74HC: 2–6 V | the slide ranges fit the older 4000 series; the two slides also disagree |
| Deck 15 slide 21 (19) | input 011 gives output 0011 | 0000 | D_{3} carries no × in the slide's array; 0011 is the word at 001 |
| Deck 15 slide 24 (19) | "4-input, 3-output PAL" | four outputs | the circuit and equations have F_{1}–F_{4} |
| Deck header vs paper | ECE 2105 | ECE2102 | same syllabus; the deck code is stale |

## How this pack was checked

- Facts: the subject knowledge base (Anand Kumar, Jain, Brown & Vranesic, Mano); device numbers in 18 from the TI SN7400 and SN74HC00 data sheets; the 555 formulas in 17 from the TI NE555 data sheet.
- Answers: every minimised expression was compared with a computer minimiser (Quine–McCluskey) and with its truth table; every counter and sequence detector was simulated; every state reduction was redone by partitioning (the v1 `verify.py`, 192 checks, plus `src/verify.py`: 746 checks: every expression in 01–03; every delay, noise margin, power, PDP, fan-out and interfacing number in 18, with the CMOS and TTL gates checked at switch level; every memory size, ROM word and PROM/PAL/PLA expression in 19, with a search showing its PLA line counts are the minimum; every adder, subtractor, BCD adder, shift, barrel shifter and ALU operation in 04 and 08 evaluated on all inputs; every segment, comparator and parity expression in 07 checked on every input row (two cascaded comparators on all 65 536 pairs of 8-bit numbers); every MUX data list, decoder circuit and encoder equation in 05–06 evaluated on every input row; every latch/flip-flop table, conversion and waveform answer in 09–10; every counter sequence, excitation equation and unused-state path in 12–13 simulated; every shift-register trace, ring and Johnson sequence (with the unused-state loops), XOR-feedback register and serial addition in 11 simulated; every timing sum in 14 recomputed; every detector in 15 simulated against a reference on all inputs up to 9 bits; every partition, implication table and closed cover in 16 recomputed; every glitch path, LFSR cycle (every start, every tap choice), pulse-train and divider count, 555 and ring-oscillator number, flow table, race and hazard cover in 17 checked by enumeration).
- Where a slide has a slip, the pack uses the corrected version and says so in a Note.
