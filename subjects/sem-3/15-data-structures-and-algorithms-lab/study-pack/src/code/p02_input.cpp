#include <iostream>
using namespace std;

int main()
{
    int a, b;                          // two whole-number boxes
    cout << "Enter two numbers: ";
    cin >> a >> b;                     // read two numbers typed by the user

    int sum = a + b;
    cout << "Sum = " << sum << endl;
    cout << "a / b = " << a / b << endl;      // int / int drops the fraction
    cout << "a % b = " << a % b << endl;      // % = remainder

    if (a > b)
        cout << "a is bigger" << endl;
    else if (a == b)                   // == compares, = stores
        cout << "equal" << endl;
    else
        cout << "b is bigger" << endl;

    return 0;
}
