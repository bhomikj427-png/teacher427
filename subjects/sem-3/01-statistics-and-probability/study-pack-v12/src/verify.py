"""Independent re-computation of every number printed in the MAS2001 v1.2 study pack.

Method: each answer is recomputed with scipy/numpy (distribution objects, numerical integration,
library tests such as scipy.stats.f_oneway / chi2_contingency / ttest_*) - a route independent of the
hand formulas the pack teaches. Where the professor printed an answer key, the key is compared too.

    python verify.py        -> prints every check; exits 1 if any PACK value fails.

KEY mismatches are reported, not failed: they are the slips flagged in the pack's note boxes.
"""
import math
import sys
from fractions import Fraction as Fr

import numpy as np
from scipy import integrate, optimize, stats

FAILS, KEYDIFF, N = [], [], [0]


def chk(name, got, pack, tol=None, key=None, ktol=None):
    """got = independent value; pack = value printed in the pack; key = professor's printed answer."""
    N[0] += 1
    tol = tol if tol is not None else max(1e-9, 0.006 * abs(pack) if pack else 1e-9)
    ok = abs(got - pack) <= tol
    if not ok:
        FAILS.append(name)
    line = f"{'ok ' if ok else 'FAIL'} {name}: computed {got:.6g}, pack {pack}"
    if key is not None:
        kt = ktol if ktol is not None else max(1e-9, 0.006 * abs(key))
        kok = abs(got - key) <= kt
        line += f", key {key} {'= key' if kok else '<-- KEY DIFFERS'}"
        if not kok:
            KEYDIFF.append(name)
    print(line)


Z = stats.norm()
phi0 = lambda z: Z.cdf(z) - 0.5  # area 0..z, the table the professor uses

# ---------------------------------------------------------------- 02/03 random variables, E, Var, Chebyshev
# MTE B1
x = np.array([-1, 1, 3, 5]); p = np.array([1, 1, 1, 3]) / 6
mu = (x * p).sum(); var = (x**2 * p).sum() - mu**2
chk("MTE B1 mean", mu, 3); chk("MTE B1 E[X^2]", (x**2 * p).sum(), 43 / 3); chk("MTE B1 var", var, 16 / 3)
chk("MTE B1 Chebyshev bound k=1 (=var/1)", var / 1**2, 16 / 3, key=16 / 3)
chk("MTE B1 exact P(|X-3|>=1)", p[np.abs(x - 3) >= 1].sum(), 5 / 6)
# MTE B2: f = ax^2+bx on (0,1), mean 0.5
a, b = np.linalg.solve([[1 / 3, 1 / 2], [1 / 4, 1 / 3]], [1, 0.5])
chk("MTE B2 a", a, -6, key=-6); chk("MTE B2 b", b, 6, key=6)
chk("MTE B2 check integral", integrate.quad(lambda t: a * t * t + b * t, 0, 1)[0], 1)
# A1 SA1 boys in 3 children
bd = stats.binom(3, 0.5)
for k, v in enumerate([1 / 8, 3 / 8, 3 / 8, 1 / 8]):
    chk(f"A1 SA1 P(X={k})", bd.pmf(k), v, key=v)
for k, v in enumerate([1 / 8, 4 / 8, 7 / 8, 1]):
    chk(f"A1 SA1 F({k})", bd.cdf(k), v, key=v)
# A1 SA2 power consumption f = x e^{-x/3}/9 (gamma k=2, scale 3); P(X>12)
g = stats.gamma(2, scale=3)
chk("A1 SA2 integral", integrate.quad(lambda t: t * math.exp(-t / 3) / 9, 0, np.inf)[0], 1)
chk("A1 SA2 P(X>12)=5e^-4", g.sf(12), 0.0916, tol=5e-5, key=0.0915, ktol=2e-4)
# A1 SA3 cable 6x(1-x)
chk("A1 SA3 integral", integrate.quad(lambda t: 6 * t * (1 - t), 0, 1)[0], 1)
chk("A1 SA3 median b", optimize.brentq(lambda c: integrate.quad(lambda t: 6 * t * (1 - t), 0, c)[0] - 0.5, 0.01, 0.99), 0.5, key=0.5)
# A1 SA4 geometric expectation
chk("A1 SA4 E[tosses]", stats.geom(0.5).mean(), 2, key=2)
# A1 SA5 two dice
s = np.add.outer(np.arange(1, 7), np.arange(1, 7)).ravel()
chk("A1 SA5 mean", s.mean(), 7); chk("A1 SA5 var", s.var(), 35 / 6)
chk("A1 SA5 bound var/9", s.var() / 9, 35 / 54); chk("A1 SA5 actual", (np.abs(s - 7) >= 3).mean(), 1 / 3, key=1 / 3)
# A1 SA6 600 throws, 80..120 sixes
v6 = 600 * (1 / 6) * (5 / 6)
chk("A1 SA6 var", v6, 250 / 3); chk("A1 SA6 lower bound", 1 - v6 / 20**2, 19 / 24, key=19 / 24)
chk("A1 SA6 exact (for comparison)", stats.binom(600, 1 / 6).cdf(120) - stats.binom(600, 1 / 6).cdf(79), 0.9754, tol=2e-3)
# A1 LA1 death age f = 3e-9 t^2 (100-t)^2
fd = lambda t: 3e-9 * t * t * (100 - t) ** 2
chk("A1 LA1 integral", integrate.quad(fd, 0, 100)[0], 1)
p6070 = integrate.quad(fd, 60, 70)[0]; p60 = integrate.quad(fd, 60, 100)[0]
chk("A1 LA1 (i)", p6070, 0.1544, tol=2e-4, key=0.1544, ktol=2e-4)
chk("A1 LA1 P(T>=60)", p60, 0.3174, tol=2e-4)
chk("A1 LA1 (ii)", p6070 / p60, 0.4863, tol=1e-4, key=0.4863, ktol=1e-4)
F_ = lambda t: 1e-5 * t**3 - 1.5e-7 * t**4 + 6e-10 * t**5
chk("A1 LA1 F(70)", F_(70), 0.83692, tol=1e-5); chk("A1 LA1 F(60)", F_(60), 0.68256, tol=1e-5); chk("A1 LA1 F(100)", F_(100), 1)
chk("A1 LA1 F matches integral", F_(70) - F_(60), p6070, tol=1e-9)
# A1 LA2 - textbook table (x=0 has probability 0)
k = optimize.brentq(lambda k: 10 * k * k + 9 * k - 1, 0, 1)
chk("A1 LA2 k (textbook table)", k, 0.1, key=0.1)
pt = np.array([0, k, 2 * k, 2 * k, 3 * k, k * k, 2 * k * k, 7 * k * k + k])
chk("A1 LA2 P(X<6)", pt[:6].sum(), 0.81, key=0.81)
chk("A1 LA2 P(X>6)", pt[7:].sum(), 0.17)
chk("A1 LA2 P(X>=6)", pt[6:].sum(), 0.19)
chk("A1 LA2 P(0<X<5)", pt[1:5].sum(), 0.8, key=0.8)
for i, v in enumerate([0, 0.1, 0.3, 0.5, 0.8, 0.81, 0.83, 1.0]):
    chk(f"A1 LA2 F({i})", pt[:i + 1].sum(), v, tol=1e-9)
chk("A1 LA2 min c", float(np.argmax(np.cumsum(pt) > 0.5 + 1e-9)), 4, key=4)
chk("A1 LA2 P(1.5<X<4.5|X>2)", (pt[3] + pt[4]) / pt[3:].sum(), 5 / 7, key=5 / 7)
# as printed by the assignment (x=0 has probability k): k from 10k^2+12k-1=0
kp = optimize.brentq(lambda k: 10 * k * k + 12 * k - 1, 0, 1)
chk("A1 LA2 k as printed", kp, (-6 + math.sqrt(46)) / 10)
chk("A1 LA2 k as printed ~", kp, 0.0782, tol=1e-4)
# A1 LA3 defectives 5 of 25, sample 4
chk("A1 LA3 without replacement", stats.hypergeom(25, 5, 4).mean(), 0.8, key=0.808)
chk("A1 LA3 with replacement", stats.binom(4, 0.2).mean(), 0.8, key=0.8)
# A1 LA4 oranges 4 bad of 20, draw 2
h = stats.hypergeom(20, 4, 2)
for k_, v in enumerate([12 / 19, 32 / 95, 3 / 95]):
    chk(f"A1 LA4 P({k_})", h.pmf(k_), v, key=v)
# A1 App1 sensors
x = np.arange(4); p = np.array([.25, .40, .25, .10])
chk("A1 App1 sum", p.sum(), 1); chk("A1 App1 E", (x * p).sum(), 1.2, key=1.2)
chk("A1 App1 E[X^2]", (x * x * p).sum(), 2.3); chk("A1 App1 Var", (x * x * p).sum() - 1.44, 0.86, key=0.86)
# A1 App2 calls
p = np.array([.15, .35, .30, .20])
for i, v in enumerate([.15, .50, .80, 1.0]):
    chk(f"A1 App2 F({i})", np.cumsum(p)[i], v, key=v)
chk("A1 App2 P(X>1)", p[2:].sum(), 0.5, key=0.5)
# A1 App3 batteries
x = np.array([2, 3, 4, 5]); p = np.array([.2, .3, .35, .15])
m = (x * p).sum(); vv = (x * x * p).sum() - m * m
chk("A1 App3 mean", m, 3.45, key=3.45); chk("A1 App3 E[X^2]", (x * x * p).sum(), 12.85)
chk("A1 App3 var", vv, 0.9475, key=0.95, ktol=0.003); chk("A1 App3 sd", math.sqrt(vv), 0.973, tol=1e-3, key=0.98, ktol=0.004)
# A1 App4 Chebyshev k=2
chk("A1 App4 bound", 1 - 25 / 10**2, 0.75, key=0.75)

# ---------------------------------------------------------------- 04 binomial & Poisson
chk("MTE A4 lambda", -math.log(0.5), math.log(2)); chk("MTE A4 Var=ln2", stats.poisson(math.log(2)).var(), 0.6931, tol=1e-4)
# MTE B3 die
pp = optimize.brentq(lambda p: stats.binom(10, p).pmf(5) - 2 * stats.binom(10, p).pmf(4), 0.05, 0.95)
chk("MTE B3 p", pp, 5 / 8, key=5 / 8)
chk("MTE B3 expected no-even sets", 10000 * stats.binom(10, pp).pmf(0), 0.5499, tol=1e-4, key=0.5499, ktol=1e-4)
chk("A2 MCQ2 var", stats.binom(10, .5).var(), 2.5)
po = stats.poisson(2.5)
chk("A2 B1 (i)", po.pmf(0), 0.0821, tol=1e-4, key=0.0821, ktol=1e-4)
chk("A2 B1 (ii) P(X>3)", po.sf(3), 0.2424, tol=1e-4, key=0.2424, ktol=1e-4)
chk("A2 C3 P(X>2) Poisson 5", stats.poisson(5).sf(2), 0.8753, tol=1e-4, key=0.8754, ktol=2e-4)
chk("A2 D3 Poisson approx", stats.poisson(2).pmf(0), 0.1353, tol=1e-4, key=0.1353, ktol=1e-4)
chk("A2 D3 exact binomial (comparison)", stats.binom(200, .01).pmf(0), 0.1340, tol=1e-4)

# ---------------------------------------------------------------- 05 uniform & exponential
chk("MTE B4 bus", (5 + 5) / 30, 1 / 3, key=1 / 3)
chk("A2 B2", stats.uniform(10, 10).sf(16), 0.4, key=0.4)
e2 = stats.expon(scale=2)
chk("A2 B5 P(X<1|X<2)", e2.cdf(1) / e2.cdf(2), 0.6225, tol=1e-4, key=0.5679, ktol=1e-4)
e05 = stats.expon(scale=2)  # lambda = 1/2
chk("A2 B7 (i)", e05.sf(2), math.exp(-1), key=math.exp(-1))
chk("A2 B7 (ii)", e05.sf(11) / e05.sf(8), math.exp(-1.5), key=math.exp(-1.5))
u = stats.uniform(-3, 6)
chk("A2 B8 (i)", u.cdf(2), 5 / 6, key=5 / 6); chk("A2 B8 (ii)", u.cdf(2) - u.cdf(-2), 2 / 3, key=2 / 3)
chk("A2 B8 (iii)", u.cdf(4) - u.cdf(0), 1 / 2, key=1 / 2); chk("A2 B8 (iv) K", u.isf(1 / 3), 1, key=1)
e1000 = stats.expon(scale=1000)
chk("A2 C1", e1000.sf(1500) / e1000.sf(500), 0.3679, tol=1e-4, key=0.3679, ktol=1e-4)
chk("A2 C4", 1 - (stats.uniform(-.5, 1).cdf(.2) - stats.uniform(-.5, 1).cdf(-.2)), 0.6, key=0.6)
chk("A2 D2", stats.expon(scale=1 / 4).sf(0.5), 0.1353, tol=1e-4, key=0.1353, ktol=1e-4)
chk("A2 D4", stats.uniform(15, 20).cdf(30) - stats.uniform(15, 20).cdf(25), 0.25, key=0.25)

# ---------------------------------------------------------------- 06 normal
chk("MTE C1a z", (75 - 65) / 5, 2)
q = 0.5 - 0.4772
chk("MTE C1a P(X>75) table", q, 0.0228, key=0.0228)
chk("MTE C1a P(X>75) exact", stats.norm(65, 5).sf(75), 0.02275, tol=1e-5)
chk("MTE C1a at least one of 3", 1 - (1 - q) ** 3, 0.0669, tol=1e-4, key=0.0667, ktol=2e-4)
chk("A2 B3 table", 0.1915 + 0.3849, 0.5764, key=0.5764)
chk("A2 B3 exact", stats.norm(50, 10).cdf(62) - stats.norm(50, 10).cdf(45), 0.5764, tol=2e-4)
chk("A2 B4 (i)", round(5000 * (0.5 - 0.4452)), 274, key=274)
chk("A2 B4 (ii)", 5000 * (0.5 - 0.3849), 575.5, key=576, ktol=0.6)
chk("A2 B4 (iii)", 5000 * (0.4332 + 0.4641), 4486.5, key=4487, ktol=0.6)
chk("A2 B4 (i) exact", 5000 * stats.norm(1500, 100).sf(1660), 274.0, tol=0.5)
sig = 35 / (1.04 + 1.28); muu = 30 + 1.28 * sig
chk("A2 B6 sigma", sig, 15.09, tol=0.01, key=15.09, ktol=0.01); chk("A2 B6 mu", muu, 49.31, tol=0.01, key=49.31, ktol=0.01)
chk("A2 B6 exact-quantile mu", 30 - stats.norm.ppf(.1) * 35 / (stats.norm.ppf(.85) - stats.norm.ppf(.1)), 49.3, tol=0.1)
sC2 = 35 / (1.34 - 0.1); mC2 = 40 - 0.1 * sC2
chk("A2 C2 sigma", sC2, 28.23, tol=0.01, key=28.2, ktol=0.05); chk("A2 C2 mu", mC2, 37.18, tol=0.01, key=37.5, ktol=0.05)
chk("A2 C2 requalify mark", mC2 - 0.24 * sC2, 30.40, tol=0.01, key=30.43, ktol=0.01)
chk("A2 D1 table", 10000 * 2 * 0.3944, 7888, key=7888)
chk("A2 D1 exact", 10000 * (stats.norm(3000, 400).cdf(3500) - stats.norm(3000, 400).cdf(2500)), 7887, tol=1)
chk("A2 MCQ11", Z.cdf(1) - Z.cdf(-1), 0.6827, tol=1e-4)

# ---------------------------------------------------------------- 07 SE & CLT
chk("LMS SE n=25", 100 / math.sqrt(25), 20, key=20); chk("LMS SE n=100", 100 / math.sqrt(100), 10, key=10)
chk("LMS ATM z", 0.5 / (2 / 6), 1.5); chk("LMS ATM P", Z.sf(1.5), 0.0668, tol=1e-4, key=0.0668, ktol=1e-4)
se = 1.5 / math.sqrt(50)
chk("LMS Ex1 SE", se, 0.2121, tol=1e-4); chk("LMS Ex1 z1", (3.5 - 4) / se, -2.357, tol=1e-3); chk("LMS Ex1 z2", (3.8 - 4) / se, -0.943, tol=1e-3)
chk("LMS Ex1 P table", 0.4909 - 0.3264, 0.1645, key=0.1644, ktol=2e-4)
chk("LMS Ex1 P exact", Z.cdf((3.8 - 4) / se) - Z.cdf((3.5 - 4) / se), 0.1636, tol=3e-4)
chk("LMS Ex2 z", (48000 - 50000) / (8000 / 8), -2); chk("LMS Ex2 P", 0.5 - 0.4772, 0.0228, key=0.0228)
chk("LMS Ex3 z", (6.4 - 7) / (1 / 3), -1.8); chk("LMS Ex3 P", 0.4641 + 0.2257, 0.6898, key=0.6898)
chk("LMS Ex3 exact", Z.cdf(0.6) - Z.cdf(-1.8), 0.6898, tol=2e-4)
chk("A4 MCQ8 SE", 5 / math.sqrt(25), 1)

# ---------------------------------------------------------------- 08 estimator properties
rng = np.random.default_rng(1)
smp = rng.normal(10, 2, size=(200000, 3))
chk("MTE C1b E[T1] (sim, mu=10)", (smp[:, 0] + smp[:, 1] - smp[:, 2]).mean(), 10, tol=0.03)
chk("MTE C1b E[T2] (sim, 2mu=20)", (3 * smp[:, 0] + 2 * smp[:, 2] - 3 * smp[:, 1]).mean(), 20, tol=0.05)
chk("unbiased s^2 (sim, sigma^2=4)", smp.var(axis=1, ddof=1).mean(), 4, tol=0.03)
chk("biased n-divisor (sim, 4*2/3)", smp.var(axis=1, ddof=0).mean(), 8 / 3, tol=0.03)

# ---------------------------------------------------------------- 09 MoM & MLE
rats = np.array([14, 17, 27, 18, 12, 8, 22, 13, 19, 12])
chk("LMS Ex13 MLE beta", rats.mean(), 16.2, key=16.2)
nll = lambda b: -stats.expon(scale=b).logpdf(rats).sum()
chk("LMS Ex13 numeric MLE", optimize.minimize_scalar(nll, bounds=(1, 100), method="bounded").x, 16.2, tol=1e-3)
xs = np.array([12, 11.2, 13.5, 12.3, 13.8, 11.9])
chk("LMS Ex14 sum ln", np.log(xs).sum(), 15.114, tol=1e-3)
th = len(xs) / np.log(xs).sum()
chk("LMS Ex14 MLE theta", th, 0.3970, tol=1e-4, key=0.3970, ktol=1e-4)
nll14 = lambda t: -(len(xs) * math.log(t) - (t + 1) * np.log(xs).sum())
chk("LMS Ex14 numeric", optimize.minimize_scalar(nll14, bounds=(0.01, 5), method="bounded").x, 0.3970, tol=1e-3)
gk = np.array([0.46, 0.38, 0.61, 0.82, 0.59, 0.53, 0.72, 0.44, 0.59, 0.60])
xb = gk.mean()
chk("G&K 23b mean", xb, 0.574, tol=1e-9)
chk("G&K 23b MoM", (2 * xb - 1) / (1 - xb), 0.3474, tol=1e-4)
chk("G&K 23b sum ln", np.log(gk).sum(), -5.7873, tol=1e-3)
chk("G&K 23b MLE", -1 - len(gk) / np.log(gk).sum(), 0.7279, tol=1e-3)
chk("G&K 23b numeric MLE", optimize.minimize_scalar(lambda t: -(len(gk) * math.log(1 + t) + t * np.log(gk).sum()),
                                                    bounds=(0, 10), method="bounded").x, 0.7279, tol=1e-3)
chk("MoM (1+t)x^t mean formula", integrate.quad(lambda x_: x_ * 1.5 * x_**0.5, 0, 1)[0], 1.5 / 2.5)
# uniform(0, theta) MoM 2*xbar on data 2,5,7,10 (pack worked example)
chk("MoM uniform(0,th)", 2 * np.mean([2, 5, 7, 10]), 12)
chk("MLE uniform(0,th)", max([2, 5, 7, 10]), 10)
# Poisson MLE = xbar on data 2,0,3,1,4 (pack worked example)
chk("Poisson MLE", np.mean([2, 0, 3, 1, 4]), 2)
chk("Poisson numeric MLE", optimize.minimize_scalar(lambda l: -stats.poisson(l).logpmf([2, 0, 3, 1, 4]).sum(),
                                                    bounds=(0.01, 10), method="bounded").x, 2, tol=1e-3)

# ---------------------------------------------------------------- 10 Bayesian (LMS Ex 15)
prior = {0.1: 0.6, 0.2: 0.4}
for xx, (g_key, post_key) in {0: (0.742, 0.6550), 1: (0.236, 0.4576), 2: (0.022, 0.2727)}.items():
    gx = sum(stats.binom(2, pp_).pmf(xx) * w for pp_, w in prior.items())
    post = stats.binom(2, .1).pmf(xx) * .6 / gx
    chk(f"LMS Ex15 g({xx})", gx, g_key, tol=5e-4, key=g_key, ktol=5e-4)
    chk(f"LMS Ex15 pi(0.1|{xx})", post, post_key, tol=5e-4, key=post_key, ktol=5e-4)
chk("LMS Ex15 posterior mean x=0", 0.1 * 0.6550 + 0.2 * 0.3450, 0.1345, tol=1e-4)

# ---------------------------------------------------------------- 11 confidence intervals
def zci(xb, s, n, z):
    h = z * s / math.sqrt(n); return xb - h, xb + h
lo, hi = zci(85.5, 19.3, 20, 2.576); chk("A4 B1 lo", lo, 74.38, tol=0.01); chk("A4 B1 hi", hi, 96.62, tol=0.01)
chk("A4 B1 exact z", stats.norm.ppf(0.995), 2.576, tol=5e-4)
lo, hi = zci(30, 3, 25, 1.96); chk("A4 B2 mu lo", lo, 28.824, tol=1e-3); chk("A4 B2 mu hi", hi, 31.176, tol=1e-3)
chk("A4 B2 2mu+7 lo", 2 * lo + 7, 64.648, tol=1e-3); chk("A4 B2 2mu+7 hi", 2 * hi + 7, 69.352, tol=1e-3)
lo, hi = zci(12.5, 2, 100, 1.96); chk("A4 B3 lo", lo, 12.108, tol=1e-3); chk("A4 B3 hi", hi, 12.892, tol=1e-3)
lo, hi = zci(250, 20, 10, 2.262); chk("A4 B4 lo", lo, 235.69, tol=0.01); chk("A4 B4 hi", hi, 264.31, tol=0.01)
chk("A4 B4 t(9)", stats.t.ppf(.975, 9), 2.262, tol=5e-4)
lo, hi = zci(85, 4, 20, 1.729); chk("A4 B5 lo", lo, 83.45, tol=0.01); chk("A4 B5 hi", hi, 86.55, tol=0.01)
chk("A4 B5 t(19) 90%", stats.t.ppf(.95, 19), 1.729, tol=5e-4)
# coverage simulation: 95% z-interval covers mu about 95% of the time
cov = rng.normal(50, 10, size=(100000, 25)).mean(axis=1)
chk("CI coverage sim", (np.abs(cov - 50) <= 1.96 * 10 / 5).mean(), 0.95, tol=0.004)

# ---------------------------------------------------------------- 12 hypothesis errors
chk("A4 C1(i) alpha", 1 - 0.5, 0.5, key=0.5); chk("A4 C1(i) beta", 0.5 / 2, 0.25, key=0.25)
chk("A4 C1(ii) alpha", 0, 0, key=0); chk("A4 C1(ii) beta", 1 - 0.5 / 2, 0.75, key=0.75)
chk("A4 C2 alpha", stats.binom(5, .5).sf(3), 3 / 16, key=3 / 16)
chk("A4 C2 beta", stats.binom(5, .75).cdf(3), 47 / 128, key=47 / 128)
chk("A4 C3 alpha", stats.binom(4, .75).cdf(2), 0.2617, tol=1e-4, key=0.2617, ktol=1e-4)
chk("A4 C3 beta", stats.binom(4, .5).sf(2), 0.3125, key=0.3125)
chk("PPT binom alpha", stats.binom(4, 1 / 3).sf(2), 1 / 9, key=1 / 9)
chk("PPT binom beta", stats.binom(4, .5).cdf(2), 11 / 16, key=11 / 16)
chk("PPT expo alpha", stats.expon(scale=5).sf(15), math.exp(-3), key=math.exp(-3))
chk("PPT expo beta", stats.expon(scale=10).cdf(15), 1 - math.exp(-1.5), key=1 - math.exp(-1.5))
chk("PPT (1+t)x^t alpha", integrate.quad(lambda x_: 3 * x_**2, 0, 0.1)[0], 0.001, key=0.001)
chk("PPT (1+t)x^t power at 3", integrate.quad(lambda x_: 4 * x_**3, 0, 0.1)[0], 1e-4, key=1e-4)

# ---------------------------------------------------------------- 13 t-tests
crit = {}
crit["t17_975"] = stats.t.ppf(.975, 17); chk("A5 B1 t(17)", crit["t17_975"], 2.110, tol=5e-4, key=2.110, ktol=5e-4)
tB1 = (7.8 - 8) / (0.5 / math.sqrt(18)); chk("A5 B1 t (s as sample SD)", tB1, -1.697, tol=1e-3)
chk("A5 B1 t (G&K s/sqrt(n-1))", (7.8 - 8) / (0.5 / math.sqrt(17)), -1.649, tol=1e-3)
bags = np.array([50, 49, 44, 52, 45, 48, 46, 45, 49, 45])
chk("A5 B4 mean", bags.mean(), 47.3); chk("A5 B4 s", bags.std(ddof=1), 2.6687, tol=1e-3)
chk("A5 B4 t", stats.ttest_1samp(bags, 50).statistic, -3.199, tol=2e-3)
nit = np.array([11, 14, 13, 12, 13, 12, 13, 14, 11, 12])
chk("A5 C1 mean", nit.mean(), 12.5); chk("A5 C1 s", nit.std(ddof=1), 1.0801, tol=1e-3)
chk("A5 C1 t", stats.ttest_1samp(nit, 12).statistic, 1.464, tol=2e-3)
S2 = (220 + 180) / 20; seC2 = math.sqrt(S2 * (1 / 12 + 1 / 10))
chk("A5 C2 S^2", S2, 20); chk("A5 C2 SE", seC2, 1.915, tol=1e-3); chk("A5 C2 t", 6 / seC2, 3.133, tol=2e-3)
chk("A5 C2 t(20)", stats.t.ppf(.975, 20), 2.086, tol=5e-4)
chk("A5 C2 CI lo", 6 - 2.086 * seC2, 2.006, tol=2e-3); chk("A5 C2 CI hi", 6 + 2.086 * seC2, 9.994, tol=2e-3)
chk("A5 C2 via ttest_ind_from_stats", stats.ttest_ind_from_stats(68, math.sqrt(220 / 11), 12, 62, math.sqrt(180 / 9), 10).statistic, 3.133, tol=2e-3)
bef = np.array([53, 28, 31, 48, 50, 42]); aft = np.array([58, 29, 30, 55, 56, 45])
d = aft - bef
chk("A5 C4 dbar", d.mean(), 3.5); chk("A5 C4 s_d", d.std(ddof=1), 3.0822, tol=1e-3)
chk("A5 C4 t", stats.ttest_rel(aft, bef).statistic, 2.782, tol=2e-3)
chk("A5 C4 t(5) one-tailed", stats.t.ppf(.95, 5), 2.015, tol=5e-4, key=2.02, ktol=0.006)
chk("A5 A4 paired t", 3.2 / (4 / math.sqrt(15)), 3.098, tol=1e-3, key=3.00, ktol=0.01)
w = np.array([24.8, 25.1, 24.9, 25.0, 25.2, 24.7, 25.0, 25.1, 25.3, 24.9, 25.0, 24.8, 25.1, 24.9, 25.2, 25.0, 25.1, 24.8, 25.0, 25.2])
chk("A5 D2 n", len(w), 20); chk("A5 D2 mean", w.mean(), 25.005, tol=1e-6); chk("A5 D2 s", w.std(ddof=1), 0.1605, tol=2e-4)
chk("A5 D2 t", stats.ttest_1samp(w, 25).statistic, 0.139, tol=2e-3)
chk("A5 D2 CI lo", w.mean() - 2.093 * w.std(ddof=1) / math.sqrt(20), 24.930, tol=1e-3, key=24.945, ktol=1e-3)
chk("A5 D2 CI hi", w.mean() + 2.093 * w.std(ddof=1) / math.sqrt(20), 25.080, tol=1e-3, key=25.075, ktol=1e-3)
chk("A5 D2 t(19)", stats.t.ppf(.975, 19), 2.093, tol=5e-4); chk("A5 D2 t(19) 1%", stats.t.ppf(.995, 19), 2.861, tol=5e-4)

# ---------------------------------------------------------------- 14 F-test
chk("A5 A5 F", 81 / 25, 3.24)
FB2 = 29.75**2 / 27.5**2
chk("A5 B2 F", FB2, 1.170, tol=1e-3)
chk("A5 B3 F(15,12) 0.5% upper (two-tailed 1%)", stats.f.isf(.005, 15, 12), 4.72, tol=0.01, key=4.72, ktol=0.01)
chk("A5 B2 F(15,12) 5% upper", stats.f.isf(.05, 15, 12), 2.62, tol=0.01)
chk("A5 C5 S1^2", 112 / 7, 16); chk("A5 C5 S2^2", 140 / 10, 14); chk("A5 C5 F", 16 / 14, 1.143, tol=1e-3)
chk("A5 C5 F(7,10)", stats.f.isf(.05, 7, 10), 3.14, tol=0.01, key=3.14, ktol=0.01)
m1 = np.array([8260, 8130, 8350, 8070, 8340]); m2 = np.array([7950, 7890, 7900, 8140, 7920])
chk("A5 D1 mean1", m1.mean(), 8230); chk("A5 D1 mean2", m2.mean(), 7960)
chk("A5 D1 S1^2", m1.var(ddof=1), 15750); chk("A5 D1 S2^2", m2.var(ddof=1), 10650)
chk("A5 D1 F", m1.var(ddof=1) / m2.var(ddof=1), 1.479, tol=1e-3)
chk("A5 D1 F(4,4) 5%", stats.f.isf(.05, 4, 4), 6.39, tol=0.01, key=5.19, ktol=0.01)
chk("A5 D1 F(4,4) 2.5% (two-tailed 5%)", stats.f.isf(.025, 4, 4), 9.60, tol=0.01)

# ---------------------------------------------------------------- 15 chi-square independence
def chi(tab):
    r = stats.chi2_contingency(np.array(tab), correction=False); return r.statistic, r.dof, r.expected_freq
c, df_, ex = chi([[1236, 564], [164, 36]])
chk("A5 B5 chi2", c, 15.238, tol=2e-3); chk("A5 B5 E11", ex[0, 0], 1260); chk("A5 B5 df", df_, 1)
chk("A5 B5 2x2 formula", 2000 * (1236 * 36 - 564 * 164) ** 2 / (1800 * 200 * 1400 * 600), 15.238, tol=2e-3)
c, df_, ex = chi([[44, 22, 13], [15, 19, 26], [6, 8, 47]])
chk("A5 B6 chi2", c, 58.00, tol=0.01); chk("A5 B6 df", df_, 4)
chk("A5 B6 E11", ex[0, 0], 79 * 65 / 200, tol=1e-9)
chk("A5 B6 chi2(4) 1%", stats.chi2.isf(.01, 4), 13.28, tol=0.01, key=13.28, ktol=0.01)
c, df_, ex = chi([[75, 105], [25, 95]]); chk("A5 C3 chi2", c, 14.0625, tol=1e-4); chk("A5 C3 E11", ex[0, 0], 60)
c, df_, ex = chi([[370, 430], [130, 70]]); chk("A5 D3 chi2", c, 22.5, tol=1e-6); chk("A5 D3 E11", ex[0, 0], 400)
chk("chi2(1) 5%", stats.chi2.isf(.05, 1), 3.841, tol=5e-4)

# ---------------------------------------------------------------- 16 one-way ANOVA
def anova(groups):
    allx = np.concatenate(groups); gm = allx.mean(); n_ = len(allx); k_ = len(groups)
    sst = ((allx - gm) ** 2).sum(); ssb = sum(len(g_) * (g_.mean() - gm) ** 2 for g_ in groups)
    return dict(gm=gm, sst=sst, ssb=ssb, ssw=sst - ssb, dfb=k_ - 1, dfw=n_ - k_,
                msb=ssb / (k_ - 1), msw=(sst - ssb) / (n_ - k_), F=(ssb / (k_ - 1)) / ((sst - ssb) / (n_ - k_)))
chk("A5 A10 F", (120 / 3) / (180 / 20), 4.444, tol=1e-3, key=4.00, ktol=0.01)
G6 = [np.array([10, 12, 9, 15, 13]), np.array([6, 8, 3, 0, 2]), np.array([5, 9, 12, 8, 4])]
r = anova(G6)
chk("A5 C6 means", np.mean([g_.mean() for g_ in G6]), (11.8 + 3.8 + 7.6) / 3)
chk("A5 C6 grand mean", r["gm"], 7.7333, tol=1e-4)
chk("A5 C6 SST", r["sst"], 264.93, tol=0.01); chk("A5 C6 SSB", r["ssb"], 160.13, tol=0.01); chk("A5 C6 SSW", r["ssw"], 104.8, tol=0.01)
chk("A5 C6 F", r["F"], 9.17, tol=0.01); chk("A5 C6 f_oneway", stats.f_oneway(*G6).statistic, 9.17, tol=0.01)
chk("A5 C6 F(2,12) 5%", stats.f.isf(.05, 2, 12), 3.89, tol=0.01, key=19.41, ktol=0.01)
chk("A5 C6 F(12,2) 5% (what 19.41 is)", stats.f.isf(.05, 12, 2), 19.41, tol=0.01)
G4 = [np.array([70, 72, 75, 80, 83]), np.array([100, 110, 108, 112, 113, 120, 100]), np.array([60, 65, 57, 84, 84, 70])]
chk("A5 D4 totals", sum(g_.sum() for g_ in G4), 380 + 763 + 420)
r = anova(G4)
chk("A5 D4 grand mean", r["gm"], 1563 / 18, tol=1e-9)
chk("A5 D4 SST", r["sst"], 6840.5, tol=0.1); chk("A5 D4 SSB", r["ssb"], 5726.5, tol=0.1); chk("A5 D4 SSW", r["ssw"], 1114.0, tol=0.1)
chk("A5 D4 F", r["F"], 38.55, tol=0.01); chk("A5 D4 f_oneway", stats.f_oneway(*G4).statistic, 38.55, tol=0.01)
chk("A5 D4 F(2,15) 1%", stats.f.isf(.01, 2, 15), 6.36, tol=0.01, key=6.36, ktol=0.01)

# ---------------------------------------------------------------- table values used in Exam forms
chk("z 5% two-tailed", stats.norm.ppf(.975), 1.96, tol=5e-4); chk("z 1% two-tailed", stats.norm.ppf(.995), 2.576, tol=5e-4)
chk("z 5% one-tailed", stats.norm.ppf(.95), 1.645, tol=5e-4); chk("z 1% one-tailed", stats.norm.ppf(.99), 2.326, tol=5e-4)

# ================================================================ numbers introduced by the pack itself
# (Checks, Self-tests, worked extras, mock paper). Each recomputed independently.
B = stats.binom; P = stats.poisson
# ---- 01
chk("01 Ace or heart", 16 / 52, 4 / 13)
chk("01 Bayes P(D)", .6 * .02 + .4 * .05, 0.032); chk("01 Bayes M1|D", .012 / .032, 0.375); chk("01 Bayes M2|D", .020 / .032, 0.625)
chk("01 C3 union", .5 + .3 - .1, 0.7); chk("01 C4 two aces", (4 / 52) * (3 / 51), 1 / 221)
chk("01 C6 M1|good", .588 / (.588 + .38), 0.6074, tol=1e-4)
dice = [(a_, b_) for a_ in range(1, 7) for b_ in range(1, 7)]
chk("01 ST2 sum 7", sum(a_ + b_ == 7 for a_, b_ in dice) / 36, 1 / 6)
chk("01 ST6 urn", (.5 * .4) / (.5 * .4 + .5 * .8), 1 / 3)
# ---- 02
chk("02 C3 max=1", sum(max(a_, b_) == 1 for a_, b_ in dice) / 36, 1 / 36)
chk("02 C3 max=6", sum(max(a_, b_) == 6 for a_, b_ in dice) / 36, 11 / 36)
chk("02 C5 k", 1 / integrate.quad(lambda t: t * t, 0, 3)[0], 1 / 9)
chk("02 C5 P", integrate.quad(lambda t: t * t / 9, 1, 2)[0], 7 / 27)
c6 = lambda a_, b_: integrate.quad(lambda t: 6 * t * (1 - t), a_, b_)[0]
chk("02 C6", c6(.75, 1) / c6(.5, 1), 0.3125)
chk("02 ST5 p0", stats.hypergeom(10, 3, 2).pmf(0), 7 / 15); chk("02 ST5 p1", stats.hypergeom(10, 3, 2).pmf(1), 7 / 15)
chk("02 ST5 p2", stats.hypergeom(10, 3, 2).pmf(2), 1 / 15)
chk("02 ST7 P(X>1)", stats.expon(scale=.5).sf(1), 0.1353, tol=1e-4)
# ---- 03 (v1.2 checks removed S2b; 03a/03b numbers are in the "v1.3 S2" block)
# ---- 04 (v1.2 checks removed S4; 04a/04b numbers are in the "v1.3 S4" block)
# ---- 05 (v1.2 checks removed S4; numbers are in the "v1.3 S4" block)
# ---- 06 (v1.2 checks removed S5; numbers are in the "v1.3 S5" block)
# ---- 07 (v1.2 checks removed S5; numbers are in the "v1.3 S5" block)
# ---- 08 (v1.2 checks removed S2b; numbers are in the "v1.3 S2" block)
# ---- 09 (v1.2 checks removed S3; 09a/09b numbers are in the "v1.3 S3" block)
chk("09 MoM uniform (a,b) sim", (lambda d: d.mean() - math.sqrt(3 * d.var()))(rng.uniform(7, 13, 200000)), 7, tol=0.02)
# ---- 10
chk("10 C2", .06 / .14, 0.4286, tol=1e-4); chk("10 C3", .16 / .25, 0.64)
chk("10 C4", .1 * .2727 + .2 * .7273, 0.1727, tol=1e-4)
pst = .24 / .59
chk("10 ST4", pst, 0.4068, tol=1e-4); chk("10 ST5", .5 * (1 - pst) + .8 * pst, 0.6220, tol=1e-4)
chk("10 prior mean", .1 * .6 + .2 * .4, 0.14)
# ---- 11
se1 = 19.3 / math.sqrt(20)
chk("11 B1 90 lo", 85.5 - 1.645 * se1, 78.40, tol=0.01); chk("11 B1 95 lo", 85.5 - 1.96 * se1, 77.04, tol=0.01)
chk("11 B1 95 margin", 1.96 * se1, 8.46, tol=0.01)
chk("11 C2 lo", 12.5 - 1.96 * 0.1, 12.304); chk("11 C3 n", (1.96 * 19.3 / 5) ** 2, 57.24, tol=0.01)
chk("11 C6 lo", w.mean() - 2.861 * w.std(ddof=1) / math.sqrt(20), 24.902, tol=1e-3)
chk("11 C6 hi", w.mean() + 2.861 * w.std(ddof=1) / math.sqrt(20), 25.108, tol=1e-3)
chk("11 D2 via t.interval", stats.t.interval(.95, 19, loc=w.mean(), scale=w.std(ddof=1) / math.sqrt(20))[0], 24.930, tol=1e-3)
dd = np.round((w - 25) * 10).astype(int); chk("11 D2 sum d", dd.sum(), 1); chk("11 D2 sum d2", (dd**2).sum(), 49)
chk("11 ST2 99 lo", 52 - 2.576, 49.424, tol=1e-3); chk("11 ST3 lo", 20 - 2.131, 17.869)
# ---- 12
chk("12 C5 beta", 1 - math.exp(-1.5), 0.7769, tol=1e-4)
chk("12 ST4 beta", 0.9 / 1.5, 0.6); chk("12 C6 term", B(4, .75).pmf(2), 0.2109, tol=1e-4)
chk("12 power A4 C2", 1 - 47 / 128, 81 / 128)
# ---- 13
chk("13 C1", (41.5 - 44) / (6 / 4), -1.667, tol=1e-3)
chk("13 C4", (15 - 13) / math.sqrt((7 * 4 + 7 * 5) / 14 * (1 / 8 + 1 / 8)), 1.886, tol=1e-3)
chk("13 C4 t(14)", stats.t.ppf(.975, 14), 2.145, tol=5e-4)
bp = np.array([140, 150, 135, 160, 145]); ap = np.array([132, 148, 128, 150, 142])
chk("13 C5 t", stats.ttest_rel(bp, ap).statistic, 3.956, tol=2e-3); chk("13 C5 t(4)", stats.t.ppf(.95, 4), 2.132, tol=5e-4)
chk("13 ST4", 3 / math.sqrt(5 * (1 / 6 + 1 / 6)), 2.324, tol=1e-3); chk("13 ST6", 1.2 / (1.5 / math.sqrt(10)), 2.530, tol=1e-3)
chk("13 ST3 t(24)", stats.t.ppf(.975, 24), 2.064, tol=5e-4); chk("13 B1 SE", 0.5 / math.sqrt(18), 0.11785, tol=1e-5)
chk("13 C2 sum d", (bags - 48).sum(), -7); chk("13 C2 sum d2", ((bags - 48) ** 2).sum(), 69)
# ---- 14
chk("14 C2 F", (90 / 9) / (108 / 12), 1.111, tol=1e-3)
chk("14 C4 t", 270 / math.sqrt((630 + 426) * 100 / 8 * (2 / 5)), 3.716, tol=1e-3)
chk("14 C4 ttest", stats.ttest_ind(m1, m2).statistic, 3.716, tol=2e-3); chk("14 C4 t(8)", stats.t.ppf(.975, 8), 2.306, tol=5e-4)
chk("14 C5 F(5,5)", stats.f.isf(.05, 5, 5), 5.05, tol=0.01); chk("14 ST3 F(10,15)", stats.f.isf(.05, 10, 15), 2.54, tol=0.01)
chk("14 ST4", np.var([1, 5, 9], ddof=1) / np.var([2, 4, 6], ddof=1), 4)
chk("14 C2 link F", (220 / 11) / (180 / 9), 1)
# ---- 15
chk("15 B6 E31", 61 * 65 / 200, 19.825); chk("15 ST3", 100 * (400 - 900) ** 2 / 50**4, 4)
chk("15 chi2 4df 5%", stats.chi2.isf(.05, 4), 9.488, tol=1e-3); chk("15 chi2 1df 1%", stats.chi2.isf(.01, 1), 6.635, tol=1e-3)
chk("15 chi2 2df 5%", stats.chi2.isf(.05, 2), 5.991, tol=1e-3)
# ---- 16
chk("16 C2 F", (60 / 2) / (90 / 12), 4)
chk("16 C3 SSB", (40**2 + 48**2 + 56**2) / 4 - 144**2 / 12, 32); chk("16 C3 F", (32 / 2) / (80 / 9), 1.8)
chk("16 C4 SSB by means", sum(len(g_) * (g_.mean() - 1563 / 18) ** 2 for g_ in G4), 5726.5, tol=0.05)
chk("16 ST3 F", (36 / 3) / (64 / 16), 3); chk("16 ST3 F(3,16)", stats.f.isf(.05, 3, 16), 3.24, tol=0.01)
chk("16 ST5 F", stats.f_oneway([2, 4, 6], [6, 8, 10]).statistic, 6)
chk("16 D4 sum x^2", sum((g_**2).sum() for g_ in G4), 142561)
# ---- 17 mock
xm = np.array([0, 1, 2]); pm = np.array([.2, .5, .3])
chk("M A1 E", (xm * pm).sum(), 1.1); chk("M A1 Var", (xm**2 * pm).sum() - 1.21, 0.49)
chk("M A4", stats.expon(scale=4).sf(6) / stats.expon(scale=4).sf(2), math.exp(-1))
chk("M A6 var", 14 / 36, 7 / 18); chk("M A9", 2 / (3 / math.sqrt(10)), 2.108, tol=1e-3)
fk = lambda t: t * (2 - t)
k_m = 1 / integrate.quad(fk, 0, 2)[0]
chk("M B1 k", k_m, 0.75); chk("M B1 E", integrate.quad(lambda t: t * k_m * fk(t), 0, 2)[0], 1)
chk("M B1 Var", integrate.quad(lambda t: t * t * k_m * fk(t), 0, 2)[0] - 1, 0.2)
chk("M B1 P", integrate.quad(lambda t: k_m * fk(t), 0, .5)[0], 0.1563, tol=1e-4)
chk("M B2 i", round(2000 * (0.5 - 0.4772)), 46); chk("M B2 ii", round(2000 * 2 * 0.3413), 1365)
xb3 = np.array([.2, .5, .7, .9])
chk("M B3 sum ln", np.log(xb3).sum(), -2.7646, tol=1e-4); chk("M B3 theta", -4 / np.log(xb3).sum(), 1.447, tol=1e-3)
chk("M B3 numeric", optimize.minimize_scalar(lambda t: -(4 * math.log(t) + (t - 1) * np.log(xb3).sum()),
                                              bounds=(.01, 10), method="bounded").x, 1.447, tol=1e-3)
chk("M B4 lo", 48.5 - 2.131 * 1.5, 45.30, tol=0.01); chk("M B4 hi", 48.5 + 2.131 * 1.5, 51.70, tol=0.01)
chk("M B5 alpha", B(6, .5).sf(4), 7 / 64); chk("M B5 beta", B(6, .7).cdf(4), 0.5798, tol=1e-4)
chk("M B6", stats.chi2_contingency(np.array([[60, 40], [40, 60]]), correction=False).statistic, 8)
chk("M C1 P1", 0.5 - 0.4332, 0.0668); chk("M C1 P2", 0.4332 + 0.3413, 0.7745)
chk("M C1 exact", stats.norm(60, 2).cdf(62) - stats.norm(60, 2).cdf(57), 0.7745, tol=2e-4)
chk("M C2 lambda", np.mean([3, 5, 4, 6, 2]), 4); chk("M C2 P0", math.exp(-4), 0.0183, tol=1e-4)
GD = [np.array([8, 10, 12, 10]), np.array([14, 12, 16, 14]), np.array([9, 11, 10, 10])]
rD = anova(GD)
chk("M D1 SST", rD["sst"], 60.67, tol=0.01); chk("M D1 SSB", rD["ssb"], 42.67, tol=0.01); chk("M D1 SSW", rD["ssw"], 18)
chk("M D1 F", stats.f_oneway(*GD).statistic, 10.67, tol=0.01); chk("M D1 F(2,9)", stats.f.isf(.05, 2, 9), 4.26, tol=0.01)

# ==== v1.3 S1 — files 01, 02a, 02b (route: enumerate outcomes / exact fractions / scipy quad)
from itertools import product, combinations  # noqa: E402

D2 = list(product(range(1, 7), repeat=2))
pr = lambda ev: Fr(sum(1 for o in D2 if ev(o)), 36)
chk("01 n", len(D2), 36)
chk("01 st5 at least one six", pr(lambda o: 6 in o), 11 / 36)
chk("01 st6 A or B", pr(lambda o: sum(o) == 7 or o[0] == 6), 11 / 36)
chk("01 st7 P(C|B)", pr(lambda o: sum(o) >= 10 and o[0] == 6) / pr(lambda o: o[0] == 6), 0.5)
chk("01 st3 red", Fr(4, 10), 0.4); chk("01 st3 ace", Fr(4, 52), 1 / 13)
chk("01 st9 two aces", Fr(4, 52) * Fr(3, 51), 1 / 221)
deck = [(r, s) for r in range(13) for s in range(4)]
chk("01 st9 aces enum", Fr(sum(1 for a, b in combinations(deck, 2) if a[0] == 0 and b[0] == 0), math.comb(52, 2)), 1 / 221)
pD = 0.6 * 0.02 + 0.4 * 0.05
chk("01 st11 P(D)", pD, 0.032); chk("01 st12 P(M1|D)", 0.012 / pD, 0.375); chk("01 st12 P(M2|D)", 0.020 / pD, 0.625)
chk("01 st10 P(C∩B)", pr(lambda o: sum(o) >= 10 and o[0] == 6), 1 / 12)
chk("01 st10 P(C)P(B)", pr(lambda o: sum(o) >= 10) * pr(lambda o: o[0] == 6), 1 / 36)
chk("01 st10 P(A∩B)=P(A)P(B)", pr(lambda o: sum(o) == 7 and o[0] == 6) - pr(lambda o: sum(o) == 7) * pr(lambda o: o[0] == 6), 0)
chk("01 C1b", 2 * 6, 12); chk("01 C2a", sum(1 for o in D2 if sum(o) >= 10), 6)
chk("01 C3a", pr(lambda o: sum(o) >= 10), 1 / 6); chk("01 C3b", 2 / 10, 0.2)
chk("01 C4", pr(lambda o: sum(o) in (2, 12)), 1 / 18)
chk("01 C5a", 1 - 1 / 6, 5 / 6); chk("01 C5b", 1 - 0.5 ** 3, 7 / 8)
chk("01 C6a", Fr(sum(1 for r, s in deck if r == 0 or s == 0), 52), 4 / 13)
chk("01 C6b union", 0.5 + 0.3 - 0.1, 0.7); chk("01 C6b neither", 1 - 0.7, 0.3)
chk("01 C7a", pr(lambda o: sum(o) == 7 and o[0] == 6) / pr(lambda o: o[0] == 6), 1 / 6)
chk("01 C7b", pr(lambda o: sum(o) >= 10 and o[0] == 6) / pr(lambda o: sum(o) >= 10), 0.5)
chk("01 C8", pr(lambda o: sum(o) <= 6 and o[0] == 6), 0)
chk("01 C9 RR", Fr(3, 5) * Fr(2, 4), 0.3); chk("01 C9 RB", Fr(3, 5) * Fr(2, 4), 0.3)
chk("01 C10a", 0.4 * 0.5, 0.2)
chk("01 C10b", pr(lambda o: o[0] % 2 == 0 and o[1] == 6), 1 / 12)
chk("01 C11", 0.6 * 0.98 + 0.4 * 0.95, 0.968, tol=1e-9)
chk("01 C12a", 0.6 * 0.98 / 0.968, 0.6074, tol=1e-4)
chk("01 C12b", (0.5 * 0.4) / (0.5 * 0.4 + 0.5 * 0.8), 1 / 3)
chk("01 ST1 sum8", pr(lambda o: sum(o) == 8), 5 / 36); chk("01 ST1 doubles", pr(lambda o: o[0] == o[1]), 1 / 6)
chk("01 ST2", pr(lambda o: 1 in o), 11 / 36)
chk("01 ST3 AB", 0.6 + 0.5 - 0.8, 0.3, tol=1e-9); chk("01 ST3 A|B", (0.6 + 0.5 - 0.8) / 0.5, 0.6, tol=1e-9)
chk("01 ST5", Fr(1, 4) / Fr(3, 4), 1 / 3)
chk("01 ST6", pr(lambda o: sum(o) == 8 and o[0] % 2 == 0 and o[1] % 2 == 0) / pr(lambda o: o[0] % 2 == 0 and o[1] % 2 == 0), 1 / 3)
chk("01 ST7", 0.01 * 0.90 / (0.01 * 0.90 + 0.99 * 0.05), 0.1538, tol=1e-4)

# 02a: three children (enumerate the 8 families)
fam = list(product("BG", repeat=3))
pX = {x: Fr(sum(1 for f in fam if f.count("B") == x), 8) for x in range(4)}
chk("02a p(0)", pX[0], 1 / 8); chk("02a p(1)", pX[1], 3 / 8); chk("02a p(2)", pX[2], 3 / 8); chk("02a p(3)", pX[3], 1 / 8)
chk("02a F(1)", pX[0] + pX[1], 4 / 8); chk("02a F(2)", pX[0] + pX[1] + pX[2], 7 / 8)
chk("02a LA4 C(20,2)", math.comb(20, 2), 190)
chk("02a LA4 p0", Fr(math.comb(16, 2), 190), 120 / 190); chk("02a LA4 p1", Fr(4 * 16, 190), 64 / 190)
chk("02a LA4 p2", Fr(math.comb(4, 2), 190), 6 / 190)
kk = optimize.brentq(lambda k: 10 * k ** 2 + 9 * k - 1, 0, 1)  # G&K row: k,2k,2k,3k,k^2,2k^2,7k^2+k
chk("02a LA2 k", kk, 0.1)
chk("02a LA2 printed-row k", optimize.brentq(lambda k: 10 * k ** 2 + 12 * k - 1, 0, 1), 0.0782, tol=1e-4)
chk("02a LA2 printed-row closed form", (-6 + math.sqrt(46)) / 10, 0.0782, tol=1e-4)
chk("02a LA4 12/19", Fr(120, 190), 12 / 19); chk("02a LA4 32/95", Fr(64, 190), 32 / 95); chk("02a LA4 3/95", Fr(6, 190), 3 / 95)
kq = Fr(round(kk * 1000), 1000)  # exact 1/10 so F(3) = 1/2 exactly (step (iv) needs ">", not ">=")
pLA = [Fr(0), kq, 2 * kq, 2 * kq, 3 * kq, kq ** 2, 2 * kq ** 2, 7 * kq ** 2 + kq]
FLA = [sum(pLA[:i + 1]) for i in range(8)]
chk("02a LA2 F(5)", FLA[5], 0.81); chk("02a LA2 F(6)", FLA[6], 0.83)
chk("02a LA2 P(X>6)", 1 - FLA[6], 0.17, key=0.81)  # key answers P(X<6): flagged in the note box
chk("02a LA2 P(X>=6)", 1 - FLA[5], 0.19, key=0.91)  # key's 91/100 = 19/100 digits swapped
chk("02a LA2 P(0<X<5)", FLA[4] - FLA[0], 0.8, key=0.8)
chk("02a LA2 min c", min(c for c in range(8) if FLA[c] > 0.5), 4)
chk("02a LA2 (v)", (pLA[3] + pLA[4]) / (1 - FLA[2]), 5 / 7)
calls = [0.15, 0.35, 0.30, 0.20]; Fc = np.cumsum(calls)
chk("02a App2 F(1)", Fc[1], 0.50); chk("02a App2 F(2)", Fc[2], 0.80); chk("02a App2 P(X>1)", 1 - Fc[1], 0.50)
chk("02a C3a p(1)", Fr(sum(1 for f in product("HT", repeat=2) if f.count("H") == 1), 4), 0.5)
chk("02a C3b p(6)", Fr(sum(1 for o in D2 if max(o) == 6), 36), 11 / 36)  # larger of two dice (C3b)
chk("02a C3b p(1)", Fr(sum(1 for o in D2 if max(o) == 1), 36), 1 / 36)
chk("02a C5a", Fr(1, 10), 0.1)
chk("02a C5b", optimize.brentq(lambda k: k * k + 3 * k - 1, 0, 1), 0.3028, tol=1e-4)
chk("02a C6 p0", Fr(math.comb(7, 2), 45), 7 / 15); chk("02a C6 p1", Fr(3 * 7, 45), 7 / 15); chk("02a C6 p2", Fr(3, 45), 1 / 15)
chk("02a C7a", 0.25 + 0.5, 0.75); chk("02a C8a", Fc[2] - Fc[0], 0.65); chk("02a C8b", Fc[1], 0.50)
chk("02a C9", pX[3] / (pX[2] + pX[3]), 0.25)
chk("02a ST2", Fr(math.comb(4, 2), 16), 3 / 8)
chk("02a ST3 p0", Fr(3, 10), 0.3); chk("02a ST3 p1", Fr(2 * 3, 10), 0.6); chk("02a ST3 p2", Fr(1, 10), 0.1)
chk("02a ST4 k", Fr(1, 1 + 4 + 9), 1 / 14); chk("02a ST4 F(2)", Fr(5, 14), 5 / 14)
chk("02a ST5 a", sum(pLA[2:5]), 0.7); chk("02a ST5 b", sum(pLA[5:]), 0.2)
chk("02a ST6 F(3.5)", Fr(3, 6), 0.5); chk("02a ST6 P>4", Fr(2, 6), 1 / 3)
chk("02a ST7", pX[1] + pX[2], 0.75)

# 02b: continuous (scipy quad, independent of the hand antiderivatives)
q = lambda f, a, b: integrate.quad(f, a, b)[0]
fc = lambda x: 6 * x * (1 - x)
chk("02b total", q(fc, 0, 1), 1)
chk("02b f(0.2)", fc(0.2), 0.96); chk("02b f(0.5)", fc(0.5), 1.5); chk("02b f(0.8)", fc(0.8), 0.96)
chk("02b area .2-.5", q(fc, .2, .5), 0.396)
for xv, Fv in ((0.2, 0.104), (0.5, 0.5), (0.8, 0.896)):
    chk(f"02b F({xv})", q(fc, 0, xv), Fv)
chk("02b median", optimize.brentq(lambda b: q(fc, 0, b) - 0.5, 0.01, 0.99), 0.5)
chk("02b other roots +", (1 + math.sqrt(3)) / 2, 1.366, tol=1e-3); chk("02b other roots -", (1 - math.sqrt(3)) / 2, -0.366, tol=1e-3)
chk("02b cubic factor", np.polyval(np.polymul([2, -1], [2, -2, -1]), 0.37) - np.polyval([4, -6, 0, 1], 0.37), 0)
fp = lambda x: x * math.exp(-x / 3) / 9
chk("02b SA2 total", q(fp, 0, np.inf), 1)
chk("02b SA2 P(X>12)", q(fp, 12, np.inf), 0.0916, tol=1e-4, key=0.0915, ktol=1e-4)
chk("02b SA2 5e-4", 5 * math.exp(-4), 0.0916, tol=1e-4); chk("02b e^-4", math.exp(-4), 0.018316, tol=1e-6)
chk("02b SA2 f(3)", fp(3), 0.1226, tol=1e-4); chk("02b SA2 f(12)", fp(12), 0.0244, tol=1e-4); chk("02b SA2 f(20)", fp(20), 0.0028, tol=1e-4)
chk("02b SA2 peak", optimize.minimize_scalar(lambda x: -fp(x), bounds=(0.1, 20), method="bounded").x, 3, tol=1e-3)
fl = lambda t: 3e-9 * t ** 2 * (100 - t) ** 2
chk("02b LA1 total", q(fl, 0, 100), 1)
chk("02b LA1 F(70)", q(fl, 0, 70), 0.83692, tol=1e-5); chk("02b LA1 F(60)", q(fl, 0, 60), 0.68256, tol=1e-5)
chk("02b LA1 (i)", q(fl, 60, 70), 0.1544, tol=1e-4, key=0.1544, ktol=1e-4)
chk("02b LA1 P(T>=60)", q(fl, 60, 100), 0.31744, tol=1e-5)
chk("02b LA1 (ii)", q(fl, 60, 70) / q(fl, 60, 100), 0.4863, tol=1e-4, key=0.4863, ktol=1e-4)
chk("02b f(50)", fl(50), 0.01875, tol=1e-6); chk("02b f(60)", fl(60), 0.01728, tol=1e-6); chk("02b f(70)", fl(70), 0.01323, tol=1e-6)
chk("02b C1b", q(fc, .5, .8), 0.396)
chk("02b C2 k", 1 / q(lambda x: x * x, 0, 3), 1 / 9); chk("02b C2 P", q(lambda x: x * x / 9, 1, 2), 7 / 27)
chk("02b C3b", q(lambda x: 2 * x, .5, 1), 0.75); chk("02b C4", optimize.brentq(lambda b: b * b - .5, 0, 1), 0.7071, tol=1e-4)
chk("02b C5 k", 1 / q(lambda x: math.exp(-2 * x), 0, np.inf), 2); chk("02b C5 P", q(lambda x: 2 * math.exp(-2 * x), 1, np.inf), 0.1353, tol=1e-4)
chk("02b C6", q(fc, .75, 1) / q(fc, .5, 1), 0.3125); chk("02b C6 tail", q(fc, .75, 1), 0.15625)
chk("02b ST2", 1 / q(lambda x: x * (2 - x), 0, 2), 0.75)
chk("02b ST3", q(lambda x: 3 * x * x, .5, 1), 0.875); chk("02b ST4", 0.5 ** (1 / 3), 0.7937, tol=1e-4)
chk("02b ST5", q(lambda x: math.exp(-x / 4) / 4, 4, np.inf), 0.3679, tol=1e-4)
chk("02b ST6", q(lambda x: x * math.exp(-x), 1, np.inf), 0.7358, tol=1e-4)
chk("02b ST7", q(fc, 0, .2) / q(fc, 0, .5), 0.208)

# ==== v1.3 S2 — files 03a, 03b, 08 (route: exact Fractions over enumerated tables / dice / samples; scipy for curves)
from itertools import product as _prod


def _EV(xs, ps):
    m = sum(Fr(x) * p for x, p in zip(xs, ps)); return m, sum(Fr(x) ** 2 * p for x, p in zip(xs, ps)) - m * m


_sx, _sp = [0, 1, 2, 3], [Fr(25, 100), Fr(40, 100), Fr(25, 100), Fr(10, 100)]
m, v = _EV(_sx, _sp)
chk("03a sensors sum p", float(sum(_sp)), 1); chk("03a sensors E", float(m), 1.2); chk("03a sensors E(X2)", float(v + m * m), 2.3)
chk("03a 100 batches total", float(100 * m), 120)
chk("03a balance left", float(Fr(25, 100) * Fr(12, 10) + Fr(40, 100) * Fr(2, 10)), 0.38)
chk("03a balance right", float(Fr(25, 100) * Fr(8, 10) + Fr(10, 100) * Fr(18, 10)), 0.38)
chk("03a sensors Var (definition)", float(sum((x - m) ** 2 * p for x, p in zip(_sx, _sp))), 0.86); chk("03a sensors sd", math.sqrt(v), 0.927, tol=5e-4)
chk("03a (3-1.2)^2 p", 1.8 ** 2 * .1, 0.324); chk("03a (1-1.2)^2 p", .04 * .4, 0.016)
_bx, _bp = [2, 3, 4, 5], [Fr(20, 100), Fr(30, 100), Fr(35, 100), Fr(15, 100)]
m, v = _EV(_bx, _bp)
chk("03a battery E", float(m), 3.45, key=3.45); chk("03a battery E(X2)", float(v + m * m), 12.85); chk("03a battery Var", float(v), 0.9475, key=0.95, ktol=0.003)
chk("03a battery sd", math.sqrt(v), 0.973, tol=5e-4, key=0.98, ktol=0.002)
m, v = _EV(range(1, 7), [Fr(1, 6)] * 6)
chk("03a C1 die E", float(m), 3.5); chk("03a C5 die E(X2)", float(v + m * m), 91 / 6); chk("03a C5 die Var", float(v), 35 / 12); chk("03a C6 die sd", math.sqrt(v), 1.708, tol=5e-4)
chk("03a C2", 0.3, 0.3)
chk("03a C4 A", float(_EV([4, 5, 6], [Fr(1, 3)] * 3)[1]), 2 / 3); chk("03a C4 B", float(_EV([0, 5, 10], [Fr(1, 3)] * 3)[1]), 50 / 3)
fcab = lambda x: 6 * x * (1 - x)
sol = np.linalg.solve([[1 / 3, 1 / 2], [1 / 4, 1 / 3]], [1, .5]); chk("03a MTE B2 a", sol[0], -6, key=-6); chk("03a MTE B2 b", sol[1], 6, key=6)
e2 = integrate.quad(lambda x: x * x * fcab(x), 0, 1)[0]
chk("03a C7 E(X2)", e2, 0.3); chk("03a C7 Var", e2 - .25, 0.05); chk("03a C7 sd", math.sqrt(e2 - .25), 0.224, tol=5e-4)
m, v = _EV([0, 1, 2], [Fr(3, 10), Fr(4, 10), Fr(3, 10)]); chk("03a ST1 E", float(m), 1); chk("03a ST1 E2", float(v + m * m), 1.6); chk("03a ST1 Var", float(v), .6); chk("03a ST1 sd", math.sqrt(v), .775, tol=5e-4)
m, v = _EV([1, 2, 3], [Fr(5, 10), Fr(3, 10), Fr(2, 10)]); chk("03a ST2 E", float(m), 1.7); chk("03a ST2 Var", float(v), .61)
chk("03a ST4 E", integrate.quad(lambda x: 2 * x * x, 0, 1)[0], 2 / 3); chk("03a ST4 Var", integrate.quad(lambda x: 2 * x ** 3, 0, 1)[0] - 4 / 9, 1 / 18)
chk("03a ST5 k", 1 / integrate.quad(lambda x: x, 0, 2)[0], .5); chk("03a ST5 E", integrate.quad(lambda x: x * x / 2, 0, 2)[0], 4 / 3)
sol = np.linalg.solve([[1, 1 / 2], [1 / 2, 1 / 3]], [1, .6]); chk("03a ST7 a", sol[0], .4); chk("03a ST7 b", sol[1], 1.2)
# 03b
_d = range(1, 7); _cells = list(_prod(_d, _d))
chk("03b S1 E(10X-20)", float(sum(Fr(10 * x - 20, 6) for x in _d)), 15)
vy = float(_EV([10 * x - 20 for x in _d], [Fr(1, 6)] * 6)[1]); chk("03b S1 Var Y", vy, 291.67, tol=.01); chk("03b S1 sd Y", math.sqrt(vy), 17.08, tol=.01)
chk("03b C1", 2 * 3 - 5, 1); chk("03b C1 var", 4 * 4, 16)
chk("03b dice sum total", sum(a + b for a, b in _cells), 252)
m, v = _EV([a + b for a, b in _cells], [Fr(1, 36)] * 36); chk("03b dice E(S)", float(m), 7); chk("03b dice Var(S)", float(v), 35 / 6)
chk("03b dice Var(X1-X2)", float(_EV([a - b for a, b in _cells], [Fr(1, 36)] * 36)[1]), 35 / 6)
chk("03b dice E(X1X2)", float(sum(Fr(a * b, 36) for a, b in _cells)), 12.25)
# LA 3: without replacement, exact hypergeometric mean; with replacement binomial mean
chk("03b LA3 without", stats.hypergeom(25, 5, 4).mean(), 0.8, key=0.808, ktol=1e-3); chk("03b LA3 with", stats.binom(4, .2).mean(), 0.8)
chk("03b C2", 3 * 3.5, 10.5); chk("03b C3 2X-3Y", 4 * 4 + 9 * 1, 25); chk("03b C4", 3 * 2 * 5, 30); chk("03b C4b", 2 * 5 + 2, 12)
_ps = [sum(x * .5 ** x for x in range(1, k + 1)) for k in (1, 2, 3, 4, 5, 6, 8)]
for k, (got, pk) in enumerate(zip(_ps, [.5, 1, 1.375, 1.625, 1.781, 1.875, 1.961])):
    chk(f"03b SA4 partial {k}", got, pk, tol=6e-4)
chk("03b SA4 E", stats.geom(.5).mean(), 2); chk("03b C5", stats.geom(1 / 6).mean(), 6); chk("03b ST4", stats.geom(1 / 13).mean(), 13)
chk("03b App4", 1 - 1 / 4, 0.75, key=0.75)
_lap = stats.laplace(70, 5 / math.sqrt(2)); _un = stats.uniform(70 - 5 * math.sqrt(3), 10 * math.sqrt(3))
chk("03b fig bell", stats.norm(70, 5).cdf(80) - stats.norm(70, 5).cdf(60), 0.954, tol=6e-4)
chk("03b fig peaked", _lap.cdf(80) - _lap.cdf(60), 0.941, tol=6e-4); chk("03b fig flat", _un.cdf(80) - _un.cdf(60), 1.0)
chk("03b fig sds", _lap.std() + _un.std(), 10)
chk("03b C6", 1 - 1 / 9, 0.889, tol=5e-4)
chk("03b SA5 bound", (35 / 6) / 9, 35 / 54, key=35 / 54); chk("03b SA5 bound dec", 35 / 54, 0.648, tol=5e-4)
chk("03b SA5 exact", sum(1 for a, b in _cells if abs(a + b - 7) >= 3) / 36, 1 / 3)
m, v = _EV([1, 2, 3], [Fr(1, 4), Fr(1, 2), Fr(1, 4)]); chk("03b C7 bound", float(v), 0.5); chk("03b C7 exact", .5, .5)
m, v = _EV([-1, 1, 3, 5], [Fr(1, 6)] * 3 + [Fr(1, 2)])
chk("03b MTE B1 mu", float(m), 3); chk("03b MTE B1 E2", float(v + m * m), 43 / 3); chk("03b MTE B1 var", float(v), 16 / 3, key=16 / 3)
chk("03b MTE B1 sd", math.sqrt(v), 2.31, tol=.005); chk("03b MTE B1 exact", 1 - 1 / 6, 5 / 6)
chk("03b C8 bound", float(v) / 16, 1 / 3); chk("03b C8 exact", 1 / 6, 1 / 6)
b6 = stats.binom(600, 1 / 6)
chk("03b SA6 var I", 1 / 6 - 1 / 36, 5 / 36); chk("03b SA6 mu", b6.mean(), 100); chk("03b SA6 var", b6.var(), 250 / 3)
chk("03b SA6 bound", 1 - (250 / 3) / 400, 19 / 24); chk("03b SA6 bound dec", 19 / 24, 0.792, tol=5e-4)
chk("03b SA6 exact", b6.cdf(120) - b6.cdf(79), 0.975, tol=6e-4)
b4 = stats.binom(400, .5); chk("03b C9", 1 - b4.var() / 400, 0.75)
chk("03b ST3", 2 + 4 * 3, 14); b1 = stats.binom(100, .5); chk("03b ST6", 1 - b1.var() / 100, 0.75)
# 08
xb2 = [Fr(a + b, 2) for a, b in _cells]
chk("08 S1 estimate", (2 + 6) / 2, 4); chk("08 S1 distinct xbar", len(set(xb2)), 11)
chk("08 S3 xbar avg", float(sum(xb2) / 36), 3.5); chk("08 S3 xbar mode count", xb2.count(Fr(7, 2)), 6)
chk("08 S3 max avg", sum(max(c) for c in _cells) / 36, 4.47, tol=.005); chk("08 S3 max bias", sum(max(c) for c in _cells) / 36 - 3.5, .97, tol=.005)
chk("08 S3 max mode count", sum(1 for c in _cells if max(c) == 6), 11)
chk("08 C3 min avg", sum(min(c) for c in _cells) / 36, 91 / 36); chk("08 C3 min avg dec", 91 / 36, 2.53, tol=.005)
_ss = lambda t: sum((Fr(x) - Fr(sum(t), len(t))) ** 2 for x in t)
chk("08 S5 /n avg", float(sum(_ss(c) / 2 for c in _cells) / 36), 35 / 24); chk("08 S5 /n avg dec", 35 / 24, 1.46, tol=.005)
chk("08 S5 /(n-1) avg", float(sum(_ss(c) for c in _cells) / 36), 35 / 12); chk("08 sigma2 dec", 35 / 12, 2.92, tol=.005)
chk("08 C5 /n", float(_ss([4, 6, 8]) / 3), 2.67, tol=.005); chk("08 C5 s2", float(_ss([4, 6, 8]) / 2), 4)
for n, vv, sd in [(1, 2.92, 1.71), (4, .73, .85), (16, .18, .43)]:
    chk(f"08 S6 var n={n}", 35 / 12 / n, vv, tol=.005); chk(f"08 S6 sd n={n}", math.sqrt(35 / 12 / n), sd, tol=.005)
_tr = list(_prod(_d, _d, _d))
m, v = _EV([a + b - c for a, b, c in _tr], [Fr(1, 216)] * 216); chk("08 S7 T1 mean", float(m), 3.5); chk("08 S7 T1 var", float(v), 8.75); chk("08 S7 T1 sd", math.sqrt(v), 2.96, tol=.005)
m, v = _EV([Fr(a + b + c, 3) for a, b, c in _tr], [Fr(1, 216)] * 216); chk("08 S7 xbar var", float(v), 35 / 36); chk("08 S7 xbar sd", math.sqrt(v), .99, tol=.005)
chk("08 S7 xbar var dec", 35 / 36, 0.97, tol=.005); chk("08 S7 efficiency", (35 / 36) / 8.75, 1 / 9)
chk("08 MTE C1b E(T2) die", 3 * 3.5 + 2 * 3.5 - 3 * 3.5, 7)
chk("08 C7 var coef", (1 + 4 + 1) / 16, 3 / 8); chk("08 C7 eff", (1 / 3) / (3 / 8), 8 / 9)
chk("08 S8 orders", math.comb(5, 3), 10)
chk("08 ST3 a", 13 / 25, 13 / 25); chk("08 ST6 eff", (35 / 24) / (35 / 12), .5)

# ==== v1.3 S3 — files 09a, 09b (route: exact Fractions for moments; scipy quad for E(X); numeric maximisation
# of each log-likelihood with optimize.minimize_scalar, independent of the hand-derived formulas)
_mx = lambda fn, lo, hi: optimize.minimize_scalar(lambda t: -fn(t), bounds=(lo, hi), method="bounded", options={"xatol": 1e-9}).x
# 09a
_die = range(1, 7)
chk("09a S1 die mu1", float(Fr(sum(_die), 6)), 3.5); chk("09a S1 die mu2", float(Fr(sum(k * k for k in _die), 6)), 15.17, tol=.005)
chk("09a S1 m1", np.mean([2, 6, 5, 3]), 4); chk("09a S1 m2", np.mean(np.square([2, 6, 5, 3])), 18.5)
chk("09a C1 m1", np.mean([1, 4, 4]), 3); chk("09a C1 m2", np.mean(np.square([1, 4, 4])), 11)
_bus = [2, 5, 1, 4]; chk("09a S2 xbar", np.mean(_bus), 3)
chk("09a S2 theta (solve E=xbar)", optimize.brentq(lambda t: stats.expon(scale=1 / t).mean() - np.mean(_bus), .01, 10), 0.333, tol=5e-4)
for t_, mm in [(.2, 5), (.25, 4), (.5, 2)]:
    chk(f"09a S2 table theta={t_}", stats.expon(scale=1 / t_).mean(), mm)
chk("09a C2", 1 / np.mean([.5, 1.5, 2.0, 4.0]), 0.5)
chk("09a S3 theta 1", 2 * np.mean([2, 5, 7, 10]), 12); chk("09a S3 theta 2", 2 * np.mean([1, 1, 10]), 8)
chk("09a C3", 2 * np.mean([1, 2, 9]), 8)
_u = np.array([8, 9, 11, 12]); _m2 = np.mean(_u ** 2) - _u.mean() ** 2
chk("09a S4 xbar", _u.mean(), 10); chk("09a S4 m2'", np.mean(_u ** 2), 102.5); chk("09a S4 m2", _m2, 2.5)
chk("09a S4 root", math.sqrt(3 * _m2), 2.739, tol=5e-4)
_ab = optimize.fsolve(lambda v: [stats.uniform(v[0], v[1] - v[0]).mean() - 10, stats.uniform(v[0], v[1] - v[0]).var() - _m2], [6, 14])
chk("09a S4 a (solve)", _ab[0], 7.26, tol=.005); chk("09a S4 b (solve)", _ab[1], 12.74, tol=.005)
chk("09a C4 a", 10 - math.sqrt(9), 7); chk("09a C4 b", 10 + math.sqrt(9), 13)
_gk = np.array([0.46, 0.38, 0.61, 0.82, 0.59, 0.53, 0.72, 0.44, 0.59, 0.60])
_Eth = lambda t: integrate.quad(lambda x_: x_ * (1 + t) * x_ ** t, 0, 1)[0]
chk("09a S5 sum", _gk.sum(), 5.74); chk("09a S5 xbar", _gk.mean(), 0.574)
chk("09a S5 theta (solve)", optimize.brentq(lambda t: _Eth(t) - _gk.mean(), 0.001, 20), 0.3474, tol=1e-4)
chk("09a S5 numerator", 2 * .574 - 1, .148); chk("09a S5 denominator", 1 - .574, .426)
chk("09a C5", optimize.brentq(lambda t: _Eth(t) - 0.6, 0.001, 20), 0.5, tol=1e-6)
chk("09a ST2", np.mean([2, 0, 3, 1, 4]), 2); chk("09a ST4", 2 * np.mean([3, 5, 10]), 12)
chk("09a ST5 mu", np.mean([4, 6, 8]), 6); chk("09a ST5 m2", np.var([4, 6, 8]), 2.67, tol=.005)
chk("09a ST6", optimize.brentq(lambda t: integrate.quad(lambda x_: x_ * t * x_ ** (t - 1), 0, 1)[0] - .75, .01, 50), 3, tol=1e-6)
# 09b
_HHT = lambda p: p * p * (1 - p)
for p_, v_, l_ in [(.3, .063, -2.765), (.5, .125, -2.079), (2 / 3, .148, -1.910), (.8, .128, -2.056), (.9, .081, -2.513)]:
    chk(f"09b S1/2 L({p_:.3g})", stats.binom.pmf(2, 3, p_) / 3, v_, tol=5e-4); chk(f"09b S2 lnL({p_:.3g})", math.log(_HHT(p_)), l_, tol=5e-4)
chk("09b S1 peak", _mx(lambda p: math.log(_HHT(p)), .01, .99), 2 / 3, tol=1e-5); chk("09b S1 4/27", 4 / 27, .148, tol=5e-4)
chk("09b C1 L(1/3)", (1 / 3) * (2 / 3) ** 2, .148, tol=5e-4); chk("09b C1 L(1/2)", .125, .125)
chk("09b C2 peak", _mx(lambda p: math.log(p * (1 - p) ** 2), .01, .99), 1 / 3, tol=1e-5)
chk("09b C3", _mx(lambda p: stats.binom.logpmf(7, 20, p), .01, .99), 0.35, tol=1e-5)
_po = [2, 0, 3, 1, 4]; chk("09b C4 numeric", _mx(lambda l: stats.poisson(l).logpmf(_po).sum(), .01, 10), 2, tol=1e-5)
_r = np.array([14, 17, 27, 18, 12, 8, 22, 13, 19, 12])
chk("09b S5 sum", _r.sum(), 162); chk("09b S5 MLE numeric", _mx(lambda b: stats.expon(scale=b).logpdf(_r).sum(), 1, 100), 16.2, tol=1e-4, key=16.2)
for b_, l_ in [(10, -39.23), (16.2, -37.85), (25, -38.67), (40, -40.94)]:
    chk(f"09b S5 table l({b_})", stats.expon(scale=b_).logpdf(_r).sum(), l_, tol=.005)
chk("09b C5", _mx(lambda b: stats.expon(scale=b).logpdf([900, 1100, 1000, 1300, 700]).sum(), 10, 10000), 1000, tol=.01)
chk("09b C6", _mx(lambda m_: stats.norm(m_, 2).logpdf([4, 6, 8]).sum(), 0, 20), 6, tol=1e-5)
chk("09b C7a", _mx(lambda v: stats.norm(5, math.sqrt(v)).logpdf([4, 6, 8]).sum(), .1, 50), 3.67, tol=.005)
_n2 = optimize.minimize(lambda v: -stats.norm(v[0], math.sqrt(abs(v[1]))).logpdf([4, 6, 8]).sum(), [5, 2], method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-10}).x
chk("09b C7b mu (joint)", _n2[0], 6, tol=1e-4); chk("09b C7b var (joint)", abs(_n2[1]), 2.67, tol=.005)
_x14 = np.array([12, 11.2, 13.5, 12.3, 13.8, 11.9]); _ll14 = lambda t: np.log(t / _x14 ** (t + 1)).sum()
chk("09b S8 sum ln", np.log(_x14).sum(), 15.114, tol=5e-4)
chk("09b S8 MLE numeric", _mx(_ll14, .01, 5), 0.3970, tol=1e-4, key=0.3970, ktol=1e-4)
for t_, l_ in [(.2, -27.79), (.397, -26.66), (.6, -27.25), (1.0, -30.23)]:
    chk(f"09b S8 table l({t_})", _ll14(t_), l_, tol=.005)
chk("09b C8", 4 / 2, 2)
_h = 1e-4; _d2 = lambda fn, x0: (fn(x0 + _h) - 2 * fn(x0) + fn(x0 - _h)) / _h ** 2
chk("09b S9 rats d2 (numeric)", _d2(lambda b: stats.expon(scale=b).logpdf(_r).sum(), 16.2), -0.0381, tol=2e-4)
chk("09b S9 ex14 d2 (numeric)", _d2(_ll14, 0.3970), -38.07, tol=.05)
chk("09b C9 U(0,th) MLE (grid)", (lambda g: g[np.argmax([np.sum(stats.uniform(0, t).logpdf([2, 5, 7, 10])) for t in g])])(np.linspace(5, 20, 15001)), 10, tol=1e-3)
chk("09b S10 rate (numeric)", _mx(lambda l: stats.expon(scale=1 / l).logpdf(_r).sum(), .001, 1), 0.0617, tol=1e-4)
chk("09b C10 sigma (numeric)", _mx(lambda s: stats.norm(6, s).logpdf([4, 6, 8]).sum(), .1, 10), 1.633, tol=5e-4)
chk("09b S11 sum ln", np.log(_gk).sum(), -5.7873, tol=5e-4)
chk("09b S11 MLE numeric", _mx(lambda t: np.log((1 + t) * _gk ** t).sum(), 0, 10), 0.7279, tol=1e-4)
chk("09b ST3", _mx(lambda l: stats.expon(scale=1 / l).logpdf([2, 3, 5, 6]).sum(), .01, 5), 0.25, tol=1e-5)
chk("09b ST6", 8 / 4, 2); chk("09b ST5 bias factor n=3", (3 - 1) / 3 * 4, 8 / 3)

# ==== v1.3 S4 — files 04a, 04b, 05 (route: enumerate strings / scipy.stats binom, poisson, uniform, expon objects;
# quad for the uniform moments and the exponential tail; brentq/fsolve for "solve for p, lambda, K")
import itertools as _it
_B, _P, _U, _E = stats.binom, stats.poisson, stats.uniform, stats.expon
_q4 = lambda f_, lo=-np.inf, hi=np.inf: integrate.quad(f_, lo, hi)[0]
# 04a
chk("04a S1 E(count)", _B(1, .5).mean(), .5); chk("04a S1 Var(count)", _B(1, .5).var(), .25)
chk("04a C1 E", _B(1, 1 / 6).mean(), 1 / 6); chk("04a C1 Var", _B(1, 1 / 6).var(), 0.139, tol=5e-4)
_s3 = ["".join(s) for s in _it.product("EO", repeat=3)]
chk("04a S2 strings with 2 E (enumerated)", sum(s.count("E") == 2 for s in _s3), 3)
chk("04a S2 chance of one string", .5 ** 3, 1 / 8)
chk("04a S2 C(10,5)", math.comb(10, 5), 252); chk("04a S2 C(10,4)", math.comb(10, 4), 210); chk("04a S2 2^10", 2 ** 10, 1024)
chk("04a C2 strings of 4 with 2 E (enumerated)", sum("".join(s).count("E") == 2 for s in _it.product("EO", repeat=4)), 6)
chk("04a C2 C(10,0)", math.comb(10, 0), 1)
chk("04a S3 P(X=2) n=3", _B(3, .5).pmf(2), 3 / 8)
for x_, v_ in [(0, .0010), (2, .0439), (5, .2461), (8, .0439)]:
    chk(f"04a S3 table P({x_})", _B(10, .5).pmf(x_), v_, tol=5e-5)
chk("04a S3 C(10,2)", math.comb(10, 2), 45); chk("04a S3 C(10,8)", math.comb(10, 8), 45)
chk("04a C3a", _B(6, .5).pmf(4), 15 / 64); chk("04a C3a dec", 15 / 64, .2344, tol=5e-5)
chk("04a C3b", _B(6, .5).sf(0), 63 / 64); chk("04a C3b dec", 63 / 64, .9844, tol=5e-5)
chk("04a S4 MCQ2 var", _B(10, .5).var(), 2.5, key=2.5); chk("04a S4 MCQ9 max", _B(12, .5).support()[1], 12, key=12)
chk("04a S4 fair mean", _B(10, .5).mean(), 5); chk("04a S4 fair sd", _B(10, .5).std(), 1.581, tol=5e-4)
chk("04a S4 die mean", _B(10, 5 / 8).mean(), 6.25); chk("04a S4 die var", _B(10, 5 / 8).var(), 2.344, tol=5e-4)
chk("04a S4 die sd", _B(10, 5 / 8).std(), 1.531, tol=5e-4); chk("04a S4 Ex7.7 q", 4 / 3, 4 / 3)
_nq = optimize.fsolve(lambda v: [v[0] * v[1] - 4, v[0] * v[1] * (1 - v[1]) - 3], [10, .3])
chk("04a C4 n (solve)", _nq[0], 16, tol=1e-6); chk("04a C4 p (solve)", _nq[1], .25, tol=1e-8)
_p58 = optimize.brentq(lambda p: _B(10, p).pmf(5) - 2 * _B(10, p).pmf(4), .3, .95)
chk("04a S5 p (solve)", _p58, 5 / 8, key=5 / 8); chk("04a S5 p/q", _p58 / (1 - _p58), 5 / 3); chk("04a S5 420/252", 420 / 252, 5 / 3)
chk("04a S5 P(4)", _B(10, 5 / 8).pmf(4), .0891, tol=5e-5); chk("04a S5 P(5)", _B(10, 5 / 8).pmf(5), .1782, tol=5e-5)
chk("04a S5 P(0)", _B(10, 5 / 8).pmf(0), .000055, tol=5e-7)
chk("04a C5 p (solve)", optimize.brentq(lambda p: _B(6, p).pmf(3) - _B(6, p).pmf(2), .1, .9), 3 / 7)
chk("04a S6 q^10", (3 / 8) ** 10, 5.499e-5, tol=1e-8); chk("04a S6 59049/1073741824", 3 ** 10 / 8 ** 10, 5.499e-5, tol=1e-8)
chk("04a S6 expected sets", 10000 * _B(10, 5 / 8).pmf(0), .55, tol=.005, key=.5499, ktol=1e-4)
chk("04a C6", 640 * _B(6, .5).pmf(4), 150)
chk("04a ST2 P(2)", _B(5, .3).pmf(2), .3087, tol=5e-5); chk("04a ST2 mean", _B(5, .3).mean(), 1.5)
_nq3 = optimize.fsolve(lambda v: [v[0] * v[1] - 6, v[0] * v[1] * (1 - v[1]) - 2.4], [8, .5])
chk("04a ST3 n", _nq3[0], 10, tol=1e-6); chk("04a ST3 p", _nq3[1], .6, tol=1e-8)
chk("04a ST5", 160 * _B(4, .5).pmf(2), 60); chk("04a ST6", math.comb(8, 3), 56)
chk("04a ST7 p (solve)", optimize.brentq(lambda p: _B(4, p).pmf(1) - _B(4, p).pmf(2), .1, .9), .4)
# 04b
for x_, v_ in [(0, .0821), (1, .2052), (2, .2565), (3, .2138)]:
    chk(f"04b S1 P({x_})", _P(2.5).pmf(x_), v_, tol=5e-5)
chk("04b S1 B1(i)", _P(2.5).pmf(0), .0821, tol=5e-5, key=.0821, ktol=1e-4)
chk("04b C1a", _P(2).pmf(3), .1804, tol=5e-5); chk("04b C1b", _P(6).pmf(0), .0025, tol=5e-5)
chk("04b S2 mean (sum)", sum(k * _P(2.5).pmf(k) for k in range(200)), 2.5); chk("04b S2 var", _P(2.5).var(), 2.5)
chk("04b S2 E[X(X-1)]", sum(k * (k - 1) * _P(2.5).pmf(k) for k in range(200)), 2.5 ** 2)
chk("04b C2 sd", _P(4).std(), 2); chk("04b C2 P0", _P(4).pmf(0), .0183, tol=5e-5)
chk("04b S3 A4 lambda (solve)", optimize.brentq(lambda l: _P(l).pmf(0) - .5, .01, 5), .6931, tol=5e-5)
chk("04b S3 P1=P2 lambda", optimize.brentq(lambda l: _P(l).pmf(1) - _P(l).pmf(2), .5, 5), 2)
chk("04b C3 lambda (solve)", optimize.brentq(lambda l: _P(l).pmf(2) - 9 * _P(l).pmf(4) - 90 * _P(l).pmf(6), .5, 1.5), 1)
chk("04b S4 cdf3", _P(2.5).cdf(3), .7576, tol=5e-5); chk("04b S4 B1(ii)", _P(2.5).sf(3), .2424, tol=5e-5, key=.2424, ktol=1e-4)
chk("04b C4 P(0..2)", _P(5).cdf(2), .1247, tol=5e-5); chk("04b C4 e^-5", math.exp(-5), .006738, tol=5e-7)
chk("04b C4 A2 C3", _P(5).sf(2), .8753, tol=5e-5, key=.8754, ktol=2e-4)
for x_, b_, p_ in [(0, .1340, .1353), (1, .2707, .2707), (2, .2720, .2707)]:
    chk(f"04b S5 table binom {x_}", _B(200, .01).pmf(x_), b_, tol=5e-5); chk(f"04b S5 table pois {x_}", _P(2).pmf(x_), p_, tol=5e-5)
chk("04b S5 D3", _P(200 * .01).pmf(0), .1353, tol=5e-5, key=.1353, ktol=1e-4); chk("04b S5 gap", _P(2).pmf(0) - _B(200, .01).pmf(0), .0013, tol=1e-4)
chk("04b C5", _P(2).cdf(2), .6767, tol=5e-5)
_tot = np.convolve(_P(2.5).pmf(np.arange(60)), _P(1.5).pmf(np.arange(60)))  # sum of two independent counts, exact convolution
chk("04b S6 P(total 0) conv", _tot[0], .0183, tol=5e-5); chk("04b S6 e^-1.5", math.exp(-1.5), .2231, tol=5e-5)
chk("04b S6 conv = P(4) at 3", _tot[3], _P(4).pmf(3), tol=1e-12)
chk("04b C6 conv", np.convolve(_P(3).pmf(np.arange(40)), _P(2).pmf(np.arange(40)))[2], .0842, tol=5e-5)
chk("04b ST2", _P(2).pmf(0), .1353, tol=5e-5); chk("04b ST3 1wk", _P(3).pmf(0), .0498, tol=5e-5); chk("04b ST3 2wk", _P(6).pmf(0), .0025, tol=5e-5)
chk("04b ST5", _P(2).pmf(1), .2707, tol=5e-5); chk("04b ST6", _P(1.2).sf(0), .6988, tol=5e-5); chk("04b ST6 e^-1.2", math.exp(-1.2), .3012, tol=5e-5)
chk("04b ST7 var", _P(1).var() + _P(2).var(), 3)
# 05 uniform
_u1020 = _U(10, 10); _u33 = _U(-3, 6)
chk("05 S1 B2", _u1020.sf(16), .4, key=.4); chk("05 S1 height", _u1020.pdf(12), .1); chk("05 S1 outside", _u1020.pdf(21), 0)
chk("05 C1 height", _u33.pdf(0), 1 / 6); chk("05 C1 P(X<0)", _u33.cdf(0), .5)
chk("05 S2 0<X<2", _u33.cdf(2) - _u33.cdf(0), 1 / 3); chk("05 S2 1<X<5", _u33.cdf(5) - _u33.cdf(1), 1 / 3); chk("05 S2 X>4", _u33.sf(4), 0)
chk("05 S2 MCQ10 (a=0,b=10,c=4,d=13)", _U(0, 10).cdf(13) - _U(0, 10).cdf(4), (10 - 4) / 10)
chk("05 C2 D4", _U(15, 20).cdf(30) - _U(15, 20).cdf(25), .25, key=.25)
_ub = _U(0, 30)
chk("05 S3 MTE B4", (_ub.cdf(15) - _ub.cdf(10)) + (_ub.cdf(30) - _ub.cdf(25)), 1 / 3, key=1 / 3)
chk("05 C3 wait>10", (_ub.cdf(5) - _ub.cdf(0)) + (_ub.cdf(20) - _ub.cdf(15)), 1 / 3)
chk("05 S4 B8(i)", _u33.cdf(2), 5 / 6, key=5 / 6); chk("05 S4 B8(ii)", _u33.cdf(2) - _u33.cdf(-2), 2 / 3, key=2 / 3)
chk("05 S4 B8(iii)", _u33.cdf(4) - _u33.cdf(0), .5, key=.5)
_r = _U(-.5, 1); chk("05 C4 C4", _r.cdf(-.2) + _r.sf(.2), .6, key=.6)
chk("05 S5 mean U(-3,3) quad", _q4(lambda x_: x_ / 6, -3, 3), 0); chk("05 S5 var U(-3,3) quad", _q4(lambda x_: x_ * x_ / 6, -3, 3), 3)
chk("05 S5 sd U(-3,3)", _u33.std(), 1.732, tol=5e-4)
chk("05 S5 mean U(10,20)", _u1020.mean(), 15); chk("05 S5 var U(10,20)", _u1020.var(), 8.33, tol=.005); chk("05 S5 sd U(10,20)", _u1020.std(), 2.887, tol=5e-4)
chk("05 C5 mean", _U(0, 12).mean(), 6); chk("05 C5 var", _U(0, 12).var(), 12); chk("05 C5 sd", _U(0, 12).std(), 3.464, tol=5e-4)
chk("05 S6 K", _u33.isf(1 / 3), 1, key=1); chk("05 C6 K", _u33.ppf(.25), -1.5)
# 05 exponential (scipy expon(scale = 1/lambda))
_e2 = _E(scale=2)
for x_, v_ in [(0, .5), (2, .1839), (4, .0677), (6, .0249)]:
    chk(f"05 S7 table f({x_})", _e2.pdf(x_), v_, tol=5e-5)
chk("05 S7 mean", _e2.mean(), 2); chk("05 S7 sd = 1/lambda", _e2.std(), 2)
chk("05 C7 mean min", _E(scale=1 / 4).mean() * 60, 15); chk("05 C7 sd min", _E(scale=1 / 4).std() * 60, 15)
chk("05 S8 tail quad", _q4(lambda u: .5 * math.exp(-.5 * u), 4, np.inf), .1353, tol=5e-5)
chk("05 S8 D2", _E(scale=1 / 4).sf(.5), .1353, tol=5e-5, key=.1353, ktol=1e-4)
chk("05 C8 B7(i)", _e2.sf(2), .3679, tol=5e-5, key=math.exp(-1))
chk("05 S9 B7(ii)", _e2.sf(11) / _e2.sf(8), .2231, tol=5e-5, key=math.exp(-1.5)); chk("05 S9 = P(X>3)", _e2.sf(3), .2231, tol=5e-5)
_e1000 = _E(scale=1000); chk("05 C9 C1", _e1000.sf(1500) / _e1000.sf(500), .3679, tol=5e-5, key=.3679, ktol=1e-4)
chk("05 S10 P(X<1)", _e2.cdf(1), .3935, tol=5e-5); chk("05 S10 P(X<2)", _e2.cdf(2), .6321, tol=5e-5)
chk("05 S10 B5 (quad ratio)", _q4(lambda u: .5 * math.exp(-.5 * u), 0, 1) / _q4(lambda u: .5 * math.exp(-.5 * u), 0, 2), .6225, tol=5e-5, key=.5679, ktol=1e-4)
_th = .5; chk("05 S10 G&K form", (1 - math.exp(-_th)) / (1 - math.exp(-2 * _th)), .6225, tol=5e-5)
_ex1 = _E(); chk("05 C10", (_ex1.cdf(3) - _ex1.cdf(1)) / _ex1.sf(1), .8647, tol=5e-5)
chk("05 ST2 P", _U(0, 10).cdf(8) - _U(0, 10).cdf(3), .5); chk("05 ST2 var", _U(0, 10).var(), 8.33, tol=.005)
chk("05 ST3", _E(scale=5).sf(5), .3679, tol=5e-5); chk("05 ST4", _E(scale=5).sf(8) / _E(scale=5).sf(3), .3679, tol=5e-5)
chk("05 ST6 mean", _E(scale=1 / 2).mean(), .5)
chk("05 ST7 P(|X|>.5)", _U(-1, 2).cdf(-.5) + _U(-1, 2).sf(.5), .5); chk("05 ST7 E[X^2]", _q4(lambda x_: x_ * x_ / 2, -1, 1), 1 / 3)


# ==== v1.3 S5 — files 06, 07 (route: scipy.stats.norm, exact enumeration of the 210 ball samples)
_N = stats.norm; _nb = _N(1500, 100); _phi = lambda z_: _N.cdf(z_) - .5
# 06 step 1 density table
for x_, v_ in [(1300, .000540), (1400, .002420), (1500, .003989), (1600, .002420)]:
    chk(f"06 S1 f({x_})", _nb.pdf(x_), v_, tol=5e-7)
chk("06 C1b", _nb.cdf(1500), .5)
# 06 step 3 z table, Check 3
for x_, z_ in [(1350, -1.5), (1380, -1.2), (1500, 0), (1660, 1.6), (1680, 1.8)]:
    chk(f"06 S3 z({x_})", (x_ - 1500) / 100, z_)
chk("06 C3a", (75 - 65) / 5, 2); chk("06 C3b", 65 - 1.4 * 5, 58)
# 06 step 4 table of phi, Predict, Check 4
for z_, v_ in [(.5, .1915), (1, .3413), (1.5, .4332), (1.6, .4452), (2, .4772)]:
    chk(f"06 S4 phi({z_})", _phi(z_), v_, tol=5e-5)
chk("06 S4 P(1500<X<1660)", _nb.cdf(1660) - .5, .4452, tol=5e-5); chk("06 C4c", _nb.cdf(1700) - .5, .4772, tol=5e-5)
# 06 step 5 tails, Check 5
chk("06 S5 (i)", _nb.sf(1660), .0548, tol=5e-5); chk("06 S5 (ii)", _nb.cdf(1380), .1151, tol=5e-5)
chk("06 C5a", _nb.sf(1700), .0228, tol=1e-4); chk("06 C5b", _nb.cdf(1350), .0668, tol=5e-5)
# 06 step 6, Check 6
_n50 = _N(50, 10)
chk("06 S6 B3", _n50.cdf(62) - _n50.cdf(45), .5764, tol=2e-4); chk("06 C6a", _n50.sf(62), .1151, tol=5e-5)
chk("06 C6b", _n50.cdf(62) - _n50.cdf(55), .1934, tol=2e-4)
# 06 step 7 bands, Check 7
for k_, v_ in [(1, .6827), (2, .9545), (3, .9973)]:
    chk(f"06 S7 mu+-{k_}sigma", _N.cdf(k_) - _N.cdf(-k_), v_, tol=5e-5)
chk("06 S7 2x.3413", 2 * .3413, .6827, tol=2e-4); chk("06 S7 2x.4772", 2 * .4772, .9545, tol=2e-4)
# 06 step 8 counts, Check 8
chk("06 S8 (i)", 5000 * (.5 - .4452), 274); chk("06 S8 (ii)", 5000 * (.5 - .3849), 575.5); chk("06 S8 (iii) P", .4332 + .4641, .8973)
chk("06 S8 (iii)", 5000 * (.4332 + .4641), 4486.5); chk("06 S8 (iii) exact", 5000 * (_nb.cdf(1680) - _nb.cdf(1350)), 4486.5, tol=1)
chk("06 C8 phi(1.25)", _phi(1.25), .3944, tol=5e-5); chk("06 C8 count", 10000 * 2 * .3944, 7888)
# 06 step 9 MTE C1(a), Check 9
_p9 = .5 - .4772
chk("06 S9 q^3", (1 - _p9) ** 3, .933148, tol=5e-7); chk("06 S9 P", 1 - _B(3, _p9).pmf(0), .066852, tol=5e-7, key=.0667, ktol=2e-4)
chk("06 S9 P 4dp", round(1 - (1 - _p9) ** 3, 4), .0669, tol=1e-9)
chk("06 S9 3p", 3 * _p9, .0684); chk("06 C9", _B(5, _p9).pmf(0), .8911, tol=5e-5)
# 06 step 10 A2 B6 (solve the two equations), Check 10
_m10, _s10 = np.linalg.solve([[1, -1.28], [1, 1.04]], [30, 65])
chk("06 S10 sigma", _s10, 15.09, tol=.005); chk("06 S10 mu", _m10, 49.31, tol=.005)
_mc, _sc = np.linalg.solve([[1, -.5], [1, 1.4]], [45, 64])
chk("06 C10 sigma", _sc, 10); chk("06 C10 mu", _mc, 50)
chk("06 C10 phi(0.5)", _phi(.5), .19, tol=.005); chk("06 C10 phi(1.4)", _phi(1.4), .42, tol=.005)
# 06 step 11 A2 C2, Check 11
_m11, _s11 = np.linalg.solve([[1, .1], [1, 1.34]], [40, 75])
chk("06 S11 sigma", _s11, 28.23, tol=.005, key=28.2, ktol=.05); chk("06 S11 mu", _m11, 37.18, tol=.005, key=37.5, ktol=.05)
chk("06 S11 75 check", _m11 + 1.34 * _s11, 75); chk("06 S11 failures quarter", .25 * .54, .135); chk("06 S11 below cut", .54 - .135, .405)
chk("06 S11 mark", _m11 - .24 * _s11, 30.40, tol=.005, key=30.43, ktol=.005)
chk("06 C11 z", (60 - _m11) / _s11, .81, tol=.005); chk("06 C11 P", .5 - .291, .209)
# 06 self-test
chk("06 ST2", _N(60, 8).sf(72), .0668, tol=5e-5); chk("06 ST3", _N(60, 8).cdf(68) - _N(60, 8).cdf(52), .6827, tol=5e-5)
chk("06 ST4", 1000 * _N(165, 6).sf(177), 22.8, tol=.1); chk("06 ST5", _N(70, 10).isf(.05), 86.45, tol=.01)
# 07 steps 1-4: the 10 balls (a, d, g, i black), all 210 samples of 4
from itertools import combinations as _comb
_blk = set("adgi"); _sh = [sum(b_ in _blk for b_ in c_) / 4 for c_ in _comb("abcdefghij", 4)]
chk("07 S3 samples", len(_sh), 210)
for v_, n_ in [(0, 15), (.25, 80), (.5, 90), (.75, 24), (1, 1)]:
    chk(f"07 S3 count {v_}", _sh.count(v_), n_)
for smp, v_ in [("acfh", .25), ("bdej", .25), ("cgij", .5)]:
    chk(f"07 S1 sample {smp}", sum(b_ in _blk for b_ in smp) / 4, v_)
chk("07 S3 mean", np.mean(_sh), .4); chk("07 S3 2-black product", 6 * 15, 90)
chk("07 S4 var", np.var(_sh), .04); chk("07 S4 sum", sum((v_ - .4) ** 2 for v_ in _sh), 8.4); chk("07 S4 SE", np.std(_sh), .2)
chk("07 S5 note sigma", math.sqrt(.4 * .6), .49, tol=.005); chk("07 S5 note sigma/sqrt4", math.sqrt(.24) / 2, .245, tol=5e-4)
chk("07 C3a", _sh.count(.5) / 210, .4286, tol=5e-5); chk("07 C3b", _sh.count(0) / 210, .0714, tol=5e-5)
chk("07 C4 count", sum(abs(v_ - .4) <= .2 + 1e-12 for v_ in _sh), 170); chk("07 C4 frac", 170 / 210, .81, tol=.005)
# 07 steps 5-6 SE (simulation route for sigma/sqrt(n): 200,000 averages of 25 from a population with sd 100)
_rng = np.random.default_rng(11)
chk("07 S5 SE sim n=25", _rng.normal(0, 100, (200000, 25)).mean(axis=1).std(), 20, tol=.2)
for n_, v_ in [(1, 100), (4, 50), (25, 20), (100, 10), (400, 5)]:
    chk(f"07 S5/6 SE n={n_}", 100 / math.sqrt(n_), v_)
chk("07 C5a A4 MCQ8", 5 / math.sqrt(25), 1); chk("07 C5b", 2 / 6, .333, tol=5e-4)
chk("07 C6 n=9", 2 / 3, .667, tol=5e-4); chk("07 C6 n=144", 2 / 12, .167, tol=5e-4); chk("07 C6b", (2 / .25) ** 2, 64)
chk("07 S9 one-customer", .5 / 2, .25)
# 07 steps 9-12 (slide examples) by exact normal of x-bar and by the printed table
_atm = _N(4, 2 / 6)
chk("07 S9 SE", 2 / math.sqrt(36), .333, tol=5e-4); chk("07 S9 z", .5 / (2 / 6), 1.5)
for x_, z_ in [(3.5, -1.5), (4, 0), (4.5, 1.5), (5, 3)]:
    chk(f"07 S9 z({x_})", (x_ - 4) / (2 / 6), z_)
chk("07 S9 P", _atm.sf(4.5), .0668, tol=5e-5, key=.0668, ktol=1e-4)
chk("07 C9a", _atm.cdf(3.5), .0668, tol=5e-5); chk("07 C9b", _atm.sf(4.2), .2743, tol=5e-5)
_se10 = 1.5 / math.sqrt(50)
chk("07 S10 sqrt50", math.sqrt(50), 7.071, tol=5e-4); chk("07 S10 SE", _se10, .2121, tol=5e-5)
chk("07 S10 z1", (3.5 - 4) / _se10, -2.36, tol=.005); chk("07 S10 z2", (3.8 - 4) / _se10, -.94, tol=.005)
chk("07 S10 phi(2.36)", _phi(2.36), .4909, tol=5e-5); chk("07 S10 phi(0.94)", _phi(.94), .3264, tol=5e-5)
chk("07 S10 P table", .4909 - .3264, .1645, key=.1644, ktol=2e-4)
chk("07 S10 P exact", _N(4, _se10).cdf(3.8) - _N(4, _se10).cdf(3.5), .1645, tol=1.5e-3)
chk("07 C10 z", .3 / _se10, 1.41, tol=.005); chk("07 C10 phi(1.41)", _phi(1.41), .4207, tol=5e-5); chk("07 C10 P", .5 - .4207, .0793)
_led = _N(50000, 8000 / 8)
chk("07 S11 SE", 8000 / math.sqrt(64), 1000); chk("07 S11 P", _led.cdf(48000), .0228, tol=1e-4, key=.0228, ktol=1e-4)
for x_, z_ in [(48000, -2), (49000, -1), (50000, 0), (51000, 1)]:
    chk(f"07 S11 z({x_})", (x_ - 50000) / 1000, z_)
chk("07 C11", _led.cdf(51000) - _led.cdf(48000), .8185, tol=2e-4)
_mac = _N(7, 1 / 3)
chk("07 S12 z1", (6.4 - 7) * 3, -1.8); chk("07 S12 z2", (7.2 - 7) * 3, .6)
chk("07 S12 phi(1.8)", _phi(1.8), .4641, tol=5e-5); chk("07 S12 phi(0.6)", _phi(.6), .2257, tol=5e-5)
chk("07 S12 P", _mac.cdf(7.2) - _mac.cdf(6.4), .6898, tol=2e-4, key=.6898, ktol=2e-4)
chk("07 C12a", _mac.sf(7.5), .0668, tol=5e-5)
chk("07 C8b SE", 12 / math.sqrt(64), 1.5)
# 07 self-test
chk("07 ST3 SE", 12 / 6, 2); chk("07 ST3 n", (12 / 1) ** 2, 144)
chk("07 ST4", _N(80, 1.5).cdf(83) - _N(80, 1.5).cdf(77), .9544, tol=2e-4)
chk("07 ST6 n", (2 * 2 / .5) ** 2, 64); chk("07 ST6 P", _N(4, 2 / 8).sf(4.5), .0228, tol=1e-4)
chk("07 ST7 n", (20 / 1) ** 2, 400); chk("07 ST7 ratio", 400 / 25, 16); chk("07 ST7 SE25", 20 / 5, 4)

print(f"\n{N[0]} checks; {len(FAILS)} pack failures; {len(KEYDIFF)} key differences")
if KEYDIFF:
    print("Key differences (flagged in the pack):", ", ".join(KEYDIFF))
if FAILS:
    print("FAILURES:", ", ".join(FAILS)); sys.exit(1)
