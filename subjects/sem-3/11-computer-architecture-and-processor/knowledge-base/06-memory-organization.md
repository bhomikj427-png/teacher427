# U6 — Memory Organization (Stage 1)

**Lectures L23–L26 · CO3 · ETE only · ⚠ NO DECK SUPPLIED · L26 (Cache) is `*` practitioner-delivered**

Scope (hand-out): L23 Memory Organization: Memory Hierarchy · L24 Main Memory & Auxiliary Memory ·
L25 Associative Memory · L26 Cache Memory.

Truth authority: **Mano 3e ch. 12**. Built textbook-primary (no deck), verified against a full
institutional reproduction of the chapter carrying Mano's own section numbers and worked numbers.

> **CO3 names cache memory explicitly** ("Explain concepts and impact of **cache memory**, pipelining
> and parallel processing on system performance"), and L26 is handed to an industry practitioner. Cache
> is the centre of gravity of this unit. **Numerical bit-split problems are the examinable core**
> (F20/F21 in `exam-map.md`).

---

## 1. Memory hierarchy — `settled`

The hierarchy runs "from the slow but high-capacity auxiliary memory, to a relatively faster main
memory, to an even smaller and faster cache memory accessible to the high-speed processing logic."

```
            ┌──────────┐   fastest, smallest, costliest per bit
            │  CPU     │
            │ registers│
            ├──────────┤
            │  CACHE   │  ← holds segments of programs currently executing
            ├──────────┤
            │   MAIN   │  ← the only memory that communicates DIRECTLY with the CPU
            │  MEMORY  │
            ├──────────┤
            │ MAGNETIC │  ← backup storage; reached via an I/O processor
            │   DISK   │
            ├──────────┤
            │ MAGNETIC │  ← removable files
            │   TAPE   │
            └──────────┘   slowest, largest, cheapest per bit
```

**Three definitions to keep exact:**

| Term | Definition |
|---|---|
| **Main memory** | the memory unit that **communicates directly with the CPU** (RAM) |
| **Auxiliary memory** | devices providing **backup storage** (disks, tapes) |
| **Cache memory** | a special **very-high-speed** memory used to increase processing speed |

**★ The access relationship that gets examined:** the **CPU has direct access to both cache and main
memory, but NOT to auxiliary memory.** The **I/O processor** manages transfers between auxiliary and
main memory. Programs not currently needed are moved out to auxiliary memory to make room.

**Supporting concepts:**
- **Multiprogramming** — "the existence of 2 or more programs in different parts of the memory
  hierarchy at the same time." Many OSes are designed so the CPU can process several independent
  programs concurrently.
- **Memory management system** — the part of the system that supervises the flow of information
  between auxiliary and main memory.

## 2. Main memory — `settled` (L24)

Built from **semiconductor integrated circuits**. RAM chips come in two operating modes:

| | **Static RAM (SRAM)** | **Dynamic RAM (DRAM)** |
|---|---|---|
| Stores a bit in | **internal flip-flops** | **charge on a capacitor** |
| Refresh | not needed | **needed** — charge leaks |
| Density | lower | higher |
| Speed | faster | slower |
| Cost per bit | higher | lower |
| Used for | cache | main memory |

Most main memory is RAM, but **a portion is ROM**, used to store programs permanently resident and
tables of constants. Specifically, ROM holds the **bootstrap loader** — "function is to start the
computer software operating when power is turned on": it loads a portion of the operating system from
disk into main memory and transfers control to it.

**Mechanism — why the bootstrap must be in ROM:** RAM is volatile, so at power-on there is nothing in
it to execute. The first instructions must come from **non-volatile** storage, wired to appear at the
address the CPU fetches from on reset. (In the 8086 that address is **FFFF0H** — U7 §3 — which is
exactly why the boot EPROM sits at the top of the memory map.)

**RAM and ROM chips.**
- A **RAM chip** uses a **bidirectional data bus with three-state buffers**. Mano's example: capacity
  **128 words × 8 bits**, needing a **7-bit address** and an 8-bit bidirectional data bus, plus RD,
  WR and **two chip-select inputs CS1, CS2**. The unit operates only when **CS1 = 1 and CS2 = 0** (the
  bar over the second select means it is enabled by 0). If the chip is not selected — or is selected
  but neither RD nor WR is enabled — the memory is inhibited and **its data bus is in a
  high-impedance state.**
- A **ROM chip** is organized similarly, but since it can only be read, **the data bus is output-only**.
  Mano's example: **512 bytes**, so **nine address lines**; same CS1 = 1, CS2 = 0 condition.

**Memory address map** — "a pictorial representation of assigned address space for each chip in the
system", listing component (RAM/ROM), the hexadecimal address range, and which address-bus lines
select within it.

**Memory connection to CPU (the worked example — this is an exam pattern):** 512 bytes of RAM (four
128-byte chips) + 512 bytes of ROM.
- Each RAM chip takes the **seven low-order** address lines (to pick 1 of 128 bytes).
- Address lines **8 and 9** go to a **2×4 decoder** whose outputs drive the four RAM chips' CS1 — so
  lines 8–9 pick *which* RAM chip (00 → first, 01 → second, …).
- Address line **10 selects RAM vs ROM**: RAMs when this bit is **0**, ROM when **1**.
- ROM gets address lines **1–9** directly (no decoder).

**The general rule to extract:** **low-order address lines select within a chip; higher-order lines
select which chip** (through a decoder driving chip-selects). That single sentence answers most
memory-interfacing questions.

## 3. Associative memory (CAM) — `settled` (L25)

**The motivating idea:** searching a RAM for a value requires reading and comparing location by
location. "The time required to find an item stored in memory can be reduced considerably if stored
data can be identified for access **by the content of the data itself** rather than by an address."

**Associative memory** = **content-addressable memory (CAM)**: "accessed simultaneously and in
parallel on the basis of data content rather than by specific address or location."

**Cost:** "more expensive than a RAM because **each cell must have storage capability as well as logic
circuits**" for matching. That is the whole trade — you pay a comparator per bit to get a
one-cycle search.

**Hardware organization** — m words × n bits, plus three registers:

| Register | Bits | Job |
|---|---|---|
| **A** — argument register | n | holds the external argument to be matched |
| **K** — key register | n | a **mask** selecting which field of the argument to compare |
| **M** — match register | **m** | one bit per **word**; Mᵢ = 1 if word i matched |

**The matching rule, exactly:** bit Aⱼ is compared with all bits in **column j** of the array **only
if Kⱼ = 1**. For each word i, if **all unmasked bits** of the argument equal the corresponding bits of
word i, then **Mᵢ ← 1**; if one or more unmasked bits differ, **Mᵢ ← 0**. Cell Cᵢⱼ is bit j of word i.

**Why the key register exists (the mechanism students miss):** without a mask you could only search
for a whole word. The key lets you search on a **field** — "find all records whose department field is
X" — by masking out the bits you don't care about. That is what makes a CAM useful rather than just
fast.

**Reading:** all matched words are read **in sequence** by applying a read signal to each word line
whose Mᵢ = 1. If the application guarantees no duplicates, only one word can match, and **Mᵢ can be
used directly as that word's read signal** — a true single-cycle lookup.

**Writing — two cases:**
1. **Load the entire memory** — address each location in sequence. The unit is then "random access
   for writing and content addressable for reading."
2. **Delete unwanted words and insert new ones** — use a **tag register** with one bit per word:
   1 = that word is active/valid, 0 = free. Deleting a word resets its tag bit. To store a new word,
   **scan the tag register for the first 0**, write there, and set the bit.

**Where CAMs actually appear** (and why this lecture precedes cache): the **fully-associative cache**
(§4) and the **associative page table / TLB** (§5) are CAMs. L25 is placed before L26 deliberately.

## 4. Cache memory — `settled` (L26 — the centre of the unit)

### Locality of reference — the entire justification

"Effectiveness of cache mechanism is based on a property of computer programs called **locality of
reference**": references to memory at any given time interval tend to be confined within localized
areas. Most execution time is spent in routines executed repeatedly — loops, nested loops, mutually
calling procedures.

| Kind | Statement | Design consequence |
|---|---|---|
| **Temporal** | "a recently executed instruction is likely to be executed again very soon" | when an item is first needed, **bring it into the cache** — it will be wanted again |
| **Spatial** | references cluster at **adjacent** addresses | don't fetch one word — **fetch a whole block** of neighbours |

**★ These two are not decoration; each one justifies a different design decision.** Temporal locality
justifies *caching at all*; spatial locality justifies *block size > 1*. An exam answer that states
both and links each to its consequence is a complete answer.

**If active segments of a program can be placed in fast cache, total execution time is reduced
significantly.**

### Mano's reference configuration (memorize these numbers — the exam builds on them)

- **Main memory: 32K words × 12 bits** → 32K = 2¹⁵, so a **15-bit address**.
- **Cache: 512 words × 12 bits.** 512 = 2⁹.
- For every word in cache there is a duplicate copy in main memory.
- The CPU sends the 15-bit address to the cache first. **Hit** → CPU takes the 12-bit data from cache.
  **Miss** → the word is read from main memory and then transferred into cache.

### Hit ratio and average access time — `settled`

- **Hit** — the requested word is in cache. **Miss** — it is not.
- **Hit ratio h** = hits / total references.
- **Average access time** = **h·tᶜ + (1 − h)·tᵐ**, where tᶜ = cache access time and tᵐ = the time on a
  miss.

*Worked:* tᶜ = 100 ns, tᵐ = 1000 ns, h = 0.9 → 0.9(100) + 0.1(1000) = 90 + 100 = **190 ns**. Compare
with 1000 ns without a cache: a 5.3× improvement from a 90% hit rate.

**Read the numbers, and you have the real lesson:** the *misses* dominate. At h = 0.9, 10% of accesses
contribute 100 of the 190 ns. Raising h from 0.9 to 0.99 gives 0.99(100) + 0.01(1000) = **109 ns**.
**Small improvements in hit ratio matter enormously** — which is why mapping and replacement policy
are worth designing carefully.

⚠ Some texts define the miss penalty as *additional* time beyond a cache probe, giving
`tᶜ + (1 − h)·penalty`. Both conventions appear. **State your convention in an exam answer.**
(`misconceptions.md` M15.)

### Mapping functions — `settled`

"Correspondence between main memory blocks and those in the cache is specified by a **mapping
function**." Three techniques.

#### (a) Direct mapping

Split the **15-bit** CPU address into two fields:

```
      15-bit CPU address
 ┌──────────────┬──────────────────┐
 │   TAG (6)    │     INDEX (9)    │
 └──────────────┴──────────────────┘
```

- **INDEX = 9 bits** because the cache has 2⁹ = 512 words — *the index is the cache address.*
- **TAG = 15 − 9 = 6 bits** — the bits the index discarded.
- Each cache word stores **data + its tag**.

**Operation:** the index field addresses the cache; the tag from the CPU address is **compared** with
the tag stored there. Match → **hit**. No match → **miss**, read from main memory.

**★ Why a tag is needed at all (threshold ★7):** 2⁶ = 64 different main-memory words share each index.
The index alone cannot say *which* of the 64 is present, so you must store the discarded 6 bits. **The
tag is exactly the part of the address the index threw away.**

**Direct mapping with blocks** — 512-word cache as **64 blocks of 8 words** (64 × 8 = 512):
```
 ┌──────────┬──────────────┬──────────┐
 │ TAG (6)  │  BLOCK (6)   │ WORD (3) │
 └──────────┴──────────────┴──────────┘
```
The index is subdivided: 6 bits of block number + 3 bits of word-within-block (2³ = 8).
**The tag is common to all eight words of the same block** — that is the storage saving blocks buy:
one tag per 8 words instead of one per word.

**Trade:** simplest and cheapest (one comparator), but **inflexible** — "a particular block of main
memory can be brought to a particular block of cache memory" and nowhere else. Two hot addresses with
the same index **evict each other repeatedly** even if the rest of the cache is empty (thrashing).

#### (b) Associative mapping

**The most flexible:** any block of main memory can reside in **any** cache position.

The cache is an **associative memory** storing **both the address and the data**: a 15-bit address
field plus its 12-bit word. The CPU's 15-bit address goes into the **argument register** and the cache
is **searched in parallel** for a matching address. Found → read the 12-bit data. Not found → go to
main memory.

**Trade:** the best possible hit ratio for a given size (nothing is evicted unnecessarily), but needs
a **comparator per entry** — expensive and power-hungry, so only used for small structures (TLBs,
victim caches).

#### (c) Set-associative mapping

**The compromise, and what real caches use.** Cache blocks are grouped into **sets**; a main-memory
block may reside in **any block of one specific set.** "Each word of cache can store two or more words
of memory under the same index address; the number of tag–data items in one word of cache is said to
form a **set**."

Mano's example with **set size 2** ("two-way"):
```
 ┌──────────┬──────────────────┐
 │ TAG (6)  │    INDEX (9)     │        each cache "word" holds TWO (tag, data) pairs
 └──────────┴──────────────────┘
 cache word width = 2 × (6 tag + 12 data) = 36 bits;  cache = 512 × 36
```
**Operation:** the index selects the set; the CPU's tag is compared with **both** tags in that set —
"the comparison logic is done by an associative search of the tags in the set, thus the name
set-associative."

**The spectrum, which is the real insight:**
- set size 1 = **direct mapping**
- set size = number of cache blocks = **fully associative**
- anything between = **set-associative**

Direct and associative mapping are the **endpoints of one parameter**, not three unrelated schemes.
That framing answers "compare the three mapping techniques" far better than three separate
descriptions.

### Replacement policies — `settled`

"When the cache is full and new data must be brought in, a decision must be made as to which data is
to be removed. The guideline is called the **replacement policy**." **Replacement policy depends on
the mapping:**

| Mapping | Policy |
|---|---|
| **Direct** | **no choice exists** — there is exactly one place the block may go, so there is no policy |
| **Associative** | **FIFO** (replace in round-robin order as new words are requested) |
| **Set-associative** | **random**, **FIFO** (the item longest in the set), or **LRU** (the item least recently used by the CPU) |

**★ "Direct mapping has no replacement policy" is a favourite exam trap** — students reflexively
answer "LRU". There is nothing to choose between. (`misconceptions.md` M14.)

### Write policies — `settled`

On a **write hit**, two options:

| Policy | Mechanism | Trade |
|---|---|---|
| **Write-through** | update **cache and main memory simultaneously** | main memory is always current (good for DMA/multiprocessors); every write costs a memory access |
| **Write-back (copy-back)** | update **only the cache**, and mark the block with a **dirty / modified bit**; write to main memory **when the block is removed** | far fewer memory writes; main memory is temporarily stale |

On a **read miss**, two options:
- **Load-through** — the entire block containing the requested word is copied to cache, and the
  requested word is forwarded to the CPU **from the cache**.
- **Early restart** — the requested word is sent to the **CPU first**, then the cache is updated.
  (Lower latency: the CPU doesn't wait for the rest of the block.)

On a **write miss**:
- with **write-through**, the information is written **directly to main memory** (no need to load the
  block);
- with **write-back**, the block is **first brought into cache**, then the word is overwritten.

## 5. Virtual memory — `settled` (part of L23–L26's "Memory Organization")

**Historical motivation:** memory was expensive and small, so programmers hand-managed **overlays** —
breaking the program into pieces, deciding where each lived in secondary storage, and arranging
transfers. **In 1961 Manchester University proposed performing the overlay process automatically**,
which gave rise to virtual memory.

**The core separation:** distinguish the **address space** from the **memory space**.

| Term | Definition |
|---|---|
| **Virtual / logical address** | the address a programmer uses; the set of them is the **address space** |
| **Physical address / location** | an address in main memory; the set of them is the **memory space** |

**In a machine with virtual memory the address space is allowed to be LARGER than the memory space.**
Programs reference instructions and data independently of how much physical memory exists; virtual
addresses are translated to physical addresses by a combination of hardware and software.

**Mano's mapping example:** map a **20-bit virtual address** to a **15-bit physical address** — i.e. a
1M-word address space on a 32K-word memory. The mapping is **dynamic**: every address is translated
immediately as it is referenced.

**Where to keep the mapping table — three options and their costs:**
1. In a **separate memory** → needs an extra unit **and one extra memory access time**.
2. In **main memory** → the table takes space from main memory, and **two accesses are required per
   reference, so the program runs at half speed.**
3. In an **associative memory** → fast parallel lookup (this is the TLB idea).

**Read option 2 carefully — it is the whole reason the TLB exists.** Naive page-table-in-memory
translation *halves* performance. The associative lookup is not an optimization; it is what makes
virtual memory viable at all.

### Address mapping using pages

| Term | Meaning |
|---|---|
| **Block** (**page frame**) | a group of equal-size physical memory locations (typically **64 to 4096 words**) |
| **Page** | a group of address-space locations **of the same size** |

Programs move between auxiliary and main memory in **records equal to the size of a page.**

**Mano's worked example:** a **13-bit virtual address** with **1024-word pages**:
```
 ┌──────────┬──────────────────┐
 │ PAGE (3) │    LINE (10)      │      2³ = 8 pages;  2¹⁰ = 1024 words per page
 └──────────┴──────────────────┘
```
The **high-order 3 bits** specify one of the **eight pages**; the **low-order 10 bits** give the line
(word) within the page.

**The memory page table** has **eight words, one per page**: the address in the table *is* the page
number, and the **content gives the block number** where that page is stored in main memory. In
Mano's figure, pages 1, 2, 5 and 6 are present in main memory in blocks 3, 0, 1 and 2 respectively. A
**presence bit** distinguishes "in main memory" from "not resident".

**Note what is NOT translated:** the line field passes through unchanged. Only the page number is
mapped. That is why page size is a power of two — it makes translation a field substitution rather
than an arithmetic division.

### Associative memory page table

"A random-access-memory page table is **inefficient with respect to storage utilization**" — you need
an entry for every page whether or not it is resident. Mano's fix: replace it with an **associative
memory of four words** (four = the number of blocks actually in main memory). Each entry has two
fields: **3 bits of page number** and **2 bits of block number**. The virtual address's page number is
placed in the **argument register** and all entries are searched in parallel. **This is the TLB.**

## 6. Memory management hardware — `settled`

"A **memory management system** is a collection of hardware and software procedures for managing the
various programs residing in memory." The software part belongs to the operating system.

**Segmentation.** A **segment** is "a set of logically related instructions or data elements
associated with a given name" — generated by the programmer or the OS. The address a segmented program
generates is a **logical address**.

**Segments vs pages — the distinction that gets examined:**

| | **Page** | **Segment** |
|---|---|---|
| Size | **fixed** | **variable** — "the length of each segment is allowed to grow and contract according to the needs of the program" |
| Chosen by | the hardware/OS | the **programmer's logical structure** |
| Purpose | efficient physical allocation | logical grouping and protection |
| Fragmentation | internal (unused tail of a page) | external (gaps between segments) |

**Segmented-page mapping** combines both: segments are divided into pages, so you get the programmer's
logical grouping *and* fixed-size physical allocation. The logical address becomes
**segment number + page number + word**, and two table lookups (segment table → page table) resolve
it. This is why real systems use both rather than choosing.

---

## Worked-problem patterns for this unit

1. Draw the memory hierarchy; define main / auxiliary / cache; state what the CPU can and cannot
   access directly.
2. **SRAM vs DRAM** table; why a bootstrap loader must be in ROM.
3. **Memory interfacing:** given chip sizes and a required capacity, work out how many chips, which
   address lines go where, and draw the address map.
4. **CAM:** draw the organization (A, K, M registers); explain the role of the key register; give the
   match rule.
5. **Locality of reference** — define both kinds and link each to its design consequence.
6. **Numerical: hit ratio → average access time** (state your convention).
7. **Numerical: cache bit-split.** Given main memory size, cache size and block size, derive
   tag/index/block/word widths — for direct, associative and set-associative mapping.
8. **Compare the three mapping functions**, ideally via the set-size spectrum.
9. Replacement policies per mapping — and **why direct mapping has none**.
10. **Write-through vs write-back**; load-through vs early restart.
11. **Virtual memory:** page/line split for a given virtual address and page size; the page table;
    why a table in main memory halves speed; the associative page table.
12. **Pages vs segments**; segmented-page mapping.

## Confidence summary

`settled`: the hierarchy and the CPU-access rule · multiprogramming and memory management definitions ·
SRAM vs DRAM · bootstrap loader in ROM · the RAM chip (128×8, 7-bit address, CS1=1/CS2=0,
high-impedance when deselected) and ROM chip (512 bytes, 9 address lines) · the memory-connection
example and the low-order/high-order address-line rule · CAM organization (A, K, M), the masked match
rule, sequential read of matches, tag-register writing · locality of reference (both kinds) ·
**32K×12 main / 512×12 cache** · direct mapping **6-bit tag + 9-bit index**, and with 8-word blocks
**6 + 6 + 3** · associative mapping storing address+data · set-associative with set size 2 giving a
**512 × 36** cache · replacement policies per mapping, including **none for direct** ·
write-through/write-back, load-through/early-restart, and the write-miss rules · virtual memory
address-space vs memory-space, 20→15 bit mapping, the three table locations and the half-speed
consequence · pages 64–4096 words, the 13-bit/1024-word example giving **3 + 10**, the 8-word page
table, the 4-word associative page table · segments vs pages and segmented-page mapping.
`likely`: the average-access-time **convention** (h·tᶜ + (1−h)·tᵐ vs tᶜ + (1−h)·penalty) — both are in
use; the formula above is the one Mano-derived courses expect.
`uncertain`: **the instructor's emphasis and depth** — no deck for L23–L26. Cache is certainly central
(named in CO3, practitioner-delivered), but whether virtual memory / segmentation is examined at all
is unconfirmed. The institutional reproduction used here labels cache "12-5" and virtual memory
"12-6"; **figure numbers in that reproduction drift slightly** from Mano's, so figure numbers are not
cited anywhere above.
Not claimed: multi-level cache (L1/L2/L3) design, cache coherence protocols, or modern DRAM timing —
out of scope per `00-map.md`.

> **Stage 2 for this unit:** `stage-2/06-memory-organization.md` — the 3 C's of cache misses
> (compulsory/capacity/conflict) and what each tells you to change, why associativity has diminishing
> returns, the AMAT recurrence for multi-level hierarchies, why LRU is approximated rather than
> implemented, the memory wall, and the page-size trade-off (TLB reach vs internal fragmentation).
