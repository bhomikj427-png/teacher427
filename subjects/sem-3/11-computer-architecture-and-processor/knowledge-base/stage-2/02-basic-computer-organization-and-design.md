# U2 — Basic Computer Organization & Design — STAGE 2 (deep structure)

> Extends `../02-basic-computer-organization-and-design.md`.

---

## §A. Where Mano's Basic Computer lies

The BC is a **pedagogical fiction**, and naming its fictions is what turns it from a thing to memorize
into a thing to reason from.

| The BC assumes | Reality |
|---|---|
| **Memory responds within one CPU clock** — "memory cycle is assumed to be short enough to complete in a CPU cycle" | Main memory is **50–200× slower** than the core. Every real design needs caches (U6), wait states, or a memory pipeline. **This single assumption is what lets the BC have a 5-step instruction cycle instead of a 50-step one** |
| Every instruction takes a **fixed, short number of T-states** | Real CPI varies enormously; a cache miss can cost hundreds of cycles |
| **One accumulator** suffices | Forces a memory access for nearly every operation — the accumulator becomes the bottleneck. Register files exist to avoid it |
| **No pipelining** — fetch completes before execute begins | Even the 8086 overlaps them (U7 §2) |
| **The bus is never contended** | The bus *is* the structural hazard (U4) |
| **Interrupts are precise and cheap** | Precise interrupts in a pipelined, out-of-order machine are a hard design problem |
| **3-bit opcode is enough** | It yields 8 opcodes, of which one (111) is overloaded to escape into 18 more instructions. A real ISA needs a systematic escape mechanism |

**The last row is the most instructive.** The BC's instruction set is not "25 instructions"; it is
**7 instructions plus an escape hatch**, where opcode 111 plus the I bit redirects the meaning of the
remaining 12 bits. **That is exactly the CISC prefix/escape trick** the 8086 uses (segment override
prefixes, the two-byte opcode escape) and exactly what RISC-V refuses to do (fixed fields, no escape).
Opcode space is a scarce resource, and every ISA's character is visible in how it spends it.

## §B. Derivation: why an accumulator machine has a one-address format

Stage 1 states that AC's singleness "buys the 3-bit opcode". Here is the actual counting argument.

An instruction must name its operands. With a 16-bit word:

| Machine type | Operands named | Bits needed (4096-word memory) | Fits in 16? |
|---|---|---|---|
| **3-address** (`ADD A,B,C`) | 3 memory addresses | 3 × 12 = 36 + opcode | **no** |
| **2-address** (`ADD A,B`) | 2 memory addresses | 2 × 12 = 24 + opcode | **no** |
| **1-address** (`ADD B`, AC implicit) | 1 memory address | 12 + 1 + 3 = **16** | **yes** |
| **0-address** (stack: `ADD`) | none — both operands on the stack | opcode only | yes, but needs a stack |

**The accumulator is not a design preference; it is the only thing that fits.** Given a 16-bit word and
a 12-bit address, exactly one address field is affordable, so one operand must be implicit — and the
implicit one is the accumulator. **Word width, address space and instruction format are three faces of
one constraint.**

This also explains the historical progression: as words widened and memories grew, machines moved to
2-address (8086: `ADD AX, BX` — one operand is both source and destination) and then, once registers
were plentiful and instructions fixed-length at 32 bits, to **3-address register-register** (RISC-V:
`ADD x1, x2, x3` — three 5-bit register fields = 15 bits, easily affordable). **Register-register
addressing is what makes 3-address formats cheap**, because a register name is 5 bits, not 12.

## §C. BSA, reentrancy, and why real machines abandoned it

Stage 1 notes BSA is not reentrant. The mechanism, precisely:

BSA stores the return address **in the callee's first word — a single, fixed location**. So:

```
CALL  SUB      → M[SUB] = return₁ ;  run SUB
  (inside SUB, something calls SUB again)
CALL  SUB      → M[SUB] = return₂ ;  return₁ is GONE
```

The second call **overwrites** the first return address. Therefore BSA forbids:
- **recursion** (a routine calling itself),
- **reentrancy** (a routine interrupted and re-entered — *including by an interrupt handler*),
- **shared library code** in a multiprogrammed system.

**The general principle:** *return addresses must be stored in a structure whose lifetime matches the
call's, and calls nest — so the structure must be a **stack**.* A single word has one lifetime; a stack
has one slot per live call. This is not an optimization, it is a correctness requirement.

**Why it matters here and not only in U3:** the BC's own **interrupt cycle** stores the return address
at **M[0]** — a single fixed word. So **the BC cannot take a second interrupt while servicing the
first**, which is exactly why `RT₂: IEN ← 0` clears the enable. **Mano's design is internally
consistent only because it forbids nesting.** Ask a learner why IEN is cleared and you are asking them
to rediscover this.

## §D. Interrupt latency and precision — the real constraint

Stage 1 gives the recognition condition `T′₀T′₁T′₂(IEN)(FGI+FGO): R ← 1`. Two deeper properties:

**(a) Interrupt latency = worst-case time from request to first instruction of the handler.** It is
bounded below by the **longest instruction**, because the interrupt is only recognized after the
current instruction completes. In the BC that is ISZ (3 execute steps). In a CISC with block-string
instructions (`REP MOVSB` moving 64 KB), a naive design would have unbounded latency — which is why
the 8086 makes `REP` **interruptible between iterations**, restoring CX and SI/DI so it can resume.
**Real-time systems care more about this bound than about throughput.**

**(b) Precise interrupts.** An interrupt is *precise* if, when the handler runs, all instructions
before the faulting one have completed and none after it have started. The BC gets this **free**,
because it executes one instruction at a time. A **pipelined** machine (U4) has 4 instructions in
flight, and an **out-of-order** machine has completed instructions *after* the faulting one —
maintaining the illusion of precision requires a **reorder buffer** that commits results in program
order. **Precise interrupts are the single hardest constraint on aggressive out-of-order design**, and
they exist only because programmers and OS writers demand the BC's simple model.

## §E. The design method, generalized

Stage 1's "scan the RTL and OR the conditions" is a special case of a general synthesis procedure:

> For each state element, the set of RTL statements that write it defines a **multiplexed input**
> (which value) and an **enable equation** (when).

In modern terms that is exactly what an HDL synthesizer does with

```verilog
always @(posedge clk)
  if (ld_ar) AR <= ar_in;
```

where `ld_ar` is the OR of conditions and `ar_in` is the MUX of sources. **The BC design exercise is
hand-synthesis of what a tool now does** — which is why this unit is the natural bridge to
`../../../verilog`. When teaching, say so: the learner is not doing archaeology, they are doing by
hand what they will later write one line for, and understanding *what the tool emits*.

**The dual insight:** the number of terms in LD(X) equals the number of distinct times X is written
across the whole machine description. A register written in many places has a wide OR gate and a wide
input MUX — **so instruction-set complexity shows up directly as control-logic area.** That is the
quantitative version of "CISC control units are big", and it is the bridge to U3's argument for
microprogramming.

## §F. Cross-topic unification

- **The BC's interrupt cycle is BSA in hardware.** Mano says so outright. Once seen, the interrupt
  mechanism needs no separate memorization.
- **The BC's I/O polling loop (U2 §9) is programmed I/O (U5 §4), rung 1 of the autonomy ladder.**
  U5 is a continuation, not a new topic.
- **The BC's flat 4096×16 memory is the model U6 deviates from.** Cache and virtual memory only make
  sense as departures from this.
- **D·T product terms (U2 §6) become microinstruction fields (U3 §4).** Same control signals, two
  encodings: **hardwired = compute the signals; microprogrammed = look them up.**

## §G. Frontier / modern comparison

What a modern datapath keeps from the BC: a PC, an instruction register, a register file, an ALU, and
a control unit that decodes an opcode into control signals. **What it adds:** pipelining, caches,
branch prediction, register renaming, out-of-order issue, speculative execution, SIMD units, multiple
cores. **What it removes:** the single accumulator, the single shared bus, and microcode for simple
instructions.

The BC is roughly a **1960s minicomputer** (PDP-8 class — also a 12-bit-address accumulator machine
with indirect addressing and one accumulator). That is not a coincidence: Mano modelled it on that
generation, which is why it feels coherent rather than arbitrary.

## §H. Harder problems (the §0 surplus test)

1. The BC has 7 MRI opcodes (000–110) and overloads 111. Suppose you wanted an 8th memory-reference
   instruction. Enumerate **every** way to find encoding space, and state each one's cost.
2. Show that BSA + BUN-indirect implements call/return. Now write a BC program in which this
   **demonstrably fails**, and identify the minimum hardware change that fixes it.
3. The interrupt cycle uses TR to hold PC while M[AR] is written. Why can't `M[0] ← PC` be done
   directly in one step? (Trace the bus.) What would it cost to make it one step?
4. Derive LD(PC), INR(PC) and CLR(PC) by scanning the complete computer description. How many product
   terms? Now argue how that count would grow if the BC had 40 instructions instead of 25.
5. Compute the BC's CPI for a program that is 40% ADD (direct), 20% LDA (indirect), 20% BUN, 20% ISZ.
   Then state the assumption about memory that makes your answer wrong on real hardware.
6. The BC recognizes interrupts only outside T₀T₁T₂. Construct the worst-case interrupt latency in
   clock cycles. Which instruction causes it?
7. **Design question:** add a stack pointer and stack-based CALL/RET to the BC. Specify the new
   register, the new instructions, their microoperation sequences, and the changes to the control
   equations. What opcode space did you spend?

## Confidence

`settled`: the operand-counting argument for one-address format · the BSA reentrancy failure and its
connection to IEN ← 0 · precise-interrupt definition and why pipelining threatens it · the
hand-synthesis correspondence to HDL.
`likely`: the PDP-8 lineage claim (widely stated; not verified against a primary record this session).
Not claimed: specific modern reorder-buffer depths or commercial microarchitecture details.
