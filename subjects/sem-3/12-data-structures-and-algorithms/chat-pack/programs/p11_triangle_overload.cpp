// A1 D1: triangle area with default constructor, parameterized constructor, function overloading
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
