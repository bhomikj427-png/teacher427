# Verilog — Sources (tiered per protocol §2)

> Tiered by authority. `[date accessed]` for moving-field items. The researcher is a model →
> recall ≠ sourced (§1); anything below not yet reached at primary level is marked accordingly,
> and load-bearing leaf facts get verified at the deep pass.

## Tier 1 — Primary / foundational
- **IEEE 1364 (Verilog HDL standard)** — 1995 / 2001 / 2005; merged into IEEE 1800 (SystemVerilog)
  in 2009. The language's formal definition (syntax, semantics, data types, gate-level modeling,
  scheduling/simulation semantics). *Accessed via IEEE SA listing 2026-06-15; full text not read
  this session — §5 scheduling semantics queued for the deep pass on blocking/nonblocking.*
  https://standards.ieee.org/ieee/1364/3641/
- **Harris & Harris, *Digital Design and Computer Architecture*** (MIPS & RISC-V editions) —
  canonical undergraduate text; Ch.2 Combinational Logic Design, Ch.3 Sequential Logic Design,
  HDL examples integrated. Tier 1 for the digital-logic foundation + standard teaching order.
  *Confirmed structure 2026-06-15; not read in full this session.*
- **Cummings, C.E., "Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!"**,
  SNUG 2000 (Sunburst Design). The field's canonical documented-error reference; source of the
  **8 coding guidelines** and the blocking/nonblocking scheduling explanation. Tier 1 for
  craft/documented-error (protocol §2 tacit-knowledge remap). *Guidelines extracted via multiple
  mirrors 2026-06-15; PDF body (scheduling mechanism detail) not fully rendered — re-read at deep
  pass.* Mirror: https://csg.csail.mit.edu/6.375/6_375_2009_www/papers/cummings-nonblocking-snug99.pdf
- **Cummings, "RTL Coding Styles That Yield Simulation and Synthesis Mismatches"** (SNUG) —
  documented sim/synth-mismatch sources (full_case/parallel_case, x, casex). *Used 2026-06-15.*
- **Cummings, "Synchronous Resets? Asynchronous Resets? I am so confused!"** SNUG 2002 — the
  canonical reset-strategy discussion (sync vs async, reset synchronizer). Tier 1 craft.
  *Used 2026-06-15 (via search excerpt + hosted PDFs at gstitt.ece.ufl.edu / lcdm-eng.com).*
- **Accellera — "scheduling semantics" extract of IEEE Std 1364-2001 §5** (sv-ec att-0836) — the
  stratified event queue (active/inactive/NBA/monitor regions), RHS-in-active / LHS-in-NBA rule.
  Tier 1 (standards-body reproduction of the standard). *Used 2026-06-15; PDF body didn't render in
  fetch — region model corroborated via chipverify scheduling page (HTML).*
- **Pong P. Chu — "SystemVerilog vs Verilog in RTL Design"** (textbook author) — SV RTL features
  (logic, always_comb/_ff, enum) and recommendation. Tier 1/2. *Used 2026-06-15 via search excerpt;
  PDF body didn't render — corroborated with Wikipedia SystemVerilog + industry commentary.*
- **Tumbush, "Signed Arithmetic in Verilog 2001 — Opportunities and Hazards"** DVCon 2005 — signed/
  unsigned expression hazards. Tier 2 (conference paper). *Used 2026-06-15.*

## Tier 1/2 — Syllabus anchors (course scope/sequence, added 2026-06-29)
- **IIT Kharagpur — NPTEL/SWAYAM "Hardware Modeling using Verilog"** (Prof. Indranil Sengupta) —
  the chosen **primary syllabus anchor** for Verilog scope & sequence (8-week layout: W1 design
  flow · W2 variables/operators/constructs · W3 combinational · W4 sequential · W5 testbenches/
  simulation · W6 behavioral vs structural · W7 pipelining/memory · W8 processor design). Anchor for
  *scope/emphasis* only — truth still triangulated to Harris & Harris/IEEE. Lectures ingestible via
  `tools/fetch_transcripts.py`. *Syllabus PDF read 2026-06-29.*
  https://onlinecourses.nptel.ac.in/noc22_cs94/preview · https://nptel.ac.in/courses/106105165
- **UC Berkeley — EECS151 "Introduction to Digital Design and Integrated Circuits"** — secondary
  syllabus anchor for the **job-grade framing**: Verilog for comb/seq + FSMs, datapath blocks
  (adders/multipliers/shifters/memories), FPGA *and* ASIC flow, industrial EDA/verification tools,
  a RISC-V-based capstone. *Course site reviewed 2026-06-29.* https://www.eecs151.org/

## Tier 2 — Authoritative secondary
- **Doulos** (knowhow/verilog — RTL Verilog) — respected commercial HDL training house; RTL
  definition & synthesizable-subset framing. *Page 403'd on direct fetch 2026-06-15; relied on via
  search excerpt.*
- **DigiKey "Introduction to FPGA" / "Types of Modeling in Verilog"** tutorials — vendor-adjacent,
  reasonable quality, used for the abstraction-level taxonomy and testbench orientation.
- **UC Berkeley EECS151 — "Finite State Machines in Verilog"** (course PDF) — FSM structure/styles.
- **Xilinx/AMD university FSM lab; CDC references (EDN, AnySilicon, eternallearning CDC)** —
  metastability, two-flop synchronizer, MTBF. Used for U11.
- **Wikipedia — SystemVerilog** — SV/Verilog relationship & feature lineage (corroboration).
- **verilogpro.com ("X Optimism"), realdigital.org (parameters)** — focused, credible explainers.

## Tier 3 — Derivative (orientation / leads only)
- **Wikipedia — Verilog / IEEE 1364** — history, standard lineage, scope. Corroboration only.
- **chipverify.com, nandland.com, asic-world.com** — widely-used Verilog tutorial sites; decent
  for orientation on always blocks, blocking/nonblocking, testbenches. **Leads, not final word.**

## Tier 4 — Low-trust (chased, not cited)
- Misc. content-farm/Q&A/Scribd/Studocu hits surfaced in search — used only to locate Tier 1–2
  originals; **never** the basis of a claim.

---
### To upgrade (standing — none blocking; teach-ready)
1. Obtain a *rendering* copy of **IEEE 1364-2005 §5** and the **Cummings paper body** if paywall
   access appears — to replace the (already-corroborated) secondary descriptions with verbatim
   primary text. Not required to teach; the mechanism is triangulated across two independent
   descriptions.
2. **Recheck on re-entry** (moving field): SystemVerilog-vs-Verilog industry default; synthesis-tool
   specifics (Vivado/Quartus/Yosys edge behaviors).
