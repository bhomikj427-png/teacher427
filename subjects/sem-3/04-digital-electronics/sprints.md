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
| S9 | **17 + integration** timing generators, asynchronous circuits; mock paper re-pointed; START-HERE ranks, times, map, slip table | old 17, 20 · `00-START-HERE.md` · KB `04`, `05` | `17-…` rebuilt; 00 and 20 updated; full build | grep finds no reference to a removed file; `src/verify.py` passes; build prints no `OVERLAP` | |

**Learner check-ins are not sprints:** report misses on any delivered file whenever you like; the next
sprint reads them first.

---

## Verify backlog (persistent — items leave only when resolved, with the sprint that closed them)

| Item | Raised | Close in |
|---|---|---|
| ETE date and format not given; no memory deck (19 is built from the KB) | progress log 2026-11-14 | [learner] |
| Deck header reads ECE 2105, MTE paper reads ECE2102 (same syllabus) `uncertain` | 2026-09-11 | [learner] |
| Deck 14 numbers still open after S8: CMOS fan-out ~50; 4000-series supply 3–15/3–18 V; ECL "±5 V" (leads −5.2 V, levels −0.9/−1.7 V); TTL typical NM 1–1.6 V. Closed in S8: CMOS NM 30 % (74HC00 data sheet: 1.25 V at 4.5 V = 28 %) (KB05 *Still open* block) | S0b 2026-11-17 | [interactive: needs a textbook or the 4000B / MC10K data sheets as text] |
| Deck 10 slide 36: brief transcription reads J1 = Q2'Q0', K1 = Q2Q0' (pack flags it as a slip, uses slide 37's J1 = Q2'Q0, K1 = Q2Q0); slide image not re-viewed `uncertain` | S3 2026-11-17 | S9 |

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

## Current hand-off

```
Sprint: S8 — 18 + 19 logic families; memories and PLDs — done (2026-11-19, session 19; session 18
  crashed at the usage limit after writing 18 + figs_u5.py, commit feeb93b; state rebuilt from it).
Written: 18-logic-families.md (session 18, checked and fixed this session): 14 steps (t_PLH/t_PHL,
    rise/fall, power, noise margin, PDP, fan-out, CMOS inverter, CMOS NAND/NOR, TTL NAND, totem pole /
    open collector, tristate bus, ECL, families compared, interfacing); running example one SN7400
    gate. Fixes: \left/\right removed from the fan-out formula; 74HC00 rise/fall figure is 7-3.
  19-memories-plds.md: 12 steps (organisation, SRAM/DRAM, ROM types, expansion, AND-OR array, 8x4
    ROM EX 15.20-21, PROM EX 15.22, PAL read EX 15.24, PAL design EX 15.25-27, PLA + output XOR,
    PLA design EX 15.31-34, PROM/PAL/PLA compared EX 15.37); running example 1K x 8 chip and
    F1 = S(0,1,2,4), F2 = S(0,5,6,7) through PROM/PAL/PLA (8 / 6 / 4 lines). 2 slip notes (slides 21, 24).
  figs_u5.py (11 figures, session 18) wired; verify_u5.py (unit u5, 85 checks) wired in verify.py.
  KB 05: Open block replaced by "Data-sheet numbers and deck-14 checks" + "Still open"; sources.md
    (4 sources) + CHANGELOG. 00-START-HERE: rank 9/10 rows (Do first, 55 min each), file rows 18/19,
    4 slip rows (deck 14 slides 14/20/21, deck 15 slides 21/24), facts + how-checked (746). 20-mock:
    formula rows 18/19, answers 9, 10, 16, 18 re-pointed to steps.
Verified this sprint: numbers: verify.py 746 checks, 0 failures (incl. a search proving the PLA line
  counts 4 and 5 are minimum; it found the 5-line answer for slide 37, better than the 7 from minimal
  forms). Facts read this session: TI SN7400 (SDLS025D) and SN74HC00 (SCLS181H) data sheets as text
  (levels, currents, I_CC, C_pd, C_i, t_pd, Fig. 7-2/7-3 definitions, unused inputs); UMBC CMPE 640
  notes (PDP = energy per switch); DJ Greaves Cambridge notes (1985 HC/F/ECL quad NAND table).
  Build 00 18 19 20: no OVERLAP; combined PDF 300 pages.
  agy failed: exit 124 (timed out at 900 s, no report; same as S7). Not retried: the context notice arrived. Page check of 18 and 19 NOT done (sheets ready in scratch sheets7/18_*.png, 19_*.png; build OVERLAP check clean); S7 leftovers (11 p1-4, 9-16; 14 p1-4, 9-12) still unchecked. First job for S9: view or agy-check these sheets.
Open (carried): deck-14 leftovers (CMOS fan-out ~50, 4000 supply, ECL levels, TTL typical NM) stay
  `uncertain` in KB 05 and are printed in 18 only as "not checked" notes; backlog row re-targeted to an
  interactive session. Deck 10 slide 36 (backlog -> S9).
Decisions made: 18 kept at 14 steps (assumption 15). 19 order: memories first, then deck 15 order
  (assumption 16). PLA tables use a T/C row as deck 15 slide 33.
Assumptions to review: 15, 16, 17 copied to the persistent table.
Helpers: none this session. figs_u5.py came from session 18 (no record of a Sonnet run; the crash
  lost its hand-off). verify_u5 written by Opus: every value in it is a teaching number chosen while
  writing 19, so a spec would have been as long as the code. agy x1 (failed, exit 124): page check of 18, 19 and the
  S7 leftovers (11 p1-4, 9-16; 14 p1-4, 9-12).
Next sprint: S9 — 17 + integration — first action: page-check 18 and 19 (rebuild sheets with scratch sheets.py; agy once, else view the sheets), plus the S7 leftovers of 11 and 14; then run src/verify.py (expect 746, 0 failures), then
  grep brief 1.x rows for 17 (decks on timing generators / async) and §2/§4/§5 rows for 17.
Read at start: this hand-off + S9 row · ../../../study-pack-sprint-protocol.md · brief rows for 17 and
  §4 row 17 · old 17 · KB 04 and 05 by heading · 00-START-HERE (rank table, map, slip table) ·
  20-mock-paper formula rows · Verify backlog row for deck 10 slide 36 · 19 lines 1-40 as format model
```
