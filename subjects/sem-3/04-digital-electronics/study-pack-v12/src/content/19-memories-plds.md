# 19 — Memories and programmable logic

<div class="sub">Memories: syllabus Unit 5 item with no deck slides (built from the KB) · deck 15 (slides 2–37: PLDs, ROM/PROM, PAL, PLA) · 14 worked slides (EX 15.20–15.37) · needs 06 step 1 (decoder: one output per input code), 02 (minimal SOP from a K-map), 09 step 1 (the latch) and 18 step 11 (chip select, tristate)</div>

## Map

[[map:1 Memory organisation > 2 SRAM and DRAM > 3 ROM types > 4 Bigger memories > 5 The AND–OR array > 6 ROM as a table > 7 PROM logic > 8 Reading a PAL > 9 PAL design > 10 PLA and output XOR > 11 PLA design > 12 PROM, PAL, PLA compared|here=1]]

Files 01–08 built each function from its own gates. This file buys logic in bulk, two ways. A **memory** stores a table: give it an address, it returns the word stored there (steps 1–4). A **programmable logic device (PLD)** is a ready-made AND array feeding an OR array, with the connections left for you to make: the two-level SOP circuits of file 02, made programmable (steps 5–12). The two meet in step 6: a ROM *is* a PLD whose AND array is a decoder.

## Symbols

| Symbol | What it means in this file |
|---|---|
| 2^{k} × m | a memory of 2^{k} words, each m bits wide (1K × 8: 1024 words of 8 bits) |
| k, m | number of address lines; number of data lines |
| K | 2^{10} = 1024 (so 4K = 4096, 64K = 65 536) |
| CS | chip select: the chip responds only when CS is active |
| N, M | inputs and outputs of a ROM or PLD |
| D_{i} (= m_{i}) | decoder output i: the minterm whose binary number is i |
| × on a line crossing | a connection (intact fuse); no × = no connection |
| product term | the output of one AND gate in the AND array |
| T, C | in a PLA table: the output is used true (T) or complemented (C) |

## Running example

Two parts, one thread each. **Memory:** the **1K × 8** chip; steps 1–4 count its lines, open its cells and build a 4K × 8 memory from four of them. **Logic:** one pair of functions from deck 15 slide 31,

$$F_{1}(A,B,C) = \Sigma(0,1,2,4) \qquad F_{2}(A,B,C) = \Sigma(0,5,6,7)$$

placed in a PROM (step 7), a PAL (step 9) and a PLA (step 11), so step 12 can compare what each device costs for the same job.

## The questions this file answers

- <span class="tag">practice</span> A 1K × 8 memory: how many address and data lines? Differentiate SRAM and DRAM. Build 4K × 8 from 1K × 8 chips. (No deck covers memories; steps 1–4 use Predict prompts.)
- <span class="tag">Deck 15 slides 20–21</span> An 8 × 4 ROM: read a word; write F_{3}…F_{0} in terms of the inputs.
- <span class="tag">Deck 15 slide 22</span> Implement a 3-input, 2-output truth table with a PROM.
- <span class="tag">Deck 15 slide 24</span> Read the equations F_{1}…F_{4} off a PAL with feedback.
- <span class="tag">Deck 15 slides 25–27</span> Fit four 4-variable functions into a PAL with three product terms per output.
- <span class="tag">Deck 15 slides 31–34, 36</span> Implement two functions with a PLA; read a PLA.
- <span class="tag">Deck 15 slide 37</span> Implement three functions with a PROM, a PAL and a PLA.

---

## Build

### 1 · Memory organisation: address lines and data lines

A decoder (file 06) turns an n-bit code into one active line out of 2^{n}. A memory puts one stored word behind each of those lines.

:::guess Predict
A memory holds 1024 words of 8 bits. To pick one word you send its number in binary. How many bits must that number have, and how many wires carry the word out?
:::

:::note Terms
**Cell:** stores one bit. **Word:** the bits read or written together, one per data line. **Address:** the binary number of a word; it arrives on the **address lines**. **Capacity:** words × bits per word. **RAM (random-access memory):** can be read and written; **volatile**, it loses its contents without power. **ROM (read-only memory):** keeps its contents without power (**non-volatile**).
:::

[[fig:memory_org|A 2^k × m memory: the k address lines enter a decoder, which activates one word line; the m cells of that word connect to the m data lines. Chip select and read/write enter the control block.|w=60]]

A **2^{k} × m** memory has **k address lines** (k bits choose one of 2^{k} words) and **m data lines** (one per bit of the word). Its capacity is 2^{k} · m bits. Two control inputs complete the chip: **CS** (chip select) and **R/W** (read or write). When CS is inactive the data outputs go to the high-impedance state of file 18 step 11, so several chips can share one data bus.

For the running example, 1K = 1024 = 2^{10}:

1. Address lines: 10, because 2^{10} = 1024.
2. Data lines: 8, the word width.
3. Capacity: 1024 × 8 = 8192 bits.

**Answer to the Predict.** **10 address bits** (2^{10} = 1024) and **8 data lines**: 8192 bits in all.

:::check Check 1
(a) A 16K × 4 memory: address lines, data lines, total bits? (b) A chip has 12 address lines and 16 data lines. Write its size as words × bits, and give its capacity in bytes.
:::

### 2 · SRAM and DRAM: two ways to hold a bit

Step 1 treated a cell as a box. RAM cells come in two kinds, and which kind sets a memory's speed, cost and use.

:::guess Predict
File 09's latch holds a bit as long as power is on. A capacitor can also hold a bit, as charge. Which cell is smaller, and what goes wrong with the capacitor over time?
:::

:::note Terms
**SRAM (static RAM):** the cell is a latch, two cross-coupled inverters, plus two access transistors: **6 transistors**. **DRAM (dynamic RAM):** the cell is **1 transistor + 1 capacitor**; the bit is the charge on the capacitor. **Refresh:** reading every DRAM row and writing it back, again and again, before the charge leaks away.
:::

<div class="two">

[[fig:sram_cell|6-transistor SRAM cell: two cross-coupled inverters (the latch) and two access transistors to the bit lines (Wikimedia Commons, public domain).]]

[[fig:dram_cell|1-transistor DRAM cell: the word line opens the transistor; the capacitor's charge is the bit.]]

</div>

| | SRAM | DRAM |
|---|---|---|
| cell | 6 transistors: a latch (file 09) + 2 access | 1 transistor + 1 capacitor |
| bit stored as | which way the latch sits | charge on the capacitor |
| refresh | not needed: the latch restores itself while powered | needed: the charge leaks |
| a read | leaves the bit in place | shares the tiny charge with the bit line, so the bit is lost and must be written back |
| speed, density, cost per bit | faster, fewer bits per chip, dearer | slower, more bits per chip, cheaper |
| used for | cache | main memory |

Both are volatile: switch off and the bit is gone.

**Answer to the Predict.** The **capacitor cell (DRAM)** is smaller: 1 transistor against 6. Its charge **leaks away**, so every cell must be refreshed periodically, and a read disturbs the charge and needs a write-back.

:::check Check 2
(a) Why does DRAM need refreshing and SRAM not? (b) A design needs the fastest possible small memory beside a processor. SRAM or DRAM, and why?
:::

### 3 · ROM types: written once, or erased and rewritten

Step 2's RAMs forget at power-off. Program code that must survive power-off goes in a ROM; the types differ in who writes it and whether it can be changed.

:::guess Predict
A toy sells a million copies with the same program. A student board is reprogrammed fifty times a day. Should both use the same kind of ROM?
:::

:::note Terms
**Mask ROM:** contents fixed by the chip maker in the last manufacturing step. **PROM (programmable ROM):** written once by the user, by blowing fuses. **EPROM (erasable PROM):** erased by ultraviolet light through a window, the whole chip at once, then rewritten in a programmer. **EEPROM (electrically erasable PROM):** erased and rewritten electrically, in the circuit. **Flash:** an EEPROM that erases a block at a time.
:::

| Type | Written by | Can be erased? |
|---|---|---|
| mask ROM | the maker, at manufacture | never |
| PROM | the user, once (fuses blown) | never |
| EPROM | the user, in a programmer | yes: UV light, whole chip |
| EEPROM | the user, in circuit | yes: electrically |
| Flash | the user, in circuit | yes: electrically, a block at a time |

EPROM, EEPROM and Flash store a bit as charge trapped on an insulated (floating) gate of a MOSFET, which shifts the voltage at which the transistor turns on; the charge stays for years without power. "Read-only" is therefore loose: all but mask ROM and PROM can be rewritten, just slowly and in special ways.

**Answer to the Predict.** **No.** The toy uses a **mask ROM**: the contents never change and the maker writes them cheapest in bulk. The student board needs an **electrically erasable** part (**Flash** or EEPROM) that is rewritten in the circuit.

:::check Check 3
(a) Which ROM types can be rewritten without taking the chip out of the board? (b) What does a PROM do to store a bit, and why can it be written only once?
:::

### 4 · Building bigger memories

Step 1's chip is 1K × 8. A system needs more words, or wider words, than one chip gives.

:::guess Predict
Four 1K × 8 chips must make one 4K × 8 memory. A 4K address has 12 bits; each chip uses only 10 of them. What should the other 2 bits do?
:::

:::note Terms
**Depth expansion:** more words. Chips share the address and data lines; extra address bits choose which chip answers. **Width expansion:** wider words. Chips sit side by side with the same address and CS; each supplies part of the word.
:::

[[fig:mem_decode|A 4K × 8 memory from four 1K × 8 chips: A9–A0 go to every chip; A11 A10 drive a 2-to-4 decoder whose outputs are the four chip selects.|w=65]]

Depth: 4096/1024 = **4 chips**, 12 address lines. The low bits **A_{9}–A_{0}** go to every chip and pick a word inside it. The top bits **A_{11}A_{10}** go to a **2-to-4 decoder** (file 06) whose four outputs drive the four CS inputs, so exactly one chip is enabled and the others' outputs sit in Hi-Z on the shared data bus.

| A_{11} A_{10} | chip enabled | addresses (decimal) | addresses (hex) |
|---|---|---|---|
| 0 0 | 0 | 0–1023 | 000–3FF |
| 0 1 | 1 | 1024–2047 | 400–7FF |
| 1 0 | 2 | 2048–3071 | 800–BFF |
| 1 1 | 3 | 3072–4095 | C00–FFF |

Width: a 1K × 16 memory is **two** 1K × 8 chips side by side: the same A_{9}–A_{0} and the same CS go to both; one gives data bits 0–7, the other bits 8–15. No decoder is needed, because both chips answer every address.

**Answer to the Predict.** The 2 top bits **choose the chip**: they enter a 2-to-4 decoder whose outputs are the four chip selects.

:::check Check 4
(a) How many 16K × 4 chips make a 64K × 8 memory? How many address lines, and which ones go to the decoder? (b) Build 2K × 16 from 2K × 8 chips: how many, and is a decoder needed?
:::

### 5 · The AND–OR array: what every PLD is made of

Steps 1–4 stored data. Deck 15 turns to logic: a board of separate gate chips needs many parts and much wiring (slides 2–3); one programmable chip can replace them (slide 5).

:::guess Predict
Every SOP expression is a layer of AND gates feeding a layer of OR gates (file 02). A chip maker wants one part that can become *any* SOP circuit after it is made. What should the part contain, and what should the user be allowed to change?
:::

:::note Terms
**PLD (programmable logic device):** an array of AND gates feeding an array of OR gates, with programmable connections (deck 15 slide 6). **Buffer/inverter:** gives each input in true and complemented form, x and x' (slide 11). **Product line:** one AND gate's output. **Fuse:** a connection that is made at manufacture and can be blown open (slide 12): an AND gate with inputs a, b, c, d whose fuses a and d are blown gives bc. **PLD notation:** a gate's inputs are drawn as **one line**; a **×** where it crosses an input line means that input is connected (slides 13–15).
:::

[[fig:u5_pld_types|The three classic PLDs as two arrays. Coloured blocks are programmable, grey are fixed. PROM: fixed AND (a decoder), programmable OR. PAL: programmable AND, fixed OR. PLA: both programmable.|w=70]]

The general structure (slide 16): n inputs → n buffer/inverters (2n lines) → AND array (p product lines) → OR array (m outputs). Which array the user may program gives the three classic types (slide 17), built in steps 6–11:

| Device | AND array | OR array |
|---|---|---|
| PROM | fixed: a decoder making all 2^{n} minterms | programmable |
| PAL (programmable array logic) | programmable | fixed |
| PLA (programmable logic array) | programmable | programmable |

These are **simple PLDs (SPLDs)**. Deck 15 slides 7–9 name two larger kinds: the **CPLD**, several PAL-like blocks with programmable wiring between them, and the **FPGA**, an array of logic blocks built round small look-up tables (each a tiny ROM, step 6) with programmable wiring.

**Answer to the Predict.** An **AND array feeding an OR array**, with the inputs available true and complemented, and **programmable connections** into the arrays. Which connections are programmable decides the device type.

:::check Check 5
(a) In PLD notation, one AND gate's input line has × marks at A and B' only. What does the gate output? (b) Which array is fixed in a PAL, and which in a PROM?
:::

### 6 · A ROM is a stored truth table

Step 5 said a PROM's AND array is a decoder. A decoder makes every minterm; so a ROM can hold any function at all.

:::q <span class="tag">Deck 15 slides 20–21</span>
An 8 × 4 ROM (3 inputs A_{2}A_{1}A_{0}, 4 outputs F_{3}…F_{0}) is programmed as in the figure. For input (A_{2}, A_{1}, A_{0}) = 011, what is the output? What are F_{3}, F_{2}, F_{1} and F_{0} in terms of A_{2}, A_{1}, A_{0}?
:::

:::guess Guess first
Input 011 activates one decoder line. Which one, and which outputs does it reach?
:::

:::note Terms
**N × M ROM** here means 2^{N} words × M bits: N inputs (address lines), M outputs (data lines). The decoder's line D_{i} is the minterm m_{i}. An **×** joins D_{i} to an output's OR line: that output is 1 when the input is i.
:::

[[fig:u5_rom8x4|The 8 × 4 ROM of deck 15 slide 20. A 3-to-8 decoder makes D0–D7; each vertical OR line collects the decoder lines marked ×. F3: D2, D5, D7. F2: D0, D7. F1: D1, D4. F0: D1, D5, D7.|w=66]]

A ROM program is "simply a multiple-output truth table" (slide 19): a 1 in output F's column for input i means an × joining D_{i} to F; a 0 means no ×. To read a word, find the one active line and read across it:

| Input A_{2}A_{1}A_{0} | Active line | F_{3}F_{2}F_{1}F_{0} |
|---|---|---|
| 001 | D_{1} | 0 0 1 1 |
| 011 | D_{3} | 0 0 0 0 (no × on D_{3}) |
| 101 | D_{5} | 1 0 0 1 |
| 111 | D_{7} | 1 1 0 1 |

Each output is the OR of its marked minterms, then simplified (file 02):

1. F_{3} = D_{2} + D_{5} + D_{7} = A_{2}'A_{1}A_{0}' + A_{2}A_{0} (D_{5} and D_{7} differ only in A_{1}).
2. F_{2} = D_{0} + D_{7} = A_{2}'A_{1}'A_{0}' + A_{2}A_{1}A_{0}.
3. F_{1} = D_{1} + D_{4} = A_{2}'A_{1}'A_{0} + A_{2}A_{1}'A_{0}'.
4. F_{0} = D_{1} + D_{5} + D_{7} = A_{1}'A_{0} + A_{2}A_{0} (D_{1}, D_{5} pair on A_{1}'A_{0}; D_{5}, D_{7} on A_{2}A_{0}).

The ROM never needs these simplified forms: it holds every minterm anyway. They only name what is stored.

:::note Slide slips
Slide 21 says input 011 gives output 0011. D_{3} carries no × in the slide's own array, so 011 gives **0000**; the word **0011** belongs to input **001** (D_{1} reaches F_{1} and F_{0}).
:::

**Answer to the question.** Input 011 activates D_{3}, which has no connections: output **0000** (the slide's 0011 is the word at 001). F_{3} = A_{2}A_{0} + A_{2}'A_{1}A_{0}', F_{2} = A_{2}A_{1}A_{0} + A_{2}'A_{1}'A_{0}', F_{1} = A_{2}A_{1}'A_{0}' + A_{2}'A_{1}'A_{0}, F_{0} = A_{2}A_{0} + A_{1}'A_{0}.

:::check Check 6
(a) What word does the ROM give for input 100? (b) Which decoder lines would you mark to add a fifth output equal to A_{2} (1 whenever A_{2} = 1)?
:::

### 7 · Logic design with a PROM

Step 6 read a programmed ROM. Designing with one is the same step backwards: write the truth table, and mark an × for every 1.

:::q <span class="tag">Deck 15 slide 22</span>
Implement with a PROM the functions of this truth table: f_{1} is 1 for x_{2}x_{1}x_{0} = 000, 001, 010, 101, 111; f_{2} is 1 for 001, 010, 100, 110.
:::

:::guess Guess first
Do you need a K-map before you can program the PROM?
:::

:::note Terms
**PROM size:** N inputs and M outputs need a **2^{N} × M** PROM: every one of the 2^{N} minterms has a line, whether used or not.
:::

The procedure has no minimising step:

1. Number the rows: f_{1} = Σm(0, 1, 2, 5, 7), f_{2} = Σm(1, 2, 4, 6).
2. Pick the size: 3 inputs, 2 outputs → an **8 × 2 PROM**.
3. On f_{1}'s OR line, put × on m_{0}, m_{1}, m_{2}, m_{5}, m_{7}; on f_{2}'s, × on m_{1}, m_{2}, m_{4}, m_{6}.

That is the whole design. It is also the PROM's weakness: each extra input doubles the number of minterm lines (2^{N}), used or not.

**Running example.** F_{1} = Σ(0, 1, 2, 4) and F_{2} = Σ(0, 5, 6, 7) go into an 8 × 2 PROM the same way: × on m_{0}, m_{1}, m_{2}, m_{4} for F_{1}; × on m_{0}, m_{5}, m_{6}, m_{7} for F_{2}. All 8 minterm lines are built; 7 are used.

**Answer to the question.** An **8 × 2 PROM**, × on **m_{0}, m_{1}, m_{2}, m_{5}, m_{7}** for f_{1} and on **m_{1}, m_{2}, m_{4}, m_{6}** for f_{2}. **No K-map is needed**: the PROM stores the truth table as it is.

:::check Check 7
(a) What size PROM holds 4-input, 3-output logic? (b) A BCD-to-7-segment decoder (file 07) has 4 inputs and 7 outputs. What size PROM replaces it, and how many of its words are never used?
:::

### 8 · The PAL: programmable ANDs, fixed ORs

Step 7's PROM builds every minterm. A PAL turns this round (slide 23): you program the AND gates to make just the product terms you need, and each OR gate takes a fixed group of them.

:::q <span class="tag">Deck 15 slide 24</span>
A 4-input PAL has fixed 3-input OR gates and feeds output F_{1} back into the AND array. Its product lines are programmed as: F_{1}: C', A'B' (third line unused); F_{2}: A'BC', AC, AB'; F_{3}: AD, BD, F_{1}; F_{4}: AB, CD, F_{1}'. What are the equations for F_{1} through F_{4}?
:::

:::guess Guess first
An unused product line is an AND gate with every fuse left intact. What does an AND of A·A'·B·B'·… give?
:::

:::note Terms
**Fixed OR:** each output's OR gate is wired to its own few product lines (here 3) at manufacture; a product line serves **one output only**. **Feedback:** an output brought back into the AND array as a new input (true and complemented), so another output can use it as one term.
:::

Each output is the OR of its three lines. An unused line keeps all its fuses: it ANDs every variable with its own complement, x·x' = 0, so it adds nothing to the OR.

1. F_{1} = C' + A'B' (third line = 0).
2. F_{2} = A'BC' + AC + AB'.
3. F_{3} = AD + BD + F_{1} = **AD + BD + C' + A'B'**: four terms, which a 3-input OR could not take directly; feedback makes room.
4. F_{4} = AB + CD + F_{1}'. With De Morgan (file 01), F_{1}' = (C' + A'B')' = C(A + B) = AC + BC, so F_{4} = **AB + CD + AC + BC**.

:::note Slide slips
Slide 24 calls this a "4-input, 3-output PAL"; the circuit and the equations have **four** outputs, F_{1}–F_{4}.
:::

**Answer to the question.** F_{1} = C' + A'B'; F_{2} = A'BC' + AC + AB'; F_{3} = AD + BD + F_{1} = AD + BD + C' + A'B'; F_{4} = AB + CD + F_{1}' = AB + CD + AC + BC.

:::check Check 8
(a) Why can F_{3} not be built from A, B, C, D alone in this PAL? (b) F_{2} and some other output both need the term AC. Can one product line serve both? Why?
:::

### 9 · PAL design: minimise, count terms, feed back

Step 8 read a PAL. To design one, every output must fit its fixed number of terms; file 02's minimisation is now compulsory.

:::q <span class="tag">Deck 15 slides 25–27</span>
Implement with a PAL whose OR gates take 3 product terms: w(A,B,C,D) = Σ(2, 12, 13), x = Σ(7, 8, 9, 10, 11, 12, 13, 14, 15), y = Σ(0, 2, 3, 4, 5, 6, 7, 8, 10, 11, 15), z = Σ(1, 2, 8, 12, 13).
:::

:::guess Guess first
z's minimal SOP needs four terms. Two of them are exactly w's two terms. What can you do?
:::

:::note Terms
**PAL programming table:** one row per product line; for each input a 1 (true), 0 (complemented) or – (not connected); the last column names the output the line feeds.
:::

1. Minimise each function (file 02): w = ABC' + A'B'CD'; x = A + BCD; y = A'B + CD + B'D'; z = ABC' + A'B'CD' + AC'D' + A'B'C'D.
2. Count terms: w 2, x 2, y 3 fit; **z needs 4**. Its minterms 1 and 2 have no neighbours in z, so no cover has fewer than 4.
3. z's first two terms are w. Feed w back: **z = w + AC'D' + A'B'C'D**, 3 terms.

| Line | A | B | C | D | w | Output |
|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 0 | – | – | w = ABC' |
| 2 | 0 | 0 | 1 | 0 | – | + A'B'CD' |
| 3 | – | – | – | – | – | (unused) |
| 4 | 1 | – | – | – | – | x = A |
| 5 | – | 1 | 1 | 1 | – | + BCD |
| 6 | – | – | – | – | – | (unused) |
| 7 | 0 | 1 | – | – | – | y = A'B |
| 8 | – | – | 1 | 1 | – | + CD |
| 9 | – | 0 | – | 0 | – | + B'D' |
| 10 | – | – | – | – | 1 | z = w |
| 11 | 1 | – | 0 | 0 | – | + AC'D' |
| 12 | 0 | 0 | 0 | 1 | – | + A'B'C'D |

[[fig:u5_pal|The fuse map of the table (deck 15 slide 27): × = connected. Lines 3 and 6 keep every fuse and give 0. Output w is fed back as the rails w and w', and line 10 takes w into z.|w=78]]

**Running example.** In the same 3-term PAL, F_{1} = A'B' + A'C' + B'C' and F_{2} = AB + AC + A'B'C' take 3 lines each: **6 product lines**. No line can serve both outputs.

**Answer to the question.** The table above: w = ABC' + A'B'CD', x = A + BCD, y = A'B + CD + B'D', and **z = w + AC'D' + A'B'C'D** with w fed back.

:::check Check 9
(a) Without feedback, how many lines would z need, and would it fit? (b) Why must you minimise before using a PAL, when a PROM never needs it?
:::

### 10 · The PLA: both arrays programmable, and an output XOR

Step 9's PAL could not share a product line between outputs. The PLA (slide 29) makes the OR array programmable too, so one product line can feed any number of outputs.

:::guess Predict
A PLA output passes through an XOR gate whose second input is a fuse to ground: intact gives 0, blown gives 1. What is f ⊕ 0? What is f ⊕ 1? What does that let the output do?
:::

:::note Terms
**PLA:** programmable AND array (any product terms) + programmable OR array (any output may take any product line). It has a **limited number of AND gates**, so the number of *distinct* product terms is what counts (slide 30). **Output polarity XOR:** each output passes through an XOR whose other input is programmed to 0 (true output) or 1 (complemented output) (slides 29, 35).
:::

[[fig:u5_pla|A 3-input PLA with 4 product lines (deck 15 slide 34). × marks connections in both arrays. OR 1 takes lines 1, 2, 3 and its XOR has the fuse blown (1): F1 = (AB + AC + BC)'. OR 2 takes lines 1, 2, 4, XOR input 0: F2 = AB + AC + A'B'C'. Lines 1 and 2 feed both outputs.|w=80]]

Since x ⊕ 0 = x and x ⊕ 1 = x', a PLA can produce either **f** or **f'** from the same OR gate. So each output may be built from the SOP of the function **or** the SOP of its complement, whichever shares more terms with the other outputs. Shared lines are drawn with × in both OR columns, as lines 1 and 2 in the figure.

Deck 15 slide 36 reads the same way: lines AB', AC, BC, A'BC'; one OR takes AB' + AC + A'BC' with its XOR at 0, giving F_{1} = AB' + AC + A'BC'; the other takes AC + BC with its XOR at 1, giving F_{2} = (AC + BC)'. Four lines in all, with AC shared.

**Answer to the Predict.** f ⊕ 0 = **f**, f ⊕ 1 = **f'**. One fuse chooses whether the output is the OR-sum or its **complement**.

:::check Check 10
(a) An OR gate's sum is 1 and its XOR fuse is blown. What is the output? (b) In slide 36's PLA, which product line is used by both outputs, and how many lines would a PAL have needed for the same two outputs?
:::

### 11 · PLA design: minimise both F and F', then share

Step 10 gave the PLA two freedoms: lines can be shared, and outputs can be complemented. Design means choosing, for each output, the form that shares most.

:::q <span class="tag">Deck 15 slides 31–34</span>
Implement the following two Boolean functions with a PLA: F_{1}(A, B, C) = Σ(0, 1, 2, 4), F_{2}(A, B, C) = Σ(0, 5, 6, 7).
:::

:::guess Guess first
F_{1} = A'B' + A'C' + B'C' and F_{2} = AB + AC + A'B'C' share no term. Before you accept 6 product lines, what else could you write for F_{1}?
:::

:::note Terms
**F'** (complement): 1 where F is 0; its minimal SOP comes from grouping F's **0s** on the K-map. **PLA programming table:** one row per product line: the inputs (1, 0, –), then for each output a 1 if the line goes into it; the last row marks each output T (true) or C (complemented) (slide 33).
:::

[[fig:v1arg8|What this graph plots: two 3-variable K-maps, rows A = 0, 1, columns BC in Gray order; each cell is one input row. Left, F1 with its 0s grouped: AB, AC, BC give F1'. Right, F2 with its 1s grouped: AB, AC, A'B'C'.|w=70]]

1. Minimise each function **and its complement** (slide 30):
   F_{1} = A'B' + A'C' + B'C' (1s grouped); F_{1}' = AB + AC + BC (0s grouped);
   F_{2} = AB + AC + A'B'C' (1s grouped).
2. Choose forms that share: F_{1}' and F_{2} both contain **AB** and **AC**.
3. Take F_{1} = (AB + AC + BC)', built as AB + AC + BC with its XOR at 1; F_{2} = AB + AC + A'B'C', XOR at 0.
4. Distinct lines: AB, AC, BC, A'B'C' = **4**. A search over every choice of terms and polarities (verify.py) finds no 3-line PLA for this pair.

| Product line | A | B | C | F_{1} | F_{2} |
|---|---|---|---|---|---|
| 1: AB | 1 | 1 | – | 1 | 1 |
| 2: AC | 1 | – | 1 | 1 | 1 |
| 3: BC | – | 1 | 1 | 1 | – |
| 4: A'B'C' | 0 | 0 | 0 | – | 1 |
| | | | | **C** | **T** |

The figure of step 10 is this table drawn out.

**Answer to the question.** F_{1} = **(AB + AC + BC)'** (complemented output), F_{2} = **AB + AC + A'B'C'** (true output): **4 product lines instead of 6**, with AB and AC shared, programmed as in the table.

:::check Check 11
(a) If both outputs were taken in true form, how many product lines would the PLA need? (b) What does the "C" under F_{1} tell the person programming the chip to do?
:::

### 12 · PROM, PAL and PLA compared

Steps 7, 9 and 11 put the same pair F_{1}, F_{2} into three devices. Deck 15 ends with one exercise for all three.

:::q <span class="tag">Deck 15 slide 37</span>
Implement the following Boolean functions with a PROM, PAL and PLA: F_{1}(A, B, C) = Σ(1, 2, 4, 6), F_{2}(A, B, C) = Σ(0, 1, 6, 7), F_{3}(A, B, C) = Σ(1, 2, 3, 5, 7).
:::

:::guess Guess first
Which of the three devices needs the most product lines for these functions, and which the fewest?
:::

**PROM.** 3 inputs, 3 outputs → **8 × 3**. × on m_{1}, m_{2}, m_{4}, m_{6} (F_{1}); m_{0}, m_{1}, m_{6}, m_{7} (F_{2}); m_{1}, m_{2}, m_{3}, m_{5}, m_{7} (F_{3}). All 8 minterm lines.

**PAL** (3 terms per output). Minimal SOPs (file 02): F_{1} = A'B'C + BC' + AC' (3 terms), F_{2} = A'B' + AB (2), F_{3} = C + A'B (2). Each fits: **7 product lines**, none shared.

**PLA.** The minimal forms share nothing, so taken as they are they need the same 7 lines. Look for shared terms, including in the complements:

1. Keep F_{1} = A'B'C + BC' + AC' (true).
2. F_{3}' = Σ(0, 4, 6) = **A'B'C'** + **AC'**; AC' is already a line of F_{1}. Take F_{3} complemented.
3. F_{2} = Σ(0, 1, 6, 7) can be written AB + **A'B'C** + **A'B'C'**: not minimal on its own, but A'B'C is F_{1}'s line and A'B'C' is F_{3}''s.
4. Distinct lines: A'B'C, BC', AC', AB, A'B'C' = **5**. The verify.py search finds no 4-line PLA.

| Line | A | B | C | F_{1} | F_{2} | F_{3} |
|---|---|---|---|---|---|---|
| 1: A'B'C | 0 | 0 | 1 | 1 | 1 | – |
| 2: BC' | – | 1 | 0 | 1 | – | – |
| 3: AC' | 1 | – | 0 | 1 | – | 1 |
| 4: AB | 1 | 1 | – | – | 1 | – |
| 5: A'B'C' | 0 | 0 | 0 | – | 1 | 1 |
| | | | | **T** | **T** | **C** |

Step 3 shows the PLA rule at work: sharing can beat minimising each output alone.

| | PROM | PAL | PLA |
|---|---|---|---|
| programmable | OR only | AND only | both |
| minimise first? | no (stores the truth table) | yes: each output must fit its terms | yes: minimise F and F', then share |
| share a product line? | (all minterms exist anyway) | no | yes |
| size grows with inputs | doubles per input (2^{N} lines) | with terms used | with distinct terms used |
| running example F_{1}, F_{2} | 8 minterm lines | 6 lines | 4 lines |
| slide 37's F_{1}, F_{2}, F_{3} | 8 minterm lines | 7 lines | 5 lines |
| speed (KB 05 §6) | — | fixed OR: fast | two programmable arrays: slowest |

**Answer to the question.** PROM: **8 × 3**, × on each function's minterms. PAL: F_{1} = A'B'C + BC' + AC', F_{2} = A'B' + AB, F_{3} = C + A'B, **7 lines**. PLA: the table, **5 lines**. The PROM builds the most lines (all 8 minterms, whether used or not), the PLA the fewest.

:::check Check 12
(a) Which device would you choose if the truth table changes every week and has 3 inputs, and why? (b) Why does a PAL with feedback (step 9) partly recover the PLA's advantage?
:::

---

## Exam form

**Memory (steps 1–4).**
1. 2^{k} × m: k address lines, m data lines, 2^{k} m bits. 1K = 2^{10}.
2. SRAM vs DRAM table: cell (6T latch vs 1T + 1C), refresh, read, speed, density, cost, use.
3. ROM types table: mask, PROM, EPROM (UV, whole chip), EEPROM, Flash (block).
4. Expansion sketch: low address bits to every chip, top bits to a decoder on the CS inputs (depth); chips side by side on one CS (width). Chips = (words needed / words per chip) × (bits needed / bits per chip).

**PLDs (steps 5–12).**
5. The PROM / PAL / PLA array table; PLD notation (× = connection).
6. ROM read: one decoder line, read the ×s across it; each output = OR of its marked minterms.
7. PROM design: 2^{N} × M, × on every 1 of the truth table, no minimising.
8. PAL: minimise, fit each output's fixed number of terms, feed an output back when it does not fit; the programming table (1, 0, –).
9. PLA: minimise F and F', pick the forms that share most; the table with the T/C row; output XOR at 1 complements.

## Traps

- Counting address lines from the bit count: 1K × 8 has 10 address lines (from 1024 words), not 13 (from 8192 bits).
- Using a decoder for width expansion: wider words need chips side by side on the **same** CS.
- Minimising before programming a PROM: not needed; it stores every minterm.
- Sharing a product line between two PAL outputs: the OR array is fixed, so each line feeds one output.
- Forgetting the T/C row (the output XOR) in a PLA table: F_{1} = (AB + AC + BC)' is wrong without it.
- In a PLA, minimising each output on its own and stopping: check the complements and non-minimal covers for shared terms.
- Copying deck 15 slide 21's "011 → 0011": the word at 011 is 0000.

## Self-test

1. How many address lines does an 8K × 8 memory have, and how many bits does it hold?
2. Build 32K × 8 from 8K × 8 chips: how many chips, and which address lines go to the decoder?
3. What size PROM is needed for 4 inputs and 2 outputs?
4. PLA for F(A, B, C) = Σ(1, 3, 5, 7) and G = Σ(3, 7): which product lines?
5. In the 8 × 4 ROM of step 6, what word is stored at address 111?
6. What size ROM stores the product of two 4-bit unsigned numbers?
7. Give two differences between SRAM and DRAM.
8. In a PAL with 3 terms per output, a function needs 4 terms and another output equals 2 of them. What do you do?

<!--ANSWERS-->

## Answers

**Check 1.** (a) 16K = 2^{14}: **14 address lines, 4 data lines**, 16 384 × 4 = **65 536 bits**. (b) 2^{12} = 4096 words: **4K × 16**; 65 536 bits = **8192 bytes** (8 KB).

**Check 2.** (a) A DRAM bit is charge on a tiny capacitor, which leaks; an SRAM bit is a latch that holds itself while powered. (b) **SRAM**: it is faster and needs no refresh; its lower density does not matter for a small memory (this is why caches are SRAM).

**Check 3.** (a) **EEPROM and Flash** (electrically erasable, in circuit). (b) It **blows fuses**; a blown fuse cannot be remade, so each bit can be changed only once.

**Check 4.** (a) Depth 64K/16K = 4, width 8/4 = 2: **8 chips**. 64K = 2^{16}: **16 address lines**; A_{13}–A_{0} go to every chip, **A_{15}A_{14}** to a 2-to-4 decoder; each decoder output enables one pair of chips. (b) **2 chips** side by side, same address and CS, one giving each byte; **no decoder**.

**Check 5.** (a) **AB'**. (b) PAL: the **OR** array is fixed. PROM: the **AND** array is fixed (it is the decoder).

**Check 6.** (a) 100 activates D_{4}, which reaches only F_{1}: **0010**. (b) **D_{4}, D_{5}, D_{6}, D_{7}**, the four minterms with A_{2} = 1.

**Check 7.** (a) **16 × 3**. (b) 4 inputs, 7 outputs: **16 × 7**; BCD uses codes 0–9, so **6 words** (10–15) are never used (they can hold anything, the don't-cares of file 07).

**Check 8.** (a) Written in A, B, C, D, F_{3} = AD + BD + C' + A'B' needs **4** terms, and each OR gate takes only 3; feeding back F_{1} = C' + A'B' fits it into 3. (b) **No**: in a PAL each product line goes to one fixed OR gate, so AC must be built twice.

**Check 9.** (a) **4** lines (ABC', A'B'CD', AC'D', A'B'C'D), more than the 3 an output has: it would **not fit**. (b) A PAL output has only a few product lines, so each function must be cut to its fewest terms; a PROM has a line for every minterm and needs no cutting.

**Check 10.** (a) 1 ⊕ 1 = **0**. (b) **AC**; a PAL would need 3 + 2 = **5** lines (AC built twice).

**Check 11.** (a) A'B', A'C', B'C', AB, AC, A'B'C': **6** lines, none shared. (b) **Blow the output XOR's fuse** (input 1), so the chip outputs the complement of the OR-sum.

**Check 12.** (a) A **PROM** (or an EEPROM/Flash used as one): no minimising, just rewrite the truth table each week; 3 inputs need only 8 words. (b) Feedback lets one output be used as a term inside another, so a group of terms is built once and used twice, a limited kind of sharing.

**Self-test.**

1. 8K = 2^{13}: **13 address lines**; 8192 × 8 = **65 536 bits**.
2. 32K/8K = **4 chips**; 32K = 2^{15}, so A_{12}–A_{0} to every chip and **A_{14}A_{13}** to a 2-to-4 decoder on the chip selects.
3. **16 × 2**.
4. F = **C**, G = **BC**: **2 product lines**, both outputs true (C feeds F; BC feeds G).
5. D_{7} reaches F_{3}, F_{2}, F_{0}: **1101**.
6. Inputs: 4 + 4 = 8 address bits; the largest product is 15 × 15 = 225 < 256, so 8 output bits: **256 × 8**.
7. Any two: SRAM cell is a latch (6 transistors), DRAM a transistor + capacitor; DRAM needs refresh, SRAM not; SRAM is faster, DRAM denser and cheaper per bit; SRAM for cache, DRAM for main memory.
8. Build those 2 terms as the other output, then **feed that output back** into the AND array and use it as one term: 4 terms become 3 (step 9's z = w + …).

<!--/ANSWERS-->
