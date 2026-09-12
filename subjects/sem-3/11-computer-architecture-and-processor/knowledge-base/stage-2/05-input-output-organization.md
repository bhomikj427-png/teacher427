# U5 — Input–Output Organization — STAGE 2 (deep structure)

> Extends `../05-input-output-organization.md`.

---

## §A. The real constraint is latency, not throughput

Stage 1 presents the transfer modes as a ladder of decreasing CPU involvement — a **throughput**
argument. The deeper design driver for most systems is **latency and its worst case.**

**Derivation — when is polling actually better than interrupts?** Let

- t_int = interrupt overhead (recognize + save state + dispatch + return) ≈ hundreds of cycles,
- t_poll = cost of one poll ≈ a few cycles,
- R = device ready-rate (events/second), and the CPU can poll at rate P.

**Interrupt cost per event** = t_int. **Polling cost per event** = t_poll × (P/R) — i.e. the number of
wasted polls between events.

> **Interrupts win when** t_int < t_poll · P/R — that is, when events are **rare** relative to polling
> frequency.
> **Polling wins when the device is almost always ready** — because then almost no poll is wasted, and
> you avoid t_int entirely.

**★ The non-obvious consequence, which reverses Stage 1's ladder:** for **very fast** devices — 100 Gb
Ethernet, NVMe SSDs — interrupts arrive so often that interrupt overhead dominates, and modern drivers
go **back to polling** (Linux **NAPI**, DPDK, `io_uring` busy-polling). **The ladder is not monotone in
"better"; it is monotone in "device autonomy", and the right rung depends on the event rate.** A learner
who thinks interrupts are simply better than polling will be wrong about every high-performance I/O
system built since about 2010.

**Interrupt latency budget** (the real-time question): worst-case latency =
longest non-interruptible instruction + interrupt-disable windows in the OS + dispatch. This is why
(a) the 8086 makes `REP` string operations interruptible mid-sequence, and (b) real-time kernels bound
the length of critical sections. **Throughput analysis never reveals this; only worst-case analysis
does.**

## §B. DMA and cache coherence — the problem Stage 1 cannot see

Stage 1's DMA is correct for the BC's world: one memory, no cache. **Add a cache (U6) and DMA becomes a
correctness problem, not just a performance one.**

**The two failure modes:**

| Direction | What goes wrong | Mechanism |
|---|---|---|
| **Device → memory** (input) | the CPU reads **stale** data | DMA writes new data into DRAM; the CPU's cache still holds the **old** copy of those lines and answers the read from cache |
| **Memory → device** (output) | the device reads **stale** data | with a **write-back** cache, the CPU's newest data is still **dirty in cache** and has not reached DRAM; the device reads the old DRAM contents |

**The fixes, in increasing sophistication:**

1. **Mark DMA buffers non-cacheable.** Simple, and costs performance on every CPU access to the buffer.
2. **Explicit software flush/invalidate** around each transfer — the classic embedded approach
   (`dma_sync_single_for_device` / `..._for_cpu` in Linux). Correct but easy to get wrong; a missing
   flush is a notoriously intermittent bug.
3. **Bus snooping / hardware coherence.** The cache controller watches bus transactions and
   invalidates or writes back lines that a DMA touches. This is what desktop/server chipsets do, and it
   is why DMA "just works" on x86 but must be managed by hand on many microcontrollers.

**★ This is the clearest example in the course of a layering violation:** two features (caching and DMA)
each correct in isolation, jointly incorrect. Stage 1 teaches them in separate units and never puts
them in the same room. **Put them in the same room** — it is exactly the kind of cross-topic question
that separates understanding from recall.

## §C. Memory-mapped I/O and the compiler problem

Stage 1 gives the isolated-vs-memory-mapped trade in hardware terms. There is a **software** consequence
that is invisible at Stage 1 and bites every embedded programmer.

A memory-mapped device register is an address that
- **changes without the program writing it** (a status register set by hardware), and
- **has side effects when read or written** (reading a FIFO *consumes* a byte).

An optimizing compiler assumes neither. It will happily:
- hoist a load out of a polling loop (`while (*STATUS == 0);` becomes an infinite loop because the value
  is cached in a register),
- **eliminate** a "redundant" second write to the same address,
- **reorder** independent-looking accesses.

**The fix is `volatile`** — which tells the compiler that every access must happen, exactly as written,
in order. And `volatile` is **not enough** on a machine with a weakly-ordered memory model: you also need
**memory barriers** to prevent the *hardware* reordering the accesses. **Isolated I/O (IN/OUT) sidesteps
all of this**, because I/O instructions are not memory accesses and are never optimized away — which is
a real advantage of the 8086's scheme that Stage 1's table does not list.

## §D. Priority interrupts, generalized

Stage 1 gives daisy-chain vs parallel priority. Two deeper points:

**(a) It is the same mechanism as bus arbitration** (U1 stage-2 §D): serial ripple (position = priority,
cheap, slow) vs centralized parallel (fast, programmable, more wires). **Learn once, apply twice.**

**(b) Priority inversion.** A nested-interrupt scheme with masking creates a classic failure: a
low-priority handler holds a resource that a high-priority handler needs, so the high-priority work is
blocked by low-priority work — **priority inversion**. The standard cures (priority inheritance,
priority ceilings) belong to real-time systems, but the *hazard* is created here, by the interrupt
architecture. Worth one sentence: **a priority scheme that can block its own highest level is not
actually prioritized.**

**(c) Modern shape.** Daisy chains are gone; the descendants are the **APIC** (x86) and **GIC** (ARM) —
programmable interrupt controllers with per-source priority, affinity (which core), and
**message-signalled interrupts (MSI/MSI-X)** in which a device "raises an interrupt" by *writing a
message to an address* rather than asserting a wire. **Note what that means: interrupts became memory
writes** — the isolated/memory-mapped distinction collapsing in the other direction.

## §E. Cross-topic unification

- **Handshaking (U5) = the flag protocol (U2 §9) = a two-phase commit.** FGI/FGO *are* a handshake with
  the handshake lines implemented as flip-flops the program can test.
- **DMA requires tri-state bus drivers** (`../../04-digital-electronics` U5) — the concrete reason
  three-state logic exists.
- **The IOP is a second processor with its own program in shared memory** — the first appearance of
  multiprocessing in the course, and structurally a **shared-memory MIMD** system (U4 §3). Mano
  introduces MIMD in ch. 9 and then builds one in ch. 11 without naming it.
- **The autonomy ladder is a recurring pattern:** poll → interrupt → delegate → offload. It reappears as
  CPU → DMA → IOP → GPU → SmartNIC/DPU. **The same ladder, 60 years apart.**

## §F. Frontier (`evolving`)

- **IOMMU.** A DMA-capable device can write **anywhere** in physical memory — which makes any malicious
  or buggy device a total compromise (the class of attacks called DMA attacks, e.g. over Thunderbolt).
  The **IOMMU** interposes address translation on device accesses, giving devices their own restricted
  address spaces. **It is virtual memory (U6) applied to devices**, and it retro-fixes a security hole
  that Stage 1's DMA model has by design.
- **Polling's return.** NAPI, DPDK, SPDK, `io_uring` — see §A.
- **DPUs / SmartNICs** — the IOP idea, scaled to a full programmable CPU complex on the network card.

## §G. Harder problems (the §0 surplus test)

1. A device delivers one word every 1 μs. Programmed I/O costs 8 instructions per word at 4 ns each;
   an interrupt costs 300 ns of overhead per word; DMA costs one memory cycle (50 ns) per word plus
   2 μs of setup per 1000-word block. **Compute the CPU time consumed per 1000 words by each mode** and
   rank them. Now redo it for a device delivering one word every 50 ns and explain the reversal.
2. Derive the break-even condition between polling and interrupts from §A, and solve it for the event
   rate at which they tie, given t_int = 300 ns, t_poll = 5 ns, P = 10⁶ polls/s.
3. A driver does: `memcpy(buf, data, n); start_dma_out(buf, n);` on a system with a **write-back**
   cache and **no** snooping. Explain precisely what the device transmits and why. Give two fixes.
4. A device sets a status bit; the code is `while (*(int*)0xF000 == 0) ;`. It hangs at -O2 but works at
   -O0. Explain, and fix it. Then explain why your fix is still insufficient on a weakly-ordered CPU.
5. Show that a daisy-chain priority interrupt with n devices has worst-case acknowledge latency
   proportional to n, and design the parallel scheme that removes it. Count the wires in each.
6. Construct a concrete priority-inversion scenario using two interrupt levels and one shared buffer.
7. In the BC, the interrupt return address goes to **M[0]** and IEN is cleared. Design the minimum
   extension permitting **nested** interrupts, and state what new failure becomes possible.
8. Why is an IOMMU "virtual memory for devices"? Map each virtual-memory component (page table, TLB,
   fault) onto its IOMMU counterpart.

## Confidence

`settled`: the polling-vs-interrupt break-even argument and the modern return to polling (NAPI/DPDK are
documented designs) · the two DMA-coherence failure modes and the three standard fixes · the
`volatile`/barrier problem · daisy-chain ≡ bus arbitration · priority inversion as a structural hazard
of masked nested interrupts · IOMMU as device-side address translation.
`likely`: specific overhead figures used in the problems (illustrative, not measured on any particular
machine) · the claim that x86 DMA is always snoop-coherent (true for normal memory; there are
exceptions).
`evolving`: DPU/SmartNIC trends and IOMMU-bypass attack research — recheck on re-entry.
