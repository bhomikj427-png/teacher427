# 01 — C++ and OOP

> **MTE blueprint: CO1 = 11 marks, the biggest block.** Section A Q1 + Q2 (2 + 2, theory: §3 OOP features,
> §4 class/object, §5 access specifiers, §6 constructor vs destructor, §7 call by value/reference) and
> **all of Section C** (2 theory + **5 coding**: a class with constructors and a destructor. Drill §8–§9, and
> the BankAccount program in `07` C2).

**A1: A2, A3, A4, A5, A7, A9, B2, C3, D1 · 15 of 50 marks · decks 1–5 · CO1 (target 85%, the highest)**

CO1 has the highest target in the hand-out (85%). Expect at least one definition question and one
class program from this file.

## Map

```
 program structure ──► loops (A2) ──► functions ──► call by value vs reference (B2)
                                                      └─► pointers: & and *
 OOP idea (A9) ──► class & object (A3) ──► access specifiers (A5)
                        │
                        └─► constructor / destructor (A4) ──► Student (C3) ──► Triangle (D1)
                                                                  overloading ─┘
 the octal trap (A7)
```

---

## 1. Program structure and the A7 trap

**Q ▸ `[A1 A7]`** What does this print, and why?

```text
#include <iostream.h>
using namespace std;
long int zip;          // Zip code
main( )
{
    zip = 021377;      // Use the zip code for Cambridge MA
    cout << "New York's zip code is: " << zip << '\n';
    return (0);
}
```

Guess first. Then read on.

**The rule:** in C++ an integer literal that **starts with 0** is **octal** (base 8). `0x…` is hex,
`0b…` is binary, and anything else is decimal.

So `021377` is octal, and `cout` prints it in decimal:

```text
021377 (octal) = 2·8⁴ + 1·8³ + 3·8² + 7·8 + 7
               = 8192 + 512 + 192 + 56 + 7
               = 8959
```

**Exam answer:** Output: `New York's zip code is: 8959`. The leading 0 makes `021377` an **octal**
literal, not decimal 21377, so its value is 8959. (The comment is a joke. The programmer wanted the
Cambridge zip code and got a different number.)

**Also worth one line in your answer:** on a modern compiler this code does **not compile**: the header
is `<iostream>`, not `<iostream.h>` (that's old Turbo C++), and `main()` must be declared `int main()`.
With those fixed, it prints 8959.

**The structure of every program you write in the exam:**

```text
#include <iostream>        // header: cin, cout
using namespace std;       // so you can write cout instead of std::cout

int main() {               // execution starts here
    // declarations, statements
    return 0;              // 0 = success
}
```

---

## 2. Loops `[A1 A2]`

**Q ▸** A `while` loop and a `do-while` loop both have the condition `i < 0` with `i = 5`. How many
times does each body run?

`while`: **0 times**. `do-while`: **1 time**. That one difference is what A2 is asking about.

| | `for` | `while` | `do-while` |
|---|---|---|---|
| Condition checked | before each iteration | before each iteration | **after** each iteration |
| Minimum runs | 0 | 0 | **1** |
| Type | entry-controlled | entry-controlled | **exit-controlled** |
| Use when | the number of iterations is **known** | repeat **until a condition** changes; count unknown | body must run **at least once** (menus, input validation) |
| Syntax | `for (init; cond; update) {…}` | `while (cond) {…}` | `do {…} while (cond);` ← **semicolon** |

---

## 3. Why OOP `[A1 A9]`

**Q ▸** In C (structured programming), a `balance` variable and the `withdraw()` function that
changes it are separate. What stops any other function setting `balance = -1000000`?

Nothing. That's the problem OOP solves: it **bundles data with the functions allowed to touch it**, and
hides the data from everything else.

| Structured (procedural), e.g. C | Object-oriented, e.g. C++ |
|---|---|
| Program = a set of **functions** | Program = a set of **objects** |
| **Top-down** design | **Bottom-up** design |
| Data is separate from functions, often global | Data and functions are **bundled** in a class |
| No data hiding | **Data hiding** via `private` |
| Reuse by copying functions | Reuse by **inheritance** |
| Hard to scale to large programs | Scales better, models real-world entities |

**Features of OOP** (write these with one line each):

1. **Class & object**: a class is a blueprint, an object is an instance of it.
2. **Encapsulation**: wrapping data and the functions that work on it into one unit (the class).
3. **Data hiding / abstraction**: show only the essentials. Keep the details `private` and expose
   a public interface.
4. **Inheritance**: a new class (derived) acquires the members of an existing class (base), giving
   code reuse.
5. **Polymorphism**: one name, many forms. **Compile-time** means function or operator overloading.
   **Run-time** means virtual functions.
6. **Message passing / dynamic binding**: objects communicate by calling each other's functions.
   Which function runs can be decided at run time.

---

## 4. Class and object `[A1 A3]`

**Q ▸** `class Car { … };` — how much memory does this line allocate?

**None.** A class is a **type**, a blueprint. Memory is allocated only when you create an **object**:
`Car c1;`.

**Exam answer (A3):** A **class** is a user-defined data type that groups **data members**
(variables) and **member functions** into one unit. An **object** is an **instance** of a class, a
real variable of that type that occupies memory. **Relation:** a class is the blueprint and objects are
built from it. One class can have many objects, each with its own copy of the data members but sharing
the same member functions. For example: class `Car` is the design, and `c1` and `c2` are two actual cars.

---

## 5. Access specifiers `[A1 A5]`

**Q ▸** If you write a class and put no access specifier at all, can `main()` read its members?

**No.** The default in a `class` is **`private`**. (In a `struct` the default is `public`, which is
the only difference between them in C++.)

| Specifier | Same class | Derived class | Outside (e.g. `main`) |
|---|---|---|---|
| `public` | ✔ | ✔ | ✔ |
| `protected` | ✔ | ✔ | ✘ |
| `private` | ✔ | ✘ | ✘ |

**Why data is private and functions public:** the data can then be changed **only** through
functions that can check it (e.g. reject negative marks). That is data hiding.

The deck-4 activity (protected + single inheritance) in one program:

```cpp
#include <iostream>
using namespace std;

class Person {
protected:
    int age;                     // visible to Student, NOT to main
public:
    Person(int a) { age = a; }
};

class Student : public Person {  // single inheritance
private:
    int marks;                   // visible only inside Student
public:
    Student(int a, int m) : Person(a) { marks = m; }
    void display() {
        cout << "Age: " << age << ", Marks: " << marks << endl;  // age OK: protected
    }
};

int main() {
    Student s(19, 88);
    s.display();
    // s.age = 20;    // ERROR: age is protected
    // s.marks = 90;  // ERROR: marks is private
    return 0;
}
```

Output:

```text
Age: 19, Marks: 88
```

---

## 6. Constructor and destructor `[A1 A4]`

**Q ▸** You create an object and never call any function on it. Is any code of the class run?

**Yes, twice:** the **constructor** when it's created, and the **destructor** when it goes out of scope.

| | Constructor | Destructor |
|---|---|---|
| Purpose | **initialise** the object | **clean up** (release memory/resources) |
| Name | same as class: `Student()` | class name with tilde: `~Student()` |
| When it runs | automatically when the object is **created** | automatically when the object is **destroyed** (goes out of scope / `delete`) |
| Arguments | can take arguments | **never** takes arguments |
| Overloading | **can be overloaded** (default, parameterized, copy) | **cannot** be overloaded, only one per class |
| Return type | none, not even `void` | none |
| Order | objects constructed in order of creation | destroyed in **reverse** order |

**Types of constructor:** **default** (no arguments), **parameterized** (takes arguments), **copy**
(`Student(const Student &s)`, builds a new object from an existing one).

This program shows the order. Know it, because it is a classic output question:

```cpp
#include <iostream>
using namespace std;

class Demo {
    int id;
public:
    Demo(int i) { id = i; cout << "Constructor " << id << endl; }
    ~Demo()     { cout << "Destructor " << id << endl; }
};

int main() {
    Demo a(1);
    Demo b(2);
    cout << "End of main" << endl;
    return 0;
}
```

Output (**destructors run in reverse order**):

```text
Constructor 1
Constructor 2
End of main
Destructor 2
Destructor 1
```

---

## 7. Call by value vs call by reference `[A1 B2 · 2 marks]`

**Q ▸** `void swap(int a, int b) { int t = a; a = b; b = t; }` — you call `swap(x, y)` with
x = 10, y = 20. What are x and y afterwards?

**Still 10 and 20.** The function swapped its **copies**.

- **Call by value**: the function gets a **copy**. Changes don't reach the caller.
- **Call by reference** (`int &a`): the parameter is an **alias** for the caller's variable. Changes
  reach the caller.
- **Call by address / pointer** (`int *a`): the function gets the **address** and changes the
  original through `*a`. Same effect as by reference, different syntax.

**Pointers in one breath (deck 8):** `&x` = "address of x". `int *p = &x;` makes p hold that address.
`*p` = "the value at the address in p" (dereference). So `*p = 5;` changes x.

```cpp
#include <iostream>
using namespace std;

void swapByValue(int a, int b) {       // gets copies
    int t = a; a = b; b = t;
    cout << "Inside swapByValue:     a = " << a << ", b = " << b << endl;
}

void swapByReference(int &a, int &b) { // a, b are aliases of the originals
    int t = a; a = b; b = t;
}

void swapByPointer(int *a, int *b) {   // gets addresses
    int t = *a; *a = *b; *b = t;
}

int main() {
    int x = 10, y = 20;

    swapByValue(x, y);
    cout << "After call by value:     x = " << x << ", y = " << y << endl;

    swapByReference(x, y);
    cout << "After call by reference: x = " << x << ", y = " << y << endl;

    swapByPointer(&x, &y);
    cout << "After call by pointer:   x = " << x << ", y = " << y << endl;
    return 0;
}
```

Output:

```text
Inside swapByValue:     a = 20, b = 10
After call by value:     x = 10, y = 20
After call by reference: x = 20, y = 10
After call by pointer:   x = 10, y = 20
```

(The last line swaps them **back**, which proves the pointer version works too.)

**The line that earns the second mark:** by value, the formal parameters are **copies**, so the
actual parameters are unchanged. By reference, the formal parameters are **aliases**, so the swap
happens on the originals.

---

## 8. Student class `[A1 C3 · 3 marks]`

> Use a **parameterized constructor** to initialise name, roll number and marks, and a member function
> to display details and calculate the grade.

The deck-3 grade bands are ≥ 90, 80–89, 70–79, 60–69, 50–59, < 50 = Fail. The letters used below are
placeholders, so use whatever the question gives.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int roll;
    float marks;
public:
    Student(string n, int r, float m) {   // parameterized constructor
        name = n;
        roll = r;
        marks = m;
    }

    char grade() {
        if (marks >= 90) return 'A';
        else if (marks >= 80) return 'B';
        else if (marks >= 70) return 'C';
        else if (marks >= 60) return 'D';
        else if (marks >= 50) return 'E';
        else return 'F';                   // Fail
    }

    void display() {
        cout << "Name: " << name << endl;
        cout << "Roll No: " << roll << endl;
        cout << "Marks: " << marks << endl;
        cout << "Grade: " << grade() << endl;
    }
};

int main() {
    Student s1("Riya", 101, 86.5);
    Student s2("Aman", 102, 47);
    s1.display();
    cout << endl;
    s2.display();
    return 0;
}
```

Output:

```text
Name: Riya
Roll No: 101
Marks: 86.5
Grade: B

Name: Aman
Roll No: 102
Marks: 47
Grade: F
```

---

## 9. Triangle area: default ctor + parameterized ctor + overloading `[A1 D1 · 4 marks]`

**Q ▸** What's the difference between two constructors in one class and two `area()` functions in one
class?

Both are **overloading**: same name, different parameter lists. The compiler picks by the arguments
(compile-time polymorphism). Constructors are overloaded by *how you create the object*. `area()` is
overloaded by *how you call it*.

Two ways to get a triangle's area, which is what makes overloading natural here:
- base and height: **½ · b · h**
- three sides (Heron's formula): **s = (a + b + c)/2, area = √(s(s−a)(s−b)(s−c))**

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Triangle {
private:
    double base, height;
public:
    Triangle() {                       // default constructor
        base = 10;
        height = 5;
    }
    Triangle(double b, double h) {     // parameterized constructor
        base = b;
        height = h;
    }

    double area() {                    // overload 1: uses the members
        return 0.5 * base * height;
    }
    double area(double a, double b, double c) {   // overload 2: Heron's formula
        double s = (a + b + c) / 2;
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }

    void display() {
        cout << "Base = " << base << ", Height = " << height
             << ", Area = " << area() << endl;
    }
};

int main() {
    Triangle t1;            // default constructor runs
    Triangle t2(6, 4);      // parameterized constructor runs

    cout << "Default constructor:       ";
    t1.display();
    cout << "Parameterized constructor: ";
    t2.display();
    cout << "Overloaded area(3, 4, 5):  " << t2.area(3, 4, 5) << endl;
    return 0;
}
```

Output:

```text
Default constructor:       Base = 10, Height = 5, Area = 25
Parameterized constructor: Base = 6, Height = 4, Area = 12
Overloaded area(3, 4, 5):  6
```

---

## Traps

- **`021377` is octal.** Any literal with a leading 0.
- **`do { } while (c);`** needs the semicolon.
- The default access in a `class` is **private**, in a `struct` **public**.
- A destructor has **no arguments and no overloading**. A constructor has **no return type**.
- `int &a` in a **parameter** means reference. `&x` in an **expression** means address-of. Same
  symbol, different jobs.
- `Triangle t();` does **not** create an object. It declares a function. Write `Triangle t;`.

## Self-test

1. Which loop is exit-controlled, and what does that guarantee?
2. Name the three types of constructor.
3. Can a derived class read a `private` member of its base class?
4. What does `cout << 017;` print?
5. `int x = 5; int *p = &x; *p = 9;` — what is x?
6. In what order are three local objects a, b, c destroyed?

## Answers

1. `do-while`. The body runs at least once.
2. Default, parameterized, copy.
3. No. Only `public` and `protected` members are accessible in the derived class.
4. `15` (octal 17 = 8 + 7).
5. 9. `*p` is x.
6. c, b, a (reverse of creation).
