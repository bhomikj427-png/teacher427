# Python — Learner Profile

> Current level, goals, known/observed misconceptions, and subject-specific preference overrides.
> Maintained by the engine via the self-update protocol (`../../CLAUDE.md`).

## Goal
- **End goal: resume-grade *professional* Python proficiency** — Python as a defensible resume skill
  (passes a junior–mid screen; writes correct, idiomatic, typed, tested, maintainable code).
  `[stated/locked 2026-06-16]` → all four curriculum phases are the target (Phase IV required, not
  optional); correctness + idiom + typing + testing held high from early on; aim for a small
  portfolio-worthy capstone near the end.
- **Target Python version: 3.14** (current stable 3.14.6). `[set 2026-06-16]` → teach modern syntax
  (`match`, `X|Y`, built-in generics, `type` aliases) with version notes; pin doc links to 3.14.

## Current level — **absolute zero** (re-diagnose each session)
- **Stated:** learning Python from absolute zero. `[stated 2026-06-16]`
- **Undiagnosed:** any prior programming experience in another language (would change pacing and
  which misconceptions are imported — e.g. a C/Java background makes T1 "boxes" and M5 "by value/
  reference" *more* likely, not less). → first session opens by probing this.
- Entry point: curriculum **U1**.

## Known / suspected misconceptions to watch
*(from `knowledge-base/misconceptions.md` — confirm or rule out via retrieval, don't assume)*
- **T1 / M1, M2, M3 (names bind, not copy; `is` vs `==`)** — the master threshold; **high-priority**
  from U3 on. If the learner has prior C/Java exposure, the "box" model is likely imported — probe
  early.
- **T2 / M11, M15 (mutability & aliasing)** — surfaces U5; predictable bug source.
- **M4 (mutable defaults), M5 (by value/reference), M12 (late-binding closures), M13
  (UnboundLocalError)** — surface U6; all corollaries of T1.
- **M8 (truthiness), M9 (division)** — surface U2/U4.
- **M6 (type hints enforced), M10 (privacy), M14 (re-import)** — later units (U9/U11/U13).

## Preferences (overrides)
*(Subject-specific only; these win over `../../learner-preferences.md` inside Python. None yet.)*
- [observed 2026-06-16] Wants the knowledge base researched to standard **before** teaching
  (directed a deep dive with cited sources before any instruction). → always complete/refresh the
  deep pass and cite before instructing; never teach from unverified recall. *(Also a universal
  value — already mirrored in `../../learner-preferences.md`.)*

## Tensions to manage
- None yet.
