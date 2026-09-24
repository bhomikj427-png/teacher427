# 02 — Data structures and arrays

> **MTE blueprint:** CO2 (14 marks, shared with 03–05). From this file, expect at most a 2-mark
> Section A question (§1 classification, §3 insert/delete shifting).

**A1: A1, A8, B4 · 4 of 50 marks · deck 6 · CO2**

Small in A1, but everything in 03–05 is compared **against** the array, so read it anyway.

## Map

```
 what is a data structure (A8) ──► linear vs non-linear, static vs dynamic
        │
        ▼
 array: contiguous memory ──► address formula ──► O(1) access
        │
        ▼
 traverse O(n) · insert O(n) · delete O(n)  (A1) ──► program (B4)
                    └─ the shifting is the cost
```

---

## 1. What is a data structure `[A1 A8]`

**Q ▸** Why can't you just store everything in plain variables?

Because the **organisation** of the data decides how fast you can do things with it. Finding the
latest browser page, serving print jobs in order and looking up a roll number each want a different
arrangement.

**Exam answer (A8):** A **data structure** is a way of **organising and storing data in memory** so that
it can be accessed and modified **efficiently**. It defines the data, the **relationships** between the
items, and the **operations** allowed on them (insert, delete, search, traverse, sort).
Examples: array (marks of 60 students), stack (undo in an editor), queue (printer jobs), linked list
(a playlist), tree (folders on a disk).

**Classification** (draw this, it's worth the mark):

```text
                     Data structures
                    /               \
           Primitive                 Non-primitive
      int, float, char,             /             \
      pointer                  Linear            Non-linear
                          array, linked list,    tree, graph
                          stack, queue
```

- **Linear**: elements form a sequence, and each has one successor.
- **Non-linear**: one element can connect to many (hierarchy or network).
- **Static**: size fixed at compile time (array). **Dynamic**: grows and shrinks at run time (linked list).

---

## 2. The array in memory

**Q ▸** `int arr[5];` with 4-byte ints, starting at address 1000. What's the address of `arr[3]`?

**1012.** You didn't need to look at arr[0], arr[1] or arr[2]. That's the whole point of an array.

- **Homogeneous**: all elements have the same type.
- **Contiguous**: one unbroken block of memory. `int arr[5]` = 5 × 4 = **20 bytes** in a row.
- **Fixed size**: decided at declaration and cannot grow.
- **Indexed from 0** to size − 1.

**Address formula** (a deck-6 activity question):

```text
1-D:   LOC(A[k]) = Base + w × (k − LB)
       Base = address of first element, w = bytes per element, LB = lower bound (0 in C++)

       arr[3] = 1000 + 4 × (3 − 0) = 1012

2-D, M rows × N columns, element A[i][j] (C++ uses row-major):
   Row-major:    LOC = Base + w × [ (i − LB_row) × N + (j − LB_col) ]
   Column-major: LOC = Base + w × [ (j − LB_col) × M + (i − LB_row) ]
```

**Why access is O(1)** (also a deck question): the address is computed by **one formula**, whatever
the index. No scanning. That is only possible **because** the memory is contiguous.

---

## 3. Traverse, insert, delete `[A1 A1]`

**Q ▸** An array holds `10 20 30 40 50` (size 5, capacity 10). You insert 25 at index 2. How many
elements have to move?

**Three** (30, 40 and 50 each shift one place right). An array can't hold a gap, so every element after
the position has to move.

| Operation | What happens | Example (on `10 20 30 40 50`) | Time |
|---|---|---|---|
| **Traversal** | visit every element once, index 0 to n−1 | print all → `10 20 30 40 50` | O(n) |
| **Insertion** at pos | shift elements pos..n−1 **right** by one (**start from the end**), put item at pos, n++ | insert 25 at 2 → `10 20 25 30 40 50` | O(n) worst |
| **Deletion** at pos | shift elements pos+1..n−1 **left** by one (**start from pos**), n−− | delete index 1 → `10 30 40 50` | O(n) worst |

**Why insertion shifts from the end:** if you shift from the front, `a[3] = a[2]` overwrites a[3]
before you've moved it. Starting at the end moves each element into a free slot.

**Algorithm INSERT(A, N, POS, ITEM)** (exam-style):

```text
1. If N == MAX, print "Overflow" and stop.
2. Set I = N − 1.
3. Repeat while I ≥ POS:  A[I+1] = A[I];  I = I − 1.
4. A[POS] = ITEM.
5. N = N + 1.  Stop.
```

**Algorithm DELETE(A, N, POS)**:

```text
1. If N == 0, print "Underflow" and stop.
2. ITEM = A[POS].
3. Repeat for I = POS to N − 2:  A[I] = A[I+1].
4. N = N − 1.  Stop.
```

---

## 4. Program: insert and delete at a position `[A1 B4 · 2 marks]`

```cpp
#include <iostream>
using namespace std;

const int MAX = 10;

void display(int a[], int n) {
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
}

bool insertAt(int a[], int &n, int pos, int item) {
    if (n == MAX) { cout << "Overflow: array full" << endl; return false; }
    if (pos < 0 || pos > n) { cout << "Invalid position" << endl; return false; }
    for (int i = n - 1; i >= pos; i--)   // shift right, from the end
        a[i + 1] = a[i];
    a[pos] = item;
    n++;
    return true;
}

bool deleteAt(int a[], int &n, int pos) {
    if (n == 0) { cout << "Underflow: array empty" << endl; return false; }
    if (pos < 0 || pos >= n) { cout << "Invalid position" << endl; return false; }
    cout << "Deleted " << a[pos] << endl;
    for (int i = pos; i < n - 1; i++)    // shift left, from pos
        a[i] = a[i + 1];
    n--;
    return true;
}

int main() {
    int a[MAX] = {10, 20, 30, 40, 50};
    int n = 5;

    cout << "Original:            "; display(a, n);
    insertAt(a, n, 2, 25);
    cout << "After insert 25 at 2: "; display(a, n);
    deleteAt(a, n, 1);
    cout << "After delete at 1:   "; display(a, n);
    return 0;
}
```

Output:

```text
Original:            10 20 30 40 50 
After insert 25 at 2: 10 20 25 30 40 50 
Deleted 20
After delete at 1:   10 25 30 40 50 
```

`n` is passed **by reference** (`int &n`) so the size change reaches `main`. That links back to 01 §7.

---

## Traps

- The size must be a **compile-time constant** for a plain array (`const int MAX`).
- Insertion shifts **from the end**, deletion **from the position**. Get this backwards and you
  overwrite data.
- Insert needs an **overflow** check, delete an **underflow** check. Both are marks.
- Index runs 0 to n−1. `a[n]` is out of bounds and C++ **won't** stop you.

## Self-test

1. Base 2000, `float` (4 bytes), what's the address of `a[7]`?
2. Why is array access O(1) but linked-list access O(n)?
3. Linear or non-linear: stack, tree, queue, graph?
4. Deleting index 0 from an array of 100 elements moves how many elements?

## Answers

1. 2000 + 4 × 7 = **2028**.
2. The array's address comes from a formula (contiguous memory). A list has to follow pointers node by node.
3. Stack: linear. Tree: non-linear. Queue: linear. Graph: non-linear.
4. **99.** That's the worst case.
