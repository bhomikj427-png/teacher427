# ECE2106 Electronic Devices & Circuits — Build Sprints (v1.3)

> **ETE: 2026-11-24** (learner, 2026-11-16). This plan runs third, after Stats and DE. Files land in priority order, so a run
> cut short by the exam leaves the highest-value files done; the learner studies the v1.2 file for any topic not yet rebuilt.
>
> **Learner rules:** one sprint = one session, fully finished, ending with the hand-off below
> (2026-11-15). **Budget: 9–10 sprints per subject, 12 fine, more only if seriously necessary**
> (2026-11-16: "i cant commit 27 fucking sprints to any one subject"). This plan uses **12**
> (E0–E11), because six delta topics (special diodes, CMOS/FinFET, BJT stability, h-parameters,
> U6 feedback, U7 oscillators) still need research before their files can be built.
>
> **Goal:** files 04–14 of `study-pack-v12/` rebuilt to `study-pack-format.md` **v1.3** (01a–03b
> already meet its depth), with each delta topic's research written into `knowledge-base/` in the
> same sprint as the file that uses it. Rewritten 2026-11-16 from the S0–S27 plan (27 sprints).
>
> **Steps for every sprint: `../../../study-pack-sprint-protocol.md`.** This file holds only the
> table, hand-off, backlog and EDC notes. Run unattended: `python auto.py run sem-3/03-electronic-devices-1`.

**EDC tier-1 texts** (`course-info.md`): Boylestad, Sedra–Smith, Streetman, Sze, Gray, Neamen; when
none is readable, Hu (*Modern Semiconductor Devices for ICs*, open online) + a second university text.

**Order:** START-HERE priority, prerequisites first (spec §7.2). 04a comes first because the JFET's
bias (rank 1) uses the load line; 10 comes before 11 (rank 3); 06 and 09 (rank 12) come last.

**Every sprint's Inputs also include:** the protocol · `src/brief.md` sections for its files ·
`03b-diode-iv-capacitance.md` lines 1–60 (header, map, symbol table, step 1: the format model) ·
`src/build.py` · the previous sprint's file header + symbol table (to recall terms by file and step).

---

## Sprint table

Old file = `study-pack-v12/src/content/<old>.md`. KB = `knowledge-base/` (+ `stage-2/`). Decks in
`exam-pack/` (index: `exam-pack/README.md`). **K** = research the delta topic into the KB first, in the
same sprint.

| # | Sprint | Inputs (beyond the standing list) | Outputs | Done when | Status |
|---|---|---|---|---|---|
| E0 | **Brief** for files 04–14 | every deck and sheet in `exam-pack/` (picture slides listed, not all viewed: each later sprint views its own) · KB `00-map`, `exam-map` · old 04–14 (question tags) · `study-pack/pdf/verify.py` constants | `src/brief.md`: per deck, slide text + list of picture/equation slides + slips found; question bank (every sheet/deck question → file + step); constants table checked against KB (gaps → KB first); figure list per file | every question on the two numericals sheets and the TIP file is mapped; every constant the decks use is in the KB or in the backlog | |
| E1 | **04a + 04b** diode circuits (load line, Q-point, models applied, series/parallel, gates) and rectifiers (half/full-wave, PIV, ripple, capacitor filter) | old `04` · KB `02` §Diode models, §Diode circuits · decks L08, L09 | `04a-diode-load-line-circuits.md`, `04b-rectifiers.md`, `figs_u4.py`, `verify_u4.py`; old 04 removed | protocol 6–12 hold; every L08/L09 worked example reproduced with the deck's numbers or flagged | |
| E2 | **07a + 07b** JFET (channel, pinch-off, Shockley built from the channel picture) and parameters/bias/amplifiers (g_m, r_d, μ = g_m·r_d "8 marks", self-bias, divider bias, CS/CD gain) | old `07` · KB `03` · deck U3 jfet · TIP file · numericals sheet Q1–Q19 | `07a-jfet-operation.md`, `07b-jfet-bias-amplifiers.md`, `figs_u7.py`, `verify_u7.py`; old 07 removed | same; every sheet question used is solved in verify, sheet answers compared | |
| E3 | **08a + 08b** MOSFET (MOS capacitor, V_t, E/D types, regions, square law) and biasing/small signal | old `08` · KB `04` · decks U4 types-and-characteristics, biasing · sheet Q20–Q31 | `08a-mosfet-operation.md`, `08b-mosfet-bias-amplifiers.md`, `figs_u8.py`, `verify_u8.py`; old 08 removed | same; region boundaries derived, not stated | |
| E4 | **10 + 11a** BJT operation (carrier flow from 03a/03b, α, β, regions, CB/CE/CC) and load line + fixed bias + why the Q-point drifts. **K:** BJT bias stability (I_CO, V_BE, β with T; S, S′, S″) | old `10`, old `11` steps 1–2 · KB `05` · decks L20–L25, L26-27 | KB `11-bjt-bias-stability.md`; `10-bjt-operation.md`, `11a-bjt-load-line-fixed-bias.md`, `figs_u10.py`, `verify_u10.py` | protocol 3–12; each S expression checked in a script | |
| E5 | **11b** emitter and voltage-divider bias, stability factor, compensation | old `11` steps 3–5 · KB `11-bjt-bias-stability.md` · deck L26-27 | `11b-bjt-stable-bias.md`; old 11 removed | same; the deck's full S derivation reproduced line by line | |
| E6 | **12a + 12b** h-parameter model and CE analysis; cascading and Darlington. **K:** h-parameters, multistage | old `12` · KB `05` §Small-signal · deck L26-27 h-slides, multistage deck · h-parameter sheet (book pp. 131–145) | KB `12-h-parameters-multistage.md`; `12a-h-parameter-ce.md`, `12b-multistage-darlington.md`, `figs_u12.py`, `verify_u12.py`; old 12 removed | same; A_i, Z_i, A_v, Z_o derived from the two-port equations in a script; sheet answers compared | |
| E7 | **05a + 05b** clippers, clampers, multipliers; breakdown, Zener regulator, Schottky | old `05` · KB `02` §Breakdown, §Special diodes · deck L10 | `05a-clippers-clampers.md`, `05b-breakdown-zener-schottky.md`, `figs_u5.py`, `verify_u5.py`; old 05 removed | same; each output waveform plotted from the circuit; regulator worked at both I_Z limits | |
| E8 | **13** feedback (A_f = A/(1 + Aβ) derived, four topologies, effects). **K:** U6 to stage-2 | old `13` · deck U6 | KB `13-feedback.md`; `13-feedback.md` rebuilt (or 13a/13b), `figs_u13.py`, `verify_u13.py` | protocol 3–12; Z_in/Z_out factors checked in a script; slide-32 slip kept in the slip table | |
| E9 | **14a + 14b** Barkhausen, RC phase-shift, Wien; Hartley, Colpitts, crystal. **K:** U7 to stage-2 | old `14` · decks U7 RC-LC (.ppt), crystal | KB `14-oscillators.md`; `14a-oscillators-rc.md`, `14b-oscillators-lc-crystal.md`, `figs_u14.py`, `verify_u14.py`; old 14 removed | same; 29 and 1/(2π√6RC) derived symbolically in a script | |
| E10 | **06 + 09** special diodes (LED, photodiode, tunnel); MOSFET switch, CMOS gates, FinFET. **K:** both | old `06`, old `09` · KB `02` §Special diodes, `04` §Switch · decks special-diodes, FinFET ×2, WSU logic PDF, mosfet biasing-and-digital | KB `06-special-diodes.md`, `09-cmos-finfet.md`; `06-special-diodes.md`, `09-cmos-finfet.md` rebuilt, `figs_u6.py`, `figs_u9.py`, `verify_u6.py`, `verify_u9.py` | same; every gate's truth table checked in verify. **Most likely sprint to split (E10a/b)** | |
| E11 | **Integration** + 01a–03b fix pass: symbol tables in 01b, 02a, 02b; "Answer to the Predict" lines where missing (01a: 6 of 7 unanswered); mock paper re-pointed; START-HERE times; cheat-sheet tags; overlap fixes left in 01a (lattices) and 03b (`eqn_points`) | `00-START-HERE.md` · `15-mock-paper.md` · 01a–02b · cheat-sheet `src/content/` | updated files; full build of pack + cheat sheet | grep finds no reference to a removed file; every `verify_*.py` and the cheat-sheet `verify.py` pass; build prints no `OVERLAP` | |

**Learner check-ins are not sprints:** report misses on any delivered file whenever you like; the next
sprint reads them first.

---

## Verify backlog (persistent — items leave only when resolved, with the sprint that closed them)

| Item | Raised | Close in |
|---|---|---|
| Si n_i `contested` (1.0 vs 1.5 × 10¹⁰ cm⁻³; pack uses 10¹⁰ and says so) | KB 2026-06-24 | E11 (state the spread in START-HERE) |
| Stage-2 frontier specifics `uncertain`: E_crit, V_BR ∝ N^−¾, ZTC point, BV_CEO exponent, FinFET years | KB 2026-06-24 | E7 (E_crit, V_BR, ZTC) · E10 (FinFET) · E4 (BV_CEO) |
| MUJ unit and MTE/ETE boundaries `uncertain` (no hand-out, no PYQ) | KB 2026-06-16 | [learner] — when a hand-out/PYQ arrives |
| Deck special-diodes, FinFET, BJT-bias, h-parameter, multistage, CMOS-gate content is pack-only | 2026-11-13 | E10, E10, E4, E6 |
| U6 feedback and U7 oscillators not in the KB | 2026-11-13 | E8, E9 |
| Figure label overlaps found by `tools/fig_overlap_check.py` (2026-11-16): `lattice_pure_broken`, `lattice_dopants` (01a), `eqn_points` (03b), `load_line` (04), `tunnel_iv` (06), `jfet_curves` (07) | 2026-11-16 | the sprint rebuilding that file; 01a/03b in E11 |

## Assumptions to review (persistent — the learner confirms or overrules)

| # | Assumption | Made in | Status |
|---|---|---|---|
| 1 | Build order = START-HERE priority with prerequisites first (spec v1.3 §7.2), replacing S0's unit order | 2026-11-16 rewrite | open |
| 2 | Each old file becomes one or two files of ≈ 8–13 steps; a further split is allowed and logged | S0 | open |
| 3 | Delta research is done in the same sprint as its file, KB first, then the file (gate: facts from the KB, not slides) | 2026-11-16 rewrite | open |
| 4 | No separate learner check-in sprint (the old S7/S27); misses are read at the start of the next sprint | 2026-11-16 rewrite | open |
| 5 | Sessions edit nothing outside this folder (auto.py commits only this folder); needed changes to `tools/` or the spec go in the hand-off | S0 | open |
| 6 | The E0 brief lists picture slides but views only those needed for the question bank and constants; each sprint views its own decks' pictures | 2026-11-16 rewrite | open |

## EDC notes (read with the hand-off)

- **E0 head start (2026-11-18):** `study-pack-v12/src/e0-transcripts/` holds agy transcripts of 16 deck/sheet pieces (every slide/page; see its README). E0 starts from them instead of re-reading each deck: view a slide image only to check a number used in the brief or a `[?]`/`⚠` mark. Not covered: the RC-LC `.ppt`, the WSU logic PDF, the FinFET decks.

- **Decks:** `python -I research-tools/deck_extract.py exam-pack/<deck>.pptx <scratch>/<name> [first] [last]`
  → `slides.txt` + pictures `sNNN-*.jpg|png`; it prints which slides are mostly pictures. The one
  `.ppt` (`slides-U7-oscillators-RC-LC.ppt`) gives text runs in file order and pictures without
  slide numbers. Scratch = the auto.py scratch folder, never the repo.
- **PDF sheets / built pages:** `python -I research-tools/render_pages.py <file.pdf> <scratch>/<dir> [first] [last] [dpi]`;
  90 dpi for page checks, 130 for small print and scanned sheets.
- **Build:** `python study-pack-v12/src/build.py 04a 04b` builds those files and keeps the combined
  PDF complete (fixed 2026-11-16). It prints `OVERLAP` lines for any figure with clashing labels.
- **Figures:** new modules import from `tools/figlib.py`; existing `figs_u1–u3` import the v1
  `study-pack/pdf/figs.py` helpers and stay as they are.
- **Verify constants:** use the ones the pack prints (ε_Si = 1.04 × 10⁻¹² F/cm, q = 1.6 × 10⁻¹⁹ C,
  V_T = 0.0259 V, n_i = 10¹⁰ cm⁻³). Run with `PYTHONIOENCODING=utf8` (`verify_u2.py` prints non-ASCII).

## Current hand-off

```
Sprint: plan rewrite — done (2026-11-16, interactive)
Written: sprints.md (E0–E11, 12 sprints; protocol moved to ../../../study-pack-sprint-protocol.md) ·
  spec v1.3 (study-pack-format.md) · tools/study_pack_build.py (partial build keeps the combined PDF) ·
  tools/figlib.py + tools/fig_overlap_check.py (EDC: 128 figures, 13 overlaps → backlog)
Verified this sprint: partial build of 01b → combined PDF still 171 pp.
Open (carried): learner's misses on 01a–03b not given (non-blocking)
Decisions made: Assumptions 1, 3, 4, 6 (new); 01a–03b count as v1.3, fixed in E11
Assumptions to review: 1–6
Next sprint: E0 — brief — first action: run deck_extract.py on every deck in exam-pack/ into the
  scratch folder; start src/brief.md with one section per deck (slide text summary, picture slides,
  slips).
Read at start: this hand-off · E0 row · ../../../study-pack-sprint-protocol.md · spec §7.1 ·
  knowledge-base/exam-map.md · exam-pack/README.md
```
