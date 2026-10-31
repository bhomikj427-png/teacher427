# ECE2131 Digital Electronics Lab — lab pack

- **Read:** `pdf/ECE2131-DE-Lab-pack.pdf` (47 pp., bookmarked) or the per-chapter PDFs in `pdf/`.
- **Edit:** `src/content/*.md` (text), `src/figures.py` (pin diagrams, K-maps, logic, TTL). PDFs are generated.
- **Rebuild:** `cd src && python verify.py && python sim/ttl.py && python build.py` (verify.py must print ALL PASS).
- **Checks:** `src/verify.py` brute-forces every design (49 checks); Exp 14 TTL gates simulated in LTspice
  (`src/sim/out/ttl.json`). Scope = `../exam-pack/MANUAL-ECE2131-DE-lab-2025.pdf`; theory = `../../04-digital-electronics/`.
