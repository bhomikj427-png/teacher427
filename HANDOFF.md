# HANDOFF

## Task
Build `subjects/sem-3/11-computer-architecture-and-processor/chat-pack/instructions-chat.md`: the CAP (ECE2108) ETE file the learner loads into claude.ai chats. **ETE is 2026-11-26** — finish it this session. Nothing is written yet.

## Hard requirements (learner, 2026-11-25)
- **Lean.** Chats re-read it constantly. No prose, no history, no "why", no source notes. Tables, formulas, solved answers only.
- **Complete.** Every important fact from the professor's material plus every assignment and MTE question solved. Nothing he could ask is missing.
- **Material-based.** Scope = his material (decks, assignments, MTE, hand-out). Truth = the textbooks his decks list as references; never a fact straight off a slide:
  - **Mano, *Computer System Architecture* 3e**: U1–U6. The decks say "Ref: M. M. Mano", and his assignments are Mano's end-of-chapter problems, so use Mano's notation and methods.
  - **Bhurchandi & Ray, *Advanced Microprocessors and Peripheral Devices* 3e**: 8086.
  - **Patterson & Hennessy, *COD RISC-V Edition***: RISC-V.
  - Hamacher 5e and Sonal Yadav (AICTE) are also listed, as secondary references.
  - The KB (`knowledge-base/01`–`08`, stage-1 files) is already checked against these.
- **No teaching script** (`learner-preferences.md` §3). Header = 2 lines: the file is the truth authority; every fact/number must be right. Fractions stacked.
- Do not copy the EDC chat file's Part A/B script. Its other parts show the shape: solved questions + compact concepts.

## Sources (all in `exam-pack/`)
- Questions: A1 (20 Q), A2 (15 Q), MTE (7 Q) — full text in `question-bank.md` lines 49–227. **A3** (10 Q) and **SPL-PRACTICE** (20 Q) are one-page text PDFs: read them with the Read tool.
- Decks: U1, U2, U4 (`slides-unit3-…`), 8086: `slides-U6-8086-part1/2/3` (text), assembler deck, image-only 85-pp deck. Hand-out = marks/scope.
- No decks for U3, U5, U6, U8: use the KB. ETE = whole course, weighted to I/O, memory, 8086 (largest unit), RISC-V.

## Decided content (already worked out; don't redo)
- 8086 unit scope (deck syllabus): intro + µP generations, BIU/EU + queue, registers/flags, segmentation + PA, addressing modes, instruction set, directives, ALP, **pins + min/max mode**, **memory interfacing**.
- Memory interfacing = the deck's method (Part 3, slides 26–33):
  - Even bank on D0–D7, selected by A0 = 0; odd bank on D8–D15, selected by BHE̅ = 0.
  - Chips take A1… upward. EPROM at the top so FFFF0H is inside it; RAM from 00000H.
  - **Deck Q2 = A3 Q9** (2×16K EPROM, 2×32K RAM):
    - EPROM F8000–FFFFF, chips on A1–A14. C = NAND(A15–A19). CS1(odd) = C + BHE̅, CS2(even) = C + A0.
    - RAM 00000–0FFFF, chips on A1–A15. C′ = OR(A16–A19). CS3(odd) = C′ + BHE̅, CS4(even) = C′ + A0.
  - **A3 Q10** (2×4K EPROM, 2×4K RAM), same method:
    - EPROM FE000–FFFFF, A1–A12, select A13–A19 all 1.
    - RAM 00000–01FFF, select A13–A19 all 0.
    - Also note the deck's version: 74138 with inputs BHE̅, A0, A13, enabled by 7430 NAND(A14–A19), block at FC000–FFFFF.
  - "Multiplexed data lines" → demultiplex AD0–AD15 with 8282 latches strobed by ALE.
- A3 Q8 (Mano 12-2):
  - Chips: 8 RAM, 4 ROM, 16 interface registers.
  - 14-bit map: RAM 0000–07FF, ROM 1000–1FFF, interface 2000–200F.

## Verification
- Every number by one script in `chat-pack/`.
- Every ALP actually assembled and run: `unicorn` + `keystone-engine` are installed (x86 16-bit mode).
- Throwaway files (slide renders etc.) go in `_tmp/` at the project root, deleted after. Never write outside the project.

## Permissions (learner hit repeated prompts on 2026-11-25)
- Read PDFs/files with Read/Grep/Glob, not shell.
- One plain shell command per call: no `cd`, no `&&` chains, no multi-line `python -c`. Put scripts in a file under `_tmp/` or `chat-pack/` and run `python <file>`.

## Pending
- Commit when done; the learner pushes.
