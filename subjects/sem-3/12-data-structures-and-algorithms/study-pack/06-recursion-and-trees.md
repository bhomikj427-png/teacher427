# 06 — Recursion, and trees up to "types of trees"

**Recursion: hand-out L16, the last lecture before the MTE divider · Trees: L17+, included because
your professor said "till red-black tree" · CO2 / CO3**

No A1 question covers this file. Recursion is **inside** the printed MTE scope. Trees are **beyond**
the hand-out's divider and included on your professor's word, so expect **definitions and
distinctions** there, not programs.

## Map

```
 recursion ──► base case + recursive case ──► the call stack (links to 04)
     │              factorial · Fibonacci · Tower of Hanoi
     ▼
 tree = hierarchy (non-linear)
     ├──► terminology: root, leaf, degree, level, depth, height …
     ├──► binary tree properties: 2^l, 2^(h+1) − 1, n₀ = n₂ + 1
     ├──► types: full · complete · perfect · skewed
     │           BST ──► AVL ──► Red-Black      heap
     └──► (bonus) traversal: pre / in / post / level order
```

---

## 1. Recursion

**Q ▸** `int f(int n) { return n * f(n - 1); }` — what happens when you call `f(3)`?

It **never stops**. It calls f(2), f(1), f(0), f(−1), … until the call stack runs out of memory (a
**stack overflow**). It's missing the **base case**.

**Recursion:** a function that **calls itself** on a **smaller** version of the same problem. Every
recursive function needs:

1. **Base case**: a condition where it returns **without** recursing (it stops the recursion).
2. **Recursive case**: calls itself on input that moves **toward** the base case.

**How it runs: the call stack.** Every call is **pushed** on the system stack (its parameters, local
variables and return address). When a call returns, it's **popped**. That's the "function calls"
application of a stack from file 04.

```text
fact(3)                             pushed:  fact(3)
 = 3 * fact(2)                      pushed:  fact(3) fact(2)
       = 2 * fact(1)                pushed:  fact(3) fact(2) fact(1)
             = 1   ◄ base case      popped from here upward
       = 2 * 1 = 2
 = 3 * 2 = 6
```

| Recursion | Iteration (loops) |
|---|---|
| function calls itself | loop repeats a block |
| stops at the **base case** | stops when the **condition** fails |
| uses the call stack: more memory, call overhead | no extra stack memory |
| shorter and clearer for trees, Hanoi, divide-and-conquer | usually faster |
| missing base case → **stack overflow** | missing update → infinite loop |

**Types (one line each if asked):** **direct** (f calls f) · **indirect** (f calls g, g calls f) ·
**tail** (the recursive call is the last thing done).

```cpp
#include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0 || n == 1) return 1;          // base case
    return n * factorial(n - 1);              // recursive case
}

int fibonacci(int n) {                        // 0 1 1 2 3 5 8 ...
    if (n == 0) return 0;                     // base cases
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

void hanoi(int n, char from, char to, char via) {
    if (n == 1) {                             // base case
        cout << "Move disk 1 from " << from << " to " << to << endl;
        return;
    }
    hanoi(n - 1, from, via, to);              // move n-1 out of the way
    cout << "Move disk " << n << " from " << from << " to " << to << endl;
    hanoi(n - 1, via, to, from);              // move n-1 on top
}

int main() {
    cout << "5! = " << factorial(5) << endl;
    cout << "Fibonacci(0..7): ";
    for (int i = 0; i <= 7; i++) cout << fibonacci(i) << " ";
    cout << endl;
    cout << "Tower of Hanoi, 3 disks:" << endl;
    hanoi(3, 'A', 'C', 'B');
    return 0;
}
```

Output:

```text
5! = 120
Fibonacci(0..7): 0 1 1 2 3 5 8 13 
Tower of Hanoi, 3 disks:
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```

**Tower of Hanoi needs 2ⁿ − 1 moves** (3 disks → 7 moves, as above).

---

## 2. Trees: terminology

**Q ▸** A folder on your laptop contains folders, which contain files. Can you store that in an
array so that "what's inside this folder" is easy to answer?

Not naturally. It's a **hierarchy**: one item has **many** children. That's a **tree**, a **non-linear**
data structure of **nodes** joined by **edges**, with one **root** and no cycles.

```text
                 A            ◄ root            level 0
               /   \
              B     C                           level 1
            /  \      \
           D    E      F      ◄ D, E, F leaves  level 2
          /
         G                                      level 3
```

| Term | Meaning | In the example |
|---|---|---|
| **Root** | the top node, with no parent | A |
| **Parent / child** | directly connected, above / below | B is D's parent. D, E are B's children |
| **Siblings** | same parent | D and E |
| **Leaf** (external / terminal node) | no children | E, F, G |
| **Internal node** | has at least one child | A, B, C, D |
| **Edge** | a link between parent and child | n nodes → **n − 1 edges** |
| **Path** | a sequence of edges between two nodes | A → B → D → G |
| **Ancestor / descendant** | anything above / below on the path | A, B, D are ancestors of G |
| **Degree of a node** | number of children | deg(B) = 2, deg(C) = 1 |
| **Degree of a tree** | the maximum degree of any node | 2 |
| **Level** | root = 0, children = parent + 1 | G is at level 3 |
| **Depth of a node** | number of edges from the root to it | depth(G) = 3 |
| **Height of a node** | number of edges on the longest path down to a leaf | height(B) = 2 |
| **Height of the tree** | height of the root | 3 |
| **Subtree** | a node and all its descendants | B, D, E, G |
| **Forest** | a set of disjoint trees (remove the root → a forest) | {B-subtree, C-subtree} |

> ⚠ **Convention warning:** some books start levels at **1** and count height in **nodes** (so this
> tree would have height 4). Both are used in Indian textbooks. **State your convention in the answer**
> ("taking root at level 0") and you cannot be marked wrong.

---

## 3. Binary tree and its properties

**Binary tree:** every node has **at most 2** children, called the **left** child and the **right**
child. (Left vs right matters. Two trees with the same shape but a child on the other side are
different binary trees.)

With root at level 0 and height counted in edges:

| Property | Formula | Example |
|---|---|---|
| Max nodes at level l | **2ˡ** | level 3 → 8 |
| Max nodes in a binary tree of height h | **2^(h+1) − 1** | h = 2 → 7 |
| Min height with n nodes | **⌈log₂(n + 1)⌉ − 1** | n = 7 → 2 |
| Leaves vs 2-child nodes (any binary tree) | **n₀ = n₂ + 1** | |

---

## 4. Types of trees

**Q ▸** A BST built by inserting 10, 20, 30, 40, 50 in that order: what shape is it, and how long
does a search take?

A straight line going right (**right-skewed**), so search is **O(n)**, no better than a linked list.
**That one problem is why AVL and Red-Black trees exist**: they keep the tree **balanced** so that
search stays **O(log n)**.

**Shape types (binary trees):**

| Type | Rule | Picture |
|---|---|---|
| **Full / strict / proper** | every node has **0 or 2** children, never 1 | `A(B(D,E),C)` |
| **Complete** | all levels full **except possibly the last**, and the last is filled **from the left** | `A(B(D,E),C(F,_))` |
| **Perfect** | all internal nodes have 2 children **and** all leaves are on the **same level** | `A(B(D,E),C(F,G))` = 2^(h+1) − 1 nodes |
| **Skewed** | every node has only one child (all left = left-skewed, all right = right-skewed) | a "linked list" |
| **Degenerate** | same as skewed: each parent has one child | |

> ⚠ Some books (e.g. older Indian texts) use "**full**" to mean **perfect**. If a question's use
> seems off, define the term you're using.

**Search and balance types:**

| Type | Defining rule | Why it exists |
|---|---|---|
| **Binary Search Tree (BST)** | for **every** node: all keys in its **left** subtree are **smaller**, all keys in its **right** subtree are **larger** | search in O(h): go left if smaller, right if larger. **Inorder traversal gives sorted order** |
| **AVL tree** (Adelson-Velsky & Landis) | a BST where every node's **balance factor** = height(left) − height(right) ∈ **{−1, 0, +1}** | stays balanced by **rotations** (LL, RR, LR, RL) → O(log n) guaranteed |
| **Red-Black tree** | a BST whose nodes are coloured, obeying the 5 rules below | also O(log n), with **fewer rotations** than AVL on insert/delete (used in C++ `std::map`) |
| **Heap** | a **complete** binary tree. **Max-heap**: every parent ≥ its children. **Min-heap**: every parent ≤ its children | the root is always the max/min → **priority queues**, heap sort |
| **B-tree** | multi-way (more than 2 children) balanced search tree, all leaves on one level | databases and file systems (disk-friendly) |
| **General tree** | any number of children | folders, organisation charts |

**Red-Black tree: the 5 properties** (the likely "till red-black tree" question):

1. Every node is either **red** or **black**.
2. The **root** is **black**.
3. Every **leaf (NIL / null child)** is **black**.
4. A **red node cannot have a red child** (no two reds in a row).
5. For every node, **every path** from it down to its descendant NIL leaves contains the **same number
   of black nodes** (its *black-height*).

Consequence: the longest root-to-leaf path is at most **twice** the shortest, so the height is at most
**2 log₂(n + 1)** and operations are O(log n).

**AVL vs Red-Black in one line:** AVL is **more strictly** balanced (faster search). Red-Black is
**more loosely** balanced (faster insert/delete, fewer rotations).

---

## 5. Bonus: the four traversals (L-plan "Traversal Algorithms")

```text
                 A
               /   \
              B     C
            /  \      \
           D    E      F
```

| Traversal | Order | Result |
|---|---|---|
| **Preorder** | **Root**, Left, Right | A B D E C F |
| **Inorder** | Left, **Root**, Right | D B E A C F |
| **Postorder** | Left, Right, **Root** | D E B F C A |
| **Level order** | level by level, left to right (uses a **queue**) | A B C D E F |

Memory hook: *pre / in / post* = where the **root** goes (before, in between, after).

```cpp
#include <iostream>
using namespace std;

struct Node {
    char data;
    Node *left, *right;
    Node(char d) { data = d; left = right = NULL; }
};

void preorder(Node *r)  { if (r) { cout << r->data << " "; preorder(r->left); preorder(r->right); } }
void inorder(Node *r)   { if (r) { inorder(r->left); cout << r->data << " "; inorder(r->right); } }
void postorder(Node *r) { if (r) { postorder(r->left); postorder(r->right); cout << r->data << " "; } }

int main() {
    Node *root = new Node('A');
    root->left = new Node('B');
    root->right = new Node('C');
    root->left->left = new Node('D');
    root->left->right = new Node('E');
    root->right->right = new Node('F');

    cout << "Preorder:  "; preorder(root);  cout << endl;
    cout << "Inorder:   "; inorder(root);   cout << endl;
    cout << "Postorder: "; postorder(root); cout << endl;
    return 0;
}
```

Output:

```text
Preorder:  A B D E C F 
Inorder:   D B E A C F 
Postorder: D E B F C A 
```

---

## Traps

- **No base case → infinite recursion → stack overflow.**
- Level/height conventions differ, so **state yours**.
- "Complete" ≠ "full". Complete = filled left to right. Full = 0 or 2 children.
- BST rule applies to the **whole subtree**, not just the immediate children.
- A heap is **not** a BST: siblings have no order, only parent vs child.
- The Red-Black root is **always black**, and **no red-red** parent-child pair is allowed.

## Self-test

1. What two parts must every recursive function have?
2. How many moves does Tower of Hanoi take for 4 disks?
3. Max nodes in a binary tree of height 3 (root at height 0)?
4. A node's balance factor is +2. Which tree type does that violate?
5. Is `50(30(20,40),70(60,80))` a BST? Is it complete? Perfect?
6. State two Red-Black properties.

## Answers

1. A base case and a recursive case (moving toward the base case).
2. 2⁴ − 1 = **15**.
3. 2⁴ − 1 = **15**.
4. **AVL** (it must be in {−1, 0, +1}).
5. **BST: yes.** Complete: yes. **Perfect: yes** (all leaves on level 2, all internal nodes have 2 children).
6. Any two: root is black · no red node has a red child · every path to NIL has the same black count ·
   every node is red or black · NIL leaves are black.
