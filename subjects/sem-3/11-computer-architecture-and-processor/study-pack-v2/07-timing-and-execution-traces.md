# 07 — Timing Signals and Instruction-Execution Traces

**Assignment 2: Q5, Q6, Q7, Q8 · 40 of 150 marks · U2 (L10–L11)**
Source problems: Mano Fig. 5-7 (timing), 5-9, 5-12, 5-16.

A2 answer policy: method + fully worked twin here; A2's own key after 16-09-2026 16:30.

---

## Map

```
   4-bit SC ──► 4×16 decoder ──► T₀ T₁ T₂ …        IR(12-14) ──► 3×8 decoder ──► D₀ … D₇
                     │                                                │
                     └────────────── control function  Dⱼ·Tₖ ─────────┘
                                          │
                                          ▼
   Fetch  T₀ AR ← PC · T₁ IR ← M[AR], PC ← PC+1 · T₂ decode, AR ← IR(0-11), I ← IR(15)
                                          │
                     T₃  ┌── D₇′I  : AR ← M[AR]   (indirect)
                         ├── D₇′I′ : nothing     (direct)
                         ├── D₇I′  : register-reference, SC ← 0
                         └── D₇I   : I/O,               SC ← 0
                                          │
                     T₄… memory-reference execution, ends with SC ← 0
```

---

## Attempt

**A2 Q5.** In the basic computer, with a timing diagram, explain the microoperation `C₇T₃: SC ← 0`.

**A2 Q6.** AC = A937 (hex), E = 1. Give AC, E, PC, AR, IR in hex after executing **CLA**.

**A2 Q7.** PC = 3AF, AC = 7EC3, M[3AF] = 932E, M[32E] = 09AC, M[9AC] = 8B9F.
(a) What instruction is fetched and executed next? (b) Show the binary operation performed on AC.

**A2 Q8.** Memory 65,536 words × 8 bits. Registers PC, AR, TR (16 bits); AC, DR, IR (8 bits). An MRI
is three words: an 8-bit opcode, then a 16-bit address in the next two words. Operands are 8 bits; no
indirect bit. List the microoperations to fetch an MRI and place its operand in DR, starting at T₀.

---

## Learn

### Timing signals and SC

- SC is a 4-bit counter; its outputs drive a 4×16 decoder producing **T₀ … T₁₅**, one active per clock
  cycle.
- SC has **INR** (count every clock) and **CLR**. When a control function clears SC, the **next**
  clock edge makes SC = 0, so the following cycle is **T₀** — the next fetch.
- **`SC ← 0` ends an instruction.** Every execution path ends with it.

**About A2 Q5's `C₇T₃`:** no signal named C₇ exists in the Basic Computer. The nearest is **D₇T₃**
(opcode 111 at T₃ — register-reference and I/O instructions finish at T₃ and clear SC). State that
reading as your assumption. The textbook's own example of this diagram is `D₃T₄: SC ← 0` (STA),
worked below — the method is identical.

### Tracing an instruction — procedure

1. **Fetch:** AR ← PC; IR ← M[AR]; PC ← PC + 1.
2. **Decode** IR: I = bit 15, opcode = bits 14–12, AR ← bits 11–0.
3. If MRI and I = 1: AR ← M[AR].
4. **Execute** by the table below.
5. Report registers at the **end** of the instruction.

| Instruction | Execute microoperations |
|---|---|
| AND | T₄ DR ← M[AR] · T₅ AC ← AC ∧ DR, SC ← 0 |
| ADD | T₄ DR ← M[AR] · T₅ AC ← AC + DR, E ← Cₒᵤₜ, SC ← 0 |
| LDA | T₄ DR ← M[AR] · T₅ AC ← DR, SC ← 0 |
| STA | T₄ M[AR] ← AC, SC ← 0 |
| BUN | T₄ PC ← AR, SC ← 0 |
| BSA | T₄ M[AR] ← PC, AR ← AR + 1 · T₅ PC ← AR, SC ← 0 |
| ISZ | T₄ DR ← M[AR] · T₅ DR ← DR + 1 · T₆ M[AR] ← DR, if DR = 0 then PC ← PC + 1, SC ← 0 |

**Register-reference instructions** (r = D₇I′T₃, Bᵢ = IR(i)): at T₃, execute and SC ← 0. AR still
holds IR(0–11) from T₂, PC already incremented at T₁, DR untouched.

| | | |
|---|---|---|
| CLA rB₁₁: AC ← 0 | CLE rB₁₀: E ← 0 | CMA rB₉: AC ← AC′ |
| CME rB₈: E ← E′ | CIR rB₇: AC ← shr AC, AC(15) ← E, E ← AC(0) | CIL rB₆: AC ← shl AC, AC(0) ← E, E ← AC(15) |
| INC rB₅: AC ← AC + 1 | SPA rB₄: if AC(15) = 0, PC ← PC + 1 | SNA rB₃: if AC(15) = 1, PC ← PC + 1 |
| SZA rB₂: if AC = 0, PC ← PC + 1 | SZE rB₁: if E = 0, PC ← PC + 1 | HLT rB₀: S ← 0 |

### Designing a fetch for a different machine

Rules that constrain every step:

- **Memory is addressed only through AR.** To read the word at PC, first `AR ← PC`.
- **One bus source per clock.** Two different values cannot travel in one step.
- A multi-word instruction increments PC once per word read.
- Assemble a multi-word address in **TR** (a spare register as wide as the address), then `AR ← TR`.
- State the byte order you assume (which address word comes first).

---

## Worked twins

**Twin of Q5 — the textbook case `D₃T₄: SC ← 0`.**

```
   Clock   ┐_┌┐_┌┐_┌┐_┌┐_┌┐_┌┐_┌─
   SC      │ 0 │ 1 │ 2 │ 3 │ 4 │ 0 │
   T₀      ‾‾‾‾‾____________________‾‾‾‾
   T₁      ____‾‾‾‾_____________________
   T₂      ________‾‾‾‾_________________
   T₃      ____________‾‾‾‾_____________
   T₄      ________________‾‾‾‾_________
   D₃      __________‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾__     (decoded from IR after T₂'s edge)
   CLR SC  ________________‾‾‾‾_________     = D₃·T₄
                               ↑
                     this edge clears SC → next cycle is T₀
```

**Explanation:** SC increments every clock, stepping T₀→T₄. The opcode is decoded during T₂, so D₃ is
active from T₃. During T₄ the AND gate D₃·T₄ = 1 drives CLR(SC). At the positive edge that ends T₄,
SC becomes 0 instead of 5, so T₀ follows and the next instruction's fetch begins. STA needed only T₄ to
execute (`M[AR] ← AC`), so its instruction cycle is 5 clock cycles long.

**Twin of Q6.** AC = A937, E = 1, PC = 021 before the fetch. Execute **CMA**, then separately **CIR**.
(A2 Q6 gives no PC — "missing data may be assumed suitably"; state an assumed PC the same way.)

```
   fetch  T₀ AR ← 021 · T₁ IR ← M[021], PC ← 022 · T₂ AR ← IR(0-11)

   CMA (7200):  AC ← AC′
      A937 = 1010 1001 0011 0111
      AC′  = 0101 0110 1100 1000 = 56C8

   CIR (7080):  shift AC right, E into AC(15), AC(0) into E
      E AC  = 1 | 1010 1001 0011 0111
      new E = AC(0) = 1
      new AC = 1101 0100 1001 1011 = D49B
```

| After | AC | E | PC | AR | IR |
|---|---|---|---|---|---|
| CMA | 56C8 | 1 | 022 | 200 | 7200 |
| CIR | D49B | 1 | 022 | 080 | 7080 |

AR = the low 12 bits of IR, loaded at T₂.

**Twin of Q7.** PC = 200, AC = 7EC3, M[200] = 8150, M[150] = 0300, M[300] = F0F0.

```
   T₀   AR ← PC           AR = 200
   T₁   IR ← M[200]       IR = 8150,  PC = 201
   T₂   decode            8150 = 1000 0001 0101 0000
                          I = 1, opcode 000 = AND, AR = 150
   T₃   indirect          AR ← M[150] = 300
   T₄   DR ← M[300]       DR = F0F0
   T₅   AC ← AC ∧ DR, SC ← 0
```

(a) **AND I 150** — AND the word whose address is stored at 150 into AC.
(b)
```
   AC   0111 1110 1100 0011    7EC3
   DR ∧ 1111 0000 1111 0000    F0F0
        ───────────────────
   AC   0111 0000 1100 0000    70C0
```
Final: AC = 70C0, PC = 201, AR = 300, DR = F0F0, IR = 8150, E unchanged.

For an **ADD** trace, also report **E = the carry out of bit 15**: e.g. 7EC3 + 9ABC = 1 197F → AC =
197F, E = 1.

**Twin of Q8.** Memory 4096 × 8 bits. PC, AR, TR are 12 bits; AC, DR, IR are 8. An MRI is two words:
word 1 = 4-bit opcode + the **high 4** address bits; word 2 = the low 8 address bits. Fetch, then
operand into DR.

```
   T₀:  AR ← PC                                 address of word 1
   T₁:  IR ← M[AR],  PC ← PC + 1                word 1 into IR
   T₂:  AR ← PC                                 address of word 2
   T₃:  TR(7-0) ← M[AR],  TR(11-8) ← IR(3-0),   assemble the 12-bit address
        PC ← PC + 1
   T₄:  AR ← TR                                 effective address
   T₅:  DR ← M[AR]                              operand into DR
```

Check each step against the rules: memory read only via AR ✓ · one bus value per step (T₃'s IR(3-0)
travels on a separate path, or the step is split in two — state which) ✓ · PC incremented once per
word ✓.

---

## Traps

| Trap | Correction |
|---|---|
| PC after an instruction = its own address | PC is incremented at T₁ — it already points to the next instruction |
| AR = "unchanged" after an RRI | T₂ loaded AR ← IR(0-11), e.g. 800 for CLA |
| CLA also clears E | CLA clears AC only. CLE clears E |
| Indirect: using 09AC-style word as the operand | I = 1: that word is the **address**; read memory again |
| ADD: forgetting E | E ← carry out of AC's bit 15 |
| Fetch design: `IR ← M[PC]` | Memory is addressed through AR only |
| Missing PC in a trace question | Assume one, **state it**, carry it through |

---

## Self-test

1. Draw the timing for `D₁T₅: SC ← 0` (ADD). How many clock cycles is ADD, direct?
2. AC = A937, E = 1, PC = 021: after **CIL**?
3. AC = 00FF, PC = 100, M[100] = 7010. Which instruction, and what is PC afterwards?
4. PC = 050, AC = 1234, M[050] = 1060, M[060] = EDCC. Instruction, final AC and E?
5. In twin Q8, why can't T₂ and T₃ be merged into one step?

---
---

## Answers

**A2 Q5–Q8:** answer key added after 16-09-2026, 16:30. Send your answers for marking.

**Self-test 1.** Same diagram with D₁ and CLR(SC) = D₁·T₅ during T₅. ADD direct: T₀–T₅ = **6 clock
cycles**.

**Self-test 2.** CIL: new E = AC(15) = 1; AC = shl A937 with E into bit 0:
1010 1001 0011 0111 → 0101 0010 0110 111**1** = **526F**, E = 1. PC = 022, AR = 040, IR = 7040.

**Self-test 3.** 7010 = **SPA**. AC(15) = 0 (00FF is positive) → skip: PC goes 100 → 101 (fetch) →
**102**.

**Self-test 4.** 1060 = I 0, opcode 001 → **ADD 060** (direct). 1234 + EDCC = 1 0000 → AC = **0000**,
E = **1**.

**Self-test 5.** At T₂ AR must first receive PC; memory is read from AR's **new** value only after
that edge. Reading M[AR] in the same step would read the old address.
