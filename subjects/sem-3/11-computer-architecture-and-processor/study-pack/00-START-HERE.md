# Computer Architecture & Processor ECE2108 — MTE Study Pack

Scope: **U1 + U2 + U3 + U4.** Built from the professor's course hand-out, the three unit decks, and
the textbook-verified knowledge base. U5 (I/O organization), U6 (memory organization), U7 (8086) and
U8 (RISC-V) are **ETE material and are not in this pack**.

> **v2 exists (2026-09-15):** `../study-pack-v2/` is rebuilt around the professor's Assignments 1 and 2
> — real question forms. This pack's ALSU table (file 03, file 11) was corrected the same day.

---

## The exam

**Mid-Term Examination · 30 marks · closed book.** (Hand-out §E, verbatim.)

| Component | Marks |
|---|---|
| **MTE** | **30** |
| CWS — (Quiz + Assignments) / (Research + Presentation) | 30 |
| End Term Exam | 40 |

**The scope boundary is not a guess.** The hand-out's 36-lecture plan prints the row
*"Mid Term Examination"* between L19 and L20:

| Unit | Lectures | In MTE? |
|---|---|---|
| U1 Architecture fundamentals + RTL & microoperations | L1–L8 | **yes** |
| U2 Basic Computer organization & design | L9–L11 | **yes** |
| U3 Control unit design & microprogrammed control | L12–L15 | **yes** |
| U4 Parallel processing & pipelining | L16–L19 | **yes** |
| U5–U8 | L20–L36 | no — ETE |

**Note how unusual this is.** *Pipelining is on your mid-term.* Most universities put it after.
Do not assume the conventional ordering.

---

## ⚠ Read this before trusting any "expected question"

**There is no ECE2108 past paper — neither MTE nor ETE.** That changes what this pack can honestly
claim:

| | Digital Electronics pack | **This pack** |
|---|---|---|
| Scope | inferred | **evidence** (the printed lecture-plan divider) |
| Question forms | **evidence** (a real 2025 paper) | **inference** |

So: the *topics* below are certain, the *shapes* of the questions are not. Every worked item here is
labelled with where it came from — **deck**, **textbook (Mano)**, or **inferred form**. Nothing is
presented as "this came up last year", because nothing did.

**The single highest-value thing you can supply is any ECE2108 paper.** It would convert half this
pack from inference to evidence.

---

## The learning path

```
   [1] Architecture vs organization        <-- START. 2-mark and compare-table fodder.
       functional units, von Neumann,
       Harvard, RISC vs CISC
        |
        v
   [2] RTL, bus, memory transfers          <-- * THE GATE. Everything below is written in RTL.
        |
        v
   [3] Microoperations + ALSU              <-- the deck's own closing exam question
        |
        v
   [4] Basic Computer: registers,          <-- the machine itself
       bus, 25 instructions
        |
        v
   [5] Timing & control, instruction       <-- fetch/decode/execute with D·T timing
       cycle, MRI, interrupt
        |
        v
   [6] Design of BC + accumulator logic    <-- * the examinable SKILL of U2 (the scan)
        |
        v
   [7] Microprogrammed control             <-- a DIFFERENT machine. Read trap T7 first.
       + the sequencer
        |
        v
   [8] Program control + status bits
        |
        v
   [9] Parallel processing + Flynn         <-- independent of [4]-[8]; do it any time
        |
        v
  [10] Pipelining: speedup + hazards       <-- the numerical question
        |
        v
  [11] Drill set (timed, 30 marks)
```

Files 2 and 3 are prerequisites for 4–8. Files **9 and 10 are independent of 4–8** — pipelining needs
only the *phases* of the instruction cycle, not the Basic Computer's design, which is exactly why the
professor can place it before the MTE.

---

## The one idea that runs through all four units

**Hardware does not decide and then compute. It computes everything and selects.**

- The ALSU computes arithmetic, logic, shift-left and shift-right **every cycle**; S₃S₂ chooses which
  one is let out.
- The common bus has all seven sources wired to it (six registers + memory); S₂S₁S₀ chooses which
  one drives it.
- The control unit is nothing but **sums of D·T products** deciding which load lines go high.
- Microprogrammed control replaces those gates with **bits read out of a ROM word** — same selection,
  different storage.

Every "design" question in U1–U3 is the same move in a different costume: *list every condition under
which this thing happens, then OR them together.*

---

## Marks-losers, collected

| # | Trap | Where it bites |
|---|---|---|
| T1 | Reading `R2 ← R1` as an **assignment statement** instead of a clock edge + load line | every design question |
| T2 | Forgetting a transfer needs **two** things: a bus source selected **and** LD asserted | U1, U2 |
| T3 | Writing BSA as one clock cycle — it is **two** (D₅T₄ then D₅T₅) | U2 MRI question |
| T4 | Putting ISZ's write-back at **T₄** — it is **T₆** (the deck has this typo) | U2 MRI question |
| T5 | Missing the primes in `T′₀T′₁T′₂(IEN)(FGI + FGO)` — they are the whole point | interrupt question |
| T6 | Scanning **only some** of the statements that change a register when deriving LD | U2 design question |
| T7 | **Fusing Mano's two machines** — BC is 4096×16 / 3-bit opcode; the microprogram example is 2048×16 / 4-bit opcode | U3, catastrophic |
| T8 | Saying speedup **equals** k. k is the ceiling; the real answer is always below it | U4 numerical |
| T9 | Claiming pipelining makes **one instruction** faster (it raises throughput, and raises latency) | U4 concept |
| T10 | Inventing an MISD example. **There is none** — say so plainly | U4 Flynn |
| T11 | Confusing **carry C** (unsigned overflow) with **overflow V** (signed, = Cₙ ⊕ Cₙ₋₁) | U3 program control |
| T12 | Using `shr` where `ashr` is meant — it turns a negative number into a large positive one | U1 shift |

---

## How to work this pack

Each file has the same shape:

```
## Map          - where the topic sits (small, 3-6 nodes)
## Attempt      - questions, no answers shown
## Method       - the compact procedure
## Worked       - a full solution, labelled with its source
## Traps
## Self-test    - more questions
## Answers      - at the bottom, on purpose
```

**Attempt before you scroll.** Write something down even when unsure — a wrong attempt that you then
correct sticks harder than a correct answer you only read. Scrolling straight to the answers turns
this pack into exactly the passive re-reading it is built to prevent.

Mark each self-test item as you go:

- **got it clean** → revisit in 3 days, not sooner
- **got it with a struggle** → revisit tomorrow
- **missed it** → redo it today, then again tomorrow

---

## Files

| File | Topic | Unit | Weight |
|---|---|---|---|
| `01-arch-vs-organization.md` | Architecture vs organization, functional units, von Neumann/Harvard, RISC/CISC | U1 | Medium — reliable easy marks |
| `02-rtl-bus-memory-transfers.md` | RTL notation, the n(n−1) argument, bus sizing, memory transfers | U1 | **Very high — the gate** |
| `03-microoperations-and-alsu.md` | Arithmetic/logic/shift microops, the 4-bit arithmetic circuit, the ALSU | U1 | **Very high** |
| `04-basic-computer-registers-instructions.md` | Instruction format, 8 registers, common bus, 25 instructions | U2 | High |
| `05-instruction-cycle-and-mri.md` | Timing & control, fetch/decode, all 7 MRI sequences, I/O + interrupt | U2 | **Very high** |
| `06-design-of-bc-and-accumulator.md` | The scan method: LD/INR/CLR derivation, accumulator logic | U2 | **High — the skill, not the list** |
| `07-microprogrammed-control.md` | Hardwired vs microprogrammed, mapping, F1/F2/F3/CD/BR/AD, fetch routine, sequencer | U3 | High |
| `08-program-control-and-status-bits.md` | C/S/Z/V, conditional branches, subroutine return strategies, stacks | U3 | Medium |
| `09-parallel-processing-and-flynn.md` | Throughput, levels of parallelism, Flynn's four classes | U4 | Medium |
| `10-pipelining-speedup-hazards.md` | k+n−1, S = n·tₙ/((k+n−1)·tₚ), FP adder, FI-DA-FO-EX, the three hazards | U4 | **Very high — the numerical** |
| `11-drill-set.md` | A 30-mark timed paper built from the inferred forms | all | — |

**If you have three days, not three weeks:** files 02, 03, 05, 06, 10 — in that order. They carry the
derivations and the numerical, which is where marks are actually won or lost. Files 01, 08, 09 are
recall-and-table material you can compress into one pass.

---

## Video lectures

A verified, unit-by-unit lecture map lives in **`../video-lectures.md`** — two layers, because no
single course matches this syllabus: NPTEL/institutional courses for **mechanism**, Mano-sequence
YouTube channels for **scope and notation**. It also lists the four worked-problem lectures that are
the closest thing to a practice paper you can get.

**Videos come second.** Attempt the questions in these files first, fail some, *then* watch. A video
watched cold is entertainment; the same video after a failed attempt is teaching.

---

## Source honesty

**Scope, emphasis and framing** come from the professor's hand-out and decks — they are authoritative
for what is taught and how it is framed.

**Facts, equations and derivations come from the textbook-verified knowledge base**
(`../knowledge-base/`), whose authority for these four units is **M. M. Mano, *Computer System
Architecture*, 3e**. Nothing here is taught straight off a slide.

**Two slide errors are corrected rather than reproduced**, and both are flagged where they appear:

1. The Unit-2 deck prints ISZ's third microoperation as `D₆T₄`. It must be **`D₆T₆`** — the same
   deck's own "Complete Computer Description" slide contradicts it. (File 05, trap T4.)
2. The Unit-1 deck's comparison table contains the row *"Architecture indicates its hardware,
   Organization indicates its performance."* That row is muddled. Reproduce the professor's table if
   the exam asks for it; do not reason from that row. (File 01.)

One further caveat carried from the knowledge base: Mano 3e could not be obtained as a clean primary
PDF. Its chapters were verified against **multiple independent institutional reproductions that agree
with each other and with the professor's decks**. That is authoritative-secondary, not primary — good
enough for every number in this pack, and stated rather than hidden.
