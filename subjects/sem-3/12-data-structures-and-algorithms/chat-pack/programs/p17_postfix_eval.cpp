// A1 C4: evaluate a postfix expression with a stack; show the stack after every operator
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
