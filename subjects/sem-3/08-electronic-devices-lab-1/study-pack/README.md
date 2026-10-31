# ECE2130 Electronic Devices Lab — lab pack

- **Read:** `pdf/ECE2130-ED-Lab-pack.pdf` (83 pp., bookmarked) or the per-chapter PDFs in `pdf/`.
- **Edit:** `src/content/*.md` (text), `src/figures.py` (circuits and plots). PDFs are generated; never edit them by hand.
- **Rebuild:** `cd src && python sim/sims.py && python sim/design.py && python build.py` (needs LTspice, markdown,
  schemdraw, ziamath, matplotlib, pypdf, numpy and Google Chrome).
- **Numbers:** every expected value comes from LTspice runs of the manual's own circuits (`src/sim/out/results.json`,
  `design.json`). Scope = the lab manual `../exam-pack/MANUAL-ECE2130-ED-lab-2025-26.pdf`; theory checked against
  `../../03-electronic-devices-1/knowledge-base/`.
