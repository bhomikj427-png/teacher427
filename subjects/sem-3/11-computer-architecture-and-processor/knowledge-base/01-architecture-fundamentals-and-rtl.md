# U1 — Architecture Fundamentals, Register Transfer & Microoperations (Stage 1)

**Lectures L1–L8 · CO1 · MTE + ETE · deck: `../exam-pack/slides-unit1-…pdf` (33 pp)**

Scope (hand-out): Introduction, computer types, functional units, von Neumann and Harvard
architectures, RISC and CISC architectures · Register Transfer Language and Register Transfer · Bus
and Memory Transfers · Arithmetic Microoperations · Logic Microoperations · Shift Microoperations ·
Arithmetic Logic Shift Unit.

Truth authority: **Mano 3e** ch. 1 & 4 (+ Hamacher for functional units). Deck = scope/framing only.

---

## 1. Architecture vs organization — `settled`

| | Computer **Architecture** | Computer **Organization** |
|---|---|---|
| Question answered | **What** the computer does | **How** it does it |
| Deals with | functional behaviour | structural relationship |
| Design level | high-level design issues | low-level design issues |
| Also called | **instruction set architecture (ISA)** | **microarchitecture** |
| Comprises | instruction sets, registers, data types, addressing modes | circuit design, peripherals, adders, buses, control logic |
| Order of design | comes **first** | comes **after** architecture is decided |

**Mechanism — why the split exists at all.** The ISA is a *contract* between hardware and software:
it is the set of promises a programmer may rely on. Organization is any implementation that keeps
those promises. This is what lets Intel ship a 8086 and a Core i9 that run the same binaries, and it
is why "architecture comes first" — you cannot implement a contract you have not written. The whole
course is a walk down this ladder.

⚠ **The deck contains one weak row** ("Architecture indicates its hardware. Organization indicates
its performance"). That row is muddled — architecture is the *abstraction*, not the hardware, and
performance is a property of the organization *and* the technology. Reproduce the table for the exam
if asked (it is the professor's framing) but do not reason from that row. See `misconceptions.md` M1.

## 2. Functional units — `settled` (Hamacher's five-part framing)

A computer has **five functionally independent main parts**:

| Unit | Job | Mechanism worth stating |
|---|---|---|
| **Input** | accepts program & data | a keypress is translated to its binary code and sent to memory or processor |
| **Memory** | stores programs & data | **primary** (fast, electronic-speed, holds executing programs) vs **secondary/auxiliary** (large, cheap, slow — disks, optical). Built of storage cells, organized so one **word** is stored or retrieved in one basic operation. **RAM** = any location reached in a *short and fixed* time after giving its address |
| **ALU** | arithmetic & logic | operands are first brought **into processor registers**, then operated on — this is why register transfers, not memory operations, are the atoms |
| **Output** | sends results out | printer, display |
| **Control** | controls everything else | sends read/write control signals, senses states, and issues **timing signals** — "signals that determine *when* a given action is to take place" |

**Processor = ALU + control.** CPU = processor + its registers.

**The key idea the deck states plainly:** combinational and sequential circuits are the *low-level
building blocks*; defining the internal organization of a computer means fixing three things —
**(1) the set of registers and their functions, (2) the set of allowable microoperations, and
(3) the control signals that initiate sequences of them.** That triple is the bridge from Digital
Electronics into this course.

## 3. Von Neumann vs Harvard — `settled`

| | **von Neumann** | **Harvard** |
|---|---|---|
| Memory | **one** memory holds both instructions and data | **separate** instruction memory and data memory |
| Buses | one shared address+data path to the CPU | two independent sets of address and data buses |
| Consequence | instruction fetch and data access **contend** for the one bus | instruction fetch and data access proceed **simultaneously** |
| Cost | simpler, cheaper, flexible (memory can be split any way) | more pins, more silicon, fixed split |
| Where used | general-purpose machines (the BC of U2 is von Neumann) | DSPs, microcontrollers, and the **L1 cache level** of most modern CPUs |

**Mechanism — the von Neumann bottleneck.** Because one bus carries both streams, the maximum speed
of the system is limited by **memory bandwidth**, not by processor speed; the CPU can outrun its
memory and then simply wait. The deck states this in U3's SISD slide: "Maximum speed of the system is
limited by the Memory Bandwidth… memory is shared by CPU and I/O." **This is not a separate fact from
big idea 3 — it is the same O(n²)-avoidance trade (share one path in time) paid for at the system
level.** It is also *why* the structural hazard in U4 exists: one memory port, two segments wanting
it.

**Stored-program concept (the reason von Neumann matters):** instructions are stored in the same
memory as data, in the same binary form. So a program can be loaded, relocated, and even modified
like data — which is what makes a general-purpose computer general.

**Modified Harvard** (worth one line, `settled`): most real CPUs are von Neumann in main memory but
Harvard at the cache level — split L1-instruction and L1-data caches — getting the bandwidth without
committing to a fixed memory split.

## 4. RISC vs CISC — `settled` (revisited concretely in U7/U8)

| | **CISC** | **RISC** |
|---|---|---|
| Instruction count / complexity | many, complex, multi-step | few, simple, one job each |
| Instruction length | **variable** (8086: 1–6 bytes) | **fixed** (RISC-V: 32 bits) |
| Memory operands | most instructions may touch memory | **load/store only** — arithmetic is register-to-register |
| Registers | few, special-purpose | many, general-purpose (RISC-V: 32) |
| Addressing modes | many (8086: ~12) | few |
| Control unit | usually **microprogrammed** | usually **hardwired** |
| Cycles per instruction | variable, often many | ~1, pipelined |
| Complexity lives in | the **hardware** | the **compiler** |

**Mechanism — why the pendulum swung.** CISC made sense when memory was scarce and expensive and
programmers wrote assembly: a dense, powerful instruction saved precious bytes, and microprogramming
made a rich instruction set cheap to build. When memory got cheap and compilers got good, the
calculus inverted — what matters now is how fast you can **pipeline**, and you can only pipeline
cleanly if instructions are uniform in length, take uniform time, and touch memory in one predictable
place. The IOE/Mano statement makes the link explicit: "Most computers based on the RISC architecture
concept use **hardwired control** rather than a control memory with a microprogram."

⚠ **Don't teach this as CISC-is-obsolete.** x86 is CISC and dominates desktops/servers — modern x86
chips decode CISC instructions into RISC-like micro-operations internally. The *ISA* is CISC; the
*organization* is RISC-ish. That is big idea 1 doing real work. (`misconceptions.md` M3.)

## 5. Register Transfer Language — `settled`

**Why a notation at all:** describing a digital system in words is ambiguous and unbuildable. RTL is
a symbolic language that states, precisely, which registers move what, when.

**Vocabulary (the whole of it):**

| Notation | Meaning |
|---|---|
| `R2 ← R1` | contents of R1 are copied into R2 (R1 **unchanged**) |
| `P: R2 ← R1` | the transfer happens **only if** control function P = 1 |
| `R2(0-7)` | a field/portion of a register |
| `AR ← DR(AD)` | transfer the AD portion of DR into AR |
| `A ← constant` | load a binary constant |
| `M[R]` | the memory word addressed by register R |
| `M` | shorthand for `M[AR]` |
| `DR ← M` | **memory read** — word addressed by AR goes into DR |
| `M ← DR` | **memory write** — DR goes into the word addressed by AR |
| `A ← B, C ← D` | comma = **simultaneous** transfers on the same clock edge |

**★ Mechanism — the threshold idea.** An RTL statement is a *hardware specification*, not a program
statement. `R2 ← R1` compiles to: R1's outputs are gated onto the path, and LD(R2) is asserted so
that at the next clock edge R2 captures it. Two registers "swapping" in one line —
`A ← B, B ← A` — is *legal and normal* in hardware (both read the old values before the edge), which
is exactly what makes RTL different from code. This is threshold concept ★1 in `00-map.md`.

## 6. Bus and memory transfers — `settled`

**The problem, stated as a count.** To connect n registers so any one can load from any other needs
**n(n−1)** lines — O(n²). The deck: "This is not a realistic approach to use in a large digital
system."

**The fix.** A **bus** — "a path (a group of wires) over which information is transferred from any of
several sources to any of several destinations." Built either from **multiplexers** (one per bit
position, with common select lines) or from **tri-state buffers + a decoder**.

**Sizing rule (`settled`, and an exam favourite):** to bus **k registers of n bits** using
multiplexers you need **n multiplexers of k inputs each** — one MUX per bit position, each choosing
among the k registers' corresponding bits. Select lines: ⌈log₂ k⌉. *Worked:* 4 registers × 4 bits →
4 MUXes, each 4-to-1, 2 select lines.

**Transfer notation with a bus:**
```
BUS ← R1,  R2 ← BUS      (or simply  R2 ← R1)
```

**Memory transfers.** AR always holds the address. Read: `DR ← M[AR]`. Write: `M[AR] ← DR`.

**RAM and ROM (as the deck frames them):** an m×n RAM is m words of n bits; **k address lines select
one of 2ᵏ words**, n data lines carry the word. RAM write = apply address → apply data → activate
write. ROM read = apply address → activate read (no data-in path; output only).

## 7. Arithmetic microoperations — `settled`

A **microoperation** is an elementary operation performed on data held in registers. Four categories:

| Category | What it does |
|---|---|
| **Register transfer** | move binary information between registers |
| **Arithmetic** | arithmetic on numeric data in registers |
| **Logic** | bit-manipulation on non-numeric data |
| **Shift** | shift operations on data in registers |

**The basic arithmetic microoperations:**

| RTL | Name | Built from |
|---|---|---|
| `R3 ← R1 + R2` | add | binary adder (n full adders, ripple carry) |
| `R3 ← R1 − R2` | subtract | usually via `R1 + R2′ + 1` (2's complement) |
| `R2 ← R2′` | 1's complement | inverters |
| `R2 ← R2′ + 1` | 2's complement (negate) | complement + increment |
| `R1 ← R1 + 1` | increment | binary incrementer (half-adders + constant 1) |
| `R1 ← R1 − 1` | decrement | add all-1s (= −1 in 2's complement) |

**Mechanism — one circuit does add *and* subtract.** Feed each B input through an XOR with a mode
line M, and feed M into C₀. M = 0 → XOR passes B, C₀ = 0 → **A + B**. M = 1 → XOR inverts B to B′,
C₀ = 1 → **A + B′ + 1 = A − B**. *One* adder-subtractor, selected by a single line. This is the
cleanest example in the course of "control signals select behaviour from fixed hardware."

**The 4-bit arithmetic circuit — `settled`, and the deck's own exam question.** One full adder per
bit, with each FA's **Y input driven by a 4-to-1 MUX** selecting B, B′, 0 or 1 under S₁S₀; X is
always A; Cᵢₙ is the third control.

| S₁ | S₀ | Cᵢₙ | Y | Output D | Microoperation |
|---|---|---|---|---|---|
| 0 | 0 | 0 | B | D = A + B | add |
| 0 | 0 | 1 | B | D = A + B + 1 | add with carry |
| 0 | 1 | 0 | B′ | D = A + B′ | subtract with borrow |
| 0 | 1 | 1 | B′ | D = A + B′ + 1 | **subtract** |
| 1 | 0 | 0 | 0 | D = A | transfer A |
| 1 | 0 | 1 | 0 | D = A + 1 | increment A |
| 1 | 1 | 0 | 1 | D = A − 1 | decrement A |
| 1 | 1 | 1 | 1 | D = A | transfer A |

*(Verified against the deck's function table; the "all 1s = −1" rows are the 2's-complement identity
A + 1111 = A − 1.)*
**Note the redundancy:** rows 5 and 8 both give "transfer A" — 3 control bits give 8 combinations but
only 7 distinct operations. Worth knowing; examiners ask why two rows agree.

## 8. Logic microoperations — `settled`

Bit-wise operations on **non-numeric** data — "useful for manipulating individual bits or a portion of
binary data… to change bit values, delete a group of bits, or insert new bit values."

Sixteen logic functions of two variables exist; four are implemented in practice: **AND (∧), OR (∨),
XOR (⊕), complement (′)**. From these, everything else.

**The three named applications (this is what gets examined):**

| Operation | Mechanism | Worked example |
|---|---|---|
| **Selective set** | `A ← A ∨ B` — 1s in B **force** the corresponding A bits to 1 | A = 1010, B = 1100 → A = 1110 |
| **Selective complement** | `A ← A ⊕ B` — 1s in B **toggle** the corresponding A bits | A = 1010, B = 1100 → A = 0110 |
| **Mask (selective clear)** | `A ← A ∧ B` — **0s in B clear** the corresponding A bits; 1s let them through | A = 1010, B = 1100 → A = 1000 |

**Insert = mask then OR** — the deck's two-step recipe: first **AND** with a mask to clear the target
field, then **OR** in the new value. *Worked:* to put 1001 into the high nibble of A = 1101 0110 →
mask: A ∧ 0000 1111 = 0000 0110 → insert: ∨ 1001 0000 = **1001 0110**.

**Clear** is `A ⊕ B` with A = B → all zeros (a test for equality: XOR gives 0 exactly when equal).

## 9. Shift microoperations — `settled`

Three kinds. **What distinguishes them is entirely what enters at the vacated serial input.**

| Type | RTL | Serial input | Use |
|---|---|---|---|
| **Logical** | `shl`, `shr` | **0** | unsigned data, bit manipulation |
| **Circular (rotate)** | `cil`, `cir` | **the bit shifted out the other end** | no information lost — rotate |
| **Arithmetic** | `ashl`, `ashr` | `ashr`: **the sign bit is replicated**; `ashl`: 0 in | signed ×2 / ÷2 |

Examples: `R2 ← shr R2`, `R3 ← cil R3`.

**Mechanism — why arithmetic shift is different.** In 2's complement, shifting right divides by 2 and
shifting left multiplies by 2 — but only if the **sign is preserved**. So `ashr` copies the sign bit
into the MSB (sign extension) rather than shifting in 0; shifting in 0 would turn a negative number
positive. For an n-bit register with sign Rₙ₋₁:

- `ashr`: Rₙ₋₁ is **unchanged** and also copied into Rₙ₋₂; everything else shifts right.
- `ashl`: 0 enters at the right. **Overflow** occurs if the sign bit changes — i.e. if Rₙ₋₁ ≠ Rₙ₋₂
  *before* the shift, because the bit about to be shifted into the sign position differs from the
  sign. That overflow test is `V = Rₙ₋₁ ⊕ Rₙ₋₂`. (`settled`; standard Mano result.)

⚠ `ashr` of an odd negative number rounds **toward −∞**, not toward zero: −5 ashr 1 = −3, not −2.
`misconceptions.md` M5.

**Hardware:** a combinational shifter built from a MUX per bit position (select = shift/no-shift and
direction) — the barrel shifter of `../../04-digital-electronics` unit 02.

## 10. Arithmetic Logic Shift Unit (ALSU) — `settled`

**The deck's closing slide is an exam question: "Design a 4-bit ALU that may perform the following
operations. Explain its working in detail."** Treat this as the single most likely U1 exam item.

**Structure — one stage, replicated n times:**

```
             ┌──────────────────────┐
   Aᵢ ──┬───→│  arithmetic circuit  │──→ Dᵢ ──┐
   Bᵢ ──┤    │  (FA + 4-to-1 MUX)   │         │      ┌─────────┐
        │    └──────────────────────┘         ├─────→│ 4-to-1  │
        │    ┌──────────────────────┐         │      │  MUX    │──→ Fᵢ
        └───→│    logic circuit     │──→ Eᵢ ──┤      │ S₁ S₀   │
             └──────────────────────┘         │      └─────────┘
   Aᵢ₊₁ ──────── shift right input ───────────┤          ▲
   Aᵢ₋₁ ──────── shift left  input ───────────┘          │
                                                    S₃ S₂ select
```

- **S₃, S₂** select which of four blocks reaches the output: arithmetic, logic, shift-right,
  shift-left.
- **S₁, S₀** (plus **Cᵢₙ**) select *which* arithmetic or logic operation within the block.
- Total: **4 select lines + Cᵢₙ**.

**Operation count (`settled`):** with S₃S₂ = 00 the arithmetic circuit's S₁S₀ + Cᵢₙ give **8**
operations; S₃S₂ = 01 the logic circuit's S₁S₀ give **4** (AND, OR, XOR, complement);
S₃S₂ = 10 gives **shift right**; S₃S₂ = 11 gives **shift left**. **8 + 4 + 1 + 1 = 14 operations.**

**ALSU function table — `settled` (corrected 2026-09-15).** The professor's ALSU slide (deck 1 p. 32)
and Mano Table 4-8 both print this ordering, which is **not** the §7 arithmetic-circuit ordering:

| S₃ | S₂ | S₁ | S₀ | Cᵢₙ | Operation | Function |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | F = A | transfer A |
| 0 | 0 | 0 | 0 | 1 | F = A + 1 | increment A |
| 0 | 0 | 0 | 1 | 0 | F = A + B | addition |
| 0 | 0 | 0 | 1 | 1 | F = A + B + 1 | add with carry |
| 0 | 0 | 1 | 0 | 0 | F = A + B′ | subtract with borrow |
| 0 | 0 | 1 | 0 | 1 | F = A + B′ + 1 | subtraction |
| 0 | 0 | 1 | 1 | 0 | F = A − 1 | decrement A |
| 0 | 0 | 1 | 1 | 1 | F = A | transfer A |
| 0 | 1 | 0 | 0 | × | F = A ∧ B | AND |
| 0 | 1 | 0 | 1 | × | F = A ∨ B | OR |
| 0 | 1 | 1 | 0 | × | F = A ⊕ B | XOR |
| 0 | 1 | 1 | 1 | × | F = A′ | complement A |
| 1 | 0 | × | × | × | F = shr A | shift right A into F |
| 1 | 1 | × | × | × | F = shl A | shift left A into F |

**Why it differs from §7, mechanically:** this table is what you get when the arithmetic stage's
4-to-1 MUX is wired **input 0 → 0, 1 → B, 2 → B′, 3 → 1** (check: S₁S₀ = 00 gives A + 0 + Cᵢₙ = transfer
or increment; 11 gives A + 1111 = A − 1, or A with Cᵢₙ = 1). §7's standalone circuit is wired B, B′, 0, 1.
Both are correct *for their own wiring*. **When answering the ALSU question, use this table and draw
the MUX with this wiring** — the professor's slide is this table. Before 2026-09-15 this section and
`study-pack/03` wrongly reused §7's ordering for the ALSU (`CHANGELOG.md`, `misconceptions.md` M24).

**Mechanism worth saying out loud:** the ALSU computes *all* candidate results in parallel, every
cycle, and the select lines merely choose which one is allowed out. Hardware does not "decide then
compute" — it computes everything and discards. That is the deep reason control is just *selection*,
and it is the idea U2's control unit is built on.

## 11. Definitions, generations, computer types, bus standards — added 2026-09-15

Added after Assignment 1 (Q1, Q3, Q5, Q13) asked for material this unit did not yet hold. Sources in
`sources.md` §"2026-09-15 additions".

**Definitions.**
- **Digital computer** (Mano ch. 1): "a digital system that performs various computational tasks. The
  word *digital* implies that the information in the computer is represented by variables that take a
  limited number of discrete values." `settled`.
- **Computer** (Hamacher §1): "a fast electronic calculating machine that accepts digitized input
  information, processes it according to a list of internally stored instructions, and produces the
  resulting output information." `settled`.
- **Microarchitecture** = computer organization (§1): the implementation of an ISA — datapath, control,
  pipelining, caches. `settled`.
- **Microoperation** (§7), **RTL** (§5). `settled`.

**Generations of computers.** Date boundaries **vary by author by a few years** (`contested` as to exact
years; the *technology* per generation is `settled`). Stating "approximately" is the honest form.

| Gen | ≈ Period | Switching technology | Landmark machines / advances | People |
|---|---|---|---|---|
| 1 | 1945–1956 | vacuum tubes; machine language; magnetic drum / delay-line memory | ENIAC (operational end-1945, 18,000+ tubes); von Neumann's *First Draft of a Report on the EDVAC* (1945) = stored-program concept; Manchester Baby ran the first stored program (21-Jun-1948); UNIVAC I (1951, first widely known commercial computer) | J. Presper Eckert & John Mauchly (ENIAC, UNIVAC); John von Neumann (stored program); Tom Kilburn & F. C. Williams (Manchester) |
| 2 | 1956–1964 | discrete **transistors** (point-contact transistor, Bell Labs, Dec 1947); magnetic-core memory; assembly + first high-level languages | TX-0 (1956, first general-purpose transistorized computer); IBM 7090; **FORTRAN** shipped 1957 | John Bardeen, Walter Brattain, William Shockley (transistor; 1956 Nobel); John Backus (FORTRAN) |
| 3 | 1964–1971 | **integrated circuits** (SSI/MSI); operating systems, multiprogramming | IBM System/360 (1964, one architecture across a 50:1 performance range — the architecture/organization split made commercial); RCA Spectra 70 (1966, first large commercial IC computers) | Jack Kilby (IC demonstrated 1958); Robert Noyce (monolithic planar IC patent 1959) |
| 4 | 1971–≈1980s | **LSI → VLSI**; the **microprocessor** (CPU on one chip); personal computers | Intel 4004 (1971, 4-bit, ~2,300 transistors); Altair 8800 (1975); Apple II (1977); IBM PC (1981) | Ted Hoff & Stanley Mazor (4004 concept); Federico Faggin & Masatoshi Shima (4004 implementation) |
| 5 | ≈1980s– | ULSI, massively parallel processing, AI-oriented design | Japan's **Fifth Generation Computer Systems** project (MITI/ICOT, 1982–1994: parallel inference machines, logic programming) | — (national programme; "fifth generation" is a label, not a single technology break) |

**Types of computers.** "In how many ways are computers divided" has **no single textbook count** —
there are three standard axes (`likely` as a framing; each category's content `settled`):

| Axis | Classes |
|---|---|
| **By size / capability** (Hamacher §1.1, the prescribed reference) | personal (desktop) · portable notebook · workstation (high-res graphics, engineering use) · enterprise system / mainframe (business data processing) · server (large databases, many access requests) · supercomputer (large-scale numerical: weather forecasting, aircraft simulation) |
| **By data representation** | analog (continuous quantities) · digital (discrete values — Mano's definition) · hybrid (both) |
| **By purpose** | general-purpose (stored program, any task) · special-purpose / embedded (fixed task) |
| **By Flynn's streams** | SISD · SIMD · MISD · MIMD (U4 §3) |

**Bus: definition and role** (§6 + standard). A bus is a shared set of wires connecting several
sources to several destinations, time-shared so only one source drives it at once. A **system bus**
has three functional groups: **data lines** (the word), **address lines** (which memory location or
I/O port), **control lines** (read/write, timing, interrupt, bus request/grant). Role: replace n(n−1)
point-to-point links with one shared path.

**Named bus standards** (for "list five popular bus structures"; `settled` facts, Tier 2–3 sources):

| Bus | Year | Character |
|---|---|---|
| **ISA** (Industry Standard Architecture) | 1981 (8-bit PC), 1984 (16-bit PC/AT) | IBM PC expansion bus |
| **EISA** (Extended ISA) | 1988 | 32-bit, ISA-compatible; clone-vendor answer to IBM's MCA |
| **VESA Local Bus (VLB)** | 1992 | 32-bit, runs at processor local-bus speed; short-lived (i486 era) |
| **PCI** (Peripheral Component Interconnect) | 1992 | processor-independent parallel bus, 32-bit at 33 MHz; dominant by the mid-1990s |
| **SCSI** (Small Computer System Interface) | ANSI X3.131 | parallel bus for disks/peripherals |
| **USB** (Universal Serial Bus) | 1996 | serial, hot-pluggable peripheral bus |
| **PCI Express (PCIe)** | 2003 | serial point-to-point *links* replacing PCI/AGP — "bus" in name only (stage-2 §) |

Hamacher 5e §4.7 ("Standard I/O Interfaces") treats **PCI, SCSI and USB** as its three examples.

---

## Worked-problem patterns for this unit

1. **Compare architecture vs organization** (6-row table) / von Neumann vs Harvard / RISC vs CISC.
2. **Write RTL** for a stated transfer, including the control function.
3. **Bus sizing:** "how many MUXes of what size to bus k registers of n bits?" → n MUXes, k-to-1.
4. **Arithmetic-circuit table:** given S₁S₀Cᵢₙ, state the microoperation (and vice versa).
5. **Logic microoperation application:** mask / insert / selective-set on given bit patterns.
6. **Shift:** apply logical vs circular vs arithmetic shift to a given register; detect `ashl`
   overflow via Rₙ₋₁ ⊕ Rₙ₋₂.
7. **Design and explain a 4-bit ALSU** — the deck's own question (F4 in `exam-map.md`).

## Confidence summary

`settled`: architecture/organization split · five functional units · von Neumann/Harvard · RISC/CISC
characteristics · RTL notation · n(n−1) interconnect and the bus fix · MUX sizing rule · arithmetic
circuit table · selective set/complement/mask/insert · the three shift types and the arithmetic-shift
sign rule · ALSU structure and the 14-operation count.
`likely`: the exact operation count depends on the specific ALSU drawn — 14 is Mano's standard
4-select-line design; a differently-drawn ALSU gives a different count, so **derive it, don't recite
it**.
Unverified / not claimed: per-technology gate delays; any specific commercial ALU part number.

> **Stage 2 for this unit:** `stage-2/01-architecture-fundamentals-and-rtl.md` — why the
> stored-program idea is the whole of computability in hardware, carry-propagation limits and why
> ripple-carry bounds the ALU's clock, the barrel-shifter/crossbar connection, Amdahl's framing of
> the bottleneck, and where the "architecture vs organization" line actually blurs.
