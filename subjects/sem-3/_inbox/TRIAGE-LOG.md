# Inbox triage log (append-only)

> One line per file routed out of `_inbox/`. Never edited, only appended — the audit trail of what
> went where (mirrors the system's live-logging / no-drift discipline).
>
> Format: `[YYYY-MM-DD] <original filename> → <NN-subject>/exam-pack/<new name> — <type> — <note>`
> Unclassifiable: `[YYYY-MM-DD] <filename> → _unsorted/ — UNSURE — <why; what you need to confirm>`

## Routings

- `[2026-09-11]` `1_Digital Logic.ppt.pdf` → `04-digital-electronics/exam-pack/slides-01-intro-syllabus-boolean.pdf` — PPT — prof deck 1; carries the **full course syllabus verbatim** (5 topic blocks). Header code reads **ECE 2105**, not ECE2102 — flagged.
- `[2026-09-11]` `2_K-MAP.pdf` → `.../exam-pack/slides-02-kmap.pdf` — PPT — deck 2, K-map minimization (MSP/MPS).
- `[2026-09-11]` `3_Adders.pdf` → `.../exam-pack/slides-03-adders.pdf` — PPT — deck 3, combinational logic + adders.
- `[2026-09-11]` `4_MUX_Demux.pdf` → `.../exam-pack/slides-04-mux-demux.pdf` — PPT — deck 4, multiplexer/demultiplexer.
- `[2026-09-11]` `5_Decoder_Encoder.pdf` → `.../exam-pack/slides-05-decoder-encoder.pdf` — PPT — deck 5, decoders/encoders.
- `[2026-09-11]` `6_Comparator_parity.pdf` → `.../exam-pack/slides-06-comparator-parity.pdf` — PPT — deck 6, magnitude comparator + parity.
- `[2026-09-11]` `7_Shifter_ALU.pdf` → `.../exam-pack/slides-07-shifter-alu.pdf` — PPT — deck 7, shift microoperations/barrel shifter + ALU.
- `[2026-09-11]` `8_Sequential_logic & flip flop.pdf` → `.../exam-pack/slides-08-sequential-logic-flipflops.pdf` — PPT — deck 8, sequential circuits + flip-flops.
- `[2026-09-11]` `Merged from 1_Digital Logic.ppt.pdf` → `.../exam-pack/slides-merged-01-05.pdf` — PPT — **partial merge of decks 1–5 only** (verified: no comparator/shifter/sequential content). Redundant with the individual decks; kept as a convenience copy, individual decks are canonical.
- `[2026-09-11]` `MTE PPR.pdf` → `.../exam-pack/PYQ-MTE-2025-09-25.pdf` — **PYQ** — MUJ Odd-Sem **Mid Term Exam, 25-Sep-2025**, Digital Electronics [ECE2102], 30 marks / 90 min, Sections A(3×2) / B(4×4) / C(1×8). **First real MUJ evidence in the whole batch** — resolves the MTE structure + MTE-vs-ETE scope question for this subject.
- `[2026-09-11]` `Practice questions set 1.png` → `.../exam-pack/practice-set-01-combinational.png` — practice set — 10 questions, all combinational (K-map w/ don't-cares → universal gates, MUX implementation, decoder implementation, parity generator, BCD→7-segment). Image, text-legible.

### Open question raised by this batch
- **Course code mismatch** — prof slide deck 1 header says `Digital Electronics ECE 2105`; the MTE
  paper and the KB/queue say `ECE2102`. Syllabus text matches the ECE2102 syllabus. Working
  assumption: stale code on a reused deck. `uncertain` — learner to confirm the code on their
  registration/handout.

- `[2026-09-12]` `3rd_sem_ECE2108_CPA_Course_Handout_Jan_2027.pdf` → `11-computer-architecture-and-processor/exam-pack/HANDOUT-ECE2108-course-handout.pdf` — **HANDOUT** — official MUJ ECE Course Hand-out, **Computer Architecture & Processor [ECE2108]**, L-T-P-C 3-0-0-3. **Triggered creation of a new subject folder** (`11-…`): ECE2108 was absent from the sem-3 registry, which was seeded from the 2023-onwards scheme PDF. Carries syllabus verbatim, 5 references, 5 COs, the assessment split (MTE 30 / CWS 30 / ETE 40) and a **36-lecture plan with the MTE divider explicitly printed after L19** — the richest scope evidence in the batch to date.
- `[2026-09-12]` `Unit 1. Register Transfer and Microoperations.pdf` → `.../exam-pack/slides-unit1-register-transfer-microoperations.pdf` — PPT — prof deck, Unit 1 (33 pp). Curated by Dr. Rohit Mathur. Arch-vs-organization, functional units, RTL, bus/memory transfers, arithmetic/logic/shift microoperations, ALSU. Slide footer dates read **8/6/2026** → real session is **Jul–Dec 2026**, not the handout's "July-Dec 2027".
- `[2026-09-12]` `Unit 2. Basic Computer Organization & Design.pdf` → `.../exam-pack/slides-unit2-basic-computer-organization-design.pdf` — PPT — prof deck, Unit 2 (48 pp). Mano's Basic Computer end-to-end: instruction codes, BC registers, common bus, instruction set, timing/control, instruction cycle, MRI, I/O & interrupt, complete computer description, design of BC + accumulator logic.
- `[2026-09-12]` `Unit 3. Parallel Processing & Pipelining.pdf` → `.../exam-pack/slides-unit3-parallel-processing-pipelining.pdf` — PPT — prof deck, Unit 3 (36 pp). Throughput, Flynn's taxonomy, SISD/SIMD/MISD/MIMD, shared-memory vs message-passing, pipeline speedup, instruction pipeline, the three hazard classes + cures.

### Open questions raised by this batch
- **ECE2108 is missing from the sem-3 scheme table** (`../README.md`), which was pulled from the
  *2023-onwards* curriculum PDF on 2026-06-16. The learner reports the reverse too — subjects listed
  there that they are **not** enrolled in. Working hypothesis: the learner's batch follows a **later
  scheme revision** than the one seeded. `uncertain` — needs the learner's own registration list or
  the current scheme PDF to reconcile. Folder numbered `11-` (append order), **not** a scheme position.
- **Session/year mismatch inside the handout itself** — header says `Session: July-Dec 2027`, filename
  says `Jan_2027`, slide footers say `8/6/2026`. Slide footers are machine-stamped and win: the live
  session is **Jul–Dec 2026**. Handout header treated as stale template text (`likely`).
- **No deck yet for L12–L15** (microprogrammed control, control memory, control unit design, program
  control) **or for anything post-MTE** (I/O organization, memory organization, 8086, RISC-V). Those
  units are researched **textbook + NPTEL-primary** per the protocol, not deck-driven.
- **No PYQ for this subject** — neither MTE nor ETE. Exam *structure* comes from the handout's marks
  table; question *forms* are `uncertain` until a paper arrives.
