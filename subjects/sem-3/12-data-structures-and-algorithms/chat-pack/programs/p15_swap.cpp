// A1 B2: swap by value vs by reference
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
