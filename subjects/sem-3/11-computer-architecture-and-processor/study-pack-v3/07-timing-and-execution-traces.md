# 07 — Timing and execution traces

**Assignment 2: Q5–Q8 · 40 of 150 marks · U2 (L10–L11) · needs 00, 06**

★ **Highest marks per hour in the pack.** Four assignment questions, all of them the same skill:
follow the machine one clock step at a time and write down what every register holds. Once the
timing table is in your head, all four are mechanical.

This file also finally answers the question file 00 opened with.

---

## Map

```
   [1] The control unit ──► T₀ T₁ T₂ … the timing signals
        SC + 2 decoders           │
                                  ▼
   [2] Fetch & decode  T₀ T₁ T₂
                                  │
                                  ▼
   [3] Which type?  T₃ ──┬──► [4] Register-reference   (A2 Q6)
                         │
                         ├──► [5] The 7 MRI sequences  T₄ onward
                         │         │
                         │         └──► [6] BSA and ISZ
                         │
                         └──► I/O  ──► [9] The interrupt cycle
                                  │
                                  ▼
                      [7] A full indirect trace   (A2 Q7)
                      [8] A different machine     (A2 Q8)
```

---

## The questions this file answers

| # | Question | Marks | Mano |
|---|---|---|---|
| 1 | `[A2 Q5]` With a timing diagram, explain the working of the microoperation `C₇T₃: SC ← 0`. | 10 | **5-8** |
| 2 | `[A2 Q6]` AC = A937, E = 1. Determine AC, E, PC, AR, IR after executing CLA. | 10 | **5-9** |
| 3 | `[A2 Q7]` PC = 3AF, AC = 7EC3, M[3AF] = 932E, M[32E] = 09AC, M[9AC] = 8B9F. What is fetched and executed next? Show the AC operation. | 10 | **5-12** |
| 4 | `[A2 Q8]` A 65,536 × 8 machine with three-word instructions. List the microoperations to fetch an MRI and place the operand in DR, from T₀. | 10 | **5-16** |

Unasked Mano follow-ups: **5-10, 5-11, 5-13, 5-14, 5-15, 5-17, 5-18.** 5-10 and 5-11 are the
direct-MRI and ISZ-indirect twins of Q7 — do them.

---

## Build

### 1 · The control unit and the timing signals

> **Q** `[A2 Q5 · 10 marks]` **= Mano 5-8**
> **In the context of a basic computer, with the help of a timing diagram explain the working of the
> microoperation: `C₇T₃: SC ← 0`.**
> *Mano's fuller wording: "Draw a timing diagram similar to Fig. 5-7 assuming that SC is cleared to 0
> at time T₃ if control signal C₇ is active. C₇ is activated with the positive clock transition
> associated with T₃."*
>
> *File 00, step 7 told you T-subscripts count clock steps. Guess what hardware produces them, and
> what clearing it accomplishes. Then read on.*

**The hardwired control unit is four things:**

```
   IR(12-14) ──► 3×8 decoder ──► D₀ … D₇        which opcode
   IR(15)    ──► the I flip-flop                direct or indirect
   IR(0-11)  ──► straight to the gates as B₀…B₁₁   (one-hot, no decoder — file 06)
   SC (4-bit counter) ──► 4×16 decoder ──► T₀ … T₁₅   which time step
                │
             increments on every positive clock transition
```

**SC increments on every clock**, so the decoder lights T₀, then T₁, then T₂, … in turn — exactly one
active at a time. **Clearing SC forces the next step back to T₀**, which is how an instruction ends
and the next fetch begins.

★ **Every control signal in this machine is a sum of products of Ds and Ts** (plus I, R and the Bᵢ).
"What does the computer do next?" has a literal answer: whatever gates the current D·T combination
enables.

**The timing diagram:**

```
              ↑     ↑     ↑     ↑     ↑     ↑
  clock     __|‾|___|‾|___|‾|___|‾|___|‾|___|‾|__

  T₀        ‾‾‾‾‾‾‾|_____________________|‾‾‾‾‾‾‾
  T₁        _______|‾‾‾‾‾|_________________________
  T₂        _____________|‾‾‾‾‾|___________________
  T₃        ___________________|‾‾‾‾‾|_____________
  C₇        ___________________|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

  SC          0  │  1  │  2  │  3  │  0  │  1
                                    ▲
                             CLR SC takes effect here
                             → T₄ NEVER OCCURS; T₀ follows T₃
```

**Explaining it — this is the 10 marks:**

1. SC counts up on each positive clock transition; its 4×16 decoder turns the count into exactly one
   active timing signal T₀, T₁, T₂, …
2. `C₇T₃` is a **control function** (file 03, step 2): it is 1 only when control signal C₇ is active
   **and** the machine is in timing step T₃ — the AND of the two.
3. When that function is 1, the **CLR input of SC** is asserted. The clear takes effect at the **next
   positive clock transition** — the same edge that would otherwise have advanced SC from 3 to 4.
4. So SC goes **3 → 0** instead of 3 → 4. **T₄ never becomes active**; T₀ follows T₃ directly, and the
   machine begins the next fetch.
5. C₇ is itself activated by the positive clock transition associated with T₃, so it is stable for
   the whole of T₃ and the AND is clean — no glitch, no partial clear.

**The general form:** `SC ← 0` is the **last microoperation of every instruction**. Which D·T it sits
on is what determines how long that instruction takes. `D₃T₄: SC ← 0` ends STA after five steps;
`D₆T₆: SC ← 0` ends ISZ after seven.

> ✓ **Check 1.** (a) What produces T₀…T₁₅ from SC? (b) Why does T₄ not occur when `C₇T₃` is active?
> (c) An instruction ends with `SC ← 0` on `D₂T₅`. How many timing steps did it take, counting T₀?

---

### 2 · Fetch and decode

> **Q** *(the foundation for Q6, Q7 and Q8 — memorise this, it is three lines)*
> **Write the fetch and decode microoperations of the Basic Computer, with timing.**
>
> *Guess where PC gets incremented, and why it is that early rather than at the end.*

```
T₀:  AR ← PC                                    S₂S₁S₀ = 010, LD(AR)
T₁:  IR ← M[AR],  PC ← PC + 1                   S₂S₁S₀ = 111, read, LD(IR), INR(PC)
T₂:  D₀…D₇ ← decode IR(12-14),  AR ← IR(0-11),  I ← IR(15)
```

**Why PC increments at T₁ and not later** — a favourite "explain" mark. The address has already been
safely copied into AR at T₀, so PC is free. Incrementing it early means PC **already points at the
next instruction** by the time a branch might overwrite it, which is exactly what makes BSA's
"save the return address" work (step 6).

Note that **AR ← IR(0-11) happens at T₂ unconditionally**, for every instruction type. That is why
register-reference instructions leave a junk-looking value in AR (step 4) — it is not junk, it is the
low 12 bits of the instruction.

> ✓ **Check 2.** (a) What is in AR at the end of T₀? At the end of T₂? (b) Why is PC incremented at
> T₁? (c) After `IR ← M[AR]`, how many memory accesses has this instruction made?

---

### 3 · Which type? — the decision at T₃

> **Q** *(the branch point of the whole machine)*
> **At T₃ the machine takes one of four mutually exclusive paths. What are they?**
>
> *From file 06: opcode 111 with I = 0 is register-reference, with I = 1 is I/O. Guess the four.*

| Condition | Action |
|---|---|
| `D′₇ I T₃` | `AR ← M[AR]` — **indirect MRI**: fetch the effective address |
| `D′₇ I′ T₃` | nothing — **direct MRI**: AR already holds EA from T₂ |
| `D₇ I′ T₃` | execute a **register-reference** instruction (call this condition **r**) |
| `D₇ I T₃` | execute an **input–output** instruction (call this condition **p**) |

**Memory-reference execution therefore starts at T₄**, because EA is in AR by the end of T₃ either
way. Register-reference and I/O instructions **finish at T₃** — they never reach T₄.

> ✓ **Check 3.** (a) What do r and p stand for? (b) Why do MRIs start executing at T₄ and not T₃?
> (c) Which of the four paths costs an extra memory access?

---

### 4 · Register-reference execution — and A2 Q6

> **Q** `[A2 Q6 · 10 marks]` **= Mano 5-9**
> **The content of AC in the basic computer is hexadecimal A937 and the initial value of E is 1.
> Determine the contents of AC, E, PC, AR, and IR in hexadecimal after the execution of the CLA
> instruction.**
> ⚠ **He dropped the workload: Mano adds "Repeat 11 more times, starting from each one of the
> register-reference instructions. The initial value of PC is hexadecimal 021."**
>
> *CLA clears AC. Guess what happens to E, and what ends up in AR. Then read on.*

The question gives no initial PC, so **assume Mano's: PC = 021** (the paper says missing data may be
assumed — say that you are assuming it).

The register-reference instructions execute under **r = D₇I′T₃**, testing IR's one-hot bits directly:

```
      r:    SC ← 0                        (always — they all finish at T₃)
CLA   rB₁₁: AC ← 0
CLE   rB₁₀: E ← 0
CMA   rB₉ : AC ← AC′
CME   rB₈ : E ← E′
CIR   rB₇ : AC ← shr AC, AC(15) ← E, E ← AC(0)
CIL   rB₆ : AC ← shl AC, AC(0) ← E, E ← AC(15)
INC   rB₅ : AC ← AC + 1
SPA   rB₄ : if (AC(15) = 0) then (PC ← PC + 1)
SNA   rB₃ : if (AC(15) = 1) then (PC ← PC + 1)
SZA   rB₂ : if (AC = 0)     then (PC ← PC + 1)
SZE   rB₁ : if (E = 0)      then (PC ← PC + 1)
HLT   rB₀ : S ← 0
```

**The trace for CLA (7800):**

| Step | Microoperation | Effect |
|---|---|---|
| T₀ | `AR ← PC` | AR = **021** |
| T₁ | `IR ← M[AR]`, `PC ← PC + 1` | IR = **7800**, PC = **022** |
| T₂ | decode; `AR ← IR(0-11)`; `I ← IR(15)` | D₇ = 1, AR = **800**, I = **0** |
| T₃ | r = D₇I′T₃; IR bit 11 = 1 → `AC ← 0`, `SC ← 0` | AC = **0000** |

**Answer:**

| Register | Value |
|---|---|
| **AC** | **0000** |
| **E** | **1** — unchanged; CLA clears AC, **CLE** is what clears E |
| **PC** | **022** |
| **AR** | **800** |
| **IR** | **7800** |

Two things people get wrong, and both are worth a mark: **E is untouched** (the question sets E = 1
precisely to see whether you know that), and **AR ends up holding 800**, not 021 — because T₂ loads
AR from IR(0-11) whatever the instruction type.

> ✓ **Check 4.** (a) Redo the table for **CME** instead of CLA. (b) Redo it for **INC** with AC = A937.
> (c) Why is AR = 800 rather than 021 at the end?

---

### 5 · The seven memory-reference instructions

> **Q** *(F8 in the exam map — "write the microoperation sequence for a named MRI")*
> **Write the full microoperation sequences for all seven memory-reference instructions.**
>
> *Try to reconstruct ADD and LDA from what you know before reading. They are two lines each.*

| Symbol | D | Operation |
|---|---|---|
| AND | D₀ | AC ← AC ∧ M[EA] |
| ADD | D₁ | AC ← AC + M[EA], E ← carry out |
| LDA | D₂ | AC ← M[EA] |
| STA | D₃ | M[EA] ← AC |
| BUN | D₄ | PC ← EA |
| BSA | D₅ | M[EA] ← PC, PC ← EA + 1 |
| ISZ | D₆ | M[EA] ← M[EA] + 1, skip next if the result is 0 |

**Memorise these — they are the spine of the unit:**

```
AND   D₀T₄: DR ← M[AR]
      D₀T₅: AC ← AC ∧ DR,  SC ← 0

ADD   D₁T₄: DR ← M[AR]
      D₁T₅: AC ← AC + DR,  E ← Cₒᵤₜ,  SC ← 0

LDA   D₂T₄: DR ← M[AR]
      D₂T₅: AC ← DR,  SC ← 0

STA   D₃T₄: M[AR] ← AC,  SC ← 0

BUN   D₄T₄: PC ← AR,  SC ← 0

BSA   D₅T₄: M[AR] ← PC,  AR ← AR + 1
      D₅T₅: PC ← AR,  SC ← 0

ISZ   D₆T₄: DR ← M[AR]
      D₆T₅: DR ← DR + 1
      D₆T₆: M[AR] ← DR,  if (DR = 0) then (PC ← PC + 1),  SC ← 0
```

**Notice the pattern:** every instruction that needs the operand spends T₄ fetching it into DR, then
acts at T₅. STA and BUN need no operand, so they finish at T₄. ISZ needs three steps because it must
read, modify and write back.

⚠ **Deck erratum.** The Unit-2 slides print ISZ's third line as **`D₆T₄`** — a typo repeating T₄. The
correct timing is **`D₆T₆`**, as the same deck's own "Complete Computer Description" slide shows.
Write `D₆T₆`.

> ✓ **Check 5.** (a) Which two MRIs finish at T₄, and why? (b) Why does ISZ need three execute steps?
> (c) Which register receives the carry out of ADD?

---

### 6 · BSA and ISZ — the two that get asked

> **Q** *(Mano's own favourite, and the deck spends a figure on it)*
> **Explain BSA with a memory before/after diagram. Why does it take two timing steps rather than one?**
>
> *BSA is "branch and save return address". Guess where the return address goes.*

**BSA is the subroutine-call instruction** and the one students get wrong.

```
 D₅T₄: M[AR] ← PC,  AR ← AR + 1
 D₅T₅: PC ← AR,  SC ← 0
```

It stores the **return address** — PC, which by T₄ already points *past* the call (step 2) — into the
word at EA, then jumps to **EA + 1**. So a subroutine's **first word is its return-address slot** and
its code starts one location later.

*Worked (the deck's figure):* `BSA 135` at location 20. At T₄, PC = 21.

```
  BEFORE                          AFTER
  20 │ BSA 135  │ ← PC=20         20 │ BSA 135  │
  21 │   next   │                 21 │   next   │
     │          │                    │          │
 135 │    ?     │                135 │    21    │  ← return address saved
 136 │ subroutine                136 │ subroutine │ ← PC = 136
```

**Returning** is `BUN` **indirect** through EA: `1 BUN 135` → PC ← M[135] = 21.

**Why two steps and not one** — the explanation mark: AR must be **incremented** *and* then **used as
the new PC**, but the bus carries only one thing per clock pulse. Hardware serializes what the
symbolic description writes as one line. (Same principle as file 06, step 6.)

**ISZ is the loop-counter instruction:** increment a memory location, and if it wraps to 0, skip the
next instruction. Counting **up to zero** rather than down from n is deliberate — the zero test is
free, because it is just "did the increment produce all-zeros".

> ✓ **Check 6.** (a) Where does BSA put the return address, and where does it jump? (b) How do you
> return from a BSA subroutine? (c) Why does ISZ count up to zero instead of down from n?

---

### 7 · A full trace — A2 Q7, the question file 00 opened with

> **Q** `[A2 Q7 · 10 marks]` **= Mano 5-12**
> **The content of PC in the basic computer is 3AF. The content of AC is 7EC3. The content of memory
> at address 3AF is 932E. The content of memory at address 32E is 09AC. The content of memory at
> address 9AC is 8B9F.**
> **a. What is the instruction that will be fetched and executed next?**
> **b. Show the binary operation that will be performed in the AC when the instruction is executed.**
> ⚠ **He dropped part (c): "Give the contents of PC, AR, DR, AC, IR in hexadecimal and the values of
> E, I and SC in binary at the end of the instruction cycle."** Do it — it is the natural exam extension.
>
> *You got part (a)'s first half in file 00. Now do the whole thing before reading.*

**Decode the instruction.** PC = 3AF, so the instruction is M[3AF] = **932E**.

```
  9    =  1001    →  bit 15 = 1  →  I = 1, INDIRECT
                     opcode = 001 = D₁ = ADD
  32E  =  the address field
```

**(a)** It is an **indirect ADD** with address field 32E. Because I = 1, the effective address is not
32E — it is `M[32E]` = **09AC**, i.e. **EA = 9AC**. The operand is `M[9AC]` = **8B9F**.

**(b)** The operation is `AC ← AC + M[EA]`:

```
     7EC3        (AC)
   + 8B9F        (operand at 9AC)
   ────────
    1 0A62       →  AC = 0A62,  carry out E = 1
```

In binary: `0111 1110 1100 0011 + 1000 1011 1001 1111 = 0000 1010 0110 0010` with a carry out of 1
into E.

**(c) The full cycle, step by step:**

| Step | Condition | Microoperation | Result |
|---|---|---|---|
| T₀ | `R′T₀` | `AR ← PC` | AR = 3AF |
| T₁ | `R′T₁` | `IR ← M[AR]`, `PC ← PC + 1` | IR = 932E, PC = **3B0** |
| T₂ | `R′T₂` | decode; `AR ← IR(0-11)`; `I ← IR(15)` | D₁ = 1, AR = 32E, I = **1** |
| T₃ | `D′₇IT₃` | `AR ← M[AR]` — the indirect fetch | AR = **9AC** |
| T₄ | `D₁T₄` | `DR ← M[AR]` | DR = **8B9F** |
| T₅ | `D₁T₅` | `AC ← AC + DR`, `E ← Cₒᵤₜ`, `SC ← 0` | AC = **0A62**, E = **1** |

| Register | End value |
|---|---|
| PC | **3B0** |
| AR | **9AC** |
| DR | **8B9F** |
| AC | **0A62** |
| IR | **932E** |
| E | **1** |
| I | **1** |
| SC | **0000** |

**The one that catches everyone** is picking the operand. Three memory values are given and only the
last is the operand — 09AC is an *address*, not data. The giveaway is bit 15 of the instruction.

> ✓ **Check 7.** (a) Which of 932E, 09AC, 8B9F is the operand, and how do you know?
> (b) Why is PC 3B0 rather than 3AF at the end? (c) If the instruction had been **132E** instead of
> 932E, what would the operand be?

---

### 8 · A different machine — A2 Q8

> **Q** `[A2 Q8 · 10 marks]` **= Mano 5-16**
> **A computer uses a memory of 65,536 words with eight bits in each word. It has registers PC, AR,
> TR (16 bits each) and AC, DR, IR (eight bits each). A memory-reference instruction consists of
> three words: an 8-bit operation code (one word) and a 16-bit address (in the next two words). All
> operands are eight bits. There is no indirect bit. List the sequence of microoperations for
> fetching a memory reference instruction and then placing the operand in DR. Start from T₀.**
>
> *The BC fetched an instruction in one memory access. Guess how many this machine needs, and why.
> Then read on.*

This question tests whether you understand the fetch sequence or merely memorised it. **The words
are 8 bits but the addresses are 16**, so one address does not fit in one word — it takes **two**. The
whole instruction is therefore three words and needs **three fetches**, plus one more for the operand.

TR (16 bits) is the natural place to assemble the two address halves before moving them to AR.

```
T₀:  AR ← PC
T₁:  IR ← M[AR],  PC ← PC + 1              fetch the opcode word
T₂:  AR ← PC,  PC ← PC + 1
T₃:  TR(8-15) ← M[AR],  AR ← PC,  PC ← PC + 1     first (high) address byte
T₄:  TR(0-7) ← M[AR]                              second (low) address byte
T₅:  AR ← TR                                      the full 16-bit address
T₆:  DR ← M[AR]                                   the operand
```

**Assumption to state** (the paper allows it): the **high-order byte of the address is stored first**.
If the low byte comes first, swap the T₃ and T₄ destinations — the structure is identical. Say which
you assumed; that is worth a mark and costs a line.

**Four memory accesses in total**: opcode, address high, address low, operand. Compare the BC's two
for a direct MRI (file 06, step 2) — this is what an 8-bit word costs you.

> ✓ **Check 8.** (a) Why does the address take two words? (b) Why is TR used rather than loading AR
> twice? (c) How many memory accesses in total, and what is each for?

---

### 9 · The interrupt cycle

> **Q** `[Mano 5-18 · not yet asked]`
> **An output program resides in memory starting from address 2300. It is executed after the computer
> recognizes an interrupt when FGO becomes 1 (while IEN = 1). a. What instruction must be placed at
> address 1? b. What must be the last two instructions of the output program?**
>
> *Guess why the question cares about address 1 in particular.*

**Setting the interrupt flip-flop R:**

```
T′₀ T′₁ T′₂ (IEN)(FGI + FGO):  R ← 1
```

Read that carefully — it is a favourite exam item. The interrupt is recognised **only when none of
T₀, T₁, T₂ is active** (so the current instruction is past fetch and decode), **and** interrupts are
enabled, **and** some flag is set. That is how *"finish the current instruction first"* is implemented
in hardware — no scheduler, just a control function.

**The interrupt cycle** (fetch/decode become `R′T₀, R′T₁, R′T₂`, so they run only when R = 0):

```
RT₀:  AR ← 0,  TR ← PC
RT₁:  M[AR] ← TR,  PC ← 0
RT₂:  PC ← PC + 1,  IEN ← 0,  R ← 0,  SC ← 0
```

**Mechanism:** the interrupt cycle is a **hardware implementation of BSA** to the fixed location 0.
The return address goes to **M[0]**; control resumes at **address 1**, where the programmer must have
placed a branch to the service routine. IEN is cleared so the service routine is not itself
interrupted.

So the answers: **(a)** address 1 must hold `BUN 2300` — the branch to the output program.
**(b)** the program must end with `ION` (re-enable interrupts) followed by `BUN 0` **indirect**, which
loads PC from M[0] — the saved return address.

> ✓ **Check 9.** (a) Why must R be recognised only outside T₀T₁T₂? (b) Where is the return address
> saved, and why that location? (c) Why is IEN cleared during the interrupt cycle?

---

## Exam form

### The timing table — the one thing to memorise

```
T₀:  AR ← PC
T₁:  IR ← M[AR],  PC ← PC + 1
T₂:  decode IR(12-14) → D₀..D₇,  AR ← IR(0-11),  I ← IR(15)
T₃:  D'₇ I  → AR ← M[AR]         (indirect)
     D'₇ I' → nothing            (direct)
     D₇ I'  → r: register-reference, SC ← 0
     D₇ I   → p: input/output,      SC ← 0
T₄+: the MRI sequence for whichever D is active
```

### How to answer any trace question

1. **Fetch:** the instruction is `M[PC]`. Write PC + 1 immediately.
2. **Decode the first hex digit into 4 bits.** Bit 15 is I; the other three are the opcode.
3. **If I = 1, do the extra indirect fetch at T₃** — EA = M[address field].
4. **Run the MRI sequence** for that D, one row per timing signal.
5. **Table the answer**: one column per register, one row per step. Show unchanged registers too.
6. **SC = 0000 at the end**, always.

### Hex ↔ instruction

First hex digit: bit 15 = I, bits 14-12 = opcode. `0/8` AND · `1/9` ADD · `2/A` LDA · `3/B` STA ·
`4/C` BUN · `5/D` BSA · `6/E` ISZ · `7` register-reference · `F` I/O.

---

## Attempt

1. `[A2 Q5 · 10]` the timing diagram + the five-point explanation.
2. `[A2 Q6 · 10]` the CLA trace — then **Mano's other 11**, one register-reference instruction at a
   time. This is the single best drill in the file and he deleted it from the assignment.
3. `[A2 Q7 · 10]` all three parts including the dropped (c).
4. `[A2 Q8 · 10]` the seven-step sequence, with your byte-order assumption stated.
5. `[Mano 5-10]` the direct-AND twin of Q7 — then repeat for six other MRIs as Mano asks.
6. `[Mano 5-11]` the ISZ-indirect trace with a row per timing signal. Hardest in the chapter.
7. `[Mano 5-18]` the interrupt question.

---

## Traps

| Trap | Correction |
|---|---|
| Writing ISZ's last line as `D₆T₄` | Deck typo. It is **`D₆T₆`** |
| Taking 09AC as the operand in A2 Q7 | It is the **effective address**. The operand is M[9AC] = 8B9F |
| Saying CLA clears E | CLA clears **AC**. CLE clears E |
| Leaving AR = the fetch address after an RRI | T₂ loads AR from IR(0-11) for **every** instruction |
| Forgetting PC + 1 | It happens at **T₁**, before any branch can overwrite PC |
| BSA jumping to EA | It jumps to **EA + 1**; EA holds the return address |
| Forgetting `SC ← 0` | It is the last microoperation of every instruction, and it is a mark |
| Showing only changed registers in a trace | Show all of them; unchanged is information too |
| Assuming a byte order in A2 Q8 silently | State the assumption. The paper explicitly allows assumptions |

---

## Self-test

1. Write the three fetch/decode lines from memory.
2. What are the four T₃ paths and their conditions?
3. Which MRIs finish at T₄?
4. PC = 100, M[100] = 2150, M[150] = 00FF, AC = 0001. What executes, and what is AC afterwards?
5. Same, but M[100] = A150. What changes?
6. Why does the interrupt cycle resemble BSA?
7. Why must SC be cleared rather than allowed to count on to T₁₅?

---
---

## Answers

**Check 1.** (a) A **4×16 decoder** on the 4-bit sequence counter. (b) Because the CLR input of SC is
asserted, so at the edge that would have taken SC from 3 to 4 it goes to **0** instead. (c) Six —
T₀ through T₅.

**Check 2.** (a) End of T₀: **PC's value** (the instruction's address). End of T₂: **IR(0-11)**, the
address field. (b) AR already holds the fetch address, so PC is free; incrementing early means PC
points at the next instruction before any branch can overwrite it. (c) **One** — the instruction fetch
at T₁.

**Check 3.** (a) **r** = register-reference (`D₇I′T₃`), **p** = input/output (`D₇IT₃`). (b) Because EA
is only guaranteed to be in AR at the *end* of T₃ — the indirect path uses T₃ to fetch it. (c) The
indirect MRI path, `D′₇IT₃`.

**Check 4.** (a) **CME** is 7100. T₀ AR = 021 · T₁ IR = 7100, PC = 022 · T₂ AR = 100, I = 0 · T₃ rB₈:
E ← E′ = **0**. So AC = **A937** (unchanged), E = **0**, PC = **022**, AR = **100**, IR = **7100**.
(b) **INC** is 7020. Same first three steps with AR = **020**, IR = **7020**; T₃ rB₅: AC ← AC + 1 =
A937 + 1 = **A938**. E = **1** unchanged, PC = **022**. (c) Because `AR ← IR(0-11)` at T₂ is
unconditional — 7800's low 12 bits are 800.

**Check 5.** (a) **STA** and **BUN** — neither needs the operand brought into DR, so there is nothing
to do at T₅. (b) It must **read** M[AR] into DR, **increment** DR, and **write** it back — three
transfers, three pulses. (c) **E**.

**Check 6.** (a) Return address into **M[EA]**; it jumps to **EA + 1**. (b) `BUN` **indirect** through
EA — `1 BUN <EA>` loads PC from M[EA]. (c) Because the zero test is free: the increment either
produces all-zeros or it does not, and no comparison hardware is needed.

**Check 7.** (a) **8B9F**. The instruction's first hex digit 9 = 1001 has bit 15 = 1, so I = 1 and the
address field is a pointer: EA = M[32E] = 9AC, operand = M[9AC]. (b) PC is incremented at **T₁**,
before execution. (c) 132E has bit 15 = 0 → direct, so EA = 32E and the operand would be
M[32E] = **09AC**.

**Check 8.** (a) Addresses are 16 bits and words are 8, so one address needs **two words**. (b) AR
must hold the *complete* 16-bit address before any access; loading it in halves would leave it
briefly pointing at a wrong location, and AR has no half-load path. TR is 16 bits and can be
assembled in two steps. (c) **Four** — opcode, high address byte, low address byte, operand.

**Check 9.** (a) So the current instruction finishes first — T₀T₁T₂ are its fetch and decode, and
interrupting mid-fetch would lose it. (b) **M[0]**, because the interrupt cycle is a hardware BSA to
the fixed location 0; control then resumes at address 1. (c) So the service routine is not itself
interrupted before it has saved what it needs.

**Self-test 1.** `T₀: AR ← PC` · `T₁: IR ← M[AR], PC ← PC + 1` · `T₂: decode IR(12-14), AR ← IR(0-11),
I ← IR(15)`.

**Self-test 2.** `D′₇IT₃` indirect fetch · `D′₇I′T₃` nothing · `D₇I′T₃` register-reference ·
`D₇IT₃` input/output.

**Self-test 3.** **STA** (`D₃T₄`) and **BUN** (`D₄T₄`).

**Self-test 4.** 2150: 2 = 0010, I = 0, opcode 010 = **LDA**, direct, address 150. So AC ← M[150] =
**00FF**.

**Self-test 5.** A150: A = 1010, I = **1** → indirect LDA. EA = M[150] = 00FF → EA = **0FF**, so
AC ← M[0FF] — a location whose contents the question does not give. The point: the same low digits
mean different things depending on bit 15.

**Self-test 6.** Because it saves the return address into a fixed memory word and then transfers
control — exactly BSA's two actions, done by hardware to location 0 instead of by an instruction to EA.

**Self-test 7.** Because SC is what selects the timing signal; leaving it to run would generate T₇…T₁₅
with no microoperations attached, wasting clock cycles. Clearing it ends the instruction immediately
and starts the next fetch at T₀.

---

## What to do next

File 08 is the other half of U2 and the last of the "design" skills: given the complete machine
description you have just learnt, **derive the control gates** for a register. That is A2 Q9 and Q10 —
and Mano leaves four more of the same kind unasked.
