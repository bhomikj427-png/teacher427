# Research Base — Overview, Standard & Reconciliation

This folder (`research/`) is the **canonical evidence base** for the `ece'` teaching engine. It
supersedes two earlier research dives by merging them and adding techniques both missed. Those
dives are preserved as a frozen **audit trail**, not as live references:

- `../_archive/dive-1-original/` — Dive 1 (the original deep dive).
- `../_archive/dive-2-independent/` — Dive 2 (independent red-team review + corrections).
- `research/` (this folder) — the reconciled, deduplicated, corrected synthesis.

---

## The evidentiary bar (unchanged, non-negotiable)

A technique is included **only** if it clears all three:
1. **Replicated empirical support** (meta-analyses / multiple independent studies, not one paper
   or a popular book).
2. **A real, measured effect size** — measurably improves learning, not merely "feels productive."
3. **Measured on learning outcomes** (retention, transfer, comprehension) — **not** engagement,
   focus, or self-rated confidence.

Exclusions are themselves justified with evidence (see `06`).

## Read this first: effect sizes are inflated — claim robustness, not magnitude

The independent dive established that education/psychology effect sizes are **systematically
inflated** by publication bias: ~800 education meta-analyses average **d ≈ 0.40**, but
pre-registered large RCTs average **d ≈ 0.06**; multi-lab replications run ~⅓ the meta-analytic
size. **Every effect size below is an optimistic upper bound.** Therefore this base ranks
techniques by **robustness and replication (especially in real classrooms)**, not by headline
magnitude, and the engine should claim methods are "well-supported and worth doing," never
"guaranteed to produce effect size X." Full treatment: `07-effect-size-honesty.md`.

---

## Master tier table

| Tier | Technique / principle | Status & headline basis | File |
|---|---|---|---|
| **Top (lab + classroom)** | Retrieval practice | Adesope g≈0.5–0.7; **+1 grade level in 5-yr classroom study** (Agarwal); transfers d=0.40 (Pan & Rickard) | 02 |
| **Top (lab + classroom)** | Spaced practice | ~doubles recall ≥1wk (Cepeda); EEF-endorsed; consolidates over sleep | 02 |
| **Top (combines the two best)** | **Successive relearning** ★new | Rawson & Dunlosky: retrieval+spacing to mastery; real exam gains | 02 |
| **Strong** | Self-explanation & elaboration | g=0.55 (Bisra); independently listed by Weinstein 2018 | 02 |
| **Strong** | Generation / pretesting / **productive failure** ★new | Pretesting (Richland); PS-I g=0.36 (Sinha & Kapur) — *conceptual only* | 02 |
| **Strong** | Worked examples + faded guidance | widely replicated for novices (Sweller); bounded by expertise reversal | 02, 03 |
| **Strong** | Dual coding / multimedia | large d's (Mayer) — *but most inflated; trim confidence* | 02 |
| **Solid** | Interleaving | g=0.42 (Brunmair) — **block first, then interleave** | 02 |
| **Solid** | **Concreteness fading** ★new | Fyfe systematic review; best transfer; generalizes | 02 |
| **Solid** | **Learning by teaching / protégé** ★new | Fiorella & Mayer d=0.30–0.59; the evidenced "Feynman" | 02 |
| **Framework** | Generative learning (SOI) ★new | Fiorella & Mayer — unifies generation techniques; resolves summarization | 02 |
| **Method** | Explicit instruction (Rosenshine), scaffolding, mastery, tutoring | converging evidence; tutoring real effect ~0.37–0.79 SD (not Bloom's 2σ) | 03 |
| **Assessment** | Formative assessment + feedback protocol | powerful but ~38% of feedback cases *negative* (Kluger & DeNisi) | 04 |
| **Mechanism** | Sleep & consolidation ★new | robust; the reason spacing works & cramming fails | 01 |
| **Contested — small** | Growth mindset | small & conditional: +0.10 GPA for at-risk in supportive schools (Yeager 2019) | 05 |
| **Contested — overstated** | Deliberate practice | only 4% of variance in education (Macnamara) | 05 |
| **EXCLUDED** | Learning styles · Pomodoro · rereading · highlighting · passive summarizing | no learning-outcome evidence / debunked | 06 |

★new = verified in the final gap-check; neither earlier dive had it.

---

## How this folder was produced: reconciliation & gap analysis

The user's explicit step: compare the two dives, find what each missed, verify the gaps online,
then merge. Here is exactly what that found.

### Gaps in Dive 1 that Dive 2 fixed (now incorporated)
- **No effect-size-inflation caveat** → added (`00` above, `07`).
- **Growth mindset too dismissive** ("WEAK, don't bother") → corrected to "small & conditional,
  real for at-risk learners" via Yeager 2019 (`05`).
- **Lab-vs-classroom distinction under-weighted** → made explicit; top tier now means
  *lab + classroom* evidence (`02`, `07`).
- **Retrieval transfer treated as automatic** → qualified: weaker than direct effect, needs
  adequate initial success (`02`).
- **Interleaving "block-first" only weakly stated** → sharpened to a rule (`02`).
- **CLT presented with too little hedging** → "germane load" soft spot noted (`01`).

### Gaps in Dive 2 relative to Dive 1 (so the merge keeps Dive 1's substance)
- Dive 2 was a *commentary* layer: it did not restate the full technique catalog, teaching
  methods, feedback protocol, motivation, or the excluded myths. The final folder restores all of
  that from Dive 1, corrected.
- Dive 2 took the **exclusions on trust** (didn't re-verify Pomodoro/learning styles). The final
  folder keeps Dive 1's evidence-based exclusions (`06`).

### Gaps BOTH dives had → verified online → now included
Six techniques neither dive covered were checked against the bar and **passed**: successive
relearning, productive failure (conceptual only), learning by teaching, concreteness fading, the
generative-learning framework, and sleep/consolidation. Details and effect sizes in `02`/`01`;
the verification searches are cited in `sources.md`.

### One genuine tension resolved
**Worked examples (instruct-first) vs. productive failure (problem-solve-first)** appear to
contradict. They don't — they apply to different goals: worked examples build **procedural
fluency** in novices (lower load); productive failure builds **conceptual understanding and
transfer** by making the learner feel the gap before instruction. The engine chooses based on the
objective (`03 §`). Likewise **summarizing**: passive summarizing is low-utility (Dunlosky), but
*generative* restructuring (mapping/self-explaining) works — the difference is whether the
learner truly generates (`02`, generative framework).

---

## File map
- `01-how-learning-works.md` — cognitive architecture + sleep/consolidation (the *why*).
- `02-core-techniques.md` — every validated technique, merged + the 6 new ones.
- `03-teaching-methods.md` — how to sequence instruction; the worked-example/PF reconciliation.
- `04-assessment-and-feedback.md` — measuring understanding; the feedback protocol.
- `05-motivation-and-metacognition.md` — metacognition, SDT, the corrected caveats.
- `06-excluded-and-contested.md` — what failed the bar, with reasons.
- `07-effect-size-honesty.md` — the inflation caveat and how to claim evidence honestly.
- `sources.md` — unified citations (both dives + gap-check).
