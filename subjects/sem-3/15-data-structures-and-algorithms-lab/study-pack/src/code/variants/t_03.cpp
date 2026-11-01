// Exp 3 assignments. Each function works on arr[] holding n elements, capacity 100.
// It returns the new n (or the old n if nothing could be inserted).
#include "check.h"
const int CAP = 100;

// ---- insertAt ----
int insertAt(int arr[], int n, int pos, int value)   // pos is 1-based
{
    if (n >= CAP || pos < 1 || pos > n + 1)
        return n;                                    // no space / bad position
    for (int i = n; i >= pos; i--)
        arr[i] = arr[i - 1];
    arr[pos - 1] = value;
    return n + 1;
}
// ---- end ----

// ---- insertMultiple ----
// Insert k values (vals[0..k-1]) at the end, stopping if the array fills up
int insertMultiple(int arr[], int n, int vals[], int k)
{
    for (int i = 0; i < k; i++)
    {
        if (n >= CAP)
        {
            cout << "Array full, " << k - i << " value(s) not inserted" << endl;
            break;
        }
        arr[n] = vals[i];
        n++;
    }
    return n;
}
// ---- end ----

// ---- insertSorted ----
// arr is sorted ascending; keep it sorted
int insertSorted(int arr[], int n, int value)
{
    if (n >= CAP)
        return n;
    int i = n - 1;
    while (i >= 0 && arr[i] > value)     // shift bigger ones right (like insertion sort)
    {
        arr[i + 1] = arr[i];
        i--;
    }
    arr[i + 1] = value;
    return n + 1;
}
// ---- end ----

// ---- insertIfSpace ----
int insertIfSpace(int arr[], int n, int value)
{
    if (n >= CAP)
    {
        cout << "No space available. Insertion not possible." << endl;
        return n;
    }
    arr[n] = value;                      // space exists: put it at the end
    return n + 1;
}
// ---- end ----

// ---- insertBefore ----
// Insert value just before the first occurrence of target
int insertBefore(int arr[], int n, int target, int value)
{
    for (int i = 0; i < n; i++)
        if (arr[i] == target)
            return insertAt(arr, n, i + 1, value);   // index i = position i+1
    cout << target << " not found" << endl;
    return n;
}
// ---- end ----

// ---- insertAfter ----
int insertAfter(int arr[], int n, int target, int value)
{
    for (int i = 0; i < n; i++)
        if (arr[i] == target)
            return insertAt(arr, n, i + 2, value);   // one place further right
    cout << target << " not found" << endl;
    return n;
}
// ---- end ----

int main()
{
    int a[CAP] = {10, 20, 30, 40, 50}, n = 5;
    int v[3] = {60, 70, 80};
    n = insertMultiple(a, n, v, 3);
    check(arrStr(a, n) == "10 20 30 40 50 60 70 80", "insertMultiple");

    int s[CAP] = {10, 20, 40, 50}, m = 4;
    m = insertSorted(s, m, 30);
    check(arrStr(s, m) == "10 20 30 40 50", "insertSorted middle");
    m = insertSorted(s, m, 5);
    m = insertSorted(s, m, 99);
    check(arrStr(s, m) == "5 10 20 30 40 50 99", "insertSorted ends");

    int full[CAP];
    for (int i = 0; i < CAP; i++) full[i] = i;
    check(insertIfSpace(full, CAP, 7) == CAP, "insertIfSpace full");
    int b[CAP] = {1, 2}, k = 2;
    k = insertIfSpace(b, k, 3);
    check(arrStr(b, k) == "1 2 3", "insertIfSpace ok");

    int c[CAP] = {10, 20, 30}, q = 3;
    q = insertBefore(c, q, 20, 15);
    check(arrStr(c, q) == "10 15 20 30", "insertBefore");
    q = insertBefore(c, q, 10, 5);
    check(arrStr(c, q) == "5 10 15 20 30", "insertBefore first");
    q = insertAfter(c, q, 30, 35);
    check(arrStr(c, q) == "5 10 15 20 30 35", "insertAfter last");
    q = insertAfter(c, q, 10, 12);
    check(arrStr(c, q) == "5 10 12 15 20 30 35", "insertAfter middle");
    check(insertAfter(c, q, 999, 1) == q, "insertAfter missing");
    return 0;
}
