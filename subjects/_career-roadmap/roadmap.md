# Career Track — Digital / VLSI Front-End (RTL → Verification)

> **Meta-doc, not a subject.** (Underscore prefix = engine meta, like `_inbox`/`_archive`.) This is
> the **sequence of subjects** that turns Verilog into a hire-able career skill. Each *goal* below
> becomes (or already is) a `subjects/<name>/` subject, built and taught to the same engine standard.
> **Verilog is Goal #1 of this track, by the learner's own framing — not the destination.**
>
> **Created:** 2026-06-29, at the learner's request ("research past Verilog — the next step and the
> next language — build it so Verilog is the first goal, with more to come").
> **Goal of the whole track:** an edge for **VLSI / digital-design internships and jobs**.
>
> **Sourcing note (engine ethos):** the *sequence* and *what-employers-want* claims below are
> grounded in current industry/roadmap sources (see §Sources), not model recall. They describe a
> **moving field** — recheck the "what's hot / what's required" specifics on each subject's launch,
> not the structural backbone (which is stable). Anything here is **scope/emphasis** guidance; when a
> goal becomes a real subject, its *truth* is built to `../subject-research-protocol.md` from primary
> sources, exactly like Verilog was.

---

## The one-screen map

```
                         ┌─────────────────────────────────────────────┐
                         │  GOAL 1 — VERILOG  (RTL design fundamentals) │  ◀── YOU ARE HERE
                         │  subjects/verilog/  · status: KB stage-2✓,   │      (active subject)
                         │  teaching not yet started)                   │
                         └───────────────────────┬─────────────────────┘
                                                 │  the language + the RTL mindset
                                                 ▼
                         ┌─────────────────────────────────────────────┐
                         │  GOAL 2 — SYSTEMVERILOG  (the industry lang) │  ◀── the literal
                         │  the real-world successor; design *and*      │      "next language"
                         │  verification both run on SV                 │
                         └───────────────────────┬─────────────────────┘
                                                 │  here the path FORKS (pick one to go deep)
                        ┌────────────────────────┴────────────────────────┐
                        ▼                                                  ▼
         ┌──────────────────────────────┐                 ┌──────────────────────────────┐
         │ GOAL 3A — RTL DESIGN +        │                 │ GOAL 3B — DESIGN VERIFICATION│
         │ MICROARCHITECTURE (front-end  │                 │ (DV) — UVM, coverage, formal │
         │ design track)                 │                 │ (highest head-count / demand) │
         └───────────────┬──────────────┘                 └───────────────┬──────────────┘
                         └──────────────────────┬──────────────────────────┘
                                                ▼
                         ┌─────────────────────────────────────────────┐
                         │  CROSS-CUTTING (learn alongside, not after): │
                         │  scripting (TCL/Python/shell) · Git · Linux ·│
                         │  EDA toolflow · static timing analysis (STA) │
                         └───────────────────────┬─────────────────────┘
                                                 ▼
                         ┌─────────────────────────────────────────────┐
                         │  GOAL 5 — SPECIALIZE (far horizon): SoC      │
                         │  integration · low-power (UPF) · DFT · formal│
                         │  · AI-HW accelerators · RISC-V · chiplets    │
                         └─────────────────────────────────────────────┘
```

**The internship-ready bar** (what actually gets a first VLSI internship, per the sources) sits at
roughly **Goal 1 + Goal 2 + a portfolio capstone + scripting awareness + UVM *awareness***. You do
**not** need the whole ladder to be hire-able — you need one track deep enough to *demonstrate*, plus
a project you can show. That shapes the order below.

---

## Goal 1 — Verilog · RTL design fundamentals  **(ACTIVE — `subjects/verilog/`)**

**Why first:** it is the substrate. Every later goal assumes you think in *registers + combinational
clouds per clock edge* and can write synthesizable RTL. Skipping straight to SystemVerilog/UVM
without this is the #1 mistake the roadmap sources warn against ("don't rush UVM without basics").

**What "done enough to move on" looks like (the exit bar):**
- Comfortable across structural / dataflow / behavioral styles; combinational *and* clocked logic.
- Owns the thresholds: hardware-is-concurrent (T1), blocking vs nonblocking + the event queue (T2),
  synthesizable subset / sim-synth mismatch / latch inference (T3), `reg`≠register (T4), the RTL
  mindset (T5). *(All five are already researched in `subjects/verilog/knowledge-base/`.)*
- **A portfolio piece:** a synthesizable design built end-to-end with a self-checking testbench —
  ideally the **small processor capstone** (NPTEL Week 8 / EECS151 RISC-V). This is the artifact a
  recruiter can actually look at; it is logged as a scope-extension in the Verilog map (§6).

**Status:** knowledge base complete (`stage-2✓`, units 01–12); teaching not yet started (parked at
the Session-1 diagnostic). Syllabus-anchored to **IIT-KGP NPTEL (Sengupta)** + **Berkeley EECS151**.

---

## Goal 2 — SystemVerilog · the industry language  **(the literal "next language")**

**Why it's *the* next step, unambiguously:** Verilog (frozen at IEEE 1364-2005) was merged into
**SystemVerilog (IEEE 1800)** in 2009, and industry has largely moved to SV for new RTL *and* for
all modern verification. It is a strict superset — you don't throw Verilog away, you extend it. This
is why the existing Verilog base already ends with a **U12 SystemVerilog-migration** unit: the track
was built to hand off here.

**Two faces of SV (you meet both, then the fork decides which you push):**
- **SV for design:** `logic` (kills the wire/reg trap), `always_comb` / `always_ff` / `always_latch`
  (intent-explicit), `enum`, `struct`/`packed`, `interface`, packages. Cleaner, safer RTL.
- **SV for verification:** OOP (classes), constrained randomization, **SystemVerilog Assertions
  (SVA)**, functional **coverage** — the foundation UVM is built on.

**Becomes:** `subjects/systemverilog/` when reached. *Possible early pivot:* because the goal is a
*job*, we may start blending SV-for-design into late Verilog (U10/U12) rather than treating it as a
fully separate later subject — flagged in the Verilog map §6 as a learner sign-off point.

---

## Goal 3 — the fork: pick a track and go deep

The sources are blunt about this: **learn ONE track deeply and build projects** rather than
sampling everything. Both forks share Goals 1–2; they diverge here.

### Goal 3A — RTL Design + Microarchitecture  *(front-end design)*
You *create* the hardware. Adds: computer architecture & **microarchitecture** (pipelining, hazards,
memory hierarchy), standard **bus/interconnect protocols** (AMBA **AXI**/AHB/APB), arithmetic/datapath
design, low-power intent, and **timing closure** (reading STA reports, fixing setup/hold). Tools:
synthesis (Synopsys Design Compiler / Cadence Genus), FPGA flows.
- *Demand note:* fewer seats than DV, but deep architectural skill is highly valued and durable.

### Goal 3B — Design Verification (DV)  *(prove the hardware is correct)*
You *break* and *prove* the hardware. Adds: **UVM** (Universal Verification Methodology — the
industry-standard SV verification framework: agents, sequences, scoreboards), constrained-random &
**coverage-driven** verification, advanced SVA, and **formal verification** (equivalence/model
checking). Tools: Synopsys VCS, Cadence Xcelium, Siemens Questa.
- *Demand note:* the sources consistently say DV has the **larger head-count and more openings** —
  often the easier first job to land. Strong reason to consider 3B if "get hired" is the priority.

> **Decision is deferred, on purpose.** You don't choose now. The choice gets made *during* Goal 2,
> once you've felt both faces of SystemVerilog and know which one you'd rather do all day. The engine
> will run that as an explicit, informed decision then — not a guess today.

---

## Cross-cutting skills — learn *alongside*, never "after"

These don't get their own goal number because they're picked up *while* doing 1–3, but they are
non-optional for employability (every internship source lists them):
- **Scripting:** **TCL** (drives every EDA tool), **Python** (automation, modeling, checkers),
  shell/Makefiles. Even basic fluency is a differentiator on a fresher resume.
- **The toolflow & Linux:** simulators (open: Icarus/Verilator; pro: VCS/Questa/Xcelium), synthesis,
  and for FPGA: Vivado/Quartus or open Yosys+nextpnr — on a Linux command line.
- **Version control (Git)** and clean, readable, reviewable RTL/testbench code.
- **Static Timing Analysis (STA)** literacy: setup/hold, clock domains — already seeded in Verilog U11.

---

## Goal 5 — specialize (far horizon, after you're employed/interning)

Branch once you have a foothold: **SoC integration**, **low-power design (UPF)**, **DFT**
(design-for-test / scan / ATPG), deep **formal verification**, **AI-hardware accelerators**,
**RISC-V** ecosystem work, **chiplet / 3D-IC** architecture, hardware security. The sources flag
these as the emerging, well-paid frontiers — but they're specializations *on top of* a solid 1–3,
not entry points.

---

## How this roadmap is used by the engine (operating rules)

1. **One active subject at a time.** Verilog is active; Goals 2+ are **scaffolded here, not built.**
   No knowledge base exists for them yet — by design (same discipline as the engine itself: build a
   subject's base to `stage-2✓` *before* teaching it).
2. **Teaching gate is unchanged.** When a later goal becomes a subject, its KB is researched to
   `stage-2✓` from primary sources first. This doc never authorizes teaching from a roadmap bullet.
3. **Moving-field recheck.** The *backbone* (Verilog → SV → design/DV fork → specialize) is stable.
   The *specifics* (which tools/skills are hottest, demand balance, what a given employer asks) drift
   — re-verify them when each subject launches, and stamp the date. Don't quote a demand claim here
   as a timeless fact.
4. **Sequencing within a goal** still obeys scoring-over-depth + the prerequisite graph; this doc
   only orders the *goals*, not the lessons inside them.
5. **Promotion path:** when ready for Goal 2, create `subjects/systemverilog/` via the normal subject-
   creation flow (`subjects/README.md`), link it back here, and flip its line below to *active*.

### Track status
| # | Goal | Subject | Status |
|---|------|---------|--------|
| 1 | Verilog (RTL fundamentals) | `subjects/verilog/` | **active** — KB `stage-2✓`, teaching not started |
| 2 | SystemVerilog (industry language) | `subjects/systemverilog/` *(not created)* | scaffolded |
| 3A | RTL design + microarchitecture | *(tbd)* | scaffolded — fork |
| 3B | Design Verification / UVM | *(tbd)* | scaffolded — fork |
| 5 | Specialization | *(tbd)* | far horizon |

---

## Sources (track sequence & employability — moving-field, dated 2026-06-29)

> These ground the *roadmap shape and the what-employers-want claims*. They are roadmap/industry
> sources (Tier 2–3 by `subject-research-protocol.md`): good for **sequence and emphasis**, never the
> final word on a *technical truth* — that is always built from primary sources when the subject is.

- **IIT Kharagpur NPTEL — *Hardware Modeling using Verilog*** (Sengupta) — Verilog syllabus anchor;
  W8 "processor design" motivates the capstone. https://onlinecourses.nptel.ac.in/noc22_cs94/preview
- **UC Berkeley EECS151** — digital-design + FPGA/ASIC flow + RISC-V capstone framing.
  https://www.eecs151.org/
- **m3y54m/FPGA-ASIC-Roadmap** (GitHub) — community FPGA/ASIC career roadmap; corroborates the
  design-vs-verification fork and the cross-cutting skill set. https://github.com/m3y54m/FPGA-ASIC-Roadmap
- **Industry/training roadmap commentary** (guvi VLSI roadmap, chipxpert career roadmap, vlsiguru /
  vlsifirst internship guides, mosartlabs RTL-vs-PD) — convergent on: strong digital fundamentals +
  Verilog/SystemVerilog → UVM for DV; scripting (TCL/Python) expected; front-end (design+DV) vs
  back-end (physical design) split; "go one track deep + build projects." *Accessed 2026-06-29; treat
  as orientation, re-verify specifics per subject launch.*
- **Primary anchors for technical truth** (already in `subjects/verilog/knowledge-base/sources.md`):
  IEEE 1364 / IEEE 1800, Harris & Harris, Cummings SNUG. The roadmap defers all *truth* to these.
