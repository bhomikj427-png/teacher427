# 00 · Start here: the trainer kit, wiring discipline, and the whole lab

<div class="sub">ECE2131 Digital Electronics Lab · source: the lab manual (2025), 55 pp. · every design in this pack is machine-checked over all inputs (src/verify.py, 49 checks pass) · marks: 100 = internal 60 + external 40; exam 3 hours</div>

## The lab as one path

[[map:1 Gates & universality > 2 Adders/subtractors > 3 NAND/NOR design > 4 Code converters > 5 Comparator & parity > 6–8 MUX, DEMUX, decoder > 9–10 Flip-flops > 11–12 Counters & shift registers > 13 FSM > 14 TTL|here=1]]

- **Experiments 1–8 are combinational:** the output depends only on the present inputs.
- **Experiments 9–13 are sequential:** they add memory (flip-flops), so the output also depends on the past.
- **Exp 14** looks inside one gate.

You already know the theory (ECE2102). What this pack adds is the part the exam tests at the bench: **which IC, which pin, which wire, what the LEDs should show, and why.**

## The IC trainer kit

| Part of the kit | Use |
|---|---|
| +5 V and GND terminals | power every IC: **+5 V only. More destroys TTL.** |
| logic input switches | give 0/1 to inputs (up = 1) |
| LED indicators | show outputs (lit = 1) |
| clock generator (≈ 1 Hz) | slow continuous clock for counters |
| pulser / mono-pulse (debounced) | one clean clock edge per press. Use this for flip-flop tables. |
| breadboard | 5-hole vertical strips are one node; the long rails are the power buses |

## Wiring discipline (the manual's "common causes of problems", made into a routine)

:::do Every circuit, every time
1. Power **off**.
2. Plug each IC across the breadboard's centre gap, with the **notch to the left** (or up) and all ICs facing the same way. Pin 1 is next to the notch or dot. Pins count **anticlockwise** seen from the top.
3. Wire **VCC and GND of every IC first**:
   - 14-pin gates: VCC = 14, GND = 7.
   - 16-pin MSI chips: VCC = 16, GND = 8.
   - **Exceptions: 7483 (VCC 5, GND 12) and 7473 (VCC 4, GND 11).**
4. Wire short connections before long ones, and tick each one off on the circuit diagram as you go.
5. Tie every unused input. Unused AND/NAND inputs go to an input you are using or to +5 V; unused OR/NOR inputs go to GND. A floating TTL input reads as HIGH, which silently forces a NOR output to 0.
6. Have a partner check the wiring. Then power **on**, and walk the truth table row by row.
7. Never drive one gate input from two outputs. Never rewire with the power on.
:::

:::trap When nothing works
In this order:

1. Is the IC powered? Check with the meter on the IC's own VCC/GND pins.
2. Is the IC in the right way round?
3. Is the IC dead? Swap it.
4. Is the LED wired to the output pin or to an input pin?

Most "wrong" truth tables are a missing ground or an IC in backwards.
:::

## How each chapter works

Each experiment gives you, in order:

1. the aim as the question;
2. a guess-first line;
3. the design (expressions, already checked);
4. the **pin-to-pin wiring table**;
5. what the LEDs should show;
6. a ready "write in your record" block;
7. traps and a check, with answers at the end of the chapter.

The pin diagram of every IC appears where it is first used.

## Errors in the manual

| Where | The manual says | Correct |
|---|---|---|
| Exp 1, NOT gate | truth table A = 0 → Y = 0, then 0 → 1 | A = 0 → Y = 1; A = 1 → Y = 0 |
| IC table | 74138 listed as "negative edge triggered dual J-K F/F" | 74138 is a 3:8 decoder (the 7473 is the JK) |
| Exp 2, Fig 2.5 | "Pin Diagram of IC 7485 (4-bit binary full adder)" | the adder is the **7483** (the 7485 is the comparator) |
| Exp 2, subtractor | "borrow output at C_{out}" | for A − B, C_{out} = 1 means **no** borrow (A ≥ B); C_{out} = 0 means the answer is negative, in 2's complement |
| Exp 4, Table 4.2 | "BCD to grey code" | BCD to **Excess-3** |
| Exp 7 | aim says "multiplexer"; parts 74151, 74153 | demultiplexer; the 1:8 needs the **74138** |
| Exp 13 | the list says detect **101**; the experiment designs **1010** | this pack gives both |
| Exp 13 (ii) | F⁺ = XY + FY'' | F⁺ = XY + FY' |
| Exp 11, ring counter | "clear all flip-flops, then clock" | a ring counter cleared to 0000 stays at 0000 forever. One flip-flop must be **preset** to 1. |
| Exp 14 | no circuit given | see Exp 14 in this pack (LTspice-verified) |
