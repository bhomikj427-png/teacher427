# U2 — Basic Computer Organization and Design (Stage 1)

**Lectures L9–L11 · CO2 · MTE + ETE · deck: `../exam-pack/slides-unit2-…pdf` (48 pp)**

Scope (deck's own contents list): Instruction Codes · Computer Registers · Computer Instructions ·
Timing and Control · Instruction Cycle · Memory-Reference Instructions · Input–Output and Interrupt ·
Complete Computer Description · Design of Basic Computer · Design of Accumulator Logic.

Truth authority: **Mano 3e ch. 5**. Verified against two independent institutional reproductions plus
the professor's deck — all three agree (see `sources.md`).

> **This is the densest unit in the course and the heart of CO2.** Everything in U3 is a
> re-implementation of what is built here. The deck spends 48 pages on it.

---

## 1. Why a toy machine at all — `settled`

A modern processor has many registers, multiple integer and floating-point units, and pipelining.
You cannot learn organization from it. Mano defines the **Basic Computer (BC)** — deliberately
simple, "similar to what real processors were like ~25 years ago" — so that the *entire* machine can
be specified in RTL, and then actually designed, in a few pages. **The BC is a teaching instrument,
not a real chip.** Every claim below is a fact about Mano's definition, so Mano is definitionally the
authority.

## 2. Instruction codes and the stored program — `settled`

- Memory: **4096 words × 16 bits.** 4096 = 2¹² → **12 bits** select a word.
- An instruction has two parts: an **opcode** (what to do) and an **address** (what to do it to).
- 16-bit word − 12 address bits − 1 mode bit = **3 bits of opcode**.

**Instruction format:**

```
 15    14  13  12   11                                  0
┌───┬──────────────┬────────────────────────────────────┐
│ I │    opcode    │              address               │
└───┴──────────────┴────────────────────────────────────┘
  1        3                       12
```

**I = addressing mode bit: I = 0 → direct, I = 1 → indirect.**

**Effective address (EA)** = "the address that can be directly used without modification to access an
operand… or as the target address for a branch."

| Mode | I | Mechanism | EA |
|---|---|---|---|
| **Direct** | 0 | the address field *is* the operand's address | EA = address field |
| **Indirect** | 1 | the address field points to a **word that holds** the address | EA = M[address field] |

*Worked (the deck's own example):* `0 ADD 457` at location 22 → I = 0, so the operand is in 457.
`1 ADD 300` at location 35 → I = 1, so go to 300, find 1350 there, and the operand is in **1350**.

**Mechanism — why indirect exists at all.** 12 bits can only name 4096 locations, and that happens to
be all of memory here — so indirection is not about *reach*. It is about **computed addresses**: the
pointer word can be changed at run time, which is how arrays, pointers and parameter passing become
possible on a machine with one accumulator. Indirection costs an **extra memory access** (T₃).

## 3. Computer registers — `settled`

| Register | Bits | Name | Function |
|---|---|---|---|
| **DR** | 16 | Data Register | holds the memory **operand** |
| **AR** | 12 | Address Register | holds the **address for memory** — always drives the memory's address pins |
| **AC** | 16 | Accumulator | the single general-purpose processor register |
| **IR** | 16 | Instruction Register | holds the instruction being executed |
| **PC** | 12 | Program Counter | holds the address of the **next** instruction |
| **TR** | 16 | Temporary Register | scratch, for intermediate results |
| **INPR** | 8 | Input Register | holds one input character |
| **OUTR** | 8 | Output Register | holds one output character |

Plus the **SC** (4-bit sequence counter) and seven flip-flops: **I, S, E, R, IEN, FGI, FGO**
(E = the carry-out/extended AC bit; S = start-stop; R = interrupt; IEN = interrupt enable; FGI/FGO =
input/output flags).

**Why 12 vs 16 bits:** AR and PC hold **addresses** (12 bits is all an address needs); DR, AC, IR, TR
hold **words** (16). INPR/OUTR are 8 because the BC's I/O model is one character at a time.

**Why only one general register (AC):** it is what makes the BC an *accumulator machine* — every
arithmetic instruction has one implicit operand (AC) and one memory operand, so the instruction needs
only one address field. That is exactly what buys the 3-bit opcode. Register count and instruction
format are not independent choices. (This is the design pressure RISC-V later resolves differently —
U8.)

## 4. Common bus system — `settled`

Nine registers plus memory share **one 16-bit common bus**, selected by **S₂S₁S₀**:

| S₂S₁S₀ | Source on the bus |
|---|---|
| 000 | (nothing) |
| 001 | **AR** |
| 010 | **PC** |
| 011 | **DR** |
| 100 | **AC** |
| 101 | **IR** |
| 110 | **TR** |
| 111 | **Memory** |

Rules that get examined:
- Exactly one source drives the bus at a time; the destination is chosen by whichever register's
  **LD** is asserted (or memory's **write**).
- **AR and PC are 12-bit**, so when they drive the 16-bit bus the **high-order 4 bits are 0s**.
- **OUTR is 8-bit** and takes the **low-order 8 bits** of the bus.
- **Five registers have LD, INR and CLR** (AR, PC, DR, AC, TR); **IR and OUTR have LD only.**
- AC's input does **not** come from the bus directly — it comes from the **adder-and-logic circuit**,
  which takes AC, DR and INPR as inputs (§10).

**Memory read is `S₂S₁S₀ = 111` + read asserted; memory write is write asserted with the bus carrying
the data.**

## 5. The instruction set — `settled` (25 instructions)

Three formats, distinguished by opcode 111 and the I bit:

- **Memory-reference (MRI):** opcode 000–110 (7 instructions), I selects direct/indirect.
- **Register-reference (RRI):** opcode **111 with I = 0** — the low 12 bits pick the operation.
- **Input–output (IO):** opcode **111 with I = 1** — the low 12 bits pick the operation.

| Symbol | I=0 | I=1 | Description |
|---|---|---|---|
| AND | 0xxx | 8xxx | AND memory word to AC |
| ADD | 1xxx | 9xxx | Add memory word to AC |
| LDA | 2xxx | Axxx | Load AC from memory |
| STA | 3xxx | Bxxx | Store AC into memory |
| BUN | 4xxx | Cxxx | Branch unconditionally |
| BSA | 5xxx | Dxxx | Branch and save return address |
| ISZ | 6xxx | Exxx | Increment and skip if zero |

| RRI | Hex | | IO | Hex |
|---|---|---|---|---|
| CLA | 7800 | clear AC | INP | F800 | input char to AC |
| CLE | 7400 | clear E | OUT | F400 | output char from AC |
| CMA | 7200 | complement AC | SKI | F200 | skip on input flag |
| CME | 7100 | complement E | SKO | F100 | skip on output flag |
| CIR | 7080 | circulate right AC & E | ION | F080 | interrupt on |
| CIL | 7040 | circulate left AC & E | IOF | F040 | interrupt off |
| INC | 7020 | increment AC | | |
| SPA | 7010 | skip if AC positive | | |
| SNA | 7008 | skip if AC negative | | |
| SZA | 7004 | skip if AC zero | | |
| SZE | 7002 | skip if E zero | | |
| HLT | 7001 | halt | | |

**7 + 12 + 6 = 25 instructions.** *(Verified: the institutional source states "the total number of
instruction coded in this computer is 25"; the deck's tables give the same three groups.)*

**Note the hex pattern:** RRI codes are 7 followed by a **one-hot** 12-bit field (7800 = bit 11,
7400 = bit 10, … 7001 = bit 0); IO codes are F followed by one-hot bits 11 down to 6. That is not
decoration — the hardware tests `IR(i) = Bᵢ` **directly**, with no decoder, which is why the codes
must be one-hot. Students who memorize the hex without seeing the one-hot structure cannot
reconstruct it.

**Instruction-set completeness — `settled`, and a standard exam question.** A set is complete if it
can compute anything computable. The BC qualifies because it has all four necessary categories:

| Category | BC instructions |
|---|---|
| Arithmetic / logic / shift | ADD, CMA, INC, CIR, CIL, AND, CLA |
| Data transfer (memory ↔ registers) | LDA, STA |
| Control (sequencing, branching) | BUN, BSA, ISZ |
| Input–output | INP, OUT |

*Why these suffice:* AND + CMA give NAND, which is functionally complete for logic; ADD + CMA + INC
give subtraction (2's complement) and hence multiplication/division by repetition; BUN + ISZ give
conditional branching and hence loops. Nothing else is *necessary* — only convenient.

## 6. Timing and control — `settled`

**Hardwired control unit** = 2 decoders + a sequence counter + combinational logic:

- **IR bits 12–14 → a 3×8 decoder → D₀ … D₇** (which opcode).
- **IR bit 15 → the I flip-flop.**
- **IR bits 0–11 → B₀ … B₁₁**, applied directly to control logic gates (the one-hot fields).
- **A 4-bit sequence counter (SC) → a 4×16 decoder → T₀ … T₁₅** (which time step).

**SC increments** on each clock, generating T₀, T₁, T₂, …, and is **cleared** to end an instruction
and start the next fetch. Example from the deck: `D₃T₄: SC ← 0` — "at time T₄, SC is cleared to 0 if
decoder output D₃ is active."

**★ This is the mechanism of instruction execution.** Every control signal in the machine is a
**sum of products of D's and T's** (plus I, R and Bᵢ). "What does the computer do next?" has a
literal answer: whatever gates are enabled by the current D·T combination.

## 7. Instruction cycle — `settled`

Four phases: **fetch → decode → (fetch effective address if indirect) → execute**, then repeat.

**Fetch and decode:**
```
T₀:  AR ← PC                                       (S₂S₁S₀ = 010, LD(AR))
T₁:  IR ← M[AR],  PC ← PC + 1                      (S₂S₁S₀ = 111, LD(IR), INR(PC))
T₂:  D₀…D₇ ← decode IR(12-14),  AR ← IR(0-11),  I ← IR(15)
```

**Why PC increments at T₁, not later:** the address has already been safely copied into AR at T₀, so
PC is free. Incrementing early means PC already points at the next instruction by the time a branch
might overwrite it — which is exactly what makes BSA's "save the return address" work (§8).

**Determining the instruction type at T₃** — four mutually exclusive paths:

| Condition | Action |
|---|---|
| `D′₇ I T₃` | `AR ← M[AR]` — indirect: fetch the effective address |
| `D′₇ I′ T₃` | nothing (direct MRI: AR already holds EA from T₂) |
| `D₇ I′ T₃` | execute a **register-reference** instruction |
| `D₇ I T₃` | execute an **input–output** instruction |

**Memory-reference execution starts at T₄**, because EA is in AR by the end of T₃ either way.

## 8. Memory-reference instructions — `settled`

| Symbol | D | Operation |
|---|---|---|
| AND | D₀ | AC ← AC ∧ M[AR] |
| ADD | D₁ | AC ← AC + M[AR], E ← Cₒᵤₜ |
| LDA | D₂ | AC ← M[AR] |
| STA | D₃ | M[AR] ← AC |
| BUN | D₄ | PC ← AR |
| BSA | D₅ | M[AR] ← PC, PC ← AR + 1 |
| ISZ | D₆ | M[AR] ← M[AR] + 1, if M[AR] + 1 = 0 then PC ← PC + 1 |

**The microoperation sequences (memorize these — F8 in `exam-map.md`):**

```
AND   D₀T₄: DR ← M[AR]
      D₀T₅: AC ← AC ∧ DR,  SC ← 0

ADD   D₁T₄: DR ← M[AR]
      D₁T₅: AC ← AC + DR,  E ← Cₒᵤₜ,  SC ← 0

LDA   D₂T₄: DR ← M[AR]
      D₂T₅: AC ← DR,  SC ← 0

STA   D₃T₄: M[AR] ← AC,  SC ← 0

BUN   D₄T₄: PC ← AR,  SC ← 0

BSA   D₅T₄: M[AR] ← PC,  AR ← AR + 1
      D₅T₅: PC ← AR,  SC ← 0

ISZ   D₆T₄: DR ← M[AR]
      D₆T₅: DR ← DR + 1
      D₆T₆: M[AR] ← DR,  if (DR = 0) then (PC ← PC + 1),  SC ← 0
```

**BSA is the subroutine-call instruction and the one students get wrong.** Mechanism: it stores the
**return address** (PC, which already points past the call) into the word at EA, then jumps to
**EA + 1**. So a subroutine's *first* word is its return-address slot and its code starts one later.
Returning is `BUN` **indirect** through EA. *Worked (deck's figure):* `BSA 135` at location 20, PC = 21
at T₄ → M[135] ← 21, AR ← 136, then PC ← 136. Return with `1 BUN 135` (I = 1) → PC ← M[135] = 21.

⚠ **Why this is a 2-step (T₄, T₅) operation and not one:** AR must be incremented *and* used as the
new PC, but the bus can carry only one thing per clock. Hardware serializes what the symbolic
description writes as a single line. (`misconceptions.md` M8.)

**ISZ** is the loop-counter instruction: increment a memory location, and if it wraps to 0, skip the
next instruction. Counting **up to zero** (rather than down from n) is deliberate — the zero test is
free.

⚠ **Deck errata:** the Unit-2 deck prints ISZ's third line as `D₆T₄` (a typo — it repeats T₄). The
correct timing is **`D₆T₆`**, as the same deck's own "Complete Computer Description" slide shows.
Logged in `CHANGELOG.md` and as `misconceptions.md` M9. *This is exactly why slides do not set facts.*

## 9. Input–output and interrupt — `settled`

**Configuration:** INPR (8) and OUTR (8) talk to the terminal **serially** and to AC **in parallel**.
Flags **FGI** (input) and **FGO** (output) are 1-bit; **IEN** enables interrupts.

**Why the flags exist:** "to synchronize the timing difference between the I/O device and the
computer." The device and CPU run at wildly different speeds; the flag is the handshake.

**Programmed I/O (polling) — the loop and its cost:**
```
   /* input, FGI initially 0 */          /* output, FGO initially 1 */
   loop: if FGI = 0 goto loop            loop: if FGO = 0 goto loop
         AC ← INPR, FGI ← 0                    OUTR ← AC, FGO ← 0
```
In BC assembly: `LOOP, SKI DEV / BUN LOOP / INP DEV`. **Cost:** continuous CPU involvement; the CPU
is slowed to the device's speed. Simple, least hardware — and wasteful. This is rung 1 of the ladder
that U5 climbs.

**I/O instructions** (p = D₇IT₃, Bᵢ = IR(i)):
```
      p:    SC ← 0
INP   pB₁₁: AC(0-7) ← INPR,  FGI ← 0
OUT   pB₁₀: OUTR ← AC(0-7),  FGO ← 0
SKI   pB₉ : if (FGI = 1) then (PC ← PC + 1)
SKO   pB₈ : if (FGO = 1) then (PC ← PC + 1)
ION   pB₇ : IEN ← 1
IOF   pB₆ : IEN ← 0
```

**Interrupt-initiated I/O.** Instead of the CPU watching the device, the **interface watches** and
raises a request when ready; the CPU finishes its instruction, saves its place, services the device,
and returns.

**Setting the interrupt flip-flop R:**
```
T′₀ T′₁ T′₂ (IEN)(FGI + FGO):  R ← 1
```
Read this carefully — it is a favourite exam item. The interrupt is recognized **only when none of
T₀, T₁, T₂ is active** (i.e. the current instruction has moved past fetch/decode), **and** interrupts
are enabled, **and** some flag is set. That is how "finish the current instruction first" is
implemented in hardware.

**The interrupt cycle** (fetch/decode are modified to `R′T₀, R′T₁, R′T₂`, so they only run when
R = 0):
```
RT₀: AR ← 0,  TR ← PC
RT₁: M[AR] ← TR,  PC ← 0
RT₂: PC ← PC + 1,  IEN ← 0,  R ← 0,  SC ← 0
```

**Mechanism:** the interrupt cycle is "a **hardware implementation of a branch-and-save-return-address
operation**" — it is BSA done by hardware, to the fixed location 0. The return address goes to
**M[0]**; control resumes at **address 1**, where the programmer must have placed a branch to the
service routine. Return is `BUN 0` **indirect**. IEN is cleared so the service routine is not itself
interrupted.

## 10. Design of the Basic Computer — `settled`

**Hardware inventory:** memory 4096×16 · registers AR, PC, DR, AC, IR, TR, OUTR, INPR, SC ·
flip-flops I, S, E, R, IEN, FGI, FGO · a 3×8 opcode decoder · a 4×16 timing decoder · a 16-bit common
bus · control logic gates · an adder-and-logic circuit attached to AC.

**★ The design method — this is the whole point of the unit.** To build the control for any register:

> **Scan every register-transfer statement in the complete machine description that changes that
> register, and OR their control conditions together.**

*Worked for AR (the deck's own example):*
```
R′T₀:    AR ← PC          ┐
R′T₂:    AR ← IR(0-11)    ├──→  LD(AR) = R′T₀ + R′T₂ + D′₇IT₃
D′₇IT₃:  AR ← M[AR]       ┘
RT₀:     AR ← 0           ───→  CLR(AR) = RT₀
D₅T₄:    AR ← AR + 1      ───→  INR(AR) = D₅T₄
```

*Worked for a flag (IEN):* the statements are `pB₇: IEN ← 1`, `pB₆: IEN ← 0`, `RT₂: IEN ← 0`, so IEN
is a JK flip-flop with J = pB₇ and K = pB₆ + RT₂.

*Worked for the bus:* PC is loaded from AR in `D₄T₄` (BUN) and `D₅T₅` (BSA), so the encoder input for
"select AR onto the bus" is x₁ = D₄T₄ + D₅T₅.

**This scan is the examinable skill of U2** (F9 in `exam-map.md`) — not the instruction list.

## 11. Design of accumulator logic — `settled`

All statements that change AC:

| Condition | Operation | Control gate |
|---|---|---|
| D₀T₅ | AC ← AC ∧ DR | AND |
| D₁T₅ | AC ← AC + DR | ADD |
| D₂T₅ | AC ← DR | DR (transfer) |
| pB₁₁ | AC(0-7) ← INPR | INPR |
| rB₉ | AC ← AC′ | COM |
| rB₇ | AC ← shr AC, AC(15) ← E | SHR |
| rB₆ | AC ← shl AC, AC(0) ← E | SHL |
| rB₁₁ | AC ← 0 | CLR |
| rB₅ | AC ← AC + 1 | INC |

(where r = D₇I′T₃ is the register-reference condition and p = D₇IT₃ the I/O condition)

So: **LD(AC)** = D₀T₅ + D₁T₅ + D₂T₅ + pB₁₁ + rB₉ + rB₇ + rB₆, **CLR(AC)** = rB₁₁, **INR(AC)** = rB₅.

**The adder-and-logic circuit** is one stage replicated 16 times, feeding AC's J-K inputs, with
inputs from DR(i), AC(i), INPR(i), and the neighbouring AC bits AC(i−1)/AC(i+1) for the shifts.
**This is U1's ALSU, instantiated for a specific machine** — which is why U1 must come first.

---

## Worked-problem patterns for this unit

1. Draw/explain the BC instruction format; distinguish the three types by opcode and I.
2. Given an instruction in hex, say what it is and what it does (use the 7xxx/Fxxx one-hot pattern).
3. Give the bus selection table; state what happens for a given S₂S₁S₀ + LD combination.
4. **Write the fetch–decode sequence with timing.**
5. **Write the full microoperation sequence for a named MRI** (BSA and ISZ are the favourites).
6. Explain BSA with a memory before/after diagram.
7. Explain the interrupt cycle; write its register transfers; explain the T′₀T′₁T′₂ condition.
8. **Derive LD/INR/CLR for a named register** by scanning the RTL.
9. Prove the instruction set is complete by category.

## Confidence summary

`settled`: memory size and instruction format · all 8 registers with widths · the S₂S₁S₀ table ·
all 25 instructions and their hex codes · fetch/decode/type-determination timing · all 7 MRI
microoperation sequences · the I/O instructions · the interrupt-cycle transfers and the R-setting
condition · the control-derivation method with the AR/AC worked results. *(Triangulated across the
professor's deck and two independent institutional reproductions of Mano ch. 5.)*
`likely`: that MUJ examines Mano's exact notation (D·T subscripts) rather than prose — inferred from
the deck reproducing it verbatim.
**Quarantined:** the deck's ISZ `D₆T₄` typo → corrected to `D₆T₆` (see `CHANGELOG.md`).

> **Stage 2 for this unit:** `stage-2/02-basic-computer-organization-and-design.md` — where the BC
> lies (single-cycle memory, no bus contention, no pipelining), why an accumulator machine forces a
> one-address format, the BSA/stack contrast and why real machines abandoned BSA, interrupt latency
> and reentrancy, and what a modern datapath keeps from this picture.
