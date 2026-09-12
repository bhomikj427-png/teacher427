# ECE2108 — Known misconceptions & predictable errors

> Feeds the teaching loop's **ACTIVATE** (predict-first), **GUIDE** (minimum hint) and **feedback**
> moves (`../../../../CLAUDE.md`; `research/02 §5`, `research/04`).
>
> **Confidence discipline (protocol §4):** a misconception list is itself a set of claims, and an
> invented-but-plausible misconception is exactly the hallucination the protocol forbids. Each entry
> is marked by **how it was established**:
> - **`observed-in-source`** — a real error found **in the supplied material this session**. The
>   strongest kind: the error is documented, not guessed.
> - **`structural`** — follows necessarily from a genuine ambiguity or asymmetry in the subject
>   matter (two machines with different parameters, a convention that varies between textbooks, an
>   encoding exception). Reliable because the *trap* is verifiable even where the student error rate
>   is not.
> - **`standard`** — widely reported in computer-architecture teaching practice, but **not** sourced
>   to discipline-based education research this session → `uncertain`, flagged to-verify.
>
> **No entry here is asserted as "the common error" on recall alone.** Where the evidence is only
> that the trap exists, the entry says so.

---

## Unit 1 — Architecture fundamentals & RTL

**M1 — "Architecture is the hardware; organization is the performance."** `observed-in-source`
The professor's own Unit-1 deck contains this row in its comparison table. It is **muddled**:
architecture is the *abstraction* (the ISA — a contract), not the hardware, and performance is a
property of the organization **and** the fabrication technology, not a definition of it.
**Teaching move:** reproduce the professor's table if the exam asks for it (it is the examined
framing) but **do not let a learner reason from that row**. Correct framing: architecture = what a
programmer can rely on; organization = how it is delivered. Test with: "two chips run the same
program at different speeds — same architecture or different?" (Answer: same architecture, different
organization.)

**M2 — "`R2 ← R1` is an assignment statement."** `structural` (threshold ★1)
The deepest error in the subject. RTL looks like code, so learners read it as code executed by
something. It is a **hardware specification**: a bus source is selected, a load line is asserted, and
the transfer happens **at a clock edge**. Consequences of the error: the learner cannot do the "design
of BC" derivations at all, and finds simultaneous transfers (`A ← B, B ← A`) impossible to accept.
**Teaching move:** before any design work, ask what two things must be true for `DR ← M[AR]`
(S₂S₁S₀ = 111 **and** LD(DR) = 1). Then ask them to explain why `A ← B, B ← A` is legal in hardware
but broken in software.

**M3 — "CISC is obsolete; RISC won."** `standard` → `uncertain`
x86 is CISC and still dominates desktops and servers. Modern x86 chips decode CISC instructions into
RISC-like micro-operations internally: **CISC architecture, RISC-ish organization.**
**Teaching move:** use it to reinforce big idea 1. The honest statement is "the RISC *argument* became
the default for new ISAs; CISC survived by adopting it underneath." See also M22.

**M4 — "A bus is just a wire / buses make things faster."** `structural`
A bus is a **shared, time-multiplexed** path adopted to avoid O(n²) interconnect — it **trades
parallelism away** to save wires. It makes a system *buildable*, not faster; sharing is precisely what
creates the von Neumann bottleneck (U1 §3) and the structural hazard (U4 §8a).
**Teaching move:** ask "what did we give up by using one common bus instead of n(n−1) direct
connections?" The answer (simultaneity) is the thread to U4.

**M5 — "Arithmetic right shift is the same as dividing by 2, always."** `structural`
For negative odd numbers, `ashr` rounds **toward −∞**, not toward zero: −5 ashr 1 = **−3**, whereas
integer division −5/2 = −2. Also: `ashr` replicates the **sign bit**, `shr` shifts in **0** — using
`shr` on a negative number silently makes it a large positive one.
**Teaching move:** have them shift 1011 (−5 in 4-bit 2's complement) right both ways and interpret
both results.

**M6 — "The ALSU decides which operation to do, then does it."** `structural`
Hardware computes **all** candidate results every cycle and the select lines choose which one is
allowed out. Learners who imagine a decision-then-compute sequence cannot explain why the ALSU's delay
is constant regardless of the operation.
**Teaching move:** ask "when S₃S₂ selects the logic block, what is the arithmetic circuit doing?"
(Answer: computing anyway; its result is discarded.)

## Unit 2 / Unit 3 — the Basic Computer and the control unit

**M7 — ★ "Mano's Basic Computer and Mano's microprogram example are the same machine."**
`observed-in-source` (structural, and **the highest-yield correction in this subject**)
They are **different machines**, and every parameter differs:

| | Basic Computer (ch. 5, U2) | Microprogram example (ch. 7, U3) |
|---|---|---|
| Memory | **4096 × 16** | **2048 × 16** |
| Address bits | **12** | **11** |
| Opcode bits | **3** | **4** |
| Control | hardwired | microprogrammed, 128 × 20 |

Symptom of the error: a learner tries to map the BC's **3-bit** opcode onto the **`0xxxx00`** scheme
(which needs 4 bits), or claims the BC has a control memory.
**Teaching move:** put the two parameter sets side by side **before** starting U3 and ask the learner
to state both from memory at the start of every U3 session. This single table prevents a cascade of
downstream errors.

**M8 — "BSA can be done in one clock cycle."** `structural`
BSA is written `M[AR] ← PC, PC ← AR + 1` but executes in **two** steps (D₅T₄ then D₅T₅), because the
single common bus can carry only one value per clock. A symbolic one-liner is not a one-cycle
operation.
**Teaching move:** ask them to try to schedule it in one cycle and discover the bus conflict
themselves — productive failure (`research/02 §5`).

**M9 — "ISZ's third microoperation happens at T₄."** `observed-in-source`
**The professor's Unit-2 deck contains this typo**, printing `D₆T₄: M[AR] ← DR…` as ISZ's third line
when it must be **`D₆T₆`** — the same deck's own "Complete Computer Description" slide gives D₆T₆.
A single instruction cannot have two different actions at the same time step.
**Teaching move:** an excellent live demonstration of why the engine never teaches a fact off a slide.
Show both slides and let the learner find the contradiction. Logged in `CHANGELOG.md`.

**M10 — "The interrupt is serviced the instant the flag is set."** `structural`
The condition is `T′₀T′₁T′₂(IEN)(FGI + FGO): R ← 1` — the primes mean the interrupt is recognized
**only when none of T₀, T₁, T₂ is active**, i.e. the current instruction is past fetch/decode. That is
how "finish the current instruction first" is built in hardware.
**Teaching move:** ask why the primes are there. The answer — atomicity of the current instruction —
is the whole idea.

**M11 — "Carry and overflow are the same thing."** `structural`
**C** = carry out of the MSB = **unsigned** overflow. **V** = Cₙ ⊕ Cₙ₋₁ = **signed** overflow. They are
independent: adding 0x7F + 0x01 in 8 bits sets **V** (127 + 1 overflows signed) but **not C**; adding
0xFF + 0x01 sets **C** but not V (−1 + 1 = 0 is correct signed).
**Teaching move:** have them compute both examples and read off both flags. Re-used directly in U7 §8
(`JA`/`JB` vs `JG`/`JL`).

## Unit 4 — Parallel processing & pipelining

**M12 — ★ "Pipelining makes each instruction faster."** `structural` (threshold ★5)
Pipelining raises **throughput**, and typically *increases* the latency of any single instruction
(the interface registers add delay tᵣ). The professor's own deck says architects raise throughput
"often at the expense of slight increases in individual task latency."
**Teaching move:** ask "does a 4-stage pipeline make one instruction finish in a quarter of the time?"
(No — it makes four instructions finish in roughly the time of one.) Follow with: "would a 12-stage
pipeline be 12× faster?" (No — segment imbalance, register overhead, and hazards. This is the exam's
favourite trap.)

**M12a — "Speedup equals k."** `structural`
k is the **theoretical ceiling** as n → ∞ *and* assuming tₙ = k·tₚ. Real speedup is lower: the deck's
own worked example gives **3.88 for a 4-stage pipeline**, and the floating-point example gives **2.9
for 4 segments** because the segments are unequal (110 ns vs 320 ns).
**Teaching move:** always ask for the ceiling *and* the actual value, then the gap's cause.

**M13 — "There are exactly four modes of transfer."** `structural` (a genuine textbook ambiguity)
Mano's §11-4 presents **three** (programmed I/O, interrupt-initiated, DMA) and treats the **IOP**
separately in §11-7; summaries of the chapter often say "four", counting the IOP.
**Teaching move:** teach "three modes of transfer, plus the IOP as a further step" — correct under
either convention. **Never assert a bare number.** Same caution as M18 and M21.

## Unit 6 — Memory organization

**M14 — ★ "Direct-mapped caches use LRU replacement."** `structural`
**Direct mapping has no replacement policy at all** — each block may occupy exactly one slot, so there
is nothing to choose. Replacement policies (FIFO, LRU, random) only arise where a block *could* go in
more than one place: associative and set-associative.
**Teaching move:** ask "which policy does a direct-mapped cache use?" and require them to justify the
answer. This is a favourite examiner trap.

**M15 — "There is one formula for average access time."** `structural`
Two conventions are in circulation: **h·tᶜ + (1 − h)·tᵐ** (tᵐ = full time on a miss) and
**tᶜ + (1 − h)·penalty** (penalty = *additional* time). They give different numbers from the same
inputs.
**Teaching move:** require the learner to **state their convention** in the answer. Marks are lost to
an unstated assumption far more often than to arithmetic.

**M15a — "A cache tag is an arbitrary label."** `structural` (threshold ★7)
The tag is **exactly the address bits the index discarded**. Learners who don't see this cannot derive
a bit-split for an unseen configuration — which is the only cache question worth asking.
**Teaching move:** for a 15-bit address and a 512-word cache, ask "how many main-memory words share
one cache slot?" (2⁶ = 64) "so how many bits must you store to tell them apart?" (6 — the tag.)

## Unit 7 — The 8086

**M16 — ★ "The sign flag (SF) is used with unsigned numbers."** `observed-in-source`
**This exact sentence appears in an institutional 8086 reference consulted this session — and it is
wrong.** The same document's own flag table contradicts it ("Sign Flag: set equal to high-order bit of
result"). SF copies the MSB, which is the sign **only under signed (2's-complement) interpretation**;
it is meaningless for unsigned values. The correct division: **CF = unsigned overflow · OF = signed
overflow · SF = signed sign.**
**Teaching move:** genuinely useful as a live demonstration that sources must be read against
themselves. Corrected in `07-8086-microprocessor.md` §3, logged in `CHANGELOG.md`.

**M17 — ★ "Each memory byte has one seg:offset address."** `structural` (threshold ★6)
**Segments overlap.** Because physical = segment × 16 + offset, many different pairs name the same
byte: `0000:0010` and `0001:0000` both give 00010H.
**Teaching move:** ask them to find a second seg:offset for a given physical address. Until they can,
any two-segment-register question will confuse them.

**M17a — "BX and BP behave the same as pointers."** `structural`
**BX defaults to DS; BP defaults to SS.** This is the one asymmetry in an otherwise uniform scheme,
and it is the most-examined detail in 8086 addressing. (*Mechanism:* BP exists to address stack
frames, so defaulting it to SS is what makes local variables work.)
**Teaching move:** ask for the physical address of `[BX]` and `[BP]` with the same offset and
different DS/SS — the results differ.

**M18 — "The 8086 has exactly N addressing modes."** `structural` (convention, not fact)
Institutional sources give **12 in 5 groups**; other textbooks compress to **7 or 8** by folding in
the I/O-port, relative and implied modes. The **mechanisms are settled; the taxonomy is a naming
convention.**
**Teaching move:** teach the 12/5 scheme, and state that the count varies by textbook. Same caution
applies to the instruction-set grouping (7 vs 8). **Do not let the learner memorize a number as if it
were a fact** — CO4 is the highest-target CO and deserves mechanism, not counting.

**M19 — "`LOOP` is a safe for-loop."** `structural`
`LOOP` **decrements CX first**, then tests. If CX = 0 on entry it wraps to FFFFH and the loop executes
**65 536** times. Guard with `JCXZ` before entering.
**Teaching move:** ask what happens when the array length is zero. This is a real bug, not a trivia
question.

**M19a — "You can move memory to memory / load a segment register with a constant."** `structural`
Both are illegal: `MOV [DI], [SI]` (the instruction format has only one r/m field) and
`MOV DS, 1000H`. Both need a general register as an intermediary.
**Teaching move:** have them write the two-instruction workaround from memory; it recurs in every ALP.

## Unit 8 — RISC-V

**M20 — "Open ISA means the chips are free / open-source."** `structural`
**Open** means the *specification* is freely usable without licence fees. Implementations may be
entirely proprietary and sold commercially. **The contract is open; the implementation need not be.**
**Teaching move:** tie straight to big idea 1 — this is architecture-vs-organization with a legal
dimension.

**M21 — "RISC-V has six instruction formats."** `observed-in-source` (spec wording)
The **ratified specification** says **four core formats (R/I/S/U)** plus **two variants (B/J)** that
differ only in immediate handling. Six layouts exist, but "six core formats" misquotes the standard.
**Teaching move:** teach the phrase "**four core formats plus two immediate variants — six in
total**", which is correct under either phrasing of the question.

**M22 — "RISC beat CISC."** `standard` → `uncertain` (see also M3)
x86 still dominates desktops and servers; **binary compatibility is an economic moat.** What RISC won
is the design *argument* — every new ISA since is a load-store, fixed-length register machine — and
CISC survived by adopting RISC organization underneath (micro-op decoding).
**Teaching move:** the honest closing statement of the course. Ask "if RISC is better, why is your
laptop x86?" and let the answer be economic as well as technical.

**M23 — "The scrambled immediate encoding in B/J is arbitrary/badly designed."** `observed-in-source`
The spec explains it: keeping the sign bit and middle bits (imm[10:1]) **in fixed positions** lets the
sign-extension and immediate-routing hardware be **shared across formats**, instead of "shifting all
bits… left by one in hardware as is conventionally done." **The ISA is optimized for the decoder, not
for the reader.**
**Teaching move:** ask *who* the encoding is designed to be convenient for. The answer reframes the
whole unit.

---

## To-verify (protocol §10 backlog)

- Entries marked `standard` (**M3, M22**) are **`uncertain`**: they are widely repeated in teaching
  practice but were **not** sourced to discipline-based education research this session. *Resolve by:*
  computer-architecture education literature, or by observing this learner. **Do not present them as
  "the common error" — present the correction on its own merits.**
- Entries marked `structural` are reliable in that **the trap provably exists** (verified in the
  sources: two machines with different parameters, a convention that varies, an encoding exception).
  What is **not** verified is *how often learners actually fall into it*. State the distinction
  honestly rather than claiming frequency data that does not exist here.
- Entries marked `observed-in-source` (**M1, M7, M9, M16, M21, M23**) are the strongest: each is an
  error or a precision point **found in the supplied or primary material this session**, with the
  contradiction documented in `CHANGELOG.md` or the unit file.
- **Once teaching begins, replace inference with observation.** Real errors this learner makes are
  first-hand evidence and outrank everything above; log them here with `[observed YYYY-MM-DD]` and
  demote or delete entries this learner never exhibits.
