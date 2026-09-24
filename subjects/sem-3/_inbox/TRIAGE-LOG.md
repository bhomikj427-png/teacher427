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

- `[2026-09-15]` `A1. ECE2108-CAP - Assignment 1 v2.pdf` → `11-computer-architecture-and-processor/exam-pack/ASSIGNMENT-A1-ECE2108-2026-08.pdf` — **ASSIGNMENT** (CWS) — Assignment 1, 20 Q, 200 marks, due 18-08-2026 extended to 24-08-2026; "one mark = 20 words". Covers U1 end-to-end + DE prerequisites (flip-flop, decoder, MUX, registers, shift register) + generations/types of computers + bus standards + RISC/CISC. **First professor-set question evidence for ECE2108.**
- `[2026-09-15]` `2. ECE2108 Assignment 2.pdf` → `.../exam-pack/ASSIGNMENT-A2-ECE2108-2026-09.pdf` — **ASSIGNMENT** (CWS) — Assignment 2, 15 Q, 150 marks, due 16-09-2026 16:30. Covers U2 (instruction format, bus control, CLA/ADD-indirect traces, 3-word fetch, JK control gates, PC control gates) + U4 (pipeline register table, k+n−1, speedup numerical, branch-handling hardware, FI-DA-FO-EX step). **12 of 15 items are verbatim Mano 3e end-of-chapter problems** (ch. 5 and ch. 9) — signals the professor draws exam-style items from Mano's exercises.

### Findings raised by this batch
- **ALSU select codes:** the professor's ALSU slide (deck 1 p. 32) uses Mano Table 4-8's ordering, which differs from the arithmetic-circuit table on deck 1 p. 25. The KB and study-pack v1 had used the p. 25 ordering for the ALSU — corrected 2026-09-15.
- **A2 Q5 `C₇T₃`** is not a BC signal name; most likely `D₇T₃`. `uncertain`.

- `[2026-09-24]` `WhatsApp Image 2026-09-23 at 11.46.47 AM.jpeg` → `11-computer-architecture-and-processor/exam-pack/PYQ-MTE-ECE2108-2026-09.jpeg` — **PYQ** — the learner's own **ECE2108 Odd-Sem MTE, Sept 2026** (photo), 30 marks / 1.5 h, A (2+2+3) / B (3×5) / C (1×8). **First ECE2108 exam paper.** 5 of 7 items trace to the assignments or the Mano problem next to one. No U3 question. Analysis: `exam-map.md` §4b. Contains the learner's name + reg. no. (private repo).
- `[2026-09-24]` `1.pptx` → `12-data-structures-and-algorithms/exam-pack/slides-01-cpp-overview.pptx` — PPT — header "Data Structure and Algorithms, **ECE/VDT 2104**". **Triggered creation of `12-data-structures-and-algorithms/`** (same precedent as ECE2108: in the learner's 2025-26 scheme, absent from the seeded 2023 scheme).
- `[2026-09-24]` `2.pptx` → `.../exam-pack/slides-02-cpp-basic-terms-operations.pptx` — PPT — C++ paradigm, C++ vs C abstractions.
- `[2026-09-24]` `3.pptx` → `.../exam-pack/slides-03-conditionals-loops-functions.pptx` — PPT — if/else, loops, functions + 6 beyond-class programs.
- `[2026-09-24]` `4.pptx` → `.../exam-pack/slides-04-class-objects-access-specifiers.pptx` — PPT — classes/objects/access specifiers + 5 programs.
- `[2026-09-24]` `5.pptx` → `.../exam-pack/slides-05-class-constructor-destructor.pptx` — PPT — constructors/destructors + 10 short-answer Qs.
- `[2026-09-24]` `6.pptx` → `.../exam-pack/slides-06-arrays.pptx` — PPT — linear arrays, memory representation, traversal, insert/delete.
- `[2026-09-24]` `7.pptx` → `.../exam-pack/slides-07-stack.pptx` — PPT — stack ADT, PUSH/POP algorithms, expression notations.
- `[2026-09-24]` `8.pptx` → `.../exam-pack/slides-08-queue-pointers.pptx` — PPT — queue, circular queue, pointers + 6 activity items.
- `[2026-09-24]` `9.pptx` → `.../exam-pack/slides-08-queue-pointers-COPY.pptx` — PPT — **duplicate of 8.pptx** (identical slide text, 27 slides, 101-byte size difference = metadata). Kept, not deleted. Safe to remove.
- `[2026-09-24]` `DSA Assignment.pdf` (arrived during this sort) → `12-data-structures-and-algorithms/exam-pack/ASSIGNMENT-A1-ECE2104-2026-08.pdf` — **ASSIGNMENT** (CWS) — Assignment 1, 50 marks, due 27-08-2026, 23 Q (A 9×1 / B 5×2 / C 5×3 / D 4×4). Covers **linked lists**, which no deck covers.

### Open questions raised by this batch
- **ECE2104 has no hand-out yet**, so no syllabus, prescribed textbook, marks split or MTE/ETE boundary. Decks cite Kanetkar, *Data Structures Through C++* (BPB 2023), and Shukla (Wiley). Neither is confirmed as the prescribed text.
- **ECE2104 is registered but not researched.** Research waits on the learner confirming the batch re-map (`../research-engine/research-queue.md`).
- **The MTE window has passed** for at least ECE2108 (sat on or before 2026-09-23). Recorded in `../research-engine/exam-calendar.md`.
