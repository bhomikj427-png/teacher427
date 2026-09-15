# ECE2108 — Sources (tiered, dated, confidence-marked)

> Tiering per `../../../../subject-research-protocol.md` §2. All sources reached **2026-09-12**.
>
> **Read §4 (Honest limitations) before trusting any Mano-derived claim.**

---

## Tier 0 — Instructor material (authoritative for SCOPE, never for truth)

| Source | Where | What it settles | Confidence |
|---|---|---|---|
| **Course Hand-out, Computer Architecture & Processor [ECE2108]**, Dr Rohit Mathur / Dr Manish Tiwari, MUJ, 4 pp | `../exam-pack/HANDOUT-ECE2108-course-handout.pdf` | course existence, code, L-T-P-C, **verbatim syllabus**, 5 COs with Bloom levels + target attainment, **assessment split MTE 30 / CWS 30 / ETE 40**, **36-lecture plan with the MTE divider printed after L19**, reference list | `settled` for scope and assessment structure |
| **Unit 1 deck — Register Transfer and Microoperations**, 33 pp | `../exam-pack/slides-unit1-…pdf` | U1 scope, framing and notation; the arch-vs-org comparison table; the arithmetic-circuit function table; **the ALSU design question the professor poses** | `settled` for scope; **not** for truth (see M1) |
| **Unit 2 deck — Basic Computer Organization & Design**, 48 pp | `../exam-pack/slides-unit2-…pdf` | U2 scope and Mano's BC reproduced end-to-end: registers, bus table, 25 instructions, timing, instruction cycle, MRI sequences, I/O & interrupt, complete description, design of BC and AC logic | `settled` for scope; **contains a typo — see M9** |
| **Unit 3 deck — Parallel Processing & Pipelining**, 36 pp | `../exam-pack/slides-unit3-…pdf` | U4 scope: throughput framing, Flynn, pipeline speedup with a worked example, FI-DA-FO-EX, the three hazard classes and all cures | `settled` for scope |

**The honesty split applies throughout** (`../../research-engine/exam-resources.md`): these files are
**Tier-1 for what is tested and how**, and **Tier-3/4 for what is true**. Two documented slide errors
this session (M1's muddled table row, M9's ISZ timing typo) are the evidence for that rule, not an
exception to it.

**No PYQ exists for this subject** — neither MTE nor ETE. **No deck for L12–L36.**

## Tier 1 — Primary / prescribed

| # | Source | Status this session |
|---|---|---|
| 1 | **M. M. Mano, *Computer System Architecture*, Pearson, 3e, 2007** — the spine; truth authority for **U1–U6** | ⚠ **Could not obtain a clean full copy** — see §4. Verified instead via multiple independent reproductions below |
| 2 | **K. M. Bhurchandi & A. K. Ray, *Advanced Microprocessors and Peripheral Devices*, McGraw-Hill, 3e, 2018** — truth authority for **U7 (8086)** | Not obtained directly; verified via institutional material using its EA/BA/MA notation |
| 3 | **D. A. Patterson & J. L. Hennessy, *Computer Organization and Design: The Hardware/Software Interface — RISC-V Edition*, Morgan Kaufmann, 2018** — truth authority for **U8** | Not obtained directly; **superseded for correctness by source 4** |
| 4 | **The RISC-V Instruction Set Manual, Volume I: Unprivileged ISA — RATIFIED** · `docs.riscv.org/reference/isa/v20240411/unpriv/` (also v20260120) | ✅ **READ DIRECTLY.** A true Tier-1 primary: the standard itself. Every U8 `settled` claim is quoted from it |
| 5 | V. C. Hamacher, Z. Vranesic & S. Zaky, *Computer Organization*, McGraw-Hill, 5e, 2002 | Not obtained; the deck's five-functional-units framing is Hamacher's and is reproduced there |
| 6 | J. P. Hayes, *Computer Architecture and Organization*, TMH, 3e, 1998 | Not obtained; listed in the hand-out |
| 7 | Sonal Yadav, *Computer System Organization*, AICTE, 1e, 2024 | Listed on the **decks** but **not** in the hand-out; not obtained |

## Tier 1–2 — Institutional reproductions actually read this session

These carry the Mano-derived content that could not be read from the book itself. Each is a
university-published course document.

| Key | Source | Covers | Used for |
|---|---|---|---|
| **[BC-PVP]** | PVP Siddhartha Institute of Technology — *COA Unit II: Basic Computer Organization and Design*, 18 pp | Mano ch. 5 | U2: registers and widths, bus rules (5 registers with LD/INR/CLR; IR and OUTR LD-only), **the "25 instructions" count stated explicitly**, instruction-set completeness, timing/control, instruction cycle, MRI, I/O and interrupt |
| **[CU-BSU]** | Beni-Suef University, Faculty of Computers — *Chapter 7: Microprogrammed Control*, 26 pp | Mano ch. 7 | U3: **the complete F1/F2/F3/CD/BR tables**, the 20-bit format 3/3/3/2/2/7, control memory 128 × 20, the example machine's parameters, mapping `0xxxx00`, the fetch routine in symbolic **and binary**, the sequencer input logic (S₁ = I₁, S₀ = I₀I₁ + I′₁T, L = I′₁I₀T) |
| **[CU-IOE]** | IOE Notes (Institute of Engineering, Tribhuvan University) — *Chapter 3: Control Unit*, 23 pp | Mano ch. 7 | U3: **independent corroboration** of the above; hardwired-vs-microprogrammed framing; WCS/dynamic microprogramming; the "RISC uses hardwired control" statement |
| **[PIPE-IOE]** | IOE Notes — *Chapter 4: Pipeline and Vector Processing*, 19 pp | Mano ch. 9 | U4: the speedup derivation and both limits, the Aᵢ×Bᵢ+Cᵢ register table, **the FP-adder four segments and the 60/70/100/80/10 ns → 110/320 → 2.9 example**, FI-DA-FO-EX, all three hazard classes and cures, the delayed-load reordering, the RISC 3-segment pipeline |
| **[MEM-SATH]** | Sathyabama Institute of Science and Technology — *Unit III: Memory Organization*, 24 pp | Mano ch. 12 | U6: hierarchy, RAM/ROM chips (128×8, 512-byte), memory connection example, **CAM organization (A, K, M registers) and the masked match rule**, locality, **32K×12 / 512×12 cache with 6-bit tag + 9-bit index**, the 64-blocks-of-8 split, set-associative 512 × 36, replacement policies per mapping, write policies, **virtual memory 20→15 bits, the 13-bit/1024-word page example, the associative page table**, segmentation |
| **[IO-AMIRAJ]** | Amiraj College of Engineering — *Unit 8: Input-Output Organization*, 19 pp (explicitly cites Mano 3e) | Mano ch. 11 | U5: the four peripheral/CPU differences, three bus organizations, strobe vs handshaking (both directions), **the three modes of transfer**, priority interrupt and daisy chaining, IOP and CPU–IOP communication, character- vs bit-oriented protocols |
| **[IO-DAU]** | Devi Ahilya Vishwavidyalaya — *Chapter 11 Lesson 04: Asynchronous Data Transfer*, 21 pp | Mano ch. 11 | U5: corroboration on strobe/handshaking |
| **[8086-BBAU]** | Babasaheb Bhimrao Ambedkar University, UIET — *The 8086 Microprocessor* (Q&A format), 33 pp | 8086 | U7: **HMOS/29 000 transistors/40-pin DIP**, speed grades, MIN/MAX modes and pins 24–31, **BIU/EU jobs and the pipelining statement**, **6-byte queue mechanics and the 2-byte refill rule**, **14 registers in four groups**, **the flag register with bit positions**, MOD/REG/r-m encoding tables, **default/alternate segment table**, BHE̅/A₀ table, bus status codes, reset vector FFFF0H, 8086-vs-8088. ⚠ **Contains the SF error — see M16** |
| **[AM-SSN]** | SSN College of Engineering — *Addressing Modes* (8086), 16 pp | 8086 | U7: **the 12 modes in 5 groups** with EA/BA/MA notation, **physical address = segment × 16 + offset worked (89AB:F012 → 98AC2H)**, the legal EA combination list, sign-extension of 8-bit displacements, string-mode DS/ES asymmetry, I/O-port and relative modes |
| **[AD-SSN]** | SSN College of Engineering — *Assembler Directives* (8086), 11 pp | 8086 | U7: directives with general forms and worked examples (DB, DW, SEGMENT/ENDS, ASSUME, ORG, END, EVEN, EQU, PROC/ENDP/FAR/NEAR, SHORT, MACRO/ENDM) |

## Tier 1 — NPTEL

| Source | Used for | Note |
|---|---|---|
| **NPTEL course 106108100, *Teacher Slides* Module 2 Lecture 2 — Assembler Directives** (M. Krishna Kumar), `archive.nptel.ac.in/…/M2L2.pdf` | U7: ASSUME, DB, DW, DD, DQ, DT, END, ENDP, ENDS, EQU, EVEN, EXTRN, GROUP, INCLUDE, PROC, PTR, PUBLIC, TYPE, **the EVEN/1-bus-cycle-vs-2 alignment mechanism**, DOS function calls via INT 21H | Tier-1 per protocol §2 (IIT-produced). Read as **text slides, not video** — the protocol's preferred ingestion path. Contains minor typographical errors (`ASUME`, `PROCE`, `PUBLC`) that do not affect content |

## Tier 1-adjacent — primary-grade reverse engineering

| Source | Used for |
|---|---|
| **Ken Shirriff, "Inside the 8086 processor's instruction prefetch circuitry" (2023)**, righto.com | U7: die-level queue mechanics — three 16-bit registers with read/write pointers; the prefetch policy (0–2 bytes → prefetch at next free cycle; 3–4 → delayed two clocks; 5–6 → no prefetch); the `FLUSH` micro-instruction; **the 8088's 4-byte queue and why** |

*Tiering note:* this is **not** a textbook, but it is **direct examination of the silicon** — primary
evidence about the artifact itself, stronger than any secondary description. Used only for mechanism
detail flagged as "deeper" in U7 §2, never for examinable Stage-1 claims.

## Tier 1 — Official university documents (scope/registry)

| Source | Settles |
|---|---|
| **MUJ B.Tech ECE Scheme 2025-2026 onwards**, `jaipur.manipal.edu/fosta/img/programs/ECE/Scheme-2025-ECE.pdf` | **ECE2108 Computer Architecture & Processor, Third Semester, 3 credits** — and the full Sem-3 list (ECE2104/2105/2106/2107/2108 + labs). **Resolves the registry discrepancy the learner reported** |
| **MUJ B Tech ECE Curriculum 2023 onwards**, `…/B%20Tech%20ECE%20Curriculum_2023%20onwards.pdf` | The **older** scheme that seeded this batch. **Verified by extraction: 67 course codes, ECE2108 absent.** Its Sem-3 is MAS2001 / MBB21XX / ECE2101 / ECE2102 / ECE2103 / Flexi ECE2120-2121 / ECE2130 / ECE2131 / ECE2170 |

## Tier 3–4 — consulted for orientation only, never cited as fact

GeeksforGeeks, TutorialsPoint, SlideShare, Scribd, Studocu, StudyMinds and similar were surfaced by
search and used **only** to locate better sources. **No claim in this knowledge base rests on any of
them.** Where such a page agreed with an institutional source, the institutional source is cited.

---

## §4 — Honest limitations of this session's sourcing

**(a) Mano 3e could not be read directly.** The one full-text copy located is served with chunked
encoding and **truncates mid-file**: 8 download attempts returned 2.0–7.3 MB, never a complete
document; `Content-Length` on HEAD was 0. An xref rebuild recovered **1262 of ~4759 objects**, but the
page tree lives in lost object streams, so no page could be rendered.

**What was done instead, and why it is adequate:** every Mano chapter in scope was verified against
**independent institutional reproductions** — and for the two most formula-dense chapters, **more than
one**:

| Chapter | Reproductions read | Agreement |
|---|---|---|
| ch. 5 (U2) | [BC-PVP] **+ the professor's 48-page deck** | agree on every register width, the bus table, all 25 instructions, and all MRI timings (**except the deck's ISZ typo, M9**) |
| ch. 7 (U3) | [CU-BSU] **+** [CU-IOE] | **agree on every field width and every table entry** |
| ch. 9 (U4) | [PIPE-IOE] **+ the professor's 36-page deck** | agree on every formula and both worked numbers |
| ch. 11 (U5) | [IO-AMIRAJ] **+** [IO-DAU] | agree |
| ch. 12 (U6) | [MEM-SATH] (single) | **single reproduction — see (b)** |

**A note on what "independent" means here (protocol §5).** These reproductions all derive from **one**
original — Mano. They are therefore **not independent evidence about the world**. But the claims in
U2–U6 are *facts about what Mano's models are*, and **Mano is definitionally the authority** for that,
being the prescribed text. Multiple faithful reproductions agreeing is strong evidence that the
reproduction is accurate; it is **not** evidence that Mano is right about anything external. Where a
claim *is* about the world rather than about Mano's model (8086 behaviour, RISC-V), genuinely
independent sources were used — Intel-derived institutional material, NPTEL, die-level analysis, and
the RISC-V standard itself.

**(b) U6 rests on a single reproduction.** [MEM-SATH] is the only full reproduction of ch. 12 read
this session. Its content is internally consistent and carries Mano's section numbering, but its
**figure numbers drift** from Mano's (it labels the associative-mapping figure 12-11 and the
direct-mapping one 12-12, then refers to 12-14 for the block-split). **Consequently no figure number
is cited anywhere in `06-memory-organization.md`** — only content. Cache numbers there are marked
`settled` on content grounds; a second reproduction would strengthen them.

**(c) U7's textbook was not read.** Bhurchandi & Ray was not obtained. U7 is built from institutional
material that **uses Bhurchandi's own EA/BA/MA notation** (strong evidence it derives from that text)
plus NPTEL and die-level analysis. The *facts* about the 8086 are well triangulated; what is
**`likely` rather than `settled` is that the instructor uses that notation** — no deck exists for
L27–L34 to confirm it.

**(d) Taxonomy counts are conventions, not facts, and are marked as such throughout:** the number of
8086 addressing modes (12 / 8 / 7), the number of instruction-set groups (7 / 8), the number of I/O
transfer modes (3 / 4), and the number of RISC-V instruction formats (4 core + 2 variants / 6). Each
is flagged in its unit file and in `misconceptions.md` (M13, M18, M21). **No bare number is asserted.**

**(e) Not verified this session:** 8086 per-instruction clock counts (AAM = 83 is single-sourced,
`likely`) and the full opcode map; RISC-V ABI register names (convention, `likely`); RISC-V's UC
Berkeley origin and governance (widely documented, not checked against a primary record).

## 2026-09-15 additions (Assignment-driven delta)

| Source | Tier | Used for | Confidence |
|---|---|---|---|
| **Assignment 1 and Assignment 2, ECE/VDT 2108**, MUJ (`../exam-pack/ASSIGNMENT-A*.pdf`) | 0 (scope/forms) | first-party question forms for U1, U2, U4 | `settled` for forms; never for truth |
| **Unit 1 deck p. 32, ALSU function table** (embedded image, extracted with pypdf and read) | 0 | the ALSU select-code ordering the professor uses | `settled` as the professor's table |
| **Solutions Manual — M. Morris Mano, *Computer System Architecture*** (reproduction hosted at uobabylon.edu.iq, `paper_11_1497_49.pdf`, 98 pp) | 1–2 (publisher solutions, via reproduction) | answers to Mano 4-12, 4-19, 4-21, 5-1, 5-3, 5-4, 5-6, 5-9, 5-10, 5-12, 5-16, 5-20, 5-21, 5-22, 5-25, 9-2…9-11 — **every one re-derived, not copied** | `settled` where re-derivation agrees; **two typos caught** (5-12(c) AR = 7AC → 9AC; 5-21 `RT7` → `RT2`, `rB4 + (AC15)′` → `rB4(AC15)′`) |
| **Adelphi Univ. CS371 lecture 9** (`home.adelphi.edu/~siegfried/cs371/371l9.pdf`), reproducing Mano ch. 4 | 2 | independent confirmation of Mano Table 4-8 ALSU ordering | `settled` (agrees with deck p. 32) |
| **Hamacher, Vranesic, Zaky, *Computer Organization* 5e §1.1** (reproduction at idoc.pub) | 1 (prescribed ref. 5) | computer definition; six computer types | `settled` |
| **Mano CSA ch. 1** definition of digital computer (quoted identically by several institutional notes, e.g. svcn.ac.in ECE lecture notes) | 1 via 2 | definition | `settled` |
| **Computer History Museum** — computers timeline (`computerhistory.org/timeline/computers/`) and *The Silicon Engine* timeline + 1971 microprocessor entry | 2 (museum, curated) | ENIAC, First Draft 1945, Manchester Baby 1948, UNIVAC 1951, TX-0 1956, IBM 7090, System/360 1964, RCA Spectra 1966, 4004 1971 (Hoff, Mazor, Faggin, Shima), Altair, Apple II, IBM PC; transistor Dec 1947; Kilby 1958; Noyce 1959 | `settled` |
| Wikipedia — *History of computing hardware*; *EISA*; *VESA Local Bus*; *Fifth Generation Computer Systems* | 3 | ENIAC tube count and dates; EISA 1988 32-bit; VLB 1992; FGCS 1982–1994 (MITI/ICOT) | `likely`; cross-checked against CHM where overlapping |
| EBSCO Research Starters / historyofinformation.com — FORTRAN | 3 | FORTRAN shipped April 1957, John Backus's IBM team | `likely` |
| 74HC194 datasheet (Nexperia) | 2 | bidirectional shift register mode table 00 hold / 01 right / 10 left / 11 load (matches Mano ch. 2 register) | `settled` |

**Generation date boundaries are `contested` across authors** (±2–5 years); the technology assigned to
each generation is not. Packs say "approximately".

## Verification log

- `[2026-09-12]` **U3 field widths triangulated** — control memory 128 × 20 and the microinstruction
  format 3/3/3/2/2/7 confirmed **independently** by [CU-BSU] and [CU-IOE], including every F1/F2/F3
  symbol and the sequencer input logic. `settled`.
- `[2026-09-12]` **BC instruction count confirmed** — [BC-PVP] states "the total number of instruction
  coded in this computer is 25"; the deck's three tables give 7 + 12 + 6 = 25 independently. `settled`.
- `[2026-09-12]` **Pipeline worked numbers confirmed** — the deck's 4-stage/100-task/3.88 example and
  [PIPE-IOE]'s 110 ns/320 ns/2.9 FP example are different examples that both illustrate S < k.
  `settled`.
- `[2026-09-12]` **RISC-V claims quoted from the ratified standard** — format count, register state,
  IALIGN, the S/B immediate rationale, and the fixed-field-position rationale are **direct quotations**
  from docs.riscv.org, not paraphrase. Strongest sourcing in this base.
- `[2026-09-12]` **Registry discrepancy resolved from two official PDFs** — ECE2108 **absent** from the
  2023-onwards curriculum (extraction: 67 codes, no match) and **present** in the 2025-2026 scheme,
  Third Semester. `settled`.
- `[2026-09-12]` **ERROR CAUGHT in [8086-BBAU]** — "SF is used with unsigned numbers" contradicts the
  same document's own flag table. Corrected; logged in `CHANGELOG.md`; retained as M16.
- `[2026-09-12]` **ERROR CAUGHT in the Unit-2 deck** — ISZ's third microoperation printed as `D₆T₄`
  instead of `D₆T₆`, contradicted by the same deck's "Complete Computer Description". Corrected;
  logged; retained as M9.
