# MAS2001 Statistics & Probability — ETE study pack (format v1.2)

Built to `study-pack-format.md` (v1.2). Start with `pdf/00-START-HERE.pdf`, or use the combined, bookmarked
`pdf/MAS2001-Statistics-and-Probability-ETE-study-pack.pdf` (121 pages).

| Path | What |
|---|---|
| `src/content/*.md` | the text of every file (source of truth) |
| `src/figures.py` | the 29 generated figures (matplotlib → SVG) |
| `src/verify.py` | recomputes every number in the pack and compares the professor's keys; run before building |
| `src/build.py` | content → `html/` → `pdf/` + combined PDF (shared builder `tools/study_pack_build.py`) |

Rebuild: `cd src && python verify.py && python build.py` (one file: `python build.py 09`).

Sources: `../exam-pack/` (blueprint, MTE 2026 + key, Assignments 1, 2, 4, 5, LMS slides) and `../books/` (Gupta & Kapoor);
facts from `../knowledge-base/`.
