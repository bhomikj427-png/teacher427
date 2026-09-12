# 02 — Register Transfer Language, Bus and Memory Transfers

**U1, lectures L3–L4 · CO1.** ★ **This is the gate.** U2 and U3 are *written* in RTL. If `R2 ← R1`
still reads to you as a line of code, every design question in the paper will look like magic.

Notation in this pack: `←` = transfer · `′` = complement · `∧` = AND · `∨` = OR · `⊕` = XOR ·
`M[AR]` = the memory word addressed by AR.

---

## Map

```
   why a notation?  words are ambiguous and unbuildable
        |
        v
   RTL:  R2 <- R1        plain transfer
         P: R2 <- R1     conditional on control function P
         A <- B, C <- D  simultaneous, same clock edge
        |
        +--> the hardware behind one statement:
        |       (1) select the SOURCE onto the path   (2) assert LD on the DESTINATION
        |       (3) it happens at the CLOCK EDGE
        |
        v
   connecting n registers pairwise costs n(n-1) lines   --> too many
        |
        v
   THE BUS: one shared, time-multiplexed path + a select code
        |
        +--> built from MUXes (n MUXes of k inputs)  or  tri-state buffers + decoder
        |
        v
   MEMORY as a bus source/destination:  DR <- M[AR]  (read) · M[AR] <- DR  (write)
```

---

## Attempt first

1. What two things must be true, simultaneously, for `DR ← M[AR]` to actually happen?
2. Is `A ← B, B ← A` legal? If you think it is a bug, say what would make it a bug.
3. You have 8 registers and want any one to be able to load from any other by direct wiring. How many
   connection lines is that?
4. To bus **4 registers of 8 bits each** using multiplexers, how many multiplexers of what size, and
   how many select lines?
5. `P: R2 ← R1` — where does P come from in a real machine?
6. Write the RTL for: "if the control signal T₁ is active, read the memory word addressed by AR into
   IR and increment PC at the same time."

---

## Method

### The whole vocabulary — there is not much of it

| Notation | Meaning |
|---|---|
| `R2 ← R1` | contents of R1 are **copied** into R2; **R1 is unchanged** |
| `P: R2 ← R1` | the transfer happens **only if** the control function P = 1 |
| `R2(0-7)` | a field or portion of a register |
| `AR ← DR(AD)` | transfer the AD portion of DR into AR |
| `A ← constant` | load a binary constant |
| `M[R]` | the memory word addressed by register R |
| `M` | shorthand for `M[AR]` |
| `DR ← M` | **memory read** — the word addressed by AR goes into DR |
| `M ← DR` | **memory write** — DR goes into the word addressed by AR |
| `A ← B, C ← D` | comma = **simultaneous** transfers on the same clock edge |

**Registers are drawn** as a rectangle with the name inside; a common convention shows the bit numbers
above and the register name below, e.g. `R1` with bits 15…0, or `PC(H)` / `PC(L)` for the two halves
of a 16-bit PC.

### ★ The threshold idea: an RTL statement is hardware, not code

`R2 ← R1` is not executed by anything. It is a **specification of wiring and timing**:

```
   R1 ----[ outputs gated onto the path ]----> R2's inputs
                                                 ^
                            LD(R2) = 1 ----------+
                                                 |
                            at the CLOCK EDGE, R2 captures
```

Three consequences you must be able to state:

1. **A transfer needs two conditions**, never one: the **source must be selected** onto the path, and
   the **destination's load line must be asserted**. Trap T2 in the pack lives here.
2. **`A ← B, B ← A` in one line is legal and normal.** Both registers read the *old* values of the
   other during the clock period, and both capture at the same edge. In software this needs a
   temporary; in hardware it does not. If your answer to Attempt 2 was "it's a bug", you were reading
   RTL as code.
3. The control function **P** is not a variable in a program. It is a **wire** — a Boolean product of
   decoder outputs, timing-counter outputs and flag bits (in U2, things like `D₅T₄` or `R′T₀`), high
   for exactly one clock period.

**Diagnostic you should be able to pass cold:** *what two things must be true for `DR ← M[AR]`?*
Answer: **S₂S₁S₀ = 111** (memory drives the common bus) **and LD(DR) = 1**.

### Why a bus exists — the counting argument

To connect **n registers** so that any one can load from any other by direct wiring needs

> **n(n − 1) lines**

— one directed path per ordered pair. For n = 8 that is 56 sets of wires (×16 bits each). The deck's
own verdict: *"This is not a realistic approach to use in a large digital system."*

**The fix: a bus** — "a path (a group of wires) over which information is transferred from any of
several sources to any of several destinations." One shared path plus a select code collapses O(n²)
into O(n).

**What you gave up:** simultaneity. Only one transfer per clock can use the bus. That single sentence
is worth marks in three different questions — it is the von Neumann bottleneck (U1), the reason BSA
needs two clock cycles (U2), and the structural hazard (U4).

### Building a bus — two constructions

**(a) Multiplexers.** One MUX per **bit position**, each choosing among the k registers' bits at that
position, all MUXes sharing the select lines.

> **To bus k registers of n bits: n multiplexers, each k-to-1, with ⌈log₂ k⌉ select lines.**

Say it as *"one MUX per bit, as many inputs as registers"* and you will never invert it under exam
pressure.

**(b) Tri-state buffers + a decoder.** Each register's output goes through tri-state buffers; a
decoder drives exactly one buffer group's enable. Cheaper in wires than a MUX tree for a wide bus.
Either construction gives the same behaviour; the exam asks for the MUX sizing rule.

⚠ **What breaks if two sources are enabled at once:** **bus contention** — a low-impedance path from
supply to ground through two fighting drivers. The bus value is undefined and the drivers can be
damaged. This is why exactly one select code is active at a time and why a "nothing on the bus" code
exists.

**Transfer notation with a bus:**

```
   BUS ← R1,  R2 ← BUS        which is written simply as        R2 ← R1
```

### Memory transfers

**AR always holds the address.** That is not a convention you may vary — the memory's address pins
are wired to AR.

| Operation | RTL | What the hardware does |
|---|---|---|
| **Read** | `DR ← M[AR]` | select memory onto the bus, assert read, assert LD(DR) |
| **Write** | `M[AR] ← DR` | select DR onto the bus, assert write |

**RAM and ROM, as the deck frames them.** An **m × n RAM** is m words of n bits. **k address lines
select one of 2ᵏ words**, and n data lines carry the word.

- RAM **write**: apply the address → apply the data → activate the write input.
- RAM **read**: apply the address → activate the read input.
- ROM **read**: apply the address → activate read. There is **no data-in path** — output only.

---

## Worked — bus sizing (inferred form F3/F5; the sizing rule is the deck's)

> **Design a common bus for four 16-bit registers using multiplexers. How many multiplexers of what
> size, how many select lines, and what does the construction look like?**

**Step 1 — apply the rule.** k = 4 registers, n = 16 bits.

> n multiplexers, each k-to-1 → **16 multiplexers, each 4-to-1**.
> Select lines: ⌈log₂ 4⌉ = **2** (call them S₁S₀), shared by all 16 MUXes.

**Step 2 — say what each MUX is wired to.** MUX number i (for i = 0…15) takes as its four inputs the
**bit i of each of the four registers**: A(i), B(i), C(i), D(i). Its output is bit i of the bus.

```
            A0 B0 C0 D0      A1 B1 C1 D1          A15 B15 C15 D15
             |  |  |  |       |  |  |  |            |   |   |   |
            +----------+     +----------+          +-------------+
     S1 S0 -|  4-to-1  |     |  4-to-1  |   ...    |   4-to-1    |
            +----+-----+     +----+-----+          +------+------+
                 |                |                       |
              BUS(0)           BUS(1)                  BUS(15)
```

**Step 3 — the selection table.**

| S₁ | S₀ | Register on the bus |
|---|---|---|
| 0 | 0 | A |
| 0 | 1 | B |
| 1 | 0 | C |
| 1 | 1 | D |

**Step 4 — the sentence that earns the last mark.** The bus supplies the *source*; the **destination
is chosen separately**, by asserting LD on whichever register is to receive. Select lines alone move
nothing.

**Compare with the direct-wiring cost:** 4 registers pairwise = 4 × 3 = **12 sets of 16 lines = 192
wires**, versus 16 MUXes and one 16-line bus. The gap grows as n(n−1), which is the whole argument.

---

## Worked — reading a machine's timing, in RTL (from Mano's Basic Computer fetch; the U2 preview)

> **Write the RTL for: at T₀ put PC into AR; at T₁ read the instruction into IR and increment PC.**

```
   T₀:   AR ← PC
   T₁:   IR ← M[AR],  PC ← PC + 1
```

**Now read the first line as hardware, which is what the mark is for:**
at T₀, the bus select code is set to **PC** (S₂S₁S₀ = 010 in the BC), **LD(AR) = 1**, and at the
clock edge AR captures the bus value.

**And the second line:** the bus select code is set to **memory** (111), **LD(IR) = 1**, and —
simultaneously and *independently of the bus* — **INR(PC) = 1**, because incrementing PC uses PC's
own incrementer, not the shared bus. That is why two things can happen in one clock here but **not**
in BSA (U2), where both actions want the bus.

**The question behind the question:** why is PC incremented at T₁ and not later? Because its old value
was already safely copied into AR at T₀, so PC is free — and incrementing it early is what makes PC
point at the *next* instruction in time for a subroutine call to save it as a return address.

---

## Traps

| # | Trap | The correction |
|---|---|---|
| M2 | **"`R2 ← R1` is an assignment statement."** The deepest error in the subject | It is a hardware specification: source selected + LD asserted + clock edge. Test yourself with `DR ← M[AR]` → 111 **and** LD(DR) |
| T2 | Naming only the source ("PC goes on the bus") in a design answer | Name **both** halves — source select **and** destination load — or the transfer never happens |
| — | Thinking `A ← B, B ← A` needs a temporary register | It does not. Both read old values; both capture at the same edge |
| — | Inverting the MUX rule (k MUXes of n inputs) | **n MUXes of k inputs** — one MUX per *bit*, as many inputs as *registers* |
| — | Forgetting `M` means `M[AR]` | AR is wired to the address pins. A memory transfer with a different address register does not exist in the BC |
| — | Allowing two bus sources at once in a design | Bus contention: undefined value, possible damage. Exactly one source code is active |

---

## Self-test

1. Write, in RTL, "transfer the low-order 8 bits of AC to OUTR when the control function `pB₁₀` is
   active".
2. A machine has 12 registers. (a) How many lines would full pairwise interconnection need?
   (b) Using one common bus built from MUXes, how many MUXes of what size for 8-bit registers, and
   how many select lines?
3. `T₄: M[AR] ← PC, AR ← AR + 1` — these are written on one line. Can both happen in the same clock
   cycle on a single-bus machine? Justify from the hardware.
4. Explain why a bus makes a computer **buildable** but not **faster**, and name the U4 phenomenon
   that is the price.
5. A 2048 × 16 RAM: how many address lines, how many data lines? What changes if it were a ROM?
6. A designer enables two registers onto the common bus in the same clock period by mistake. What
   physically happens, and what should the design have done instead?
7. Write the sequence of RTL statements to swap the contents of registers R1 and R2 **on a single-bus
   machine with no direct register-to-register path except the bus**. How many clock cycles?
8. Why is the select code for the Basic Computer's bus 3 bits wide when there are 7 registers plus
   memory?

---

## Answers

**1.** `pB₁₀:  OUTR ← AC(0-7)`

**2.** (a) n(n − 1) = 12 × 11 = **132** sets of lines.
(b) **8 multiplexers** (one per bit), each **12-to-1**, with ⌈log₂ 12⌉ = **4** select lines.

**3.** **No.** `M[AR] ← PC` requires PC to drive the bus while memory's write line is asserted;
`AR ← AR + 1` uses AR's own incrementer and does **not** need the bus — so on this machine those two
*can* coexist. The real test is whether two statements both need the **bus**. (This is exactly BSA's
D₅T₄, which is legal; what forces BSA into two cycles is that the *next* action, `PC ← AR`, needs the
bus again — see file 05.)

**4.** A bus replaces O(n²) direct wiring with one shared path plus a select code, which is what makes
a machine with many registers physically constructible. What it costs is **simultaneity**: only one
transfer per clock may use it. The U4 price is the **structural hazard** — two pipeline segments
needing the same memory/bus in one clock, forcing a stall.

**5.** 2048 = 2¹¹ → **11 address lines**, **16 data lines**. As a ROM, the 16 data lines become
**output-only** — there is no data-in path and no write control; you apply an address and enable the
read.

**6.** **Bus contention**: two drivers fight, creating a low-impedance path from supply to ground
through them. The bus value is undefined and the output drivers can be damaged. The design should
have ensured exactly one select code is active at a time (the decoder or MUX select guarantees this
by construction, which is precisely why buses are built from MUXes or decoder-enabled tri-state
buffers rather than from plain wires).

**7.** The bus can carry only one value per clock, so you need a third register as scratch (TR in the
BC):

```
   T₀:  TR ← R1
   T₁:  R1 ← R2
   T₂:  R2 ← TR
```

**Three clock cycles.** Note the contrast with `A ← B, B ← A`, which *is* legal — but only on a
machine where A and B have **direct** paths to each other, not a shared single bus. The bus is what
forces serialization.

**8.** Count the **sources**, not the registers in the machine. Only six registers can drive the bus
(AR, PC, DR, AC, IR, TR), plus **memory** — seven sources — and the code must also encode
**"nothing on the bus"** (000). Seven sources + the idle state = **8 codes = 3 bits**. In general an
n-source bus needs ⌈log₂(n + 1)⌉ select lines when "no source" must be encodable. INPR and OUTR are
not bus sources: INPR feeds AC through the adder-and-logic circuit, and OUTR is load-only.
