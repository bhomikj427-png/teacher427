# 19 — Memories and programmable logic

<div class="sub">Deck 15 (PROM slides 19–22, PAL 25–28, PLA 31–37) · memories: syllabus item with no deck slides · syllabus Unit 5 · needs 06 (decoders) and 02 (minimal SOP)</div>

## Map

[[map:1 Memory organisation, RAM > 2 ROM types, building bigger memories > 3 PROM, PAL, PLA|here=1]]

Two ways of buying logic in bulk. A memory stores a table: give it an address, get a word. A programmable logic device is an AND array feeding an OR array, with the connections left for you to make: 01's two-level logic, made programmable.

## The questions this file answers

- <span class="tag">practice</span> Differentiate SRAM and DRAM. A 1K × 8 memory: address and data lines? Build 4K × 8 from 1K × 8 chips.
- <span class="tag">Deck 15 slides 31–34</span> Implement F_{1} = Σ(0, 1, 2, 4), F_{2} = Σ(0, 5, 6, 7) with a PLA.
- <span class="tag">Deck 15 slides 25–27</span> Fit four functions into a PAL with three terms per output.

---

## Build

### 1 · Memory organisation and RAM

:::q <span class="tag">practice</span>
Differentiate static and dynamic RAM. A memory is specified as 1K × 8: how many address lines and data lines does it have?
:::

:::guess Guess first
To pick one of 1024 words, how many bits must the address have?
:::

:::note Terms
**Cell:** stores one bit. **Word:** bits read or written together. **Address:** selects one word. **RAM:** read/write, volatile. **ROM:** read-only, keeps its contents without power.
:::

[[fig:memory_org|2^{k} × m memory: a decoder turns the address into one word line.|w=60]]

A **2^{k} × m** memory has **k address lines** and **m data lines**; a decoder (06) selects the word; controls: chip select (CS), read/write.

<div class="two">

[[fig:sram_cell|6-transistor SRAM cell (Wikimedia Commons, public domain).]]

[[fig:dram_cell|1-transistor DRAM cell.]]

</div>

| | SRAM | DRAM |
|---|---|---|
| Cell | 6 transistors: a latch (09) + 2 access | 1 transistor + 1 capacitor |
| Bit stored as | latch state | charge |
| Refresh | not needed | every few ms (charge leaks; reads destroy it) |
| Speed · density · cost/bit | faster · lower · higher | slower · higher · lower |
| Used for | cache | main memory |

**Answer.** 1K = 2^{10}: **10 address lines, 8 data lines** (8192 bits). SRAM vs DRAM: the table.

:::check Check 1
(a) Address lines of a 16K × 4 memory? (b) Why does DRAM need refreshing but SRAM does not?
:::

### 2 · ROM types and bigger memories

:::q <span class="tag">practice</span>
How is a 4K × 8 memory built from 1K × 8 chips?
:::

:::guess Guess first
Four chips each answer to 1024 addresses. Which address bits choose the chip?
:::

| ROM | Written | Erased |
|---|---|---|
| Mask ROM | at manufacture | never |
| PROM | once by the user (blow fuses) | never |
| EPROM | in a programmer | UV light, whole chip |
| EEPROM, Flash | electrically, in circuit | electrically (Flash: a block at a time) |

[[fig:mem_decode|4K × 8 from four 1K × 8 chips and a 2:4 decoder.|w=65]]

**Answer.** 4096/1024 = **4 chips**, 12 address lines. **A_{9}–A_{0}** go to every chip; **A_{11}A_{10}** go to a **2:4 decoder** driving the four chip selects, so each chip answers to its own block of 1024 addresses.

:::check Check 2
(a) How many 16K × 4 chips make a 64K × 8 memory? (b) EPROM vs EEPROM in one line.
:::

### 3 · PROM, PAL and PLA

:::q <span class="tag">Deck 15 slides 31–34</span>
Implement the following two Boolean functions with a PLA: F_{1}(A, B, C) = Σ(0, 1, 2, 4), F_{2}(A, B, C) = Σ(0, 5, 6, 7).
:::

:::guess Guess first
Every SOP is a layer of ANDs feeding a layer of ORs. Which layer would you make programmable?
:::

:::note Terms
**PLD:** an AND array feeding an OR array with programmable connections. **Product term:** one AND gate's output. In diagrams a gate's inputs are one line and × marks a connection.
:::

[[fig:pld_arrays|PROM, PAL and PLA arrays.]]

| | AND array | OR array | Notes |
|---|---|---|---|
| PROM | fixed (a decoder: all minterms) | programmable | stores the truth table; no minimising; doubles per input |
| PAL | programmable | fixed | fixed terms per output, no sharing; fast, cheap |
| PLA | programmable | programmable | terms shared between outputs; output XOR can invert |

**PLA design:** a PLA has few AND gates, so minimise each function **and its complement**, and pick the forms sharing the most terms.

[[fig:v1arg8|F_{1}: group the 0s → F_{1}'. F_{2}: group the 1s.]]

**Answer.** F_{1} directly is A'B' + A'C' + B'C', sharing nothing. Its complement is F_{1}' = **AB + AC + BC**; F_{2} = **AB + AC + A'B'C'**. Two terms shared: use F_{1} = (AB + AC + BC)' with the output inverted: **4 product terms instead of 6**.

| Term | A B C | F_{1} | F_{2} |
|---|---|---|---|
| AB | 1 1 – | 1 | 1 |
| AC | 1 – 1 | 1 | 1 |
| BC | – 1 1 | 1 | – |
| A'B'C' | 0 0 0 | – | 1 |
| Output | | C (complemented) | T (true) |

**PAL design** (deck 15 slides 25–27): with three terms per output, z = ABC' + A'B'CD' + AC'D' + A'B'C'D needs four, but its first two are w; feed w back: **z = w + AC'D' + A'B'C'D**. Larger devices: **CPLD** (several PAL-like blocks) and **FPGA** (look-up tables with programmable wiring), described in Verilog or VHDL.

:::note Slip in the slides
Deck 15 slide 28 writes F_{2}(A, B, C) = m(4–7, 10–11) and F_{3}(A, B, C) = m(4–7, 9–15). Three variables have only minterms 0–7; these are functions of A, B, C, D (the mock paper, 20, uses them that way).
:::

:::check Check 3
<span class="tag">Deck 15 slide 37</span> F_{1}(A, B, C) = Σ(1, 2, 4, 6), F_{2} = Σ(0, 1, 6, 7), F_{3} = Σ(1, 2, 3, 5, 7). (a) What size PROM, and which minterms on each output? (b) Minimal SOP of each (the terms a PAL would need).
:::

---

## Exam form

**Memory.** 2^{k} × m → k, m; organisation sketch; SRAM vs DRAM table; ROM types table; expansion with a decoder on the top address bits.

**PLDs.** PROM/PAL/PLA table; PLA procedure (minimise F and F', share terms) and the programming table; PAL feedback trick.

## Traps

- Counting address lines from the bit count instead of the word count.
- Expanding width (more data bits) with a decoder: width needs chips side by side, sharing CS.
- Forgetting the output-inversion column in a PLA table.
- Sharing product terms in a PAL.

## Self-test

1. Address lines of an 8K × 8 memory?
2. Build 32K × 8 from 8K × 8 chips.
3. PROM size for 4 inputs and 2 outputs?
4. PLA for F = Σ(1, 3, 5, 7) and G = Σ(3, 7) (A, B, C): product terms?
5. Flash vs EEPROM?
6. ROM size to store the product of two 4-bit numbers?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **14**. (b) A DRAM bit is charge on a leaky capacitor; an SRAM bit is a latch that restores itself while powered.

**Check 2.** (a) 4 for words × 2 for width = **8 chips**. (b) EPROM: UV erase, whole chip, out of circuit; EEPROM: electrical erase, in circuit, byte at a time.

**Check 3.** (a) **8 × 3 PROM**. F_{1}: 1, 2, 4, 6; F_{2}: 0, 1, 6, 7; F_{3}: 1, 2, 3, 5, 7. (b) **F_{1} = A'B'C + BC' + AC'**, **F_{2} = A'B' + AB**, **F_{3} = C + A'B**.

**Self-test.**

1. **13**.
2. **4 chips**; A_{12}–A_{0} to all; **A_{14}A_{13}** to a 2:4 decoder on the chip selects.
3. **16 × 2**.
4. F = **C**, G = **BC**: **2** terms.
5. Both are electrically erasable in circuit; Flash erases a block at a time (denser, cheaper), EEPROM a byte at a time.
6. 8 address bits, 8 output bits: **256 × 8**.

<!--/ANSWERS-->
