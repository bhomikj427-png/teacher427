# U3 — Control Unit Design & Microprogrammed Control (Stage 1)

**Lectures L12–L15 · CO2 · MTE + ETE · ⚠ NO DECK SUPPLIED for this unit**

Scope (hand-out lecture plan): L12 Microprogrammed Control · L13 Control Memory · L14 Control unit
design · L15 Program Control.

Truth authority: **Mano 3e ch. 7** (microprogrammed control) and **ch. 8 §8-7** (program control).
Because no slide deck exists for this unit, it is built **textbook-primary** per protocol §2, and
verified against **three independent institutional reproductions of Mano ch. 7 that agree in every
field width and table entry** (see `sources.md`).

> ⚠ **Read `misconceptions.md` M7 before anything else in this unit.** Mano's microprogram example
> uses a **different machine** from U2's Basic Computer. Fusing them is the single most damaging
> error in this subject.

---

## 1. The two ways to build a control unit — `settled`

The control unit's job is fixed: **translate a machine instruction into the timed control signals
that carry out its microoperations.** There are exactly two implementation strategies.

| | **Hardwired** | **Microprogrammed** |
|---|---|---|
| Built from | combinational + sequential logic (decoders, sequence counter, gates) | a **control memory** (ROM) holding microinstructions + CAR + sequencer |
| Control signals come from | gate outputs — sums of D·T products | **bits read out of a control word** |
| Speed | **fast** (gate delay) | slower (a memory read per microinstruction) |
| Changing the instruction set | **redesign and rewire** | **rewrite the microprogram** |
| Cost of a complex ISA | grows badly | grows gently (just more control memory) |
| Typical user | RISC machines, simple/fast controllers | CISC machines with rich instruction sets |
| U2's Basic Computer uses | **this one** | — |

**Mechanism — the real trade.** Hardwired control hard-codes the D·T equations in silicon: minimal
delay, but the design is a tangle of special cases and any ISA change means re-deriving every
equation. Microprogramming replaces that tangle with a **lookup**: each machine instruction gets a
*routine* of microinstructions in ROM, and the control signals are simply bits in the word you just
read. The instruction set becomes **firmware**. The cost is one control-memory access per
microinstruction — you have put a memory in the critical path.

> "The main advantage of the microprogrammed control is the fact that once the hardware
> configuration is established, there should be no need for further hardware or wiring changes."
> — and, directly relevant to U8: **"Most computers based on the reduced instruction set computer
> (RISC) architecture concept use hardwired control rather than a control memory with a
> microprogram."** That sentence is the bridge from this unit to RISC-V.

**Key vocabulary (`settled`):**

| Term | Definition |
|---|---|
| **Control word** | a string of 1s and 0s representing the control variables |
| **Microinstruction** | a control word stored in control memory |
| **Microprogram** | a sequence of microinstructions |
| **Control memory** | the (usually ROM) memory holding microprograms |
| **Routine** | the group of microinstructions implementing one machine instruction |
| **CAR** | Control Address Register — holds the address of the next microinstruction |
| **CDR** | Control Data Register (a.k.a. pipeline register) — holds the microinstruction just read |
| **SBR** | Subroutine Register — holds the return address for microsubroutines |
| **Microprogram sequencer** | the next-address generator |

**On the CDR:** it lets the microoperations of the *current* microinstruction execute **at the same
time** as the *next* microinstruction's address is generated and fetched — pipelining inside the
control unit. "The control unit can operate without CDR" (at lower speed).

**Writable control store (WCS) / dynamic microprogramming** (`settled`, one line): if control memory
is writable rather than ROM, the microprogram — and therefore the machine's instruction set — can be
changed by a systems programmer. Rare in practice; conceptually striking.

## 2. Address sequencing — `settled`

Each machine instruction's routine lives somewhere in control memory. Getting from one
microinstruction to the next requires exactly **four** capabilities:

1. **Increment CAR** — the in-line case, the common one.
2. **Unconditional or conditional branch** — depending on status bits.
3. **Mapping** from the instruction's opcode to the address of its routine.
4. **Subroutine call and return** — via SBR.

**The flow for one machine instruction:**
```
    power on / instruction done
              │
              ▼
    load CAR with the FETCH routine's address
              │
              ▼
    FETCH routine runs (reads the instruction into IR/DR)
              │
              ▼
    MAP: opcode ──→ address of that instruction's routine ──→ CAR
              │
              ▼
    the routine runs (CAR increments; may branch on status; may CALL a shared subroutine)
              │
              ▼
    return to FETCH
```

**Mapping — the mechanism.** Rather than store a lookup table, Mano's mapping is pure wiring: a
**4-bit opcode `xxxx` becomes the 7-bit control-memory address `0xxxx00`.**

```
   opcode        control-memory address
   0000  ADD  →  0 0000 00  =  0
   0001  AND  →  0 0001 00  =  4
   0010  LDA  →  0 0010 00  =  8
   0011  ...  →  0 0011 00  = 12
```

**Why the two trailing zeros:** they leave each routine **4 words** of space (addresses n, n+1, n+2,
n+3) before the next routine begins. Why the leading zero: it confines all 16 routines to the
**first 64 words**, leaving the **upper 64** for the fetch routine and shared subroutines. So the
"0…00" is not arbitrary — it is a storage-allocation decision encoded in wires.
**16 routines × 4 words = 64 words; 64 + 64 = the 128-word control memory.** The numbers are designed
together.

## 3. The microprogram example machine — `settled` (⚠ NOT the Basic Computer)

| | **U2's Basic Computer** (Mano ch. 5) | **U3's microprogram example** (Mano ch. 7) |
|---|---|---|
| Memory | **4096 × 16** | **2048 × 16** |
| Address bits | **12** | **11** |
| Opcode bits | **3** | **4** |
| Instruction format | I(1) + opcode(3) + address(12) | I(1) + opcode(4) + address(11) |
| AR, PC width | 12 | **11** |
| Control | **hardwired** | **microprogrammed**, control memory 128 × 20 |
| CAR, SBR | — | **7 bits each** |
| Instructions | 25 | **4** (ADD, BRANCH, STORE, EXCHANGE) |

**Memorize the right column separately. They are different machines.** (`misconceptions.md` M7.)

The four instructions of the example machine:

| Symbol | Opcode | Operation |
|---|---|---|
| ADD | 0000 | AC ← AC + M[EA] |
| BRANCH | 0001 | if (AC < 0) then (PC ← EA) |
| STORE | 0010 | M[EA] ← AC |
| EXCHANGE | 0011 | AC ← M[EA], M[EA] ← AC |

## 4. Microinstruction format — `settled` (20 bits)

```
┌────────┬────────┬────────┬──────┬──────┬───────────┐
│   F1   │   F2   │   F3   │  CD  │  BR  │    AD     │
├────────┼────────┼────────┼──────┼──────┼───────────┤
│   3    │   3    │   3    │  2   │  2   │     7     │   = 20 bits
└────────┴────────┴────────┴──────┴──────┴───────────┘
 F1,F2,F3 : microoperation fields      CD : condition for branching
 BR       : branch field               AD : address field
```

**Why these widths:** AD is **7 bits** because control memory is 128 = 2⁷ words. Each F field is
**3 bits** because it selects one of 8 microoperations (including "none"). CD and BR are 2 bits each
= 4 conditions and 4 branch types.

**Why *three* microoperation fields and not one big one:** F1, F2 and F3 are decoded **independently
and in parallel** (three 3×8 decoders), so **up to three microoperations can be specified in a single
microinstruction** — provided they come from different fields and don't conflict. That is why the
fields are grouped the way they are: operations that could sensibly happen together sit in different
fields. This is *vertical* microprogramming (encoded fields, compact) as opposed to *horizontal*
(one bit per control signal, wide but fully parallel).

**F1 — microoperation field 1:**

| F1 | Microoperation | Symbol |
|---|---|---|
| 000 | none | NOP |
| 001 | AC ← AC + DR | ADD |
| 010 | AC ← 0 | CLRAC |
| 011 | AC ← AC + 1 | INCAC |
| 100 | AC ← DR | DRTAC |
| 101 | AR ← DR(0-10) | DRTAR |
| 110 | AR ← PC | PCTAR |
| 111 | M[AR] ← DR | WRITE |

**F2 — microoperation field 2:**

| F2 | Microoperation | Symbol |
|---|---|---|
| 000 | none | NOP |
| 001 | AC ← AC − DR | SUB |
| 010 | AC ← AC ∨ DR | OR |
| 011 | AC ← AC ∧ DR | AND |
| 100 | DR ← M[AR] | READ |
| 101 | DR ← AC | ACTDR |
| 110 | DR ← DR + 1 | INCDR |
| 111 | DR(0-10) ← PC | PCTDR |

**F3 — microoperation field 3:**

| F3 | Microoperation | Symbol |
|---|---|---|
| 000 | none | NOP |
| 001 | AC ← AC ⊕ DR | XOR |
| 010 | AC ← AC′ | COM |
| 011 | AC ← shl AC | SHL |
| 100 | AC ← shr AC | SHR |
| 101 | PC ← PC + 1 | INCPC |
| 110 | PC ← AR | ARTPC |
| 111 | *reserved* | — |

**CD — condition field:**

| CD | Condition | Symbol | Meaning |
|---|---|---|---|
| 00 | always = 1 | **U** | unconditional |
| 01 | DR(15) | **I** | indirect-address bit |
| 10 | AC(15) | **S** | sign bit of AC |
| 11 | AC = 0 | **Z** | AC is zero |

**BR — branch field:**

| BR | Symbol | Function |
|---|---|---|
| 00 | **JMP** | if condition = 1: CAR ← AD; else CAR ← CAR + 1 |
| 01 | **CALL** | if condition = 1: CAR ← AD **and SBR ← CAR + 1**; else CAR ← CAR + 1 |
| 10 | **RET** | CAR ← SBR (return from microsubroutine) |
| 11 | **MAP** | CAR(2-5) ← DR(11-14), CAR(0,1,6) ← 0 |

**Note MAP is where the `0xxxx00` wiring lives:** the opcode bits DR(11-14) are dropped into CAR bits
2–5 and the remaining bits (0, 1, 6) are forced to 0 — producing exactly `0 xxxx 00`.

**Symbolic microinstruction format:** `Label: Micro-ops CD BR AD`, where Micro-ops is 1–3 symbols
separated by commas, CD ∈ {U, I, S, Z}, BR ∈ {JMP, CALL, RET, MAP}, AD is a symbolic address, `NEXT`,
or empty.

## 5. The fetch routine — `settled` (the standard exam item)

**What fetch must do:** read the instruction from memory, decode it, update PC.

```
              AR ← PC
              DR ← M[AR],  PC ← PC + 1
              AR ← DR(0-10),  CAR(2-5) ← DR(11-14),  CAR(0,1,6) ← 0
```

**As a symbolic microprogram** (placed at address 64, the start of the upper half):

```
         ORG 64
FETCH:   PCTAR            U   JMP   NEXT
         READ, INCPC      U   JMP   NEXT
         DRTAR            U   MAP
```

**As binary** (address, then F1 F2 F3 CD BR AD):

```
 1000000   110  000  000   00   00   1000001
 1000001   000  100  101   00   00   1000010
 1000010   101  000  000   00   11   0000000
```

Read the middle line as a worked example of the three-field parallelism: **F2 = 100 (READ: DR ← M[AR])
and F3 = 101 (INCPC: PC ← PC + 1) execute in the same microinstruction**, because they occupy
different fields. That is the whole argument for splitting F1/F2/F3.

The third line uses **BR = 11 (MAP)**, so AD is irrelevant (shown as 0s) — the next address comes
from the opcode.

**Microsubroutine example — INDRCT.** The indirect-address fetch is needed by several routines, so it
is written once as a subroutine and reached with **CALL**:
```
INDRCT:  READ             U   JMP   NEXT
         DRTAR            U   RET
```
A routine calls it conditionally on the indirect bit: `ADD: NOP  I  CALL  INDRCT`. **CD = I** means
"call only if DR(15) = 1" — conditional subroutine call, in one microinstruction.

## 6. Design of the control unit — `settled`

**Two halves:**

**(a) The microoperation decoders.** F1, F2, F3 each drive a **3×8 decoder** → 24 outputs, of which
the 21 non-NOP ones are the control signals. Signals from different fields that do the same thing are
OR-ed: e.g. `AR ← PC` is asserted by **PCTAR** (F1 = 110) and `AR ← DR(0-10)` by **DRTAR** (F1 = 101),
so AR's load input is PCTAR + DRTAR, and its multiplexer select chooses between PC and DR(0-10).
**This is exactly U2's "scan the statements" method, applied to decoder outputs instead of D·T
products.**

**(b) The microprogram sequencer** — computes the next CAR value. Components: two multiplexers, an
incrementer, CAR, SBR, and input logic.

- **MUX1** selects the next address from: CAR + 1 (in-line), AD (branch), SBR (return), or the
  external MAP value.
- **MUX2** selects **which status bit** to test, under the **CD** field: 1 (unconditional), I, S, or
  Z. Its output is the **test value T**.

**Input logic (`settled` — the derivation examiners ask for):** with I₁I₀ = the BR field and T = the
tested condition,

| I₁ I₀ T | Meaning | Source of address | S₁S₀ | L |
|---|---|---|---|---|
| 0 0 0 | in-line | CAR + 1 | 00 | 0 |
| 0 0 1 | JMP | CS(AD) | 01 | 0 |
| 0 1 0 | in-line | CAR + 1 | 00 | 0 |
| 0 1 1 | CALL | CS(AD) and SBR ← CAR + 1 | 01 | **1** |
| 1 0 x | RET | SBR | 10 | 0 |
| 1 1 x | MAP | DR(11-14) | 11 | 0 |

From which:
```
S₁ = I₁
S₀ = I₀I₁ + I′₁T
L  = I′₁I₀T          (L = load SBR, i.e. this is a taken CALL)
```

**Read the table as the mechanism:** when I₁ = 0 (JMP or CALL), the branch is **taken only if T = 1** —
rows with T = 0 fall through to CAR + 1. When I₁ = 1 (RET or MAP), T is irrelevant (`x`), which is why
those rows are unconditional.

## 7. Program control — `settled` (L15)

This is the *machine-instruction*-level counterpart of the microinstruction branching above, and it
is Mano ch. 8 material, not ch. 7.

**Program control instructions** change the value of PC, so they alter the sequence of execution:
branch, jump, skip, call, return, compare, test.

**Status bit conditions (the flags).** A status register holds bits set by the ALU's last operation.
The four classical ones, defined from an n-bit ALU result with carries C into and out of the sign
position:

| Bit | Name | Set when |
|---|---|---|
| **C** | carry | carry-out of the MSB |
| **S** | sign | MSB of the result is 1 |
| **Z** | zero | all result bits are 0 |
| **V** | overflow | **Cₙ ⊕ Cₙ₋₁** — carry into the sign position differs from carry out of it |

**Mechanism — why V is that XOR.** Signed overflow means the true result did not fit. If the carry
*into* the sign bit differs from the carry *out* of it, the sign bit has been corrupted by the
magnitude bits — exactly the condition Cₙ ⊕ Cₙ₋₁ detects. **C is for unsigned overflow; V is for
signed.** Confusing them is `misconceptions.md` M11.

**Conditional branch instructions** test these bits: BZ (branch if zero, Z = 1), BNZ, BC, BNC, BP
(positive, S = 0), BM (minus, S = 1), BV (overflow). For **unsigned** comparison the relevant bit is
C; for **signed**, the combination of S and V.

**Subroutine call and return.** CALL must (i) save the return address and (ii) jump. Three historical
places to save it:

| Where the return address goes | Consequence |
|---|---|
| a fixed memory location (**BSA**, U2's way) | simple; **not reentrant, no recursion** |
| a processor register | fast; only one level deep unless saved |
| **a stack** | **reentrant and recursive** — the modern answer |

**Mechanism:** with a stack, CALL is `SP ← SP − 1; M[SP] ← PC; PC ← EA` and RET is
`PC ← M[SP]; SP ← SP + 1`. Because each call pushes a *new* frame, a subroutine may call itself. U2's
BSA overwrites the single saved word, so a second (or recursive) call destroys the first return
address. **This is why real machines use a stack and the BC does not** — and it is a clean exam
compare/contrast.

**Program interrupt** (the machine-level view of U2 §9): external, internal (traps — overflow,
divide-by-zero, invalid opcode) and software (supervisor call) interrupts. The CPU must save
**program state**: PC, plus status bits, plus (depending on the machine) registers. Interrupts differ
from subroutine calls in that they are **asynchronous** — initiated by something other than the
running program.

---

## Worked-problem patterns for this unit

1. **Hardwired vs microprogrammed control** — comparison table + when to use each.
2. Draw the microprogrammed control organization (CAR, control memory, CDR, sequencer).
3. State the four address-sequencing capabilities; explain mapping `0xxxx00` and *why* 4 words per
   routine and 64 + 64.
4. **Given the F1/F2/F3/CD/BR/AD format, decode a binary microinstruction into its microoperations**
   (or encode a symbolic one to binary).
5. **Write the fetch routine** symbolically and in binary.
6. Explain how three microoperations can occur in one microinstruction, and when they cannot.
7. Derive the sequencer's input logic (S₁, S₀, L) from the I₁I₀T table.
8. Status bits: define C, S, Z, V; derive V = Cₙ ⊕ Cₙ₋₁; pick the right flag for a signed vs
   unsigned comparison.
9. Compare return-address strategies; explain why a stack permits recursion and BSA does not.

## Confidence summary

`settled`: hardwired vs microprogrammed trade · all vocabulary · the four sequencing capabilities ·
mapping 0xxxx00 and the 64/64 split · **control memory 128 × 20** · **microinstruction fields
3/3/3/2/2/7** · the complete F1, F2, F3, CD, BR tables · the fetch routine in symbolic and binary ·
the sequencer input logic S₁ = I₁, S₀ = I₀I₁ + I′₁T, L = I′₁I₀T · the example machine's parameters
(2048×16, 4-bit opcode, CAR/SBR 7 bits) · program-control status bits and V = Cₙ ⊕ Cₙ₋₁ · the
BSA-vs-stack reentrancy argument.
*(Triangulated: three independent institutional reproductions of Mano ch. 7 agree on every field
width and every table entry.)*
`uncertain`: **the emphasis** the instructor places here — no deck was supplied for L12–L15, so the
depth expected is inferred from the lecture count (4 lectures, CO2) rather than observed.

> **Stage 2 for this unit:** `stage-2/03-control-unit-and-microprogrammed-control.md` — horizontal vs
> vertical microprogramming and the encoding/parallelism trade, nanoprogramming, why microcode
> survived into modern x86 (and what "microcode update" actually patches), the Wilkes 1951 origin,
> and the real reason RISC abandoned it.
