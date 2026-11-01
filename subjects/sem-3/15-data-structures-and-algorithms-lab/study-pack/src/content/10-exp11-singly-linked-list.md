# 10 · Exp 11 — Singly linked list (insert, delete, traverse)

<div class="sub">The pointers from Exp 1 finally pay off. New C++: struct, new / delete, and the arrow operator ->. Read 10.1 slowly; everything after builds on it.</div>

[[map:struct Node > new Node > head > insert at end > delete from beginning > traverse until NULL|here=1]]

## 10.1 New C++: struct, new, delete, ->

A **struct** bundles several variables into one new type:

```cpp
struct Node
{
    int data;      // the value
    Node *next;    // address of the next node (NULL if none)
};
```

- **`new Node`** asks for memory for one Node **while the program runs** and gives back its **address**: `Node *newNode = new Node;`
- **`p->data`** means "the `data` field of the node that `p` points to". It is shorthand for `(*p).data`.
- **`delete p;`** gives that node's memory back. Every `new` should have a matching `delete`.
- **`NULL`** is the "points nowhere" address: the end of the list, or an empty list (`head == NULL`).

:::guess Guess first
An array keeps its elements side by side. How does a linked list know where its second element is, if the nodes can be anywhere in memory?
:::

[[fig:sll_fig|The manual's list after inserting 10, 20, 30. Each node stores the address of the next.]]

The list is reached only through **`head`**, the address of the first node. Lose `head` and the whole list is lost.

## 10.2 The three operations

| Operation | Steps | Time |
|---|---|---|
| **insert at end** | make node (next = NULL) → if `head == NULL`, head = node → else walk `temp` until `temp->next == NULL`, then `temp->next = newNode` | O(n) (the walk) |
| **delete from beginning** | if empty → message → else `temp = head`, `head = head->next`, `delete temp` | O(1) |
| **traverse** | `temp = head`; while `temp != NULL`: print `temp->data`, `temp = temp->next` | O(n) |

:::trap The two classic linked-list bugs
1. **Forgetting `temp = temp->next;`** in traverse: `temp` never moves, so the loop never ends. The manual's IMPLEMENTATION screenshot (page 9) has exactly this bug, and its insert never links the new node in. Its **listing** (page 6) is correct; use that.
2. **`delete head;` before moving head**: the second node's address was inside the deleted node, so the rest of the list is lost. Always save the node in `temp`, move `head`, *then* `delete temp`.
:::

## 10.3 The program

The manual's listing was correct (one line was cut off at the page edge: `cout << temp->data << " deleted from list." << endl;`).

[[code:e11_singly_linked_list.cpp]]

The manual's Sample Inputs 1 and 2 in one run:

[[run:e11]]

Edge cases (delete and traverse on an empty list, delete the only node):

[[run:e11_empty]]

:::write Write in your record
**Aim:** To implement a singly linked list and perform insertion, deletion and traversal.
**Algorithm:** head = NULL. *Insert (end):* create node (data = value, next = NULL); if head == NULL, head = node; else move temp to the last node (temp->next == NULL) and set temp->next = node. *Delete (beginning):* if head == NULL → "empty"; else temp = head, head = head->next, delete temp. *Traverse:* temp = head; while temp ≠ NULL print temp->data, temp = temp->next.
**Complexity:** insert at end O(n), delete at beginning O(1), traverse O(n); space O(n) for n nodes.
**Result:** Inserted 10, 20, 30 (list: 10 20 30); deleting from the beginning removed 10 (list: 20 30).
:::

## 10.4 Viva questions

| Question | Answer |
|---|---|
| Linked list vs. array? | List: nodes anywhere in memory, size grows/shrinks, insert/delete by changing pointers, but no direct `a[i]` access (must walk) and an extra pointer per node. Array: contiguous, fixed size, O(1) indexing, O(n) insert/delete. |
| What does the last node's next hold? | NULL. |
| What is head? | A pointer to the first node; `head == NULL` means the list is empty. |
| Why is insert at end O(n)? | You must walk from head to the last node. (Keeping a `tail` pointer makes it O(1).) |
| Why is delete at beginning O(1)? | Only head changes; no walking. |
| What is `->`? | Access a field through a pointer: `p->data` = `(*p).data`. |
| Why `delete temp`? | Return the node's memory; otherwise it leaks. |
| Can you traverse backwards? | Not in a singly linked list (only next pointers). A doubly linked list adds `prev`. |

## 10.5 If the examiner changes the question

Insert at end and delete from beginning are the experiment. The rest (9 checks, all pass), each a function to add above `main()` and to the menu:

**Insert at the beginning** (O(1)):
[[snip:t_11.cpp#insertBegin]]

**Delete from the end.** Stop at the second-last node:
[[snip:t_11.cpp#deleteEnd]]

**Search** (returns the position) and **count nodes**:
[[snip:t_11.cpp#search]]
[[snip:t_11.cpp#countNodes]]

**Display in reverse** (recursion: the deepest call prints first):
[[snip:t_11.cpp#displayReverse]]

**Insert at a position:**
[[snip:t_11.cpp#insertAtPos]]

**Delete at a position:**
[[snip:t_11.cpp#deleteAtPos]]

:::check Check 10.1
For inserting a new node after node `temp`, these two lines come in some order: `temp->next = newNode;` and `newNode->next = temp->next;`. Which must come first, and what happens if you swap them?
:::

:::check Check 10.2
List: head → 4 → 8 → NULL. Trace `deleteNode()` then `insert(5)`. Draw the list after each.
:::

<!--ANSWERS-->
## Answers

**Check 10.1:** `newNode->next = temp->next;` **first**. If `temp->next = newNode;` runs first, the old `temp->next` address is overwritten, so `newNode->next` would point to newNode itself and the rest of the list is lost.

**Check 10.2:** delete: temp = (4), head = (8), delete temp → head → 8 → NULL. insert(5): walk to 8 (next is NULL), link → head → 8 → 5 → NULL.
<!--/ANSWERS-->
