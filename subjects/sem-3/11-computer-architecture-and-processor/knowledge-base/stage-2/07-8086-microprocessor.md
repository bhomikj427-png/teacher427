# U7 — The 8086 Microprocessor — STAGE 2 (deep structure)

> Extends `../07-8086-microprocessor.md`.

---

## §A. Why segmentation? The design pressure, and the bug that became an ABI

**The constraint.** Intel wanted ≥ 1 MB of address space (20 bits) on a machine whose registers, ALU and
data bus were **16 bits**. Four options existed:

| Option | Cost | Chosen? |
|---|---|---|
| **32-bit registers** | doubles register file, ALU and bus width; far more transistors and pins than 1978 economics allowed | no |
| **Bank switching** (a paging register selecting a window) | software must constantly reload the bank register; addresses are not linear; awful for compilers | no |
| **Segmentation** (base register × 16 + 16-bit offset) | 16-bit registers keep working; four simultaneous windows; a program ≤ 64 KB per segment needs **no** address arithmetic at all | **yes** |
| **A flat 20-bit address in a 24-bit register** | odd word size, wasteful | no |

**Why ×16 specifically.** The shift must reconcile 16 bits with 20, so the segment base is shifted by
**4** bits. That makes segment bases land every **2⁴ = 16 bytes** — a "paragraph". A larger shift would
waste address space in coarser granularity; a smaller one would not reach 1 MB. **20 − 16 = 4 is forced
by the arithmetic**, not chosen.

**What segmentation bought (and this is the part usually omitted):** four segment registers mean a
program has **four simultaneously addressable 64 KB windows** (code, data, stack, extra) with **no
address computation** — small programs are genuinely simpler than on a flat machine, because "near"
pointers are 16 bits. The cost is that anything crossing 64 KB needs "far" pointers and **segment
arithmetic**, which is why C compilers of that era had `near`/`far`/`huge` pointer models and why this
period is remembered with distaste.

### The A20 wraparound — a hardware quirk that became a permanent compatibility fixture — `settled`

**The mechanism.** The 8086 has exactly **20 address lines (A0–A19)**, so any computed address above
1 MB **wraps to zero** — the 21st bit simply does not exist. Concretely, `FFFF:0010` computes
0xFFFF × 16 + 0x10 = 0xFFFF0 + 0x10 = **0x100000** = 1,048,576, one byte past 1 MB. On the 8086/8088
that address **wraps to 0x00000** — so `FFFF:0010` is equivalent to `0000:0000`.

**Why it mattered.** A number of commercial software packages — intentionally or otherwise — **relied on
that wraparound.** Then the **80286** arrived with 24 address lines, and in real mode it **did not
wrap**: `FFFF:FFFF` produced linear 0x10FFEF and *stayed* there instead of wrapping to 0x0FFEF. Software
depending on the wrap broke.

**The fix, which is gloriously ugly.** IBM, in the original PC/AT, used **spare lines in the keyboard
controller** to gate the **A20 line** — forcing it low to emulate the 8086's wrap. Hence the **"A20
gate"**: a switch that makes a newer CPU misbehave exactly like an older one. Enabling A20 became a
mandatory boot-time ritual for operating systems for the next **thirty years**.

A side effect: with A20 enabled, the first 0xFFEF bytes above 1 MB (0x100000–0x10FFEF) become reachable
from real mode — the **High Memory Area (HMA)**, which DOS exploited to move itself out of conventional
memory.

**★ Why this belongs in a Stage-2 file and not as trivia.** It is the cleanest case study in the course
of an **architectural contract being set by an implementation accident.** The wraparound was not a
documented feature; it was a consequence of having 20 pins. Programs depended on the observable
behaviour, so it *became* part of the architecture, and every subsequent chip had to reproduce it. **This
is U1 big idea 1 failing in the real world: anything programs can observe becomes architecture, whether
you meant it or not.** Compare Spectre (U4 stage-2 §E) — the same lesson, 40 years later, with higher
stakes.

## §B. ModR/M: how variable-length decoding actually works, and what it costs

Stage 1 gives the MOD/REG/r-m tables. The structural insight is about **decoding**, and it is the whole
RISC/CISC argument in one mechanism.

**An 8086 instruction is self-describing, byte by byte:**

```
byte 1   opcode + D + W        → tells you whether a ModR/M byte follows
byte 2   MOD REG r/m          → MOD tells you whether 0, 1 or 2 displacement bytes follow
byte 3-4 displacement          → the opcode + W tell you whether 1 or 2 immediate bytes follow
byte 5-6 immediate
```

**★ Therefore instruction length is only known after partially decoding the instruction** — and the
*next* instruction's address depends on this instruction's length. **Consequences:**

1. **Decoding is inherently serial.** You cannot find instruction boundaries in parallel: to know where
   instruction n+1 starts you must decode instruction n. Contrast **RISC-V**, where every instruction is
   4 bytes and the boundaries are known **before any decoding at all** (U8 §5).
2. **You cannot decode k instructions per cycle naively.** A superscalar x86 must either speculatively
   try to decode from *every* byte offset (expensive, and real x86 decoders do variants of this) or
   cache the decoded results. **This is why modern x86 has a micro-op cache / decoded-instruction
   cache** — it lets the machine skip the expensive length-determination on hot code entirely.
3. **The cost is asymmetric.** Variable length gives excellent **code density** (an instruction is as
   short as it needs to be — good for the instruction cache, U6). It costs **decode complexity and
   power.** RISC makes the opposite trade. Neither is simply right; ARM's **Thumb** and RISC-V's **C
   extension** reintroduce 16-bit instructions precisely because code density turned out to matter after
   all.

**The `[BP]`-cannot-be-encoded quirk (Stage 1 §5) is a symptom of the same pressure:** the encoding has
exactly 8 r/m patterns per MOD value and someone had to give one up for direct addressing. **Encoding
space is a scarce resource, and CISC ISAs are full of these scars.** (Compare U2 stage-2 §A: the BC
overloading opcode 111.)

## §C. The 8086's pipeline, honestly assessed

Stage 1 calls the BIU/EU overlap "pipelining", quoting the source. Correct, but the depth is worth
stating precisely:

- It is a **2-stage** pipeline (fetch | execute) with a **6-byte buffer** between the stages, not a
  classic k-stage pipeline with a register per stage.
- The **queue decouples** the stages, which is what makes the overlap robust to variable instruction
  length and variable execution time. A fixed-depth pipeline could not absorb an instruction taking 83
  clocks (AAM); a **buffer** can.
- **Every hazard from U4 is visible in it:**
  - **control hazard** → the queue is **flushed** on JUMP/CALL, and the EU waits (Stage 1 §2);
  - **structural hazard** → "the instruction execution cycle is never broken for fetch operation" — the
    EU has bus priority, so prefetch happens only in free cycles. That is an **arbitration rule
    resolving a structural hazard**;
  - **no data hazard in the U4 sense**, because there is no overlap *between* instructions' execution —
    only between one's fetch and another's execution.

**★ The generalizable insight:** a **queue between pipeline stages is an elasticity mechanism.** Rigid
pipelines require every stage to take the same time; a buffer lets a fast producer run ahead of a slow
consumer. This is the same idea as a FIFO in any producer/consumer system, and it reappears in modern
CPUs as issue queues, store buffers and reservation stations.

## §D. Why x86 survived — the honest economic answer

The technical case against x86 is strong (§B): serial decoding, register starvation (8 GPRs vs RISC's
32), segmentation, condition codes, variable length. It nevertheless won the desktop and server market.
**The reason is not technical.**

1. **Binary compatibility is an economic moat.** The installed base of x86 binaries — much of it with no
   surviving source — meant a new machine that couldn't run them had no market. Intel could not abandon
   the ISA, and competitors could not enter without cloning it.
2. **Volume funded process leadership.** High unit volume paid for fabrication processes a generation
   ahead of competitors, and a process advantage can outweigh an architectural disadvantage.
3. **The ISA was decoupled from the implementation.** From the **Pentium Pro (1995)** onward, x86 chips
   **decode CISC instructions into RISC-like micro-operations** and execute those out-of-order. The
   external contract stayed CISC; the internal engine became RISC.
4. **Intel's own attempt to leave failed.** Itanium (IA-64, VLIW) was a clean-sheet design; it did not
   displace x86, and **x86-64 — designed by AMD as an extension rather than a replacement — won
   instead.** The market chose compatibility over cleanliness, twice.

**★ The lesson to teach, and it is a genuine architecture lesson, not a business aside:** an ISA is a
**contract with an installed base**, and contracts have inertia proportional to the value of what is
built on them. **Architecture is partly an economic artifact.** That is also precisely why RISC-V's
openness is strategically significant (U8) — it attacks the moat rather than the technology.

**Where the technical case did win:** phones and embedded systems had **no legacy binaries**, so ARM
took them completely — and Apple's move from x86 to ARM shows the moat erodes once binary translation
becomes good enough. **Compatibility is a moat, not a wall.**

## §E. Cross-topic unification

- **The 8086's queue flush = U4's pipeline flush on a control hazard.** Identical mechanism.
- **The 8086 is microprogrammed (U3)**, which is what makes 1–6-byte instructions and 83-clock
  instructions affordable. A hardwired control unit for this ISA would be enormous — **U3's argument,
  instantiated**.
- **Isolated I/O (`IN`/`OUT`, 64 KB port space) is U5 §2's second bus organization**, and its immunity to
  compiler reordering is the advantage noted in U5 stage-2 §C.
- **Segmentation is *not* virtual memory** (U6 §6) — a critical distinction. 8086 segments provide no
  **protection**, no **translation table**, and no **presence bit**; they are pure base-plus-offset
  address *formation*. Protected segmentation (with descriptors, limits and privilege) arrives with the
  **80286**. Conflating the two is a real misconception; flag it if the learner does.
- **BCD/ASCII adjust instructions (`DAA`, `AAA`, `AAM`)** rest on packed/unpacked BCD from
  `../../04-digital-electronics` U1 (BCD adder, +6 correction). `DAA` **is** the +6 correction in one
  instruction — ask the learner to connect them.
- **`SHR`/`SAR`** are exactly U1 §9's logical vs arithmetic shift, and `RCL`/`RCR` are the BC's
  `CIR`/`CIL` (rotate through E, where E is the carry). **The BC's E flip-flop is the 8086's CF.**

## §F. Frontier (`evolving`)

- **x86-64** widened registers to 64 bits, added 8 more GPRs (16 total), and **made segmentation vestigial
  in 64-bit mode** (CS/DS/ES/SS bases forced to 0 — flat addressing at last). Segmentation, the defining
  feature of U7, is effectively **dead** in modern 64-bit code, surviving only for FS/GS as
  thread-local-storage base pointers.
- **Micro-op caches and decoded-instruction caches** are now standard, precisely because of §B.
- **x86 is under real pressure for the first time** — Apple Silicon, ARM servers (Graviton), and RISC-V.
  Whether the moat holds is an open question; state it as open.
- **APX / AVX-512** continue the "extend, never break" pattern that defines the architecture.

## §G. Harder problems (the §0 surplus test)

1. Compute the physical address for `1234:5678`, and then find **three different** seg:offset pairs that
   name the same byte. Prove there are exactly 4096 such pairs for a typical address, and characterize
   the addresses for which there are fewer.
2. Why exactly ×16 and not ×256 or ×4? Derive the shift from the requirement "20-bit address from 16-bit
   registers" and state what each alternative would cost.
3. On an 8086, what does `MOV AX, [FFFF:0010]` read? Explain via the 20-line wraparound, then explain
   what an 80286 in real mode does differently and what the A20 gate does about it.
4. An instruction is `8B 47 0A`. Decode it fully: opcode, D, W, MOD, REG, r/m, displacement — and give
   the assembly, the addressing mode, and the default segment. (`8B` = MOV, D=1, W=1.)
5. Explain why an x86 decoder cannot determine instruction boundaries in parallel, and estimate the
   work required to decode 4 instructions per cycle by brute force from a 16-byte window.
6. `[BP]` with no displacement is unencodable. Show which encoding slot it would need and what occupies
   it. Then explain why the assembler's workaround costs one byte and how often that matters.
7. The 8086's queue refills only when **2 bytes** are free, the 8088's when **1** is. Derive both rules
   from the respective bus widths, and explain why the 8087 must know which CPU it is attached to.
8. Write an 8086 ALP to add two 32-bit numbers stored in memory, using `ADC`. Then explain why `ADC`
   exists at all on a 16-bit machine — and what RISC-V does instead (hint: it has no carry flag).
9. Argue both sides of "the 8086's segmentation was a good design decision", given 1978 constraints and
   1993 hindsight.

## Confidence

`settled`: the segmentation design rationale and the forced ×16 shift · **the 20-line wraparound,
`FFFF:0010` ≡ `0000:0000` on the 8086/8088, the 80286's non-wrap, the keyboard-controller A20 gate, and
the HMA at 0x100000–0x10FFEF** (all verified this session) · ModR/M self-describing length and the serial
decoding consequence · the 2-stage queue-decoupled pipeline and its hazard mapping · Pentium Pro (1995)
as the start of internal micro-op decoding · x86-64 flattening segmentation.
`likely`: the specific claim that "a number of commercial packages relied on the wraparound" —
documented but not enumerable · the four-option design-space table in §A (a reconstruction of the
rationale, not a quotation of Intel's deliberations) · the economic argument in §D (well-supported, but
an interpretation rather than a measurement).
`evolving`: x86's competitive position — genuinely open, recheck on re-entry; do not teach an outcome.
