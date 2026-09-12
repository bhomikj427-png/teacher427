# U4 — Parallel Processing & Pipelining — STAGE 2 (deep structure)

> Extends `../04-parallel-processing-and-pipelining.md`.

---

## §A. Amdahl's law — the hard ceiling on everything in this unit

Stage 1 gives S ≤ k for a pipeline. **Amdahl's law is the more general and more brutal bound**, and it
governs parallel processing as well as pipelining.

**Setup.** Let **f** be the fraction of a program's execution time that can be sped up, and **s** the
speedup applied to that fraction. The unimproved fraction (1 − f) takes the same time as before.

> **S_overall = 1 / [ (1 − f) + f/s ]**

**Limit as s → ∞:**

> **S_max = 1 / (1 − f)**

**Read that.** If 10% of a program is inherently serial, then **no amount of parallel hardware —
infinite cores, infinite pipeline depth — can give more than a 10× speedup.** The serial fraction is an
absolute wall.

**Worked, to make it bite:**

| f (parallelizable) | s = 10 | s = 100 | s → ∞ |
|---|---|---|---|
| 0.50 | 1.82× | 1.98× | **2×** |
| 0.90 | 5.26× | 9.17× | **10×** |
| 0.95 | 6.90× | 16.8× | **20×** |
| 0.99 | 9.17× | 50.3× | **100×** |

**Why this belongs in U4 and not a footnote:** it explains, in one formula, (a) why adding cores stops
helping, (b) why the pipeline-fill overhead (k − 1)/n matters at small n, and (c) why architects chase
the *serial* fraction rather than the parallel one. It also generalizes Stage 1's speedup formula —
the pipeline result S → k is Amdahl with f = 1 and s = k.

**The honest counterweight (`settled`):** **Gustafson's observation** — in practice, users given a
faster machine solve a **larger** problem rather than the same problem faster, and the serial fraction
often does **not** grow with problem size. So Amdahl bounds *fixed-size* (strong) scaling; Gustafson
describes *scaled* (weak) scaling. **Both are right about different questions.** Teaching only Amdahl
leaves a learner unable to explain why supercomputers are useful.

## §B. Dependences: RAW, WAR, WAW — and why only one is real

Stage 1 says "data hazard: an instruction needs a result not yet available." There are actually
**three** kinds of register dependence, and they are not equally fundamental.

| Name | Pattern | Example | Is it a *true* dependence? |
|---|---|---|---|
| **RAW** (read after write) — *true dependence* | i writes r, j reads r | `ADD r1,…` then `SUB …,r1` | **YES** — information genuinely flows |
| **WAR** (write after read) — *anti-dependence* | i reads r, j writes r | `ADD …,r1` then `MOV r1,…` | **no** — an artifact of reusing a name |
| **WAW** (write after write) — *output dependence* | i writes r, j writes r | `MOV r1,…` then `ADD r1,…` | **no** — an artifact of reusing a name |

**★ The deep point:** WAR and WAW are **name conflicts, not data conflicts.** No value flows between
the instructions; they merely happen to use the same register *name*. Give each write a fresh name and
the dependence vanishes:

```
   before renaming            after renaming
   ADD r1, r2, r3             ADD p1, p2, p3
   MOV r1, r5       ← WAW     MOV p4, p5        ← no dependence at all
```

**This is register renaming**, and it is why out-of-order processors have far more *physical* registers
than *architectural* ones. **Only RAW dependences are irreducible** — they encode actual dataflow, and
no hardware can remove them (only forwarding can shorten them).

**Consequence for Stage 1's cures:** forwarding addresses **RAW**. Renaming eliminates **WAR/WAW**. The
two cures are aimed at different problems, which is why a machine needs both.

## §C. Deeper pipelines: the derivation, and the Pentium 4 lesson

**Why deeper looks better.** If combinational work totalling T is split into k equal stages, each stage
takes T/k, so the clock period is T/k + tᵣ (register overhead) and

> **f_clock = 1 / (T/k + tᵣ)**

As k → ∞, f_clock → 1/tᵣ. **Frequency appears to grow without bound** — which is exactly the reasoning
that produced the deep-pipeline era.

**Why it fails.** Three costs grow with k:

1. **Register overhead dominates.** Once T/k ≈ tᵣ, half the clock period is spent on latches doing no
   useful work. Throughput per watt collapses.
2. **Branch misprediction penalty grows linearly in k.** A mispredict flushes the whole pipeline, so
   the penalty is ~k cycles. Combined with a mispredict rate m and branch frequency b, the average
   CPI penalty is **b · m · k** — *linear in depth*. Deep pipelines are only viable with very accurate
   prediction.
3. **Power.** Dynamic power ≈ **α·C·V²·f** — linear in frequency, and higher frequency demands higher
   voltage for timing closure, so power grows roughly as f³ in the regime that matters.

**The historical verification (`settled`):** Intel's NetBurst microarchitecture used a **20-stage**
pipeline in **Willamette/Northwood**, then **31 stages** in **Prescott**, explicitly to reach higher
clock frequencies — "the deep 20-stage pipeline allowed for higher frequencies by reducing the
complexity of each stage." It ran into exactly the costs above: a longer mispredict recovery, and heat.
**Intel abandoned the deep-pipeline strategy** and returned to a shorter, wider design (the Core line).
**The clock-frequency race ended around 2004–2005 and has not resumed.** This is the empirical answer
to "would a 12-stage pipeline be 12× faster?" — *no, and the industry proved it at scale and at cost.*

## §D. Branch prediction, properly

Stage 1 lists "branch prediction" as one of five cures. Its mechanism deserves more, because **modern
performance depends on it more than on almost anything else.**

**Static prediction:** always-not-taken (simplest — just keep fetching), always-taken, or
backward-taken/forward-not-taken (BTFNT — exploits the fact that loop branches jump **backwards** and
are usually taken). Costs nothing; accuracy maybe 60–70%.

**Dynamic — 1-bit predictor:** store the last outcome per branch; predict the same again. **Failure
mode:** a loop executed repeatedly mispredicts **twice** per entry — once on the final iteration
(loop exits, predictor said taken) and once on re-entry (predictor now says not-taken). For a
10-iteration inner loop run many times, that is ~20% misprediction on a branch that is 90% taken.

**Dynamic — 2-bit saturating counter:** four states (strongly/weakly not-taken, weakly/strongly taken);
a prediction must be wrong **twice** to flip. This fixes the loop case — the single exit mispredict
only weakens the counter, so re-entry still predicts taken. **One extra bit removes half the
mispredicts**, which is why 2-bit is the textbook baseline.

**Correlating / two-level predictors** index a table by the **global history** of recent branches as
well as the branch address, capturing correlations between branches (`if (a) … if (a && b) …`). Modern
predictors (TAGE-class, perceptron-based) exceed **95–99%** accuracy on typical code.

**Why accuracy matters so much:** with penalty k ≈ 20 and branch frequency b ≈ 20%, going from 90% to
99% accuracy changes the CPI penalty from 0.2 × 0.10 × 20 = **0.4** to 0.2 × 0.01 × 20 = **0.04** — a
**tenfold** reduction in wasted work. **Prediction accuracy, not pipeline depth, is what made deep
pipelines survivable at all.**

## §E. Speculation and its security cost — `evolving`

Speculative execution — running instructions past an unresolved branch and discarding them if the guess
was wrong — is the logical end of §D. Architecturally, discarded work is invisible: registers and
memory are never committed.

**But it is not invisible microarchitecturally.** Speculatively executed loads **leave data in the
cache**. **Spectre** and **Meltdown** (disclosed 2018) exploit exactly this: induce a mispredicted
branch, speculatively access memory the program may not read, and then recover the value through a
**cache timing side channel** — even though the speculative instructions were "never executed."

**Why this belongs in this unit:** it is the precise point where the architecture/organization
distinction (U1 big idea 1) **breaks**. Pipeline depth, branch prediction and caching were all supposed
to be invisible implementation details. They are not. **Performance techniques from this unit created a
class of vulnerability that spans the entire industry**, and mitigations (fencing, flushing predictors
across contexts, disabling some speculation) **cost real performance** — the first time in decades that
architects deliberately gave performance back.

## §F. Where Flynn's taxonomy breaks

Stage 1 notes pipelining doesn't fit Flynn. Two more failures:

- **SIMT (GPUs).** An NVIDIA/AMD GPU runs one instruction across a *warp* of threads — SIMD-like — but
  each thread has its **own program counter and can diverge** at a branch (the hardware serializes the
  divergent paths). It is neither clean SIMD nor MIMD. Vendors call it **SIMT** (single instruction,
  multiple threads) precisely because Flynn has no box for it.
- **Modern superscalar out-of-order cores** issue several *different* instructions per cycle from one
  stream onto multiple units — multiple instructions, multiple data, one program. Flynn would call it
  SISD, which tells you nothing useful.

**The honest assessment:** Flynn (1966) classifies by stream *count* and was designed before ILP,
pipelining, vector units and GPUs. It remains a useful **vocabulary** and an exam staple, but it is not
a modern taxonomy. Teach it as a historical framework with known gaps — not as the truth about parallel
machines. **That is exactly the protocol's "never teach a live debate as a closed fact."**

## §G. Cross-topic unification

- **The structural hazard (one memory port) is the von Neumann bottleneck (U1 §3), and the cure — split
  instruction/data memory — is the Harvard architecture.** Same fact, three names across two units.
- **Forwarding is a bypass path; the BTB is an associative memory (U6 §3); the loop buffer is a
  cache.** U4's cures are U6's structures, applied early.
- **The 8086's BIU/EU overlap is a 2-stage instruction pipeline, and its queue flush on JUMP is a
  control-hazard pipeline flush** (U7 §2). U4 is the theory; U7 is the first real instance.
- **RISC-V's fixed-length, load-store, no-condition-code design is a direct response to every hazard
  in this unit** (U8 §5). U4 supplies the *why* for U8's *what*.
- **Delayed branch and delayed load are compiler fixes to hardware problems** — the RISC thesis
  (complexity moves to the compiler) in miniature.

## §H. Harder problems (the §0 surplus test)

1. A program is 25% inherently serial. You are offered (a) 4 cores, (b) 1000 cores. Compute the
   speedup of each via Amdahl. Explain to a manager why (b) is barely better than (a).
2. Derive f_clock = 1/(T/k + tᵣ) and find the k that **maximizes throughput** when the mispredict
   penalty is k cycles, branch frequency b, mispredict rate m. Show that an optimum exists and that it
   **decreases** as m rises.
3. Classify each dependence in this sequence as RAW/WAR/WAW, then rename registers to eliminate every
   removable one:
   `ADD r1,r2,r3 / SUB r2,r1,r4 / MUL r1,r5,r6 / ADD r7,r1,r2`
4. A 1-bit predictor on a loop with n iterations, executed m times: derive the total number of
   mispredictions. Repeat for a 2-bit saturating counter. At n = 10, m = 100, compute both.
5. The Stage-1 FP-adder example has segment delays 60/70/100/80 ns. **Re-balance** it into 4 segments
   of near-equal delay (you may split the 100 ns stage). Recompute tₚ and the speedup. What does this
   tell you about where pipeline design effort goes?
6. Explain how Meltdown extracts a value that was **never architecturally read**. Identify precisely
   which U4 and U6 mechanisms it composes.
7. Argue whether a GPU is SIMD or MIMD, then explain why the question is malformed.
8. With forwarding, a 5-stage pipeline still stalls **one cycle** on a load-use dependence. Explain why
   forwarding cannot remove this one, unlike an ALU-to-ALU dependence.

## Confidence

`settled`: Amdahl's law and its limit · Gustafson's counterweight · RAW/WAR/WAW and the renaming
argument · the f_clock derivation and the three costs of depth · **NetBurst 20 stages
(Willamette/Northwood) → 31 stages (Prescott)**, verified, with the stated frequency rationale ·
1-bit vs 2-bit predictor failure modes · Spectre/Meltdown (2018) as cache-timing side channels on
speculation · SIMT as outside Flynn.
`likely`: specific modern predictor accuracy figures (95–99%) — design- and workload-dependent · the
2004–2005 date for the end of the frequency race (widely documented, approximate).
`evolving`: speculative-execution security — active research, recheck on re-entry.
