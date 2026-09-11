# ECE2102 Digital Electronics — sources (tiered, dated, confidence-marked)

> Per `../../../../subject-research-protocol.md` §2. Tier 0 = instructor material (scope, not truth).
> Tier 1 = prescribed/canonical texts + manufacturer datasheets (truth). Recall ≠ sourced — every
> load-bearing specific is checked against one of these *this session* before promotion past
> `uncertain`. Stage-2 primary/graduate sources will live in `stage-2/sources.md`.

## Tier 0 — instructor material (SCOPE only; never sets a fact)
- **MUJ ECE Syllabus 2023-onwards** (ECE2102), `../course-info.md` — official unit list. `settled`
  for *scope*. URL in course-info. **No PYQ/PPT in `../exam-pack/` yet** → exam-targeting `uncertain`.

## Tier 1 — prescribed textbooks (truth anchors)
- **A. Anand Kumar — *Fundamentals of Digital Circuits*, 2e, PHI 2016.** Prescribed #1. Indian-UG
  standard; problem style matches MUJ. Primary anchor for combinational/sequential worked methods.
  *(Held as canonical; specific page/number citations to be added per unit as verified.)*
- **R. P. Jain — *Modern Digital Electronics*, 4e, McGraw-Hill 2009.** Prescribed #2. Strong on
  logic families (TTL/ECL/CMOS specs), MSI, memories. Co-anchor for U5.
- **Brown & Vranesic — *Fundamentals of Digital Logic with Verilog Design*, 3e, McGraw-Hill 2013.**
  Prescribed #4. Rigorous structural treatment, FSM synthesis, the Verilog bridge (→ `../../../verilog`).
  Tier-1 for U4 FSM rigor and as a Stage-2 lean-in.
- **W. H. Gothmann — *Digital Electronics: An Introduction to Theory and Practice*, 2e, PHI 2006.**
  Prescribed #3. Not yet sourced this session — `uncertain` whether MUJ leans on it.

## Tier 1 — standard-TTL DC table + logic-family numbers (for U5)
- **Standard-TTL (7400) DC parameters — `settled` (VERIFIED + TRIANGULATED this session, U5):**
  V_OH=2.4 V, V_OL=0.4 V, V_IH=2.0 V, V_IL=0.8 V; I_OH=400 µA, I_OL=16 mA, I_IH=40 µA, I_IL=1.6 mA →
  **fan-out = 10**, **NM_H = NM_L = 0.4 V**, t_pd ≈ 10 ns. Triangulated across **four independent**
  sources:
  - Nuts & Volts "Understanding Digital Logic ICs Part 2" (nutsvolts.com) — fan-out=10 from both
    I_OL/I_IL and I_OH/I_IH, with the exact currents.
  - Cornell P360 Experiment-3 lecture notes (classe.cornell.edu) — NM = 0.4 V from the level table.
  - Macnica "What is VIH/VIL/VOH/VOL" (macnica.co.jp) — the band model.
  - EduRev/askfilo worked fan-out problems — I_OL/I_IL=10 method.
  - (Manufacturer PDFs TI SN7400 / Fairchild DM7400 <web.mit.edu/6.131/www/document/7400.pdf> and
    <pages.uoregon.edu/torrence/432/spec/7400_series.pdf> confirmed by metadata but **did not
    text-extract via WebFetch** — binary PDF; values instead triangulated from the four sources above.
    TI page confirms V_CC 4.75–5.25 V.) `settled`.
- Per-series numbers (74L/H/S/LS/AS/ALS/F, 74HC/HCT/AC) are series-dependent — `uncertain` for exact
  specifics; read the relevant datasheet. Standard-TTL table above is the anchor.

## Tier 1/2 — PLD structure (U6/§6)
- **PROM/PLA/PAL programmable-array structure — `settled` (triangulated this session):** testbook.com
  "Programmable Logic Devices", elprocus.com "PAL and PLA", international-university.eu Digital Design.
  PROM=fixed-AND/prog-OR; PLA=prog-AND/prog-OR; PAL=prog-AND/fixed-OR; fixed array is faster.

## Tier 1/2 — institutional course material (structure + triangulation)
- **IIT Roorkee Virtual Labs — Digital Electronics** (de-iitr.vlabs.ac.in / ade-iitr.vlabs.ac.in).
  Used (U1) to triangulate half/full subtractor forms (D=A⊕B⊕Bin, Bout=A′B+Bin(A⊕B)′) and
  MUX-based realizations. `settled` for those standard forms (corroborated by tutorialspoint + GfG).
- **University of Cambridge — *Digital Electronics Part I: Combinational and Sequential Logic*** (CST
  lecture notes PDF, cl.cam.ac.uk). <https://www.cl.cam.ac.uk/teaching/0708/DigElec/Digital_Electronics_pdf.pdf>
  Used (map pass) to triangulate the combinational/sequential split + FSM = combinational + state
  register structure. `settled` for course structure.
- **NPTEL — Digital Circuits / Digital Electronics (IIT)** — structured lecture companion + problem
  style; default primary where a unit needs more than the texts. Ingest via `tools/fetch_transcripts.py`
  (captions Tier-1 *with caveats*: ASR mangles numbers — verify every formula vs textbook). Not yet
  pulled this session.

## Tier 1/2 — clock-generation hardware (U4 §5, verified this session)
- **555 timer formulas — `settled` (triangulated):** astable f = 1.44/((R₁+2R₂)C), duty>50%;
  monostable T = 1.1·R·C. — allaboutcircuits 555 calc, electronics-tutorials.ws 555-circuits,
  circuitdigest 555 astable calculator.
- **Ring oscillator f = 1/(2N·t_pd), N odd — `settled` (triangulated):** JHU 216 Ch.6 handout
  (pages.jh.edu/aandreo1), elprocus ring-oscillator.
- **Code converters / Gray code / excess-3 self-complementing — `settled (standard)`** (standard texts
  + NPTEL Digital Circuits week-5 outline).

## Cross-check sources (syllabus completeness pass, 2026-06-27)
- **NPTEL "Digital Circuits" (IIT Kharagpur, S. Chattopadhyay)** — onlinecourses.nptel.ac.in/noc21_ee75,
  nptel.ac.in/courses/108105113. Week outline used to cross-check scope (surfaced: clock-gen hardware,
  parity/Hamming, code converters, and out-of-scope ADC/DAC + 8085).
- **MIT OCW 6.004 Computation Structures + 6.111 Intro Digital Systems Lab** — ocw.mit.edu. Used to
  cross-check depth (surfaced: CMOS gates-from-MOS, arithmetic structures, power; out-of-scope:
  pipelining, FPGA project flow → Verilog subject).

## Tier 3 — derivative (orientation/leads only)
- tutorialspoint, electronics-tutorials, GeeksforGeeks, bysmax — used only to orient/locate the
  canonical claim, never to settle a fact. (Map-pass FSM/structure leads.)

## Open sourcing tasks (→ register in `00-map.md`)
- Lock the standard-TTL DC table (V_OH 2.4 / V_OL 0.4 / V_IH 2.0 / V_IL 0.8, I_OH/I_OL → fan-out 10,
  t_pd ~10 ns) against the DM7400/SN7400 datasheet **in U5**, then promote to `settled`.
- Pull an NPTEL Digital Circuits playlist for U3/U4 (FSM, ASM) triangulation.
- Source Gothmann or drop it from the tier-1 set if MUJ doesn't use it.
