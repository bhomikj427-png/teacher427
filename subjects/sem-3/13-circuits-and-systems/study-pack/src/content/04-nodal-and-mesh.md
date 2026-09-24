# 04 — Nodal and mesh (loop) analysis

<div class="sub">Set 2 p.11–12 (nodal, used by the professor) · MTE syllabus item 4 · 1 board circuit + 1 textbook problem · needs 03</div>

## Map

[[map:1 Nodal: unknowns are node voltages > 2 Nodal on the class circuit > 3 Mesh: unknowns are loop currents > 4 Mesh with a current source > 5 Which one to use|here=1]]

## The questions this file answers

- <span class="tag">textbook</span> 10 V, 2 kΩ, 4 kΩ (shared), 2 kΩ, 4 V: find every current by nodal analysis, then by mesh analysis.
- <span class="tag">Class p.7 · set 2 p.8</span> The superposition circuit by nodal and by mesh (answer known: I = 3 A).
- <span class="tag">Set 2 p.11–12</span> The professor's nodal working for V_{Th}: see 06 §2, which uses this file's method.

Both methods are KCL (nodal) or KVL (mesh) from 03, written in a fixed order so that nothing gets missed.

---

## Build

### 1 · Nodal analysis

:::q <span class="tag">textbook</span>
Find V_{1}, and the current in every branch.
:::

[[fig:mesh2|Two sources, three resistors. One ground at the bottom; one unknown node, V_{1}.|w=62]]

:::guess Guess first
How many unknowns do you need if the unknowns are node voltages? And if they are loop currents?
:::

**Procedure.**
1. Pick a **reference node** (ground, 0 V). Usually the node with the most connections.
2. Name every other node's voltage: V_{1}, V_{2}, … A node joined to ground only by a voltage source is known already.
3. At each unknown node write KCL with **every current written as leaving**: \frac{V_{node} − V_{other}}{R}.
4. Solve the equations.

Here the only unknown is V_{1}. Currents leaving it through the left 2 kΩ, the 4 kΩ and the right 2 kΩ (units V, kΩ, mA):

$$\frac{V_{1} − 10}{2} + \frac{V_{1}}{4} + \frac{V_{1} − 4}{2} = 0$$

Multiply by 4: 2V_{1} − 20 + V_{1} + 2V_{1} − 8 = 0 ⇒ 5V_{1} = 28 ⇒ **V_{1} = 5.6 V**.

| Branch | Current | Value |
|---|---|---|
| left 2 kΩ, to the right | \frac{10 − 5.6}{2} | **2.2 mA** |
| 4 kΩ, downwards | \frac{5.6}{4} | **1.4 mA** |
| right 2 kΩ, to the right | \frac{5.6 − 4}{2} | **0.8 mA** |

KCL check at V_{1}: 2.2 = 1.4 + 0.8 ✓.

The Guess answer: nodal needs **(nodes − 1)** unknowns, here **1**. Mesh needs one per window, here **2**.

### 2 · Nodal on the class circuit

:::q <span class="tag">Class p.7 · set 2 p.8</span>
Find I (down through the 2 Ω) by nodal analysis.
:::

[[fig:sp_q||w=50]]

One unknown, V_{A}. Currents leaving A: through the 4 Ω, \frac{V_{A} − 10}{4}; through the 2 Ω, \frac{V_{A}}{2}; the 2 A source pushes **into** A, so it counts as −2 leaving:

$$\frac{V_{A} − 10}{4} + \frac{V_{A}}{2} − 2 = 0  ⇒  V_{A} = 6 V,   I = \frac{6}{2} = 3 A$$

Same 3 A as superposition (05) and source transformation (03). A current source simply puts a known current into the KCL equation.

**With a dependent source** (06 §2, set 2 p.11): write the source's value in terms of the node voltages first (there, I = \frac{10 − V_{A}}{2}), substitute, and the equation again has one unknown. That is exactly the professor's nodal working.

:::check Check 1
In the textbook circuit, change the 4 V source to 0 V (a short). Write the nodal equation and find V_{1}.
:::

### 3 · Mesh analysis

:::q <span class="tag">textbook</span>
Same circuit. Find the mesh currents i_{1}, i_{2}.
:::

**Procedure.**
1. Give each **window** (mesh) of the circuit a clockwise current: i_{1}, i_{2}, …
2. A resistor shared by two meshes carries the **difference**: (i_{1} − i_{2}) in mesh 1's direction.
3. Write KVL round each mesh: Σ rises = Σ drops.
4. Solve.

Mesh 1 (10 V rise; drops across the left 2 kΩ and the shared 4 kΩ):

$$10 = 2i_{1} + 4(i_{1} − i_{2})  ⇒  6i_{1} − 4i_{2} = 10$$

Mesh 2 (clockwise, the current goes **down** through the 4 V source from + to −, a drop):

$$0 = 4(i_{2} − i_{1}) + 2i_{2} + 4  ⇒  −4i_{1} + 6i_{2} = −4$$

Solve (determinant 6·6 − 4·4 = 20): **i_{1} = 2.2 mA, i_{2} = 0.8 mA**. The 4 kΩ carries i_{1} − i_{2} = **1.4 mA** down, and 1.4 × 4 = **5.6 V**: the same answers as nodal ✓.

:::key Reading a mesh answer
A mesh current is a **bookkeeping** current. The current in a resistor that belongs to one mesh is that mesh current; in a shared resistor it is the difference.
:::

### 4 · Mesh with a current source

:::q <span class="tag">Class p.7 · set 2 p.8</span>
Find I by mesh analysis.
:::

[[fig:sp_mesh|The 2 A source (arrow up) sits on the outer edge of mesh 2 only.|w=55]]

A current source on the **outside edge** of a mesh fixes that mesh current. Mesh 2 goes **down** through the source, but the source pushes 2 A **up**:

$$i_{2} = −2 A$$

Mesh 1: 10 = 4i_{1} + 2(i_{1} − i_{2}) = 6i_{1} + 4 ⇒ **i_{1} = 1 A**.

The 2 Ω carries i_{1} − i_{2} = 1 − (−2) = **3 A downwards** ✓. The 4 Ω carries i_{1} = 1 A, which agrees with nodal: \frac{10 − 6}{4} = 1 A.

If a current source is **shared** by two meshes, its current fixes their difference, and you write one KVL round the combined loop that avoids the source (a **supermesh**). The nodal twin: a voltage source between two unknown nodes fixes their difference, and you write one KCL round both (a **supernode**).

:::check Check 2
Why can't you write a KVL equation for mesh 2 in this circuit the normal way?
:::

### 5 · Which one to use

| Use **nodal** when… | Use **mesh** when… |
|---|---|
| fewer nodes than meshes | fewer meshes than nodes |
| the circuit has current sources | the circuit has voltage sources in series with resistors |
| you need voltages (e.g. V_{Th}) | you need loop currents |
| the circuit is non-planar (wires cross) | the circuit is planar (mesh needs that) |

---

## Exam form

**Nodal.** (1) Choose a reference node. (2) Label the other node voltages. (3) KCL at each unknown node, currents written as leaving: (V_{n} − V_{m})/R. (4) Solve. Unknowns = nodes − 1 (less any fixed by voltage sources). Voltage source between two unknown nodes → supernode.

**Mesh.** (1) One clockwise current per window. (2) Shared element carries the difference. (3) KVL per mesh. (4) Solve. Unknowns = number of windows. Current source on an outer edge fixes that mesh current; a shared one → supermesh.

**Dependent sources.** Write the controlling variable in terms of the unknowns, substitute, then solve.

## Traps

- Mixing "leaving" and "entering" within one nodal equation.
- In mesh analysis, writing the shared resistor's voltage as R·i_{1} instead of R(i_{1} − i_{2}).
- Mesh analysis on a circuit with a current source: trying to write the source's voltage as "0". It is unknown; use the source to fix the mesh current instead.
- Unit mix: with kΩ, currents come out in **mA** (the set 2 p.12 working mixes kΩ and A; see 06 §2).

## Self-test

1. How many equations does nodal analysis need for a circuit with 5 nodes and no voltage sources?
2. In the textbook circuit, find the power delivered by the 10 V source.
3. Write the two mesh equations if the 4 V source were reversed (+ at the bottom).
4. What is a supernode, and when do you need one?
5. Solve the class circuit by mesh if the 2 A source pointed down.

<!--ANSWERS-->
## Answers

**Check 1.** \frac{V_{1} − 10}{2} + \frac{V_{1}}{4} + \frac{V_{1}}{2} = 0 ⇒ 5V_{1} = 20 ⇒ **V_{1} = 4 V**.

**Check 2.** The voltage across a current source is not known in advance (it is whatever the circuit makes it), so the KVL equation would contain an extra unknown. The source already gives i_{2} directly.

**Self-test.**

1. **4** (nodes − 1).
2. 10 V × 2.2 mA = **22 mW** (current leaves its + terminal: it delivers).
3. 6i_{1} − 4i_{2} = 10 and −4i_{1} + 6i_{2} = **+4** (now a rise) ⇒ i_{1} = 3.8 mA, i_{2} = 3.2 mA.
4. A voltage source connected between two non-reference nodes: enclose both nodes, write one KCL for the pair plus V_{a} − V_{b} = V_{s}.
5. i_{2} = +2 A; 10 = 6i_{1} − 4 ⇒ i_{1} = 7/3 A; I = i_{1} − i_{2} = **1/3 A** (matches 05 Check 1b).
<!--/ANSWERS-->
