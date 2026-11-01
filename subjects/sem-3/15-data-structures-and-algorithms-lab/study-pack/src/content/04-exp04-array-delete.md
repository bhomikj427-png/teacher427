# 4 · Exp 4 — Delete from an array (beginning, any position, end)

<div class="sub">The mirror image of Exp 3: close the gap by shifting <b>left</b>, then n = n − 1.</div>

[[map:Pick the element > Shift the rest left > n = n − 1 > print 0..n−1|here=2]]

## 4.1 The idea

:::guess Guess first
In Exp 3 the shift loop had to run from the **end** backwards. For deletion (shift left), which end must the loop start from, and why?
:::

[[fig:array_delete|Delete position 3: shift from just after the gap, moving forwards.]]

When shifting **left**, start right after the deleted element and move **forward**: `arr[i] = arr[i+1]` for i = pos−1 … n−2. Going the other way would copy 50 over 40 before 40 has moved. **Rule of thumb: always copy the element that is about to be overwritten first.**

The last element is never erased; after `n--` the program simply never prints index n. That's why delete-at-end is just `n--`: O(1), no shifting.

## 4.2 The manual's bug

The PROGRAM listing (manual page 9) asks **"Enter value:"** in all three branches and reads a number it never uses. Deleting needs only a *position*. With the manual's own Sample Input 1 (`5`, `10 20 30 40 50`, `1`) that listing stops at "Enter value:" and waits for input the sample never gives. The IMPLEMENTATION screenshot (page 11) has no such line. This pack uses the screenshot's logic, plus a position check, and prints which element was deleted.

## 4.3 The program (corrected)

[[code:e04_array_delete.cpp]]

The manual's three sample inputs:

[[run:e04_begin]]
[[run:e04_pos]]
[[run:e04_end]]

A bad position is refused:

[[run:e04_bad_pos]]

| Case | Loop | Then |
|---|---|---|
| Beginning | `for (i = 0; i < n-1; i++) arr[i] = arr[i+1];` | `n--` |
| Position | `for (i = pos-1; i < n-1; i++) arr[i] = arr[i+1];` | `n--` |
| End | (none) | `n--` |

Valid deletion positions are **1 to n** (not n+1: there's nothing there to delete). With n = 0 there's nothing to delete at all: **underflow**.

:::write Write in your record
**Aim:** To delete an element from an array at the beginning, at a given position, and at the end.
**Algorithm:** read n and the elements → read choice → *beginning:* shift elements 1…n−1 one place left → *position:* check 1 ≤ pos ≤ n, shift elements after pos−1 one place left → *end:* nothing to shift → `n--` → print.
**Complexity:** beginning O(n), position O(n) (worst case), end O(1). Space O(1).
**Result:** 10 20 30 40 50 became 20 30 40 50 (beginning), 10 20 40 50 (position 3, deleted 30), 10 20 30 40 (end).
:::

## 4.4 Viva questions

| Question | Answer |
|---|---|
| Why does deletion at the end need no shifting? | Reducing n hides the last element; no gap is created. |
| Is the deleted value really erased from memory? | No. It stays in the slot until overwritten; the program just stops counting it. |
| What is underflow here? | Trying to delete from an empty array (n = 0). |
| Insertion shifts from the end, deletion from the front. Why? | So no element is overwritten before it has been copied. |
| Time complexity of deleting a value you first have to search for? | O(n): the search is O(n) and the shift is O(n), so O(n) overall. |

## 4.5 If the examiner changes the question

Beginning, position and end are the experiment itself. The other two items:

**Delete a given value** (search, then shift):
[[snip:t_04.cpp#deleteByValue]]

**Menu-driven insertion and deletion on one array.** A full program combining Exp 3 and Exp 4, with a repeating menu (the `do … while` pattern from Exp 10):

[[code:e04b_array_menu.cpp]]
[[run:e04b]]

:::check Check 4.1
`arr` = `7 3 9 1`, n = 4. Delete position 2. Write the assignments the loop performs, the final n, and the printed array.
:::

:::check Check 4.2
Someone writes the position loop as `for (i = pos-1; i < n; i++) arr[i] = arr[i+1];`. What goes wrong?
:::

<!--ANSWERS-->
## Answers

**Check 4.1:** i = 1: `arr[1] = arr[2]` (9); i = 2: `arr[2] = arr[3]` (1); stop at i = 3. n = 3 → **7 9 1**.

**Check 4.2:** On the last pass (i = n−1) it reads `arr[n]`, one past the data: junk (or past the end of the array if n = 100). The result still prints correctly, because n−1 elements are printed, but it reads memory it shouldn't. The correct bound is `i < n-1`.
<!--/ANSWERS-->
