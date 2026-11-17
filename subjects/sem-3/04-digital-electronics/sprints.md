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

## Current hand-off

```
Sprint: S3 — 12 + 13 ripple and synchronous counters — done (2026-11-17, sessions 7–8)
Written: content/12-ripple-counters.md (8 steps: T FF halves f, 2-bit ripple, 3-bit up = running
  example, down + edge/clock-source rule, ripple delay 011->010->000->100, MOD-6 by reset, decade,
  cascading; deck 10 slide 14's four exercises as questions/Self-test);
  content/13-synchronous-counters.md (12 steps: why one clock (f_max 50 vs 25 MHz), state diagram/
  table, D, T, JK on the 2-bit counter (PS2 Q4), MTE Q8 table + K-maps/circuit, down (PS2 Q5, Q6),
  decade T, unused states/self-start, up/down, Gray JK); src/figs_u3c.py (14 figures: ripple_sch,
  ripple waves, delay, MOD-6 waves, cascade, state rings) + 4 K-maps in build.py; verify.py unit u3c;
  00-START-HERE: rank 1/8 "Do first", file-table rows 12/13, 3 slip rows (deck 10 slides 6, 12-13,
  36), how-checked = 311 checks
Verified this sprint: numbers: src/verify.py 311 checks, 0 failures (u3c 75); build 12 13 00: no
  OVERLAP; agy page check 12 (13 pp) + 13 (18 pp): only raw \qquad in 3 math lines, fixed + rebuilt
Open (carried): deck-14 numbers (backlog -> S8); deck 10 slide 36 transcription (backlog -> S9)
Decisions made: 13 not split (12 steps); session 7's crash left only verify u3c (fixed a list-slice
  slip in the 12 s6 check). Steps 3-6, 8 (table part), 9, 11 of 13 are table-led with no figure (the
  table is the figure); 13 step 1 shows counter_T, which step 7 refers back to
Assumptions to review: 8 (direction input named Dn)
Helpers: Sonnet subagent wrote figs_u3c.py + K-map registrations from my spec (14 + 4 figures, no
  overlaps; it viewed 6 of them); agy page check (one run, ok); I wrote all teaching text and verify
  additions
Next sprint: S4 — 15 + 16 FSM design; state reduction, ASM — first action: grep '^## |^### ' in old
  content/15 and 16 and the brief's 1.11-1.13 + section 4 rows for 15/16; plan steps (16a/16b if > 13)
Read at start: this hand-off + S4 row · ../../../study-pack-sprint-protocol.md · brief 1.11-1.13
  (decks 11-13) by range · old 15, 16 by heading ranges · 13 header + Symbols (lines 1-30) · KB 04
```
