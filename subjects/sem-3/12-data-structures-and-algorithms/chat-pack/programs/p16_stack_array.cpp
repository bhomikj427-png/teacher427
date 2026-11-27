// A1 B5 / A1 C1: stack using an array with PUSH, POP, PEEK, DISPLAY; overflow + underflow
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
