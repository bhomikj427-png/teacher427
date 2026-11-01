#include <iostream>
using namespace std;

int square(int x)                  // takes an int, gives back an int
{
    return x * x;
}

void printArray(int arr[], int n)  // void = gives nothing back
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

void doubleAll(int arr[], int n)   // arrays are NOT copied: changes are seen by main
{
    for (int i = 0; i < n; i++)
        arr[i] = arr[i] * 2;
}

void tryToChange(int x)            // plain int IS copied: main's variable is untouched
{
    x = 99;
    cout << "inside tryToChange: " << x << endl;
}

void reallyChange(int &x)          // & = reference: x IS main's variable
{
    x = 99;
}

int main()
{
    cout << "square(7) = " << square(7) << endl;

    int a[3] = {1, 2, 3};
    doubleAll(a, 3);
    printArray(a, 3);

    int v = 5;
    tryToChange(v);
    cout << "after tryToChange: " << v << endl;
    reallyChange(v);
    cout << "after reallyChange: " << v << endl;
    return 0;
}
