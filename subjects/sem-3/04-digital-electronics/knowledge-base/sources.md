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

## Tier 1 — MSI chip data (S5, 2026-11-17)
- **'151 8:1 MUX strobe — `settled` (primary):** a high level at the strobe G forces Y low and W high;
  G low enables, Y = D(CBA), W = Y'. — TI SN54ALS151/SN74ALS151/SN74AS151 datasheet, description +
  function table (ti.com/lit/gpn/SN74ALS151), read 2026-11-17. The LS part's own sheet was not readable
  (no text layer); same '151 function. Used in 05 step 9.

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

## Leads only (S0b, 2026-11-17 — web search summaries; not tier-1 until read in S8)
- ST CMOS 4000B series data (mikrocontroller.net/attachment/633885/ST-4000.pdf): "45 % V_DD typical" noise immunity → KB05 Open block.
- TI CD4002B product page (ti.com/product/cd4002b): noise margin 1 V @ 5 V, 2 V @ 10 V, 2.5 V @ 15 V → KB05 Open block.
- ROHM logic FAQ (rohm.com faq node 1137/1138): V_IL < 0.3 V_DD, V_IH > 0.7 V_DD → KB05 Open block.
- Cornell PHYS3360 logic-families lecture and notes (classe.cornell.edu/~ib38/...): ECL V_EE = −5.2 V, levels ≈ −0.9/−1.7 V → KB05 Open block (PDF did not text-extract).

## S7 (2026-11-18) — registers and timing analysis
- **Nexperia 74HC194 data sheet**, Rev. 4, 16 Mar 2021 (docs.ampnuts.ru mirror of nexperia.com), Table 3
  function table + pin table: 74194 mode codes (00 hold, 01 shift right via DSR, 10 shift left via DSL,
  11 parallel load), rising edge, asynchronous active-low MR. Primary (manufacturer) source. KB 03 §5.
- **UCSD CSE140 (sp19) lecture 10 "timing"** slides (cseweb.ucsd.edu/classes/sp19/cse140-a/slides/lec10timing.pdf):
  setup T_c ≥ t_pcq + t_pd + t_setup, hold t_ccq + t_cd > t_hold; with skew + t_skew on both (worst case);
  hold fix by adding delay. KB 03 §6.
- **Cornell ECE4740 lecture 17 "sequential circuits"** (ocw.ece.cornell.edu, 2018): signed skew (capture
  clock delayed by a buffer): T_min = t_pd,ff + t_pd,A + t_su − t_buf ("useful skew"), hold
  t_cd,ff + t_cd,A ≥ t_h + t_buf; hold violations not fixable by clock frequency. KB 03 §6.
- **TI SN7400 data sheet** (SDLS025D, ti.com): standard-TTL V_OH/V_OL/V_IH/V_IL, I_OH/I_OL/I_IH/I_IL,
  I_CCH/I_CCL, t_PLH 11/22 ns, t_PHL 7/15 ns (400 Ω, 15 pF), 1.5 V timing reference. KB 05 S8 block.
- **TI SN74HC00 data sheet** (SCLS181H, 2021): V_CC 2–6 V; 4.5 V levels 3.15/1.35/4.4/3.98/0.1/0.26 V;
  I_CC 2 µA; C_i 3/10 pF; C_pd 20 pF; t_pd 9/18 ns; Fig. 7-2 (50 % points, t_pd = greater of t_PLH,
  t_PHL), Fig. 7-3 (10–90 %); unused inputs terminated. KB 05 S8 block.
- **UMBC CMPE 640 lecture "Quality metrics of a digital design"** (courses.cs.umbc.edu): PDP = energy
  per switching event, constant for a given technology. KB 05 S8 block.
- **DJ Greaves, University of Cambridge Computer Laboratory, ACS P35 notes** ("speed-power product"
  table, cl.cam.ac.uk): 1985 74HC00 7 ns 1 mW 7 pJ, 74F00 3.4 ns 5 mW 17 pJ, ECL SP92701 0.8 ns 200 mW
  160 pJ. KB 05 S8 block.
- **TI NA555/NE555/SA555/SE555 data sheet, SLFS022K (rev. March 2026)** (ti.com, read as text S9
  2026-11-19): astable eq. (1)–(6), monostable t_w = 1.1 R_A C, ⅓/⅔ V_CC thresholds. KB 04 §5.
- **University of Utah CS 5780 lecture 11 slides** (my.eng.utah.edu/~cs5780) and **UNC Charlotte ECGR 2156
  experiment 2 "switch debouncing"** (ece.charlotte.edu): SPDT switch + SR latch debouncer, bounce on one
  contact leaves the latch holding. KB 04 §3. Utah read as text + slide 9 image (SPDT, common grounded,
  two pull-ups, cross-coupled NAND; slide 10 "one will bounce the other won't"; bounce "typical a few ms
  but can be as bad as 100's of ms"). Charlotte: search-result summary only (the PDF now redirects).
