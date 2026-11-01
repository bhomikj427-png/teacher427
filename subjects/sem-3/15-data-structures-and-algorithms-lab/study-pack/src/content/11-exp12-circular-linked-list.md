# 11 · Exp 12 — Circular linked list (insert, delete, traverse)

<div class="sub">Exp 11 with one change: the last node points back to head instead of NULL. Every "== NULL" test becomes "== head".</div>

[[map:Exp 11 list > last node points to head > find last: next == head > traverse: do-while > delete first: fix the last node|here=2]]

## 11.1 The idea

:::guess Guess first
In a circular list there is no NULL to stop at. If traverse used `while (temp != head)` with `temp = head` at the start, what would it print?
:::

[[fig:cll_fig|The manual's list after inserting 10, 20, 30.]]

[[fig:one_node_circle|A single node points to itself. The program must treat this case separately.]]

| | Singly (Exp 11) | Circular (Exp 12) |
|---|---|---|
| last node's next | NULL | head |
| "is this the last node?" | `temp->next == NULL` | `temp->next == head` |
| traverse loop | `while (temp != NULL)` | `do { … } while (temp != head);` |
| delete from beginning | O(1) | **O(n)**: the last node must be found and re-pointed to the new head |

The answer to the guess: **nothing**. temp starts *equal* to head, so a `while` loop exits before its first pass. A `do … while` prints first and tests afterwards.

## 11.2 The program (corrected)

The manual's PROGRAM listing doesn't compile:

[[err:m12_listing]]

The four problems: `insert(intvalue)` (missing space); the menu `cout` lines are missing their closing `" << endl;`; `delete temp;` sits after the closing `}` of the block where `temp` was declared; and `main()` is cut off at the page end. The IMPLEMENTATION screenshot (page 7) is correct and complete; this pack follows it.

[[code:e12_circular_linked_list.cpp]]

The manual's sample run, reproduced exactly:

[[run:e12]]

Deleting the only node (the `head->next == head` branch), then deleting from an empty list:

[[run:e12_one]]

:::trap Delete-from-beginning, three cases
1. **Empty** (`head == NULL`): print a message.
2. **One node** (`head->next == head`): delete it, set `head = NULL`. Without this case, the general code would set head to the deleted node itself.
3. **General:** find `last` (its next is head), move `head = head->next`, set `last->next = head`, then `delete temp`.
:::

:::write Write in your record
**Aim:** To implement a circular linked list and perform insertion, deletion and traversal.
**Algorithm:** *Insert (end):* create node; if head == NULL: head = node, node->next = head; else move temp until temp->next == head, temp->next = node, node->next = head. *Delete (beginning):* if empty → message; if one node → delete it, head = NULL; else find last, temp = head, head = head->next, last->next = head, delete temp. *Traverse:* temp = head; do { print temp->data; temp = temp->next } while (temp ≠ head).
**Complexity:** insert at end O(n), delete at beginning O(n) (finding the last node), traverse O(n); space O(n), auxiliary O(1).
**Result:** Inserted 10, 20, 30 (list: 10 20 30); deleted 10 (list: 20 30). The last node always pointed back to head.
:::

## 11.3 Viva questions

| Question | Answer |
|---|---|
| What is a circular linked list? | A linked list whose last node points to the first node instead of NULL. |
| How do you detect the last node? | `temp->next == head`. |
| Why `do-while` for traversal? | The stop condition (`temp == head`) is already true at the start; do-while prints head first. |
| Why is delete-from-beginning O(n) here but O(1) in Exp 11? | The last node's next must be updated to the new head, and finding it takes a walk. (A `tail` pointer would make it O(1).) |
| One-node list: what is head->next? | head itself. |
| Advantages? | Any node can reach every other node; natural for round-robin scheduling, multiplayer turns, repeating playlists. |
| Risk? | Infinite loops, if a traversal's stop condition is wrong. |
| Types? | Circular singly linked (next only) and circular doubly linked (next and prev). |

## 11.4 If the examiner changes the question

The same assignment list as Exp 11, adapted so the circle stays closed (10 checks, all pass, each including "is it still circular?").

**Insert at the beginning.** The last node must point to the new head:
[[snip:t_12.cpp#insertBegin]]

**Delete from the end:**
[[snip:t_12.cpp#deleteEnd]]

**Search and count** (do-while again):
[[snip:t_12.cpp#search]]
[[snip:t_12.cpp#countNodes]]

**Display in reverse** (recursion that stops when the next node is head):
[[snip:t_12.cpp#displayReverse]]

**Insert / delete at a position:**
[[snip:t_12.cpp#insertAtPos]]
[[snip:t_12.cpp#deleteAtPos]]

:::check Check 11.1
Circular list head → 3 → 6 → 9 → (back to 3). Run delete-from-beginning by hand: what are `last`, the new head, and `last->next` afterwards?
:::

:::check Check 11.2
Why does `insert` in Exp 12 need `newNode->next = head;` even in the `head == NULL` branch?
:::

<!--ANSWERS-->
## Answers

**Check 11.1:** last = node 9; head moves to node 6; `last->next = head` → 9 now points to 6; node 3 is deleted. List: 6 → 9 → (back to 6).

**Check 11.2:** A lone node is both first and last, so its next must point to head (itself) to keep the list circular. If it were left unset, the next traversal or insert would follow a garbage address.
<!--/ANSWERS-->
