# 06 — Design of the Basic Computer and of the Accumulator Logic

**U2, lectures L9–L11 · CO2.** ★ **This file is a skill, not a list.** A learner who can recite all 25
instructions but cannot perform the scan below has memorized U2 and understood none of it — and the
scan is what a "design" question actually asks for.

---

## Map

```
   THE COMPLETE COMPUTER DESCRIPTION  (every RTL statement the machine can execute)
        |
        |   THE SCAN:  for one register X, find EVERY statement that changes X,
        |              then OR their control conditions together
        v
   +---------------------+-------------------------+------------------------+
   | statements that     | statements that set     | statements that        |
   | LOAD X from the bus | X to zero               | INCREMENT X            |
   |     -> LD(X)        |     -> CLR(X)           |     -> INR(X)          |
   +---------------------+-------------------------+------------------------+
        |
        +--> same method for a FLIP-FLOP: J = (statements that set it)
        |                                 K = (statements that clear it)
        |
        +--> same method for the BUS: x_i = (statements that put source i on the bus)
        |
        v
   AC IS THE EXCEPTION: its input comes from the ADDER-AND-LOGIC CIRCUIT, not the bus
```

---

## Attempt first

1. State the design method in one sentence, without an example.
2. Which register-transfer statements in the whole machine change **AR**? List them before reading
   on.
3. From that list, write LD(AR), CLR(AR) and INR(AR).
4. IEN is set by `pB₇`, cleared by `pB₆` and cleared by `RT₂`. If IEN is a JK flip-flop, what are J
   and K?
5. Why can AC's control not be derived exactly the same way as AR's?
6. The encoder that drives the bus select lines has an input meaning "put AR on the bus". Which
   statements activate it?

---

## Method

### The hardware inventory (say this first in a "design the BC" answer)

| Category | Items |
|---|---|
| Memory | 4096 × 16 |
| Registers | AR, PC, DR, AC, IR, TR, OUTR, INPR, SC |
| Flip-flops | I, S, E, R, IEN, FGI, FGO |
| Decoders | a **3×8** opcode decoder (D₀–D₇), a **4×16** timing decoder (T₀–T₁₅) |
| Interconnect | a **16-bit common bus** |
| Logic | control-logic gates, and an **adder-and-logic circuit** attached to AC |

### ★ The design method

> **Scan every register-transfer statement in the complete machine description that changes a given
> register, and OR their control conditions together.**

That is the entire method. It produces a Boolean equation per control input, and those equations
*are* the control unit.

**Worked for AR** — the deck's own example:

```
   R′T₀:     AR ← PC          ┐
   R′T₂:     AR ← IR(0-11)    ├──►  LD(AR) = R′T₀ + R′T₂ + D′₇IT₃
   D′₇IT₃:   AR ← M[AR]       ┘

   RT₀:      AR ← 0           ────►  CLR(AR) = RT₀

   D₅T₄:     AR ← AR + 1      ────►  INR(AR) = D₅T₄
```

Three things to notice, because each is a mark:

1. **The primes on R matter.** `R′T₀` is the *fetch* at T₀; `RT₀` is the *interrupt cycle* at T₀.
   Same time step, mutually exclusive machine states. Dropping the prime merges two different
   behaviours.
2. **One statement can only contribute to one control input.** `AR ← AR + 1` is an increment, not a
   load — it goes to INR, never to LD.
3. **Missing a statement is the standard way to lose this question** (trap T6). Work from the
   complete description systematically, not from memory of "the ones I remember".

**The same method for a flip-flop.** A flip-flop has no LD/CLR; it has J and K:

```
   pB₇:  IEN ← 1     ──►  J = pB₇
   pB₆:  IEN ← 0     ┐
   RT₂:  IEN ← 0     ├──►  K = pB₆ + RT₂
```

**The same method for the bus.** The bus select lines come from an encoder; each encoder input means
"put source i on the bus", and it is the OR of every statement that needs that source. For example,
PC is loaded **from AR** in `D₄T₄` (BUN) and `D₅T₅` (BSA), so the encoder input for *select AR onto
the bus* is

> **x₁ = D₄T₄ + D₅T₅**

### Design of the accumulator logic

**Why AC is different.** AC's input does **not** come from the common bus. It comes from the
**adder-and-logic circuit**, whose inputs are **AC, DR and INPR** — so AC's control includes not only
LD/CLR/INR but also *which function* the adder-and-logic circuit should perform.

**All the statements that change AC** (with **r = D₇I′T₃** the register-reference condition and
**p = D₇IT₃** the input–output condition):

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

**The scan then gives:**

```
   LD(AC)  = D₀T₅ + D₁T₅ + D₂T₅ + pB₁₁ + rB₉ + rB₇ + rB₆
   CLR(AC) = rB₁₁
   INR(AC) = rB₅
```

**Why CLR and INR are separated out:** `AC ← 0` and `AC ← AC + 1` are done by the register's **own**
clear and increment inputs, not by routing a value through the adder-and-logic circuit. Only the
seven operations that produce a *new value* on AC's data inputs appear in LD(AC).

**The adder-and-logic circuit** is **one stage replicated 16 times**, feeding AC's J-K inputs, with
inputs from DR(i), AC(i), INPR(i) and the neighbouring bits AC(i−1)/AC(i+1) for the shifts.
**It is U1's ALSU, instantiated for this specific machine** — which is why file 03 had to come first.

---

## Worked — derive the control inputs of PC (inferred form F9; method and statements from Mano)

> **Derive LD(PC), INR(PC) and CLR(PC) for the Basic Computer by scanning the machine description.**

**Step 1 — collect every statement that changes PC.** Go through the complete description in order:
fetch, the T₃ decision, the seven MRI, the register-reference skips, the I/O skips, the interrupt
cycle. Do not stop at the obvious ones.

| Where | Statement | Kind |
|---|---|---|
| fetch | `R′T₁: PC ← PC + 1` | increment |
| BUN | `D₄T₄: PC ← AR` | load |
| BSA | `D₅T₅: PC ← AR` | load |
| ISZ | `D₆T₆: if (DR = 0) then (PC ← PC + 1)` | increment |
| SPA | `rB₄: if (AC(15) = 0) then (PC ← PC + 1)` | increment |
| SNA | `rB₃: if (AC(15) = 1) then (PC ← PC + 1)` | increment |
| SZA | `rB₂: if (AC = 0) then (PC ← PC + 1)` | increment |
| SZE | `rB₁: if (E = 0) then (PC ← PC + 1)` | increment |
| SKI | `pB₉: if (FGI = 1) then (PC ← PC + 1)` | increment |
| SKO | `pB₈: if (FGO = 1) then (PC ← PC + 1)` | increment |
| interrupt | `RT₁: PC ← 0` | clear |
| interrupt | `RT₂: PC ← PC + 1` | increment |

*(The B-bit index of each register-reference instruction is read straight off its one-hot hex code in
file 04 — SPA = 7010 → bit 4, SNA = 7008 → bit 3, SZA = 7004 → bit 2, SZE = 7002 → bit 1. Recover the
subscript from the hex code rather than trusting a remembered number; that route never fails.)*

**Step 2 — sort by control input and OR the conditions.**

```
   LD(PC)  = D₄T₄ + D₅T₅

   CLR(PC) = RT₁

   INR(PC) = R′T₁
           + D₆T₆·(DR = 0)
           + rB₄·(AC(15) = 0)          SPA
           + rB₃·(AC(15) = 1)          SNA
           + rB₂·(AC = 0)              SZA
           + rB₁·(E = 0)               SZE
           + pB₉·FGI                   SKI
           + pB₈·FGO                   SKO
           + RT₂
```

**Step 3 — the sentence that shows you understand what you wrote.**

> Every skip instruction is an **increment of PC under a data-dependent condition**. There is no
> separate "skip" hardware: a skip *is* a second increment of a program counter that was already
> incremented during fetch, so the instruction after the skip is never fetched.

**The common failure here** is producing only `LD(PC) = D₄T₄ + D₅T₅` and stopping. The branch
instructions are the *obvious* writers of PC; the **six skip instructions and the interrupt cycle**
are where the marks are, and they all land on INR, not LD.

---

## Worked — derive the control of the E flip-flop (inferred form; statements from Mano)

> **E is the extended accumulator bit. Give its J and K inputs.**

**Step 1 — every statement that touches E:**

| Condition | Statement |
|---|---|
| D₁T₅ | `E ← Cₒᵤₜ` (ADD) |
| rB₇ | `E ← AC(0)` (CIR — the bit shifted out of AC enters E) |
| rB₆ | `E ← AC(15)` (CIL) |
| rB₁₀ | `E ← 0` (CLE) |
| rB₈ | `E ← E′` (CME) |

**Step 2 — classify.** Three of these *load a value* into E (from Cₒᵤₜ, AC(0), AC(15)), one clears it,
one complements it.

**Step 3 — build J and K.** For a JK flip-flop, J must be 1 exactly when E is to be set and K exactly
when it is to be cleared:

```
   set E   when:  D₁T₅·Cₒᵤₜ  +  rB₇·AC(0)  +  rB₆·AC(15)  +  rB₈·E′
   clear E when:  D₁T₅·Cₒᵤₜ′ +  rB₇·AC(0)′ +  rB₆·AC(15)′ +  rB₈·E  +  rB₁₀
```

so `J(E)` and `K(E)` are those two sums.

**The point of the exercise:** "load a value into a flip-flop" is not a primitive — a JK flip-flop is
**set when the value is 1 and cleared when the value is 0**, so a single RTL statement `E ← X`
contributes to *both* J and K, with X and X′ respectively. Complement (`CME`) contributes
`rB₈·E′` to J and `rB₈·E` to K — the classic JK toggle, which can equivalently be written as
J = K = rB₈.

---

## Traps

| # | Trap | The correction |
|---|---|---|
| T6 | Scanning only some of the statements | The method is exhaustive by definition. A missed statement is a control input that never asserts — a machine that silently does the wrong thing |
| — | Dropping the prime in `R′T₀` vs `RT₀` | Those are two different machine states (normal fetch vs interrupt cycle) that happen to share a time step |
| — | Putting `AR ← AR + 1` into LD(AR) | Increment uses **INR**. One statement, one control input |
| — | Deriving AC exactly like AR | AC is loaded from the **adder-and-logic circuit**, not the bus, so its design also fixes *which function* that circuit performs |
| — | Forgetting the skip instructions when deriving INR(PC) | Six of them, plus ISZ's conditional skip, plus the interrupt's RT₂ |
| — | Treating `E ← X` as needing only J | A JK flip-flop needs **J = X and K = X′**. One statement, two contributions |
| — | Answering "design of the BC" with the instruction list | The question wants **equations derived by the scan**, plus the hardware inventory |

---

## Self-test

1. State the design method in one sentence, then apply it to **DR**: list every statement that
   changes DR and give LD(DR) and INR(DR).
2. Why does `CLR(AR) = RT₀` have no other terms?
3. The bus encoder input meaning "put **DR** on the bus" — which statements activate it?
4. Give J and K for the **IEN** flip-flop and explain why `RT₂` appears in K.
5. Derive LD(IR). Why is it so short?
6. `LD(AC) = D₀T₅ + D₁T₅ + D₂T₅ + pB₁₁ + rB₉ + rB₇ + rB₆` — explain why `rB₁₁` (CLA) is absent from
   this expression even though CLA obviously changes AC.
7. A designer adds a new instruction `SUB` (opcode 111 was full, so they use a spare MRI code) with
   the sequence `D₇T₄: DR ← M[AR]` and `D₇T₅: AC ← AC − DR, SC ← 0`. Which existing control equations
   must change, and how?
8. Explain, in terms of this method, why hardwired control is fast but hard to modify.

---

## Answers

**1.** *Method:* for the register in question, find every register-transfer statement in the complete
machine description that changes it, and OR their control conditions together, sorted by which
control input (LD, INR, CLR) each statement uses.

*Applied to DR* — the statements are the operand fetches and ISZ's increment:

```
   D₀T₄:  DR ← M[AR]        (AND)
   D₁T₄:  DR ← M[AR]        (ADD)
   D₂T₄:  DR ← M[AR]        (LDA)
   D₆T₄:  DR ← M[AR]        (ISZ)
   D₆T₅:  DR ← DR + 1       (ISZ)

   LD(DR)  = D₀T₄ + D₁T₄ + D₂T₄ + D₆T₄     =  (D₀ + D₁ + D₂ + D₆)·T₄
   INR(DR) = D₆T₅
   CLR(DR) = 0   (nothing clears DR)
```
The factored form `(D₀ + D₁ + D₂ + D₆)·T₄` is the better answer — it shows you noticed that four
instructions share one operand-fetch step.

**2.** Because the interrupt cycle is the **only** place in the whole machine where AR is set to a
constant. Every other use of AR loads it from the bus (PC, IR's address field, or memory) or
increments it. `AR ← 0` at RT₀ exists so the return address can be written to location 0.

**3.** DR drives the bus when its contents are written to memory or transferred: `D₆T₆: M[AR] ← DR`
(ISZ's write-back). In Mano's design DR also feeds AC through the adder-and-logic circuit rather than
the bus, so that path does **not** activate the bus encoder. The full-credit point is the distinction:
*DR reaching AC is not a bus transfer; DR reaching memory is.*

**4.** `J(IEN) = pB₇` (the ION instruction), `K(IEN) = pB₆ + RT₂` (IOF, and the interrupt cycle).
`RT₂` is in K because the interrupt cycle **disables further interrupts** before jumping to the
service routine — otherwise a second interrupt could arrive while the first is being serviced,
overwrite the return address in M[0], and destroy the return path.

**5.** `LD(IR) = R′T₁`. It is short because IR is written **exactly once per instruction**, during the
fetch, and never again — nothing else in the machine has any reason to change the instruction
currently being executed. (The prime on R excludes the interrupt cycle, which does not fetch.)

**6.** Because CLA clears AC through the register's **own CLR input**, not by loading a value: it
appears as `CLR(AC) = rB₁₁`. LD(AC) collects only the statements that place a *new value* on AC's data
inputs via the adder-and-logic circuit. Same reason INC (`rB₅`) appears in INR(AC) rather than LD(AC).

**7.** Three changes:
- **LD(DR)** gains `D₇T₄`, becoming `(D₀ + D₁ + D₂ + D₆ + D₇)·T₄`.
- **LD(AC)** gains `D₇T₅`.
- The **adder-and-logic circuit** needs a new function select for subtraction (`AC + DR′ + 1`), which
  means a new control gate driven by `D₇T₅` — plus, if E is to hold the borrow, a new term in J(E)/K(E).
Also worth stating: opcode 111 is the escape code for register-reference and I/O instructions, so
using D₇ for an MRI would **destroy all 18 of those instructions** — the premise of the question is
itself a design error, and saying so is part of the answer.

**8.** Because the method **bakes the equations into gates**. Each control input is a fixed sum of
D·T products wired in silicon, so asserting it costs one gate delay — nothing is fetched, nothing is
looked up. But changing the instruction set changes the *set of statements*, which changes the sums,
which changes the wiring: you must re-run the scan for **every** register and re-fabricate. That is
precisely the trade microprogrammed control exists to invert (file 07).
