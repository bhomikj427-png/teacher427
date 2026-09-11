# U8 — Verification & Testbenches (deep notes)

> Deep pass 2026-06-15. How you know the hardware is correct *before* it's built. This is where
> the non-synthesizable part of the language lives and is legitimate.

## A. Why simulation/verification exists
- You cannot "run" hardware to debug it cheaply; a fabrication respin is enormously expensive. The
  **testbench** drives stimulus into the **DUT** (device under test) and checks responses, in
  simulation, before synthesis. `[settled — testbench literature]`
- A testbench is a Verilog **module with no ports**, used **only for simulation** (never
  synthesized) — so it freely uses the non-synthesizable subset (U10). `[settled]`

## B. Testbench mechanics
- **Instantiate the DUT**, generate a **clock** (`always #5 clk = ~clk;`), apply **stimulus** in an
  `initial` block (legitimate here — initial is sim-only), observe outputs. `[settled]`
- **Time control:** `#delay` (sim-only), `@(posedge clk)`, `wait`. `[settled]`
- **System tasks:** `$display` (print now), `$monitor` (print on any change), `$strobe` (print at
  end of time step — **use for nonblocking-assigned values**, Cummings #7), `$finish`, `$dumpvars`
  (waveform/VCD). `[settled — corroborated; Cummings #7]`

## C. From ad-hoc to self-checking
- **Self-checking testbench:** compare DUT output against an **expected value** (a reference model
  or precomputed table) and flag mismatches automatically — scales far better than eyeballing
  waveforms. `[settled]`
- Techniques: directed tests (specific cases), **randomized** stimulus (`$random`) for coverage,
  edge/boundary cases, assertions (full power arrives in SystemVerilog — U12). `[settled]`
- **Waveform viewing** (GTKWave/VCD) for debugging when a check fails. `[settled]`

## D. The verification mindset (professional)
Verification is often the majority of real chip effort; coverage ("did I exercise every case?")
and constrained-random + assertions are the professional toolkit — Verilog covers the basics,
SystemVerilog/UVM the industrial scale (U12). `[settled — corroborated; industry-standard claim]`

## What the engine teaches from this
Introduce once the learner has something worth testing (after U5/U6) so the testbench verifies
*their* design — retrieval-rich because they predict outputs and the self-check confirms/refutes.
Reinforces T1 (testbench `initial`/`#delay` are sim-only, not hardware) and the sim/synth split.

## Confidence / gaps
All `settled`. No open items.
