# MAS2001 — Stage-2 Sources (tiered, dated, confidence-noted)

> Per `../../../../../subject-research-protocol.md` §2. These are the **Stage-2** (deep-structure)
> sources, kept separate from the clean Stage-1 `../sources.md`. Every load-bearing Stage-2 specific
> (CRLB, Neyman–Pearson, Wilks, Berry–Esseen constant, exponential-family form, max-entropy Normal,
> t/χ²/F constructions) was verified against an external source **this session (2026-06-19)** — recall
> alone never settled a result (protocol §1). Where authorities genuinely differ or a value is still
> open (the Berry–Esseen constant), the claim is marked `contested`, never flattened.

## Tier 1 — Primary / foundational (graduate texts & canonical course material)

- **Walpole / Montgomery & Runger / Ross** (Stage-1 anchors, carried forward) — the sampling-
  distribution chapters ground the t/χ²/F constructions (Unit 3 §5, Unit 4 §3). `settled`
- **Stanford Stats 200 / 300A lecture notes** (Mackey; stats200) — Fisher information & Cramér–Rao
  (L15/L4), Neyman–Pearson lemma (300A L13), exponential families (300A L2).
  <https://web.stanford.edu/class/stats200/Lecture15.pdf>,
  <https://web.stanford.edu/~lmackey/stats300a/doc/stats300a-fall15-lecture13.pdf>. `settled`
- **University of Wisconsin — Shao, Stat 709 L15** — Rao–Blackwell / Lehmann–Scheffé / UMVUE.
  <https://pages.stat.wisc.edu/~shao/stat709/stat709-15.pdf>. `settled`
- **University of Regina — Kozdron, ch.4** — Fisher information & the Cramér–Rao inequality (two forms).
  <https://uregina.ca/~kozdron/Teaching/Regina/252Winter16/Handouts/ch4.pdf>. `settled`
- **University of Iowa — Breheny, 7110 notes** — Lindeberg–Feller CLT (conditions).
  <https://myweb.uiowa.edu/pbreheny/7110/f20/notes/9-23.pdf>. `settled`
- **IISc — Probability Theory notes 16–18** — characteristic-function proof of the CLT + Lévy continuity.
  <https://math.iisc.ac.in/~manju/Old/ProbTheory/Notes/16-18%20CLT.pdf>. `settled`
- **Purdue — Dasgupta, "The Exponential Family and Statistical Applications"** — canonical form,
  A(η) as cumulant generator, sufficiency. <https://www.stat.purdue.edu/~dasgupta/expfamily.pdf>. `settled`
- **ASA — Wasserstein & Lazar (2016), "The ASA Statement on p-Values," *The American Statistician***
  — the six principles (Unit 4 §6). <https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf>;
  <https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1154108>. `settled`

## Tier 1/2 — Authoritative secondary (verification & triangulation this session)

- **Wikipedia — "Lévy's continuity theorem", "Wilks' theorem", "Neyman–Pearson lemma",
  "Lehmann–Scheffé theorem"** — used to confirm exact statements; each cross-checked against an
  independent lecture-note source above (not used as sole authority). 2026-06-19. `settled`
- **stephens999 fiveMinuteStats — Wilks' theorem; Asymptotic normality of the MLE.**
  <https://stephens999.github.io/fiveMinuteStats/wilks.html>. Triangulates Wilks df + MLE √n-normality. `settled`
- **Karlin / Charles Univ. (Kulich) MLE theory summary** — MLE consistency, asymptotic normality with
  variance I₁(θ)⁻¹, efficiency. <https://www.karlin.mff.cuni.cz/~kulich/vyuka/glm/doc/mle_summary.pdf>. `settled`
- **W&M (Leemis) UDR chart — Exponential→Erlang**; **randomservices.org Gamma**; **Univ. of Nairobi
  thesis "Sums of Exponential RVs"** — sum of n iid Exponential = Gamma/Erlang(n,λ). Triangulated. `settled`
- **HBS Research Computing — "The Cramér–Rao Lower Bound: Derivation and Examples."**
  <https://www.hbs.edu/.../cramerrao.pdf>. Confirms CRLB form + Cauchy–Schwarz mechanism. `settled`

## Berry–Esseen constant — `contested` (open value), triangulated for form

- **numberanalytics "Mastering the Berry–Esseen Theorem"** and **emergentmind "Berry–Esseen rates /
  inequality"** — bound sup|Fₙ−Φ| ≤ Cρ/(σ³√n), rate O(1/√n) best-possible; **best known C < 0.4748**
  (Shevtsova 2011), lower bound ≈0.409 ⇒ exact optimal C still open. Form `settled`; constant `contested`/`evolving`.

## Misconception sources (promoting M3, M7, M11 — Unit 1/3/4)

- **AAMT Topdrawer "Statistics → Misunderstandings"** — expected value vs typical/short-run (M3).
  <https://topdrawer.aamt.edu.au/Statistics/Misunderstandings>. `settled` (documented difficulty).
- **UT Austin "statmistakes / error types"; NIH/PMC hypothesis-testing reviews; Scribbr Type I/II** —
  Type I/II ↔ α/β confusion (M11). Documented teaching hazard across independent pedagogical sources
  (not a single controlled study — noted honestly). `settled` (as documented hazard).
- **M7** grounded by the rigorous fact (MLE only *asymptotically* unbiased; Normal σ̂² biased) in
  `03-estimation.md` §4 — Stanford 200 L15 / Karlin MLE summary. `settled`.

## Independence note (protocol §5)

Each load-bearing Stage-2 result was confirmed across **≥2 independent external origins reached this
session** — e.g. CRLB (Stanford + U.Regina + HBS), Wilks (Wikipedia + stephens999 + Bohrium),
Neyman–Pearson (Stanford 300A + Wikipedia + CUNY), Exponential→Erlang (Leemis + randomservices +
Nairobi), max-entropy Normal (KL/Gibbs derivations from independent expositions). Two *recalled*
phrasings are **not** two sources (§5); only distinct external documents counted.
