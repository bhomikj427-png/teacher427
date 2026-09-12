# ECE2108 — Computer Architecture & Processor — course info

> Official anchor for research scope. Unlike every other subject in this batch, the scope here comes
> from the **professor's own course hand-out** (`exam-pack/HANDOUT-ECE2108-course-handout.pdf`), not
> from the university scheme PDF — so syllabus, assessment split, reference list and **lecture-level
> sequencing** are all `settled` first-party evidence.
>
> **This file describes the course, never the research status.** Live status → the queue:
> `../research-engine/research-queue.md`.

- **Course name:** Computer Architecture & Processor  ·  **Code:** ECE2108
- **L-T-P-C:** 3-0-0-3  ·  Class: 3rd Sem (2nd Yr), B.Tech ECE, MUJ
- **Course Coordinator:** Dr Rohit Mathur  ·  **Instructors:** Dr Manish Tiwari & Dr Rohit Mathur
- **Additional practitioners:** industry sessions (eInfochip / SoCTEAMUP / TrueChip / VLSI System
  Design) — the handout marks **L16 Parallel Processing, L17 Pipelining, L26 Cache Memory, L36
  RISC-V architecture** with `*` as practitioner-delivered.
- **Session printed on the handout:** "July-Dec 2027" — **`likely` stale template text.** The unit
  decks carry machine footers dated **8/6/2026**, so the live run is **Jul–Dec 2026**. Filename says
  "Jan 2027". Three dates, no two agreeing; the slide footer is the only machine-stamped one.

## Assessment split — `settled` (verbatim from the hand-out, §E)

| Component | Description | Marks |
|---|---|---|
| Internal (summative) | **Mid-Term Examination** (closed book) | **30** |
| Internal (summative) | **CWS** — (Quiz + Assignments) / (Research + Presentation) | **30** |
| End Term (summative) | **End Term Exam** (closed book) | **40** |
| | **Total** | **100** |

This is the **first verified MUJ marks split in the entire batch** — `exam-resources.md` had it
flagged `uncertain` batch-wide. It is verified **for ECE2108 only**; do not generalize to other
courses without their own handouts.

## Official syllabus (verbatim, hand-out §F)

> Computer Architecture: Introduction, computer types, functional units, Von Neumann and Harvard
> architectures, RISC and CISC Architectures. Register Transfer and Microoperations, Design of Basic
> Computer, Design of Accumulator Logic, Control unit design, Microprogrammed Control, Parallel
> Processing, Pipelining, Input-Output Organization, Memory Organization. 8086 Microprocessor: 8086
> Architecture, 8086 Instruction Set: types of instructions and addressing modes, assembler and
> assembler directives, assembly language programming. RISC V: Introduction to the Reduced
> Instruction Set Computer, RISC V architecture and features.

## Course Outcomes (verbatim, hand-out §C)

| CO | Statement | Bloom | Target |
|---|---|---|---|
| CO1 | Demonstrate understanding of Register Transfer and Microoperations | L2 | 75% / L2 |
| CO2 | Demonstrate understanding of control unit and its subsystem design | L2 | 75% / L2 |
| CO3 | Explain concepts and impact of cache memory, pipelining and parallel processing on system performance | L2 | 75% / L2 |
| CO4 | Explain the operation of various addressing modes of 8086 microprocessor | L2 | **85% / L3** |
| CO5 | Develop Logical and Conditional assembly language programming skills for 8086 microprocessor | **L3** | 75% / L2 |

**CO4/CO5 carry the highest target and the only L3 verb ("Develop").** 8086 addressing modes +
assembly programming are where the course expects the most, and they are **ETE-only**.

## Prescribed textbooks (hand-out §F references, + the decks' own list)

1. **M. M. Mano, *Computer System Architecture*, Pearson, 3e, 2007.** — the spine. The decks say
   "Ref: M. M. Mano" on the syllabus slide and reproduce his Basic Computer verbatim. **Tier-1 truth
   for units 1–6.**
2. **K. M. Bhurchandi & A. K. Ray, *Advanced Microprocessors and Peripheral Devices*, McGraw-Hill,
   3e, 2018.** — the decks name it as the 8086 reference. **Tier-1 truth for unit 7.**
3. **D. A. Patterson & J. L. Hennessy, *Computer Organization and Design: The Hardware/Software
   Interface — RISC-V Edition*, Morgan Kaufmann, 2018.** — named as the RISC-V reference.
   **Tier-1 truth for unit 8.**
4. V. C. Hamacher, Z. Vranesic & S. Zaky, *Computer Organization*, McGraw-Hill, 5e, 2002. — the
   functional-units / I-O framing in deck 1 is Hamacher's, not Mano's.
5. J. P. Hayes, *Computer Architecture and Organization*, TMH, 3e, 1998.
6. *(decks only, not in the handout)* Sonal Yadav, *Computer System Organization*, AICTE, 1e, 2024.

**Per-unit truth authority is split three ways** (Mano → Bhurchandi/Ray → Patterson/Hennessy). That
is unusual for this batch and is recorded in `knowledge-base/sources.md`.

## Material in hand (`exam-pack/`)

| File | What it is | Covers |
|---|---|---|
| `HANDOUT-ECE2108-course-handout.pdf` | official course hand-out, 4 pp | whole course: syllabus, COs, marks, 36-lecture plan |
| `slides-unit1-…pdf` | prof deck, 33 pp | U1 (arch vs org, functional units, RTL, bus/memory, micro-ops, ALSU) |
| `slides-unit2-…pdf` | prof deck, 48 pp | U2 (Mano's Basic Computer, end to end) |
| `slides-unit3-…pdf` | prof deck, 36 pp | U4 (parallel processing, pipelining, hazards) |

**No deck** for control-unit/microprogrammed control (L12–L15) or for any ETE unit (I/O org, memory
org, 8086, RISC-V). **No PYQ** — neither MTE nor ETE.

## Source

- Professor's course hand-out, dropped by the learner 2026-09-12 via `../_inbox/`; routed and logged
  in `../_inbox/TRIAGE-LOG.md`.
- ⚠ **ECE2108 does not appear in the MUJ "2023 onwards" ECE scheme PDF** that seeded this batch
  (`../README.md`). The handout is first-party and wins for this course's existence and content; the
  registry discrepancy is an open question for the learner (see `../README.md` note).
