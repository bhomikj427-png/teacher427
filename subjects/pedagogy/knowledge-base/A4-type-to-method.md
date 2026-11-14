# A4 — The Bridge: Kind of Information → Method

> Reads off the A3 §3 table ("A3 row N"). Every Part B entry will attach to a row here.
> **Grades:** **S** strong (meta-analytic, replicated) · **M** moderate (meta-analysis with real
> moderators/heterogeneity, or a few strong studies) · **T** thin · **X** not supported.
> Effect sizes are optimistic upper bounds (publication bias; engine `research/07`); quote them as
> "well-supported", never as a promise.
> Confidence tags: `settled` / `contested` / `uncertain` / `suspect`. Source IDs → `sources.md`.

---

## 1. The methods, with their evidence

| Method | What you do | Evidence | Grade | Main boundary |
|---|---|---|---|---|
| **Retrieval practice** (practice testing) | Produce the answer from memory, then check | D13 rated *high*; ATS17 meta (272 ES) moderate-to-large vs restudy; RK06; KB11; transfer d ≈ 0.40 (PR18) | **S** | Prompt type matters: verbatim prompts build verbatim knowledge (A1 §5); feedback needed when errors are likely |
| **Spacing** (distributed practice) | Spread sessions over time, across nights | D13 *high*; C06 (839 assessments): the best gap grows with how long you must retain | **S** | Very long gaps before any retrieval let retrieval strength fall to zero → relearn, don't abandon |
| **Successive relearning** | Retrieve to a criterion, then again on later days | RDS13 (real course, 2 experiments; abstract-level, numbers → S11); combines the two **S** methods above | **S** | Needs a criterion and scheduling |
| **Interleaving** | Mix categories or problem types instead of blocking them | BR19 meta: g = 0.42; paintings 0.67; stronger when categories look *similar to each other*; maths small but significant | **M** | Weak or reversed for words/expository text (BR19, verify S11); **block first, then mix** for novices (engine rule) |
| **Worked examples → fading** | Study a solved problem, then complete partial solutions, then solve alone | Worked-example effect (CLT; Sweller); KACS03; CRK22 (examples favoured skills) | **S** for novices | **Expertise reversal:** loses value or hurts once the learner knows the steps (KACS03, CKS17) |
| **Self-explanation** | Explain *why* each step or sentence is true, to yourself | Bi18 meta: g = 0.55 (64 reports) | **S** | Needs enough prior knowledge to generate explanations; quality of explanation matters |
| **Elaborative interrogation** | Ask "why would this be true?" of facts | D13 *moderate* (verify list at full text) | **M** | Works best with some prior knowledge |
| **Explicit, guided instruction** (vs minimal guidance) | Teacher shows and guides, then releases | KSC06 review | **S** for novices / `contested` at edges | Scaffolded inquiry and PBL ≠ minimal guidance (2007 rebuttals) |
| **Productive failure** (problem → then instruction) | Attempt a well-designed problem *before* being taught, then get instruction that builds on the attempts | SK21 meta: g = 0.36 [0.20, 0.51] for PS-I vs I-PS | **M** | Reversed for young learners (grades 2–5) and domain-general skills; the reported bias-adjusted g = 0.87 is unusual → `contested`; depends on design fidelity |
| **Pretesting** | Guess answers before studying | RKK09; KHB09; SCA24 preregistered meta: g = 0.54 on the asked items, **g = 0.04 on everything else** | **S** (asked items) | No general effect; factual > conceptual prequestions; answer must follow (A6 §5) |
| **Concept mapping** (constructing) | Draw the relationships yourself | Sch17: g = 0.58 overall; constructing 0.72 > studying 0.43; loses to retrieval in KB11 | **M** | Construction > studying given maps; not superior to retrieval |
| **Rereading / highlighting / summarizing** | — | D13 *low* | **T** | Feels productive (A1 §6) |
| **Deliberate practice** | Targeted practice on weaknesses with feedback, at the edge of ability | MHO14: explains 26% (games) … 4% (education) of variance | **M** for skills / small share in academic domains | Practice matters, but so do other factors; definitions disputed |

## 2. The bridge table (A3 row → methods)

| A3 row | Learning process (KLI) | First choice | Then / also | Avoid |
|---|---|---|---|---|
| **1 Facts** | Memory & fluency | **Retrieval practice + spacing** (successive relearning) | Pretesting before study; mnemonics for arbitrary items (D13 rates keyword mnemonic *low* for general use) | Rereading, highlighting |
| **2 Concepts / categories** | Induction & refinement | **Many varied examples, interleaved** across similar categories (BR19, KoB08) | Contrast cases side by side; ask "what feature decides it?" | Teaching one category at a time with near-identical examples |
| **3 Principles / models** | Understanding & sense-making | **Self-explanation** (Bi18) + **retrieval of explanations** (relational prompts) | Productive failure *if* the learner has prerequisites (SK21); elaborative interrogation; construct a concept map, then retrieve it | Memorizing the statement without derivation or use |
| **4 Procedures** | Induction → memory & fluency | **Worked examples → completion problems → independent practice** (fading, KACS03) | Self-explanation of steps; spaced, then interleaved practice; practice to speed | Problem-solving cold as a novice (KSC06); worked examples once the learner is fluent (expertise reversal) |
| **5 Conditional (when to use what)** | Induction | **Interleaved problem types** (must choose the method), **contrasting cases** | Ask "why this method, not that one?" (self-explanation) | Blocked practice only (choice never exercised) |
| **6 Metacognitive** | Understanding + regulation | Teach the illusions explicitly (A1 §6) **plus delayed self-tests that expose them** | Calibration practice: predict, test, compare (→ A7) | Trusting feelings of fluency |
| **7 Perceptual** | Induction | High-volume classification with immediate feedback (KMS10, `uncertain`) | Interleave confusable patterns | Long explanations instead of examples |
| **8 Motor** | Practice → fluency | Practice with feedback, staged from cognitive to autonomous (FP67) | Deliberate practice on weak sub-skills (MHO14) | Watching only |

**Confidence:** rows 1, 4: `settled` · rows 2, 3, 5: `settled` on the method, `contested` on
best sequencing (e.g. productive failure vs examples first) · row 6: `uncertain` (→ A7) ·
rows 7–8: `uncertain` / `settled` respectively.

## 3. Three rules that cut across rows

1. **Expertise changes the row's method** (KACS03, CKS17). The same material moves from
   "worked example" to "practice" as chunks form. Diagnose level first; re-diagnose often. `settled`
2. **Guidance first for novices; generation once something can be generated** (KSC06 vs SK21).
   - The two meta-analyses are compatible once prerequisites are counted.
   - Productive failure works when learners can make *informed* attempts (older learners, designed
     problems), and it is followed by instruction.
   - Minimal guidance with no instruction does not work for novices.
   - `contested` on exact boundaries.
3. **Desirable difficulty only within reach** (BB11, A1 §4). Interleaving, spacing and testing help
   only if the learner can succeed with effort (~80% success, engine principle 4).

## 4. Resolving the encoding-vs-retrieval split (prepares S10)
- The bridge table assigns **retrieval** a central role in rows 1, 3 and 4, but with *different prompts*:
  - row 1: recall the fact
  - row 3: recall and explain the relationship
  - row 4: produce the full solution
- Justin Sung's emphasis on encoding (organization, relationships) corresponds to rows 2, 3 and 5
  methods (contrasting, explaining, mapping).
- The evidence suggests **both, chosen by row**, rather than one over the other (CRK22 + KB11 + Bi18).
- Verdict deferred to S10.

## 5. Uses
- **As a learner:** for each chapter, split content by A3 row and run the matching first-choice
  method; schedule everything on spaced relearning.
- **As a teacher:** plan a lesson as rows: facts get retrieval starters; principles get
  explain-why prompts; procedures get worked example → fading; then a mixed set that forces
  method choice.
- **For the engine:** the ROUTE step (procedure → worked example; concept → productive failure)
  matches rows 4 and 3. The table suggests explicit routes for rows 1, 2 and 5 (retrieval-first;
  interleaved examples; contrasting cases). → S12 engine proposal candidate (no edit).

## Misconceptions owned
M6, M16 (shared, A1), M17, M31, M32, M33 → `misconceptions.md`.
