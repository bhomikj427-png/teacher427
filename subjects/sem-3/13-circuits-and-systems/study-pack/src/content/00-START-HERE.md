# Circuits & Systems — Study Pack (MTE)

<div class="sub">ECE2107 · B.Tech ECE Sem 3 · follows the professor's MTE syllabus (dated 10/9/26) · built from two sets of class notes · every answer checked by circuit simulation</div>

## The path through this pack

The order is the professor's MTE syllabus, item by item.

**Part I — elements, laws, analysis**

[[map:01 Elements & sources > 02 Ohm, dividers, power & energy > 03 KVL, KCL, source transformation > 04 Nodal & mesh|here=1]]

**Part II — theorems (DC and AC)**

[[map:05 Superposition > 06 Thévenin & Norton > 07 Maximum power transfer]]

**Part III — transient analysis**

[[map:08 First order: step-wise, Laplace, test signals > 09 Second order RLC > 10 Mock paper]]

Each file needs the ones before it. 04 is KCL/KVL (03) written as a method. 06 uses 05's "switch a source off" rule, 04's nodal analysis and 01's dependent sources. 07 is built on 06. 08 uses 06 for the time constant; 09 uses 08's Laplace route.

| File | Syllabus item | What it teaches | Board Qs |
|---|---|---|---|
| 01 | 1 · elements (R, L, C, IDS, DS) | active vs passive, independent and dependent sources (with devices), R, L, C laws, what can't jump, lumped vs distributed | — |
| 02 | 2 · laws | Ohm, voltage and current division (DC and AC), power sign convention, energy, ladders | 4 |
| 03 | 3 · KVL, KCL, source transformation | the two laws, power balance, source transformation | 1 + 1 textbook |
| 04 | 4 · nodal and mesh | both methods, with current sources and dependent sources | 1 + 1 textbook |
| 05 | 5 · superposition | method, the cases where it fails, AC sources at different frequencies | 2 + 1 textbook |
| 06 | 5 · Thévenin & Norton | with a dependent source; with AC impedances | 1 + 1 textbook |
| 07 | 5 · maximum power transfer | R_{L} = R_{Th}, efficiency, conjugate match (worked) | 2 sets + 1 textbook |
| 08 | 6 · first order | 0⁻ / 0⁺ / ∞, τ, the one formula, Laplace, test signals δ, u, r | 4 + 2 textbook |
| 09 | 7 · second order | series RLC: over-, critically, under-damped, undamped | textbook |
| 10 | all | one paper: 12 theory prompts + 20 numericals | 14 + 6 textbook |

## Where the questions come from

A question that opens a section is **quoted from the professor's board** where one exists, and tagged with its notes page:
<span class="tag">Class p.7</span> = first notes set (the 23-page scan), <span class="tag">Set 2 p.9</span> = second notes set (22 photos).
Where the syllabus names a topic the class has not yet worked a question on, the pack uses a standard textbook-style problem, tagged <span class="tag">textbook</span>.

| | Base | Status |
|---|---|---|
| **P1** | The professor's board questions (notes sets 1 and 2) | **14 questions**, all used |
| **P2** | Textbook problems | **7**, written for syllabus items with no board question (KVL, nodal/mesh, AC theorems, Laplace, test signals, RLC). Values chosen so answers are clean; all checked by simulation |

Marks per question: **not known** (no hand-out, no past paper yet).

## How each file runs

| Part | What happens |
|---|---|
| **Map** | the file's pieces, in order |
| **Build** | each step opens with a real question → you guess → the answer teaches the idea → a Check |
| **Exam form** | what to reproduce in the exam: statements, procedures, the formula sheet |
| **Traps** | the mistakes that cost marks |
| **Self-test**, **Answers** | answers are on the last page(s) of every file |

:::key The one rule that makes this work
When you reach a **Guess first** box, write a guess on paper **before** reading on: one line, however wrong.
A wrong guess that gets corrected sticks better than a right answer you only read.
:::

Mark every Check and Self-test item:

- **clean** → revisit in 3 days
- **with struggle** → revisit tomorrow
- **wrong** → redo today, after the file

## Units and symbols used everywhere

- Uppercase **V, I** = DC (constant) values. Lowercase **v, i** = values that change with time. Complex values such as 5 − j5 V are **phasors**: amplitude and phase in one number.
- Resistances in **kΩ** with currents in **mA** give voltages in **V** directly: 2 kΩ × 3 mA = 6 V. Most questions use this.
- **R_{Th}**, **V_{Th}** = Thévenin resistance and voltage. **I_{N}** = Norton current. **R_{L}** = load resistance.
- **0⁻** = just before the switch moves. **0⁺** = just after. **∞** = long after (steady state).

## Where the two notes sets disagree with the pack

| Topic | Notes say | Pack says | Why |
|---|---|---|---|
| Superposition, two 5 V sources (05 §5) | set 2: 0 + 0 = 0 A, "LIMITATION"; set 1: 10 mA | 0 A by superposition, true 5 mA | set 2 is the correct use of the rule and shows why it fails; the pack follows set 2 |
| Thévenin with 2I (06 §2) | set 2: V_{Th} = 5.0025 V | 20/3 V | set 2 reads 2I as 2 Ω × I; the pack reads 2 kΩ × I. Both are right for their reading. **Ask the professor** |
| RL switch that opens (08 §5) | I_{R}(0⁺) = 0, I_{L}(0⁺) = 10 mA | cannot both hold in one series loop | **ask the professor** which path the current takes |

## How this pack was checked

- Facts: checked against the textbook-sourced circuits knowledge base (Hayt, Van Valkenburg, Sudhakar & Shyammohan)
  and Alexander & Sadiku.
- Numbers: every circuit in this pack was solved a second time by computer (nodal analysis and time simulation),
  and the answers here match. The script is `src/verify_mte.py`.
- Where the class notes had a slip of the pen, the pack uses the corrected version and says so in a Note.
