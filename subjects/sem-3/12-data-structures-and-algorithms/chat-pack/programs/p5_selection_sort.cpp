#include <iostream>
using namespace std;
int main() {
    int a[] = {64, 25, 12, 22, 11};
    int n = 5;
    for (int i = 0; i < n - 1; i++) {             // pass i fixes position i
        int min = i;                               // assume a[i] is smallest
        for (int j = i + 1; j < n; j++)            // scan the unsorted part
            if (a[j] < a[min]) min = j;            // remember smaller one
        int t = a[i]; a[i] = a[min]; a[min] = t;   // one swap per pass
        cout << "Pass " << i + 1 << ": ";
        for (int k = 0; k < n; k++) cout << a[k] << " ";
        cout << "\n";
    }
    return 0;
}
