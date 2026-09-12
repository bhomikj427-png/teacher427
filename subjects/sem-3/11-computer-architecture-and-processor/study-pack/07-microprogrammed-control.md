# 07 — Microprogrammed Control: Control Memory, Address Sequencing, the Sequencer

**U3, lectures L12–L15 · CO2.** ⚠ **No slide deck exists for this unit.** It is built textbook-first
from Mano ch. 7, verified against three independent institutional reproductions that agree on every
field width and every table entry. The *emphasis* your instructor places here is therefore less
certain than for U1/U2/U4 — but the content is not.

---

## ⚠ Read this before anything else in the file

**Mano uses TWO different machines, and fusing them is the single most damaging error in this
subject.**

| | **U2's Basic Computer** (ch. 5) | **U3's microprogram example** (ch. 7) |
|---|---|---|
| Memory | **4096 × 16** | **2048 × 16** |
| Address bits | **12** | **11** |
| Opcode bits | **3** | **4** |
| Instruction format | I(1) + opcode(3) + address(12) | I(1) + opcode(4) + address(11) |
| AR, PC width | 12 | **11** |
| Control | **hardwired** | **microprogrammed**, control memory 128 × 20 |
| CAR, SBR | — | **7 bits each** |
| Instructions | **25** | **4** (ADD, BRANCH, STORE, EXCHANGE) |

**Symptom of the error:** trying to map the BC's **3-bit** opcode onto the `0xxxx00` scheme (which
needs 4 bits), or claiming the Basic Computer has a control memory. **Recite the right-hand column
before every U3 study session** until the two stop blurring.

---

## Map

```
   ONE JOB: turn an opcode into a timed pattern of control signals
        |
        +---------------------------+
        v                           v
   HARDWIRED                   MICROPROGRAMMED
   gates + sequence counter    control memory (ROM) + CAR + sequencer
   signals = sums of D.T       signals = BITS READ OUT OF A CONTROL WORD
   fast, rigid                 slower, rewritable
        |
        v  (the rest of this file)
   ADDRESS SEQUENCING - four capabilities:
        increment CAR | branch (cond.) | MAP opcode->routine | CALL/RET via SBR
        |
        v
   MICROINSTRUCTION:  F1(3) F2(3) F3(3) CD(2) BR(2) AD(7) = 20 bits
        |
        v
   THE SEQUENCER: MUX1 picks next address, MUX2 picks the status bit to test
                  S1 = I1,  S0 = I0I1 + I'1 T,  L = I'1 I0 T
```

---

## Attempt first

1. Give the one-sentence job of a control unit, then the two ways to build it.
2. Why is a microprogrammed control unit *slower* than a hardwired one? Name the component in the
   critical path.
3. A 4-bit opcode maps to the control-memory address `0xxxx00`. Why the two trailing zeros? Why the
   leading zero?
4. The microinstruction has three microoperation fields instead of one big one. What does that buy,
   and what is the restriction?
5. Write the fetch routine symbolically (three microinstructions).
6. In the sequencer's input-logic table, rows with I₁ = 1 show `x` in the T column. Why?
7. Control memory is 128 × 20. Which field's width does the 128 fix, and which does the 20 fix?

---

## Method

### Hardwired vs microprogrammed

| | **Hardwired** | **Microprogrammed** |
|---|---|---|
| Built from | combinational + sequential logic (decoders, sequence counter, gates) | a **control memory** (usually ROM) + CAR + sequencer |
| Control signals come from | gate outputs — sums of D·T products | **bits read out of a control word** |
| Speed | **fast** (one gate delay) | slower (a memory read per microinstruction) |
| Changing the instruction set | **redesign and rewire** | **rewrite the microprogram** |
| Cost of a complex ISA | grows badly | grows gently (just more control memory) |
| Typical user | RISC machines, simple fast controllers | CISC machines with rich instruction sets |
| U2's Basic Computer | **this one** | — |

**The real trade.** Hardwired control hard-codes the D·T equations in silicon: minimal delay, but the
design is a tangle of special cases and any ISA change forces a re-derivation of every equation
(file 06's scan, redone). Microprogramming replaces that tangle with a **lookup**: each machine
instruction gets a **routine** of microinstructions in ROM, and the control signals are simply bits in
the word you just read. **The instruction set becomes firmware.** The cost is one control-memory
access per microinstruction — you have put a memory in the critical path.

> *"The main advantage of the microprogrammed control is the fact that once the hardware
> configuration is established, there should be no need for further hardware or wiring changes."*
>
> And the bridge to U8: *"Most computers based on the reduced instruction set computer (RISC)
> architecture concept use **hardwired control** rather than a control memory with a microprogram."*

**Vocabulary — every one of these is worth a definition mark:**

| Term | Definition |
|---|---|
| **Control word** | a string of 1s and 0s representing the control variables |
| **Microinstruction** | a control word stored in control memory |
| **Microprogram** | a sequence of microinstructions |
| **Control memory** | the memory (usually ROM) holding microprograms |
| **Routine** | the group of microinstructions implementing **one machine instruction** |
| **CAR** | Control Address Register — holds the address of the next microinstruction |
| **CDR** | Control Data Register (pipeline register) — holds the microinstruction just read |
| **SBR** | Subroutine Register — holds the return address for microsubroutines |
| **Microprogram sequencer** | the next-address generator |

**On the CDR:** it lets the *current* microinstruction's microoperations execute **at the same time**
as the *next* microinstruction's address is generated and fetched — pipelining inside the control
unit. The control unit can work without a CDR, at lower speed.

**Writable control store (dynamic microprogramming):** if control memory is writable rather than ROM,
the microprogram — and hence the machine's instruction set — can be changed by a systems programmer.
Rare in practice, conceptually striking, and the ancestor of today's "microcode update".

### Address sequencing — the four capabilities

Getting from one microinstruction to the next needs exactly four things:

1. **Increment CAR** — the in-line case, the common one.
2. **Conditional or unconditional branch** — on a status bit.
3. **Mapping** from the instruction's opcode to the address of its routine.
4. **Subroutine call and return** — via SBR.

**The flow for one machine instruction:**

```
   power on / previous instruction done
              |
              v
   load CAR with the FETCH routine's address
              |
              v
   FETCH routine runs (brings the instruction in, updates PC)
              |
              v
   MAP:  opcode --> the address of that instruction's routine --> CAR
              |
              v
   the routine runs (CAR increments; may branch on a status bit; may CALL a shared subroutine)
              |
              v
   return to FETCH
```

### Mapping — where the `0xxxx00` comes from

Rather than store a lookup table, the mapping is **pure wiring**: a **4-bit opcode `xxxx` becomes the
7-bit control-memory address `0xxxx00`.**

```
   opcode        control-memory address
   0000  ADD  ->  0 0000 00  =   0
   0001  AND  ->  0 0001 00  =   4
   0010  LDA  ->  0 0010 00  =   8
   0011  ...  ->  0 0011 00  =  12
```

**Why the two trailing zeros:** they leave each routine **4 words** (addresses n, n+1, n+2, n+3)
before the next routine starts.
**Why the leading zero:** it confines all 16 routines to the **first 64 words**, leaving the **upper
64** for the fetch routine and shared microsubroutines.

> **16 routines × 4 words = 64 words; 64 + 64 = the 128-word control memory.**

The numbers are designed together. That sentence is the answer to "explain the mapping function".

### The microinstruction format — 20 bits

```
+--------+--------+--------+------+------+-----------+
|   F1   |   F2   |   F3   |  CD  |  BR  |    AD     |
+--------+--------+--------+------+------+-----------+
|   3    |   3    |   3    |  2   |  2   |     7     |   = 20 bits
+--------+--------+--------+------+------+-----------+
 F1,F2,F3 : microoperation fields     CD : condition for branching
 BR       : branch field              AD : address field
```

**Why these widths** — every one is derivable, so derive it rather than recall it:

- **AD is 7 bits** because control memory is **128 = 2⁷** words.
- Each **F field is 3 bits** because it selects one of **8** microoperations (including "none").
- **CD and BR are 2 bits** each = 4 conditions and 4 branch types.

**★ Why three microoperation fields and not one.** F1, F2 and F3 are decoded **independently and in
parallel** by three 3×8 decoders, so **up to three microoperations can be specified in a single
microinstruction** — provided they come from *different* fields and do not conflict. The fields are
grouped so that operations which could sensibly happen together sit in different fields. This is
**vertical** microprogramming (encoded fields, compact); the alternative, **horizontal**, gives one
bit per control signal — wide, but fully parallel.

**F1:**

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

**F2:**

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

**F3:**

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

**CD — the condition field:**

| CD | Condition | Symbol | Meaning |
|---|---|---|---|
| 00 | always = 1 | **U** | unconditional |
| 01 | DR(15) | **I** | indirect-address bit |
| 10 | AC(15) | **S** | sign bit of AC |
| 11 | AC = 0 | **Z** | AC is zero |

**BR — the branch field:**

| BR | Symbol | Function |
|---|---|---|
| 00 | **JMP** | if condition = 1: CAR ← AD; else CAR ← CAR + 1 |
| 01 | **CALL** | if condition = 1: CAR ← AD **and SBR ← CAR + 1**; else CAR ← CAR + 1 |
| 10 | **RET** | CAR ← SBR |
| 11 | **MAP** | CAR(2-5) ← DR(11-14), CAR(0,1,6) ← 0 |

**MAP is where the `0xxxx00` wiring lives:** the opcode bits DR(11-14) drop into CAR bits 2–5 and
bits 0, 1, 6 are forced to 0 — producing exactly `0 xxxx 00`.

**Symbolic format:** `Label:  Micro-ops  CD  BR  AD`, where Micro-ops is one to three symbols
separated by commas, CD ∈ {U, I, S, Z}, BR ∈ {JMP, CALL, RET, MAP}, and AD is a symbolic address,
`NEXT`, or empty.

### The fetch routine

**What fetch must do:** read the instruction from memory, get its address field into AR, update PC,
and jump to the right routine.

```
   AR ← PC
   DR ← M[AR],  PC ← PC + 1
   AR ← DR(0-10),  CAR(2-5) ← DR(11-14),  CAR(0,1,6) ← 0
```

**Symbolically** (placed at address 64, the start of the upper half):

```
         ORG 64
FETCH:   PCTAR            U   JMP   NEXT
         READ, INCPC      U   JMP   NEXT
         DRTAR            U   MAP
```

**In binary** (address, then F1 F2 F3 CD BR AD):

```
 1000000   110  000  000   00   00   1000001
 1000001   000  100  101   00   00   1000010
 1000010   101  000  000   00   11   0000000
```

**Read the middle line as the proof of the three-field design:** F2 = 100 (**READ**: DR ← M[AR]) and
F3 = 101 (**INCPC**: PC ← PC + 1) execute in the **same microinstruction**, because they occupy
different fields. The third line uses BR = 11 (**MAP**), so AD is irrelevant and shown as zeros — the
next address comes from the opcode.

**Microsubroutine — INDRCT.** The indirect-address fetch is needed by several routines, so it is
written once and reached with CALL:

```
INDRCT:  READ             U   JMP   NEXT
         DRTAR            U   RET
```

A routine calls it *conditionally on the indirect bit*: `ADD:  NOP   I   CALL   INDRCT`.
**CD = I** means "call only if DR(15) = 1" — a conditional subroutine call in one microinstruction.

### Design of the control unit

**(a) The microoperation decoders.** F1, F2, F3 each drive a **3×8 decoder** → 24 outputs, of which
the 21 non-NOP ones are control signals. Signals from different fields that drive the same thing are
**OR-ed**: `AR ← PC` is asserted by **PCTAR** (F1 = 110) and `AR ← DR(0-10)` by **DRTAR** (F1 = 101),
so AR's load input is PCTAR + DRTAR and a multiplexer chooses between PC and DR(0-10) as the source.
**This is file 06's scan, applied to decoder outputs instead of D·T products.**

**(b) The microprogram sequencer** — computes the next CAR value. Components: **two multiplexers, an
incrementer, CAR, SBR, and input logic.**

- **MUX1** selects the next address from: **CAR + 1** (in-line), **AD** (branch), **SBR** (return), or
  the external **MAP** value.
- **MUX2** selects **which status bit to test**, under the **CD** field: 1 (unconditional), I, S, or Z.
  Its output is the **test value T**.

**The input logic** — with I₁I₀ = the BR field and T = the tested condition:

| I₁ I₀ T | Meaning | Source of address | S₁S₀ | L |
|---|---|---|---|---|
| 0 0 0 | in-line | CAR + 1 | 00 | 0 |
| 0 0 1 | JMP | CS(AD) | 01 | 0 |
| 0 1 0 | in-line | CAR + 1 | 00 | 0 |
| 0 1 1 | CALL | CS(AD), and SBR ← CAR + 1 | 01 | **1** |
| 1 0 × | RET | SBR | 10 | 0 |
| 1 1 × | MAP | DR(11-14) | 11 | 0 |

From which:

```
   S₁ = I₁
   S₀ = I₀I₁ + I′₁T
   L  = I′₁I₀T          (L = load SBR, i.e. this is a taken CALL)
```

**Read the table as a mechanism:** when I₁ = 0 (JMP or CALL) the branch is **taken only if T = 1**, so
the T = 0 rows fall through to CAR + 1. When I₁ = 1 (RET or MAP) the condition is irrelevant — which
is exactly what the `×` entries say, and why those two operations are unconditional.

---

## Worked — decode a binary microinstruction (inferred form F12; format from Mano ch. 7)

> **The control word `101 100 101 01 01 1000011` is read from control memory. State every
> microoperation it performs and what the next CAR value will be.**

**Step 1 — split it by the format.** Always write the field widths above the bits before doing
anything else:

```
    F1    F2    F3   CD   BR      AD
   101   100   101   01   01   1000011
    3     3     3    2    2       7
```

**Step 2 — look up the microoperation fields.**

| Field | Code | Symbol | Microoperation |
|---|---|---|---|
| F1 | 101 | DRTAR | AR ← DR(0-10) |
| F2 | 100 | READ | DR ← M[AR] |
| F3 | 101 | INCPC | PC ← PC + 1 |

**Three microoperations in one microinstruction** — legal, because they come from three different
fields.

⚠ **But say the caveat**, because it is the discriminating remark: DRTAR writes AR from DR while READ
reads memory *using* AR. Whether that is meaningful depends on the hardware's timing — the fields are
independent, which is not the same as the operations being sensible in every combination. A
microprogrammer is responsible for choosing combinations that make sense.

**Step 3 — the sequencing half.** CD = 01 = **I** → the condition tested is **DR(15)**, the
indirect-address bit. BR = 01 = **CALL**.

```
   if DR(15) = 1:   CAR ← AD = 1000011 (= 67 decimal)   and   SBR ← CAR + 1
   if DR(15) = 0:   CAR ← CAR + 1        (the call is not taken)
```

**Step 4 — name it.** This is a **conditional microsubroutine call on the indirect bit** — the
standard way a routine invokes the shared INDRCT subroutine only when the instruction was indirect.

---

## Worked — encode a symbolic microprogram to binary (inferred form F12)

> **Encode this routine into binary:**
>
> ```
> ADD:   NOP     I   CALL   INDRCT
>        READ    U   JMP    NEXT
>        ADD     U   JMP    FETCH
> ```
>
> **Placement (Mano's standard):** ADD's routine begins at control-memory address `0000000`,
> `FETCH` is at `1000000` (= 64) and `INDRCT` at `1000011` (= 67).

**Line 1: `ADD: NOP I CALL INDRCT`** at address `0000000`.

- No microoperation → F1 = F2 = F3 = **000**.
- CD = **I** = **01**. BR = **CALL** = **01**. AD = INDRCT = **1000011**.

```
   0000000   000 000 000  01  01  1000011
```

**Line 2: `READ U JMP NEXT`** at address `0000001`.

- READ is in **F2** → F2 = **100**; F1 = F3 = 000.
- CD = **U** = 00. BR = **JMP** = 00. AD = NEXT = the following address = **0000010**.

```
   0000001   000 100 000  00  00  0000010
```

**Line 3: `ADD U JMP FETCH`** at address `0000010`.

- ADD is in **F1** → F1 = **001**; F2 = F3 = 000.
- CD = 00, BR = 00 (JMP), AD = FETCH = **1000000**.

```
   0000010   001 000 000  00  00  1000000
```

**The three habits this question is testing:**

1. **Know which field each symbol lives in.** READ is F2, ADD is F1, INCPC is F3 — a symbol placed in
   the wrong field is simply a different instruction.
2. **`NEXT` means "the address after this one"**, so it is written out as an explicit binary address,
   not as a special code.
3. **A microinstruction with no microoperation is normal.** Line 1 does nothing but decide whether to
   call INDRCT — its entire purpose is sequencing.

---

## Traps

| # | Trap | The correction |
|---|---|---|
| M7 | **Fusing the two machines** | BC: 4096×16, 3-bit opcode, hardwired, 25 instructions. Microprogram example: 2048×16, 4-bit opcode, control memory 128×20, 4 instructions |
| — | "Microprogrammed control is better" | It is **slower** — a memory read sits in the critical path. It is better only for *flexibility* and for *complex* instruction sets |
| — | Quoting `0xxxx00` without explaining it | The two trailing zeros give 4 words per routine; the leading zero confines 16 routines to the lower 64 words. 64 + 64 = 128 |
| — | Saying three microoperations can *always* be combined | Only from **different fields**, and only if they do not conflict. Two F1 operations in one microinstruction is impossible by construction |
| — | Forgetting that AD is meaningless under MAP and RET | Under MAP the address comes from the opcode; under RET it comes from SBR |
| — | Deriving S₀ as just `T` | `S₀ = I₀I₁ + I′₁T`. The first term is what makes MAP (I₁I₀ = 11) work |
| — | Calling the CDR essential | The control unit works without it, at lower speed. It exists to overlap execution with the next fetch |

---

## Self-test

1. Give four differences between hardwired and microprogrammed control, and say which one the Basic
   Computer uses.
2. Control memory is 128 × 20. Derive the width of AD and explain what the 20 is spent on.
3. A machine has a **5-bit** opcode and wants 8 words per routine in a control memory of 512 words.
   Design the mapping function (give the address pattern) and check the arithmetic.
4. Decode `000 000 000 10 00 1010101`. What does it do?
5. Write the fetch routine symbolically, then say exactly which two microoperations run in parallel
   and why they are allowed to.
6. Why does CALL need SBR when JMP does not? What limits how deeply microsubroutines can nest in this
   design?
7. Derive S₁, S₀ and L from the I₁I₀T table, and explain in words what L = 1 means.
8. A designer proposes replacing F1/F2/F3 (9 bits) with a single 21-bit horizontal field, one bit per
   control signal. What is gained, what is lost?

---

## Answers

**1.** Any four of: gates + sequence counter vs control memory + CAR + sequencer · signals as sums of
D·T products vs bits read from a control word · fast (gate delay) vs slower (a memory read per
microinstruction) · change by rewiring vs change by rewriting the microprogram · cost grows badly vs
gently with ISA complexity · typical of RISC vs typical of CISC.
**The Basic Computer is hardwired.**

**2.** 128 = 2⁷, so a control-memory address is **7 bits** → AD = 7 bits. The 20 bits are spent as
**3 + 3 + 3** (three microoperation fields, 8 codes each including NOP) **+ 2** (CD, four conditions)
**+ 2** (BR, four branch types) **+ 7** (AD) = 20.

**3.** 5-bit opcode → **32 routines**. 8 words each → 32 × 8 = **256 words** for the routines, leaving
512 − 256 = **256** for fetch and shared subroutines. 512 = 2⁹ → **9-bit** control-memory address.
8 words per routine → **3 trailing zeros**. 32 routines in the lower half → **1 leading zero**.

```
   opcode xxxxx  ->  address  0 xxxxx 000
                              1 +  5  + 3  = 9 bits
```
Check: the largest routine address is `0 11111 000` = 248, and the next routine would start at 256 —
exactly the boundary. The arithmetic closes.

**4.** F1 = F2 = F3 = **000** → **no microoperation**. CD = **10** = **S** → test AC(15), the sign bit.
BR = **00** = **JMP**, AD = `1010101` (= 85).
So: **if AC is negative (AC(15) = 1), CAR ← 85; otherwise CAR ← CAR + 1.** It is a pure conditional
branch on sign — which is exactly the body of the example machine's BRANCH instruction.

**5.**
```
FETCH:   PCTAR            U   JMP   NEXT
         READ, INCPC      U   JMP   NEXT
         DRTAR            U   MAP
```
The parallel pair is **READ (DR ← M[AR])** and **INCPC (PC ← PC + 1)** in the second
microinstruction. They are allowed because READ is encoded in **F2** and INCPC in **F3** — different
fields, decoded independently by different 3×8 decoders, so both control signals are asserted in the
same clock. Two operations from the *same* field could never be combined: the field holds one 3-bit
code.

**6.** JMP throws away the current address, so nothing needs saving. CALL must come back, so the
**return address CAR + 1 is saved in SBR** and RET restores it. Because **SBR is a single register**,
not a stack, **microsubroutines cannot nest**: a second CALL overwrites the first return address.
(This is the same limitation BSA has at the machine-instruction level — and the same reason real
machines use a stack; see file 08.)

**7.** From the table:
- `S₁` is 1 exactly in the rows where I₁ = 1 (RET → 10, MAP → 11), so **S₁ = I₁**.
- `S₀` is 1 in the JMP-taken row (I₁I₀T = 001), the CALL-taken row (011), and the MAP row (11×), which
  gives **S₀ = I₀I₁ + I′₁T**.
- `L` is 1 only in the CALL-taken row (I₁ = 0, I₀ = 1, T = 1), so **L = I′₁I₀T**.

**L = 1 means "this is a CALL whose condition came out true"** — the one situation in which SBR must
be loaded with CAR + 1 so that a later RET can come back.

**8.** *Gained:* full parallelism — any combination of the 21 control signals can be asserted in one
microinstruction, including several that the F1/F2/F3 grouping forbids, so routines get shorter and
the machine can be faster. *Lost:* **width**. Every microinstruction now costs 21 + 2 + 2 + 7 = 32
bits instead of 20, so the control memory is ~60% larger for the same number of microinstructions, and
most of those bits are 0 in any given word. This is the **horizontal vs vertical** trade: horizontal
buys parallelism with control-store area; vertical buys density by encoding, at the cost of forbidding
some combinations.
