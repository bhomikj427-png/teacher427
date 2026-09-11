# MAS2001 — Misconceptions & predictable errors

> Feeds the engine's productive-failure & feedback moves. Each is a *claim* (protocol §4): the
> well-documented statistics-education misconceptions are `settled`; ones marked `uncertain` are
> plausible-but-unsourced and flagged to-verify, never asserted as "the common error" on recall.

## Probability & random variables (U1)
- **M1 `settled` — "P(X=x) must be positive for continuous X."** No: for continuous RVs P(X=x)=0;
  probability is *area under the pdf*, not the pdf's height (which can exceed 1). Root of many sign/
  setup errors. *(Documented in standard texts; consistent across sources.)*
- **M2 `settled` — confusing the pmf/pdf with the CDF.** Students integrate/differentiate the wrong
  one. Anchor: f=F′, F=∫f.
- **M3 `settled` — "expectation = the most likely / a typical value."** E[X] need not be
  attainable (e.g. E of a die = 3.5) and isn't the mode. *(Promoted 2026-06-19: documented in
  statistics-education sources — AAMT Topdrawer "Misunderstandings"; the related long-run-vs-short-run
  and expected-value-vs-sample-mean confusions are widely reported.)*

## The big threshold confusions (U1→U3→U4)
- **M4 `settled` — conflating population, sample, and sampling distribution.** *The* central error
  (the ★ threshold). The sample mean has its own distribution (≈Normal, SD σ/√n by CLT); students
  treat it as if it had the population's spread. Cascades into every CI/test error below.
- **M5 `settled` — "CLT says the data become normal as n grows."** No: the *distribution of the
  sample mean* (or sum) approaches Normal; the raw data keep their own distribution. *(Widely
  documented statistics-education misconception.)*

## Estimation (U3)
- **M6 `settled` — confidence-interval misinterpretation.** "There's a 95% probability the true μ is
  in *this* interval" is wrong under the frequentist meaning: the 95% refers to the *procedure's*
  long-run coverage; a given interval either contains μ or not. *(Classic, heavily documented.)*
- **M7 `settled` — "the MLE is always unbiased."** Not generally (e.g. the MLE of Normal
  variance divides by n, which is biased; n−1 corrects it). *(Promoted 2026-06-19: the underlying fact
  is rigorously settled — MLE is only *asymptotically* unbiased/efficient, see `stage-2/03-estimation.md`
  §4; the small-sample bias is a direct, well-known consequence students miss.)*

## Hypothesis testing (U4)
- **M8 `settled` — "p-value = probability the null is true."** No: p = P(data this extreme | H₀),
  not P(H₀ | data). *(Documented; central to the ASA p-value statement.)*
- **M9 `settled` — "fail to reject H₀" means "H₀ is proven true."** It means insufficient evidence
  against it — absence of evidence ≠ evidence of absence.
- **M10 `settled` — "statistically significant = important / large effect."** With large n, trivial
  effects reach significance. Significance ≠ effect size ≠ practical importance.
- **M11 `settled` — confusing α with the per-test error probability / with power.** Many
  students swap Type I/II and α/β. *(Promoted 2026-06-19: a standard, independently-warned-about
  difficulty across pedagogical sources — UT Austin "statmistakes", NIH/PMC hypothesis-testing reviews,
  Scribbr. Grounded as a documented teaching hazard, though not from a single controlled study.)*

## To-verify (route to `00-map.md` register)
- ~~Confirm M3, M7, M11 against a statistics-education / documented-error source~~ **Resolved
  2026-06-19** — M3/M7/M11 verified against ed-research / pedagogical sources and promoted to
  `settled` (see each entry + `stage-2/sources.md`). No open misconception items remain.
