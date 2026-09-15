# 03 — RTL, Conditional Transfers and the Common Bus

**Assignment 1: Q10, Q11, Q12, Q13, Q14 · 48 of 200 marks · U1 (L3–L5)**

Everything in files 05–08 is written in this notation. An RTL statement is a **hardware
specification**: a data path + a load line + a clock edge.

---

## Map

```
   RTL statement  ──►  what it compiles to in hardware
   P: R2 ← R1          R1's outputs → R2's inputs, P → LD(R2), transfer on the clock edge
        │
        ▼
   Too many registers? n(n−1) wires
        │
        ▼
   Common bus ──► (i) one MUX per bit          (ii) tri-state buffers + decoder
        │
        ▼
   Memory transfers: M[AR] read / write
```

---

## Attempt

1. Classify as **register** or **memory** transfer and explain the operation:
   **(i)** `A ← B` **(ii)** `A(L) ← B(H)` **(iii)** `R1 ← M[AR]` **(iv)** `M ← R2`
2. Write `If (S = 1) then (AL ← BH)` as a register transfer statement. Explain it.
3. Write `If (y = 1 && T2 = 1) then (R2 ← R1) and (R1 ← R2)` as a register transfer statement. Draw
   the block diagram of the hardware and explain its working.
4. What is a bus? What is its role? Name five popular bus structures.
5. Draw a common bus system for **four 4-bit registers** using **(i)** multiplexers **(ii)** tri-state
   buffers and a decoder. Explain each.

---

## Learn

### RTL vocabulary

| Notation | Meaning |
|---|---|
| `R2 ← R1` | copy R1 into R2; R1 unchanged |
| `P: R2 ← R1` | only when control function P = 1 |
| `R2(0-7)`, `R(L)`, `R(H)` | a field: bits 0–7, low half, high half |
| `M[AR]` | memory word addressed by AR |
| `M` | shorthand for `M[AR]` |
| `DR ← M[AR]` | **memory read** |
| `M[AR] ← DR` | **memory write** |
| `A ← B, B ← A` | comma = **simultaneous**, same clock edge |
| `xT₂:` | control function = x AND T₂ |

**Register transfer vs memory transfer:** a register transfer has registers on both sides. A memory
transfer has `M[…]` (or `M`) on one side: on the right it is a **read**, on the left a **write**.

### What `P: R2 ← R1` is in hardware

```
                     n lines
   ┌────┐  ───────────────────────►  ┌────┐
   │ R1 │                            │ R2 │
   └────┘                   P ──────►│ LD │
                        Clock ──────►│ >  │
                                     └────┘
```

Timing — P is produced by the control unit **after** one clock edge, stays 1 for the cycle, and the
transfer happens **on the next edge**, when LD(R2) = 1:

```
   Clock   ─┐_┌─┐_┌─┐_┌─┐_┌─
               t        t+1
   P       ____┌────────┐____
                        ↑ R2 ← R1 happens here
```

### The problem a bus solves

n registers fully interconnected need **n(n − 1)** sets of lines. A **bus** is one shared set of lines
that any source can drive and any destination can load from — **one source at a time**.

**System bus = three line groups:** data lines (the word) · address lines (where) · control lines
(read, write, timing, interrupt, bus request/grant).

**Named bus standards:**

| Bus | Year | Note |
|---|---|---|
| ISA | 1981 / 1984 | IBM PC and PC/AT expansion bus |
| EISA | 1988 | 32-bit extension of ISA |
| VESA Local Bus | 1992 | 32-bit, processor-speed, short-lived |
| **PCI** | 1992 | processor-independent; dominant through the 1990s |
| **SCSI** | ANSI X3.131 | parallel bus for disks and peripherals |
| **USB** | 1996 | serial, hot-pluggable |
| PCI Express | 2003 | serial point-to-point links replacing PCI |

Hamacher's textbook examples are **PCI, SCSI, USB**. Name those three plus ISA and PCIe for "five".

### (i) Bus from multiplexers

For **k registers of n bits**: **n** multiplexers, each **k-to-1**, sharing ⌈log₂ k⌉ select lines.
Four 4-bit registers → **four 4-to-1 MUXes, 2 select lines, a 4-line bus.**

```
         A₃ B₃ C₃ D₃        A₂ B₂ C₂ D₂        A₁ B₁ C₁ D₁        A₀ B₀ C₀ D₀
          │  │  │  │         │  │  │  │         │  │  │  │         │  │  │  │
        ┌─┴──┴──┴──┴─┐     ┌─┴──┴──┴──┴─┐     ┌─┴──┴──┴──┴─┐     ┌─┴──┴──┴──┴─┐
  S₁ ──►│  0  1  2  3│ ──► │  0  1  2  3│ ──► │  0  1  2  3│ ──► │  0  1  2  3│
  S₀ ──►│  MUX 3     │     │  MUX 2     │     │  MUX 1     │     │  MUX 0     │
        └─────┬──────┘     └─────┬──────┘     └─────┬──────┘     └─────┬──────┘
              │                  │                  │                  │
   bus ═══════╪══════════════════╪══════════════════╪══════════════════╪═══ 4 lines
              3                  2                  1                  0
              └──── each bus line goes to the same-numbered input of all four registers
```

| S₁ | S₀ | Register on bus |
|---|---|---|
| 0 | 0 | A |
| 0 | 1 | B |
| 1 | 0 | C |
| 1 | 1 | D |

**Working:** bit i of every register goes into MUX i, at the input matching that register's code.
The common S₁S₀ makes all four MUXes pick the **same** register, so its whole word appears on the bus.
The destination is whichever register has **LD = 1** at the clock edge.
*Example:* `C ← A` → S₁S₀ = 00, LD(C) = 1, clock.

### (ii) Bus from tri-state buffers + decoder

A **tri-state buffer** has a data input and an enable: enable = 1 → output = input; enable = 0 →
output is **high impedance** (electrically disconnected). Many outputs can then share one wire.

```
                         ┌─────────────┐
   S₁ ──────────────────►│  2-to-4     │── D₀ ── enables A's 4 buffers
   S₀ ──────────────────►│  decoder    │── D₁ ── enables B's 4 buffers
   E (bus enable) ──────►│             │── D₂ ── enables C's 4 buffers
                         └─────────────┘── D₃ ── enables D's 4 buffers

   One bus line (repeat for lines 0–3):

   A₀ ──▷── ┐      each ▷ is a tri-state buffer,
            │      its enable from the decoder output
   B₀ ──▷── ┤
            ├════ bus line 0
   C₀ ──▷── ┤
            │
   D₀ ──▷── ┘
```

**16 buffers** (4 per register), one 2-to-4 decoder.

**Working:** the decoder raises exactly one output, enabling one register's four buffers; the other 12
are in high impedance, so exactly one register drives each line. **E = 0** puts all 16 in high
impedance — the bus floats, nobody drives it. Destination chosen by LD, as before.

**MUX vs tri-state:** the MUX version is a logic circuit that always outputs something. The tri-state
version lets the bus wires physically run past every register and supports **bidirectional** buses
(e.g. memory's data lines), which a MUX cannot.

---

## Worked (A1 — full answers)

**Q10.**

| | Type | Operation |
|---|---|---|
| (i) `A ← B` | register transfer | all bits of B copied into A; B unchanged |
| (ii) `A(L) ← B(H)` | register transfer (partial) | high-order half of B copied into low-order half of A; A(H) and B unchanged |
| (iii) `R1 ← M[AR]` | memory transfer — **read** | word at the address held in AR copied into R1 |
| (iv) `M ← R2` | memory transfer — **write** | R2 written into the word addressed by AR (M = M[AR]) |

**Q11.**
```
   S: AL ← BH
```
When S = 1, at the next clock edge the high half of B is loaded into the low half of A. Hardware: BH's
outputs wired to AL's inputs; S drives LD(AL); AH has no load and keeps its value. When S = 0 nothing
changes.

**Q12.**
```
   yT₂: R2 ← R1, R1 ← R2
```

```
   y  ──┐
        [AND]──── P = yT₂ ────┬──────────────► LD(R1)
   T₂ ──┘                     └──────────────► LD(R2)

          ┌──────┐   R1 outputs (n lines)   ┌──────┐
          │  R1  │ ───────────────────────► │  R2  │
          │      │ ◄─────────────────────── │      │
          └──────┘   R2 outputs (n lines)   └──────┘
             ▲                                  ▲
   Clock ────┴──────────────────────────────────┘
```

**Working:** the AND gate forms the control function P = y·T₂. P drives both load inputs, so both
registers load on the **same** clock edge. Each register's inputs are wired to the other's outputs.
The flip-flops sample their inputs at the edge and change only afterwards, so R1 captures R2's **old**
value and R2 captures R1's **old** value — a swap, with no temporary register. In software this would
need a temp; in hardware it does not.

**Q13.** A bus is a group of shared wires carrying information from any of several sources to any of
several destinations, with only one source active at a time. **Role:** it interconnects CPU, memory
and I/O without n(n−1) dedicated links; it carries data, addresses and control signals. **Five
structures:** ISA, EISA, PCI, SCSI, USB (PCI Express also acceptable).

**Q14.** The two diagrams, tables and working paragraphs in Learn.

---

## Traps

| Trap | Correction |
|---|---|
| `M ← R2` called a register transfer | M means M[AR] — it is a memory **write** |
| Q12 drawn with a temporary register | Not needed: both registers load on one edge from each other's old outputs |
| Drawing P as a clock | P goes to **LD**; the clock is separate and common |
| MUX bus with one MUX per register | One MUX per **bit**, each with one input per register |
| Tri-state bus: "0 when disabled" | High **impedance**, not logic 0 — that is the point |
| Forgetting what loads | Selecting a source does nothing unless a destination's LD is 1 |

---

## Self-test

1. Eight registers of 16 bits on a MUX bus: how many MUXes, of what size, how many select lines?
2. Same system with tri-state buffers: how many buffers, what decoder?
3. Write RTL: when x = 1 and T₁ = 1, load R3 with R1; otherwise when T₁ = 1, load R3 with R2.
4. Is `R1 ← R2, R1 ← R3` legal? Why or why not?
5. For the 4-register MUX bus, give S₁S₀ and the LD line for `A ← D`.

---
---

## Answers

**Attempt 1–5.** See Worked.

**Self-test 1.** 16 multiplexers, each 8-to-1, 3 select lines.

**Self-test 2.** 8 × 16 = 128 tri-state buffers; a 3-to-8 decoder (with enable).

**Self-test 3.**
```
   xT₁:  R3 ← R1
   x′T₁: R3 ← R2
```
Hardware: a 2-to-1 MUX per bit in front of R3, select = x; LD(R3) = T₁.

**Self-test 4.** Illegal. Two different values cannot be loaded into one register on the same edge.

**Self-test 5.** S₁S₀ = 11 (D on the bus), LD(A) = 1.
