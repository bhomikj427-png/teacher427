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
| 11 | 07's digit shapes: 6 with the top bar a, 9 with the bottom bar d, 7 = a b c (deck 05 slides 28-29); other shapes change the a, d, f equations | S6 | open |
| 12 | 07 step 8 models 7485 cascading as G = G_own + E_own·I(A>B), E = E_own·I(A=B), L = L_own + E_own·I(A<B) with the lowest stage seeded 0/1/0 (KB 02 §1); the datasheet's full table for odd cascade-input combinations is not taught | S6 | open |
| 13 | 11 step 4's PISO first stage takes 0 during a shift (an AND gate SHIFT'·D₀); the brief transcribes slide 15's D₀ as wired straight to FF0. The serial output for the first n bits is the same either way | S7 | open |
| 14 | 14 uses one t_pd for both the setup and the hold sums (exam style); KB 03 §6 notes that the hold check strictly uses the minimum (contamination) clock-to-Q delay | S7 | open |

## Current hand-off

```
Sprint: S7 — 11 + 14 registers; timing analysis — done (2026-11-18, session 17; session 16 was cut
  off with no changes, state rebuilt from e6ff646 = S6 done).
Written: 11-registers.md: 10 steps (register, SISO delay, SIPO loading 1011, PISO SHIFT/LOAD',
    universal 74194, ring EX 9.20, Johnson EX 9.22 + decode, lock-out, XOR feedback EX 9.24, serial
    adder EX 9.26); running example the word 1011; 4 slip notes (deck 09 slides 2, 13, 15, 17).
  14-timing-analysis.md: 8 steps (clock-to-Q, setup, hold, metastability, longest path -> f_max,
    hold check, clock skew, ripple vs synchronous counters); running example t_pd 8, t_su 3, t_h 2,
    t_comb 12/1 ns (43.5 MHz). No deck: Predict prompts only.
  figs_u3r.py (14 figures, Sonnet) wired in build.py; verify_u3r.py (unit u3r) wired in verify.py.
  KB 03 §5 (74194 mode table) and §6 (clock skew in setup/hold) + sources.md + CHANGELOG.
  00-START-HERE: rank 8 and 14 rows (Do first + times), file rows 11 and 14, 4 slip rows (deck 09),
    how-checked = 661 checks. 20-mock-paper: 11 and 14 formula rows.
Verified this sprint: numbers: verify.py 661 checks, 0 failures (every shift-register trace,
  74194 mode, ring/Johnson sequence and decode term, both unused-state loops, the XOR register's
  15-state cycle, serial additions, every timing sum and skew case). New facts: 74194 mode table from
  the Nexperia 74HC194 data sheet (Table 3); skew in the setup/hold inequalities from UCSD CSE140
  lec10 and Cornell ECE4740 lecture 17 (agree). Build 00 11 14 20: no OVERLAP.
  agy failed: exit 124 twice (900 s full task, then 570 s short task; log shows only "Failed to refresh
  cache in background: admin controls not applicable"). Page check done by Opus instead: sheets
  11 p5-8 and 14 p5-8 viewed: 4 captions in 14 printed raw t_pd/t_su (fixed to t_{pd}), PISO label
  "SHIFT/LOAD'" crossed by the D0 wire (moved left, zoom re-viewed: clean). Sheets 11 p1-4, 9-16 and
  14 p1-4, 9-12 not viewed (build OVERLAP check clean): first job for S8's agy run is to check them.
Open (carried): deck-14 numbers (backlog -> S8); deck 10 slide 36 (backlog -> S9). Tri-state buffer
  still owed to file 18 (S8). Sonnet noted: some wire crossings in u3r_reg4, u3r_ring4,
  u3r_serial_adder have no crossing dot (crossings, not joins: correct as drawn).
Decisions made: 11 writes words Q0Q1Q2Q3 with Q0 the serial-input stage (deck 09 slides 8, 11, 22);
  slide 23's left-shift Johnson and slide 17's ring are the same counters in the other bit order.
  11 keeps deck order (registers, SISO, SIPO, PISO, universal, ring, Johnson, XOR, serial adder);
  lock-out is its own step. 14's skew sign: δ = capture clock later than launch (positive helps
  setup, hurts hold); worst-case |δ| form mentioned.
Assumptions to review: 13 (PISO first stage), 14 (one t_pd for hold): copied to the persistent table.
Helpers: Sonnet x1: all 14 figures + build of 11/14 (107k subagent tokens, 42 tool uses, 6.7 min).
  agy x2: both timed out (exit 124), no report. Opus viewed one sheet per file + one zoom. Opus: 11 and 14 text, verify_u3r, KB + source
  checks (web: 2 searches, 3 fetches, 1 script download), START-HERE/mock rows.
Next sprint: S8 — 18 + 19 logic families; memories and PLDs — first action: run src/verify.py
  (expect 661, 0 failures; run it without -I), then grep brief 1.14, 1.15 and the §2/§4/§5 rows for
  18 and 19.
Read at start: this hand-off + S8 row · ../../../study-pack-sprint-protocol.md · brief 1.14, 1.15
  (rows truncated to ~400 chars with a script; print with sys.stdout.reconfigure(encoding='utf-8'))
  and §2/§4/§5 rows for 18, 19 · old 18, 19 · KB 05 by heading · Verify backlog rows for deck 14 ·
  11 lines 1-40 as the v1.3 format model
```
