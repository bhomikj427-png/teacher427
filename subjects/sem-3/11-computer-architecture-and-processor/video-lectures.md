# ECE2108 — Video lecture map

> Built 2026-09-13. Every course below was verified by **listing its actual lecture titles**
> (`yt-dlp --flat-playlist`), not from recall. Video IDs are taken from those live listings.
>
> **Read §0 before using this file.** The honest finding is that no single course matches this
> syllabus, and pretending otherwise would send you to the wrong lectures.

---

## §0 — The finding, stated plainly

Your syllabus is **Mano-based** for U1–U6 (`knowledge-base/sources.md`). Mano's Basic Computer —
the 4096×16 machine, the S₂S₁S₀ bus, the 25 instructions, the D·T timing, the 128×20 control memory —
is a **specific teaching machine from a specific textbook**.

**The Tier-1 NPTEL courses do not teach it.** IIT Guwahati, IIT Madras and IIT Kharagpur all teach
computer organization from a **MIPS/RISC or generic-CPU** angle. They cover the same *ideas*
(instruction cycle, control signals, microprogramming, pipelining) with different machines and
different notation.

**The courses that follow Mano unit by unit are individual-educator YouTube channels** — which the
engine's own sourcing rule classes as **Tier 4** (`../../../subject-research-protocol.md` §2).

So this file has two layers, and they do different jobs:

| Layer | What it is | What it is for | What it is **not** for |
|---|---|---|---|
| **A — Tier 1** | NPTEL / institutional | **mechanism and correctness.** Why a control signal is a sum of products; why a pipeline stalls | matching your exam's exact notation |
| **B — Tier 4** | individual educators following Mano | **scope coverage and exam-shaped worked problems** in your syllabus's exact order and notation | deciding what is *true* |

**The rule when they disagree:** `study-pack/` and `knowledge-base/` win. Both were verified against
Mano and triangulated across independent institutional reproductions. A video is a **second
explanation**, never a source of fact. If a Tier-4 video states a number that contradicts the study
pack, the study pack is right until proven otherwise — and tell me, because that is worth checking.

**Why this matters more for you than for most students.** You are the first batch, so there is no
PYQ and no senior's notes. What you *can* do is watch someone else's *examination* of the same
material — so **§5 is the section to read first**. It is also the section where transcripts were
actually fetched and read, which is why two of its original four recommendations had to be
retracted: titles lie, and the only cure is opening the thing.

---

## §1 — The courses

### Layer A — Tier 1 (institutional)

| Key | Course | Instructor / Institute | Size | Provenance |
|---|---|---|---|---|
| **[IITG-COA]** | Computer Organization and Architecture | IIT Guwahati | 40 videos, Modules 01–05 | channel titled "Computer Organization and Architecture NPTEL IITG" — `likely` the NPTEL IITG course; the channel's owner could **not** be confirmed programmatically |
| **[IITM-CO]** | Computer Organization | Prof. S. Raman, IIT Madras | 33 lectures | classic NPTEL course; the playlist used here is a **third-party compilation** of it |
| **[KGP-HPCA]** | High Performance Computer Architecture | Prof. Ajit Pal, IIT Kharagpur | 41 lectures | **uploader verified as `nptelhrd`** — the official NPTEL channel. `settled` |
| **[IITG-ACA]** | Introduction to Advanced Computer Architecture | Prof. John Jose, IIT Guwahati | 14+ lectures incl. 3 tutorials | content is IITG/NPTEL; the playlist is a **re-upload by a third party** |
| **[KGP-CAO]** | Computer Architecture and Organization | Prof. Indranil Sengupta & Prof. Kamalika Datta, IIT Kharagpur | full NPTEL course | course page verified; **RISC-platform based**, per NPTEL's own description |
| **[IITG-MPI]** | Microprocessors and Interfacing | Prof. Shaik Rafi Ahamed, IIT Guwahati | NPTEL course `noc20_ee11` | for **U7 (8086)** — ETE material |

### Layer B — Tier 4 (syllabus-matched, verify before trusting)

| Key | Playlist | Size | Why it is here |
|---|---|---|---|
| **[MANO-SA]** | *Computer Organization and Architecture* — Sudhakar Atchala | **60 videos** | Walks **Mano chapter by chapter** — ch. 4 → 5 → 7 → 8 → 3 → 12 → 11 → 9. The closest match to your syllabus of anything found. Covers **all four MTE units** |
| **[MANO-LM]** | *Computer Architecture & Organization* — Learning Monkey | granular | Same Mano sequence, broken into smaller pieces (one idea per video). Useful when one Atchala video moves too fast |

**Playlist links**

- [IITG-COA] — `https://www.youtube.com/channel/UC2GUBG_WsP0OO5tXXocwp3Q/videos`
- [IITM-CO] — `https://www.youtube.com/playlist?list=PLdlPA9pGVVtYgnOSdZBCpoVtY0u3Jkhjb`
- [KGP-HPCA] — `https://www.youtube.com/playlist?list=PLbMVogVj5nJQmNqgs7GLBE-HhMi0GQOPW`
- [IITG-ACA] — `https://www.youtube.com/playlist?list=PLEAYkSg4uSQ3dmkbCah82ek0KJnpz_DxL`
- [MANO-SA] — `https://www.youtube.com/playlist?list=PLXj4XH7LcRfDXDRzSLv1FfZ-SSA38SiC0`
- [MANO-LM] — `https://www.youtube.com/playlist?list=PLAoF4o7zqskS79z2MRuDM9p_K_TPAc4PR`
- [KGP-CAO] course page — `https://nptel.ac.in/courses/106105163` · `https://onlinecourses.nptel.ac.in/noc22_cs88/preview`
- [IITG-MPI] course page — `https://onlinecourses.nptel.ac.in/noc20_ee11/preview`

---

## §2 — MTE map: U1 → U4

Watch order matches `study-pack/`. **Pair each video with its study-pack file** — the file is where
the retrieval happens; the video is only exposure.

### U1 — Architecture fundamentals, RTL, microoperations, ALSU
*(study-pack 01, 02, 03)*

| Topic | Tier 4 — your syllabus's order | Tier 1 — the mechanism |
|---|---|---|
| Arch vs organization | [MANO-LM] #2 | [IITG-COA] M01 L01 `msqxkEKFg8I` · M01 L04 `pGQ69Y60tvA` |
| RTL, microoperations, control function | [MANO-SA] #1 `kTdvOlA2ko0` | [IITG-COA] M03 L01 `L2SLS9FgTx0` (instruction cycle and micro-operations) |
| Bus and memory transfers | [MANO-SA] #2 `PUyCDZTK5V4` · #3 `qx2vDKnVzQk` (tri-state) | [IITG-COA] M03 L09 `iaWX3Au19zo` (internal CPU bus organization) |
| Arithmetic microoperations, the 4-bit arithmetic circuit | [MANO-SA] #4 `oTtvWDdeSEQ` | — |
| Logic microoperations | [MANO-SA] #5 `VIR_jcKo94E` | — |
| Shift microoperations | [MANO-SA] #6 `6TwX8d9GuOc` | — |
| **ALSU — the deck's own exam question** | [MANO-SA] #7 `LjuIcbqRrbI` | — |

⚠ **U1 has almost no Tier-1 video coverage**, because "arithmetic/logic/shift microoperations and a
one-stage ALSU" is a Mano-specific treatment. This is the unit where you lean hardest on
`study-pack/03` and the professor's Unit-1 deck, and use the Tier-4 videos only to see the circuit
drawn.

### U2 — The Basic Computer
*(study-pack 04, 05, 06)*

| Topic | Tier 4 | Tier 1 |
|---|---|---|
| Instruction codes, direct/indirect | [MANO-SA] #8 `Rfa0QHhzfRw` | [IITG-COA] M02 L04 `H7QrDhPFwIA` (instruction format) · M03 L04 `vrZmX3VsZ-A` (addressing modes) |
| Registers + common bus | [MANO-SA] #9 `MT8YzfzKaP4` | [IITG-COA] M02 L01 `fvtOGHXqYBs` |
| The 25 instructions | [MANO-SA] #10 `hISl36xIMGo` · #12 `0wi91k1eSS0` · #13 `tMtxrElswak` · #14 `W0hDfef5E1c` | [IITG-COA] M02 L05 `BEvWyiDu4x4` (instruction set) |
| **Timing and control, hardwired CU** | [MANO-SA] #11 `Bsh_WYIlLXs` | [IITG-COA] M03 L02 `LNLjGgsDjBk` (control signals and timing) · M03 L06 `b5thcNYBrQc` (hardwired CU design) |
| Instruction cycle | [MANO-SA] #15 `5jIg-D5gKtY` | [IITG-COA] M02 L03 `HfPS8DCzxEE` · M03 L03 `KvjmIpOYn4o` |
| Interrupt cycle | [MANO-SA] #16 `qHQrtaB2T1I` | — |
| **Design of BC + accumulator logic** | [MANO-SA] #17 `qw05VJh_f-w` · #18 `dSQtryKGkVE` | [IITG-COA] M03 L03 `KvjmIpOYn4o` — *the same scan method, different machine* |

**[IITG-COA] M03 L03 is the single most transferable Tier-1 video for U2.** It derives control
signals for a complete instruction execution — which is exactly `study-pack/06`'s scan method, done
on a non-Mano machine. Watch it to understand *why* the method works, then do the scan on the BC.

### U3 — Control unit design and microprogrammed control
*(study-pack 07, 08)*

| Topic | Tier 4 | Tier 1 |
|---|---|---|
| Control memory, microprogrammed organization | [MANO-SA] #19 `eC6pWLNPSQ4` | [IITG-COA] M03 L07 `UMqHq_9omr0` (microinstructions and microprograms) · [IITM-CO] L7 `fo-yfZyrW4c` |
| **Address sequencing, the sequencer** | [MANO-SA] #20 `nxNytEYQLKI` | [IITM-CO] L11 `UYv36HV3Sng` (typical micro instructions) |
| The microprogram example, mapping `0xxxx00` | [MANO-SA] #21 `3UWhMaZcJfY` | — |
| Design of the control unit | [MANO-SA] #22 `n2bC_Rh1YIA` | [IITG-COA] M03 L08 `lKQfg96D408` (organization + optimization of microprogrammed CU) |
| **Hardwired vs microprogrammed** | — | [IITM-CO] L9 `6CCwWCstDGc` — *the comparison, taught directly* · [IITG-COA] M03 L06 `b5thcNYBrQc` |
| Program control: flags, conditional branch | [MANO-SA] #28 | [IITG-COA] M02 L07 `t4mzLPvv1yQ` (**flags and conditional instructions**) |
| Subroutine call/return, stacks | [MANO-SA] #23 (stack organization) | [IITG-COA] M02 L08 `bGFgMK9qz00` (**procedure CALL/RETURN**) |

**U3 is the unit with no professor deck** (`knowledge-base/03-…` header). It is therefore the unit
where video coverage earns the most — you have no slides to tell you the emphasis, so seeing two
independent treatments is the best substitute available.

### U4 — Parallel processing and pipelining
*(study-pack 09, 10)*

| Topic | Tier 4 | Tier 1 |
|---|---|---|
| Parallel processing, **Flynn's classification** | [MANO-SA] #53 `0l_KkiaQECk` | — |
| Pipelining, the k + n − 1 timing | [MANO-SA] #54 `zF23S5PcUT8` | [KGP-HPCA] Lec-06 `3p8kZpT56lQ` (pipelining introduction) · [IITG-ACA] Lec 3 |
| **Arithmetic pipeline (the FP adder)** | [MANO-SA] #55 `Q6rdSDKn544` | — |
| Instruction pipeline (FI-DA-FO-EX) | [MANO-SA] #56 `_cNrYUUDaq8` | [KGP-HPCA] Lec-07 `5YurAgw70g0` |
| **Hazards — all three classes** | — | [KGP-HPCA] Lec-08 `l7auULi7zls` (pipeline hazards) · Lec-09 `Rzl13ESnVWY` (**data hazards**) · Lec-15 `awdwcvDgJkI` (**control hazards**) · [IITG-ACA] Lec 4, Lec 5 |
| Branch prediction (a control-hazard cure) | — | [KGP-HPCA] Lec-16 `H-lL_Z3dacE` · Lec-17 `rJAEGbpRrL4` |
| RISC three-segment pipeline | [MANO-SA] #57 `8SemUimYUJ4` | — |

**U4 is the one unit where Tier 1 is clearly better than Tier 4.** [KGP-HPCA] Lec-08/09/15 treat the
three hazard classes at a depth no syllabus-summary video reaches, and hazards are `exam-map.md`'s
F16 — "identify the hazard type in a given instruction pair and state the cure".

**A caution on [KGP-HPCA]:** it is a *high-performance* architecture course, so it goes well past
your syllabus (Tomasulo, speculation, ILP). Watch Lec-06 through Lec-09 and Lec-15/16; stop there.
Everything after Lec-18 is out of MTE scope.

---

## §3 — ETE units (U5–U8), for later

Not on the mid-term. Listed so you do not have to re-do this search in November.

| Unit | Tier 4 | Tier 1 |
|---|---|---|
| **U5 I/O organization** | [MANO-SA] #45–52 (peripherals → IOP → serial) | [IITG-COA] Module 05 L01–L04 (I/O primitives, interrupt-driven I/O, DMA, storage) · [IITM-CO] L24–L28 |
| **U6 Memory organization** | [MANO-SA] #40–44 (hierarchy → cache → associative → virtual) | [IITG-COA] Module 04 L01–L12 (**12 lectures** — cache indexing/tagging, associative, multi-level, TLB, paging) · [IITM-CO] L15–L23 · [KGP-HPCA] Lec-21–26 |
| **U7 The 8086** | — | **[IITG-MPI]** *Microprocessors and Interfacing*, Prof. Shaik Rafi Ahamed, IIT Guwahati — 8086-specific, with assembly programming |
| **U8 RISC-V** | — | **[KGP-CAO]** Sengupta/Datta — NPTEL states the course is built on a RISC platform, which makes it the natural fit |

⚠ **U7 carries CO4 (85% target) and CO5 (the only L3 "Develop" outcome)** — the two highest-value
blocks in the whole course, both ETE. [IITG-MPI] is the single most important video resource on this
page for the *year*, even though it is worth nothing for the MTE. `knowledge-base/exam-map.md` §3.

---

## §4 — What to actually do

**Do not watch these front to back.** Video is the weakest study format there is — it feels like
learning while producing almost none. The study pack is question-first for exactly that reason.

**The pattern that makes a video worth its time:**

```
   1. Read the study-pack file's Map + Attempt section.  Try the questions. Fail some.
   2. NOW watch the mapped video(s).  You are looking for the thing you got wrong.
   3. Close the video. Redo the Attempt questions from memory.
   4. Only then read the file's Method section.
```

Step 3 is the one that does the work. A video watched *after* a failed attempt lands on a prepared
mind; the same video watched cold is entertainment.

**Priority, if time is short** — these five, in this order:

| # | Video | Why |
|---|---|---|
| 1 | [IITG-COA] M03 L03 `KvjmIpOYn4o` | the control-signal derivation — the examinable skill of U2 |
| 2 | [KGP-HPCA] Lec-08 `l7auULi7zls` | hazards, the likeliest U4 concept question |
| 3 | [MANO-SA] #7 `LjuIcbqRrbI` | the ALSU — the professor's own exam question |
| 4 | [MANO-SA] #17 `qw05VJh_f-w` | design of the Basic Computer in Mano's exact notation |
| 5 | [IITM-CO] L9 `6CCwWCstDGc` | hardwired vs microprogrammed, taught as a comparison |

---

## §5 — The part that substitutes for a PYQ

**Updated 2026-09-13 — transcripts fetched and read. Two of the four claims in the first version of
this section were wrong, and are corrected below rather than quietly edited away.**

You have no past paper and never will for this cohort. The closest substitute is **someone else's
worked problems on the same material**. Here is what survived checking.

### ✅ [IITG-ACA] Tutorial 2 — `MjjFqj01PzU` — the one real find

A genuine week-2 tutorial: **8 true/false items and 3 numericals, worked end to end.** Verified by
transcript, not by title.

**But read this before you open it.** It works in **MIPS 5-stage / CPI / RAW-WAR-WAW** terms — not
Mano's FI-DA-FO-EX segments and not S = n·tₙ/((k+n−1)·tₚ). Same topic, **different formulation**.
Watching it as if it were your syllabus would drill the wrong formula.

| Part of it | Verdict for your MTE |
|---|---|
| True/false: *"RAW data hazard can be reduced by operand forwarding"* (true) | **useful** — this is `study-pack/10`'s forwarding, in different vocabulary |
| True/false: *"a normal in-order 5-stage MIPS pipeline can achieve IPC > 1"* (false) | **useful** — it is the throughput ceiling argument |
| Numerical: CPI-based speedup | **useful with the caveat** — worked in `study-pack/10`, Appendix |
| Numerical: Load/Add chain, stalls with and without forwarding | **the best single item** — worked in `study-pack/10`, Appendix |
| Numerical: 2-bit correlating branch predictor | **out of scope** — stage-2 depth, skip for the MTE |
| True/false on FP multi-cycle initiation interval, WAW, big/little endian | **out of scope** |

Both usable numericals are now **worked, with the arithmetic independently re-derived**, in
`study-pack/10` → *Appendix — the CPI formulation*. You do not need to watch the video to get them.

### ❌ [IITM-CO] L13 and L14 — claim retracted

The first version of this file called these *"worked control-unit / microprogramming problems — the
U3 unit with no deck."* **That was inferred from the titles and it is wrong.** The transcripts say:

- **L13 `F5pU5LbmLVg`** — instruction-format and operand-count design (how many bits for opcode
  vs. source vs. destination, 2⁴ = 16 combinations). Relevant to **U2 instruction codes**, on a
  machine that is not Mano's. Not a control-unit problem.
- **L14 `hhvl7nbVpLo`** — a conceptual recap (data path, control signals, "a microinstruction is one
  small step", ALU + controller = CPU) that then **moves on to memory** — i.e. **U6, ETE material**.
  Not a problem exercise.

Neither is useless — L14's opening is a clean statement of *processor = data path + controller* — but
they are **not** the U3 practice this file claimed. ASR quality on both is poor ("up code" for opcode,
"for nyman" for von Neumann), so treat any specific in them with suspicion.

### ⚠ [IITG-ACA] "Tutorial 1" — does not contain Tutorial 1

`deKUGMHZjB4` is titled *"Tutorial 1: Instruction Pipeline and Performance"*. Its transcript opens:

> *"Welcome to the fourth lecture of the course. Today's lecture will be dedicated on discussion
> related to pipeline hazards."*

That is **Lec 4**, not a tutorial. And `IQql2ojVzsU`, titled *"Lec 4: Pipeline Hazards"*, opens
*"Welcome to lecture number five… control hazards and branch prediction"* — i.e. **Lec 5**.

**The playlist's titles are unreliable; the speedup-numericals tutorial was not found at its labelled
link.** What `deKUGMHZjB4` actually contains is still worth watching — a careful structural-hazard
walkthrough on a uni-port memory, with both cures (stall/bubble, or duplicate the hardware into
separate instruction and data memories) — which **corroborates `study-pack/10` §8(a) exactly**. Just
do not expect the tutorial the title promises.

### The item that still outranks every video here

Your professor's Unit-1 deck ends on a slide reading *"Design a 4-bit ALU that may perform the
following operations. Explain its working in detail"*, marked "QnA". That is the
**highest-confidence single question item in the subject** (`exam-map.md` F4) — the instructor's own
question, in the instructor's own deck. Worth more than everything above. Worked in
`study-pack/03` and again as `study-pack/11` Drill A, Section C.

---

## §6 — Known limits of this file

Stated rather than hidden, so you know what has and has not been checked.

1. **Five lectures have now been transcribed and read** (§5). **Everything else on this page is
   still recommended from verified lecture titles only** — pulled from live playlist listings, never
   from a claim about content. Titles are strong evidence of topic and weak evidence of depth, and
   §5 is the proof: of the five transcripts fetched, **two were not what their titles said**.
2. **The transcript path works; the earlier failure was rate-limiting, not breakage.** The HTTP 429
   cleared on the third retry, ~25 minutes later, and all five lectures downloaded. Diagnosis
   confirmed along the way: captions do exist (`--list-subs` shows `en`, `en-orig` and an official
   *English — NPTEL Official* track), and **two independent libraries** (yt-dlp and
   `youtube-transcript-api`) both reported an IP block, so it was request volume, not a tool bug.
   `tools/fetch_transcripts.py` now passes `--js-runtimes node` (Node v20 is installed — deno was
   never needed), sleeps between requests, and reports a 429 honestly instead of claiming "no
   captions found".
3. **Channel provenance is confirmed for only one source, and one re-upload is now proven
   mis-titled.** [KGP-HPCA]'s uploader is `nptelhrd`, the official NPTEL channel. [IITG-COA]'s owner
   could not be confirmed programmatically. [IITM-CO] and [IITG-ACA] are third-party re-uploads —
   and **[IITG-ACA]'s titles are verifiably wrong** for at least two entries (§5). Treat every
   lecture-number reference to that playlist as approximate: **open the video and check the opening
   sentence**, which always states which lecture it is.
4. **[KGP-CAO] and [IITG-MPI] were identified from their NPTEL course pages, not from lecture
   listings.** NPTEL's course pages do not fetch cleanly (JS-loaded tabs), so their per-lecture
   contents are **unverified** — unlike every entry in §2, which came from a real listing.
5. **Tier-4 sources have not been checked for errors.** They match your syllabus's *sequence*; that
   is all that has been established. Every number, formula and definition still gets checked against
   `study-pack/` and `knowledge-base/` before you believe it.
