# ECE2131 Digital Electronics Lab — progress log

## Session resume
- Last session: 2026-10-31. Lab pack built: `study-pack/pdf/ECE2131-DE-Lab-pack.pdf` (47 pp.). Nothing taught live;
  no misses reported yet.

## Where we stopped
- 2026-10-31: pack complete and visually reviewed. Next: learner works through it and reports misses only; when the
  DSA lab manual arrives, build its pack and merge all three lab packs into one PDF (learner's stated end goal).

## Log
- `[2026-10-31]` Learner request (same as ECE2130 log): lab prep PDF from the uploaded manual; learner is comfortable with
  digital, so this pack is lighter on theory and heavy on wiring (IC pinouts, pin-to-pin connections, designs, truth
  tables). Manual filed as `exam-pack/MANUAL-ECE2131-DE-lab-2025.pdf`.
- `[2026-10-31]` Gate note: theory = ECE2102 (`../04-digital-electronics`, **stage-2✓**); manual = defined scope source.
  Every design's truth table is checked by script against the Boolean expressions used.
- `[2026-10-31]` Building `study-pack/` (src/content/*.md + figures.py + build.py, same pipeline as 08/13) →
  `study-pack/pdf/ECE2131-DE-Lab-pack.pdf`. Design check `src/verify.py`: 49 checks, ALL PASS (every expression over
  all inputs; counters, ring/Johnson, shift registers and both sequence detectors simulated clock by clock).
- `[2026-10-31]` Manual has no pages for Exp 14 (TTL NAND/NOR); built the standard 7400-type circuit and a TTL NOR in
  LTspice (`src/sim/ttl.py`): NAND 1,1→0.009 V else 3.99 V; NOR 0,0→3.99 V else ≈0.01 V; switching ≈ 1.37–1.39 V.
- `[2026-10-31]` Manual errors to flag in the pack: NOT truth table (0→0, 0→1); Fig 2.5 calls the 7483 "7485"; Table 4.2
  captioned "BCD to grey"; Exp 7 parts list 74151/74153 (needs 74138); list says detect "101", Exp 13 designs "1010"
  (pack covers both); Exp 13(ii) "FY''" = FY'; IC table lists 74138 as a JK flip-flop; 2's-complement subtractor says
  "borrow at Cout" (Cout = 1 means no borrow, A ≥ B); ring counter cleared to 0000 never runs (one FF must be preset).
- `[2026-10-31]` Built `study-pack/pdf/ECE2131-DE-Lab-pack.pdf`, 47 pp., 12 files: start-here (trainer kit, wiring
  routine, manual-errors table), Exps 1–14, revision set (23 questions). Every chapter: aim as question → guess-first →
  design → pin-to-pin wiring table → expected LEDs/table → record block → traps → check (answers at end). 28 figures
  (19 IC pin diagrams, 2 K-maps, NAND/NOR logic, counter timing, 1010 state diagram, TTL circuit + VTC), visually reviewed.
  One self-error caught in review and fixed before release: 7485 behaviour with wrong cascade inputs (all-0 cascade with
  A = B lights A>B and A<B, per the function table).
