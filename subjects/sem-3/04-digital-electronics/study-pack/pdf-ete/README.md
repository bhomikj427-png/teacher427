# ECE 2105 / ECE2102 Digital Electronics: ETE study pack

- **Read:** `DE-ETE-v1.pdf` (61 pp., A4). Parts A–E = Units 1–5, then a mock paper with key, a formula sheet and sources.
- **Format:** the EDC-ETE-v1 format (`../../../03-electronic-devices-1/study-pack/pdf/`): Q (sourced) → guess → figure → teaching → answer → Check;
  Check answers end each Part.
- **Edit:** `parts/*.html` (text), `figs1.py` (helpers, cover, Parts A–B), `figs2.py` (Parts C–E). The PDF is generated; never edit it by hand.
- **Rebuild:** `python verify.py && python build.py` (needs matplotlib, schemdraw, pymupdf and Google Chrome). Reuses the DE-v1 figures in
  `../pdf/figs.py`, the K-map renderer in `../web/figures.py` and the K-map CSS in `site/static/style.css`.
- **Answers:** `verify.py` recomputes every printed answer (192 checks: Quine–McCluskey minimum for each expression, truth-table comparison for
  MUX/decoder/PLA tables, simulation for counters and sequence detectors, re-partitioning for state reductions). `qm.py` holds the shared logic.
  It must pass before a build.
- **Review helpers:** `figtest.py` renders every figure to one preview PDF; `tile.py` and `topng.py` turn PDF pages into PNG sheets.
- **Scope:** the syllabus on slide 2 of `../../exam-pack/slides-01-…`. Questions: the 2025 MTE paper (all 8), decks 01–15, practice sets 1 and 2;
  the rest are labelled "practice". Facts from `../../knowledge-base/` (stage-2).
- **Earlier builds:** `../pdf/DE-v1.pdf` (ETE half only, 2026-10-17) and `../pdf-v2/` (one-chapter river demo). This pack supersedes DE-v1 for exam use.
