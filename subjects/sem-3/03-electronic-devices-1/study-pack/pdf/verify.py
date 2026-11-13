"""Re-derives every number printed in EDC-ETE-v1.pdf. Run: python verify.py  (exit 0 = all pass).

Each check recomputes a worked answer from first principles (and, where a closed form is quoted,
confirms it against an independent numerical solution). ok(label, value, printed, tol) compares
with the value printed in the PDF.
"""
import cmath
import math

import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad

q, k = 1.602e-19, 1.381e-23
VT = k * 300 / q          # 25.86 mV at 300 K
N = [0]


def ok(label, value, printed, tol=0.006):
    N[0] += 1
    rel = abs(value - printed) / (abs(printed) if printed else 1)
    assert rel <= tol, f"FAIL {label}: computed {value:.6g}, printed {printed}"
    print(f"ok  {label:58s} {value:.5g}  (printed {printed})")


# ---------------- Part A: semiconductor physics
ok("VT at 300 K (mV)", VT * 1e3, 25.9)
ni = 1e10
ok("A2 minority holes, Nd=1e16", ni**2 / 1e16, 1e4)
ok("A2 with ni=1.5e10", 1.5e10**2 / 1e16, 2.25e4)
ok("A3 EF-Ei (eV), Nd=1e16", VT * math.log(1e16 / ni), 0.357)
ok("A3 f(EF + 0.1 eV)", 1 / (1 + math.exp(0.1 / VT)), 0.0205, 0.01)
sig_i = q * ni * (1500 + 450)
ok("A4 deck: intrinsic sigma (S/cm)", sig_i, 3.12e-6)
ok("A4 deck: intrinsic rho (ohm cm)", 1 / sig_i, 3.2e5)
ok("A4 doped/intrinsic sigma ratio", 32 / sig_i, 1.0e7, 0.03)
sig = q * 1e16 * 1350
ok("A4 check sigma n-type (S/cm)", sig, 2.16)
ok("A4 check rho (ohm cm)", 1 / sig, 0.462)
ok("A4 sheet resistance (ohm/sq), t=1um", (1 / sig) / 1e-4, 4620)
ok("A4 resistor L/W=10 (kohm)", (1 / sig) / 1e-4 * 10 / 1e3, 46.2)
ok("A4 drift velocity (cm/s), E=100 V/cm", 1350 * 100, 1.35e5)
Dn = VT * 1350
ok("A5 Dn (cm2/s)", Dn, 34.9)
ok("A5 Dp (cm2/s), mu_p=480", VT * 480, 12.4)
ok("A5 diffusion J (A/cm2)", q * Dn * 1e18, 5.59)

# ---------------- Part B: pn junction and diodes
ok("B1 Vbi (V)", VT * math.log(1e17 * 1e16 / ni**2), 0.774)
ok("B1 deck: W1/W0 forward 0.6 V", math.sqrt((0.85 - 0.6) / 0.85), 0.54, 0.01)
ok("B1 deck: W2/W0 reverse 2 V", math.sqrt((0.85 + 2) / 0.85), 1.83)
ok("B2 ID (mA), Is=1pA, 0.6 V", 1e-12 * (math.exp(0.6 / VT) - 1) * 1e3, 12.0, 0.02)
ok("B2 ID at 0.66 V / ID at 0.60 V", math.exp(0.06 / VT), 10.2, 0.01)
ok("B2 Is at 55 C from 10 nA at 25 C (nA)", 10 * 2 ** 3, 80)
ok("B3 rd (ohm) at 2 mA", 26 / 2, 13)
ok("B3 RD (ohm) 0.7 V / 2 mA", 0.7 / 2e-3, 350)
# B4 load line, deck L08 S4: E = 10 V, R = 0.5 k
ok("B4 load line: ID intercept (mA)", 10 / 0.5, 20)
ok("B4 load line: VR = E - VDQ (V)", 10 - 0.78, 9.22)
ok("B4 load line: VR = IDQ*R (V)", 18.5 * 0.5, 9.25)
ok("B4 S9: ID (mA)", (8 - 0.7) / 2.2, 3.32)
ok("B4 S12: Vo (V)", 12 - 0.7 - 1.8, 9.5)
ok("B4 S12: ID (mA)", 9.5 / 0.68, 13.97)
I = (10 + 5 - 0.7) / (4.7 + 2.2)
ok("B4 S14: I (mA)", I, 2.07)
ok("B4 S14: V1 (V)", I * 4.7, 9.74)
ok("B4 S14: V2 (V)", I * 2.2, 4.56)
ok("B4 S14: Vo (V)", I * 2.2 - 5, -0.44, 0.02)
ok("B4 S15: I1 (mA)", (10 - 0.7) / 0.33, 28.18)
ok("B4 S15: each diode (mA)", (10 - 0.7) / 0.33 / 2, 14.09)
ok("B4 S18: I1 (mA)", 0.7 / 3.3, 0.212)
ok("B4 S18: I2 (mA)", (20 - 0.7 - 0.7) / 5.6, 3.32)
ok("B4 S18: ID2 (mA)", (20 - 1.4) / 5.6 - 0.7 / 3.3, 3.11)
# B5 rectifiers: averages by numerical integration
hw = quad(lambda t: max(math.sin(t), 0), 0, 2 * math.pi, points=[math.pi])[0] / (2 * math.pi)
fw = quad(lambda t: abs(math.sin(t)), 0, 2 * math.pi, points=[math.pi])[0] / (2 * math.pi)
ok("B5 half-wave Vdc/Vm", hw, 0.318)
ok("B5 full-wave Vdc/Vm", fw, 0.636)
rms_hw = math.sqrt(quad(lambda t: max(math.sin(t), 0) ** 2, 0, 2 * math.pi, points=[math.pi])[0] / (2 * math.pi))
rms_fw = math.sqrt(quad(lambda t: math.sin(t) ** 2, 0, 2 * math.pi)[0] / (2 * math.pi))
ok("B5 half-wave Vrms/Vm", rms_hw, 0.5)
ok("B5 full-wave Vrms/Vm", rms_fw, 0.707)
ok("B5 ripple factor HW", math.sqrt((rms_hw / hw) ** 2 - 1), 1.21)
ok("B5 ripple factor FW", math.sqrt((rms_fw / fw) ** 2 - 1), 0.482, 0.01)
ok("B5 efficiency HW (%)", (hw / rms_hw) ** 2 * 100, 40.6, 0.01)
ok("B5 efficiency FW (%)", (fw / rms_fw) ** 2 * 100, 81.2, 0.01)
ok("B5 deck: HW ideal Vdc (V), Vm=20", -0.318 * 20, -6.36)
ok("B5 deck: HW Si Vdc (V)", -0.318 * (20 - 0.7), -6.14)
ok("B5 deck: bridge with 2 resistors, peak (V)", 10 / 2, 5)
ok("B5 deck: bridge with 2 resistors, Vdc (V)", 0.636 * 5, 3.18)
ok("B5 check: 12 V rms peak", 12 * math.sqrt(2), 17.0, 0.01)
ok("B5 check: bridge Si, Vm=17 -> Vdc", 0.636 * (17 - 1.4), 9.92)
# B6 / B7
ok("B6 series clipper peak (V)", 20 + 5, 25)
ok("B6 parallel clipper Si level (V)", 4 - 0.7, 3.3)
ok("B7 clamper VC (V)", 20 + 5, 25)
ok("B7 clamper upper level (V)", 10 + 25, 35)
ok("B7 tau (ms)", 100e3 * 0.1e-6 * 1e3, 10)
ok("B7 5 tau / (T/2)", 5 * 10 / 0.5, 100)
# B8 zener regulator
ok("B8 open-zener VL, RL=1.2k (V)", 16 * 1.2 / 2.2, 8.73)
ok("B8 open-zener V, RL=3k (V)", 16 * 3 / 4, 12)
ok("B8 IR (mA)", (16 - 10) / 1, 6)
ok("B8 IL (mA)", 10 / 3, 3.33)
ok("B8 IZ (mA)", 6 - 10 / 3, 2.67)
ok("B8 PZ (mW)", 10 * (6 - 10 / 3), 26.7)
ok("B8 RL(min) (ohm)", 1000 * 10 / (16 - 10), 1667)
ok("B3 check: rd at 0.5 mA (ohm)", 26 / 0.5, 52)
ok("B6 check: reversed battery peak (V)", 20 - 5, 15)
ok("B7 check: no battery upper level (V)", 10 + 20, 30)
ok("B8 check: IZ at Vi = 20 V (mA)", (20 - 10) / 1 - 10 / 3, 6.67)
ok("B9 check: wavelength (nm), Eg = 1.9 eV", 6.626e-34 * 2.998e8 / (1.9 * q) * 1e9, 653)
ok("A6 check: fraction left after 3 tau", math.exp(-3), 0.05, 0.01)

# ---------------- Part C: JFET (professor's numericals sheet)
shock = lambda idss, vgs, vp: idss * (1 - vgs / vp) ** 2
ok("C2 sheet Q2: ID (mA)", shock(32, -4.5, -8), 6.12, 0.01)
ok("C2 sheet Q3: VGS (V)", -6 * (1 - math.sqrt(5 / 10)), -1.76)
ok("C2 sheet Q5: ID (mA)", shock(3, -2, -6), 1.33)
ok("C2 sheet Q4: VDD min (V)", 4 + 12e-3 * 560, 10.72)
ok("C3 sheet Q7: gm (uS)", 0.3e-3 / 0.1 * 1e6, 3000)
ok("C3 sheet Q8: gm (uS)", 4000 * (1 - 3 / 8), 2500)
ok("C3 gm0 = 2 IDSS/|VP| (mS), 8 mA, 4 V", 2 * 8 / 4, 4)
ok("C3 mu = gm rd", 2e-3 * 50e3, 100)
d = (shock(8, -2 + 1e-6, -4) - shock(8, -2 - 1e-6, -4)) / 2e-6
ok("C3 gm at VGS=-2 by differentiation (mS)", d, 2.0)
ID = brentq(lambda i: shock(8, -i * 1.0, -4) - i, 0.01, 4)
ok("C4 self-bias ID (mA)", ID, 2.0)
ok("C4 self-bias VDS (V)", 20 - 2 * (3.3 + 1), 11.4)
ID17 = (12 - 7) / 3.3
ok("C4 sheet Q17: ID (mA)", ID17, 1.52, 0.01)
ok("C4 sheet Q17: VS (V)", ID17 * 1.8, 2.73)
ok("C4 sheet Q17: VG (V)", 12 * 1 / 7.8, 1.54)
ok("C4 sheet Q17: VGS (V)", 12 / 7.8 - ID17 * 1.8, -1.19, 0.01)
vgs18 = -5 * (1 - math.sqrt(2.5 / 10))
ok("C4 sheet Q18: VGS (V)", vgs18, -2.5)
ok("C4 sheet Q18: RS (kohm)", (30 * 500 / 1500 - vgs18) / 2.5, 5)
ok("C4 sheet Q19: ID max (mA)", 20 / 0.5, 40)
ok("C5 CS gain", -2e-3 * (2.2e3 * 50e3 / 52.2e3), -4.21)
ok("C5 CD gain", 2e-3 * 1e3 / (1 + 2e-3 * 1e3), 0.667)
ok("C5 CD Zo (ohm) = RS || 1/gm", 1 / (1 / 1e3 + 2e-3), 333)

# ---------------- Part D: MOSFET
K = 500 / (10 - 1) ** 2
ok("D2 sheet Q30: K (mA/V2)", K, 6.17)
ok("D2 sheet Q30: ID at 5 V (mA)", K * 16, 98.8)
ok("D2 sheet Q26: ID at -3 V (mA)", shock(10, -3, -8), 3.91)
ok("D2 sheet Q26: ID at +3 V (mA)", shock(10, 3, -8), 18.9)
ok("D2 sheet Q28: VDS (V)", 18 - 12 * 0.62, 10.56)
ok("D2 triode ID (mA)", 2 * ((3 - 1) * 1 - 0.5), 3)
ok("D2 sat ID (mA)", 0.5 * 2 * (3 - 1) ** 2, 4)
IDm = brentq(lambda i: 0.5 * (6 - i * 1 - 2) ** 2 - i, 0.1, 3.9)
ok("D3 divider bias ID (mA)", IDm, 2.0)
ok("D3 VGS (V)", 6 - IDm, 4.0)
ok("D3 VDS (V)", 20 - IDm * (3 + 1), 12)
ok("D3 drain-feedback (RD = 4k): ID (mA)", brentq(lambda i: 0.5 * (12 - 4 * i - 2) ** 2 - i, 0.1, 2.4), 2.0)
gm = 2 * 0.5 * (4 - 2)
ok("D4 gm (mS)", gm, 2)
ok("D4 gm = 2 sqrt(K ID)", 2 * math.sqrt(0.5 * 2), 2)
ok("D4 CS gain", -gm * 3, -6)
ok("D4 CG Rin (ohm)", 1e3 / gm, 500)
ok("D4 CD gain", gm * 1 / (1 + gm * 1), 0.667)
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            pd = a and (b or c)                    # nFET network: a in series with (b || c)
            pu = (not a) or ((not b) and (not c))  # pFET network: the dual
            assert bool(pd) != bool(pu), "complex gate: networks must be complementary"
N[0] += 1
print("ok  D5 f = (a(b+c))' pull-up and pull-down are complementary for all 8 inputs")

ok("D3 check: rejected root (mA)", (41 + 9) / 16, 3.125)
ok("D4 check: gm at 8 mA (mS)", 2 * math.sqrt(0.5 * 8), 4)
ok("D5 check: rDS(on) (ohm)", 1 / (2 * 0.5e-3 * 8), 125)
ok("D5 check: weak 1 (V)", 5 - 1, 4)

# ---------------- Part E: BJT
ok("E2 alpha from beta=100", 100 / 101, 0.990)
ok("E2 beta from alpha=0.98", 0.98 / 0.02, 49)
ok("E2 ICEO (uA), ICBO=20 nA, beta=100", 101 * 20e-3, 2.02)
IB = (12 - 0.7) / 240e3
ok("E3 deck fixed bias: IB (uA)", IB * 1e6, 47.08)
ok("E3 deck fixed bias: IC (mA)", 50 * IB * 1e3, 2.35)
ok("E3 deck fixed bias: VCE (V)", 12 - 50 * IB * 2.2e3, 6.82)
ok("E3 ICsat (mA)", 12 / 2.2, 5.45)
IB = (20 - 0.7) / (430e3 + 51 * 1e3)
ok("E4 deck emitter bias: IB (uA)", IB * 1e6, 40.1)
ok("E4 deck emitter bias: IC (mA)", 50 * IB * 1e3, 2.01)
ok("E4 deck emitter bias: VCE (V)", 20 - 50 * IB * 2e3 - 51 * IB * 1e3, 13.94)
ok("E4 ICsat (mA)", 20 / 3, 6.67)
S = lambda b, rb, re: (1 + b) * (1 + rb / re) / (1 + b + rb / re)
ok("E4 S fixed bias", 1 + 50, 51)
ok("E4 S emitter bias", S(50, 430, 1), 45.7)
Eth, Rth = 22 * 3.9 / 42.9, 39 * 3.9 / 42.9
IB = (Eth - 0.7) / (Rth * 1e3 + 101 * 1.5e3)
ok("E4 divider: ETh (V)", Eth, 2.0)
ok("E4 divider: RTh (kohm)", Rth, 3.55)
ok("E4 divider: IB (uA)", IB * 1e6, 8.38)
ok("E4 divider: IC (mA)", 100 * IB * 1e3, 0.84)
ok("E4 divider: VCE (V)", 22 - 100 * IB * 10e3 - 101 * IB * 1.5e3, 12.35)
ok("E4 divider approx: IC (mA)", (Eth - 0.7) / 1.5, 0.87)
ok("E4 S divider", S(100, Rth, 1.5), 3.29)


def ic(ico, b=50, vcc=20, rb=430e3, re=1e3):
    # IC = b IB + (1+b) ICO ; VCC = IB RB + VBE + (IC + IB) RE
    ib = (vcc - 0.7 - (1 + b) * ico * re) / (rb + (1 + b) * re)
    return b * ib + (1 + b) * ico


ok("E4 S emitter bias by numeric dIC/dICO", (ic(2e-9) - ic(1e-9)) / 1e-9, 45.7)
# E5 h-parameters, professor's sheet Problem 9
hie, hfe, hoe, hre, Rs, RL = 1100, 50, 25e-6, 2.5e-4, 800, 2000
Ai = -hfe / (1 + hoe * RL); Ri = hie + hre * Ai * RL; Av = Ai * RL / Ri
Yo = hoe - hfe * hre / (hie + Rs)
ok("E5 P9: Ai", Ai, -47.6)
ok("E5 P9: Ri (ohm)", Ri, 1076.2)
ok("E5 P9: Av", Av, -88.5)
ok("E5 P9: Avs", Av * Ri / (Ri + Rs), -50.75)
ok("E5 P9: Yo (uS)", Yo * 1e6, 18.42)
ok("E5 P9: Ro (kohm)", 1 / Yo / 1e3, 54.28)
ok("E5 P9: Rot (kohm)", 1 / (Yo + 1 / RL) / 1e3, 1.93)
ok("E5 P9: Ap", Ai * Av, 4214)
ok("E5 P9 approx: Av", -hfe * RL / hie, -90.9)
ok("E5 P9: % error in Ai", (50 - 47.62) / 47.62 * 100, 5.0, 0.01)
# independent check: set ib = 1 and solve the two h-parameter equations with vc = -ic RL
vc = -hfe * RL / (1 + hoe * RL); icv = hfe + hoe * vc; vb = hie + hre * vc
ok("E5 P9: Ai by direct solve", -icv, -47.6)
ok("E5 P9: Ri by direct solve", vb, 1076.2)
ok("E5 P9: Av by direct solve", vc / vb, -88.5)
ok("E6 two-stage gain (dB)", 20 * math.log10(40 * 60), 67.6)
ok("E6 Darlington beta exact", 100 * 100 + 100 + 100, 10200)

# ---------------- Part F: feedback
Af = lambda A, b: A / (1 + A * b)
ok("F1 deck: A=1000, beta=0.01", Af(1000, 0.01), 90.9)
ok("F1 deck: A=10000", Af(10000, 0.01), 99.0)
ok("F1 deck: A=20000", Af(20000, 0.01), 99.5)
ok("F1 A=5000 (deck prints 98.3)", Af(5000, 0.01), 98.04)
ok("F3 Af, A=1000, beta=0.1", Af(1000, 0.1), 9.90)
ok("F3 % change in Af for 10 % drop in A", (Af(1000, 0.1) - Af(900, 0.1)) / Af(1000, 0.1) * 100, 0.11, 0.02)
ok("F3 fH with feedback (MHz)", 20e3 * 101 / 1e6, 2.02)
ok("F3 fL with feedback (Hz)", 100 / 101, 0.99)
ok("F3 Zif series (kohm)", 2 * 101, 202)
ok("F3 Zof voltage (ohm)", 20e3 / 101, 198)
ok("F3 distortion 10 % -> (%)", 10 / 101, 0.099)
ok("F3 gain-bandwidth before (MHz)", 1000 * 20e3 / 1e6, 20)
ok("F3 gain-bandwidth after (MHz)", Af(1000, 0.1) * 20e3 * 101 / 1e6, 20)


# ---------------- Part G: oscillators
def ladder(w, R=1.0, C=1.0, n=3):
    """Vout/Vin of n cascaded sections (series C, shunt R), exact, with loading."""
    Zc = 1 / (1j * w * C)
    M = np.array([[1 + Zc / R, Zc], [1 / R, 1]], complex)
    T = np.linalg.matrix_power(M, n)
    return 1 / T[0, 0]


H = ladder(1 / math.sqrt(6))
ok("G2 RC ladder |beta| at w0", abs(H), 1 / 29)
ok("G2 RC ladder phase at w0 (deg)", abs(math.degrees(cmath.phase(H))), 180)
R = 1 / (2 * math.pi * 800 * 10e-9 * math.sqrt(6))
ok("G2 deck design: R (kohm)", R / 1e3, 8.12)
ok("G2 deck design: Rf = 29 x 8.2k (kohm)", 29 * 8.2, 238, 0.01)
ok("G2 f with 8.2k (Hz)", 1 / (2 * math.pi * 8.2e3 * 10e-9 * math.sqrt(6)), 792)


def wien(w, R=1.0, C=1.0):
    Zs = R + 1 / (1j * w * C); Zp = 1 / (1 / R + 1j * w * C)
    return Zp / (Zs + Zp)


ok("G3 Wien beta at w0", abs(wien(1.0)), 1 / 3)
assert abs(cmath.phase(wien(1.0))) < 1e-9; N[0] += 1
print("ok  G3 Wien network phase at w0 is 0 deg")
ok("G3 Wien f (kHz), 10k, 10 nF", 1 / (2 * math.pi * 10e3 * 10e-9) / 1e3, 1.59)
ok("G4 Hartley f (kHz)", 1 / (2 * math.pi * math.sqrt(2e-3 * 100e-12)) / 1e3, 356)
ok("G4 Colpitts Ceq (pF)", 200 * 200 / 400, 100)
ok("G4 Colpitts f (kHz)", 1 / (2 * math.pi * math.sqrt(1e-3 * 100e-12)) / 1e3, 503)
fs = 1 / (2 * math.pi * math.sqrt(1.0 * 0.01e-12))
ok("G5 crystal fs (MHz)", fs / 1e6, 1.592)
ok("G5 fp - fs (Hz)", fs * (math.sqrt(1 + 0.01 / 10) - 1), 795, 0.01)
ok("G5 Q = ws L / R, R = 1 kohm", 2 * math.pi * fs * 1.0 / 1e3, 10000)

print(f"\nAll {N[0]} checks passed.")
