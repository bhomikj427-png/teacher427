# ECE2106 Electronic Devices & Circuits — Build & Research Sprints

> **Learner rule (stated 2026-11-15, pedagogy; extended to EDC 2026-11-16):** work runs in sprints.
> **One sprint = one session**, fully finished (researched *and* written, or built *and* checked),
> ending with a hand-off below so the next session starts from files, never from carried context.
> A sprint too big to finish splits into a/b — it is never half-done.
>
> **Goal of this plan:** the v1.2 study pack (`study-pack-v12/`) rebuilt from scratch at the
> 01a–03b depth for files 04–15 (learner, 2026-11-16: "not a build from scratch explaining every
> term and variable and then combining them together properly … work on the next ones"), and the
> ECE2106 scope delta (special diodes, CMOS/FinFET, BJT bias/stability, h-parameters/multistage,
> U6 feedback, U7 oscillators) researched into `knowledge-base/` **before** the pack files that
> rest on it. Plan written 2026-11-16; the old plan lines in `../research-engine/research-queue.md`
> point here.

---

## Definitions used by every sprint

- **Verified** = checked **this session** at a tier-1 text — a prescribed textbook passage
  (`course-info.md`: Boylestad, Sedra–Smith, Streetman, Sze, Gray, Neamen) or, when none of those
  is readable, **two** agreeing university-author texts/notes (e.g. Hu, *Modern Semiconductor
  Devices for ICs*, open online; MIT OCW; NPTEL transcripts checked against a text) — **or** a
  number/derivation recomputed by the pack's `verify_*.py`. A professor slide, web summary or AI
  answer is **not** verification: it sets scope or gives a lead. Anything else is tagged
  `uncertain` and goes to the Verify backlog.
- **Professor material = scope, textbook = truth** (`subject-research-protocol.md` §2). A fact is
  never taught straight off a slide. Deck slips are flagged in a note box and in START-HERE's slip
  table, with the corrected version used.
- **Pack sprint "P"** = rebuild one topic file. **Research sprint "K"** = bring one delta topic to
  stage-2 in `knowledge-base/`. **[learner]** = needs the learner; an unattended session reaching it
  stops with `STATUS: BLOCKED`.

---

## Sprint protocol (every sprint, fixed order)

**Session entry (before anything else)**
0. `CLAUDE.md` session-start steps 0–0b as usual (load `learner-preferences.md`; `git status` —
   under auto.py, skip the commit step: auto.py commits). No start-of-session recall: nothing has
   been taught; **the hand-off below is the resume.** The trigger phrase is the sprint id ("S3").

**Start (context hygiene)**
1. Read only: this file's *Current hand-off* block → the sprint's **Inputs** list → `CLAUDE.md`
   rules already loaded. Do not read other pack/KB files "for context"; if a file is needed, it
   must be in Inputs. Read long files by section (grep the heading, then read that range).
2. Log the sprint start in `progress-log.md` (log-first rule: the log line comes before any other
   file changes).

**Research (K sprints; also any fact a P sprint finds missing from the KB)**
3. Every load-bearing claim (definition, formula, mechanism, constant, typical value) is
   **verified** (definition above). Formulas are also re-derived or recomputed in a script.
4. **Write-as-you-verify.** Verify one claim → write it into the KB file at once (source +
   confidence tag `settled` / `contested` / `uncertain` / `suspect`) → next claim. Never batch.
5. Unverifiable this session → `uncertain` + Verify backlog row; never written as fact.
6. KB file shape = the existing unit files: `## Stage 1 (MUJ level)` (definitions, mechanism,
   formulas, worked-problem patterns, key formulas) and `## Stage 2` (why it works, derivations,
   limits of each model). Sources → `knowledge-base/sources.md` (tiered); one line in
   `knowledge-base/CHANGELOG.md`; deck evidence row in `knowledge-base/exam-map.md`.
7. **Misconceptions are a first-class output.** Each K sprint adds ≥ 3 entries to
   `knowledge-base/misconceptions.md` in that file's format, from the sources read, from the decks'
   own slips, and from common student errors.

**Build (P sprints — the content standard is `study-pack-format.md` §4–§7, v1.2)**
8. Order inside the file follows the professor's deck for that topic (read with
   `research-tools/deck_extract.py`; picture slides are read as images). Real questions come from
   the decks/numerical sheets first (tagged), Predict prompts otherwise.
9. **Build up, then combine (§6).** The file opens with a symbol table (symbol · meaning in this
   file · typical value) and, where numbers recur, one running example used by every graph. Every
   variable is explained (what it counts, unit, what sets it, a typical number) before its formula;
   a combined result gets its own step naming each piece and the file/step it came from; terms from
   earlier files are recalled in one line with file + step. One idea per step, never merged.
10. Every graph's caption says what each axis is and what one point means. Figures go in a new
    module `src/figs_uNN.py` (NN = the old file number, e.g. `figs_u4.py` for 04a/04b), registered
    in `src/build.py` like `figs_u3`. Old v1 figures may be reused only if they meet this rule.
11. Every number printed in the file — teaching, answers, Checks, Self-test — is recomputed in a new
    `src/verify_uNN.py` (pattern: `verify_u3.py`, `chk(name, got, printed, rel)`, exit non-zero on a
    failure) using the constants the pack prints. It passes, and all earlier `verify_*.py` still pass.
12. Build: `python src/build.py <prefixes>` for the file, then **always a full `python
    src/build.py`** (a subset build leaves the combined PDF holding only that subset). Render every
    page of the new file(s) with `research-tools/render_pages.py` and look at each one; fix
    overlaps, cut captions, unrendered math, wrong colour words in captions.
13. Replace, don't duplicate: remove the old file's `src/content/`, `html/`, `pdf/` copies; update
    `00-START-HERE.md` (ranked row, unit map, what-each-file table, slip table, "how checked") and
    every cross-reference (`grep -rn "<old name>" src/content`); re-point `15-mock-paper.md` rows.

**Close**
14. Self-check the sprint's **Done-when** item by item; anything failing → stays open in the
    hand-off (sprint marked `partial`, never `done`).
15. Move every open item into the **Verify backlog** and new assumptions into **Assumptions to
    review** (both persist; the hand-off is overwritten). Overwrite *Current hand-off* (template
    below); tick the sprint in the table; overwrite the progress-log *Where we stopped* / *Next up*
    lines; commit + push (under auto.py: no git — auto.py commits).

---

## Sprint table

Source key: decks/sheets in `exam-pack/` (index `exam-pack/README.md`); old file = `study-pack-v12/src/content/<old>.md`; KB = `knowledge-base/`; spec = `../../../study-pack-format.md` §4–§7. **Every P sprint's Inputs also include:** spec §4–§7 · `03b-diode-iv-capacitance.md` lines 1–60 (format model: header, map, symbol table, step 1) · `src/build.py` · `src/verify_u3.py` lines 1–40 · `src/figs_u3.py` lines 1–40 (imports/helpers) · the previous P sprint's file header + symbol table (to recall terms by file/step).

| # | Sprint | Inputs (read only these) | Outputs | Done when | Status |
|---|---|---|---|---|---|
| S0 | Sprint setup | progress-log, course-info, research-queue row, pedagogy sprints.md | this file; `research-tools/deck_extract.py`, `render_pages.py` | tools tested on a .pptx, the .ppt and a PDF | **done 2026-11-16** |
| S1 | **P 04a — diode circuits**: load line, Q-point, the three models applied, series and parallel circuits, AND/OR diode gates (deck L08 order) | old `04-diode-circuits` steps 1–2 · KB `02-pn-junctions` §Diode models, §Diode circuits · `stage-2/02` matching § · deck L08 · `03b` step 9 (models) | `04a-diode-load-line-circuits.md`, `figs_u4.py`, `verify_u4.py` | protocol 8–13 all hold; every L08 worked example reproduced with the deck's numbers or flagged; verify_u1–u4 pass; combined PDF full build | |
| S2 | **P 04b — rectifiers**: half-wave (V_dc, V_rms, PIV, efficiency), full-wave centre-tap and bridge, ripple and the capacitor filter if the deck has it (deck L09 order) | old `04` steps 3–4 + Exam form/Traps · KB `02` §Diode circuits · deck L09 · `04a` header + symbol table | `04b-rectifiers.md`; old `04-diode-circuits` removed; figs/verify extended | same; every formula derived from a waveform step, not stated; old 04 gone from content/html/pdf and every cross-ref | |
| S3 | **P 05a — clippers, clampers, multipliers** (deck L10 order) | old `05-clippers-clampers-zener` steps 1–4 · KB `02` §Diode circuits · deck L10 · `04b` header | `05a-clippers-clampers.md`, `figs_u5.py`, `verify_u5.py` | same; each clipper/clamper output waveform plotted from the circuit, not drawn by hand | |
| S4 | **P 05b — breakdown, Zener regulator, Schottky** | old `05` steps 5–6 · KB `02` §Breakdown, §Special diodes (Zener, Schottky) · `stage-2/02` breakdown § · deck L10 Zener slides · `03b` step 4 | `05b-breakdown-zener-schottky.md`; old `05` removed | same; regulator load-range limits worked both ends (I_Z min / max) | |
| S5 | **K 06 — special diodes to stage-2**: LED (band gap → colour, efficiency), photodiode (generation, modes, responsivity), tunnel diode (degenerate doping, negative resistance) | KB `02` §Special diodes · `stage-2/02` · deck special-diodes · `sources.md` tier list | `knowledge-base/06-special-diodes.md` (Stage 1 + Stage 2); sources, CHANGELOG, exam-map rows; ≥ 3 misconceptions | every load-bearing claim verified or `uncertain`+backlog; each device has mechanism + I–V + one worked number | |
| S6 | **P 06 — special diodes** rebuilt (may split 06a/06b if > 12 steps) | old `06-special-diodes` · KB `06-special-diodes.md` · deck special-diodes · `05b` header | `06-special-diodes.md` rebuilt (or 06a/06b), `figs_u6.py`, `verify_u6.py` | protocol 8–13; Unit 2 (03a–06) complete in the combined PDF | |
| S7 | **[learner] Unit 2 check-in** | — | learner's misses (or verdict) on 03a–06, logged | learner has answered; depth/shape changes written into spec §6 if any | |
| S8 | **P 07a — JFET: what it is and Shockley's equation** (construction, channel + gate junction from 03a, pinch-off, output and transfer curves, I_DSS, V_P) | old `07-jfet` steps 1–2 · KB `03-jfets` · `stage-2/03` · deck U3 jfet · numericals sheet Q1–Q19 (render pages) | `07a-jfet-operation.md`, `figs_u7.py`, `verify_u7.py` | protocol 8–13; Shockley derived from the channel picture, each term built first | |
| S9 | **P 07b — JFET parameters, bias, amplifiers** (g_m, r_d, g_d, μ = g_m r_d [the "8 marks" TIP], self-bias, voltage-divider bias, CS/CD gain) | old `07` steps 3–6 + Exam form · KB `03-jfets` · TIP file · numericals sheet Q1–Q19 · `07a` header | `07b-jfet-bias-amplifiers.md`; old `07-jfet` removed | same; every sheet question Q1–Q19 used is solved in verify; sheet answers compared, mismatches flagged | |
| S10 | **P 08a — MOSFET: structure, types, regions, current equations** (MOS capacitor, V_t, E- vs D-type, triode/saturation, the region test, square law) | old `08-mosfet` steps 1–2 · KB `04-mosfets` §Structure → §Square law · `stage-2/04` · decks U4 types-and-characteristics | `08a-mosfet-operation.md`, `figs_u8.py`, `verify_u8.py` | protocol 8–13; region boundaries derived, not stated | |
| S11 | **P 08b — MOSFET biasing and small signal** (D-/E-MOSFET bias circuits, g_m, CS/CD/CG) | old `08` steps 3–4 · KB `04` §Small-signal · deck U4 biasing · numericals sheet Q20–Q31 · `08a` header | `08b-mosfet-bias-amplifiers.md`; old `08` removed | same; sheet Q20–Q31 used are solved in verify | |
| S12 | **K 09 — MOSFET switch, CMOS gates, FinFET to stage-2** (switch resistance, inverter VTC/noise margins, NAND/NOR sizing, FinFET structure, why fins, fabrication outline) | KB `04` §Switch, §Digital circuits · `stage-2/04` · decks U4 finfet ×2, WSU logic PDF (render pages), mosfet biasing-and-digital | `knowledge-base/09-cmos-finfet.md`; sources, CHANGELOG, exam-map; ≥ 3 misconceptions | as S5; FinFET year/node claims verified or `uncertain` (existing KB flags them) | |
| S13 | **P 09 — MOSFET switch, CMOS logic, FinFET** | old `09-cmos-finfet` · KB `09-cmos-finfet.md` · same decks · `08b` header | `09-cmos-finfet.md` rebuilt (or 09a/09b), `figs_u9.py`, `verify_u9.py` | protocol 8–13; every gate's truth table checked in verify | |
| S14 | **P 10 — BJT operation** (construction, carrier flow across two junctions built from 03a/03b, α, β, γ, active/saturation/cutoff, CB/CE/CC, BJT vs MOSFET) — split 10a/10b if > 12 steps | old `10-bjt-operation` · KB `05-bjts` §Construction → §Characteristics, §BJT vs MOSFET · `stage-2/05` · decks L20, L21, L22, L23-25 | `10-bjt-operation.md` rebuilt (or 10a/10b), `figs_u10.py`, `verify_u10.py` | protocol 8–13 | |
| S15 | **K 11 — BJT bias stability to stage-2** (Q-point drift: I_CO, V_BE, β with T; stability factors S, S′, S″ derived for fixed, collector-feedback, emitter, voltage-divider bias; diode/thermistor compensation) | KB `05` §Biasing · `stage-2/05` · deck L26-27 | `knowledge-base/11-bjt-bias-stability.md`; sources, CHANGELOG, exam-map; ≥ 3 misconceptions | as S5; each S expression derived in a script (symbolic or numeric check) | |
| S16 | **P 11a — DC load line, Q-point, fixed bias, why the Q-point drifts** | old `11-bjt-biasing` steps 1–2 · KB `11-bjt-bias-stability.md` · deck L23-25 load line, L26-27 · `10` header | `11a-bjt-load-line-fixed-bias.md`, `figs_u11.py`, `verify_u11.py` | protocol 8–13 | |
| S17 | **P 11b — emitter bias, voltage-divider bias, stability factor, compensation** | old `11` steps 3–5 + Exam form · KB `11-bjt-bias-stability.md` · deck L26-27 · `11a` header | `11b-bjt-stable-bias.md`; old `11` removed | same; the deck's full S derivation reproduced line by line | |
| S18 | **K 12 — h-parameters, CE analysis, cascading, Darlington to stage-2** | KB `05` §Small-signal · `stage-2/05` · deck L26-27 h-parameter slides · deck multistage-and-Darlington · h-parameter sheet (book pp. 131–145, render pages) | `knowledge-base/12-h-parameters-multistage.md`; sources, CHANGELOG, exam-map; ≥ 3 misconceptions | as S5; A_i, Z_i, A_v, Z_o formulas derived from the two-port equations in a script | |
| S19 | **P 12a — the h-parameter model and CE analysis** | old `12-h-parameters` steps 1–2 · KB `12-…md` · h-parameter sheet · `11b` header | `12a-h-parameter-ce.md`, `figs_u12.py`, `verify_u12.py` | protocol 8–13; sheet Problems used are solved in verify, book answers compared | |
| S20 | **P 12b — cascading stages and the Darlington pair** | old `12` steps 3–4 + Exam form · KB `12-…md` · multistage deck · sheet · `12a` header | `12b-multistage-darlington.md`; old `12` removed | same | |
| S21 | **K 13 — U6 feedback to stage-1 + stage-2** (A_f = A/(1+Aβ) derived, sampling/mixing, the four topologies, effect on gain, bandwidth, Z_in, Z_out, distortion, noise, desensitivity) | `course-info.md` scope delta · deck U6 feedback-amplifiers · old `13-feedback` (for deck slips already found) | `knowledge-base/13-feedback.md`; sources, CHANGELOG, exam-map; ≥ 3 misconceptions | as S5; each topology's Z_in/Z_out factor checked in a script | |
| S22 | **P 13 — feedback** (split 13a/13b if > 12 steps) | old `13-feedback` · KB `13-feedback.md` · deck U6 · `12b` header | `13-feedback.md` rebuilt (or 13a/13b), `figs_u13.py`, `verify_u13.py` | protocol 8–13; deck slide-32 slip (98.3 → 98.0) kept in the slip table | |
| S23 | **K 14 — U7 oscillators to stage-1 + stage-2** (Barkhausen, start-up vs steady state, RC phase-shift R_f = 29R derived, Wien bridge, Hartley/Colpitts frequencies, crystal model and series/parallel resonance) | `course-info.md` scope delta · decks U7 RC-LC (.ppt) + crystal · old `14-oscillators` | `knowledge-base/14-oscillators.md`; sources, CHANGELOG, exam-map; ≥ 3 misconceptions | as S5; 29 and 1/(2π√6RC) derived symbolically in a script | |
| S24 | **P 14a — Barkhausen, RC phase-shift, Wien bridge** | old `14-oscillators` steps 1–3 · KB `14-oscillators.md` · deck U7 RC-LC · `13` header | `14a-oscillators-rc.md`, `figs_u14.py`, `verify_u14.py` | protocol 8–13 | |
| S25 | **P 14b — LC (Hartley, Colpitts) and crystal oscillators** | old `14` steps 4–5 + Exam form · KB `14-oscillators.md` · decks U7 ×2 · `14a` header | `14b-oscillators-lc-crystal.md`; old `14` removed | same | |
| S26 | **Integration** — mock paper re-pointed to the new files, START-HERE times re-estimated, cheat sheet (`study-pack-v12/cheatsheet/`) tags for 04–06 re-pointed, `course-info.md` status line, full build of pack + cheat sheet, every `verify_*.py` + cheat-sheet `verify.py` passes | `00-START-HERE.md` · `15-mock-paper.md` · cheat-sheet `src/content/` tags (grep) · `course-info.md` Status | updated 00, 15, cheat sheet, course-info; proposed new `research-queue.md` row text written into the hand-off (that file is outside this folder) | grep finds no reference to a removed file; combined PDF page count logged; all scripts pass | |
| S27 | **[learner] final review** | — | learner's misses on 07–15; the S26 research-queue row applied (interactive session, outside auto.py's scope); stage stamp `stage-2✓ (ECE2106 scope)` if every K sprint closed its backlog rows | learner has answered | |

Unattended run before the first stop: **S1–S6** (6 sprints). After S7: **S8–S26** (19 sprints).

---

## Hand-off template (overwrite *Current hand-off* each sprint end)

```
Sprint: Sx — <name> — done | partial (date)
Written: <files, one line each, with what they now contain>
Verified this sprint: <key claims + source, or "numbers: verify_uNN.py, N checks pass">
Open (carried): <unverified claims, page fixes left, anything failing Done-when>
Decisions made: <scope/split/naming choices the next sprint must respect>
Assumptions to review: <new numbered items, also copied to the persistent section below>
Next sprint: Sy — first action: <one concrete step>
Read at start: <exact file list = Sy Inputs>
```

## Verify backlog (persistent — items leave only when resolved, with the sprint that closed them)

| Item | Raised | Close in |
|---|---|---|
| Si n_i `contested` (1.0 vs 1.5 × 10¹⁰ cm⁻³; pack uses 10¹⁰ and says so) — carried from the 2026-06-24 KB pass | KB 2026-06-24 | S26 (state the spread in START-HERE) |
| Stage-2 frontier specifics still `uncertain` in the KB: E_crit, V_BR ∝ N^−¾, ZTC point, BV_CEO exponent, FinFET years (`CHANGELOG.md`) | KB 2026-06-24 | S4 (E_crit, V_BR, ZTC) · S12 (FinFET) · S15 (BV_CEO) |
| MUJ unit and MTE/ETE boundaries `uncertain` (no hand-out, no PYQ) | KB 2026-06-16 | [learner] — when a hand-out/PYQ arrives |
| Deck special-diodes, FinFET, BJT-bias, h-parameter, multistage, CMOS-gate content is pack-only (built 2026-11-13 without stage-2) | 2026-11-13 | S5, S12, S15, S18 |
| U6 feedback and U7 oscillators not in the KB | 2026-11-13 | S21, S23 |

## Assumptions to review (persistent — the learner confirms or overrules; rows leave only with that answer)

| # | Assumption | Made in | Status |
|---|---|---|---|
| 1 | Files are rebuilt in **unit order** (04 → 15), not START-HERE priority order (spec §7), because the "build up, then combine" rule makes each file recall terms from the one before it; START-HERE ranking is unchanged | S0 | open |
| 2 | Each old file is rebuilt as one or two new files of ≈ 12 steps (03 → 03a/03b set the size); a/b names are fixed in the sprint table, a further split is allowed and logged | S0 | open |
| 3 | Pack files for the delta topics wait for their K sprint (gate: facts from the KB, not slides), even though the old pack already covers them | S0 | open |
| 4 | One [learner] check-in after Unit 2 (S7) so a depth problem is caught before 19 more files; the learner can delete S7 to run straight through | S0 | open |
| 5 | Sessions do not edit anything outside this subject folder (auto.py commits only this folder): a needed change to `tools/study_pack_build.py`, `study-pack-format.md` or `research-queue.md` is written into the hand-off for an interactive session | S0 | open |

## Research and build tooling notes (read with the hand-off)

- **Decks:** `python -I research-tools/deck_extract.py exam-pack/<deck>.pptx <scratch>/<name> [first] [last]`
  → `slides.txt` (text per slide) + pictures `sNNN-*.jpg|png`; it prints which slides are mostly
  pictures — Read those images (the U1–U2 deck's slides 46–100 are mostly pictures). The one `.ppt`
  (`slides-U7-oscillators-RC-LC.ppt`) gives text runs in file order and pictures without slide
  numbers (no `olefile` installed). Scratch = the auto.py scratch folder, never the repo.
- **PDF sheets / built pages:** `python -I research-tools/render_pages.py <file.pdf> <scratch>/<dir> [first] [last] [dpi]`
  then Read the PNGs. 90 dpi for page checks, 130 for small print and scanned sheets.
- **Build:** `python study-pack-v12/src/build.py 04a 04b` (subset) then `python study-pack-v12/src/build.py`
  (full; required last). Chrome headless renders the PDFs (path set in `tools/study_pack_build.py`).
- **Markup that bites (found 2026-11-16):** `|` separates `[[fig:name|caption|w=NN]]` fields, so a
  caption must not contain `|` (write "magnitude of I_D"); `$$…$$` handles `\frac`, `\sqrt` but not
  `\left`/`\right`; note titles are uppercased by CSS (η became "H" — keep Greek out of titles);
  a Predict line starting with "+" renders as a bullet; circled digits ①② fail inside mathtext
  labels (`_m()` turns `X_y` into mathtext).
- **Verify scripts:** run with `PYTHONIOENCODING=utf8` on Windows if one prints non-ASCII
  (`verify_u2.py` does). Use the constants the pack prints (ε_Si = 1.04 × 10⁻¹² F/cm,
  q = 1.6 × 10⁻¹⁹ C, V_T = 0.0259 V, n_i = 10¹⁰ cm⁻³) so printed and checked numbers agree.
- **Shell under auto.py:** no `$VAR`, loops, `cd … &&` with writes; long edits with the Edit tool;
  multi-step jobs as a small Python script in `research-tools/` (committed) or the scratch folder.

## Current hand-off

```
Sprint: S0 — sprint setup — done (2026-11-16)
Written: sprints.md (this file) · research-tools/deck_extract.py (pptx text + pictures per slide;
  .ppt text runs + pictures) · research-tools/render_pages.py (PDF pages → PNG) · progress-log
  setup line + resume pointer · research-queue.md row pointer (outside this folder; done in the
  interactive setup session)
Verified this sprint: tools tested on deck L08 (.pptx, 19 slides, picture slides listed), the U7
  .ppt (310 text runs, 8 pictures) and 04-diode-circuits.pdf (pages 1–2 rendered)
Open (carried): learner's misses on 03a/03b not yet given (non-blocking; S7 collects them)
Decisions made: unit order; one file ≈ 12 steps; K before P for delta topics; S7 check-in
  (Assumptions 1–5)
Assumptions to review: 1–5 (persistent table)
Next sprint: S1 — P 04a diode circuits — first action: extract deck L08
  (slides-U2-L08-diode-load-line-and-series-parallel.pptx) and read its picture slides
  4, 8–15, 17, 18; list its worked examples with their numbers.
Read at start: sprints.md (hand-off, S1 row, protocol 8–13, tooling notes) · spec §4–§7 ·
  03b-diode-iv-capacitance.md lines 1–60 and step 9 · old 04-diode-circuits.md steps 1–2 ·
  knowledge-base/02-pn-junctions.md §Diode models + §Diode circuits · stage-2/02 matching § ·
  src/build.py · src/verify_u3.py lines 1–40 · src/figs_u3.py lines 1–40
```
