# 07 — Mock MTE (30 marks, 90 minutes)

**This is a prediction, not a leak.** The format copies the real **ECE2108 MTE** from the same
department and the same week (A: 2 + 2 + 3 · B: 3 × 5 · C: 1 × 8). Question choice follows the pattern
from that paper: **most questions were assignment questions or their close neighbours.**

**Short on time?** Do **Section A** only (7 marks, ~10 min) and check it. Otherwise, set a timer,
write on paper, **then** check.

---

## Section A

**Q1** *(2)* What is the output of the following, and why?
```text
int x = 012;
cout << x + 1;
```

**Q2** *(2)* A stack of size 4 undergoes `PUSH(5) PUSH(7) POP() PUSH(9) PUSH(2) PUSH(4) PUSH(6)`.
Give the final contents and TOP, and identify any overflow/underflow.

**Q3** *(3)* Convert `A + (B * C - D) / E` to postfix, showing the operator stack at each step.

## Section B

**Q4** *(5)* Differentiate between a constructor and a destructor. Write a C++ class `Rectangle` with a
default constructor and a parameterized constructor, and a member function that returns the area.

**Q5** *(5)* Write a C++ function to delete a node with a given value from a singly linked list.
Handle all cases, and draw the pointer change for deletion from the middle.

**Q6** *(5)* What is the drawback of a linear queue implemented using an array? Explain how a circular
queue overcomes it. For MAX = 4, trace: `ENQ(1) ENQ(2) ENQ(3) DEQ DEQ ENQ(4) ENQ(5) ENQ(6)`, giving
front and rear after each step.

## Section C

**Q7** *(8)* (a) Evaluate the postfix expression `6 2 3 + - 3 8 2 / + *` using a stack, showing the
stack after each operator. *(4)*
(b) Differentiate between an array and a linked list (any 4 points). Which would you use to implement
a stack whose maximum size is not known in advance? Justify. *(4)*

---
---

## Answers

**Q1.** `11`. `012` is **octal** = 1·8 + 2 = 10, and 10 + 1 = 11. *(file 01 §1)*

**Q2.** MAX = 4, so full at TOP = 3.

| Op | TOP | Stack |
|---|---|---|
| PUSH 5 | 0 | 5 |
| PUSH 7 | 1 | 5 7 |
| POP | 0 | 5 (returns 7) |
| PUSH 9 | 1 | 5 9 |
| PUSH 2 | 2 | 5 9 2 |
| PUSH 4 | 3 | 5 9 2 4 → **full** |
| PUSH 6 | 3 | **OVERFLOW**, 6 not inserted |

Final: `5 9 2 4`, TOP = 3, 4 on top. Overflow at PUSH(6). No underflow. *(file 04 §2)*

**Q3.** `A + (B * C - D) / E`

| Symbol | Stack | Postfix |
|---|---|---|
| A | | A |
| + | + | A |
| ( | + ( | A |
| B | + ( | A B |
| * | + ( * | A B |
| C | + ( * | A B C |
| - | + ( - | A B C * ← `*` popped (higher than `-`) |
| D | + ( - | A B C * D |
| ) | + | A B C * D - |
| / | + / | A B C * D - ← `/` is higher than `+`, so push |
| E | + / | A B C * D - E |
| end | | A B C * D - E / + |

**`A B C * D - E / +`** *(file 04 §6)*

**Q4.** The table from file 01 §6 (purpose, name with `~`, when it runs, arguments, overloading,
return type). Program:

```cpp
#include <iostream>
using namespace std;

class Rectangle {
    double length, width;
public:
    Rectangle() { length = 1; width = 1; }                 // default
    Rectangle(double l, double w) { length = l; width = w; } // parameterized
    double area() { return length * width; }
    ~Rectangle() { }                                        // destructor (optional)
};

int main() {
    Rectangle r1, r2(4, 5);
    cout << "r1 area = " << r1.area() << endl;
    cout << "r2 area = " << r2.area() << endl;
    return 0;
}
```

Output:

```text
r1 area = 1
r2 area = 20
```

**Q5.** `deleteNode` from file 03 §6. Four cases: empty list · value at head (`head = head->next`)
· middle/end (`prev->next = temp->next`) · not found. Plus `delete temp;`. Diagram:

```text
 before:  prev ──► [temp] ──► next
 after:   prev ─────────────► next      (temp freed with delete)
```

**Q6.** Drawback: `rear == MAX − 1` reports full even when dequeued slots at the front are empty.
Circular: `rear = (rear + 1) % MAX` wraps to index 0. Full when `(rear + 1) % MAX == front`.

| Op | front | rear | Contents by index [0 1 2 3] |
|---|---|---|---|
| start | −1 | −1 | – – – – |
| ENQ 1 | 0 | 0 | 1 – – – |
| ENQ 2 | 0 | 1 | 1 2 – – |
| ENQ 3 | 0 | 2 | 1 2 3 – |
| DEQ (1) | 1 | 2 | – 2 3 – |
| DEQ (2) | 2 | 2 | – – 3 – |
| ENQ 4 | 2 | 3 | – – 3 4 |
| ENQ 5 | 2 | **0** | 5 – 3 4 ← wrapped |
| ENQ 6 | 2 | 1 | 5 6 3 4 → now (1 + 1) % 4 = 2 = front → **full** |

In a linear queue, ENQ(5) would already overflow (rear = 3 = MAX − 1). *(file 05 §3)*

**Q7(a).** `6 2 3 + - 3 8 2 / + *`

| Token | Action | Stack |
|---|---|---|
| 6, 2, 3 | push | 6 2 3 |
| + | 2 + 3 = 5 | **6 5** |
| − | 6 − 5 = 1 | **1** |
| 3, 8, 2 | push | 1 3 8 2 |
| / | 8 / 2 = 4 | **1 3 4** |
| + | 3 + 4 = 7 | **1 7** |
| * | 1 × 7 = 7 | **7** |

**Result = 7.** *(file 04 §7)*

**Q7(b).** Four rows from the file 03 §1 table (memory, size, access, insert/delete cost, extra memory).
Choice: a **linked list**. It has no fixed size, so the stack never overflows (except when memory runs
out). PUSH/POP are insert/delete at the **head**, which are O(1). *(file 04 §4)*

---

## Last 10 minutes before the exam

Re-read only these: the **Traps** sections of 04, 03, 01, 05 (in that order), then the Red-Black
properties in 06 §4. Anything you missed in a Self-test goes first.
