# 04 — Stack

**A1: B3, B5, C1, C4, D3 · 14 of 50 marks · deck 7 · hand-out L12–L14 · CO2**

**The highest-yield file.** Five A1 questions. On the exam, a stack trace or an expression conversion is a
near-certain short question, and a stack program a near-certain long one.

## Map

```
 LIFO ──► array stack: TOP, MAX ──► PUSH / POP / PEEK / DISPLAY (B5)
  │            └─ overflow  TOP == MAX−1        underflow  TOP == −1
  │                         └────────── trace an operation sequence (C1)
  ├──► linked-list stack (no overflow)
  │
  └──► applications
         ├─ infix / prefix / postfix, precedence
         ├─ infix → postfix, by hand with stack table (B3) ── program (D3)
         └─ evaluate postfix with a stack (C4)
```

---

## 1. LIFO and the array stack

**Q ▸** A pile of plates: you add plates on top and take them from the top. Which plate comes off
first, the first one added or the last?

The **last**. **LIFO: Last In, First Out.** A **stack** is a linear data structure (an **ADT**) where
insertion and deletion both happen at **one end only**, called the **TOP**.

| Operation | Does | Array version | Error |
|---|---|---|---|
| **PUSH(x)** | add on top | `top++; stack[top] = x;` | **Overflow** if `top == MAX − 1` |
| **POP()** | remove and return top | `x = stack[top]; top--;` | **Underflow** if `top == −1` |
| **PEEK()** | return top, don't remove | `return stack[top];` | empty if `top == −1` |
| **isEmpty()** | | `top == −1` | |
| **isFull()** | | `top == MAX − 1` | |

**TOP starts at −1** (empty). With MAX = 5, the valid indices are 0–4, so the stack is full when TOP = 4.

The deck's algorithms (write them in exactly this shape):

```text
Algorithm PUSH(STACK, TOP, MAX, ITEM)          Algorithm POP(STACK, TOP)
1. If TOP == MAX − 1:                          1. If TOP == −1:
       print "Stack Overflow"; stop                   print "Stack Underflow"; stop
2. TOP = TOP + 1                               2. ITEM = STACK[TOP]
3. STACK[TOP] = ITEM                           3. TOP = TOP − 1
4. stop                                        4. return ITEM; stop
```

Note the order: PUSH **increments first, then stores**. POP **reads first, then decrements**.

---

## 2. Tracing a stack `[A1 C1 · 3 marks]`

> Analyze an array-based stack and identify its condition after these operations. Explain where
> overflow or underflow can occur.
> `PUSH(10) PUSH(20) POP() POP() POP() PUSH(30) PUSH(40)`

**Q ▸** Before reading: at which operation does something go wrong?

The question doesn't give MAX, so **state your assumption** (MAX = 5). That's a free mark and it
shows you know overflow depends on it.

| # | Operation | TOP after | Stack (bottom → top) | Note |
|---|---|---|---|---|
| 0 | start | −1 | empty | |
| 1 | PUSH(10) | 0 | 10 | |
| 2 | PUSH(20) | 1 | 10 20 | |
| 3 | POP() | 0 | 10 | returns 20 |
| 4 | POP() | −1 | empty | returns 10 |
| 5 | POP() | −1 | empty | **UNDERFLOW**: TOP == −1, nothing to pop. TOP stays −1 |
| 6 | PUSH(30) | 0 | 30 | |
| 7 | PUSH(40) | 1 | 30 40 | |

**Final condition:** TOP = 1, stack = [30, 40], and 40 is on top.
**Underflow** occurs at operation 5, a POP on an empty stack.
**Overflow does not occur:** at most 2 elements are ever present. It would occur only if MAX were 1
(at PUSH(20) or PUSH(40)). In general, overflow happens on a PUSH when TOP == MAX − 1.

---

## 3. Program: array stack `[A1 B5 · 2 marks]`

> Implement a stack using an array with PUSH, POP, PEEK and DISPLAY. Handle overflow and underflow.

```cpp
#include <iostream>
using namespace std;

#define MAX 5

class Stack {
private:
    int arr[MAX];
    int top;
public:
    Stack() { top = -1; }                 // empty stack

    bool isEmpty() { return top == -1; }
    bool isFull()  { return top == MAX - 1; }

    void push(int x) {
        if (isFull()) { cout << "Stack Overflow! Cannot push " << x << endl; return; }
        arr[++top] = x;                   // increment, then store
        cout << "Pushed " << x << endl;
    }

    int pop() {
        if (isEmpty()) { cout << "Stack Underflow! Nothing to pop" << endl; return -1; }
        int x = arr[top--];               // read, then decrement
        cout << "Popped " << x << endl;
        return x;
    }

    void peek() {
        if (isEmpty()) cout << "Stack is empty" << endl;
        else cout << "Top element: " << arr[top] << endl;
    }

    void display() {
        if (isEmpty()) { cout << "Stack is empty" << endl; return; }
        cout << "Stack (top to bottom): ";
        for (int i = top; i >= 0; i--) cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Stack s;
    s.pop();                               // underflow demo
    for (int i = 1; i <= 6; i++) s.push(i * 10);   // 6th push overflows
    s.display();
    s.peek();
    s.pop();
    s.pop();
    s.display();
    return 0;
}
```

Output:

```text
Stack Underflow! Nothing to pop
Pushed 10
Pushed 20
Pushed 30
Pushed 40
Pushed 50
Stack Overflow! Cannot push 60
Stack (top to bottom): 50 40 30 20 10 
Top element: 50
Popped 50
Popped 40
Stack (top to bottom): 30 20 10 
```

---

## 4. Stack using a linked list (hand-out L13)

**Q ▸** Where in a linked list should the TOP be: at the head or at the tail?

At the **head.** Insert-at-beginning and delete-at-beginning are both O(1) (file 03). At the tail,
POP would have to walk the whole list to find the node before the last.

- PUSH = **insert at beginning**. POP = **delete from beginning**. `top` = `head`.
- **No overflow** (until the machine runs out of memory). Underflow is still `top == NULL`.

```text
PUSH(x): newNode->data = x; newNode->next = top; top = newNode;
POP():   if (top == NULL) underflow;
         temp = top; x = temp->data; top = top->next; delete temp; return x;
```

| | Array stack | Linked stack |
|---|---|---|
| Size | fixed MAX | dynamic |
| Overflow | yes | no (only if memory runs out) |
| Memory per item | just the data | data + pointer |

---

## 5. Applications, and the three notations

**Applications of a stack** (list 4–5): **expression conversion** (infix → postfix/prefix) ·
**postfix evaluation** · **function calls and recursion** (the call stack, file 06) · **parenthesis
matching** · **undo** in editors · the **browser back button** · **reversing** a string.

**Q ▸** `A + B * C`: which operation happens first, and how would a computer know without being
taught precedence?

`B * C` first. In **postfix**, `A B C * +`, the order is written into the **position** of the operators,
so no precedence rules or brackets are needed. That's why compilers convert to postfix.

| Notation | Operator position | `A + B` | `A + B * C` | Also called |
|---|---|---|---|---|
| **Infix** | between operands | `A + B` | `A + B * C` | (normal) |
| **Prefix** | **before** operands | `+ A B` | `+ A * B C` | Polish notation |
| **Postfix** | **after** operands | `A B +` | `A B C * +` | **Reverse Polish** (RPN) |

**Precedence** (deck 7): **`^`** highest → **`*` `/`** → **`+` `-`** lowest.
**Associativity:** `* / + -` are **left to right**. `^` is **right to left** (`2^3^2 = 2^9`).

**Doing it by hand** (a quick check of your stack-table answer): fully bracket by precedence, then move
each operator to just **after** (postfix) or just **before** (prefix) its bracket, and drop the brackets.

```text
A + B * C  →  (A + (B * C))  →  postfix: A (B C *) +  = A B C * +
                              →  prefix:  + A (* B C)  = + A * B C
```

---

## 6. Infix → postfix with a stack `[A1 B3 · 2 marks]`

**The algorithm (deck 7):** scan left to right.
- **Operand** → append it to the postfix output.
- **`(`** → push it.
- **`)`** → pop to the output until `(`, then discard the `(`.
- **Operator** → while the top of the stack is an operator of **higher or equal** precedence, pop it to
  the output. Then push the current operator. (For **`^`**: pop only on strictly **higher**, because
  it's right-associative.)
- **End of input** → pop everything remaining to the output.

> Convert `((A+B)/C)(D-E)` and show the operator stack at each step.

**Q ▸** Something's missing between `)` and `(`. What?

An operator. `)(` means **multiplication** (implicit, as in algebra). Say so in your answer and treat
it as `((A+B)/C) * (D-E)`.

| Step | Symbol | Stack (bottom → top) | Postfix so far |
|---|---|---|---|
| 1 | ( | ( | |
| 2 | ( | ( ( | |
| 3 | A | ( ( | A |
| 4 | + | ( ( + | A |
| 5 | B | ( ( + | A B |
| 6 | ) | ( | A B + |
| 7 | / | ( / | A B + |
| 8 | C | ( / | A B + C |
| 9 | ) | *empty* | A B + C / |
| 10 | * | * | A B + C / |
| 11 | ( | * ( | A B + C / |
| 12 | D | * ( | A B + C / D |
| 13 | - | * ( - | A B + C / D |
| 14 | E | * ( - | A B + C / D E |
| 15 | ) | * | A B + C / D E - |
| 16 | end | *empty* | **A B + C / D E - \*** |

**Answer: `AB+C/DE-*`**

Check it by hand: `((A+B)/C) * (D-E)` → `(AB+ C /)` then `(DE-)` then `*` → `AB+C/DE-*`. ✔

**Deck 7 worked example** (practise it): `((8 + (6 − 2)) × 5) ÷ 4`
→ postfix **`8 6 2 − + 5 × 4 ÷`** → value **15** (6−2 = 4, 8+4 = 12, 12×5 = 60, 60÷4 = 15).

---

## 7. Evaluate postfix `[A1 C4 · 3 marks]`

**The algorithm (deck 7):** scan left to right.
- **Operand** → push it.
- **Operator** → pop **A** (the top), then pop **B** (the next one), compute **B op A**, and push the result.
- At the end, the single value left on the stack is the answer.

**Q ▸** In `6 2 /`, you pop 2 then 6. Is the answer 2/6 or 6/2?

**6 / 2 = 3.** The **second** value popped is the **left** operand. For `+` and `*` it doesn't matter,
but for **`-` and `/` it does**, and it's the most common error in this question.

> Evaluate `12 3 4 * + 6 2 / -`, showing the stack after every operator.

| Step | Token | Action | Stack (bottom → top) |
|---|---|---|---|
| 1 | 12 | push | 12 |
| 2 | 3 | push | 12 3 |
| 3 | 4 | push | 12 3 4 |
| 4 | * | pop 4, pop 3 → 3 × 4 = 12, push | **12 12** |
| 5 | + | pop 12, pop 12 → 12 + 12 = 24, push | **24** |
| 6 | 6 | push | 24 6 |
| 7 | 2 | push | 24 6 2 |
| 8 | / | pop 2, pop 6 → 6 / 2 = 3, push | **24 3** |
| 9 | - | pop 3, pop 24 → 24 − 3 = 21, push | **21** |

**Result = 21.** (In infix it is `12 + 3*4 − 6/2`.)

The C4 program. It reads space-separated tokens, so **multi-digit numbers like 12 work**, and it
prints the stack after each operator as the question asks:

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

#define MAX 50
int st[MAX];
int top = -1;

void push(int x) {
    if (top == MAX - 1) { cout << "Stack Overflow" << endl; return; }
    st[++top] = x;
}

int pop() {
    if (top == -1) { cout << "Stack Underflow" << endl; return 0; }
    return st[top--];
}

void showStack() {
    cout << "  stack: ";
    for (int i = 0; i <= top; i++) cout << st[i] << " ";
    cout << endl;
}

int main() {
    string expr = "12 3 4 * + 6 2 / -";
    stringstream ss(expr);
    string tok;
    cout << "Postfix: " << expr << endl;

    while (ss >> tok) {
        if (tok == "+" || tok == "-" || tok == "*" || tok == "/") {
            int a = pop();          // top  = right operand
            int b = pop();          // next = left operand
            int r;
            if (tok == "+") r = b + a;
            else if (tok == "-") r = b - a;
            else if (tok == "*") r = b * a;
            else r = b / a;
            push(r);
            cout << "After '" << tok << "' (" << b << " " << tok << " " << a << " = " << r << ")" << endl;
            showStack();
        } else {
            push(stoi(tok));        // operand
        }
    }
    cout << "Result = " << pop() << endl;
    return 0;
}
```

Output:

```text
Postfix: 12 3 4 * + 6 2 / -
After '*' (3 * 4 = 12)
  stack: 12 12 
After '+' (12 + 12 = 24)
  stack: 24 
After '/' (6 / 2 = 3)
  stack: 24 3 
After '-' (24 - 3 = 21)
  stack: 21 
Result = 21
```

---

## 8. Program: infix → postfix `[A1 D3 · 4 marks]`

> General in nature and fully user friendly.

Single-letter or single-digit operands, `+ - * / ^`, and brackets. The user types the expression.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

#define MAX 100
char st[MAX];
int top = -1;

void push(char c) { if (top < MAX - 1) st[++top] = c; }
char pop()        { return (top == -1) ? '\0' : st[top--]; }
char peek()       { return (top == -1) ? '\0' : st[top]; }

int prec(char op) {
    if (op == '^') return 3;
    if (op == '*' || op == '/') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;                          // '(' or empty
}

string infixToPostfix(string infix) {
    string postfix = "";
    for (char c : infix) {
        if (c == ' ') continue;
        if (isalnum(c)) {                      // operand
            postfix += c;
        } else if (c == '(') {
            push(c);
        } else if (c == ')') {
            while (top != -1 && peek() != '(') postfix += pop();
            pop();                              // discard '('
        } else {                                // operator
            while (top != -1 && peek() != '(' &&
                   (prec(peek()) > prec(c) ||
                   (prec(peek()) == prec(c) && c != '^')))   // ^ is right-assoc
                postfix += pop();
            push(c);
        }
    }
    while (top != -1) postfix += pop();         // empty the stack
    return postfix;
}

int main() {
    // Sample input: ((A+B)/C)*(D-E)
    string infix;
    cout << "Enter an infix expression (use * for multiplication): ";
    getline(cin, infix);
    cout << "\nPostfix: " << infixToPostfix(infix) << endl;
    return 0;
}
```

Output (with the sample input):

```text
Enter an infix expression (use * for multiplication): 
Postfix: AB+C/DE-*
```

The output matches the hand trace in §6.

---

## Traps

- **Overflow** is `TOP == MAX − 1`, **not** `TOP == MAX`. **Underflow** is `TOP == −1`.
- PUSH: increment **then** store. POP: read **then** decrement.
- In postfix evaluation the **second** value popped is the **left** operand: `B op A`.
- Operators of **equal** precedence: pop the stack's one first (left-to-right), **except `^`**.
- `)(` in an expression means **multiply**, so say so.
- Operands go **straight to the output**. Only operators and `(` ever go on the stack.
- Postfix and prefix need **no brackets**.

## Self-test

1. MAX = 3. `PUSH 1, PUSH 2, PUSH 3, PUSH 4, POP, POP` — where's the error, and what's left?
2. Convert `A + B * C - D` to postfix.
3. Convert `A * (B + C) / D` to postfix and prefix.
4. Evaluate postfix `5 3 - 4 *`.
5. Evaluate postfix `2 3 4 * + 5 -`.
6. Why is a linked-list stack's TOP kept at the head?

## Answers

1. PUSH 4 → **overflow** (TOP = 2 = MAX − 1). Two POPs remove 3 and 2. Left: [1], TOP = 0.
2. `A B C * + D -`
3. Postfix `A B C + * D /`. Prefix `/ * A + B C D`.
4. 5 − 3 = 2, then 2 × 4 = **8**.
5. 3 × 4 = 12, 2 + 12 = 14, 14 − 5 = **9**.
6. Insert/delete at the head are O(1). At the tail, POP would have to walk the list.
