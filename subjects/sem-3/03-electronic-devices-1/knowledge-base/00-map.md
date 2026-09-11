# ECE2101 Electronic Devices-I — 00 MAP (Stage 1, MUJ level)

> Big ideas, prerequisite graph, threshold concepts, scope, and the standing to-verify register.
> Built to `../../../../subject-research-protocol.md`. Scope = the official unit list in
> `../course-info.md` (syllabus text is `settled` — verbatim from the MUJ PDF). Tier-1 truth =
> Boylestad 10e + Sedra-Smith 7e + Neamen 4e + Streetman 7e (`sources.md`).

## The handful of big ideas (the expert's organizing schema)

1. **Two carriers, two transport mechanisms — that's the whole substrate.** Everything downstream
   is electrons and holes moving by **drift** (field-driven, J=σE) and **diffusion** (gradient-
   driven, J=qD·dn/dx). Doping sets *how many* carriers; transport sets *how they move*. Master
   "carriers + drift + diffusion" and every device is a boundary-condition problem on top.
2. **The PN junction is the atom of all devices.** A junction is just n-type meeting p-type → a
   built-in field across a depletion region. Forward bias lowers the barrier (current floods),
   reverse bias widens the depletion region (current chokes). Diode, BJT (two junctions), JFET
   (reverse-biased gate junction), MOSFET (junction-isolated) — **all are junctions under bias.**
3. **A device is a *controlled* current path.** A diode is uncontrolled (1 terminal pair). A
   transistor adds a *third terminal that modulates the path*: BJT modulates with base **current**
   (charge injection); FETs modulate with gate **voltage** (a field that opens/pinches a channel).
   Current-controlled vs voltage-controlled is the deepest BJT-vs-FET split.
4. **Every transistor has the same three-act life: cutoff → active/saturation → on.** The names
   differ by device (BJT: cutoff/active/saturation; MOSFET: cutoff/triode/saturation) but the
   structure is identical — off, a region where it amplifies (acts as a controlled source), and a
   region where it's a closed switch. Bias picks the act; the act picks the model.
5. **Large-signal sets the operating point; small-signal linearizes around it.** DC analysis finds
   Q-point (where on the curves you sit); then you replace the device with a *linear* small-signal
   model (gm, rπ, ro) to find gain. **Bias first, then amplify** — this two-step is the spine of
   the analog half of the course.
6. **The MOSFET is the protagonist of modern electronics.** JFET and BJT are foundational and still
   used, but the MOSFET — voltage-controlled, scalable, low static power in CMOS — is *why* the
   syllabus ends on it as a switch and as the basis of digital logic. The arrow points at VLSI.

## Prerequisite graph (load-bearing — triangulated, `settled`)

```
                 Atomic/bonding + energy bands (intrinsic Si)
                              │
                 Doping → extrinsic (n/p), carrier conc. (n·p = ni²)
                              │
        ┌─────────────────────┴─────────────────────┐
   Drift (mobility,                            Diffusion
   resistivity, sheet R)                     (D, Einstein D/μ=kT/q)
        └─────────────────────┬─────────────────────┘
                              ▼
                 PN JUNCTION  (built-in field, depletion region)
                 ├─ electrostatics (Poisson) → depletion width, Vbi, junction C
                 ├─ continuity → diode (Shockley) equation, I-V
                 ├─ breakdown (avalanche, Zener), Schottky, switching/charge storage
                 └─ diode CIRCUITS (rectifier, clipper, clamper, Zener regulator)
                              │
        ┌─────────────────────┼──────────────────────┐
        ▼                     ▼                       ▼
      JFET                 MOSFET                    BJT
  (reverse-biased    (MOS-capacitor → inversion   (two junctions; base
   gate pinches       channel; triode/sat;         current controls
   channel)           CS/CG/CD; switch; digital)   collector current)
        └─────────────────────┼──────────────────────┘
                              ▼
              SMALL-SIGNAL MODELS + amplifier configs
              (Q-point → linearize → gm/rπ/ro → gain)
                              │
                              ▼
                  BJT ↔ MOSFET comparison; MOSFET → digital logic
```

Topological teaching order = the official unit order: **U1 semiconductor physics → U2 PN junctions
(+ diode circuits) → U3 JFETs → U4 MOSFETs → U5 BJTs.** Note: U1→U2 is the hardest, most load-
bearing edge (junction electrostatics rests entirely on drift/diffusion + doping). FETs and BJT all
sit on the junction, so U2 must be solid before any transistor.

## Threshold concepts (budget extra teaching here — where learners stall)

- **★ Drift vs diffusion, and that both currents coexist.** Novices think "current = drift" (Ohm's
  law instinct). Diffusion current — driven by a *concentration gradient*, not a field — is the
  one they miss, yet it *dominates* the forward-biased diode. The Einstein relation D/μ=V_T tying
  them is itself a threshold.
- **★ The depletion region and the built-in potential.** That a junction in *equilibrium*, with no
  battery, has an internal field and a voltage (Vbi) you can't measure with a voltmeter — because
  it's exactly cancelled by contact potentials — is deeply counterintuitive and the root of most
  junction errors.
- **★ "The transistor is a controlled source," not a magic amplifier.** Seeing the BJT's collector
  as a current source set by base current (or the MOSFET's drain as one set by VGS) — *independent
  of the drain/collector voltage in the active region* — is the gateway to all amplifier analysis.
- **★ Inversion in the MOSFET.** That a *voltage* on an insulated gate, touching nothing
  conductively, induces a conducting channel of the *opposite* type to the substrate, with a sharp
  threshold (Vt). The capacitor-that-becomes-a-resistor mental model is the threshold.
- **★ Large-signal vs small-signal (Q-point then linearize).** Two analyses of the *same* circuit
  for *different* questions (where do I sit / how much do I amplify). Conflating them — e.g. using
  small-signal gm at zero bias — is a classic stall.

## Scope (Stage 1 = the official units; cover all, don't exceed)

U1 Semiconductor physics fundamentals · U2 PN junctions (+ diode circuits, breakdown, Zener,
Schottky) · U3 JFETs · U4 MOSFETs (incl. as switch + digital) · U5 BJTs (+ comparison with MOSFET).
Per-unit notes: `01`–`05`. The official syllabus groups these as ~5 blocks; exact MUJ unit/MTE-ETE
boundaries pending the handout + PYQs (`exam-map.md`, register below).

## Open questions / to-verify register

- `[opened 2026-06-24]` **Exact MUJ unit boundaries + MTE/ETE split** — `course-info.md` syllabus
  text is verbatim/`settled`, but the partition into examined units and what falls in MTE vs ETE is
  unknown without the official handout/PYQs. *Resolve by:* dropping papers into `../exam-pack/` and
  rebuilding `exam-map.md`. Until then exam-targeting is `uncertain`, research is syllabus-driven.
- `[opened 2026-06-24]` **No PYQ/PPT ingested** — `exam-map.md` is a provisional stub; topic
  weightage is inferred from standard course emphasis + the textbook, not from MUJ evidence.
- `[opened 2026-06-24]` **Silicon intrinsic carrier concentration nᵢ — textbook discrepancy
  (`contested`, resolved-as-teach-the-spread).** Boylestad/older texts use nᵢ ≈ 1.5×10¹⁰ cm⁻³ at
  300 K; refined experimental value is ≈1.0×10¹⁰ (Sproul/Green); best modern measurement
  ≈9.65×10⁹ (Altermatt 2003). *(verified 2026-06-24: PVEducation; OSTI; Springer Silicon 2023.)*
  *Resolve by:* nothing to pin — **teach as "≈1.0–1.5×10¹⁰, textbook-dependent; use the value your
  exam's textbook uses."** Carries into every nᵢ²-based calc (n·p, I_S, Vbi). See `01` §intrinsic.
- `[opened 2026-06-24]` **Which prescribed textbook MUJ actually examines from.** course-info lists
  6; Boylestad is the standard ECE-UG anchor and Sedra-Smith for MOSFET/BJT small-signal. Treating
  Boylestad+Sedra as tier-1 for Stage 1, Sze/Streetman/Neamen for Stage 2. Confirm via handout.
- `[opened 2026-06-24]` **Paired lab ECE2130** (`../../08-electronic-devices-lab-1`) — diode/BJT/
  FET characteristic-curve experiments will re-scope emphasis once its KB/experiment list exists.
