# 10 — Mock Paper · 30 marks · 90 minutes

Built only from question forms the professor used in Assignments 1 and 2 — all numbers new.
**Layout assumed** from the sibling MUJ MTE (Digital Electronics, Sep 2025: 3 × 2 + 4 × 4 + 1 × 8);
ECE2108's own MTE layout is unknown. U3 (microprogrammed control) is excluded here because neither
assignment tested it — it is still in MTE scope; drill it from v1 file 07.

Closed book. Timer on. No scrolling past the line until time is up.

---

## Section A — 3 × 2 = 6 marks

**A1.** Define *microarchitecture*. Give one architecture with two different microarchitectures.

**A2.** Represent −37 in 8-bit signed-magnitude, 1's complement and 2's complement.

**A3.** A Basic Computer memory word holds `9A3F`. Which instruction is it, and what does it do?

## Section B — 4 × 4 = 16 marks

**B1.** Three 8-bit registers share a bus built from tri-state buffers. How many buffers and what
decoder are needed? Draw one bus line and explain what happens when the decoder's enable is 0.

**B2.** A 4-bit ALSU (professor's function table) has A = 1100, B = 1010. Give the select code and F for
**(i)** subtraction **(ii)** OR. Interpret (i).

**B3.** Basic Computer: PC = 0A0, AC = 0F0F, E = 0, M[0A0] = 1123, M[123] = F0F0. Give AC, E, PC, AR,
DR, IR after the next instruction executes.

**B4.** A flip-flop F obeys `aT₂: F ← 0`, `bT₄: F ← F′`, `cT₁: F ← G`, otherwise unchanged. Give J and K
for a JK implementation and list the gates.

## Section C — 1 × 8 = 8 marks

**C1.** A 4-segment pipeline has combinational delays 35, 50, 60 and 45 ns; each interface register
adds 5 ns.
(a) Clock period tₚ. (b) Non-pipelined time per task tₙ (one register remains).
(c) Speedup for 20 tasks and for 200 tasks. (d) Maximum speedup — and why it is not 4.
(e) Clock cycles to finish 200 tasks.

---
---

## Answers

**A1.** Microarchitecture = computer organization: the hardware implementation (datapath, control,
pipelining, caches) of an instruction set architecture. Example: x86 — the Intel 8086 and a modern
Core i9 run the same instruction set on entirely different microarchitectures.

**A2.** +37 = 0010 0101.

| SM | 1's | 2's |
|---|---|---|
| 1010 0101 | 1101 1010 | 1101 1011 |

**A3.** 9A3F = **1**001 1010 0011 1111 → I = 1, opcode 001 = **ADD**, address A3F.
**ADD I A3F**: EA = M[A3F]; AC ← AC + M[EA], E ← carry out.

**B1.** 3 × 8 = **24 tri-state buffers**; a **2-to-4 decoder** with enable (one output unused).

```
   R1₀ ──▷──┐
   R2₀ ──▷──┼════ bus line 0       each ▷ enabled by its register's decoder output
   R3₀ ──▷──┘
```

The decoder raises one output, enabling that register's 8 buffers; the other 16 are high impedance.
**Enable = 0:** all decoder outputs 0 → all 24 buffers high impedance → no register drives the bus;
the lines float.

**B2.**
```
 (i)  subtraction  S₃S₂S₁S₀Cᵢₙ = 0 0 1 0 1
      F = A + B′ + 1 = 1100 + 0101 + 1 = 1 0010  →  F = 0010, Cₒᵤₜ = 1
      Unsigned 12 − 10 = 2 ✓; Cₒᵤₜ = 1 → A ≥ B.

 (ii) OR  S₃S₂S₁S₀ = 0 1 0 1, Cᵢₙ = ×
      F = 1100 ∨ 1010 = 1110
```

**B3.** 1123 = I 0, opcode 001 → **ADD 123** (direct).
```
   T₀ AR ← 0A0 · T₁ IR ← 1123, PC ← 0A1 · T₂ AR ← 123
   T₄ DR ← M[123] = F0F0
   T₅ AC ← 0F0F + F0F0 = FFFF, E ← 0 (no carry out)
```

| AC | E | PC | AR | DR | IR |
|---|---|---|---|---|---|
| FFFF | 0 | 0A1 | 123 | F0F0 | 1123 |

**B4.**
```
   J = bT₄ + cT₁·G
   K = aT₂ + bT₄ + cT₁·G′
```
Gates: AND(a, T₂) · AND(b, T₄) shared by both ORs · AND(c, T₁) shared · NOT G · AND(cT₁, G) ·
AND(cT₁, G′) · 2-input OR → J · 3-input OR → K.
Check: bT₄ alone → J = K = 1 → complement ✓; cT₁ with G = 0 → J = 0, K = 1 → F = 0 = G ✓.

**C1.**
```
   (a) tₚ = max(35, 50, 60, 45) + 5 = 65 ns
   (b) tₙ = 35 + 50 + 60 + 45 + 5 = 195 ns
   (c) S₂₀  = 20 × 195 / ((4 + 19) × 65)  = 3900 / 1495   = 2.61
       S₂₀₀ = 200 × 195 / ((4 + 199) × 65) = 39000 / 13195 = 2.96
   (d) Sₘₐₓ = tₙ / tₚ = 195 / 65 = 3.0
       Not 4: the segments are unequal. The clock must fit the 60 ns segment, so the 35, 50 and 45 ns
       segments idle part of every cycle; tₙ = 195 < k·tₚ = 260.
   (e) 4 + 200 − 1 = 203 cycles
```

---

## Scoring

| Score | Next step |
|---|---|
| 26–30 | Redo only the items you lost, tomorrow |
| 18–25 | Redo the matching file's Self-test for each lost item today; this paper again in 2 days |
| < 18 | Work files 05, 07, 08, 09 Attempt sections again before retaking |
