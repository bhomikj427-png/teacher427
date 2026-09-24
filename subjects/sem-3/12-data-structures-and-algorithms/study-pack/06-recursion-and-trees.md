# 06 — Recursion, and trees up to BST

**Recursion: hand-out L16 (CO2) · Trees up to BST: CO3 = 5 marks on the MTE (A Q4 = 2, B Q4 = 3)**

> **MTE blueprint (2026-09-24): trees stop at BST.** AVL, Red-Black and heaps (§4, lower table) are
> **not on the MTE**, so skip them. For CO3's 5 marks, do **§2 terminology, §3–4 binary tree types,
> §5 traversals and §6 BST** (build / search / delete).

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

## 6. BST — build, search, delete (**the CO3 marks**)

**BST rule:** for **every** node, all keys in its **left subtree < node < all keys in its right
subtree**. Duplicates are normally not allowed (if a question allows them, say "equal keys go right").

### Construct: insert one key at a time, always starting at the root

**Q ▸** Build the BST for **45, 15, 79, 90, 10, 55, 12, 20, 50**. Try it on paper first.

Each key starts at the root: **smaller → go left, larger → go right**, until you reach an empty spot.

```text
 45             root
 15  < 45                 → left of 45
 79  > 45                 → right of 45
 90  > 45, > 79           → right of 79
 10  < 45, < 15           → left of 15
 55  > 45, < 79           → left of 79
 12  < 45, < 15, > 10     → right of 10
 20  < 45, > 15           → right of 15
 50  > 45, < 79, < 55     → left of 55

              45
           /      \
         15        79
        /  \      /  \
      10    20   55    90
        \       /
        12     50
```

**Check your tree:** the **inorder** traversal of a BST is always **sorted**.
Inorder = `10 12 15 20 45 50 55 79 90` ✔ sorted.
Preorder = `45 15 10 12 20 79 55 50 90`. Postorder = `12 10 20 15 50 55 90 79 45`.

### Search

Start at the root. Equal → found. Smaller → go left. Larger → go right. NULL → not found.
Search 50: 45 → 79 → 55 → **50**, found in 4 comparisons. Search 25: 45 → 15 → 20 → right of 20 is
NULL → **not found**.

### Delete: three cases (the classic 3-mark question)

| Case | Rule | Example on the tree above |
|---|---|---|
| **1. Leaf** (no children) | just remove it | delete 12 → 10 now has no children |
| **2. One child** | replace the node with its only child (link the parent to the child) | delete 55 → 50 moves up to be 79's left child |
| **3. Two children** | copy in its **inorder successor** (the **smallest** key in its **right** subtree), then delete the successor node, which is always case 1 or 2 | delete 45 → successor is **50** → the root becomes 50, and 55's left becomes empty |

(The **inorder predecessor**, the largest key in the left subtree, is equally correct. Name the one you use.)

```text
 delete 45 (two children) → successor 50

              50
           /      \
         15        79
        /  \      /  \
      10    20   55    90
        \
        12
```

**Efficiency:** search, insert and delete are all **O(h)**: **O(log n)** when balanced, **O(n)** when
skewed (keys inserted in sorted order). That answers "advantages/disadvantages of a BST".

**Binary tree vs BST (2-mark favourite):** a binary tree only limits each node to ≤ 2 children. A
BST **also orders** the keys (left < root < right), which is what makes search fast. Every BST is a
binary tree, but not every binary tree is a BST.

The program (insert + search + delete + inorder):

```cpp
#include <iostream>
using namespace std;

struct Node {
    int key;
    Node *left, *right;
};

Node* newNode(int k) {
    Node *n = new Node;
    n->key = k;
    n->left = n->right = NULL;
    return n;
}

Node* insert(Node *root, int k) {
    if (root == NULL) return newNode(k);          // empty spot found
    if (k < root->key) root->left = insert(root->left, k);
    else if (k > root->key) root->right = insert(root->right, k);
    return root;                                  // duplicates ignored
}

bool search(Node *root, int k) {
    while (root != NULL) {
        if (k == root->key) return true;
        root = (k < root->key) ? root->left : root->right;
    }
    return false;
}

Node* minNode(Node *n) {                          // leftmost = smallest
    while (n->left != NULL) n = n->left;
    return n;
}

Node* deleteKey(Node *root, int k) {
    if (root == NULL) return NULL;
    if (k < root->key) root->left = deleteKey(root->left, k);
    else if (k > root->key) root->right = deleteKey(root->right, k);
    else {
        if (root->left == NULL) {                 // case 1 or 2
            Node *t = root->right; delete root; return t;
        }
        if (root->right == NULL) {                // case 2
            Node *t = root->left; delete root; return t;
        }
        Node *s = minNode(root->right);           // case 3: inorder successor
        root->key = s->key;
        root->right = deleteKey(root->right, s->key);
    }
    return root;
}

void inorder(Node *r) {
    if (r) { inorder(r->left); cout << r->key << " "; inorder(r->right); }
}

int main() {
    int keys[] = {45, 15, 79, 90, 10, 55, 12, 20, 50};
    Node *root = NULL;
    for (int k : keys) root = insert(root, k);

    cout << "Inorder: "; inorder(root); cout << endl;
    cout << "Search 50: " << (search(root, 50) ? "found" : "not found") << endl;
    cout << "Search 25: " << (search(root, 25) ? "found" : "not found") << endl;

    root = deleteKey(root, 45);
    cout << "After deleting 45, root = " << root->key << endl;
    cout << "Inorder: "; inorder(root); cout << endl;
    return 0;
}
```

Output:

```text
Inorder: 10 12 15 20 45 50 55 79 90 
Search 50: found
Search 25: not found
After deleting 45, root = 50
Inorder: 10 12 15 20 50 55 79 90 
```

**Practice (answers at the bottom, item 7):** (P1) Build the BST for `50 30 70 20 40 60 80` and give its
preorder. (P2) Build it for `8 3 10 1 6 14 4 7 13`, then delete 3 and describe the result.

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
7. **P1:** root 50, children 30 and 70, leaves 20 40 60 80 (a perfect tree). Preorder `50 30 20 40 70 60 80`.
   **P2:** built = `8(3(1, 6(4,7)), 10(_, 14(13,_)))`. Delete 3 (two children) → successor **4** →
   `8(4(1, 6(_,7)), 10(_, 14(13,_)))`. Inorder after: `1 4 6 7 8 10 13 14`.
