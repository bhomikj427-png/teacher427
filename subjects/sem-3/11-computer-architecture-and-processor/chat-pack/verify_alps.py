"""Assemble (keystone, 16-bit) and run (unicorn, 16-bit real mode) every ALP in instructions-chat.md.
Code sits at CS:0100H (ORG 100H). Data uses the file's offsets; labels are replaced by those offsets.
Run: python verify_alps.py"""
from keystone import Ks, KS_ARCH_X86, KS_MODE_16
from unicorn import Uc, UC_ARCH_X86, UC_MODE_16
from unicorn.x86_const import *

ks = Ks(KS_ARCH_X86, KS_MODE_16)
SEG = 0x1000          # CS = DS = ES = 1000H unless the program sets its own
BASE = SEG * 16

def run(name, asm, data, check, seg=SEG):
    code, _ = ks.asm(asm, 0x100)
    code = bytes(code) + b"\xF4"                 # HLT marks the end
    mu = Uc(UC_ARCH_X86, UC_MODE_16)
    mu.mem_map(0, 0x100000)
    for off, bs in data.items():
        mu.mem_write(seg * 16 + off, bytes(bs))
    mu.mem_write(BASE + 0x100, code)
    for r in (UC_X86_REG_CS, UC_X86_REG_DS, UC_X86_REG_ES, UC_X86_REG_SS):
        mu.reg_write(r, SEG)
    mu.reg_write(UC_X86_REG_SP, 0xFFFE)
    end = BASE + 0x100 + len(code) - 1
    mu.emu_start(BASE + 0x100, end, count=100000)
    rd = lambda off, n=1, s=seg: bytes(mu.mem_read(s * 16 + off, n))
    check(mu, rd)
    print(f"ok  {name}")

# 1. Count positive / negative signed bytes (ETE26 C1, ETE25 C2, A3 Q3) - REPEAT-UNTIL with LOOP
arr = [0x81, 0x9E, 0x31, 0xAB, 0x83, 0xA4, 0x4F, 0x68, 0x92, 0xA2]   # deck's array: 3 +ve, 7 -ve
def c1(mu, rd):
    assert rd(0x20A, 2) == bytes([3, 7]), rd(0x20A, 2)
run("count +ve/-ve", """
        MOV CX, 10
        MOV SI, 0x200
        XOR BX, BX
REPT:   MOV AL, [SI]
        TEST AL, 0x80
        JNZ NEG1
        INC BL
        JMP UNTIL
NEG1:   INC BH
UNTIL:  INC SI
        LOOP REPT
        MOV [0x20A], BL
        MOV [0x20B], BH
""", {0x200: arr}, c1)

# 2. Exchange two 10-byte blocks at 1200H and 1220H - WHILE-DO (test at top)
b1, b2 = list(range(0x10, 0x1A)), list(range(0x20, 0x2A))
def c2(mu, rd):
    assert rd(0x1200, 10) == bytes(b2) and rd(0x1220, 10) == bytes(b1)
run("block exchange", """
        MOV SI, 0x1200
        MOV DI, 0x1220
        MOV CX, 10
WHILE1: JCXZ DONE
        MOV AL, [SI]
        XCHG AL, [DI]
        MOV [SI], AL
        INC SI
        INC DI
        DEC CX
        JMP WHILE1
DONE:   NOP
""", {0x1200: b1, 0x1220: b2}, c2)

# 3. Capital -> small case (A3 Q2)
for ch, want in [(0x41, 0x61), (0x5A, 0x7A), (0x61, 0x61), (0x35, 0x35)]:
    def c3(mu, rd, want=want):
        assert rd(0x201) == bytes([want]), rd(0x201)
    run(f"case {chr(ch)}", """
        MOV AL, [0x200]
        CMP AL, 0x41
        JB  DONE
        CMP AL, 0x5A
        JA  DONE
        ADD AL, 0x20
DONE:   MOV [0x201], AL
""", {0x200: [ch]}, c3)

# 4. Move 16-byte string 7000:0200 -> 7000:0300 (A3 Q5)
src = list(range(0x41, 0x51))
def c4(mu, rd):
    assert rd(0x300, 16, 0x7000) == bytes(src)
run("string move", """
        MOV AX, 0x7000
        MOV DS, AX
        MOV ES, AX
        MOV SI, 0x200
        MOV DI, 0x300
        MOV CX, 16
        CLD
        REP MOVSB
""", {0x200: src}, c4, seg=0x7000)

# 5. Binary -> Gray (A3 Q6)
for x in (0xB6, 0x00, 0xFF, 0x2D):
    def c5(mu, rd, x=x):
        assert rd(0x201) == bytes([x ^ (x >> 1)]), (hex(x), rd(0x201))
    run(f"gray {x:02X}", """
        MOV AL, [0x200]
        MOV BL, AL
        SHR BL, 1
        XOR AL, BL
        MOV [0x201], AL
""", {0x200: [x]}, c5)
print("    gray B6 ->", hex(0xB6 ^ (0xB6 >> 1)))

# 6. Square root of a perfect square, odd-number subtraction (A3 Q7)
for n in (16, 25, 49, 64, 81):
    def c6(mu, rd, n=n):
        assert rd(0x201)[0] ** 2 == n, (n, rd(0x201))
    run(f"sqrt {n}", """
        MOV AL, [0x200]
        MOV BL, 1
        XOR CL, CL
NEXT:   INC CL
        SUB AL, BL
        JZ  DONE
        ADD BL, 2
        JMP NEXT
DONE:   MOV [0x201], CL
""", {0x200: [n]}, c6)

# 7. Even/odd count; odd -> DS:010CH, even -> DS:010DH (Summer C2). Data segment 2000H.
nums = [3, 8, 15, 22, 7, 10, 41, 100, 9, 64]   # 5 odd, 5 even
def c7(mu, rd):
    assert rd(0x10C, 2, 0x2000) == bytes([5, 5])
run("even/odd", """
        MOV AX, 0x2000
        MOV DS, AX
        MOV SI, 0x100
        MOV CX, 10
        XOR BX, BX
NEXT:   MOV AL, [SI]
        TEST AL, 1
        JZ  EVEN1
        INC BL
        JMP CONT
EVEN1:  INC BH
CONT:   INC SI
        LOOP NEXT
        MOV [0x10C], BL
        MOV [0x10D], BH
""", {0x100: nums}, c7, seg=0x2000)

# 8. SPL Q18: DS = 2000H; [0500H] -> BX, CX; [0600H] + 05H -> [0700H]
def c8(mu, rd):
    assert mu.reg_read(UC_X86_REG_BX) == 0x1234 == mu.reg_read(UC_X86_REG_CX)
    assert rd(0x700, 1, 0x2000) == bytes([0x3A])
run("SPL Q18", """
        MOV AX, 0x2000
        MOV DS, AX
        MOV BX, [0x500]
        MOV CX, BX
        MOV AL, [0x600]
        ADD AL, 0x05
        MOV [0x700], AL
""", {0x500: [0x34, 0x12], 0x600: [0x35]}, c8, seg=0x2000)

# 9. Count 'e' in 'exercise' (SPL Q19)
def c9(mu, rd):
    assert rd(0x208) == bytes([3])
run("count e", """
        MOV SI, 0x200
        MOV CX, 8
        XOR BL, BL
NEXT:   CMP BYTE PTR [SI], 0x65
        JNE SKIP
        INC BL
SKIP:   INC SI
        LOOP NEXT
        MOV [0x208], BL
""", {0x200: list(b"exercise")}, c9)

# 10. 16-bit binary -> unpacked BCD digits, most significant first (SPL Q20)
for v in (0xFFFF, 0x04D2, 0x0007):
    digits = [int(d) for d in str(v)]
    def c10(mu, rd, digits=digits):
        assert rd(0x210, len(digits)) == bytes(digits), (digits, rd(0x210, 5))
        assert mu.reg_read(UC_X86_REG_BX) == 10
    run(f"bin->BCD {v}", """
        MOV AX, [0x200]
        MOV BX, 10
        XOR CX, CX
NEXT:   XOR DX, DX
        DIV BX
        PUSH DX
        INC CX
        OR  AX, AX
        JNZ NEXT
        MOV DI, 0x210
POPD:   POP DX
        MOV [DI], DL
        INC DI
        LOOP POPD
""", {0x200: [v & 0xFF, v >> 8]}, c10)

# 11. Smallest of ten (deck Part 2, procedure)
arr2 = [0xAB, 0x23, 0xA5, 0xC3, 0x22, 0xAC, 0x97, 0x79, 0x20, 0xB1]
def c11(mu, rd):
    assert rd(0x20A) == bytes([0x20])
run("smallest (PROC)", """
        MOV SI, 0x200
        MOV CX, 9
        MOV AL, [SI]
        CALL SMALL
        MOV [0x20A], AL
        JMP FIN
SMALL:  INC SI
        CMP AL, [SI]
        JB  SKIP
        MOV AL, [SI]
SKIP:   LOOP SMALL
        RET
FIN:    NOP
""", {0x200: arr2}, c11)

# 12. Add two 8-bit numbers with carry into a 16-bit result (deck Part 2)
def c12(mu, rd):
    assert rd(0x202, 2) == bytes([0x1A, 0x01])
run("8-bit add with carry", """
        MOV SI, 0x200
        XOR AX, AX
        MOV AL, [SI]
        ADD AL, [SI+1]
        ADC AH, 0
        MOV [SI+2], AX
""", {0x200: [0xF6, 0x24]}, c12)
print("\nALL ALPs OK")
