# 05 — Timing & Control, the Instruction Cycle, MRI, Input–Output and Interrupt

**U2, lectures L9–L11 · CO2.** The densest file in the pack. The fetch sequence and the seven MRI
microoperation sequences are the canonical exam items of this unit everywhere the subject is taught.

---

## Map

```
   TIMING & CONTROL
      IR(12-14) -> 3x8 decoder -> D0..D7      (which opcode)
      IR(15)    -> I flip-flop               (direct or indirect)
      IR(0-11)  -> B0..B11 straight to gates (one-hot RRI/IO fields)
      SC (4-bit) -> 4x16 decoder -> T0..T15  (which time step)
        |
        |  EVERY control signal = a sum of D.T products
        v
   INSTRUCTION CYCLE
      T0  fetch address    T1  fetch instruction + PC++    T2  decode
        |
        +-- T3 splits four ways on (D7, I)
        |      D'7 I  T3 -> indirect: AR <- M[AR]
        |      D'7 I' T3 -> nothing (AR already holds EA)
        |      D7  I' T3 -> execute register-reference
        |      D7  I  T3 -> execute input-output
        v
      T4 onward: the 7 memory-reference instructions
        |
        v
   INTERRUPT: R <- 1 only when T'0 T'1 T'2 (IEN)(FGI + FGO)
              then RT0 RT1 RT2  = BSA done by hardware, to location 0
```

---

## Attempt first

1. What two hardware pieces turn an opcode into a *timed* pattern of control signals?
2. Why is PC incremented at T₁ rather than at the end of the instruction?
3. At T₃ the machine takes one of four paths. What decides which?
4. Why does memory-reference execution start at T₄ and not earlier?
5. Write the microoperation sequence for `ADD`.
6. `BSA 135` sits at location 20. Trace exactly what ends up where, and say what the return
   instruction must be.
7. In `T′₀T′₁T′₂(IEN)(FGI + FGO): R ← 1`, what are the primes doing? Answer with a mechanism, not a
   restatement.

---

## Method

### Timing and control — the hardwired control unit

Four pieces and nothing else:

| Piece | Feeds | Produces |
|---|---|---|
| **3×8 decoder** | IR bits 12–14 | **D₀ … D₇** — which opcode |
| **I flip-flop** | IR bit 15 | direct / indirect |
| **direct wires** | IR bits 0–11 | **B₀ … B₁₁** — the one-hot RRI/IO fields, no decoder needed |
| **4-bit sequence counter → 4×16 decoder** | the clock | **T₀ … T₁₅** — which time step |

**SC increments on every clock**, generating T₀, T₁, T₂, …, and is **cleared** to end an instruction
and begin the next fetch — e.g. `D₃T₄: SC ← 0`.

**★ This is the mechanism of instruction execution.** Every control signal in the machine is a **sum
of products of D's and T's** (plus I, R and Bᵢ). "How does the computer know what to do next?" has a
literal answer: *whatever gates are enabled by the current D·T combination.* And "why is it a
sequence at all?" also has one: *because SC increments.*

### Fetch and decode

```
   T₀:  AR ← PC
   T₁:  IR ← M[AR],  PC ← PC + 1
   T₂:  D₀…D₇ ← decode IR(12-14),  AR ← IR(0-11),  I ← IR(15)
```

Read as hardware (file 02's discipline):

| Step | Bus select | Loads asserted |
|---|---|---|
| T₀ | PC (010) | LD(AR) |
| T₁ | memory (111) | LD(IR), INR(PC) |
| T₂ | IR (101) | LD(AR) — and the decoder output is just combinational |

**Why PC increments at T₁.** Its old value was already copied into AR at T₀, so PC is free. Doing it
early means PC points at the *next* instruction by the time an instruction that saves a return
address runs — which is precisely what makes BSA work.

**Note that `PC ← PC + 1` does not use the bus** — it uses PC's own incrementer. That is why two
things happen at T₁ without conflict.

### Determining the instruction type at T₃

Four mutually exclusive paths:

| Condition | Action |
|---|---|
| `D′₇ I T₃` | `AR ← M[AR]` — indirect: fetch the effective address |
| `D′₇ I′ T₃` | nothing (direct MRI — AR already holds EA from T₂) |
| `D₇ I′ T₃` | execute a **register-reference** instruction (this condition is called **r**) |
| `D₇ I T₃` | execute an **input–output** instruction (this condition is called **p**) |

**Memory-reference execution begins at T₄** because by the end of T₃ the effective address is in AR
**either way** — directly from T₂, or through the indirect fetch. The two paths converge, which is
exactly why one T₄-onward sequence serves both modes.

### The seven memory-reference instructions

| Symbol | D | Operation |
|---|---|---|
| AND | D₀ | AC ← AC ∧ M[AR] |
| ADD | D₁ | AC ← AC + M[AR], E ← Cₒᵤₜ |
| LDA | D₂ | AC ← M[AR] |
| STA | D₃ | M[AR] ← AC |
| BUN | D₄ | PC ← AR |
| BSA | D₅ | M[AR] ← PC, PC ← AR + 1 |
| ISZ | D₆ | M[AR] ← M[AR] + 1, and if the result is 0 then PC ← PC + 1 |

**The microoperation sequences — the exam item. Learn these as sequences, not as lines.**

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

**Three patterns worth seeing rather than memorizing:**

1. **Every instruction ends with `SC ← 0`** — that is what returns the machine to T₀ for the next
   fetch. An answer without it is incomplete.
2. **AND, ADD and LDA share `D T₄: DR ← M[AR]`** — you cannot operate on a memory word until it is
   in a register. Three instructions, one first step.
3. **STA and BUN take one clock; ISZ takes three.** The length is set by how many *bus transfers* are
   required, not by how complicated the instruction sounds.

⚠ **The deck prints ISZ's third line as `D₆T₄`. It is `D₆T₆`** — the same deck's own "Complete
Computer Description" slide gives D₆T₆, and a single instruction cannot have two different actions at
the same time step. Write **D₆T₆**.

### BSA — the one students get wrong

**What it does:** store the **return address** (PC, which already points *past* the call) into the
word at EA, then jump to **EA + 1**.

```
   before:  location 20 holds  BSA 135        PC = 21 at T₄ (already incremented)

   D₅T₄:  M[135] ← 21          AR ← 136
   D₅T₅:  PC ← 136             SC ← 0

   after:  M[135] = 21   (the return address slot)
           PC     = 136  (the subroutine's first instruction)

   return:  1 BUN 135     ->   indirect BUN:  PC ← M[135] = 21
```

So a subroutine's **first word is its return-address slot**, and its code starts one word later. The
return instruction is an **indirect BUN** through EA.

⚠ **Why BSA needs two clock periods and not one.** The symbolic description `M[AR] ← PC, PC ← AR + 1`
looks like one line, but the second half needs the **bus** to carry AR into PC, and the first half is
already using the bus to carry PC to memory. **The single bus serializes what the notation writes as
one statement.** A symbolic one-liner is not a one-cycle operation.

**ISZ** is the loop-counter instruction: increment a memory location, and if it wraps to 0, skip the
next instruction. Counting **up to zero** rather than down from n is deliberate — the zero test is
free.

### Input–output instructions

INPR (8 bits) and OUTR (8 bits) talk to the terminal **serially** and to AC **in parallel**. **FGI**
and **FGO** are 1-bit flags; **IEN** enables interrupts.

**Why the flags exist:** to synchronize the timing difference between the device and the computer.
The device and the CPU run at wildly different speeds; the flag is the handshake.

**Programmed I/O (polling):**

```
   /* input, FGI initially 0 */        /* output, FGO initially 1 */
   loop: if FGI = 0 goto loop          loop: if FGO = 0 goto loop
         AC ← INPR, FGI ← 0                  OUTR ← AC, FGO ← 0
```

In BC assembly: `LOOP, SKI DEV / BUN LOOP / INP DEV`.
**Cost:** continuous CPU involvement — the CPU is slowed to the device's speed. Simplest hardware,
most wasted time. This is rung 1 of the ladder U5 climbs (ETE material).

**The six I/O instructions** (with **p = D₇IT₃** and **Bᵢ = IR(i)**):

```
      p:    SC ← 0
INP   pB₁₁: AC(0-7) ← INPR,  FGI ← 0
OUT   pB₁₀: OUTR ← AC(0-7),  FGO ← 0
SKI   pB₉ : if (FGI = 1) then (PC ← PC + 1)
SKO   pB₈ : if (FGO = 1) then (PC ← PC + 1)
ION   pB₇ : IEN ← 1
IOF   pB₆ : IEN ← 0
```

### The interrupt

**Setting the interrupt flip-flop R:**

> **`T′₀ T′₁ T′₂ (IEN)(FGI + FGO):  R ← 1`**

Read it term by term — this is a favourite exam item:

| Term | What it demands |
|---|---|
| `T′₀ T′₁ T′₂` | **none** of T₀, T₁, T₂ is active — the current instruction is past fetch and decode |
| `IEN` | interrupts are enabled |
| `(FGI + FGO)` | some device flag is set — there is actually something to service |

**The primes are how "finish the current instruction first" is implemented in hardware.** There is no
rule written anywhere saying the CPU should complete the instruction; the condition simply cannot be
satisfied during the fetch/decode steps. Atomicity by construction.

**The interrupt cycle.** Fetch and decode are modified to `R′T₀, R′T₁, R′T₂`, so they run only when
R = 0. When R = 1:

```
   RT₀:  AR ← 0,  TR ← PC
   RT₁:  M[AR] ← TR,  PC ← 0
   RT₂:  PC ← PC + 1,  IEN ← 0,  R ← 0,  SC ← 0
```

**The mechanism, in one sentence:** the interrupt cycle is a **hardware implementation of
branch-and-save-return-address** — it is BSA, done by hardware, to the fixed location 0.

- The return address goes to **M[0]**.
- Control resumes at **address 1**, where the programmer must have placed a branch to the service
  routine.
- **IEN is cleared** so the service routine is not itself interrupted.
- Return is **`BUN 0` indirect** — the same return mechanism as BSA.

Note the role of **TR**: PC must be saved while AR is being cleared in the *same* clock, and the
single bus cannot do both, so PC is parked in TR at RT₀ and written to memory at RT₁.

---

## Worked — write the complete sequence for `ISZ`, indirect (inferred form F8; sequences from Mano)

> **Give every microoperation executed for an indirect `ISZ`, from fetch to completion, with timing.**

Full credit needs **fetch, decode, the indirect phase, and execution** — most answers give only the
execution.

```
   R′T₀:      AR ← PC
   R′T₁:      IR ← M[AR],  PC ← PC + 1
   R′T₂:      D₀…D₇ ← decode IR(12-14),  AR ← IR(0-11),  I ← IR(15)
   D′₇ I T₃:  AR ← M[AR]                       ← the indirect phase; AR now holds EA
   D₆T₄:      DR ← M[AR]
   D₆T₅:      DR ← DR + 1
   D₆T₆:      M[AR] ← DR,  if (DR = 0) then (PC ← PC + 1),  SC ← 0
```

**Seven clock periods.** Say why each phase exists:

- T₀–T₂: you cannot execute an instruction you have not fetched and decoded.
- T₃: because I = 1, the address field was a **pointer**, so one extra memory read converts it to the
  effective address. A direct ISZ would simply do nothing at T₃ and cost one clock less.
- T₄–T₆: read the counter word, increment it in DR, write it back — **three separate bus transfers,
  hence three clocks.**
- `SC ← 0` returns the machine to T₀.

**The skip:** `PC ← PC + 1` is conditional on the *incremented* value in DR being zero. Since PC was
already incremented at T₁, a second increment makes the machine skip the instruction immediately
following the ISZ — which is how the loop exit is written.

---

## Worked — trace an interrupt (inferred form F10; transfers from Mano)

> **The CPU is executing an instruction at location 255 when an input device raises FGI. IEN = 1.
> Show what happens, step by step, and give the memory picture before and after.**

**Step 1 — when R is set.** Not immediately. The condition `T′₀T′₁T′₂(IEN)(FGI + FGO)` can only be
satisfied once the current instruction is past T₂, so the machine **finishes the instruction at 255
first**. PC is by then **256**.

**Step 2 — the interrupt cycle runs:**

```
   RT₀:  AR ← 0,  TR ← PC        (TR = 256; AR = 0)
   RT₁:  M[0] ← TR,  PC ← 0      (M[0] = 256)
   RT₂:  PC ← PC + 1 = 1,  IEN ← 0,  R ← 0,  SC ← 0
```

**Step 3 — the memory picture:**

```
                 before                         after
        0    +-------------+            0   +-------------+
             |      -      |                |     256     |  <- return address
        1    |  BUN 1120   |            1   |  BUN 1120   |  <- branch to the service routine
       ...                                 ...
      255    | instruction |          255   | instruction |
      256    |  next inst  |          256   |  next inst  |
       ...                                 ...
     1120    | service     |         1120   | service     |  <- PC goes here via the BUN at 1
             | routine     |                | routine     |
             |    ...      |                |    ...      |
             | BUN 0  (I=1)|                | BUN 0  (I=1)|  <- return: PC ← M[0] = 256
```

**Step 4 — the three sentences that carry the marks:**

- The return address is saved to **location 0**, and execution resumes at **location 1**, which the
  programmer must have loaded with a branch to the service routine.
- **IEN is cleared** at RT₂ so that the service routine cannot itself be interrupted.
- The return is an **indirect BUN through 0**, which is the same mechanism BSA uses — the interrupt
  cycle *is* a hardware BSA to a fixed address.

---

## Traps

| # | Trap | The correction |
|---|---|---|
| T3 | BSA in one clock | **Two**: D₅T₄ (write PC to memory, increment AR) then D₅T₅ (PC ← AR). The single bus forces it |
| T4 | ISZ's write-back at T₄ | **D₆T₆.** The deck's typo; its own summary slide contradicts it |
| — | Omitting `SC ← 0` | It is what ends the instruction. Without it the machine runs on into T₆, T₇, … |
| T5 | Reading `T′₀T′₁T′₂` as "at T₀, T₁, T₂" | The primes mean **not** — the interrupt is recognized only *outside* fetch/decode. That is the atomicity mechanism |
| M10 | "The interrupt is serviced the instant the flag is set" | The flag only makes R *eligible* to be set; the current instruction finishes first |
| — | Writing the execution phase only | A full-credit MRI answer includes fetch (T₀–T₂), the T₃ decision, then execution |
| — | Forgetting that indirect costs a clock | `D′₇IT₃: AR ← M[AR]` is a whole extra memory access |
| — | Thinking the interrupt return address is in a register | It is in **M[0]**; the return is `BUN 0` **indirect** |

---

## Self-test

1. Write the fetch and decode phase with its timing, then say what is on the bus at each step.
2. Why can `IR ← M[AR]` and `PC ← PC + 1` happen in the same clock, when `M[AR] ← PC` and `PC ← AR + 1`
   cannot?
3. Give the full microoperation sequence for a **direct** `BSA`, and say how many clock periods the
   whole instruction takes including fetch.
4. What are the four possible actions at T₃, and what selects among them?
5. `ADD` and `STA` both reference memory, yet one takes two clocks in execution and the other one.
   Explain from the datapath.
6. State the condition that sets R and explain each of its three terms.
7. A subroutine is called with `BSA 300`. At which address does its first *executable* instruction
   sit, and what instruction returns from it?
8. Write the sequence for register-reference `CIR` given r = D₇I′T₃ and B₇, and say why no decoder is
   needed for the B bits.

---

## Answers

**1.**
```
   T₀:  AR ← PC                              bus carries PC      (S₂S₁S₀ = 010)
   T₁:  IR ← M[AR],  PC ← PC + 1             bus carries memory  (111)
   T₂:  decode IR(12-14) → D₀…D₇,            bus carries IR      (101)
        AR ← IR(0-11),  I ← IR(15)
```
The decode itself is combinational — the 3×8 decoder's outputs follow IR continuously; T₂ is when
AR and I capture.

**2.** Because `PC ← PC + 1` uses **PC's own incrementer** and never touches the bus, so it can run
alongside a bus transfer. In BSA, **both** halves need the bus: `M[AR] ← PC` puts PC on the bus for
memory to write, and `PC ← AR + 1` needs AR on the bus to reach PC. Two bus transfers cannot share
one clock. **The test is always "how many transfers want the bus?", not "how many statements are on
the line?"**

**3.**
```
   R′T₀:      AR ← PC
   R′T₁:      IR ← M[AR],  PC ← PC + 1
   R′T₂:      decode,  AR ← IR(0-11),  I ← IR(15)
   D′₇I′T₃:   (nothing — direct mode, AR already holds EA)
   D₅T₄:      M[AR] ← PC,  AR ← AR + 1
   D₅T₅:      PC ← AR,  SC ← 0
```
**Six clock periods** (T₀ through T₅) — T₃ is consumed even though nothing happens in it, because the
sequence counter still advances.

**4.** `D′₇IT₃`: indirect fetch `AR ← M[AR]`. `D′₇I′T₃`: nothing. `D₇I′T₃` (= r): execute a
register-reference instruction. `D₇IT₃` (= p): execute an input–output instruction.
**What selects:** the decoder output **D₇** (is the opcode 111?) together with the **I flip-flop**.

**5.** `STA` writes AC to memory: AC drives the bus, memory's write line is asserted — **one transfer,
one clock**, done at D₃T₄. `ADD` must first bring the operand into a register (`DR ← M[AR]` at D₁T₄,
one transfer) and only then can the adder-and-logic circuit compute AC + DR and load AC (D₁T₅) — the
ALU's inputs are registers, never memory. **Two transfers, two clocks.** The general rule: the BC can
compute only on register contents, so any memory operand costs an extra clock to fetch.

**6.** `T′₀T′₁T′₂(IEN)(FGI + FGO): R ← 1`.
`T′₀T′₁T′₂` — the current instruction is past fetch/decode, so it will not be torn in half (atomicity).
`IEN` — interrupts have been enabled by the program (`ION`); a program can protect a critical section
with `IOF`.
`(FGI + FGO)` — at least one device flag is set, so there is genuinely something to service.

**7.** `BSA 300` stores the return address in **M[300]** and sets PC to **301**, so the first
executable instruction is at **301**. The return is `BUN 300` with **I = 1** (indirect), i.e. the hex
form `D300`, which loads PC with M[300].

**8.** `rB₇:  AC ← cir AC,  E ← AC(0),  AC(15) ← E` — a circular right shift of the 17-bit chain
formed by AC and E, together with `SC ← 0` (asserted by r itself for all register-reference
instructions).
**No decoder is needed** because the 12 low-order bits of a register-reference instruction are
**one-hot**: exactly one of B₀…B₁₁ is 1, so each bit *is* its own instruction-select line and can be
ANDed with r directly. Encoding chosen to make the hardware free.
