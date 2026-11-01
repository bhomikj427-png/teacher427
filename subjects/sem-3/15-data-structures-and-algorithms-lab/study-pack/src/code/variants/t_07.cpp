// Exp 7 assignments (separate functions = the experiment itself).
#include "check.h"

// ---- insertionSortDesc ----
// Descending: the ONLY change is  arr[j] > key  ->  arr[j] < key
void insertionSortDesc(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] < key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
// ---- end ----

// ---- insertionSortCount ----
// Counts comparisons (each arr[j] > key test) and shifts (each arr[j+1] = arr[j])
void insertionSortCount(int arr[], int n, int &comparisons, int &shifts)
{
    comparisons = 0;
    shifts = 0;
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0)
        {
            comparisons++;
            if (arr[j] > key)
            {
                arr[j + 1] = arr[j];
                shifts++;
                j--;
            }
            else
                break;
        }
        arr[j + 1] = key;
    }
}
// ---- end ----

// ---- insertionSortFloat ----
// Floating-point version: change the type of the array and of key - nothing else
void insertionSortFloat(float arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        float key = arr[i];
        int j = i - 1;                       // j is an index: stays int
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
// ---- end ----

// ---- findPosition ----
// After sorting, find where x ended up (1-based position, -1 if absent)
int findPosition(int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
        if (arr[i] == x)
            return i + 1;
    return -1;
}
// ---- end ----

int main()
{
    int a[] = {5, 2, 4, 6, 1, 3};
    insertionSortDesc(a, 6);
    check(arrStr(a, 6) == "6 5 4 3 2 1", "insertionSortDesc");

    int c, s;
    int sorted[] = {1, 2, 3, 4, 5, 6};
    insertionSortCount(sorted, 6, c, s);
    check(c == 5 && s == 0, "count sorted: 5 comparisons, 0 shifts (n-1)");
    int rev[] = {6, 5, 4, 3, 2, 1};
    insertionSortCount(rev, 6, c, s);
    check(c == 15 && s == 15 && arrStr(rev, 6) == "1 2 3 4 5 6", "count reverse: 15 = n(n-1)/2");
    int mix[] = {5, 2, 4, 6, 1, 3};
    insertionSortCount(mix, 6, c, s);
    check(s == 9 && c == 12, "count manual example: 9 shifts, 12 comparisons");
    cout << "manual example: comparisons=" << c << " shifts=" << s << endl;

    float f[] = {3.5f, -1.25f, 2.0f, 0.5f};
    insertionSortFloat(f, 4);
    check(f[0] == -1.25f && f[1] == 0.5f && f[2] == 2.0f && f[3] == 3.5f, "insertionSortFloat");

    int p[] = {1, 2, 3, 4, 5, 6};
    check(findPosition(p, 6, 4) == 4 && findPosition(p, 6, 9) == -1, "findPosition");
    return 0;
}
