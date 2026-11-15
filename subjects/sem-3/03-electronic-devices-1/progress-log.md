# ECE2101 Electronic Devices-I — Progress Log

> Written **live** as sessions happen (log-first artifact pairing; never reconstructed at
> wrap-up). Session-resume block is overwritten each session-end; Session history is append-only.
> See `../../README.md`.

## Session resume
- Last session: 2026-11-15 — no teaching. No misses reported on 01a/01b. Rebuilt `02-carrier-transport` at the 01a/01b depth as `02a-drift` (9 steps, 12 pp.) + `02b-diffusion-continuity` (13 steps, 18 pp.); new `src/figs_u2.py` + `src/verify_u2.py` (97 checks pass); combined PDF now 141 pp. Deck slips flagged: slide 64 (J_p = +qF_n → +qF_p), slide 65 (hole diffusion term sign). KB stage-2 §11 gained the Si mobility-vs-doping fit (web-checked).
- Where we stopped: 2026-11-16 built `study-pack-v12/cheatsheet/pdf/EDC-U1-U2-formula-cheatsheet.pdf` (27 pp.: Unit 1 F1–F20, 16 pp.; Unit 2 F21–F37, 11 pp.); pages viewed. Learner has not worked any card yet.
- Next up: (1) learner's misses on the cheat-sheet cards and 01a–02b, if any; (2) ask the learner before rebuilding `03-pn-junction` at the same depth.
- Due for review today: nothing yet (no items mastered).
- Open: U6 Feedback, U7 Oscillators and the deck extras are in the pack but not in `knowledge-base/` (no stage-2 research). Push is blocked in-session; learner runs `! git push`.

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
- [2026-11-15] Full v1.2 EDC pack **built**: `study-pack-v12/pdf/` = 00 + files 01–15 (07 from the demo; 01–06, 08–15 new, content from v1 parts A–H, numbers from v1 `verify.py`; new Self-test numbers recomputed in Python) + combined `ECE2106-EDC-ETE-study-pack.pdf` (97 pp.). Shared builder `tools/study_pack_build.py` gained the `.two` two-figure grid. Pages of 04 and 09 viewed. **No teaching event.**
- Where we stopped: EDC v1.2 pack delivered; learner has not worked any Check. Next: DE v1.2 full build.
- [2026-11-15] Learner feedback (stated) on `study-pack-v12/.../01-semiconductors`: "a bit too compressed … at fermi levels, i have 0 idea whats even going on … Nc and Nv are not even explained properly, i dont understand the graph much, what is it trying to graph? … edc will need much more depth … lets only do the 01 unit for now". Diagnosis: step 3 merged five ideas (f(E), density of states, N_C/N_V, the n/p formulas, E_F shift) into one step, against spec §5 ("ideas are never merged"); N_C/N_V got a one-phrase gloss; the f(E) figure never said what its axes mean. Rebuilding 01 at full depth, split in two files per spec §2 (long topic → two files): `01a-silicon-bands-carriers` (atoms, bonds, electron/hole, bands, n_i(T), donors, acceptors, mass action) and `01b-fermi-level` (states, f(E) read point by point, density of states, n = ∫g·f, Boltzmann approximation, N_C/N_V, np = n_i², E_F at mid-gap, E_F with doping). Order follows deck slides 3–40. Facts from `knowledge-base/01` + `stage-2/01`; numbers checked by a new `src/verify_u1.py`. Old `01-semiconductors` source/HTML/PDF removed once replaced. Deck slips found: slide 36 writes pn = N_VN_C e^{−2E_F/kT} (correct: e^{−E_g/kT}, no E_F); slide 38 says "at equilibrium N_C = N_V" (it is an approximation, not a consequence of equilibrium). **No teaching event.**
- [2026-11-15] KB gap found while rebuilding 01: values the deck uses but the KB lacked (Si DOS effective masses 1.08/0.56 and N_V = 1.04×10^{19}; n_i of Ge and GaAs; shallow-dopant binding energies P 45, As 54, B 45 meV). Checked by web search 2026-11-15 (Hu ch1 slides; URI/eesemi property tables; dmccreary course page; boron 45 meV from the deck and Sze, not independently confirmed this session). Appended to `knowledge-base/stage-2/01-semiconductor-physics.md` §11 + CHANGELOG line.
- [2026-11-15] 01 rebuild **done**: `study-pack-v12/pdf/01a-silicon-bands-carriers.pdf` (8 steps, 11 pp.) and `01b-fermi-level.pdf` (10 steps, 13 pp.); old `01-semiconductors` source/HTML/PDF removed; START-HERE rows + Unit 1 map and the 02 header updated; combined PDF rebuilt (115 pp.). New `src/figs_u1.py` (15 figures, each caption says what the graph plots) and `src/verify_u1.py` (all checks pass). Both files run longer than spec §2's 4–8 pages; the learner asked for depth. Every page of 01a/01b viewed after the build; label overlaps fixed. Spec §5.4 amended (every graph says what it plots; symbols explained) + `learner-preferences.md` §3 line. **No teaching event.**
- Where we stopped: 01a/01b delivered for the learner to work through; no Check worked yet. Next: learner's misses on 01a/01b, then 02 (rest of syllabus Unit 1) at the same depth if asked.
- [2026-11-15] Learner sign-off on the rebuilt 01a/01b (stated): "this looks good". Session ended at learner request ("the session is getting too long"); handoff prompt given for the next session (02 rebuild at the same depth).
- [2026-11-15] Session start (learner prompt): no misses reported on 01a/01b. Task: rebuild `02-carrier-transport` at the 01a/01b depth, split as `02a-drift` (thermal motion, mobility, velocity saturation, μ vs doping/T, drift current from flux, σ/ρ deck example slide 51, effect of doping slide 52, resistance of a bar, sheet resistance) and `02b-diffusion-continuity` (diffusion spreading, Fick's law, diffusion current signs, total current, equilibrium balance, Einstein relation slide 57, G–R, direct, trap/SRH, lifetime, continuity slides 62–64, diffusion length, Poisson slide 65). Order = deck slides 43–65 (read as images: slides 46–65 are pictures). New `src/figs_u2.py`, `src/verify_u2.py`. Deck slips found: slide 64 writes J_p = +qF_n (should be +qF_p); slide 65 (pveducation screenshot) writes J_p = qμ_p pE **+** qD_p dp/dx (diffusion term must be **−**; slide 55 has it right). Slide 52's σ = 32 for N_D = 5×10^17 implies μ_n = 400, not 1500: used in the pack as the mobility-falls-with-doping example. **No teaching event.**
- [2026-11-15] KB gap found while rebuilding 02: the doping-dependent mobility curve (deck slide 48) had no numbers in the KB (stage-2 §6 names the Caughey–Thomas form only). Checked by web search 2026-11-15: MINIMOS/Caughey–Thomas Si parameters, electrons μ_max 1430, μ_min 80, N_ref 1.12×10^17, α 0.72; holes 460, 45, 2.23×10^17, 0.72 (TU Wien Palankovski thesis Table 3.22 for μ_min/N_ref/α; nextnano MINIMOS page for μ_max). Fit gives μ_n(5×10^17) ≈ 420, consistent with deck slide 52's implied 400. Appended to `knowledge-base/stage-2/01-semiconductor-physics.md` §11 + CHANGELOG line.
- [2026-11-15] 02 rebuild **done**: `study-pack-v12/pdf/02a-drift.pdf` (9 steps, 12 pp.) and `02b-diffusion-continuity.pdf` (13 steps, 18 pp.); old `02-carrier-transport` source/HTML/PDF removed; START-HERE rows, Unit 1 map, rank-10 row, slip table (+ deck slides 64, 65) and "how checked" line updated; 03 header and cross-references in 01a, 03, 06 point to 02a/02b; combined PDF rebuilt (141 pp.). New `src/figs_u2.py` (19 figures, each graph's caption says what its axes are and what a point means) and `src/verify_u2.py` (97 checks, all pass; `verify_u1.py` still passes). Every page of 02a/02b viewed after the build; fixed: random-walk seeds (no-field walk had visible drift), literal "μ_n" in figure labels, five label/curve overlaps, dangling "Answer." labels in 02a steps 6–7. 02b runs past spec §2's 4–8 pages (learner asked for 01a/01b depth). **No teaching event.**
- Where we stopped: 02a/02b delivered; no Check worked. Next: learner's misses on 01a–02b, then ask before rebuilding 03 at the same depth.
- [2026-11-16] Learner request (stated): low energy; "make me a cheat sheet question per formula building my understanding … defining each term … graphs and diagrams", then narrowed: "use the pdf u created and only do unit-1 and unit-2". Building `study-pack-v12/cheatsheet/` (own src → html/pdf, so the pack's combined PDF is untouched): one card per formula from v1.2 files 01a–06, each = question → formula → every term defined → pack figure → answers at the end of the unit. Numbers recomputed in `cheatsheet/verify.py` (72 checks pass). One rounding fix vs 03 Check 1: V_{bi} = 0.775 V, not 0.774. **No teaching event.**
