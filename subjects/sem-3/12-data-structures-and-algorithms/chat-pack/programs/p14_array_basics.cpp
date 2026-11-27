// 50Q 11-15, booklet 10-17, 28-29: the one-loop array programs + pointer moves
#include <iostream>
using namespace std;
int main() {
    int a[10] = {12, -5, 8, 21, -3, 40, 7, 0, 16, -9};
    int n = 10;
    // sum, average, max, min: one pass, keep a running answer
    int sum = 0, mx = a[0], mn = a[0];
    for (int i = 0; i < n; i++) {
        sum += a[i];
        if (a[i] > mx) mx = a[i];
        if (a[i] < mn) mn = a[i];
    }
    cout << "Sum " << sum << ", Avg " << (float)sum / n << ", Max " << mx << ", Min " << mn << "\n";
    // linear search: walk and compare; stop at the first match
    int key = 21, found = -1;
    for (int i = 0; i < n; i++)
        if (a[i] == key) { found = i; break; }
    if (found != -1) cout << key << " found at index " << found << "\n";
    else cout << key << " not found\n";
    // count even / odd / positive / negative
    int ev = 0, od = 0, pos = 0, neg = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) ev++; else od++;
        if (a[i] > 0) pos++; else if (a[i] < 0) neg++;
    }
    cout << "Even " << ev << ", Odd " << od << ", Positive " << pos << ", Negative " << neg << "\n";
    // reverse in place: swap the two ends, walk inward
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }
    cout << "Reversed: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << "\n";
    // pointer moves (booklet 28): p += k moves k ELEMENTS, not k bytes
    int b[6] = {10, 20, 30, 40, 50, 60};
    int *p = b;                                  // p -> b[0]
    p += 3; cout << "*p after +3: " << *p << "\n";   // b[3]
    p -= 2; cout << "*p after -2: " << *p << "\n";   // b[1]
    return 0;
}
