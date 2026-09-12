# ECE2108 — knowledge-base CHANGELOG (correction audit trail)

> Protocol §10 format:
> `[YYYY-MM-DD] <claim/topic> — <what changed> — <why> — <trigger> — <confidence: old → new>`
>
> **Never silently overwrite.** Every correction is recorded here with what caused it.

---

## 2026-09-12 — subject created, Stage 1 built

- `[2026-09-12]` **Subject created** — `11-computer-architecture-and-processor/` scaffolded and
  Stage 1 built across 8 units — triggered by the learner dropping the ECE2108 course hand-out and
  three unit decks into `../../_inbox/` and reporting that the subject was missing from the sem-3
  registry — confidence: n/a → base established.

- `[2026-09-12]` **Registry discrepancy (ECE2108 absent from the sem-3 batch)** — RESOLVED as a
  **scheme-revision mismatch**, not an omission — the batch was seeded (2026-06-16) from the MUJ
  *2023-onwards* ECE curriculum PDF, in which **ECE2108 does not appear** (verified by text
  extraction: 67 course codes, no match); ECE2108 **is** present in the MUJ **2025-2026 onwards**
  scheme, Third Semester, 3 credits — trigger: learner reported both "subjects I don't have" and "a
  subject I have that isn't listed", and the hand-out's existence contradicted the registry —
  confidence: `unknown → settled` for this course; **batch-level reconciliation deliberately NOT
  performed** (it would restructure subjects with built knowledge bases) and logged as an open
  question in `../../research-engine/research-queue.md`.

- `[2026-09-12]` **Sibling subject: Digital Electronics course-code mismatch (ECE 2105 vs ECE2102)**
  — RESOLVED as a **side effect** of the above — `../../_inbox/TRIAGE-LOG.md` flagged on 2026-09-11
  that the professor's Digital Electronics deck 1 headed itself **ECE 2105** while the MTE paper and
  that subject's KB said **ECE2102**; the 2025-2026 scheme shows **ECE2105 Digital Electronics** in
  Sem-3, so the deck carries the **new** code and the paper/KB the **old** one — trigger: reading the
  2025 scheme for this subject — confidence: `uncertain → settled`. **Both codes are correct, for
  different scheme revisions.** Recorded here and in the research queue; that subject's own files are
  **not** edited from this session (log-first rule — no subject file changes in a session whose
  progress log doesn't say why).

### Corrections made to source material while building

- `[2026-09-12]` **U2, ISZ third microoperation timing** — corrected **`D₆T₄` → `D₆T₆`** — the
  professor's Unit-2 deck prints `D₆T₄: M[AR] ← DR, if (DR = 0)…` as ISZ's *third* line, repeating T₄;
  a single instruction cannot perform two different actions at the same time step, and the **same
  deck's own "Complete Computer Description" slide gives `D₆T₆`** — trigger: internal inconsistency
  between two slides in one deck, caught while transcribing the MRI sequences — confidence:
  `slide-as-given (suspect) → settled` as D₆T₆. Retained as `misconceptions.md` **M9**.

- `[2026-09-12]` **U7, the sign flag (SF)** — **rejected** the claim "SF is used with unsigned
  numbers" found in [8086-BBAU] — SF is set equal to the **high-order bit of the result**, which is
  the sign **only under signed (2's-complement) interpretation**; the claim is contradicted by the
  **same document's own flag table** ("Sign Flag: Set equal to high-order bit of result (0 is
  positive, 1 if negative)") — trigger: internal contradiction within one source, caught while
  building the flag table — confidence: `source-as-given (suspect) → rejected`; the correct division
  (**CF = unsigned overflow · OF = signed overflow · SF = signed sign**) marked `settled`. Retained as
  `misconceptions.md` **M16**.

- `[2026-09-12]` **U1, "Architecture indicates its hardware; Organization indicates its performance"**
  — **flagged as muddled, not adopted as a definition** — architecture is the *abstraction* (the ISA),
  not the hardware, and performance is a property of the organization **and** the fabrication
  technology — trigger: the row conflicts with the same table's own stronger rows ("architecture =
  what it does / also called instruction set architecture") — confidence: `slide-as-given → uncertain`;
  the table is reproduced for exam purposes with an explicit warning not to reason from that row.
  Retained as `misconceptions.md` **M1**.

- `[2026-09-12]` **U8, "RISC-V has six instruction formats"** — **refined to "four core formats
  (R/I/S/U) plus two variants (B/J)"** — this is the **ratified specification's own wording**, read
  directly; the common teaching shorthand "six formats" is not wrong about the layouts but misstates
  the standard — trigger: reading the primary source rather than relying on recall — confidence:
  `recalled (uncertain) → settled` as the spec's phrasing. Retained as `misconceptions.md` **M21**.

### Ambiguities recorded rather than resolved (protocol §5: don't average conflicting sources to mush)

- `[2026-09-12]` **Number of 8086 addressing modes** — sources give **12 in 5 groups** (institutional)
  vs **7 or 8** (other textbooks, folding in I/O-port / relative / implied) — **not reconciled into a
  single number**; the *mechanisms* are `settled` and the *taxonomy* is recorded as a naming
  convention — trigger: cross-source disagreement — confidence: mechanisms `settled`, count
  `uncertain`. **CO4 is the highest-target CO (85%), so this is flagged prominently** in U7 §5 and
  `misconceptions.md` **M18**.

- `[2026-09-12]` **Number of I/O "modes of transfer"** — Mano §11-4 presents **three** (programmed I/O,
  interrupt-initiated, DMA) and treats the **IOP** separately in §11-7; chapter summaries often say
  **four** — recorded as "three, plus the IOP as a further step", correct under either convention —
  confidence: `uncertain` as a count, `settled` as mechanisms. `misconceptions.md` **M13**.

- `[2026-09-12]` **Average-access-time formula convention** — `h·tᶜ + (1−h)·tᵐ` vs
  `tᶜ + (1−h)·penalty` — **both are in circulation and give different numbers**; recorded with an
  instruction to state the convention in any answer rather than picking one silently —
  confidence: `uncertain` as convention. `misconceptions.md` **M15**.

- `[2026-09-12]` **Number of 8086 instruction-set groups** — 7 vs 8 depending on the text — mnemonics
  and behaviour `settled`, grouping recorded as convention.

- `[2026-09-12]` **Hand-out internal contradiction: lectures 29–32** — printed **after** the "Mid Term
  Examination" divider but their *Mode of assessing CO* column lists "MTE" — **not resolved**; the
  positional divider is taken as authoritative (`likely`) and the contradiction is logged in
  `00-map.md` and `exam-map.md` rather than hidden — trigger: reading the lecture plan against itself.

- `[2026-09-12]` **Hand-out session year** — header says "July-Dec 2027", the filename says "Jan
  2027", the deck footers are machine-stamped **8/6/2026** — **not resolved**; Jul–Dec **2026** taken
  as the live session (`likely`) on the strength of the machine-generated footer — affects only the
  exam calendar, not content.

### Limitations recorded (protocol §1: log what could not be verified)

- `[2026-09-12]` **Mano 3e could not be read directly** — the located full-text copy is served chunked
  and truncates (8 attempts, 2.0–7.3 MB, never complete; `Content-Length: 0` on HEAD); an xref rebuild
  recovered 1262 of ~4759 objects but the page tree was lost in object streams — **mitigation:** every
  chapter verified against independent institutional reproductions, two of them for chs. 5, 7, 9 and
  11 — confidence: Mano-derived claims `settled` where two reproductions agree, `likely` where one.
  Full account in `sources.md` §4. **U6 (ch. 12) rests on a single reproduction** whose figure numbers
  drift, so **no figure numbers are cited** in that unit.

- `[2026-09-12]` **Bhurchandi & Ray (U7) and Patterson & Hennessy (U8) not obtained** — U7 built from
  institutional material using Bhurchandi's own EA/BA/MA notation plus NPTEL and die-level analysis;
  **U8 built from the ratified RISC-V standard itself, which is stronger than the textbook would have
  been** — confidence: U7 facts `settled`, "the instructor uses this notation" `likely`; U8 `settled`
  from primary.

- `[2026-09-12]` **No PYQ for this subject** — `exam-map.md` §4 (question forms) is explicitly marked
  **inference, not evidence**; §1 (assessment structure) and §2 (MTE/ETE scope) are `settled` from the
  hand-out — confidence: exam-targeting `uncertain` for question form, `settled` for scope.

## 2026-09-12 — exit tests

### Stage-1 exit test — **PASSED** (`two-stage-depth.md`: 3–5 problems spanning the units)

⚠ **No PYQ exists**, so representative problems were used and the exam-targeting is flagged
unconfirmed, exactly as the protocol requires. Problems were chosen from `exam-map.md` §4, weighted to
the highest-confidence rows.

| # | Problem | Unit | Base answers from mechanism? |
|---|---|---|---|
| 1 | "Design a 4-bit ALU performing the listed operations and explain its working in detail" — **the professor's own deck question** | U1 | **yes** — §10 gives the one-stage structure, the S₃S₂ block select vs S₁S₀/Cᵢₙ operation select, and the 8+4+1+1 = 14 operation count derived rather than recited |
| 2 | "Give the complete microoperation sequence for BSA and explain with a memory before/after diagram" | U2 | **yes** — §8 gives D₅T₄/D₅T₅, the worked `BSA 135` trace, the indirect-BUN return, **and** the mechanism for why it takes two clocks (single-bus serialization) |
| 3 | "Decode the binary microinstruction `000 100 101 00 00 1000010`" | U3 | **yes** — §4/§5 identify F2 = READ, F3 = INCPC, CD = U, BR = JMP, AD = 1000010, and explain the three-field parallelism that lets READ and INCPC co-issue |
| 4 | "A 4-stage pipeline, tₚ = 20 ns, 100 tasks. Find the speedup and explain the shortfall from the ceiling" | U4 | **yes** — §5 gives 8000/2060 = **3.88**, the ceiling k = 4, and the four named reasons for the gap |
| 5 | "Main memory 32K×12, cache 512×12. Give the direct-mapping address split; repeat with 8-word blocks" | U6 | **yes** — §4 gives 6-bit tag + 9-bit index, then 6 + 6 + 3, **with the mechanism** (the tag is the bits the index discarded) |
| 6 | "Compute the physical address for `89AB:F012`; then name the addressing mode of `MOV CX,[SI+0A2H]` and compute EA/BA/MA" | U7 | **yes** — §4 gives **98AC2H** with the paragraph-shift mechanism and segment overlap; §5 gives indexed mode **and the sign-extension trap** (0A2H → FFA2H) |
| 7 | "How many instruction formats does RV32I have?" | U8 | **yes** — §4 gives four core (R/I/S/U) + two variants (B/J), quoted from the ratified spec |

**All 7 answered from mechanism with a cited source. Stage 1 → `stage-1✓`.**

### Stage-2 exit test (§0 surplus test, by output) — **PASSED**

Expert-level / "why-not-what" questions were generated per unit (the `§H Harder problems` blocks) and
the base was checked for whether it answers them **from mechanism, with sources**. Representative:

| Question | Answered from | Verdict |
|---|---|---|
| "Would a 12-stage pipeline be 12× faster?" | U4 s2 §C — the f_clock derivation, the three costs, **and the verified NetBurst 20→31-stage history with its abandonment** | pass |
| "Why is an accumulator machine one-address?" | U2 s2 §B — the operand bit-counting argument (3-address needs 36 bits in a 16-bit word) | pass |
| "Why did RISC abandon microcode?" | U3 s2 §D — the four-step causal chain, ending at **the cache, not ideology** — plus §E showing microcode *survives* in x86 as field-updatable WCS | pass |
| "My cache hit rate is 85%, what do I change?" | U6 s2 §A — unanswerable until the **three C's** are separated; each class names a different fix | pass |
| "How do you load a 32-bit constant with 32-bit instructions?" | U8 s2 §B — `LUI`+`ADDI` **with the sign-extension compensation rule derived** and checked on 0xDEADBEEF | pass |
| "DMA and caching are each correct; why are they jointly wrong?" | U5 s2 §B — both coherence failure directions and the three standard fixes | pass |
| "How did a missing pin become part of an architecture for 30 years?" | U7 s2 §A — the verified A20 wraparound → 80286 divergence → keyboard-controller gate → HMA chain | pass |

**Open-questions register worked but deliberately not emptied** (protocol §10: an empty backlog usually
means you stopped looking). 12 items stand in `00-map.md`; 9 more in `stage-2/sources.md`.

**Numeric audit:** **all 34 numeric claims across both stages were re-computed programmatically and
PASSED** — the 8086 physical-address arithmetic, both pipeline speedups, the AMAT recurrence, both
average-access-time figures, every cache bit-split, the TLB-reach figures, ⌈log₂(8!)⌉, all eight Amdahl
table entries, and the `LUI`/`ADDI` compensation (including the deliberately-wrong naive variant).

`[2026-09-12]` **Status: `stage-2✓` — TEACH-READY.** Both stages complete, both exit tests passed. The
hard teaching gate (`../../research-engine/two-stage-depth.md`) is met. **Caveats that survive into
teaching and must be stated to the learner, not hidden:** exam *question forms* are inference (no PYQ);
no deck exists for L12–L36; Mano was verified through reproductions rather than read directly; and
taxonomy counts (addressing modes, instruction groups, transfer modes) are conventions, not facts.
