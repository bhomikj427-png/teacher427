# ECE2108 — Stage-2 sources (primary / graduate tier)

> Sources reached **2026-09-12** specifically for Stage 2. The Stage-1 source set
> (`../sources.md`) still applies — this file lists only what Stage 2 added, and keeps the Stage-1
> `sources.md` clean per `../../../research-engine/two-stage-depth.md`.

---

## Verified this session

| Claim | Source reached | Confidence |
|---|---|---|
| **Microprogramming's origin** — M. V. Wilkes, *"The Best Way to Design an Automatic Calculating Machine"*, **Manchester University Computer Inaugural Conference, July 1951**, proceedings **pp. 16–18**; the first presentation of microprogramming. Proposed a **variable instruction set** assembled from micro-operations, implemented with a **diode matrix** = what we now call ROM. **EDSAC 2 (1958)** was the first microprogrammed computer (control ROM from magnetic cores) | MIT Press *Ideas That Created the Future: Classic Papers of Computer Science* (ch. 15, reprints the paper); Computer History Museum catalogue entry 102655149; Bosworth, *Microprogramming: History and Evolution* | `settled` — triangulated across three independent records |
| **Deep-pipeline history** — Intel **NetBurst**: Willamette/Northwood = **20-stage** pipeline; **Prescott = 31 stages**; the stated rationale was higher clock frequency via simpler stages; the strategy was abandoned | Tom's Hardware (Prescott architecture review), AnandTech ("31 Stages"), NetBurst technical summaries | `settled` for the stage counts and the rationale; the abandonment is well documented |
| **8086 address wraparound and the A20 gate** — the 8086/8088 have only A0–A19, so addresses above 1 MB **wrap**; `FFFF:0010` = 0x100000 → **wraps to 0000:0000**. The **80286** (24 address lines) did **not** wrap in real mode (`FFFF:FFFF` → 0x10FFEF, not 0x0FFEF), breaking software that relied on the wrap. IBM's PC/AT used **spare lines in the keyboard controller** to gate **A20** and emulate the old behaviour. With A20 on, 0x100000–0x10FFEF becomes reachable from real mode = the **High Memory Area** | OS/2 Museum ("The A20-Gate Fallout"); Yale CS BIOS notes ("The High Memory Area and the A20 Line"); OSDev Wiki (A20 Line) | `settled` — three independent accounts agreeing on the mechanism, the addresses and the keyboard-controller fix |
| **The three C's of cache misses** — Hill & Smith (1989) partition: **compulsory** (referencing a previously unreferenced block), **capacity** (not compulsory, misses in both the target cache and a **fully-associative cache of equal capacity with LRU**), **conflict** (not compulsory, **hits** in that fully-associative cache but misses in the target — "because of the restriction in the address mapping and not because of lack of space"). The classification exists to **evaluate associativity** | UW CSE 471 lecture notes; Berkeley CS252 (Patterson) Lecture 7 "Memory Hierarchy — 3 Cs"; cache-modelling literature (arXiv 2001.01653) reproducing the definitions | `settled` — the operational definitions are quoted consistently across sources, including Patterson's own course material |
| **RISC-V design goals and encoding rationale** (also used in Stage 1) | **The RISC-V Instruction Set Manual, Volume I: Unprivileged ISA — RATIFIED**, `docs.riscv.org/reference/isa/v20240411/unpriv/` (intro + rv32 chapters) | `settled` — **primary standard, read directly** |

## Carried over from Stage 1 and used again here

- **[8086-BBAU]** (Babasaheb Bhimrao Ambedkar University, UIET) — the ModR/M/instruction-format tables
  underpinning stage-2 §B of U7, and the 8086/8088 queue-depth comparison including the detail that the
  **8087 identifies the CPU via pin 34** to set its own queue length.
- **[CU-BSU]** and **[CU-IOE]** — the microinstruction format that stage-2 §B of U3 analyses for the
  horizontal/vertical trade.
- **[PIPE-IOE]** and the professor's Unit-3 deck — the pipeline formulas Amdahl generalizes.
- **Ken Shirriff, righto.com (2023)** — die-level 8086 prefetch analysis; used in U7 for queue mechanics.

## Cross-subject reuse (do NOT re-derive — cite across)

| Needed for | Already built in |
|---|---|
| **Carry-lookahead / parallel-prefix adders** (U1 stage-2 §C) — Kogge-Stone O(log₂ n), Brent-Kung 2log₂ n − 2 | `../../../04-digital-electronics/knowledge-base/stage-2/01-combinational-logic-design.md` |
| **SRAM cell, butterfly SNM, DRAM charge sharing** (U6) | `../../../04-digital-electronics/knowledge-base/stage-2/05-logic-families-and-memories.md` |
| **Emerging NVM frontier** (MRAM/ReRAM/PCM/FeFET — U6 stage-2 §H) | same file (**keep the two in sync**; shared `evolving` claim) |
| **Tri-state buffers / bus contention** (U1 stage-2 §D, U5 DMA) | `../../../04-digital-electronics/knowledge-base/05-logic-families-and-memories.md` |
| **BCD +6 correction** underlying `DAA`/`AAA` (U7 stage-2 §E) | `../../../04-digital-electronics/knowledge-base/01-combinational-logic-design.md` |
| **RTL as an HDL** (U2 stage-2 §E) | `../../../../verilog/` |
| **MOSFET physics under SRAM/DRAM** (U6) | `../../../03-electronic-devices-1/knowledge-base/stage-2/04-mosfets.md` |

## Claimed from reasoning, not from a source (labelled as such in the unit files)

These are **derivations or interpretations**, explicitly marked in place. They are sound but are not
citations, and must not be presented to the learner as sourced facts:

- The **operand-counting argument** for why an accumulator machine has a one-address format
  (U2 stage-2 §B) — arithmetic, verifiable by the learner.
- The **horizontal-vs-vertical combination count** Π(mᵢ+1) vs 2^N (U3 stage-2 §B) — arithmetic.
- The **polling-vs-interrupt break-even condition** (U5 stage-2 §A) — a model, with illustrative
  constants that are **not** measured on any real machine.
- The **`LUI`/`ADDI` sign-extension compensation rule** (U8 stage-2 §B) — derived and checked
  arithmetically against a worked example (0xDEADBEEF); also standard assembler behaviour.
- The **four-option segmentation design-space table** (U7 stage-2 §A) — a *reconstruction* of the design
  rationale, not a record of Intel's deliberations.
- The **economic argument for x86's survival** (U7 stage-2 §D) — well-supported interpretation, not
  measurement.
- The **§F RISC audit verdicts** (U8) — reasoned judgements, labelled as judgements.

## Not verified this session (Stage-2 to-verify backlog)

| Item | Where used | What would settle it |
|---|---|---|
| Motorola 68000 as a **nanoprogramming** example | U3 stage-2 §B | a 68000 design reference or Motorola documentation |
| Microsequencer **return-stack depths** (4–16) | U3 stage-2 §C | a specific commercial microsequencer datasheet (e.g. Am2910) |
| **CPU ~50%/yr vs DRAM latency ~7%/yr** growth figures | U6 stage-2 §E | Hennessy & Patterson, *Computer Architecture: A Quantitative Approach* — the canonical source for these curves |
| "**2N direct-mapped ≈ N 2-way**" rule of thumb | U6 stage-2 §C | Hennessy & Patterson (it is their heuristic) |
| Modern **branch-predictor accuracy** 95–99% | U4 stage-2 §D | TAGE/perceptron predictor literature |
| **C-extension code-size reduction** ~25–30% | U8 stage-2 §E | RISC-V C-extension rationale or published measurements |
| **PDP-8 lineage** of Mano's Basic Computer | U2 stage-2 §G | a PDP-8 architecture reference |
| **Exact RV32I instruction count** | U8 stage-2 §A | count directly from the ratified opcode tables |
| **Pentium Pro (1995)** as the first x86 with internal micro-op decoding | U7 stage-2 §D | an Intel P6 microarchitecture reference |

**The single highest-value acquisition for Stage 2** would be **Hennessy & Patterson, *Computer
Architecture: A Quantitative Approach*** — it is the primary source for the memory-wall curves, the
associativity heuristics, Amdahl's quantitative treatment, and the branch-prediction data, and would
convert most of the backlog above from `likely` to `settled` in one pass.
