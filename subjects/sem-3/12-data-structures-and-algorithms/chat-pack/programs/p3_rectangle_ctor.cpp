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
