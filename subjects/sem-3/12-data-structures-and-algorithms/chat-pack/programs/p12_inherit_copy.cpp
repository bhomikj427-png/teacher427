// booklet 4: single inheritance (Result derived from Student); 50Q 8: copy constructor
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
