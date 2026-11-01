# 9 · Exp 10 — Queue using an array (enqueue, dequeue)

<div class="sub">A queue is a line at a ticket counter: join at the back (rear), leave from the front. Two indexes, front and rear, do all the work.</div>

[[map:Two ends > enqueue: rear++ > dequeue: front++ > FIFO > linear-queue flaw > circular queue|here=1]]

## 9.1 The idea

A **queue** inserts at the **rear** and removes from the **front**: **FIFO** (First In, First Out). `front` and `rear` both start at **−1** (empty).

:::guess Guess first
MAX = 5. Enqueue 1, 2, 3, 4, 5, dequeue twice, then enqueue 6. There are 2 empty slots. Does the program accept 6?
:::

[[fig:queue_fig|The manual's example: enqueue 10, 20, 30, then one dequeue.]]

| Operation | Check first | Then |
|---|---|---|
| **enqueue(v)** | `rear == MAX-1` → Overflow | if `front == -1` set `front = 0`; `rear++`; `queueArr[rear] = v` |
| **dequeue()** | `front == -1` → Underflow | print `queueArr[front]`; if `front == rear` (last one) reset both to −1, else `front++` |
| **display()** | `front == -1` → empty | print `queueArr[front]` … `queueArr[rear]` |

:::key Why reset to −1 when the last element leaves
After dequeuing the only element, front would pass rear, which is confusing. Resetting both to −1 means "empty" is always `front == -1`, and the next enqueue starts again from index 0.
:::

## 9.2 The program (corrected)

The manual's **listing** (page 5) is right; its **screenshot** (page 9) doesn't compile. In the screenshot, `enqueue(value);` sits after the `if`'s closing brace, so the next `else` has no `if`; choice 3 prints "Program terminated" instead of displaying; and there's a bare `else` with no statement:

[[err:m10_screenshot]]

Two more fixes: the array is renamed from `queue` to `queueArr` (with `#include <bits/stdc++.h>`, `queue` clashes with the library's `std::queue`), and the dead `|| front > rear` test is dropped (after the reset rule it can never be true).

[[code:e10_queue.cpp]]

The manual's Sample Inputs 1 and 2 in one run:

[[run:e10]]

## 9.3 The linear queue's flaw (a favourite viva question)

[[fig:queue_waste|Slots freed by dequeue are never reused, because rear only moves forward.]]

[[run:e10_limits]]

Underflow on the empty queue; then 1–5 fill it; 6 overflows (correct, it's full); two dequeues free slots 0 and 1, **yet 7 still overflows**, because rear is still MAX−1. The fix is the **circular queue** (9.5).

:::write Write in your record
**Aim:** To implement a queue using an array and perform enqueue, dequeue and display operations.
**Algorithm:** front = rear = −1. *Enqueue:* if rear == MAX−1 → overflow; else (if front == −1, front = 0), rear++, queue[rear] = value. *Dequeue:* if front == −1 → underflow; else print queue[front]; if front == rear, front = rear = −1, else front++. *Display:* print queue[front…rear].
**Complexity:** enqueue O(1), dequeue O(1), display O(n); space O(MAX).
**Result:** Enqueued 10, 20, 30 (display 10 20 30); dequeue removed 10 (display 20 30), confirming FIFO. Overflow and underflow were detected.
:::

## 9.4 Viva questions

| Question | Answer |
|---|---|
| What is FIFO? | First In, First Out: elements leave in the order they arrived. |
| Where is insertion / deletion done? | Insertion at the rear, deletion at the front. |
| Overflow / underflow conditions? | rear == MAX−1 / front == −1. |
| Drawback of a linear array queue? | Freed slots at the front are never reused, so it can report overflow while slots are empty. |
| How does a circular queue fix it? | Indexes wrap: `rear = (rear + 1) % MAX`, so slot 0 is reused after slot MAX−1. |
| Applications? | CPU and printer scheduling, keyboard buffers, network packets, breadth-first search. |
| Why are enqueue and dequeue O(1)? | Each touches one index; nothing is shifted (unlike array deletion in Exp 4). |

## 9.5 If the examiner changes the question

**Circular queue** (full program). The only changes from Exp 10: wrap with `% MAX`, and "full" becomes `(rear + 1) % MAX == front`.

[[fig:circular_queue|After enqueue 1–5, dequeue 1 and 2, enqueue 6 and 7: the new values reuse slots 0 and 1.]]

[[code:e10b_circular_queue.cpp]]

The same sequence that defeated the linear queue. 6 and 7 are now accepted:

[[run:e10b]]

**Linear vs. circular queue** ("WAP to compare"): run both programs on the input above. The linear one reports overflow with free slots; the circular one stores 6 and 7. Both are O(1) per operation.

**Peek, isEmpty / isFull, show front and rear** (add to Exp 10's program and to the menu):
[[snip:t_10.cpp#peek]]
[[snip:t_10.cpp#emptyFull]]
[[snip:t_10.cpp#frontRear]]

**Reverse the queue** (swap the two ends, move inwards):
[[snip:t_10.cpp#reverseQueue]]

**Queue using a linked list** (read chapter 10 first; no MAX, so no overflow):
[[snip:t_10.cpp#linkedQueue]]

**Queue for CPU scheduling (FCFS).** Processes are served in arrival order. Tested: bursts 24, 3, 3 give waiting times 0, 24, 27, average 17.
[[snip:t_10.cpp#fcfs]]

:::check Check 9.1
MAX = 4, linear queue. enqueue 5, enqueue 6, dequeue, dequeue, enqueue 7. What are front and rear after each step?
:::

:::check Check 9.2
Circular queue, MAX = 4, front = 2, rear = 3. Enqueue 9: which index is it stored at? Is the queue full now?
:::

<!--ANSWERS-->
## Answers

**Check 9.1:** enqueue 5 → front 0, rear 0. enqueue 6 → 0, 1. dequeue (5) → 1, 1. dequeue (6): front == rear → reset → −1, −1. enqueue 7 → 0, 0.

**Check 9.2:** rear = (3 + 1) % 4 = **0**, so 9 goes to index 0. Full? (0 + 1) % 4 = 1 ≠ front (2), so **not full**: index 1 is still free.
<!--/ANSWERS-->
