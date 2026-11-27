// 50Q 13, booklet 73-76: bubble sort (with early stop) and insertion sort, user input
#include <iostream>
using namespace std;
void show(int a[], int n) { for (int i = 0; i < n; i++) cout << a[i] << " "; cout << "\n"; }
void bubble(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {            // after pass i, the last i+1 are in place
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++)      // compare neighbours in the unsorted part
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
                swapped = true;
            }
        if (!swapped) break;                     // no swap = already sorted: stop early
    }
}
void insertion(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];                          // the next card
        int j = i - 1;
        while (j >= 0 && a[j] > key) {           // shift bigger cards one place right
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;                          // drop the card into the gap
    }
}
int main() {
    int a[50], b[50], n;
    cout << "How many elements? "; cin >> n;
    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) { cin >> a[i]; b[i] = a[i]; }
    bubble(a, n);    cout << "Bubble:    "; show(a, n);
    insertion(b, n); cout << "Insertion: "; show(b, n);
    return 0;
}
