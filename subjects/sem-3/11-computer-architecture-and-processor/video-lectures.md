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
material — which is why §5 (tutorial/problem-solving lectures) is the most valuable section in this
file, not the lecture lists.

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

You have no past paper and you never will for this cohort. The closest available substitute is
**someone else's worked problems on the same material**, and two of these courses have them
explicitly:

| Source | What it gives you |
|---|---|
| **[IITG-ACA] Tutorial 1** — instruction pipeline and performance | worked **speedup numericals** — `exam-map.md` F14, the likeliest U4 numerical |
| **[IITG-ACA] Tutorial 2** — pipeline hazard analysis | worked **hazard identification**, F16 |
| **[IITG-ACA] Tutorial 3** — static and dynamic scheduling | partly beyond scope; the static-scheduling half is `study-pack/10`'s delayed-load material |
| **[IITM-CO] L13, L14** `F5pU5LbmLVg`, `hhvl7nbVpLo` — "Problem Exercise" ×2 | worked **control-unit / microprogramming problems** — the U3 unit with no deck |

**Treat these four as unofficial practice papers.** Pause before each solution, attempt it, then
watch. They are not your examiner's questions — but they are *examiners'* questions on your topics,
which is one step better than nothing and one step worse than a real PYQ. Say exactly that much
about them, no more.

**The other substitute you already have:** the professor's Unit-1 deck ends on a slide reading
*"Design a 4-bit ALU that may perform the following operations. Explain its working in detail"* —
marked "QnA". That is the **highest-confidence single question item in the entire subject**
(`exam-map.md` F4), because it is the instructor's own question in the instructor's own deck. It is
worth more than every video on this page. It is fully worked in `study-pack/03` and again as
`study-pack/11` Drill A, Section C.

---

## §6 — Known limits of this file

Stated rather than hidden, so you know what has and has not been checked.

1. **No video content was watched or transcribed.** Every recommendation is made from **verified
   lecture titles** pulled from live playlist listings — never from a claim about what a lecture
   says. Titles are strong evidence of topic and weak evidence of depth.
2. **The transcript ingestion path was attempted and is currently rate-limited.**
   `tools/fetch_transcripts.py` reported "no captions" on three test videos; the diagnosis is that
   captions **do** exist (`yt-dlp --list-subs` shows `en`, `en-orig` and an official
   *English — NPTEL Official* track) but the download returns **HTTP 429 Too Many Requests** after
   this session's playlist enumeration. yt-dlp also warns that **no JS runtime (deno) is installed**,
   which it now deprecates for YouTube extraction. Retry spaced out; install deno.
3. **Channel provenance is confirmed for only one source.** [KGP-HPCA]'s uploader is `nptelhrd`, the
   official NPTEL channel. [IITG-COA]'s owner could not be confirmed programmatically; [IITM-CO] and
   [IITG-ACA] are third-party compilations/re-uploads of institutional content. Content quality is
   not in question; *channel identity* is unverified, and re-uploads can be incomplete or reordered.
4. **[KGP-CAO] and [IITG-MPI] were identified from their NPTEL course pages, not from lecture
   listings.** NPTEL's course pages do not fetch cleanly (JS-loaded tabs), so their per-lecture
   contents are **unverified** — unlike every entry in §2, which came from a real listing.
5. **Tier-4 sources have not been checked for errors.** They match your syllabus's *sequence*; that
   is all that has been established. Every number, formula and definition still gets checked against
   `study-pack/` and `knowledge-base/` before you believe it.
