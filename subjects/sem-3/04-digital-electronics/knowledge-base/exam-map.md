# ECE2102 Digital Electronics — exam-map (marks-aiming map)

> **REBUILT 2026-09-11 from real MUJ evidence** (supersedes the syllabus-inferred stub of
> 2026-06-27). Evidence now in `../exam-pack/`: the professor's 8-deck slide set, one MTE past
> paper (**25-Sep-2025**), and a 10-question practice set.
>
> **Honesty rule (`../../../research-engine/exam-resources.md`):** this material is tier-1 for
> *what is tested and how* and sets **scope/emphasis/framing** — it is **not** the authority on
> *what is true*. Every fact still comes from the prescribed textbook. Nothing here is taught
> straight off a slide.
>
> **Confidence:** structure + question forms below are `settled` **for the 2025 MTE**. Generalizing
> one paper to "the pattern" is `likely`, not proven — one sitting, one examiner. ETE remains
> **`uncertain`**: no ETE paper has been supplied.

---

## 1. MTE structure — `settled` (from `PYQ-MTE-2025-09-25.pdf`)

**MUJ Odd-Semester Mid Term Examination, 25-Sep-2025 · 11:30–13:00 · 30 marks · 90 minutes.**
All questions compulsory. "Missing data may be assumed suitably."

| Section | Label on paper | Qs | Marks each | Subtotal |
|---|---|---|---|---|
| A | Memory Based Questions | 3 | 2 | 6 |
| B | Concept Based Questions | 4 | 4 | 16 |
| C | Analytical Based Questions | 1 | 8 | 8 |

**Section names are the examiner's own cognitive-level labels** — A = recall/one-step, B = apply a
standard method, C = design end-to-end. That maps onto the CHECK ladder: an item is not MTE-ready
until it survives a **Section-C-style** demand, not just a Section-A one.

**Time budget: 90 min / 30 marks = 3 min per mark.** Section C alone is a 24-minute design.

## 2. MTE scope — `likely` (the real find)

The 2025 MTE drew on **U1 + U2 + the first half of U3**, and stopped there:

| Unit | In the 2025 MTE? | Evidence |
|---|---|---|
| U1 Combinational logic design | yes, heavily | Q1 (NOR implementation), Q2 (parity), Q4 (K-map), Q6 (full adder) |
| U2 MSI devices | yes, heavily | Q5 (8:1 MUX), Q6 (decoder), Q2 (parity generator) |
| U3 Sequential logic design | yes, partially | Q3 (T-FF excitation), Q7 (edge-triggered waveform), Q8 (synchronous counter) |
| U4 State machines | **absent** | no FSM/ASM/state-reduction question |
| U5 Logic families & memories | **absent** | no noise-margin/fan-out/memory/PLD question |

**Working split (`likely`, supersedes the old provisional guess):**
**MTE ≈ U1 + U2 + U3 through counters.** **ETE ≈ comprehensive, weighted to U3–U5.**

**Corroborated by the slide set:** the professor's decks run 1–8 and **stop at flip-flops** — no
deck for FSM, ASM, logic families, or memories was supplied. Deck coverage and MTE coverage agree.

⚠ **Material gap:** MTE Q8 required a **synchronous 0–7 counter** design, but **no deck covers
counters, shift registers, or excitation-table design** — that content was taught (or assigned)
without a deck in this drop. Later decks likely exist. `uncertain` — ask the learner.

## 3. Verified question patterns — the forms that actually appear

Each row cites the paper/practice item it came from. **These are the shapes to drill.**

| # | Question form | Marks | Source | Unit |
|---|---|---|---|---|
| P1 | Optimize an expression, then **implement in one specified gate type** (2-input NOR / NAND / universal) | 2–4 | MTE Q1; Practice Q1, Q2 | U1 |
| P2 | Parity generator output for a given bit sequence / draw a 4-bit odd-even parity generator | 2–4 | MTE Q2; Practice Q9 | U1–U2 |
| P3 | Flip-flop **excitation** input for a required output behaviour | 2 | MTE Q3 | U3 |
| P4 | **K-map minimization with don't-cares**, then draw the logic circuit | 4 | MTE Q4; Practice Q1, Q2 | U1 |
| P5 | Implement a Boolean function using a **single 8:1 MUX** | 4 | MTE Q5; Practice Q3, Q6 | U2 |
| P6 | Implement a function / **full adder using a decoder** (+ OR/NOR gate) | 4 | MTE Q6; Practice Q7, Q8 | U2 |
| P7 | Draw the **output waveform** for a given input waveform + stated edge sensitivity, Q initially 0 | 4 | MTE Q7 | U3 |
| P8 | **Design a synchronous counter** for a given count range using a stated FF type + edge | 8 | MTE Q8 | U3 |
| P9 | Design a combinational circuit from a **word-problem specification** (e.g. output 1 when two consecutive input bits are 1) | 4 | Practice Q4 | U1 |
| P10 | Implement a function with a **smaller MUX than variables** (4:1 for 4 vars) — one variable fed as a data input | 4 | Practice Q5 | U2 |
| P11 | **BCD to 7-segment decoder** for a stated display polarity (common anode) | 4 | Practice Q10 | U2 |

### Pattern-level observations (the framing to teach into)
- **Constrained implementation is the house style.** Almost never "minimize F." Always minimize
  **and then realize it under a constraint** — NOR only, NAND only, one 8:1 MUX, a decoder plus one
  gate, a 4:1 MUX with a variable as data input. Minimization is the easy half; **the realization
  constraint is where the marks are lost.**
- **Don't-cares appear in nearly every K-map question** (MTE Q4; Practice Q1, Q2). Treating `d` as 0
  is the standard mark-losing error.
- **Both minterm (Σm) and maxterm (ΠM) forms are used** (Practice Q7 is ΠM) — conversion fluency is
  assumed, not taught in the question.
- **Waveform/timing questions specify edge polarity and initial state explicitly** — the same
  waveform gives a different answer for positive vs negative edge.
- **Section C is a full design procedure**, not a fact: count table → excitation table → K-map per
  FF input → circuit. It is 27% of the MTE in one question.

## 4. Per-unit weighting — rebuilt

| Unit | Topic | MTE weight | ETE weight | Confidence |
|---|---|---|---|---|
| U1 | K-map minimization (with don't-cares) + constrained realization | **Very high** | High | `likely` (MTE-verified) |
| U1 | Adders/subtractors/BCD adder | **High** | High | `likely` |
| U1 | Parity generation/checking | Medium | Medium | `settled` for MTE |
| U2 | MUX-based function implementation | **Very high** | High | `likely` (MTE-verified) |
| U2 | Decoder/encoder implementation | **High** | High | `likely` (MTE-verified) |
| U2 | Comparator, barrel shifter, ALU, 7-seg display | Medium | Medium | deck-supported, unseen in MTE |
| U3 | Flip-flops: characteristic/excitation tables, edge triggering, waveforms | **High** | High | `likely` (MTE-verified) |
| U3 | Counters (synchronous, excitation-table design) | **High** (the 8-mark slot) | High | `likely` (MTE-verified) |
| U3 | Shift registers, timing analysis | Low in MTE | Medium | `uncertain` |
| U4 | FSM / ASM / async design | **Absent from MTE** | High | `likely` — ETE material |
| U5 | Logic families, memories, PLDs | **Absent from MTE** | High | `likely` — ETE material |

## 5. What this changes for teaching order

Scoring-over-depth (`CLAUDE.md`, source-sequencing rule) now has real evidence to obey:

1. **U1 K-map + constrained realization** (NOR/NAND-only), don't-cares included — the densest
   scoring block on the paper.
2. **U2 MUX/decoder implementation** — second densest; three distinct forms (8:1 exact, 4:1
   undersized, decoder + gate).
3. **U3 flip-flops → waveforms → synchronous counter design** — carries the 8-mark Section C.
4. Then the U2 remainder (comparator/ALU/shifter/7-seg), then **U4/U5 for the ETE**.

Depth (Stage 2, already built) still follows — taught *after* the scoring spine of each unit, not
instead of it.

## 6. Still open

- **No ETE paper.** ETE structure, marks split, and duration are `uncertain`. Ask the learner.
- **No answer key** supplied — and per the honesty rule a key would not be authoritative anyway.
- **One MTE only.** Pattern claims are `likely`; a second year's paper would settle them.
- **Course code:** decks say `ECE 2105`, paper and KB say `ECE2102`, syllabus text identical.
  `uncertain` — learner to confirm against their registration/handout.
- **Missing decks** for counters/registers/FSM/logic families/memories (see §2 gap).
- **2026 exam dates** not supplied — `../../research-engine/exam-calendar.md` still empty. The 2025
  MTE fell on **25 September**; if 2026 tracks it, the MTE is roughly two weeks out.
