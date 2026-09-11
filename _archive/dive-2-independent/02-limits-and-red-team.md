# 02 — Limits & Red-Team Findings

This is the adversarial half: the genuine boundary conditions and weaknesses. None of these
overturn the engine, but each one *sharpens* it and guards against over-claiming. A teacher who
knows the limits applies the techniques better.

## 1. Lab evidence is strong; *classroom-over-time* evidence is thinner

**EEF review (University of Birmingham):** even for the best-supported principles — retrieval
practice, spacing, worked examples — the evidence "for the application of cognitive science
principles in everyday classroom conditions is **limited**." Most foundational studies are
short-term lab experiments.

**Caveat to the caveat:** this is a "we need more field studies" verdict, not a "it fails in the
field" verdict — and Agarwal's classroom program (`01 §3`) *is* positive field evidence for
retrieval practice specifically. **Implication for the engine:** trust most the techniques that
have *both* lab and classroom support (retrieval, spacing); treat the rest as well-evidenced in
principle but apply-and-observe.

## 2. Transfer is real but *weaker* than direct retrieval — and needs initial success

**Pan & Rickard (2018):** transfer effect d = 0.40, but explicitly **"less potent than the
corresponding direct testing effect,"** and **"the transfer effect disappears completely for
particularly poor performance."** Moderators: initial accuracy, response congruency, and
*elaborated* retrieval practice.

**Implication for the engine:** retrieval only transfers if the learner can *succeed* at it
reasonably often — which is exactly why the ~80% success target (`../research/03 §1`) matters.
Quizzing a learner who's failing isn't building transferable knowledge. Get them to a foothold
first, prefer *elaborated* retrieval (explain, don't just name), then test for transfer.

## 3. Interleaving: block FIRST, then interleave (the first dive's caveat, confirmed & sharpened)

The first dive said "don't interleave too early." The independent search confirms and sharpens:

- Blocked practice **gives better initial acquisition**; interleaving **hurts** initial
  performance while **helping** long-term retention/transfer (a textbook desirable difficulty).
- "**If learners do not reach a minimum threshold of prior achievement/accuracy during practice,
  they will not be able to effectively respond to the cognitive overload caused by
  interleaving.**" Novices benefit from initial blocking's predictability and fluency.
- The evidenced pattern: **block to a minimum competence, then switch to interleaving** to force
  discrimination between categories.

**Implication for the engine:** interleaving is a step-7 move (`../research/03 §6`) *for a
reason* — never the opening move. Block until ~accurate, then mix.

## 4. The testing effect with *complex* materials is debated (but survives)

**van Gog & Sweller (2015)** argued the testing effect **decreases or disappears as material
complexity (element interactivity) rises**. This was rebutted (Karpicke & Aue; Rawson and
others): the rebuttal notes "element interactivity" was never operationalized quantitatively,
the relevant studies didn't manipulate it, and several studies *do* show retrieval benefits with
complex materials.

**Honest synthesis:** the testing effect is **robust but likely smaller for highly complex,
high-element-interactivity material** than for simple facts. **Implication:** for hard, deeply
interconnected topics, still use retrieval — but scaffold it (worked-example recall, structured
prompts) rather than expecting cold free-recall to work as well as it does for facts.

## 5. "Desirable difficulties" are NOT one-size-fits-all (aptitude–treatment interactions)

A recurring red-team theme: the same manipulation helps some learners and harms others.

- **Prior knowledge** moderates everything (the expertise-reversal effect — what helps novices
  harms experts and vice versa).
- **Working-memory capacity** moderates: **lower-WMC learners benefit *more* from worked
  examples** (which offload WM) and are *more* easily overloaded by unguided difficulty.
- Poorly-fitted difficulty doesn't just fail to help — it can **"emotionally upset and
  de-motivate"** the learner.

**Implication for the engine:** this is the strongest possible vindication of *diagnose-then-
adapt* (`../research/01 §3`, `teaching-manual.md §4`). A fixed difficulty for all learners is
wrong; the engine's continual re-diagnosis is not optional polish — it's load-bearing.

## 6. Cognitive Load Theory: useful framework, but watch its soft spot

**The falsifiability critique:** once "germane load" was introduced, CLT risked becoming
unfalsifiable — any result could be explained post-hoc (performance drop = "extraneous load,"
performance gain = "germane load"), with no independent way to measure either. Notably,
**Sweller himself responded by dropping germane load as a separate category.**

**Implication for the engine:** keep using CLT's *actionable* parts — minimize extraneous load,
sequence intrinsic load, respect WM limits (these are well-supported and concrete) — but don't
treat CLT as a precise predictive law or invoke "germane load" as an explanation. Use it as a
design heuristic, which is exactly how `../research/01 §2` frames it.

## Net effect on the engine

Every limit here either (a) confirms an existing caveat (interleaving timing, expertise
reversal) or (b) reinforces the engine's core design choices (the 80% success target, continual
diagnosis, minimizing extraneous load). **Nothing here breaks the engine. It makes it more
precise.** The one thing that changes the *tone* of all claims is effect-size inflation —
covered next.
