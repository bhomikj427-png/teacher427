# U8 — RISC-V — STAGE 2 (deep structure)

> Extends `../08-risc-v.md`. **Stage 1 for this unit is already quoted from the ratified standard**, so
> Stage 2 goes to encoding arithmetic, the pipeline realization, and an honest audit of the RISC claims.

---

## §A. RV32I: the actual instruction set, and why it is this small

The base integer ISA is deliberately minimal. Grouped by function (RV32I, ~40 instructions):

| Group | Instructions | Note |
|---|---|---|
| **Arithmetic (R)** | `ADD` `SUB` `SLT` `SLTU` `AND` `OR` `XOR` `SLL` `SRL` `SRA` | register–register only |
| **Arithmetic (I)** | `ADDI` `SLTI` `SLTIU` `ANDI` `ORI` `XORI` `SLLI` `SRLI` `SRAI` | 12-bit immediate |
| **Loads** | `LB` `LH` `LW` `LBU` `LHU` | sign- or zero-extended |
| **Stores** | `SB` `SH` `SW` | |
| **Branches (B)** | `BEQ` `BNE` `BLT` `BGE` `BLTU` `BGEU` | **compare two registers directly** |
| **Jumps** | `JAL` (J) `JALR` (I) | link register written to `rd` |
| **Upper immediate (U)** | `LUI` `AUIPC` | §B |
| **System** | `ECALL` `EBREAK` `FENCE` | |

**★ Note what is absent, and that the absences are the design:**

| Missing | Why, and what replaces it |
|---|---|
| **`MOV`** | `ADDI rd, rs, 0` — or `ADD rd, rs, x0` |
| **`NOP`** | `ADDI x0, x0, 0` — writes to `x0` are discarded |
| **`NEG`** | `SUB rd, x0, rs` |
| **`NOT`** | `XORI rd, rs, -1` |
| **multiply / divide** | the **M extension** — not in the base at all |
| **condition-code register** | branches compare registers; there is no flags register to rename or serialize on |
| **`BGT`, `BLE`** | **swap the operands** of `BLT`/`BGE` — the assembler provides them as pseudo-instructions |
| **increment/decrement** | `ADDI rd, rd, 1` |

**The principle:** *don't add an instruction if a general mechanism already covers the case.* A learner
who can derive the missing ones from `x0` and operand swapping has understood RISC-V better than one who
memorizes a table. The **pseudo-instruction** layer (assembler conveniences that expand to base
instructions) is where the human-friendly names live — **and it is the cleanest example of "complexity
moves to the software" in the whole course.**

## §B. Building a 32-bit constant from 32-bit instructions — the encoding paradox

**The problem.** An instruction is 32 bits. An immediate cannot be 32 bits, because the opcode and
register fields need room — the I-format immediate is **12 bits**. So how do you load a 32-bit constant?

**The answer: two instructions, and `LUI` + `ADDI`.**

```
    LUI  rd, imm[31:12]      ; rd ← imm[31:12] << 12      (upper 20 bits, lower 12 zeroed)
    ADDI rd, rd, imm[11:0]   ; rd ← rd + sign-extended imm[11:0]
```

**★ The subtlety that makes this a real derivation, not a recipe.** `ADDI` **sign-extends** its 12-bit
immediate. So if bit 11 of the target constant is 1, `ADDI` adds a **negative** number, and the upper
part comes out **1 too small**. The assembler must therefore **pre-compensate**:

> if imm[11] = 1, use **(imm[31:12] + 1)** in the `LUI`.

*Worked.* Load 0xDEADBEEF.
- imm[11:0] = 0xEEF; bit 11 = 1, so this sign-extends to **−0x111** (0xFFFFFEEF).
- Naive `LUI 0xDEADB` then `ADDI −0x111` gives 0xDEADB000 − 0x111 = 0xDEADAEEF — **wrong by 0x1000.**
- So use **`LUI rd, 0xDEADC`** then `ADDI rd, rd, 0xEEF`: 0xDEADC000 − 0x111 = **0xDEADBEEF** ✓

**Why `AUIPC` exists** (*add upper immediate to PC*): `AUIPC rd, imm` computes **PC + (imm << 12)**.
Paired with `ADDI` or a load, it forms a **PC-relative** address. This is what makes
**position-independent code** possible on RISC-V — the same instruction sequence works wherever the code
is loaded, with no relocation. Together, `LUI`/`AUIPC` give absolute and PC-relative 32-bit address
formation in two instructions each, **without any instruction longer than 32 bits.** That is the
constraint-satisfying design, and it is worth admiring.

**The trade, stated honestly:** RISC-V spends **two instructions and 8 bytes** on something the 8086 does
in one instruction and 3 bytes (`MOV AX, imm16`). **RISC-V has worse code density here and it does not
care**, because fixed-length decoding is worth more than the bytes — which is precisely the choice §D
audits.

## §C. Instruction-field arithmetic: why the immediates look scrambled

Stage 1 quotes the spec's rationale. Here is the arithmetic that makes it concrete.

Across formats, the immediate's bits are placed so that **the same instruction bit drives the same
immediate bit wherever possible**:

| Format | Immediate bits, and where they sit |
|---|---|
| **I** | imm[11:0] ← inst[31:20] |
| **S** | imm[11:5] ← inst[31:25], imm[4:0] ← inst[11:7] |
| **B** | imm[12] ← inst[31], imm[10:5] ← inst[30:25], imm[4:1] ← inst[11:8], imm[11] ← inst[7] |
| **U** | imm[31:12] ← inst[31:12] |
| **J** | imm[20] ← inst[31], imm[10:1] ← inst[30:21], imm[11] ← inst[20], imm[19:12] ← inst[19:12] |

**Three invariants make the hardware cheap:**

1. **inst[31] is always the immediate's sign bit**, in every format. So the sign-extension logic is a
   single fan-out of one wire — no format-dependent multiplexing at all.
2. **imm[10:1] always comes from inst[30:21]** in B and J, and imm[10:5] from inst[30:25] in S and B. The
   middle bits barely move, so the same wires serve multiple formats.
3. **B and J encode offsets in multiples of 2**, so imm[0] is always 0 and is **not stored** — buying one
   extra bit of range for free (a ±4 KiB branch range from 12 stored bits, ±1 MiB jump range from 20).

**★ The cost is paid by the human, and only once.** The encoding is ugly to read and trivial to
implement: the immediate-generation unit is a handful of wires and one sign-extension, rather than a
per-format shifter. **Stage 1's "optimized for the decoder, not the reader" is quantified here.** The
number of multiplexers saved is the whole justification, and a learner who sees invariant 1 will never
call the encoding arbitrary again.

## §D. The classic five-stage pipeline on RV32I — where U4 lands

RV32I was designed so that the textbook pipeline works with almost no special cases:

| Stage | Work |
|---|---|
| **IF** | fetch instruction at PC; PC ← PC + 4 |
| **ID** | decode; **read rs1 and rs2** (fields at fixed positions — no decoding needed first); sign-extend immediate |
| **EX** | ALU operation, or address calculation, or branch comparison |
| **MEM** | data memory access — **only** for loads and stores |
| **WB** | write result to `rd` |

**Why each RISC-V feature earns its place — this table *is* the answer to "why RISC?":**

| Feature | What it buys in the pipeline |
|---|---|
| **fixed 32-bit, aligned** | IF needs **no decoding** to find the next instruction: PC + 4, always |
| **fields at fixed positions** | ID reads the register file **in parallel with** decoding, not after |
| **load/store only** | memory access happens in **exactly one** stage (MEM); no instruction needs two memory accesses, so **no structural hazard on memory** beyond IF/MEM |
| **no condition codes** | branch comparison is **local to EX** — no hidden serial dependence through a shared flags register |
| **3-address register-register** | dependences are **explicit in the instruction fields**, so forwarding logic is straightforward |
| **12-bit immediate, one addressing mode** | address calculation is **one add** — it fits in EX with no extra stage |

**The residual hazards (nothing is free):**

- **Load-use RAW** still costs **one stall cycle** even with full forwarding: the loaded value is only
  available at the *end* of MEM, and a dependent instruction needs it at the *start* of its EX. **No
  forwarding path can send data backwards in time.** This is the one irreducible stall, and it is why
  compilers schedule loads early.
- **Branches** resolve in EX, costing 1–2 cycles of misprediction penalty in the classic design (modern
  implementations predict and resolve earlier).
- **Classic MIPS exposed the branch delay slot architecturally; RISC-V deliberately did not** — the
  designers judged that exposing a pipeline artifact in the ISA was a mistake, because it locks all
  future implementations into one pipeline depth. **That judgement is a direct lesson learned from
  U7 stage-2 §A's A20 story: don't let an implementation detail become a contract.**

## §E. The compressed extension — code density comes back

**The C extension** adds 16-bit encodings for the most common instructions, chosen by frequency analysis:
those using the most-used registers, small immediates, and common patterns (`C.ADDI`, `C.LW`, `C.MV`,
`C.J`). Typical result: **~25–30% reduction in code size** (`likely` — workload-dependent).

**Why this matters philosophically.** Fixed-length encoding was presented in Stage 1 as a RISC virtue. The
C extension **partially retreats** from it: instruction length becomes 2 **or** 4 bytes, and IALIGN drops
to 16. **Why retreat?** Because code size affects the **instruction cache hit rate** (U6) and embedded
ROM cost, and both turned out to matter more than the purity of fixed length.

**But note how the retreat is engineered to stay cheap:** the length is determined by the **low 2 bits of
the first halfword** alone. So boundaries are still found by inspecting **2 bits**, not by full decoding —
nothing like the 8086's ModR/M chain (U7 stage-2 §B). **RISC-V recovered most of CISC's density while
keeping O(1) length determination.** That is the honest synthesis: the two philosophies converged, and
the convergence point is closer to RISC.

ARM did the same thing earlier with **Thumb** and **Thumb-2** — independent arrival at the same answer,
which is decent evidence it is the right one.

## §F. An honest audit of the RISC claims

Stage 1 presents RISC-V's features approvingly. Protocol §4 requires teaching live debates as debates,
so:

| RISC claim | Verdict in 2026 |
|---|---|
| "Simple instructions, ~1 cycle each" | **Held as a design principle**, but modern high-performance RISC-V cores are deeply out-of-order and superscalar — the *simplicity* is in the ISA, not the implementation. A high-end RISC-V core is not a simple machine |
| "Fixed length is essential" | **Softened** — the C extension exists (§E). The durable claim is **O(1) length determination**, not fixed length |
| "The compiler will handle it" | **Mostly held** — register allocation and scheduling are solved problems. But the delay-slot experiment (MIPS) **failed**, and RISC-V correctly declined to repeat it |
| "More registers is better" | **Held.** 32 architectural registers is now standard. Note x86-64 went from 8 to 16 — moving *toward* RISC |
| "Load/store separation" | **Held universally.** Every ISA designed since 1985 does this |
| "No condition codes" | **Held for new designs**, and vindicated by out-of-order implementation difficulty (flags are a rename bottleneck) |
| "RISC is faster than CISC" | **Not the right question.** Performance is dominated by microarchitecture, process node and memory hierarchy — not by ISA class. The ISA affects *how hard it is* to build a fast implementation, not the ceiling |
| "An open ISA will win on merit" | **Genuinely open.** RISC-V has real adoption (embedded, accelerators, some datacenter) but has not displaced ARM or x86 in their strongholds. **Do not teach an outcome** |

**The defensible summary:** the RISC *design argument* won — every ISA designed after 1985 is a
load-store register machine with uniform-ish encoding and many registers. **But no ISA class wins on
performance**, and CISC survived commercially by adopting RISC organization internally (U7 stage-2 §D).
**What RISC-V adds that is genuinely new is not technical but structural: an ISA nobody owns.**

## §G. Cross-topic unification

- **Every RISC-V feature in §D maps to a hazard in U4.** Fixed length → no IF complexity; load/store →
  no memory structural hazard; no condition codes → no hidden RAW through flags; fixed fields → cheap
  forwarding. **U8 is U4's answer sheet.**
- **`x0` is the ALSU's "transfer" row generalized** — U1's arithmetic circuit had rows producing `D = A`
  by selecting Y = 0. RISC-V makes that a *register* rather than a control encoding, and gets a dozen
  instructions for free.
- **RISC-V's hardwired control is U3's conclusion** ("most RISC machines use hardwired control"), and its
  fixed-length uniform instructions are exactly what makes hardwiring tractable.
- **The C extension is a U6 argument** — code density is an instruction-cache hit-rate argument.
- **`FENCE` exists because of U5's memory-ordering problem** (the `volatile`/barrier issue in U5
  stage-2 §C) — RISC-V makes memory ordering explicit in the ISA rather than implicit.
- **RISC-V's custom-extension space realizes Wilkes' variable instruction set** (U3 stage-2 §A) — 75
  years later, in silicon rather than microcode.

## §H. Harder problems (the §0 surplus test)

1. Write RV32I sequences, using only base instructions, for: `MOV rd, rs`; `NOP`; `NEG rd, rs`;
   `NOT rd, rs`; "branch if rs1 > rs2"; "load the constant 1". Explain which are pseudo-instructions and
   which are genuine.
2. Load **0x12345678** and **0xFFFFF800** into `x5` with `LUI`+`ADDI`. Show the sign-extension
   compensation (or its absence) in each, and state the rule you applied.
3. Prove the `LUI`/`ADDI` compensation rule: if imm[11] = 1, the `LUI` argument must be imm[31:12] + 1.
4. B-format stores 12 immediate bits but reaches ±4 KiB. Account for every factor of 2.
5. Show that inst[31] is the sign bit in **all** of I, S, B, U and J. How many multiplexers does that
   save in the immediate-generation unit versus a naive per-format design?
6. With full forwarding, show that a load-use dependence still needs one stall, and prove no forwarding
   path can remove it. Then show that an ALU-to-ALU dependence needs **none**.
7. RISC-V omits the branch delay slot that MIPS exposed. Argue why that was correct, referring to a
   concrete cost MIPS paid when implementations got deeper.
8. The C extension makes instructions 2 or 4 bytes. Show how the length is determined from 2 bits, and
   compare the decoder cost with the 8086's ModR/M chain (U7 stage-2 §B).
9. RISC-V has **no carry flag**. Write RV32I code to add two 64-bit numbers held in register pairs.
   (Hint: detect carry with `SLTU`.) Then argue whether omitting the carry flag was wise.
10. x86-64 went from 8 to 16 registers; RISC-V has 32. Estimate the encoding cost of 32 vs 16 registers
    in a 32-bit fixed-length instruction with three register fields, and say what had to be given up.

## Confidence

`settled`: the RV32I instruction inventory and the omissions/replacements · `LUI`+`ADDI` constant
formation **including the sign-extension compensation rule** (derivable and verified arithmetically) ·
`AUIPC` for PC-relative addressing · the immediate-field placement invariants and the inst[31]-sign-bit
property · the five-stage mapping and the feature→benefit table · the irreducible load-use stall · that
RISC-V deliberately omits a branch delay slot · that the C extension exists and determines length from
the low bits.
`likely`: the **~25–30% code-size reduction** from the C extension (workload-dependent) · the exact
instruction count of RV32I (~40, depending on whether `FENCE`/`ECALL`/`EBREAK` and `SYSTEM` variants are
counted) · the §F audit verdicts (reasoned judgements, clearly labelled as such, not measurements).
`evolving`: RISC-V's market position and the extension ratification list — **do not teach an outcome**;
recheck on re-entry per protocol §10.
