# 11 — Drill Set: a 30-mark timed paper

⚠ **This is not a past paper. No ECE2108 paper exists.** It is a drill built from the inferred question
forms in `../knowledge-base/exam-map.md` §4 (F1–F17), weighted by the hand-out's lecture counts and CO
targets. Use it to **rehearse the forms**, not to predict the paper.

**The structure is borrowed** from the sibling MUJ ECE2102 mid-term (3 × 2 "memory based" + 4 × 4
"concept based" + 1 × 8 "analytical" = 30 marks). That is a *different course and examiner* — the
hand-out fixes only the **30 marks** and the **U1–U4 scope**. Treat the section split as a plausible
shape, not a promise.

---

## How to run this

**Closed book. 90 minutes. Write full answers, not notes.**

Then mark yourself against the solutions at the bottom — **after** finishing, not question by
question.

**3 minutes per mark** is the budget the structure implies. Section C alone is a 24-minute answer:
if you have never written an 8-mark design answer under time pressure, that is the single most
valuable thing in this file.

Score honestly and route the result:

| Score | What to do next |
|---|---|
| **≥ 24 / 30** | spaced review only — redo the missed items in 3 days |
| **18–23** | redo the files behind each lost mark, then re-sit Drill B below |
| **< 18** | files 02, 05, 06 and 10 in full before re-drilling — those four carry most of the paper |

---

# DRILL A

## Section A — Memory based (3 × 2 = 6 marks)

**A1. (2)** The Basic Computer has a memory of 4096 × 16. Derive the number of opcode bits in its
instruction format, showing the arithmetic.

**A2. (2)** State which Flynn class has no extant machine, and give the standard one-line statement
about it.

**A3. (2)** Write the two microoperations of the fetch phase with their timing (T₀, T₁).

---

## Section B — Concept based (4 × 4 = 16 marks)

**B1. (4)** Distinguish computer architecture from computer organization in a table of at least four
points, and give one concrete example of two machines that share an architecture but not an
organization.

**B2. (4)** Give the complete microoperation sequence for **BSA** with timing, explain with a memory
before/after sketch what it does, and state how a subroutine called this way returns.

**B3. (4)** A 4-stage pipeline has a clock period of 20 ns. A non-pipelined unit performs the same task
in 80 ns. Compute the total time and the speedup for 100 tasks. State the theoretical maximum speedup
and explain the gap.

**B4. (4)** Decode the microinstruction `110 100 101 00 00 1000010` using the F1/F2/F3/CD/BR/AD format
(3-3-3-2-2-7). State every microoperation it performs and the next value of CAR.

---

## Section C — Analytical based (1 × 8 = 8 marks)

**C1. (8)** Design a 4-bit **arithmetic logic shift unit**. Draw one stage, give the function table of
the arithmetic circuit, give the logic-circuit selection table, state the total number of operations
with the derivation, and **explain its working in detail** — including why the propagation delay does
not depend on the operation selected.

---
---

# DRILL B — a second paper, same structure

Sit this only after marking Drill A.

## Section A (3 × 2 = 6)

**A4. (2)** State the condition that sets the interrupt flip-flop R in the Basic Computer, and explain
what the primed T terms achieve.

**A5. (2)** Give the arithmetic-shift-left overflow test for an n-bit register, and apply it to
R = 0110.

**A6. (2)** Name the four address-sequencing capabilities a microprogram sequencer must provide.

## Section B (4 × 4 = 16)

**B5. (4)** Derive **LD(AR)**, **CLR(AR)** and **INR(AR)** for the Basic Computer by scanning its
register-transfer statements. List the statements you used.

**B6. (4)** Explain the mapping of a 4-bit opcode to the control-memory address `0xxxx00`. Why two
trailing zeros? Why the leading zero? Show that the arithmetic closes against a 128-word control
memory.

**B7. (4)** A floating-point adder pipeline has segment delays 60, 70, 100 and 80 ns with an interface
register delay of 10 ns. Find the pipeline clock period, the non-pipelined time, and the speedup for a
large number of operations. Explain why the speedup is not 4.

**B8. (4)** For each pair, identify the hazard class and give a cure with its mechanism:
(i) `ADD R1, R2, R3` then `SUB R4, R1, R5`;
(ii) an instruction fetch and an operand fetch colliding on a single-port memory;
(iii) a conditional branch followed by the next sequential instruction.

## Section C (1 × 8 = 8)

**C2. (8)** Write the **complete microoperation sequence for an indirect ISZ**, from fetch to
completion, with timing. Explain the purpose of each phase, state how many clock periods the
instruction takes, and explain how the "skip" is actually implemented in hardware.

---
---
---

# SOLUTIONS

*Stop here until you have written both papers.*

---

## Drill A — Section A

**A1. (2)** 4096 = 2¹², so an address needs **12 bits**. The instruction word is 16 bits and one bit
is the addressing-mode bit I. Therefore opcode bits = **16 − 12 − 1 = 3**.
*(Full marks need the arithmetic, not the number.)*

**A2. (2)** **MISD.** *"There is no computer at present that can be classified as MISD"* — it is of
theoretical interest only. **Do not supply an example.**

**A3. (2)**
```
   T₀:  AR ← PC
   T₁:  IR ← M[AR],  PC ← PC + 1
```
*(Strictly `R′T₀` and `R′T₁` — the prime excludes the interrupt cycle. Writing the primes is worth
saying you know why.)*

---

## Drill A — Section B

**B1. (4)**

| | Architecture | Organization |
|---|---|---|
| Question answered | **what** the computer does | **how** it does it |
| Deals with | functional behaviour | structural relationship |
| Also called | instruction set architecture (ISA) | microarchitecture |
| Comprises | instruction set, registers, data types, addressing modes | buses, adders, control logic, peripherals |
| Design order | comes first | comes after |

**Example:** the Intel 8086 and a modern Core i9 share an **architecture** — a binary compiled for one
runs on the other, because both honour the same contract of instructions, registers and addressing
modes. Their **organizations** differ completely: caches, pipelines, out-of-order execution and
multiple cores exist in one and not the other. One architecture, many organizations.

*Marking note:* the table alone is about 2 of the 4 marks. The example and the sentence explaining
*why* the split exists (the ISA is a contract; organization is any implementation that keeps it) carry
the rest.

---

**B2. (4)**

```
   D₅T₄:  M[AR] ← PC,  AR ← AR + 1
   D₅T₅:  PC ← AR,  SC ← 0
```

**What it does** — `BSA 135` at location 20, with PC already incremented to 21 during fetch:

```
        before                        after
   135  |     -     |            135  |    21     |   <- return address saved here
   136  | first     |            136  | first     |   <- PC now points here
        | subroutine|                 | subroutine|
        | instruction|                | instruction|
```

So BSA stores the **return address** into the word at EA and jumps to **EA + 1**. A subroutine's first
word is its return-address slot; its code begins one word later.

**Return:** an **indirect BUN through EA** — `1 BUN 135` (hex `D135`), which loads PC with M[135] = 21.

**Say why it takes two clock periods:** both halves need the **common bus** — PC must drive the bus for
the memory write, and AR must drive it to reach PC — and the bus carries one value per clock.

---

**B3. (4)**

```
   non-pipelined:  n·tₙ           = 100 × 80             = 8000 ns
   pipelined:      (k + n − 1)·tₚ = (4 + 100 − 1) × 20  = 103 × 20 = 2060 ns
   speedup:        S = 8000 / 2060                      = 3.88
```

**Theoretical maximum = k = 4.**

**The gap:** the pipeline must **fill** — the first task needs all 4 segments, so 103 clock periods
are required for 100 tasks rather than 100. As n grows the fill cost is amortized (n = 1000 gives
S = 3.99) but k is never reached. In a real machine three further causes keep it lower still:
**unequal segment delays** (the clock is set by the slowest), the **interface register delay tᵣ**
included in tₚ, and **hazards**.

---

**B4. (4)**

```
    F1    F2    F3   CD   BR      AD
   110   100   101   00   00   1000010
```

| Field | Code | Symbol | Microoperation |
|---|---|---|---|
| F1 | 110 | PCTAR | AR ← PC |
| F2 | 100 | READ | DR ← M[AR] |
| F3 | 101 | INCPC | PC ← PC + 1 |

**Three microoperations in one microinstruction** — legal because they occupy three different fields,
which are decoded independently and in parallel.

**Sequencing:** CD = 00 = **U** (unconditional, condition = 1); BR = 00 = **JMP**.
Therefore **CAR ← AD = 1000010** (= 66 decimal).

*(A sharp answer adds: PCTAR writes AR while READ uses AR, so this particular combination is only
meaningful if the hardware's timing allows it — the fields are independent, which is not the same as
every combination being sensible.)*

---

## Drill A — Section C

**C1. (8)** Six parts. Allocate roughly 1 mark each to (1), (2), (4) and (6), and 2 each to (3) and
(5).

**(1) Specification.** A 4-bit ALSU performing 14 operations on two 4-bit operands A and B under four
select lines S₃S₂S₁S₀ plus a carry input Cᵢₙ.

**(2) One stage of the circuit:**

```
             +----------------------+
   Ai --+--->|  arithmetic circuit  |--> Di --+
   Bi --+    |  (FA + 4-to-1 MUX)   |         |      +---------+
        |    +----------------------+         +----->| 4-to-1  |
        |    +----------------------+         |      |  MUX    |--> Fi
        +--->|    logic circuit     |--> Ei --+      | S1 S0   |
             +----------------------+         |      +---------+
   Ai+1 --------- shift right input ----------+           ^
   Ai-1 --------- shift left  input ----------+           |
                                                     S3 S2 select
```

**This stage is replicated four times**, one per bit; all four share the select lines, and the carry
ripples from stage i to stage i+1.

**(3) The arithmetic circuit.** One full adder per bit. X = Aᵢ. **Y is the output of a 4-to-1 MUX**
selecting Bᵢ, Bᵢ′, 0 or 1 under S₁S₀. Cᵢₙ enters stage 0.

| S₁ | S₀ | Cᵢₙ | Y | Output D | Microoperation |
|---|---|---|---|---|---|
| 0 | 0 | 0 | B | A + B | add |
| 0 | 0 | 1 | B | A + B + 1 | add with carry |
| 0 | 1 | 0 | B′ | A + B′ | subtract with borrow |
| 0 | 1 | 1 | B′ | A + B′ + 1 | subtract |
| 1 | 0 | 0 | 0 | A | transfer A |
| 1 | 0 | 1 | 0 | A + 1 | increment A |
| 1 | 1 | 0 | 1 | A − 1 | decrement A |
| 1 | 1 | 1 | 1 | A | transfer A |

*(The last two rows use the identity "all 1s = −1 in 2's complement".)*

**(4) The logic circuit** — four gates per bit, selected by S₁S₀:

| S₁ | S₀ | Eᵢ | Operation |
|---|---|---|---|
| 0 | 0 | Aᵢ ∧ Bᵢ | AND |
| 0 | 1 | Aᵢ ∨ Bᵢ | OR |
| 1 | 0 | Aᵢ ⊕ Bᵢ | XOR |
| 1 | 1 | Aᵢ′ | complement A |

**(5) The output multiplexer and the operation count.** The 4-to-1 output MUX takes Dᵢ (arithmetic),
Eᵢ (logic), Aᵢ₊₁ (shift right) and Aᵢ₋₁ (shift left) under S₃S₂:

| S₃S₂ | Block selected | Operations |
|---|---|---|
| 00 | arithmetic | **8** |
| 01 | logic | **4** |
| 10 | shift right | **1** |
| 11 | shift left | **1** |
| | | **14 total** |

**Derive the 14 — do not assert it.** 8 + 4 + 1 + 1, where the 8 comes from S₁S₀ plus Cᵢₙ (three bits)
and the 4 from S₁S₀ alone.

**(6) Explanation of working.**

> All four blocks receive A and B and produce their results **simultaneously and continuously**. S₃S₂
> drives the output multiplexer, which admits exactly one of those results to F; S₁S₀ and Cᵢₙ choose
> the operation *within* the arithmetic or logic block. Nothing is decided before computing — the
> unselected blocks compute too, and their outputs are discarded. **The propagation delay is therefore
> the worst-case path through the slowest block plus the output MUX** — in practice the ripple-carry
> adder, whose carry must propagate through all four stages — **and it does not depend on which
> operation was requested.**

---

## Drill B — Section A

**A4. (2)** `T′₀ T′₁ T′₂ (IEN)(FGI + FGO):  R ← 1`.
The **primed T terms mean none of T₀, T₁, T₂ is active**, i.e. the current instruction is past fetch
and decode. That is how "finish the current instruction before servicing an interrupt" is implemented
— atomicity by construction, not by a rule written anywhere.

**A5. (2)** Overflow on `ashl` occurs when **V = Rₙ₋₁ ⊕ Rₙ₋₂ = 1**, evaluated **before** the shift.
For R = 0110: R₃ ⊕ R₂ = 0 ⊕ 1 = **1 → overflow**. Check: 0110 = +6, and `ashl` gives 1100 = **−4**,
not +12 (which is outside the 4-bit range −8…+7).

**A6. (2)** (1) **Increment CAR** (in-line); (2) **conditional or unconditional branch**;
(3) **mapping** the opcode to the address of its routine; (4) **subroutine call and return** via SBR.

---

## Drill B — Section B

**B5. (4)** *Statements that change AR:*

```
   R′T₀:     AR ← PC
   R′T₂:     AR ← IR(0-11)
   D′₇IT₃:   AR ← M[AR]
   RT₀:      AR ← 0
   D₅T₄:     AR ← AR + 1
```

*Sorted by control input:*

```
   LD(AR)  = R′T₀ + R′T₂ + D′₇IT₃
   CLR(AR) = RT₀
   INR(AR) = D₅T₄
```

**State the method explicitly for the last mark:** scan every register-transfer statement in the
complete machine description that changes the register, and OR their control conditions, sorted by
which control input each uses. Note that `R′T₀` (fetch) and `RT₀` (interrupt cycle) share a time step
but are mutually exclusive machine states — the prime is load-bearing.

---

**B6. (4)** The mapping is pure wiring: the 4-bit opcode `xxxx` becomes the 7-bit control-memory
address **`0 xxxx 00`**.

```
   0000 -> 0 0000 00 =  0
   0001 -> 0 0001 00 =  4
   0010 -> 0 0010 00 =  8
```

**Two trailing zeros:** they space consecutive routines **4 words apart**, giving each routine
addresses n, n+1, n+2, n+3 before the next begins.
**Leading zero:** it confines all routines to the **lower half** of control memory.

**The arithmetic:** a 4-bit opcode gives **16 routines**; 16 × 4 = **64 words**, occupying addresses
0–63, i.e. exactly the lower half. The **upper 64** words hold the fetch routine and shared
microsubroutines. 64 + 64 = **128**, which is the control memory's size — and 128 = 2⁷ is why AD is
7 bits. **The numbers were designed together.**

---

**B7. (4)**

```
   tₚ = max(60, 70, 100, 80) + tᵣ = 100 + 10 = 110 ns   <- the SLOWEST segment sets the clock
   tₙ = 60 + 70 + 100 + 80 + 10              = 320 ns
   S  = tₙ / tₚ = 320 / 110                  = 2.9
```

**Why not 4:** the segments are **unequal**. The 100 ns segment forces a 110 ns clock, so the 60 ns
segment idles for 50 ns of every cycle. A k-segment pipeline reaches k only when the segments are
balanced *and* tₙ = k·tₚ; neither holds here. The improvement that matters is **rebalancing the
segments**, not adding more of them.

---

**B8. (4)**

| | Hazard | Cure and mechanism |
|---|---|---|
| (i) | **Data hazard** — SUB needs R1 before ADD has written it back | **Forwarding**: a data path routes ADD's ALU output directly to SUB's ALU input, bypassing the register file, so the value is available a stage earlier. Alternatives: a hardware **interlock** that stalls, or **compiler scheduling** that moves independent work between them |
| (ii) | **Structural hazard** — one memory port, two claimants in the same clock | **Duplicate the resource**: a two-port memory, or separate instruction and data memories (**Harvard**), or split I-cache and D-cache |
| (iii) | **Control hazard** — the next address is unknown until the branch resolves | Any one of: **prefetch both streams** · **branch target buffer** (associative memory of past branch targets, searched at fetch) · **loop buffer** · **branch prediction** · **delayed branch** (the compiler fills the delay slot with a useful instruction). Name the mechanism, not just the term |

---

## Drill B — Section C

**C2. (8)** **The complete sequence, fetch through completion:**

```
   R′T₀:      AR ← PC
   R′T₁:      IR ← M[AR],  PC ← PC + 1
   R′T₂:      D₀…D₇ ← decode IR(12-14),  AR ← IR(0-11),  I ← IR(15)
   D′₇ I T₃:  AR ← M[AR]
   D₆T₄:      DR ← M[AR]
   D₆T₅:      DR ← DR + 1
   D₆T₆:      M[AR] ← DR,  if (DR = 0) then (PC ← PC + 1),  SC ← 0
```

**Purpose of each phase:**

| Steps | Why it exists |
|---|---|
| T₀–T₂ | you cannot execute an instruction you have not fetched and decoded. T₀ puts the address in AR, T₁ brings the instruction in and advances PC, T₂ decodes and extracts the address field |
| T₃ | because **I = 1**, the address field was a **pointer**; one extra memory read converts it into the effective address. A direct ISZ does nothing here and costs one clock less |
| T₄–T₆ | read the counter word into DR, increment it, write it back — **three separate bus transfers, hence three clocks**. The bus carries one value per clock |
| `SC ← 0` | clears the sequence counter, ending the instruction and returning the machine to T₀ |

**Clock periods: 7** (T₀ through T₆).

**How the skip is implemented:** there is **no skip hardware**. PC was already incremented during
fetch (T₁), so it points at the instruction following the ISZ. The conditional `PC ← PC + 1` at T₆ is
a **second increment**, which makes PC point one further on — so the instruction immediately after the
ISZ is never fetched. **A skip is an extra increment of the program counter.** Every skip instruction
in the machine (SPA, SNA, SZA, SZE, SKI, SKO) works exactly this way.

⚠ **Write `D₆T₆`, not `D₆T₄`.** The professor's Unit-2 deck contains that typo; its own "Complete
Computer Description" slide gives D₆T₆, and one instruction cannot have two different actions at the
same time step.

---

## Marking sheet

| Q | Marks | Yours | File to revisit if lost |
|---|---|---|---|
| A1 | 2 | | 04 |
| A2 | 2 | | 09 |
| A3 | 2 | | 05 |
| B1 | 4 | | 01 |
| B2 | 4 | | 05 |
| B3 | 4 | | 10 |
| B4 | 4 | | 07 |
| C1 | 8 | | 03 |
| **Drill A total** | **30** | | |
| A4 | 2 | | 05 |
| A5 | 2 | | 03 |
| A6 | 2 | | 07 |
| B5 | 4 | | 06 |
| B6 | 4 | | 07 |
| B7 | 4 | | 10 |
| B8 | 4 | | 10 |
| C2 | 8 | | 05 |
| **Drill B total** | **30** | | |
