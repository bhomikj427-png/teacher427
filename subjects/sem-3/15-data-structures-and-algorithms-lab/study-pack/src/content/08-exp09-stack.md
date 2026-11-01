# 8 · Exp 9 (probable) — Stack using an array

<div class="sub"><b>Not in your uploaded files.</b> No Exp 9 file arrived, but Exp 10's figures are captioned "Enqueue Operation on Stack", which points to a stack experiment just before it. This chapter is written in exactly the style of Exp 10, so if Exp 9 is Stack, you're covered. Confirm with a classmate.</div>

[[map:One open end (top) > push: top++, store > pop: read, top-- > LIFO|here=1]]

## 8.1 The idea

A **stack** is a pile: you add and remove only at the **top**. The last item pushed is the first popped: **LIFO** (Last In, First Out). Examples: undo history, the browser back button, function calls (the "call stack" quick sort's recursion uses).

:::guess Guess first
Push 10, 20, 30, then pop twice. Which values come out, in what order, and what is left?
:::

[[fig:stack_fig|An array stack after pushing 10, 20, 30. top is the index of the top element; −1 means empty.]]

## 8.2 The program

New C++ here (also used in Exp 10):

- **`#define MAX 5`**: the compiler replaces every `MAX` with 5. Change it in one place to resize.
- **Global variables** (declared above all functions): `stackArr` and `top` are shared by `push`, `pop`, `peek`, `display` and `main`.
- **Menu loop:** `do { show menu; read choice; act } while (choice != 5);` runs until the user picks Exit.

[[code:e09_stack.cpp]]

Push 10, 20, 30 → display → peek → pop all three → pop again (underflow) → exit:

[[run:e09]]

Overflow test (6 pushes into MAX = 5):

[[run:e09_over]]

:::write Write in your record
**Aim:** To implement a stack using an array with push, pop, peek and display operations.
**Algorithm:** top = −1. *Push:* if top == MAX−1 → overflow; else top++, stackArr[top] = value. *Pop:* if top == −1 → underflow; else print stackArr[top], top−−. *Peek:* print stackArr[top]. *Display:* print from top down to 0.
**Complexity:** push, pop, peek O(1); display O(n); space O(MAX).
**Result:** Pushed 10, 20, 30; popped 30, 20, 10 (LIFO). Overflow on the 6th push and underflow on popping an empty stack were detected.
:::

## 8.3 Viva questions

| Question | Answer |
|---|---|
| What is LIFO? | Last In, First Out: the most recently added item is removed first. |
| Overflow / underflow? | Push onto a full stack (top == MAX−1) / pop from an empty stack (top == −1). |
| Why does top start at −1? | So the first push makes it 0, the first array index. −1 = empty. |
| Stack vs. queue? | Stack: one end, LIFO. Queue: insert at rear, delete at front, FIFO. |
| Applications? | Function calls and recursion, undo, expression evaluation (postfix), bracket matching, backtracking. |
| Does pop erase the value? | No, it only moves top down; the old value is overwritten by the next push. |

:::check Check 8.1
MAX = 3. Operations: push 4, push 7, pop, push 9, push 2, push 6. What does each print? What is top at the end?
:::

<!--ANSWERS-->
## Answers

**Check 8.1:** 4 pushed (top 0), 7 pushed (top 1), pop prints 7 (top 0), 9 pushed (top 1), 2 pushed (top 2), push 6 → **Stack Overflow!** (top == MAX−1 = 2). top ends at **2**, and the stack is 4 9 2 (bottom → top).
<!--/ANSWERS-->
