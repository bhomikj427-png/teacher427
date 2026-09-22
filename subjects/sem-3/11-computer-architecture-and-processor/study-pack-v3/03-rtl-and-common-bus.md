# 03 — RTL and the common bus

**Assignment 1: Q10–Q14 · 40 of 200 marks · U1 (L3–L4) · needs 00, 02**

★ **The highest-value file in the pack.** Every file after this one is written in the notation taught
here, and the bus built here is the thing the Basic Computer (files 06–08) is made of. If one file
gets your best hours, it is this one.

---

## Map

```
   [1] RTL — the notation ───► [2] Control functions ───► [3] RTL → hardware
        R2 ← R1                     P: R2 ← R1                 (a drawing you can
        M[AR], A(L)                 the colon                   be asked to produce)
             │
             ▼
   [4] The n(n−1) problem  ──┬──► [5] Bus from multiplexers
       why a bus exists      │
                             └──► [6] Bus from tri-state buffers + decoder
             │
             ▼
   [7] Memory transfers      [8] What is illegal
       AR and M[AR]              (the viva question)
```

---

## The questions this file answers

| # | Question | Marks | Mano |
|---|---|---|---|
| 1 | `[A1 Q10]` Categories the following as register or memory transfer statements. Explain the operation. | 4 | 4-7 |
| 2 | `[A1 Q11]` Represent as a register transfer statement: If (S = 1) then (AL ← BH). Explain the operation. | 4 | ≈4-3 |
| 3 | `[A1 Q12]` Represent: If (y = 1 && T2 = 1) then (R2 ← R1) and (R1 ← R2). Create a block diagram of the hardware. Explain the circuit. | 8 | 4-1 |
| 4 | `[A1 Q13]` What specifically is a bus? What is its role? List five most popular such structures. | 8 | — |
| 5 | `[A1 Q14]` Draw a common bus system transferring data between four 4-bit registers, using (i) multiplexers (ii) tri-state buffers and a decoder. Explain the working in each case. | 16 | 4-6, 4-5 |

Mano's unasked follow-ups for this file: **4-2, 4-4, 4-8, 4-9, 4-10, 4-11, 4-23.**

---

## Build

### 1 · RTL — the notation

> **Q** `[A1 Q10 · 4 marks]` **≈ Mano 4-7**
> **Categories the following statements as register or memory transfer statement. Explain the
> operation being performed.**
> **i) `A ← B`  ii) `A(L) ← B(H)`  iii) `R1 ← M[AR]`  iv) `M ← R2`**
>
> *You can already read (i) and (iii) from file 00. Guess (ii) and (iv). Then read on.*

**Why a notation exists at all:** describing a digital system in English is ambiguous and unbuildable.
RTL states exactly which register moves what, and when. That is the whole justification, and it is
worth a sentence in any "what is RTL" answer.

This is the entire vocabulary. There is no more.

| Notation | Meaning |
|---|---|
| `R2 ← R1` | contents of R1 are **copied** into R2. **R1 is unchanged** |
| `P: R2 ← R1` | the transfer happens **only if** control function P = 1 |
| `R2(0−7)` | a **field** — part of a register |
| `AR ← DR(AD)` | transfer the AD portion of DR into AR |
| `A ← 1010` | load a binary constant |
| `M[R]` | the memory word **addressed by** register R |
| `M` | shorthand for `M[AR]` |
| `DR ← M` | **memory read** |
| `M ← DR` | **memory write** |
| `A ← B, C ← D` | comma = both happen **simultaneously**, on the same clock edge |

Now the question. The test for "memory transfer" is one thing only: **does `M` appear?**

| Statement | Type | Operation |
|---|---|---|
| `A ← B` | **register** transfer | copy the contents of B into A; B unchanged |
| `A(L) ← B(H)` | **register** transfer | copy the **high** half of B into the **low** half of A — a field transfer, not a whole word |
| `R1 ← M[AR]` | **memory** transfer (read) | take the address in AR, read that memory word, place it in R1 |
| `M ← R2` | **memory** transfer (write) | write R2 into memory at the address held in AR (`M` means `M[AR]`) |

> ✓ **Check 1.** (a) Which of the four leave memory unchanged?
> (b) In `M ← R2`, where does the address come from — it is not written in the statement?
> (c) `[Mano 4-7(c)]` What does `R5 ← M[R5]` do, and why is it legal?

---

### 2 · Control functions — the colon

> **Q** `[A1 Q11 · 4 marks]`
> **Represent the following conditional control statement as a register transfer statement:
> If (S = 1) then (AL ← BH). Explain the operation being performed.**
>
> *Guess how you'd write "only when S = 1" in one line. Then read on.*

A transfer that should happen *sometimes* gets a **control function** in front of a colon:

```
 P :  R2 ← R1
 ▲       ▲
 │       └── the transfer
 └────────── a Boolean condition. When it is 1, the transfer happens at the next
             clock edge. When it is 0, nothing happens at all.
```

So the answer is one line:

```
S: AL ← BH
```

**Explaining it** (the other two marks): when control signal S = 1, the **high byte of register B** is
copied into the **low byte of register A** at the next clock transition; A's high byte and all of B are
unchanged. When S = 0, no transfer occurs.

**The control function may be any Boolean expression**, and usually is — you have already seen
`C₇T₃:` in file 00. `xT₀ + y′T₂:` is a perfectly ordinary control function.

⚠ **The `+` trap, which Mano calls out explicitly.** In a control function, `+` means **OR**. In a
microoperation, `+` means **arithmetic plus**. Same symbol, opposite sides of the colon:

```
 x + yz :  AR ← AR + BR
 └──┬──┘        └──┬──┘
   OR            ADD
```

> ✓ **Check 2.** (a) Write: copy R1 into R3 only when T = 1. (b) In `x + yz: AR ← AR + BR`, how many
> of the three `+` signs mean addition? (c) What happens on the clock edge when the control function
> is 0?

---

### 3 · From RTL to hardware — and the swap

> **Q** `[A1 Q12 · 8 marks]` **= Mano 4-1**
> **Represent the following conditional control statement as a register transfer statement:
> If (y = 1 && T2 = 1) then (R2 ← R1) and (R1 ← R2). Create a block diagram of the hardware that
> implements the register transfer statement. Explain the working of the circuit.**
>
> *Read it carefully: R2 gets R1 and R1 gets R2, at the same time. Guess whether that is even
> possible, and what extra hardware it needs. Then read on.*

Most people answer "impossible — you'd need a temporary register, like in code." **That answer is
wrong, and the question is set to catch it.**

The statement in RTL:

```
yT₂: R2 ← R1, R1 ← R2
```

The comma means simultaneous. And in hardware, simultaneous exchange is **free** — no temporary
register, no extra step.

**Why.** An RTL statement is a *hardware specification*, not a program statement. `R2 ← R1` compiles
to: R1's outputs are wired to R2's inputs, and LD(R2) is asserted so that **at the clock edge** R2
captures what is on its inputs. Both registers read the other's **old** value during the whole clock
period; both capture at the same edge. There is no moment at which one has already changed and the
other has not.

That is the deepest idea in this file, and it is what makes RTL different from code.

**The block diagram:**

```
                  ┌───────────────────────────────┐
                  │                               │
              ┌───▼───┐                       ┌───┴───┐
    ──────────│  R1   │───────────────────────►  R2   │
              │       │◄──────────────────────│       │
              └───▲───┘                       └───▲───┘
                  │ LD                            │ LD
                  └──────────┬────────────────────┘
                             │
                   ┌─────────┴─────────┐
              y ──►│       AND         │
             T₂ ──►│                   │
                   └─────────┬─────────┘
                             ▼
                   LD of both registers      CLK ──► both registers
```

**Explaining the circuit** (this is where the 8 marks are):
1. R1's data outputs go to R2's data inputs; R2's outputs go to R1's inputs — two parallel n-bit paths.
2. y and T₂ feed a **two-input AND gate**, whose output drives the **LD** input of *both* registers.
3. The clock is common and is **never gated** (file 02, step 5).
4. When y = T₂ = 1, both LD inputs are 1, so at the next positive clock edge both registers load
   whatever is on their inputs — which is the other's previous content. The values exchange in one
   clock pulse.

> ✓ **Check 3.** (a) Why is no temporary register needed? (b) What single gate implements the control
> function `yT₂`? (c) What would go wrong if you AND-ed y and T₂ with the clock instead of driving LD?
> (d) `[Mano 4-8]` Sketch the control gating for `x + yz: AR ← AR + BR`.

---

### 4 · Why a bus exists — the n(n−1) problem

> **Q** `[A1 Q13 · 8 marks]`
> **What specifically is a bus in the context of computer architecture? What is its role? List the
> names of five most popular such structures.**
>
> *Guess the role first — and note that "it carries data" is worth almost nothing. Then read on.*

The role is not "carrying data". It is **avoiding a counting disaster**, and stating the count is what
earns the marks.

**The problem.** To wire n registers so that any one can load from any other, using point-to-point
paths, needs **n(n − 1)** sets of lines. For 4 registers that is 12. For 16 it is 240. Mano's own words:
*"this is not a realistic approach to use in a large digital system."* The cost grows as O(n²).

**The fix.** A **bus** — *a path (a group of wires) over which information is transferred from any of
several sources to any of several destinations*. One shared path, **time-shared** so that exactly one
source drives it at a time. n(n−1) paths collapse to one.

**Definition to write:** a shared set of wires connecting several sources to several destinations, on
which only one source may drive at any moment; a **system bus** has three functional groups of lines:

| Group | Carries |
|---|---|
| **Data lines** | the word being transferred |
| **Address lines** | which memory location or I/O port |
| **Control lines** | read/write, timing, interrupt, bus request/grant |

**Five popular bus standards** (he asks for names — give years and one word of character):

| Bus | Year | Character |
|---|---|---|
| **ISA** — Industry Standard Architecture | 1981 (8-bit), 1984 (16-bit) | the original IBM PC expansion bus |
| **EISA** — Extended ISA | 1988 | 32-bit, ISA-compatible |
| **VESA Local Bus (VLB)** | 1992 | 32-bit at processor local-bus speed; short-lived |
| **PCI** — Peripheral Component Interconnect | 1992 | processor-independent, 32-bit at 33 MHz; dominant by the mid-1990s |
| **SCSI** — Small Computer System Interface | ANSI X3.131 | parallel bus for disks and peripherals |
| **USB** — Universal Serial Bus | 1996 | serial, hot-pluggable |
| **PCIe** — PCI Express | 2003 | serial point-to-point links; a "bus" in name only |

Any five. **Bus transfer notation:** `BUS ← R1, R2 ← BUS`, usually abbreviated to just `R2 ← R1`.

> ✓ **Check 4.** (a) How many point-to-point paths to fully connect 8 registers? (b) Name the three
> functional groups of lines in a system bus. (c) Why can only one source drive the bus at a time?

---

### 5 · Common bus from multiplexers

> **Q** `[A1 Q14(i) · 8 marks]` **≈ Mano 4-6**
> **Draw a neatly labelled diagram of a common bus system that facilitates the transfer of data
> between four registers each of which is 4-bits, using multiplexers. Explain the working.**
>
> *From file 02: a MUX picks one source. Guess how many MUXes you need here — and resist the obvious
> answer of "one per register". Then read on.*

The common wrong answer is 4 MUXes because there are 4 registers, which happens to be right here **for
the wrong reason** — and that reason breaks the moment the numbers change.

**The sizing rule.** To bus **k registers of n bits** with multiplexers you need:

> **n multiplexers, each k-to-1** — one MUX **per bit position**, each choosing among the k registers'
> corresponding bits. Select lines: **⌈log₂ k⌉**, shared by all n MUXes.

Here k = 4 registers, n = 4 bits → **4 MUXes, each 4-to-1, 2 select lines (S₁S₀).**

```
            A₃ B₃ C₃ D₃   A₂ B₂ C₂ D₂   A₁ B₁ C₁ D₁   A₀ B₀ C₀ D₀
             │  │  │  │    │  │  │  │    │  │  │  │    │  │  │  │
            ┌▼──▼──▼──▼┐  ┌▼──▼──▼──▼┐  ┌▼──▼──▼──▼┐  ┌▼──▼──▼──▼┐
            │  4×1 MUX │  │  4×1 MUX │  │  4×1 MUX │  │  4×1 MUX │
            └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
                 │             │             │             │
   S₁ S₀ ────────┴─────────────┴─────────────┴─────────────┘
   (common)      │             │             │             │
              BUS₃          BUS₂          BUS₁          BUS₀
```

**Working, explained:**
1. MUX *j* receives bit *j* of **all four** registers — so MUX 3 sees A₃, B₃, C₃, D₃.
2. All four MUXes share the same S₁S₀, so they all select the **same register**. That is the point of
   sharing: a per-MUX select would splice bits from different registers together.
3. S₁S₀ = 00 puts register A on the bus, 01 puts B, 10 puts C, 11 puts D.
4. The bus is wired to the **inputs of every register**. The destination is chosen separately, by
   asserting that register's **LD** (file 02, step 5). Source = select lines; destination = load line.

| S₁ | S₀ | Register on the bus |
|---|---|---|
| 0 | 0 | A |
| 0 | 1 | B |
| 1 | 0 | C |
| 1 | 1 | D |

**Say this in the exam:** the select lines choose the **source**; the LD inputs choose the
**destination**; `C ← A` is therefore S₁S₀ = 00 with LD(C) = 1.

> ✓ **Check 5.** (a) How many MUXes, of what size, for **8 registers of 16 bits**?
> (b) `[Mano 4-6]` 16 registers of 32 bits: how many selection inputs per MUX, what size MUX, how many
> MUXes? (c) Why is one shared set of select lines used rather than one per MUX?

---

### 6 · Common bus from tri-state buffers and a decoder

> **Q** `[A1 Q14(ii) · 8 marks]` **= Mano 4-5**
> **Same bus, same four 4-bit registers — but built with tri-state buffers and a decoder instead.
> Explain the working.**
>
> *A MUX has one output wire. Guess what has to be true if you instead let four registers all connect
> to the same wire. Then read on.*

If four outputs are wired to one line and two of them drive different values, you get a short circuit.
So the second construction needs a component that can **disconnect itself**.

**Tri-state buffer.** An ordinary gate outputs 0 or 1. A tri-state buffer has a **third** state:

```
        control C
            │
            ▼
  in ──────►│▶──────► out
```

| C | Output |
|---|---|
| 1 | = input (0 or 1) |
| 0 | **high-impedance (Hi-Z)** — electrically disconnected, as if the wire were cut |

That third state is what makes shared wiring safe.

**The construction:** one buffer per register per bit line — **4 registers × 4 bits = 16 buffers** —
with all four buffers of a given bit position wired to the same bus line. A **2-to-4 decoder** (file
02, step 2) takes the same S₁S₀ and produces four enable lines, **exactly one active**, driving the
four buffers of one register.

```
             S₁ S₀
               │
        ┌──────▼──────┐
        │  2-to-4     │  E₀ ──► the four buffers of register A
        │  decoder    │  E₁ ──► the four buffers of register B
        │             │  E₂ ──► … C
        └─────────────┘  E₃ ──► … D

   A₃ ─►│▶─┐
   B₃ ─►│▶─┤
   C₃ ─►│▶─┼──────────► BUS₃        (same pattern for bits 2, 1, 0)
   D₃ ─►│▶─┘
```

**Working:** the decoder guarantees exactly one enable is 1, so exactly one register's buffers are
driving; the other twelve are in Hi-Z and are invisible to the bus. Selection is otherwise identical
to the MUX version — S₁S₀ picks the source, LD picks the destination.

**Comparing the two — this is what the "explain the working in each case" half is really asking:**

| | Multiplexers | Tri-state buffers + decoder |
|---|---|---|
| Hardware | n MUXes of k inputs | n × k buffers + one decoder |
| Selection done by | the MUX select lines | the decoder's enable outputs |
| Bus line is | a MUX **output** | a shared wire driven by whoever is enabled |
| Scales to many registers | poorly (MUX inputs grow) | **well** — add a buffer, widen the decoder |
| Danger | none | **two enables at once = short circuit** |
| Used in | small, on-chip selection | real system buses |

> ✓ **Check 6.** (a) How many tri-state buffers for 8 registers of 16 bits? (b) What exactly does the
> decoder guarantee that makes this safe? (c) Name the third state and say what it means electrically.

---

### 7 · Memory transfers

> **Q** `[Mano 4-7 · not yet asked in full]`
> **The following transfer statements specify a memory. Explain the memory operation in each case:
> a) `R2 ← M[AR]`  b) `M[AR] ← R3`  c) `R5 ← M[R5]`**
>
> *You answered (a) and (b) in step 1. Guess what makes (c) different. Then read on.*

Memory is reached in exactly one way: **an address register holds the address**. In the Basic Computer
that register is always **AR**, which is why `M` alone means `M[AR]`.

| Statement | Operation | What happens on the wires |
|---|---|---|
| `DR ← M[AR]` | **read** | AR drives the memory address lines; the read control line is activated; the memory's data output is loaded into DR at the clock edge |
| `M[AR] ← DR` | **write** | AR drives the address lines; DR drives the data input lines; the write control line is activated |

**An m × n memory** is m words of n bits. **k address lines select one of 2ᵏ words** — so 4096 words
needs 12 address lines (file 00, step 4), and the data lines number n.

Part (c), `R5 ← M[R5]`, is the interesting one: **R5 supplies the address and also receives the word
read from it.** It is legal for exactly the reason the swap in step 3 was legal — R5's *old* value is
on the address lines throughout the cycle, and the new value is captured only at the edge. This is
precisely the mechanism of **indirect addressing**, which is where file 06 goes.

> ✓ **Check 7.** (a) How many address lines does a 65,536-word memory need?
> (b) Which register must be loaded before any memory access can happen?
> (c) Write RTL for: read the word at the address in AR into DR, then add it to AC. (Two statements.)

---

### 8 · What is illegal

> **Q** `[Mano 4-23 · not yet asked — and a standard viva question]`
> **What is wrong with the following register transfer statements?**
> **a) `xT: AR ← AR, AR ← 0`  b) `yT: R1 ← R2, R1 ← R3`  c) `zT: PC ← AR, PC ← PC + 1`**
>
> *Step 3 said simultaneous transfers are fine. Guess why these three are not. Then read on.*

Step 3's rule has a limit, and this question is where it bites. Simultaneous transfers are legal when
they have **different destinations**. All three of these have the **same destination twice**:

| | Problem |
|---|---|
| (a) | AR is told to load **itself** and to load **0** at the same edge. One register, one set of inputs, two conflicting values. |
| (b) | R1 is told to load R2 **and** R3 on the same edge. Same conflict. |
| (c) | PC is told to load AR **and** to load PC + 1 on the same edge. Same conflict. |

**The rule, stated properly:** two microoperations may share a clock pulse if and only if they write
to **different destination registers**. The destination is a single set of flip-flops with a single set
of D inputs; it can capture exactly one value per edge.

The fix in each case is to put the two transfers in **consecutive timing steps** — which is exactly
what `T₀, T₁, T₂ …` are for, and why `ADD 201` takes several ticks (file 01, step 3).

> ✓ **Check 8.** (a) State the rule in one sentence. (b) Is `yT₂: R2 ← R1, R1 ← R2` legal? Why does it
> not break the rule? (c) Rewrite (c) above as two legal timed statements.

---

## Exam form

### The RTL vocabulary table

Reproduce the table in step 1. Nothing else is needed — that is the whole language.

### Bus sizing — memorise both constructions

| | Multiplexer bus | Tri-state bus |
|---|---|---|
| For **k registers of n bits** | **n** MUXes, each **k-to-1** | **n × k** buffers + one **k-output decoder** |
| Select lines | ⌈log₂ k⌉, shared | ⌈log₂ k⌉ into the decoder |
| Worked: 4 registers × 4 bits | 4 MUXes, 4-to-1, 2 select lines | 16 buffers + 2-to-4 decoder |
| Worked: 16 registers × 32 bits | 32 MUXes, 16-to-1, 4 select lines | 512 buffers + 4-to-16 decoder |

### Source and destination

> **Select lines choose the source. LD lines choose the destination.**

`C ← A` on a 4-register bus = `S₁S₀ = 00` **and** `LD(C) = 1`. Every bus-control question in file 06
is this sentence applied.

### Definitions

| Term | Write |
|---|---|
| **Bus** | A path (a group of wires) over which information is transferred from any of several sources to any of several destinations; only one source drives it at a time. Replaces n(n−1) point-to-point links with one shared, time-shared path. |
| **Tri-state buffer** | A gate whose output can be 0, 1, or a **high-impedance** state in which it is electrically disconnected from the line, allowing many outputs to share one wire. |
| **Register transfer language** | A symbolic notation describing the microoperations among registers and the control conditions under which they occur, e.g. `P: R2 ← R1`. |

---

## Attempt

On paper, in order:

1. `[A1 Q10 · 4]` all four statements, categorised and explained.
2. `[A1 Q11 · 4]` the RTL line **plus** the explanation — the explanation is half the marks.
3. `[A1 Q12 · 8]` RTL, block diagram, and the working. Say explicitly why no temporary register is needed.
4. `[A1 Q13 · 8]` definition, role **stated as the n(n−1) count**, three line groups, five named standards.
5. `[A1 Q14 · 16]` both bus constructions, drawn and explained, with the comparison.

Then from Mano: **4-2** (four registers into R5 via MUXes), **4-4** (any-to-any on Fig. 4-3),
**4-8**, **4-9** (control gating), **4-10**, **4-11**, **4-23**.

---

## Traps

| Trap | Correction |
|---|---|
| "A simultaneous swap needs a temp register" | It does not. Both registers read the old values and capture at the same edge |
| Bus role = "it carries data" | The role is replacing **n(n−1)** paths with one. State the count |
| One MUX per register | **One MUX per bit position**, each with one input per register |
| Separate select lines per MUX | Shared — otherwise you splice bits from different registers |
| `+` always means addition | Left of the colon it means **OR** |
| Forgetting LD when asked for a transfer | Select lines give the source only; the destination needs its LD asserted |
| Two enables active on a tri-state bus | Short circuit. The decoder exists to prevent it |
| `R1 ← R2, R1 ← R3` looks like the legal swap | Same **destination** twice — illegal. The swap had two different destinations |

---

## Self-test

1. `M ← R2` — where does the address come from, and what type of transfer is it?
2. Write RTL: when x = 1 and T₃ = 1, copy the low byte of R1 into the high byte of R2.
3. 12 registers of 8 bits on a MUX bus: how many MUXes, what size, how many select lines?
4. Same 12 registers on a tri-state bus: how many buffers, and what decoder?
5. Why is `R5 ← M[R5]` legal?
6. Give the two control settings needed to perform `B ← D` on the four-register bus of step 5.
7. Which of these can share one clock pulse? `AC ← DR, DR ← AC` · `PC ← AR, PC ← PC + 1`

---
---

## Answers

**Check 1.** (a) (i) and (ii) — no `M` appears. (b) From **AR**; `M` is shorthand for `M[AR]`, so the
address register is implied by the notation. (c) R5 supplies the address *and* receives the word
found there. Legal because the old R5 drives the address lines for the whole cycle and the new value
is captured only at the clock edge.

**Check 2.** (a) `T: R3 ← R1`. (b) **One** — the `+` in `AR + BR`. The other two are ORs in the control
function. (c) Nothing. The registers still tick, but their LD inputs are 0, so they reload their own
contents.

**Check 3.** (a) Both registers read the other's **old** contents throughout the clock period and both
capture at the same edge; there is no instant at which one has updated and the other has not.
(b) A two-input **AND** gate. (c) Clock skew — those registers would capture later than all the others
(file 02, step 5). Gate the **data/LD**, never the clock. (d) One AND gate for `yz`, feeding an OR gate
with x; the OR output drives LD(AR), with the adder's output wired to AR's inputs.

**Check 4.** (a) 8 × 7 = **56**. (b) **Data, address, control** lines. (c) Because all sources share one
set of physical wires — two drivers with different values would short.

**Check 5.** (a) **16 MUXes** (one per bit), each **8-to-1**, 3 select lines. (b) 16 registers → **4
selection inputs**; **16-to-1** MUXes; **32** of them (one per bit). (c) All bit positions must select
the *same* register; separate selects would splice bits from different registers into one bus word.

**Check 6.** (a) 8 × 16 = **128 buffers**, plus a 3-to-8 decoder. (b) That **exactly one** enable line
is active at a time, so only one register drives the bus. (c) **High-impedance (Hi-Z)** — the output is
electrically disconnected, as though the wire were cut.

**Check 7.** (a) 65,536 = 2¹⁶ → **16**. (b) **AR**. (c) `DR ← M[AR]` then `AC ← AC + DR` — two
statements, two clock pulses, because one adder cannot reach memory directly.

**Check 8.** (a) Two microoperations may share a clock pulse **only if their destination registers are
different**. (b) **Legal** — the destinations are R2 and R1, which are different. The illegal cases all
write the same register twice. (c) `zT₁: PC ← AR` then `zT₂: PC ← PC + 1` (any two distinct timing
signals).

**Self-test 1.** From **AR** (`M` = `M[AR]`); it is a **memory write**.

**Self-test 2.** `xT₃: R2(H) ← R1(L)`

**Self-test 3.** **8 MUXes** (one per bit), each **12-to-1**, **4** select lines (⌈log₂ 12⌉ = 4).

**Self-test 4.** 12 × 8 = **96 buffers**, plus a **4-to-16 decoder** (only 12 outputs used).

**Self-test 5.** The old contents of R5 drive the address lines throughout the cycle; the word read is
captured at the clock edge. Nothing is read from a register that has already changed.

**Self-test 6.** `S₁S₀ = 11` (puts D on the bus) **and** `LD(B) = 1`.

**Self-test 7.** `AC ← DR, DR ← AC` **can** — different destinations. `PC ← AR, PC ← PC + 1` **cannot**
— same destination twice.

---

## What to do next

File 04 next: the operations that run *on* the data this bus moves — arithmetic, logic and shift
microoperations, plus the signed-number questions A1 Q8 and Q9. After that, file 05 assembles all of
them into the ALSU, which is A1's single biggest technical question.
