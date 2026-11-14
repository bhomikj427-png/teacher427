# ECE 2106 Electronic Devices & Circuits: ETE study pack

> ⚠ **Does not conform to `study-pack-format.md` (v1.2). Rejected by the learner 2026-11-14. Do not copy this pack's shape.**
> Its questions, figures and verification script are sound and are the raw material for the rebuild.

- **Read:** `pdf/EDC-ETE-v1.pdf` (63 pp., A4). Parts A–G = Units 1–7, then a mock paper with key and a formula sheet.
- **Format:** the DE-v1 format (`../../04-digital-electronics/study-pack/pdf/`): Q (sourced) → guess → figure → teaching → answer → Check; Check answers end each Part.
- **Edit:** `pdf/parts/*.html` (text), `pdf/figs.py`, `figs2.py`, `figs3.py` (every figure). The PDF is generated; never edit it by hand.
- **Rebuild:** `cd pdf && python verify.py && python build.py` (needs matplotlib, schemdraw, ziamath, numpy, scipy, pymupdf and Google Chrome; reuses
  drawing helpers from `../../08-electronic-devices-lab-1/study-pack/src/figures.py`).
- **Numbers:** `pdf/verify.py` recomputes every printed value (211 checks) and must pass before a build.
- **Review helpers:** `pdf/figtest.py` renders every figure to one preview PDF; `pdf/tile.py` tiles PDF pages into PNG sheets.
- **Scope:** the ECE 2106 syllabus on slide 2 of `../exam-pack/slides-U1-U2-…`. Questions come from the professor's decks and numerical sheets where they
  have one; the rest are labelled "practice". Units 6–7 and the deck extras are not in `../knowledge-base/` yet (see `../progress-log.md`, 2026-11-13/14).
