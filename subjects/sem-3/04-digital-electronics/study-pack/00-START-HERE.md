# Digital Electronics ECE2102 — MTE Study Pack

Scope: **U1 + U2 + U3 through counters.** Built from the 25-Sep-2025 MTE paper, the professor's
decks 1-8, and the practice set. U4 (FSM/ASM) and U5 (logic families, memories) are **not on the
MTE** — they are ETE material and are not in this pack.

---

## The exam

**30 marks · 90 minutes · all questions compulsory.**

| Section | Paper's own label | Qs | Each | Total | What it actually demands |
|---|---|---|---|---|---|
| A | Memory Based | 3 | 2 | 6 | one fact / one step |
| B | Concept Based | 4 | 4 | 16 | apply a standard method |
| C | Analytical Based | 1 | 8 | 8 | a full design, start to finish |

**3 minutes per mark.** Section C alone is a 24-minute design question.

Section B is **53% of the paper**. Section C is 27% and it is one question — a single unrehearsed
design procedure costs you a quarter of the exam.

---

## The learning path

```
   [1] Boolean + K-map          <-- START. Feeds everything below.
        |
        v
   [2] NAND / NOR realization   <-- the house style; where marks are lost
        |
        +-------------------+-------------------+
        v                   v                   v
   [3] Adders          [4] MUX / Demux    [5] Decoder / Encoder
       Subtractors          implement F        implement F
       Parity               on a MUX           on a decoder
        |                   |                   |
        +-------------------+-------------------+
                            |
                            v
                   [6] Comparator / Shifter / ALU
                            |
                            v
                   [7] Flip-flops + waveforms   <-- combinational ends, memory begins
                            |
                            v
                   [8] Synchronous counter design   <-- the 8-mark Section C
                            |
                            v
                   [9] Drill set (real paper, timed)
```

Files 1 and 2 are prerequisites for everything. Files 3, 4, 5 are independent of each other —
do them in any order. File 7 must precede file 8.

---

## The one pattern that runs through the whole paper

**Nothing asks you only to minimize.** Every question minimizes *and then realizes under a
constraint:*

- minimize, then implement in **2-input NOR only**
- implement a 4-variable function on **one 8:1 MUX**
- implement a 4-variable function on an **undersized 4:1 MUX**
- build a full adder **from a decoder** plus one gate
- realize a maxterm form with **a decoder and one NOR gate**

Minimization is the cheap half of the marks. The realization constraint is the expensive half.
Every file in this pack drills the constraint, not just the algebra.

---

## Marks-losers, collected

These are the errors the question forms are built to catch.

| # | Trap | Where it bites |
|---|---|---|
| T1 | Treating a **don't-care as 0** | nearly every K-map question |
| T2 | Grouping legally but **not maximally** (4-cell group when an 8 exists) | K-map |
| T3 | Stopping at the minimized expression, **never drawing the constrained circuit** | Section B |
| T4 | Forgetting **wrap-around** adjacency (edges and corners) | K-map |
| T5 | Reading **ΠM as if it were Σm** | any maxterm question |
| T6 | Ignoring the stated **edge polarity** or **initial state** | waveform question |
| T7 | Confusing the **characteristic table** with the **excitation table** | FF and counter questions |
| T8 | Using the wrong FF's excitation table in a counter design | Section C |
| T9 | Leaving **unused states** undefined in a counter | Section C |
| T10 | Common **anode vs cathode** inversion on a display decoder | 7-segment |

---

## How to work this pack

Each file has the same shape:

```
## Map          - where the topic sits (small, 3-6 nodes)
## Attempt      - questions, no answers shown
## Method       - the compact procedure
## Worked       - a real exam question solved in full
## Traps
## Self-test    - more questions
## Answers      - at the bottom, on purpose
```

**Attempt before you scroll.** Write something down even when unsure — a wrong attempt that you
then correct sticks harder than a correct answer you only read. Scrolling straight to the answers
turns this pack into exactly the passive re-reading it is built to prevent.

Mark each self-test item as you go:

- **got it clean** -> revisit in 3 days, not sooner
- **got it with a struggle** -> revisit tomorrow
- **missed it** -> redo it today, then again tomorrow

---

## Files

| File | Topic | MTE weight |
|---|---|---|
| `01-boolean-kmap.md` | Boolean algebra, SOP/POS, K-maps, don't-cares | Very high |
| `02-nand-nor-realization.md` | Universal gates, 2-level conversion, bubble pushing | Very high |
| `03-adders-subtractors-parity.md` | HA/FA, ripple, BCD adder, subtractors, parity | High |
| `04-mux-demux.md` | Function implementation on a MUX, exact and undersized | Very high |
| `05-decoder-encoder-display.md` | Decoder implementation, encoders, BCD to 7-segment | High |
| `06-comparator-shifter-alu.md` | Magnitude comparator, barrel shifter, ALU | Medium |
| `07-flipflops-waveforms.md` | Latches, SR/D/JK/T, excitation tables, waveform drawing | High |
| `08-counter-design.md` | Synchronous counter design — the Section C procedure | High (8 marks) |
| `09-drill-set.md` | The 2025 paper + practice set, timed | — |

---

## Source honesty

Question **forms, emphasis and framing** come from the professor's decks and the 2025 paper —
they are authoritative for what gets asked and how.

**Facts, equations and derivations come from the textbook-verified knowledge base**
(`../knowledge-base/`), not from the slides. Slides and answer keys contain errors; nothing here is
taught straight off a slide.

Two things in this pack are marked where they appear: the course code on the decks reads `ECE 2105`
while the paper reads `ECE2102`, and no deck covers counters even though the MTE tested counter
design — file 08 is built from the knowledge base alone.
