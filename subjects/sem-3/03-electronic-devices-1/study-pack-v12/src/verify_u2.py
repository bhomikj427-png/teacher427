"""Recompute every number printed in 02a-drift and 02b-diffusion-continuity.

Run: python verify_u2.py   (exits non-zero on any mismatch)
Each check computes the value from the formula and compares it with the value the pack prints.
Where an independent route exists (e.g. R from ρL/A and from J·A), both are computed.
"""
import math
import sys

q, k_J, m0, eps0 = 1.602e-19, 1.381e-23, 9.109e-31, 8.854e-14   # eps0 in F/cm
kT = 0.0259
fails = []


def chk(name, got, printed, rel=0.02):
    ok = abs(got - printed) <= rel * abs(printed)
    print(f"{'ok ' if ok else 'BAD'} {name}: computed {got:.4g}, printed {printed:.4g}")
    if not ok:
        fails.append(name)


def mu_fit(N, c="n"):
    mmax, mmin, nref, a = (1430, 80, 1.12e17, 0.72) if c == "n" else (460, 45, 2.23e17, 0.72)
    return mmin + (mmax - mmin) / (1 + (N / nref) ** a)


# ================= 02a =================
# step 1: thermal velocity with free-electron mass; distance between collisions
vth = math.sqrt(3 * k_J * 300 / m0) * 100          # cm/s
chk("v_th (free-electron mass) cm/s", vth, 1.2e7, 0.03)
chk("mean free path 1e7 cm/s * 0.2 ps (nm)", 1e7 * 0.2e-12 * 1e7, 20)
# step 2
chk("v_d electrons mu=1350 E=100", 1350 * 100, 1.35e5)
chk("v_th / v_d", 1.17e7 / 1.35e5, 87, 0.02)
chk("v_d holes mu=480 E=100", 480 * 100, 4.8e4)
tau = 0.135 * 0.26 * m0 / q                          # SI: mu in m^2/Vs
chk("tau from mu=1350, m*=0.26 m0 (ps)", tau * 1e12, 0.20, 0.03)
chk("1 V across 100 um = V/cm", 1 / 100e-4, 100)
# step 3: saturation
chk("E where mu_n E = vsat (V/cm)", 1e7 / 1350, 7.4e3)
chk("E where mu_p E = vsat (V/cm)", 1e7 / 480, 2.1e4, 0.01)
chk("v at E=E_c (half vsat)", 1350 * 7407 / (1 + 1350 * 7407 / 1e7), 5e6, 0.01)
chk("v at 1e5 V/cm, model", 1350 * 1e5 / (1 + 1350 * 1e5 / 1e7), 9.3e6)
chk("mu E at 1e5 (no saturation)", 1350 * 1e5, 1.35e8)
chk("1 V over 100 nm in V/cm", 1 / 100e-7, 1e5)
# step 4: mobility table
for N, c, pr in ((1e14, "n", 1420), (1e16, "n", 1230), (1e17, "n", 780), (5e17, "n", 420), (1e18, "n", 310),
                 (1e14, "p", 460), (1e16, "p", 420), (1e17, "p", 310), (1e18, "p", 150)):
    chk(f"mu_{c}({N:.0e})", mu_fit(N, c), pr, 0.02)
chk("lattice mu 300->400 K factor", (400 / 300) ** -1.5, 0.65, 0.01)
chk("mu_n at 400 K from 1430", 1430 * (400 / 300) ** -1.5, 930, 0.01)
# step 5
chk("J drift n=1e16 mu 1350 E 10", 1.6e-19 * 1e16 * 1350 * 10, 21.6)
# step 6 (deck slide 51)
s_i = 1.6e-19 * 1e10 * (1500 + 450)
chk("sigma intrinsic (ni=1e10)", s_i, 3.12e-6)
chk("rho intrinsic", 1 / s_i, 3.2e5)
chk("sigma intrinsic ni=1.5e10", 1.6e-19 * 1.5e10 * 1950, 4.68e-6)
chk("rho intrinsic ni=1.5e10", 1 / (1.6e-19 * 1.5e10 * 1950), 2.14e5)
chk("slide table 45C/25C n_i ratio", 3.5e10 / 8.1e9, 4.3, 0.02)
chk("slide table 35C/25C", 1.7e10 / 8.1e9, 2.1, 0.01)
# step 7 (deck slide 52)
chk("mu implied by slide 52 sigma=32", 32 / (1.6e-19 * 5e17), 400)
chk("sigma with mu=1500 at 5e17", 1.6e-19 * 5e17 * 1500, 120)
chk("sigma with model mu at 5e17", 1.6e-19 * 5e17 * mu_fit(5e17), 34, 0.02)
chk("sigma ratio 32/3.12e-6", 32 / 3.12e-6, 1.03e7, 0.01)
chk("one donor per 5e22/5e17 atoms", 5e22 / 5e17, 1e5)
chk("minority p for ND=5e17, ni=1e10", 1e20 / 5e17, 200)
chk("minority term / majority term", 200 * 450 / (5e17 * 400), 4.5e-16, 0.02)
chk("ND=1e16 sigma with mu 1230", 1.6e-19 * 1e16 * 1230, 1.97)
chk("ND=1e16 rho", 1 / (1.6e-19 * 1e16 * 1230), 0.508)
chk("NA=1e16 sigma mu 420", 1.6e-19 * 1e16 * 420, 0.672)
chk("NA=1e16 rho", 1 / 0.672, 1.49)
# step 8: bar
R = 0.5 * 0.1 / (0.01 * 0.01)
chk("bar R = rho L / A", R, 500)
chk("bar I at 5 V (mA)", 5 / R * 1e3, 10)
chk("bar field 5 V / 0.1 cm", 5 / 0.1, 50)
chk("bar J = sigma E", (1 / 0.5) * 50, 100)
chk("bar I = J A (mA) independent route", 100 * 1e-4 * 1e3, 10)
chk("bar R doubled L", 2 * R, 1000)
chk("bar R halve W and t", R * 4, 2000)
# step 9: sheet
chk("Rs = 0.01/1e-4", 0.01 / 1e-4, 100)
chk("R = 100 * 200/10", 100 * 200 / 10, 2000)
chk("Rs for rho=0.5, 1 um", 0.5 / 1e-4, 5000)
chk("squares for 10k at 200 ohm/sq", 10e3 / 200, 50)
chk("L for 50 squares at W=5um (um)", 50 * 5, 250)
# self-test 02a
chk("ST1 NA=1e17 sigma (mu_p 310)", 1.6e-19 * 1e17 * 310, 4.96)
chk("ST1 rho", 1 / (1.6e-19 * 1e17 * 310), 0.202, 0.01)
chk("ST2 v_d mu 480 E 500", 480 * 500, 2.4e5)
chk("ST3 Rs 50, L 300 W 6", 50 * 300 / 6, 2500)
chk("ST4 R = rho L/A 1.5 ohm cm, 2 mm, 0.5mm x 0.5mm", 1.5 * 0.2 / (0.05 * 0.05), 120)
chk("ST6 Rs for t=2um rho=0.02", 0.02 / 2e-4, 100)

# ================= 02b =================
VT = kT
chk("Fick flux slope", 35 * (1e17 - 1e16) / 1e-4, 3.15e22)
chk("diff J dn/dx=-1e18, D=35", 1.6e-19 * 35 * -1e18, -5.6)
chk("hole diff J dp/dx=-1e18, D=12.4", -1.6e-19 * 12.4 * -1e18, 1.98)
# total current
chk("total: drift part", 1.6e-19 * 1e16 * 1350 * 10, 21.6)
chk("total: sum", 21.6 - 5.6, 16.0)
chk("gradient that cancels drift", -1e16 * 1350 * 10 / 35, -3.86e18)
# equilibrium: built-in potential across 1e17 -> 1e15
chk("built-in potential kT ln(100)", kT * math.log(100), 0.119)
chk("E_C - E_F at n=1e17", kT * math.log(2.8e19 / 1e17), 0.146)
chk("E_C - E_F at n=1e15", kT * math.log(2.8e19 / 1e15), 0.265)
# Einstein
chk("D_n = 1350 V_T", 1350 * VT, 35.0)
chk("D_p = 480 V_T", 480 * VT, 12.4)
chk("V_T at 400 K", 8.617e-5 * 400, 0.0345)
chk("D_n at 400 K mu 1000", 1000 * 8.617e-5 * 400, 34.5)
chk("D_n for mu 1500", 1500 * VT, 38.9)
# direct G-R photon wavelengths
chk("lambda GaAs 1.42 eV (nm)", 1240 / 1.42, 873)
chk("lambda Si 1.12 eV (nm)", 1240 / 1.12, 1107)
# SRH low-injection reduction: n-type ND=1e16, ni=1e10, dp=1e12, tau=1us, mid-gap trap
ND, ni, dp, tp, tn = 1e16, 1e10, 1e12, 1e-6, 1e-6
p0 = ni ** 2 / ND
n, p = ND + dp, p0 + dp
U = (n * p - ni ** 2) / (tp * (n + ni) + tn * (p + ni))
chk("SRH exact vs dp/tau", U, dp / tp, 0.02)
# lifetime
chk("dp after 1 tau", 1e14 * math.exp(-1), 3.68e13)
chk("dp after 3 tau", 1e14 * math.exp(-3), 4.98e12)
chk("e^-2", math.exp(-2), 0.135, 0.01)
chk("time to 1% (tau units)", math.log(100), 4.6)
chk("half-life (tau units)", math.log(2), 0.693, 0.001)
# diffusion length
Lp = math.sqrt(12.4 * 1e-6)
chk("L_p um", Lp * 1e4, 35.2)
chk("dp(50um)/Δp(0)", math.exp(-50e-4 / Lp), 0.242)
chk("dp(50um)", 1e14 * math.exp(-50e-4 / Lp), 2.42e13)
chk("L_n um D 35 tau 1us", math.sqrt(35e-6) * 1e4, 59.2)
chk("L ratio when tau x4", math.sqrt(4), 2)
chk("hole current at x=0: q D dp/L (A/cm2)", 1.6e-19 * 12.4 * 1e14 / Lp, 0.0564)
# numerical check that e^{-x/L} solves D p'' = p/tau
h = 1e-6
f = lambda x: math.exp(-x / Lp)
x0 = 20e-4
d2 = (f(x0 + h) - 2 * f(x0) + f(x0 - h)) / h ** 2
chk("D p'' = p/tau (numerical)", 12.4 * d2, f(x0) / 1e-6, 1e-3)
# Poisson
eps = 11.7 * eps0
chk("field rise across 1 um of N_D=1e16", 1.6e-19 * 1e16 * 1e-4 / eps, 1.54e5, 0.005)
chk("eps_Si F/cm", eps, 1.036e-12, 0.01)
chk("lambda 1.97 eV (nm)", 1240 / 1.97, 629)
# self-test 02b
chk("ST D_p mu 450", 450 * VT, 11.7, 0.01)
chk("ST L sqrt(10 * 1e-7) um", math.sqrt(10 * 1e-7) * 1e4, 10)
chk("ST fraction after 2 tau", math.exp(-2), 0.135, 0.01)
chk("ST diff J holes dp/dx = 1e19, D 12", -1.6e-19 * 12 * 1e19, -19.2)

if fails:
    print("\nFAILED:", fails)
    sys.exit(1)
print("\nall checks pass")
