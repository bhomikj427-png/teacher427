"""Check every number in 04b-ac-in-15-minutes.md (phasor algebra + a time simulation of the worked example)."""
import cmath, math
import numpy as np
from scipy.integrate import solve_ivp

def pol(z): return f"{abs(z):.4g} ∠ {math.degrees(cmath.phase(z)):.2f}°"

print("3+j4 =", pol(3+4j), "| -3+j4 =", pol(-3+4j), "| 5-j5 =", pol(5-5j))
print("10∠30° =", cmath.rect(10, math.radians(30)))
print("(2∠30)(3∠20) =", pol(cmath.rect(2, math.radians(30))*cmath.rect(3, math.radians(20))))
print("10∠0 / 5∠-90 =", pol(10/cmath.rect(5, math.radians(-90))), " 1/j =", 1/1j)
w = 1000
ZL, ZC = 1j*w*1, 1/(1j*w*1e-6)
print("ZL =", ZL, " ZC =", ZC)
Z = 1000+ZL; I = 10/Z
print("RL: Z =", pol(Z), " I(mA) =", pol(I*1e3), " VR =", pol(I*1000), " VL =", pol(I*ZL), " VR+VL =", I*1000+I*ZL)
Z2 = 1000+ZC; I2 = 10/Z2
print("RC: Z =", pol(Z2), " I(mA) =", pol(I2*1e3))
# self-test
print("ST2 6-j8 =", pol(6-8j))
print("ST3 ZL(0.2H,500) =", 1j*500*0.2, " ZC(10uF,500) =", 1/(1j*500*10e-6))
Z3 = 100+1j*500*0.2; print("ST4 Z =", pol(Z3), " I(mA) =", pol(10/Z3*1e3))
print("ST5 rms of 5 mA peak =", 5/math.sqrt(2))
# time simulation of RL example: L di/dt = 10cos(1000t) - R i
sol = solve_ivp(lambda t, i: [(10*np.cos(w*t) - 1000*i[0])/1.0], [0, 0.02], [0], max_step=1e-6, dense_output=True)
t = np.linspace(0.015, 0.02, 5000); i = sol.sol(t)[0]
k = np.argmax(i); print("sim: peak i = %.4f mA at phase %.1f° (expect 7.071 mA, -45°)" % (i[k]*1e3, math.degrees((w*t[k]) % (2*math.pi)) - 360 if math.degrees((w*t[k]) % (2*math.pi))>180 else math.degrees((w*t[k]) % (2*math.pi))))
