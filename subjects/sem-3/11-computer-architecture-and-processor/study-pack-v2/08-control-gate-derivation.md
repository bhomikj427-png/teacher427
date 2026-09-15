# 08 — Deriving Control Gates From RTL

**Assignment 2: Q9, Q10 · 20 of 150 marks · U2 (L11 — Design of Basic Computer)**
Source problems: Mano 5-20, 5-21.

A2 answer policy: method + fully worked twin here; A2's own key after 16-09-2026 16:30.

**One method answers both questions and every variant:**

> **Scan every statement that changes the target. Group by the kind of change. OR the control
> functions within each group. Map each group to a control input.**

---

## Map

```
   Complete RTL description of the machine
            │  scan for the target (register or flip-flop)
            ▼
   Group statements by effect ─── load new value ──► LD
            │                 ├── +1             ──► INR
            │                 ├── ← 0            ──► CLR
            │                 └── set/clear/complement (flip-flop) ──► J, K
            ▼
   OR the control functions per group ──► factor common terms ──► gate diagram
```

---

## Attempt

**A2 Q9.** A flip-flop F (not in the BC) is controlled by:
```
   xT₃: F ← 1      set
   yT₁: F ← 0      clear
   zT₂: F ← F′     complement
   wT₅: F ← G      transfer G
```
Otherwise F must not change. Draw the logic: gates forming the control functions and the inputs of F.
Use a **JK flip-flop**; minimize gates.

**A2 Q10.** Derive the control gates for **PC** in the basic computer. Draw the logic diagram and show
the connections to PC's **LD, INR, CLR**. Minimize gates.

---

## Learn

### JK flip-flop as a controllable 1-bit register

| J | K | Q(t+1) | Use it for |
|---|---|---|---|
| 0 | 0 | Q | **no change** |
| 1 | 0 | 1 | **set** |
| 0 | 1 | 0 | **clear** |
| 1 | 1 | Q′ | **complement** |

**Mapping rules:**

| Statement | Contributes to J | Contributes to K |
|---|---|---|
| `c: F ← 1` | c | — |
| `c: F ← 0` | — | c |
| `c: F ← F′` | c | c |
| `c: F ← G` | c·G | c·G′ |

Why the transfer row works: G = 1 → J = 1, K = 0 → set; G = 0 → J = 0, K = 1 → clear. Either way F = G.
When no control function is active, J = K = 0 → hold — "otherwise unchanged" comes free.

### Register control inputs

| Statement shape | Control input |
|---|---|
| `c: R ← (any value from bus/logic)` | **LD** |
| `c: R ← R + 1` | **INR** |
| `c: R ← 0` | **CLR** |
| `c: if (cond) then (R ← R + 1)` | **INR**, with the term **c·cond** |

**Minimizing:** factor shared variables (D₀T₄ + D₁T₄ = (D₀ + D₁)T₄); share an AND output that feeds
two ORs; reuse r = D₇I′T₃ and p = D₇IT₃ as single signals.

### The complete Basic Computer description — scan this table

| Phase | Control | Microoperations |
|---|---|---|
| Fetch | R′T₀ | AR ← PC |
| | R′T₁ | IR ← M[AR], PC ← PC + 1 |
| Decode | R′T₂ | D₀…D₇ ← decode IR(12-14), AR ← IR(0-11), I ← IR(15) |
| Indirect | D₇′IT₃ | AR ← M[AR] |
| Interrupt | T₀′T₁′T₂′(IEN)(FGI + FGO) | R ← 1 |
| | RT₀ | AR ← 0, TR ← PC |
| | RT₁ | M[AR] ← TR, PC ← 0 |
| | RT₂ | PC ← PC + 1, IEN ← 0, R ← 0, SC ← 0 |
| AND | D₀T₄ / D₀T₅ | DR ← M[AR] / AC ← AC ∧ DR, SC ← 0 |
| ADD | D₁T₄ / D₁T₅ | DR ← M[AR] / AC ← AC + DR, E ← Cₒᵤₜ, SC ← 0 |
| LDA | D₂T₄ / D₂T₅ | DR ← M[AR] / AC ← DR, SC ← 0 |
| STA | D₃T₄ | M[AR] ← AC, SC ← 0 |
| BUN | D₄T₄ | PC ← AR, SC ← 0 |
| BSA | D₅T₄ / D₅T₅ | M[AR] ← PC, AR ← AR + 1 / PC ← AR, SC ← 0 |
| ISZ | D₆T₄ / D₆T₅ / D₆T₆ | DR ← M[AR] / DR ← DR + 1 / M[AR] ← DR, if (DR = 0) then (PC ← PC + 1), SC ← 0 |
| RRI | r = D₇I′T₃ | SC ← 0 |
| | rB₁₁ … rB₀ | CLA AC ← 0 · CLE E ← 0 · CMA AC ← AC′ · CME E ← E′ · CIR · CIL · INC AC ← AC + 1 · **SPA** if (AC(15) = 0) then (PC ← PC + 1) · **SNA** if (AC(15) = 1) then (PC ← PC + 1) · **SZA** if (AC = 0) then (PC ← PC + 1) · **SZE** if (E = 0) then (PC ← PC + 1) · HLT S ← 0 |
| I/O | p = D₇IT₃ | SC ← 0 |
| | pB₁₁ … pB₆ | INP AC(0-7) ← INPR, FGI ← 0 · OUT OUTR ← AC(0-7), FGO ← 0 · **SKI** if (FGI = 1) then (PC ← PC + 1) · **SKO** if (FGO = 1) then (PC ← PC + 1) · ION IEN ← 1 · IOF IEN ← 0 |

(RRI bit order: B₁₁ CLA, B₁₀ CLE, B₉ CMA, B₈ CME, B₇ CIR, B₆ CIL, B₅ INC, B₄ SPA, B₃ SNA, B₂ SZA,
B₁ SZE, B₀ HLT. I/O: B₁₁ INP, B₁₀ OUT, B₉ SKI, B₈ SKO, B₇ ION, B₆ IOF.)

**For A2 Q10: scan this table for every statement with PC on the left — including the conditional
ones hidden inside ISZ, SPA, SNA, SZA, SZE, SKI, SKO.** Missing one is the standard mark loss.

---

## Worked twins

**Twin of Q9.**
```
   pT₁: F ← 1       qT₂: F ← 0       rT₄: F ← F′      sT₃: F ← G′
```

Apply the mapping (the transfer is of **G′**, so the G and G′ terms swap):

```
   J = pT₁ + rT₄ + sT₃·G′
   K = qT₂ + rT₄ + sT₃·G
```

Gate list, minimized:

| Gate | Inputs | Output | Feeds |
|---|---|---|---|
| AND₁ | p, T₁ | pT₁ | OR_J |
| AND₂ | q, T₂ | qT₂ | OR_K |
| AND₃ | r, T₄ | rT₄ | **OR_J and OR_K** (shared) |
| AND₄ | s, T₃ | sT₃ | AND₅, AND₆ (shared) |
| NOT | G | G′ | AND₅ |
| AND₅ | sT₃, G′ | sT₃G′ | OR_J |
| AND₆ | sT₃, G | sT₃G | OR_K |
| OR_J | 3 inputs | J | JK flip-flop J |
| OR_K | 3 inputs | K | JK flip-flop K |

```
   p, T₁ ──[AND₁]── pT₁ ─────────────┐
                                     │
   r, T₄ ──[AND₃]── rT₄ ─────────┬───┼──►┐
                                 │   │   [OR_J]──► J ─┐
   s, T₃ ──[AND₄]── sT₃ ──┬──────┼───┼──►┘            │   ┌────────┐
                          │      │   │                └──►│ J      │
            G ──[NOT]─ G′─┤      │   │                    │   JK   │──► F
                          │      │   │                ┌──►│ K      │
                    [AND₅: sT₃·G′] ──┘                │   │  >     │◄── Clock
                    [AND₆: sT₃·G ] ──┐                │   └────────┘
                                     │                │
                                 └───┼──►┐            │
   q, T₂ ──[AND₂]── qT₂ ─────────────┼──►[OR_K]──► K ─┘
                                     └──►┘

   OR_J inputs: pT₁, rT₄, sT₃G′        OR_K inputs: qT₂, rT₄, sT₃G
```

Check every row: only pT₁ active → J = 1, K = 0 → set ✓ · only qT₂ → clear ✓ · only rT₄ → J = K = 1 →
complement ✓ · only sT₃ with G = 1 → J = 0, K = 1 → F = 0 = G′ ✓ · none active → J = K = 0 → hold ✓.

**Twin of Q10 — control gates for DR, plus memory Write.**

Scan the table for DR on the left:

| Statement | Effect | Input |
|---|---|---|
| D₀T₄: DR ← M[AR] | load | LD |
| D₁T₄: DR ← M[AR] | load | LD |
| D₂T₄: DR ← M[AR] | load | LD |
| D₆T₄: DR ← M[AR] | load | LD |
| D₆T₅: DR ← DR + 1 | increment | INR |

```
   LD(DR)  = D₀T₄ + D₁T₄ + D₂T₄ + D₆T₄ = (D₀ + D₁ + D₂ + D₆)·T₄
   INR(DR) = D₆T₅
   CLR(DR) = 0          (no statement clears DR)
```

```
   D₀ ─┐
   D₁ ─┤
   D₂ ─┼─[OR]──┐
   D₆ ─┘       [AND]──► LD(DR)          ┌────────┐
   T₄ ─────────┘                        │        │
                                        │   DR   │
   D₆ ─┐                                │        │
   T₅ ─┴[AND]──────────► INR(DR) ──────►│  INR   │
                                        │  LD    │◄── LD(DR)
   0 ──────────────────► CLR(DR) ──────►│  CLR   │
                         Clock ────────►│  >     │
                                        └────────┘
```
Factoring saved three AND gates: one 4-input OR + one AND instead of four ANDs + a 4-input OR.

Scan for memory writes (M[AR] on the left):

```
   Write = D₃T₄ + D₅T₄ + D₆T₆ + RT₁          (STA, BSA, ISZ, interrupt)
         = (D₃ + D₅)T₄ + D₆T₆ + RT₁
```

---

## Traps

| Trap | Correction |
|---|---|
| JK: `F ← G` as J = c, K = c | That complements. Use J = cG, K = cG′ |
| Using a D flip-flop "to minimize" | The question says JK; with D you would need a MUX to hold |
| PC: listing only fetch and BUN | Seven conditional skips + ISZ + interrupt also change PC |
| Conditional increment written as INR = rB₄ | The condition is part of the term: rB₄·AC(15)′ |
| PC ← 0 put under LD | Clearing is CLR; LD is for loading a value (from AR) |
| Duplicating an AND that two ORs need | Share it — that is the "minimize" mark |

---

## Self-test

1. Flip-flop IEN: give J and K from the table.
2. Derive LD(AR), INR(AR), CLR(AR).
3. Derive CLR(SC) and simplify.
4. LD(TR)? INR(TR)? CLR(TR)?
5. A flip-flop F: `aT₀: F ← 1`, `bT₀: F ← F′`. If a = b = 1 during T₀, what do J and K become, and is
   the spec sound?

---
---

## Answers

**A2 Q9–Q10:** answer key added after 16-09-2026, 16:30. Send your answers for marking.

**Self-test 1.** Statements: pB₇: IEN ← 1 · pB₆: IEN ← 0 · RT₂: IEN ← 0.
J = pB₇, K = pB₆ + RT₂.

**Self-test 2.**
```
   LD(AR)  = R′T₀ + R′T₂ + D₇′IT₃          (← PC, ← IR(0-11), ← M[AR])
   INR(AR) = D₅T₄                            (BSA)
   CLR(AR) = RT₀                             (interrupt)
```

**Self-test 3.**
```
   CLR(SC) = RT₂ + D₇I′T₃ + D₇IT₃ + (D₀ + D₁ + D₂ + D₅)T₅ + (D₃ + D₄)T₄ + D₆T₆
           = RT₂ + D₇T₃ + (D₀ + D₁ + D₂ + D₅)T₅ + (D₃ + D₄)T₄ + D₆T₆
```
(I′ + I = 1 merges the RRI and I/O terms.)

**Self-test 4.** LD(TR) = RT₀; INR(TR) = 0; CLR(TR) = 0.

**Self-test 5.** J = aT₀ + bT₀ = 1, K = bT₀ = 1 → F complements, not sets. The spec is contradictory:
two different transfers to one flip-flop under the same condition. Mutually exclusive control
functions are a requirement of every RTL description.
