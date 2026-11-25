# CAP (ECE2108) ETE — chat file
This file is the truth authority: answer from it, and say so before adding anything not in it. Every fact, number and program must be right (all numbers here were recomputed by script; every ALP was assembled and run on an 8086 emulator). Fractions as stacked display maths ($$\frac{a}{b}$$).

---

## 0. Books, paper, priority

**Books** (the course's references; truth comes from the book, never from a slide):

| Book | Governs | Weight |
|---|---|---|
| **Mano, *Computer System Architecture* 3e — his favourite** | everything except 8086 and RISC-V | Decks say "Ref: M. M. Mano". A2 = 15 of 15 Mano end-of-chapter problems; A1 = Mano ch. 4 problems with new numbers; ETE papers copy Mano sentences word for word. **Use Mano's notation, tables and methods.** |
| **Bhurchandi & Ray, *Advanced Microprocessors and Peripheral Devices* 3e** | 8086 | his 8086 decks follow it (EA, BA, MA; addressing-mode groups) |
| **Hamacher, *Computer Organization* 5e** | single-bus control sequences; functional units | 3 of 4 past papers ask "control signals … single bus architecture" |
| **Patterson & Hennessy, *COD RISC-V Ed.*** | RISC-V; the cache "sets and tag bits" question | |
| Sonal Yadav (AICTE) | secondary only | |

**Paper:** 3 h, 80 marks (scaled to 40), no calculator. A: 6 × 2–3 (fill-in, MCQ, true/false). B: 4 × 8. C: 2 × 10. D: 1 × 12, **always 8086 memory interfacing**. The past papers are the old code ECE2202 (same course, same professor's style). No paper has asked RISC-V yet; it is in this year's syllabus.

**Priority:** P1 = the two real ETEs (Apr–May 2025, Apr–May 2026) + assignments A1, A2, A3, Special Practice. P2 = June 2026 make-up, July 2026 summer, the Sept 2026 MTE.

**What repeats (most marks first):**

| Topic | Marks | Where |
|---|---|---|
| 8086 memory interfacing (EPROM + RAM, 20 address lines, multiplexed data) | 12–20 | all 4 papers, A3 Q9, Q10 |
| ALP: count +ve/−ve in 10 signed bytes + loop structures | 10 | ETE25 C2, ETE26 C1, A3 Q3; make-up C1 (block exchange), summer C2 (even/odd) |
| Control signals on single-bus CPU (Hamacher) | 8 | ETE26 B2, make-up B2, summer B2 |
| 8086 instruction group: list, operands, flags | 8 | ETE26 B3 (subtraction), make-up B3 (mul/div) |
| Mano 4-10 / 4-11 block diagrams; bus with MUX / tri-state | 8–10 | ETE26 B1, C2, make-up B1, A1 Q12, Q14 |
| I/O interface, strobe/handshake, isolated vs memory-mapped, async status bits | 5–8 | all 4 papers |
| Pipeline speedup + hazards | 3–10 | ETE25 B6, C1, summer A5, B3, make-up A5, MTE Q3, A2 Q11–15 |
| Logic microoperation A = 11011001 → 01101101 | 2–10 | ETE26 A2, make-up C2 |
| Bus MUX count/size, RAM-chip count, flag count, field/opcode bits | 2–3 each | every paper's section A |

---

## 1. P1 · ETE April–May 2026 (ECE2202), solved

**A1 (2).** First electronic computer: **(d) ENIAC**.

**A2 (2).** A = 11011001, B = 10110100, A becomes 01101101: **XOR (selective complement), A ← A ⊕ B**. 1s in B complement those bits of A. Check: 11011001 ⊕ 10110100 = 01101101.

**A3 (3).** 256K words = 2¹⁸ → address 18 bits; 64 registers → 6 bits; indirect 1 bit.
Opcode = 32 − 1 − 6 − 18 = **7 bits**. (= A2 Q1 = Mano 5-1.)

**A4 (3).** 2⁵ = 32 ≥ 30 → **5 bits**.

**A5 (3).**
$$\frac{2048}{128} = \mathbf{16\ chips}$$

**A6 (3).** 16 registers × 32 bits → **32 multiplexers, each 16 × 1** (4 select lines). Rule: n-bit registers, k of them → n MUXes of k × 1.

**B1 (8). Mano 4-10.** `xT: R1 ← R1 + R2`, `x′T: R1 ← R2`.
```
        R2 ──┬────────────────────────┐
             │                        ▼ B
             │                 ┌────────────┐
             │   R1 ──────────►│ 4-bit adder│ A
             │                 └─────┬──────┘
             ▼ I0 (x=0)              ▼ I1 (x=1)
        ┌──────────────────────────────────┐
  x ───►│ S   quadruple 2×1 MUX            │
        └────────────────┬─────────────────┘
                         ▼ 4 lines
  T ─────────────► Load  R1 (4-bit)  ◄─ clock
```
- MUX select S = x: x = 1 → adder output R1 + R2; x = 0 → R2.
- Load(R1) = xT + x′T = **T**. At the clock edge with T = 1, R1 takes the MUX output.

**B2 (8). Move [R1],R2 = Hamacher memory read** (R2 ← [[R1]]). Single bus; MAR, MDR, PC, IR, Y, Z, TEMP.

| Step | Signals |
|---|---|
| 1 | R1out, MARin, Read |
| 2 | MDRinE, WMFC (wait for memory function complete) |
| 3 | MDRout, R2in |

```
           step 1        step 2 (waits)        step 3
Clock     _|‾‾|__|‾‾|__|‾‾|__|‾‾|__|‾‾|__|‾‾|__
MARin     ‾‾‾‾‾‾‾‾__________________________________
Address   ====<  valid address from R1 ........>
Read      ‾‾‾‾‾‾‾‾______
MR            ‾‾‾‾‾‾‾‾____                (MAR → memory read)
MDRinE              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾_____
Data                     <== valid ==>
MFC                           ‾‾‾‾‾____
MDRout,R2in                            ‾‾‾‾‾‾‾‾
```
- Read is issued with the address; the processor waits (WMFC) until memory raises MFC; the word, latched in MDR, is then moved to R2.

**B3 (8). 8086 subtraction instructions** (Bhurchandi). Operands for SUB/SBB/CMP: reg,reg · reg,mem · mem,reg · reg,imm · mem,imm (never mem,mem; 8 or 16 bit).

| Instr | Operation | Operands | Flags |
|---|---|---|---|
| SUB d,s | d ← d − s | as above | OF SF ZF AF PF CF |
| SBB d,s | d ← d − s − CF | as above | OF SF ZF AF PF CF |
| DEC d | d ← d − 1 | reg / mem | OF SF ZF AF PF (**CF unchanged**) |
| NEG d | d ← 0 − d (2's complement) | reg / mem | all 6; CF = 1 unless d = 0 |
| CMP d,s | d − s, result discarded | as SUB | OF SF ZF AF PF CF |
| DAS | decimal adjust AL after BCD subtraction | AL implied | SF ZF AF PF CF (OF undefined) |
| AAS | ASCII adjust AL after subtraction | AL (AH) implied | AF CF (rest undefined) |

Example: `SUB AL, BL` with AL = 05H, BL = 07H → AL = FEH, CF = 1, SF = 1, ZF = 0.

**B4 (8). Interface** (Mano §11-2). An I/O interface is the hardware between the CPU bus and a peripheral that resolves their differences. Purpose: let the CPU control and exchange data with each device without disturbing the others. The **communication link** resolves four differences:
1. Peripherals are electromechanical/electromagnetic, CPU is electronic → **signal conversion**.
2. Peripherals are slower → **synchronization**.
3. Data codes and formats differ from CPU words → **format conversion**.
4. Operating modes differ per device → **control** of each without disturbing others.
Interface parts: data register, control register, status register, port select and register select decoding, I/O read/write lines. Four I/O commands: control, status, data output, data input.

**C1 (10). REPEAT-UNTIL vs WHILE-DO + count +ve/−ve.**

| | REPEAT-UNTIL (do-while) | WHILE-DO |
|---|---|---|
| Test | at the **bottom**, after the body | at the **top**, before the body |
| Body runs | **at least once** | zero or more times |
| 8086 form | body … `LOOP label` / `DEC` + `JNZ` | `JCXZ done` (or `CMP`+`Jcc`) … body … `JMP top` |
| Use case | process a 10-element array (count known ≥ 1) | process a block whose length may be 0 |

```asm
        ORG 100H
        JMP START
ARR     DB 81H,9EH,31H,0ABH,83H,0A4H,4FH,68H,92H,0A2H
PCNT    DB ?            ; count of positive numbers
NCNT    DB ?            ; count of negative numbers
START:  MOV CX, 10      ; 10 elements
        LEA SI, ARR
        XOR BX, BX      ; BL = +ve count, BH = -ve count
REPT:   MOV AL, [SI]
        TEST AL, 80H    ; MSB = sign bit
        JNZ NEG1
        INC BL          ; MSB 0 -> positive (0 counted as positive)
        JMP UNTIL
NEG1:   INC BH          ; MSB 1 -> negative
UNTIL:  INC SI
        LOOP REPT       ; CX = CX - 1, repeat until CX = 0
        MOV PCNT, BL
        MOV NCNT, BH
        RET
```
Result for this array: **PCNT = 03H, NCNT = 07H**. (Deck variant: `AND AL,80H` + `JNS`; `ROL AL,1` + `JC` also works.)

**C2 (10). Bus for four 4-bit registers: two ways** (Mano §4-3; = A1 Q14).
1. **Multiplexers:** four 4×1 MUXes. MUX i takes bit i of R0, R1, R2, R3. Common select S1S0 picks the register (00 → R0 … 11 → R3). The four MUX outputs form the 4-line bus, wired to the inputs of every register; the destination's Load decides who receives.
2. **Three-state buffers + decoder:** one group of 4 buffers per register (16 buffers). Bus line i is the wired join of bit i from each group. A 2×4 decoder (with enable) on S1S0 enables exactly one group, so only one register drives the bus; the rest are high-impedance. Decoder enable = 0 → bus floats.
```
 MUX bus (one bit line shown)          Tri-state bus (one bit line shown)
 R0₀ ─┐                                 R0₀ ─▷─┐ ◄ D0
 R1₀ ─┤ 4×1 ─► bus line 0               R1₀ ─▷─┤ ◄ D1   2×4 decoder: S1 S0, E
 R2₀ ─┤ MUX                             R2₀ ─▷─┼─► bus line 0
 R3₀ ─┘ S1 S0                           R3₀ ─▷─┘ ◄ D3
```
Selection table (both designs): S1S0 = 00 R0, 01 R1, 10 R2, 11 R3.

**D1 (12). Interface 2 × 8K×8 EPROM + 2 × 8K×8 RAM; decoder IC or gates?**
Method (deck, Part 3): see §1a. Answer:
- Pair = 16 KB; each chip on **A1–A13** (8K = 2¹³); even chip on D0–D7, odd chip on D8–D15.
- **EPROM FC000H–FFFFFH** (contains FFFF0H, the reset address). **RAM 00000H–03FFFH** (vector table area).
- Gates: C = NAND(A14…A19) (0 only when all 1) → EPROM. C′ = OR(A14…A19) (0 only when all 0) → RAM.
  CS1 (EPROM odd) = C + BHE̅ · CS2 (EPROM even) = C + A0 · CS3 (RAM odd) = C′ + BHE̅ · CS4 (RAM even) = C′ + A0 (all active low; "+" = OR gate).
- Decoder version: 74138 select inputs (LSB → MSB) BHE̅, A0, A14, enabled when A15–A19 = 1 (7430 NAND → E̅1, E̅2; inverter → E3). EPROM pair FC000–FFFFF (A14 = 1), RAM pair F8000–FBFFF (A14 = 0). Outputs O4 = word in EPROM, O5 = even EPROM byte, O6 = odd EPROM byte; O0, O1, O2 same for RAM. EPROM-even CS = AND(O4, O5), EPROM-odd = AND(O4, O6), RAM-even = AND(O0, O1), RAM-odd = AND(O0, O2).
- **Best: the decoder IC.** One 74138 + one NAND gives all four chip selects including word/byte selection, fewer ICs, same delay to every chip, and spare outputs for adding chips. Gates suit only 1–2 blocks, or a spec that puts RAM at 00000H and EPROM at the top (the deck's Q2 wording), which one decoder block cannot span.

### 1a. Memory interfacing method (all variants)

1. Two banks: **even bank D0–D7 selected by A0 = 0; odd bank D8–D15 selected by BHE̅ = 0.**
2. Each chip takes address lines from **A1** upward: chip of 2ⁿ bytes → A1…An.
3. EPROM at the **top** so **FFFF0H** (reset: CS = FFFFH, IP = 0000H) is inside it; RAM from **00000H**.
4. Remaining high lines decode the block: NAND (all 1s, top) or OR (all 0s, bottom), or a 74138.
5. Chip select (active low) = block select + bank select.
6. Multiplexed AD0–AD15: latch the address with **8282/74373 latches strobed by ALE**; data through 8286 transceivers (DT/R̅, DEN̅). Control: M/IO̅ with RD̅/WR̅ give MEMRD̅/MEMWR̅; EPROM gets only MEMRD̅ (to OE̅).

| BHE̅ | A0 | Access |
|---|---|---|
| 0 | 0 | whole word, both banks |
| 0 | 1 | upper byte, odd address (D8–D15) |
| 1 | 0 | lower byte, even address (D0–D7) |
| 1 | 1 | none |

| Variant | Chip lines | EPROM block | RAM block | Block decode |
|---|---|---|---|---|
| 2×16K EPROM, 2×32K RAM (ETE25 D1, A3 Q9, deck Q2) | EPROM A1–A14, RAM A1–A15 | F8000–FFFFF | 00000–0FFFF | C = NAND(A15–A19); C′ = OR(A16–A19) |
| 2×8K + 2×8K (ETE26 D1) | A1–A13 | FC000–FFFFF | 00000–03FFF | NAND / OR of A14–A19 |
| 2×4K + 2×4K (A3 Q10, make-up D1, summer D1) | A1–A12 | FE000–FFFFF | 00000–01FFF | NAND / OR of A13–A19 |
| deck's 4K decoder version | A1–A12 | FE000–FFFFF (A13 = 1) | FC000–FDFFF (A13 = 0) | 74138: A = BHE̅, B = A0, C = A13; enable NAND(A14–A19) |

Deck's 16K/32K map (draw it):
```
A19 A18 A17 A16 A15 | A14 … A0
 1   1   1   1   1  |  0 … 0  F8000H  ┐ 32 KB EPROM (two 16K chips)
 1   1   1   1   1  |  1 … 1  FFFFFH  ┘
 0   0   0   0 | A15 … A0
 0   0   0   0 |  0 … 0       00000H  ┐ 64 KB RAM (two 32K chips)
 0   0   0   0 |  1 … 1       0FFFFH  ┘
```
CS1 (EPROM odd) = C + BHE̅, CS2 (EPROM even) = C + A0, CS3 (RAM odd) = C′ + BHE̅, CS4 (RAM even) = C′ + A0.
Diagram: EPROMs' OE̅ ← MEMRD̅; RAMs' RD̅ ← MEMRD̅, WR̅ ← MEMWR̅; A1–A14 to EPROMs, A1–A15 to RAMs; odd chips on D8–D15, even on D0–D7.
Summer D1 says "starting address of EPROM is FFFFFH": read it as the EPROM pair ending at FFFFFH (FE000–FFFFF); state the assumption.

---

## 2. P1 · ETE April–May 2025 (EC2202), solved

**A1 (2).** = §1 A6 shape: 16 registers × 32 bits → **32 MUXes of 16 × 1** (4 select inputs each). (Mano 4-6.)

**A2 (2).** `M[AR] ← R3`: **memory write**. The content of R3 is written into the memory word whose address is in AR. (Mano 4-7.)

**A3 (2).** "Pipelining does not fit Flynn's classification": **True** (Mano §9-1). Flynn counts instruction/data streams; a pipeline overlaps the phases of one stream in time.

**A4 (2).** Mano's own example. On a miss the cache is checked first, then memory: miss time = 100 + 1000 = 1100 ns.
$$t_{avg} = h\,t_c + (1-h)(t_c + t_m) = 0.9(100) + 0.1(1100) = \mathbf{200\ ns}$$
(If cache and memory are accessed in parallel: 0.9(100) + 0.1(1000) = 190 ns. State the assumption; Mano's text gives 200 ns.)

**A5 (2).** P&H problem (byte-addressed, 4-byte words). Block = 4 words = 16 bytes → offset 4 bits. Direct-mapped: **sets = 4096** (one block per set) → index 12 bits. Tag = 32 − 12 − 4 = **16 bits**. Total tag bits = 16 × 4096 = **64 Kbits (65,536)**.
(2-way: 2048 sets, tag 17, 69,632 · 4-way: 1024 sets, tag 18, 73,728 · fully associative: 1 set, tag 28, 114,688.)

**B1 (5). 4-bit decrementer with four full adders** (Mano 4-13). A − 1 = A + 1111 (2's complement of 1).
```
   A3   1    A2   1    A1   1    A0   1
   │    │    │    │    │    │    │    │
  ┌▼────▼┐  ┌▼────▼┐  ┌▼────▼┐  ┌▼────▼┐
C4◄ FA  ◄──┤ FA  ◄──┤ FA  ◄──┤ FA  ◄── C0 = 0
  └──┬───┘  └──┬───┘  └──┬───┘  └──┬───┘
     D3        D2        D1        D0
```
Example: A = 0110 (6): 0110 + 1111 = 1 0101 → D = **0101 (5)**, carry ignored. A = 0000 → 1111 (−1 / 15), C4 = 0.

**B2 (5).** 7-bit signed 2's complement:
- +35 = 0100011 → −35 = **1011101**; +40 = 0101000 → −40 = **1011000**.
```
   1011101   (−35)
 + 1011000   (−40)
 ─────────
 1 0110101   7-bit result = 0110101 = +53 (wrong sign)
```
- Carry into sign bit = **0**, carry out = **1**: unequal → **overflow**. (−75 is outside −64 … +63.)

**B3 (5). MOV AX, [SI]** — **register indirect** (deck lists it as indexed; both accepted with the rule).
EA = (SI) = 1234H; BA = (DS) × 10H = 02000H; PA = 02000 + 1234 = **03234H**. AL ← [03234H], AH ← [03235H]. CS, IP, BX, AX do not take part.
Before/after: memory 03234H = low byte, 03235H = high byte → AX = (03235H)(03234H); SI, DS unchanged.

**B4 (5). Three-word instruction placement** (Mano 5-16(b)). 8-bit words; opcode word, then the 16-bit address in two words; operand at that address.
```
 address   content
 0100H     3A    ← opcode (word 1)            PC points here
 0101H     25    ← address high byte (word 2)
 0102H     30    ← address low byte  (word 3)  → effective address 2530H
 0103H     …     ← next instruction
   ⋮
 2530H     7B    ← 8-bit operand → DR
```
Fetch: AR ← PC, IR ← M[AR], PC ← PC+1; then two more reads into TR (high, low byte); AR ← TR; DR ← M[AR] (full list A2 Q8).

**B5 (5). Six status bits of an asynchronous communication interface** (Mano §11-3):
1. Transmitter (buffer) register empty — ready for next character.
2. Transmitter shift register empty.
3. Receiver register full — character available.
4. Parity error — received character's parity wrong.
5. Framing error — no valid stop bit.
6. Overrun error — new character arrived before the previous one was read.

**B6 (5).** t_n = 80 ns, k = 4, t_p = 20 ns, n = 100.
$$S = \frac{n\,t_n}{(k+n-1)\,t_p} = \frac{100 \times 80}{103 \times 20} = \frac{8000}{2060} = \mathbf{3.88} \qquad S_{max} = \frac{t_n}{t_p} = \frac{80}{20} = \mathbf{4}$$

**C1 (10). Pipeline conflicts** (Mano §9-4/9-5). Conflicts (hazards) stop a pipeline from completing one instruction per clock:

| Hazard | Cause | Example | Fix |
|---|---|---|---|
| **Resource (structural)** | two segments need the same hardware, usually memory | FI of one instruction and FO of another both access memory | separate instruction and data memories / caches |
| **Data dependency** | an instruction needs a result not yet produced | `ADD R1,R2,R3` then `SUB R4,R1,R5` | hardware interlock (stall), **operand forwarding**, delayed load (compiler inserts no-op/reorders) |
| **Branch (control)** | branch changes PC; fetched instructions are wrong | `JMP` / conditional branch | prefetch target, branch target buffer, loop buffer, branch prediction, **delayed branch** |

Technique, with example — **operand forwarding**: in `ADD R1,R2,R3; SUB R4,R1,R5`, the ALU result of ADD is routed straight back to the ALU input for SUB through a bypass path, instead of waiting for R1 to be written, so no stall. Delayed branch: compiler fills the slot after a branch with a useful instruction (or no-op) that always executes.

**C2 (10).** = §1 C1 program ("ten signed hex numbers", Repeat-Until).

**D1 (20).** = §1a, 16K/32K row. Write: memory map table, address-bit map, gate logic (C, C′, four CS), full diagram, BHE̅/A0 table.

---

## 3. P1 · Assignment 3 (8086 + memory), solved

**Q1.** `MOV CX, [1234H]` — **direct addressing**. EA = 1234H, BA = 0200H × 10H = 02000H, **PA = 03234H**. CL ← [03234H], CH ← [03235H]. Before: CX = ?, memory 03234H = x, 03235H = y. After: CX = yx; memory unchanged.

**Q2. Capital → small case.** ASCII 'A'–'Z' = 41H–5AH, 'a'–'z' = 61H–7AH; difference 20H.
```asm
        ORG 100H
        JMP START
CHAR    DB 'A'
RES     DB ?
START:  MOV AL, CHAR
        CMP AL, 'A'
        JB  DONE        ; below 'A': not a capital
        CMP AL, 'Z'
        JA  DONE        ; above 'Z': not a capital
        ADD AL, 20H     ; 'A'(41H) -> 'a'(61H)
DONE:   MOV RES, AL
        RET
```
Test: 'A' → 'a', 'Z' → 'z', 'a' and '5' unchanged.

**Q3.** = §1 C1.

**Q4. Exchange two 10-byte blocks, While loop.**
```asm
        MOV SI, 1200H   ; block 1
        MOV DI, 1220H   ; block 2
        MOV CX, 10
WHILE1: JCXZ DONE       ; test first (while CX != 0)
        MOV AL, [SI]
        XCHG AL, [DI]   ; AL <-> block-2 byte
        MOV [SI], AL
        INC SI
        INC DI
        DEC CX
        JMP WHILE1
DONE:   RET
```
(Deck version: same body, `CMP CL,0` / `JZ` at the top.)

**Q5. Move 16-byte string 7000:0200H → 7000:0300H.** Flowchart: Start → DS = ES = 7000H → SI = 0200H, DI = 0300H, CX = 16 → DF = 0 → [ES:DI] ← [DS:SI], SI+1, DI+1, CX−1 → CX = 0? no: repeat; yes: End.
```asm
        MOV AX, 7000H
        MOV DS, AX      ; source segment
        MOV ES, AX      ; destination segment (MOVS writes ES:DI)
        MOV SI, 0200H
        MOV DI, 0300H
        MOV CX, 16      ; byte count
        CLD             ; DF = 0: auto-increment
        REP MOVSB       ; repeat CX times
        HLT
```
Test: 70200H–7020FH = 41H…50H ('A'…'P') → after run 70300H–7030FH = 41H…50H; source unchanged.

**Q6. Binary → Gray.** G = B ⊕ (B >> 1).
```asm
        MOV AL, BIN     ; e.g. B6H = 1011 0110
        MOV BL, AL
        SHR BL, 1       ; B >> 1 = 0101 1011
        XOR AL, BL      ; Gray = 1110 1101 = EDH
        MOV GRAY, AL
```

**Q7. Square root of a perfect square** (sum of first n odd numbers = n²).
```asm
        MOV AL, NUM     ; e.g. 49
        MOV BL, 1       ; current odd number
        XOR CL, CL      ; root counter
NEXT:   INC CL
        SUB AL, BL      ; subtract 1, 3, 5, ...
        JZ  DONE
        ADD BL, 2
        JMP NEXT
DONE:   MOV ROOT, CL    ; 49 -> 7
```
49 − 1 − 3 − 5 − 7 − 9 − 11 − 13 = 0 after 7 subtractions → root 7. (Tested 16, 25, 49, 64, 81.)

**Q8. Mano 12-2.** RAM 256×8, ROM 1024×8; need 2 KB RAM, 4 KB ROM, 4 interfaces × 4 registers.
- (a) RAM chips = 2048/256 = **8**; ROM chips = 4096/1024 = **4**; interface registers = **16**.
- Address: largest block (ROM 4 KB) needs 12 bits; plus 2 highest-order select bits → **14-bit address**.

| Component | Hex range | A13 A12 | Lines used inside |
|---|---|---|---|
| RAM (8 chips) | **0000–07FF** | 00 | 3-to-8 decoder on A10–A8, chip on A7–A0 |
| ROM (4 chips) | **1000–1FFF** | 01 | 2-to-4 decoder on A11–A10, chip on A9–A0 |
| Interface (16 regs) | **2000–200F** | 10 | 2 bits unit select, 2 bits register select (A3–A0) |

**Q9.** = §1a 16K/32K. **Q10.** = §1a 4K row (gates); add the deck's 74138 version if asked "decoder".

---

## 4. P1 · Special Practice Assignment, solved

| Q | Answer |
|---|---|
| 1 | **Von Neumann** (stored-program) model |
| 2 | CPU (ALU + control unit), memory, input/output |
| 3 | Word length = number of bits the CPU processes as one unit (register / data-bus width); 8086 = 16 bits |
| 4 | Mnemonic = short symbolic name for an opcode (MOV, ADD) |
| 5 | Instruction = binary command telling the processor to do one operation: opcode + operand(s) |
| 6 | 1M × 16: **20 address lines** (2²⁰ = 1M), **16 data lines** |
| 7 | **16** chips |
| 8 | `Sum EQU 200` gives the name Sum the constant value 200; the assembler substitutes 200 wherever Sum appears; no memory, no machine code |

**Q9.** `XCHG AX, BX`: swaps (AX = 1234H, BX = 5678H → AX = 5678H, BX = 1234H); reg–reg or reg–mem; no flags. `CMP AL, BL`: AL − BL, result discarded, sets OF SF ZF AF PF CF (AL = 05, BL = 07 → CF = 1, ZF = 0). `MOVSB/MOVSW`: [ES:DI] ← [DS:SI], then SI, DI ± 1 (byte) or ± 2 (word) by DF; no flags. `CLD`: DF ← 0 → string ops auto-increment.

**Q10.** Immediate: operand in the instruction, `MOV AL, 50H`. Based indexed with displacement: EA = BX/BP + SI/DI + disp, `MOV AH, [BX][SI] + 1234H`, PA = DS × 10H + EA (SS if BP).

**Q11.**

| Compiler | Interpreter |
|---|---|
| translates whole program to object code first | translates and executes line by line |
| errors listed after full compilation | stops at first error |
| fast execution, object file kept | slower, no object file |
| C, C++ | Python, BASIC |

**Q12.** Bus = shared group of lines between CPU, memory and I/O. **Address bus** (unidirectional, CPU → memory/I/O; 8086: 20 lines, 1 MB). **Data bus** (bidirectional, carries data; 8086: 16 lines). **Control bus** (RD̅, WR̅, M/IO̅, ALE, INTR…; timing and direction).

**Q13.** 8086 flag (status) register: 16 bits, 9 used — 6 status + 3 control (table §8.4).

**Q14.** **DT/R̅** (min mode): data transmit/receive; 1 = CPU sends (write), 0 = CPU receives (read); sets direction of the 8286 transceivers. **DEN̅**: data enable, active low; enables the transceivers while data is on the bus (mid-T2 to mid-T4).

**Q15.** DS = 1000H → BA = 10000H.
- (i) `MOV AX, [BX]`: register indirect. EA = 2000H, **PA = 12000H**.
- (ii) `MOV AX, 5000[BX][SI]`: based indexed with displacement. EA = 5000 + 2000 + 3000 = **A000H**, **PA = 1A000H**.

**Q16.**

| Instr | Action | Example | Flags |
|---|---|---|---|
| AND d,s | bitwise AND | AL = 0F5H, `AND AL,0FH` → 05H | CF = OF = 0; SF ZF PF set; AF undefined |
| SAR d,1/CL | arithmetic right shift, sign bit copied | AL = 94H (−108) → CAH (−54), CF = 0 | CF = last bit out; SF ZF PF; OF = 0 for count 1 |
| REPE / REPZ | repeat string instruction while CX ≠ 0 and ZF = 1 | `REPE CMPSB` compares until mismatch | none itself |
| CMPS | [DS:SI] − [ES:DI], SI/DI ± 1/2 | `CMPSB` | OF SF ZF AF PF CF |
| NOP | no operation, 3 clocks | delay / padding | none |

**Q17. Queue.** 6-byte FIFO in the BIU. BIU fetches ahead while EU executes (pipelining). Refill starts when 2 bytes are free (word fetch). EU takes bytes from the queue's front; empty queue → EU waits. On JMP/CALL/RET the queue is flushed and refilled from the new address.

**Q18.**
```asm
        MOV AX, 2000H
        MOV DS, AX      ; DS = 2000H
        MOV BX, [0500H] ; word at 20500H -> BX
        MOV CX, BX      ; and to CX
        MOV AL, [0600H] ; byte at 20600H
        ADD AL, 05H     ; add immediate 05H
        MOV [0700H], AL ; result -> 20700H
```

**Q19.** Count of 'e' in "exercise" = **3**.
```asm
STR     DB 'exercise'
COUNT   DB ?
        LEA SI, STR
        MOV CX, 8
        XOR BL, BL
NEXT:   CMP BYTE PTR [SI], 'e'
        JNE SKIP
        INC BL
SKIP:   INC SI
        LOOP NEXT
        MOV COUNT, BL   ; 3
```

**Q20. 16-bit binary → BCD** (divide by 10, remainders are digits).
```asm
        MOV AX, BIN     ; e.g. FFFFH = 65535
        MOV BX, 10
        XOR CX, CX      ; digit count
NEXT:   XOR DX, DX
        DIV BX          ; AX = quotient, DX = remainder (one digit)
        PUSH DX
        INC CX
        OR  AX, AX
        JNZ NEXT
        LEA DI, BCD     ; store most significant digit first
POPD:   POP DX
        MOV [DI], DL
        INC DI
        LOOP POPD       ; FFFFH -> 06 05 05 03 05
```
(Unpacked BCD, one digit per byte; packed = two digits per byte, 65535 → 06 55 35.)

---

## 5. P1 · Assignment 2 (= Mano 5-1 … 5-21, 9-1 … 9-11), solved

**Q1 (5-1).** Address 18 bits, register 6, I 1, **opcode 7**. Format: `I(1) | opcode(7) | register(6) | address(18)` = 32. Memory: **18 address inputs, 32 data inputs**.

**Q2 (5-3).** Bus select: 1 AR, 2 PC, 3 DR, 4 AC, 5 IR, 6 TR, 7 memory.
a. 111, LD IR, read → **IR ← M[AR]** · b. 110, LD PC → **PC ← TR** · c. 100, LD DR, write → **DR ← AC, M[AR] ← AC** · d. 000, LD AC, add → **AC ← AC + DR**.

**Q3 (5-4).**

| Transfer | S2S1S0 | LD | Memory | Adder/logic |
|---|---|---|---|---|
| AR ← PC | 010 | AR | — | — |
| IR ← M[AR] | 111 | IR | read | — |
| M[AR] ← TR | 110 | — | write | — |
| AC ← DR, DR ← AC | 100 | AC, DR | — | transfer DR to AC |

**Q4 (5-6).**
- 0001 0000 0010 0100 = **1024H**: I = 0, opcode 001 **ADD**, address 024 → AC ← AC + M[024]. Memory-reference, direct. (= MTE Q2.)
- 1011 0001 0010 0100 = **B124H**: I = 1, opcode 011 **STA** indirect → M[M[124]] ← AC.
- 0111 0000 0010 0000 = **7020H**: opcode 111, I = 0 → register-reference, bit 5 → **INC**: AC ← AC + 1.

**Q5 (5-8). C7T3: SC ← 0.** C7 goes high with the clock edge that starts T3. At the next positive edge (end of T3) SC is cleared, so T0 follows T3 instead of T4.
```
Clock  _|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_
T0     ‾‾‾‾____________________‾‾‾‾      (T0 again after T3)
T1     ____‾‾‾‾________________
T2     ________‾‾‾‾____________
T3     ____________‾‾‾‾________
T4     ________________________  (never occurs)
C7     ____________‾‾‾‾________
SC     0   1   2   3   0
```

**Q6 (5-9).** AC = A937, E = 1, PC = 021 (Mano). Each row: IR = code, AR = low 12 bits.

| Instr | IR | AC | E | PC |
|---|---|---|---|---|
| CLA | 7800 | 0000 | 1 | 022 |
| CLE | 7400 | A937 | 0 | 022 |
| CMA | 7200 | 56C8 | 1 | 022 |
| CME | 7100 | A937 | 0 | 022 |
| CIR | 7080 | D49B | 1 | 022 |
| CIL | 7040 | 526F | 1 | 022 |
| INC | 7020 | A938 | 1 | 022 |
| SPA | 7010 | A937 | 1 | 022 (AC negative, no skip) |
| SNA | 7008 | A937 | 1 | **023** (skip) |
| SZA | 7004 | A937 | 1 | 022 |
| SZE | 7002 | A937 | 1 | 022 |
| HLT | 7001 | A937 | 1 | 022 (S ← 0) |
CLA alone: AC = 0000, E = 1, PC = 022, AR = 800, IR = 7800.

**Q7 (5-12) = MTE Q6.** M[3AF] = 932E → I = 1, opcode 001 **ADD indirect**, address 32E. M[32E] = 09AC = effective address; M[9AC] = 8B9F = operand.
```
  0111 1110 1100 0011   AC = 7EC3
+ 1000 1011 1001 1111   DR = 8B9F
─────────────────────
1 0000 1010 0110 0010   AC = 0A62, E = 1
```
End of cycle: PC = 3B0, AR = 9AC, DR = 8B9F, AC = 0A62, IR = 932E, E = 1, I = 1, SC = 0000.

**Q8 (5-16).** (Assume first address word = high byte.)
```
T0: AR ← PC
T1: IR ← M[AR], PC ← PC + 1
T2: AR ← PC
T3: TR(8–15) ← M[AR], PC ← PC + 1
T4: AR ← PC
T5: TR(0–7) ← M[AR], PC ← PC + 1
T6: AR ← TR
T7: DR ← M[AR]
```

**Q9 (5-20). JK flip-flop F.** J = xT3 + zT2 + wT5·G; K = yT1 + zT2 + wT5·G′.
Check: set → J = 1, K = 0; clear → K = 1; complement → J = K = 1; transfer G → G = 1 sets, G = 0 clears.
Gates: AND(x,T3), AND(y,T1), AND(z,T2), P = AND(w,T5), AND(P,G), AND(P,G′), OR → J, OR → K.

**Q10 (5-21). PC control gates.**
- LD(PC) = D4T4 + D5T5 (BUN, BSA)
- CLR(PC) = RT1 (interrupt)
- INR(PC) = R′T1 + RT2 + D6T6·(DR = 0) + r(B4·AC15′ + B3·AC15 + B2·(AC = 0) + B1·E′) + p(B9·FGI + B8·FGO), with r = D7I′T3, p = D7IT3.

**Q11 (9-1). (Ai + Bi)(Ci + Di).** Segment 1: R1 ← Ai, R2 ← Bi, R3 ← Ci, R4 ← Di. Segment 2: R5 ← R1 + R2, R6 ← R3 + R4. Segment 3: R7 ← R5 × R6.

| Clock | R1 R2 R3 R4 | R5, R6 | R7 |
|---|---|---|---|
| 1 | A1 B1 C1 D1 | — | — |
| 2 | A2 B2 C2 D2 | A1+B1, C1+D1 | — |
| 3 | A3 B3 C3 D3 | A2+B2, C2+D2 | (A1+B1)(C1+D1) |
| 4 | A4 … D4 | i = 3 sums | i = 2 product |
| 5 | A5 … D5 | i = 4 sums | i = 3 product |
| 6 | A6 … D6 | i = 5 sums | i = 4 product |
| 7 | — | A6+B6, C6+D6 | i = 5 product |
| 8 | — | — | (A6+B6)(C6+D6) |

**Q12 (9-3).** k + n − 1 = 6 + 199 = **205 cycles**.

**Q13 (9-5). (Ai × Bi) + Ci.** Segment 1: R1 ← Ai, R2 ← Bi (40 ns). Segment 2: R3 ← R1 × R2, R4 ← Ci (45 + 5 = 50 ns). Segment 3: R5 ← R3 + R4 (15 ns).
- a. t_p = **50 ns** (largest segment). b. t_n = 40 + 45 + 15 = **100 ns**.
- c.
$$S_{10} = \frac{10 \times 100}{12 \times 50} = \mathbf{1.67} \qquad S_{100} = \frac{100 \times 100}{102 \times 50} = \mathbf{1.96}$$
- d. S_max = 100/50 = **2**.
Register table (MTE Q7 adds it): clock 1: R1 = A1, R2 = B1; clock 2: R3 = A1B1, R4 = C1, R1 R2 = A2 B2; clock 3: R5 = A1B1 + C1, R3 = A2B2, R4 = C2, R1 R2 = A3 B3; … clock 8: R5 = A6B6 + C6.

**Q14 (9-10). Branch hardware:**
1. **Prefetch target instruction** — fetch both the target and the next sequential instruction; keep both until the branch resolves.
2. **Branch target buffer (BTB)** — associative memory holding recent branch addresses with their target instructions; a hit supplies the target at once.
3. **Loop buffer** — small fast register file holding a whole loop; the loop runs without memory fetches.
4. **Branch prediction** — guess the outcome (from history) and fetch along the predicted path.
(Software: **delayed branch** — compiler fills the slot after the branch.)

**Q15 (9-11).** Four segments FI, DA, FO, EX; step 4:
- Load (1st) in **EX**: R1 ← M[312] completed (word transferred to R1).
- ADD (2nd) in **FO**: operand M[313] fetched.
- INC (3rd) in **DA**: decoded (no address to compute).
- STORE (4th) in **FI**: fetched from memory.

---

## 6. P1 · Assignment 1 (Mano ch. 1–4), solved

**Q1.** (i) **Digital computer**: a digital system that performs computational tasks, with information in variables of a limited number of discrete values (binary). (ii) **Architecture**: the attributes visible to the programmer — instruction set, data types, addressing modes, registers (what it does). (iii) **Organization**: the operational units and their interconnections that implement the architecture — control signals, interfaces, memory technology (how). (iv) **Microarchitecture**: the specific implementation of an ISA — datapath, control, pipelining, caches. (v) **Microoperation**: an elementary operation on data stored in registers, done in one clock pulse. (vi) **RTL**: symbolic notation describing microoperation transfers among registers.

**Q2.** Architecture vs organization:

| Architecture | Organization |
|---|---|
| what the computer does | how it does it |
| functional behaviour | structural relationships |
| high-level design (ISA) | low-level design (circuits) |
| instruction set, registers, data types, addressing modes | control signals, buses, adders, memory technology |
| decided first | follows the architecture |

**Q3. Generations** (dates approximate):

| Gen | Period | Technology | Machines | People |
|---|---|---|---|---|
| 1 | 1945–56 | vacuum tubes, machine language | ENIAC, EDVAC, UNIVAC I | Eckert & Mauchly, von Neumann |
| 2 | 1956–64 | transistors, magnetic core, assembly + FORTRAN | IBM 7090, TX-0 | Bardeen, Brattain, Shockley; Backus |
| 3 | 1964–71 | ICs (SSI/MSI), operating systems | IBM System/360 | Kilby, Noyce |
| 4 | 1971–80s | LSI/VLSI, microprocessor, PCs | Intel 4004, IBM PC | Hoff, Faggin |
| 5 | 1980s– | ULSI, parallel processing, AI | Japan FGCS project | — |

**Q4. Functional units** (Hamacher): input (accepts data/program), memory (stores; primary and secondary), ALU (arithmetic/logic on registers), output (sends results), control unit (timing and control signals to all units). Processor = ALU + control.

**Q5. Types:** by size — personal, notebook, workstation, mainframe/enterprise, server, supercomputer; by data — analog, digital, hybrid; by purpose — general-purpose, special-purpose/embedded.

**Q6.**

| von Neumann | Harvard |
|---|---|
| one memory for program and data | separate program and data memories |
| one shared bus | separate buses |
| fetch and data access take turns (von Neumann bottleneck) | fetch and data access simultaneously |
| simpler, cheaper | faster, more hardware |
| general-purpose PCs | DSPs, microcontrollers, split L1 caches |
Features of von Neumann: stored-program concept (program in memory as binary, like data), sequential execution, CPU + memory + I/O, single shared path.

**Q7. Circuits** (Mano ch. 2):
- (i) D flip-flop: Q(t+1) = D at the clock edge (gated SR with S = D, R = D′).
- (ii) 3-to-8 decoder: 8 AND gates, each one minterm of A2A1A0, with enable E; E = 0 → all outputs 0.
- (iii) 4-to-1 MUX: Y = S1′S0′I0 + S1′S0I1 + S1S0′I2 + S1S0I3.
- (iv) Quadruple 2×1 MUX: four 2-to-1 MUXes sharing select S and enable E: Y = A if S = 0, B if S = 1.
- (v) 4-bit register with parallel load: 4 D flip-flops; each D = Load·Iᵢ + Load′·Qᵢ (2×1 MUX feedback); common clock, clear.
- (vi) Bidirectional shift register with parallel load: each flip-flop driven by a 4×1 MUX: S1S0 = 00 no change, 01 shift right, 10 shift left, 11 parallel load.

**Q8.** 8 bits:

| | +64 | −64 |
|---|---|---|
| signed magnitude | 01000000 | 11000000 |
| 1's complement | 01000000 | 10111111 |
| 2's complement | 01000000 | 11000000 |

**Q9.** 01000000 (+64) + 01010100 (+84) = **10010100**. Carry into sign 1, carry out 0 → **overflow**; 148 > +127 (result reads −108).

**Q10.** (i) A ← B: register transfer. (ii) A(L) ← B(H): register transfer of a field — high byte of B into low byte of A. (iii) R1 ← M[AR]: memory read. (iv) M ← R2: memory write into M[AR].

**Q11.** **S: AL ← BH** — when control S = 1, the high half of B is copied into the low half of A at the clock edge.

**Q12.** **yT2: R2 ← R1, R1 ← R2** — simultaneous exchange. AND gate y·T2 drives Load of both R1 and R2; R1 outputs → R2 inputs, R2 outputs → R1 inputs; both load on the same edge (old values read before the edge).

**Q13.** Bus = group of common lines (one per bit) carrying data between registers/units, one source at a time. Role: replaces n(n−1) point-to-point links. Five structures: ISA, EISA, PCI, PCI Express, USB (also SCSI, VESA Local Bus).

**Q14.** = §1 C2.

**Q15.** Microoperation = §6 Q1(v). Types: register transfer, arithmetic, logic, shift.

**Q16.** M = 0 add, M = 1 subtract (B XORed with M, C0 = M).
- (i) M = 0: 0111 + 0110 = **1101**, C4 = 0.
- (ii) M = 1: 0101 + 0101 + 1 = **1011**, C4 = 0 (5 − 10 = −5 in 2's complement).

**Q17. ALSU** (Mano Table 4-8; table §8.1). i) Transfer A: S3S2S1S0 Cin = 0000 0. ii) Add with carry: 0001 1 → A + B + 1. iii) XOR: 0110 x. iv) Shift right A: 10xx x.

**Q18 (Mano 4-19).** R1 = 11110010, R2 = 11111111, R3 = 10111001, R4 = 11101010.
- i) R1 ← R1 + R2 = 11110001 (carry out 1).
- ii) R3 ← R3 ∧ R4 = 10101000; R2 ← R2 + 1 = 00000000.
- iii) R1 ← R1 − R3 = 11110001 − 10101000 = 01001001.
- **Final: R1 = 01001001, R2 = 00000000, R3 = 10101000, R4 = 11101010.**

**Q19.** From R = 11111111, each on the previous result: shr → **01111111**; cir → **10111111**; shl → **01111110**; cil → **11111100**.

**Q20.**

| CISC | RISC |
|---|---|
| many, complex instructions | few, simple instructions |
| variable length (8086: 1–6 bytes) | fixed length (32 bits) |
| many addressing modes | few addressing modes |
| memory operands in most instructions | load/store only; register-to-register ALU ops |
| few registers | many registers |
| multi-cycle instructions | ~1 instruction per cycle, pipelined |
| microprogrammed control | hardwired control |
| complexity in hardware | complexity in compiler |
| 8086, x86 | RISC-V, ARM |

---

## 7. P2 · June 2026 make-up, July 2026 summer, Sept 2026 MTE (new items only)

**Make-up June 2026**
- A1: 8086 flag register has **(c) 9 flags**.
- A2: **16** chips.
- A3: async, 1 start + 8 data + 2 stop = 11 bits/char → 1200/11 = **109 characters/s** (synchronous: 150; one stop bit: 120).
- A4: 5 bits → **32** microoperations.
- A5: k + n − 1 = 7 + 99 = **106** clock cycles.
- A6: 32 registers × 16 bits → 16 MUXes, each **32 × 1** (5 select lines).
- B1 (Mano 4-11): `x: R1 ← R1 + R2`, `x′y: R1 ← R1 + 1`. R1 = 4-bit counter with parallel load; adder inputs R1 and R2; adder output → R1's parallel inputs. **Load = x**, **Increment = x′y** (AND of x′ and y). Clock to R1.
- B2: **unconditional branch, Hamacher:**

| Step | Signals |
|---|---|
| 1 | PCout, MARin, Read, Select4, Add, Zin |
| 2 | Zout, PCin, Yin, WMFC |
| 3 | MDRout, IRin |
| 4 | Offset-field-of-IRout, Add, Zin |
| 5 | Zout, PCin, End |
Steps 1–3 fetch (Y keeps the updated PC). Step 4 adds the branch offset to it; step 5 loads the new PC. (Conditional branch: step 4 adds "If N = 0 then End".)
- B3: **multiply/divide** (operand reg/mem, 8 or 16 bit, never immediate):

| Instr | Byte | Word | Flags |
|---|---|---|---|
| MUL s (unsigned) | AX ← AL × s | DX:AX ← AX × s | CF = OF = 1 if upper half ≠ 0; SF ZF AF PF undefined |
| IMUL s (signed) | AX ← AL × s | DX:AX ← AX × s | CF = OF = 1 if upper half is not a sign extension; others undefined |
| DIV s (unsigned) | AL ← AX / s, AH ← rem | AX ← DX:AX / s, DX ← rem | all undefined; quotient too big or s = 0 → type 0 interrupt |
| IDIV s (signed) | same, signed | same, signed | same |
| AAM | AH ← AL / 10, AL ← AL mod 10 | | SF ZF PF; OF AF CF undefined |
| AAD | AL ← AH × 10 + AL, AH ← 0 | | SF ZF PF; OF AF CF undefined |
| CBW / CWD | AL sign → AH | AX sign → DX | none |
- B4: **isolated vs memory-mapped I/O:**

| Isolated I/O | Memory-mapped I/O |
|---|---|
| separate address space for I/O | I/O registers occupy memory addresses |
| separate control lines (IOR̅, IOW̅ / M/IO̅) | same read/write lines as memory |
| special instructions IN, OUT (8086) | any memory instruction (MOV, AND…) works on devices |
| full memory space kept | memory space reduced |
| + clear in program, protects memory map; − few I/O instructions, extra lines | + powerful instructions on I/O, simple; − uses addresses, I/O and memory decoding mixed |
- C1: LOOP structures = §1 C1 table (REPEAT-UNTIL, WHILE-DO, plus `LOOP`, `LOOPE/LOOPZ`, `LOOPNE/LOOPNZ`, `JCXZ`); program = §3 Q4.
- C2 (Mano 4-17 + 4-18): one stage = 4×1 MUX with inputs I0 = Ai ⊕ Bi, I1 = (Ai ⊕ Bi)′, I2 = (Ai + Bi)′, I3 = (AiBi)′; select S1S0 = 00 XOR, 01 XNOR, 10 NOR, 11 NAND; output Ei. Truth table per gate. A = 11011001 → 01101101: **B = 10110100, XOR, S1S0 = 00**.
- D1: = §1a 4K row (gates and 74138 versions; justification as §1 D1).

**Summer July 2026**
- A1: control flags = **(d) 3** (TF, IF, DF).
- A2: 4K × 8: **4096 words, 8-bit word, 32,768 bits = 4 KB**.
- A3: **(d) 256 KB** active at a time (four segments × 64 KB).
- A4: **(b) 2ᵏ**.
- A5: = MTE Q3: **4.76**, max **5**.
- A6: **True** (Mano §11-7: the IOP combines interface logic with DMA).
- B1: shifts — need: multiply/divide by 2, serial transfer, bit testing, packing. Logical (0 in), circular (bit out re-enters), arithmetic (sign kept on right shift; overflow if sign changes on left shift). From R = 11011101 in the asked order: shr **01101110**, cir **00110111**, shl **01101110**, cil **11011100**. (If R = 11111111: §6 Q19.) (Mano 4-21 order shl, cir, shr, cil: 10111010, 01011101, 00101110, 01011100.)
- B2: **Add [R3],R1** (R1 ← [[R3]] + R1), Hamacher:

| Step | Signals |
|---|---|
| 1 | PCout, MARin, Read, Select4, Add, Zin |
| 2 | Zout, PCin, Yin, WMFC |
| 3 | MDRout, IRin |
| 4 | R3out, MARin, Read |
| 5 | R1out, Yin, WMFC |
| 6 | MDRout, SelectY, Add, Zin |
| 7 | Zout, R1in, End |
- B3: **parallel processing** = simultaneous data processing to raise throughput (multiple functional units, Flynn classes). **Pipeline** = splitting a process into sub-operations in segments that overlap, each with a register. Relation: pipelining is a form of parallel processing (temporal overlap, not counted by Flynn).
- B4: **destination-initiated strobe**: destination pulses strobe to request; source puts data on the bus; destination reads at the strobe's trailing edge. Weakness: no confirmation the data was valid/accepted. **Destination-initiated handshake**: destination raises "ready for data" → source puts data, raises "data valid" → destination accepts, drops "ready for data" → source drops "data valid". Two control lines, both units take part, timeouts detect failure.
```
Strobe:      Data bus   ────<  valid  >──
             Strobe     ___|‾‾‾‾‾‾|______   (from destination)
Handshake:   Ready for data ‾‾‾‾‾‾|_______
             Data valid     ____|‾‾‾‾‾‾|__
             Data bus       ───<  valid  >─
```
- C1 (Mano 5-5): **none can run in one clock in the basic computer:**
  - a. IR ← M[PC]: memory is addressed only by AR. → T0: AR ← PC; T1: IR ← M[AR].
  - b. AC ← AC + TR: adder takes only AC and DR. → T: DR ← TR; T+1: AC ← AC + DR.
  - c. DR ← DR + AC (AC unchanged): adder output goes only to AC. → AC ← AC + DR, DR ← AC (bus carries old AC); then AC ← DR, DR ← AC (swap) → DR = sum, AC restored.
- C2: even/odd. Algorithm: count = 10, SI → array; for each: test bit 0; 1 → odd++, 0 → even++; store.
```asm
        MOV AX, 2000H   ; data segment (not the code segment)
        MOV DS, AX
        MOV SI, 0100H   ; ten numbers at DS:0100H-0109H
        MOV CX, 10
        XOR BX, BX      ; BL = odd count, BH = even count
NEXT:   MOV AL, [SI]
        TEST AL, 01H    ; LSB 1 = odd
        JZ  EVEN1
        INC BL
        JMP CONT
EVEN1:  INC BH
CONT:   INC SI
        LOOP NEXT
        MOV [010CH], BL ; odd count
        MOV [010DH], BH ; even count
        HLT
```
- D1: = §1a 4K row.

**MTE Sept 2026**
- Q1: masking = AND. R1 ∧ 1100 = 1000 → original R1 = **10xx** (1000, 1001, 1010 or 1011); bits 1 and 0 were masked (cleared).
- Q2: = §5 Q4, 1024H = ADD, memory-reference.
- Q3: Mano 9-4: **4.76**, max **5**.
$$S = \frac{100 \times 50}{(6 + 99) \times 10} = \frac{5000}{1050} = 4.76 \qquad S_{max} = \frac{50}{10} = 5$$
- Q4: `x + yT2: AR ← AR + BR`: control = OR(x, AND(y, T2)) → Load(AR); adder inputs AR, BR; adder output → AR inputs.
- Q5 (Mano 5-2): direct: address part = operand address → **1 memory reference** for the operand. Indirect (I = 1): address part points to the operand's address → **2 references**. Example: ADD 32E direct: AC ← AC + M[32E]; indirect: AC ← AC + M[M[32E]].
- Q6: = §5 Q7. Q7: = §5 Q13 (S10 = 1.67).

---

## 8. Compact concepts (by unit)

### 8.1 U1 · RTL and microoperations (Mano ch. 4)
- `P: R2 ← R1` (only when P = 1) · `,` = same clock · `M[AR]` memory word · `+` in control function = OR.
- Bus of k registers × n bits: **n MUXes of k × 1**, log₂k select lines; or tri-state buffers + log₂k × k decoder.
- Arithmetic circuit (S1 S0 Cin): 000 A+B, 001 A+B+1, 010 A+B′, 011 A−B, 100 A, 101 A+1, 110 A−1, 111 A.
- Logic: selective set A ∨ B; selective complement A ⊕ B; selective clear A ∧ B′; mask A ∧ B (0s clear); insert = mask then OR; clear = A ⊕ A.
- Shifts: logical (0 in), circular, arithmetic (ashr keeps sign; ashl overflow V = Rn−1 ⊕ Rn−2).
- **ALSU (Mano Table 4-8):**

| S3S2 | S1S0 | Cin=0 | Cin=1 |
|---|---|---|---|
| 00 | 00 | F = A | F = A + 1 |
| 00 | 01 | A + B | A + B + 1 |
| 00 | 10 | A + B′ | A + B′ + 1 (A − B) |
| 00 | 11 | A − 1 | F = A |
| 01 | 00 / 01 / 10 / 11 | AND / OR / XOR / A′ | |
| 10 | xx | shr A | |
| 11 | xx | shl A | |
14 operations. One stage: arithmetic circuit + logic circuit + shr/shl inputs → 4×1 MUX selected by S3S2.

### 8.2 U2 · Basic computer (Mano ch. 5)
Registers: DR 16, AR 12, AC 16, IR 16, PC 12, TR 16, INPR 8, OUTR 8. Memory 4096 × 16. Bus codes: 1 AR, 2 PC, 3 DR, 4 AC, 5 IR, 6 TR, 7 memory. Formats: MRI `I | opcode(3) | address(12)`; register-ref 7xxx; I/O Fxxx.

| MRI | I=0 | I=1 | Execute (from T4) |
|---|---|---|---|
| AND | 0xxx | 8xxx | D0T4: DR ← M[AR]; D0T5: AC ← AC ∧ DR, SC ← 0 |
| ADD | 1xxx | 9xxx | D1T4: DR ← M[AR]; D1T5: AC ← AC + DR, E ← Cout, SC ← 0 |
| LDA | 2xxx | Axxx | D2T4: DR ← M[AR]; D2T5: AC ← DR, SC ← 0 |
| STA | 3xxx | Bxxx | D3T4: M[AR] ← AC, SC ← 0 |
| BUN | 4xxx | Cxxx | D4T4: PC ← AR, SC ← 0 |
| BSA | 5xxx | Dxxx | D5T4: M[AR] ← PC, AR ← AR + 1; D5T5: PC ← AR, SC ← 0 |
| ISZ | 6xxx | Exxx | D6T4: DR ← M[AR]; D6T5: DR ← DR + 1; D6T6: M[AR] ← DR, if DR = 0 then PC ← PC + 1, SC ← 0 |

Register-ref: 7800 CLA, 7400 CLE, 7200 CMA, 7100 CME, 7080 CIR, 7040 CIL, 7020 INC, 7010 SPA, 7008 SNA, 7004 SZA, 7002 SZE, 7001 HLT. I/O: F800 INP, F400 OUT, F200 SKI, F100 SKO, F080 ION, F040 IOF.
Cycle: R′T0: AR ← PC · R′T1: IR ← M[AR], PC ← PC + 1 · R′T2: D0–D7 ← decode IR(12–14), AR ← IR(0–11), I ← IR(15) · D7′IT3: AR ← M[AR] (indirect) · D7′I′T3: nothing.
Interrupt: R ← 1 when T0′T1′T2′·IEN·(FGI + FGO); RT0: AR ← 0, TR ← PC; RT1: M[AR] ← TR, PC ← 0; RT2: PC ← PC + 1, IEN ← 0, R ← 0, SC ← 0.
Control gates: LD(AR) = R′T0 + R′T2 + D7′IT3; CLR(AR) = RT0; INR(AR) = D5T4. Memory write = D3T4 + D5T4 + D6T6 + RT1. Set E to 1: CLE then CME.

### 8.3 U3 · Control unit (Mano ch. 7, ch. 8 status bits)
| Hardwired | Microprogrammed |
|---|---|
| logic gates, decoders, flip-flops | control words in control memory (ROM) |
| fast | slower (memory access per step) |
| hard to change | change by rewriting the microprogram |
| RISC | CISC |
- Control memory, CAR (control address register), CDR (control data register, pipeline register), sequencer (next-address: increment, branch, mapping, subroutine call/return).
- Microinstruction (Mano §7-3): F1 F2 F3 (3 bits each) | CD 2 | BR 2 | AD 7 = **20 bits**. Mapping: opcode xxxx → address **0 xxxx 00** (0010 → 08H, 1011 → 2CH, 1111 → 3CH).
- Field of n bits → 2ⁿ microoperations (or 2ⁿ − 1 + no-op).
- Mano 7-4: with CDR clock = 1/100 ns = **10 MHz**; without CDR 1/130 ns = **7.69 MHz**.
- Status bits: C carry, S sign, Z zero, V overflow (V = C8 ⊕ C7). Unsigned compare uses C, Z; signed uses S ⊕ V, Z.

### 8.4 U4 · Parallel processing and pipelining (Mano ch. 9)
$$S = \frac{n\,t_n}{(k+n-1)\,t_p} \qquad S_{max} = \frac{t_n}{t_p} = k \text{ (if } t_n = k\,t_p) \qquad \text{cycles} = k + n - 1$$
- Flynn: SISD (uniprocessor), SIMD (array/vector), MISD (theoretical), MIMD (multiprocessor).
- Instruction pipeline (4 segments): FI fetch, DA decode + effective address, FO fetch operand, EX execute.
- Arithmetic pipeline (floating add, 4 segments): compare exponents → align mantissas → add/subtract → normalize.
- RISC 3-segment pipeline: I (fetch), A (ALU), E (execute/store); delayed load, delayed branch.
- Hazards and fixes: §2 C1 table.

### 8.5 U5 · Input–output (Mano ch. 11)
- Bus organizations: separate buses (IOP) · common bus, separate control lines (**isolated I/O**) · common bus and control (**memory-mapped I/O**).
- Synchronous (common clock) vs asynchronous (control signals). Strobe (one line, source- or destination-initiated) vs handshake (two lines; reliable, timeout possible).
- Modes of transfer: **programmed I/O** (CPU polls flag) · **interrupt-initiated** (device interrupts when ready) · **DMA** (controller takes the bus with BR/BG; CPU idle on the bus). (IOP as a further step.)
- DMA: CPU loads start address, word count, direction; **burst** (whole block) vs **cycle stealing** (one word per bus grant). 8086: HOLD/HLDA.
- Priority interrupt: **daisy chain** (serial, position = priority, few wires) vs **parallel** (interrupt register + mask + priority encoder → vector address). Fast devices (disk) high priority.
- IOP: separate processor with its own I/O program; CPU starts it, IOP interrupts when done.

### 8.6 U6 · Memory (Mano ch. 12)
- Hierarchy: registers → cache → main → magnetic disk → tape (faster/costlier up). CPU directly accesses cache and main memory only.
- SRAM (flip-flops, no refresh, fast, cache) vs DRAM (capacitor, refresh, dense, cheap, main memory). ROM holds the bootstrap loader.
- Mano RAM chip 128 × 8 (7 address lines, CS1 = 1, CS2̅ = 0, RD, WR); ROM 512 × 8 (9 lines). Low address lines select inside a chip; high lines select the chip.
- Associative memory (CAM): argument A, key K (mask), match M; search by content in parallel; costly.
- Locality: temporal (cache it) and spatial (fetch blocks). Hit ratio h; t_avg as §2 A4.
- Mapping (Mano: main 32K × 12 → 15-bit address; cache 512 × 12): **direct** tag 6 + index 9 (blocks of 8: tag 6, block 6, word 3) · **associative** stores 15-bit address + data · **set-associative** (2-way: cache word = 2 × (6 + 12) = 36 bits).
- General split: offset = log₂(block bytes), index = log₂(sets), tag = address − index − offset; sets = blocks / ways.
- Replacement: direct — none; associative/set — FIFO, LRU, random. Write: **write-through** (cache + memory) vs **write-back** (cache only, dirty bit).
- Virtual memory: address space > memory space; page table; page = fixed size; 13-bit address with 1K pages → page 3 bits + line 10 bits. Segments: variable, logical.

### 8.7 8086 (Bhurchandi & Ray)
| Item | Value |
|---|---|
| Data bus / address bus | 16-bit / 20-bit → 1 MB; I/O 64 KB |
| Package / technology / transistors | 40-pin DIP, HMOS, ≈ 29,000 |
| Clock | 5 MHz (8086), 8 MHz (8086-2), 10 MHz (8086-1); 33 % duty |
| Queue | 6 bytes (8088: 4) |
| Registers | 14 × 16-bit: AX BX CX DX, SP BP SI DI, IP, CS DS SS ES, flags |
| Reset | CS = FFFFH, IP = 0000H → first fetch at FFFF0H; held high ≥ 4 clocks |

- **BIU**: segment registers, IP, address adder, 6-byte queue, bus control — fetches, reads/writes, computes PA. **EU**: ALU, general/pointer/index registers, flags, decoder, control — decodes and executes; no bus connection. Overlap = pipelining.
- Registers: AX accumulator (MUL/DIV, I/O), BX base (pointer), CX count (LOOP, string, CL = shift count), DX data (MUL/DIV high word, I/O port address), SP stack top, BP stack-frame base, SI source index, DI destination index.
- **Flags** (16-bit, 9 used: 6 status + 3 control): bit 0 CF, 2 PF (even 1s in low byte), 4 AF (carry from bit 3), 6 ZF, 7 SF (= MSB), 8 TF (single step), 9 IF (INTR enable), 10 DF (string direction), 11 OF (signed overflow).
- **Segmentation:** 16 segments of 64 KB, starting on 16-byte boundaries; may overlap. **PA = segment × 10H + offset** (2010H : 3535H → 23635H). Max active at once: 4 × 64 KB = 256 KB.

| Reference | Default | Override |
|---|---|---|
| instruction fetch | CS : IP | none |
| stack | SS : SP | none |
| data | DS : EA | CS, ES, SS |
| BP as pointer | SS | CS, DS, ES |
| string source | DS : SI | CS, ES, SS |
| string destination | ES : DI | none |

- **Addressing modes** (EA = offset, PA = seg × 10H + EA):

| Mode | Example | EA |
|---|---|---|
| immediate | MOV AL, 50H | operand in instruction |
| register | MOV CX, BX | — |
| direct | MOV CX, [1234H] | 1234H |
| register indirect | MOV AX, [BX] | BX / SI / DI |
| based (register relative) | MOV AX, [BX+08H] | BX/BP + disp |
| indexed | MOV AX, [SI+0A2H] | SI/DI + disp (8-bit disp sign-extended: A2H → FFA2H) |
| based indexed | MOV AX, [BX][SI] | BX/BP + SI/DI |
| based indexed + disp | MOV AH, [BX][SI]+1234H | BX/BP + SI/DI + disp |
| string | MOVSB | DS:SI → ES:DI, ±1 by DF |
| I/O direct / indirect | IN AL, 09H / OUT DX, AX | 8-bit port / port in DX |
| relative | JZ 0AH | IP + disp |
| implied | CLC | — |
Control-transfer modes: intrasegment direct (`JMP SHORT/NEAR label`, IP ± disp) and indirect (`JMP [BX]`); intersegment direct (`JMP 5000H:2000H`) and indirect (`JMP DWORD PTR [2000H]`: IP then CS from memory).
Illegal: memory-to-memory MOV; immediate into a segment register; [BX+BP], [SI+DI].

- **Instruction groups:** data transfer (MOV PUSH POP XCHG IN OUT LEA LDS LES XLAT LAHF SAHF PUSHF POPF) · arithmetic (ADD ADC INC AAA DAA · SUB SBB DEC NEG CMP AAS DAS · MUL IMUL AAM · DIV IDIV AAD CBW CWD) · logical (AND OR XOR NOT TEST) · shift/rotate (SHL/SAL SHR SAR ROL ROR RCL RCR) · string (MOVS CMPS SCAS LODS STOS + REP REPE REPNE) · program transfer (JMP CALL RET, Jcc, LOOP LOOPE LOOPNE JCXZ, INT IRET) · flag control (CLC STC CMC CLD STD CLI STI) · machine control (HLT NOP WAIT LOCK ESC).
- Addition flags: ADD/ADC all 6; INC all except CF; AAA AF CF; DAA SF ZF AF PF CF. Logical: CF = OF = 0. Unsigned jumps JA/JB (CF, ZF); signed JG/JL (SF, OF, ZF).
- **Directives** (no machine code): DB DW DD DQ DT, DUP, EQU, ORG, ASSUME, SEGMENT/ENDS, PROC/ENDP (NEAR/FAR), END, EVEN, MACRO/ENDM, PTR, OFFSET, SHORT, PUBLIC/EXTRN. Assembler: mnemonics → machine code; label | mnemonic operands | ;comment.
- **Pins** (common): AD15–AD0 (address in T1 when ALE = 1, then data), A19/S6–A16/S3 (S4S3 = segment in use, S5 = IF, S6 = 0), BHE̅/S7, RD̅, READY (0 → wait states), INTR (level, maskable by IF), NMI (positive edge, type 2, not maskable), TEST̅ (WAIT instruction; 8087 BUSY), RESET, MN/MX̅ (+5 V min, GND max), CLK, Vcc +5 V ± 10 %, 2 GND.
- **Min mode** (pins 24–31): INTA̅, ALE, DEN̅, DT/R̅, M/IO̅, WR̅, HLDA, HOLD. **Max mode**: QS1 QS0 (queue status), S̄2 S̄1 S̄0 (bus cycle, decoded by 8288), LOCK̅, RQ̅/GT̅1, RQ̅/GT̅0. S̄2S̄1S̄0: 000 INTA, 001 I/O read, 010 I/O write, 011 halt, 100 code, 101 memory read, 110 memory write, 111 passive.
- Microprocessor generations (deck): 1st 1971–73 PMOS, 4004 (4-bit), 8008; 2nd 1974–78 NMOS 8-bit, 8085, Z80, 6800; 3rd 1978 HMOS 16-bit, 8086, Z8000, multiply/divide; 4th 1980s HCMOS 32-bit, 80386; 5th Pentium, superscalar, 64-bit. Microprocessor (CPU only, external memory/I/O) vs microcontroller (CPU + memory + I/O ports on one chip, control applications).
- Procedure: CALL pushes IP (near) or CS, IP (far); RET pops; saves memory, costs call/return time. Macro: body copied at each use, no CALL overhead, larger code.

### 8.8 RISC-V (Patterson & Hennessy; ratified spec)
- Open, royalty-free ISA from UC Berkeley; small base + optional extensions; base frozen, new instructions added as extensions.
- Names: RV32I (32-bit integer base), RV64I, RV32E (16 registers); M multiply/divide, A atomic, F single float, D double float, C compressed 16-bit, G = IMAFD.
- 32 registers x0–x31 (x0 hardwired 0), XLEN = 32 in RV32I, plus pc. ABI: x1 ra, x2 sp, x10–x17 a0–a7.
- Fixed 32-bit, 4-byte-aligned instructions; formats **R, I, S, U** + variants **B, J** (six); rs1, rs2, rd at the same positions in every format (decode in parallel).
- Load/store architecture; one addressing mode (base + 12-bit displacement); no condition flags (BEQ rs1, rs2 compares directly); hardwired control; built for pipelining.
- x0 uses: `ADDI x5, x0, 42` load constant · `ADD x6, x5, x0` move · `ADDI x0, x0, 0` NOP.

| | 8086 (CISC) | RISC-V (RISC) |
|---|---|---|
| Instruction length | 1–6 bytes | 32 bits fixed |
| Registers | 14, special-purpose | 32, general |
| Memory operands | most instructions | load/store only |
| Addressing modes | ~12 | 1 |
| Flags | 9-flag register | none |
| Memory | segmented | flat |
| Control | microprogrammed | hardwired |
| Licence | proprietary | open |
