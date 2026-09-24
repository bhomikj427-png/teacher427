# 07 — Mock MTE (30 marks, 90 minutes), built on the real blueprint

**Rebuilt 2026-09-24 to match the blueprint exactly:** A = 4 × 2 (CO1, CO1, CO2, CO3) · B = 4 + 4 + 4 + 3
(CO2 coding, CO2, CO2, CO3) · C = CO1, 2 + 5 coding. The questions are predictions, not a leak. They
are new numbers on the same topics, so you can't just remember the pack's answers.

**Short on time?** Do Section A (10 min) and B Q4, the BST question (5 min). Write your answers on
paper, **then** check.

---

## Section A (4 × 2 = 8 marks)

**A1** *(2 · CO1)* Differentiate between a constructor and a destructor (any four points).

**A2** *(2 · CO1)* What is the output? Justify.
```text
void change(int x, int &y) { x = x + 10; y = y + 10; }
int main() { int a = 5, b = 5; change(a, b); cout << a << " " << b; return 0; }
```

**A3** *(2 · CO2)* A circular queue has MAX = 5, front = 3, rear = 2. Is it full? Where will the next
element be inserted after one dequeue?

**A4** *(2 · CO3)* Differentiate between a binary tree and a binary search tree, with one example of
each.

## Section B (4 + 4 + 4 + 3 = 15 marks)

**B1** *(4 · CO2 · coding)* Write a C++ program to implement a **stack using a linked list** with PUSH,
POP and DISPLAY operations. Handle underflow.

**B2** *(4 · CO2)* Convert the infix expression `(A + B) * C - D / E` to postfix, showing the stack at
every step. Then evaluate your postfix for A = 2, B = 3, C = 4, D = 8, E = 2.

**B3** *(4 · CO2)* Explain insertion of a node **at the beginning** and **after a given node** of a
singly linked list, with diagrams. Give two advantages of a linked list over an array.

**B4** *(3 · CO3)* Construct a BST by inserting `60, 25, 75, 10, 40, 90, 35, 70`. Give its inorder
traversal, then delete 25 and draw the resulting tree.

## Section C (2 + 5 = 7 marks · CO1)

**C1** *(2)* Explain encapsulation and data hiding. Which access specifier provides data hiding?

**C2** *(5 · coding)* Write a C++ class `BankAccount` with data members account number, name and
balance. Provide a **default constructor**, a **parameterized constructor**, a **destructor**, and
member functions `deposit()`, `withdraw()` (reject a withdrawal larger than the balance) and
`display()`. Demonstrate them in `main()`.

---
---

## Answers

**A1.** Any four rows of the `01` §6 table: purpose (initialise vs clean up) · name (`ClassName` vs
`~ClassName`) · when it runs (creation vs destruction) · arguments (allowed vs never) · overloading
(yes vs no) · order (creation order vs reverse).

**A2.** Output **`5 15`**. `x` is passed **by value** (the function changes a copy, so `a` stays 5).
`y` is passed **by reference** (an alias of `b`, so `b` becomes 15). *(file 01 §7)*

**A3.** Full test: `(rear + 1) % MAX == front` → (2 + 1) % 5 = 3 = front → **full**. After one dequeue,
front = 4. The next insert goes to `(rear + 1) % 5` = **index 3**, the slot that was just freed.
*(file 05 §3)*

**A4.** A binary tree: each node has **at most 2** children, and the keys have no order. A BST also
satisfies **left subtree < node < right subtree** for every node, so its inorder traversal is sorted
and search takes O(h). Examples: `5(9, 2)` is a binary tree but not a BST. `5(2, 9)` is a BST. *(file 06 §6)*

**B1.** PUSH = insert at the head, POP = delete from the head (*file 04 §4*):

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *next;
};

Node *top = NULL;

void push(int x) {
    Node *newNode = new Node;
    newNode->data = x;
    newNode->next = top;      // connect first
    top = newNode;            // then move top
    cout << "Pushed " << x << endl;
}

void pop() {
    if (top == NULL) { cout << "Stack Underflow!" << endl; return; }
    Node *temp = top;
    cout << "Popped " << temp->data << endl;
    top = top->next;
    delete temp;
}

void display() {
    if (top == NULL) { cout << "Stack is empty" << endl; return; }
    cout << "Stack (top to bottom): ";
    for (Node *t = top; t != NULL; t = t->next) cout << t->data << " ";
    cout << endl;
}

int main() {
    pop();                    // underflow demo
    push(10);
    push(20);
    push(30);
    display();
    pop();
    display();
    return 0;
}
```

Output:

```text
Stack Underflow!
Pushed 10
Pushed 20
Pushed 30
Stack (top to bottom): 30 20 10 
Popped 30
Stack (top to bottom): 20 10 
```

Worth one line in the answer: there is **no overflow check**, because a linked stack grows dynamically.

**B2.** `(A + B) * C - D / E`

| Symbol | Stack | Postfix |
|---|---|---|
| ( | ( | |
| A | ( | A |
| + | ( + | A |
| B | ( + | A B |
| ) | | A B + |
| * | * | A B + |
| C | * | A B + C |
| - | - | A B + C * ← `*` popped (higher than `-`) |
| D | - | A B + C * D |
| / | - / | A B + C * D ← `/` is higher than `-`, so push |
| E | - / | A B + C * D E |
| end | | A B + C * D E / - |

**Postfix: `A B + C * D E / -`**
Evaluate `2 3 + 4 * 8 2 / -`: 2 + 3 = 5 → 5 × 4 = 20 → 8 / 2 = 4 → 20 − 4 = **16**. *(file 04 §6–7)*

**B3.** At the beginning: `newNode->next = head; head = newNode;`. After node P:
`newNode->next = P->next; P->next = newNode;`. **Always connect before you break the old link.**
Draw before/after diagrams (*file 03 §4*). Advantages: dynamic size (no overflow of a fixed array) ·
insertion/deletion without shifting · no wasted capacity. *(file 03 §1)*

**B4.**

```text
              60
           /      \
         25        75
        /  \      /  \
      10    40   70    90
           /
          35
```

Inorder: `10 25 35 40 60 70 75 90` (sorted ✔).
Delete 25: it has **two children**, so replace it with its **inorder successor**, the smallest key in
its right subtree = **35**. Then remove 35 from its old place (it was a leaf).

```text
              60
           /      \
         35        75
        /  \      /  \
      10    40   70    90
```

*(file 06 §6)*

**C1.** Encapsulation = bundling data and the functions that operate on it into one unit, a class.
Data hiding = restricting direct access to the data so that it can only be changed through member
functions. **`private`** provides data hiding (`protected` also hides from outside code, but not from
derived classes). *(file 01 §3, §5)*

**C2.**

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    int accNo;
    string name;
    double balance;
public:
    BankAccount() {                                   // default constructor
        accNo = 0; name = "Unknown"; balance = 0;
    }
    BankAccount(int a, string n, double b) {          // parameterized constructor
        accNo = a; name = n; balance = b;
    }
    ~BankAccount() {                                  // destructor
        cout << "Account " << accNo << " closed" << endl;
    }

    void deposit(double amt) {
        if (amt <= 0) { cout << "Invalid amount" << endl; return; }
        balance += amt;
        cout << "Deposited " << amt << endl;
    }

    void withdraw(double amt) {
        if (amt > balance) { cout << "Insufficient balance!" << endl; return; }
        balance -= amt;
        cout << "Withdrew " << amt << endl;
    }

    void display() {
        cout << "Acc No: " << accNo << ", Name: " << name
             << ", Balance: " << balance << endl;
    }
};

int main() {
    BankAccount a1;                          // default constructor
    BankAccount a2(101, "Riya", 5000);       // parameterized constructor

    a1.display();
    a2.display();
    a2.deposit(1500);
    a2.withdraw(10000);                      // rejected
    a2.withdraw(2000);
    a2.display();
    return 0;                                // destructors run here, in reverse order
}
```

Output:

```text
Acc No: 0, Name: Unknown, Balance: 0
Acc No: 101, Name: Riya, Balance: 5000
Deposited 1500
Insufficient balance!
Withdrew 2000
Acc No: 101, Name: Riya, Balance: 4500
Account 101 closed
Account 0 closed
```

Note the last two lines: **a2 is destroyed before a1** (reverse order of creation). A good line to write
in your answer.

---

## Last 10 minutes before the exam

Read, in this order: `01` §6 table + Traps · `06` §6 delete cases · `04` Traps · `05` Traps.
Anything you missed in this mock goes first.
