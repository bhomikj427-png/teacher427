# ECE2107 theorems assignment

- **Read:** `pdf/ECE2107-Theorems-Assignment.pdf` (generated; never edit by hand).
- **Edit:** `src/content/*.md` (one file per part), `src/crops.py` (which book region each figure comes from).
- **Rebuild:** `cd src && python crops.py && python build.py` (needs pymupdf, markdown, pypdf, Chrome; reuses `../study-pack/src/` styling).
- Figures are cropped straight from the two books in `../../_inbox/_unsorted/` (real figures, not redrawn).
- Layout per question (marathon protocol, `../../../../marathon.md`): Question → Try it first → Hint: what's new (only if new) → compact Given / To find / steps → Answer → side note / book error.
- `manifest.md` lists every question, its ideas, book vs verified answer, and build status.
- `src/verify.py` re-solves every circuit numerically (all sources on, plus each partial).
- Every answer is re-derived and checked a second way; "= book" marks a match with a printed answer.
