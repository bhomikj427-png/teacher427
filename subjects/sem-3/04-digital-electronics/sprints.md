# ECE2102 Digital Electronics — Build Sprints (v1.3)

> **ETE: 2026-11-21** (learner, 2026-11-16). This plan runs second, after Stats. Files land in priority order, so a run
> cut short by the exam leaves the highest-value files done; the learner studies the v1.2 file for any topic not yet rebuilt.
>
> **Learner rules:** one sprint = one session, fully finished, ending with the hand-off below.
> **Budget: 9–10 sprints per subject, 12 fine, more only if seriously necessary** (2026-11-16).
> This plan uses **10** (S0–S9).
>
> **Goal:** files 01–19 of `study-pack-v12/` rebuilt to `study-pack-format.md` **v1.3** (the v1.2 files
> are too compressed: ideas merged, symbols named but not explained). The KB is `stage-2✓`, so no
> research sprints; a missing fact goes into the KB inside the sprint that finds it. Written 2026-11-16.
>
> **Steps for every sprint: `../../../study-pack-sprint-protocol.md`.** This file holds only the
> table, hand-off, backlog and subject notes. Run unattended: `python auto.py run sem-3/04-digital-electronics`.

**Order:** START-HERE priority, prerequisites first (spec §7.2). Rank 1 is 13 synchronous counters,
which needs Boolean algebra and K-maps (01–02, for excitation equations) and flip-flops (09); so S1–S2
build those, S3 builds 12–13.

**DE specifics:** the "running example" (spec §4) is one circuit or one function carried through
the file (e.g. one 4-variable function through 01–03). A digital figure's "what this graph plots"
line applies to timing diagrams (time across, one row per signal, high/low) and K-maps (what a cell
and a group stand for). Numbers to verify are truth tables, minimised expressions, state tables and
counts: `verify` checks them by exhaustive evaluation.

**Every sprint's Inputs also include:** the protocol · `src/brief.md` sections for its files ·
`src/build.py` · the previous sprint's file header + symbol table. Until the first v1.3 file exists,
the format model is EDC `../03-electronic-devices-1/study-pack-v12/src/content/01b-fermi-level.md`
lines 1–100 (depth only; never copy its content).

---

## Sprint table

Old file = `study-pack-v12/src/content/<old>.md`. KB = `knowledge-base/` (+ `stage-2/`). Real questions
in `exam-pack/` (index: `exam-pack/README.md`): MTE 2025 paper, practice sets 1–2 (images), decks 01–15.

| # | Sprint | Inputs (beyond the standing list) | Outputs | Done when | Status |
|---|---|---|---|---|---|
| S0 | **Brief**; plus `src/verify.py` started (v1.2 relies on the v1 pack's `study-pack/pdf-ete/verify.py`) | every file in `exam-pack/` · KB `00-map`, `exam-map` · old 00 (ranking) · v1 `verify.py` | `src/brief.md`: decks transcribed (diagram slides viewed), question bank (MTE + practice sets + deck examples → file + step), figure list per file (reuse from v1 `figs1/figs2` or `v1figs.json`, or new); `src/verify.py` skeleton importing the v1 checks | every MTE and practice-set question is mapped; v1 checks run from `src/verify.py` | split 2026-11-17: **S0a** Gemini transcribes decks/MTE/practice sets → brief §1–§2 (`GEMINI-TASK.md`); **S0b** Claude reviews S0a, writes §3–§5 + `src/verify.py` · **done** 2026-11-17 (S0a + S0b) |
| S1 | **01 + 02 + 03** Boolean algebra; K-maps; NAND/NOR | old 01–03 · KB `01` · decks 01, 02 · MTE Q1, Q4 · set 1 Q1, Q2, Q4 | `01-…`, `02-…`, `03-…` rebuilt (a/b if > 13 steps), `src/figs_u1.py` | protocol 6–12 hold; every minimisation checked by truth table in verify | **done** 2026-11-17 (01: 10 steps, 02: 10, 03: 7; no split) |
| S2 | **09 + 10** latches and flip-flops; waveforms | old 09, 10 · KB `03` · deck 08 · MTE Q3, Q7 · set 2 Q1–Q3 | `09-…`, `10-…` rebuilt, `src/figs_u3.py` | same; every waveform answer simulated in verify | **done** 2026-11-17 (sessions 4–6; 09: 13 steps, 10: 7; no split) |
| S3 | **12 + 13** ripple counters; synchronous counters (rank 1: the MTE's only 8-mark question) | old 12, 13 · KB `03` · deck 10 · set 2 Q4–Q6 | `12-…`, `13-…` rebuilt (13a/13b likely) | same; every counter's state sequence simulated in verify | **done** 2026-11-17 (sessions 7–8; 12: 8 steps, 13: 12 steps; no 13a/13b split) |
| S4 | **15 + 16** FSM design; state reduction, ASM | old 15, 16 · KB `04` · decks 11, 12, 13 | `15-…`, `16-…` rebuilt, `src/figs_u4.py` | same; the five detectors on deck 11's last slide simulated in verify |**done** 2026-11-17 (sessions 9-10; 15: 12 steps, 16: 12; no split; START-HERE rows + slips done; agy page check of 15, 16 done in S5 session 12: clean) |
| S5 | **05 + 06** MUX/DEMUX; decoder/encoder | old 05, 06 · KB `02` · decks 04, 05 · MTE Q5, Q6 · set 1 Q3, Q5–Q8 | `05-…`, `06-…` rebuilt, `src/figs_u2.py` | same | **done** 2026-11-17/18 (sessions 10-12; 05: 10 steps, 06: 10 steps; no split; agy page check 05, 06 clean) |
| S6 | **04 + 07 + 08** adders/subtractors; display, comparator, parity; shifter, ALU | old 04, 07, 08 · KB `01`, `02` · decks 03, 06, 07 · MTE Q2 · set 1 Q9–Q10 | `04-…`, `07-…`, `08-…` rebuilt | same | **done** 2026-11-18 (sessions 13-14; 04: 13 steps, 07: 11, 08: 8; no split) |
| S7 | **11 + 14** registers; timing analysis | old 11, 14 · KB `03` · deck 09 | `11-…`, `14-…` rebuilt | same | **done** 2026-11-18 (session 17; 11: 10 steps, 14: 8 steps; no split) |
| S8 | **18 + 19** logic families; memories and PLDs | old 18, 19 · KB `05` · decks 14, 15 | `18-…`, `19-…` rebuilt, `src/figs_u5.py` | same; noise margins and fan-out in verify; PLA/PAL tables checked | **done** 2026-11-19 (sessions 18-19; 18: 14 steps, 19: 12 steps; no split) |
| S9 | **17 + integration** timing generators, asynchronous circuits; mock paper re-pointed; START-HERE ranks, times, map, slip table | old 17, 20 · `00-START-HERE.md` · KB `04`, `05` | `17-…` rebuilt; 00 and 20 updated; full build | grep finds no reference to a removed file; `src/verify.py` passes; build prints no `OVERLAP` | **done** 2026-11-19 (session 20; 17: 13 steps; no split; full build 312 pp, verify 821/0) |

**Learner check-ins are not sprints:** report misses on any delivered file whenever you like; the next
sprint reads them first.

---

## Verify backlog (persistent — items leave only when resolved, with the sprint that closed them)

| Item | Raised | Close in |
|---|---|---|
| ETE date and format not given; no memory deck (19 is built from the KB) | progress log 2026-11-14 | [learner] |
| Deck header reads ECE 2105, MTE paper reads ECE2102 (same syllabus) `uncertain` | 2026-09-11 | [learner] |
| Deck 14 numbers still open after S8: CMOS fan-out ~50; 4000-series supply 3–15/3–18 V; ECL "±5 V" (leads −5.2 V, levels −0.9/−1.7 V); TTL typical NM 1–1.6 V. Closed in S8: CMOS NM 30 % (74HC00 data sheet: 1.25 V at 4.5 V = 28 %) (KB05 *Still open* block) | S0b 2026-11-17 | [interactive: needs a textbook or the 4000B / MC10K data sheets as text] |

## Assumptions to review (persistent — the learner confirms or overrules)

| # | Assumption | Made in | Status |
|---|---|---|---|
| 1 | Build order = START-HERE priority with prerequisites first (spec v1.3 §7.2) | plan | open |
| 2 | New figures go in per-unit `src/figs_uN.py` on `tools/figlib.py`; the v1 figure modules and `v1figs.json` stay as reuse sources until S9 | plan | open |
| 3 | The pack gets its own `src/verify.py` in S0 (spec §7.4: the script lives in the pack's `src/`) | plan | open |
| 4 | One `src/verify.py` with a function per unit (`u1`, `u3`, …) instead of separate `verify_*.py` files; Part 0 runs the v1 `verify.py` unchanged until S9 | S0b | open |
| 5 | New K-maps, gate circuits and waveforms are drawn by calling the v1 drawers (`figs1.km/km5/two_level/mux_fig`, `figs2` waveform code) with new arguments from `figs_uN.py`, since `tools/figlib.py` has no K-map/gate/timing primitives; matplotlib (figlib) only for graphs | S0b | open |
| 6 | PS1 Q4 "two consecutive input bits are 1" read as "at least one adjacent pair (A,B), (B,C), (C,D) is 11" → F = AB + BC + CD (02 step 10 states the reading and the alternative) | S1 | open |
| 7 | Gate counts in 03 assume complemented inputs are available; the text adds the inverter count each time | S1 | open |
| 8 | 13's up/down direction input is named Dn (Dn = 1 counts down; deck 10 slides 29–32 call it X) so it does not clash with the don't-care X; slide 33's Up kept | S3 | open |
| 9 | 16's running example is deck 12's five-state Mealy machine (slides 4, 10, 16), not "15's 1101 table reduced" (brief §4): verify shows the Mealy and Moore 1101 tables are already minimal | S4 | open |
| 10 | Deck 11 slide 43's detectors are solved as overlapping (deck 11's default, slide 6); 1X1/1XX1 read X as "either bit" | S4 | open |
| 11 | 07's digit shapes: 6 with the top bar a, 9 with the bottom bar d, 7 = a b c (deck 05 slides 28-29); other shapes change the a, d, f equations | S6 | open |
| 12 | 07 step 8 models 7485 cascading as G = G_own + E_own·I(A>B), E = E_own·I(A=B), L = L_own + E_own·I(A<B) with the lowest stage seeded 0/1/0 (KB 02 §1); the datasheet's full table for odd cascade-input combinations is not taught | S6 | open |
| 13 | 11 step 4's PISO first stage takes 0 during a shift (an AND gate SHIFT'·D₀); the brief transcribes slide 15's D₀ as wired straight to FF0. The serial output for the first n bits is the same either way | S7 | open |
| 14 | 14 uses one t_pd for both the setup and the hold sums (exam style); KB 03 §6 notes that the hold check strictly uses the minimum (contamination) clock-to-Q delay | S7 | open |
| 15 | 18 keeps 14 steps in one file (the S1 rule says a/b above 13): splitting would cost a sprint for one extra step | S8 | open |
| 16 | 19 puts memories (steps 1–4, no deck) before deck 15's PLDs, and carries one function pair (deck 15 slide 31) through PROM, PAL and PLA so step 12 can compare costs | S8 | open |
| 17 | 19 step 12 answers deck 15 slide 37's PLA with 5 lines (F2 written non-minimally as AB + A'B'C + A'B'C', F3 complemented), found by verify.py's exhaustive search; a 7-line answer from the minimal forms is also correct | S8 | open |
| 18 | 17 runs in three parts (timing issues 1–3, generators 4–9, asynchronous 10–13) with no deck; the running example is the brief's 3-bit LFSR (steps 4–6) plus the EC6302 function (step 13); clock skew is left to 14 step 7, not repeated | S9 | open |
| 19 | 17's teaching examples are the pack's own choices (no deck): 2-bit counter decode glitch, pulse train 110100, MOD-50 divider, 555 with 1 kΩ/10 kΩ/10 nF, NOR-latch flow table, race tables A/B/C | S9 | open |
| 20 | The v1 figure modules (`figs1`, `figs2`) and `v1figs.json` stay: build.py still draws reused figures from them (lfsr3, astable_555, ring_osc, hazard, K-maps, etc.); removing them is a tooling job, not a sprint | S9 | open |

## Current hand-off

```
Sprint: S9 — 17 + integration — done except one page check (2026-11-19, session 20); see Page checks and Next.
Written: 17-timing-generators-async.md: 13 steps (decoding glitches, metastability + synchronizer,
    switch bounce + SR-latch debouncer, LFSR trace, maximal length / lock-out / taps, pulse train,
    clock division, 555 astable/monostable, ring oscillator + crystal, NOR-latch flow table, races and
    state assignment, static hazards + consensus, hazard-free EC6302 f); running example 3-bit LFSR
    D1 = Q2 xor Q3 from 100. figs_u4b.py (4 timing figures, Sonnet) wired in build.py; reuses v1 lfsr3,
    astable_555, ring_osc, hazard. verify_u4b.py (unit u4b, 75 checks) wired in verify.py.
  18 and 19: raw LaTeX in display math fixed (\qquad, \times, \text, \min, \cdot, \Sigma, \, ; the
    renderer supports only \frac, \sqrt, _{}, ^{}): 6 lines.
  13: the deck 10 slide 36 "slip" note removed; START-HERE slip row removed (slide 36 viewed: it reads
    J1 = Q2'Q0, K1 = Q2Q0, same as slide 37; the brief's transcription was wrong). Backlog row closed.
  00-START-HERE: rank 14 Do-first (17 steps 12–13 and 4, 60 min), file row 17, facts (NE555 sheet),
    how-checked (821, 17's checks). 20-mock: formula row 17 rewritten. KB 04: §3 debounce block, §5 555
    re-check note; sources.md (2 entries), CHANGELOG.
Verified this sprint: numbers: verify.py 821 checks, 0 failures. Facts: TI NE555 data sheet SLFS022K
  read as text (eq. 1-6, t_w = 1.1 R_A C, 1/3 and 2/3 V_CC); Utah CS 5780 lecture 11 (text + slide 9
  image: SPDT + pull-ups + NAND latch debouncer); deck 10 slides 36-37 viewed.
  Full build (all 21 files): no OVERLAP; combined PDF 312 pages.
  Page checks: agy run 1 (18, 19: 10 sheets): raw LaTeX on 18 p6-8, p13 and 19 p1, fixed (6 lines). agy run 2 (S7 leftovers 11 p1-4, p9-16; 14 p1-4, p9-12): all OK. agy run 3 (17 + the 18/19 re-check) hung: no report, log stalled at 01:14:51, then failed with exit 124 (timeout at 900 s). I viewed 17 p1-4 myself (clean) and p13-16 (2 fixes: the nested list in step 13 rendered inline, now one sentence; the hazard caption said Left/Right for a stacked figure, now Top/Bottom; 17 rebuilt). NOT checked: 17 p5-12, p17-20; the re-check of 18 p5-8, p13-16 and 19 p1-4 after the LaTeX fix.
Open (carried): deck-14 leftovers (backlog row, interactive). UNC Charlotte debounce handout seen only as a
  search summary (PDF redirects); Utah alone was read.
Decisions made: 17 kept at 13 steps; assumptions 18-20.
Assumptions to review: 18, 19, 20 copied to the persistent table.
Helpers: Sonnet x1: figs_u4b.py (4 figures) + build.py wiring from my spec, no overlaps, 37k tokens.
  agy: page checks (see above). verify_u4b written by Opus (teaching numbers chosen while writing).
Next sprint: none in the plan; one close-out job left — first action: render sheets
  (python -X utf8 <scratch>/sheets.py 17-timing-generators-async 18-logic-families 19-memories-plds) and
  page-check 17 p5-12 and p17-20, 18 p5-8 and p13-16 (raw-LaTeX fix), 19 p1-4 (agy once, else view);
  fix any fault, rebuild those files. Then the plan is DONE. Tooling (interactive): study_pack_build.inline()
  could map \times, \cdot, \qquad etc. so raw LaTeX can't leak again; it has no nested lists either.
Read at start (for the follow-up): this hand-off · Verify backlog · Assumptions 1-20.
```
