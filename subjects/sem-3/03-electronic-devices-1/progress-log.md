# ECE2101 Electronic Devices-I — Progress Log

> Written **live** as sessions happen (log-first artifact pairing; never reconstructed at
> wrap-up). Session-resume block is overwritten each session-end; Session history is append-only.
> See `../../README.md`.

## Session resume
- Last session: 2026-11-13/14 — no teaching; inbox triage (21 professor files) + built `study-pack/pdf/EDC-ETE-v1.pdf` (63 pp., all 7 ECE2106 units).
- Where we stopped: pack delivered; learner has not worked any Check. ETE stated as about 2026-11-15.
- Next up: **rebuild the ETE pack to `study-pack-format.md` (v1.2)**, pilot file first; the v1 pack was rejected 2026-11-14.
- Due for review today: nothing yet (no items mastered).
- Open: U6 Feedback, U7 Oscillators and the deck extras are in the pack but not in `knowledge-base/` (no stage-2 research).

## Mastery ledger
*(empty — nothing mastered to criterion yet)*

## Spaced-review / relearning queue
*(empty — fills as items are mastered)*

## Session history
- [2026-07-05] Scaffolded (engine audit; no teaching): curriculum derived from 00-map,
  profile + this log initialized. KB state unchanged (`stage-2✓` since 2026-06-24).
- [2026-10-05] Inbox triage (no teaching): the professor's JFET-parameters slide (via a classmate's
  WhatsApp, captioned "8 marks") filed to `exam-pack/TIP-JFET-parameters-8marks-2026-10-05.md`.
  Gap found: KB `03-jfets.md` had g_m and r_d but **not g_d or μ, or μ = g_m·r_d**. Added them,
  checked by derivation. `exam-map.md` gets its first evidence row (U3, 8-mark item, `likely`).
- [2026-11-13] Inbox triage (no teaching): **22 files** uploaded by the learner to `../_inbox/_unsorted/`, all
  Electronic Devices. **21 filed** into `exam-pack/` under unit-ordered names (index: `exam-pack/README.md`).
  **1 deleted** (`jfet numericals (1).pdf`), a byte-identical copy of `jfet numericals.pdf` (same MD5). No other duplicates:
  all pairs compared by text overlap (max 30%, CB vs CE decks sharing a template); `finfet.pptx` and
  `finfet-1.pptx` are different decks on one topic, both kept. Scans (`jfet numericals.pdf`, `hpara numerical.pdf`) and the
  image-only `crystal.pptx` were read visually.
  **Scope finding:** slide 2 of the professor's intro deck prints the syllabus for **ECE 2106 Electronic Devices &
  Circuits** (2025-26 scheme), i.e. ECE2101's five units **plus Feedback topologies (U6) and Oscillators (U7)**.
  The KB has no U6/U7 files. The decks also teach topics outside the syllabus text that the KB doesn't cover: special diodes
  (LED, tunnel, photodiode), FinFET, BJT biasing + stability factor + bias compensation, h-parameter CE analysis,
  multistage/Darlington, CMOS logic gates. → The `stage-2✓` stamp covers the ECE2101 scope only; the ECE2106 delta is open
  (noted in `course-info.md` and `../research-engine/research-queue.md`). `knowledge-base/exam-map.md` gains an
  evidence block listing the decks per unit.
- [2026-11-13] Inbox triage, second drop: `crystal.pptx` (same MD5 as filed `slides-U7-crystal-oscillators.pptx`) and
  `Mosfet biasing and digital circuit.pptx` deleted as duplicates. The MOSFET deck has the same text as filed
  `slides-U4-mosfet-biasing-and-digital-circuits.pptx`; 15/21 images are identical and the 6 that differ (slides 10–12, 15) are
  re-renders of the same equations, checked side by side. Filed copy kept.
- [2026-11-13] Learner request (stated): "make me the ete combined study ready pdf, lets start only with one subject edc". Answers to
  the three scoping questions: format = "v1 pdf format for now" (the `04-digital-electronics/study-pack/pdf/DE-v1.pdf` build: A4,
  Q → guess → figure → answer → Check); scope = all 7 ECE2106 units, equal depth; time = "more like 2 days, take 20-24 hours" (ETE
  ≈ 2026-11-15, exact date not given). Learner level: zero in ED (stated 2026-10-31, lab-pack request). Building
  `study-pack/pdf/EDC-ETE-v1.pdf`. U1–U5 facts from the `stage-2✓` KB; **U6 Feedback, U7 Oscillators and the deck extras are
  not in the KB** → pack built for them on learner request without stage-2 research (same exception shape as ECE2104/MEE2003
  packs), every formula checked by derivation/numerical simulation in `verify.py`. **No teaching event.**
- [2026-11-13] `study-pack/pdf/EDC-ETE-v1.pdf` **partly built: Parts A–E (Units 1–5)**: A semiconductor physics (A1–A6), B pn junction + diode circuits
  (B1–B9), C JFET (C1–C5), D MOSFET (D1–D6), E BJT (E1–E7). Each concept = Q (professor's deck/numerical sheet where one exists, else "practice")
  → guess → figure → teaching → answer → Check; Check answers end each Part. `verify.py` passes (177 checks). Deck slip flagged in the PDF: L08 slide 5
  prints V_R = 18.5 V (R is 0.5 kΩ → 9.25 V). Source = `parts/*.html` + `figs*.py` + `build.py`.
  **Not built yet (session hit its usage limit):** Part F feedback, Part G oscillators, mock paper, formula sheet. Their figures are already drawn in
  `figs3.py` and their numbers are already in `verify.py`. Parts A–D pages were viewed; **Part E pages have not been viewed after the build.**
  **Where we stopped:** write `parts/F.html`, `parts/G.html`, `parts/H.html` (mock + formula sheet), view Part E–H pages, then README + commit. **No teaching event.**
- [2026-11-14] `study-pack/pdf/EDC-ETE-v1.pdf` **complete: 63 pages, A4.** Added Part F feedback (F1 gain with feedback, F2 four topologies, F3 effects),
  Part G oscillators (G1 Barkhausen, G2 RC phase-shift, G3 Wien bridge, G4 Hartley/Colpitts, G5 crystal), a mock paper (19 Qs, 80 marks, laid out on the
  MAS2001 blueprint because no ECE2106 blueprint exists; 5 unused professor-sheet items: Q6, Q29, Q31, h-parameter Problem 3) with key, a formula sheet and
  sources. `verify.py` passes (211 checks). Second deck slip flagged in the PDF: feedback slide 32 prints 98.3 for A = 5000 (formula gives 98.0).
  All pages viewed after the final build. `study-pack/README.md` written. **No teaching event; mastery ledger and review queue unchanged.**
  **Where we stopped:** pack delivered; learner has not worked any Check. Open: U6/U7 + deck extras still absent from `knowledge-base/` (pack-only).
- [2026-11-14] Learner verdict (stated) on the v1-format packs: "this isnt really what i wanted … v1 isnt good at all"; the expected shape is the
  Circuits & Systems pack. Format written down as `study-pack-format.md` (v1.2) at the project root. `study-pack/pdf/EDC-ETE-v1.pdf` is listed there as
  **non-conforming** (one question and one Check per topic, no ranked start page, no Exam form/Traps/Self-test); its questions, figures and
  `verify.py` are sound and will be reused in the rebuild. README marked. Rebuild not started. **No teaching event.**
- [2026-11-14] Learner request (stated): "start with electronic devices … build a demo for both subjects first", without the cost of a
  full rebuild. Building the v1.2 demo (`study-pack-format.md`): `study-pack-v12/` = `00-START-HERE` + one topic file (`07-jfet`),
  rendered by the shared builder `tools/study_pack_build.py` (copied from the reference pack's own build script). Figures, questions
  and numbers reused from the v1 pack and its `verify.py`. Awaiting learner sign-off before the rest. **No teaching event.**
- [2026-11-14] v1.2 demo **built**: `study-pack-v12/pdf/` = `00-START-HERE` + `07-jfet (6 steps)` + combined PDF (4 + 9 = 13 pp.). Every step has a
  question or Predict, a guess line and a Check; Exam form, Traps, Self-test, Answers at the end. All numbers are ones the v1 `verify.py` already checks
  (plus one new g_m value / Gray-step check, hand-verified). All pages viewed. **Awaiting learner sign-off; no teaching event.**
- [2026-11-15] Learner signed off both v1.2 demos ("looks good to me, do for the entire file and do make the final combined pdf"). Full v1.2 build started: files 01–06, 08–15 in START-HERE priority order, content reused from `study-pack/pdf/parts/A–H.html` + `verify.py` numbers; combined PDF at the end.
- [2026-11-15] Full v1.2 EDC pack **built**: `study-pack-v12/pdf/` = 00 + files 01–15 (07 from the demo; 01–06, 08–15 new, content from v1 parts A–H, numbers from v1 `verify.py`; new Self-test numbers recomputed in Python) + combined `ECE2106-EDC-ETE-study-pack.pdf` (98 pp.). Shared builder `tools/study_pack_build.py` gained the `.two` two-figure grid. Pages of 04 and 09 viewed. **No teaching event.**
- Where we stopped: EDC v1.2 pack delivered; learner has not worked any Check. Next: DE v1.2 full build.
