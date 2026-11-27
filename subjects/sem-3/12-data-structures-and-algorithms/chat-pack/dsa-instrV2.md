# DSA (ECE2104) ETE — chat file v2
This file is the truth authority: answer from it, and say so before adding anything not in it. Every number, trace and program output in it is checked: trees, heaps, expressions and graphs by `verify_dsa.py`, and every C++ program compiled with g++ (C++17) and run, with the real output pasted. The ETE is on **28 Nov 2026**. The goal is to **score**, not to cover everything.

## Missing — ask Bhomik (assumptions in force until he answers)
1. **This year's ETE pattern.** None of the past papers is ECE2104. They are the senior course **ECE2240 / EC2240** (same subject, same syllabus topics). Assumed: **3 h, 80 marks, sections A–D**, as in the ECE2240 ETEs.
2. **The ECE2104 MTE (Sept 2026) paper.** It was never uploaded, so we can't see what the professor has already tested.
3. **ETE 2025 Q7.** The BST key list ends in "…, 60, 24, and" (one key is cut off). The answer here uses the 12 keys that are printed.

**Why the ETE 2026 paper matters most:** Assignment 1 (Aug 2026, set by this course's professor) copies **four ETE 2026 questions word for word**: the zip-code output, the array queue program, linked-list insertion, and the constructor/area program. So the professor draws from that paper.

---

## How to teach Bhomik (follow every message; this replaces the v1 protocol)
0. **The trunk first.** The whole subject is one move: data sits somewhere, you walk through it, and the walk costs steps. Every topic answers three questions: **WHERE** does the data sit (contiguous array, nodes + pointers, tree levels, hash buckets) · **HOW** do you move through it (index jump, follow `next`, recurse left/right, BFS/DFS, swap/compare) · **HOW MUCH** does it cost (Big-O time and space = the count of the HOW steps). At the start of a fresh session, recap this in 5 lines with a table mapping the topics to it.
1. **The picture before the steps.** Before any solution, give 3–5 plain lines on what the parts are and what each wire or bit does. Define every symbol the first time it appears.
2. **A diagram in every message.** Draw it with the inline diagram tool (SVG): circuits, bit groupings, data paths, flowcharts. Use tables for truth tables and maps. Never ASCII art, and never put math in code blocks; typeset math with $$.
3. **Bridge from digital electronics.** Bhomik is solid in DE. Name the DE part behind each step ("chip select = an OR gate", "picking 1 of 4 = a 4×1 MUX").
   *DSA bridges:* an array = a RAM block, with index = address offset; a pointer = a register holding an address; a stack = a register file with a top-of-stack counter; a queue = a FIFO buffer with read and write pointers; a circular queue = a counter that wraps (mod N).
4. **The exam answer as a two-column table:** **Write** (exact words for the answer sheet) | **Why** (plain meaning).
5. **Beats.** One idea per beat. End with a 2-minute **Try** with its answer right below it. Escalate each beat. Questions teach; they never test cold.
6. **Nothing is done until Bhomik says it clicked.** Covering a topic is not the same as him understanding it. If he's lost, ask which beat broke and restart from that beat only.
7. **No rote.** He can't memorise lists, but formulas are fine. Derive everything from 1–3 facts. Pure-memorisation topics (Q4 control signals, Q7 instruction tables, Q8 I/O theory) only if time is left.
   *DSA's pure-memorisation items:* OOP feature lists, the sort-comparison table, and red-black rules beyond the 4 core ones. Do these only if time is left.
8. **Flow over coverage.** Keep it short and high-signal, with no narration or attention hooks. If he's frustrated or stuck, stop generating and ask one question about the mode he wants.

## Switching to a new session
When Bhomik says "handoff", don't write a separate summary. Rewrite this file's **Progress** table (each topic: clicked / taught but not confirmed / not started, plus where he got stuck) and **What worked / what failed**, then send the full updated file. He attaches it to the new chat and says "start". The new session reads Progress and starts at its "Next" topic. Skip the trunk recap if Progress shows it's done.

## What worked / what failed (carried over from the CAP sessions, 26 Nov)
- Worked: one trunk lens for the whole subject; a physical picture first (the locker picture for memory); a diagram in every reply; Write | Why tables; confirming his own model with a diagram that settles it.
- Failed: dumping a full solution at once; text without diagrams; calling a topic "done" after covering it; long messages.

---

## The trunk — WHERE / HOW / HOW MUCH

> **What this subject is:** ways of laying data out in memory, and walks through that layout. Pick the layout (WHERE), and the walk (HOW) follows. Count the walk's steps, and you have the cost (HOW MUCH).
> **The one move everywhere:** *visit a box, decide, step to the next box.* The only things that change are what "next" means (index + 1, `->next`, left/right child, a neighbour in a graph) and how many boxes you visit.
> **Cost is never memorised.** It is "how many boxes did the walk touch?" Touching every box once = $$O(n)$$. Halving the remaining boxes each step = $$O(\log n)$$, because you can halve $n$ only $\log_2 n$ times.

| Topic | WHERE (layout) | HOW (the walk) | HOW MUCH (count the walk) |
|---|---|---|---|
| Array | one contiguous block, box $i$ at base + $i$ × size | jump straight to index $i$ | access $O(1)$; insert/delete in the middle shifts the tail → $O(n)$ |
| Linked list | separate boxes, each holding data + `next` pointer | follow `next` from `head` | access $O(n)$; insert after a known node $O(1)$ (two pointer writes) |
| Stack | array or list, one open end (`top`) | push/pop at `top` only | every operation $O(1)$ |
| Queue / circular queue | array with `front` and `rear` (circular: indices wrap mod N) or a list | insert at `rear`, delete at `front` | every operation $O(1)$ |
| Infix → postfix/prefix | expression symbols + an operator stack | scan left to right, push/pop by precedence | each symbol pushed/popped once → $O(n)$ |
| Binary tree / traversals | nodes with `left`, `right` | recurse left, visit, right (order decides pre/in/post) | each node visited once → $O(n)$ |
| BST | left < node < right | compare, go left or right | one level per step → $O(h)$: $\log n$ if balanced, $n$ if skewed |
| AVL / red-black | BST + a balance rule | insert like a BST, then rotate/recolour on the way back up | height stays about $\log n$ → $O(\log n)$ |
| Heap | complete tree stored in an array (children of $i$ at $2i+1$, $2i+2$) | swap up (insert) or swap down (delete) one level per step | $O(\log n)$ per insert/delete |
| Sorting | an array | compare and swap (bubble, selection), shift (insertion), split and merge (merge, quick) | passes × work per pass: $n \times n$ or $\log n \times n$ |
| Graph | adjacency matrix ($V \times V$ grid) or adjacency list | BFS = queue (level by level), DFS = stack (go deep, then backtrack) | each vertex and edge touched once → $O(V+E)$ with a list |
| Dijkstra / Prim / Kruskal | graph + a distance/key table | pick the cheapest unfinished item, update its neighbours | $V$ picks × (scan of $V$) = $O(V^2)$ with a table |
| Hashing | array of buckets; key → bucket by $k \bmod m$ | compute the index, probe on collision | $O(1)$ average |

---

## Example flow — copy this rhythm
Three model replies. Diagrams are described in [brackets]; in a session, actually draw them.

**Reply A (opening a fresh session: the trunk)**
> **What this subject is:** how to lay data out in memory and walk through it. Every structure is boxes plus a rule for "next".
> **The one concept that applies everywhere:** three questions.
> | Question | Meaning | Example |
> |---|---|---|
> | WHERE? | how the boxes sit in memory | array = one block; list = scattered boxes joined by arrows |
> | HOW? | the rule for reaching the next box | `i+1`, `p->next`, left/right child |
> | HOW MUCH? | how many boxes the walk touches | every box = $O(n)$; halve each time = $O(\log n)$ |
> [diagram: left, an array of 5 boxes in one row with addresses 1000, 1004, …; right, 5 boxes scattered on the page joined by coral arrows from `head` to NULL]
> Then the topic table (above).
> **Try:** find the 4th element in each. Which one needs a walk? → The array jumps straight to base + 3 × 4 = 1012 ($O(1)$). The list follows 3 arrows from `head` ($O(n)$).

**Bhomik:** "ok so BST is just the list but each box has two arrows?"

**Reply B (confirming his model, then the exam question, diagram-first)**
> "Yes: a BST node is a list node with two arrows, `left` and `right`. One rule is added: smaller keys go left, larger keys go right."
> [diagram: one node box split into three cells, left-ptr | 50 | right-ptr; arrows to 15 (left, labelled "< 50") and 62 (right, labelled "> 50")]
> **ETE 2025, Q7–9:** insert 50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24.
> [diagram: the final BST drawn level by level (50 / 15 62 / 5 20 58 91 / 3 8 37 60 / 24); the path of 24 (50 → 15 → 20 → 37 → left) in coral]
> | Write | Why |
> |---|---|
> | Inorder: 3 5 8 15 20 24 37 50 58 60 62 91 | left–root–right always gives sorted order (a free self-check) |
> **Try:** where does 30 go? → 50 → 15 → 20 → 37 → left child of 37 is 24 → 30 > 24 → **right child of 24**.

**Reply C (AVL, the one rotation that matters: ETE 2026 Q9, step 6)**
> "Insert 21 into 27(9(2, 15), 50). 21 goes 27 → left → 9 → right → 15 → right."
> [diagram: the tree before rotating; BF written beside each node (27: +2, 9: −1, 15: −1); the path 27 → 9 → 15 → 21 in coral, labelled "Left, then Right = LR"]
> One line: "The first unbalanced node walking up is 27. The path from 27 to the new key turns Left then Right, so this is the LR case: left-rotate 9, then right-rotate 27."
> [diagram: before → after; 15 rises to the root with 9 on its left (child 2) and 27 on its right (children 21, 50)]
> **Try:** keys 30, 10, 20. Which case? → 30 → L → 10 → R = **LR**, and the root becomes 20.

**Don't do this (what failed earlier):** a full 9-step solution dumped in one message, no diagram, the topic then called "done". That got "I understood 0 percent of this."

---

## Progress (27 Nov — nothing taught yet)
| Topic | State |
|---|---|
| Trunk recap | not started |
| Q1 BST build + traversals | not started |
| Q2 infix → postfix/prefix | not started |
| Q3 AVL insertion | not started |
| Q4 constructors program | not started |
| Q5 queue programs | not started |
| Q6 linked list insertion / reverse | not started |
| Q7 heap delete / insert | not started |
| Q8 sorting | not started |
| Q9 graph terms + BFS/DFS | not started |
| Q10 Dijkstra | not started |
| Q11 Prim / Kruskal | not started |
| Q12 section A one-liners | not started |
| Q13 output prediction | not started |
| Q14 red-black insertion | not started |
| Q15 Huffman + hashing | not started |

**Next, in order:** trunk → Q1 → Q2 → Q3 → Q4 → Q5 → Q6 → Q7 → Q12 → the rest as time allows.

---

## 0. Books, paper, what repeats

**Books** (hand-out list; truth comes from the book, never from a slide or a solution key):

| Book | Governs |
|---|---|
| **Kanetkar, *Data Structures Through C++* (BPB 2023)**, listed first, and the reference on every deck | everything; his notation for stack/queue/linked list |
| Weiss, *Data Structure and Algorithm Analysis in C++* (2014) | AVL rotations, red-black trees, heaps |
| Balagurusamy, *OOP with C++* (2020) | classes, constructors, destructors |
| Goodrich–Tamassia–Mount (2011), Drozdek (2012) | graphs, sorting, complexity |

**Paper (ECE2240 pattern):** 3 h, 80 marks, no calculator. **ETE 2026:** A = 6 short (3, 3, 2, 2, 3, 3 = 16: constructor vs destructor, array vs linked list, degree, leaf/depth, bubble vs selection, output prediction) · B = 4 × 8 (array queue program, linked-list insertion program, AVL insertion, max-heap delete) · C = 2 × 8 (BST + 3 traversals, infix → prefix and postfix) · D = 1 × 16 (constructor program). **ETE 2025:** A = graph terms (10) · B = BST + 3 traversals + subtree counts (30) · C = two expression conversions (20) · D = queue with a linked list + selection sort program (20). **MTE 2024:** output prediction (2–4 marks each) + reverse a linked list (8).

**What repeats (most marks first):**

| Topic | Marks | Where |
|---|---|---|
| BST: build from a key list, preorder/inorder/postorder | 8–30 | ETE25 B, ETE26 C11; 50Q 32–35, 46–47 |
| Expression conversion (infix ↔ prefix/postfix) | 8–20 | ETE25 C, ETE26 C12; A1 B3, C4; booklet 34–43; 50Q 26–27 |
| Programs: queue (array / linked list), linked-list insertion/reversal, constructors | 8–20 each | every paper; A1 B1, C5, D1, D4 |
| AVL insertion with rotations | 8 | ETE26 B9; booklet 44–53; 50Q 37–39, 49 |
| Max-heap delete-root | 8 | ETE26 B10; booklet 65, 67, 70 |
| Sorting (selection, bubble, insertion; merge/quick/heap ideas) | 3–10 | ETE25 D13, ETE26 A5; booklet 64–76 |
| Short definitions (trees, graphs, ctor/dtor, array vs list) | 2–10 | every section A |
| Graphs: BFS/DFS, Dijkstra, Prim, Kruskal | likely 8 | in no past paper, but **40 booklet questions** + deck 9 slides 71–135 + named in the syllabus |
| Red-black insertion | likely 8 | booklet 54–63; 50Q 40–43, 50; CO3 names it |

---

## Q. Exam question bank — ranked by chance × marks (work top to bottom)

| Rank | Question type | Marks | Seen in | Rote load | Minutes today |
|---|---|---|---|---|---|
| Q1 | BST build + pre/in/post + counts | 8–30 | ETE25, ETE26, 50Q | low | 30 |
| Q2 | Infix → postfix/prefix; evaluate postfix | 8–20 | ETE25, ETE26, A1, booklet | low | 35 |
| Q3 | AVL insertion with rotations | 8 | ETE26, booklet ×10, 50Q | low | 40 |
| Q4 | Constructors program (area) + destructor | 16 | ETE26 D, A1 D1, booklet 1–9 | low | 25 |
| Q5 | Queue: array program, linked-list program, circular idea | 8–20 | ETE26 B7, ETE25 D12, A1 D4 | low | 35 |
| Q6 | Linked list: insertion program; reversal | 8 | ETE26 B8, MTE C8, A1 B1/C5 | low | 30 |
| Q7 | Max heap: delete root / insert | 8 | ETE26 B10, booklet | low | 20 |
| Q8 | Sorting: selection/bubble/insertion + merge/quick | 3–10 | ETE25 D13, ETE26 A5, booklet | med | 35 |
| Q9 | Graph terms, representation, BFS/DFS | 8–10 | ETE25 A, booklet ×10 | low | 30 |
| Q10 | Dijkstra | 8 | booklet ×10, deck 9 | low | 20 |
| Q11 | Prim / Kruskal | 8 | booklet ×20, deck 9 | low | 20 |
| Q12 | Section A one-liners | ~16 | every paper | med | 25 |
| Q13 | Output prediction | 2–4 each | ETE26 A6, MTE | low | 15 |
| Q14 | Red-black insertion | 8 | booklet ×10, 50Q | med | 30 — *only if time is left* |
| Q15 | Huffman code, hashing | 3–5 | syllabus only | med | 15 — *only if time is left* |

Cut today: Python, std::variant lists (booklet 30–33), the airport/parking/lift simulations (A2: too long for a paper), topological sort, B-trees.

---

### Q1. BST: build + traversals (8–30 marks)
**Question (ETE 2025, B, 30 marks):** "Create a Binary Search Tree (BST), generated by inserting in order of the following integers- 50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24, and. Q7 Find Preorder traversal sequence of the above tree? Q8 Find Inorder traversal sequence of the above tree? Q9 Find Post order traversal sequence of the above tree? How many no. of nodes is there in left subtree and right subtree."

**Picture.** A **node** is a box with three cells: a left pointer, a key, and a right pointer. A **pointer** is an arrow holding another box's address. The first key becomes the **root** (the top box). Each new key starts at the root and asks one question per box: smaller → go left, larger → go right. It stops at the first empty arrow (NULL) and hangs there. A **traversal** is a fixed order for visiting every box: **pre**order = root, left, right; **in**order = left, root, right; **post**order = left, right, root. The prefix names *when the root is visited*.

**Diagram spec.**
- [BST level by level: 50 / 15 62 / 5 20 58 91 / 3 8 37 60 / 24. The path of 24 (50 → 15 → 20 → 37 → left) in coral. Left subtree shaded light blue with "7 nodes"; right subtree shaded light green with "4 nodes"]
- [traversal "walk": a dotted line hugging the tree anticlockwise from the root's left side. Mark each node on its left side (pre), underneath (in) and right side (post), in three colours]

**Exam answer.**

| Write | Why |
|---|---|
| Insertion: 50 root; 15 < 50 left; 62 right; 5 left of 15; 20 right of 15; 58 left of 62; 91 right of 62; 3 left of 5; 8 right of 5; 37 right of 20; 60 right of 58; 24 left of 37 | each key compares down from the root, one level per comparison |
| **Preorder: 50 15 5 3 8 20 37 24 62 58 60 91** | root first, then the whole left subtree, then the right |
| **Inorder: 3 5 8 15 20 24 37 50 58 60 62 91** | inorder of a BST is always sorted: check this first |
| **Postorder: 3 8 5 24 37 20 15 60 58 91 62 50** | the root comes last; the last key is always the root |
| **Left subtree: 7 nodes** (15, 5, 3, 8, 20, 37, 24) · **Right subtree: 4 nodes** (62, 58, 60, 91) · total 12 | count each side of the root |
| Height = 5 levels (the deck counts levels in nodes, root = level 1) = 4 edges | the deck's convention: "height = maximum level" |

**Program (ETE 2026 Q11 says "implement a BST").** Keys 45, 36, 76, 23, 89, 115, 98, 39, 41, 56, 69, 48:
```cpp
#include <iostream>
using namespace std;
struct Node { int data; Node *left, *right; };       // one box, two arrows
Node* insert(Node* r, int x) {
    if (r == NULL) {                                  // empty spot found
        r = new Node; r->data = x; r->left = r->right = NULL; return r;
    }
    if (x < r->data) r->left = insert(r->left, x);    // smaller goes left
    else r->right = insert(r->right, x);              // bigger goes right
    return r;
}
void preorder(Node* r)  { if (r) { cout << r->data << " "; preorder(r->left); preorder(r->right); } }   // root, L, R
void inorder(Node* r)   { if (r) { inorder(r->left); cout << r->data << " "; inorder(r->right); } }     // L, root, R
void postorder(Node* r) { if (r) { postorder(r->left); postorder(r->right); cout << r->data << " "; } } // L, R, root
int main() {
    int a[] = {45, 36, 76, 23, 89, 115, 98, 39, 41, 56, 69, 48};
    Node* root = NULL;                                // empty tree
    for (int i = 0; i < 12; i++) root = insert(root, a[i]);
    cout << "Preorder:  "; preorder(root);  cout << "\n";
    cout << "Inorder:   "; inorder(root);   cout << "\n";
    cout << "Postorder: "; postorder(root); cout << "\n";
    return 0;
}
```
Real output:
```
Preorder:  45 36 23 39 41 76 56 48 69 89 115 98
Inorder:   23 36 39 41 45 48 56 69 76 89 98 115
Postorder: 23 41 39 36 48 69 56 98 115 89 76 45
```
Tree: 45 / 36 76 / 23 39 56 89 / 41 (right of 39), 48 69 (children of 56), 115 (right of 89) / 98 (left of 115).

**Trace of `insert` for 41** (state table):

| Step | r (current box) | compare | go |
|---|---|---|---|
| 1 | 45 | 41 < 45 | left |
| 2 | 36 | 41 > 36 | right |
| 3 | 39 | 41 > 39 | right |
| 4 | NULL | — | new box 41 = right child of 39 |

**HOW MUCH (derive it):** each comparison drops one level. A balanced tree with $n$ nodes has about $\log_2 n$ levels (each level doubles the count: $1 + 2 + 4 + \dots = 2^h - 1$), so search/insert = $O(\log n)$. If the keys arrive sorted, every key goes right, the tree is a list, and the cost is $O(n)$. That is why AVL exists (Q3).

**Deletion (50Q 35, 47; one line per case):** leaf → just remove it · one child → the child takes its place · two children → replace the key with its **inorder successor** (the smallest key in the right subtree: go right once, then left all the way), then delete that successor.

**Try:**
1. ETE 2025 tree: delete 15. → 15 has two children; successor = 20 (right once, no left child). Result: 50 / 20 62 / 5 37 58 91 / 3 8 24 60.
2. 50Q 33: insert 45, 25, 65, 15, 35, 55, 75, 10, 20, 30, 40, 50, 60, 70, 80, 5, 18. Min, max, height? → **min 5, max 80, height 4 edges (5 levels)**; 5 and 18 sit on level 5 (5 = left of 10, 18 = left of 20).

---

### Q2. Infix → postfix / prefix (8–20 marks)
**Question (ETE 2026 C12, 8 marks):** "A deep-space AI system computes warp-speed travel paths using prefix notation. Convert the following infix expression to prefix and postfix: ((A + B × C)(D − E / (F + G))) × (H + I / (J − K × L))"

**Picture.** **Infix** puts the operator between its operands (A + B). **Postfix** puts it after (A B +), and **prefix** puts it before (+ A B). Postfix needs no brackets because the order of the symbols is the order of the work. The tool is a **stack** of operators, a pile you only touch at the top. Operands go straight to the output. An operator waits on the stack until something weaker arrives. **Precedence** (who binds tighter): ^ > × / > + −; equal precedence pops left to right (^ is the exception: right to left). A `(` is a wall; a `)` pops everything down to its `(`.

**Diagram spec.**
- [expression tree for the ETE26 expression: root ×; left child × (the implicit multiply between the two brackets) with subtrees + (A, × (B, C)) and − (D, / (E, + (F, G))); right child + (H, / (I, − (J, × (K, L))))]
- [beside the tree: three arrows round the same tree. Visit order root-first = prefix, root-last = postfix]
- State table for a small one: [A+B*C−D: columns symbol | stack | output, as below]

**Exam answer (method 1 — fully bracket, move the operators; fastest by hand):**

| Write | Why |
|---|---|
| Note: `)(` between the two brackets means multiplication | missing data "assumed suitably" (paper instruction) |
| **Postfix: A B C × + D E F G + / − × H I J K L × − / + ×** | each operator moves to just after its two operands, innermost first |
| **Prefix: × × + A × B C − D / E + F G + H / I − J × K L** | each operator moves to just before its two operands |
| Check: postfix has 12 operands and 11 operators | an expression with $n$ operands always has $n - 1$ binary operators |

**Method 2 — the stack algorithm, which the professor asks for as "show the operator stack at each step" (A1 B3, 50Q 26).** (A + B) × (C − D) / E:

| Symbol | Stack (bottom → top) | Output |
|---|---|---|
| ( | ( | |
| A | ( | A |
| + | ( + | A |
| B | ( + | A B |
| ) | — | A B + |
| × | × | A B + |
| ( | × ( | A B + |
| C | × ( | A B + C |
| − | × ( − | A B + C |
| D | × ( − | A B + C D |
| ) | × | A B + C D − |
| / | / | A B + C D − × *(× pops: equal precedence, left first)* |
| E | / | A B + C D − × E |
| end | — | **A B + C D − × E /** |

Prefix of the same: **/ × + A B − C D E**. (Prefix by stack: reverse the infix, swap the ( and ), take the postfix, then reverse it.)

**Postfix evaluation (A1 C4; 50Q 27):** an operand is pushed; an operator pops two (the **first pop is the right operand**), computes, and pushes the result. 8 3 2 × + 5 1 − /:

| Symbol | Stack |
|---|---|
| 8, 3, 2 | 8 3 2 |
| × | 8 6 |
| + | 14 |
| 5, 1 | 14 5 1 |
| − | 14 4 |
| / | **3.5** |

A1: 12 3 4 × + 6 2 / − → 12 12 → 24 → 24 3 → **21**.

**Logical expression (ETE 2025 C10):** ((!(A && !((B < C) || (C > D))) || (C < E)) && (F && G || H || I)). Precedence: `!` (unary, takes one operand) > `<` `>` > `&&` > `||`.
- **Postfix:** A B C < C D > || ! && ! C E < || F G && H || I || &&
- **Prefix:** && || ! && A ! || < B C > C D < C E || || && F G H I

**Trap (ETE 2025 C11):** "Convert the postfix expression +AB^CD*EF+GH*I/J+KL-MN+OP/ to infix and prefix." As printed this is **not valid postfix**: the first symbol is an operator with nothing on the stack. It is not valid prefix either: + A B is complete after 3 symbols. Write that sentence, then show the method on the part that is well formed. The marks are for the method.

**HOW MUCH:** each symbol is pushed and popped at most once → $O(n)$.

**Try** (booklet 34, 36; numbers stay as operands):
1. (20 + 5 × (8 − 3)) / (6 + 2) → postfix **20 5 8 3 − × + 6 2 + /** · prefix **/ + 20 × 5 − 8 3 + 6 2** · value **5.625**.
2. 100 / 5 × (4 + 2) − (8 / 2 + 3) → postfix **100 5 / 4 2 + × 8 2 / 3 + −** · prefix **− × / 100 5 + 4 2 + / 8 2 3** · value **113**.

---

### Q3. AVL insertion (8 marks)
**Question (ETE 2026 B9):** "Show the AVL tree that results after each of the integer keys 9, 27, 50, 15, 2, 21, and 36 are inserted, in that order, into an initially empty AVL tree. Clearly show the tree that results after each insertion, and make clear any rotations that must be performed."

**Picture.** An **AVL tree** is a BST that refuses to lean. Every node carries a **balance factor** (BF) = height of its left subtree − height of its right subtree. The rule is BF ∈ {−1, 0, +1}. Insert exactly as in a BST. Then walk back up from the new node: the **first** node whose BF hits ±2 is the one to fix. Read the first two turns of the path from that node down to the new key: that names the case. A **rotation** is a three-node swap that keeps the inorder order and lifts the middle key up.

| Path from the unbalanced node | Case | Fix |
|---|---|---|
| Left, Left | LL | right-rotate the node |
| Right, Right | RR | left-rotate the node |
| Left, Right | LR | left-rotate the child, then right-rotate the node |
| Right, Left | RL | right-rotate the child, then left-rotate the node |

(Derive, don't memorise: a straight line of 3 needs one rotation; a zig-zag first gets straightened into a line.)

**Diagram spec.** One small tree per insertion, BF beside each node, with the rotation drawn as before → after:
- [+50: 9 → 27 → 50 in a straight right line, BF(9) = −2, labelled RR → after: 27 (9, 50)]
- [+21: 27(9(2, 15(−, 21)), 50), BF(27) = +2, BF(9) = −1, path L-R in coral → after left-rotate 9: 27(15(9(2), 21), 50) → after right-rotate 27: 15(9(2), 27(21, 50))]
- [+36: 15(9(2), 27(21, 50(36))); BF table: 15 = −1, 9 = +1, 27 = −1, 50 = +1 → all legal, no rotation]

**Exam answer (state table, one row per insertion):**

| Insert | Tree after (level by level) | Rotation |
|---|---|---|
| 9 | 9 | none |
| 27 | 9 / 27 | none |
| 50 | 27 / 9 50 | **RR at 9 → left-rotate 9** |
| 15 | 27 / 9 50 / 15 (right of 9) | none (BF 27 = +1) |
| 2 | 27 / 9 50 / 2 15 | none |
| 21 | 15 / 9 27 / 2 21 50 | **LR at 27 → left-rotate 9, then right-rotate 27** |
| 36 | 15 / 9 27 / 2 21 50 / 36 (left of 50) | **none** |

| Write | Why |
|---|---|
| Final AVL tree: root 15; 9 (left child 2); 27 (children 21, 50); 36 = left child of 50 | |
| BF: 15 = −1, 9 = +1, 27 = −1, 50 = +1, leaves 0 → AVL property holds | write the BF of every node: it's the proof |
| Inorder 2 9 15 21 27 36 50 (sorted ✓) | rotations never break BST order |

**Trap:** the circulating "with solutions" key for this paper rotates again at step 7 ("RL at 27"). That is wrong. After inserting 36, 27 has a left height of 1 and a right height of 2, so BF = −1, which is legal. Its final tree (15 / 9 36 / 2 27 50 / 21) is still a valid AVL tree, but it isn't the result of the algorithm, and the rotation it shows wouldn't earn marks. Don't copy it.

**HOW MUCH:** the rotation keeps the height at about $1.44 \log_2 n$, so search/insert/delete stay $O(\log n)$. A plain BST fed sorted keys degrades to $O(n)$.

**Try:**
1. 10, 20, 30, 40, 50, 25 → +30: **RR at 10** → 20(10, 30); +50: **RR at 30** → 20(10, 40(30, 50)); +25: **RL at 20** (right-rotate 40, then left-rotate 20) → **30 / 20 40 / 10 25 50**.
2. Booklet 44 (24, 12, 36, 8, 16, 30, 42, 4, 10, 14, 20, 28, 34): which insertion rotates? → **None.** The list is already in level order (root, then level 2, then level 3…), so the tree is never off balance. Final BF: 36 = +1, every other node 0. This is the trick in all ten booklet AVL questions (44–53) and in 50Q 37 and 38. Say it, show the BF table, and you're done.

---

### Q4. Constructors program (16 marks)
**Question (ETE 2026 D13, 16 marks):** "Design and implement a system program to calculate the area of a rectangle and display it using default Constructor, parameterized constructor, constructor overloading and destructor in C++ suitably." (A1 D1 is the same with a triangle.)

**Picture.** A **class** is a blueprint (a form with empty fields); an **object** is one filled-in copy. A **constructor** is a member function with the class's own name and **no return type**. It runs by itself the moment an object is created, to fill the fields. **Default** = takes no arguments. **Parameterized** = takes values. **Overloading** = several constructors with the same name and different argument lists; the compiler picks one by the arguments. A **destructor** is `~ClassName()`: no arguments, one per class. It runs by itself when the object dies (at the end of its block) to release resources. Objects die in the **reverse** order of creation (a stack).

**Diagram spec.**
- [class box "Rectangle": fields length, breadth; methods Rectangle(), Rectangle(l, b), Rectangle(s), area(), ~Rectangle(). Three arrows from it to object boxes r1 (1×1), r2 (10×5), r3 (4×4), each arrow labelled with the constructor it called]
- [timeline: creation r1 → r2 → r3 left to right; destruction r3 → r2 → r1 right to left at "}" (stack order)]

**Exam answer.**

| Write | Why |
|---|---|
| A constructor initialises an object automatically when it's created; same name as the class, no return type, can be overloaded | the definitions are the first marks |
| A destructor (~ + class name) runs automatically when the object goes out of scope; no arguments, no return type, cannot be overloaded | |
| Program (below) + its output | |
| Constructor overloading = same name, different parameter lists; chosen at compile time | that's why `Rectangle r3(4)` picks the one-argument version |

```cpp
#include <iostream>
using namespace std;
class Rectangle {
    float length, breadth;                       // private data (encapsulation)
public:
    Rectangle() {                                // default constructor
        length = 1; breadth = 1;
        cout << "Default constructor called\n";
    }
    Rectangle(float l, float b) {                // parameterized constructor
        length = l; breadth = b;
        cout << "Parameterized constructor called\n";
    }
    Rectangle(float s) {                         // overloaded: one argument = square
        length = s; breadth = s;
        cout << "One-argument constructor called\n";
    }
    float area() { return length * breadth; }    // the actual work
    void display() { cout << "Length = " << length << ", Breadth = " << breadth
                          << ", Area = " << area() << "\n"; }
    ~Rectangle() {                               // destructor
        cout << "Destructor called for " << length << " x " << breadth << "\n";
    }
};
int main() {
    Rectangle r1;            // calls the default constructor
    Rectangle r2(10, 5);     // calls the parameterized constructor
    Rectangle r3(4);         // calls the overloaded one-argument constructor
    r1.display(); r2.display(); r3.display();
    return 0;                // destructors run here: r3, r2, r1
}
```
Real output:
```
Default constructor called
Parameterized constructor called
One-argument constructor called
Length = 1, Breadth = 1, Area = 1
Length = 10, Breadth = 5, Area = 50
Length = 4, Breadth = 4, Area = 16
Destructor called for 4 x 4
Destructor called for 10 x 5
Destructor called for 1 x 1
```

**Try:**
1. Add `Rectangle r4(r2);`. Which constructor runs, and what does it print? → The compiler's **copy constructor**. It prints no message, but r4 gets 10 × 5. Its destructor prints first at exit: "Destructor called for 10 x 5".
2. Triangle version (A1 D1): what changes? → the fields become base and height; area = 0.5 × base × height; the overloading example becomes `area(b, h)` vs `area(a, b, c)` (Heron's formula), i.e. **function overloading**, which A1 asks for.

---

### Q5. Queue programs (8–20 marks)
**Question (ETE 2026 B7 = A1 D4, 8 marks):** "Write a C++ program to implement a queue using an array. The program must be able to add and delete the data from the queue."
**Question (ETE 2025 D12):** "Write a user-friendly program to implement a queue in C++ using link list. The program should have member functions for insertion, deletion and display the contents of a queue."

**Picture.** A **queue** is a line at a counter: you join at the **rear** and leave from the **front**. That is **FIFO**, first in, first out. In an array, two integer indices track the ends: `rear` moves right on every insert, and `front` moves right on every delete. **Overflow** = inserting when no space is left; **underflow** = deleting from an empty queue. In a linked list, `front` and `rear` are pointers to the first and last boxes. There is no fixed size, so there's no overflow while memory lasts.

**Diagram spec.**
- [array of 5 boxes, indices 0–4; state after the run below: box 0 greyed "used and wasted", boxes 1–4 = 20 30 40 50; arrows front → 1, rear → 4; red note "rear = 4 = MAX − 1 → 'full' although box 0 is free"]
- [circular version: the same 5 boxes bent into a ring; rear wraps 4 → 0 with the label "rear = (rear + 1) % 5"]
- [linked queue: front → [10|•] → [20|•] → [30|NULL] ← rear; insert = a new box after rear (coral); delete = front moves one box right (dashed old arrow)]

**Exam answer — array queue:**
```cpp
#include <iostream>
using namespace std;
#define MAX 5                         // size of the array that holds the queue
class Queue {
    int a[MAX];                       // the boxes
    int front, rear;                  // front = next to leave, rear = last to join
public:
    Queue() { front = -1; rear = -1; }               // empty queue
    void enqueue(int x) {
        if (rear == MAX - 1) { cout << "Queue full (overflow)\n"; return; }
        if (front == -1) front = 0;                   // first element ever
        a[++rear] = x;                                // move rear, then store
        cout << x << " added\n";
    }
    void dequeue() {
        if (front == -1 || front > rear) { cout << "Queue empty (underflow)\n"; return; }
        cout << a[front++] << " deleted\n";           // read front, then move it
    }
    void display() {
        if (front == -1 || front > rear) { cout << "Queue empty\n"; return; }
        cout << "Queue: ";
        for (int i = front; i <= rear; i++) cout << a[i] << " ";   // front to rear
        cout << "\n";
    }
};
int main() {
    Queue q; int ch, x;
    do {                                              // menu = "user friendly"
        cout << "1.Add 2.Delete 3.Display 4.Exit: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Value: "; cin >> x; q.enqueue(x); break;
            case 2: q.dequeue(); break;
            case 3: q.display(); break;
        }
    } while (ch != 4);
    return 0;
}
```
Real run (inputs: add 10, 20, 30; delete; display; add 40, 50, 60; delete ×4; display):

| Action | Printed | front | rear | Array |
|---|---|---|---|---|
| add 10, 20, 30 | 10 added · 20 added · 30 added | 0 | 2 | 10 20 30 _ _ |
| delete | 10 deleted | 1 | 2 | (10) 20 30 _ _ |
| display | Queue: 20 30 | 1 | 2 | |
| add 40, 50 | 40 added · 50 added | 1 | 4 | (10) 20 30 40 50 |
| add 60 | **Queue full (overflow)** | 1 | 4 | box 0 is free but unusable |
| delete ×4 | 20 deleted · 30 deleted · 40 deleted · 50 deleted | 5 | 4 | |
| display | Queue empty | | | |

**Why circular (50Q 29, A1 A6):** the "add 60" row shows the waste. A linear queue never reuses a box behind `front`. A **circular queue** moves with `rear = (rear + 1) % MAX` and `front = (front + 1) % MAX`, so after index 4 it wraps to 0. It is full when `(rear + 1) % MAX == front`.

**Exam answer — linked-list queue (ETE 2025 D12):**
```cpp
#include <iostream>
using namespace std;
struct Node { int data; Node* next; };               // one box
class Queue {
    Node *front, *rear;              // front = leaves first, rear = joined last
public:
    Queue() { front = rear = NULL; }                  // empty
    void insert(int x) {             // enqueue at rear
        Node* t = new Node; t->data = x; t->next = NULL;
        if (rear == NULL) front = rear = t;           // first node is both ends
        else { rear->next = t; rear = t; }            // link after rear, move rear
        cout << x << " inserted\n";
    }
    void remove() {                  // dequeue from front
        if (front == NULL) { cout << "Queue empty (underflow)\n"; return; }
        Node* t = front;
        cout << t->data << " deleted\n";
        front = front->next;                          // move front forward
        if (front == NULL) rear = NULL;               // queue became empty
        delete t;                                     // free the old box
    }
    void display() {
        if (front == NULL) { cout << "Queue empty\n"; return; }
        cout << "Queue: ";
        for (Node* p = front; p != NULL; p = p->next) cout << p->data << " ";
        cout << "\n";
    }
};
int main() {
    Queue q; int ch, x;
    do {
        cout << "1.Insert 2.Delete 3.Display 4.Exit: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Value: "; cin >> x; q.insert(x); break;
            case 2: q.remove(); break;
            case 3: q.display(); break;
        }
    } while (ch != 4);
    return 0;
}
```
Real run (insert 10, 20, 30; display; delete; display; delete ×3): `10 inserted`, `20 inserted`, `30 inserted`, `Queue: 10 20 30`, `10 deleted`, `Queue: 20 30`, `20 deleted`, `30 deleted`, `Queue empty (underflow)`.

**HOW MUCH:** insert and delete touch one box each → $O(1)$; display walks all $n$ → $O(n)$.

**Try:**
1. 50Q 28: enqueue 11, 22, 33, 44; dequeue twice; enqueue 55, 66 (array starting at index 0, MAX large). front, rear? → **front = 2 (33), rear = 5 (66)**; the queue is 33 44 55 66.
2. Capacity 5, circular, after the table above (front = 1, rear = 4): add 60 → **rear = (4 + 1) % 5 = 0**; 60 goes into box 0. Full now? (0 + 1) % 5 = 1 = front → **yes, full**.

---

### Q6. Linked list: insertion and reversal (8 marks each)
**Question (ETE 2026 B8 = A1 C5):** "Write a C++ program to implement linked list insertion."
**Question (MTE 2024 C8):** "Write a program to create a singly linked list and reverse the list by interchanging the links and not the data."

**Picture.** A **singly linked list** is boxes scattered anywhere in memory. Each box (node) holds **data** + **next**, the address of the following box. `head` points to the first box; the last box's `next` is **NULL** (points nowhere). To insert, you never move data: you **rewire two arrows**. The order matters: point the new box at its successor first, then point the predecessor at the new box. Done the other way round, you lose the rest of the list.

**Diagram spec.**
- [list 12 → 24 → 36 → 48 → 60 → NULL; insert 6 at the beginning: new box 6 with a coral arrow to 12, and head's arrow moved to 6 (old head arrow dashed)]
- [insert 42 after 36: new box 42 under the list; ① coral arrow 42 → 48 labelled "first"; ② coral arrow 36 → 42 labelled "then"; old arrow 36 → 48 dashed]
- [reversal: 4 boxes; three pointer labels prev / curr / nxt under them; four frames showing each arrow flipping to point left]

**Exam answer — insertion:**
```cpp
#include <iostream>
using namespace std;
struct Node {                         // one box: data + arrow to the next box
    int data;
    Node* next;
};
Node* head = NULL;                    // arrow to the first box (NULL = empty list)
void insertBegin(int x) {
    Node* t = new Node;               // make a new box
    t->data = x;
    t->next = head;                   // new box points to old first box
    head = t;                         // head now points to new box
}
void insertEnd(int x) {
    Node* t = new Node;
    t->data = x; t->next = NULL;      // last box points to nothing
    if (head == NULL) { head = t; return; }
    Node* p = head;
    while (p->next != NULL) p = p->next;   // walk to the last box
    p->next = t;                      // old last box points to new box
}
void insertAfter(int key, int x) {
    Node* p = head;
    while (p != NULL && p->data != key) p = p->next;   // find the box holding key
    if (p == NULL) { cout << key << " not found\n"; return; }
    Node* t = new Node;
    t->data = x;
    t->next = p->next;                // FIRST: new box points to p's old next
    p->next = t;                      // THEN: p points to new box
}
void display() {
    for (Node* p = head; p != NULL; p = p->next) cout << p->data << " -> ";
    cout << "NULL\n";
}
int main() {
    insertEnd(12); insertEnd(24); insertEnd(36); insertEnd(48); insertEnd(60);
    display();
    insertBegin(6);       display();
    insertAfter(36, 42);  display();
    insertEnd(72);        display();
    return 0;
}
```
Real output (this is also 50Q 23):
```
12 -> 24 -> 36 -> 48 -> 60 -> NULL
6 -> 12 -> 24 -> 36 -> 48 -> 60 -> NULL
6 -> 12 -> 24 -> 36 -> 42 -> 48 -> 60 -> NULL
6 -> 12 -> 24 -> 36 -> 42 -> 48 -> 60 -> 72 -> NULL
```

**Exam answer — reversal (the core function; the rest is the same as above):**
```cpp
void reverse() {
    Node *prev = NULL, *curr = head, *nxt;
    while (curr != NULL) {
        nxt = curr->next;      // 1. save the rest of the list
        curr->next = prev;     // 2. flip this arrow backwards
        prev = curr;           // 3. step prev forward
        curr = nxt;            // 4. step curr forward
    }
    head = prev;               // last box is the new first box
}
```
Real output on 10, 20, 30, 40: `10 -> 20 -> 30 -> 40 -> NULL` then `40 -> 30 -> 20 -> 10 -> NULL`.

State table:

| Loop | prev | curr | nxt | Arrow flipped |
|---|---|---|---|---|
| start | NULL | 10 | — | |
| 1 | 10 | 20 | 20 | 10 → NULL |
| 2 | 20 | 30 | 30 | 20 → 10 |
| 3 | 30 | 40 | 40 | 30 → 20 |
| 4 | 40 | NULL | NULL | 40 → 30 |
| end | head = 40 | | | |

**HOW MUCH:** insert at the beginning = 2 arrow writes → $O(1)$. Insert at the end or after a key = a walk → $O(n)$. Reverse = one pass → $O(n)$ time, $O(1)$ extra space.

**Array vs linked list (ETE 2026 A2, 3 marks; 50Q 22):**

| Write | Why (from the picture) |
|---|---|
| Memory: array contiguous, fixed size · list scattered, grows at run time | one block vs separate boxes |
| Access: array $O(1)$ by index · list $O(n)$ | address = base + i × size vs following arrows |
| Insert/delete: array $O(n)$ (shift) · list $O(1)$ once the spot is found | moving the tail vs rewiring 2 arrows |
| Extra memory: array none · list one pointer per node | the `next` field |

**Try:**
1. Delete the node after 36 in 6 → 12 → 24 → 36 → 42 → 48. Which single assignment? → `p->next = p->next->next;` (with p at 36), then `delete` the old box 42.
2. Swap the two lines in `insertAfter` (`p->next = t;` first). What breaks? → `t->next = p->next` then copies `t` itself, so 42 points to itself and **48 onwards is lost**.

---

### Q7. Max heap: delete root / insert (8 marks)
**Question (ETE 2026 B10):** "Consider the above max heap. Delete root node (90) from the max heap and draw the final balanced max heap. Show all the necessary steps." Heap: 90 / 89 70 / 36 85 63 65 / 21 18 15 75 (21, 18 under 36; 15, 75 under 85).

**Picture.** A **heap** is a **complete binary tree**: every level is full except the last, which fills left to right. In a **max heap**, every parent ≥ its children, so the largest key sits at the root. Being complete, it lives in a plain array with no pointers: the node at index $i$ (counting from 0) has children at $2i + 1$ and $2i + 2$, and its parent at $(i - 1)/2$. **Delete** always removes the root: move the **last** element to the root, then **sift down** (swap with the larger child until both children are smaller). **Insert:** append at the end, then **sift up** (swap with the parent while bigger).

**Diagram spec.**
- [array row: index 0–10 = 90 89 70 36 85 63 65 21 18 15 75, with curved arrows from index 1 to 3 and 4 labelled "2i+1, 2i+2"]
- [4 frames: (1) 75 moved to the root, last box crossed out; (2) 75 vs children 89, 70 → swap with 89 (coral); (3) 75 vs children 36, 85 → swap with 85; (4) 75 vs child 15 → stop. Final tree highlighted]

**Exam answer.**

| Step | Array (index 0 → 9) | Why |
|---|---|---|
| Remove 90; move last (75) to the root | 75 89 70 36 85 63 65 21 18 15 | keeps the tree complete |
| 75 < larger child 89 → swap | 89 75 70 36 85 63 65 21 18 15 | the larger child must rise, or it would sit below a smaller parent |
| 75 < larger child 85 → swap | 89 85 70 36 75 63 65 21 18 15 | |
| 75 vs child 15 → stop | **89 85 70 36 75 63 65 21 18 15** | heap property holds everywhere |

| Write | Why |
|---|---|
| Final max heap: 89 / 85 70 / 36 75 63 65 / 21 18 15 | 10 nodes, complete |

**HOW MUCH:** one swap per level and $\log_2 n$ levels → $O(\log n)$. **Heap sort** = build the heap, then delete the root $n$ times, each removed root going to the end of the array → $O(n \log n)$.

**Try:** insert 95 into the original heap. → Append at index 11 (child of 63) → swap with 63 → swap with 70 → swap with 90 → **95 / 89 90 / 36 85 70 65 / 21 18 15 75 63**.

---

### Q8. Sorting (3–10 marks)
**Question (ETE 2025 D13):** "How Selection Sort works? Write a user-friendly program to implement the Selection Sort in C++. Explain application of Selection Sort?" **(ETE 2026 A5, 3 marks):** "What is the Bubble sort and how it differs from Selection Sort?"

**Picture.** All the simple sorts split the array into a **sorted part** and an **unsorted part**, and each pass grows the sorted part by one. **Selection** scans the unsorted part for the minimum and makes one swap per pass. **Bubble** compares neighbours and swaps them when they're out of order, so the largest "bubbles" to the end each pass. **Insertion** takes the next card and shifts larger ones right to slot it in, like sorting a hand of cards. **Merge** splits in half until single items remain, then merges sorted halves. **Quick** picks a **pivot**, puts smaller keys left and larger keys right, then repeats on each side.

**Diagram spec.**
- [selection sort on 64 25 12 22 11: 4 rows (one per pass); the sorted prefix shaded green; the min found in coral; a curved swap arrow]
- [merge sort tree: 64 25 12 22 11 90 split → [64 25 12] [22 11 90] → singles → merged back up level by level]

**Exam answer — selection sort:**
```cpp
#include <iostream>
using namespace std;
int main() {
    int a[] = {64, 25, 12, 22, 11};
    int n = 5;
    for (int i = 0; i < n - 1; i++) {             // pass i fixes position i
        int min = i;                               // assume a[i] is smallest
        for (int j = i + 1; j < n; j++)            // scan the unsorted part
            if (a[j] < a[min]) min = j;            // remember the smaller one
        int t = a[i]; a[i] = a[min]; a[min] = t;   // one swap per pass
        cout << "Pass " << i + 1 << ": ";
        for (int k = 0; k < n; k++) cout << a[k] << " ";
        cout << "\n";
    }
    return 0;
}
```
Real output:
```
Pass 1: 11 25 12 22 64
Pass 2: 11 12 25 22 64
Pass 3: 11 12 22 25 64
Pass 4: 11 12 22 25 64
```
(For a "user-friendly" version, read `n` and the elements with `cin` first; the logic is unchanged.)

**Application (write this):** small lists; cases where writes are expensive (it makes at most $n - 1$ swaps, e.g. flash/EEPROM memory); simple embedded code.

**Bubble vs selection (3 marks):**

| Write | Why |
|---|---|
| Bubble swaps adjacent pairs repeatedly; selection finds the minimum and swaps once per pass | the picture |
| Swaps: bubble up to $n(n-1)/2$; selection at most $n - 1$ | one swap per pass |
| Best case: bubble with a `swapped` flag is $O(n)$ on sorted input; selection is always $O(n^2)$ | selection always scans everything |
| Bubble is stable; selection is not | the long-distance swap can jump over an equal key |

**Real traces** (program `p9_sorts.cpp`, booklet arrays):
- Bubble 29 10 14 37 13 5: pass 1 → 10 14 29 13 5 **37** · pass 2 → 10 14 13 5 **29 37** · pass 3 → 10 13 5 **14 29 37** · pass 4 → 10 5 **13 14 29 37** · pass 5 → **5 10 13 14 29 37**.
- Insertion 78 45 92 67 56 84: 45 78 | 92 … → 45 78 92 | … → 45 67 78 92 | … → 45 56 67 78 92 | 84 → **45 56 67 78 84 92**.
- Quick 42 17 63 8 31 25 (last element = pivot): pivot 25 → 17 8 **25** 42 31 63 · pivot 8 → **8** 17 … · pivot 63 → … **63** · pivot 31 → 8 17 25 **31** 42 63.
- Merge 64 25 12 22 11 90: [25 64] → [12 25 64] · [11 22] → [11 22 90] → **11 12 22 25 64 90**.

**HOW MUCH (derive):** the simple sorts do $n - 1$ passes, each scanning up to $n$ → $$\frac{n(n-1)}{2} = O(n^2)$$ Merge sort halves the list $\log_2 n$ times, and each level of merging touches all $n$ items → $O(n \log n)$, with $O(n)$ extra array. Quick sort is $O(n \log n)$ on average, but **$O(n^2)$ worst** when the pivot is always the smallest or largest (already-sorted input with a last-element pivot).

**Try:** selection sort in **descending** order (booklet 72): which line changes? → `if (a[j] > a[min])` (find the maximum). 34 12 56 8 45 21 → **56 45 34 21 12 8**.

---

### Q9. Graph terms, representation, BFS/DFS (8–10 marks)
**Question (ETE 2025 A, 10 marks):** "Explain the following terms vertex, edge, degree, path, and cycle in graphs." **(Booklet 107):** "perform BOTH Breadth-First Search (BFS) and Depth-First Search (DFS), starting from vertex A … write the order … show the queue/stack … draw the resulting spanning tree."

**Picture.** A **graph** G = (V, E) is a set of dots (**vertices**) joined by lines (**edges**). A tree is a graph with no cycles. **Degree** of a vertex = the number of edges touching it (in a directed graph: **in-degree** = arrows coming in, **out-degree** = arrows going out). A **path** = a sequence of vertices, each joined to the next by an edge. A **cycle** = a path that starts and ends at the same vertex. Stored as an **adjacency matrix** (a V × V grid, 1 or the weight where an edge exists) or an **adjacency list** (each vertex keeps a linked list of its neighbours). **BFS** explores like ripples: a **queue**, nearest first. **DFS** explores like a maze walker: a **stack**, go deep, back up at dead ends.

**Graph G1 (booklet Q103; also used in Q10):** edges A–B 5, A–C 2, B–C 1, B–D 6, C–D 4, C–E 8, D–E 2, D–F 7, E–F 3, E–G 6, F–G 1. Neighbours are taken in alphabetical order.

**Diagram spec.**
- [G1 drawn as in the booklet: A on the left; B, D top; C, E bottom; F, G right; weights on the edges]
- [BFS: the same graph with the BFS tree edges in coral (A–B, A–C, B–D, C–E, D–F, E–G) and level rings 0 | 1 | 2 | 3]
- [DFS: tree edges in coral forming one long path A–B–C–D–E–F–G; the back-edges dashed grey]

**Exam answer — terms (2 marks each):**

| Term | Write |
|---|---|
| Vertex | a node of the graph; it represents an item (city, computer) |
| Edge | a connection (u, v) between two vertices; directed or undirected, possibly weighted |
| Degree | the number of edges incident on a vertex; directed: in-degree + out-degree. Sum of all degrees = 2 × number of edges |
| Path | a sequence of vertices v1, v2, …, vk with an edge between each consecutive pair; *simple* if no vertex repeats |
| Cycle | a path whose first and last vertices are the same; *simple* if nothing else repeats |

**BFS from A** (state table):

| Visit | Queue after (front → rear) | Tree edges added |
|---|---|---|
| A | B C | A–B, A–C |
| B | C D | B–D |
| C | D E | C–E |
| D | E F | D–F |
| E | F G | E–G |
| F | G | |
| G | empty | |

**BFS order: A B C D E F G.**

**DFS from A** (stack = the current path):

| Visit | Stack (bottom → top) |
|---|---|
| A | A |
| B (first unvisited neighbour of A) | A B |
| C (of B) | A B C |
| D (of C) | A B C D |
| E (of D) | A B C D E |
| F (of E) | A B C D E F |
| G (of F) | A B C D E F G |
| backtrack × 7 | empty |

**DFS order: A B C D E F G.** Tree edges: A–B, B–C, C–D, D–E, E–F, F–G. Same order as BFS here, but a **different tree**: BFS is wide and shallow, DFS is one deep path.

**HOW MUCH:** each vertex enters the queue/stack once and each edge is checked once (twice when undirected) → $O(V + E)$ with an adjacency list. With a matrix, finding the neighbours means scanning a whole row → $O(V^2)$. Matrix memory $V^2$; list memory $V + 2E$.

**Try:** an undirected graph has degrees 3, 2, 2, 3. How many edges? → $(3 + 2 + 2 + 3)/2 =$ **5**.

---

### Q10. Dijkstra's shortest path (8 marks)
**Question (booklet 103):** "Apply Dijkstra's algorithm with source vertex A to find the shortest path from A to every other vertex. Show the distance table after each iteration and draw the final shortest-path tree." (Graph G1 above.)

**Picture.** Every vertex carries a label: the best distance from A found so far. Start with A = 0 and all others ∞. Each round: **pick the unfinished vertex with the smallest label**; it is now final, because every other route would start from a bigger label. Then **relax** its edges: if label(u) + weight < label(v), lower v's label and record u as its parent. Repeat until all are final. This only works with non-negative weights.

**Diagram spec.**
- [G1 with the final labels in boxes beside each vertex (A 0, B 3, C 2, D 6, E 8, F 11, G 12); shortest-path tree edges in coral: A–C, C–B, C–D, D–E, E–F, F–G]

**Exam answer (* = final):**

| Pick | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| start | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| A | 0* | 5 | 2 | ∞ | ∞ | ∞ | ∞ |
| C | 0* | **3** | 2* | 6 | 10 | ∞ | ∞ |
| B | 0* | 3* | 2* | 6 | 10 | ∞ | ∞ |
| D | 0* | 3* | 2* | 6* | **8** | 13 | ∞ |
| E | 0* | 3* | 2* | 6* | 8* | **11** | 14 |
| F | 0* | 3* | 2* | 6* | 8* | 11* | **12** |
| G | 0* | 3* | 2* | 6* | 8* | 11* | 12* |

| Write | Why |
|---|---|
| Paths: B = A–C–B (3) · C = A–C (2) · D = A–C–D (6) · E = A–C–D–E (8) · F = A–C–D–E–F (11) · G = A–C–D–E–F–G (12) | follow the parents back from each vertex |
| B dropped from 5 to 3 via C | the direct edge isn't always the shortest: that's the whole point |

**HOW MUCH:** V rounds × a scan of V labels → $O(V^2)$ with a table ($O((V + E) \log V)$ with a heap).

**Try:** in the row after picking C, why did D get 6 and not 6 via B (= 3 + 6 = 9)? → B wasn't final yet; when B is picked, 9 > 6, so no change.

---

### Q11. Minimum spanning tree: Prim and Kruskal (8 marks)
**Question (booklet 77):** "Apply Prim's algorithm to the weighted graph, starting from vertex A … Then draw/list the final MST and calculate its total weight." **(Booklet 87–96):** the same with Kruskal: "Clearly mark each edge as ACCEPTED or REJECTED".

**Graph G2 (booklet Q77 figure):** A–B 16, A–C 9, B–F 10, B–C 7, B–D 25, C–F 8, E–F 5, C–E 15, C–D 14.

**Picture.** A **spanning tree** keeps all V vertices and only V − 1 edges, with no cycle. The **minimum** spanning tree (MST) is the one with the least total weight (e.g. the cheapest cable to connect every town). **Prim** grows one tree from a start vertex: always add the cheapest edge leaving the tree. **Kruskal** sorts all the edges, takes them cheapest first, and **rejects any edge that would close a cycle** (both ends already connected). Both give the same total.

**Diagram spec.**
- [G2: F top-left, A top-middle, B top-right, E bottom-left, C right, D bottom-middle; MST edges in coral: E–F 5, B–C 7, C–F 8, A–C 9, C–D 14; the rejected B–F 10 dashed red]

**Exam answer — Prim from A:**

| Step | Edge added | Tree vertices | Keys of the rest (cheapest link to the tree) |
|---|---|---|---|
| 0 | — | A | B 16, C 9, others ∞ |
| 1 | A–C (9) | A C | B 7, D 14, E 15, F 8 |
| 2 | C–B (7) | A C B | D 14, E 15, F 8 |
| 3 | C–F (8) | A C B F | D 14, E 5 |
| 4 | F–E (5) | A C B F E | D 14 |
| 5 | C–D (14) | all | — |

**Exam answer — Kruskal:**

| Edge (sorted) | Decision |
|---|---|
| E–F 5 | ACCEPT |
| B–C 7 | ACCEPT |
| C–F 8 | ACCEPT |
| A–C 9 | ACCEPT |
| B–F 10 | **REJECT** (B–C–F already joined → cycle) |
| C–D 14 | ACCEPT → 5 edges = V − 1, stop |

| Write | Why |
|---|---|
| MST = {E–F, B–C, C–F, A–C, C–D}; **total = 5 + 7 + 8 + 9 + 14 = 43** | both algorithms agree |

**HOW MUCH:** Kruskal = sort E edges → $O(E \log E)$. Prim with a key table = V picks × V scan → $O(V^2)$.

**Try:** Prim from E instead of A. First two edges? → E–F (5), then F–C (8). Same total **43**.

---

### Q12. Section A one-liners (~16 marks)
Each row is a picture-derived answer, not a list to memorise.

| Question (paper) | Write | Picture behind it |
|---|---|---|
| Constructor vs destructor (ETE26 A1) | see Q4: initialises vs cleans up; auto-called at creation vs at scope end; can overload vs one only; ~ prefix | the object's birth vs its death |
| Array vs linked list (ETE26 A2) | the table in Q6 | one block vs scattered boxes |
| Degree of a node / of a tree (ETE26 A3) | degree of a node = its number of children; degree of a tree = the maximum node degree in it | count the arrows leaving a box |
| Leaf node / depth of a tree (ETE26 A4) | leaf = a node with no children; depth of a node = edges from the root to it; depth (height) of a tree = the longest root-to-leaf path | |
| Bubble vs selection (ETE26 A5) | the table in Q8 | |
| Stack, LIFO (50Q 25) | last in, first out: push 15, 25, 35, 45, pop ×2, push 55, 65 → **15 25 55 65** (top = 65) | a pile of plates |
| Queue, FIFO (A1 A6) | first in, first out; ENQUEUE at rear, DEQUEUE at front | a ticket line |
| Full vs complete vs perfect binary tree (50Q 31) | full = every node has 0 or 2 children · complete = all levels full except the last, filled left to right (a heap) · perfect = every level full, $2^h - 1$ nodes | |
| Max nodes / min height | a binary tree of height $h$ has at most $2^h - 1$ nodes (h counted in levels); min height $= \lceil \log_2(n+1) \rceil$ | each level doubles: $1 + 2 + 4 + \dots$ |
| OOP pillars (50Q 5, A1 A9) | encapsulation (data + functions in one class, data hidden), abstraction (show what, hide how), inheritance (reuse a parent class), polymorphism (one name, many forms: overloading) | *only if time is left* |
| Call by value vs reference (50Q 3) | value = the function gets a copy, so the original is unchanged; reference (`int &c`) = an alias, so changes hit the original | see MTE Q1/Q2 in Q13 |
| Data structure (A1 A8) | a way of organising data in memory so operations on it are efficient; linear (array, list, stack, queue) vs non-linear (tree, graph) | |

---

### Q13. Output prediction (2–4 marks each)
All run with g++. The real output is shown.

| Paper | Code (key line) | Output | Why |
|---|---|---|---|
| ETE26 A6 | `zip = 021377;` `cout << zip` | **8959** | a leading 0 makes an **octal** literal: $$2 \cdot 8^4 + 1 \cdot 8^3 + 3 \cdot 8^2 + 7 \cdot 8 + 7 = 8959$$ (Also: `<iostream.h>` is pre-standard and fails on modern compilers; say so in one line, then answer 8959.) |
| MTE Q1 | `Sum(x, y, y)` with `int &c`; x = 2, y = 3 | **2 15** | a, b are copies, c is y itself: a = 3 + 3 = 6, b = 6 + 3 = 9, c = 6 + 9 = 15 → y = 15; x unchanged |
| MTE Q2 | `fun(x, x)` by value | **10** | copies changed, original untouched |
| MTE Q3 | `-2[array]` with {10, 20, 30} | **−30** | `2[array]` = `*(2 + array)` = `array[2]` = 30; the unary minus applies after |
| MTE Q4 | sum of array1 (5 items) + first 4 of array2 | **6533** | 6473 + 60 |
| MTE Q5 | `class Derived: public Base1, public Base2` | Base1's constructor called / Base2's constructor called / Derived's constructor called | bases are built first, in the order they are **listed**, then the derived class |
| MTE Q6 | local class with `int rno = 10;` | **10** (once `Cout` → `cout` and `rno` made public) | as printed: a compile error (`Cout` undeclared, and a member is private by default) |
| MTE Q7 | `y = ++x * ++x;` | g++ prints **749735** | **undefined behaviour** (x modified twice with no sequencing). Write "undefined, compiler-dependent", then give one compiler's result |

**Try:** `int a[] = {5, 6, 7}; cout << 1[a] + *(a + 2);` → 6 + 7 = **13**.

---

### Q14. Red-black insertion (8 marks) — *only if time is left*
**Question (booklet 54):** "Construct a Red-Black Tree by inserting the following elements in the given order: 22, 11, 33, 5, 17, 27, 44, 3, 8, 14, 19, 38, 50 … indicating the rotations and recolouring operations performed."

**Picture.** A BST whose nodes are painted red or black, under 4 rules (deck slide 43): **(1)** every node is red or black; **(2)** the root is black; **(3)** a red node has no red child; **(4)** every path from a node down to NULL passes the same number of black nodes (the **black height**). Together they keep the height ≤ $2 \log_2(n+1)$. A new node is always inserted **red** (that can't break rule 4). If its parent is red, look at the **uncle** (the parent's sibling): **uncle red → recolour** (parent and uncle black, grandparent red, then check again from the grandparent). **Uncle black/NULL → rotate:** for a zig-zag ("triangle"), first rotate the parent to make a line; for a line, rotate the grandparent and swap the colours of the old grandparent and parent.

**Diagram spec.**
- [one frame per event: +5 → uncle 33 red → recolour 11, 33 black and 22 red → 22 back to black (root)]
- [+3 → uncle 17 red → 5, 17 black, 11 red]
- [+38 → uncle 27 red → 44, 27 black, 33 red]
- [final tree with red nodes filled coral]

**Exam answer (state table):**

| Insert | Event | Tree after (B = black, R = red) |
|---|---|---|
| 22 | root → black | 22B |
| 11, 33 | parent black, done | 22B / 11R 33R |
| 5 | uncle 33 red → recolour 11, 33 B; 22 R → root back to B | 22B / 11B 33B / 5R |
| 17, 27, 44 | parent black | 22B / 11B 33B / 5R 17R 27R 44R |
| 3 | uncle 17 red → recolour 5, 17 B; 11 R | 22B / 11R 33B / 5B 17B 27R 44R / 3R |
| 8, 14, 19 | parent black | … / 3R 8R 14R 19R |
| 38 | uncle 27 red → recolour 44, 27 B; 33 R | 22B / 11R 33R / 5B 17B 27B 44B / 3R 8R 14R 19R 38R |
| 50 | parent black | **22B / 11R 33R / 5B 17B 27B 44B / 3R 8R 14R 19R 38R 50R** |

Check: black height = 2 on every path (22 + one of 5/17/27/44); no red–red pair. Like the AVL booklet questions, these keys arrive in level order, so **only recolouring happens**.

**Try (rotation case):** 10, 20, 30, 15, 25, 5. → +30: parent 20 red, uncle NULL (black), line R-R → **left-rotate 10, swap colours** → 20B / 10R 30R. +15: uncle 30 red → recolour → 20B / 10B 30B / 15R. Then 25 and 5: parent black, done → **20B / 10B 30B / 5R 15R 25R**.

---

### Q15. Huffman code + hashing (3–5 marks) — *only if time is left*
**Huffman (syllabus: "Path length: Huffman's algorithm").** Picture: frequent characters get short codes. Repeatedly join the two smallest weights into a parent, and label the left branch 0 and the right branch 1. Frequencies a 5, b 9, c 12, d 13, e 16, f 45: merge 5 + 9 = 14 → 12 + 13 = 25 → 14 + 16 = 30 → 25 + 30 = 55 → 45 + 55 = 100. Codes: **f 0, c 100, d 101, a 1100, b 1101, e 111**. Total bits $= 45 \cdot 1 + (12 + 13 + 16) \cdot 3 + (5 + 9) \cdot 4 =$ **224** (fixed 3-bit codes would need 300).
[diagram: the Huffman tree, root 100 → f 45 (0) and 55 (1) → 25 (c, d) and 30 (14 (a, b), e)]

**Hashing.** Picture: an array of $m$ buckets, with the key going to bucket $k \bmod m$ (the **hash function**). A **collision** = two keys land in the same bucket. **Linear probing:** step to the next free bucket. Keys 23, 43, 13, 27, 37 with $m = 10$: 23 → 3; 43 → 3 taken → 4; 13 → 3, 4 taken → 5; 27 → 7; 37 → 7 taken → 8. Table: [3] 23, [4] 43, [5] 13, [7] 27, [8] 37. Cost $O(1)$ on average; the worst case $O(n)$ is when everything collides.

---

## 1. ETE April–May 2026 (ECE2240), solved — the paper A1 copies from
| Q | Answer |
|---|---|
| A1 ctor vs dtor (3) | Q4 / Q12 |
| A2 array vs linked list (3) | Q6 table |
| A3 degree of a node / tree (2) | Q12 |
| A4 leaf / depth (2) | Q12 |
| A5 bubble vs selection (3) | Q8 table |
| A6 zip output (3) | **8959** (octal), Q13 |
| B7 array queue program (8) | Q5 |
| B8 linked-list insertion program (8) | Q6 |
| B9 AVL 9, 27, 50, 15, 2, 21, 36 (8) | Q3: RR at 9; LR at 27; final 15 / 9 27 / 2 21 50 / 36 |
| B10 max-heap delete 90 (8) | Q7: **89 85 70 36 75 63 65 21 18 15** |
| C11 BST 45 … 48 + traversals (8) | Q1 program output: pre 45 36 23 39 41 76 56 48 69 89 115 98 · in 23 36 39 41 45 48 56 69 76 89 98 115 · post 23 41 39 36 48 69 56 98 115 89 76 45 |
| C12 infix → prefix/postfix (8) | Q2: postfix A B C × + D E F G + / − × H I J K L × − / + × · prefix × × + A × B C − D / E + F G + H / I − J × K L |
| D13 rectangle constructors + destructor (16) | Q4 |

## 2. ETE April–May 2025 (ECE2240), solved
| Q | Answer |
|---|---|
| A1–5 graph terms (10) | Q9 table |
| B7–9 BST 50 … 24 (30) | Q1: pre 50 15 5 3 8 20 37 24 62 58 60 91 · in 3 5 8 15 20 24 37 50 58 60 62 91 · post 3 8 5 24 37 20 15 60 58 91 62 50 · left 7, right 4 |
| C10 logical expression (10) | Q2: postfix A B C < C D > \|\| ! && ! C E < \|\| F G && H \|\| I \|\| && · prefix && \|\| ! && A ! \|\| < B C > C D < C E \|\| \|\| && F G H I |
| C11 "postfix" +AB^CD… (10) | Q2 trap: invalid as printed; say so and show the method |
| D12 queue with a linked list (10) | Q5 |
| D13 selection sort + application (10) | Q8 |

## 3. MTE March 2024 (EC2240), solved
| Q | Answer |
|---|---|
| Q1 | **2 15** |
| Q2 | **10** |
| Q3 | **−30** |
| Q4 | **6533** |
| Q5 | Base1 …, Base2 …, Derived … (in that order) |
| Q6 | 10 (after fixing `Cout`/`public`); as printed: a compile error |
| Q7 | undefined behaviour; g++: 749735 |
| Q8 | Q6 reversal program |

## 4. Assignment 1 (ECE2104, Aug 2026) — compact key
| Q | Answer |
|---|---|
| A1–A6, A8, A9 | Q12 rows |
| A7 | 8959 |
| B1 | Q6 program (+ delete: `p->next = p->next->next`; search: walk and compare) |
| B2 | swap by value leaves x, y unchanged; by reference (`int &a, int &b`) swaps them |
| B3 ((A+B)/C)(D−E) | **A B + C / D E − ×** |
| B4 | array insert at pos: shift `a[i] = a[i-1]` from the end down to pos, then `a[pos] = x`, n++; delete: shift left from pos, n-- |
| B5 | stack: `top = -1`; push `if (top == MAX-1) overflow; a[++top] = x`; pop `if (top == -1) underflow; return a[top--]` |
| C1 PUSH 10, 20, POP, POP, POP, PUSH 30, 40 | stack 10 → 10 20 → 10 → empty → **underflow** (3rd POP) → 30 → **30 40** (top = 40); overflow only if MAX < 2 |
| C2 | browser back = **stack** (latest page first); printer = **queue** (FIFO); dynamic student records = **linked list** (grows, cheap insert/delete) |
| C3 | Q4 pattern with name, roll, marks; grade by if-else |
| C4 12 3 4 × + 6 2 / − | stack after each operator: × → 12 12 · + → 24 · / → 24 3 · − → **21** |
| C5 | Q6 |
| D1 | Q4 with a triangle + function overloading |
| D2 sort a linked list by swapping data | bubble sort on nodes: `for (p = head; p; p = p->next) for (q = p->next; q; q = q->next) if (p->data > q->data) swap(p->data, q->data);` |
| D3 infix → postfix program | the Q2 stack algorithm in code: operand → output; `(` push; `)` pop to `(`; operator: pop while top has ≥ precedence, then push; at the end pop all |
| D4 | Q5 array queue |

## 5. DSA 50-question assignment — keys for the trace questions
| Q | Answer |
|---|---|
| 25 | stack bottom → top: **15 25 55 65** |
| 26 | **A B + C D − × E /** (stack table in Q2) |
| 27 | **3.5** |
| 28 | front at 33, rear at 66 (Q5 Try 1) |
| 32 (letters M G T D J P W B F H K N R U Y) | tree = level order as given (perfect, 4 levels) · pre **MGDBFJHKTPNRWUY** · in **BDFGHJKMNPRTUWY** · post **BFDHKJGNRPUYWTM** |
| 33 | min 5, max 80, height 4 edges |
| 34 (C A F B E H D G I) | search G: C → F → H → G **found** · search Z: C → F → H → I → right is NULL **not found** |
| 35 (60, 40, 80, …, 95) | −10 (leaf): removed · −20 (now has one child, 30): 30 moves up · −60 (two children): successor **65** becomes the root |
| 36 | tree A / B C / D E F G · post **D E B F G C A** |
| 37, 38 | level-order input → **no rotations**; 37 final BF: 40 = +1, 20 = +1, 10 = +1, all others 0 |
| 44 | R(K(D, F), M(−, P(−, Z(X, −)))) · post **D F K X Z P M R** |
| 46 | levels S / K W / D N U Z / A F M P T V X / C E G L O Y · pre SKDACFEGNMLPOWUTVZXY · in ACDEFGKLMNOPSTUVWXYZ · post CAEGFDLMOPNKTVUYXZWS · search V: S → W → U → V |
| 47 | −D (two children) → successor E · −S (two children, root) → successor T is the new root · −W (two children) → successor X |
| 49 (A C E G I … N) | rotations: RR at A, E, C, I, M, K, Q, G, U; final root O; levels O / G S / C K Q W / A E I M U Y / B D F H J L N |
| 41 (RB) | rotations: +30 left-rotate 10; +22 right-rotate 30; recolours at +15, +1, +28, +40 (twice) · final 20B / 10B 25B / 5B 15B 22B 30R / 1R 8R 12R 18R 28B 35B / 32R 40R |

## 6. Booklet 34–43 — infix → postfix / prefix (numbers as operands)
| # | Postfix | Prefix | Value |
|---|---|---|---|
| 34 | 20 5 8 3 − × + 6 2 + / | / + 20 × 5 − 8 3 + 6 2 | 5.625 |
| 35 | 50 10 2 3 1 + × − / 7 + | + / 50 − 10 × 2 + 3 1 7 | 32 |
| 36 | 100 5 / 4 2 + × 8 2 / 3 + − | − × / 100 5 + 4 2 + / 8 2 3 | 113 |
| 37 | 15 3 2 + 4 × − 7 6 3 / − / | / − 15 × + 3 2 4 − 7 / 6 3 | −1 |
| 38 | 40 12 3 1 + / 2 × − 8 5 2 × − + | + − 40 × / 12 + 3 1 2 − 8 × 5 2 | 32 |
| 39 | 25 8 6 2 − × 4 2 + / + | + 25 / × 8 − 6 2 + 4 2 | 30.33 |
| 40 | 18 6 + 4 2 − / 7 3 + × | × / + 18 6 − 4 2 + 7 3 | 120 |
| 41 | 20 8 2 + − 15 3 2 + / × | × − 20 + 8 2 / 15 + 3 2 | 30 |
| 42 | 50 10 5 8 3 − × + 6 2 − / − | − 50 / + 10 × 5 − 8 3 − 6 2 | 41.25 |
| 43 | 100 5 / 2 3 + × 8 4 1 − × − | − × / 100 5 + 2 3 × 8 − 4 1 | 76 |

---
*Sources checked:* every trace above is printed by `chat-pack/verify_dsa.py`; every program is in `chat-pack/programs/` (p1 array queue, p2 list insertion, p3 rectangle, p4 linked queue, p5 selection sort, p6 reversal, p7 BST, p8 output questions, p9 sort traces), compiled with `g++ -std=c++17` and run on 27 Nov 2026.
