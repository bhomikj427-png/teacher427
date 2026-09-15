# 09 — Pipelining: Register Tables, Clock Cycles, Speedup, Branch Hardware

**Assignment 2: Q11, Q12, Q13, Q14, Q15 · 50 of 150 marks · U4 (L17–L19)**
Source problems: Mano 9-1, 9-3, 9-5, 9-10, 9-11.

A2 answer policy: method + fully worked twin here; A2's own key after 16-09-2026 16:30.

---

## Map

```
   Arithmetic pipeline                       Instruction pipeline
   (one expression, stream of data)          (stream of instructions)
        │                                         │
        ▼                                         ▼
   segment = register + combinational      FI · DA · FO · EX  (4 segments)
        │                                         │
        ▼                                         ▼
   register-content table              which instruction is in which segment at step t
        │                                         │
        └────────────► timing ◄───────────────────┘
                   k + n − 1 cycles
                   tₚ = slowest segment
                   S = n·tₙ / ((k+n−1)·tₚ),  Sₘₐₓ = tₙ/tₚ
                          │
                          ▼
                   branches break it → 4 hardware fixes (+ 1 software)
```

---

## Attempt

**A2 Q11.** Compute (Aᵢ + Bᵢ)(Cᵢ + Dᵢ) on a stream of numbers. Specify a pipeline configuration. List
the contents of all registers for i = 1 to 6.

**A2 Q12.** How many clock cycles to process 200 tasks in a six-segment pipeline?

**A2 Q13.** A three-segment pipeline computes (Aᵢ × Bᵢ) + Cᵢ, i = 1…6. R1–R5 load on every clock.
Delays: 40 ns to read operands from memory into R1 and R2; 45 ns through the multiplier; 5 ns for the
transfer into R3; 15 ns to add into R5.
(a) Minimum clock cycle? (b) Non-pipelined time per operation, with R3 and R4 removed?
(c) Speedup for 10 tasks and for 100 tasks? (d) Maximum speedup?

**A2 Q14.** Explain four hardware schemes that reduce the performance loss from branching in an
instruction pipeline.

**A2 Q15.** Four instructions in a four-segment pipeline, the first starting at step 1:
```
   LOAD    R1 ← M[312]
   ADD     R2 ← R2 + M[313]
   INC     R3 ← R3 + 1
   STORE   M[314] ← R3
```
What operation is performed in each of the four segments during **step 4**?

---

## Learn

### Designing an arithmetic pipeline

1. **Segment 1** loads every input operand into its own register.
2. Each later segment does **one** operation level of the expression; operations at the same level
   run **in parallel** in the same segment.
3. A value needed later but not used in this segment is **carried forward** in a register.
4. Registers: one per value alive at each segment boundary.

**Register table rules:** at clock t, segment 1 holds item t; segment s holds item t − s + 1; empty
("—") before the item arrives and after the stream ends. The table has **k + n − 1** rows.

### Clock cycles

```
   first task:        k cycles
   each later task:   1 cycle
   total:             k + n − 1
```

### Speedup numericals

| Quantity | How to get it |
|---|---|
| **tₚ** (pipeline clock) | the **slowest segment's** total delay, including the register it loads |
| **tₙ** (non-pipelined time per task) | sum of the combinational delays **with the intermediate registers removed** |
| Pipelined time, n tasks | (k + n − 1)·tₚ |
| Non-pipelined time, n tasks | n·tₙ |
| **S** | n·tₙ / ((k + n − 1)·tₚ) |
| **Sₘₐₓ** (n → ∞) | tₙ / tₚ |
| Sₘₐₓ if tₙ = k·tₚ | k |

**S < k in real problems** because segments are unequal (the clock waits for the slowest) and the
pipeline must fill.

**Two ways problems state delays — read which one you have:**

| Given as | tₚ | tₙ | Example |
|---|---|---|---|
| each delay already **includes** loading its register (A2 Q13 style) | largest segment total | sum of the delays, minus the transfers into registers that are removed | Mano 9-5: tₚ = 45 + 5 = 50, tₙ = 40 + 45 + 15 = 100 |
| combinational delays tᵢ **plus a separate register delay tᵣ** | max(tᵢ) + tᵣ | Σtᵢ + tᵣ (the unpipelined circuit keeps one register) | Mano's FP adder: tₚ = 100 + 10 = 110, tₙ = 60 + 70 + 100 + 80 + 10 = 320 |

### Instruction pipeline: FI · DA · FO · EX

| Segment | Job |
|---|---|
| FI | fetch the instruction |
| DA | decode it and calculate the effective address |
| FO | fetch the operand from memory |
| EX | execute |

**At step t, instruction j is in segment t − j + 1** (if 1 ≤ t − j + 1 ≤ 4). Some instructions have
nothing to do in FO (e.g. INC — no memory operand); the segment is still occupied for that step.

```
   step →        1    2    3    4    5    6    7
   instr 1       FI   DA   FO   EX
   instr 2            FI   DA   FO   EX
   instr 3                 FI   DA   FO   EX
   instr 4                      FI   DA   FO   EX
```

### Branch handling — four hardware schemes (+ one software)

| Scheme | Mechanism |
|---|---|
| **Prefetch target instruction** | fetch both the next sequential instruction and the branch target; keep both until the branch resolves, then use the right one |
| **Branch target buffer (BTB)** | an **associative memory** in the fetch segment holding previously executed branch addresses with their target instructions (and the next few). On fetch, search it: hit → take the target from the BTB immediately; miss → fetch normally and store the new entry |
| **Loop buffer** | a small, very fast register file that holds an entire program loop; the loop runs from the buffer without repeated memory access |
| **Branch prediction** | extra logic guesses taken/not-taken (from history) and fetches speculatively; a right guess costs nothing, a wrong one flushes |
| *Delayed branch* — **software** | the compiler places useful instructions (or no-ops) after the branch so they execute regardless; used in RISC. Not one of the "hardware" four |

---

## Worked twins

**Twin of Q11 — compute Aᵢ × Bᵢ + Cᵢ, i = 1…5.**

Configuration (k = 3):
```
   Segment 1:   R1 ← Aᵢ,   R2 ← Bᵢ                   load
   Segment 2:   R3 ← R1 × R2,   R4 ← Cᵢ              multiply; Cᵢ carried forward
   Segment 3:   R5 ← R3 + R4                          add
```

```
        Aᵢ     Bᵢ          Cᵢ
        │      │           │
      ┌─▼─┐  ┌─▼─┐         │
      │R1 │  │R2 │         │
      └─┬─┘  └─┬─┘         │
        └─[×]──┘           │
          │                │
        ┌─▼─┐            ┌─▼─┐
        │R3 │            │R4 │
        └─┬─┘            └─┬─┘
          └──────[+]───────┘
                  │
                ┌─▼─┐
                │R5 │
                └───┘
```

| Clock | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| 1 | A1 | B1 | — | — | — |
| 2 | A2 | B2 | A1B1 | C1 | — |
| 3 | A3 | B3 | A2B2 | C2 | A1B1 + C1 |
| 4 | A4 | B4 | A3B3 | C3 | A2B2 + C2 |
| 5 | A5 | B5 | A4B4 | C4 | A3B3 + C3 |
| 6 | — | — | A5B5 | C5 | A4B4 + C4 |
| 7 | — | — | — | — | A5B5 + C5 |

k + n − 1 = 3 + 5 − 1 = **7 rows** ✓.

For A2 Q11: note that (Aᵢ + Bᵢ)(Cᵢ + Dᵢ) has **two additions at the same level** — they share a segment.
Count the segments and registers before drawing the table.

**Twin of Q12.** 4-segment pipeline, 100 tasks → 4 + 100 − 1 = **103 cycles**.
Six-segment pipeline, 8 tasks → 6 + 8 − 1 = **13 cycles**:

```
   cycle →   1  2  3  4  5  6  7  8  9 10 11 12 13
   seg 1    T1 T2 T3 T4 T5 T6 T7 T8
   seg 2       T1 T2 T3 T4 T5 T6 T7 T8
   seg 3          T1 T2 T3 T4 T5 T6 T7 T8
   seg 4             T1 T2 T3 T4 T5 T6 T7 T8
   seg 5                T1 T2 T3 T4 T5 T6 T7 T8
   seg 6                   T1 T2 T3 T4 T5 T6 T7 T8
```

**Twin of Q13 — compute (Aᵢ + Bᵢ) × Cᵢ in three segments.** Delays: 30 ns to read Aᵢ, Bᵢ into R1, R2;
55 ns through the adder; 5 ns to transfer into R3; 40 ns through the multiplier into R5.

```
   Segment delays:
     seg 1 (read into R1, R2)          30 ns
     seg 2 (adder + transfer into R3)  55 + 5 = 60 ns
     seg 3 (multiplier into R5)        40 ns

   (a) tₚ = slowest segment = 60 ns

   (b) Non-pipelined: remove R3, R4 → the 5 ns register transfer disappears
       tₙ = 30 + 55 + 40 = 125 ns

   (c) k = 3
       n = 10:   S = 10 × 125 / ((3 + 10 − 1) × 60) = 1250 / 720  = 1.74
       n = 100:  S = 100 × 125 / ((3 + 100 − 1) × 60) = 12500 / 6120 = 2.04

   (d) Sₘₐₓ = tₙ / tₚ = 125 / 60 = 2.08
```

Why far below k = 3: the segments are unequal (30, 60, 40 ns) — the clock is set by the 60 ns segment
and the others idle.

**Twin of Q15 — five instructions, step 5.**
```
   1  LOAD   R4 ← M[500]
   2  SUB    R5 ← R5 − M[501]
   3  DEC    R6 ← R6 − 1
   4  STORE  M[502] ← R4
   5  ADD    R7 ← R7 + M[503]
```
At step 5: instruction j is in segment 5 − j + 1.

| Segment | Instruction | Operation during step 5 |
|---|---|---|
| EX | 2 (SUB) | compute R5 − (operand), store in R5 |
| FO | 3 (DEC) | no memory operand — segment idles for DEC |
| DA | 4 (STORE) | decode STORE, compute EA = 502 |
| FI | 5 (ADD) | fetch the ADD instruction from memory |

Instruction 1 (LOAD) completed its EX at step 4.

---

## Traps

| Trap | Correction |
|---|---|
| tₚ = average or sum of segment delays | tₚ = the **slowest** segment |
| tₙ including the pipeline register delay | Remove the registers the question removes; add only combinational delays |
| Q13-type: treating the 5 ns as a separate segment | It is part of segment 2's delay into R3 |
| k + n − 1 written as k·n | The first task takes k; each later task adds 1 |
| Sₘₐₓ = k always | k only if tₙ = k·tₚ. In delay problems Sₘₐₓ = tₙ/tₚ |
| Delayed branch listed as hardware | It is a compiler technique |
| Register table cut off when inputs stop | Keep going until the last result reaches the final register |
| Step t: counting from step 0 | Instruction j enters FI at step j |

---

## Self-test

1. How many cycles for 50 tasks in an 8-segment pipeline?
2. tₙ = 50 ns, k = 6, tₚ = 10 ns, n = 100. Speedup and maximum speedup?
3. Pipeline for (Aᵢ − Bᵢ) × Cᵢ + Dᵢ: how many segments, which registers carry values forward?
4. In the A2 Q15 program, at which step does STORE execute, and what is in DA at that step?
5. A BTB miss occurs on a branch that is taken. What does the pipeline do, and what is updated?

---
---

## Answers

**A2 Q11–Q15:** answer key added after 16-09-2026, 16:30. Send your answers for marking.

**Self-test 1.** 8 + 50 − 1 = **57**.

**Self-test 2.** S = 100 × 50 / ((6 + 99) × 10) = 5000 / 1050 = **4.76**; Sₘₐₓ = 50 / 10 = **5**
(here tₙ < k·tₚ = 60, so Sₘₐₓ < k).

**Self-test 3.** Four segments:
```
   1: R1 ← Aᵢ, R2 ← Bᵢ, R3 ← Cᵢ, R4 ← Dᵢ
   2: R5 ← R1 − R2,  R6 ← R3,  R7 ← R4        (Cᵢ, Dᵢ carried)
   3: R8 ← R5 × R6,  R9 ← R7                   (Dᵢ carried)
   4: R10 ← R8 + R9
```

**Self-test 4.** STORE is instruction 4: EX at step 4 + 3 = **7**. DA at step 7 holds instruction
7 − 2 + 1 = 6 — **none** (the program has 4 instructions), so DA is empty.

**Self-test 5.** Fetch proceeds with the sequential instruction; when the branch resolves as taken,
the wrongly fetched instructions are discarded and fetch restarts at the target. The branch address
and its target instruction are then **stored in the BTB**, so the next encounter is a hit.
