# U6 — Memory Organization — STAGE 2 (deep structure)

> Extends `../06-memory-organization.md`.

---

## §A. The three C's — a classification that tells you what to *change*

Stage 1 teaches hit ratio as a single number. **Hill and Smith (1989)** partition misses into three
classes, and the value of the partition is that **each class points at a different fix.**

| Class | Definition (Hill & Smith) | Cause | **What fixes it** |
|---|---|---|---|
| **Compulsory** (cold) | caused by referencing a **previously unreferenced** memory block | the first touch of any data | **larger blocks**, prefetching. **Cannot be removed** by size or associativity — the data has to arrive once |
| **Capacity** | not compulsory, and misses **both** in the target cache **and** in a fully-associative cache of equal capacity with LRU | the program's working set exceeds the cache | **a bigger cache** (or a program with a smaller working set) |
| **Conflict** | not compulsory, **hits** in a fully-associative cache of equal capacity with LRU, but **misses** in the target cache | "because of the restriction in the address mapping and not because of lack of space" | **more associativity**, or a victim cache, or changing the data layout |

**★ Why the definitions are operational, not just descriptive.** Each class is defined by a *simulation
experiment*: run the reference stream against a fully-associative LRU cache of the same capacity. Misses
there but not compulsory = **capacity**. Hits there but misses in your cache = **conflict**. **This is
how associativity is actually evaluated** — it isolates the penalty attributable to the mapping
function alone.

**Diagnostic use, which is the real payoff:** a learner told "my cache hit rate is 85%, what do I do?"
cannot answer. A learner who asks "which of the three C's dominates?" can:
- mostly **compulsory** → bigger blocks / prefetch (size and associativity are wasted money);
- mostly **capacity** → more capacity;
- mostly **conflict** → more associativity (and note Stage 1's M14: direct-mapped caches have
  **only** conflict misses available to fix, because they have no choice of placement).

## §B. AMAT as a recurrence — the multi-level hierarchy

Stage 1's formula covers one cache level. Real hierarchies have three. The correct generalization is a
**recurrence**, and it is where the concept of a **local** vs **global** miss rate becomes necessary.

> **AMAT = t_L1 + m_L1 · (t_L2 + m_L2 · (t_L3 + m_L3 · t_mem))**

where mᵢ is the **local** miss rate of level i (misses at level i ÷ **accesses to level i**), *not* the
fraction of all CPU references.

**★ The distinction that trips everyone:** L2's *local* miss rate looks terrible (often 40–50%) because
L2 only ever sees requests L1 already failed on — a pre-filtered, hard stream. Its **global** miss rate
(misses ÷ *all CPU references*) = m_L1 · m_L2, which is small. **Quoting a local miss rate as if it were
global makes a good cache look broken.**

**Worked:** t_L1 = 1 cycle, m_L1 = 0.05; t_L2 = 12, m_L2 = 0.40; t_L3 = 40, m_L3 = 0.30; t_mem = 250.

```
AMAT = 1 + 0.05 × (12 + 0.40 × (40 + 0.30 × 250))
     = 1 + 0.05 × (12 + 0.40 × 115)
     = 1 + 0.05 × 58
     = 3.9 cycles
```

Note what this shows: **a 5% L1 miss rate costs nearly 3 cycles on top of a 1-cycle hit.** The hierarchy
is doing enormous work, and the memory latency (250 cycles) is still visible in the third decimal place
of every access. That is the memory wall, quantified.

## §C. Why associativity has diminishing returns

Stage 1 presents the direct → set-associative → fully-associative spectrum. The empirical shape of that
spectrum is the design fact:

- 1-way → 2-way: **large** improvement (removes most conflict misses).
- 2-way → 4-way: **modest**.
- 4-way → 8-way: **small**.
- 8-way → fully associative: **negligible for most workloads**.

**The mechanism.** Conflict misses require **≥ 2 hot blocks mapping to the same set**. Doubling
associativity halves the probability that k hot blocks collide beyond capacity, so the *remaining*
conflict misses shrink roughly geometrically — while the **cost** grows roughly **linearly** in ways
(one comparator and one tag-read per way, plus a wider mux and worse hit latency).

> **Benefit decays geometrically; cost grows linearly. Therefore an optimum exists at low associativity
> — typically 4–16 ways.** That is why no real cache is fully associative except tiny ones (TLBs,
> victim caches), which is exactly what Stage 1 observes without explaining.

**The classic rule of thumb** (`likely` — a heuristic, not a law): *a direct-mapped cache of size 2N has
about the same miss rate as a 2-way set-associative cache of size N.* Useful for arguing "should I spend
transistors on capacity or associativity?" — and it says: **capacity, usually.**

## §D. LRU is approximated, never implemented

Stage 1 lists LRU as a replacement policy. In hardware it is essentially **never** exact for
associativity > 4.

**Why:** true LRU on an n-way set requires a total order over n items, i.e. ⌈log₂(n!)⌉ bits of state per
set — 5 bits for 4-way, **16 bits for 8-way** — updated **on every hit**, in the critical path. The
update logic, not the storage, is what kills it.

**What is actually built:**

| Approximation | Mechanism | Cost |
|---|---|---|
| **Pseudo-LRU (tree-based)** | a binary tree of 1-bit "go left/right" flags; a hit flips the bits along its path away from itself | **n − 1 bits** per set; trivial update |
| **NRU / clock** | one "recently used" bit per line, cleared periodically; evict any line with the bit clear | 1 bit per line |
| **Random** | no state at all | 0 bits — and **surprisingly competitive**, within a few percent of LRU |
| **RRIP / SHiP** (modern) | predict re-reference *interval*, not recency — resists thrashing from streaming data | more state, better on scans |

**★ The honest point that matters pedagogically:** Stage 1's "FIFO, LRU, random" is a *conceptual*
taxonomy. Real caches use **pseudo-LRU or a re-reference predictor**, and **random is not a joke** — it
is a legitimate choice, because it never has a pathological worst case, whereas LRU thrashes completely
on a cyclic access pattern one block larger than the set. **LRU's failure mode is total; random's is
average.**

## §E. The memory wall — the number behind the whole unit

**The trend (`settled` as a direction, figures `likely`):** CPU performance grew roughly 50%/year for
decades while DRAM **latency** improved only ~7%/year. Bandwidth improved far faster than latency,
because bandwidth can be bought with parallelism (more banks, wider buses, more channels) while
**latency is bounded by physics** — charge transfer, sense-amplifier settling, and signal propagation.

**Consequence:** the gap compounds. A main-memory access that cost a few CPU cycles in 1980 costs
**hundreds** today. Everything in this unit — multi-level caches, prefetching, out-of-order execution
(U4), multithreading — exists to **hide** a latency that has not improved.

**The deeper structural point:** the hierarchy does not make memory faster. **It makes memory *appear*
fast for programs with locality, and does nothing at all for programs without it.** A pointer-chasing
workload with no locality runs at DRAM latency no matter how much cache you buy. **Caching is not a
speedup; it is a bet, and the bet is on the program's behaviour.** That is the single most important
sentence in U6, and Stage 1 can only gesture at it.

## §F. The page-size trade-off, derived

Stage 1 gives page sizes of 64–4096 words without saying why the number is contested.

**Larger pages:**
- ✅ **smaller page table** (fewer entries for the same address space),
- ✅ **more TLB reach** (TLB entries × page size = bytes covered — the figure that actually matters),
- ✅ fewer page faults for sequential access, and more efficient disk transfers (amortized seek),
- ❌ **more internal fragmentation** (the unused tail of the last page of every allocation),
- ❌ **longer transfer time** per fault, and more wasted I/O if only part is used.

**Smaller pages:** the reverse.

**Why "huge pages" (2 MB, 1 GB) exist in modern systems:** TLB reach. With 4 KB pages, a 1536-entry TLB
covers only 1536 × 4 KB ≈ **6 MB** — far less than a database's working set, so large-footprint
applications miss in the TLB constantly and pay a page-walk on each miss. **2 MB pages raise the same
TLB's reach to ~3 GB.** So the modern answer is not one page size but **multiple simultaneous sizes**,
which is precisely why Stage 1's "pages are fixed-size" is a simplification worth flagging.

## §G. Cross-topic unification

- **Cache index/tag and U3's microprogram mapping (`0xxxx00`) are the same operation:** split an
  identifier into "which slot" + "what's left over". Teach them together and the second is free.
- **The TLB is an associative memory (U6 §3) used as a cache (U6 §4) of a page table.** Three concepts,
  one structure. Similarly the **BTB** (U4) is a CAM, and the **loop buffer** is a cache.
- **Virtual memory is the memory hierarchy applied between main memory and disk**, with page faults as
  misses, page tables as tags, and replacement policies as replacement policies. **Cache and virtual
  memory are the same design pattern at two scales** — the differences (hardware vs OS handling, ns vs
  ms penalty) follow from the 10⁵× difference in miss cost, not from different principles.
- **The IOMMU (U5 stage-2 §F) is this machinery applied to devices.**
- **SRAM vs DRAM** rests on `../../03-electronic-devices-1` (MOSFET physics, leakage, charge storage) and
  the SRAM cell / butterfly SNM analysis already in
  `../../04-digital-electronics/knowledge-base/stage-2/05-…`. **Reuse; do not re-derive.**

## §H. Frontier (`evolving`)

- **The end of Dennard scaling (~2005)** means transistors no longer get proportionally more
  power-efficient as they shrink, so caches can't simply grow. Area now trades against power budget.
- **Emerging non-volatile memory** (MRAM, ReRAM, PCM, FeFET) threatens to blur the main/auxiliary
  boundary that Stage 1 treats as fundamental — byte-addressable persistent memory makes "load from
  disk" an anachronism. Shared frontier with
  `../../04-digital-electronics/knowledge-base/stage-2/05-…` — keep both in sync.
- **3D-stacked / HBM memory** attacks **bandwidth** by stacking DRAM on or beside the die. Note it does
  **not** fix latency (§E) — which is exactly why it helps GPUs (throughput machines) far more than
  latency-sensitive CPUs.
- **CXL and disaggregated memory** add another hierarchy tier between local DRAM and storage.

## §I. Harder problems (the §0 surplus test)

1. A 64 KB, 4-way set-associative cache with 32-byte blocks on a 32-bit byte-addressed machine. Derive
   the tag/index/offset split **from first principles** (state every step). Then recompute for the same
   capacity as (a) direct-mapped, (b) fully associative, and explain how the tag width moves.
2. Using §A's definitions, design an experiment that separates the three C's for a given program. What
   two simulations do you need, and what does each difference measure?
3. A program strides through an array with stride exactly equal to the cache size. Show that a
   direct-mapped cache has a **0%** hit rate and that 2-way associativity fixes it. Which C is this?
4. Given the §B recurrence, compute AMAT; then compute the **global** miss rate of L2 and L3 and explain
   why L2's local rate of 0.40 is not alarming.
5. Show that exact LRU on an 8-way set needs ⌈log₂(8!)⌉ = 16 bits, and design a tree-based pseudo-LRU
   using 7 bits. Give an access sequence where they choose **different** victims.
6. Construct an access pattern on which **LRU performs worse than random**. Explain what property of
   LRU you exploited.
7. A system has 1536 TLB entries. Compute TLB reach for 4 KB, 2 MB and 1 GB pages. For a database with
   a 40 GB working set, which page size makes TLB misses negligible, and what does it cost in
   fragmentation?
8. Argue that cache and virtual memory are the same design pattern; then list every design decision the
   10⁵× difference in miss penalty forces to differ (hardware vs software handling, associativity,
   write policy, replacement sophistication).
9. Write-back caches complicate DMA (U5 stage-2 §B). Would a write-through cache eliminate **both**
   coherence failure modes, or only one? Prove it.

## Confidence

`settled`: the three C's with Hill & Smith's operational definitions (verified) · the AMAT recurrence
and the local/global miss-rate distinction · the geometric-benefit/linear-cost argument for limited
associativity · exact-LRU bit count ⌈log₂(n!)⌉ and tree pseudo-LRU at n−1 bits · the page-size trade-off
and the TLB-reach calculation · cache ≡ virtual memory as one pattern at two scales.
`likely`: the "2N direct-mapped ≈ N 2-way" rule of thumb (a heuristic) · the ~50%/yr CPU vs ~7%/yr DRAM
latency figures (widely cited, directionally solid, exact values vary by source and era) · specific
TLB-entry counts (design-dependent).
`evolving`: Dennard-scaling end (~2005), emerging NVM, HBM/3D stacking, CXL — dated 2026, recheck on
re-entry per protocol §10.
