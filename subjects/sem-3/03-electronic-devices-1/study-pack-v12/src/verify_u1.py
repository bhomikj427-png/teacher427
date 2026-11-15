"""Recompute every number printed in 01a-silicon-bands-carriers and 01b-fermi-level.

Run: python verify_u1.py   (exits non-zero on any mismatch)
Each check computes the value from first principles and compares it with the value the pack prints.
"""
import math
import sys

k_eV = 8.617e-5          # eV/K
k_J, h, m0, q = 1.381e-23, 6.626e-34, 9.109e-31, 1.602e-19
T = 300
kT = k_eV * T            # 0.02585 eV; pack prints 0.0259
fails = []


def chk(name, got, printed, rel=0.02):
    ok = abs(got - printed) <= rel * abs(printed)
    print(f"{'ok ' if ok else 'BAD'} {name}: computed {got:.4g}, printed {printed:.4g}")
    if not ok:
        fails.append(name)


def f(dE, kt=0.0259):
    return 1 / (1 + math.exp(dE / kt))


# ---- 01a -------------------------------------------------------------
chk("kT at 300 K (eV)", kT, 0.0259, 0.01)
chk("one bond in 10^12 (5e22/1.5e10 ~ 3e12)", 5e22 / 1.5e10, 3.3e12, 0.02)
# n_i ratio per +10 K, E_g held at 1.12 eV: (T2/T1)^1.5 * exp(Eg/2k (1/T1 - 1/T2))
r10 = (310 / 300) ** 1.5 * math.exp(1.12 / (2 * k_eV) * (1 / 300 - 1 / 310))
chk("n_i ratio 300->310 K", r10, 2.1, 0.03)
chk("deck table 35C/25C", 1.7e10 / 8.1e9, 2.1, 0.03)
# Check 1a(c): 300 -> 330 K = three doublings
chk("n_i ratio 300->330 K", (330 / 300) ** 1.5 * math.exp(1.12 / (2 * k_eV) * (1 / 300 - 1 / 330)), 8.3, 0.02)
# Exp factor only: e^{-Eg/2kT} for Ge, Si, GaAs at 300 K
for name, Eg, pr in (("Ge", 0.66, 2.8e-6), ("Si", 1.12, 4.1e-10), ("GaAs", 1.42, 1.2e-12)):
    chk(f"e^(-Eg/2kT) {name}", math.exp(-Eg / (2 * kT)), pr, 0.05)
# Doping worked example + Checks (n_i = 1.5e10 deck value)
ni = 1.5e10
chk("ND=1e16: p", ni ** 2 / 1e16, 2.25e4)
chk("ND=1e16, ni=1e10: p", 1e20 / 1e16, 1e4)
chk("NA=5e17: n", ni ** 2 / 5e17, 450)
chk("compensated NA=1e16, ND=4e15: p", 1e16 - 4e15, 6e15)
chk("compensated: n", ni ** 2 / 6e15, 3.75e4)
chk("ppm doping: 1e-6 * 5e22", 1e-6 * 5e22, 5e16)
chk("ppm doping vs n_i ratio", 5e16 / ni, 3.3e6, 0.02)
# quadratic for ND = 1e10 (comparable to n_i=1.5e10)
ND = 1e10
n = ND / 2 + math.sqrt((ND / 2) ** 2 + ni ** 2)
chk("quadratic ND=1e10: n", n, 2.08e10)
chk("quadratic ND=1e10: p", ni ** 2 / n, 1.08e10)
# self-test 01a
chk("ST ND=1e15 p (ni=1e10)", 1e20 / 1e15, 1e5)
chk("ST ND=2e17 NA=5e16 n", 2e17 - 5e16, 1.5e17)
chk("ST ND=2e17 NA=5e16 p", ni ** 2 / 1.5e17, 1500)
chk("ST binding P / kT", 0.045 / 0.0259, 1.74)

# ---- 01b -------------------------------------------------------------
for dE, pr in ((0.0, 0.5), (0.0259, 0.269), (0.0518, 0.119), (0.0777, 0.0474), (0.1, 0.0206), (-0.0777, 0.953),
               (0.2, 4.43e-4), (-0.2, 0.99956)):
    chk(f"f at E-EF = {dE}", f(dE), pr)
chk("Boltzmann at 3kT", math.exp(-3), 0.0498)
chk("Boltzmann error at 3kT (%)", (math.exp(-3) / f(3 * 0.0259) - 1) * 100, 5.0, 0.03)
chk("f at 0.56 eV (mid-gap to E_C)", f(0.56), 4.1e-10, 0.05)
chk("f at 0.1 eV, T=600 K", f(0.1, k_eV * 600), 0.127, 0.03)
# N_C, N_V from effective masses
NC = 2 * (2 * math.pi * 1.08 * m0 * k_J * T / h ** 2) ** 1.5 / 1e6
NV = 2 * (2 * math.pi * 0.56 * m0 * k_J * T / h ** 2) ** 1.5 / 1e6
chk("N_C (cm^-3)", NC, 2.8e19)
chk("N_V (cm^-3)", NV, 1.04e19, 0.03)
chk("N_C at 600 K / 300 K", 2 ** 1.5, 2.83)
chk("electron seats vs atoms", 2.8e19 / 5e22, 5.6e-4)
# n from E_C - E_F
chk("n for Ec-EF=0.25 eV", 2.8e19 * math.exp(-0.25 / 0.0259), 1.8e15)
chk("p for EF-Ev=0.20 eV", 1.04e19 * math.exp(-0.20 / 0.0259), 4.6e15, 0.03)
chk("Ec-EF for n=1e16", 0.0259 * math.log(2.8e19 / 1e16), 0.206)
# n_i from N_C N_V
ni_calc = math.sqrt(2.8e19 * 1.04e19) * math.exp(-1.12 / (2 * 0.0259))
chk("n_i from NC,NV,Eg", ni_calc, 6.9e9, 0.03)
chk("sqrt(NC NV)", math.sqrt(2.8e19 * 1.04e19), 1.71e19)
# product independent of E_F: try three E_F positions in a 1.12 eV gap
for EF in (0.3, 0.56, 0.9):
    n_ = 2.8e19 * math.exp(-(1.12 - EF) / 0.0259)
    p_ = 1.04e19 * math.exp(-EF / 0.0259)
    chk(f"np at EF={EF} equals NC NV e^-Eg/kT", n_ * p_, 2.8e19 * 1.04e19 * math.exp(-1.12 / 0.0259), 1e-9)
# E_i offset
chk("E_i offset (meV)", 0.0259 / 2 * math.log(1.04 / 2.8) * 1000, -12.8, 0.02)
chk("E_i offset with Ioffe 3.2/1.8 (meV)", 0.0259 / 2 * math.log(1.8 / 3.2) * 1000, -7.5, 0.02)
# Doped E_F
chk("EF-Ei ND=1e16 ni=1e10", 0.0259 * math.log(1e6), 0.358)
chk("EF-Ei ND=1e16 ni=1.5e10", 0.0259 * math.log(1e16 / 1.5e10), 0.347)
chk("Ei-EF NA=1e17 ni=1e10", 0.0259 * math.log(1e7), 0.417)
chk("EF-Ei ND=1e15 ni=1.5e10", 0.0259 * math.log(1e15 / 1.5e10), 0.288)
chk("n from EF-Ei=0.3, ni=1.5e10", 1.5e10 * math.exp(0.3 / 0.0259), 1.6e15, 0.03)
chk("Ec-Ei with ni=1e10 (meV)", 0.0259 * math.log(2.8e19 / 1e10) * 1000, 562)

chk("Ge/Si n_i ratio", 2.4e13 / 1.5e10, 1600)
chk("Si/GaAs n_i ratio", 1.5e10 / 1.8e6, 8333, 0.01)
chk("e^(-0.30/0.0518)", math.exp(-0.30 / 0.0518), 1 / 327, 0.02)
chk("atoms per N_C seat", 5e22 / 2.8e19, 1786, 0.01)
chk("f at 5kT exact", f(5 * 0.0259), 0.00669, 0.005)
chk("e^-5", math.exp(-5), 0.00674, 0.005)
chk("f at +1kT", f(0.0259), 0.269)
chk("ln(1e6)*kT", 0.0259 * 13.8, 0.357, 0.01)
chk("E_F per decade of doping", 0.0259 * math.log(10), 0.06, 0.01)
chk("n for Ec-EF=0.206", 2.8e19 * math.exp(-0.206 / 0.0259), 1e16, 0.02)
chk("half-gap check 0.358+0.206", 0.358 + 0.206, 0.564, 0.001)

if fails:
    print("\nFAILED:", fails)
    sys.exit(1)
print("\nall checks pass")
