// A1 B4: insert an element at a position and delete from a position (user-friendly)
#include <iostream>
using namespace std;
void display(int a[], int n) {
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
}
int main() {
    int a[50], n, pos, x;
    cout << "How many elements? "; cin >> n;
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << "Insert: value and position (1.." << n + 1 << "): "; cin >> x >> pos;
    if (pos < 1 || pos > n + 1) cout << "Invalid position\n";
    else {
        for (int i = n; i >= pos; i--)           // shift right, starting from the END
            a[i] = a[i - 1];
        a[pos - 1] = x;                          // drop the value into the gap
        n++;                                     // one more element
        cout << "After insertion: "; display(a, n);
    }
    cout << "Delete: position (1.." << n << "): "; cin >> pos;
    if (pos < 1 || pos > n) cout << "Invalid position\n";
    else {
        cout << "Deleted " << a[pos - 1] << "\n";
        for (int i = pos - 1; i < n - 1; i++)    // shift left over the hole
            a[i] = a[i + 1];
        n--;                                     // one fewer element
        cout << "After deletion: "; display(a, n);
    }
    return 0;
}
