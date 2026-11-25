# exam-pack/ — ECE2108 exam & course material

Material for **Computer Architecture & Processor [ECE2108]**. Routed here from `../../_inbox/` on
2026-09-12; audit trail in `../../_inbox/TRIAGE-LOG.md`.

## What's here

| File | Type | Covers |
|---|---|---|
| `HANDOUT-ECE2108-course-handout.pdf` | **course hand-out** (official, 4 pp) | whole course: verbatim syllabus, 5 COs with Bloom levels + targets, **assessment split MTE 30 / CWS 30 / ETE 40**, references, and a **36-lecture plan with the MTE divider printed after L19** |
| `slides-unit1-register-transfer-microoperations.pdf` | prof deck (33 pp) | U1 — arch vs organization, functional units, RTL, bus/memory transfers, arithmetic/logic/shift microoperations, ALSU |
| `slides-unit2-basic-computer-organization-design.pdf` | prof deck (48 pp) | U2 — Mano's Basic Computer end to end |
| `slides-unit3-parallel-processing-pipelining.pdf` | prof deck (36 pp) | U4 — parallel processing, Flynn, pipelining, hazards |
| `ASSIGNMENT-A1-ECE2108-2026-08.pdf` | **assignment** (CWS, 20 Q / 200 marks) — added 2026-09-15 | U1 + DE prerequisites + generations/types of computers + bus standards + RISC/CISC |
| `PYQ-MTE-ECE2108-2026-09.jpeg` | **the real MTE paper** (Sept 2026, 30 marks, photo of the learner's own copy) — added 2026-09-24 | U1 + U2 + U4, no U3; 5 of 7 items trace to the assignments / adjacent Mano problems (`../knowledge-base/exam-map.md` §4b) |
| `ASSIGNMENT-A2-ECE2108-2026-09.pdf` | **assignment** (CWS, 15 Q / 150 marks, due 16-09-2026) — added 2026-09-15 | U2 instruction format/bus/traces/control gates + U4 pipeline numericals; 12 of 15 are Mano ch. 5/9 end-of-chapter problems |
| `slides-unit7-8086-architecture-addressing-modes-instructions.pdf` | prof deck (85 pp., **image-only**, pages rotated 90°; titled "UNIT-1 THE 8086 MICROPROCESSORS") — added 2026-11-13 | U7: 8086 architecture, addressing modes, instruction set |
| `slides-unit7-8086-assembler-directives-and-programming.pdf` | prof deck (36 pp., text) — added 2026-11-13 | U7: directives (DB/DW/DD/DQ/DT, DUP, ASSUME, MACRO/ENDM, location counter/alignment, modular linking) + programs (direct addressing, register swap, mem↔reg transfer, 8-bit add, 16-bit sub, 8-bit mul, 16÷8 div) |

**The hand-out is the most valuable single document in the whole sem-3 batch so far** — it is the only
first-party source that fixes a marks split and an MTE/ETE boundary by direct statement rather than
inference.

## What's missing (and worth chasing)

**2026-11-25 list (learner is fetching these; the chat file waits on them):**
1. Memory organization deck incl. cache (L23–L26)
2. I/O organization deck (L20–L22)
3. RISC-V deck (L35–L36)
4. Control unit / microprogrammed control deck (L12–L15)
5. Possibly an 8086 loops / conditional-jump programming deck (CO5; the programming deck has only transfer/arithmetic programs)
6. Assignment 3+ (if any)
7. Quiz papers (CWS)
8. Any ETE model paper / question bank / "important questions"

*Older notes:*

Ranked by value to exam performance — see `../knowledge-base/exam-map.md` §5:

1. **ETE-style evidence.** The MTE paper arrived 2026-09-24; no ETE paper can exist for this first
   batch, so CWS quizzes / any ETE practice set for U5–U8 are now the most valuable things to chase.
2. *(2026-11-13: the two **8086** decks arrived, see the table. Still missing: control unit, I/O, memory, RISC-V.)* **Decks for L12–L36** — i.e. everything from microprogrammed control onward: control unit design,
   program control, I/O organization, memory organization, **the 8086** (8 lectures, the highest-value
   unit), and RISC-V. Those units were built textbook-primary.
3. **What CWS actually consists of** — 30 marks, composition unspecified in the hand-out.
4. **MTE / ETE dates** — drives the review taper (`../../research-engine/exam-calendar.md`).

## Honesty rule (`../../research-engine/exam-resources.md`)

These files tell us **what is tested and how** — trust them for scope, emphasis and framing. They do
**not** set facts; content correctness comes from the prescribed textbooks.

**This is not a formality here — two real errors were caught in this very folder:**
- the Unit-2 deck prints ISZ's third microoperation as `D₆T₄`; it must be **`D₆T₆`** (contradicted by
  the same deck's own "Complete Computer Description" slide);
- the Unit-1 deck's comparison table contains a muddled row ("Architecture indicates its hardware,
  Organization indicates its performance").

Both are logged in `../knowledge-base/CHANGELOG.md` and kept as `misconceptions.md` M9 and M1.

## Note on the course code

ECE2108 does **not** appear in the MUJ *2023-onwards* ECE curriculum that seeded this batch; it **does**
appear in the **2025-2026 onwards** scheme, Third Semester, 3 credits. The learner is on the newer
scheme. See `../knowledge-base/CHANGELOG.md` and `../../research-engine/research-queue.md`.
