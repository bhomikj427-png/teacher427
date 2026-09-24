# ECE2107 Circuits & Systems — study pack

- **Read:** `pdf/ECE2107-Circuits-and-Systems-study-pack.pdf` (everything, bookmarked) or the per-file PDFs `pdf/00…10` (order = the professor's MTE syllabus).
- **Edit:** `src/content/*.md` (text), `src/figures.py` (every circuit and plot). The PDFs are generated. Never edit them by hand.
- **Rebuild:** `cd src && python build.py` (needs markdown, schemdraw, ziamath, matplotlib, pypdf and Google Chrome).
- `html/` is the intermediate output from Chrome; it is kept so a page can be opened in a browser.

Questions come from the professor's board questions in `../exam-pack/NOTES-handwritten-2026-09.pdf` (tag *Class p.N*) and `../exam-pack/NOTES-set2-2026-09/` (tag *Set 2 p.N*); syllabus topics with no board question use textbook-style problems (tag *textbook*).
Facts are checked against `../../06-circuits-and-network-theory/knowledge-base/`, and every number in the pack was confirmed by simulation (`src/verify_mte.py` for the MTE additions).
