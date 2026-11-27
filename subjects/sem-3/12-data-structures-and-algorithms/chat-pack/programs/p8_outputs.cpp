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
