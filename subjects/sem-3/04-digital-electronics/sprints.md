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
| S1 | **01 + 02 + 03** Boolean algebra; K-maps; NAND/NOR | old 01–03 · KB `01` · decks 01, 02 · MTE Q1, Q4 · set 1 Q1, Q2, Q4 | `01-…`, `02-…`, `03-…` rebuilt (a/b if > 13 steps), `src/figs_u1.py` | protocol 6–12 hold; every minimisation checked by truth table in verify | |
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

## Current hand-off

```
Sprint: S0b — Brief §3–§5 + src/verify.py — done (2026-11-17, auto; session 1 crashed after its log line, redone in session 2)
Written: src/brief.md §3 constants vs KB05 (deck 14 is the only source of physical numbers; 4 match,
  7 open → S8) · §4 file plan (est. steps, splits: 13a/13b likely, 16a/b only if > 13 steps; running
  examples) · §5 figure list (reuse source per figure; new figures per file)
  src/verify.py: Part 0 runs the v1 pdf-ete/verify.py (192 checks); helpers fn/same/check_sop (truth
  table + QM cost)/check_pos, ff_next, run_sync, run_ripple, run_fsm, detect; unit u0 self-test
  KB05: *Open — deck-14 numbers* block (uncertain); sources.md leads; CHANGELOG line
  sprints.md: S1 and S6 Inputs gain PS1 Q4 and PS1 Q9–Q10 (§2 maps them there)
Verified this sprint: python src/verify.py → 12 checks, 0 failures (incl. v1 verify exit 0).
  KB05 TTL NM 0.4/0.4 V and fan-out 10 recomputed. §1–§2 not re-transcribed (S0a spot-checks stand);
  §2 vs sprint rows cross-checked: every MTE/PS question sits in a file of the sprint that uses it.
Open (carried): deck-14 numbers (backlog, close in S8); learner has not worked any v1.2 Check
Decisions made: verify is one file with a function per unit (assumption 4); new logic figures call the
  v1 SVG drawers with new arguments (assumption 5); 13 likely splits 13a/13b in S3
Assumptions to review: 4, 5 (persistent section)
Next sprint: S1 — first action: read brief §1.1–1.2 by grep (decks 01, 02 rows only where the file's
  steps need them), §2 rows 01–03, §4 rows 01–03, §5 rows 01–03; then rebuild 01-boolean-algebra.md
  to v1.3, adding u1 checks in src/verify.py (every minimisation via check_sop).
Read at start: this hand-off · S1 row · ../../../study-pack-sprint-protocol.md · spec §5 ·
  brief §2/§4/§5 rows 01–03 · old 01–03 (v1.2) · KB 01 by section · EDC 01b-fermi-level.md lines 1–100 (format depth only)
```
