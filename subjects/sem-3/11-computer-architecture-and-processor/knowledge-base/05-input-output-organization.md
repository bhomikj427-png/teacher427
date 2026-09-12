# U5 — Input–Output Organization (Stage 1)

**Lectures L20–L22 · CO3 · ETE only · ⚠ NO DECK SUPPLIED**

Scope (hand-out): L20 Input-Output Organization: Peripheral Devices · L21 Asynchronous & Synchronous
Data Transfer · L22 Modes of Transfer.

Truth authority: **Mano 3e ch. 11**. Built textbook-primary (no deck), verified against two
independent institutional reproductions of that chapter.

> **The organizing idea for the whole unit (big idea 7):** everything here is a rung on **one ladder
> of increasing device autonomy and decreasing CPU involvement** — strobe → handshake → polled flags →
> interrupts → DMA → I/O processor. Teach it as a ladder, not as six unrelated topics; the "explain
> the need for X" questions in the hand-out's Session Outcomes are all answered by "the previous rung
> wasted too much CPU time."

---

## 1. Why an interface is needed at all — `settled`

Peripherals cannot be wired to the CPU bus directly. **Four differences** must be resolved (Mano's
list — this is the "explain the need for I/O organization" answer):

1. **Peripherals are electromechanical / electromagnetic**; the CPU and memory are **electronic**. So
   **signal values must be converted.**
2. **Peripherals are slower** than the CPU, so a **synchronization mechanism** is needed.
3. **Data codes and formats differ** from the CPU's word format.
4. **Operating modes differ** between peripherals, and each must be controlled so as not to disturb
   the others.

The hardware that resolves these sits between the CPU bus and the device and is called an **interface
unit**.

**Peripheral devices** (L20): input (keyboard, mouse, scanner), output (printer, display, plotter),
and both (magnetic disk, magnetic tape, communication link). Classified as **peripherals** because
they are outside the CPU–memory core.

## 2. Bus organization for memory and I/O — `settled`

Three ways a computer's buses can serve both memory and I/O:

| Scheme | Description | Consequence |
|---|---|---|
| **Two separate buses** | one for memory, one for I/O (a dedicated **IOP**) | most parallel, most hardware |
| **One common bus, separate control lines** | shared address/data; distinct memory-read/write vs I/O-read/write | **isolated I/O** — I/O ports live in their own address space, needing distinct IN/OUT instructions (this is the 8086's scheme, → U7) |
| **One common bus, common control lines** | I/O ports occupy addresses in the memory map | **memory-mapped I/O** — no special instructions; any memory instruction can touch a device, at the cost of address space |

**Mechanism / trade:** isolated I/O keeps the full memory address space for memory and makes I/O
visible in the program text, but needs extra instructions and control lines. Memory-mapped I/O gets
the whole instruction set for free on devices (you can `AND` directly into a control register) but
consumes memory addresses. This is a clean compare/contrast exam item.

## 3. Asynchronous data transfer — `settled` (L21)

**Synchronous** transfer: both units share a **common clock**; no extra signalling is needed because
both know when data is valid. Only workable when the units are close and matched in speed.

**Asynchronous** transfer: the units have **independent clocks**, so **control signals must be
transmitted to indicate when data is being transferred.** Two methods:

### (a) Strobe control — one control line

A single **strobe pulse**, supplied by one unit, tells the other when to act.

**Source-initiated:** the source places data on the bus, waits for it to settle, then pulses the
strobe; the destination captures data on the strobe (usually its trailing edge).

```
   data     ──────⟨ valid data ⟩──────
   strobe   ________╱‾‾‾‾‾╲__________
                    ↑ destination samples here
```

**Destination-initiated:** the destination pulses the strobe to *request* data; the source responds by
placing data on the bus.

**★ The fatal weakness — say this, it is the whole reason handshaking exists:** the strobe is
**one-way**. The source has **no way to know the destination actually received** the data (it might be
busy or absent), and the destination has no way to know the data is still valid. A strobe assumes a
timing relationship rather than confirming one.

### (b) Handshaking — two control lines

Add a **second control line for the reply**. One unit signals "data ready", the other replies "data
accepted".

**Source-initiated handshaking** (lines: `data valid` from source, `data accepted` from destination):

```
1. source places data on the bus and asserts  data valid
2. destination reads the data and asserts     data accepted
3. source removes data and de-asserts         data valid
4. destination de-asserts                     data accepted     → ready for the next
```

**Destination-initiated handshaking** (lines: `ready for data` from destination, `data valid` from
source): the destination asserts `ready for data`; the source responds with data + `data valid`; and
so on symmetrically.

**Advantage:** "a high degree of flexibility and reliability because the successful completion of a
data transfer relies on active participation by both units." **Timeout:** if one unit never replies,
the other can detect the error rather than hang forever — impossible with a strobe.

## 4. Modes of transfer — `settled` (L22)

Binary information received from a device is ultimately stored in **memory**; information sent out
originates in memory. The CPU merely executes the I/O instructions. **Three modes** (Mano §11-4):

| Mode | Who moves the data | CPU cost | Device autonomy |
|---|---|---|---|
| **1. Programmed I/O** | the CPU, under program control | **highest** — the CPU polls and copies every word | none |
| **2. Interrupt-initiated I/O** | the CPU, but only when told to | medium — no polling, but the CPU still copies | some |
| **3. Direct Memory Access (DMA)** | **the DMA controller**, not the CPU | **lowest** — the CPU is bypassed entirely for the transfer | high |

⚠ **Count caveat (`likely`, and worth a sentence in an exam):** Mano's §11-4 "Modes of Transfer"
presents **three** modes, and treats the **I/O Processor** as a separate topic (§11-7). Some
summaries of the chapter therefore say "four modes of transfer", counting the IOP. **Both readings are
defensible** — say "three modes of transfer, plus the IOP as a further step" and you are safe either
way. Do not assert a number as fact. (`misconceptions.md` M13.)

### Programmed I/O

The CPU tests a **flag** in a loop and transfers one word at a time (exactly U2 §9). Each transfer
requires the CPU to execute instructions.
**Cost:** continuous CPU involvement; the CPU is slowed to the device's speed. **Benefit:** simplest,
least hardware. Acceptable only for slow devices or small transfers.

### Interrupt-initiated I/O

Instead of the CPU polling, the **interface monitors the device** and raises an **interrupt request**
when ready. The CPU finishes its current instruction, saves its state, branches to a service routine,
transfers the data, and returns.
**Benefit:** the CPU does useful work while the device is not ready. **Remaining cost:** the CPU still
executes the transfer itself, and pays interrupt overhead (save/restore state) per transfer.

### Priority interrupt — `settled`

With several devices, two questions arise: **which is serviced first** when requests coincide, and
**which may interrupt an in-progress service routine.**

**Assignment principle:** higher priority goes to requests that would have serious consequences if
delayed — **fast devices (magnetic disk) get high priority, slow devices (keyboard) get low.**
*Mechanism:* a slow device can wait many milliseconds without losing data; a disk delivering a word
every few microseconds will **overrun** if not serviced promptly. Priority follows data-loss risk, not
importance.

Two implementations:

| Scheme | Mechanism | Trade |
|---|---|---|
| **Daisy chain (serial)** | all devices are connected in **series**; the highest-priority device is placed **first**, and each device passes an "acknowledge" signal along only if it is not itself requesting | few wires; priority is fixed by **physical position**; the acknowledge ripples, so latency grows with chain length |
| **Parallel priority** | a **register** holds one interrupt-request bit per device, and a **priority encoder** selects the highest active one; a **mask register** can individually enable/disable levels | faster, and priority is **programmable** via the mask; costs more hardware |

The **interrupt vector** / priority encoder output supplies the address of the correct service routine
— which answers Mano's own question "how can the CPU obtain the starting address of the appropriate
routine?" (asked verbatim on the U2 deck's "Further questions on interrupt" slide).

**The four questions the priority-interrupt section answers** (the U2 deck poses them; this is where
they close):
1. How does the CPU recognize which device requested? → daisy-chain acknowledge, or the
   interrupt-request register.
2. How does it find that device's service-routine address? → interrupt vector / encoder.
3. May a device interrupt an in-progress service routine? → only if its priority is higher (nested
   interrupts), controlled by the mask.
4. What if two requests arrive simultaneously? → the priority scheme resolves it.

### Direct Memory Access (DMA) — `settled`

**The idea:** remove the CPU from the transfer path entirely. The **DMA controller** takes over the
buses and transfers data **directly between the device and memory.**

**Mechanism — bus mastery.** The DMA controller asserts a **bus request (BR)**; the CPU finishes its
current bus cycle, **floats (tri-states) its address, data and control lines**, and replies with a
**bus grant (BG)**. The DMA controller is now **bus master** and drives memory itself. When done it
releases BR and the CPU resumes.

**Why tri-state buffers matter here:** this is the concrete reason the CPU's bus drivers must be
three-state — two masters cannot drive one bus. (Links to `../../04-digital-electronics` unit 05.)

**What the CPU must tell the DMA controller before starting** (its register set):
- the **starting address in memory**,
- the **word count** (how many words to transfer),
- the **direction** (read or write) and control mode.

**Two transfer modes:**

| Mode | Mechanism | Effect on CPU |
|---|---|---|
| **Burst transfer** (block) | the DMA controller keeps the bus and transfers **the whole block** before releasing it | CPU is stalled for the duration — fastest transfer, worst CPU availability. Needed for devices that cannot be stopped mid-block (e.g. disk) |
| **Cycle stealing** | the controller takes **one word per bus acquisition**, releasing the bus in between | CPU runs almost normally, only slightly slowed — the CPU "loses" occasional memory cycles |

**DMA as a synchronization idea:** DMA does not make memory faster; it removes the *instruction
execution overhead* of moving data. A programmed transfer costs several instructions per word; DMA
costs one memory cycle per word.

### Input–Output Processor (IOP) — `settled`

The next rung: a **processor dedicated to I/O**, with its own instruction set (a **channel program**),
capable of executing a sequence of I/O operations autonomously and doing format conversion.

**CPU–IOP communication:** the CPU does not command the IOP step by step. It places a **program for
the IOP in memory** and issues a single instruction to start it; the IOP fetches and executes that
program, performs the transfers, and **interrupts the CPU when finished.** The two communicate through
memory-resident control blocks.
*In IBM terminology the IOP is a **channel**; a CPU instruction that starts it is a channel command.*

**Data communication processor** — a specialized IOP that serves many remote terminals over
communication lines.
*The key structural difference from an ordinary IOP:* an IOP talks to peripherals over a **common I/O
bus with many parallel data and control lines**; a data communication processor talks to each terminal
over **a single pair of wires**, transferring both data and control **serially** — so the rate is much
slower, and a **protocol** is needed.
**Protocols** divide by message-framing technique into **character-oriented** (based on a character
code, usually **ASCII**) and **bit-oriented** (no characters, code-independent, allows a serial bit
stream of any length). The equipment and lines between stations form a **data link**.

---

## Worked-problem patterns for this unit

1. **Explain the need for an I/O interface** — the four differences between peripherals and CPU.
2. Compare the three bus organizations; **isolated vs memory-mapped I/O**.
3. **Strobe vs handshaking** — draw both timing diagrams; say why handshaking is more reliable.
4. Draw source-initiated and destination-initiated handshaking sequences.
5. **Compare the three modes of transfer** on CPU involvement and device autonomy.
6. **Explain DMA**: the BR/BG mechanism, the controller's registers, burst vs cycle stealing.
7. **Daisy-chain vs parallel priority interrupt** — mechanism and trade-off.
8. Explain the IOP and CPU–IOP communication.
9. Character-oriented vs bit-oriented protocols.

## Confidence summary

`settled`: the four peripheral/CPU differences · the three bus organizations and the isolated vs
memory-mapped trade · synchronous vs asynchronous · strobe (both directions) and its one-way weakness ·
handshaking (both directions) and its reliability/timeout argument · the three modes of transfer ·
priority-interrupt principle and both implementations · DMA bus-mastery mechanism, controller
registers, burst vs cycle stealing · IOP and CPU–IOP communication via a memory-resident program ·
character- vs bit-oriented protocols.
`likely`: **the "three vs four modes of transfer" count** — a genuine ambiguity in how Mano's chapter
is summarized (§11-4 gives three; the chapter overall covers the IOP too). Teach as "three, plus the
IOP."
`uncertain`: **the instructor's emphasis** — no deck for L20–L22, so depth is inferred from lecture
count (3 lectures, descriptive Session Outcomes: "Explain the need of…"). Reads as a
descriptive/compare unit with low numerical yield, hence MEDIUM priority in `exam-map.md`.
Not claimed: specific controller ICs (8237 DMA, 8259 PIC) — out of scope per `00-map.md`; serial
standards (RS-232 levels, UART bit timings) beyond the protocol classification.

> **Stage 2 for this unit:** `stage-2/05-input-output-organization.md` — why interrupt latency and not
> throughput is the real design constraint, DMA cache-coherence and why device transfers must not be
> cached, memory-mapped I/O and the volatile-qualifier problem, IOMMUs and modern device isolation,
> and how this ladder ends at MSI-X and polling drivers (where fast devices go back to polling).
