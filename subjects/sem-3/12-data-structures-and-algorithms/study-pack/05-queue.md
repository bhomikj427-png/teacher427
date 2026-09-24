# 05 — Queue (and choosing a data structure)

> **MTE blueprint:** CO2. Likely a 2-mark Section A question or a 4-mark Section B theory question
> (§3 circular queue conditions, §5 stack vs queue, §6 comparison table). The §2 queue program
> is the backup for the coding question.

**A1: A6, C2, D4 · 8 of 50 marks · deck 8 · hand-out L14–L15 · CO2**

## Map

```
 FIFO ──► FRONT (delete end) · REAR (insert end)
  │
  ├──► linear array queue ──► the wasted-space problem
  │         (D4)                     │
  │                                  ▼
  │                        circular queue: (i + 1) % MAX
  ├──► linked-list queue
  ├──► types: simple · circular · deque · priority
  │
  └──► stack vs queue ──► array vs stack vs queue vs linked list (C2)
```

---

## 1. FIFO `[A1 A6]`

**Q ▸** A ticket counter line: where do new people join, and who gets served first?

They join at the **back** (REAR), and the person at the **front** (FRONT) is served first. **FIFO: First
In, First Out.** A **queue** is a linear data structure where insertion happens at one end (**REAR**) and
deletion at the other end (**FRONT**).

| | ENQUEUE | DEQUEUE |
|---|---|---|
| Does | **inserts** an element | **removes** an element |
| At | the **REAR** | the **FRONT** |
| Pointer moved | REAR advances | FRONT advances |
| Error | **Overflow**: queue full | **Underflow**: queue empty |

Other operations: **isEmpty**, **isFull**, **peek/front** (see the first element without removing
it), **size**.

**Exam answer (A6):** FIFO means the element inserted first is removed first, like people in a
queue at a ticket counter. **ENQUEUE** inserts at the REAR (and can overflow if the queue is full).
**DEQUEUE** removes from the FRONT (and can underflow if it is empty). A stack adds and removes at the
same end. A queue uses **two different ends**.

---

## 2. Linear queue with an array `[A1 D4 · 4 marks]`

Convention: `front = rear = -1` means empty.

```text
ENQUEUE(x):                               DEQUEUE():
 if rear == MAX − 1: Overflow; stop        if front == −1 or front > rear: Underflow; stop
 if front == −1: front = 0                 x = Q[front]
 rear = rear + 1                           front = front + 1
 Q[rear] = x                               return x
```

```cpp
#include <iostream>
using namespace std;

#define MAX 5

class Queue {
private:
    int arr[MAX];
    int front, rear;
public:
    Queue() { front = -1; rear = -1; }

    bool isEmpty() { return front == -1 || front > rear; }
    bool isFull()  { return rear == MAX - 1; }

    void enqueue(int x) {
        if (isFull()) { cout << "Queue Overflow! Cannot insert " << x << endl; return; }
        if (front == -1) front = 0;     // first element
        arr[++rear] = x;
        cout << "Inserted " << x << endl;
    }

    void dequeue() {
        if (isEmpty()) { cout << "Queue Underflow! Nothing to delete" << endl; return; }
        cout << "Deleted " << arr[front++] << endl;
    }

    void display() {
        if (isEmpty()) { cout << "Queue is empty" << endl; return; }
        cout << "Queue (front to rear): ";
        for (int i = front; i <= rear; i++) cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Queue q;
    q.dequeue();                             // underflow demo
    for (int i = 1; i <= 5; i++) q.enqueue(i * 10);
    q.display();
    q.dequeue();
    q.dequeue();
    q.display();
    q.enqueue(60);                           // overflow, even though 2 slots are free!
    return 0;
}
```

Output:

```text
Queue Underflow! Nothing to delete
Inserted 10
Inserted 20
Inserted 30
Inserted 40
Inserted 50
Queue (front to rear): 10 20 30 40 50 
Deleted 10
Deleted 20
Queue (front to rear): 30 40 50 
Queue Overflow! Cannot insert 60
```

**Q ▸** Look at the last line. Two slots (index 0 and 1) are empty. Why did the queue say it's full?

Because `rear == MAX − 1` and REAR can only move **forward**. The freed slots at the front are never
reused. That is the **main drawback of a linear queue**, and it's exactly why the circular queue
exists.

---

## 3. Circular queue (deck 8 activity)

**Q ▸** When REAR reaches the last index, where could it go next if the array were bent into a ring?

To **index 0**, if that slot is free. The trick is modulo: `next = (i + 1) % MAX`. With MAX = 5,
index 4 → (4 + 1) % 5 = 0.

```text
             [0]
       [4]         [1]         front: next to delete
                                rear:  last inserted
          [3]   [2]            both move clockwise with (i + 1) % MAX
```

| Condition | Test |
|---|---|
| Empty | `front == −1` |
| **Full** | `(rear + 1) % MAX == front` |
| Enqueue | if empty → `front = rear = 0`; else `rear = (rear + 1) % MAX`; `Q[rear] = x` |
| Dequeue | `x = Q[front]`; if `front == rear` (last element) → `front = rear = −1`; else `front = (front + 1) % MAX` |

```cpp
#include <iostream>
using namespace std;

#define MAX 5

class CircularQueue {
private:
    int arr[MAX];
    int front, rear;
public:
    CircularQueue() { front = rear = -1; }

    bool isEmpty() { return front == -1; }
    bool isFull()  { return (rear + 1) % MAX == front; }

    void enqueue(int x) {
        if (isFull()) { cout << "Queue Overflow! Cannot insert " << x << endl; return; }
        if (isEmpty()) front = rear = 0;
        else rear = (rear + 1) % MAX;      // wrap around
        arr[rear] = x;
        cout << "Inserted " << x << " at index " << rear << endl;
    }

    void dequeue() {
        if (isEmpty()) { cout << "Queue Underflow!" << endl; return; }
        cout << "Deleted " << arr[front] << " from index " << front << endl;
        if (front == rear) front = rear = -1;   // queue became empty
        else front = (front + 1) % MAX;
    }

    void peek() {
        if (isEmpty()) cout << "Queue is empty" << endl;
        else cout << "Front element: " << arr[front] << endl;
    }

    void display() {
        if (isEmpty()) { cout << "Queue is empty" << endl; return; }
        cout << "Queue (front to rear): ";
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear) break;
            i = (i + 1) % MAX;
        }
        cout << endl;
    }
};

int main() {
    CircularQueue q;
    for (int i = 1; i <= 5; i++) q.enqueue(i * 10);
    q.enqueue(60);              // full
    q.dequeue();
    q.dequeue();
    q.enqueue(60);              // reuses index 0
    q.enqueue(70);              // reuses index 1
    q.display();
    q.peek();
    return 0;
}
```

Output:

```text
Inserted 10 at index 0
Inserted 20 at index 1
Inserted 30 at index 2
Inserted 40 at index 3
Inserted 50 at index 4
Queue Overflow! Cannot insert 60
Deleted 10 from index 0
Deleted 20 from index 1
Inserted 60 at index 0
Inserted 70 at index 1
Queue (front to rear): 30 40 50 60 70 
Front element: 30
```

**This is what the deck activity means by "demonstrate how the circular queue reuses the vacant
positions":** 60 and 70 went into indices 0 and 1, the two slots the linear queue wasted.

---

## 4. Queue with a linked list, and the types of queue

**Linked queue:** keep **two** pointers, `front` (head) and `rear` (tail).
ENQUEUE = insert at **rear** (O(1), because you have the tail pointer). DEQUEUE = delete at **front** (O(1)).
There's no overflow and no wasted space. When the last node is removed, set **both** to NULL.

| Type | Rule | Use |
|---|---|---|
| **Simple / linear** | insert at rear, delete at front | basic buffering |
| **Circular** | rear wraps to index 0 | CPU round-robin, traffic lights, buffers |
| **Deque** (double-ended) | insert **and** delete at **both** ends | undo + redo, sliding windows |
| **Priority queue** | the highest-priority element leaves first, not the oldest | OS scheduling, Dijkstra (later) |

**Applications of queues:** printer spooling, CPU/process scheduling, keyboard buffer, call-centre
waiting lines, BFS traversal of graphs (later in the course).

---

## 5. Stack vs queue (deck 8 activity)

| | Stack | Queue |
|---|---|---|
| Principle | **LIFO** | **FIFO** |
| Insertion | PUSH at **TOP** | ENQUEUE at **REAR** |
| Deletion | POP from **TOP** (same end) | DEQUEUE from **FRONT** (other end) |
| Pointers | one (top) | two (front, rear) |
| Real life | pile of plates, undo, back button | ticket line, printer jobs |

---

## 6. Choosing the structure `[A1 C2 · 3 marks]`

> Compare array, stack, queue and singly linked list for insertion, deletion, memory allocation and
> element access. Then choose one for a **browser back button**, a **printer queue** and a **dynamic
> student record list**, and justify.

**Q ▸** Before the table: for each of the three uses, which item comes out next, the newest, the
oldest, or any one?

Back: the **newest** page. Printer: the **oldest** job. Records: **any** record, at any time.
That answers the second half before you've written the table.

| | Array | Stack | Queue | Singly linked list |
|---|---|---|---|---|
| **Insertion** | anywhere, O(n) shift | only at TOP, O(1) | only at REAR, O(1) | anywhere, O(1) once the position is reached |
| **Deletion** | anywhere, O(n) shift | only at TOP, O(1) | only at FRONT, O(1) | anywhere, O(1) once the position is reached |
| **Memory** | static, contiguous, fixed size | array (fixed) or linked (dynamic) | array (fixed) or linked (dynamic) | **dynamic**, non-contiguous, extra pointer per node |
| **Access** | **direct / random, O(1)** by index | only the top | only the front | **sequential, O(n)** from head |
| **Order** | by index | LIFO | FIFO | by links |

**Choices:**
- **Browser back button → Stack.** Each visited page is PUSHed. Back POPs the most recent page, and the
  last page visited is the first one returned to (**LIFO**).
- **Printer queue → Queue.** Jobs are printed in the order they were sent, so the first job submitted
  is printed first (**FIFO**). Fairness needs this.
- **Dynamic student record list → Singly linked list.** The number of students changes (admissions,
  withdrawals), so a **dynamic size** avoids a fixed array. Inserting or deleting a record needs only a
  pointer change, not shifting, and records can be added or removed **anywhere**, not just at one end.
  (Trade-off, worth one line: no direct access, so finding a record is O(n).)

---

## Traps

- Circular **full** test: `(rear + 1) % MAX == front`, not `rear == MAX − 1`.
- A linear queue can say "full" with empty slots. Name that drawback when asked why circular queues exist.
- When the last element is dequeued, reset **both** front and rear (to −1, or NULL).
- ENQUEUE is at the **rear**, DEQUEUE at the **front**. Don't swap them.

## Self-test

1. Circular queue, MAX = 4, front = 2, rear = 1. Full or not?
2. Circular queue, MAX = 5, rear = 4. At what index does the next enqueue go (if not full)?
3. Which queue type lets you insert and delete at both ends?
4. Undo in an editor: stack or queue? Print jobs: stack or queue?

## Answers

1. (1 + 1) % 4 = 2 = front → **full**.
2. (4 + 1) % 5 = **0**.
3. **Deque.**
4. Undo: **stack**. Print jobs: **queue**.
