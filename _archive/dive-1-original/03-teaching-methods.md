# 03 — Teaching Methods (How to Structure Instruction)

`02` covers what the *learner* does. This file covers how the *teacher* sequences and delivers
instruction. The two strongest, best-evidenced frameworks are explicit instruction
(Rosenshine) and the scaffolding/mastery tradition.

---

## 1. Explicit / direct instruction — Rosenshine's Principles of Instruction

Barak Rosenshine (2012) distilled **ten principles** from three converging sources: cognitive
science of memory, observation of master teachers (those whose students gained most), and
research on cognitive supports / intelligent tutoring. The convergence of three independent
sources is what gives it weight.

**The ten principles:**

1. **Begin with a short review** of prior learning (daily/weekly review — leverages spacing &
   retrieval).
2. **Present new material in small steps**, with student practice after each step (respects WM
   limits — see `01`).
3. **Ask a large number of questions** and check the responses of all students (retrieval +
   checking for understanding, not "any questions?").
4. **Provide models** and worked examples (worked-example effect).
5. **Guide student practice** — supervise initial practice closely.
6. **Check for understanding** frequently; obtain a high success rate before moving on.
7. **Obtain a high success rate** — aim for ~**80%** correct during guided practice. Lower
   means material is too hard / steps too big; much higher means it's too easy.
8. **Provide scaffolds** for difficult tasks; fade them as competence grows.
9. **Require independent practice** — students need extensive successful solo practice to reach
   fluency / automaticity.
10. **Engage in weekly and monthly review** (spacing again).

**Scope/limits (honest):** strongest when the goal is to *master a defined body of knowledge or
a procedure with clear steps*. For open-ended creative or ill-defined tasks, pure explicit
instruction is less sufficient — guided discovery with strong support fits better. (Note:
*unguided* discovery learning for novices is poorly supported — novices lack the schemas to
discover efficiently and tend to overload or learn misconceptions.)

---

## 2. Scaffolding and the Zone of Proximal Development (Vygotsky)

**ZPD:** the band between what a learner can do alone and what they can do *with support*.
Effective teaching operates inside this band — material just beyond independent ability but
reachable with help.

**Scaffolding:** temporary support (hints, prompts, partial solutions, structure) that lets the
learner succeed at something they couldn't do alone, **removed progressively** as they
internalize the skill. This is the pedagogical sibling of guidance fading (`02 §7`) and
directly serves the "desirable difficulty" calibration: keep the task hard-but-reachable.

**How to apply:** Diagnose the edge of current ability, pitch tasks just beyond it, support
with the *minimum* hint needed (not the full answer), and withdraw support as the learner
succeeds.

---

## 3. Mastery learning (Bloom)

**What:** Learners must demonstrate mastery of a unit (typically ~80–90% on a formative check)
*before* progressing. Those who haven't reach mastery get corrective instruction and re-test;
the bar is fixed and time is variable (the inverse of traditional teaching).

**Evidence (honest):** Bloom (1984) originally reported ~1σ effects. Modern syntheses find more
modest but still real benefits, and the approach's logic — *don't build on a shaky foundation*
— is sound and complements cognitive load theory (you can't form higher schemas on missing
prerequisites).

**How to apply:** Gate progression on demonstrated retrieval-based mastery, not on coverage or
elapsed time. When a check fails, re-teach differently and re-test before advancing.

---

## 4. Tutoring and Bloom's "2 sigma problem" — with the myth corrected

Bloom (1984) reported that **one-to-one tutoring** produced a ~**2 standard deviation** gain
over conventional classes and posed the "2 sigma problem": find scalable methods that match it.

**The honest, current picture:**
- Modern meta-analysis (Nickow, Oreopoulos & Quan, 2020) of randomized tutoring studies:
  average effect ≈ **0.37 SD**. **None of 96 studies reached 2σ.**
- Intelligent tutoring systems (VanLehn synthesis): **d ≈ 0.76**, approaching human tutoring's
  **d ≈ 0.79**.

**Takeaway:** the *mythic* 2σ figure is not reliably reproduced — but tutoring's *real* effect
(~0.4–0.8 SD) is still large and among the most powerful interventions known. A 1-to-1
adaptive tutor (which is what this engine is) is operating in the best-evidenced format there
is. We claim the realistic number, not the legend.

---

## 5. Socratic questioning / guided discovery — where it fits

Questioning that leads a learner to construct understanding has real value — but its benefit
comes from the **retrieval, generation, and self-explanation** it forces (`02`), not from
"discovery" per se. It works **when the learner has enough prior knowledge** to reason
productively; for true novices it collapses into guessing and overload.

**How to apply:** Use Socratic questioning to *activate and extend* existing knowledge and to
drive self-explanation. For brand-new material with no foothold, lead with explicit
instruction + worked examples first, then switch to questioning once there's something to
reason *from*.

---

## 6. The synthesized instructional sequence

Combining the above with `01`–`02`, a single piece of new material should move through:

```
1. ACTIVATE   → review prior related material (spacing/retrieval) + pretest/predict (generation)
2. PRESENT    → explicit, small steps, low extraneous load, words+visuals (CLT + multimedia)
3. MODEL      → worked example, think aloud (worked-example effect)
4. GUIDE      → completion problems + heavy questioning, self-explanation, ~80% success
5. CHECK      → retrieval-based check for understanding; gate on mastery
6. FADE       → withdraw scaffolds; independent practice toward fluency
7. INTERLEAVE → mix with other learned types once individually solid
8. SPACE      → schedule expanding-interval retrieval in future sessions
```

This loop is the backbone of the teaching manual. Each step cites a specific, evidenced reason
for existing — nothing is there for decoration.
