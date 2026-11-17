# ECE2102 Digital Electronics — Progress Log

> Written **live** as sessions happen (log-first artifact pairing; never reconstructed at
> wrap-up). Session-resume block is overwritten each session-end; Session history is append-only.
> See `../../README.md`.

## Session resume
- Last session: 2026-11-14 — no teaching; built `study-pack/pdf-ete/DE-ETE-v1.pdf` (61 pp., all 5 units, EDC-ETE-v1 format).
- Where we stopped: v1.3 rebuild S0–S5 done (00–03, 05, 06, 09, 10, 12, 13, 15, 16 rebuilt); learner has not worked any Check. **No teaching yet; learner level undiagnosed.**
- Next up: **Study-pack rebuild to v1.3 runs in sprints: resume from `sprints.md` → *Current hand-off*** (S0–S9; next: S6, files 04 + 07 + 08; `python auto.py run sem-3/04-digital-electronics`).
- Due for review today: nothing yet (no items mastered).
- Open: ETE date and format not given; no memory deck from the professor (E6 is built from the KB).

## Mastery ledger
*(empty — nothing mastered to criterion yet)*

## Spaced-review / relearning queue
*(empty — fills as items are mastered)*

## Session history
- [2026-07-05] Scaffolded (engine audit; no teaching): curriculum derived from 00-map,
  profile + this log initialized. KB state unchanged (`stage-2✓` since 2026-06-27).
- [2026-09-11] Inbox triage (no teaching): **first exam material received.** 11 files routed from
  `../_inbox/_unsorted/` into `exam-pack/` — professor's 8-deck slide set (syllabus + K-map +
  adders + MUX/demux + decoder/encoder + comparator/parity + shifter/ALU + sequential/FFs), one
  partial merged deck (decks 1-5), the **MTE PYQ (25-Sep-2025, 30 marks / 90 min)**, and a
  10-question practice set (combinational). Triage-log: `../_inbox/TRIAGE-LOG.md`.
  **Code discrepancy logged:** slide deck header reads **ECE 2105**, MTE paper + KB read
  **ECE2102** — same syllabus text; treated as a stale code on a reused deck, marked `uncertain`.
  Next artifact: `knowledge-base/exam-map.md` rebuilt from this evidence (was an inferred stub).
- [2026-09-11] `knowledge-base/exam-map.md` **rebuilt from evidence** (was an inferred stub):
  MTE structure settled (30 marks/90 min; Sec A 3x2 "memory", Sec B 4x4 "concept", Sec C 1x8
  "analytical"); **MTE scope resolved to U1 + U2 + U3-through-counters** (U4/U5 absent, corroborated
  by the decks stopping at flip-flops); 11 verified question patterns P1-P11 cited to paper/practice
  items; per-unit weights re-rated; teaching order re-set to K-map+constrained-realization ->
  MUX/decoder -> FFs/waveforms/counter design. Next artifacts: KB CHANGELOG + research-queue row.
- [2026-09-11] Learner request: **exam-ready study files (.md) to self-study from**, MTE scope,
  built to the universal preferences (ASCII math, scannable, flow-map-first, feed-big). Building
  `study-pack/` (10 files: 00 start-here/flow map, 01 Boolean+K-map, 02 NAND/NOR realization,
  03 adders/subtractors/parity, 04 MUX/demux, 05 decoder/encoder/7-seg, 06 comparator/shifter/ALU,
  07 flip-flops+waveforms, 08 counter design, 09 drill set). **Tension named to learner and logged:**
  passive reading is not studying -> every file is question-first with answers separated to the
  bottom, so the mechanism (retrieval) survives the format. Content sequenced by the 2026-09-11
  exam-map scoring order; facts from the Stage-1/Stage-2 KB, framing from the prof decks + PYQ.
- [2026-09-11] `study-pack/` **built — 10 files, ~3,465 lines**, all MTE scope. Every file is
  question-first (Map -> Attempt -> Method -> Worked -> Traps -> Self-test -> Answers-at-bottom);
  ASCII math throughout (no LaTeX, verified by grep); small per-file maps, not one dense tree.
  All 8 MTE-2025 questions and all 10 practice-set questions solved and verified by substitution;
  7-segment equations checked digit-by-digit against the display table. **No teaching event —
  nothing taught, nothing assessed, mastery ledger and review queue unchanged.**
- [2026-09-11] **Where we stopped:** study-pack delivered; learner has not yet worked any drill.
  Next session: start-of-session recall, then a live diagnostic against Drill A Section B to place
  level before teaching (`curriculum.md` U1 entry), scoring order per `knowledge-base/exam-map.md` §5.
- [2026-09-11] Learner correction (stated): study-pack spelled out `Sigma-m`/`Pi-M`/`(+)` instead
  of the real symbols — "costing me precious processing time". Fixing all 10 files to Σm / ΠM / ⊕
  (+ ≥, superscript exponents, log₂). Not a conflict with the ASCII-math rule: that rule bans
  **TeX** (`$...$`, rac), not Unicode symbols, and the KB already used Σm. Rule logged to
  `learner-preferences.md` §3 as a hard standing rule for every generated document.
- [2026-09-27] Learner request: a **personal study website** (free, own site; GitHub Pages),
  pictorial, "basic demo then iterate" — DE chosen as the pilot. Building a figure-first web
  version of `study-pack/01-boolean-kmap.md` in `study-pack/web/` (content + figures.py) plus a
  root `site/` generator (home → subject → chapter). Answers behind click-to-reveal so the
  attempt-first mechanism survives. Engine design context: `_PARKED-visual-study-packs.md` (D2 → B
  for the site). **No teaching event.**
- [2026-09-27] Web demo **built**: `study-pack/web/` = `content/01-boolean-kmap.md` (figure-first
  rewrite of study-pack 01: Venn laws, Σm/ΠM strip, K-map layout with wrap arcs, group-size and
  legal/illegal strips, don't-care and POS maps, Q1 NOR inverter, Q4 click-through grouping +
  circuit, 6 self-test answers behind reveals with K-map figures) + `figures.py` + `meta.json`;
  `verify.py` passes (every answer + every drawn group machine-checked). Site generator at root
  `site/` (home → subject page with exam-split bar + clickable learning path → chapter). Checked by
  screenshot at desktop and 390px. Not yet deployed (needs a public repo). **No teaching event.**
- [2026-09-27] Learner feedback on the demo (stated): "too much info dump" on first look; wants the
  landing to be a **map of everything in the material**, colour-coded; **one concept at a time**;
  no sidebar; one page where clicking a concept **zooms into it** and shows its content. Rebuilt
  the site as a zoomable subject map: 9 chapter islands (hue = stage: foundations / building
  blocks / memory / drill), 76 concept nodes (badge = kind: idea, method, exam, trap, practice;
  outline titles for ch 2-9 from the text study pack, marked "not drawn yet"), click chapter →
  zoom, click concept → card grows out of the node, ◀ ▶ + progress pips walk the order, Esc /
  Back zooms out; phone view = ring + concept list sheet. Ch1 content split into 13 concept cards,
  added quick-check reveals + a 5-variable demo figure; `verify.py` passes. **No teaching event.**
- [2026-09-27] Learner feedback on the map (stated): "not tree like enough"; leaf-only sets should
  be lists; show how concepts **build on** each other; **minimalistic**, nothing tacky; the key is
  the balance of information vs overwhelm. Rebuilt as a tree: subject → stage → chapter → group →
  concept. Landing = 4 stages + 9 folded chapters (number, exam-weight bars, concept count). Open
  a chapter → its branch grows; groups either fan out (independent) or draw a spine with dots
  (each builds on the one above); hovering a concept highlights what it builds on; card shows
  path + "Builds on" links + prev/next. Phones: indented outline. Old radial map removed. Ch1 tree
  + needs in `meta.json`, ch2-9 outlined as groups/sequences. **No teaching event.**
- [2026-09-28] Learner (stated): "i like this … i want this format to be the site-v1, note
  everything down". Format frozen as **site-v1**: full spec written to `site/SITE-V1.md` (tree
  hierarchy, fan/spine/list encoding, behaviour, minimal visual language, card rules, authoring,
  code map, version history); git tag `site-v1`; README, parked design doc, universal preferences
  (§3) and CLAUDE.md file map point at it. **No teaching event.**
- [2026-10-17] Learner request (stated): "lets finish it … use the course handout and the high
  quality stuff online and make me a v1 pdf … finish up digital electronics tonight." No new
  professor material (no decks past flip-flops, no ETE paper). Building **study-pack PDF v1** =
  the un-packed ETE half — U3 remainder (ripple/mod-N counters, shift registers, ring/Johnson,
  timing analysis), U4 (FSM design, state reduction, timing issues, ASM, pulse-train/PRBS/clock
  generation, async circuits), U5 (TTL specs/noise margin/fan-out, tristate, ECL, CMOS +
  interfacing, memories, PLDs) — plus a one-section recap sheet of the MTE half. Scope = the
  syllabus in `exam-pack/slides-01` (course hand-out text); facts from the stage-2✓ KB; questions
  sourced from real papers (GATE/university) where found, else marked textbook-style. Output:
  `study-pack/pdf/DE-v1.pdf` + its HTML source + figure script. **No teaching event.**
- [2026-10-17] `study-pack/pdf/DE-v1.pdf` **built — 29 pages, A4**: cover flow map → Part A MTE recap
  sheet (4 recall tables) → Part B U3 rest (B1 ripple/mod-N, B2 shift registers, B3 ring/Johnson, B4
  timing) → Part C U4 (C1 Moore/Mealy, C2 010 detector Mealy+Moore, C3 state reduction, C4 timing
  issues, C5 ASM, C6 LFSR/pulse train/555/ring osc, C7 races + hazard-free realization) → Part D U5
  (D1 NM/fan-out, D2 TTL totem pole, D3 tristate, D4 ECL + family table, D5 CMOS + interfacing, D6
  memories, D7 PLDs) → mock paper (13 real questions) + key. Every concept is Q (quoted, sourced,
  marks) → guess line → figure-first teaching → answer → Check; Check answers at the end of each Part.
  **Question sources (real):** Anna Univ. EC6302 Apr/May 2015 (QP 77112) + Nov/Dec 2021 (QP 70427),
  EC1201 Nov/Dec 2021 (QP 86565), RTU 3E2075 (2012). B4, C3, C4, C6, D2 have no real item found →
  labelled "practice". **All worked answers machine-checked by `study-pack/pdf/verify.py`** (010
  Mealy/Moore equations + simulation, hazard-free cover, LFSR period 7, Johnson mod-8, partition
  7→5, PLA shared term, EC1201 counter D-equations + self-start, f_max, fan-out, 555, ring osc).
  ECL noise-margin levels flagged illustrative (10K-class; not datasheet-verified). Images: 4
  Wikimedia Commons schematics (7400 TTL, CMOS inverter, CMOS NAND, 6T SRAM; licences printed),
  rest generated. Source = `content.html` + `figs.py` + `build.py`. **No teaching event —
  nothing assessed; mastery ledger and review queue unchanged.**
- [2026-10-17] **Where we stopped:** DE-v1.pdf delivered; learner has not worked any Check yet.
  Next session: start-of-session recall, then run the mock paper (Section C first) as the diagnostic.
- [2026-10-17] Learner verdict on DE-v1.pdf (stated): "feels very disconnected … starts from a random
  place … expected to know alot before hand … all the shit i … tried to build … feels like non of it is
  there, especially the visual weight and attention thing … make a v2, maybe just a demo". Diagnosis:
  v1 ignored the site-v2 river rules (staircase map, priming ≤3 terms, one concept in focus, edges as
  bridge content, visual-load budget) and the 2026-09-15 define-before-use rule. Building
  `study-pack/pdf-v2/` = **one-chapter demo** (registers → shift registers → ring → Johnson →
  decoding/lock-out, ending on the Anna 2015 Q13(b)(i) Johnson question), river-shaped, starting
  from the D flip-flop, one idea per page, with a mechanical per-page load test. **No teaching event.**
- [2026-10-17] `study-pack/pdf-v2/DE-v2-demo.pdf` **built: 47 landscape pages, one chapter**
  ("Shift registers & shift counters"). It opens on the Anna 2015 Q13(b)(i) Johnson question, then
  a where-it-sits staircase, then 6 stops (D flip-flop → register → shift register → ring → Johnson
  → decode + lock-out). Each stop = staircase map + ≤3 priming terms → guess → idea pages → check →
  answer on the next page; a bridge page between stops; it closes with the exam question again, an
  answer outline mapped to stops, and a connects-to page. Load test passed (worst page 74 words,
  budget 75; ≤1 figure per page). Awaiting the learner's verdict before scaling to other chapters.
  **No teaching event.**
- [2026-11-13] Inbox triage (no teaching): `_inbox/_unsorted/OneDrive_1_11-13-2026.zip` (9 files) unzipped. **8 filed** into `exam-pack/`:
  the professor's decks 9–15, which continue the 1–8 set (`slides-09-registers-shift-registers`, `slides-10-counters`, `slides-11-fsm-sequential-circuit-design`,
  `slides-12-state-reduction`, `slides-13-asm-charts`, `slides-14-logic-families`, `slides-15-plds`), plus `practice-set-02-flipflops-counters.png`
  (6 Qs: D-FF from SR/JK/T, D/JK latch timing, JK negative-edge waveforms with CLR/PR, 2-bit sync up counter, 2-bit sync down with TFF,
  3-bit sync down with DFF). **1 dropped:** `MTE PPR.pdf`, same MD5 as the filed `PYQ-MTE-2025-09-25.pdf`. KB grep found every deck topic
  already covered in `03`/`04`/`05` (+ stage-2). Closes the "missing decks" gap in `exam-map.md` §6, except memories. Index written to `exam-pack/README.md`.
- [2026-11-13] `exam-pack/slides-merged-01-05.pdf` (232 pp.) deleted under the learner's rule "exact same page for page → remove". It was
  compared with decks 01–05 in order: 232/232 pages have identical text, identical embedded images (MD5) and identical rendered pixels.
  Restorable from git history.
- [2026-11-14] Learner request (stated): "lets do digital electronics ete study-ready pdf, make it the same as the last one which was
  electronic devices". Building `study-pack/pdf-ete/DE-ETE-v1.pdf` in the EDC-ETE-v1 format (parts/*.html + figs*.py + verify.py + build.py;
  Q sourced → guess → figure → teaching → answer → Check; Check answers end each Part; mock paper + key; formula sheet). Scope = all 5
  syllabus units, from zero. Questions from the professor's decks 01–15, the 2025 MTE paper and the two practice sets where they have one,
  else labelled "practice". Facts from the `stage-2✓` KB. **No teaching event.**
- [2026-11-14] `study-pack/pdf-ete/DE-ETE-v1.pdf` **built: 61 pages, A4.** Part A Unit 1 (A1 Boolean algebra, A2 canonical forms, A3 K-map, A4 POS + 5 variables,
  A5 NAND/NOR, A6 half/full adder + subtractors, A7 ripple/CLA/adder-subtractor, A8 serial + BCD adder), Part B Unit 2 (B1 MUX, B2 decoder/DEMUX, B3 encoder,
  B4 7-segment + multiplexed display, B5 comparator, B6 parity, B7 shifts + barrel shifter, B8 ALU), Part C Unit 3 (C1 latches, C2 flip-flops, C3 excitation +
  conversion, C4 waveforms, C5 shift registers, C6 ring/Johnson, C7 ripple counters, C8 synchronous counter design, C9 timing), Part D Unit 4 (D1 Moore/Mealy,
  D2 1101 detector, D3 state reduction, D4 ASM, D5 timing issues, D6 generators, D7 asynchronous), Part E Unit 5 (E1 yardsticks, E2 TTL NAND, E3 tristate,
  E4 ECL + comparison, E5 CMOS + interfacing, E6 memories, E7 PLDs), mock paper (19 Qs, 80 marks, on the MAS2001 blueprint because no DE blueprint exists; uses
  practice set 1 Q4/Q6/Q8, practice set 2 Q4, deck 11 slide 43 Q1, deck 12 slide 18, deck 15 slide 28) with key, formula sheet, sources.
  **Question sources:** all 8 questions of the 2025 MTE (Q1 A5, Q2 B6, Q3 C2, Q4 A3, Q5 B1, Q6 B2, Q7 C4, Q8 C8), decks 01–15, practice sets 1–2; the rest
  labelled "practice". MTE Q7's waveform image is missing from the filed PDF, so C4 uses a practice waveform in the same form (stated in the PDF).
  `verify.py` passes (192 checks). **Deck slips flagged in the PDF:** deck 01 slide 31 (a'bc should be a'bc'); deck 15 slide 28 (F2, F3 written as 3-variable
  functions with minterms above 7). Not flagged because the slide image could not be read with certainty: deck 13 slide 8's 1010-detector equations.
  Reuses the DE-v1 ETE-half figures (`study-pack/pdf/figs.py`) and 4 Wikimedia Commons drawings. All 61 pages viewed after the final build.
  `study-pack/pdf-ete/README.md` written. **No teaching event; mastery ledger and review queue unchanged.**
  **Where we stopped:** pack delivered; learner has not worked any Check.
- [2026-11-14] Learner verdict (stated) on the v1-format packs: "this isnt really what i wanted … v1 isnt good at all"; the expected shape is the
  Circuits & Systems pack. Format written down as `study-pack-format.md` (v1.2) at the project root. `study-pack/pdf-ete/DE-ETE-v1.pdf` (and `study-pack/pdf/DE-v1.pdf`) is listed there as
  **non-conforming** (one question and one Check per topic, no ranked start page, no Exam form/Traps/Self-test); its questions, figures and
  `verify.py` are sound and will be reused in the rebuild. README marked. Rebuild not started. **No teaching event.**
- [2026-11-14] Learner request (stated): "start with electronic devices … build a demo for both subjects first", without the cost of a
  full rebuild. Building the v1.2 demo (`study-pack-format.md`): `study-pack-v12/` = `00-START-HERE` + one topic file (`13-synchronous-counters`),
  rendered by the shared builder `tools/study_pack_build.py` (copied from the reference pack's own build script). Figures, questions
  and numbers reused from the v1 pack and its `verify.py`. Awaiting learner sign-off before the rest. **No teaching event.**
- [2026-11-14] v1.2 demo **built**: `study-pack-v12/pdf/` = `00-START-HERE` + `13-synchronous-counters (6 steps)` + combined PDF (5 + 7 = 12 pp.). Every step has a
  question or Predict, a guess line and a Check; Exam form, Traps, Self-test, Answers at the end. All numbers are ones the v1 `verify.py` already checks
  (plus one new g_m value / Gray-step check, hand-verified). All pages viewed. **Awaiting learner sign-off; no teaching event.**
- [2026-11-15] Learner signed off both v1.2 demos. Full v1.2 build queued after EDC: files 01–12, 14–20 in START-HERE priority order, content reused from `study-pack/pdf-ete/parts/A–H.html` + `verify.py` numbers; combined PDF at the end.
- [2026-11-15] Full v1.2 DE pack **built**: `study-pack-v12/pdf/` = 00 + files 01–20 (13 from the demo; the rest new, content from v1 parts A–E, H; numbers from v1 `verify.py`; new K-map Self-test answers checked with `qm.py`) + combined `ECE2102-DE-ETE-study-pack.pdf` (114 pp.). 23 v1 figures had no source module left; recovered from `DE-ETE-v1.html` by `src/extract_v1figs.py` → `src/v1figs.json` (an end-of-figure bug that pulled following tables into 11 and 19 was found on viewing and fixed). Pages of 11, 18, 19 viewed. **No teaching event.**
- Where we stopped: DE v1.2 pack delivered; learner has not worked any Check.
- [2026-11-16] Spec now **v1.3** (`study-pack-format.md`); the v1.2 files 01–19 are listed as not meeting it. Writing `sprints.md` (S0–S9, 10 sprints, learner's budget 9–10): S0 builds the subject brief, then 1–3 files per sprint in START-HERE priority with prerequisites first, run by `auto.py` (shared steps: `../../../study-pack-sprint-protocol.md`). **No teaching event.**
- [2026-11-16] ETE dates (learner-stated): Stats 19 Nov, DE 21 Nov, EDC 24 Nov (`research-engine/exam-calendar.md`). Sprint runs in that order; `sprints.md` header gets the date. **No teaching event.**

- [2026-11-17] Learner approved splitting work with Gemini (AI Pro, Gemini CLI) to fit the weekly Claude limit. S0 splits: **S0a** (Gemini, `GEMINI-TASK.md`) transcribes the 15 decks, the MTE paper and both practice sets into `src/brief.md` §1 and maps every question in §2; **S0b** (Claude) reviews S0a, then writes §3 constants vs KB, §4 file plan, the figure list and `src/verify.py`. **No teaching event.**
- [2026-11-17] **Sprint S0a done** (interactive, driven via agy = Gemini 3.8 Flash High, Google quota). `src/brief.md` §1: all 15 decks (561 pages, one row each, checked by script: no page missing or duplicated), MTE paper (Q1–Q8) and Practice Sets 1–2 (10 + 6) transcribed; §2 question bank: 8 MTE + 16 PS + 213 slide examples mapped to files 01–19, each exactly once (checked by script), 0 unmapped. Claude spot-checks: deck 07 in full, deck 01 p.30, 03 p.12, 08 p.41 (image), MTE word-for-word vs the PDF text, PS1 vs the image — all match. Transcription facts are leads for S0b, not verified truth. Deck 08 needed a split run (first run hit the 20-min cap). **No teaching event.**

- 2026-11-17 auto S0b start: review brief §1-§2 by spot-check; write §3 constants, §4 file plan, §5 figure list; start src/verify.py importing v1 checks.
- 2026-11-17 auto S0b resumed (session 2; session 1 crashed after its start line, no other changes): writing brief §3-§5 and src/verify.py. **No teaching event.**
- 2026-11-17 auto **Sprint S0b done**: brief §3 (deck-14 constants vs KB05: 4 match, 7 open → S8), §4 file plan, §5 figure list; src/verify.py (v1 checks via Part 0 + helpers + u0) → 12 checks, 0 failures. KB05 Open block (uncertain), sources leads, CHANGELOG. Where we stopped: S0 done. Next up: S1 (files 01–03). **No teaching event.**

- 2026-11-17 (auto) S1 start: rebuild 01-03 (Boolean algebra, K-maps, NAND/NOR) to v1.3 + u1 checks in src/verify.py.

- 2026-11-17 (auto) S1 done: 01 (10 steps), 02 (10), 03 (7) rebuilt to v1.3; src/figs_u1.py (25 figures); verify u1 -> 153 checks, 0 failures; build 12+15+10 pp, no OVERLAP; agy page check ok (2nd try); START-HERE rows/slips updated. Where we stopped: S1 complete. Next up: S2 (09 latches/flip-flops, 10 waveforms).

- 2026-11-17 S2 start (auto): rebuild 09-latches-flip-flops + 10-waveforms to v1.3, src/figs_u3.py, verify u3.

- 2026-11-17 (auto) session 5: rebuilt state after session 4 crash (token limit). Commit 51f85be holds 09 + 10 content rebuilt, src/figs_u3.py, src/figs_u3_sch.py, build.py import, verify u3; python src/verify.py -> 237 checks, 0 failures; 09/10 PDFs and combined PDF rebuilt. Not yet done: agy page check of 09/10, START-HERE rows, S2 sign-off. Operator stop requested; no further edits.

- 2026-11-17 auto session 6: S2 close-out started (09/10 section check, build, page check, START-HERE)
- 2026-11-17 auto session 6: S2 done. 09/10 section check (13 + 7 steps), build 09 10 00 no OVERLAP, agy page check 30 pp no problems (1st run timed out, retry ok), START-HERE how-checked = 237 checks, MTE Q7 sentence fixed. Next up: S3 (12 + 13 counters).

- 2026-11-17 S3 start (session 7): rebuild 12 ripple counters + 13 synchronous counters to v1.3; figures to Sonnet subagent.

- 2026-11-17 auto session 8: resumed S3 after session 7 crash (usage limit). Session 7 left only verify.py u3c (64 checks; one syntax slip in the 12 s6 check fixed, now 0 failures); no content or figures written. Writing 12 (8 steps) + 13 (12 steps, no a/b split); figures to a Sonnet subagent.
- 2026-11-17 auto session 8: S3 done. 12 (8 steps) + 13 (12 steps, no split) rebuilt; figs_u3c.py (Sonnet) + 4 K-maps; verify 311 checks 0 failures; build 12 13 00 no OVERLAP; agy page check: 3 raw \qquad lines fixed; START-HERE ranks/table/slips/how-checked updated. Next up: S4 (15 + 16 FSM, reduction, ASM).

- 2026-11-17 session 9 (auto-v2): S4 start (15 FSM design + 16 state reduction/ASM rebuild to v1.3).

- 2026-11-17 session 9: S4 figures: Sonnet subagent wrote src/figs_u4.py (12 figures) + 7 K-map registrations in build.py from my spec; deck 13 slide 8 image viewed: D0 = X(y0)' and D1 = X'm1 + Xm2 printed (slip; table gives D0 = X, D1 = X'm1 + Xm2 + X'm3).

- 2026-11-17 session 9: S4 partial: 15 (12 steps) and 16 (12 steps) rebuilt; verify 387 checks, 0 failures (u4 76, in src/verify_u4.py); build 15 16 00 no OVERLAP (v1 mealy_1101 overlap fixed by u4_mealy_1101). Left for next session: START-HERE rows/slips, agy page check, mock re-point. Where we stopped: S4 closing items. Next up: finish S4 closing, then S5.

- 2026-11-17 session 10 (auto-v2): resumed after session 9 crash (hard token limit); 89d7d05 holds 15/16 built + verified (387 checks). Mock Q17 (1011 Moore) equations checked by hand against 15 step 12 table: match. Doing S4 closing: START-HERE rows/slips/how-checked, agy page check; then S5.

- 2026-11-17 session 10: S4 START-HERE rows/slips/how-checked done (00, 15, 16 rebuilt, no OVERLAP); agy page check run 1 timed out (exit 124), retry on contact sheets running. S5 start: verify_u2.py (63 checks, 0 failures) wired as unit u2; Sonnet wrote figs_u2.py (15 figures). 74LS151 disabled-output = 0 not checked (TI PDF has no text layer): uncertain.

- 2026-11-17 session 11 (auto-v2): rebuilt state from 5b1e6ae (session 10 crashed, usage limit): S4 START-HERE rows/slips/how-checked committed; agy page check of 15/16 result not recorded (retry was running at crash); S5 started: verify_u2.py (63 checks) + figs_u2.py (15 figures) wired, content 05/06 not yet written. Operator stop request at session start: hand-off rewritten only, no other work.
- 2026-11-17 session 12 (auto-v2): S5 continue: write 05 + 06 to v1.3 from verify_u2.py and figs_u2.py; build; page check.
- 2026-11-18 session 12: S5 done: 05 (10 steps) and 06 (10 steps) rebuilt to v1.3; verify 450/0; build no OVERLAP; agy page checks 05, 06, 15, 16 clean; START-HERE, mock, sources.md updated. Next: S6.
