# 04 — The Basic Computer: Instruction Codes, Registers, Bus, Instruction Set

**U2, lectures L9–L11 · CO2.** The professor's deck spends **48 pages** on this unit — more than any
other. This file is the machine's anatomy; file 05 is what it does each clock; file 06 is how you
design its control.

⚠ **The Basic Computer is a teaching instrument, not a real chip.** Every number below is a fact about
**Mano's definition**, so Mano is definitionally the authority. There is nothing to "look up" — the
machine is exactly what he says it is.

---

## Map

```
   memory 4096 x 16   ->   12 address bits   ->   16 - 12 - 1 = 3 OPCODE BITS
        |                                              |
        v                                              v
   instruction format:  I | opcode | address     only 8 opcodes possible
        |                                              |
        +--> I = 0 direct, I = 1 indirect              +--> 000..110 = 7 memory-reference
        |                                              +--> 111 with I=0 = register-reference
        v                                              +--> 111 with I=1 = input-output
   8 REGISTERS: AR PC DR AC IR TR INPR OUTR                    = 7 + 12 + 6 = 25 instructions
        |
        +--> widths: addresses 12 bits, words 16 bits, I/O 8 bits
        |
        v
   ONE 16-bit COMMON BUS, selected by S2 S1 S0 (7 sources + idle)
```

---

## Attempt first

1. Memory is 4096 × 16. Derive the number of opcode bits. Do not recall it — derive it.
2. Why is AR 12 bits while DR is 16?
3. `0 ADD 457` sits at location 22; `1 ADD 300` sits at location 35, and location 300 contains 1350.
   Where is each instruction's operand?
4. Indirect addressing is not needed to *reach* more memory here (12 bits already covers all 4096
   words). So what is it for?
5. The Basic Computer has exactly one general-purpose register. What does that buy, and what does it
   cost?
6. `CLA` is 7800 in hex and `HLT` is 7001. What is the pattern, and why must the codes have it?
7. How many instructions in total, split by type?

---

## Method

### Instruction codes and the format

- Memory: **4096 words × 16 bits.** 4096 = 2¹² → **12 bits** select a word.
- An instruction carries an **opcode** (what to do) and an **address** (what to do it to).
- 16 bits − 12 address bits − 1 mode bit = **3 bits of opcode**. That is the whole derivation.

```
 15    14  13  12   11                                  0
+---+--------------+------------------------------------+
| I |    opcode    |              address               |
+---+--------------+------------------------------------+
  1        3                       12
```

**I is the addressing-mode bit: I = 0 → direct, I = 1 → indirect.**

**Effective address (EA)** = the address that can be used **without further modification** to reach
the operand, or as the target of a branch.

| Mode | I | Mechanism | EA |
|---|---|---|---|
| **Direct** | 0 | the address field **is** the operand's address | EA = address field |
| **Indirect** | 1 | the address field points to a **word that holds** the address | EA = M[address field] |

*Worked (the deck's own example):*

```
   location 22:  0 ADD 457     I = 0  ->  operand is in 457
   location 35:  1 ADD 300     I = 1  ->  go to 300, find 1350 there,
                                          the operand is in 1350
```

**Why indirection exists at all.** Not for reach — 12 bits already names all of memory. It is for
**computed addresses**: the pointer word can be changed at run time, which is how arrays, pointers
and parameter passing become possible on a one-accumulator machine. The price is an **extra memory
access** (a whole clock period, T₃).

### The registers

| Register | Bits | Name | Function |
|---|---|---|---|
| **DR** | 16 | Data Register | holds the memory **operand** |
| **AR** | 12 | Address Register | holds the **address for memory** — wired to the address pins |
| **AC** | 16 | Accumulator | the single general-purpose processor register |
| **IR** | 16 | Instruction Register | holds the instruction being executed |
| **PC** | 12 | Program Counter | holds the address of the **next** instruction |
| **TR** | 16 | Temporary Register | scratch, for intermediate results |
| **INPR** | 8 | Input Register | holds one input character |
| **OUTR** | 8 | Output Register | holds one output character |

Plus the **SC** (4-bit sequence counter) and seven flip-flops:

| FF | Meaning |
|---|---|
| **I** | addressing-mode bit of the current instruction |
| **S** | start–stop |
| **E** | extended AC bit — the carry-out of the adder |
| **R** | interrupt (set when an interrupt is to be serviced) |
| **IEN** | interrupt enable |
| **FGI** | input flag |
| **FGO** | output flag |

**The widths are not arbitrary:**
AR and PC hold **addresses** → 12 bits is all an address needs. DR, AC, IR, TR hold **words** → 16.
INPR/OUTR are **8** because the I/O model is one character at a time.

**Why only one general register.** It is what makes the BC an **accumulator machine**: every
arithmetic instruction has one implicit operand (AC) and one memory operand, so the instruction needs
only **one address field** — which is exactly what buys the 3-bit opcode. *Register count and
instruction format are not independent choices.* (RISC-V resolves the same pressure the opposite way:
32 registers and a load/store ISA.)

### The common bus

Six registers and memory share **one 16-bit common bus**, selected by **S₂S₁S₀**:

| S₂S₁S₀ | Source on the bus |
|---|---|
| 000 | (nothing) |
| 001 | **AR** |
| 010 | **PC** |
| 011 | **DR** |
| 100 | **AC** |
| 101 | **IR** |
| 110 | **TR** |
| 111 | **Memory** |

**Rules that get examined:**

- Exactly one source drives the bus per clock; the **destination** is whichever register's **LD** is
  asserted (or memory's **write**).
- **AR and PC are 12-bit**, so when they drive the 16-bit bus the **high-order 4 bits are 0s**.
- **OUTR is 8-bit** and takes the **low-order 8 bits** of the bus.
- **Five registers have LD, INR and CLR** (AR, PC, DR, AC, TR); **IR and OUTR have LD only.**
- **AC's input does not come from the bus.** It comes from the **adder-and-logic circuit**, whose
  inputs are AC, DR and INPR. (This matters in file 06.)
- Memory read = `S₂S₁S₀ = 111` + read asserted. Memory write = write asserted with the bus carrying
  the data.

### The instruction set — 25 instructions, three formats

Distinguished by opcode 111 and the I bit:

- **Memory-reference (MRI):** opcode **000–110** (7 instructions); I selects direct/indirect.
- **Register-reference (RRI):** opcode **111 with I = 0**; the low 12 bits pick the operation.
- **Input–output (IO):** opcode **111 with I = 1**; the low 12 bits pick the operation.

**Memory-reference (7):**

| Symbol | I = 0 | I = 1 | Description |
|---|---|---|---|
| AND | 0xxx | 8xxx | AND memory word to AC |
| ADD | 1xxx | 9xxx | Add memory word to AC |
| LDA | 2xxx | Axxx | Load AC from memory |
| STA | 3xxx | Bxxx | Store AC into memory |
| BUN | 4xxx | Cxxx | Branch unconditionally |
| BSA | 5xxx | Dxxx | Branch and save return address |
| ISZ | 6xxx | Exxx | Increment and skip if zero |

**Register-reference (12) and input–output (6):**

| RRI | Hex | Meaning | | IO | Hex | Meaning |
|---|---|---|---|---|---|---|
| CLA | 7800 | clear AC | | INP | F800 | input character to AC |
| CLE | 7400 | clear E | | OUT | F400 | output character from AC |
| CMA | 7200 | complement AC | | SKI | F200 | skip on input flag |
| CME | 7100 | complement E | | SKO | F100 | skip on output flag |
| CIR | 7080 | circulate right AC and E | | ION | F080 | interrupt on |
| CIL | 7040 | circulate left AC and E | | IOF | F040 | interrupt off |
| INC | 7020 | increment AC | | | | |
| SPA | 7010 | skip if AC positive | | | | |
| SNA | 7008 | skip if AC negative | | | | |
| SZA | 7004 | skip if AC zero | | | | |
| SZE | 7002 | skip if E zero | | | | |
| HLT | 7001 | halt | | | | |

> **7 + 12 + 6 = 25 instructions.**

**★ The hex codes are one-hot, and that is structural, not decorative.** RRI codes are `7` followed
by a **single 1** in the 12-bit field (7800 = bit 11, 7400 = bit 10, … 7001 = bit 0); IO codes are
`F` followed by a single 1 in bits 11 down to 6. The reason: the control logic tests
**`IR(i) = Bᵢ` directly, with no decoder.** A student who memorizes the hex without seeing the
one-hot structure cannot reconstruct a forgotten code; one who sees it can regenerate all 18 from the
bit position.

### Instruction-set completeness

A set is **complete** if it can compute anything computable. The BC qualifies because it covers all
four necessary categories:

| Category | BC instructions |
|---|---|
| Arithmetic / logic / shift | ADD, CMA, INC, CIR, CIL, AND, CLA |
| Data transfer (memory ↔ register) | LDA, STA |
| Control (sequencing, branching) | BUN, BSA, ISZ |
| Input–output | INP, OUT |

*Why these suffice:* AND + CMA give **NAND**, which is functionally complete for logic;
ADD + CMA + INC give subtraction by 2's complement, and hence multiplication and division by
repetition; BUN + ISZ give conditional branching, and hence loops. Everything else is **convenient,
not necessary**.

---

## Worked — decode an instruction from hex (inferred form; the encoding is the deck's)

> **Identify each instruction and say exactly what it does: (a) `2AF3`, (b) `B100`, (c) `7100`,
> (d) `F200`, (e) `7048`.**

**The decoding procedure — always these three steps, in this order:**

```
   step 1:  write the hex as 16 bits, split  I | opcode(3) | address(12)
   step 2:  is the opcode 111?   no  -> memory-reference, read I for the mode
                                 yes -> read I: 0 = register-reference, 1 = input-output
   step 3:  for MRI, the address field is the operand address (or the pointer if I = 1);
            for RRI/IO, find the ONE bit set in the low 12 and look it up
```

**(a) `2AF3`** → `0010 1010 1111 0011` → I = **0**, opcode = **010**, address = **AF3**.
Opcode 010 = **LDA**, direct. → `AC ← M[AF3]`.

**(b) `B100`** → `1011 0001 0000 0000` → I = **1**, opcode = **011**, address = **100**.
Opcode 011 = **STA**, **indirect**. → EA = M[100]; then `M[EA] ← AC`. **Two memory accesses**: one to
fetch the pointer, one to store.

**(c) `7100`** → I = 0, opcode = **111** → register-reference. Low 12 bits = `0001 0000 0000` → bit 8
set → **CME**: `E ← E′` (complement the extended bit).

**(d) `F200`** → I = 1, opcode = 111 → input–output. Low 12 = `0010 0000 0000` → bit 9 → **SKI**:
skip the next instruction if the input flag FGI = 1.

**(e) `7048`** → I = 0, opcode = 111 → register-reference. Low 12 bits = `0000 0100 1000` — **two**
bits set (bit 6 and bit 3). **This is not a valid instruction.** The one-hot encoding exists precisely
because the hardware ORs the effects of every set bit; `7048` would attempt CIL and SNA in the same
clock. Saying *"invalid — the RRI field must be one-hot"* is the full-credit answer.

---

## Worked — derive the format from the memory size (inferred form F1-adjacent)

> **A Basic Computer is redesigned with a memory of 8192 × 16. What changes in the instruction
> format, and what does it cost?**

**Step 1 — address bits.** 8192 = 2¹³ → **13 address bits**.

**Step 2 — what is left.** 16 − 13 − 1 (the I bit) = **2 opcode bits** → only **4 opcodes**.

**Step 3 — the consequence, which is the actual answer.** With 4 opcodes you cannot keep 7
memory-reference instructions *and* reserve one code for the register-reference/IO escape. The
machine would need either a **longer instruction word** (two-word instructions, so the fetch takes
two memory cycles) or a **different escape mechanism**.

**Step 4 — the principle to state.** In a fixed-width instruction, **address space and opcode space
trade against each other directly**. That single trade is why real machines use variable-length
instructions (CISC, 1–6 bytes on the 8086) or wider fixed words (RISC-V, 32 bits with a load/store
ISA that needs fewer address bits per instruction).

---

## Traps

| # | Trap | The correction |
|---|---|---|
| — | Reciting "3 opcode bits" without the derivation | 16 − 12 − 1 = 3. The derivation is the mark |
| — | Treating AR as a general register | AR is **wired to the memory's address pins**. Every memory access uses it, with no exception |
| — | Forgetting AC is not loaded from the bus | AC's input is the **adder-and-logic circuit** (inputs AC, DR, INPR). This is why file 06 treats AC separately |
| — | Calling INPR/OUTR bus sources | They are not in the S₂S₁S₀ table. INPR feeds AC through the adder-and-logic circuit; OUTR is load-only from the low 8 bits |
| — | Memorizing the 18 RRI/IO hex codes as a list | They are **one-hot**: 7 or F, then a single set bit. Regenerate them from the bit position |
| — | Saying a register-reference instruction has an address | Opcode 111 with I = 0 — the low 12 bits are an **operation selector**, not an address |
| — | Listing 25 instructions but not the completeness argument | The examinable claim is *why* they suffice: NAND from AND+CMA, subtraction from ADD+CMA+INC, loops from BUN+ISZ |

---

## Self-test

1. A machine has 16-bit instructions, a 1-bit mode field, and 32 opcodes. How large can its directly
   addressable memory be?
2. Write out `9F00` in binary, identify it fully, and state how many memory accesses its execution
   needs (excluding the instruction fetch).
3. Which of these can drive the common bus: AR, PC, INPR, IR, OUTR, TR, memory, AC?
4. AR drives the 16-bit bus. What appears on bus lines 15–12, and why?
5. Give the hex code for: clear the accumulator · skip if AC is negative · turn interrupts on.
6. Why does the Basic Computer need a TR (temporary register) at all, given that it has AC?
7. Argue that the instruction set would still be complete if `AND` were removed but `CMA`, `ADD` and
   `INC` were kept. Then say what is lost.
8. The BC's opcode field is 3 bits, yet there are 25 instructions. Explain, in two sentences, how
   that is possible without contradiction.

---

## Answers

**1.** 32 opcodes = 5 opcode bits. 16 − 1 (mode) − 5 (opcode) = **10 address bits** → **1024 words**
directly addressable.

**2.** `9F00` = `1001 1111 0000 0000` → I = **1**, opcode = **001** = **ADD**, address = **F00**.
So: **indirect ADD** → EA = M[F00], then `AC ← AC + M[EA]`.
**Two** memory accesses during execution: one to read the pointer at F00 (the indirect phase, T₃),
one to read the operand at EA (D₁T₄). The instruction fetch itself is a third, but the question
excluded it.

**3.** **AR, PC, DR, AC, IR, TR and memory** — seven sources. **INPR and OUTR cannot**: INPR reaches
AC through the adder-and-logic circuit, and OUTR is a destination only (load from the low 8 bus
lines). *(DR was not in the question's list but is a source; the question's list was deliberately
mixed.)*

**4.** **Zeros.** AR is only 12 bits, so when it drives a 16-bit bus the high-order 4 lines are filled
with 0s. Same for PC. (This is why an address placed on the bus and captured in a 16-bit register
reads as a small positive number.)

**5.** CLA = **7800** · SNA = **7008** · ION = **F080**.

**6.** Because the bus can carry **one value per clock**, and some operations need a value held
somewhere while the bus is used for something else. The interrupt cycle is the concrete case:
`RT₀: AR ← 0, TR ← PC` parks PC in TR so that AR can be cleared in the same clock and PC can be
overwritten in the next one, without losing the return address. Without TR the return address would
have to be written to memory in the same clock in which the address register is being set — which the
single bus forbids.

**7.** With CMA, ADD and INC you have complement and addition, hence 2's-complement subtraction, hence
comparison and multiplication by repeated addition. Logic can be reconstructed arithmetically for
specific cases, and BUN/ISZ still give control flow, so the machine remains Turing-complete in
principle. **What is lost is bit manipulation in one step** — masking, selective clear, field
extraction — which is exactly what `AND` is *for*. The honest framing: completeness is preserved,
**convenience and efficiency are destroyed**, and the resulting programs are far longer. That
distinction (necessary vs convenient) is the point of the completeness argument.

**8.** Seven of the eight opcodes (000–110) are spent on memory-reference instructions; the eighth
(111) is an **escape code** whose meaning is decided by the I bit and whose operation is selected by
the 12 low-order bits, which are unused as an address in that case. So 7 MRI + 12 register-reference
+ 6 input–output = 25, from only 8 opcode values.
