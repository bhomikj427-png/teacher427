# Verilog — Progress Log

> Written **live** as sessions happen (not reconstructed at wrap-up). Session-resume block is
> overwritten each session-end; Session history is append-only. See `../README.md`.

## Session resume
- Last session: 2026-07-03 (orientation session — **this log was not updated that day; block
  reconstructed 2026-07-05 from dated on-disk artifacts, not from memory** — see the ⚠ history
  entry. Confirm against learner recall at next session start.)
- Where we stopped (per artifacts): orientation lesson rendered + saved
  (`lessons/00-orientation/2026-07-03-verilog-the-learning-path.html`); its flow map places the
  learner at **Stage 3 (combinational logic) "YOU ARE HERE", Stage 4 (sequential) next** — implying
  at least a partial diagnostic placement happened. Same day: Verilog override logged (no
  gate-level reproduction drills, `learner-profile.md`) + two universal prefs
  (`learner-preferences.md` §1 no-scaffolding-language, §3 flow-map + sub-maps). **Unknown:**
  whether any concept was taught/checked beyond orientation — nothing was logged; treat nothing as
  mastered.
- Earlier state (2026-06-29): KB fully built (units 01–12), backlog cleared; goal re-framed to
  internship/job edge, step #1 of `../_career-roadmap/roadmap.md`; anchored to NPTEL-KGP
  (Sengupta) + Berkeley EECS151; 3 scope-extensions queued, not built.
- Recap (what happened):
  - Set goal (professional RTL) and rough level (developing — built half/full adder).
  - Built the Verilog knowledge base to protocol standard: map, misconceptions (9), sources,
    changelog, curriculum — then, at learner's request, the **exhaustive deep pass** (per-unit deep
    notes 01–12 for the whole curriculum).
  - Resolved all closable open items (event-queue scheduling, x/z synthesis, SV-vs-Verilog
    decision, Cummings guidelines). Only genuinely-open items left: learner diagnosis (T1 +
    sequential foundations) and moving-field rechecks.
  - Did **not** yet teach — diagnosis (U1) is the immediate next step.
- Where we stopped (live, 2026-07-08): diagnostic done, placed at **U3**; about to open the U3
  live project — learner's first attempt at writing a full-adder module in Verilog.
- Due for review today: nothing yet (no items mastered).

## Mastery ledger
*(empty — nothing mastered to criterion yet)*

## Spaced-review / relearning queue
*(empty — fills as items are mastered)*

## Session history
- [2026-07-08] Teaching session (Studio canvas). Start-of-session recall: learner recalled
  2026-07-03 as "tried to cover the overview, didn't get anything done" — **corroborates the
  reconstructed record; nothing-mastered assumption confirmed.** Learner asked to redo the
  overview. Plan: flow map + Phase-I sub-map on the board, then the U1 diagnostic (T1 probe +
  sequential foundations + prior-adder style), behavioral-level per the profile override.
  - Diagnostic results (typed on board 21:03): **T1 probe PASSED** — "all assign statements fire
    all at once" (concurrency model present, preliminary confirm). Full-adder recall = correct
    block model ("two half adders... count till 3, each counts till 2"); code-level style not
    recalled — unconfirmed. **Sequential foundations = zero by self-report** ("don't know shit
    about flip flops") — needs U1-level foundations before Phase II; not blocking U3.
  - Placement: **U3 confirmed** (consolidate combinational + 4-bit adder project). Routed there.
  - Surface change (learner, mid-session): Studio = diagrams only (unpolished, token-heavy);
    dialogue back in terminal. Logged to learner-preferences.md §3.
- [2026-07-06] Engine maintenance (no teaching): **Studio v3 CANVAS demo session** opened under
  `whiteboard/2026-07-06/` — teacher content now lands as objects ON one shared Excalidraw board
  (learner-directed redesign; headless-verified render: text + MathJax math + Mermaid map as
  canvas objects). Demo blocks only; nothing taught or assessed.
- [2026-06-15] Subject created. Set goal=professional, level=developing (half/full adder built).
  Researched & wrote knowledge base (map pass) + curriculum. No teaching yet.
- [2026-06-15] Exhaustive deep pass at learner request: wrote per-unit deep notes 01–12, resolved
  all closable to-verify items, updated map/sources/changelog. Base is teach-ready end-to-end. No
  teaching yet. Next: U1 diagnostic.
- [2026-06-29] Career re-frame (no teaching): goal restated as internship/job edge + step #1 of a
  track; built `subjects/_career-roadmap/roadmap.md` (Verilog → SystemVerilog → Design/DV fork →
  cross-cutting → specialize), sourced. Anchored syllabus to NPTEL-KGP (Sengupta) + Berkeley EECS151;
  mapped units→weeks in curriculum; opened 3 scope-extension items in 00-map §6; logged in CHANGELOG.
  No truth claims changed. Next: still U1 diagnostic (now with the career horizon named up front).
- [2026-07-03] ⚠ **Session happened but was never logged here — entry reconstructed 2026-07-05
  (engine audit) from dated artifacts, not memory.** Evidence: orientation lesson saved
  (`lessons/00-orientation/2026-07-03-verilog-the-learning-path.html` + its build script, flow map
  marking Stage 3 = "you are here", Stage 4 = next); Verilog override added to `learner-profile.md`
  (no gate-reproduction drills); two universal prefs added same day (`learner-preferences.md` §1/§3).
  What else the session covered is **unknown** — nothing mastered is assumed. The live-logging rule
  failed this session; systemic fix proposed in `_audit-2026-07-05.md`.
- [2026-07-05] Engine maintenance (no teaching): orientation lesson **re-rendered** from its build
  script after the Mermaid theme fix (dark→neutral — dark-theme edges/labels were low-contrast on
  the white figure cards) → new file `lessons/00-orientation/2026-07-05-verilog-the-learning-path.html`
  (2026-07-03 copy preserved, per dated-lesson rule). Content unchanged. Learner to judge the
  visual A/B.
- [2026-07-05] Engine maintenance (no teaching): **Teacher 2.0 whiteboard demo session** opened
  under `whiteboard/2026-07-05/` — a surface demo (orientation-level blocks only, no new content
  taught, nothing assessed). Purpose: learner tries live push + the sketch pad (draw → Save →
  engine reads the PNG). Demo blocks are not curriculum events. **Same day: upgraded to Studio v2
  at the learner's direction** — one app window with in-window chat (learner types, teacher
  answers in-window), camera/paste/drop intake, engine long-poll loop; same session resumed, v2
  demo blocks appended. Still zero curriculum events.
