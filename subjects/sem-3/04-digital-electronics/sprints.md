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
| S2 | **09 + 10** latches and flip-flops; waveforms | old 09, 10 · KB `03` · deck 08 · MTE Q3, Q7 · set 2 Q1–Q3 | `09-…`, `10-…` rebuilt, `src/figs_u3.py` | same; every waveform answer simulated in verify | |
| S3 | **12 + 13** ripple counters; synchronous counters (rank 1: the MTE's only 8-mark question) | old 12, 13 · KB `03` · deck 10 · set 2 Q4–Q6 | `12-…`, `13-…` rebuilt (13a/13b likely) | same; every counter's state sequence simulated in verify | |
| S4 | **15 + 16** FSM design; state reduction, ASM | old 15, 16 · KB `04` · decks 11, 12, 13 | `15-…`, `16-…` rebuilt, `src/figs_u4.py` | same; the five detectors on deck 11's last slide simulated in verify | |
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

## Current hand-off

```
Sprint: S1 — 01 + 02 + 03 Boolean algebra, K-maps, NAND/NOR — done (2026-11-17, auto)
Written: content/01-boolean-algebra.md v1.3: 10 steps (AND/OR/NOT switch anchor, 2^n rows, gates,
  laws, De Morgan, simplification, minterms, maxterms, Σm↔ΠM, standard→canonical); running example
  deck 01 slide 18 F(x,y,z) = x'y + xz = Σm(2,3,5,7) = ΠM(0,1,4,6); 10 Checks, 7 self-test
  content/02-k-map.md v1.3: 10 steps (2-var, Gray order, reading groups, largest groups, PI/EPI,
  4-var, don't-cares = MTE Q4, POS from 0s, 5-var = PS1 Q1, words→map = PS1 Q4); running example MTE Q4
  content/03-nand-nor.md v1.3: 7 steps (NAND universal, NOR universal = MTE Q1, SOP→NAND-NAND,
  multi-level NAND (slide 42 table, 6 gates), POS→NOR-NOR, map→NAND = PS1 Q2 + PS1 Q1 circuit, XOR 4 NAND)
  src/figs_u1.py: 25 figures (K-maps, two-level AND/NAND/NOR circuits, universal_nor) via v1 figs1
  drawers; build.py imports it. src/verify.py: unit u1 (helpers eq, rows_of, pos_min, nbrs)
  00-START-HERE: rank rows 3 and 12, what-each-file rows 02/03, slip table +2 (deck 02 slide 28,
  deck 01 slide 41), how-checked line
Verified this sprint: python src/verify.py → 153 checks, 0 failures (u1: every expression, Σm/ΠM
  list, minimal cover vs QM cost, POS literal minimum, every NAND/NOR network row by row). Facts used
  are all `settled` in KB01 §1–§2 (no new KB facts). Build: 01 12 pp, 02 15 pp, 03 10 pp, combined
  135 pp, no OVERLAP lines.
  Page check: agy run 1 timed out (exit 124, no report); retry ok: all 10 contact sheets 'ok'. Viewed 03 pp.1-4 myself (new universal_nor figure): clean; zoomed 03 p.4 NAND-NAND: 3-input labels tight, readable, no overlap.
Open (carried): deck-14 numbers (backlog → S8); question-bank row EX 2.69 lists d(3,5,7,9,11) but the
  slide 69 transcription (brief §1.2) gives d(3,4,9): pack uses d(3,4,9)
Decisions made: 02's running example is MTE Q4 (3-var steps use 01's F); 5-var step opens on PS1 Q1
  with slide 58 as the worked warm-up; PS1 Q1's universal-gate half is answered in 03 step 6
Assumptions to review: 6, 7 (persistent section)
Helpers: agy (Gemini Flash) = contact-sheet check of 01–03; no Sonnet/Haiku subagents (all work was
  teaching text or truth calls)
Next sprint: S2 — first action: read brief §2 rows 09–10, §4 rows 09–10, §5 rows 09–10 and grep
  brief §1.8 (deck 08) slide titles; then rebuild 09-latches-flip-flops.md to v1.3 with u3 checks
  (ff_next, qm.edge_ff / qm.d_latch for every waveform) and figures in src/figs_u3.py
Read at start: this hand-off · S2 row · ../../../study-pack-sprint-protocol.md · spec §5 ·
  brief §2/§4/§5 rows 09–10 · old 09, 10 (v1.2) · KB 03 by section · 01-boolean-algebra.md lines 1–30
  (format model: header, map, symbols, running example)
```
