# 09 — Microprogrammed control

**U3 (L12–L14) · MTE scope · needs 06, 07, 08**

> ⚠ **Read this before anything else in this file.**
>
> **Neither assignment touches U3.** Not one question in A1 or A2. It is tempting to conclude the
> unit is not examined — that conclusion is wrong. The course hand-out's lecture plan prints the row
> *"Mid Term Examination"* **after L19**, and U3 is **L12–L15**. It is on the mid-term.
>
> Because he has asked nothing here, **Mano chapter 7's 24 problems are the only question evidence
> that exists for this unit.** Every question below is one of them. There is also **no slide deck**
> for L12–L15, so this unit is built textbook-first and verified against three independent
> institutional reproductions that agree on every field width and table entry.

> ⚠ **The second warning, and it is the most damaging error in the subject.**
> Mano's microprogram example uses a **different machine** from U2's Basic Computer. Different memory
> size, different opcode width, different registers. Step 3 is entirely about keeping them apart.

---

## Map

```
   [1] Two ways to build control ──► hardwired (U2) vs microprogrammed (here)
         │
         ▼
   [2] The organization ──► CAR · control memory · CDR · sequencer
         │                        │
         ▼                        ▼
   [3] ⚠ A DIFFERENT machine   [4] Address sequencing — the 4 capabilities
                                    incl. mapping 0xxxx00
         │                                │
         ▼                                ▼
   [5] The microinstruction format    [6] Encode / decode one
       F1 F2 F3 CD BR AD                   (3 at once — when, and when not)
         │
         ▼
   [7] The fetch routine ──► [8] Microsubroutines ──► [9] The sequencer logic
```

---

## The questions this file answers

All from Mano chapter 7. **None has been asked yet — that is the point.**

| # | Question | Mano |
|---|---|---|
| 1 | Explain the difference between hardwired control and microprogrammed control. Is it possible to have hardwired control associated with a control memory? | **7-2** |
| 2 | Define: microoperation, microinstruction, microprogram, microcode. | **7-3** |
| 3 | Given propagation delays, what is the maximum clock frequency? What if the CDR is removed? | **7-4** |
| 4 | Control memory 1024 × 32, microoperations field 16 bits — size the other fields. | **7-5** |
| 5 | Control memory 4096 × 24 — CAR bits, MUX input widths, MUX count. | **7-6** |
| 6 | Using the mapping of Fig. 7-3, give the first microinstruction address for opcodes 0010, 1011, 1111. | **7-7** |
| 7 | Give the 9-bit microoperation field for stated microoperations. | **7-11** |
| 8 | Convert symbolic microoperations to register transfers and to binary. | **7-12** |
| 9 | Divide a 9-bit microoperation field into subfields to specify 46 microoperations. | **7-20** |
| 10 | 16 registers, ALU with 32 operations, shifter with 8 — formulate a control word. | **7-21** |

Also live: **7-1, 7-8, 7-9, 7-10, 7-13, 7-14, 7-15, 7-16, 7-17, 7-18, 7-19, 7-22, 7-23, 7-24.**

---

## Build

### 1 · Two ways to build a control unit

> **Q** `[Mano 7-2]`
> **Explain the difference between hardwired control and microprogrammed control. Is it possible to
> have a hardwired control associated with a control memory?**
>
> *You built a hardwired control unit in file 08 — the D·T gate equations. Guess what the alternative
> could possibly be. Then read on.*

The control unit's job never changes: **turn a machine instruction into the timed control signals
that carry out its microoperations.** There are exactly two ways to do it.

| | **Hardwired** | **Microprogrammed** |
|---|---|---|
| Built from | decoders, a sequence counter, gates | a **control memory** (ROM) + CAR + sequencer |
| Control signals are | gate outputs — sums of D·T products | **bits read out of a control word** |
| Speed | **fast** (gate delay) | slower (a memory read per microinstruction) |
| Changing the instruction set | redesign and **rewire** | **rewrite the microprogram** |
| Cost of a rich ISA | grows badly | grows gently — just more ROM |
| Typical user | RISC, simple fast controllers | CISC with many complex instructions |
| U2's Basic Computer | **this one** | — |

★ **The real trade.** Hardwired control hard-codes the D·T equations in silicon: minimal delay, but the
design is a tangle of special cases and any ISA change means re-deriving every equation — you did
twelve of them for PC alone in file 08. Microprogramming replaces that tangle with a **lookup**: each
machine instruction gets a *routine* of microinstructions in ROM, and the control signals are simply
bits in the word you just read. **The instruction set becomes firmware.** The price is one
control-memory access per microinstruction — you have put a memory in the critical path.

Mano's own sentence, which is also the bridge to U8: *"Most computers based on the reduced
instruction set computer (RISC) architecture concept use **hardwired control** rather than a control
memory with a microprogram."*

**The second half of the question** — can hardwired control have a control memory? **Yes, in the sense
that a ROM can be used inside a hardwired design as a lookup table for some of the control
equations** (a ROM is just combinational logic with the truth table stored rather than gated). What
makes a design *microprogrammed* is not the presence of a memory but that the memory holds
**sequences** of microinstructions with a CAR sequencing through them. A ROM used as a static
function of D and T is still hardwired control.

> ✓ **Check 1.** (a) Where do control signals physically come from in each design?
> (b) Which is faster and why? (c) Why does a rich instruction set favour microprogramming?

---

### 2 · The organization, and what CDR buys

> **Q** `[Mano 7-4]`
> **The microprogrammed control organization of Fig. 7-1 has the following propagation delays: 40 ns
> to generate the next address, 10 ns to transfer the address into the control address register,
> 40 ns to access the control memory ROM, 10 ns to transfer the microinstruction into the control
> data register, and 40 ns to perform the required microoperations. What is the maximum clock
> frequency the control can use? What would the frequency be if the control data register is not
> used?**
>
> *This is the only numerical in the chapter. Guess whether removing a register makes the machine
> faster or slower. Then read on.*

**The vocabulary first** — Mano 7-3 asks for it directly:

| Term | Definition |
|---|---|
| **Control word** | a string of 1s and 0s representing the control variables |
| **Microinstruction** | a control word stored in control memory |
| **Microprogram** | a sequence of microinstructions |
| **Control memory** | the (usually ROM) memory holding microprograms |
| **Routine** | the group of microinstructions implementing **one machine instruction** |
| **Microcode** | the microinstructions collectively — the machine's firmware |
| **CAR** | Control Address Register — holds the address of the next microinstruction |
| **CDR** | Control Data Register (pipeline register) — holds the microinstruction just read |
| **SBR** | Subroutine Register — holds the return address for microsubroutines |

```
        ┌─────────────┐
        │ next-address│◄────── status bits, BR/CD fields
        │  generator  │
        │ (sequencer) │
        └──────┬──────┘  40 ns
               ▼
        ┌─────────────┐
        │     CAR     │  10 ns
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │   control   │  40 ns
        │   memory    │
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │     CDR     │  10 ns
        └──────┬──────┘
               ▼
        control signals ──► 40 ns of microoperations
```

★ **What CDR is for:** it lets the microoperations of the **current** microinstruction execute *at the
same time* as the **next** microinstruction's address is generated and fetched. It is pipelining,
inside the control unit. Mano: *"the control unit can operate without CDR"* — at lower speed.

**With CDR** — the two paths run in parallel, so the clock period is the **longer** of them:

| Path | Time |
|---|---|
| address generation + CAR + ROM access + CDR | 40 + 10 + 40 + 10 = **100 ns** |
| microoperations | 40 ns |

Period = **100 ns** → **maximum clock frequency = 10 MHz**.

**Without CDR** — nothing overlaps; everything happens in one serial cycle:

40 (generate) + 10 (CAR) + 40 (ROM) + 40 (microoperations) = **130 ns** → **≈ 7.69 MHz**.

So removing a register makes the machine **slower**, which is the counter-intuitive point of the
question. A pipeline register costs 10 ns of latency and buys you the overlap of a 40 ns stage.

> ✓ **Check 2.** (a) Why does adding CDR increase the clock frequency? (b) Which path sets the clock
> period with CDR present? (c) What is CDR also called, and why is that name apt?

---

### 3 · ⚠ A different machine

> **Q** *(no Mano problem — but this is where marks are lost)*
> **How does Mano's microprogram example machine differ from the Basic Computer of U2?**
>
> *Guess whether the control memory in this chapter controls the machine you spent files 06–08 on.*

**It does not.** Chapter 7's example is a *different* machine, and fusing the two is the single most
damaging error in this subject.

| | **U2's Basic Computer** (ch. 5) | **U3's example machine** (ch. 7) |
|---|---|---|
| Memory | **4096 × 16** | **2048 × 16** |
| Address bits | **12** | **11** |
| Opcode bits | **3** | **4** |
| Instruction format | I(1) + opcode(3) + address(12) | I(1) + opcode(4) + address(11) |
| AR, PC width | 12 | **11** |
| Control | **hardwired** | **microprogrammed**, control memory **128 × 20** |
| CAR, SBR | — | **7 bits each** |
| Instructions | 25 | **4** |

The example machine's four instructions:

| Symbol | Opcode | Operation |
|---|---|---|
| ADD | 0000 | AC ← AC + M[EA] |
| BRANCH | 0001 | if (AC < 0) then (PC ← EA) |
| STORE | 0010 | M[EA] ← AC |
| EXCHANGE | 0011 | AC ← M[EA], M[EA] ← AC |

**Memorise the right-hand column separately.** If an exam question says "control memory", it is this
machine; if it says "Basic Computer" or names AR/PC as 12 bits, it is U2's.

> ✓ **Check 3.** (a) How many bits in this machine's AR, and why? (b) How many instructions does it
> have? (c) A question mentions a 7-bit CAR. Which machine is it about?

---

### 4 · Address sequencing and the mapping

> **Q** `[Mano 7-7]`
> **Using the mapping procedure described in Fig. 7-3, give the first microinstruction address for the
> following operation codes: (a) 0010 (b) 1011 (c) 1111.**
>
> *Guess how an opcode could become a ROM address with no lookup table at all.*

**Four capabilities** are needed to get from one microinstruction to the next:

1. **Increment CAR** — the in-line case, the common one.
2. **Branch**, conditional or unconditional, on status bits.
3. **Mapping** from the instruction's opcode to the address of its routine.
4. **Subroutine call and return** — via SBR.

```
    instruction done
          │
          ▼
    CAR ← address of the FETCH routine
          │
          ▼
    FETCH runs (reads the instruction into DR)
          │
          ▼
    MAP: opcode ──► address of that instruction's routine ──► CAR
          │
          ▼
    the routine runs (CAR increments; may branch; may CALL a shared subroutine)
          │
          ▼
    back to FETCH
```

★ **Mapping is pure wiring, not a table.** A 4-bit opcode `xxxx` becomes the 7-bit control-memory
address **`0xxxx00`**.

| Opcode | Address bits | Decimal |
|---|---|---|
| 0000 | `0 0000 00` | 0 |
| 0001 | `0 0001 00` | 4 |
| 0010 | `0 0010 00` | **8** |
| 1011 | `0 1011 00` | **44** |
| 1111 | `0 1111 00` | **60** |

So the answers are **8, 44 and 60**.

**Why the two trailing zeros:** they leave each routine **4 words** of space (n, n+1, n+2, n+3) before
the next routine starts. **Why the leading zero:** it confines all 16 routines to the **first 64
words**, leaving the **upper 64** for the fetch routine and shared subroutines.
**16 routines × 4 words = 64; 64 + 64 = the 128-word control memory.** The numbers are designed
together — the `0…00` is a storage-allocation decision encoded in wires.

> ✓ **Check 4.** (a) Give the address for opcode 0110. (b) How many words does each routine get, and
> why exactly that many? (c) `[Mano 7-8]` Design a mapping giving **8** consecutive microinstructions
> per routine, with a 6-bit opcode and a 2048-word control memory.

---

### 5 · The microinstruction format

> **Q** `[Mano 7-5]`
> **The system uses a control memory of 1024 words of 32 bits each. The microinstruction has three
> fields; the microoperations field has 16 bits. a. How many bits are in the branch address field and
> the select field? b. If there are 16 status bits, how many bits of the branch logic select a status
> bit? c. How many bits are left to select an input for the multiplexers?**
>
> *Every part is the file-00 counting fact again. Do it before reading.*

**(a)** 1024 words = 2¹⁰ → branch address field = **10 bits**. 32 − 16 − 10 = **6 bits** for the
select field.
**(b)** 16 status bits = 2⁴ → **4 bits** select one of them.
**(c)** 6 − 4 = **2 bits** left for the multiplexer input select.

**Now the format of the example machine** — 20 bits, and the widths are all derived the same way:

```
┌────────┬────────┬────────┬──────┬──────┬───────────┐
│   F1   │   F2   │   F3   │  CD  │  BR  │    AD     │
├────────┼────────┼────────┼──────┼──────┼───────────┤
│   3    │   3    │   3    │  2   │  2   │     7     │   = 20 bits
└────────┴────────┴────────┴──────┴──────┴───────────┘
```

**AD is 7 bits** because control memory is 128 = 2⁷ words. **Each F field is 3 bits** because it
selects one of 8 microoperations (including "none"). **CD and BR are 2 bits** each = 4 conditions and
4 branch types.

★ **Why three microoperation fields rather than one big one:** F1, F2 and F3 are decoded
**independently and in parallel** by three 3×8 decoders, so **up to three microoperations can be
specified in one microinstruction** — provided they come from different fields. The grouping is
deliberate: operations that could sensibly happen together sit in different fields.

This is **vertical** microprogramming (encoded fields, compact, needs decoders) as opposed to
**horizontal** (one bit per control signal — wide, fully parallel, no decoding).

**F1**

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

**F2**

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

**F3**

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

**CD — condition field**

| CD | Condition | Symbol |
|---|---|---|
| 00 | always = 1 | **U** (unconditional) |
| 01 | DR(15) | **I** (indirect bit) |
| 10 | AC(15) | **S** (sign of AC) |
| 11 | AC = 0 | **Z** |

**BR — branch field**

| BR | Symbol | Function |
|---|---|---|
| 00 | **JMP** | if condition: CAR ← AD, else CAR ← CAR + 1 |
| 01 | **CALL** | if condition: CAR ← AD **and SBR ← CAR + 1**, else CAR ← CAR + 1 |
| 10 | **RET** | CAR ← SBR |
| 11 | **MAP** | CAR(2-5) ← DR(11-14), CAR(0,1,6) ← 0 |

**MAP is where the `0xxxx00` wiring lives** — the opcode bits are dropped into CAR bits 2–5 and the
rest forced to 0.

Symbolic form: `Label: Micro-ops  CD  BR  AD`.

> ✓ **Check 5.** (a) Why is AD 7 bits? (b) `[Mano 7-6]` Control memory 4096 × 24: how many bits in
> CAR, how many in each of the four MUX inputs, and how many multiplexers?
> (c) What is the difference between horizontal and vertical microprogramming?

---

### 6 · Encoding and decoding microinstructions

> **Q** `[Mano 7-11]` **Using Table 7-1, give the 9-bit microoperation field for:**
> **a. `AC ← AC + 1, DR ← DR + 1`  b. `PC ← PC + 1, DR ← M[AR]`  c. `DR ← AC, AC ← DR`**
>
> **and** `[Mano 7-12]` **Convert to register transfer statements and to binary:**
> **a. READ, INCPC  b. ACTDR, DRTAC  c. ARTPC, DRTAC, WRITE**
>
> *Do 7-11 first — it is lookup. Then attempt 7-12(c) and notice something.*

**7-11** — find each symbol's field, then fill the other fields with NOP:

| | Microoperations | F1 | F2 | F3 | 9-bit field |
|---|---|---|---|---|---|
| a | INCAC (F1), INCDR (F2) | 011 | 110 | 000 | **011 110 000** |
| b | READ (F2), INCPC (F3) | 000 | 100 | 101 | **000 100 101** |
| c | DRTAC (F1), ACTDR (F2) | 100 | 101 | 000 | **100 101 000** |

**(c) is the simultaneous swap again** — `DR ← AC, AC ← DR` in one microinstruction, for exactly the
reason file 03 step 3 gave: both read the other's old value and both capture at the same edge. It
works here because the two symbols live in **different fields**.

**7-12** — the same lookup, run backwards:

| | RTL | F1 | F2 | F3 | Binary |
|---|---|---|---|---|---|
| a | `DR ← M[AR], PC ← PC + 1` | 000 | 100 | 101 | **000 100 101** |
| b | `AC ← DR, DR ← AC` | 100 | 101 | 000 | **100 101 000** |
| c | *see below* | — | — | — | **impossible** |

★ **(c) cannot be encoded, and that is the point of the question.**
ARTPC is **F3** (110) — fine. But **DRTAC is F1 = 100** and **WRITE is F1 = 111**. Both live in F1,
and a 3-bit field holds one value. The microinstruction can specify at most one F1 operation, so
`DRTAC` and `WRITE` **cannot occur in the same microinstruction**. They must be split across two:

```
  DRTAC, ARTPC     U  JMP  NEXT
  WRITE            U  JMP  NEXT
```

**The general rule, which is the exam-worthy sentence:** three microoperations fit in one
microinstruction **if and only if they come from three different fields**. Two from the same field is
a conflict, and the field grouping is what decides which combinations a machine can do at once. That
is the cost of vertical microprogramming — and the reason horizontal microprogramming exists.

> ✓ **Check 6.** (a) Give the 9-bit field for `AC ← 0, DR ← M[AR], PC ← PC + 1`.
> (b) Why can `SUB` and `READ` not share a microinstruction? (c) State the fit-in-one rule.

---

### 7 · The fetch routine

> **Q** *(the standard exam item for this unit; `[Mano 7-14]` is its cousin)*
> **Write the fetch routine of the example machine, symbolically and in binary.**
>
> *The BC's fetch was three lines (file 07, step 2). Guess whether this one is longer or shorter.*

**What fetch must do:** read the instruction from memory, decode it, update PC.

```
   AR ← PC
   DR ← M[AR],  PC ← PC + 1
   AR ← DR(0-10),  CAR(2-5) ← DR(11-14),  CAR(0,1,6) ← 0
```

**Symbolically**, placed at address 64 (the start of the upper half):

```
         ORG 64
FETCH:   PCTAR            U   JMP   NEXT
         READ, INCPC      U   JMP   NEXT
         DRTAR            U   MAP
```

**In binary** (address, then F1 F2 F3 CD BR AD):

```
 1000000   110 000 000   00  00   1000001
 1000001   000 100 101   00  00   1000010
 1000010   101 000 000   00  11   0000000
```

Read the middle line as the worked example of three-field parallelism: **F2 = 100 (READ) and
F3 = 101 (INCPC) execute in the same microinstruction** because they occupy different fields. That is
the whole argument for splitting F1/F2/F3.

The third line uses **BR = 11 (MAP)**, so AD is irrelevant (shown as zeros) — the next address comes
from the opcode.

> ✓ **Check 7.** (a) Why is AD all zeros on the MAP line? (b) Which two microoperations run together
> on the middle line, and why can they? (c) Why is the fetch routine at address 64 rather than 0?

---

### 8 · Microsubroutines

> **Q** `[Mano 7-13]`
> **Suppose we change the ADD routine to the two microinstructions `ADD: READ I CALL INDR2` /
> `ADD U JMP FETCH`. What should subroutine INDR2 be?**
>
> *Guess what work the subroutine has to do, given that the caller has already done the READ.*

The indirect-address fetch is needed by several routines, so it is written **once** as a
microsubroutine:

```
INDRCT:  READ             U   JMP   NEXT
         DRTAR            U   RET
```

A routine calls it conditionally on the indirect bit: `ADD: NOP  I  CALL  INDRCT`.
**CD = I** means *call only if DR(15) = 1* — a conditional subroutine call in **one microinstruction**.
`CALL` saves CAR + 1 into SBR; `RET` restores CAR from SBR.

Now the question. The caller has already performed the READ (`ADD: READ I CALL INDR2`), so INDR2
must **not** read again — it starts from the value already in DR:

```
INDR2:   DRTAR            U   JMP   NEXT      AR ← DR(0-10): the indirect address
         READ             U   RET             DR ← M[AR]:    the real operand
```

The caller's second line then adds. **The difference from INDRCT is only where the first READ
happens** — which is precisely what the question is testing.

⚠ **One-level limit.** SBR is a single register, so a microsubroutine **cannot call another
microsubroutine**. This is the same reentrancy problem as U2's BSA (file 07, step 6), and file 10
explains why real machines solved it with a stack.

> ✓ **Check 8.** (a) What does CALL save, and where? (b) Why can a microsubroutine not call another
> one? (c) What does `CD = I` mean on a CALL line?

---

### 9 · The microprogram sequencer

> **Q** `[Mano 7-22]`
> **The input logic of the microprogram sequencer has four inputs I₂, I₁, I₀, T and three outputs
> S₁, S₀, L. Design the input logic circuit with a minimum number of gates.**
>
> *This is file 08's derivation skill applied to the sequencer. Try the truth table before reading.*

**The sequencer computes the next CAR value.** Components: two multiplexers, an incrementer, CAR, SBR
and the input logic.

- **MUX1** selects the next address from: **CAR + 1** (in-line), **AD** (branch), **SBR** (return), or
  the external **MAP** value.
- **MUX2** selects **which status bit to test**, under the CD field: 1, I, S or Z. Its output is the
  test value **T**.

With I₁I₀ = the BR field and T = the tested condition:

| I₁ I₀ T | Meaning | Address source | S₁S₀ | L |
|---|---|---|---|---|
| 0 0 0 | in-line | CAR + 1 | 00 | 0 |
| 0 0 1 | JMP taken | AD | 01 | 0 |
| 0 1 0 | in-line | CAR + 1 | 00 | 0 |
| 0 1 1 | CALL taken | AD, **SBR ← CAR + 1** | 01 | **1** |
| 1 0 × | RET | SBR | 10 | 0 |
| 1 1 × | MAP | DR(11-14) | 11 | 0 |

**From which:**

```
 S₁ = I₁
 S₀ = I₀I₁ + I′₁T
 L  = I′₁I₀T           (load SBR — i.e. a taken CALL)
```

**Read the table as the mechanism:** when **I₁ = 0** (JMP or CALL) the branch is taken **only if
T = 1** — the T = 0 rows fall through to CAR + 1. When **I₁ = 1** (RET or MAP) T is a don't-care,
which is why those two are unconditional.

> ✓ **Check 9.** (a) Why is T a don't-care for RET and MAP? (b) What does L do, and when is it 1?
> (c) What does MUX2 select?

---

### 10 · Sizing a control word from scratch

> **Q** `[Mano 7-21]`
> **A computer has 16 registers, an ALU with 32 operations, and a shifter with eight operations, all
> connected to a common bus. a. Formulate a control word for a microoperation. b. Specify the number
> of bits in each field and give a general encoding scheme. c. Show the bits of the control word that
> specify `R4 ← R5 + R6`.**
>
> *Everything you need is file 03's bus plus file 05's ALSU. Try it before reading.*

**(a)** A microoperation on a bus machine needs to say: which two registers feed the ALU, what the ALU
does, what the shifter does, and where the result goes. **Five fields:**

```
┌──────┬──────┬──────┬──────┬──────┐
│  A   │  B   │  D   │ ALU  │  SH  │
├──────┼──────┼──────┼──────┼──────┤
│  4   │  4   │  4   │  5   │  3   │  = 20 bits
└──────┴──────┴──────┴──────┴──────┘
  src1  src2   dest  operation  shift
```

**(b)** 16 registers = 2⁴ → **4 bits** each for A, B and D. 32 ALU operations = 2⁵ → **5 bits**.
8 shifter operations = 2³ → **3 bits**. Total **20 bits**. (Encoding: reserve code 0000 in the
register fields for "no register / external", and 000 in SH for "no shift".)

**(c)** `R4 ← R5 + R6`: A = R5 = **0101**, B = R6 = **0110**, D = R4 = **0100**, ALU = the *add* code,
SH = **000** (no shift).

```
  0101   0110   0100   <add>   000
   R5     R6     R4     ALU     no shift
```

This is the same counting rule as A2 Q1 (file 06, step 1) in a different costume: **n bits name 2ⁿ
things**, applied field by field.

> ✓ **Check 10.** (a) 32 registers instead of 16 — what happens to the word length?
> (b) `[Mano 7-20]` Divide a 9-bit microoperation field into subfields to specify **46**
> microoperations. How many can be specified in one microinstruction?

---

## Exam form

### The comparison table (most likely question)

Reproduce the hardwired-vs-microprogrammed table from step 1, then the sentence: *the instruction set
becomes firmware; the price is a memory in the critical path.*

### The numbers of the example machine

```
 control memory   128 × 20           CAR, SBR   7 bits
 microinstruction F1 F2 F3 CD BR AD  =  3 3 3 2 2 7
 mapping          opcode xxxx  →  0xxxx00
 allocation       16 routines × 4 words = 64,  + 64 for fetch/subroutines = 128
 machine          2048 × 16, 4-bit opcode, 11-bit address, 4 instructions
```

### Field sizing, in general

| Quantity | Bits |
|---|---|
| address field | ⌈log₂(control memory words)⌉ |
| microoperation subfield | ⌈log₂(operations + 1)⌉ — the +1 is NOP |
| condition select | ⌈log₂(status bits)⌉ |
| register field | ⌈log₂(registers)⌉ |

### The three rules that get asked as "explain"

1. **Three microoperations in one microinstruction** iff they come from three **different fields**.
2. **Mapping `0xxxx00`** — trailing zeros give room per routine; leading zero splits the memory in half.
3. **CDR raises the clock frequency** by overlapping microoperation execution with the next fetch.

---

## Attempt

1. `[Mano 7-2]` and `[7-3]` — the comparison and the definitions. These are the most likely exam items.
2. `[Mano 7-4]` the frequency numerical, both parts, with the parallel/serial reasoning shown.
3. `[Mano 7-5]`, `[7-6]` the two sizing questions.
4. `[Mano 7-7]`, `[7-8]` mapping.
5. `[Mano 7-11]`, `[7-12]` encode and decode — and say why 7-12(c) is impossible.
6. The fetch routine, symbolic and binary, from memory.
7. `[Mano 7-13]` INDR2.
8. `[Mano 7-21]` the control word; `[7-20]` the subfield split.
9. `[Mano 7-22]` the sequencer input logic.
10. Harder, if time: `[7-16]`, `[7-17]`, `[7-18]` — write microprogram routines for new instructions.

---

## Traps

| Trap | Correction |
|---|---|
| Using the Basic Computer's numbers in a ch. 7 question | Different machine: 2048 × 16, 4-bit opcode, 11-bit address, 128 × 20 control memory |
| Thinking U3 is not examined because no assignment asked | The hand-out puts the MTE divider after L19; U3 is L12–L15 |
| "Removing CDR makes it faster" | Slower — CDR is a pipeline register; it buys overlap |
| Putting two microoperations from the same field in one microinstruction | Impossible. A 3-bit field holds one value |
| Treating mapping as a lookup table | It is wiring: `0xxxx00` |
| Forgetting the +1 for NOP when sizing a subfield | k bits give 2ᵏ − 1 operations **plus** NOP |
| Letting a microsubroutine call another | SBR is one register — one level only |
| Thinking any ROM in a control unit makes it microprogrammed | What makes it microprogrammed is CAR **sequencing through stored microinstructions** |

---

## Self-test

1. Give the control-memory address for opcode 0111 under Mano's mapping.
2. Why is the microinstruction 20 bits and not 19 or 21? Justify every field.
3. A control memory is 512 × 26 with a 12-bit microoperation field and one address field. How many
   bits remain, and what are they for?
4. Convert `CLRAC, INCDR, SHR` to a 9-bit microoperation field — or say why you cannot.
5. Why does the fetch routine end with MAP rather than JMP?
6. With CDR removed, which delays must be summed?
7. Name the four address-sequencing capabilities.

---
---

## Answers

**Check 1.** (a) Hardwired: from **gate outputs**, the sums of D·T products you derived in file 08.
Microprogrammed: from **bits of a control word read out of ROM**. (b) **Hardwired** — a gate delay
versus a memory access. (c) Because the cost of a rich ISA is only more control memory and more
microcode, rather than a combinatorial explosion of special-case gate equations.

**Check 2.** (a) It splits the loop into two stages that run **in parallel**: the current
microinstruction's microoperations execute while the next one's address is generated and fetched.
(b) The **fetch path** (40 + 10 + 40 + 10 = 100 ns), which is longer than the 40 ns of
microoperations. (c) The **pipeline register** — because that is exactly what it is.

**Check 3.** (a) **11 bits** — its memory is 2048 = 2¹¹ words. (b) **Four**: ADD, BRANCH, STORE,
EXCHANGE. (c) The **ch. 7 example machine** — the Basic Computer has no CAR at all.

**Check 4.** (a) 0110 → `0 0110 00` = **24**. (b) **Four words**, because the two trailing zeros leave
addresses n, n+1, n+2, n+3 free before the next routine's base. (c) 2048 = 2¹¹ → 11-bit address;
8 words per routine → **3** trailing zeros; opcode is 6 bits; 11 − 6 − 3 = **2 leading zeros**. So the
address is `00 xxxxxx 000`, putting 64 routines × 8 words = 512 words in the low half and leaving
1536 for fetch and subroutines.

**Check 5.** (a) Control memory is 128 = 2⁷ words, so an address needs 7 bits. (b) 4096 = 2¹² → CAR is
**12 bits**; each of the four MUX inputs is an address, so **12 bits** each; one MUX per address bit →
**12 multiplexers**, each **4-to-1**. (c) **Horizontal**: one bit per control signal — wide word, no
decoding, full parallelism. **Vertical**: encoded fields — compact word, needs decoders, and only one
operation per field at a time.

**Check 6.** (a) CLRAC is F1 = 010, READ is F2 = 100, INCPC is F3 = 101 → **010 100 101**.
(b) Both are **F2** (SUB = 001, READ = 100), and a 3-bit field holds one value. (c) Three
microoperations fit in one microinstruction **iff they come from three different fields**.

**Check 7.** (a) Because BR = MAP takes the next address from the opcode wiring, so the AD field is
unused. (b) **READ** (F2 = 100) and **INCPC** (F3 = 101) — different fields, decoded in parallel.
(c) Because addresses 0–63 are reserved for the 16 instruction routines by the `0xxxx00` mapping; the
upper 64 words hold fetch and the shared subroutines.

**Check 8.** (a) **CAR + 1**, into **SBR**. (b) Because SBR is a single register — a second CALL would
overwrite the first return address. (c) Call **only if DR(15) = 1**, i.e. only when the instruction is
indirect — a conditional call in one microinstruction.

**Check 9.** (a) Because RET and MAP are unconditional by definition: RET always takes SBR, MAP always
takes the opcode wiring. (b) **L loads SBR** with CAR + 1; it is 1 exactly on a **taken CALL**
(`I′₁I₀T`). (c) **Which status bit to test** — 1, I, S or Z — under the CD field, producing T.

**Check 10.** (a) 32 registers = 2⁵, so A, B and D become 5 bits each: 5 + 5 + 5 + 5 + 3 = **23 bits**.
(b) A k-bit subfield gives 2ᵏ − 1 operations plus NOP. Try **5 + 4 bits**: (2⁵ − 1) + (2⁴ − 1) =
31 + 15 = **46** ✓, using all 9 bits. So two subfields, and therefore **2 microoperations** can be
specified in one microinstruction. (Three equal 3-bit subfields would give only 7 + 7 + 7 = 21.)

**Self-test 1.** 0111 → `0 0111 00` = **28**.

**Self-test 2.** F1, F2, F3 = 3 each (8 codes: 7 operations + NOP) = 9; CD = 2 (four conditions U, I,
S, Z); BR = 2 (four types JMP, CALL, RET, MAP); AD = 7 (128-word control memory). 9 + 2 + 2 + 7 = **20**.

**Self-test 3.** 512 = 2⁹ → address field 9 bits. 26 − 12 − 9 = **5 bits**, for the condition select
and branch-type fields.

**Self-test 4.** CLRAC = F1 010, INCDR = F2 110, SHR = F3 100 → **010 110 100**. All three are in
different fields, so it is legal.

**Self-test 5.** Because after fetch the machine must jump to the routine for **whichever instruction
was just read** — the address depends on the opcode, which is what MAP wires in. A JMP would need a
fixed address.

**Self-test 6.** All four in series: **40 (generate) + 10 (CAR) + 40 (ROM) + 40 (microoperations) =
130 ns**. The 10 ns CDR transfer disappears with the register.

**Self-test 7.** Increment CAR · conditional/unconditional branch · mapping from opcode to routine
address · subroutine call and return.

---

## What to do next

File 10 finishes U3 with its **program control** half — status bits C, S, Z, V, conditional branching,
and why signed comparison uses S ⊕ V while unsigned uses C. That material is Mano chapter 8, not
chapter 7, and it is where the overflow rule from file 04 becomes a hardware flag.
