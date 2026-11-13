# exam-pack/: professor material for Digital Electronics

Course: **ECE 2105 Digital Electronics** (decks' header; the KB and 2025 paper say ECE2102, same syllabus; see `../knowledge-base/exam-map.md` §6).
These files set **scope, emphasis and question forms** only. Facts come from the prescribed textbook (honesty rule,
`../../research-engine/exam-resources.md`). Never teach a fact straight off a slide.

Decks are numbered in the professor's own order (`slides-NN-topic.pdf`). Audit trail: `../../_inbox/TRIAGE-LOG.md`.

## Index

| File | pp. | Covers | KB file |
|---|---|---|---|
| `PYQ-MTE-2025-09-25.pdf` | 2 | **The 2025 MTE paper** (30 marks, 90 min; A 3×2 / B 4×4 / C 1×8). Analysis: `../knowledge-base/exam-map.md` §1–2 | — |
| `practice-set-01-combinational.png` | 1 | 10 combinational practice Qs | 01, 02 |
| `practice-set-02-flipflops-counters.png` | 1 | 6 Qs (added 2026-11-13): D-FF from SR/JK/T + gates; D and JK latch timing (high-level, Q₀ = 1); JK negative-edge waveforms incl. CLR/PR (Q₀ = 0); 2-bit sync up counter; 2-bit sync down counter (TFF); 3-bit sync down counter (DFF) | 03 |
| `slides-01-intro-syllabus-boolean.pdf` | 47 | Intro, syllabus, Boolean algebra | 01 |
| `slides-02-kmap.pdf` | 70 | K-maps | 01 |
| `slides-03-adders.pdf` | 28 | Adders | 01, 02 |
| `slides-04-mux-demux.pdf` | 39 | MUX / DEMUX | 02 |
| `slides-05-decoder-encoder.pdf` | 48 | Decoders / encoders | 02 |
| `slides-06-comparator-parity.pdf` | 26 | Comparators, parity | 02 |
| `slides-07-shifter-alu.pdf` | 10 | Shifter, ALU | 02 |
| `slides-08-sequential-logic-flipflops.pdf` | 58 | Latches, flip-flops | 03 |
| `slides-09-registers-shift-registers.pdf` | 26 | Registers; SISO/SIPO/PIPO/PISO shift registers; ring + Johnson counters; serial addition | 03 |
| `slides-10-counters.pdf` | 37 | Asynchronous (ripple) up/down, MOD < 2ⁿ, cascading; synchronous up, up/down; designing synchronous counters with any FF | 03 |
| `slides-11-fsm-sequential-circuit-design.pdf` | 43 | Design procedure; sequence recognizer (1101): state diagram → table → state assignment (counting vs Gray) → K-maps; SR/JK/T excitation tables | 04 |
| `slides-12-state-reduction.pdf` | 27 | Equivalent states: inspection, partitioning, implication tables; incompletely specified machines: compatibles, merger diagrams, maximal compatibles | 04 |
| `slides-13-asm-charts.pdf` | 20 | ASM elements (state, decision, conditional output); worked: 1010 detector, mod-6 counter, D/JK FF, serial adder, 2-bit up and up/down counters | 04 |
| `slides-14-logic-families.pdf` | 25 | Propagation delay, rise/fall, power, noise margin, speed-power product, fan-in/out; integration levels; CMOS + TTL gates | 05 |
| `slides-15-plds.pdf` | 37 | PLD notation, SPLD/CPLD/FPGA, PROM logic design, PAL (table + fuse map), PLA | 05 |

## Still missing
- **No ETE paper** (structure `uncertain`).
- **No deck on memories** (RAM/ROM organisation). Deck 15 covers ROM only as a PLD.

## Duplicates removed
- 2026-11-13: `MTE PPR.pdf` from the zip, byte-identical to `PYQ-MTE-2025-09-25.pdf`.
- 2026-11-13: `slides-merged-01-05.pdf`, identical to decks 01–05 on all 232 pages (text, images, rendered pixels).
