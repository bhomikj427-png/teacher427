# ECE2120 Circuits & Network Theory — 00 MAP (Stage 1, MUJ level)

> Big ideas, prerequisite graph, threshold concepts, scope, and the standing to-verify register.
> Built to `../../../../subject-research-protocol.md`. Scope = the official unit list in
> `../course-info.md` (syllabus text is `settled` — verbatim from the MUJ PDF). Content is canonical
> textbook material (Van Valkenburg / Sudhakar-Shyammohan / Hayt) — `settled` unless marked.

## The handful of big ideas (the expert's organizing schema)

1. **The complex frequency `s = σ + jω` is the one variable the whole subject lives in.** A resistor,
   inductor and capacitor become *one* object — an **impedance Z(s)** (R, sL, 1/sC). Every later
   idea (transients, two-ports, network functions, synthesis) is "what does this circuit's Z(s) or
   H(s) look like, and where are its poles and zeros?" Master "the circuit *is* a function of s" and
   the course unifies. *[Van Valkenburg ch.1–4; Hayt ch.14–16]*
2. **A network function H(s) is a ratio of polynomials in s; its poles and zeros are its DNA.**
   Poles = the circuit's **natural frequencies** (how it rings/decays on its own); zeros = where it
   blocks. The *transient* response is read off the poles; the *steady-state* off H(jω); *stability*
   off whether poles sit in the left half-plane. One object, three readings.
3. **Linearity buys you the theorems.** Superposition, Thévenin, Norton, and maximum-power-transfer
   are all consequences of the circuit being a *linear* map from sources to responses. They let you
   replace any one-port by `V_th` in series with `Z_th` — the move that makes big circuits tractable.
4. **Analysis and synthesis are inverse arrows.** Analysis: given the circuit → find H(s). Synthesis:
   given a *desired* H(s) → build a circuit that realizes it. The hinge between them is **realizability**
   — *which* functions H(s) can actually be an impedance of a passive RLCM network. The answer is the
   **positive-real (PR) function** (★ threshold), and the constructive recipes are **Foster & Cauer**.
5. **A two-port is a 2×2 matrix of network functions.** Z, Y, h, ABCD parameters are four coordinate
   systems for the *same* black box; reciprocity and symmetry are structural facts visible in each.
   Cascading/series/parallel connections become matrix products/sums — the engineering payoff.

## Prerequisite graph (load-bearing — triangulated, `settled`)

```
Circuit fundamentals (KVL/KCL, R-L-C v–i laws, phasors, impedance Z(s)=R, sL, 1/sC)
   │
   ├─► U1 Network theorems (superposition → Thévenin/Norton → max power transfer; dependent sources)
   │
   ├─► [Laplace transform + initial conditions]
   │        │
   │        └─► U2 Transient analysis (1st/2nd order; impulse/step/ramp/sinusoid;
   │                                    time-domain ↔ transform-domain; initial & final value)
   │
   └─► U4 Network functions (driving-point Z/Y & transfer fns; poles/zeros;
            │                  stability & causality; Hurwitz polynomial; PR function ★)
            │
            ├─► U3 Two-port networks (Z,Y,h,ABCD; interrelations; interconnection;
            │                          image impedance; symmetric T & π; filters)
            │
            └─► U5 Network synthesis (reactance functions; Foster I/II; Cauer I/II;
                                       RL, RC, LC realization)
```

**Teaching order (topological):** U1 → U2 → U4 → U3 → U5. *Rationale:* theorems (U1) need only
fundamentals; transients (U2) add the Laplace/s-domain machinery; **network functions (U4) are the
prerequisite spine for both two-ports (U3) and synthesis (U5)** — you cannot judge realizability
(PR/Hurwitz, U5) or write two-port parameters as functions of s (U3) without the pole-zero / network-
function language of U4. The official syllabus *lists* two-ports before network functions; we **teach
U4 before U3/U5** for prerequisite soundness (the syllabus order is a list, not a dependency claim).

## Threshold concepts (budget extra teaching here — where learners stall)

- **★ The complex-frequency variable s and the pole-zero plane.** That `s` is simultaneously
  "jω for steady state," "σ for decay," and "the Laplace variable" is the conceptual hinge of the
  whole subject. Learners who keep s as "just a symbol" never connect transient ↔ frequency ↔
  stability. *Once grasped, U2, U4, U5 stop being three separate courses.*
- **★ Poles = natural frequencies.** That the denominator roots of H(s) *are* the exponents in the
  source-free time response (e^{p t}) — and that LHP poles ⇒ decay/stable, jω-axis poles ⇒ sustained
  oscillation, RHP poles ⇒ growth/unstable — is the idea everything downstream rests on.
- **★ The positive-real (PR) function — the realizability gate.** *Which* H(s) is a physical passive
  impedance. This is the single hardest idea of synthesis and the bridge from analysis to synthesis;
  Hurwitz polynomials and the Foster/Cauer recipes all hang off it (`05-network-synthesis.md`).
- **★ t = 0⁻ vs t = 0⁺ and the continuity rules** (inductor current and capacitor voltage cannot jump
  for finite energy). The root of most transient-analysis errors is sloppy initial conditions.

## Scope (Stage 1 = the official units; cover all, don't exceed)

U1 Network theorems & elements · U2 Transient analysis · U3 Two-port networks · U4 Network functions
· U5 Network synthesis. (Lab is separate — hardware/software circuit analysis; not a content unit.)
Per-unit notes: `01`–`05`. **Flexi Core 1:** confirm whether the learner is enrolled in ECE2120
(this subject) or ECE2121 (Linear Integrated Circuits) before teaching — research covers both.

## Open questions / to-verify register

- `[opened 2026-06-22]` **No PYQ/PPT ingested** — `../exam-pack/` is empty, so `exam-map.md` is a
  provisional `uncertain` stub: revision priority is inferred from topic structure, **not** exam
  evidence. *Resolve by:* dropping MUJ MTE+ETE papers + course PPTs into `../exam-pack/` (via
  `../../_inbox/`) and rebuilding the exam-map. (See `../../research-engine/exam-resources.md`.)
- `[opened 2026-06-22]` **MTE/ETE mark weightage** for ECE2120 — unverified (no handout/PYQ in hand).
- `[opened 2026-06-22]` **Flexi enrollment** — which of ECE2120 / ECE2121 the learner actually takes
  is unconfirmed; affects whether this subject is taught at all. *Resolve by:* ask the learner.
- `[opened 2026-06-22]` **Which prescribed text the professor follows** — five texts are listed
  (`course-info.md`); Van Valkenburg is the synthesis/network-functions anchor, Sudhakar-Shyammohan
  & Hayt the analysis/transient anchors. Emphasis split is `uncertain` pending PPTs.
