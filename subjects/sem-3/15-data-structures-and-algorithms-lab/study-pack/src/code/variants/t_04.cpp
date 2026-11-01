// Exp 4 assignments (delete at beginning / position / end = the experiment itself).
#include "check.h"

// ---- deleteByValue ----
// Search for value; if found, delete it (first occurrence) and shift left
int deleteByValue(int arr[], int n, int value)
{
    int pos = -1;
    for (int i = 0; i < n; i++)          // linear search
        if (arr[i] == value)
        {
            pos = i;
            break;
        }

    if (pos == -1)
    {
        cout << value << " not found in array" << endl;
        return n;
    }
    for (int i = pos; i < n - 1; i++)
        arr[i] = arr[i + 1];
    return n - 1;
}
// ---- end ----

int main()
{
    int a[100] = {10, 20, 30, 40, 50}, n = 5;
    n = deleteByValue(a, n, 30);
    check(arrStr(a, n) == "10 20 40 50", "deleteByValue middle");
    n = deleteByValue(a, n, 10);
    n = deleteByValue(a, n, 50);
    check(arrStr(a, n) == "20 40", "deleteByValue ends");
    check(deleteByValue(a, n, 7) == 2, "deleteByValue missing");
    return 0;
}
