# MEE2003 Engineering Economics — Progress Log

> Written **live** (log-first artifact pairing; never reconstructed at wrap-up). Session-resume block
> is overwritten each session-end; Session history is append-only. See `../README.md`.

## Session resume
- Last session: 2026-09-25 (no teaching).
- Status: **folder created by inbox triage only. No knowledge base, below `stage-1`.** Not teachable
  (teaching gate: `stage-2✓`). Research has not been started.
- Where we stopped: `study-pack/` being built (see Session history).
- Next up: learner decides whether to activate MEE2003 for research. When activated, the prof decks in
  `exam-pack/` set **scope and emphasis**. Facts come from the prescribed textbook (Panneerselvam,
  *Engineering Economics*, PHI), never from the slides.
- Due for review today: nothing.
- ⚠ **[2026-09-25] Learner-requested study pack without research (same shape as the ECE2104 exception
  of 2026-09-24):** "sort and remove duplicates and make me a study pack with assignment centered format."
  The `stage-2✓` gate is not met and is **not** being met. No assignment has been uploaded, so the
  question base is the **professor's own problems**: deck numericals, the L13 EOQ practice sheet, and
  the handwritten L14–19 notes. Accuracy guard: standard textbook content only, and **every number is
  re-computed by script** (`verify` run logged below). Slide errors found this way are flagged in the
  pack, not copied.

## Mastery ledger
*(empty)*

## Spaced-review / relearning queue
*(empty)*

## Session history
- [2026-09-25] **Folder created by `_inbox/` triage.** 17 files in `_inbox/_unsorted/`, all "Engineering
  Economics" (course hand-out code **MEE2003**; decks still carry the old footer "ME2001"/"ME 2003").
  MEE2003 fills the "Principles of Management / Engineering Economics" slot of the learner's **2025-26
  scheme** (`../research-engine/research-queue.md`, scheme table). Numbered `14-` (append order, not a
  scheme position). Hand-out: session 2026-27, coordinator Dr Ramanpreet Singh; decks by Dr Sanjeev
  Jakhar. **MTE 30 / CWS 30 (quiz, assignment) / ETE 40.** **MID TERM EXAM printed after L24** (L1–L24 =
  economics basics, demand/supply, elasticity, decision making, estimates, EOQ, payback, TVM, NPV, IRR,
  cost analysis, LCC, break-even). Textbooks: Panneerselvam (T1), Riggs et al. (T2), P.L. Mehta (T3).
- [2026-09-25] **Duplicate check** (md5, then word-level text diff, then content comparison). No two files
  were byte-identical. **4 files were strict subsets of a newer file and have been deleted** (learner
  asked for duplicates to be removed):
  - `Estimation and its types_L10-12.pdf` (2025, 32 pp., A. Joshi) ⊂ `Engg. Economics_Lecture_10-12 new.pdf`
    (2026-08-24, 37 pp.). The new deck adds the accuracy ranges, the Delhi–Mumbai and web-app ROM
    examples, and 2 parametric numericals. Everything else is reworded.
  - `EOQ_L13.ppt` (legacy binary) ⊂ `Engg. Economics_Lecture_13.pdf` (2026-08-27, 17 pp.). Every slide's text is
    present in the PDF, which adds inventory types, costs, control systems and the battery example.
  - `Engg. Economics_Lecture_Payback.pptx` (21 slides, modified 2026-02-12, A. Srivastava) ⊂
    `Engg. Economics_Lecture_NPV,IRR_L14-19.pdf` (2026-09-09, 37 pp.). Same slides, and the PDF adds
    the furnace, payback+NPV, real-estate and IRR-interpolation problems.
  - `Engg. Economics_Lecture_13_EOQ practice Ques.docx` ⊂ `EOQ practice Ques.docx`. The texts are identical
    except that the kept file adds one line (`Re Order Point (ROP)= Demand Rate X Lead Time`).
  **Not a duplicate, kept:** `Estimation models_L14-19.pdf`. It is a scanned handwritten notebook (NAPS2,
  2025-03-27, 11 pp.) on the L14–19 content, and it adds 2 problems the deck lacks (₹150000/₹50000 NPV;
  8-year variant of the real-estate problem).
- [2026-09-25] 13 remaining files moved + renamed into `exam-pack/`. Triage lines appended to
  `../_inbox/TRIAGE-LOG.md`.
- [2026-09-25] **Numerical verification run** (Python, exact fractions for the equilibrium problems).
  Every worked answer in every deck, the EOQ sheet and the notes was recomputed. **Slide errors found:**
  1. **L8-9 cloud-hosting example:** the slide gives EAC(B) = ₹1,40,000 and chooses B. From the slide's
     own data, EAC(B) = 84,000 + 2,50,000 × (A/P, 10%, 3) = 84,000 + 2,50,000 × 0.40211 = **₹1,84,529**, which is
     **more** than A's ₹1,80,000, so **A is cheaper at 10%**. Even with no interest, B = ₹1,67,333, not 1,40,000.
  2. **L14-19 Project A vs B NPV:** the slide gives NPV A = $780.18 and NPV B = $1052.19. The correct values are
     **A = $788.20, B = $1004.03**. The B year-3 PV should be 4000/1.331 = 3005.26, not 3053.43. The
     choice (B) is unchanged.
  3. **L14-19 equipment IRR:** the slide's NPV₁₃ = +9,635 and NPV₁₄ = −6,774 are wrong. The correct
     values are **+6,581 and −4,202**. The final IRR ≈ **13.61%** is right, provided the ₹50,000 salvage
     arrives in year 4. The handwritten notes put the salvage in year 5, which gives **13.28%** (notes: 13.27%).
     The two sources read the question differently.
  4. **Minor slips:** EOQ sheet Q1 writes `(1200*100)/20` for (1200/100)×20 (the result, 240, is right).
     EOQ sheet Q3 says "0.16%", which should be **16%**. L3 says Pepsi and Coke are "both priced at Rs. 90
     and Rs. 20". L6 explains a negative cross elasticity using "income" where it means the price of Y.
  Everything else checks out exactly (all 4 equilibrium problems, the 3 elasticities, every EOQ, payback, ROR,
  PV, furnace, real estate, machine IRR 15.24% exact / 15.26% interpolated).
- [2026-09-25] Building `study-pack/`, question-first (ECE2108-v3 / ECE2104 shape). **With no assignment
  uploaded, "assignment-centred" is implemented as follows:** every professor-set problem (deck
  numericals, EOQ sheet, notes) is quoted, then answered in place, and a question→file table sits in
  `00`. Planned files: 00 start-here · 01 economics basics + demand/supply theory (L1–3) · 02 equilibrium,
  tax, subsidy (L4–5) · 03 elasticity (L6–7) · 04 economic decision making (L8–9) · 05 types of estimates
  (L10–12) · 06 EOQ (L13) · 07 payback + ROR · 08 TVM + NPV · 09 IRR (L14–19) · 10 mock MTE. **Gap:** L20–24
  (cost elements, LCC, project financing, break-even) are on the MTE per the hand-out, but no deck for
  them has been uploaded.
