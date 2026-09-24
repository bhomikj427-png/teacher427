# research-queue — the batch tracker (single source of truth for "what's next")

> Updated **live**, one work-item at a time, by the autonomous loop in `AUTONOMOUS-RUN.md`. Any
> session reads this first and resumes exactly. **Never reconstruct it from memory at session end**
> — it is written as work happens (same no-drift rule as `progress-log.md`).
>
> Status vocabulary (`two-stage-depth.md`): `stage-0` · `stage-1` · `stage-1✓` · `stage-2` ·
> `stage-2✓` · `parked`.

## Selection policy (restated)

Breadth-first: bring **every** subject to `stage-1✓` (in the priority order below) **before** any
subject is deepened to Stage 2. Skip `parked`. Within a subject, follow its `00-map.md` prereq
order; if no map yet, the map pass is the first item.

## Priority order & live status

| Pri | # | Subject | Code | Status | Units done | Last updated | Next action |
|-----|---|---------|------|--------|-----------|--------------|-------------|
| 1 | 01 | Statistics & Probability | MAS2001 | **stage-2✓** | 4/4 | 2026-06-19 | TEACH-READY. Re-verify official handout/PYQs when they arrive (re-scope only); recheck Berry–Esseen constant on re-entry |
| 2 | 03 | Electronic Devices-I | ECE2101 | **stage-2✓** (S1 verified; S2 honest) | 5/5 | 2026-06-24 | **TEACH-READY** (learner-activated, depth-first). Verification pass done: Stage-1 load-bearing claims source-verified (caught + fixed the reverse-current "5°C"→"10°C" error; added missing continuity eqn). Stage-2 derivations sound; **frontier/empirical specifics flagged `uncertain`** (E_crit, V_BR∝N^−¾, ZTC, BV_CEO exp, FinFET yrs). To fully close S2: source-verify those + solve the listed harder problems. Open: Si nᵢ `contested`; MUJ unit/MTE-ETE boundaries `uncertain`; rebuild exam-map when PYQs land |
| 3 | 04 | Digital Electronics | ECE2102 | **stage-2✓ (TEACH-READY)** | 5/5 S1 + 5/5 S2 | **2026-09-11** | **COMPLETE BASE — teaching gate met (learner-activated, depth-first).** Stage 1 (exam) + Stage 2 (deep structure) both done, all 5 units. Load-bearing specifics verified+triangulated this session: S1 (FS-borrow, BCD+6, comparator, JK char+excitation, LFSR 2ⁿ−1, std-TTL→fan-out10/NM0.4V, PROM/PLA/PAL); S2 (CMOS V_M, metastability MTBF, Kogge-Stone/Brent-Kung, SRAM butterfly SNM, Golomb postulates, 2's-comp from ℤ/2ⁿℤ). §0 surplus test passed per unit. **Confirmation cross-check vs NPTEL(IIT-Kgp)+MIT 6.004/6.111 done** —
MUJ scope fully covered; filled clock-gen hardware (555/ring/Schmitt/multivibrators), CMOS PUN/PDN gate
construction, parity→Hamming + code converters; logged out-of-scope boundaries (ADC/DAC→LIC, 8085, Booth/
pipelining→COA, FPGA→verilog). **Ready to TEACH** (diagnose→curriculum from 00-map→profile/log→loop). Open (mechanisms settled, exacts only): short-circuit-%, DRAM ΔV, essential-hazard delay, 74181 rows `likely`; frontier `evolving` (recheck on re-entry); **MTE/ETE split RESOLVED 2026-09-11** from the 25-Sep-2025 MTE paper (MTE = U1+U2+U3-to-counters; U4/U5 = ETE) — `exam-map.md` rebuilt from real evidence, 11 cited question patterns, teaching order re-sequenced by scoring value; still open: no ETE paper, one MTE only (`likely`), course code ECE 2105 (decks) vs ECE2102 (paper) `uncertain`, which textbook examined `uncertain`; Gothmann unsourced |
| 4 | 05 | Signals and Systems | ECE2103 | stage-0 | 0/? | 2026-06-16 | Map pass |
| 5 | 06 | Circuits & Network Theory *(Flexi A)* | ECE2120 | **stage-1✓** | 5/5 | 2026-06-22 | Learner-activated (depth-first). Stage 1 complete; **Stage 2 in progress next sprint** → bring to stage-2✓ before teaching. Confirm Flexi enrollment (ECE2120 vs ECE2121); exam-targeting unconfirmed (no PYQ) |
| 6 | 07 | Linear Integrated Circuits *(Flexi B)* | ECE2121 | stage-0 | 0/? | 2026-06-16 | Map pass |
| 7 | 08 | Electronic Devices Lab-I | ECE2130 | stage-0 | 0/? | 2026-06-16 | Map pass (lab; pairs with 03) |
| 8 | 09 | Digital Electronics Lab | ECE2131 | stage-0 | 0/? | 2026-06-16 | Map pass (lab; pairs with 04) |
| 9 | 10 | Project-Based Learning 1 | ECE2170 | stage-0 | 0/? | 2026-06-16 | Minimal KB (process/method, not a content syllabus) |
| 3.5 | 11 | **Computer Architecture & Processor** | **ECE2108** | **stage-2✓ (TEACH-READY)** | 8/8 S1 + 8/8 S2 | **2026-09-12** | **NEW SUBJECT, created + fully built this session** (learner dropped the course hand-out + 3 unit decks; reported the subject missing from the registry). **COMPLETE BASE — teaching gate met.** Scope is the best-evidenced in the batch: built from the professor's **own course hand-out** (36-lecture plan) + 3 decks, not an inferred syllabus. **Assessment split `settled` — MTE 30 / CWS 30 / ETE 40 (first verified MUJ marks split anywhere in the batch; ECE2108 only, do not generalize).** **MTE/ETE boundary `settled` from the printed lecture-plan divider after L19 → MTE = U1+U2+U3+U4 (incl. pipelining), ETE = U5–U8.** 8 units: 01 arch-fundamentals+RTL · 02 Basic Computer · 03 control unit/microprogrammed · 04 parallel+pipelining · 05 I/O org · 06 memory org · 07 **8086** · 08 **RISC-V**. Verified this session: Mano ch.7 field widths triangulated across **2 independent** reproductions (128×20, F1/F2/F3/CD/BR/AD = 3/3/3/2/2/7, sequencer input logic); BC's 25 instructions; pipeline speedup + both worked examples; Mano ch.12 cache splits; 8086 architecture/flags/ModR-M/segment table; **RISC-V quoted directly from the ratified spec** (the one true primary here); Wilkes 1951, NetBurst 20→31 stages, the A20 gate, Hill & Smith's 3 C's. **All 34 numeric claims re-computed programmatically — all pass.** Both exit tests passed. **Caught + corrected 2 real source errors** (deck's ISZ `D₆T₄`→`D₆T₆`; an institutional doc's "SF is used with unsigned numbers"). **Ready to TEACH.** Open: **no PYQ at all** → question forms are inference (scope is not); no deck for L12–L36; **Mano 3e could not be read directly** (server truncates — verified via multiple agreeing reproductions instead, `sources.md` §4); taxonomy counts (addressing modes 12/8/7, instruction groups 7/8, transfer modes 3/4) are conventions not facts; CWS composition unspecified |
| 10 | 02 | Management of Technology | **MBB2101** | **stage-1✓** (content complete; no PYQ) | 5/5 | 2026-06-24 | **UN-PARKED + Stage-1 built** (learner-activated). Resolved MBB21XX→MBB2101; official topic list located in MUJ R&AI Scheme PDF. **Reframe:** it's an entrepreneurship+biz-functions+IPR survey, not classical MOT. **Stage-2 analysis done; learner decided 2026-06-26: NO full Stage 2 — `stage-1✓` IS the teaching gate for this subject (logged exception).** Fold targeted "Stage 1.5" (IPR→Acts, finance worked-probs if PYQ, innovation theory +1 notch) into Stage 1 on teaching activation. **TEACH-READY** (subject-scoped exception; global gate unchanged). Open: unit/MTE-ETE split & "Project Formulations 1/2/3" `uncertain` (no handout/PYQ); GI term `likely`; NPTEL week outline not extracted |

`Units done = ?` means the unit count is set by the map pass (it hasn't run yet).

## Parked / blocked items (why, and what un-parks them)

- *(none — 02 Management of Technology un-parked 2026-06-24; see log below.)*

### Resolved un-park
- **02 Management of Technology** — was parked on a missing syllabus. **Un-parked 2026-06-24:**
  code resolved `MBB21XX → MBB2101`; official topic list + references + NPTEL link found in the MUJ
  B.Tech *Scheme & Syllabus 2024* (R&AI PDF; MBB2101 is a shared management-dept course). No
  invention needed — lifted verbatim.

## Exam calendar

MTE/ETE dates: **not yet provided** — see `exam-calendar.md` (created 2026-07-05; drives the
review-taper rule). Learner supplies dates; the engine never invents them.

## Exam material (PYQs/PPTs) — batch status

Stage 1 is now **PYQ/PPT-driven** (`exam-resources.md`, `two-stage-depth.md`). Each subject has an
`exam-pack/` drop-folder; the engine builds `knowledge-base/exam-map.md` from it. **As of 2026-06-17
no exam-pack is populated** — portals (MUJ Central/Stella/Toppers) confirmed but not machine-
scrapable for Sem-3 ECE, and MUJ Central's catalog didn't yet list Sem-3 ECE. **Action:** learner drops
material (any subject, unsorted) into the central **`../_inbox/`**; the engine **triages it first**
(see `AUTONOMOUS-RUN.md` "Inbox triage" + `../_inbox/README.md`), routing each file to the right
subject's `exam-pack/` and logging it to `../_inbox/TRIAGE-LOG.md`. Until material arrives, exam-maps
are `uncertain` and research proceeds syllabus-driven. MTE/ETE weightage unverified. **Inbox status 2026-09-11: EMPTIED — first material received and routed.** 11 files -> `04-digital-electronics/exam-pack/` (8 prof decks + 1 partial merge + **MTE PYQ 25-Sep-2025** + practice set); `04`'s `exam-map.md` rebuilt from it (2026-09-11).

**Inbox status 2026-09-12: EMPTIED again — second drop.** 4 files -> **new** `11-computer-architecture-and-processor/exam-pack/`: the **official ECE2108 course hand-out** + 3 prof unit decks. **The hand-out is the most valuable single document in the batch so far** — it is the only first-party source that states a **marks split (MTE 30 / CWS 30 / ETE 40)** and an **MTE/ETE boundary** outright instead of by inference, and it carries a full 36-lecture plan. Both are `settled` **for ECE2108 only** — `exam-resources.md`'s batch-wide `uncertain` on weightage still stands for every other course.

Every subject other than `04` and `11` still has an empty exam-pack and an inferred exam-map stub. **Still missing for `11`: any past paper (MTE or ETE) — question forms there are inference, not evidence — and any deck for L12–L36, which includes the 8086 (8 lectures, the highest-value unit in that course).**

## ⚠ BATCH-LEVEL OPEN QUESTION — the registry is built on the WRONG SCHEME REVISION

`[opened 2026-09-12]` **The learner is enrolled under the MUJ *2025-2026 onwards* ECE scheme, but this
batch was seeded (2026-06-16) from the *2023-onwards* curriculum PDF.** That is why the learner reports
both "subjects I don't have" and "a subject I have that isn't listed."

**Evidence (both official MUJ PDFs, text-extracted this session):**
- *2023-onwards* curriculum: **67 course codes, ECE2108 absent.**
- *2025-2026 onwards* scheme (`jaipur.manipal.edu/fosta/img/programs/ECE/Scheme-2025-ECE.pdf`):
  **ECE2108 present, Third Semester, 3 credits.**

**The two Sem-3 lists, side by side:**

| 2023-onwards (what this batch has) | 2025-2026 onwards (what the learner is on) |
|---|---|
| MAS2001 Statistics & Probability | MASXXXX Probability and Statistics |
| MBB21XX Management of Technology | *Principles of Management / Engineering Economics* |
| ECE2101 Electronic Devices-I | **ECE2106 Electronics Devices & Circuits** |
| ECE2102 Digital Electronics (4 cr) | **ECE2105 Digital Electronics (3 cr)** |
| ECE2103 Signals and Systems | — *(not in Sem-3)* |
| Flexi Core 1: ECE2120 CNT / ECE2121 LIC | — *(not in Sem-3)* |
| — | **ECE2104 Data Structures and Algorithms** ← subject the learner has. **Folder `12-` created 2026-09-24** (exam-pack: 8 decks + Assignment 1). Not researched |
| — | **ECE2108 Computer Architecture & Processor** ← built this session |
| ECE2130 Electronic Devices Lab-I | ECE2134 Electronics Devices & Circuits Lab |
| ECE2131 Digital Electronics Lab | ECE2133 Digital Electronics lab |
| ECE2170 Project-Based Learning 1 | — *(PBL-1 is ECE2271, Sem 4)* |
| — | **ECE2132 Data Structures and Algorithms Lab** |
| Total 25 credits | **Total 24 credits** |

**Consequences:**
- **Likely not the learner's courses at all:** 05 Signals & Systems, 06 Circuits & Network Theory,
  07 Linear Integrated Circuits, 10 Project-Based Learning 1, and 02 Management of Technology as
  currently framed. **`06` already has a `stage-1✓` knowledge base that may be wasted effort** — and
  `01`/`03`/`04` may need re-scoping to the new course titles (note `ECE2106` is "Devices **& Circuits**",
  a wider scope than `ECE2101` "Devices-I").
- **Missing entirely:** **ECE2104 Data Structures and Algorithms** + its lab, and **ECE2107 Circuits &
  Systems**. `[2026-09-25]` **ECE2107 folder `13-circuits-and-systems/` created** by inbox triage (learner's
  handwritten notes; exam-pack only, not researched). Its topics so far match `06`'s U1–U2 KB.
- **`[RESOLVED]` the ECE 2105 vs ECE2102 code mismatch** flagged in `../_inbox/TRIAGE-LOG.md`
  (2026-09-11): the professor's Digital Electronics deck heads itself **ECE 2105** because that is the
  **new** code; the MTE paper and that subject's KB say **ECE2102**, the **old** one. **Both are
  correct, for different scheme revisions.** `uncertain → settled`.

**NOT ACTED ON UNILATERALLY.** Restructuring the registry would touch subjects with built knowledge
bases (`01`, `03`, `04` teach-ready; `06` at stage-1✓) and is an architecture-level change — the
learner's standing rule is design-first, sign-off before editing the core. **Resolve by:** the learner
confirming their actual registered course list, then re-mapping the batch in one deliberate pass.
Nothing in `01`–`10` was edited this session.

## Open questions surfaced during research (batch-level)

- `[opened 2026-06-16]` **01 MAS2001 unit list** — seeded from a derivative source (study-notes
  aggregator), not the official handout PDF. **Resolve by** fetching the official "Course Handout
  MAS2001" PDF and reconciling. Until then unit scope is `uncertain` (the *statistics content*
  itself is settled textbook material; only the exact MUJ unit boundaries are unverified).

## Log of completed work-items (append-only)

- `[2026-06-16]` Batch scaffolded; engine + queue created. Demo: **01 Statistics → stage-1✓**
  (map + 4 units + misconceptions + sources + Stage-1 curriculum). Source caveat above logged.
- `[2026-06-19]` **01 Statistics → stage-2✓** (depth-first, learner-activated for teaching).
  Built `stage-2/01–04` + `stage-2/sources.md`; promoted misconceptions M3/M7/M11 to `settled`;
  every load-bearing specific verified vs external sources this session. Subject is now teach-ready.
  Open: Berry–Esseen best constant (`contested`/open); Stage-2-vs-exam scope (`uncertain`, needs handout).
- `[2026-06-22]` **06 Circuits & Network Theory → stage-1✓** (depth-first, learner-activated for
  teaching). Built `00-map` + `exam-map` (uncertain stub) + units `01`–`05` + `misconceptions` +
  `sources` + `CHANGELOG`. High-risk exact claims (PR/Hurwitz, RC/RL/LC pole-zero rules, Foster/Cauer,
  AC conjugate match, two-port reciprocity/symmetry) verified vs external sources this session. Stage-1
  exit test passed on representative problems (no PYQ → exam-targeting unconfirmed). **Next: Stage 2 →
  stage-2✓ before teaching.** Open: Flexi enrollment ECE2120 vs ECE2121; M8/M10 `uncertain`.
- `[2026-06-24]` **03 Electronic Devices-I → stage-1✓** (depth-first, learner-activated for
  teaching). Built `00-map` + `exam-map` (uncertain stub) + units `01` semiconductor physics, `02`
  PN junctions + diode circuits, `03` JFETs, `04` MOSFETs (+switch+digital/CMOS), `05` BJTs (+MOSFET
  comparison) + `misconceptions` (M1–M25) + `sources` + `CHANGELOG`. Verified high-risk exact
  constants vs external sources this session: **Si nᵢ is textbook-dependent** (1.0–1.5×10¹⁰ —
  Boylestad 1.5e10 / refined 1.0e10 / Altermatt 9.65e9; PVEducation, OSTI, Springer 2023) → logged
  `contested`, teach-the-spread; Si E_g≈1.12 eV, V_T≈25.85 mV `settled`. Stage-1 exit test passed on
  representative problems (no PYQ → exam-targeting unconfirmed). **Next: Stage 2 → stage-2✓ before
  teaching.** Open: MUJ unit/MTE-ETE boundaries `uncertain`; misconceptions M6/M13/M19/M24 to source
  in Stage 2.
- `[2026-06-24]` **03 Electronic Devices-I → stage-2✓ (TEACH-READY)** (same session, depth-first).
  Built `stage-2/01`–`05` + `stage-2/sources.md`: DOS/nᵢ-convention, Fermi-Dirac/freeze-out/BGN,
  Einstein-from-detailed-balance, μ(T,N) + velocity saturation, continuity engine; **full Shockley-
  diode derivation**, η=2/generation leakage, breakdown quantitatively, Schottky thermionic emission,
  reverse recovery; **MOS V_t/γ + square-law derivations + four short-channel corrections (incl. the
  60 mV/dec subthreshold floor)**, CMOS scaling→FinFET/GAA; JFET GCA/ZTC/1-f-noise/HEMT; **BJT
  base-profile→α/β derivation**, Ebers-Moll, Early, Kirk/Webster, BV_CEO, SiGe HBT; cross-topic
  unification (quasi-Fermi; subthreshold MOSFET = BJT). Verified this session: Si N_C≈2.8e19,
  N_V≈1.0–1.8e19 (m*-spread → grounds nᵢ `contested`); S=ln10·kT/q=59.5 mV/dec. Promoted M6/M13/M19/M24
  → `settled`. §0 surplus exit test passed. Open: exam-targeting still needs PYQs; process constants
  (E_crit, ZTC, BV_CEO exp, N_V exact) `uncertain`, mechanisms-not-numbers.
- `[2026-06-24]` **03 Electronic Devices-I — verification pass** (triggered by a completeness
  challenge: "do the real work"). Source-verified Stage-1 load-bearing claims this session
  (μ/v_sat/ε_r, V_T, V_D tempco, breakdown ranges+TC signs, cut-in V, V_bi/depletion-width/Shockley/
  MOSFET forms) + derivation-verified BJT/JFET/MOSFET/rectifier identities. **Caught & fixed a real
  error:** reverse current "doubles every ~5 °C" → **~10 °C** (measured/generation ∝nᵢ; 5 °C only for
  ideal nᵢ² diffusion) in unit 02 + M12. **Patched syllabus gap:** added the continuity equation to
  unit 02. Honest re-marking: `settled` only where checked; unverified Stage-2 frontier/empirical
  specifics kept `uncertain`. Audit trail: `knowledge-base/sources.md` "Verification pass" + `CHANGELOG`.
  Remaining to fully close S2: source-verify the flagged specifics + solve the listed harder problems.
- `[2026-06-27]` **04 Digital Electronics → stage-2✓ (TEACH-READY)** (same day, learner: "dig deep,
  important to ECE"). Built `stage-2/01`–`05` + `stage-2/sources.md`: §A first-principles derivations,
  model limits / "where the UG textbook lies," cross-topic unification, frontier, harder problems per
  unit. **Verified + triangulated vs primary this session:** CMOS V_M=[r(V_DD−|V_Tp|)+V_Tn]/(1+r),
  r=√(k_p/k_n) (Tufts/Weste-Harris); metastability MTBF=e^{t_r/τ}/(T_W·f_c·f_d) (NXP AN219/Trilobyte);
  parallel-prefix Kogge-Stone O(log₂n)/Brent-Kung 2log₂n−2 (Wikipedia/Concordia); SRAM SNM=largest
  square in butterfly, read<hold (SNM lit.); m-sequence Golomb R1–R3 (IIT-G/Golomb); 2's-comp from
  ℤ/2ⁿℤ. Promoted M14→`settled`. §0 surplus exit PASSED all 5 units. **Now teach-ready** (full base,
  both stages). Open: short-circuit-%/DRAM-ΔV/essential-hazard-delay/74181-rows `likely` (mechanisms
  settled, exacts to primary); frontier `evolving` (recheck on re-entry); MUJ exam split + textbook
  `uncertain` (rebuild exam-map when PYQs land); Gothmann unsourced.
- `[2026-06-27]` **04 Digital Electronics → stage-1✓** (learner-activated "start making kb",
  depth-first). Built `00-map` (6 big ideas, prereq graph + 6 threshold concepts triangulated vs
  Cambridge CST notes) + `exam-map` (uncertain stub, no PYQ) + units `01` combinational (Boolean/
  K-map/Q-McCluskey, HA/FA/HS/FS, ripple/serial/CLA, BCD adder) `02` MSI (comparator/MUX/decoder/
  encoder/display/barrel/ALU) `03` sequential (latches/FFs + char & excitation tables, master-slave/
  edge race, ripple/sync counters, shift regs, timing f_max) `04` state machines (Mealy/Moore, FSM
  design pipeline, state reduction, ASM, PRBS/LFSR, async hazards/races) `05` logic families+memories
  (TTL/tristate/ECL/CMOS, NM/fan-out/t_pd, SRAM/DRAM/ROM, PROM/PLA/PAL) + `misconceptions` (M1–M19) +
  `sources` + `CHANGELOG`. **Verified + triangulated against external sources this session:** FS-borrow,
  BCD +6 correction, 4-bit comparator eqns, JK char-eqn + 4 excitation tables, LFSR 2ⁿ−1 + all-zeros
  lockout, **standard-TTL DC table → fan-out 10 / NM 0.4 V (4 independent sources)**, PROM/PLA/PAL
  arrays. Stage-1 exit tests passed per unit (no PYQ → exam-targeting `uncertain`). **Next: Stage 2 →
  stage-2✓ before teaching** (teaching gate). Open: MUJ unit/MTE-ETE split + which textbook examined
  `uncertain`; Gothmann not sourced; per-series TTL/ECL numbers `uncertain`; M14 to source.
- `[2026-06-24]` **02 Management of Technology — UN-PARKED → stage-1✓** (learner-activated). Resolved
  `MBB21XX→MBB2101`; pulled the official topic list/references/NPTEL link from the MUJ R&AI Scheme
  PDF (text-extracted via pypdf). Built `00-map` (+ Stage-2 deserves-analysis) + units `01`–`05` +
  `exam-map` (uncertain stub) + `misconceptions` (M1–M12) + `sources` + `CHANGELOG`. Verified this
  session: Indian IP terms, finance formulas, Ansoff quadrants/risk, Rogers adopter %. **Reframe
  logged:** course is entrepreneurship+biz-functions+IPR, not classical MOT. **Stage-2 verdict:
  recommend NO full Stage 2** (no first-principles substrate; non-core; the real frontier is a
  different course) — stop at stage-1✓ + a targeted "Stage 1.5." **Awaiting learner's call** on
  treating stage-1✓ as the teaching gate for this subject. Open: unit/MTE-ETE split & "Project
  Formulations 1/2/3" `uncertain`; GI term `likely`; NPTEL outline not extracted; no PYQ.

- `[2026-09-12]` **NEW SUBJECT `11 Computer Architecture & Processor (ECE2108)` — created and taken to
  `stage-2✓` in one session** (learner: "make the subject… go do research for this session, do it hands
  free"). Inbox triaged (4 files → `11-…/exam-pack/`, logged). Built `course-info` + `00-map` +
  `exam-map` + Stage-1 units `01`–`08` + `misconceptions` (M1–M23) + `sources` + `CHANGELOG`, then
  `stage-2/01`–`08` + `stage-2/sources`. **Scope `settled` from the professor's own hand-out** (36-lecture
  plan): **MTE 30 / CWS 30 / ETE 40** (first verified MUJ marks split in the batch) and **MTE = U1–U4,
  ETE = U5–U8** from the printed divider after L19. **Verified this session:** Mano ch.7 triangulated
  across 2 independent reproductions; BC 25-instruction count; pipeline speedup + both worked examples;
  ch.12 cache splits; 8086 architecture/flags/ModR-M/segment defaults; **RISC-V quoted directly from the
  ratified specification**; and for Stage 2 — Wilkes 1951/EDSAC 2, NetBurst 20→31 stages, the 8086 A20
  wraparound + keyboard-controller gate + HMA, Hill & Smith's three C's. **34/34 numeric claims
  re-computed programmatically — all pass.** Stage-1 and Stage-2 exit tests passed. **Two real source
  errors caught and corrected** (deck ISZ `D₆T₄`→`D₆T₆`; "SF is used with unsigned numbers" rejected).
  **Also resolved a standing batch question as a side effect** — the ECE 2105 vs ECE2102 Digital
  Electronics code mismatch (different scheme revisions) — and **surfaced a batch-level problem: the
  registry is built on the 2023 scheme while the learner is on the 2025-2026 one** (see the section
  above; deliberately not acted on). Open for `11`: no PYQ (question forms are inference); no deck for
  L12–L36; Mano 3e unreadable directly (mitigated, `sources.md` §4); taxonomy counts are conventions.
- `[2026-09-11]` **Inbox triage — first exam material in the batch.** 11 files routed out of
  `_inbox/_unsorted/` into `04-digital-electronics/exam-pack/` (audit: `_inbox/TRIAGE-LOG.md`):
  professor's decks 1-8 (syllabus/Boolean, K-map, adders, MUX-demux, decoder-encoder,
  comparator-parity, shifter-ALU, sequential-logic/FFs), one partial merge of decks 1-5, the
  **MTE past paper 25-Sep-2025** (ECE2102, 30 marks / 90 min), and a 10-question combinational
  practice set. **`04`'s exam-map rebuilt from evidence** — MTE structure `settled`; **MTE scope =
  U1 + U2 + U3 through synchronous counters**, U4/U5 absent (corroborated by deck coverage);
  11 cited question patterns; teaching order re-sequenced by scoring value. Open: no ETE paper;
  one MTE only (patterns `likely`); **course-code mismatch ECE 2105 (decks) vs ECE2102 (paper/KB)**;
  missing decks for counters/registers/FSM/logic-families/memories; 2026 exam dates still unset
  (2025 MTE was 25 Sep).
