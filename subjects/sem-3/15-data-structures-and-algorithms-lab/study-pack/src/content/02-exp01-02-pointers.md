# 2 · Exp 1 + 2 — Pointers and pointer arithmetic

<div class="sub">Manual Exp 1: "implement Pointers". Exp 2: "implement Pointer Arithmetic". Both have no user input, so they are the shortest programs in the lab.</div>

[[map:Address > Pointer variable > & and * > Pointer + 1 > Arrays are pointers > (later) linked lists|here=1]]

## 2.1 The idea

Every variable lives in memory at a numbered location: its **address**. A **pointer** is a variable whose value *is* an address.

:::guess Guess first
`int number = 25;` and `int *ptr = &number;`. If you print `ptr`, do you see 25? If you print `*ptr`?
:::

[[fig:pointer_basic|Exp 1's variables. The address 0x61FF08 is the manual's example; yours will differ on every run.]]

| Symbol | Read it as | In Exp 1 |
|---|---|---|
| `int *ptr;` | "ptr is a pointer to an int" | declares the pointer |
| `&number` | "address of number" | `ptr = &number;` |
| `*ptr` | "value at the address in ptr" | prints 25 |

:::trap `*` means two different things
In a **declaration** (`int *ptr;`), `*` means "this is a pointer". In an **expression** (`cout << *ptr;`), `*` means "go to that address" (dereference).
:::

## 2.2 Exp 1 program (manual's code was correct)

[[code:e01_pointers.cpp]]
[[run:e01]]

Lines 2 and 3 of the output always match each other; the actual number changes on every run and every PC. The manual says so too ("memory address varies").

## 2.3 Exp 2: pointer arithmetic

:::guess Guess first
`ptr` points at `arr[0]`, which is at address …00. After `ptr++`, is the address …01 or …04? Why?
:::

`ptr + 1` doesn't add 1 byte. It moves to the **next int**, which is `sizeof(int)` = 4 bytes further. That only works because an array's elements sit **side by side** in memory.

[[fig:pointer_arith|The manual's Figure 1, redrawn: each move is one whole element.]]

[[code:e02_pointer_arithmetic.cpp]]
[[run:e02]]

The real run shows exactly the pattern the manual predicts: …700 → …704 → …700 → …708, values 10 → 20 → 10 → 30.

:::key Two facts the viva loves
- `int *ptr = arr;` works because **an array's name is the address of its first element**: `arr` == `&arr[0]`.
- `*(ptr + i)` is the same as `arr[i]`. Square brackets are pointer arithmetic in disguise.
:::

:::write Write in your record
**Aim (Exp 1):** To store the address of a variable in a pointer and access the variable through the pointer.
**Algorithm:** declare `int number = 25` → declare `int *ptr` → `ptr = &number` → print number, `&number`, `ptr`, `*ptr`.
**Aim (Exp 2):** To perform increment, decrement and addition on a pointer to an integer array.
**Algorithm:** `ptr = arr` → print → `ptr++` → print → `ptr--` → print → `ptr = ptr + 2` → print.
**Complexity:** time O(1), space O(1) for both.
**Result (Exp 1):** The pointer stored the address of `number` (same value as `&number`), and `*ptr` gave 25.
**Result (Exp 2):** Each increment moved the pointer by 4 bytes (one int): values 10, 20, 10, 30 at addresses base, +4, base, +8.
:::

## 2.4 Viva questions

| Question | Answer |
|---|---|
| What is a pointer? | A variable that stores the memory address of another variable. |
| What does `&` do? `*`? | `&x` gives x's address; `*p` gives the value stored at the address in p. |
| Why does `ptr++` add 4, not 1? | Pointer arithmetic moves in units of the pointed-to type; an int is 4 bytes here. |
| What would `ptr++` add for a `char *`? A `double *`? | 1 byte; 8 bytes. |
| What is a NULL pointer? | A pointer that points nowhere (`ptr = NULL;`). Linked lists use it to mark the end. |
| What happens if you dereference an uninitialised pointer? | Undefined behaviour: it points to a random address, and the program may crash. |
| Where are pointers used? | Dynamic memory (`new`), linked lists, trees, graphs, passing by reference, arrays. |

:::check Check 2.1
`int a[4] = {5, 6, 7, 8}; int *p = a + 3;`. What is `*p`? What is `*(p - 2)`?
:::

:::check Check 2.2
Without looking, write the four lines of Exp 1 that declare `number`, declare `ptr`, assign it, and print the value through the pointer.
:::

<!--ANSWERS-->
## Answers

**Check 2.1:** `*p` = a[3] = **8**; `*(p − 2)` = a[1] = **6**.

**Check 2.2:** `int number = 25;` · `int *ptr;` · `ptr = &number;` · `cout << *ptr;`. If you wrote `ptr = number` (no `&`), the compiler rejects it: you can't store an int in a pointer.
<!--/ANSWERS-->
