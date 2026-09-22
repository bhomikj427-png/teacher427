# 08 — Control-gate derivation

**Assignment 2: Q9, Q10 · 20 of 150 marks · U2 (L11) · needs 06, 07**

★ **This is the examinable skill of U2** — not the instruction list. One method, applied to whichever
register the examiner names. Mano has **six** problems of this exact shape and the professor asked
two of them; assume the other four are on the table.

> A2 Q10 is Mano 5-21 **word for word**, including "Minimize the number of gates."

---

## Map

```
   [1] The method ── scan every statement that changes X, OR the conditions
         │
         ├──► [2] AR      worked in the deck
         │
         ├──► [3] a lone flip-flop, JK    (A2 Q9 = Mano 5-20)
         │
         ├──► [4] PC                      (A2 Q10 = Mano 5-21)
         │
         ├──► [5] AC — the accumulator logic
         │
         ├──► [6] memory read / write     (Mano 5-22)
         │
         └──► [7] SC itself               (Mano 5-25)
```

---

## The questions this file answers

| # | Question | Marks | Mano |
|---|---|---|---|
| 1 | `[A2 Q9]` Flip-flop F with `xT₃: F←1`, `yT₁: F←0`, `zT₂: F←F′`, `wT₅: F←G`; otherwise unchanged. Draw the logic diagram of the control functions and the flip-flop inputs. Use a JK flip-flop, minimise gates. | 10 | **5-20** |
| 2 | `[A2 Q10]` Derive the control gates associated with the PC in the basic computer. Draw the logic diagram and show how the output connects to LD, INR and CLR of PC. Minimise gates. | 10 | **5-21** |

Unasked Mano problems of the same kind: **5-19, 5-22, 5-23, 5-24, 5-25.**

---

## Build

### 1 · The method

> **Q** *(no question yet — this is the tool the rest of the file uses)*
> **You are given the complete description of a machine as a list of register transfers. How do you
> work out the circuit that drives one register's control inputs?**
>
> *Guess the method in one sentence. It is genuinely one sentence.*

> ★ **Scan every register-transfer statement in the complete machine description that changes that
> register, and OR their control conditions together.**

That is the whole method. Each register has up to three control inputs, and each statement tells you
which one it needs:

| The statement does | Goes to |
|---|---|
| `X ← something` | **LD(X)** |
| `X ← X + 1` | **INR(X)** |
| `X ← 0` | **CLR(X)** |

So the derivation is mechanical:

1. Go through the complete machine description line by line.
2. Every time the register appears on the **left** of an arrow, note the condition in front of the colon.
3. Sort those conditions into LD, INR, CLR.
4. **OR** each group together.
5. Minimise (factor common terms), draw the gates.

**"Minimise the number of gates" means factor**: `D₄T₄ + D₅T₅` cannot be factored, but
`D₀T₅ + D₁T₅ + D₂T₅` becomes `(D₀ + D₁ + D₂)T₅` — three AND gates and an OR become one OR and one AND.
Say that you have factored; it is what the instruction is asking for.

> ✓ **Check 1.** (a) State the method in one sentence. (b) Which control input does
> `D₅T₄: AR ← AR + 1` contribute to? (c) Factor `D₃T₄ + D₄T₄ + D₅T₄`.

---

### 2 · Worked: the AR gates

> **Q** *(the deck's own worked example — do it before the assignment questions)*
> **Derive LD, INR and CLR for AR.**
>
> *Scan files 06 and 07 for every line with AR on the left. There are five. Find them before reading.*

The statements that change AR, from the complete machine description:

```
R′T₀:    AR ← PC
R′T₂:    AR ← IR(0-11)
D′₇IT₃:  AR ← M[AR]
D₅T₄:    AR ← AR + 1        (BSA)
RT₀:     AR ← 0             (interrupt cycle)
```

Sorted and OR-ed:

| Control | Expression |
|---|---|
| **LD(AR)** | `R′T₀ + R′T₂ + D′₇IT₃` |
| **INR(AR)** | `D₅T₄` |
| **CLR(AR)** | `RT₀` |

Factored: `LD(AR) = R′(T₀ + T₂) + D′₇IT₃` — one OR, one AND for the first term instead of two ANDs.

Note the `R′` on the fetch lines: those transfers happen **only when no interrupt is being serviced**
(file 07, step 9). Forgetting R′ is a common slip, and it is precisely where the interrupt cycle hooks
into the machine.

> ✓ **Check 2.** (a) Why do the fetch statements carry R′? (b) Which instruction contributes INR(AR),
> and why does it need it? (c) Write LD(AR) factored.

---

### 3 · Controlling a lone flip-flop — A2 Q9

> **Q** `[A2 Q9 · 10 marks]` **= Mano 5-20**
> **The operations to be performed with a flip-flop F (not used in the basic computer) are specified
> by: `xT₃: F ← 1` (set) · `yT₁: F ← 0` (clear) · `zT₂: F ← F′` (complement) · `wT₅: F ← G`
> (transfer G to F). Otherwise, the content of F must not change. Draw the logic diagram showing the
> connections of the gates that form the control functions and the inputs of flip-flop F. Use a JK
> flip-flop and minimise the number of gates.**
>
> *A single flip-flop has no LD/INR/CLR — it has J and K. Guess how "complement" and "transfer G"
> map onto J and K before reading.*

**Why a JK flip-flop is specified**, and this is the insight the question tests: a JK does all four
required behaviours with **no extra logic**, because its table already contains them.

| J | K | Q(next) | Behaviour |
|---|---|---|---|
| 0 | 0 | Q | **no change** ← "otherwise F must not change" |
| 1 | 0 | 1 | **set** |
| 0 | 1 | 0 | **clear** |
| 1 | 1 | Q′ | **complement** |

So the derivation is: **each required operation contributes to J, to K, or to both.**

| Statement | Needs | Contributes to J | Contributes to K |
|---|---|---|---|
| `xT₃: F ← 1` | set | `xT₃` | — |
| `yT₁: F ← 0` | clear | — | `yT₁` |
| `zT₂: F ← F′` | complement (J = K = 1) | `zT₂` | `zT₂` |
| `wT₅: F ← G` | set **if G = 1**, clear **if G = 0** | `wT₅G` | `wT₅G′` |

**The answer:**

```
 J = xT₃ + zT₂ + wT₅G
 K = yT₁ + zT₂ + wT₅G′
```

```
      x ──┐
     T₃ ──┴─AND──┐
      z ──┐      │
     T₂ ──┴─AND──┼──┬──► OR ──► J ┌──────┐
      w ──┐      │  │            │  JK   │
     T₅ ──┼─AND──┘  │        CLK►│  FF   │──► F
      G ──┘         │            │       │
                    │            └──────┘
      y ──┐         │                ▲
     T₁ ──┴─AND──┐  │                │
                 ├──┴──► OR ─────────┘ K
      w ──┐      │
     T₅ ──┼─AND──┘
      G ──►o (inverter)
```

**Gate count, minimised:** the `zT₂` AND gate is **shared** between J and K — that is the minimisation
the question wants, and saying so out loud is worth a mark. Likewise `wT₅` can be formed once and
then AND-ed with G and with G′. Total: 5 AND gates (or 4 plus a shared `wT₅` term), 2 OR gates,
1 inverter.

**When F is not being addressed**, every product term is 0, so J = K = 0 and F holds — which is
exactly the "otherwise, the content of F must not change" requirement, satisfied for free.

> ✓ **Check 3.** (a) Why does "complement" drive both J and K? (b) How does `F ← G` split across J and
> K? (c) Which single term is shared between J and K, and what does sharing it save?
> (d) `[Mano 5-23]` Do the same for the interrupt flip-flop **R** in the basic computer.

---

### 4 · The PC gates — A2 Q10

> **Q** `[A2 Q10 · 10 marks]` **= Mano 5-21, verbatim**
> **Derive the control gates associated with the program counter PC in the basic computer. Draw the
> logic diagram of the gates and show how the output is connected to the LD, INR and CLR inputs of
> PC. Minimise the number of gates.**
>
> *Apply step 1's method. Before reading: roughly how many statements in the whole machine change PC?
> Guess a number — most people guess far too few.*

**Twelve.** PC is the most-written register in the machine, because every branch and every skip
touches it. Scan the complete description:

| Condition | Statement | Group |
|---|---|---|
| `R′T₁` | `PC ← PC + 1` (fetch) | INR |
| `D₄T₄` | `PC ← AR` (BUN) | LD |
| `D₅T₅` | `PC ← AR` (BSA) | LD |
| `D₆T₆(DR = 0)` | `PC ← PC + 1` (ISZ skip) | INR |
| `rB₄(AC₁₅)′` | `PC ← PC + 1` (SPA, skip if positive) | INR |
| `rB₃(AC₁₅)` | `PC ← PC + 1` (SNA, skip if negative) | INR |
| `rB₂(AC = 0)` | `PC ← PC + 1` (SZA, skip if AC zero) | INR |
| `rB₁E′` | `PC ← PC + 1` (SZE, skip if E zero) | INR |
| `pB₉ FGI` | `PC ← PC + 1` (SKI) | INR |
| `pB₈ FGO` | `PC ← PC + 1` (SKO) | INR |
| `RT₁` | `PC ← 0` (interrupt) | CLR |
| `RT₂` | `PC ← PC + 1` (interrupt) | INR |

*(r = D₇I′T₃, p = D₇IT₃ — file 07, step 3.)*

**The answer:**

```
 LD(PC)  = D₄T₄ + D₅T₅

 CLR(PC) = RT₁

 INR(PC) = R′T₁ + RT₂
         + D₆T₆(DR = 0)
         + rB₄(AC₁₅)′ + rB₃(AC₁₅) + rB₂(AC = 0) + rB₁E′
         + pB₉FGI + pB₈FGO
```

```
   D₄ ──┐                          ┌───────────┐
   T₄ ──┴AND──┐                    │           │
              ├── OR ──────────────► LD        │
   D₅ ──┐     │                    │           │
   T₅ ──┴AND──┘                    │    PC     │
                                   │           │
   R ───┐                          │           │
   T₁ ──┴AND───────────────────────► CLR       │
                                   │           │
   (the ten INR terms) ── OR ──────► INR       │
                                   └───────────┘
```

**Minimisation to mention:** the four skip terms all share **r**, so form `r` once and fan it out;
likewise `p` for the two I/O skips. `R′T₁` and `RT₁` share T₁. That takes the gate count from ~14 ANDs
to about 10 plus two shared product terms.

⚠ **Two warnings, both from real errors.**
**(1)** The widely-circulated solutions manual for this problem contains **two typos**: it prints
`RT₇` where it should read `RT₂`, and `rB₄ + (AC₁₅)′` where the term is `rB₄(AC₁₅)′` — an AND, not an
OR. The expressions above are the corrected ones. If your downloaded solution disagrees at those two
places, it is the solution that is wrong.
**(2)** `(AC = 0)` is not a signal you can wire directly — it is the output of a **16-input NOR gate**
across all of AC (Mano's "check for zero" circuit). Say so; it is the kind of detail that separates a
derivation from a copy.

> ✓ **Check 4.** (a) Which two instructions contribute LD(PC)? (b) Why are there so many INR terms?
> (c) How is `(AC = 0)` generated? (d) Why does the fetch increment carry R′?

---

### 5 · The accumulator logic

> **Q** *(the deck's other worked derivation, and the natural extension of A2 Q10)*
> **Derive LD, INR and CLR for AC, and say what feeds AC's data inputs.**
>
> *AC is special — file 06, step 4 told you why. Recall it before reading.*

All statements that change AC:

| Condition | Operation | Gate name |
|---|---|---|
| `D₀T₅` | `AC ← AC ∧ DR` | AND |
| `D₁T₅` | `AC ← AC + DR` | ADD |
| `D₂T₅` | `AC ← DR` | DR (transfer) |
| `pB₁₁` | `AC(0-7) ← INPR` | INPR |
| `rB₉` | `AC ← AC′` | COM |
| `rB₇` | `AC ← shr AC, AC(15) ← E` | SHR |
| `rB₆` | `AC ← shl AC, AC(0) ← E` | SHL |
| `rB₁₁` | `AC ← 0` | CLR |
| `rB₅` | `AC ← AC + 1` | INC |

```
 LD(AC)  = D₀T₅ + D₁T₅ + D₂T₅ + pB₁₁ + rB₉ + rB₇ + rB₆
 CLR(AC) = rB₁₁
 INR(AC) = rB₅
```

Factored: `(D₀ + D₁ + D₂)T₅ + pB₁₁ + r(B₉ + B₇ + B₆)`.

★ **AC's data input does not come from the bus.** It comes from the **adder-and-logic circuit** — one
stage replicated 16 times, taking DR(i), AC(i), INPR(i) and the neighbouring bits AC(i−1)/AC(i+1) for
the shifts, and feeding AC's J-K inputs. **That circuit is U1's ALSU (file 05), instantiated for this
machine.** Which is exactly why U1 had to come first, and it is a good sentence to end an answer on.

> ✓ **Check 5.** (a) Which single condition both clears AC and appears nowhere in LD(AC)? (b) Why is
> `AC ← AC + 1` on INR rather than routed through the adder? (c) What are the four inputs to one stage
> of the adder-and-logic circuit?

---

### 6 · Memory read and write

> **Q** `[Mano 5-22 · not yet asked]`
> **Derive the control gates for the write input of the memory in the basic computer.**
>
> *Same method, but the "register" is memory. Guess how many statements write to memory.*

Memory's two control inputs are **read** and **write**, and they are derived exactly like LD and CLR.

**Write** — scan for `M[AR] ← …` :

```
 Write = D₃T₄  (STA: M[AR] ← AC)
       + D₅T₄  (BSA: M[AR] ← PC)
       + D₆T₆  (ISZ: M[AR] ← DR)
       + RT₁   (interrupt: M[AR] ← TR)
```

**Read** — scan for `… ← M[AR]` :

```
 Read  = R′T₁                    (IR ← M[AR], fetch)
       + D′₇IT₃                  (AR ← M[AR], indirect)
       + (D₀ + D₁ + D₂ + D₆)T₄   (DR ← M[AR], the four MRIs that need an operand)
```

Note which four: AND, ADD, LDA and ISZ. **STA and BUN are absent from Read** — STA writes, BUN needs
no operand (file 07, step 5).

> ✓ **Check 6.** (a) Which four instructions read an operand at T₄? (b) Why is STA in Write but not
> in Read? (c) What is on the bus during each of the four write conditions?

---

### 7 · Clearing the sequence counter

> **Q** `[Mano 5-25 · not yet asked]`
> **Derive the Boolean expression for the gate structure that clears the sequence counter SC to 0.
> Draw the logic diagram and show how the output is connected to the INR and CLR inputs of SC.
> Minimise the number of gates.**
>
> *File 07, step 1 said `SC ← 0` is the last microoperation of every instruction. So scan for it —
> and watch for a simplification.*

Every `SC ← 0` in the machine:

| From | Condition |
|---|---|
| register-reference | `r` = D₇I′T₃ |
| input/output | `p` = D₇IT₃ |
| AND, ADD, LDA | `D₀T₅`, `D₁T₅`, `D₂T₅` |
| STA, BUN | `D₃T₄`, `D₄T₄` |
| BSA | `D₅T₅` |
| ISZ | `D₆T₆` |
| interrupt | `RT₂` |

**The simplification worth finding:** `r + p = D₇I′T₃ + D₇IT₃ = D₇T₃(I′ + I) = **D₇T₃**`. The I bit
falls out entirely — both register-reference *and* I/O instructions end at T₃, so you never need to
know which.

```
 CLR(SC) = D₇T₃
         + (D₀ + D₁ + D₂ + D₅)T₅
         + (D₃ + D₄)T₄
         + D₆T₆
         + RT₂

 INR(SC) = CLR(SC)′        SC counts up on every clock unless it is being cleared
```

That last line is the part people miss: SC has no separate "count" condition. It **always** counts,
and CLR is what interrupts the count — so INR is simply the complement, one inverter.

> ✓ **Check 7.** (a) Simplify `r + p` and explain why the I bit disappears. (b) Which MRIs end at T₅?
> (c) Why is INR(SC) just the complement of CLR(SC)?

---

## Exam form

### The method, in five lines

```
1. List every statement in the machine description with the register on the LEFT.
2. Sort by what it does:   X ← y  → LD      X ← X+1 → INR      X ← 0 → CLR
3. OR each group.
4. Factor common terms — this is what "minimise the number of gates" asks for.
5. Draw: AND per product term, OR per group, into LD / INR / CLR.
```

### For a lone flip-flop, use JK

| Required | J gets | K gets |
|---|---|---|
| set on S | `S` | — |
| clear on C | — | `C` |
| complement on X | `X` | `X` |
| transfer G on W | `W·G` | `W·G′` |
| otherwise hold | (nothing — J = K = 0 holds automatically) | |

### Results worth carrying into the exam

```
 LD(AR)  = R'T₀ + R'T₂ + D'₇IT₃        INR(AR) = D₅T₄        CLR(AR) = RT₀
 LD(PC)  = D₄T₄ + D₅T₅                 CLR(PC) = RT₁
 LD(AC)  = (D₀+D₁+D₂)T₅ + pB₁₁ + r(B₉+B₇+B₆)    CLR(AC) = rB₁₁   INR(AC) = rB₅
 Write   = D₃T₄ + D₅T₄ + D₆T₆ + RT₁
 Read    = R'T₁ + D'₇IT₃ + (D₀+D₁+D₂+D₆)T₄
 CLR(SC) = D₇T₃ + (D₀+D₁+D₂+D₅)T₅ + (D₃+D₄)T₄ + D₆T₆ + RT₂
```

---

## Attempt

1. `[A2 Q9 · 10]` the J and K expressions **plus the drawn circuit**, and name the shared term.
2. `[A2 Q10 · 10]` all twelve statements listed, the three expressions, the circuit, and a sentence on
   what you factored.
3. `[Mano 5-22]` the memory write gates — then do Read as well.
4. `[Mano 5-23]` the interrupt flip-flop R with a JK.
5. `[Mano 5-25]` the SC clear, including the `r + p = D₇T₃` simplification.
6. `[Mano 5-19]` register R and memory from three random control functions — the abstract version of
   the same skill.
7. `[Mano 5-24]` the Boolean expression for x₁ (the bus encoder input).

---

## Traps

| Trap | Correction |
|---|---|
| Missing statements when scanning | PC has **twelve**. Work through the whole description, not just the MRIs |
| Forgetting R′ on the fetch statements | Fetch only happens when no interrupt is being serviced |
| Writing `rB₄ + (AC₁₅)′` | It is an **AND**: `rB₄(AC₁₅)′`. The circulating solutions manual has this typo |
| Writing `RT₇` in INR(PC) | It is `RT₂`. Same manual, same problem, second typo |
| Treating `(AC = 0)` as a wire | It is a 16-input NOR across AC |
| Not factoring | "Minimise the number of gates" is an instruction, not a suggestion |
| Using D flip-flops for A2 Q9 | The question says JK, and JK is what makes "complement" free |
| Forgetting that J = K = 0 holds | That is how "otherwise F must not change" is satisfied — say it |
| Routing AC's data from the bus | AC is loaded from the **adder-and-logic circuit** |

---

## Self-test

1. State the derivation method in one sentence.
2. A register X is changed by `aT₁: X ← Y`, `bT₂: X ← 0`, `cT₃: X ← X + 1`. Give LD, INR, CLR.
3. For a JK flip-flop, what must J and K be to complement? To hold?
4. Give LD(PC) and CLR(PC) for the Basic Computer.
5. Why do both r and p end at T₃, and what does that let you simplify?
6. Which four instructions appear in the memory Read expression at T₄?
7. What feeds AC's data inputs, and which earlier file built that circuit?

---
---

## Answers

**Check 1.** (a) Scan every statement in the machine description that changes the register, and OR
their control conditions together, sorted into LD / INR / CLR. (b) **INR(AR)**. (c) `(D₃ + D₄ + D₅)T₄`.

**Check 2.** (a) Because the interrupt cycle replaces fetch and decode when R = 1 — `R′` ensures the
normal fetch runs only when no interrupt is being serviced. (b) **BSA** (`D₅T₄: AR ← AR + 1`), because
it must jump to EA + 1 while EA is still needed at T₄ to store the return address. (c)
`LD(AR) = R′(T₀ + T₂) + D′₇IT₃`.

**Check 3.** (a) Because J = K = 1 is the JK flip-flop's toggle condition — the hardware already does
complement, so no extra gate is needed. (b) `F ← G` means set when G = 1 and clear when G = 0, so
J gets `wT₅G` and K gets `wT₅G′`. (c) **`zT₂`** — one AND gate feeds both OR gates instead of two.
(d) R is set by `T′₀T′₁T′₂(IEN)(FGI + FGO)` and cleared by `RT₂`, so **J = T′₀T′₁T′₂·IEN·(FGI + FGO)**
and **K = RT₂** (which, since R = 1 whenever the cycle runs, reduces to T₂ gated by R).

**Check 4.** (a) **BUN** (`D₄T₄`) and **BSA** (`D₅T₅`). (b) Because PC is incremented by the fetch, by
every skip instruction (SPA, SNA, SZA, SZE, SKI, SKO), by the ISZ skip, and by the interrupt cycle —
ten conditions in all. (c) By a **16-input NOR gate** across all bits of AC. (d) So that the ordinary
fetch does not also run during an interrupt cycle, which uses T₀, T₁, T₂ for its own transfers.

**Check 5.** (a) **`rB₁₁`** — CLA clears AC via the CLR input, so it never appears in LD. (b) Because
AC has a dedicated INR (increment) input, which is cheaper than routing a constant 1 through the
adder. (c) **DR(i), AC(i), INPR(i)**, and the neighbouring AC bits **AC(i−1)/AC(i+1)** for the shifts.

**Check 6.** (a) **AND, ADD, LDA, ISZ** (D₀, D₁, D₂, D₆). (b) STA's memory access *writes* AC into
memory; it never brings an operand in. (c) `D₃T₄` → AC · `D₅T₄` → PC · `D₆T₆` → DR · `RT₁` → TR.

**Check 7.** (a) `r + p = D₇I′T₃ + D₇IT₃ = D₇T₃(I′ + I) = D₇T₃`. The I bit disappears because **both**
register-reference and I/O instructions finish at T₃, so which one it is does not matter for clearing
SC. (b) **AND, ADD, LDA** (at T₅) and **BSA** (also T₅). (c) Because SC has no separate count
condition — it increments on every clock unless cleared, so INR is simply CLR inverted.

**Self-test 1.** Scan every statement that changes the register, sort by LD / INR / CLR, and OR each
group.

**Self-test 2.** LD(X) = `aT₁`, CLR(X) = `bT₂`, INR(X) = `cT₃`.

**Self-test 3.** Complement: **J = K = 1**. Hold: **J = K = 0**.

**Self-test 4.** `LD(PC) = D₄T₄ + D₅T₅`; `CLR(PC) = RT₁`.

**Self-test 5.** Register-reference (r = D₇I′T₃) and I/O (p = D₇IT₃) both complete within T₃, so their
sum simplifies to **D₇T₃** — the I bit cancels.

**Self-test 6.** **D₀ (AND), D₁ (ADD), D₂ (LDA), D₆ (ISZ)**.

**Self-test 7.** The **adder-and-logic circuit**, fed by DR, AC, INPR and AC's neighbouring bits — it
is U1's ALSU, built in **file 05**.

---

## What to do next

U2 is complete. File 09 starts **U3**, which neither assignment touches — so Mano chapter 7 is the
only question evidence that exists for it. It is on the mid-term all the same.
