# U7 — The 8086 Microprocessor (Stage 1)

**Lectures L27–L34 · CO4 + CO5 · ETE only · ⚠ NO DECK SUPPLIED · L27 is flipped-classroom**

Scope (hand-out): L27 Internal Architectural Model, operational details · L28–L29 Addressing modes ·
L30 Machine Language, Assembly Language and Assembler · L31 Programming Arithmetic and Logic
Operations · L32 Program Loops & Subroutines · L33 Instruction Set: types of instructions & assembler
directives · L34 Assembly Language Programming.

Truth authority: **Bhurchandi & Ray, *Advanced Microprocessors and Peripheral Devices* 3e** (the
hand-out's and the decks' named 8086 reference). Verified against an institutional Q&A reproduction,
an institutional addressing-modes deck, **NPTEL** slides for assembler directives, and Ken Shirriff's
die-level reverse-engineering of the 8086 for the prefetch queue.

> **★ THIS IS THE HIGHEST-VALUE UNIT IN THE COURSE.**
> - **CO4** (addressing modes) is the **only CO with a target above 75% — 85%, attainment level 3.**
> - **CO5** (assembly programming) is the **only CO with an L3 "Develop" verb** — a *doing* outcome.
> - Eight of 36 lectures (22%) are spent here.
>
> Consequence for teaching: **practice, not reading.** CO5 cannot be met by explanation; it needs
> programs written. Budget accordingly (`exam-map.md` F24–F27).

---

## 1. What the 8086 is — `settled`

| Property | Value |
|---|---|
| Data bus | **16-bit**, internal and external |
| Address bus | **20-bit** → addresses **2²⁰ = 1 MB** of memory |
| I/O address space | uses A₀–A₁₅ → **2¹⁶ = 64 KB** of I/O ports |
| Technology | **HMOS** (high-performance MOS) |
| Transistors | **≈ 29,000** |
| Package | **40-pin DIP** |
| Registers | **14 × 16-bit** |
| Instruction queue | **6 bytes**, FIFO |
| Instruction length | **1 to 6 bytes** (variable — it is a CISC) |
| Speed grades | 8086 = **5 MHz**, 8086-2 = **8 MHz**, 8086-1 = **10 MHz** |
| Operating modes | **MIN** (MN/MX̄ pin high) and **MAX** (MN/MX̄ low) |

**MIN vs MAX mode:** MIN is for a single-processor (uniprocessor) system — **the CPU issues its own
control signals**. MAX is for multiprocessor systems — the **8288 bus controller** generates the
control signals instead. **Pins 24–31 (8 pins) change meaning** between the two modes.

**Data types handled:** signed and unsigned integers (byte and word), **BCD in packed and unpacked
form**, and **ASCII** (one character per byte). The 8086 can do bit, byte, word and block operations,
**including multiplication and division** (which the 8085 could not).

## 2. Internal architecture — BIU and EU — `settled` (L27)

The 8086 has **two separate functional units** that work **at the same time**:

```
┌───────────────────── BIU (Bus Interface Unit) ──────────────────┐
│  CS  DS  SS  ES   (segment registers)                           │
│  IP               (instruction pointer)                         │
│  address generation + bus control logic                         │
│  ┌─────────────────────────────┐                                │
│  │ instruction queue  6 5 4 3 2 1 │  ← 6 bytes, FIFO           │
│  └─────────────────────────────┘                                │
└────────────────────────┬────────────────────────────────────────┘
                         │  Q bus (queue supplies instructions)
┌────────────────────────┴───────── EU (Execution Unit) ──────────┐
│  AH AL │ BH BL │ CH CL │ DH DL   (general-purpose registers)     │
│  SP  BP  SI  DI                                                 │
│  ALU  ·  FLAGS  ·  control unit  ·  instruction register        │
│  **EU has NO connection to the system buses**                    │
└─────────────────────────────────────────────────────────────────┘
```

| Unit | Jobs |
|---|---|
| **BIU** | the 8086's **interface to the outside world** — *all* external bus operations. Fetches instructions; reads/writes data and operands for memory; inputs/outputs data for peripherals; **fills the instruction queue**; **generates addresses** |
| **EU** | **decodes and executes** instructions. Takes instructions from the output end of the queue and data from registers or memory; generates operand addresses and **hands them to the BIU**, requesting a read or write; tests and updates the flags; **waits when the queue is empty** |

**★ The mechanism that matters: this is pipelining.** Because BIU and EU are independent, while the EU
decodes and executes, the **BIU fetches ahead** into the queue. Fetch and execute **overlap** —
unlike the 8085, where fetch and execute were strictly sequential. The source states it plainly:
"This feature of fetching the next instruction when the current instruction is being executed, is
called **Pipelining**." Result: efficient use of the system bus and reduced effective instruction time.

**This is U4's instruction pipeline appearing in a real chip** — a 2-stage (fetch | execute) pipeline.
Make that link explicitly when teaching; it is the payoff for having done U4 first.

### Instruction queue mechanics — `settled`

- **6 bytes, FIFO.** The BIU fetches ahead of time.
- **On a JUMP or CALL the queue is dumped** and refilled from the new address. (Prefetched bytes are
  now wrong — the fetch was speculative.) **This is a control hazard and a pipeline flush, in
  hardware** (U4 §8c).
- **Refill does not start until two bytes are free:** "the filling in operation of the queue is not
  started until two bytes of the instruction queue is empty." *Mechanism:* the 8086 fetches **a word
  (2 bytes) at a time** over its 16-bit bus, so there must be room for 2 bytes before a fetch is
  worthwhile.
- **"The instruction execution cycle is never broken for fetch operation"** — execution has priority
  on the bus; the BIU prefetches only in **free** bus cycles.
- Startup: the queue is empty, CS:IP is loaded, and the 8086 fetches **1 byte if CS:IP is odd, 2 bytes
  if even** (alignment).
- The **first byte is always an opcode**; decoding it reveals whether the instruction has a second
  opcode byte and how long it is.

*Deeper (verified against die-level analysis, Shirriff 2023):* the queue is physically **three 16-bit
registers** with read/write pointers; the documented prefetch policy is — queue holds 0–2 bytes →
prefetch at the next free bus cycle; 3–4 bytes → prefetch delayed two clocks; **5–6 bytes → no
prefetch possible**. A `FLUSH` micro-instruction empties it on a change of control flow. The **8088
has a 4-byte queue** instead of 6, because its bus is 8 bits wide — fetching is half as fast, so a
deep queue would rarely fill.

**EU enters a WAIT state in three situations:** (1) an instruction needs a memory location not in the
queue; (2) a **JUMP** executes — the queue is aborted and the EU waits for the instruction at the jump
address; (3) a very slow instruction executes (e.g. **AAM takes 83 clock cycles**; `likely`,
single-sourced) — the BIU then waits until the EU pulls bytes before resuming fetches.

## 3. Register set — `settled` (14 registers)

**Four groups.** (4 data + 4 pointer/index + IP + 4 segment + 1 flag = **14**.)

### (a) Data group — general purpose, byte- or word-addressable

Each splits into a high and low byte: **X** = word, **H** = high byte, **L** = low byte.

| Register | Name | Dedicated functions |
|---|---|---|
| **AX** (AH, AL) | **A**ccumulator | **AX**: word multiply, word divide, word I/O. **AL**: byte multiply, byte divide, byte I/O, **translate**, **decimal arithmetic**. **AH**: byte multiply, byte divide |
| **BX** (BH, BL) | **B**ase | **translate**; and the only *general* register usable as a memory **pointer** |
| **CX** (CH, CL) | **C**ount | **string operations, loops**. **CL**: variable shift and rotate counts |
| **DX** (DH, DL) | **D**ata | word multiply, word divide, **indirect I/O** (holds the 16-bit port address) |

All four can be source or destination for ADD/AND/etc., "although particular registers are earmarked
for specific operations."

**★ Teach the dedications as the reason the 8086 is a CISC:** these registers are *not*
interchangeable. `MUL` implicitly uses AX and DX; `LOOP` implicitly decrements CX; `IN`/`OUT` with a
16-bit port need DX; string instructions need SI, DI and CX. **Contrast with RISC-V's 32 registers
that are all the same** (U8) — that contrast *is* the RISC/CISC lesson made concrete.

### (b) Pointer and index group

All 16-bit; they hold **offset addresses** relative to a segment register, i.e. they act as memory
pointers.

| Register | Name | Default segment | Job |
|---|---|---|---|
| **SP** | Stack Pointer | **SS** | offset of the **stack top** |
| **BP** | Base Pointer | **SS** | offset for accessing data **inside the stack segment** (stack frames); also usable as a general register |
| **SI** | Source Index | **DS** | source offset for **string** operations; general pointer |
| **DI** | Destination Index | **ES** (for strings) | destination offset for string operations; general pointer |
| **IP** | Instruction Pointer | **CS** | offset of the **next instruction** |

**IP vs the 8085's PC (an exam favourite):** IP holds the **offset**, not the actual address. The real
address is formed from **CS:IP**. **IP cannot be programmed directly** by the programmer (no `MOV IP,…`)
— it changes only via jumps, calls and returns. It increments by the size of each instruction fetched.

*Example of pointer use:* `MOV AH, [SI]` = "move the byte whose address is in SI into AH."

### (c) Segment group — `settled`

| Register | Name | Holds the base of |
|---|---|---|
| **CS** | Code Segment | the currently executing code |
| **DS** | Data Segment | the program's data |
| **SS** | Stack Segment | the stack |
| **ES** | Extra Segment | extra data (string destinations) |

Contents can be changed so a program may jump from one active code segment to another.

### (d) Flag register — `settled`

**16-bit** (also called the **status register** or **PSW**). **Nine flags are used; seven bits are
unused.** Of the nine: **six condition flags** (set by results) and **three control flags** (set by the
programmer).

```
 bit: 15 14 13 12 │11 │10 │ 9 │ 8 │ 7 │ 6 │ 5 │ 4 │ 3 │ 2 │ 1 │ 0
       -  -  -  - │OF │DF │IF │TF │SF │ZF │ - │AF │ - │PF │ - │CF
```

| Bit | Flag | Type | Set when |
|---|---|---|---|
| 0 | **CF** carry | condition | carry out of, or borrow into, the **MSB** |
| 2 | **PF** parity | condition | the **low-order 8 bits** of the result contain an **even** number of 1s |
| 4 | **AF** auxiliary carry | condition | carry out of / borrow into **bit 3** (the low nibble of AL) — used by BCD adjust instructions |
| 6 | **ZF** zero | condition | the result is zero |
| 7 | **SF** sign | condition | **equal to the high-order (most significant) bit of the result** — 0 positive, 1 negative |
| 8 | **TF** trap | **control** | when set, a single-step interrupt occurs after the next instruction |
| 9 | **IF** interrupt enable | **control** | when set, maskable interrupts (INTR) are enabled |
| 10 | **DF** direction | **control** | when set, string instructions **auto-decrement** SI/DI; when clear, auto-increment |
| 11 | **OF** overflow | condition | the **signed** result cannot be represented in the destination's bits |

⚠ **CORRECTED SOURCE ERROR.** One institutional source states "**SF is used with unsigned numbers**."
**That is wrong** — and the *same document's own flag table* contradicts it ("Sign Flag: Set equal to
high-order bit of result"). SF copies the MSB, which is the **sign bit under signed (2's-complement)
interpretation**; it is meaningless for unsigned values. **CF is the unsigned-overflow flag; OF is the
signed-overflow flag; SF is the signed-sign flag.** Logged in `CHANGELOG.md`; kept as
`misconceptions.md` M16.

**Control-flag details worth having:**
- **TF** cannot be set or reset directly. You do it indirectly: **push the flag register onto the
  stack, modify TF, pop it back.** When an interrupt is recognized TF is cleared; `IRET` restores it.
- **IF** is set by **STI**, cleared by **CLI**. On interrupt recognition IF is cleared (so INTR is
  disabled inside the ISR) and restored by `IRET`. **On reset, IF is cleared.**
- **DF** is set by **STD**, cleared by **CLD**. With DF = 1, `MOVS` walks the string from **high
  addresses down**.

## 4. Memory segmentation and physical address — `settled` (the U7 threshold)

**The problem:** the address bus is **20 bits** but the largest register is **16 bits**. 16 bits can
only express 64 KB. So how does a 16-bit machine address 1 MB?

**The answer — segmentation.** Memory is divided into **16 logical segments**; each segment is at most
**64 KB** (so any location inside it is reachable with a 16-bit offset). A memory address is written
**segment : offset**.

> **Physical address = (segment register) × 16 + offset**
> equivalently: **shift the segment value left one hexadecimal digit, then add the offset.**

**Worked (the canonical exam item, F24):** `89AB : F012`
```
   segment  89AB  shifted left one hex digit →  89AB0
   offset   F012                             →  0F012
                                               ───────
   physical address                             98AC2 H
```

**Two consequences that must be taught, not just the formula:**

1. **Segments begin every 16 bytes.** Multiplying by 16 means a segment base is always a multiple of
   16 — a **"paragraph"** boundary. Hence "paragraph to byte" conversion.
2. **★ SEGMENTS OVERLAP.** Many different seg:offset pairs name the **same** physical byte. Example:
   `0000:0010` and `0001:0000` both give 00010H. So a logical address is **not unique**. Students who
   miss this get confused by any question involving two segment registers. (`misconceptions.md` M17.)

**Default and alternate segment assignments — `settled`, and an exam table:**

| Type of memory reference | Default segment | Alternate allowed | Offset from |
|---|---|---|---|
| **Instruction fetch** | **CS** | **none** | IP |
| **Stack operation** (PUSH/POP) | **SS** | **none** | SP, BP |
| General data | **DS** | CS, ES, SS | effective address |
| **String source** | **DS** | CS, ES, SS | **SI** |
| **String destination** | **ES** | **none** | **DI** |
| **BX** used as pointer | **DS** | CS, ES, SS | effective address |
| **BP** used as pointer | **SS** | CS, ES, DS | effective address |

**★ Note the three "none" rows** — instruction fetch, stack operations and string destinations
**cannot be overridden**. And note **BP defaults to SS while BX defaults to DS** — the single most
examined detail in 8086 addressing, because it is the one asymmetry in an otherwise uniform scheme.
(*Mechanism:* BP exists to address **stack frames**, so defaulting it to SS is what makes local
variables work.)

**Segment override prefix.** A one-byte prefix `001 rr 110` placed **before the opcode** forces a
different segment: **rr = 00 → ES, 01 → CS, 10 → SS, 11 → DS.** Written in assembly as e.g.
`MOV AX, ES:[BX]`.

## 5. Addressing modes — `settled` mechanisms, `likely` taxonomy (L28–L29, **CO4 = 85%**)

⚠ **On the count:** institutional sources give **12 modes in 5 groups**; other textbooks compress to
7 or 8 by folding in the I/O-port, relative and implied modes. **The mechanisms are settled; the
number is a naming convention.** Teach the 12/5 scheme and say the count varies — never assert "there
are exactly N addressing modes" as fact. (`misconceptions.md` M18.)

**Notation used below** (Bhurchandi's, and the one to write in an exam):
**EA** = effective address (the offset) · **BA** = base address = (segment register) × 16 ·
**MA** = memory address = BA + EA.

### Group I — register and immediate data

| # | Mode | Rule | Example |
|---|---|---|---|
| 1 | **Register** | the operand is **in a named register** | `MOV CL, DH` → (CL) ← (DH) |
| 2 | **Immediate** | the operand (8- or 16-bit) is **part of the instruction** | `MOV DL, 08H` → (DL) ← 08H; `MOV AX, 0A9FH` |

### Group II — memory data

| # | Mode | Rule | Example |
|---|---|---|---|
| 3 | **Direct** | EA is **written literally in the instruction** (a 16-bit number) | `MOV BX, [1354H]` |
| 4 | **Register indirect** | EA is **in a register** — **BX, BP, SI or DI** | `MOV CX, [BX]`: EA = (BX), BA = (DS)×16, MA = BA + EA |
| 5 | **Based** | EA = **base register (BX or BP)** + signed 8-bit / unsigned 16-bit displacement | `MOV AX, [BX + 08H]` |
| 6 | **Indexed** | EA = **index register (SI or DI)** + displacement | `MOV CX, [SI + 0A2H]` |
| 7 | **Based-index** | EA = **base (BX/BP) + index (SI/DI) + displacement** | `MOV DX, [BX + SI + 0AH]` |
| 8 | **String** | EA of source is **implicitly SI**, of destination **implicitly DI** | `MOVS BYTE` |

**Sign-extension rule (`settled`, and a favourite trap):** an **8-bit displacement is sign-extended to
16 bits before being added.** So `[SI + 0A2H]` uses **FFA2H**, not 00A2H — i.e. the displacement is
**negative** (−94). A learner who adds 00A2 gets the wrong address. Worked in the source:
"FFA2H ← A2H (sign extended), EA = (SI) + FFA2H."

**String mode, in full:** source MA = (DS)×16 + (SI); destination MAₑ = (ES)×16 + (DI); then
`(MAₑ) ← (MA)`. Afterwards, **if DF = 1, SI and DI are decremented; if DF = 0, incremented.**
Note the **DS for source / ES for destination** asymmetry — that is why ES exists.

**The legal EA combinations (`settled`)** — you may *not* combine registers arbitrarily. Only these:
```
  [BX+SI]  [BX+DI]  [BP+SI]  [BP+DI]        (base + index)
  [SI]     [DI]     [BX]     [BP+disp]      (single register)
  d16                                        (direct)
  … each of the above, optionally + d8 or + d16
```
**One base (BX or BP) + one index (SI or DI), never two bases and never two indexes.** So `[BX+BP]`
and `[SI+DI]` are **illegal**. (This falls straight out of the MOD/r-m encoding — §6.)

**And one encoding quirk worth knowing:** `[BP]` with **no** displacement cannot be encoded, because
that bit pattern (MOD = 00, r/m = 110) is taken by **direct addressing**. Assemblers therefore emit
`[BP + 00H]`. This is why the legal-combinations list shows `[BP+disp]` but never bare `[BP]`.

### Group III — I/O ports

| # | Mode | Rule | Example |
|---|---|---|---|
| 9 | **Direct I/O port** | an **8-bit** port address is given in the instruction | `IN AL, [09H]` |
| 10 | **Indirect I/O port** | the **16-bit** port address is in **DX** | `OUT [DX], AX` |

*Why DX:* a direct port address is only 8 bits (256 ports). To reach the full 64 K I/O space you must
put the 16-bit address in a register — and the 8086 dedicates **DX** to it.

### Group IV — relative

| # | Mode | Rule | Example |
|---|---|---|---|
| 11 | **Relative** | EA = **(IP) + 8-bit signed displacement** | `JZ 0AH`: if ZF = 1 then EA = (IP) + 000AH, BA = (CS)×16, MA = BA + EA |

*Why relative and not absolute for jumps:* the displacement is small (1 byte) and the code stays
**position-independent** — the same bytes work wherever the segment is loaded.

### Group V — implied

| # | Mode | Rule | Example |
|---|---|---|---|
| 12 | **Implied** | **no operands**; the instruction itself names the data | `CLC` (clear carry) |

## 6. Instruction format — `settled`

Up to **6 bytes**:

```
┌──────────────────┬────────────────────┬──────────┬──────────┬──────────┬──────────┐
│ byte 1: opcode D W│ byte 2: MOD REG r/m│ low disp │ high disp│ low data │ high data│
└──────────────────┴────────────────────┴──────────┴──────────┴──────────┴──────────┘
```

**Byte 1** carries the opcode plus two 1-bit fields:
- **D (direction):** D = 1 → the register named in REG is the **destination**; D = 0 → it is the
  **source**.
- **W (word/byte):** W = 0 → **8-bit** operation; W = 1 → **16-bit**.

**Byte 2** has three fields:

| Field | Bits | Meaning |
|---|---|---|
| **MOD** | 2 | addressing mode / displacement size |
| **REG** | 3 | the register operand |
| **r/m** | 3 | register or memory, the second operand |

**MOD encoding:**

| MOD | Meaning |
|---|---|
| 00 | memory addressing, **no displacement** |
| 01 | memory addressing, **8-bit** displacement |
| 10 | memory addressing, **16-bit** displacement |
| 11 | **register** addressing (W picks byte or word) |

**r/m with MOD = 00 / 01 / 10 (effective-address selection) — `settled`:**

| r/m | MOD 00 | MOD 01 | MOD 10 | default segment |
|---|---|---|---|---|
| 000 | [BX]+[SI] | [BX]+[SI]+d8 | [BX]+[SI]+d16 | DS |
| 001 | [BX]+[DI] | [BX]+[DI]+d8 | [BX]+[DI]+d16 | DS |
| 010 | [BP]+[SI] | [BP]+[SI]+d8 | [BP]+[SI]+d16 | **SS** |
| 011 | [BP]+[DI] | [BP]+[DI]+d8 | [BP]+[DI]+d16 | **SS** |
| 100 | [SI] | [SI]+d8 | [SI]+d16 | DS |
| 101 | [DI] | [DI]+d8 | [DI]+d16 | DS |
| 110 | **direct (d16)** | [BP]+d8 | [BP]+d16 | DS (direct) / **SS** (BP) |
| 111 | [BX] | [BX]+d8 | [BX]+d16 | DS |

**Note r/m = 110 again:** with MOD = 00 it means **direct addressing**, which is exactly why bare
`[BP]` has no encoding. **The encoding table and the legal-combinations list in §5 are the same fact,
seen from two sides** — teach them together.

**REG / r/m register encoding (MOD = 11):**

| code | W = 0 | W = 1 |
|---|---|---|
| 000 | AL | AX |
| 001 | CL | CX |
| 010 | DL | DX |
| 011 | BL | BX |
| 100 | AH | SP |
| 101 | CH | BP |
| 110 | DH | SI |
| 111 | BH | DI |

## 7. Two hard architectural restrictions — `settled`

Both are standard exam questions and both trip up first-time programmers.

**(a) No direct memory-to-memory transfer.** `MOV [DI], [SI]` is **illegal**. Go through a register:
```
MOV AH, [SI]      ; memory → register
MOV [DI], AH      ; register → memory
```
*Mechanism:* the instruction format has **one** r/m field, so only one operand can be a memory
operand. (String instructions like `MOVS` are the exception — they are memory-to-memory, which is
precisely why they exist as a special class.)

**(b) A segment register cannot be loaded with an immediate.** `MOV DS, 1000H` is **illegal**. Go
through a general register:
```
MOV AX, 1000H
MOV DS, AX
```

## 8. Instruction set — `settled` mnemonics, `likely` grouping (L33)

⚠ **The number of groups is convention.** Sources give **7** (arithmetic & logical · data transfer ·
branch & loop · machine control · flag manipulation · shift & rotate · string) and others **8**.
Mnemonics and behaviour are settled; the taxonomy is not. Present a grouping and say so.

| Group | Representative instructions |
|---|---|
| **Data transfer** | `MOV` `PUSH` `POP` `XCHG` `IN` `OUT` `LEA` `LDS` `LES` `XLAT` `LAHF` `SAHF` |
| **Arithmetic** | `ADD` `ADC` `SUB` `SBB` `INC` `DEC` `NEG` `CMP` `MUL` `IMUL` `DIV` `IDIV` `CBW` `CWD` · **BCD/ASCII adjust:** `DAA` `DAS` `AAA` `AAS` `AAM` `AAD` |
| **Logical** | `AND` `OR` `XOR` `NOT` `TEST` |
| **Shift & rotate** | `SHL`/`SAL` `SHR` `SAR` `ROL` `ROR` `RCL` `RCR` |
| **String** | `MOVS` `CMPS` `SCAS` `LODS` `STOS` with prefixes `REP` `REPE`/`REPZ` `REPNE`/`REPNZ` |
| **Branch / program transfer** | `JMP` `CALL` `RET` · conditional: `JZ`/`JE` `JNZ`/`JNE` `JC` `JNC` `JG` `JL` `JGE` `JLE` `JA` `JB` `JO` `JS` `JP` · iteration: `LOOP` `LOOPE`/`LOOPZ` `LOOPNE`/`LOOPNZ` `JCXZ` |
| **Flag manipulation** | `CLC` `STC` `CMC` `CLD` `STD` `CLI` `STI` |
| **Machine / processor control** | `HLT` `NOP` `WAIT` `ESC` `LOCK` |

**Distinctions worth teaching (each is a plausible short question):**

| Pair | Difference |
|---|---|
| `CMP` vs `SUB` | `CMP` subtracts but **discards the result**, keeping only the flags |
| `TEST` vs `AND` | `TEST` ANDs but **discards the result**, keeping only the flags |
| `MOV` vs `LEA` | `MOV AX,[BX]` loads the **contents**; `LEA AX,[BX]` loads the **address (offset)** |
| `MUL` vs `IMUL` | unsigned vs **signed** multiply |
| `SHR` vs `SAR` | logical (0 in) vs **arithmetic** (sign replicated) — exactly U1 §9 |
| `ROL` vs `RCL` | rotate within the operand vs rotate **through the carry flag** |
| `JA`/`JB` vs `JG`/`JL` | **unsigned** (above/below, tests CF) vs **signed** (greater/less, tests SF & OF) |

**★ That last row is the one students get wrong**, and it is the payoff for §3's flag discussion: use
`JA`/`JB` after comparing **unsigned** quantities and `JG`/`JL` after comparing **signed** ones.
Choosing wrongly gives code that works until a value crosses 7FH.

**Implicit-operand facts to memorize** (CISC-ness made concrete):
- `MUL` byte: `AX ← AL × operand`. `MUL` word: `DX:AX ← AX × operand`.
- `DIV` byte: `AL ← AX / operand`, `AH ← remainder`. Word: `AX ← DX:AX / operand`, `DX ← remainder`.
- `LOOP` decrements **CX** and jumps if CX ≠ 0.
- String instructions use **SI** (source), **DI** (destination), **CX** (count with `REP`), and **DF**
  (direction).

## 9. Assembler, machine language and assembler directives — `settled` (L30, L33)

**The three levels:** **machine language** (binary the CPU executes) → **assembly language**
(mnemonics, one-to-one with machine instructions) → the **assembler** (translates assembly to machine
code). Assembly is *not* a high-level language: each statement maps to one instruction.

**Assembler directives** (a.k.a. **pseudo-instructions**) are "instructions to the Assembler regarding
the program being executed." **★ They generate NO machine code** — they control how the assembler
builds the program. That sentence is the definition to give.

Used to: specify the start and end of a program · attach values to variables · allocate storage for
I/O data · define the start and end of segments, procedures and macros.

**Data definition:**

| Directive | Meaning | Example |
|---|---|---|
| **DB** | define **byte** (8-bit) | `PRICE DB 49H, 98H, 29H` — an array of 3 bytes · `NAME DB 'ABCDEF'` — 6 bytes of ASCII · `TEMP DB 100 DUP(?)` — 100 **uninitialized** bytes |
| **DW** | define **word** (16-bit) | `MULTIPLIER DW 437AH` · `EXP1 DW 1234H, 3456H, 5678H` · `STOR1 DW 100 DUP(0)` — 100 words, all zero |
| **DD** | define **double word** (32-bit) | |
| **DQ** | define **quad word** (64-bit) | |
| **DT** | define **ten bytes** | |

Ranges: DB unsigned 00H–FFH (signed 00H–7FH positive, 80H–FFH negative); DW unsigned 0000H–FFFFH
(signed 0000H–7FFFH positive, 8000H–FFFFH negative).
**`DUP`** is an operator that initializes memory with repeated values; **`?`** means "reserve but do
not initialize."

**Segment, procedure and program structure:**

| Directive | Meaning |
|---|---|
| **SEGMENT / ENDS** | mark the beginning / end of a code, data or stack segment: `segname SEGMENT … segname ENDS` |
| **ASSUME** | tell the assembler **which logical segment to use for each segment register**: `ASSUME CS:CODE, DS:DATA` |
| **PROC / ENDP** | begin / end a procedure: `procname PROC [NEAR|FAR] … RET … procname ENDP` |
| **NEAR / FAR** | **intra**segment call (offset only) / **inter**segment call (segment + offset) |
| **END** | end of the program module — the assembler **ignores anything after it** |
| **ORG** | **originate** — set the location counter / starting effective address: `ORG 1000H` |
| **EQU** | **equate** — give a name to a value: `FACTOR EQU 03H`, then `ADD AL, FACTOR` assembles as `ADD AL, 03H` |
| **EVEN** | align the location counter to the **next even address** |
| **SHORT** | reserve **one** byte for an 8-bit signed jump displacement: `JMP SHORT AHEAD` |
| **MACRO / ENDM** | begin / end a macro: `macroname MACRO [args] … ENDM` |
| **PROC**, **PUBLIC**, **EXTRN** | declare a name visible to / defined in other modules |
| **GROUP** | group logical segments into one group segment |
| **INCLUDE** | insert source from a named file |

**Operators (often examined alongside directives):**

| Operator | Meaning |
|---|---|
| **PTR** | assign/override a type: `INC BYTE PTR [BX]` — resolves the ambiguity in `INC [BX]` (byte or word?); `MOV AL, BYTE PTR WORDS` |
| **OFFSET** | the offset of a variable from the start of its segment |
| **TYPE** | the size in bytes of a variable — **byte → 1, word → 2, double word → 4**; e.g. `ADD BX, TYPE WORD_ARRAY` advances BX by one element |
| **LABEL** | give a name to the current location with a specified type |

**Why EVEN exists (the mechanism, worth stating):** **"If the word is at an even address the 8086 can
read the memory in 1 bus cycle. If the word starts at an odd address, the 8086 will take 2 bus
cycles."** `EVEN` increments the location counter (inserting a **NOP**) so arrays of words start
aligned. This is a *performance* directive, and it connects straight back to the BHE̅/A₀ byte-bank
mechanism (§10).

*Worked (from the NPTEL slides):*
```
DATA1 SEGMENT
SALES  DB  9 DUP(?)        ; location counter now at 0009
EVEN                       ; advance to 000AH
RECORD DW  100 DUP(0)      ; 100 words, starting at an even address → faster reads
DATA1 ENDS
```

**PROC/ENDP worked:**
```
ADD64 PROC NEAR            ; CALL/RET assembled as near (intrasegment)
      …
      RET
ADD64 ENDP

CONVERT PROC FAR           ; CALL/RET assembled as far (intersegment)
      …
      RET
CONVERT ENDP
```

**DOS function calls via `INT 21H`** (needed to write runnable programs):

| AH | Function |
|---|---|
| 00H | terminate a program |
| 01H | read the keyboard (with echo) |
| 02H | write to standard output |
| 08H | read standard input **without** echo |
| 09H | **display a character string** (terminated by `$`) |
| 0AH | buffered keyboard input |
| 4CH | terminate with return code (the modern replacement for 00H) |

## 10. Signals and modes — `settled` (supporting L27)

Not the focus of the hand-out, but the standard "explain these pins" questions:

- **AD₁₅–AD₀** — **multiplexed** address/data. During **T1** they carry address A₁₅–A₀; during **T2,
  T3, T4** they carry **data**.
- **A₁₉/S₆–A₁₆/S₃** — multiplexed address/status. **T1:** the upper address bits A₁₉–A₁₆; **T2–T4:**
  status. **S₄S₃ identify which segment register** was used for the address; **S₅** gives the
  interrupt-enable status; **S₆** stays low. **During I/O operations these lines are low** (I/O
  addresses are only 16 bits).
- **BHE̅/S₇** — during T1, **bus high enable** (selects the **upper** byte D₁₅–D₈); during T2–T4 a
  status bit.
- **ALE** — address latch enable. **Demultiplexing** uses an **8282/8283 octal latch**: during T1 ALE
  is high and the latch is transparent; ALE's high-to-low transition at the end of T1 **latches the
  address**, so it remains available through T2–T4 while AD carries data.

**BHE̅ / A₀ byte-bank table — `settled`:**

| BHE̅ | A₀ | Access |
|---|---|---|
| 0 | 0 | **both banks** active — 16-bit word on AD₁₅–AD₀ |
| 0 | 1 | only **high** bank — upper byte from/to an **odd** address on AD₁₅–AD₈ |
| 1 | 0 | only **low** bank — lower byte from/to an **even** address on AD₇–AD₀ |
| 1 | 1 | **no** bank active |

*Mechanism:* memory is organized as two 8-bit banks (even addresses in the low bank, odd in the high
bank) so that a 16-bit word at an even address can be fetched in one cycle. **A word at an odd address
straddles both banks and needs two cycles** — which is exactly what `EVEN` avoids.

**RESET — `settled`:** active **high**, must be held for at least **4 clock cycles**. On reset all
internal registers are cleared to 0000H **except CS = F000H and IP = FFF0H**, so execution starts at
physical address **FFFF0H**. Therefore the boot **EPROM is placed at FFFF0H–FFFFFH — the top of the
memory map.** (Only 16 bytes there, so the first instruction is invariably a far jump.)

**Bus status codes (MAX mode, S̄₂S̄₁S̄₀) — `settled`:**

| S̄₂S̄₁S̄₀ | Cycle |
|---|---|
| 000 | interrupt acknowledge |
| 001 | read I/O port |
| 010 | write I/O port |
| 011 | HALT |
| 100 | code access |
| 101 | read memory |
| 110 | write memory |
| 111 | passive |

**Other pins:** **DT/R̄** sets transceiver direction (1 = transmit, 0 = receive); **DEN̄** enables the
transceivers, active from mid-T2 to mid-T4; **LOCK̄** (MAX mode) prevents other bus masters from
taking the bus, asserted by the `LOCK` prefix; **TEST̄** is normally driven by the **8087** coprocessor's
BUSY output so the `WAIT` instruction can pause until the coprocessor finishes.

**8086 vs 8088 — `settled`:**

| | **8086** | **8088** |
|---|---|---|
| External data bus | **16-bit** (AD₀–AD₁₅) | **8-bit** (AD₀–AD₇) |
| Instruction queue | **6 bytes** | **4 bytes** |
| Queue refill starts when | **2 bytes** are free | **1 byte** is free |
| Pin 28 (MIN mode) | M/IO̅ | **IO/M̄** (inverted) |
| Pin 34 | BHE̅/S₇ | **SS̄₀** |
| Upper-byte select | **BHE̅** | not needed (byte bus) |
| BIU / EU | BIU differs, **EU identical**; instruction set identical | same |

*Note the elegance of the queue difference:* in MAX mode the **8087 monitors pin 34 to identify
whether it is attached to an 8086 or an 8088, and sets its own queue length to 6 or 4 accordingly.*

## 11. Assembly language programming — `settled` (L31, L32, L34 — **CO5, the L3 outcome**)

**Program skeleton** (the shape every answer should use):
```asm
DATA SEGMENT
    ARRAY   DB   12H, 34H, 56H, 78H, 9AH
    COUNT   EQU  05H
    RESULT  DB   ?
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE, DS:DATA
START:  MOV AX, DATA          ; segment registers cannot take an immediate
        MOV DS, AX            ; …so go through AX (§7b)
        …                     ; the actual work
        MOV AH, 4CH           ; terminate
        INT 21H
CODE ENDS
    END START
```

**The three control structures, as 8086 idioms:**

**(a) Counted loop** — `LOOP` decrements CX and jumps while CX ≠ 0:
```asm
        MOV CX, COUNT
        MOV SI, OFFSET ARRAY
        MOV AL, 0
NEXT:   ADD AL, [SI]
        INC SI
        LOOP NEXT             ; CX ← CX − 1; jump to NEXT if CX ≠ 0
```
⚠ **`LOOP` is a trap when CX might start at 0:** it decrements *first*, so CX = 0 wraps to FFFFH and
the loop runs **65 536 times**. Guard with `JCXZ` before the loop. (`misconceptions.md` M19.)

**(b) Conditional** — compare then branch, with the **signed/unsigned** choice from §8:
```asm
        CMP AL, BL
        JA  BIGGER            ; unsigned comparison
        ; JG BIGGER           ; the signed version
```

**(c) Subroutine** — `CALL` pushes the return address, `RET` pops it:
```asm
        CALL ADD64
        …
ADD64 PROC NEAR
        PUSH AX               ; save what you modify
        …
        POP  AX
        RET
ADD64 ENDP
```
**Mechanism:** `CALL NEAR` pushes **IP** only; `CALL FAR` pushes **CS then IP**. `RET` must match —
which is why `PROC NEAR`/`PROC FAR` exists: the directive tells the assembler which form of CALL/RET
to generate. Mismatching them corrupts the stack. **This is U3 §7's stack-based return, in a real
machine** — and the reason 8086 subroutines *are* recursive where U2's BSA was not.

**The canonical programs to be able to write** (CO5 is *Develop* — these must be practiced, not read):

| Program | Key technique |
|---|---|
| Sum of an array of bytes / words | `LOOP` + pointer increment; watch for carry (use `ADC` or a 16-bit accumulator) |
| Largest / smallest in an array | `CMP` + conditional jump; **signed vs unsigned matters** |
| Block move / block exchange | `MOVS` with `REP`, or `MOV` via a register (§7a) |
| String reverse / palindrome check | SI from the front, DI from the back, `DF` control |
| Count positive/negative/zero elements | test **SF/ZF**, or `TEST` against 80H |
| BCD ↔ binary, ASCII ↔ binary conversion | `AAA` `DAA` `AAM` `AAD`; ASCII digit = value + 30H |
| Multiply / divide by repeated addition | `LOOP`; contrast with `MUL`/`DIV` |
| Sort an array (bubble) | nested loops, `XCHG` |
| Factorial / Fibonacci | `MUL` with implicit AX; or recursion via `CALL` |
| Even/odd or 1s count in a byte | `SHR` + `JC`, or `TEST` against a mask |

---

## Worked-problem patterns for this unit

1. **Draw and explain the 8086 architecture**; jobs of BIU and EU; explain the queue and pipelining.
2. List the 14 registers by group; explain each **special-purpose** use.
3. **Explain the flag register**; give bit positions; distinguish condition vs control flags; explain
   how TF is set.
4. **Compute a physical address from seg:offset** — and explain why segments overlap.
5. **Give the default/alternate segment table**; explain why **BP defaults to SS**.
6. **For a given instruction, name the addressing mode and compute EA, BA and MA** — including
   **sign-extension** of an 8-bit displacement.
7. Explain the segment override prefix.
8. Explain the instruction format; decode a given MOD/REG/r-m byte.
9. Explain why memory-to-memory `MOV` and immediate-to-segment-register `MOV` are illegal, and give
   the workaround.
10. Classify the instruction set; distinguish `CMP`/`SUB`, `TEST`/`AND`, `MOV`/`LEA`, `SHR`/`SAR`,
    `JA`/`JG`.
11. **Explain named assembler directives with examples**; explain why they generate no machine code.
12. **Write an 8086 ALP** for a stated task, with proper segment/ASSUME/termination structure.
13. 8086 vs 8088; MIN vs MAX mode; the BHE̅/A₀ table; the reset vector.

## Confidence summary

`settled`: all architectural parameters (16-bit data, 20-bit address/1 MB, 64 KB I/O, HMOS, ≈29 000
transistors, 40-pin DIP, speed grades) · MIN/MAX modes and pins 24–31 · BIU/EU division of labour and
the pipelining mechanism · the 6-byte queue, flush-on-branch, 2-byte refill threshold, and the
8086/8088 4-vs-6 difference · all 14 registers with their dedicated uses · the flag register with bit
positions and the condition/control split · **physical address = segment × 16 + offset** and segment
overlap · the default/alternate segment table · the 12 addressing modes with EA/BA/MA rules and the
sign-extension rule · the legal EA combinations and why `[BP]` alone is unencodable · the instruction
format with D, W, MOD, REG, r/m tables · both architectural restrictions · the instruction mnemonics
and the instruction distinctions · the assembler directives and operators with examples (NPTEL +
institutional, agreeing) · the EVEN/alignment mechanism and the BHE̅/A₀ table · the reset vector
FFFF0H · MAX-mode bus status codes.
`likely`: **AAM = 83 clock cycles** (single-sourced) · that the instructor uses Bhurchandi's
**EA/BA/MA** notation (inferred from the prescribed text, not observed — no deck).
**`uncertain` — taxonomy, not fact:** the **number** of addressing modes (12 / 8 / 7 by convention)
and the **number** of instruction groups (7 / 8). Teach the mechanisms; state that counts vary.
**Quarantined and corrected:** "SF is used with unsigned numbers" — **wrong**, see §3 and
`CHANGELOG.md`.
Not claimed: per-instruction clock counts generally; the full opcode map; the 8087/8259/8255
peripherals (out of scope per `00-map.md`).

> **Stage 2 for this unit:** `stage-2/07-8086-microprocessor.md` — why segmentation was chosen over a
> wider register (and the 20-bit address-wraparound bug that became an ABI), how the ModR/M encoding
> makes the instruction length self-describing and what that costs a decoder, the real reason x86
> survived (binary compatibility as an economic moat), and how modern x86 decodes CISC into
> RISC-like micro-ops.
