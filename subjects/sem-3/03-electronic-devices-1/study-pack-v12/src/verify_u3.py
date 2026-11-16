"""Recompute every number printed in 03a-pn-junction-equilibrium and 03b-diode-iv-capacitance.

Run: python verify_u3.py   (exits non-zero on any mismatch)
Each check computes the value from the formula and compares it with the value the pack prints.
Where an independent route exists (e.g. V_bi from the hole ratio and from ½·E_max·W), both are computed.
"""
import math
import sys

q, eps0 = 1.6e-19, 8.854e-14            # C, F/cm (the values the pack prints)
eps = 1.04e-12                           # Si, F/cm, as printed (11.7 eps0 = 1.036e-12)
VT = 0.0259
ni = 1e10                                # the deck's value (02a step 6)
fails = []


def chk(name, got, printed, rel=0.02):
    ok = abs(got - printed) <= rel * abs(printed)
    print(f"{'ok ' if ok else 'BAD'} {name}: computed {got:.4g}, printed {printed:.4g}")
    if not ok:
        fails.append(name)


def W_of(NA, ND, V):                     # cm, V = V_bi - V_a
    return math.sqrt(2 * eps / q * (1 / NA + 1 / ND) * V)


# ================= 03a =================
NA, ND = 1e17, 1e16                      # running example: p side 1e17, n side 1e16
chk("eps_Si F/cm", eps, 1.04e-12, 0.01)
# step 4: carriers on each side
chk("n on p side = ni^2/NA", ni**2 / NA, 1e3)
chk("p on n side = ni^2/ND", ni**2 / ND, 1e4)
chk("hole ratio across junction", NA / (ni**2 / ND), 1e13)
chk("electron ratio across junction", ND / (ni**2 / NA), 1e13)
# step 7: E_F positions (01b step 10)
chk("E_F - E_V on p side (eV), NV=1.04e19", VT * math.log(1.04e19 / NA), 0.120, 0.03)
chk("E_C - E_F on n side (eV), NC=2.8e19", VT * math.log(2.8e19 / ND), 0.206, 0.02)
# step 8: V_bi
Vbi = VT * math.log(NA * ND / ni**2)
chk("ln(1e33/1e20)", math.log(1e13), 29.93, 0.001)
chk("V_bi running example", Vbi, 0.775, 0.002)
chk("V_bi from E_F positions: Eg - 0.120 - 0.206 with Eg=1.12, NC/NV route",
    1.12 - VT * math.log(1.04e19 / NA) - VT * math.log(2.8e19 / ND), 0.79, 0.03)
chk("V_bi NA=ND=1e16", VT * math.log(1e32 / 1e20), 0.716)
chk("V_bi NA=1e18 ND=1e15", VT * math.log(1e33 / 1e20), 0.775, 0.002)
chk("V_bi NA=ND=1e18", VT * math.log(1e36 / 1e20), 0.954)
chk("V_bi Check: NA=1e18 ND=1e16", VT * math.log(1e34 / 1e20), 0.835)
# step 9: charge balance
W0 = W_of(NA, ND, Vbi)
xn = W0 * NA / (NA + ND)
xp = W0 * ND / (NA + ND)
chk("x_n/x_p = NA/ND", xn / xp, 10)
# step 10: field
Emax_n = q * ND * xn / eps
Emax_p = q * NA * xp / eps
chk("E_max from n side == from p side", Emax_n, Emax_p, 1e-9)
chk("E_max running example (V/cm)", Emax_n, 4.66e4, 0.02)
# step 11: W
chk("2eps/q (cm/V)", 2 * eps / q, 1.30e7, 0.005)
chk("W0 running example (um)", W0 * 1e4, 0.333, 0.01)
chk("x_n (um)", xn * 1e4, 0.303, 0.01)
chk("x_p (um)", xp * 1e4, 0.0303, 0.01)
chk("V_bi = 1/2 Emax W (independent route)", 0.5 * Emax_n * W0, Vbi, 0.002)
chk("V on n side share = xn/W", 0.5 * Emax_n * xn / Vbi, 0.909, 0.01)
chk("W for NA=ND=1e16 (um)", W_of(1e16, 1e16, 0.716) * 1e4, 0.431, 0.01)
chk("p+n one-sided W, NA=1e18 ND=1e16 (um)", W_of(1e18, 1e16, VT * math.log(1e34 / 1e20)) * 1e4, 0.331, 0.01)
chk("one-sided approx (ignore 1/NA)", math.sqrt(2 * eps / q / 1e16 * VT * math.log(1e34 / 1e20)) * 1e4, 0.329, 0.01)
# step 12: bias (deck slides 77-78)
chk("W1/W0 forward 0.6 V, Vbi 0.85", math.sqrt(0.25 / 0.85), 0.54, 0.01)
chk("W1/W0 reverse 2 V, Vbi 0.85", math.sqrt(2.85 / 0.85), 1.83, 0.01)
chk("running example W at +0.5 V (um)", W_of(NA, ND, Vbi - 0.5) * 1e4, 0.198, 0.01)
chk("running example W at -5 V (um)", W_of(NA, ND, Vbi + 5) * 1e4, 0.909, 0.01)
chk("ratio 5 V reverse", math.sqrt((Vbi + 5) / Vbi), 2.73, 0.01)
chk("Check 12 (a): Vbi 0.7, forward 0.4 ratio", math.sqrt(0.3 / 0.7), 0.655, 0.01)
chk("Check 12 (b): Vbi 0.7, reverse 6.3 ratio", math.sqrt(7.0 / 0.7), 3.16, 0.01)

# ================= 03b =================
Is = 1e-12
def I(V, n=1, Is=Is, VT=VT):
    return Is * (math.exp(V / (n * VT)) - 1)

# step 1 / 3: deck slide 75 curve and the practice question
chk("I at 0.6 V, Is=1pA (mA)", I(0.6) * 1e3, 11.5, 0.02)
chk("factor for +60 mV", math.exp(0.06 / VT), 10.1, 0.01)
chk("I at 0.66 V (mA)", I(0.66) * 1e3, 116, 0.02)
chk("I at 0.5 V (mA)", I(0.5) * 1e3, 0.243, 0.02)
chk("I at 0.4 V (uA)", I(0.4) * 1e6, 5.13, 0.02)
chk("I at 0.6 V, eta=2 (uA)", I(0.6, 2) * 1e6, 0.107, 0.02)
chk("V_T at 300 K = T/11600 (mV)", 300 / 11600 * 1e3, 25.9, 0.002)
chk("V_T = kT/q at 300 K (mV)", 1.381e-23 * 300 / q * 1e3, 25.9, 0.002)
chk("V_T at 27 C (mV)", 300.15 / 11600 * 1e3, 25.9, 0.002)
chk("V_T at 100 C (mV)", 373 / 11600 * 1e3, 32.2, 0.01)
# step 4: decades and the reverse side
chk("mV per decade = VT ln10", VT * math.log(10) * 1e3, 59.6, 0.005)
chk("mV per decade eta=2", 2 * VT * math.log(10) * 1e3, 119, 0.01)
chk("reverse -0.1 V: I/Is", I(-0.1) / Is, -0.979, 0.002)
chk("reverse -0.05 V: I/Is", I(-0.05) / Is, -0.855, 0.005)
chk("forward 0.1 V: exp", math.exp(0.1 / VT), 47.5, 0.01)
chk("V for 1 mA, Is=1pA (V)", VT * math.log(1e-3 / Is + 1), 0.537, 0.003)
chk("V for 10 mA (V)", VT * math.log(1e-2 / Is + 1), 0.596, 0.003)
# step 5: I_s scales with ni^2
ni_Ge, ni_Si = 2.4e13, 1e10
chk("(ni_Ge/ni_Si)^2", (ni_Ge / ni_Si) ** 2, 5.8e6, 0.01)
# step 6: temperature
chk("Is 10 nA 25->55 C (nA)", 10 * 2 ** ((55 - 25) / 10), 80)
chk("Is 5 nA 25->45 C (nA)", 5 * 2 ** ((45 - 25) / 10), 20)
chk("Is 1 pA 25->125 C", 1e-12 * 2 ** 10, 1.02e-9, 0.01)
chk("V_D 0.7 V at 25 C -> 75 C (V)", 0.7 - 0.002 * 50, 0.60)
chk("V_D 0.65 V at 25 C -> -15 C (V)", 0.65 - 0.002 * (-40), 0.73)
# step 7-8: resistances
chk("R_D 0.7 V / 2 mA (ohm)", 0.7 / 2e-3, 350)
chk("r_d 26 mV / 2 mA", 0.026 / 2e-3, 13)
chk("r_d at 0.5 mA", 0.026 / 0.5e-3, 52)
chk("r_d at 5 mA", 0.026 / 5e-3, 5.2)
chk("r_d at 10 mA", 0.026 / 10e-3, 2.6)
chk("R_D at 0.6 V, 11.5 mA", 0.6 / I(0.6), 52.2, 0.02)
chk("r_d at 0.6 V from 25.9 mV", VT / I(0.6), 2.25, 0.02)
# numerical slope check of r_d
dV = 1e-6
chk("r_d numeric slope at 0.6 V", dV / (I(0.6 + dV) - I(0.6)), VT / I(0.6), 0.001)
chk("R_D reverse -5 V with Is 1 pA (ohm)", 5 / 1e-12, 5e12, 0.001)
chk("r_d eta=2 at 2 mA", 2 * 0.026 / 2e-3, 26)
# step 9: equivalent circuits, 5 V source, 1 kohm
chk("ideal I (mA)", 5 / 1000 * 1e3, 5.0)
chk("simplified I (mA)", (5 - 0.7) / 1000 * 1e3, 4.3)
chk("r_av from (0.7,0) to (0.8,10 mA)", 0.1 / 10e-3, 10)
chk("PWL I (mA)", (5 - 0.7) / 1010 * 1e3, 4.26, 0.005)
chk("PWL V_D", 0.7 + 4.257e-3 * 10, 0.743, 0.005)
# exact: solve 5 = 1000 I + VT ln(I/Is) with Is chosen so the curve passes 0.7 V at 2 mA? use Is = 1 pA
Ix = 4e-3
for _ in range(60):
    Ix = (5 - VT * math.log(Ix / Is + 1)) / 1000
chk("exact exponential I, Is=1pA (mA)", Ix * 1e3, 4.43, 0.005)
chk("exact V_D (V)", VT * math.log(Ix / Is + 1), 0.575, 0.005)
chk("Check 9: 12 V, 2.2k simplified (mA)", (12 - 0.7) / 2200 * 1e3, 5.14, 0.005)
chk("Check 9: 12 V, 2.2k ideal (mA)", 12 / 2200 * 1e3, 5.45, 0.005)
chk("Check 9: 2 V, 1k, simplified vs ideal % error", (2 / 1000 - 1.3 / 1000) / (1.3 / 1000) * 100, 54, 0.01)
# step 10: C_T
A = (100e-4) ** 2                         # 100 um x 100 um in cm^2
chk("A = 1e-4 cm^2", A, 1e-4)
CT0 = eps * A / W0
chk("C_T at 0 V (pF)", CT0 * 1e12, 3.12, 0.005)
CT5 = eps * A / W_of(NA, ND, Vbi + 5)
chk("C_T at 5 V reverse (pF)", CT5 * 1e12, 1.14, 0.01)
chk("C_T ratio 5 V", CT5 / CT0, 0.366, 0.01)
chk("C_T at 20 V reverse (pF)", eps * A / W_of(NA, ND, Vbi + 20) * 1e12, 0.60, 0.02)
chk("C_T 4x down needs (Vbi+VR)=16 Vbi -> VR (V)", 15 * Vbi, 11.6, 0.01)
chk("Check 10 (a): 2 pF at 1 V rev, Vbi 0.7 -> at 9.5 V", 2 * math.sqrt(1.7 / 10.2), 0.816, 0.01)
# numerical dQ/dV check: Q = q ND x_n A ; x_n = W NA/(NA+ND)
def Q(VR):
    return q * ND * W_of(NA, ND, Vbi + VR) * NA / (NA + ND) * A
chk("C_T by dQ/dV at 5 V (pF)", (Q(5.001) - Q(5.0)) / 0.001 * 1e12, CT5 * 1e12, 0.002)
chk("Q at 0 V (pC)", Q(0) * 1e12, 4.84, 0.01)
# step 11: C_D
chk("C_D tau 1us, 1 mA, eta 1 (nF)", 1e-6 * 1e-3 / VT * 1e9, 38.6, 0.01)
chk("C_D tau 1us, 1 mA, eta 2 (nF)", 1e-6 * 1e-3 / (2 * VT) * 1e9, 19.3, 0.01)
chk("C_D / C_T(0)", 38.6e-9 / CT0, 1.24e4, 0.01)
chk("stored charge Q = tau I (nC)", 1e-6 * 1e-3 * 1e9, 1.0)
chk("Check 11 (a): tau 20 ns, 10 mA (nF)", 20e-9 * 10e-3 / VT * 1e9, 7.72, 0.01)
chk("Check 11 (b) doubling I doubles C_D", 2 * 38.6, 77.2)
# step 12: reverse recovery, charge-control t_s = tau ln(1 + IF/IR)
chk("I_F = 10 V / 1k (mA)", 10 / 1000 * 1e3, 10)
chk("I_R = 5 V / 1k (mA)", 5 / 1000 * 1e3, 5)
chk("t_s tau=100ns IF=10 IR=5 (ns)", 100 * math.log(1 + 10 / 5), 110, 0.01)
chk("t_s IR=10 (ns)", 100 * math.log(1 + 10 / 10), 69.3, 0.01)
chk("t_s IR=20 (ns)", 100 * math.log(1 + 10 / 20), 40.5, 0.01)
chk("t_rr = t_s + t_t, 110 + 30", 110 + 30, 140)
chk("max f ~ 1/(10 t_rr) for 140 ns (MHz)", 1 / (10 * 140e-9) / 1e6, 0.714, 0.01)

# self-tests (03a)
chk("ST 03a-1: Vbi NA=1e16 ND=1e17", VT * math.log(1e33 / 1e20), 0.775, 0.002)
chk("ST 03a-2: x_n/x_p NA=1e18 ND=1e15", 1e18 / 1e15, 1000)
chk("ST 03a-3: W NA=ND=1e17, Vbi (um)", W_of(1e17, 1e17, VT * math.log(1e34 / 1e20)) * 1e4, 0.147, 0.01)
chk("ST 03a-3: Vbi NA=ND=1e17", VT * math.log(1e34 / 1e20), 0.835)
chk("ST 03a-4: Vbi 0.8, reverse 7.2 ratio", math.sqrt(8.0 / 0.8), 3.16, 0.01)
# self-tests (03b)
chk("ST 03b-1: I at 0.65 V (mA)", I(0.65) * 1e3, 79.6, 0.02)
chk("ST 03b-2: V for 5 mA Is=1pA", VT * math.log(5e-3 / Is), 0.578, 0.003)
chk("ST 03b-3: r_d at 1 mA", 0.026 / 1e-3, 26)
chk("ST 03b-4: Is 2 nA 20->60 C", 2 * 2 ** 4, 32)
chk("ST 03b-5: C_T 10 pF at 0 V, Vbi 0.75, 8.25 V rev", 10 * math.sqrt(0.75 / 9.0), 2.89, 0.01)
chk("ST 03b-6: C_D tau 5 us, 2 mA, eta 2 (nF)", 5e-6 * 2e-3 / (2 * VT) * 1e9, 193, 0.01)
chk("ST 03b-7: PWL 10 V, 470 ohm, r_av 5 (mA)", (10 - 0.7) / 475 * 1e3, 19.6, 0.01)

# extra printed values (03a checks, 03b prose)
chk("03a Ch8(b): VT ln 100", VT * math.log(100), 0.119, 0.01)
chk("03a Ch4(a): n on p side NA=1e16", ni**2 / 1e16, 1e4)
chk("03a Ch4(a): p on n side ND=1e18", ni**2 / 1e18, 1e2)
chk("03a ST5: n-side share for NA=4ND", 4 / 5, 0.8)
chk("03a Ch10(c): Emax from p side (V/cm)", q * 1e17 * 3.03e-6 / eps, 4.66e4, 0.01)
chk("03b: C_D/C_T about 12000", 38.6e-9 / 3.12e-12, 12000, 0.04)
chk("03b Ch7(a): 0.65 V / 5 mA", 0.65 / 5e-3, 130)
chk("03b step 4: two decades in V", 2 * VT * math.log(10), 0.12, 0.01)
chk("03b step 9: ideal vs exact within 15 %", (5.0 - 4.43) / 4.43, 0.13, 0.05)
chk("03b Ch3(b) check 0.243 mA", I(0.5) * 1e3, 0.243, 0.01)
chk("03b Ch2(a)", math.exp(0.1 / VT), 47.5, 0.01)

print()
if fails:
    print(f"{len(fails)} FAILED:", *fails, sep="\n  ")
    sys.exit(1)
print("all checks pass")
