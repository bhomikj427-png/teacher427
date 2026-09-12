# U3 — Control Unit & Microprogrammed Control — STAGE 2 (deep structure)

> Extends `../03-control-unit-and-microprogrammed-control.md`.

---

## §A. The origin, and what Wilkes actually proposed — `settled`

Microprogramming was proposed by **Maurice Wilkes** in a paper titled **"The Best Way to Design an
Automatic Calculating Machine"**, delivered at the **Manchester University Computer Inaugural
Conference in July 1951** (proceedings pp. 16–18). It is the first presentation of the idea.

**What he proposed, and why it is cleverer than Stage 1 suggests:** a machine with a **variable
instruction set**, in which the programmer could *assemble micro-operations into any instruction the
machine was inherently capable of executing* — so "a machine's instruction repertoire could be altered
from day to day as its applications vary." His implementation mechanism was a **diode matrix** —
**essentially what we now call ROM.**

The **EDSAC 2** (1958) was the first microprogrammed computer, using a control ROM made from magnetic
cores. The 7-year gap is the honest part of the story: **the idea preceded the memory technology that
made it cheap.** Microprogramming only became dominant when ROM became denser and faster than random
logic — i.e. it won for **technological**, not purely logical, reasons. That framing matters, because
the same reasoning **reversed** when RAM/logic economics changed again (§D).

## §B. The real design axis: horizontal vs vertical microprogramming

Stage 1 gives Mano's format (F1 F2 F3 CD BR AD) without naming the axis it sits on. **This is the
central design decision in microprogramming.**

| | **Horizontal** | **Vertical** |
|---|---|---|
| Encoding | **one bit per control signal** (unencoded) | **encoded fields**, decoded at run time |
| Word width | **very wide** (100s of bits) | narrow (Mano: 20 bits) |
| Parallelism | **maximum** — any combination of microoperations at once | **limited** — one microoperation per field |
| Decoding | **none needed** — bits drive control lines directly | needs decoders (Mano: three 3×8) |
| Speed | faster (no decode delay) | slower by one decode level |
| Control memory size | large | **small** |
| Microprogram length | shorter (more work per microinstruction) | longer |

**Mano's design is vertical**, with a **partially horizontal** flavour: three independent fields give
**up to 3 parallel microoperations**, which is more than pure vertical (1) and far less than horizontal
(any subset).

**★ The derivation that makes the trade concrete.** Suppose a machine has **N distinct control
signals**.
- **Horizontal:** width = N bits; expressible combinations = **2^N**.
- **Vertical with k fields** of width ⌈log₂(mᵢ+1)⌉ each (mᵢ microoperations in field i):
  width = Σ⌈log₂(mᵢ+1)⌉; expressible combinations = **Π(mᵢ+1)** — vastly fewer.

For Mano: 3 fields × 3 bits = 9 bits encode 7+7+7 = 21 microoperations, giving 8×8×8 = **512**
combinations. Horizontal encoding of 21 signals would need **21 bits** but allow **2²¹ ≈ 2 million**
combinations. **Vertical buys a 2.3× narrower field and loses 4000× the parallelism** — and the
designer's judgement is that the lost combinations were mostly meaningless anyway (you never want
`AC ← AC + DR` and `AC ← 0` simultaneously).

**That last point is the real insight:** the grouping of microoperations into fields is not arbitrary.
**Operations that conflict** (all write AC) are placed in the **same** field, so the encoding makes
conflict *unrepresentable*. Operations that are usefully concurrent (`DR ← M[AR]` and `PC ← PC + 1`)
are placed in **different** fields. **The field structure encodes the machine's conflict graph.** Ask a
learner why READ is in F2 and INCPC in F3 and you are asking them to see this.

**Nanoprogramming** (a third level, `settled` as a concept): a two-level store — microinstructions
point into a **nanostore** of wide horizontal words. Common microinstruction patterns are stored once
in the nanostore and referenced many times, giving horizontal speed with vertical size. Used in the
Motorola 68000. **It is just compression of a repetitive microprogram.**

## §C. The sequencer, and why address sequencing is the hard part

Stage 1 gives the four capabilities and the input logic. The deeper point: **generating the next
address is most of the cost of a microprogrammed control unit.**

The microoperation fields are trivial — decode and drive. But the next-address logic must support
in-line, conditional branch, mapping and subroutine return, each with a different source, and must do
it **within one control-memory cycle** so there is no bubble. Hence:

- the **CDR / pipeline register** (Stage 1 §1) exists precisely to overlap *this* address computation
  with the *previous* microinstruction's execution — **the control unit is itself pipelined**, and it
  is U4's idea appearing one level down;
- the **SBR is only one word deep** in Mano's design, so **microsubroutines cannot nest**. That is the
  same single-word-return-address flaw as BSA (U2 stage-2 §C), one abstraction level lower. Real
  microsequencers use a small **stack** of return addresses (typically 4–16 deep).

**Ask the learner:** "can INDRCT call another microsubroutine?" The answer (no — SBR would be
overwritten) links three units in one question.

## §D. Why RISC abandoned microcode — the honest argument

Stage 1 quotes "most RISC machines use hardwired control." The reasoning, in the order it actually
happened:

1. **Microcode won in the 1960s–70s because ROM was faster than main memory.** A microinstruction
   fetch from control ROM cost far less than an instruction fetch from core memory, so *implementing*
   a complex instruction in microcode was nearly free relative to the memory access it saved. Dense
   CISC instructions **reduced program size**, which mattered when memory was the scarcest resource.
2. **Caches destroyed that advantage.** Once an instruction cache ran at core speed, a sequence of
   simple instructions from cache was **as fast as** a microcoded complex instruction from control ROM.
   The economic premise of microcode evaporated.
3. **Measurement showed compilers didn't use the complex instructions.** The RISC studies found
   compilers emitted a small subset of the available instruction set; the rest was silicon spent on
   instructions nobody generated.
4. **So spend the silicon differently:** simple instructions + hardwired control + **registers and
   pipelining**.

**The correct causal statement is therefore: the cache killed microcode, not RISC ideology.** A learner
who can say that understands both units. (And note the honesty requirement: microcode did **not**
disappear — §E.)

## §E. Where microcode survives — `settled`

Microcode is alive in modern x86, and knowing where sharpens the whole unit:

- **Simple instructions are hardwired.** `ADD`, `MOV` and the common cases decode directly into 1–4
  micro-ops by fixed logic.
- **Complex/rare instructions are microcoded.** String operations, `CPUID`, transcendental legacy FP,
  and system instructions trap to a microcode ROM sequencer. This is Wilkes' escape hatch, kept for
  exactly the cases where hardwiring would cost more area than it saves time.
- **"Microcode updates" are real and shipped.** Intel and AMD distribute patchable microcode loaded by
  the BIOS/OS at boot into a **writable control store** — exactly Mano's WCS / dynamic
  microprogramming. **This is how Spectre/Meltdown and errata mitigations were deployed to already-sold
  chips.** It is the clearest possible demonstration of the Stage-1 advantage ("no hardware changes
  needed") paying off 70 years after Wilkes proposed it.

**Teaching note:** this is the single most motivating fact in the unit. A learner who thinks
microprogramming is a historical curiosity should be told that their laptop loads a microcode patch
every time it boots.

## §F. Cross-topic unification

- **Hardwired vs microprogrammed = compute vs look up.** The same trade appears as: combinational logic
  vs ROM-based function generation (`../../04-digital-electronics`: implementing a function with gates
  vs with a PROM/PLA), and as calculation vs memoization in software. **One idea, three vocabularies.**
- **The control unit's D·T product terms (U2) and the microinstruction's F-fields (U3) specify the same
  control signals.** Hardwired = the equation; microprogrammed = the truth table stored.
- **Mapping (`0xxxx00`) is a hash function** — opcode → routine address, with 2 bits of slack for
  collision-free spacing. Compare directly with **cache index/tag** (U6 §4): both split an identifier
  into "which slot" and "what's left over." Teaching them together makes the second one nearly free.
- **CDR = pipelining the control unit** (U4); **SBR's single word = BSA's single word** (U2).

## §G. Frontier (`evolving`)

- **Microcode as an attack surface.** Because the control store is writable and signed, microcode
  update integrity is a security boundary; researchers have demonstrated microcode reverse-engineering
  and, on some parts, unauthorized modification. An active area — recheck on re-entry.
- **FPGA overlays and soft processors** revive Wilkes' variable-instruction-set idea literally: the ISA
  itself is reconfigurable, which is also the argument for RISC-V's custom-extension space (U8).

## §H. Harder problems (the §0 surplus test)

1. Mano's control memory is 128 × 20 = 2560 bits. Compute the width and total size of a **horizontal**
   control store for the same 21 microoperations + CD + BR + AD. Which is smaller, and by how much?
   Now compute the **microprogram length** in each case for the fetch routine.
2. The F-field grouping makes conflicting microoperations unrepresentable. Identify a **pair of
   microoperations in different fields that would conflict** if issued together, and say what hardware
   prevents it (or whether the microprogrammer must simply avoid it).
3. Mano's SBR is one word. Write a microprogram that **breaks** because of this, and specify the
   minimum change to fix it.
4. Derive the total number of control-memory words needed if the example machine had **32**
   instructions instead of 16, keeping 4 words per routine. Does the `0xxxx00` mapping still work? What
   must change?
5. `MAP` sets CAR(2-5) ← DR(11-14) and CAR(0,1,6) ← 0. Prove that this allocates exactly 4 words per
   routine and that no two routines overlap. Then design a mapping giving **8** words per routine and
   state the cost.
6. Compare the **latency** of one machine instruction under hardwired vs microprogrammed control for
   the BC's ADD, assuming a control-memory access takes one clock. Where exactly does the extra time
   go, and does the CDR remove it?
7. **Argue the reverse case:** give a scenario in 2026 where microprogramming a *new* design would be
   the right choice. (Candidates: a rarely-used compatibility ISA; an instruction set still being
   specified; anything needing field-updatable behaviour.)

## Confidence

`settled`: Wilkes 1951, the Manchester conference, the diode-matrix/ROM mechanism, EDSAC 2 (1958) as
the first microprogrammed machine · horizontal vs vertical trade and the combination-count derivation ·
nanoprogramming as two-level compression · the cache-killed-microcode causal chain · microcode's
survival in x86 including field-updatable writable control store.
`likely`: Motorola 68000 as a nanoprogramming example (widely stated; not verified to a primary source
this session) · specific microsequencer stack depths (4–16, typical rather than standard).
`evolving`: microcode security research — recheck on re-entry.
