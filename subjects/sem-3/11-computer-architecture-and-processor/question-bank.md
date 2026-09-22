# ECE2108 — Question Bank

**Two priorities, in this order.**

| | Base | Why it ranks there | Items |
|---|---|---|---|
| **P1** | The professor's **Assignment 1 + Assignment 2** | First-party. This is literally what he wrote and marked. | 35 |
| **P2** | **Mano's end-of-chapter problems** | He builds the assignments out of them — *Assignment 2 is 15 of 15 Mano problems.* So Mano is the best available predictor of everything he hasn't asked yet. | 118 in MTE scope |

There is still **no ECE2108 past paper**. P1 and P2 are the best evidence that exists; neither is an exam paper.

---

## How the two bases relate — the finding that sets the order

With Mano 3e finally readable (see *Sourcing*, bottom), every assignment question was traced to its source.

**Assignment 2 = Mano, copied.** All 15 items, in Mano's own order, sub-parts sometimes dropped:

| A2 | Mano | A2 | Mano | A2 | Mano |
|---|---|---|---|---|---|
| Q1 | **5-1** | Q6 | **5-9** | Q11 | **9-1** |
| Q2 | **5-3** | Q7 | **5-12** | Q12 | **9-3** |
| Q3 | **5-4** | Q8 | **5-16** | Q13 | **9-5** |
| Q4 | **5-6** | Q9 | **5-20** | Q14 | **9-10** |
| Q5 | **5-8** | Q10 | **5-21** | Q15 | **9-11** |

**Assignment 1 = Mano, adapted.** Same problems, different numbers:

| A1 | Mano | What he changed |
|---|---|---|
| Q10 | **4-7** | swapped which transfer statements are listed |
| Q12 | **4-1** | `yT₃` → `yT₂` |
| Q14 (i) | **4-6** | 16 registers × 32 bits → 4 registers × 4 bits |
| Q14 (ii) | **4-5** | unchanged |
| Q16 | **4-12** | kept Mano's rows (a) and (d) exactly, dropped (b)(c)(e) |
| Q18 | **4-19** | registers AR/BR/CR/DR → R1–R4; **values and operations identical** |
| Q19 | **4-21** | `R = 11011101` → `11111111`; shift order changed |
| Q17 | — | not a problem — it is Mano §4-7 / Fig. 4-13, the ALSU itself |

**What this means for how you drill.**
For **U2 and U4** (Mano ch. 5, 9) the Mano problem *is* the question — numbers and all.
For **U1** (ch. 4) the Mano problem predicts the *form*, and he moves the numbers — so drill the method, never the answer.
For **U3** (ch. 7) **neither assignment touches it.** Mano ch. 7 is the only question evidence that exists for that unit. Do not skip it because no assignment did.

---

## P1 · Assignment 1 — 20 questions, 200 marks

*Submitted 24-08-2026. Word limit: 1 mark = 20 words.*

| Q | Marks | v3 file | Mano |
|---|---|---|---|
| 1 | 12 | 01 | — |
| 2 | 4 | 01 | — |
| 3 | 10 | 01 | — |
| 4 | 10 | 01 | — |
| 5 | 10 | 01 | — |
| 6 | 10 | 01 | — |
| 7 | 24 | 02 | ch. 2 |
| 8 | 4 | 04 | ch. 3 |
| 9 | 4 | 04 | ch. 3 |
| 10 | 4 | 03 | 4-7 |
| 11 | 4 | 03 | — |
| 12 | 8 | 03 | 4-1 |
| 13 | 8 | 03 | — |
| 14 | 16 | 03 | 4-5, 4-6 |
| 15 | 4 | 04 | — |
| 16 | 8 | 04 | 4-12 |
| 17 | 16 | 05 | §4-7 |
| 18 | 8 | 04 | 4-19 |
| 19 | 8 | 04 | 4-21 |
| 20 | 20 | 01 | — |

**Q1** *(2 × 6 = 12)* Define the following terms: (i) Digital Computer (ii) Computer Architecture (iii) Computer Organization (iv) Microarchitecture (v) Microoperations (vi) Register Transfer Language

**Q2** *(4)* What distinguishes computer organization from computer architecture?

**Q3** *(10)* Briefly explain about the different generations of computers. Tabulate & highlight the significant technological contributions & human contributors of each generation.

**Q4** *(10)* List the various elements that constitute a computer? Explain the roles and responsibility of each element.

**Q5** *(10)* In how many ways are computers divided? Distinguish between each type of computers.

**Q6** *(10)* Describe the features of the Von Neumann architecture. Compare & contrast Von Neumann and Harvard architecture.

**Q7** *(4 × 6 = 24)* Explain the working of the following. Support your answer with circuits formed with basic gates: (i) D Flip-Flop (ii) 3-to-8 line Decoder (iii) 4-to-1-line multiplexer (iv) Quadruple 2×1 multiplexer (v) 4-bit register with parallel load (vi) 4-bit Bidirectional Shift Register with Parallel Load

**Q8** *(4)* How are the +64 and −64 signed numbers represented in the signed-magnitude, 1's complement, and 2's complement number systems?

**Q9** *(4)* Perform the addition of two signed numbers R1 = +64 and R2 = +84 using 2's complement number systems. The size of each register is 8-bit.

**Q10** *(4)* Categories the following statements as register or memory transfer statement. Explain the operation being performed.
i) A ← B  ii) A(L) ← B(H)  iii) R1 ← M[AR]  iv) M ← R2

**Q11** *(4)* Represent the following conditional control statement as a register transfer statement. If (S = 1) then (AL ← BH). Explain the operation being performed.

**Q12** *(8)* Represent the following conditional control statement as a register transfer statement. If (y = 1 && T2 = 1) then (R2 ← R1) and (R1 ← R2). Create a block diagram of the hardware that implements the register transfer statement. Explain the working of the circuit.

**Q13** *(8)* What specifically is a bus in the context of computer architecture. What is its role. List the names of five most popular such structures.

**Q14** *(8 × 2 = 16)* Draw a neatly labelled diagram of a common bus system, as per the constraints mentioned below, that facilitates the transfer of data between four registers each of which is 4-bits. Explain the working in each case. i) Multiplexers, ii) Tri-state buffers and a decoder.

**Q15** *(4)* What is micro-operation? What are the different types of micro-operations?

**Q16** *(8)* Design a 4-bit adder-subtractor combinational circuit using four full-adder circuits. Explain its working using the following combination.

| Case | M | A | B |
|---|---|---|---|
| i) | 0 | 0111 | 0110 |
| ii) | 1 | 0101 | 1010 |

**Q17** *(8 + 8 = 16)* Design a 4-bit arithmetic-logic-shift circuit. Explain the working of the circuit for the following functions. i) Transfer A ii) Add with carry iii) XOR iv) Shift right A

**Q18** *(8)* The initial values of the 8-bit registers R1, R2, R3, and R4 are as follows. Determine the results in each register once the following sequence of micro-operations has been performed.
i) R1 ← R1 + R2  ii) R3 ← R3 ∧ R4, R2 ← R2 + 1  iii) R1 ← R1 − R3
Given: R1 = 11110010, R2 = 11111111, R3 = 10111001, and R4 = 11101010.

**Q19** *(8)* Find the sequence of binary values in register R following a logical shift-right, a circular shift right, a logical shift left, and a circular shift left, starting from R = 11111111.

**Q20** *(10 × 2 = 20)* Write short note on the following: i) RISC architecture and ii) CISC architecture.

---

## P1 · Assignment 2 — 15 questions, 150 marks

*Due 16-09-2026 16:30 (passed).* **Every item is a Mano problem.** The Mano number is given so you can
find the rest of the sub-parts he dropped — those are fair game for the exam.

**Q1** *(10)* `= Mano 5-1` · v3 file 06
A computer uses a memory unit with 256K words of 32 bits each. A binary instruction code is stored in one word of memory. The instruction has four parts: an indirect bit, an operation code, a register code part to specify one of 64 registers, and an address part.
a. How many bits are there in the operation code, the register code part, and the address part?
b. Draw the instruction word format and indicate the number of bits in each part.
c. How many bits are there in the data and address inputs of the memory?

**Q2** *(10)* `= Mano 5-3` · v3 file 06
The following control inputs are active in the common bus system taught in the class. For each case, specify the register transfer that will be executed during the next clock transition.
*(Mano's table: S₂S₁S₀ / LD of register / Memory / Adder — a. 111, IR, Read, — · b. 110, PC, —, — · c. 100, DR, Write, — · d. 000, AC, —, Add)*

**Q3** *(10)* `= Mano 5-4` · v3 file 06
The following register transfers are to be executed in the system of Fig. 5-4. For each transfer, specify: (1) the binary value that must be applied to bus select inputs S₂, S₁, and S₀; (2) the register whose LD control input must be active (if any); (3) a memory read or write operation (if needed); and (4) the operation in the adder and logic circuit (if any).
a. AR ← PC  b. IR ← M[AR]  c. M[AR] ← TR  d. AC ← DR, DR ← AC (done simultaneously)

**Q4** *(10)* `= Mano 5-6` · v3 file 06
Consider the instruction formats of the basic computer and respective list of instructions. For each of the following 16-bit instructions. a) 1011 0001 0010 0100  b) 0111 0000 0010 0000
i) Determine the equivalent four-digit hexadecimal code for each and ii) Explain in your own words what it is that the instruction is going to perform.
> ⚠ **He dropped Mano's part (a): `0001 0000 0010 0100`.** Do that one too.

**Q5** *(10)* `= Mano 5-8` · v3 file 07
In the context of a basic computer, with the help of a timing diagram explain the working of the microoperation: C₇T₃: SC ← 0.
> Mano's wording adds: *"Draw a timing diagram similar to Fig. 5-7 assuming that SC is cleared to 0 at time T₃ if control signal C₇ is active. C₇ is activated with the positive clock transition associated with T₃."*

**Q6** *(10)* `= Mano 5-9` · v3 file 07
The content of AC in the basic computer is hexadecimal A937 and the initial value of E is 1. Determine the contents of AC, E, PC, AR, and IR in hexadecimal after the execution of the CLA instruction.
> ⚠ **He dropped Mano's real workload:** *"Repeat 11 more times, starting from each one of the register-reference instructions. The initial value of PC is hexadecimal 021."* All 12 register-reference instructions are drillable here.

**Q7** *(10)* `= Mano 5-12` · v3 file 07
The content of PC in the basic computer is 3AF. The content of AC is 7EC3. The content of memory at address 3AF is 932E. The content of memory at address 32E is 09AC. The content of memory at address 9AC is 8B9F.
a. What is the instruction that will be fetched and executed next?
b. Show the binary operation that will be performed in the AC when the instruction is executed.
> ⚠ **He dropped Mano's part (c):** *"Give the contents of registers PC, AR, DR, AC, and IR in hexadecimal and the values of E, I, and the sequence counter SC in binary at the end of the instruction cycle."*

**Q8** *(10)* `= Mano 5-16` · v3 file 07
A computer uses a memory of 65,536 words with eight bits in each word. It has the following registers: PC, AR, TR (16 bits each), and AC, DR, IR (eight bits each). A memory-reference instruction consists of three words: an 8-bit operation-code (one word) and a 16-bit address (in the next two words). All operands are eight bits. There is no indirect bit. List the sequence of microoperations for fetching a memory reference instruction and then placing the operand in DR. Start from timing signal T₀.
> ⚠ **He dropped Mano's parts (a) and (b):** draw the block diagram of the computer (no common bus), and draw the placement in memory of a typical three-word instruction and its 8-bit operand.

**Q9** *(10)* `= Mano 5-20` · v3 file 08
The operations to be performed with a flip-flop F (not used in the basic computer) are specified by the following register transfer statements:
`xT₃: F ← 1` (set F to 1) · `yT₁: F ← 0` (clear F to 0) · `zT₂: F ← F′` (complement F) · `wT₅: F ← G` (transfer value of G to F)
Otherwise, the content of F must not change. Draw the logic diagram showing the connections of the gates that form the control functions and the inputs of flip flop F. Use a JK flip-flop and minimize the number of gates.

**Q10** *(10)* `= Mano 5-21` · v3 file 08 · **verbatim, word for word**
Derive the control gates associated with the program counter PC in the basic computer. Draw the logic diagram of the gates and show how the output is connected to the LD, INR and CLR inputs of PC. Minimize the number of gates.

**Q11** *(10)* `= Mano 9-1` · v3 file 11
In certain scientific computations it is necessary to perform the arithmetic operation (Aᵢ + Bᵢ)(Cᵢ + Dᵢ) with a stream of numbers. Specify a pipeline configuration to carry out this task. List the contents of all registers in the pipeline for i = 1 through 6.

**Q12** *(10)* `= Mano 9-3` · v3 file 11 · **verbatim**
Determine the number of clock cycles that it takes to process 200 tasks in a six-segment pipeline.

**Q13** *(10)* `= Mano 9-5` · v3 file 11
A three segment pipeline structure is used to perform the arithmetic operation (Aᵢ × Bᵢ) + Cᵢ for i = 1 through 6 with a stream of numbers. R1 through R5 are registers that receive new data with every clock pulse. The pipeline configuration has the following propagation times: 40 ns for the operands to be read from memory into registers R1 and R2, 45 ns for the signal to propagate through the multiplier, 5 ns for the transfer into R3, and 15 ns to add the two numbers into R5.
a. What is the minimum clock cycle time that can be used?
b. A non-pipeline system can perform the same operation by removing R3 and R4. How long will it take to multiply and add the operands without using the pipeline?
c. Calculate the speedup of the pipeline for 10 tasks and again for 100 tasks.
d. What is the maximum speedup that can be achieved?

**Q14** *(10)* `= Mano 9-10` · v3 file 11 · **verbatim**
Explain four possible hardware schemes that can be used in an instruction pipeline in order to minimize the performance degradation caused by instruction branching.

**Q15** *(10)* `= Mano 9-11` · v3 file 11
Consider the four instructions in the following program. Suppose that the first instruction starts from step 1 in the four-segment pipeline. Specify what operations are performed in the four segments during step 4.
```
Load    R1 ← M[312]
ADD     R2 ← R2 + M[313]
INC     R3 ← R3 + 1
STORE   M[314] ← R3
```

---
---

# P2 · Mano's end-of-chapter problems — MTE scope

Transcribed from the book itself (see *Sourcing*). Each is tagged with the v3 file it belongs to.
**`[A1]` / `[A2]`** marks the ones he has already asked — those are the confirmed ones; the rest are
the same author's questions on the same material, which is exactly why they rank second.

## Chapter 3 — Data Representation → files 00, 04

Prerequisite chapter. A1 Q8 and Q9 are this chapter's form.

- **3-1** Convert the following binary numbers to decimal: 101110; 1110101; and 110110100.
- **3-2** Convert the following numbers with the indicated bases to decimal: (12121)₃; (4310)₅; (50)₇; and (198)₁₂.
- **3-3** Convert the following decimal numbers to binary: 1231; 673; and 1998.
- **3-4** Convert the following decimal numbers to the bases indicated. a. 7562 to octal b. 1938 to hexadecimal c. 175 to binary
- **3-5** Convert the hexadecimal number F3A7C2 to binary and octal.
- **3-6** What is the radix of the numbers if the solution to the quadratic equation x² − 10x + 31 = 0 is x = 5 and x = 8?
- **3-7** Show the value of all bits of a 12-bit register that hold the number equivalent to decimal 215 in (a) binary; (b) binary-coded octal; (c) binary-coded hexadecimal; (d) binary-coded decimal (BCD).
- **3-8** Show the bit configuration of a 24-bit register when its content represents the decimal equivalent of 295: (a) in binary; (b) in BCD; (c) in ASCII using eight bits with even parity.
- **3-9** Write your name in ASCII using an 8-bit code with the leftmost bit always 0. Include a space between names and a period after a middle initial.
- **3-10** Decode the following ASCII code: `1001010 1001111 1001000 1001110 0100000 1000100 1001111 1000101`
- **3-11** Obtain the 9's complement of the following eight-digit decimal numbers: 12349876; 00980100; 90009951; and 00000000.
- **3-12** Obtain the 10's complement of the following six-digit decimal numbers: 123900; 090657; 100000; and 000000.
- **3-13** Obtain the 1's and 2's complements of the following eight-digit binary numbers: 10101110; 10000001; 10000000; 00000001; and 00000000. — `≈ A1 Q8`
- **3-14** Perform the subtraction with the following unsigned decimal numbers by taking the 10's complement of the subtrahend. a. 5250 − 1321 b. 1753 − 8640 c. 20 − 100 d. 1200 − 250
- **3-15** Perform the subtraction with the following unsigned binary numbers by taking the 2's complement of the subtrahend. a. 11010 − 10000 b. 11010 − 1101 c. 100 − 110000 d. 1010100 − 1010100
- **3-16** Perform the arithmetic operations (+42) + (−13) and (−42) − (−13) in binary using signed-2's complement representation for negative numbers. — `≈ A1 Q9`
- **3-17** Perform the arithmetic operations (+70) + (+80) and (−70) + (−80) with binary numbers in signed-2's complement representation. Use eight bits to accommodate each number together with its sign. Show that overflow occurs in both cases, that the last two carries are unequal, and that there is a sign reversal. — **the overflow rule; examinable**
- **3-18** Perform the following arithmetic operations with the decimal numbers using signed-10's complement representation for negative numbers. a. (−638) + (+785) b. (−638) − (+185)
- **3-19** A 36-bit floating-point binary number has eight bits plus sign for the exponent and 26 bits plus sign for the mantissa. The mantissa is a normalized fraction. Numbers in the mantissa and exponent are in signed-magnitude representation. What are the largest and smallest positive quantities that can be represented, excluding zero?
- **3-20** Represent the number (+46.5)₁₀ as a floating-point binary number with 24 bits. The normalized fraction mantissa has 16 bits and the exponent has 8 bits.
- **3-21** The Gray code is sometimes called a reflected code because the bit values are reflected on both sides of any 2ⁿ value. Using this property, obtain: a. The Gray code numbers for 16 through 31 as a continuation of Table 3-5. b. The excess-3 Gray code for decimals 10 to 19 as a continuation of Table 3-6.
- **3-22** Represent decimal number 8620 in (a) BCD; (b) excess-3 code; (c) 2421 code; (d) as a binary number.
- **3-23** List the 10 BCD digits with an even parity in the leftmost position (total of five bits per digit). Repeat with an odd-parity bit.
- **3-24** Represent decimal 3984 in the 2421 code of Table 3-6. Complement all bits of the coded number and show that the result is the 9's complement of 3984 in the 2421 code.
- **3-25** Show that the exclusive-OR function x = A ⊕ B ⊕ C ⊕ D is an odd function — x = 1 only when the total number of 1's in A, B, C, and D is odd.
- **3-26** Derive the circuits for a 3-bit parity generator and 4-bit parity checker using an even-parity bit. (The circuits of Fig. 3-3 use odd parity.)

## Chapter 2 — Digital Components → file 02

Only the items A1 Q7 examines. (The full chapter runs 2-1 … 2-23; the rest is Digital Electronics revision.)

- **2-4** Draw the logic diagram of a 2-to-4-line decoder with only NOR gates. Include an enable input.
- **2-5** Modify the decoder of Fig. 2-2 so that the circuit is enabled when E = 1 and disabled when E = 0. List the modified truth table.
- **2-6** Construct a 5-to-32-line decoder with four 3-to-8-line decoders with enable and one 2-to-4-line decoder.
- **2-8** Construct a 16-to-1-line multiplexer with two 8-to-1-line multiplexers and one 2-to-1-line multiplexer.
- **2-9** Draw the block diagram of a dual 4-to-1-line multiplexer and explain its operation by means of a function table. — `≈ A1 Q7(iv)`
- **2-10** Include a two-input AND gate with the register of Fig. 2-6 and connect the gate output to the clock inputs of all the flip-flops. One input receives the clock pulses; the other provides a parallel load control. Explain the operation of the modified register.
- **2-12** Include a synchronous clear capability to the register with parallel load of Fig. 2-7. — `≈ A1 Q7(v)`
- **2-13** The content of a 4-bit register is initially 1101. The register is shifted six times to the right with the serial input being 101101. What is the content of the register after each shift?
- **2-14** What is the difference between serial and parallel transfer? Using a shift register with parallel load, explain how to convert serial input data to parallel output and parallel input data to serial output.
- **2-15** A ring counter is a shift register as in Fig. 2-8 with the serial output connected to the serial input. Starting from an initial state of 1000, list the sequence of states of the four flip-flops after each shift.
- **2-16** The 4-bit bidirectional shift register with parallel load shown in Fig. 2-9 is enclosed within one IC package. a. Draw a block diagram of the IC showing all inputs and outputs. b. Draw a block diagram using two ICs to produce an 8-bit bidirectional shift register with parallel load. — `≈ A1 Q7(vi)`

## Chapter 4 — Register Transfer and Microoperations → files 03, 04, 05 (U1)

**He re-numbers this chapter.** Drill the method, not the answer.

- **4-1** *(file 03)* Show the block diagram of the hardware (similar to Fig. 4-2a) that implements the following register transfer statement: `yT₃: R2 ← R1, R1 ← R2` — `[A1 Q12, as yT₂]`
- **4-2** *(file 03)* The outputs of four registers, R0, R1, R2, and R3, are connected through 4-to-1-line multiplexers to the inputs of a fifth register, R5. Each register is eight bits long. The required transfers are dictated by four timing variables T₀ through T₃: `T₀: R5 ← R0` · `T₁: R5 ← R1` · `T₂: R5 ← R2` · `T₃: R5 ← R3`. The timing variables are mutually exclusive. Draw a block diagram showing the hardware implementation, including the connections from the four timing variables to the selection inputs of the multiplexers and to the load input of R5.
- **4-3** *(file 03)* Represent the following conditional control statement by two register transfer statements with control functions: `If (P = 1) then (R1 ← R2) else if (Q = 1) then (R1 ← R3)` — `≈ A1 Q11`
- **4-4** *(file 03)* What has to be done to the bus system of Fig. 4-3 to be able to transfer information from any register to any other register? Specifically, show the connections that must be included to provide a path from the outputs of register C to the inputs of register A.
- **4-5** *(file 03)* Draw a diagram of a bus system similar to the one shown in Fig. 4-3, but use three-state buffers and a decoder instead of the multiplexers. — `[A1 Q14(ii)]`
- **4-6** *(file 03)* A digital computer has a common bus system for 16 registers of 32 bits each. The bus is constructed with multiplexers. a. How many selection inputs are there in each multiplexer? b. What size of multiplexers are needed? c. How many multiplexers are there in the bus? — `[A1 Q14(i), shrunk to 4 × 4]`
- **4-7** *(file 03)* The following transfer statements specify a memory. Explain the memory operation in each case. a. `R2 ← M[AR]` b. `M[AR] ← R3` c. `R5 ← M[R5]` — `[A1 Q10]`
- **4-8** *(file 03)* Draw the block diagram for the hardware that implements the following statements: `x + yz: AR ← AR + BR`, where AR and BR are two n-bit registers and x, y, z are control variables. Include the logic gates for the control function. (Remember that `+` designates OR in a control function but arithmetic plus in a microoperation.)
- **4-9** *(file 03)* Show the hardware that implements the following statement. Include the logic gates for the control function and a block diagram for the binary counter with a count enable input: `xyT₀ + T₁ + y′T₂: AR ← AR + 1`
- **4-10** *(file 03)* Consider the following register transfer statements for two 4-bit registers R1 and R2: `xT: R1 ← R1 + R2` · `x′T: R1 ← R2`. Draw a diagram showing the hardware implementation, using block diagrams for the two 4-bit registers, a 4-bit adder, and a quadruple 2-to-1-line multiplexer that selects the inputs to R1.
- **4-11** *(file 03)* Using a 4-bit counter with parallel load as in Fig. 2-11 and a 4-bit adder as in Fig. 4-6, draw a block diagram that shows how to implement: `x: R1 ← R1 + R2` · `x′y: R1 ← R1 + 1`
- **4-12** *(file 04)* The adder-subtractor circuit of Fig. 4-7 has the following values for input mode M and data inputs A and B. In each case, determine the values of the outputs S₃, S₂, S₁, S₀, and C₄. a. M=0, A=0111, B=0110 · b. M=0, A=1000, B=1001 · c. M=1, A=1100, B=1000 · d. M=1, A=0101, B=1010 · e. M=1, A=0000, B=0001 — `[A1 Q16 = rows a and d, unchanged]`
- **4-13** *(file 04)* Design a 4-bit combinational circuit decrementer using four full-adder circuits.
- **4-14** *(file 04)* Assume that the 4-bit arithmetic circuit of Fig. 4-9 is enclosed in one IC package. Show the connections among two such ICs to form an 8-bit arithmetic circuit.
- **4-15** *(file 04)* Design an arithmetic circuit with one selection variable S and two n-bit data inputs A and B, generating: S=0, Cᵢₙ=0 → D = A + B · S=0, Cᵢₙ=1 → D = A + 1 · S=1, Cᵢₙ=0 → D = A − 1 · S=1, Cᵢₙ=1 → D = A + B̄ + 1. Draw the logic diagram for the first two stages.
- **4-16** *(file 04)* Derive a combinational circuit that selects and generates any of the 16 logic functions listed in Table 4-5.
- **4-17** *(file 04)* Design a digital circuit that performs the four logic operations of exclusive-OR, exclusive-NOR, NOR, and NAND. Use two selection variables. Show the logic diagram of one typical stage.
- **4-18** *(file 04)* Register A holds the 8-bit binary 11011001. Determine the B operand and the logic microoperation to be performed in order to change the value in A to: a. 01101101 b. 11111101 — **the mask / set / clear trick**
- **4-19** *(file 04)* The 8-bit registers AR, BR, CR, and DR initially have AR = 11110010, BR = 11111111, CR = 10111001, DR = 11101010. Determine the 8-bit values in each register after: `AR ← AR + BR` · `CR ← CR ∧ DR, BR ← BR + 1` · `AR ← AR − CR` — `[A1 Q18, renamed R1–R4]`
- **4-20** *(file 04)* An 8-bit register contains the binary value 10011100. What is the register value after an arithmetic shift right? Starting from 10011100, determine the value after an arithmetic shift left, and state whether there is an overflow.
- **4-21** *(file 04)* Starting from an initial value of R = 11011101, determine the sequence of binary values in R after a logical shift-left, followed by a circular shift-right, followed by a logical shift-right and a circular shift-left. — `[A1 Q19, from 11111111, reordered]`
- **4-22** *(file 05)* What is the value of output H in Fig. 4-12 (the ALSU stage) for the given A, S and carry inputs? — *OCR-damaged in the source; read the figure in the book before attempting.*
- **4-23** *(file 03)* What is wrong with the following register transfer statements? a. `xT: AR ← AR, AR ← 0` b. `yT: R1 ← R2, R1 ← R3` c. `zT: PC ← AR, PC ← PC + 1` — **a favourite viva question**

## Chapter 5 — Basic Computer Organization and Design → files 06, 07, 08 (U2)

**He copies this chapter outright.** Ten of its 25 problems are Assignment 2 Q1–Q10. Assume the other
fifteen are the exam.

- **5-1** *(file 06)* `[A2 Q1]` — full text under Assignment 2 above.
- **5-2** *(file 06)* What is the difference between a direct and an indirect address instruction? How many references to memory are needed for each type of instruction to bring an operand into a processor register? — **not asked yet; classic 4-mark question**
- **5-3** *(file 06)* `[A2 Q2]`
- **5-4** *(file 06)* `[A2 Q3]`
- **5-5** *(file 06)* Explain why each of the following microoperations cannot be executed during a single clock pulse in the system shown in Fig. 5-4. Specify a sequence of microoperations that will perform the operation. a. `IR ← M[PC]` b. `AC ← AC + TR` c. `DR ← DR + AC` (AC does not change) — **not asked yet; tests the bus bottleneck directly**
- **5-6** *(file 06)* `[A2 Q4]` — he dropped part (a), `0001 0000 0010 0100`.
- **5-7** *(file 06)* What are the two instructions needed in the basic computer in order to set the E flip-flop to 1? — **not asked yet**
- **5-8** *(file 07)* `[A2 Q5]`
- **5-9** *(file 07)* `[A2 Q6]` — he dropped the other 11 register-reference instructions.
- **5-10** *(file 07)* An instruction at address 021 in the basic computer has I = 0, an operation code of the AND instruction, and an address part equal to 083 (all numbers are in hexadecimal). The memory word at address 083 contains the operand B8F2 and the content of AC is A937. Go over the instruction cycle and determine the contents of the following registers at the end of the execute phase: PC, AR, DR, AC, and IR. Repeat the problem six more times starting with an operation code of another memory-reference instruction. — **not asked yet; the direct-MRI twin of A2 Q7**
- **5-11** *(file 07)* Show the contents in hexadecimal of registers PC, AR, DR, IR, and SC of the basic computer when an ISZ indirect instruction is fetched from memory and executed. The initial content of PC is 7FF. The content of memory at address 7FF is EA9F. The content of memory at address A9F is 0C35. The content of memory at address C35 is FFFF. Give the answer in a table with five columns, one for each register and a row for each timing signal. Show the contents of the registers after the positive transition of each clock pulse. — **not asked yet; the per-timing-signal table is the hardest form in the chapter**
- **5-12** *(file 07)* `[A2 Q7]` — he dropped part (c), the full register dump at end of cycle.
- **5-13** *(file 07)* Assume that the first six memory-reference instructions listed in Table 5-4 are changed to XOR, ADM, SUB, XCH, SEQ, BPA (definitions in the book's table). Give the sequence of register transfer statements needed to execute each, starting from timing T₄. The adder and logic circuit can do `AC ← AC ⊕ DR` but cannot subtract directly — subtraction must use the 2's complement. AC must not change unless the instruction says so; TR may be used for temporary storage.
- **5-14** *(file 07)* Make the following changes to the basic computer. 1. Add a register CTR (count register) to the bus system, selected with S₂S₁S₀ = 000. 2. Replace the ISZ instruction with `LDC Address: CTR ← M[Address]`. 3. Add a register-reference instruction ICSZ: increment CTR and skip next instruction if zero. Discuss the advantage of this change.
- **5-15** *(file 07)* The memory unit of the basic computer is to be changed to a 65,536 × 16 memory, requiring a 16-bit address. The memory-reference instruction format stays the same for I = 1, with the address part in positions 0–11. But when I = 0, the address is given by the 16 bits in the next word following the instruction. Modify the microoperations during T₂, T₃ (and T₄ if necessary) to conform with this configuration.
- **5-16** *(file 07)* `[A2 Q8]` — he dropped parts (a) and (b), the two block diagrams.
- **5-17** *(file 07)* A digital computer has a memory unit with a capacity of 16,384 words, 40 bits per word. The instruction code format consists of six bits for the operation part and 14 bits for the address part (no indirect mode bit). Two instructions are packed in one memory word, and a 40-bit instruction register IR is available in the control unit. Formulate a procedure for fetching and executing instructions for this computer. — **not asked yet; the packed-instruction variant**
- **5-18** *(file 07)* An output program resides in memory starting from address 2300. It is executed after the computer recognizes an interrupt when FGO becomes 1 (while IEN = 1). a. What instruction must be placed at address 1? b. What must be the last two instructions of the output program? — **the interrupt cycle**
- **5-19** *(file 08)* The register transfer statements for a register R and the memory in a computer are as follows (the X's are control functions that occur at random): `X₁X₂′: R ← M[AR]` (read memory word into R) · `X₁′X₂: R ← AC` (transfer AC to R) · `X₁X₃: M[AR] ← R` (write R to memory). Draw the hardware implementation of R and the memory in block diagram form. Show how the control functions select the load control input of R, the select inputs of the multiplexers you include, and the read and write inputs of the memory. — *(subscripts partly OCR-damaged; the structure is what matters)*
- **5-20** *(file 08)* `[A2 Q9]`
- **5-21** *(file 08)* `[A2 Q10]` — verbatim.
- **5-22** *(file 08)* Derive the control gates for the write input of the memory in the basic computer. — **not asked yet; same method as A2 Q10**
- **5-23** *(file 08)* Show the complete logic of the interrupt flip-flop R in the basic computer. Use a JK flip-flop and minimize the number of gates.
- **5-24** *(file 08)* Derive the Boolean logic expression for x₁ (see Table 5-7). Show that x₁ can be generated with one AND gate and one OR gate.
- **5-25** *(file 08)* Derive the Boolean expression for the gate structure that clears the sequence counter SC to 0. Draw the logic diagram of the gates and show how the output is connected to the INR and CLR inputs of SC (see Fig. 5-6). Minimize the number of gates.

## Chapter 7 — Microprogrammed Control → file 09 (U3)

**Neither assignment touches U3.** This chapter is the *only* question evidence that exists for it.
The MTE covers U3 (lectures L12–L15, before the mid-term divider), so do not skip it.

- **7-1** What is the difference between a microprocessor and a microprogram? Is it possible to design a microprocessor without a microprogram? Are all microprogrammed computers also microprocessors?
- **7-2** Explain the difference between hardwired control and microprogrammed control. Is it possible to have a hardwired control associated with a control memory?
- **7-3** Define the following: (a) microoperation; (b) microinstruction; (c) microprogram; (d) microcode.
- **7-4** The microprogrammed control organization shown in Fig. 7-1 has the following propagation delay times: 40 ns to generate the next address, 10 ns to transfer the address into the control address register, 40 ns to access the control memory ROM, 10 ns to transfer the microinstruction into the control data register, and 40 ns to perform the required microoperations specified by the control word. What is the maximum clock frequency that the control can use? What would the clock frequency be if the control data register is not used? — **a numerical; the only one in the chapter**
- **7-5** The system shown in Fig. 7-2 uses a control memory of 1024 words of 32 bits each. The microinstruction has three fields; the microoperations field has 16 bits. a. How many bits are there in the branch address field and the select field? b. If there are 16 status bits in the system, how many bits of the branch logic are used to select a status bit? c. How many bits are left to select an input for the multiplexers?
- **7-6** The control memory in Fig. 7-2 has 4096 words of 24 bits each. a. How many bits are there in the control address register? b. How many bits are there in each of the four inputs going into the multiplexers? c. What are the number of inputs in each multiplexer and how many multiplexers are needed?
- **7-7** Using the mapping procedure described in Fig. 7-3, give the first microinstruction address for the following operation code: (a) 0010; (b) 1011; (c) 1111. — **the `0xxxx00` mapping; near-certain exam item**
- **7-8** Formulate a mapping procedure that provides eight consecutive microinstructions for each routine. The operation code has six bits and the control memory has 2048 words.
- **7-9** Explain how the mapping from an instruction code to a microinstruction address can be done by means of a read-only memory. What is the advantage of this method compared to the one in Fig. 7-3?
- **7-10** Why do we need the two multiplexers in the computer hardware configuration shown in Fig. 7-4? Is there another way that information from multiple sources can be transferred to a common destination?
- **7-11** Using Table 7-1, give the 9-bit microoperation field for the following microoperations: a. `AC ← AC + 1, DR ← DR + 1` b. `PC ← PC + 1, DR ← M[AR]` c. `DR ← AC, AC ← DR`
- **7-12** Using Table 7-1, convert the following symbolic microoperations to register transfer statements and to binary. a. READ, INCPC b. ACTDR, DRTAC c. ARTPC, DRTAC, WRITE
- **7-13** Suppose that we change the ADD routine listed in Table 7-2 to the following two microinstructions: `ADD: READ I CALL INDR2` / `ADD U JMP FETCH`. What should subroutine INDR2 be?
- **7-14** The following is a symbolic microprogram for an instruction in the computer defined in Sec. 7-3: `ORG 40` / `NOP S JMP FETCH` / `NOP Z JMP FETCH` / `NOP I CALL INDRCT` / `ARTPC U JMP FETCH`. a. Specify the operation performed when the instruction is executed. b. Convert the four microinstructions into their equivalent binary form.
- **7-15** The computer of Sec. 7-3 has a given binary microprogram at addresses 60–63. a. Translate it to a symbolic microprogram as in Table 7-2 (FETCH is at address 64 and INDRCT at 67). b. List all the things that will be wrong when this microprogram is executed. — *the four binary words are OCR-destroyed; read them from the book.*
- **7-16** Add the instructions AND, SUB, ADM, BTCL, BZ, SEQ, BPNZ (opcodes 0100–1010, definitions in the book's table) to the computer of Sec. 7-3. Write the symbolic microprogram for each routine as in Table 7-2. (AC must not change unless the instruction specifies a change in AC.)
- **7-17** Write a symbolic microprogram routine for the ISZ (increment and skip if zero) instruction defined in Chap. 5 (Table 5-4). Use the microinstruction format of Sec. 7-3. Note that the DR = 0 status condition is not available in the CD field — you can exchange AC and DR and check if AC = 0 with the Z bit.
- **7-18** Write the symbolic microprogram routine for the BSA (branch and save address) instruction defined in Chap. 5 (Table 5-4). Minimize the number of microinstructions.
- **7-19** Show how outputs 5 and 6 of decoder F3 in Fig. 7-7 are to be connected to the program counter PC.
- **7-20** Show how a 9-bit microoperation field in a microinstruction can be divided into subfields to specify 46 microoperations. How many microoperations can be specified in one microinstruction?
- **7-21** A computer has 16 registers, an ALU with 32 operations, and a shifter with eight operations, all connected to a common bus system. a. Formulate a control word for a microoperation. b. Specify the number of bits in each field of the control word and give a general encoding scheme. c. Show the bits of the control word that specify the microoperation `R4 ← R5 + R6`. — **the control-word-sizing form; high exam likelihood**
- **7-22** Assume that the input logic of the microprogram sequencer of Fig. 7-8 has four inputs I₂, I₁, I₀, T (test) and three outputs S₁, S₀, L, performing the operations in the book's table. Design the input logic circuit using a minimum number of gates.
- **7-23** Design a 7-bit combinational circuit incrementer for the microprogram sequencer of Fig. 7-8 (see Fig. 4-8). Modify the incrementer by including a control input D: when D = 0 the circuit increments by one, when D = 1 by two.
- **7-24** Insert an exclusive-OR gate between MUX 2 and the input logic of Fig. 7-8. One input to the gate comes from the test output of the multiplexer; the other from a polarity bit P in the microinstruction. Explain the effect.

## Chapter 8 — Central Processing Unit (program control + status bits) → file 10 (U3)

U3's *program control and status bits* half. Only the in-scope items are listed.

- **8-20** Perform the logic AND, OR, and XOR with the two binary strings 10011100 and 10101010.
- **8-21** Given the 16-bit value 1001101011001101. What operation must be performed in order to: a. clear to 0 the first eight bits? b. set to 1 the last eight bits? c. complement the middle eight bits?
- **8-22** An 8-bit register contains the value 01111011 and the carry bit is equal to 1. Perform the eight shift operations given in Table 8-9. Each time, start from the initial value given above.
- **8-23** Represent the following signed numbers in binary using eight bits: +83; −83; +68; −68. a. Perform (−83) + (+68) and interpret the result. b. Perform (−68) − (+83) and indicate if there is an overflow. c. Shift binary −68 once to the right and give the shifted value in decimal. d. Shift binary −83 once to the left and indicate if there is an overflow.
- **8-24** Show that the circuit labeled "check for zero output" in Fig. 8-8 is an 8-bit NOR gate.
- **8-25** An 8-bit computer has a register R. Determine the values of status bits C, S, Z, and V after each of the following instructions. The initial value of R in each case is hexadecimal 72; the numbers below are also hexadecimal. a. Add immediate operand C6 to R. b. Add immediate operand 1E to R. c. Subtract immediate operand 9A from R. d. AND immediate operand 8D to R. e. Exclusive-OR R with R. — **the status-bit drill; near-certain exam item**
- **8-26** Two unsigned numbers A and B are compared by subtracting A − B. The carry status bit is treated as a borrow, so C = 1 if A < B. Show that the relative magnitude of A and B can be determined from inspection of status bits C and Z: A > B ⟺ C = 0 and Z = 0 · A ≥ B ⟺ C = 0 · A < B ⟺ C = 1 · A ≤ B ⟺ C = 1 or Z = 1 · A = B ⟺ Z = 1 · A ≠ B ⟺ Z = 0.
- **8-27** Two signed numbers A and B in signed-2's complement form are compared by subtracting A − B. Show that the relative magnitude can be determined from the status bits: A > B ⟺ (S ⊕ V) = 0 and Z = 0 · A ≥ B ⟺ (S ⊕ V) = 0 · A < B ⟺ (S ⊕ V) = 1 · A ≤ B ⟺ (S ⊕ V) = 1 or Z = 1 · A = B ⟺ Z = 1 · A ≠ B ⟺ Z = 0. — **why signed comparison uses S ⊕ V, not C**
- **8-28** Design a digital circuit with four inputs C, S, Z, V and 10 outputs, one for each of the branch conditions in Problems 8-26 and 8-27. Draw the logic diagram using two OR gates, one XOR gate, and five inverters.
- **8-29** Consider the two 8-bit numbers A = 01000001 and B = 10000100. a. Give the decimal equivalent of each assuming (1) unsigned and (2) signed. b. Add them and interpret the sum under both assumptions. c. Determine the values of C, Z, S, V after the addition. d. List the conditional branch instructions from Table 8-11 that will have a true condition.
- **8-30** The program compares two unsigned numbers A and B by A − B and updating the status bits. A = 01000001, B = 10000100. a. Evaluate the difference and interpret the binary result. b. Determine C (borrow) and Z. c. List the conditional branch instructions from Table 8-11 that will have a true condition.
- **8-31** As 8-30, but A and B are **signed**.

## Chapter 9 — Pipeline and Vector Processing → file 11 (U4)

**He copies this chapter too.** Five of its 20 problems are Assignment 2 Q11–Q15.

- **9-1** *(file 11)* `[A2 Q11]`
- **9-2** *(file 11)* Draw a space-time diagram for a six-segment pipeline showing the time it takes to process eight tasks. — **not asked yet; the diagram behind A2 Q12's formula**
- **9-3** *(file 11)* `[A2 Q12]` — verbatim.
- **9-4** *(file 11)* A nonpipeline system takes 50 ns to process a task. The same task can be processed in a six-segment pipeline with a clock cycle of 10 ns. Determine the speedup ratio of the pipeline for 100 tasks. What is the maximum speedup that can be achieved? — **not asked yet; the cleanest speedup numerical in the book**
- **9-5** *(file 11)* `[A2 Q13]`
- **9-6** *(file 11)* It is necessary to design a pipeline for a fixed-point multiplier that multiplies two 8-bit binary integers. Each segment consists of a number of AND gates and a binary adder similar to an array multiplier (Fig. 10-10). a. How many AND gates are there in each segment, and what size of adder is needed? b. How many segments are there in the pipeline? c. If the propagation delay in each segment is 30 ns, what is the average time to multiply two fixed-point numbers in the pipeline?
- **9-7** *(file 11)* The time delays of the four segments in the pipeline of Fig. 9-6 are t₁ = 50 ns, t₂ = 30 ns, t₃ = 95 ns, t₄ = 45 ns. The interface register delay tᵣ = 5 ns. a. How long would it take to add 100 pairs of numbers in the pipeline? b. How can we reduce the total time to about one-half of the time calculated in part (a)? — **the unequal-segment case; the bottleneck segment sets the clock**
- **9-8** *(file 11)* How would you use the floating-point pipeline adder of Fig. 9-6 to add 100 floating-point numbers X₁ + X₂ + X₃ + ⋯ + X₁₀₀?
- **9-9** *(file 11)* Formulate a six-segment instruction pipeline for a computer. Specify the operations to be performed in each segment. — **not asked yet; the FI-DA-FO-EX four-segment version is what the deck teaches**
- **9-10** *(file 11)* `[A2 Q14]` — verbatim.
- **9-11** *(file 11)* `[A2 Q15]`
- **9-12** *(file 11)* Give an example of a program that will cause data conflict in the three-segment pipeline of Sec. 9-5.
- **9-13** *(file 11)* Give an example that uses delayed load with the three-segment pipeline of Sec. 9-5.
- **9-14** *(file 11)* Give an example of a program that will cause a branch penalty in the three-segment pipeline of Sec. 9-5.
- **9-15** *(file 11)* Give an example that uses delayed branch with the three-segment pipeline of Sec. 9-5.
- **9-16** *(file 11)* Consider the multiplication of two 40 × 40 matrices using a vector processor. a. How many product terms are there in each inner product, and how many inner products must be evaluated? b. How many multiply-add operations are needed to calculate the product matrix?
- **9-17** *(file 11)* How many clock cycles does it take to process an inner product in the pipeline of Fig. 9-12 when used to evaluate the product of two 60 × 60 matrices? How many inner products are there, and how many clock cycles does it take to evaluate the product matrix?
- **9-18** *(file 11)* Assign addresses to an array of data of 1024 words to be stored in the memory described in Fig. 9-13.
- **9-19** *(file 11)* A weather forecasting computation requires 250 billion floating-point operations. The problem is processed in a supercomputer that can perform 100 megaflops. How long will it take to do these calculations?
- **9-20** *(file 11)* Consider a computer with four floating-point pipeline processors, each using a cycle time of 40 ns. How long will it take to perform 400 floating-point operations? Is there a difference if the same 400 operations are carried out using a single pipeline processor with a cycle time of 10 ns?

---

## Sourcing

**P1 — the assignments.** Text extracted with `pypdf` from `exam-pack/ASSIGNMENT-A1-ECE2108-2026-08.pdf`
and `ASSIGNMENT-A2-ECE2108-2026-09.pdf`. Tier 0, first-party. `settled`.

**P2 — Mano.** M. Morris Mano, *Computer System Architecture*, 3rd ed., Pearson. Transcribed
`[2026-09-23]` from the **archive.org** item `computer-system-architecture-morris-mano-third-edition`
(OCR full text, 1.1 MB, complete). This **closes the limitation opened 2026-09-12** — until now the book
could not be obtained and every Mano fact rested on institutional reproductions. Verified as the right
book by matching problem 5-1 word-for-word against Assignment 2 Q1.

**OCR caveat.** The source is scanned text. Mathematical subscripts, primes and figure values are the
parts OCR damages, and a few are damaged here — each one is **marked in place**, never guessed at.
Where a problem is also an assignment question, the assignment PDF's clean text is used instead.
**Before trusting any number in a P2 item, check it against the figure or table in the book.**

**Confidence.** Problem *statements*: `settled`. The **A2 → Mano map**: `settled` — cross-anchored on
5-9 and 5-12, which were independently verified against the solutions manual on 2026-09-15, with the
rest following from statement text. The **A1 → Mano map**: `settled` for Q10, Q12, Q14, Q16, Q18, Q19
(identical data or identical wording); Q11 is `likely` (same form as 4-3, different registers).
