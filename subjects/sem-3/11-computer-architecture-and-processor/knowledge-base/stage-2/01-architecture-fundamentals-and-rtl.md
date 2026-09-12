# U1 — Architecture Fundamentals & RTL — STAGE 2 (deep structure)

> Extends `../01-architecture-fundamentals-and-rtl.md`. **Stage 1 is the exam set; this is the
> generative structure underneath it.** Nothing here replaces a Stage-1 claim.

---

## §A. First-principles: why a stored-program machine is *the* design

Stage 1 says "instructions and data share one memory." The deeper claim: **that choice is what makes
a computer universal rather than a calculator.**

**The argument.** A machine whose program is fixed in wiring computes exactly one function. To compute
a different one you must rewire it — the program is *part of the hardware*. Put the program in
**readable, writable memory** and the machine's behaviour becomes **data it manipulates**. This is the
hardware realization of the **universal Turing machine**: one fixed machine that, given a description
of any machine as input, behaves like it. Every modern convenience follows from that single move:

| Consequence | Why it follows from stored-program |
|---|---|
| **Compilers** | a program can *write* another program — it is just data |
| **Operating systems** | one program can load, relocate and schedule others |
| **Bootstrapping** | a small ROM program can fetch a bigger one |
| **Self-modifying code / JIT** | code is writable, so it can be generated at run time |
| **Buffer-overflow attacks** | the same property, unguarded: data can become code |

**The security cost is not incidental.** The reason a stack-smashing attack works at all is precisely
the von Neumann property — injected *data* is executed as *instructions*. Modern mitigations (the NX
bit, W^X, Harvard-style split caches with no execute path from the data cache) are all attempts to
**re-introduce a Harvard separation** for safety while keeping von Neumann flexibility. When a learner
asks "why is Harvard not just better?", this is the honest answer: **it is better for safety and
bandwidth, worse for flexibility, and modern machines cheat by being both.**

## §B. Where the undergraduate treatment simplifies (the "white lies")

| Stage-1 statement | What's actually true |
|---|---|
| "Architecture is what; organization is how" | The line is **negotiated, not natural**. Cache size is "organization" — yet it is architecturally visible via timing side channels (Spectre). Pipeline depth is "organization" — yet the MIPS delay slot made it **architectural**. **Anything a program can observe has leaked into the architecture**, whether the designers intended it or not |
| "The adder adds in one microoperation" | A ripple-carry adder's delay is **O(n)** — the carry must propagate through all n full adders. §C |
| "Bus = one shared path" | Real systems use **split-transaction**, pipelined and packet-switched interconnects; a single arbitrated bus stopped scaling past a few masters |
| "RISC vs CISC is a clean dichotomy" | It is a **spectrum**, and the endpoints converged: ARM added complex instructions, x86 decodes to micro-ops. The useful modern question is not "RISC or CISC?" but **"fixed-length and load-store, or not?"** |
| "The ALSU computes in one clock" | Its delay sets a **lower bound on the clock period** for any single-cycle design — §C |

## §C. Derivation: why ripple-carry bounds the clock, and what replaces it

**The mechanism Stage 1 leaves implicit.** In an n-bit ripple-carry adder, each full adder's carry-out
feeds the next stage's carry-in. Stage i cannot produce a correct sum until stage i−1's carry is
valid. So:

> **t_add ≈ n · t_carry**

For the 8086's 16-bit ALU, that is 16 carry delays in series — and the **ALU sits in the critical path
of every arithmetic instruction**. Since the clock period must exceed the longest combinational path,
**the adder's width directly limits the clock frequency.** This is why "make the machine 64-bit" is
not free.

**The fix (from `../../04-digital-electronics` stage-2 §A):** **carry-lookahead**. Define for each bit
the *generate* and *propagate* terms

> **gᵢ = Aᵢ · Bᵢ**  (this bit generates a carry regardless of carry-in)
> **pᵢ = Aᵢ ⊕ Bᵢ**  (this bit propagates an incoming carry)

then

> **C_{i+1} = gᵢ + pᵢ·Cᵢ**

Expanding the recurrence eliminates the serial dependence:

> C₁ = g₀ + p₀C₀
> C₂ = g₁ + p₁g₀ + p₁p₀C₀
> C₃ = g₂ + p₂g₁ + p₂p₁g₀ + p₂p₁p₀C₀

Every carry is now a **two-level** function of the inputs — **O(log n)** with tree-structured
(parallel-prefix) lookahead, at the cost of O(n log n) gates. **This is the single most important
speed/area trade in the whole datapath**, and it is why the Stage-1 claim "one microoperation" hides
real engineering.

**Cross-link:** the parallel-prefix structures (Kogge-Stone O(log₂ n) depth, Brent-Kung 2log₂ n − 2)
are already derived in `../../04-digital-electronics/knowledge-base/stage-2/01-…`. **Reuse that
derivation; do not repeat it.**

## §D. The bus, properly: arbitration, and why it stopped scaling

Stage 1 gives the O(n²) → O(n) argument. What it omits:

**(a) Only one master may drive at a time — so who decides?** With several potential masters (CPU,
DMA controller, IOP), you need **arbitration**:

| Scheme | Mechanism | Cost |
|---|---|---|
| **Daisy chain** | grant ripples along a serial chain; position = priority | few wires; **fixed** priority; latency grows with chain length |
| **Centralized parallel** | each master has its own request/grant pair into an arbiter | fast, programmable priority; **O(n) wires into one arbiter** |
| **Distributed / self-selection** | masters compare priority codes on a shared wired-OR bus | no central arbiter; more logic per master |

Note this is **the same structure as the priority-interrupt problem** in U5 — daisy chain vs parallel
priority. **One mechanism, two applications.** Teaching them as one idea halves the load.

**(b) The bus is a *shared, blocking* resource.** While a slow device holds the bus, everything else
waits. Hence **split-transaction** buses (release the bus between request and reply) and eventually
**point-to-point packet links** (PCIe, HyperTransport, QPI) — at which point "bus" is a legacy word
for a network. **The O(n²) problem came back, and the modern answer is a switched network, not a
shared wire.**

## §E. Cross-topic unification

- **The ALSU (U1) *is* the AC's adder-and-logic circuit (U2 §11) *is* the F1/F2/F3 microoperation set
  (U3 §4) *is* the 8086's EU ALU (U7 §2).** One block, four vocabularies. Whenever a unit introduces
  "an ALU", ask the learner which earlier one it is.
- **Time-multiplexing appears four times:** the common bus (U1/U2), the von Neumann bottleneck (U1),
  the structural hazard (U4), and AD₁₅–AD₀ address/data multiplexing in the 8086 (U7 §10). **All four
  are "share one resource in time to save wires, and pay in contention."**
- **Selection, not decision.** The ALSU computes everything and selects (§Stage-1 §10); the control
  unit selects which control lines are asserted; the MUX selects a bus source. **Hardware does not
  branch — it computes all paths and discards.** This is why a conditional in hardware costs the *max*
  of both arms, not the average, and it is the seed of why branch prediction (U4) is necessary.
- **Shift = multiply/divide by 2** connects U1 §9 to the 8086's `SHL`/`SAR` (U7 §8) and to RISC-V's
  lack of a dedicated multiply in the base ISA (U8 §2) — shifts are free, multipliers are not.

## §F. Frontier (`evolving` — recheck on re-entry)

- **The architecture/organization line is eroding.** Speculative-execution side channels (Spectre,
  Meltdown, 2018) proved that *microarchitectural* state is **architecturally observable**. Security
  researchers now treat timing as part of the ISA contract — a genuine revision to the definition
  Stage 1 teaches as clean.
- **Domain-specific architectures.** With Dennard scaling ended and Moore's law slowing, the growth
  area is specialization: TPUs, NPUs, DSP blocks. Hennessy & Patterson's Turing lecture calls this "a
  new golden age for computer architecture" — the general-purpose CPU is no longer the only answer.
- **Open hardware.** RISC-V (U8) is the ISA-level instance of the same trend.

## §G. Harder problems (the §0 surplus test for this unit)

1. Prove that {NAND} is functionally complete and explain why that makes a single-cell-type ALU
   fabricable. Then explain why real ALUs are *not* built from NAND alone.
2. An n-bit ripple-carry adder has carry delay t_c per stage and the register setup time is t_s.
   Derive the maximum clock frequency of a single-cycle datapath using it. Now redo it for
   carry-lookahead with O(log n) depth. At what n does the difference exceed 2×?
3. The BC's bus uses 3 select lines for 7 sources. Show that an n-source bus needs ⌈log₂(n+1)⌉ select
   lines if "no source" must be encodable, and explain what breaks if two sources are enabled at once
   (answer: bus contention — a low-impedance path from Vdd to ground through two drivers).
4. Give a sequence of logic microoperations that swaps the two nibbles of an 8-bit register **using
   only AND, OR and shifts** (no XCHG, no rotate). Then do it with **three XORs and no temporary**
   and explain why the XOR-swap works algebraically.
5. `ashl` overflows when Rₙ₋₁ ⊕ Rₙ₋₂ = 1 *before* the shift. Prove this is exactly the condition for
   the true product 2x to be unrepresentable in n-bit two's complement.
6. Argue both sides: "cache size is organization, not architecture." Give a concrete program whose
   *correctness* (not just speed) depends on cache behaviour. (Hint: a side-channel attack, or a
   device driver relying on write ordering.)
7. Why does the 8086 multiplex address and data on the same pins, when the BC's bus does not need to?
   (Answer: a 40-pin DIP cannot carry 20 address + 16 data + control lines separately — packaging
   economics as an architectural driver.)

## Confidence

`settled`: the universality argument · carry-lookahead generate/propagate derivation · bus arbitration
schemes · the stored-program/security connection.
`likely`: the claim that carry-lookahead is *the* dominant limit in a specific modern design — depends
entirely on the microarchitecture.
`evolving`: the architecture/organization erosion and domain-specific-architecture claims — dated
2026, recheck on re-entry.
