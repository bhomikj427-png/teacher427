"""Recompute every number in instructions-chat.md. Run: python verify_numbers.py
Each check prints the value used in the file; an assert fails loudly on any mismatch."""
from math import ceil, log2

def b(x, n=8):
    return format(x & ((1 << n) - 1), f"0{n}b")

def chk(label, got, want):
    assert got == want, f"{label}: got {got}, want {want}"
    print(f"ok  {label}: {got}")

# ---------- pipeline ----------
def speedup(n, k, tp, tn):
    return n * tn / ((k + n - 1) * tp)
chk("MTE Q3 / Mano 9-4 / Summer A5 S(100)", round(speedup(100, 6, 10, 50), 2), 4.76)
chk("ETE25 B6 S(100)", round(speedup(100, 4, 20, 80), 2), 3.88)
chk("ETE25 B6 Smax", 80 / 20, 4.0)
chk("A2 Q12 cycles 200 tasks k=6", 6 + 200 - 1, 205)
chk("Makeup A5 cycles 100 tasks k=7", 7 + 100 - 1, 106)
tp, tn = max(40, 45 + 5, 15), 40 + 45 + 15
chk("A2 Q13 tp", tp, 50); chk("A2 Q13 tn", tn, 100)
chk("A2 Q13 S(10)", round(speedup(10, 3, tp, tn), 2), 1.67)
chk("A2 Q13 S(100)", round(speedup(100, 3, tp, tn), 2), 1.96)
chk("A2 Q13 Smax", tn / tp, 2.0)

# ---------- cache ----------
chk("ETE25 A4 Mano avg (miss = 100+1000)", round(0.9 * 100 + 0.1 * 1100), 200)
chk("ETE25 A4 alt avg (parallel)", round(0.9 * 100 + 0.1 * 1000), 190)
for ways, sets, tag in [(1, 4096, 16), (2, 2048, 17), (4, 1024, 18), (4096, 1, 28)]:
    s = 4096 // ways
    t = 32 - int(log2(s)) - 4          # 4 = byte offset in a 16-byte block
    chk(f"ETE25 A5 {ways}-way sets", s, sets); chk(f"ETE25 A5 {ways}-way tag", t, tag)
    print(f"      total tag bits = {t * 4096}")

# ---------- sizes ----------
chk("ETE26 A3 opcode bits", 32 - 1 - 6 - 18, 7)
chk("ETE26 A4 bits for 30 uops", ceil(log2(30)), 5)
chk("128x8 chips for 2048 B", 2048 // 128, 16)
chk("1200 baud, 11 bits/char", 1200 // 11, 109)
chk("A3 Q8 RAM chips", 2048 // 256, 8); chk("A3 Q8 ROM chips", 4096 // 1024, 4)
chk("SPL Q15(i) PA", 0x1000 * 16 + 0x2000, 0x12000)
chk("SPL Q15(ii) EA", 0x5000 + 0x2000 + 0x3000, 0xA000)
chk("SPL Q15(ii) PA", 0x1000 * 16 + 0xA000, 0x1A000)
chk("A3 Q1 PA", 0x0200 * 16 + 0x1234, 0x3234)
chk("ETE25 B3 PA", 0x0200 * 16 + 0x1234, 0x3234)
chk("deck PA 2010:3535", 0x2010 * 16 + 0x3535, 0x23635)
chk("e in 'exercise'", "exercise".count("e"), 3)

# ---------- arithmetic ----------
def add(a, c, n):
    m = (1 << n) - 1
    s = (a & m) + (c & m)
    cin_sign = (((a & (m >> 1)) + (c & (m >> 1))) >> (n - 1)) & 1
    cout = s >> n
    return s & m, cin_sign, cout
r, ci, co = add(-35, -40, 7)
chk("ETE25 B2 -35 (7b)", b(-35, 7), "1011101"); chk("ETE25 B2 -40 (7b)", b(-40, 7), "1011000")
chk("ETE25 B2 sum", b(r, 7), "0110101"); chk("ETE25 B2 carries in/out", (ci, co), (0, 1))
r, ci, co = add(64, 84, 8)
chk("A1 Q9 sum", b(r), "10010100"); chk("A1 Q9 carries", (ci, co), (1, 0))
chk("A1 Q8 -64 1s", b(~64), "10111111"); chk("A1 Q8 -64 2s", b(-64), "11000000")
# A1 Q16 adder-subtractor
chk("A1 Q16 i", (b(0b0111 + 0b0110, 4), (0b0111 + 0b0110) >> 4), ("1101", 0))
s = 0b0101 + (~0b1010 & 0xF) + 1
chk("A1 Q16 ii", (b(s, 4), s >> 4), ("1011", 0))
# A1 Q18 / Mano 4-19
R1, R2, R3, R4 = 0b11110010, 0b11111111, 0b10111001, 0b11101010
R1 = (R1 + R2) & 0xFF
R3, R2 = R3 & R4, (R2 + 1) & 0xFF
R1 = (R1 - R3) & 0xFF
chk("A1 Q18", (b(R1), b(R2), b(R3), b(R4)), ("01001001", "00000000", "10101000", "11101010"))
# decrementer example
chk("ETE25 B1 0110-1", b(0b0110 + 0b1111, 4), "0101")

# ---------- logic / shifts ----------
chk("ETE26 A2 B", b(0b11011001 ^ 0b01101101), "10110100")
chk("Mano 4-18b OR operand", b(0b11011001 | 0b00100100), "11111101")
def shr(x): return x >> 1
def shl(x): return (x << 1) & 0xFF
def cir(x): return (x >> 1) | ((x & 1) << 7)
def cil(x): return ((x << 1) & 0xFF) | (x >> 7)
def seq(x, ops):
    out = []
    for f in ops:
        x = f(x); out.append(b(x))
    return out
chk("A1 Q19 from 11111111", seq(0xFF, [shr, cir, shl, cil]),
    ["01111111", "10111111", "01111110", "11111100"])
chk("Summer B1 order from 11011101", seq(0b11011101, [shr, cir, shl, cil]),
    ["01101110", "00110111", "01101110", "11011100"])
chk("Mano 4-21 from 11011101", seq(0b11011101, [shl, cir, shr, cil]),
    ["10111010", "01011101", "00101110", "01011100"])
x = 0b10011100
chk("Mano 4-20 ashr", b((x >> 1) | (x & 0x80)), "11001110")
chk("Mano 4-20 ashl", b(shl(x)), "00111000")

# ---------- basic computer (Mano 5-9, 5-12) ----------
AC, E = 0xA937, 1
def cir16(ac, e): return ((e << 15) | (ac >> 1)), ac & 1
def cil16(ac, e): return (((ac << 1) & 0xFFFF) | e), ac >> 15
chk("CMA", hex(~AC & 0xFFFF), "0x56c8")
chk("CIR", tuple(map(hex, cir16(AC, E))), ("0xd49b", "0x1"))
chk("CIL", tuple(map(hex, cil16(AC, E))), ("0x526f", "0x1"))
chk("INC", hex(AC + 1), "0xa938")
s = 0x7EC3 + 0x8B9F
chk("Mano 5-12 AC,E", (hex(s & 0xFFFF), s >> 16), ("0xa62", 1))
chk("Mano 5-6 a", hex(0b0001000000100100), "0x1024")
chk("Mano 5-6 b", hex(0b1011000100100100), "0xb124")
chk("Mano 5-6 c", hex(0b0111000000100000), "0x7020")

# ---------- memory maps ----------
def block(base, size): return f"{base:05X}-{base + size - 1:05X}"
chk("16K EPROM pair", block(0x100000 - 0x8000, 0x8000), "F8000-FFFFF")
chk("32K RAM pair", block(0, 0x10000), "00000-0FFFF")
chk("8K EPROM pair", block(0x100000 - 0x4000, 0x4000), "FC000-FFFFF")
chk("8K RAM pair", block(0, 0x4000), "00000-03FFF")
chk("4K EPROM pair", block(0x100000 - 0x2000, 0x2000), "FE000-FFFFF")
chk("4K RAM pair", block(0, 0x2000), "00000-01FFF")
chk("deck 4K RAM (A13=0)", block(0xFC000, 0x2000), "FC000-FDFFF")
def block4(base, size): return f"{base:04X}-{base + size - 1:04X}"
chk("A3 Q8 RAM", block4(0x0000, 2048), "0000-07FF")
chk("A3 Q8 ROM", block4(0x1000, 4096), "1000-1FFF")
chk("A3 Q8 IF", block4(0x2000, 16), "2000-200F")
# ---------- microprogrammed control (Mano 7-4, 7-7, 7-20, 7-21) ----------
chk("7-4 with CDR (MHz)", round(1e3 / max(40 + 10 + 40 + 10, 40), 2), 10.0)
chk("7-4 without CDR (MHz)", round(1e3 / (40 + 10 + 40 + 40), 2), 7.69)
for op, want in [(0b0010, 0x08), (0b1011, 0x2C), (0b1111, 0x3C)]:
    chk(f"7-7 map {op:04b}", op << 2, want)
chk("7-20 5+4 split", (2**5 - 1) + (2**4 - 1), 46)
chk("7-21 control word bits", 4 + 4 + 4 + 5 + 3, 20)
print("\nALL NUMBERS OK")
