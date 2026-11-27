// A1 D3: convert infix to postfix with a stack (single-letter/digit operands), user-friendly
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
