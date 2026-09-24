# 03 — Linked list

**A1: B1, C5, D2 · 9 of 50 marks · no deck yet · hand-out L8–L12 (5 lectures) · CO2**

> **Why this file matters more than the decks suggest:** none of the 8 decks covers linked lists, but
> the hand-out gives them **5 lectures** before the MTE and A1 asks about them **three times**. A slide
> set is probably missing. The content here is standard textbook material.

## Map

```
 array's two problems: fixed size, O(n) shifting
        │
        ▼
 node = [ data | next ] ──► head ──► ... ──► NULL
        │
        ├──► representation in memory: INFO[] + LINK[] + START
        ├──► types: singly · doubly · circular · circular doubly
        │
        ▼
 traverse ─ search ─ insert (begin / end / after) ─ delete ─ sort by swapping data
   (B1)                (C5)                         (B1)       (D2)
```

---

## 1. Why a linked list

**Q ▸** You have 1000 records in an array and must insert one at the front, 50 times a day. What does
the array cost you each time?

**999 shifts**, every time. And if record 1001 arrives, the array is **full**. A linked list fixes
both problems: **no shifting** (you change two pointers) and **no fixed size** (you allocate each node
as it's needed).

**What it gives up:** **no direct access**. To reach the 500th node you walk 499 links: O(n), not O(1).
Each node also stores an extra pointer.

| | Array | Linked list |
|---|---|---|
| Memory | contiguous | scattered, joined by pointers |
| Size | fixed (static) | grows/shrinks (dynamic) |
| Access k-th element | **O(1)** by index | O(n), traverse from head |
| Insert/delete at front | O(n), shifting | **O(1)**, pointer change |
| Extra memory | none | one pointer per node |
| Wasted space | unused capacity | none |

---

## 2. The node and the list

**Q ▸** If nodes are scattered anywhere in memory, how does the program find the second one?

The first node **stores the address** of the second. Every node carries its data **plus** a pointer
to the next node.

```text
 head
  │
  ▼
┌────┬───┐    ┌────┬───┐    ┌────┬──────┐
│ 10 │ ●─┼───►│ 20 │ ●─┼───►│ 30 │ NULL │
└────┴───┘    └────┴───┘    └────┴──────┘
 data  next
```

```text
struct Node {
    int data;       // INFO part
    Node *next;     // LINK part: address of the next node
};
Node *head = NULL;  // empty list
```

- **head** (START) points to the first node. **If head is lost, the whole list is lost.**
- The last node's `next` is **NULL**, which marks the end.
- An empty list is `head == NULL`.

**Representing a linked list in memory (syllabus wording):** textbooks also show it **without
pointers**, as two parallel arrays, **INFO[k]** for the data and **LINK[k]** for the *index* of the
next node, plus a variable **START** holding the index of the first node. LINK = 0 (or −1) means NULL.

```text
 START = 4
  k :   1    2    3    4    5
 INFO:  C    –    E    A    B       list: A → B → C → E
 LINK:  3    –    0    5    1       (4 → 5 → 1 → 3 → end)
```

Unused cells form a second list called the **AVAIL** list (free storage).

**Types of linked list:**

| Type | Node | Last node points to | Can go backwards? |
|---|---|---|---|
| **Singly** | data, next | NULL | no |
| **Doubly** | prev, data, next | NULL | **yes** |
| **Circular (singly)** | data, next | **the first node** | no, but it loops |
| **Circular doubly** | prev, data, next | first node, and first's prev = last | yes |

**Applications:** implementing stacks and queues (files 04/05), polynomial arithmetic (one node per
term), dynamic memory management (free lists), music playlists / image viewer next-prev (doubly),
round-robin CPU scheduling (circular), undo history.

---

## 3. Traversal and searching

**Q ▸** Why do you traverse with a separate pointer `temp` instead of moving `head` itself?

Moving `head` **loses the list**: nothing points to the first node any more.

```text
TRAVERSE:
1. PTR = START
2. Repeat while PTR ≠ NULL:
       process INFO[PTR]
       PTR = LINK[PTR]
3. Exit

SEARCH(ITEM) — unsorted list:
1. PTR = START
2. Repeat while PTR ≠ NULL:
       If ITEM == INFO[PTR]: LOC = PTR, exit   (found)
       Else PTR = LINK[PTR]
3. LOC = NULL                                (not found)
```

In a **sorted** list the search can also stop as soon as `INFO[PTR] > ITEM`. It is still O(n):
**binary search does not work on a linked list** because there's no direct access to the middle.

---

## 4. Insertion — three cases

**Q ▸** Inserting at the beginning: which do you do first, `newNode->next = head` or `head = newNode`?

**`newNode->next = head` first.** If you set `head = newNode` first, the old first node's address is
gone and the rest of the list is lost. **Always connect the new node before you break the old link.**

```text
 AT BEGINNING                       AT END
 newNode->next = head;              if head == NULL: head = newNode
 head = newNode;                    else: walk temp to the last node
                                          temp->next = newNode
                                    (newNode->next = NULL)

 AFTER A GIVEN NODE (position/value)
 walk temp to that node
 newNode->next = temp->next;   ◄ first: connect to the rest
 temp->next = newNode;         ◄ then: hook in
```

Insert-at-beginning is **O(1)**. Insert-at-end is **O(n)** (walk to the last node), or O(1) if you also
keep a `tail` pointer.

## 5. Deletion

**Q ▸** To delete a node from the middle, which node's pointer do you have to change?

The node **before** it, so you stop one step early. Then `prev->next = target->next;` skips the target,
and `delete target;` frees its memory. **Forgetting `delete` leaks memory**, and examiners notice.

Cases: **empty list** (underflow, nothing to do) · **deleting the head** (`head = head->next`) ·
**middle or end** (need `prev`) · **value not found**.

---

## 6. The full program `[A1 B1 · 2 marks]` (covers C5 too)

> Create a singly linked list and perform insertion at the beginning, insertion at the end, deletion of
> a node, searching, and traversal.

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *next;
};

Node *head = NULL;

void insertAtBeginning(int value) {
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = head;       // 1. connect to the old first node
    head = newNode;             // 2. then move head
}

void insertAtEnd(int value) {
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = NULL;
    if (head == NULL) {         // empty list: new node is the head
        head = newNode;
        return;
    }
    Node *temp = head;
    while (temp->next != NULL)  // walk to the last node
        temp = temp->next;
    temp->next = newNode;
}

void insertAfter(int key, int value) {    // insert after the node holding key
    Node *temp = head;
    while (temp != NULL && temp->data != key)
        temp = temp->next;
    if (temp == NULL) { cout << key << " not found" << endl; return; }
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = temp->next; // 1. connect to the rest
    temp->next = newNode;       // 2. hook in
}

void deleteNode(int value) {
    if (head == NULL) { cout << "List is empty" << endl; return; }
    Node *temp = head;
    if (head->data == value) {  // deleting the first node
        head = head->next;
        delete temp;
        cout << "Deleted " << value << endl;
        return;
    }
    Node *prev = NULL;
    while (temp != NULL && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) { cout << value << " not found" << endl; return; }
    prev->next = temp->next;    // bypass the node
    delete temp;                // free memory
    cout << "Deleted " << value << endl;
}

void search(int value) {
    Node *temp = head;
    int pos = 1;
    while (temp != NULL) {
        if (temp->data == value) {
            cout << value << " found at position " << pos << endl;
            return;
        }
        temp = temp->next;
        pos++;
    }
    cout << value << " not found" << endl;
}

void traverse() {
    if (head == NULL) { cout << "List is empty" << endl; return; }
    Node *temp = head;
    while (temp != NULL) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

int main() {
    insertAtEnd(20);
    insertAtEnd(30);
    insertAtBeginning(10);
    insertAtEnd(40);
    traverse();

    insertAfter(20, 25);
    traverse();

    search(30);
    search(99);

    deleteNode(10);   // head
    deleteNode(30);   // middle
    deleteNode(99);   // absent
    traverse();
    return 0;
}
```

Output:

```text
10 -> 20 -> 30 -> 40 -> NULL
10 -> 20 -> 25 -> 30 -> 40 -> NULL
30 found at position 4
99 not found
Deleted 10
Deleted 30
99 not found
20 -> 25 -> 40 -> NULL
```

**For C5 ("write a C++ program to implement linked list insertion", 3 marks):** write the `Node`
struct, `insertAtBeginning`, `insertAtEnd`, `insertAfter`, `traverse` and a `main` that uses all three.
Draw the before/after pointer diagram for one insertion. It is quick and shows understanding.

---

## 7. Sort a linked list by swapping data `[A1 D2 · 4 marks]`

**Q ▸** "Sort by swapping **data**" versus sorting by re-linking nodes: which is easier?

Swapping **data** is far easier. The nodes stay where they are, and you just exchange the numbers
inside them, exactly like bubble sort on an array. Re-linking means rewiring up to four pointers per swap.

**Bubble sort on a list:** make repeated passes. In each pass, compare every adjacent pair `(p, p->next)`
and swap their data if they're out of order. Stop after a pass with **no swaps**.

"General in nature and fully user friendly" means it **reads** the count and values from the user and
handles an empty list:

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *next;
};

Node *head = NULL;

void insertAtEnd(int value) {
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = NULL;
    if (head == NULL) { head = newNode; return; }
    Node *temp = head;
    while (temp->next != NULL) temp = temp->next;
    temp->next = newNode;
}

void display() {
    for (Node *t = head; t != NULL; t = t->next) cout << t->data << " ";
    cout << endl;
}

void sortList() {                       // bubble sort, swapping data only
    if (head == NULL || head->next == NULL) return;   // 0 or 1 node: already sorted
    bool swapped;
    do {
        swapped = false;
        for (Node *p = head; p->next != NULL; p = p->next) {
            if (p->data > p->next->data) {
                int t = p->data;
                p->data = p->next->data;
                p->next->data = t;
                swapped = true;
            }
        }
    } while (swapped);
}

int main() {
    // Sample input: 5  then  40 10 50 20 30
    int n, value;
    cout << "How many elements? ";
    cin >> n;
    if (n <= 0) { cout << "Nothing to sort" << endl; return 0; }
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> value;
        insertAtEnd(value);
    }
    cout << "\nBefore sorting: ";
    display();
    sortList();
    cout << "After sorting:  ";
    display();
    return 0;
}
```

Output (with the sample input):

```text
How many elements? Enter 5 elements: 
Before sorting: 40 10 50 20 30 
After sorting:  10 20 30 40 50 
```

(On screen your typed numbers appear after each prompt. They're missing above only because the
input was piped in.)

---

## Traps

- **Connect before you break**: `newNode->next = head;` then `head = newNode;`.
- Traverse with `temp`, **never** by moving `head`.
- Check `head == NULL` **before** touching `head->next`, or the program crashes.
- Delete needs the **previous** node, and `delete` the removed one.
- The last node's `next` must be **NULL**, or traversal never stops.
- Binary search does **not** work on linked lists.

## Self-test

1. List `5 → 8 → 3`. Write the two statements to insert 1 at the front, in the right order.
2. What's the time to access the 6th node of a linked list? Of an array?
3. In a circular singly linked list, what does the last node's `next` hold?
4. Give one application each of a doubly and a circular linked list.
5. `START = 3`, `INFO[1..3] = P, Q, R`, `LINK[1..3] = 0, 1, 2`. What's the list?

## Answers

1. `newNode->next = head; head = newNode;` → `1 → 5 → 8 → 3`.
2. List: O(n) (walk 5 links). Array: O(1).
3. The address of the **first** node (head).
4. Doubly: browser/playlist next-previous. Circular: round-robin scheduling.
5. START = 3 → R, LINK[3] = 2 → Q, LINK[2] = 1 → P, LINK[1] = 0 → end. **R → Q → P.**
