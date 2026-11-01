# 1 · C++ from zero (just what the lab needs)

<div class="sub">No C assumed. Only the pieces the 12 experiments actually use. New pieces (pointers, 2-D arrays, struct, new/delete) are taught in the experiment that first needs them.</div>

[[map:Run a program > Program skeleton > Variables + cin/cout > if / else > Loops > Arrays > Functions > Reading errors|here=1]]

## 1.1 Running a program

A C++ program is a text file ending in **.cpp**. A **compiler** (g++) turns it into an **.exe** you can run. If the text breaks the language rules, the compiler refuses and prints **errors** with line numbers. Nothing runs until every error is fixed.

| Where | How to compile + run |
|---|---|
| **Code::Blocks** | File → New → Empty file → save as `exp1.cpp` → **F9** (Build and run) |
| **Dev-C++** | File → New → Source File → save as `.cpp` → **F11** (Compile & Run) |
| **VS Code** | Open the folder, then in the terminal (Ctrl+\`): `g++ exp1.cpp -o exp1` then `.\exp1` |
| **This laptop** | Any new terminal: `g++ -static exp1.cpp -o exp1` then `.\exp1` |

:::trap Save as .cpp, not .c
A `.c` file is compiled as C, and `cout`, `cin`, `new` and `bool &` all fail. On this laptop, always add `-static`: another program on the PATH carries an older C++ library, and without `-static` your `.exe` may exit silently.
:::

## 1.2 The skeleton every experiment starts with

:::guess Guess first
Which line would you guess makes the program *start*, and what do you think `return 0;` reports, and to whom?
:::

[[code:p01_hello.cpp]]
[[run:p01]]

- `#include <iostream>` brings in **cout** (print) and **cin** (read). Every experiment has it.
- `using namespace std;` lets you write `cout` instead of `std::cout`. Every experiment has it.
- `int main() { ... }` is where running starts. Statements run **top to bottom**.
- Every statement ends with **`;`**. Blocks of statements live inside **`{ }`**.
- `endl` (or `"\n"` inside a string) moves to a new line.
- `return 0;` tells the operating system "finished normally".
- `//` starts a comment. The compiler ignores the rest of the line.

## 1.3 Variables, input, arithmetic, decisions

A **variable** is a named box that holds one value of a fixed **type**:

| Type | Holds | Example |
|---|---|---|
| `int` | whole numbers | `int n = 5;` |
| `float` | numbers with decimals | `float x = 2.5;` |
| `char` | one character | `char c = 'A';` |
| `bool` | `true` / `false` | `bool done = false;` |

[[code:p02_input.cpp]]
[[run:p02]]

:::trap The three classic beginner slips
1. `=` **stores**, `==` **compares**. `if (a = b)` compiles but is wrong.
2. `int / int` **throws away** the fraction: 17 / 5 = 3. `%` gives the remainder: 17 % 5 = 2.
3. `cin >> a >> b;` uses **`>>`** (data flows *into* a). `cout << x;` uses **`<<`** (data flows *out to* the screen).
:::

`if (…) {…} else if (…) {…} else {…}`: only the first true branch runs. With a single statement the `{ }` are optional; with more than one they are **required**. Exp 10's manual screenshot breaks exactly this rule.

## 1.4 Loops and arrays

An **array** is a row of boxes of the same type, numbered from **0**. `int arr[5]` has `arr[0]` … `arr[4]`. There is **no** `arr[5]`; using it reads or writes someone else's memory, and C++ won't stop you.

[[code:p03_loops_arrays.cpp]]
[[run:p03]]

| Loop | Use it when | In the lab |
|---|---|---|
| `for (int i = 0; i < n; i++)` | you know how many times | walking an array (every experiment) |
| `while (condition)` | you stop on a condition | insertion sort's shifting, linked-list walking |
| `do { } while (condition);` | body must run **at least once** | menus (Exp 10–12), circular list traversal |

`i++` means "add 1 to i"; `i--` means "subtract 1".

:::check Check 1.1
What does this print?  `for (int i = 4; i > 0; i--) cout << i;`
:::

## 1.5 Functions

A **function** is a named piece of code you can call. From Exp 5 on, every experiment splits its work into functions (`inputMatrix`, `insertionSort`, `enqueue`, …).

[[code:p04_functions.cpp]]
[[run:p04]]

Read the result carefully. It explains three things you'll meet again:

- **`int square(int x)`**: the first `int` is what the function *gives back* via `return`; `void` means it gives nothing back.
- **An array parameter is not copied.** The function works on the caller's array, so `doubleAll` changed `a`. That's why `insertionSort(arr, n)` sorts `main`'s array.
- **A plain `int` parameter is a copy**, so `tryToChange` changed only its own copy. Add **`&`** (`int &x`) and the parameter *is* the caller's variable. Exp 8's `swapElements(int &a, int &b)` needs this.

:::key Order rule
A function must appear **above** the place that calls it. Write helper functions first and `main()` last, as every experiment in the manual does.
:::

## 1.6 Reading compiler errors (exam-day survival)

The compiler reports `file:LINE:COLUMN: error: message`. **Fix the first error first**: one missing `;` can produce ten errors below it. Here is the manual's own Exp 12 listing, compiled:

[[err:m12_listing]]

| Message | Usual cause |
|---|---|
| `expected ';' before …` | missing `;` on the line **above** |
| `'x' was not declared in this scope` | typo in a name, or a variable used outside the `{ }` it was made in |
| `missing terminating " character` | a string without its closing `"` |
| `expected '}' at end of input` | a `{` was never closed |
| `'else' without a previous 'if'` | a statement squeezed between `}` and `else` |
| `ISO C++ forbids variable length array` | `int arr[n]` with `n` read at run time; use `int arr[100]` |

<!--ANSWERS-->
## Answers

**Check 1.1:** `4321`. It starts at 4, prints while i > 0, and stops once i becomes 0.
<!--/ANSWERS-->
