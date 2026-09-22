# ECE2108 Computer Architecture & Processor — exam-map (marks-aiming map)

> Built 2026-09-12 from the professor's **course hand-out** + three unit decks (`../exam-pack/`).
>
> **Honesty rule (`../../research-engine/exam-resources.md`):** this material is tier-1 for *what is
> tested and how* and sets **scope, emphasis and framing** — it is **not** the authority on *what is
> true*. Every fact still comes from the prescribed textbook. Nothing here is taught off a slide.
>
> **Read the confidence column before trusting a row.** This subject has **no past paper at all**,
> so this map is much stronger on *scope* than on *question form* — the reverse of
> `../../04-digital-electronics`, which has a real MTE paper but had to infer its scope.

---

## 1. Assessment structure — `settled` (hand-out §E, verbatim)

| Component | Description | Marks |
|---|---|---|
| Internal (summative) | **Mid-Term Examination** — closed book | **30** |
| Internal (summative) | **CWS** — (Quiz + Assignments) / (Research + Presentation) | **30** |
| End Term (summative) | **End Term Exam** — closed book | **40** |
| | **Total** | **100** |

**Two things follow, and they change how this subject should be studied:**

1. **The MTE is worth only 30% and the ETE 40% — but CWS is another 30%.** Sixty marks of the grade
   are decided *before* the ETE. The CWS composition is **unspecified** in the hand-out (no weights,
   no count) — that is an open question for the learner, and it is 30 marks of unplanned exposure.
2. **This is the first verified MUJ marks split anywhere in the batch.** `exam-resources.md` had the
   MTE/ETE/internals weightage flagged `uncertain` batch-wide since 2026-06-17. It is now `settled`
   **for ECE2108 only** — do **not** generalize it to other courses without their own hand-outs.

## 2. MTE vs ETE scope — `settled` (the strongest finding here)

The hand-out's lecture plan **prints the row "Mid Term Examination" between L19 and L20.** That is
first-party, unambiguous evidence — no inference needed:

| Unit | Lectures | In MTE? | In ETE? |
|---|---|---|---|
| U1 Architecture fundamentals + RTL & microoperations | L1–L8 | **yes** | yes |
| U2 Basic Computer organization & design | L9–L11 | **yes** | yes |
| U3 Control unit design & microprogrammed control | L12–L15 | **yes** | yes |
| U4 Parallel processing & pipelining | L16–L19 | **yes** | yes |
| U5 Input–output organization | L20–L22 | no | yes |
| U6 Memory organization | L23–L26 | no | yes |
| U7 8086 microprocessor | L27–L34 | no | yes |
| U8 RISC-V | L35–L36 | no | yes |

**MTE = U1 + U2 + U3 + U4** (everything up to and including pipeline hazards).
**ETE = comprehensive, weighted to U5–U8** (the hand-out's "Mode of assessing CO" column lists ETE
for every lecture, and only ETE for L16–L26 and L33–L36).

⚠ **One contradiction, logged not hidden:** L29–L32 sit *after* the MTE divider but their assessment
column still says "MTE". Positional divider vs boilerplate column — the divider wins (`likely`).
Treat 8086 as ETE material; if the instructor says otherwise, U7 moves and this map is rebuilt.

**Note how unusual the MTE scope is.** Four of eight units, including *pipelining* — which most
universities put after the mid-term. The professor front-loads concurrency (and hands L16/L17 to an
industry practitioner). Do not assume the conventional ordering.

## 3. Per-topic priority — derived from CO targets + lecture count

No PYQ exists, so weightage is **inferred**, not measured. Two signals are real, though, and they
point the same way:

- **Lecture count** = how much class time a topic got (proxy for emphasis).
- **CO target attainment + Bloom level** from hand-out §C — the instructor's own statement of how
  hard they intend to push each outcome.

| Topic | Lectures | CO | Bloom | Target | Priority | Why |
|---|---|---|---|---|---|---|
| **8086 addressing modes** | L28–L29 | CO4 | L2 | **85% / level 3** | **HIGHEST (ETE)** | the **only** CO above 75%; the instructor has singled it out |
| **8086 assembly programming** | L30–L34 | CO5 | **L3** | 75% | **HIGHEST (ETE)** | the **only L3 ("Develop") CO** — a *doing* outcome, not a *knowing* one; 5 lectures |
| Basic Computer + design of BC/AC logic | L9–L11 | CO2 | L2 | 75% | HIGH (MTE) | the richest derivation content; the deck runs 48 pages on it |
| RTL + arithmetic/logic/shift microops + ALSU | L3–L8 | CO1 | L2 | 75% | HIGH (MTE) | **6 of 19 pre-MTE lectures**; CO1 exists only for this |
| Control unit + microprogrammed control | L12–L15 | CO2 | L2 | 75% | HIGH (MTE) | 4 lectures, no deck — likely assignment-heavy |
| Pipelining + hazards | L17–L19 | CO3 | L2 | 75% | HIGH (MTE) | numerical speedup problems are the natural exam form |
| Memory organization + cache | L23–L26 | CO3 | L2 | 75% | MEDIUM (ETE) | cache is `*`-marked practitioner-delivered and named in CO3 |
| I/O organization | L20–L22 | CO3 | L2 | 75% | MEDIUM (ETE) | mostly descriptive; low numerical yield |
| Parallel processing / Flynn | L16 | CO3 | L2 | 75% | MEDIUM (MTE) | 1 lecture, `*` practitioner — likely descriptive/short-answer |
| Arch vs org, von Neumann/Harvard, RISC/CISC | L1–L2 | CO1 | L2 | 75% | MEDIUM | classic 2-mark and compare-table fodder |
| RISC-V | L35–L36 | CO5 | L2 | 75% | LOWEST (ETE) | last 2 lectures, `*` practitioner, "Quiz, ETE" only — descriptive |

**Scoring-over-depth consequence for teaching order:** the MTE units (U1–U4) come first because
they're examined first. But **within the whole course, the two highest-value blocks are 8086
addressing modes and 8086 assembly programming** (CO4 at 85%, CO5 at L3) — both ETE. Budget real
practice time there, not just reading; CO5 is a *Develop* verb, which means writing programs.

## 4. Expected question forms — `uncertain` (inference, clearly labelled)

**There is no ECE2108 paper.** The forms below are inferred from (a) the topic's natural assessment
shape, (b) the hand-out's *Session Outcome* verbs, and (c) the sibling MUJ MTE pattern. Treat as a
drill list, **not** as evidence of what will be asked.

| # | Likely question form | Unit | Basis |
|---|---|---|---|
| F1 | Distinguish computer architecture from organization (table, 4–6 points) | U1 | deck 1 gives a 6-row comparison table verbatim — a strong tell |
| F2 | Compare von Neumann vs Harvard / RISC vs CISC (table) | U1 | L2 outcome is "Identify basic components… explain the purpose" |
| F3 | Write the RTL / microoperation sequence for a stated transfer | U1 | L3–L4 outcomes are literally "Register Transfer Language and Register Transfer" |
| F4 | **Design a 4-bit arithmetic circuit / ALSU and explain its working** | U1 | **deck 1's last slide is this exact question, marked "QnA"** — highest-confidence single item in the map |
| F5 | Given S₃S₂S₁S₀ + Cᵢₙ, state the ALSU microoperation (table row) | U1 | deck 1's function table |
| F6 | Explain the BC common bus; give the S₂S₁S₀ selection table | U2 | deck 2 table |
| F7 | Write the fetch/decode microoperations with T-timing | U2 | deck 2, and it's the canonical exam item everywhere |
| F8 | Give the complete microoperation sequence for a named MRI (BSA / ISZ / ADD) | U2 | deck 2 lists all seven with D·T timing |
| F9 | **Derive LD/INR/CLR for a named register by scanning the RTL** | U2 | deck 2's "Control of Registers and Memory" — the AR worked example |
| F10 | Explain the interrupt cycle; give its register transfers | U2 | deck 2, 3 slides + a memory before/after figure |
| F11 | Hardwired vs microprogrammed control (table) | U3 | standard; deck 2 introduces the split explicitly |
| F12 | Decode / write a microinstruction given the F1 F2 F3 CD BR AD format | U3 | Mano ch. 7's central exercise |
| F13 | Explain mapping of a 4-bit opcode to a control-memory address | U3 | Mano ch. 7 (0xxxx00) |
| F14 | **Numerical: pipeline speedup given k, n, tₙ, tₚ** | U4 | deck 3 works a 4-stage / 100-task / 20 ns example to S = 3.88 |
| F15 | Space-time diagram for a k-segment pipeline over n tasks | U4 | deck 3 figure |
| F16 | Identify the hazard type in a given instruction pair + state the cure | U4 | deck 3's L19 outcome: "Differentiate different types of Pipeline Hazards" |
| F17 | Flynn's classification with one example system each | U4 | deck 3 |
| F18 | Compare strobe vs handshaking; draw the timing | U5 | Mano ch. 11 |
| F19 | Explain the three modes of transfer / DMA operation | U5 | L22 outcome |
| F20 | **Numerical: cache bit-split (tag/index/block/word) for a given configuration** | U6 | Mano ch. 12's 32K×12 / 512-word example |
| F21 | Numerical: hit ratio → average access time | U6 | standard |
| F22 | Compare direct / associative / set-associative mapping | U6 | Mano ch. 12 |
| F23 | 8086 architecture: BIU vs EU, jobs of each, the queue | U7 | L27 outcome, flipped-classroom |
| F24 | **Compute the physical address from a given seg:offset** | U7 | the single most-asked 8086 item in Indian UG papers |
| F25 | **For a given instruction, name the addressing mode and compute EA/BA/MA** | U7 | CO4 at 85% — expect several |
| F26 | Explain named assembler directives with examples (ASSUME, DB, DW, EQU, PROC…) | U7 | L33 outcome names "assembler directives" |
| F27 | **Write an 8086 ALP** (block move, sum of array, largest, string reverse, BCD↔binary) | U7 | **CO5 is L3 "Develop"** — the only doing-CO |
| F28 | RISC-V: why an open ISA; RV32I features; the register file | U8 | L35–L36 outcomes ("need & USP") |
| F29 | Identify/decode a RISC-V instruction format (R/I/S/U + B/J variants) | U8 | Patterson & Hennessy |

## 4a. Question forms now EVIDENCED by the professor's assignments — `settled` (added 2026-09-15)

Assignment 1 (200 marks) and Assignment 2 (150 marks) are first-party. They are **CWS** instruments, not
the MTE — so they settle *what the professor asks and how*, not the MTE mark split.

| Form | Where it appears | Promotes |
|---|---|---|
| Define 6 terms at 2 marks each (digital computer, architecture, organization, microarchitecture, microoperation, RTL) | A1 Q1 | F1 |
| Arch vs org · von Neumann vs Harvard · RISC/CISC short notes (10 marks each) | A1 Q2, Q6, Q20 | F1, F2 |
| **Generations of computers, tabulated with technology + people** | A1 Q3 | new |
| Functional units and their roles · types of computers | A1 Q4, Q5 | new |
| **Explain + draw from basic gates:** D FF, 3:8 decoder, 4:1 MUX, quad 2:1 MUX, 4-bit parallel-load register, 4-bit bidirectional shift register with parallel load | A1 Q7 (24 marks) | new — DE prerequisites are examinable here |
| Signed-magnitude / 1's / 2's representation; 8-bit 2's-complement addition | A1 Q8, Q9 | new |
| Classify register vs memory transfer; conditional RTL → block diagram | A1 Q10–Q12 | F3 |
| Bus: definition, role, five named standards; **common bus for 4×4-bit registers with MUXes and with tri-state + decoder** | A1 Q13, Q14 | F6 |
| **4-bit adder-subtractor with given M, A, B** | A1 Q16 | new |
| **Design 4-bit ALSU, explain named functions** | A1 Q17 (16 marks) | F4 — confirmed |
| Micro-operation sequence on 8-bit registers; shift sequence on R | A1 Q18, Q19 | F5 |
| Instruction-format bit sizing (memory size + register count) | A2 Q1 | new |
| **Bus control inputs ↔ register transfer, both directions** | A2 Q2, Q3 | F6 — confirmed |
| Binary instruction → hex → meaning | A2 Q4 | new |
| Timing diagram for one `D·T: SC ← 0` | A2 Q5 | F7 |
| **Register-contents trace after an RRI / an indirect MRI** | A2 Q6, Q7 | new |
| Fetch sequence for a non-BC machine (3-word instruction) | A2 Q8 | F7 variant |
| **JK control gates for a flip-flop from RTL** · **PC control gates LD/INR/CLR** | A2 Q9, Q10 | F9 — confirmed |
| Pipeline configuration + register table for an arithmetic expression | A2 Q11 | F15 |
| k + n − 1 · **delay-based speedup (tₚ, tₙ, S for two n, Sₘₐₓ)** | A2 Q12, Q13 | F14 — confirmed |
| Four hardware branch-handling schemes | A2 Q14 | F16 |
| FI-DA-FO-EX contents at step k | A2 Q15 | F15 |

**Two structural signals:** (1) ~~12~~ **ALL 15 of A2's items are verbatim Mano 3e end-of-chapter
problems** — corrected `[2026-09-23]` once the book itself became readable (`sources.md`); the earlier
count of 12 was taken from the solutions manual's answer list and missed **5-8** and **5-16**. Map:
Q1=5-1, Q2=5-3, Q3=5-4, Q4=5-6, Q5=5-8, Q6=5-9, Q7=5-12, Q8=5-16, Q9=5-20, Q10=5-21, Q11=9-1, Q12=9-3,
Q13=9-5, Q14=9-10, Q15=9-11. Sub-parts are sometimes dropped — those remain fair exam game.
**A1 is Mano-derived too, but adapted:** Q10←4-7, Q12←4-1 (`yT₃`→`yT₂`), Q14(i)←4-6 (16×32→4×4),
Q14(ii)←4-5, Q16←4-12 (rows a and d **unchanged**), Q18←4-19 (registers renamed, values identical),
Q19←4-21 (start value changed). **Consequence:** for U2/U4 the Mano problem *is* the question; for U1
it predicts the form and he moves the numbers. Full transcription: `../question-bank.md`.
(2) **U3 (microprogrammed control) appears in neither assignment** — its forms F11–F13 stay inference,
so **Mano ch. 7's 24 problems are U3's only question evidence** (in the question bank).

## 5. What would sharpen this map

Ranked by how much it would improve exam targeting:

1. **Any ECE2108 MTE or ETE paper** — would fix the per-question mark split; §4a (assignments) now
   evidences forms for U1/U2/U4 but not exam marks or U3. *Still the highest-value item.*
2. **The decks for L12–L36** — would confirm emphasis for U3 and all four ETE units, and resolve
   whether 8086 is taught from Bhurchandi's notation (BA/EA/MA) or Intel's.
3. **What CWS actually consists of** — 30 marks, currently unplannable.
4. **Confirmation of the MTE/ETE dates** — drives the review taper
   (`../../research-engine/exam-calendar.md`).
5. **Whether the instructor examines Mano's notation exactly** (e.g. `AC ← AC ∧ DR` with D·T
   subscripts) — affects how answers should be written, not what is true.
