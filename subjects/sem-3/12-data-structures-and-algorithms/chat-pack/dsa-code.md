# DSA (ECE2104) ETE — all programs, compact

Companion to `dsa-instrV2.md` (§P explains them). Every program compiled with g++ -std=c++17 and run; the output shown is real (`cin` prompts removed, inputs listed). Order = most marks first.

**Three skeletons cover almost everything:** class (fields + constructors + one working function) · array loop (`for (i = 0; i < n; i++)`, change one line) · node walk (`for (p = head; p != NULL; p = p->next)`, change where you stop). **Marks go to:** the core lines, the full/empty/not-found checks, and the output.

## 1. Constructors + destructor: rectangle area — ETE26 D13 (16 m)
```cpp
#include <iostream>
using namespace std;
class Rectangle {
    float length, breadth;
public:
    Rectangle() {                                  // default constructor: no arguments
        length = 1; breadth = 1;
        cout << "Default constructor called\n";
    }
    Rectangle(float l, float b) {                  // parameterized constructor
        length = l; breadth = b;
        cout << "Parameterized constructor called\n";
    }
    Rectangle(float s) {                           // overloaded: one argument = square
        length = s; breadth = s;
        cout << "One-argument constructor called\n";
    }
    float area() { return length * breadth; }
    void display() { cout << "Length = " << length << ", Breadth = " << breadth
                          << ", Area = " << area() << "\n"; }
    ~Rectangle() {                                 // destructor: runs when object dies
        cout << "Destructor called for " << length << " x " << breadth << "\n";
    }
};
int main() {
    Rectangle r1;            // default
    Rectangle r2(10, 5);     // parameterized
    Rectangle r3(4);         // overloaded (square)
    r1.display(); r2.display(); r3.display();
    return 0;                // destructors run here, in reverse order: r3, r2, r1
}
```
Output:
```
Default constructor called
Parameterized constructor called
One-argument constructor called
Length = 1, Breadth = 1, Area = 1
Length = 10, Breadth = 5, Area = 50
Length = 4, Breadth = 4, Area = 16
Destructor called for 4 x 4
Destructor called for 10 x 5
Destructor called for 1 x 1
```

## 2. Triangle: default + parameterized constructor + function overloading — A1 D1
```cpp
#include <iostream>
#include <cmath>
using namespace std;
class Triangle {
    float base, height;
public:
    Triangle() {                                         // default constructor
        base = 1; height = 1;
        cout << "Default constructor called\n";
    }
    Triangle(float b, float h) {                         // parameterized constructor
        base = b; height = h;
        cout << "Parameterized constructor called\n";
    }
    float area() { return 0.5 * base * height; }         // version 0: the stored sides
    float area(float b, float h) { return 0.5 * b * h; } // overload 1: base and height
    float area(float a, float b, float c) {              // overload 2: three sides (Heron)
        float s = (a + b + c) / 2;                       // semi-perimeter
        return sqrt(s * (s - a) * (s - b) * (s - c));
    }
};
int main() {
    Triangle t1;                                         // default
    Triangle t2(10, 6);                                  // parameterized
    cout << "t1 area = " << t1.area() << "\n";
    cout << "t2 area = " << t2.area() << "\n";
    cout << "area(4, 5) = " << t2.area(4, 5) << "\n";    // compiler picks by argument count
    cout << "area(3, 4, 5) = " << t2.area(3, 4, 5) << "\n";
    return 0;
}
```
Output:
```
Default constructor called
Parameterized constructor called
t1 area = 0.5
t2 area = 30
area(4, 5) = 10
area(3, 4, 5) = 6
```

## 3. Student class, parameterized constructor, grade — A1 C3; booklet 2, 3, 9
```cpp
#include <iostream>
#include <string>
using namespace std;
class Student {
    string name;                                 // private data members
    int roll;
    float marks;
public:
    Student(string n, int r, float m) {          // parameterized constructor fills the fields
        name = n; roll = r; marks = m;
    }
    char grade() {                               // if-else ladder, top band first
        if (marks >= 90) return 'A';
        else if (marks >= 75) return 'B';
        else if (marks >= 60) return 'C';
        else if (marks >= 40) return 'D';
        else return 'F';
    }
    void display() {                             // member function uses the private data
        cout << "Name: " << name << ", Roll: " << roll << ", Marks: " << marks
             << ", Grade: " << grade() << (marks >= 40 ? " (Pass)" : " (Fail)") << "\n";
    }
};
int main() {
    Student s1("Riya", 101, 82);                 // constructor runs here
    Student s2("Aman", 102, 35);
    s1.display();
    s2.display();
    return 0;
}
```
Output:
```
Name: Riya, Roll: 101, Marks: 82, Grade: B (Pass)
Name: Aman, Roll: 102, Marks: 35, Grade: F (Fail)
```

## 4. Single inheritance + copy constructor — booklet 4; 50Q 8
```cpp
#include <iostream>
#include <string>
using namespace std;
class Student {
protected:                                       // protected: the child class can use these
    string name; int roll; float marks;
};
class Result : public Student {                  // Result IS-A Student, gets its fields
public:
    void getData() {
        cout << "Enter name, roll, marks: ";
        cin >> name >> roll >> marks;
    }
    void displayResult() {
        cout << name << " (" << roll << "): " << marks
             << (marks >= 40 ? " Pass" : " Fail") << "\n";
    }
};
class Point {
    int x, y;
public:
    Point(int a, int b) { x = a; y = b; }
    Point(const Point &p) {                      // copy constructor: build from another object
        x = p.x; y = p.y;
        cout << "Copy constructor called\n";
    }
    void show() { cout << "(" << x << ", " << y << ")\n"; }
};
int main() {
    Result r;
    r.getData();
    r.displayResult();
    Point p1(3, 4);
    Point p2 = p1;                               // copy constructor runs here
    p1.show(); p2.show();
    return 0;
}
```
Input: `Riya 101 82`
Output:
```
Riya (101): 82 Pass
Copy constructor called
(3, 4)
(3, 4)
```

## 5. Queue using an array (menu) — ETE26 B7 = A1 D4 (8 m)
```cpp
#include <iostream>
using namespace std;
#define MAX 5                         // size of the array that holds the queue
class Queue {
    int a[MAX];                       // the boxes
    int front, rear;                  // front = next to leave, rear = last to join
public:
    Queue() { front = -1; rear = -1; }               // empty queue
    void enqueue(int x) {
        if (rear == MAX - 1) { cout << "Queue full (overflow)\n"; return; }
        if (front == -1) front = 0;                   // first element ever
        a[++rear] = x;                                // move rear, then store
        cout << x << " added\n";
    }
    void dequeue() {
        if (front == -1 || front > rear) { cout << "Queue empty (underflow)\n"; return; }
        cout << a[front++] << " deleted\n";           // read front, then move it
    }
    void display() {
        if (front == -1 || front > rear) { cout << "Queue empty\n"; return; }
        cout << "Queue: ";
        for (int i = front; i <= rear; i++) cout << a[i] << " ";
        cout << "\n";
    }
};
int main() {
    Queue q; int ch, x;
    do {
        cout << "1.Add 2.Delete 3.Display 4.Exit: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Value: "; cin >> x; q.enqueue(x); break;
            case 2: q.dequeue(); break;
            case 3: q.display(); break;
        }
    } while (ch != 4);
    return 0;
}
```
Input: `1 · 10 · 1 · 20 · 1 · 30 · 2 · 3 · 1 · 40 · 1 · 50 · 1 · 60 · 2 · 2 · 2 · 2 · 3 · 4`
Output:
```
10 added
20 added
30 added
10 deleted
Queue: 20 30
40 added
50 added
Queue full (overflow)
20 deleted
30 deleted
40 deleted
50 deleted
Queue empty
```

## 6. Circular queue (array of 5) — deck 8; 50Q 29
```cpp
#include <iostream>
using namespace std;
#define MAX 5
class CQueue {
    int a[MAX], front, rear, count;
public:
    CQueue() { front = 0; rear = -1; count = 0; }
    void enqueue(int x) {
        if (count == MAX) { cout << "Queue full, cannot add " << x << "\n"; return; }
        rear = (rear + 1) % MAX;                 // step right, wrap 4 -> 0
        a[rear] = x; count++;
        cout << "Added " << x << " at index " << rear << "\n";
    }
    void dequeue() {
        if (count == 0) { cout << "Queue empty\n"; return; }
        cout << "Removed " << a[front] << "\n";
        front = (front + 1) % MAX;               // front wraps the same way
        count--;
    }
    void display() {
        cout << "Queue (front -> rear): ";
        for (int i = 0, k = front; i < count; i++, k = (k + 1) % MAX) cout << a[k] << " ";
        cout << "\n";
    }
};
int main() {
    CQueue q;
    for (int x = 10; x <= 50; x += 10) q.enqueue(x);   // fill all 5
    q.enqueue(60);                                      // full
    q.dequeue(); q.dequeue();                           // free index 0 and 1
    q.enqueue(60); q.enqueue(70);                       // reuse them (wrap)
    q.display();
    return 0;
}
```
Output:
```
Added 10 at index 0
Added 20 at index 1
Added 30 at index 2
Added 40 at index 3
Added 50 at index 4
Queue full, cannot add 60
Removed 10
Removed 20
Added 60 at index 0
Added 70 at index 1
Queue (front -> rear): 30 40 50 60 70
```

## 7. Queue using a linked list (menu) — ETE25 D12 (10 m)
```cpp
#include <iostream>
using namespace std;
struct Node { int data; Node* next; };
class Queue {
    Node *front, *rear;              // front = leaves first, rear = joined last
public:
    Queue() { front = rear = NULL; }
    void insert(int x) {             // enqueue at rear
        Node* t = new Node; t->data = x; t->next = NULL;
        if (rear == NULL) front = rear = t;        // first node is both ends
        else { rear->next = t; rear = t; }         // link after rear, move rear
        cout << x << " inserted\n";
    }
    void remove() {                  // dequeue from front
        if (front == NULL) { cout << "Queue empty (underflow)\n"; return; }
        Node* t = front;
        cout << t->data << " deleted\n";
        front = front->next;                       // move front forward
        if (front == NULL) rear = NULL;            // queue became empty
        delete t;                                  // free the old box
    }
    void display() {
        if (front == NULL) { cout << "Queue empty\n"; return; }
        cout << "Queue: ";
        for (Node* p = front; p != NULL; p = p->next) cout << p->data << " ";
        cout << "\n";
    }
};
int main() {
    Queue q; int ch, x;
    do {
        cout << "1.Insert 2.Delete 3.Display 4.Exit: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Value: "; cin >> x; q.insert(x); break;
            case 2: q.remove(); break;
            case 3: q.display(); break;
        }
    } while (ch != 4);
    return 0;
}
```
Input: `1 · 10 · 1 · 20 · 1 · 30 · 3 · 2 · 3 · 2 · 2 · 2 · 4`
Output:
```
10 inserted
20 inserted
30 inserted
Queue: 10 20 30
10 deleted
Queue: 20 30
20 deleted
30 deleted
Queue empty (underflow)
```

## 8. Stack using an array: PUSH, POP, PEEK, DISPLAY — A1 B5, C1
```cpp
#include <iostream>
using namespace std;
#define MAX 5
class Stack {
    int a[MAX];
    int top;                                     // index of the top box; -1 = empty
public:
    Stack() { top = -1; }
    void push(int x) {
        if (top == MAX - 1) { cout << "Overflow: cannot push " << x << "\n"; return; }
        a[++top] = x;                            // move up first, then store
        cout << "Pushed " << x << "\n";
    }
    void pop() {
        if (top == -1) { cout << "Underflow: stack empty\n"; return; }
        cout << "Popped " << a[top--] << "\n";   // read first, then move down
    }
    void peek() {
        if (top == -1) cout << "Stack empty\n";
        else cout << "Top = " << a[top] << "\n";
    }
    void display() {
        if (top == -1) { cout << "Stack empty\n"; return; }
        cout << "Stack (bottom -> top): ";
        for (int i = 0; i <= top; i++) cout << a[i] << " ";
        cout << "\n";
    }
};
int main() {
    Stack s;
    s.push(10); s.push(20);                      // A1 C1 sequence
    s.pop(); s.pop(); s.pop();                   // third POP = underflow
    s.push(30); s.push(40);
    s.peek(); s.display();
    return 0;
}
```
Output:
```
Pushed 10
Pushed 20
Popped 20
Popped 10
Underflow: stack empty
Pushed 30
Pushed 40
Top = 40
Stack (bottom -> top): 30 40
```

## 9. Infix to postfix — A1 D3
```cpp
#include <iostream>
#include <string>
using namespace std;
char st[100]; int top = -1;
void push(char c) { st[++top] = c; }
char pop() { return st[top--]; }
int prec(char c) {                               // bigger number = binds tighter
    if (c == '^') return 3;
    if (c == '*' || c == '/') return 2;
    if (c == '+' || c == '-') return 1;
    return 0;                                    // '(' sits lowest, never popped by an operator
}
int main() {
    string in, out = "";
    cout << "Enter infix expression: ";
    cin >> in;
    for (char c : in) {
        if (isalnum(c)) out += c;                // operand: straight to output
        else if (c == '(') push(c);              // '(' : always push
        else if (c == ')') {                     // ')' : pop until the matching '('
            while (st[top] != '(') out += pop();
            pop();                               // throw the '(' away
        } else {                                 // operator
            while (top != -1 && prec(st[top]) >= prec(c) && c != '^')
                out += pop();                    // pop everything that binds at least as tight
            push(c);
        }
    }
    while (top != -1) out += pop();              // empty the stack at the end
    cout << "Postfix: " << out << "\n";
    return 0;
}
```
Input: `((A+B)/C)*(D-E)`
Output:
```
Postfix: AB+C/DE-*
```

## 10. Postfix evaluation, stack after every operator — A1 C4
```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int st[50], top = -1;
void push(int x) { st[++top] = x; }
int pop() { return st[top--]; }
void show() {
    cout << "  stack: ";
    for (int i = 0; i <= top; i++) cout << st[i] << " ";
    cout << "\n";
}
int main() {
    string line, tok;
    cout << "Enter postfix (tokens separated by spaces): ";
    getline(cin, line);
    stringstream ss(line);                       // split the line into tokens
    while (ss >> tok) {
        if (isdigit(tok[0])) push(stoi(tok));    // operand: push it
        else {
            int b = pop();                       // operator: pop the RIGHT operand first
            int a = pop();                       // then the left one
            int r;
            if (tok == "+") r = a + b;
            else if (tok == "-") r = a - b;
            else if (tok == "*") r = a * b;
            else r = a / b;
            push(r);                             // result goes back on the stack
            cout << "after " << tok; show();
        }
    }
    cout << "Result = " << pop() << "\n";
    return 0;
}
```
Input: `12 3 4 * + 6 2 / -`
Output:
```
after *  stack: 12 12
after +  stack: 24
after /  stack: 24 3
after -  stack: 21
Result = 21
```

## 11. Linked list insertion: beginning, end, after a node — ETE26 B8 = A1 C5 (8 m)
```cpp
#include <iostream>
using namespace std;
struct Node {                         // one box: data + arrow to the next box
    int data;
    Node* next;
};
Node* head = NULL;                    // arrow to the first box (NULL = empty list)
void insertBegin(int x) {
    Node* t = new Node;               // make a new box
    t->data = x;
    t->next = head;                   // new box points to old first box
    head = t;                         // head now points to new box
}
void insertEnd(int x) {
    Node* t = new Node;
    t->data = x; t->next = NULL;      // last box points to nothing
    if (head == NULL) { head = t; return; }
    Node* p = head;
    while (p->next != NULL) p = p->next;   // walk to the last box
    p->next = t;                      // old last box points to new box
}
void insertAfter(int key, int x) {
    Node* p = head;
    while (p != NULL && p->data != key) p = p->next;   // find the box holding key
    if (p == NULL) { cout << key << " not found\n"; return; }
    Node* t = new Node;
    t->data = x;
    t->next = p->next;                // FIRST: new box points to p's old next
    p->next = t;                      // THEN: p points to new box
}
void display() {
    for (Node* p = head; p != NULL; p = p->next) cout << p->data << " -> ";
    cout << "NULL\n";
}
int main() {
    insertEnd(12); insertEnd(24); insertEnd(36); insertEnd(48); insertEnd(60);
    display();
    insertBegin(6);       display();
    insertAfter(36, 42);  display();
    insertEnd(72);        display();
    return 0;
}
```
Output:
```
12 -> 24 -> 36 -> 48 -> 60 -> NULL
6 -> 12 -> 24 -> 36 -> 48 -> 60 -> NULL
6 -> 12 -> 24 -> 36 -> 42 -> 48 -> 60 -> NULL
6 -> 12 -> 24 -> 36 -> 42 -> 48 -> 60 -> 72 -> NULL
```

## 12. Linked list: insert, delete, search, display, sort by swapping data — A1 B1, D2
```cpp
#include <iostream>
using namespace std;
struct Node {
    int data;
    Node *next;
};
Node *head = NULL;
void insertBegin(int x) {
    Node *n = new Node; n->data = x;
    n->next = head;                              // new box points at the old first box
    head = n;                                    // head now points at the new box
}
void insertEnd(int x) {
    Node *n = new Node; n->data = x; n->next = NULL;
    if (head == NULL) { head = n; return; }      // empty list: it becomes the head
    Node *p = head;
    while (p->next != NULL) p = p->next;         // walk to the last box
    p->next = n;                                 // hook the new box on
}
void deleteValue(int x) {
    if (head == NULL) { cout << "List empty\n"; return; }
    if (head->data == x) {                       // deleting the first box
        Node *t = head; head = head->next; delete t;
        cout << "Deleted " << x << "\n"; return;
    }
    Node *p = head;
    while (p->next != NULL && p->next->data != x) p = p->next;   // stop one box BEFORE it
    if (p->next == NULL) { cout << x << " not found\n"; return; }
    Node *t = p->next;
    p->next = t->next;                           // bypass the box
    delete t;                                    // free its memory
    cout << "Deleted " << x << "\n";
}
void search(int x) {
    int pos = 1;
    for (Node *p = head; p != NULL; p = p->next, pos++)
        if (p->data == x) { cout << x << " found at position " << pos << "\n"; return; }
    cout << x << " not found\n";
}
void display() {
    for (Node *p = head; p != NULL; p = p->next) cout << p->data << " -> ";
    cout << "NULL\n";
}
void sortList() {                                // swap DATA, not links
    for (Node *p = head; p != NULL; p = p->next)
        for (Node *q = p->next; q != NULL; q = q->next)
            if (p->data > q->data) { int t = p->data; p->data = q->data; q->data = t; }
}
int main() {
    int n, x;
    cout << "How many nodes? "; cin >> n;
    cout << "Enter " << n << " values: ";
    for (int i = 0; i < n; i++) { cin >> x; insertEnd(x); }
    cout << "\nList: "; display();
    insertBegin(5); cout << "After insertBegin(5): "; display();
    deleteValue(30); cout << "List: "; display();
    search(40);
    sortList(); cout << "Sorted: "; display();
    return 0;
}
```
Input: `5 · 40 10 30 50 20`
Output:
```
List: 40 -> 10 -> 30 -> 50 -> 20 -> NULL
After insertBegin(5): 5 -> 40 -> 10 -> 30 -> 50 -> 20 -> NULL
Deleted 30
List: 5 -> 40 -> 10 -> 50 -> 20 -> NULL
40 found at position 2
Sorted: 5 -> 10 -> 20 -> 40 -> 50 -> NULL
```

## 13. Reverse a linked list — MTE24 Q8 (8 m)
```cpp
#include <iostream>
using namespace std;
struct Node { int data; Node* next; };
Node* head = NULL;
void insertEnd(int x) {
    Node* t = new Node; t->data = x; t->next = NULL;
    if (!head) { head = t; return; }
    Node* p = head; while (p->next) p = p->next; p->next = t;
}
void display() { for (Node* p = head; p; p = p->next) cout << p->data << " -> "; cout << "NULL\n"; }
void reverse() {
    Node *prev = NULL, *curr = head, *nxt;
    while (curr != NULL) {
        nxt = curr->next;      // 1. save the rest of the list
        curr->next = prev;     // 2. flip this arrow backwards
        prev = curr;           // 3. step prev forward
        curr = nxt;            // 4. step curr forward
    }
    head = prev;               // last box is the new first box
}
int main() {
    insertEnd(10); insertEnd(20); insertEnd(30); insertEnd(40);
    display(); reverse(); display();
    return 0;
}
```
Output:
```
10 -> 20 -> 30 -> 40 -> NULL
40 -> 30 -> 20 -> 10 -> NULL
```

## 14. BST insert + preorder / inorder / postorder — ETE26 C11, ETE25 B
```cpp
#include <iostream>
using namespace std;
struct Node { int data; Node *left, *right; };
Node* insert(Node* r, int x) {
    if (r == NULL) { r = new Node; r->data = x; r->left = r->right = NULL; return r; }
    if (x < r->data) r->left = insert(r->left, x);     // smaller goes left
    else r->right = insert(r->right, x);               // bigger goes right
    return r;
}
void preorder(Node* r)  { if (r) { cout << r->data << " "; preorder(r->left); preorder(r->right); } }
void inorder(Node* r)   { if (r) { inorder(r->left); cout << r->data << " "; inorder(r->right); } }
void postorder(Node* r) { if (r) { postorder(r->left); postorder(r->right); cout << r->data << " "; } }
int main() {
    int a[] = {45, 36, 76, 23, 89, 115, 98, 39, 41, 56, 69, 48};
    Node* root = NULL;
    for (int i = 0; i < 12; i++) root = insert(root, a[i]);
    cout << "Preorder:  "; preorder(root);  cout << "\n";
    cout << "Inorder:   "; inorder(root);   cout << "\n";
    cout << "Postorder: "; postorder(root); cout << "\n";
    return 0;
}
```
Output:
```
Preorder:  45 36 23 39 41 76 56 48 69 89 115 98
Inorder:   23 36 39 41 45 48 56 69 76 89 98 115
Postorder: 23 41 39 36 48 69 56 98 115 89 76 45
```

## 15. Selection sort — ETE25 D13 (10 m)
```cpp
#include <iostream>
using namespace std;
int main() {
    int a[] = {64, 25, 12, 22, 11};
    int n = 5;
    for (int i = 0; i < n - 1; i++) {             // pass i fixes position i
        int min = i;                               // assume a[i] is smallest
        for (int j = i + 1; j < n; j++)            // scan the unsorted part
            if (a[j] < a[min]) min = j;            // remember smaller one
        int t = a[i]; a[i] = a[min]; a[min] = t;   // one swap per pass
        cout << "Pass " << i + 1 << ": ";
        for (int k = 0; k < n; k++) cout << a[k] << " ";
        cout << "\n";
    }
    return 0;
}
```
Output:
```
Pass 1: 11 25 12 22 64
Pass 2: 11 12 25 22 64
Pass 3: 11 12 22 25 64
Pass 4: 11 12 22 25 64
```

## 16. Bubble sort + insertion sort — 50Q 13; booklet 73-76
```cpp
#include <iostream>
using namespace std;
void show(int a[], int n) { for (int i = 0; i < n; i++) cout << a[i] << " "; cout << "\n"; }
void bubble(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {            // after pass i, the last i+1 are in place
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++)      // compare neighbours in the unsorted part
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
                swapped = true;
            }
        if (!swapped) break;                     // no swap = already sorted: stop early
    }
}
void insertion(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];                          // the next card
        int j = i - 1;
        while (j >= 0 && a[j] > key) {           // shift bigger cards one place right
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;                          // drop the card into the gap
    }
}
int main() {
    int a[50], b[50], n;
    cout << "How many elements? "; cin >> n;
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) { cin >> a[i]; b[i] = a[i]; }
    bubble(a, n);    cout << "Bubble:    "; show(a, n);
    insertion(b, n); cout << "Insertion: "; show(b, n);
    return 0;
}
```
Input: `6 · 29 10 14 37 13 5`
Output:
```
Bubble:    5 10 13 14 29 37
Insertion: 5 10 13 14 29 37
```

## 17. Bubble / insertion / quick / merge with pass traces — booklet 64-76
```cpp
#include <iostream>
using namespace std;
void show(int a[], int n) { for (int k = 0; k < n; k++) cout << a[k] << " "; cout << "\n"; }
int partition(int a[], int lo, int hi) {          // last element is the pivot
    int p = a[hi], i = lo - 1;
    for (int j = lo; j < hi; j++)
        if (a[j] < p) { i++; int t = a[i]; a[i] = a[j]; a[j] = t; }   // small ones go left
    int t = a[i + 1]; a[i + 1] = a[hi]; a[hi] = t;                   // pivot to its final seat
    return i + 1;
}
void quick(int a[], int lo, int hi) {
    if (lo < hi) {
        int p = partition(a, lo, hi);
        cout << "  pivot " << a[p] << " placed at index " << p << ": "; show(a, 6);
        quick(a, lo, p - 1); quick(a, p + 1, hi);
    }
}
void merge(int a[], int l, int m, int r) {
    int t[10], i = l, j = m + 1, k = 0;
    while (i <= m && j <= r) t[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];   // take the smaller front
    while (i <= m) t[k++] = a[i++];
    while (j <= r) t[k++] = a[j++];
    for (k = 0; k < r - l + 1; k++) a[l + k] = t[k];
}
void msort(int a[], int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;
        msort(a, l, m); msort(a, m + 1, r);               // split
        merge(a, l, m, r);                                // join the sorted halves
        cout << "  merged [" << l << ".." << r << "]: "; show(a, 6);
    }
}
int main() {
    int a[] = {29, 10, 14, 37, 13, 5}, n = 6;
    cout << "Bubble 29 10 14 37 13 5\n";
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++)                      // compare neighbours
            if (a[j] > a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; swapped = true; }
        cout << "  pass " << i + 1 << ": "; show(a, n);
        if (!swapped) break;                                     // no swap = sorted
    }
    int b[] = {78, 45, 92, 67, 56, 84};
    cout << "Insertion 78 45 92 67 56 84\n";
    for (int i = 1; i < 6; i++) {
        int key = b[i], j = i - 1;                               // pick the next card
        while (j >= 0 && b[j] > key) { b[j + 1] = b[j]; j--; }   // shift bigger ones right
        b[j + 1] = key;                                          // drop it into the gap
        cout << "  i=" << i << ": "; show(b, 6);
    }
    int q[] = {42, 17, 63, 8, 31, 25};
    cout << "Quick 42 17 63 8 31 25\n"; quick(q, 0, 5);
    int m[] = {64, 25, 12, 22, 11, 90};
    cout << "Merge 64 25 12 22 11 90\n"; msort(m, 0, 5);
    return 0;
}
```
Output:
```
Bubble 29 10 14 37 13 5
  pass 1: 10 14 29 13 5 37
  pass 2: 10 14 13 5 29 37
  pass 3: 10 13 5 14 29 37
  pass 4: 10 5 13 14 29 37
  pass 5: 5 10 13 14 29 37
Insertion 78 45 92 67 56 84
  i=1: 45 78 92 67 56 84
  i=2: 45 78 92 67 56 84
  i=3: 45 67 78 92 56 84
  i=4: 45 56 67 78 92 84
  i=5: 45 56 67 78 84 92
Quick 42 17 63 8 31 25
  pivot 25 placed at index 2: 17 8 25 42 31 63
  pivot 8 placed at index 0: 8 17 25 42 31 63
  pivot 63 placed at index 5: 8 17 25 42 31 63
  pivot 31 placed at index 3: 8 17 25 31 42 63
Merge 64 25 12 22 11 90
  merged [0..1]: 25 64 12 22 11 90
  merged [0..2]: 12 25 64 22 11 90
  merged [3..4]: 12 25 64 11 22 90
  merged [3..5]: 12 25 64 11 22 90
  merged [0..5]: 11 12 22 25 64 90
```

## 18. Array: insert at a position, delete from a position — A1 B4
```cpp
#include <iostream>
using namespace std;
void display(int a[], int n) {
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
}
int main() {
    int a[50], n, pos, x;
    cout << "How many elements? "; cin >> n;
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << "Insert: value and position (1.." << n + 1 << "): "; cin >> x >> pos;
    if (pos < 1 || pos > n + 1) cout << "Invalid position\n";
    else {
        for (int i = n; i >= pos; i--)           // shift right, starting from the END
            a[i] = a[i - 1];
        a[pos - 1] = x;                          // drop the value into the gap
        n++;                                     // one more element
        cout << "After insertion: "; display(a, n);
    }
    cout << "Delete: position (1.." << n << "): "; cin >> pos;
    if (pos < 1 || pos > n) cout << "Invalid position\n";
    else {
        cout << "Deleted " << a[pos - 1] << "\n";
        for (int i = pos - 1; i < n - 1; i++)    // shift left over the hole
            a[i] = a[i + 1];
        n--;                                     // one fewer element
        cout << "After deletion: "; display(a, n);
    }
    return 0;
}
```
Input: `5 · 10 20 30 40 50 · 99 3 · 5`
Output:
```
After insertion: 10 20 99 30 40 50
Deleted 40
After deletion: 10 20 99 30 50
```

## 19. Array one-loop programs + pointer moves — booklet 10-17, 28; 50Q 11-15
```cpp
#include <iostream>
using namespace std;
int main() {
    int a[10] = {12, -5, 8, 21, -3, 40, 7, 0, 16, -9};
    int n = 10;
    // sum, average, max, min: one pass, keep a running answer
    int sum = 0, mx = a[0], mn = a[0];
    for (int i = 0; i < n; i++) {
        sum += a[i];
        if (a[i] > mx) mx = a[i];
        if (a[i] < mn) mn = a[i];
    }
    cout << "Sum " << sum << ", Avg " << (float)sum / n << ", Max " << mx << ", Min " << mn << "\n";
    // linear search: walk and compare; stop at the first match
    int key = 21, found = -1;
    for (int i = 0; i < n; i++)
        if (a[i] == key) { found = i; break; }
    if (found != -1) cout << key << " found at index " << found << "\n";
    else cout << key << " not found\n";
    // count even / odd / positive / negative
    int ev = 0, od = 0, pos = 0, neg = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) ev++; else od++;
        if (a[i] > 0) pos++; else if (a[i] < 0) neg++;
    }
    cout << "Even " << ev << ", Odd " << od << ", Positive " << pos << ", Negative " << neg << "\n";
    // reverse in place: swap the two ends, walk inward
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }
    cout << "Reversed: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
    // pointer moves (booklet 28): p += k moves k ELEMENTS, not k bytes
    int b[6] = {10, 20, 30, 40, 50, 60};
    int *p = b;                                  // p -> b[0]
    p += 3; cout << "*p after +3: " << *p << "\n";   // b[3]
    p -= 2; cout << "*p after -2: " << *p << "\n";   // b[1]
    return 0;
}
```
Output:
```
Sum 87, Avg 8.7, Max 40, Min -9
21 found at index 3
Even 5, Odd 5, Positive 6, Negative 3
Reversed: -9 16 0 7 40 -3 21 8 -5 12
*p after +3: 40
*p after -2: 20
```

## 20. Swap by value vs by reference — A1 B2
```cpp
#include <iostream>
using namespace std;
void swapValue(int a, int b) {                   // a, b are COPIES
    int t = a; a = b; b = t;
}
void swapRef(int &a, int &b) {                   // a, b are other names for x, y
    int t = a; a = b; b = t;
}
int main() {
    int x = 5, y = 9;
    swapValue(x, y);
    cout << "After swapValue: x = " << x << ", y = " << y << "\n";
    swapRef(x, y);
    cout << "After swapRef:   x = " << x << ", y = " << y << "\n";
    return 0;
}
```
Output:
```
After swapx = 5, y = 9
After swapRef:   x = 9, y = 5
```

## 21. Output-prediction snippets — ETE26 A6 = A1 A7; MTE24 Q1-Q7
```cpp
#include <iostream>
using namespace std;
long int zip;
void Sum(int a, int b, int &c) { a = b + c; b = a + c; c = a + b; }
void fun(int x, int y) { x = 20; y = 10; }
class Base1 { public: Base1() { cout << "Base1's constructor called" << endl; } };
class Base2 { public: Base2() { cout << "Base2's constructor called" << endl; } };
class Derived : public Base1, public Base2 { public: Derived() { cout << "Derived's constructor called" << endl; } };
int array1[] = {1200, 200, 2300, 1230, 1543};
int array2[] = {12, 14, 16, 18, 20};
int main() {
    zip = 021377;
    cout << "ETE26 Q6: New York's zip code is: " << zip << '\n';
    { int x = 2, y = 3; Sum(x, y, y); cout << "MTE Q1: " << x << " " << y << "\n"; }
    { int x = 10; fun(x, x); cout << "MTE Q2: " << x << "\n"; }
    { int array[] = {10, 20, 30}; cout << "MTE Q3: " << -2[array] << "\n"; }
    { int temp, result = 0;
      for (temp = 0; temp < 5; temp++) result += array1[temp];
      for (temp = 0; temp < 4; temp++) result += array2[temp];
      cout << "MTE Q4: " << result << "\n"; }
    { cout << "MTE Q5:\n"; Derived d; }
    { class student { public: int rno = 10; } v; cout << "MTE Q6: " << v.rno << "\n"; }
    return 0;
}
```
Output:
```
ETE26 Q6: New York's zip code is: 8959
MTE Q1: 2 15
MTE Q2: 10
MTE Q3: -30
MTE Q4: 6533
MTE Q5:
Base1's constructor called
Base2's constructor called
Derived's constructor called
MTE Q6: 10
```
