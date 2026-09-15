# 06 — Instruction Format Sizing, Bus Control, Hex Decoding

**Assignment 2: Q1, Q2, Q3, Q4 · 40 of 150 marks · U2 (L9–L10)**
Source problems: Mano 5-1, 5-3, 5-4, 5-6.

A2 answer policy: method + fully worked twin here; A2's own key after 16-09-2026 16:30.

---

## Map

```
   Memory size ──► address bits ──► instruction word format (I | opcode | reg | address)
                                            │
   Basic Computer (4096 × 16):              ▼
   8 registers on one 16-bit bus ──► S₂S₁S₀ selects the source
                                     LD / memory write selects the destination
                                     adder-logic circuit feeds AC
                                            │
                                            ▼
                     16-bit word ──► hex ──► opcode + I ──► MRI / RRI / IO ──► meaning
```

---

## Attempt

**A2 Q1.** A memory has 256K words of 32 bits. An instruction in one word has an indirect bit, an
opcode, a register code for one of 64 registers, and an address.
(a) Bits in the opcode, register code and address? (b) Draw the format. (c) Bits in the memory's data
and address inputs?

**A2 Q2.** In the BC common bus, give the transfer executed on the next clock for:

| | S₂ | S₁ | S₀ | LD of | Memory | Adder |
|---|---|---|---|---|---|---|
| a | 1 | 1 | 1 | IR | Read | — |
| b | 1 | 1 | 0 | PC | — | — |
| c | 1 | 0 | 0 | DR | Write | — |
| d | 0 | 0 | 0 | AC | — | Add |

**A2 Q3.** For each transfer give (1) S₂S₁S₀ (2) the register with LD active (3) memory read/write
(4) the adder-logic operation:
(a) `AR ← PC` (b) `IR ← M[AR]` (c) `M[AR] ← TR` (d) `AC ← DR, DR ← AC` simultaneously.

**A2 Q4.** For (a) `1011 0001 0010 0100` and (b) `0111 0000 0010 0000`: (i) hex code (ii) what the
instruction does.

---

## Learn

### Sizing an instruction word

1. **Address bits** = log₂(number of words). Use **K = 2¹⁰**, **M = 2²⁰**.
2. **Register-code bits** = log₂(number of registers).
3. **Mode bit** I = 1 bit.
4. **Opcode bits** = word length − everything else.
5. Memory **data inputs** = word length; **address inputs** = address bits.

### The Basic Computer's common bus

| S₂S₁S₀ | Source on bus |
|---|---|
| 000 | none |
| 001 | AR |
| 010 | PC |
| 011 | DR |
| 100 | AC |
| 101 | IR |
| 110 | TR |
| 111 | Memory (with Read) |

**Rules that answer every question of this type:**

- One source per clock: **S₂S₁S₀**.
- Destination = every register whose **LD** is 1, and/or **memory Write** (writes the bus into M[AR]).
- **Several destinations can load from the bus on the same edge.**
- **AC never loads from the bus.** AC loads from the **adder-and-logic circuit**, whose inputs are AC,
  DR and INPR. So `AC ← DR` is "LD(AC), adder-logic set to *transfer DR*", independent of S₂S₁S₀.
- DR and AC both have LD, INR, CLR; IR has LD only.
- AR and PC are 12-bit: they put 0s on the bus's top 4 lines.

### Why `AC ← DR, DR ← AC` works in one clock

AC drives the bus (S = 100) → DR loads the bus. At the same edge, AC loads DR's **old** value through
the adder-logic circuit. Two different paths, one edge, old values captured — a swap.

### Decoding a 16-bit BC instruction

```
   bit   15 | 14 13 12 | 11 ………………… 0
          I |  opcode  |   address / operation bits
```

| Opcode | I | Type | Low 12 bits |
|---|---|---|---|
| 000–110 | 0 | MRI, direct | address |
| 000–110 | 1 | MRI, indirect | address of the address |
| 111 | 0 | register-reference (hex 7xxx) | one-hot operation |
| 111 | 1 | input-output (hex Fxxx) | one-hot operation |

**MRI opcodes:** 000 AND · 001 ADD · 010 LDA · 011 STA · 100 BUN · 101 BSA · 110 ISZ

**Hex quick-read of the first digit:** 0–6 = direct MRI; 8–E = indirect MRI (8 = AND … E = ISZ);
7 = RRI; F = I/O.

**RRI codes:** 7800 CLA · 7400 CLE · 7200 CMA · 7100 CME · 7080 CIR · 7040 CIL · 7020 INC · 7010 SPA ·
7008 SNA · 7004 SZA · 7002 SZE · 7001 HLT
**I/O codes:** F800 INP · F400 OUT · F200 SKI · F100 SKO · F080 ION · F040 IOF

---

## Worked twins

**Twin of Q1.** 128K words of 24 bits; register code picks one of 8 registers.

```
   128K = 2⁷ × 2¹⁰ = 2¹⁷     → address   = 17 bits
   8    = 2³                 → register  =  3 bits
                               indirect  =  1 bit
   opcode = 24 − 17 − 3 − 1  →  3 bits

   ┌───┬────────┬──────────┬───────────────────┐
   │ I │ opcode │ register │      address      │
   └───┴────────┴──────────┴───────────────────┘
     1      3         3             17            = 24

   memory data inputs = 24, address inputs = 17
```

**Twin of Q2.**

| | S₂S₁S₀ | LD | Memory | Adder | Transfer |
|---|---|---|---|---|---|
| a | 001 | PC | — | — | `PC ← AR` |
| b | 011 | TR | — | — | `TR ← DR` |
| c | 010 | — | Write | — | `M[AR] ← PC` |
| d | 000 | AC | — | AND | `AC ← AC ∧ DR` |

Method: read S₂S₁S₀ → source; LD / Write → destination(s); if LD(AC) is active, the source is the
adder-logic circuit, not the bus.

**Twin of Q3.**

| Transfer | S₂S₁S₀ | LD | Memory | Adder-logic |
|---|---|---|---|---|
| `DR ← M[AR]` | 111 | DR | Read | — |
| `PC ← TR` | 110 | PC | — | — |
| `M[AR] ← AC` | 100 | — | Write | — |
| `AC ← AC + DR` | — (bus unused) | AC | — | Add (also loads E) |

**Twin of Q4.**

```
 (a) 1101 0000 0100 0101 = D045
     I = 1, opcode 101 = BSA, address 045
     → BSA indirect: EA = M[045]. Store the return address (PC) at M[EA],
       branch to EA + 1.   Symbolic: BSA I 045

 (b) 1111 0100 0000 0000 = F400
     opcode 111, I = 1 → I/O instruction; bit 10 set → OUT
     → OUTR ← AC(0-7), FGO ← 0: send AC's low byte to the output device.
```

---

## Traps

| Trap | Correction |
|---|---|
| 256K = 256 × 1000 | K = 1024: 256K = 2¹⁸ |
| Memory address inputs = word length | Address inputs = address bits; data inputs = word length |
| `AC ← DR` with S₂S₁S₀ = 011 and LD(AC) | AC does not load from the bus; set the adder-logic circuit to transfer DR |
| Memory Write needs an LD | No register loads; only the memory write line |
| Two destinations in one clock "illegal" | Legal — two LDs on one bus value; what is illegal is two sources |
| Decoding 7020 as "ADD" | First hex digit 7 → register-reference, not MRI |
| Indirect MRI read as "operand at address" | I = 1: the word at the address holds the operand's **address** |

---

## Self-test

1. 1M words × 36 bits, 128 registers, one indirect bit: sizes of every field?
2. S₂S₁S₀ = 101, LD(AR), no memory, no adder. What transfer, and what arrives in AR?
3. Give all four control items for `TR ← AC`.
4. Decode `0010 0001 1111 0000`.
5. Decode `7004`. When does the next instruction get skipped?

---
---

## Answers

**A2 Q1–Q4:** answer key added after 16-09-2026, 16:30. Send your answers for marking.

**Self-test 1.** Address 20, register 7, I 1, opcode 36 − 28 = 8. Data inputs 36, address inputs 20.

**Self-test 2.** IR on the bus, AR loads: `AR ← IR(0-11)` — AR is 12-bit, so it takes the low 12 bits.
(This is T₂ of the fetch cycle.)

**Self-test 3.** S₂S₁S₀ = 100 (AC), LD(TR), no memory operation, no adder operation.

**Self-test 4.** 21F0: I = 0, opcode 010 = **LDA 1F0** (direct) → `AC ← M[1F0]`.

**Self-test 5.** 7004 = **SZA**: skip the next instruction if AC = 0 (`PC ← PC + 1` when AC = 0).
