"""Checks every number in content/04c-polar-vs-rectangular.md."""
import cmath, math

def P(m, deg): return cmath.rect(m, math.radians(deg))
def pol(z): return round(abs(z), 3), round(math.degrees(cmath.phase(z)), 2)

# anchor: Sadiku PP 10.5 partials (assignment B81)
i1, i2 = P(2.808, 81.84), P(3.370, 51.84)
print("I' rect", i1, "I'' rect", i2, "sum", i1 + i2, pol(i1 + i2))
assert abs(abs(i1 + i2) - 5.97) < 0.005
# 10 A divider of PP10.5: Z = j4 || 6
Z = (4j * 6) / (6 + 4j)
print("Z", Z, pol(Z), "I''", pol(10 * Z / ((8 - 2j) + Z)))
# 3,4 at 0/90/180
for a in (0, 90, 180): print(a, abs(3 + P(4, a)))
# multiply / divide demos
print("(3+j4)(1+j1)", (3 + 4j) * (1 + 1j), pol((3 + 4j) * (1 + 1j)))
print("10/(3+j4)", 10 / (3 + 4j), pol(10 / (3 + 4j)))
print("(3+j4)*2 at 30", pol((3 + 4j) * P(2, 30)))
print("j(3+j4)", 1j * (3 + 4j))
# self-test
print("ST1", (4 + 3j) + (4 - 3j), abs(4 + 3j))
print("ST2", P(2, 30) * P(3, 60))
z1, z2 = 4 + 3j, -5j
print("ST3", z1 * z2 / (z1 + z2), pol(z1 * z2 / (z1 + z2)), pol(z1 * z2), pol(z1 + z2))
print("check1", P(10, 30) + P(10, -30), pol(P(6, 0) / P(2, -90)), pol(8 - 6j))
