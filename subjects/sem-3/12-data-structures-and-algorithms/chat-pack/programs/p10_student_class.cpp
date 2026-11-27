// A1 C3 / booklet 2, 3, 9: Student class, parameterized constructor, display + grade
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
