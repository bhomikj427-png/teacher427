# MAS2001 — Knowledge-base CHANGELOG

> Correction/audit trail (protocol §10). Format:
> `[YYYY-MM-DD] <claim/topic> — <what changed> — <why> — <trigger> — <confidence: old → new>`

- `[2026-06-16]` **Whole base (Stage 1)** — created: 00-map + units 01–04 + misconceptions +
  sources — initial Stage-1 build to MUJ level — trigger: batch research engine, demo run —
  confidence: (new) units `settled`, unit-boundary scope `uncertain`.
- `[2026-06-16]` **Chebyshev inequality & CLT exact statements** — verified against external sources
  (CMU Stat-700 notes; MIT OCW 18.600; Wikipedia) rather than recall — why: protocol §1 (recall ≠
  sourced) — trigger: load-bearing specifics — confidence: recalled → `settled`.
- `[2026-06-16]` **MAS2001 unit boundaries** — flagged `uncertain` and logged to to-verify — why:
  seeded from a derivative aggregator, not the official handout — trigger: source-tier audit —
  confidence: (new) `uncertain`.
- `[2026-06-19]` **Stage 2 built — all 4 units → `stage-2✓`** — created `stage-2/01–04` + `stage-2/sources.md`
  (measure-theoretic RV, convergence modes, CF proof of CLT, Lindeberg/Lyapunov, Berry–Esseen;
  exponential family, MGF/convolution closure, max-entropy Normal; Cramér–Rao/Fisher, Rao–Blackwell/
  Lehmann–Scheffé, MLE asymptotics, t/χ²/F derivations, conjugacy/decision theory; Neyman–Pearson, LRT/
  Wilks, power & sample size, CI–test duality, replication crisis/ASA) — why: learner activated the
  subject for teaching → depth-first to the `stage-2✓` gate — trigger: subject activation — every
  load-bearing specific verified vs external sources this session — confidence: (new) `settled` (units),
  Berry–Esseen **best constant** `contested`/open, advanced-topic **scope** `uncertain` pending handout.
- `[2026-06-19]` **Misconceptions M3, M7, M11** — promoted `uncertain → settled` — why: verified against
  ed-research / pedagogical sources (AAMT Topdrawer; UT Austin statmistakes; NIH/PMC; Scribbr) + the
  settled MLE-bias fact — trigger: Stage-2 to-verify worked down — confidence: `uncertain → settled`.
- `[2026-11-16]` **Table values (z, t, χ², F)** — added a section to `04-hypothesis-testing.md` listing
  every table value the course's questions print, with exact values — why: the KB held none, and the
  study pack needs them (spec v1.3 §7.1 item 3) — trigger: study-pack sprint S0 — confidence: (new) `settled`
  (scipy computation); two key values marked as slips (A5 C6 F(12,2), A5 D1 F(4,5)).
- `[2026-11-17]` **MLE / MoM properties (G&K ch. 15)** — added a section to `03-estimation.md`: L = Π f(xᵢ, θ) (eq. 15·53), Thms 15.11 (consistent; MLE of σ² not unbiased), 15.13 (asymptotically
  normal), 15.14 (most efficient), 15.15 (function of a sufficient estimator), 15.17 (invariance); MoM
  remarks (consistent, asymptotically normal, generally less efficient than MLE); ex. 20(b) prints θ — why:
  the facts were checked in S3 session 1 but lived only in the hand-off (review backlog row) — trigger:
  study-pack sprint S3 — confidence: (new) `settled`; G&K added to `sources.md`.
- `[2026-11-17]` **G&K locations for Unit 2 (S4)** — added "Prescribed-textbook locations" to `02-probability-distributions.md`: §7.2 (Ex. 7.4 = MTE B3, Ex. 7.7), §7.3 (limit, additive property), §8.1, §8.6 (Ex. 8.40 memoryless; ch. 8 ex. 7(a) = A2 B5, answer 0.6225) — why: the v1.3 files 04a, 04b, 05 cite the prescribed textbook — trigger: study-pack sprint S4 — confidence: `settled` (read on the PDF text layer).
- `[2026-11-17]` **G&K locations for the normal, CLT and SE (S5)** — added S5 bullets to `02-probability-distributions.md` "Prescribed-textbook locations": §8.2 (normal, areas 0·6826/0·9544/0·9973), §8.10 (Lindeberg–Lévy CLT, mean form 8·31-2), §12.3 and §12.3.2 (parameter/statistic, standard error) — why: the v1.3 files 06 and 07 cite the prescribed textbook — trigger: study-pack sprint S5 — confidence: `settled` (read on the PDF text layer).
- `[2026-11-17]` **G&K locations for confidence intervals and hypothesis testing (S6)** — added "Prescribed-textbook locations" to `04-hypothesis-testing.md` (§12.5–12.8, §16.2.4–16.3: H₀/H₁, Type I/II, producer's/consumer's risk, critical region, tails, critical-value table, steps, size, power function) and a §15.15 bullet to `03-estimation.md` — why: the v1.3 files 11, 12a, 12b cite them — trigger: study-pack sprint S6 — confidence: `settled` (PDF text layer).
- `[2026-11-17]` **G&K locations for t- and F-tests (S7)** — added §14.2, §14.2.10 (remarks 3–4) and §14.5.5 (remarks 1–2, two-tailed rule) bullets to `04-hypothesis-testing.md` "Prescribed-textbook locations"; sources.md entry — why: study-pack files 13, 14 cite them — trigger: sprint S7 — confidence: (new) `settled` (text layer).
