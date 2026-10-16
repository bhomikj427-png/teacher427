# ECE2102 Digital Electronics — Progress Log

> Written **live** as sessions happen (log-first artifact pairing; never reconstructed at
> wrap-up). Session-resume block is overwritten each session-end; Session history is append-only.
> See `../../README.md`.

## Session resume
- Last session: 2026-10-17 — no teaching; built `study-pack/pdf/DE-v1.pdf` (ETE half + MTE recap)
- Where we stopped: subject scaffolded 2026-07-05 (engine audit) — KB was already `stage-2✓`
  (TEACH-READY, queue 2026-06-27); curriculum/profile/log created so activation needs no
  mid-boot improvisation. **No teaching yet; learner level undiagnosed.**
- Next up: **Session 1** — diagnostic (K-map probe, memory-boundary probe, latch-race probe),
  then open U1 via the loop at the placed level (U0 number-systems prereq: verify by retrieval,
  teach only gaps).
- Due for review today: nothing yet (no items mastered).

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
