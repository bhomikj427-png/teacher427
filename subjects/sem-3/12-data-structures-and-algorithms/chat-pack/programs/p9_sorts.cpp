#include <iostream>
using namespace std;
void show(int a[], int n) { for (int k = 0; k < n; k++) cout << a[k] << " "; cout << "\n"; }
int partition(int a[], int lo, int hi) {          // last element is the pivot
    int p = a[hi], i = lo - 1;
    for (int j = lo; j < hi; j++)
        if (a[j] < p) { i++; int t = a[i]; a[i] = a[j]; a[j] = t; }   // small ones go left
    int t = a[i + 1]; a[i + 1] = a[hi]; a[hi] = t;                   // pivot to its final seat
    return i + 1;
}
void quick(int a[], int lo, int hi) {
    if (lo < hi) {
        int p = partition(a, lo, hi);
        cout << "  pivot " << a[p] << " placed at index " << p << ": "; show(a, 6);
        quick(a, lo, p - 1); quick(a, p + 1, hi);
    }
}
void merge(int a[], int l, int m, int r) {
    int t[10], i = l, j = m + 1, k = 0;
    while (i <= m && j <= r) t[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];   // take the smaller front
    while (i <= m) t[k++] = a[i++];
    while (j <= r) t[k++] = a[j++];
    for (k = 0; k < r - l + 1; k++) a[l + k] = t[k];
}
void msort(int a[], int l, int r) {
    if (l < r) {
        int m = (l + r) / 2;
        msort(a, l, m); msort(a, m + 1, r);               // split
        merge(a, l, m, r);                                // join the sorted halves
        cout << "  merged [" << l << ".." << r << "]: "; show(a, 6);
    }
}
int main() {
    int a[] = {29, 10, 14, 37, 13, 5}, n = 6;
    cout << "Bubble 29 10 14 37 13 5\n";
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++)                      // compare neighbours
            if (a[j] > a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; swapped = true; }
        cout << "  pass " << i + 1 << ": "; show(a, n);
        if (!swapped) break;                                     // no swap = sorted
    }
    int b[] = {78, 45, 92, 67, 56, 84};
    cout << "Insertion 78 45 92 67 56 84\n";
    for (int i = 1; i < 6; i++) {
        int key = b[i], j = i - 1;                               // pick the next card
        while (j >= 0 && b[j] > key) { b[j + 1] = b[j]; j--; }   // shift bigger ones right
        b[j + 1] = key;                                          // drop it into the gap
        cout << "  i=" << i << ": "; show(b, 6);
    }
    int q[] = {42, 17, 63, 8, 31, 25};
    cout << "Quick 42 17 63 8 31 25\n"; quick(q, 0, 5);
    int m[] = {64, 25, 12, 22, 11, 90};
    cout << "Merge 64 25 12 22 11 90\n"; msort(m, 0, 5);
    return 0;
}
