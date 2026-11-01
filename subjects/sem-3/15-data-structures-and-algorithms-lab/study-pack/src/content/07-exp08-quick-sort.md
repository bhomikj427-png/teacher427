# 7 · Exp 8 — Quick sort, and comparison with other sorts

<div class="sub">The hardest program in the lab: recursion + partition. Learn partition first; once that's solid, quickSort itself is 6 lines.</div>

[[map:Pick pivot (last) > Partition: small left, big right > Pivot is now final > Recurse on left part > Recurse on right part|here=2]]

## 7.1 The idea: divide and conquer

1. **Pick a pivot.** This program uses the **last** element.
2. **Partition:** rearrange so everything smaller than the pivot is on its left and everything else on its right. The pivot is then in its **final sorted position**.
3. **Recurse:** quick-sort the left part and the right part the same way. A part of 0 or 1 element is already sorted, and the recursion stops there.

## 7.2 Partition, step by step (learn this cold)

:::guess Guess first
In `partitionArray`, the variable `i` starts at `low − 1`. What does `i` keep track of? (Hint: watch where small elements get swapped to.)
:::

```cpp
int pivot = arr[high];
int i = low - 1;                 // last index of the "smaller than pivot" zone
for (int j = low; j < high; j++)
    if (arr[j] < pivot)          // small one found: grow the zone, swap it in
    {
        i++;
        swapElements(arr[i], arr[j]);
    }
swapElements(arr[i + 1], arr[high]);   // pivot goes right after the zone
return i + 1;                          // pivot's final index
```

[[fig:partition_trace|First partition of the manual's example 10 7 8 9 1 5. Same result as the manual's "Pass 1".]]

[[fig:quick_tree|The whole recursion. Each box is one call to partition; the manual's Passes 1–4 are these four pivots.]]

:::key What `int &a` does in swapElements
`swapElements(arr[i], arr[j])` must change the array itself. `int &a` makes `a` **another name** for `arr[i]` (a reference, chapter 1.5). With plain `int a`, the function would swap two copies and the array would not change.
:::

## 7.3 The program (corrected)

Same VLA fix as Exp 7 (`int arr[100]`). Partition and recursion are exactly the manual's.

[[code:e08_quick_sort.cpp]]
[[run:e08]]

With duplicates and negatives:

[[run:e08_dup]]

## 7.4 The missing half: comparing with other sorts

The aim says "compare its performance with other sorting techniques". The manual's algorithm (steps 11–12) and explanation table list `bubbleSort()`, `selectionSort()`, `insertionSort()`, `copyArray()` and `clock()`, but **none of them are in the printed code**. Here is the full program:

- Every sort gets its **own copy** of the same input (`copyArray`). Sorting the already-sorted output again wouldn't be a fair test.
- Timing **6 numbers** gives 0 ms for everything, so part 2 times 10 000 random numbers. `srand(1)` makes the "random" data the same on every run.
- `clock()` counts processor ticks; `(end − start) / CLOCKS_PER_SEC` converts to seconds, and × 1000 to milliseconds.

[[code:e08_sort_compare.cpp]]
[[run:e08_compare]]

The times vary from PC to PC, but the **ranking** is what the experiment shows: quick sort is far faster than the three O(n²) sorts on large random input.

| Algorithm | Best | Average | Worst | Extra space | Stable? |
|---|---|---|---|---|---|
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) avg (recursion) | No |
| Bubble sort (with early exit) | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge sort (assignment) | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |

:::trap Quick sort's worst case, in this program
With the **last element as pivot**, an **already sorted** array is the worst case: every pivot is the largest, so each partition peels off just one element. That gives n(n−1)/2 comparisons (15 for n = 6; tested in 7.6). Fix: pick the middle (or a random) element as pivot.
:::

:::write Write in your record
**Aim:** To sort an integer array using quick sort and compare its performance with bubble, selection and insertion sort.
**Algorithm:** quickSort(low, high): if low < high → pi = partition(low, high) → quickSort(low, pi−1) → quickSort(pi+1, high). partition: pivot = arr[high], i = low−1; for j = low…high−1: if arr[j] < pivot, i++ and swap arr[i], arr[j]; finally swap arr[i+1], arr[high]; return i+1. Comparison: copy the same input for each sort, time each with clock().
**Complexity:** best/average O(n log n), worst O(n²) (sorted input with last-element pivot); space O(log n) average for the recursion, O(n) worst.
**Result:** 10 7 8 9 1 5 → 1 5 7 8 9 10. All four sorts gave the same output. On 10 000 random numbers quick sort took about 1 ms; bubble, selection and insertion took tens to over a hundred ms (bubble slowest).
:::

## 7.5 Viva questions

| Question | Answer |
|---|---|
| What is divide and conquer? | Split into smaller subproblems, solve each (recursively), combine. Quick sort splits by a pivot. |
| What is a pivot? | The element used to split; after partition it sits at its final sorted index. |
| Why `low < high` in quickSort? | A part with 0 or 1 element is sorted. This is the recursion's stopping condition (base case). |
| Why O(n log n) on average? | Each level of recursion does O(n) partition work, and balanced splits give about log₂ n levels. |
| Worst case and when? | O(n²), when the pivot is always the smallest or largest (sorted / reverse-sorted input with last-element pivot). |
| Space complexity? | In-place, but the recursion stack uses O(log n) on average and O(n) in the worst case. |
| Is quick sort stable? | No. Long-distance swaps can reorder equal elements. |
| Why copy the array before each sort in the comparison? | So every algorithm sorts the same unsorted input; a fair test. |
| Why does `swapElements` use `&`? | To swap the actual array elements, not copies. |

## 7.6 If the examiner changes the question

"Separate functions for input, partitioning, sorting and display" is the program above. The rest (7 checks, all pass):

**Descending order** (one character in partition):
[[snip:t_08.cpp#quickSortDesc]]

**First element as pivot:** swap it to the end, then partition exactly as before (`quickSort` stays the same, just calling `partitionFirst`):
[[snip:t_08.cpp#pivotFirst]]

**Middle element as pivot** (the worst-case fix):
[[snip:t_08.cpp#pivotMiddle]]

**Count comparisons and swaps.** On the manual's example this gives 11 comparisons and 5 swaps; on a sorted array of 6, 15 comparisons (the worst case). Run it on sorted, reverse-sorted and random input for the "compare performance" item.
[[snip:t_08.cpp#quickSortCount]]

**Merge sort** (for "compare quick sort with merge sort"; time it with `clock()` as in 7.4):
[[snip:t_08.cpp#mergeSort]]

:::check Check 7.1
Partition `4 9 2 7 5` (pivot 5). Track i and the array after each swap. What index does partition return?
:::

:::check Check 7.2
Without looking, write `quickSort(int arr[], int low, int high)`. Six lines.
:::

<!--ANSWERS-->
## Answers

**Check 7.1:** pivot 5, i = −1. j = 0: 4 < 5 → i = 0, swap(arr[0], arr[0]) → `4 9 2 7 5`. j = 1: 9 no. j = 2: 2 < 5 → i = 1, swap(arr[1], arr[2]) → `4 2 9 7 5`. j = 3: 7 no. End: swap(arr[2], arr[4]) → `4 2 5 7 9`. Returns **2**.

**Check 7.2:** `void quickSort(int arr[], int low, int high) { if (low < high) { int pi = partitionArray(arr, low, high); quickSort(arr, low, pi - 1); quickSort(arr, pi + 1, high); } }`
<!--/ANSWERS-->
