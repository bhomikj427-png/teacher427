# U8 — RISC-V (Stage 1)

**Lectures L35–L36 · CO5 · ETE only · ⚠ NO DECK · L36 is `*` practitioner-delivered**

Scope (hand-out): L35 RISC-V: Introduction to the Reduced Instruction Set Computer · L36 RISC-V
architecture and features.

Truth authority: **Patterson & Hennessy, *Computer Organization and Design — RISC-V Edition*** (the
hand-out's named reference) **+ the official ratified RISC-V Instruction Set Manual, Volume I:
Unprivileged ISA** (docs.riscv.org). **This is the one unit in the course with a genuine Tier-1
primary source** — RISC-V is an open standard, so the specification itself is freely readable and was
read directly this session.

> **Two lectures, "Quiz, ETE" only, practitioner-delivered — this is the lowest-yield unit for marks**
> (`exam-map.md`). Expect descriptive questions: *why* an open ISA, *what* the features are. But it is
> also the unit that retroactively explains units 1, 3, 4 and 7 — teach it as the closing argument,
> not as a list.

---

## 1. Why RISC-V exists — `settled` (quoted from the ratified spec)

The specification states its own goals. The two that matter for L35:

> "**A completely open ISA that is freely available to academia and industry.**"
> "**A real ISA suitable for direct native hardware implementation, not just simulation or binary
> translation.**"

**What "open" means here, precisely:** the *instruction set architecture* is freely usable without a
licence fee or royalty. It does **not** mean chips are free or that implementations must be
open-source — a company may build and sell a proprietary RISC-V core. **The contract is open; the
implementation need not be.** That distinction is exactly big idea 1 (architecture vs organization)
and is the most likely thing to be got wrong in a quiz. (`misconceptions.md` M20.)

**Why this was worth doing (the historical argument for L35's "need & USP"):** every other major ISA
is owned — x86 by Intel/AMD, ARM licensed per-core by Arm Ltd. A university could not build and ship a
chip without negotiating rights, and a researcher could not modify the ISA to try an idea. An open ISA
removes that gate. RISC-V originated at **UC Berkeley** as a teaching and research ISA and became an
industry standard, now stewarded by **RISC-V International**.

**The modular design — the real architectural idea:**

> "An ISA separated into a **small base integer ISA**, usable by itself as a base for customized
> accelerators or for educational purposes, and **optional standard extensions**, to support
> general-purpose software development."

**Mechanism / why modularity is the USP.** A conventional ISA is one monolithic set that every
implementation must support, so a small embedded core pays (in area and power) for instructions it
will never run. RISC-V splits the ISA into a **minimal mandatory base** plus **opt-in extensions**, so
an implementer takes only what the application needs. Same ISA family, from a sensor microcontroller to
a server.

**Stability guarantee** — worth quoting, because it answers "is it safe to build on a standard that is
still evolving?":

> "RISC-V will endeavor to keep the base and each standard extension constant over time, and instead
> **layer new instructions as further optional extensions.**"

So the base is frozen; growth happens by addition, never by change. **This is why the base can be
taught as settled while the extension ecosystem is `evolving`.**

## 2. Naming convention — `settled`

**`RV` + register width + extension letters.**

| Name | Meaning |
|---|---|
| **RV32I** | 32-bit registers (**XLEN = 32**), base **I**nteger instruction set |
| **RV64I** | 64-bit registers (XLEN = 64), base integer |
| **RV32E** | a reduced base with only 16 registers, for deeply embedded use |

**Standard extensions** (each a letter):

| Letter | Adds |
|---|---|
| **M** | integer **m**ultiply and divide |
| **A** | **a**tomic memory operations |
| **F** | single-precision **f**loating point |
| **D** | **d**ouble-precision floating point |
| **C** | **c**ompressed (16-bit) instruction encodings |
| **G** | shorthand for **IMAFD** — the "general-purpose" combination |

So **RV32IMC** = 32-bit base + multiply/divide + compressed; **RV64G** = 64-bit general-purpose.
**Note that even integer multiply is an extension** — the base really is minimal. That is the single
most surprising fact here and makes the modularity concrete.

## 3. Register state — `settled` (quoted from the spec)

> "For RV32I, the **32 `x` registers** are each 32 bits wide, i.e. **XLEN = 32**. Register **`x0` is
> hardwired with all bits equal to 0**… There is one additional unprivileged register: the **program
> counter `pc`** holds the address of the current instruction."

| Item | Value |
|---|---|
| General registers | **32** — `x0` … `x31` |
| Width | XLEN = 32 bits (RV32I) |
| **`x0`** | **hardwired to zero** — writes are discarded, reads give 0 |
| `x1`–`x31` | general purpose, fully interchangeable |
| `pc` | holds the address of the **current** instruction |

**★ Why `x0` being hardwired zero is a design masterstroke — this is the exam-worthy insight.** It
removes the need for several separate instructions, because they become special cases of existing
ones:

| Desired operation | Written as | Mechanism |
|---|---|---|
| move `x5` into `x6` | `ADD x6, x5, x0` | add zero |
| load a constant | `ADDI x5, x0, 42` | add immediate to zero |
| negate | `SUB x6, x0, x5` | subtract from zero |
| no-operation | `ADDI x0, x0, 0` | writes to `x0` are discarded |
| discard a result | any instruction with `rd = x0` | |
| branch if `x5` ≠ 0 | `BNE x5, x0, label` | compare against zero for free |

**One hardwired register eliminates a handful of opcodes.** That is the RISC philosophy in a single
design decision: don't add an instruction if a general mechanism already covers the case.

**ABI register names** (`likely` — a convention layered on the ISA, not part of it): `x0` = `zero`,
`x1` = `ra` (return address), `x2` = `sp` (stack pointer), `x5`–`x7` and `x28`–`x31` = `t0`–`t6`
(temporaries), `x8`–`x9` and `x18`–`x27` = `s0`–`s11` (saved), `x10`–`x17` = `a0`–`a7` (arguments /
return values). **The hardware does not care** — the calling convention does. Distinguish the two.

## 4. Instruction formats — `settled` (and a precision point)

> "In the base RV32I ISA, there are **four core instruction formats (R/I/S/U)**… All are a fixed
> **32 bits** in length. The base ISA has **IALIGN = 32**, meaning that instructions must be aligned
> on a four-byte boundary in memory."
> "There are a further **two variants of the instruction formats (B/J)** based on the handling of
> immediates."

**★ Precision matters here.** Most teaching material says "RISC-V has six instruction formats". The
**ratified specification says four core formats (R, I, S, U) plus two variants (B, J)** that differ
only in how the immediate is encoded. Both statements describe the same six layouts — but if an
examiner asks "how many *core* formats?", the specification's answer is **four**. **Say "four core
formats plus two immediate variants, six in total"** and you are correct under either phrasing.
(`misconceptions.md` M21.)

| Format | Used for | Fields |
|---|---|---|
| **R** | register–register arithmetic (`ADD`, `SUB`, `AND`) | funct7 · rs2 · rs1 · funct3 · rd · opcode |
| **I** | immediate arithmetic, **loads**, `JALR` | imm[11:0] · rs1 · funct3 · rd · opcode |
| **S** | **stores** | imm[11:5] · rs2 · rs1 · funct3 · imm[4:0] · opcode |
| **B** | conditional **branches** (S-variant) | branch offset, in multiples of 2 |
| **U** | **upper immediate** (`LUI`, `AUIPC`) | imm[31:12] · rd · opcode |
| **J** | **jumps** (`JAL`) (U-variant) | jump offset, in multiples of 2 |

**Two design decisions the spec explains, and both are excellent exam answers:**

**(a) Register fields sit in fixed positions.**
> "The RISC-V ISA keeps the source (*rs1* and *rs2*) and destination (*rd*) registers **at the same
> position in all formats to simplify decoding**."

*Mechanism:* the decoder can begin reading the register file **before** it has finished determining
which instruction this is, because it always knows *where* the register numbers are. Register read
and instruction decode happen **in parallel** rather than in sequence. **Contrast the 8086**, where
the operand's very existence and location depend on decoding the opcode and then the ModR/M byte
(U7 §6) — decoding is strictly serial there. **This is the concrete reason RISC pipelines more
easily than CISC** and it ties U8 back to U4.

**(b) Why S and B differ — the immediate is scrambled on purpose.**
> "The only difference between the S and B formats is that the 12-bit immediate field is used to
> encode branch offsets in multiples of 2 in the B format. Instead of **shifting all bits in the
> instruction-encoded immediate left by one in hardware as is conventionally done**, the middle bits
> (imm[10:1]) and sign bit **stay in fixed positions**."

*Mechanism:* the immediate's bits look jumbled in the encoding, and that is deliberate. Keeping the
**sign bit** and the middle bits in fixed positions across formats means the sign-extension hardware
and most of the immediate-routing multiplexers are **shared** between formats — the hardware is
smaller, at the cost of an encoding that is ugly to read on paper. **The ISA is optimized for the
decoder, not for the human.** Students who see the scrambled immediate as arbitrary have missed the
entire point.

## 5. Architectural features — `settled` (the L36 answer)

| Feature | Statement | Why it matters |
|---|---|---|
| **Fixed 32-bit instruction length** | every base instruction is exactly 4 bytes, aligned (IALIGN = 32) | the next instruction's address is always PC + 4 — **fetch needs no decoding**, so fetch and decode pipeline cleanly |
| **Load/store architecture** | **only** load and store instructions access memory; all arithmetic is register-to-register | memory access happens in **one** pipeline stage at a **predictable** point |
| **32 general-purpose registers, all equivalent** | no dedicated accumulator or count register | the compiler allocates freely; no false dependencies from forced register use |
| **`x0` hardwired to zero** | §3 | eliminates whole classes of instruction |
| **No condition-code register** | branches **compare two registers directly** (`BEQ rs1, rs2, label`) | no hidden serializing dependency through a flags register — a major pipelining win |
| **Few, simple addressing modes** | essentially **base + 12-bit signed displacement** | address computation is one add; no multi-term EA as in the 8086 |
| **Modular base + extensions** | §1 | one ISA family scales from microcontroller to server |
| **Open and royalty-free** | §1 | anyone may implement it |
| **Designed for a pipeline** | the consequence of all the above | |

**★ On the absence of condition codes** — the most under-appreciated item, and the sharpest contrast
with U7. In the 8086, `CMP` sets flags and a later `Jcc` reads them: an invisible dependency through a
single shared resource that every arithmetic instruction writes. In RISC-V the comparison is **part of
the branch instruction**, so there is no shared flag register to serialize on and nothing to rename in
an out-of-order implementation. **Removing a feature made the machine faster.** That sentence is the
thesis of the whole unit.

## 6. RISC-V vs the 8086 — the course's closing comparison — `settled`

This table is the natural ETE question and the reason the hand-out puts these two units side by side.

| | **8086 (CISC)** | **RISC-V (RISC)** |
|---|---|---|
| Instruction length | **variable, 1–6 bytes** | **fixed 32 bits** |
| Instruction alignment | any byte | **4-byte aligned** |
| Memory operands | most instructions may address memory | **load/store only** |
| Registers | **14**, heavily special-purpose | **32**, all general |
| A zero register | no | **yes (`x0`)** |
| Condition codes | **yes** — a 9-flag register | **no** — compare-and-branch |
| Addressing modes | **~12** (base + index + displacement combinations) | essentially **1** (base + displacement) |
| Address space | **segmented** (seg × 16 + offset) | **flat** |
| Control unit | **microprogrammed** | **hardwired** |
| Instruction decode | **serial** (opcode → ModR/M → length) | **parallel** (fields at fixed positions) |
| Complexity lives in | the **hardware** | the **compiler** |
| ISA ownership | proprietary (Intel) | **open, royalty-free** |
| Extensibility | new instructions bolted on, compatibility forever | **modular opt-in extensions** |

**The historical point to close on, stated honestly:** RISC did **not** simply win. x86 still dominates
desktops and servers because **binary compatibility is an economic moat**, and modern x86 chips get
RISC-like performance by **decoding CISC instructions into RISC-like micro-operations internally** —
architecture CISC, organization RISC (big idea 1, one last time). What RISC won is the *design
argument*: every new ISA since — ARM, RISC-V — is a load-store register machine with fixed-length
instructions. **Don't teach "RISC beat CISC"; teach "the RISC argument became the default, and CISC
survived by adopting it underneath."** (`misconceptions.md` M22.)

---

## Worked-problem patterns for this unit

1. **Why an open ISA?** State the spec's goals; explain what "open" does and does not mean.
2. Explain the **base + extensions** model; decode a name like `RV32IMC` or `RV64G`.
3. Describe the RV32I register state; **explain the significance of `x0`** with examples.
4. **How many instruction formats?** — four core (R/I/S/U) + two variants (B/J); name each one's use.
5. Explain **why register fields are at fixed positions** and what it buys.
6. Explain why S and B differ in immediate encoding.
7. **List and explain RISC-V's architectural features** (the §5 table).
8. **Compare RISC-V with the 8086** (the §6 table) — the most likely ETE question here.
9. Explain why the absence of condition codes helps pipelining.

## Confidence summary

`settled` (**read directly from the ratified specification this session** — the strongest sourcing in
this knowledge base): the stated design goals and the "real ISA, not simulation-only" claim · the
base-plus-extensions model and the stability commitment · **32 x-registers, XLEN = 32, `x0` hardwired
to zero, `pc` as an additional register** · **four core formats (R/I/S/U) plus two variants (B/J), all
fixed 32 bits, IALIGN = 32** · the fixed-position rs1/rs2/rd rationale ("to simplify decoding") · the
S-vs-B immediate rationale, quoted · the naming convention and extension letters.
`likely`: the **ABI register names** (`ra`, `sp`, `t0`…) — a calling convention layered above the ISA,
stable in practice but not part of the base spec · UC Berkeley origin and RISC-V International
stewardship (widely documented, not verified against a primary record this session).
`evolving`: the **extension ecosystem** — which extensions exist and which are ratified changes over
time. Verified against the ratified unprivileged ISA (v20240411 / v20260120 reference library);
**recheck on subject re-entry** (protocol §10 staleness trigger). The **base is stable by the spec's
own commitment**, so RV32I may be taught as settled.
Not claimed: privileged architecture (machine/supervisor modes, CSRs), vector extension detail,
specific commercial core performance, or market-share figures — out of scope per `00-map.md`.

> **Stage 2 for this unit:** `stage-2/08-risc-v.md` — the full RV32I instruction listing and encoding
> arithmetic, why `AUIPC` exists and how 32-bit constants are built from two instructions, the
> compressed (C) extension's 16-bit encoding and why code density mattered again, what the classic
> five-stage RISC pipeline looks like on RV32I, and an honest account of where the RISC argument's
> claims have and haven't held up.
