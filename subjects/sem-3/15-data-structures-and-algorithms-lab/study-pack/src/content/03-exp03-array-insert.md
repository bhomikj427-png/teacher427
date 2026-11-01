# 3 · Exp 3 — Insert into an array (beginning, any position, end)

<div class="sub">The first "data structure" experiment. The skill here, shifting elements in a loop, comes back in Exp 4 and inside insertion sort (Exp 7).</div>

[[map:Array = fixed boxes > Make a gap by shifting right > Drop the value in > n = n + 1|here=2]]

## 3.1 The idea

An array's elements sit side by side and can't move by themselves. To put a value at index 2 you must first **make a gap** there by shifting everything from index 2 onward one place to the right.

:::guess Guess first
To shift `10 20 30 40 50` right from index 2, should the loop copy **30 first** or **50 first**? Try both on paper and see what goes wrong.
:::

[[fig:array_insert|Insert 25 at position 3. The arrows are numbered in the order the loop does them.]]

If you copy 30 first, `arr[3] = arr[2]` overwrites 40 before 40 has moved: you get `10 20 30 30 30 30`. So the loop must run **from the end down**: `for (i = n; i >= pos; i--) arr[i] = arr[i-1];`.

:::key Position vs index
The program asks for a **position** counted from 1 (what humans say), but C++ indexes from 0. Position 3 = `arr[2]`, hence `arr[pos - 1] = value;`. Valid positions for insertion are **1 to n+1** (n+1 = "after the last one").
:::

## 3.2 The program (corrected)

The manual's logic was right. This version adds the two checks it was missing: free space (`n < 100`) and a valid position.

[[code:e03_array_insert.cpp]]

The manual's three sample inputs, run for real:

[[run:e03_begin]]
[[run:e03_pos]]
[[run:e03_end]]

The added checks working (position 7 in a 3-element array):

[[run:e03_bad_pos]]

| Case | Loop | Why |
|---|---|---|
| Beginning | `for (i = n; i > 0; i--) arr[i] = arr[i-1];` then `arr[0] = value;` | every element moves |
| Position | `for (i = n; i >= pos; i--) arr[i] = arr[i-1];` then `arr[pos-1] = value;` | elements from index pos−1 onward move |
| End | `arr[n] = value;` | first free slot is index n; nothing moves |

All three end with **`n++`**: the array now holds one more element.

:::write Write in your record
**Aim:** To insert an element into an array at the beginning, at a given position, and at the end.
**Algorithm:** read n and the elements → read choice → *beginning:* shift all right (from the end), `arr[0] = value` → *position:* check 1 ≤ pos ≤ n+1, shift right from the end down to index pos−1, `arr[pos−1] = value` → *end:* `arr[n] = value` → `n++` → print.
**Complexity:** beginning O(n), position O(n) (worst case), end O(1). Space O(1) extra.
**Result:** 10 20 30 40 50 became 5 10 20 30 40 50 (beginning), 10 20 25 30 40 50 (25 at position 3), 10 20 30 40 50 60 (end).
:::

:::trap Mistakes that cost marks
- Forgetting `n++`: the new last element never prints.
- Shifting left-to-right: duplicates the value (see the guess above).
- `arr[pos] = value` instead of `arr[pos-1]`: everything lands one place too far right.
:::

## 3.3 Viva questions

| Question | Answer |
|---|---|
| Why is insertion at the beginning O(n)? | All n elements must shift one place right. |
| Why is insertion at the end O(1)? | No shifting: write at index n (if there is space). |
| What is the drawback of arrays for insertion? | Fixed size, and shifting costs O(n). A linked list inserts by changing pointers. |
| Why `int arr[100]` and not `int arr[n]`? | Array sizes must be constants in standard C++; 100 is the maximum capacity, n is how many are in use. |
| What if n is already 100? | Overflow: there's no room. The program must refuse (our first check). |

## 3.4 If the examiner changes the question

The manual's ASSIGNMENT list. Each function is tested (10 checks, all pass) and is written to drop into the program above. Each returns the new n.

**Insert at a position (reused by the next two):**
[[snip:t_03.cpp#insertAt]]

**Insert multiple elements:**
[[snip:t_03.cpp#insertMultiple]]

**Insert into a sorted array, keeping it sorted.** This is the core move of insertion sort (Exp 7):
[[snip:t_03.cpp#insertSorted]]

**Insert only if space is available:**
[[snip:t_03.cpp#insertIfSpace]]

**Insert before / after a given element:** search for the element, then reuse `insertAt`.
[[snip:t_03.cpp#insertBefore]]
[[snip:t_03.cpp#insertAfter]]

In `main` you call these like `n = insertSorted(arr, n, value);`.

:::check Check 3.1
`arr` = `4 8 15`, n = 3. Trace the "any position" branch for pos = 2, value = 6: which assignments run, in order, and what is the final array?
:::

:::check Check 3.2
Is `pos = 4` valid for this n = 3 array? Is `pos = 5`?
:::

<!--ANSWERS-->
## Answers

**Check 3.1:** i = 3: `arr[3] = arr[2]` (15); i = 2: `arr[2] = arr[1]` (8); the loop stops (i = 1 < pos). Then `arr[1] = 6`, n = 4 → **4 6 8 15**.

**Check 3.2:** pos = 4 = n+1 is valid (insert at the end). pos = 5 is invalid: it would leave a gap at index 3.
<!--/ANSWERS-->
