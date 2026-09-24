# Circuits & Systems — Study Pack

<div class="sub">ECE2107 · B.Tech ECE Sem 3 · built from the professor's class (notes to 12 Sept 2026) · every answer checked by circuit simulation</div>

## The path through this pack

[[map:01 Elements & sources > 02 Dividers & source transformation > 03 Superposition > 04 Thévenin & Norton > 05 Maximum power transfer > 06 First-order transients > 07 Mock paper|here=1]]

Each file needs the ones before it. 04 uses 03's "switch a source off" rule and 01's dependent sources.
05 is built on 04. 06 uses 04 for the time constant.

| File | What it teaches | Professor's questions in it |
|---|---|---|
| 01 | active vs passive, independent and dependent sources, the R, L, C laws, what can't change suddenly | none yet (theory) |
| 02 | voltage division, current division, source transformation, series–parallel reduction | 4 |
| 03 | superposition: method, and the cases where it fails | 2 |
| 04 | Thévenin and Norton, with a dependent source | 1 |
| 05 | maximum power transfer, efficiency, conjugate matching | 2 sets |
| 06 | 0⁻ / 0⁺ / ∞ analysis, time constant, the one first-order formula | 3 |
| 07 | all of the above as one paper | 13 |

## Where the questions come from

Every question that opens a section is **quoted from the professor's board**, as written in the class notes, and tagged
with the notes page: <span class="tag">Class p.7</span>. No question is invented.

| | Base | Status |
|---|---|---|
| **P1** | The professor's board questions (class notes, 23 pages) | **13 questions**, all used |
| **P2** | Textbook end-of-chapter problems | **empty for now**: no course hand-out yet, so the prescribed book is unconfirmed. The notes name Alexander & Sadiku, Van Valkenburg, A.K. Chakraborty |

Marks per question: **not known** (no hand-out, no past paper yet).

## How each file runs

| Part | What happens |
|---|---|
| **Map** | the file's pieces, in order |
| **Build** | each step opens with a real question → you guess → the answer teaches the idea → a Check |
| **Exam form** | what to reproduce in the exam: statements, procedures, the formula sheet |
| **Attempt** | the professor's questions again, now answerable |
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

- Uppercase **V, I** = DC (constant) values. Lowercase **v, i** = values that change with time.
- Resistances in **kΩ** with currents in **mA** give voltages in **V** directly: 2 kΩ × 3 mA = 6 V. Most questions use this.
- **R_{Th}**, **V_{Th}** = Thévenin resistance and voltage. **I_{N}** = Norton current. **R_{L}** = load resistance.
- **0⁻** = just before the switch moves. **0⁺** = just after. **∞** = long after (steady state).

## How this pack was checked

- Facts: checked against the textbook-sourced circuits knowledge base (Hayt, Van Valkenburg, Sudhakar & Shyammohan)
  and Alexander & Sadiku.
- Numbers: every circuit in this pack was solved a second time by computer (nodal analysis and time simulation),
  and the answers here match.
- Where the class notes had a slip of the pen, the pack uses the corrected version and says so in a Note.
