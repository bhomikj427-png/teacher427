# ECE2104 Data Structures and Algorithms — Progress Log

> Written **live** (log-first artifact pairing; never reconstructed at wrap-up). Session-resume block
> is overwritten each session-end; Session history is append-only. See `../README.md`.

## Session resume
- Last session: 2026-09-24 (no teaching).
- Status: **folder created by inbox triage only — no knowledge base, below `stage-1`.** Not teachable
  (teaching gate: `stage-2✓`). Research has **not** been started; it waits on the batch re-map the
  learner has to confirm (`../research-engine/research-queue.md`, scheme-revision section).
- Where we stopped: `study-pack/` built for the MTE (2026-09-24). No teaching or mastery yet.
- Next up: learner decides whether to activate ECE2104 for research. When it is activated, the 8 prof
  decks in `exam-pack/` set **scope and emphasis** (C++ → OOP → arrays → stack → queue/pointers);
  facts come from the prescribed textbook, never the slides.
- Due for review today: nothing.
- ⚠ **[2026-09-24] Learner-decided gate exception (MTE in ~2 h):** "do not research data structures, just
  go off of slides and assignment; make me a study pack around answering assignment questions."
  The `stage-2✓` gate is not met and is **not** being met. Logged as a subject-scoped exception, like
  MoT's. Scope per the learner: **up to "types of trees"** (professor said "till red-black tree", learner
  reads that as tree types). The hand-out prints the MTE divider after L16 (recursion), so trees are
  beyond the printed boundary. Covered anyway, briefly. Accuracy guard: standard textbook DSA content
  only, every program compiled and run before inclusion.

## Mastery ledger
*(empty)*

## Spaced-review / relearning queue
*(empty)*

## Session history
- [2026-09-24] **Folder created by `_inbox/` triage**: 9 `.pptx` decks arrived, all headed "Data
  Structure and Algorithms, ECE2104" (deck 1: "ECE/VDT 2104"). ECE2104 had no folder: it is in the
  learner's 2025-26 scheme but absent from the 2023 scheme that seeded the batch. Same precedent as
  ECE2108 (2026-09-12). Numbered `12-` (append order, not scheme position). Decks 8 and 9 have
  **identical slide text** (27 slides each, files differ by 101 bytes). Both kept, 9 filed as a copy.
  Reference cited on every deck: **Yashavant Kanetkar, *Data Structures Through C++*, BPB, 2023**. Deck 8
  adds **Rajesh K. Shukla, *Data Structures using C & C++*, Wiley**. Prescribed textbook still
  unconfirmed (no handout). No teaching event.
- [2026-09-24] **Assignment 1 arrived mid-triage** (`DSA Assignment.pdf`, dropped into `_inbox/` during
  this sort) → `exam-pack/ASSIGNMENT-A1-ECE2104-2026-08.pdf`. 50 marks, due 27-08-2026, 23 Q in 4 sections:
  A 9×1 · B 5×2 · C 5×3 · D 4×4. **First professor-set question evidence for ECE2104.** It includes
  **singly linked lists** (B1, C5, D2 sort-by-swapping-data), and none of the 8 decks covers them, so
  course scope goes beyond the decks. Also: infix→postfix with stack trace (B3, D3), postfix
  evaluation `12 3 4 * + 6 2 / -` (C4), a stack overflow/underflow trace (C1), a DS-selection
  justification (C2), and a C++ output question about an octal literal (A7, `021377`). Bloom verbs
  in the questions (Apply/Analyze) suggest CO-tagged items. No teaching event.
- [2026-09-24] **Course hand-out arrived** (`Course Handout ECE2104VDT2104_26.pdf`) →
  `exam-pack/HANDOUT-ECE2104-course-handout.pdf`. Session July–Nov 2026. Coordinator Dr. Kamal Kishor
  Upadhyay. Assessment MTE 30 / CWS 30 (quiz, MOOC, assignment) / ETE 40. 5 COs. **Prescribed
  textbook [1] = Kanetkar, *Data Structures Through C++*** (matches the decks). Lecture plan prints
  **MID SEMESTER EXAMINATION after L16 (recursion)**: MTE = C++ intro, DS memory representation,
  linked lists, stack, queue, circular queue, recursion.
- [2026-09-24] Learner request: **MTE study pack in ~2 h, built around answering Assignment 1**, shaped
  like ECE2108 study-pack-v3 but more informative. Building `study-pack/`.
- [2026-09-24] `study-pack/` **built — 8 files, 00–07**, question-first, every A1 question (23/23) answered
  in place: 00 start-here + A1→file map + 2-h plan · 01 C++/OOP (A2–A5, A7, A9, B2, C3, D1) · 02 arrays
  (A1, A8, B4) · 03 linked list (B1, C5, D2) · 04 stack (B3, B5, C1, C4, D3) · 05 queue + DS choice
  (A6, C2, D4) · 06 recursion + tree terminology/types incl. AVL, Red-Black 5 properties, heap, bonus
  traversals · 07 mock MTE in the ECE2108 MTE format, with answers. **All 20 C++ programs compiled
  (zig c++ / clang, C++17) and run. Printed outputs are the real outputs.** The checker caught 2 of my
  errors before they shipped: linked-list search position (3 → **4** after an insert) and a circular
  queue peek line. Self-test and mock answers were re-verified by execution (postfix conversions,
  evaluations 21 / 7, octal 8959 / 11). No teaching event.
- [2026-09-24] **MTE blueprint received from the learner** (pasted, source not stated, presumably the
  professor/class). Marks by CO: **CO1 11 · CO2 14 · CO3 5**, with scope **up to BST only, BST = 5
  marks**. The paper is mostly theory, with **2 coding questions**. **A:** 4 × 2 (Q1, Q2 CO1 · Q3 CO2 · Q4 CO3).
  **B:** Q1 CO2 **coding**, Q2 CO2, Q3 CO2, Q4 CO3, marked 4 + 4 + 4 + 3 (the arithmetic forces the three
  CO2 questions to be 4 marks and the CO3 one 3). **C:** all CO1, 2 + 5, where the **5 is coding**. Totals check: 8 + 15 + 7 = 30.
  Consequences: C++/OOP rises to the top (11 marks). AVL/Red-Black are out of scope. **Gap found: file 06
  had only the BST definition, with no construction, search or deletion**. Adding it now, verified.
- [2026-09-24] Pack updated for the blueprint: `06` §6 **BST build/search/delete added** (worked tree for
  45 15 79 90 10 55 12 20 50 + 3 deletion cases + program + 2 practice items). Every tree, traversal
  and deletion was verified by execution. AVL/RB marked off-MTE. `00` gains the blueprint table.
- [2026-09-24] Learner asked whether the mock and other files were updated for the blueprint. Honest
  answer: only 00 and 06 had been. Then: **`07` mock rebuilt to the exact blueprint** (A CO1/CO1/CO2/CO3,
  B 4c/4/4/3, C 2 + 5c). New numbers throughout. Every answer verified by execution: `5 15`, circular
  queue full, `AB+C*DE/-` = 16, BST 60 25 75 10 40 90 35 70 with delete 25 → successor 35, linked-stack
  and BankAccount programs. Blueprint headers added to 01–05. Full pack re-check: 18 programs, 0 problems.
