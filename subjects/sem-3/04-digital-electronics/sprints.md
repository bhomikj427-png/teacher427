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
| S4 | **15 + 16** FSM design; state reduction, ASM | old 15, 16 · KB `04` · decks 11, 12, 13 | `15-…`, `16-…` rebuilt, `src/figs_u4.py` | same; the five detectors on deck 11's last slide simulated in verify |**partial** 2026-11-17 (session 9; 15: 12 steps, 16: 12; no split; built + verified; START-HERE rows, slip rows, page check left) |
| S5 | **05 + 06** MUX/DEMUX; decoder/encoder | old 05, 06 · KB `02` · decks 04, 05 · MTE Q5, Q6 · set 1 Q3, Q5–Q8 | `05-…`, `06-…` rebuilt, `src/figs_u2.py` | same | |
| S6 | **04 + 07 + 08** adders/subtractors; display, comparator, parity; shifter, ALU | old 04, 07, 08 · KB `01`, `02` · decks 03, 06, 07 · MTE Q2 · set 1 Q9–Q10 | `04-…`, `07-…`, `08-…` rebuilt | same | |
| S7 | **11 + 14** registers; timing analysis | old 11, 14 · KB `03` · deck 09 | `11-…`, `14-…` rebuilt | same | |
| S8 | **18 + 19** logic families; memories and PLDs | old 18, 19 · KB `05` · decks 14, 15 | `18-…`, `19-…` rebuilt, `src/figs_u5.py` | same; noise margins and fan-out in verify; PLA/PAL tables checked | |
| S9 | **17 + integration** timing generators, asynchronous circuits; mock paper re-pointed; START-HERE ranks, times, map, slip table | old 17, 20 · `00-START-HERE.md` · KB `04`, `05` | `17-…` rebuilt; 00 and 20 updated; full build | grep finds no reference to a removed file; `src/verify.py` passes; build prints no `OVERLAP` | |

**Learner check-ins are not sprints:** report misses on any delivered file whenever you like; the next
sprint reads them first.

---

## Verify backlog (persistent — items leave only when resolved, with the sprint that closed them)

| Item | Raised | Close in |
|---|---|---|
| ETE date and format not given; no memory deck (19 is built from the KB) | progress log 2026-11-14 | [learner] |
| Deck header reads ECE 2105, MTE paper reads ECE2102 (same syllabus) `uncertain` | 2026-09-11 | [learner] |
| Deck 14 numbers not verified: CMOS noise immunity 30 % (slide) vs KB05 0.45 V_DD; CMOS fan-out ~50; CMOS supply 3–15 vs 5–15 V; ECL "±5 V" (likely −5.2 V); TTL typical NM 1–1.6 V (KB05 *Open* block, brief §3) | S0b 2026-11-17 | S8 |
| Deck 10 slide 36: brief transcription reads J1 = Q2'Q0', K1 = Q2Q0' (pack flags it as a slip, uses slide 37's J1 = Q2'Q0, K1 = Q2Q0); slide image not re-viewed `uncertain` | S3 2026-11-17 | S9 |
| t_PLH/t_PHL at 50 % points, rise/fall 10–90 %, PDP = t_pd × P: not yet checked against textbook (`likely`) | S0b 2026-11-17 | S8 |

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

## Current hand-off

```
Sprint: S4 — 15 + 16 FSM design; state reduction, ASM — partial (2026-11-17, session 9): files
  built and verified; closing items left (context limit)
Written: content/15-fsm-design.md (12 steps: what a state remembers, 1101 chain + overlap arc,
  completing arcs, overlap vs non-overlap (1010; slide-27 slip), state table, counting-order D
  (cost 22), Gray D + circuit (cost 9), T + JK (cost 10), Mealy vs Moore, 111 both ways + false-
  output timing, Moore 1101 (3 FFs, y = Y2), slide 43's five detectors (table of state counts;
  1011 Moore solved, others in Self-test/Answers)); content/16-state-reduction-asm.md (12 steps:
  equivalence via response table, inspection, Moore partition (slide 8), Mealy partition = running
  example, implication table, implication loops (8-state), compatibility, maximal compatibles +
  closed cover (5 -> 2), ASM elements, ASM 1010 + equations (slide-8 slip), Moore-output counter
  (slides 9/18 slips), serial adder); src/figs_u4.py (13 figures) + 7 K-maps (_kmy) in build.py;
  src/verify_u4.py (unit u4, 76 checks, wired into verify.py UNITS)
Verified this sprint: numbers: src/verify.py 387 checks, 0 failures; every detector table
  simulated against a reference detector on all strings <= 9 bits; all deck 12 partitions,
  implication tables, maximal compatibles and closures recomputed; build 15 16 00: no OVERLAP
Slips found (put in START-HERE slip table): deck 11 slide 27 (empty Overlapping panel; same
  diagram for 110); deck 13 slide 8 (image viewed: D0 = X(y0)', D1 = X'm1 + Xm2 printed; correct
  D0 = X, D1 = X'm1 + Xm2 + X'm3); deck 13 slide 9 (no hold terms; D0 = X xor y0); deck 13 slide
  18 (redundant decision after S3). Brief §1.12 p.4: response-table columns are 00, 01, 10, 11
  (brief header says 00, 01, 11, 10; values match 00, 01, 10, 11 by simulation)
Open (carried): S4 closing items: (1) 00-START-HERE: rank rows, file-table rows 15/16, the slip
  rows above, how-checked = 387 checks; (2) agy page check of 15 (19 pp) and 16 (19 pp);
  (3) grep cross-references to 15/16 and re-point mock rows; deck-14 numbers (backlog -> S8);
  deck 10 slide 36 (backlog -> S9)
Decisions made: no 16a/16b split (12 steps each); 16's running example = deck 12's 5-state
  machine (assumption 9); 15 uses plain Y1, Y2 (Y2 Y1 Y0 in step 11); reused v1 figures:
  fsm_blocks, moore_1101, implication_chart; mealy_1101 replaced by u4_mealy_1101 (overlap fix)
Assumptions to review: 9 (16 running example), 10 (practice detectors overlapping)
Helpers: Sonnet subagent wrote figs_u4.py (12 figures) + build.py K-map registrations from my spec,
  viewed all 12 as PNG; I wrote all teaching text and verify_u4.py (written as the computation tool
  while checking the deck's tables, so not delegated); agy not run (context limit)
Next sprint: S4 closing, then S5 — first action: one Python script that adds the START-HERE rows
  and slip rows above (grep '^## |^\| 1[3-7]' in content/00-START-HERE.md first), then render 15
  and 16 to PNG contact sheets for the agy page check; then start S5 (05 + 06)
Read at start: this hand-off + S5 row · ../../../study-pack-sprint-protocol.md · 00-START-HERE
  headings · brief 1.4-1.5 (decks 04, 05) by range · old 05, 06 by heading ranges · KB 02
```
