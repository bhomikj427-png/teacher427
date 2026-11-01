// Exp 8 assignments (separate functions = the experiment itself). Uses swapElements from Exp 8.
#include "check.h"

void swapElements(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

// ---- quickSortDesc ----
// Descending: the ONLY change is  arr[j] < pivot  ->  arr[j] > pivot
int partitionDesc(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
        if (arr[j] > pivot)
        {
            i++;
            swapElements(arr[i], arr[j]);
        }
    swapElements(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSortDesc(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partitionDesc(arr, low, high);
        quickSortDesc(arr, low, pi - 1);
        quickSortDesc(arr, pi + 1, high);
    }
}
// ---- end ----

// ---- pivotFirst ----
// First element as pivot: swap it to the end, then partition exactly as before
int partitionFirst(int arr[], int low, int high)
{
    swapElements(arr[low], arr[high]);
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
        if (arr[j] < pivot)
        {
            i++;
            swapElements(arr[i], arr[j]);
        }
    swapElements(arr[i + 1], arr[high]);
    return i + 1;
}
// ---- end ----

// ---- pivotMiddle ----
// Middle element as pivot: same trick (sorted input no longer gives the worst case)
int partitionMiddle(int arr[], int low, int high)
{
    int mid = low + (high - low) / 2;
    swapElements(arr[mid], arr[high]);
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
        if (arr[j] < pivot)
        {
            i++;
            swapElements(arr[i], arr[j]);
        }
    swapElements(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSortMiddle(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partitionMiddle(arr, low, high);
        quickSortMiddle(arr, low, pi - 1);
        quickSortMiddle(arr, pi + 1, high);
    }
}
// ---- end ----

void quickSortFirst(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partitionFirst(arr, low, high);
        quickSortFirst(arr, low, pi - 1);
        quickSortFirst(arr, pi + 1, high);
    }
}

// ---- quickSortCount ----
// Global counters: every function can add to them; reset to 0 before sorting
int comparisons = 0, swaps = 0;

int partitionCount(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++)
    {
        comparisons++;
        if (arr[j] < pivot)
        {
            i++;
            swapElements(arr[i], arr[j]);
            swaps++;
        }
    }
    swapElements(arr[i + 1], arr[high]);
    swaps++;
    return i + 1;
}

void quickSortCount(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partitionCount(arr, low, high);
        quickSortCount(arr, low, pi - 1);
        quickSortCount(arr, pi + 1, high);
    }
}
// ---- end ----

// ---- mergeSort ----
// Merge Sort: split in half, sort each half, merge the two sorted halves
void merge(int arr[], int low, int mid, int high)
{
    int temp[100];                           // holds the merged result
    int i = low, j = mid + 1, k = 0;
    while (i <= mid && j <= high)
    {
        if (arr[i] <= arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }
    while (i <= mid)                         // leftovers of the left half
        temp[k++] = arr[i++];
    while (j <= high)                        // leftovers of the right half
        temp[k++] = arr[j++];
    for (int t = 0; t < k; t++)              // copy back
        arr[low + t] = temp[t];
}

void mergeSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int mid = (low + high) / 2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}
// ---- end ----

int main()
{
    int a[] = {10, 7, 8, 9, 1, 5};
    quickSortDesc(a, 0, 5);
    check(arrStr(a, 6) == "10 9 8 7 5 1", "quickSortDesc");
    int b[] = {10, 7, 8, 9, 1, 5, 5, -2};
    quickSortFirst(b, 0, 7);
    check(arrStr(b, 8) == "-2 1 5 5 7 8 9 10", "pivot first");
    int c[] = {10, 7, 8, 9, 1, 5, 5, -2};
    quickSortMiddle(c, 0, 7);
    check(arrStr(c, 8) == "-2 1 5 5 7 8 9 10", "pivot middle");

    int d[] = {10, 7, 8, 9, 1, 5};
    comparisons = swaps = 0;
    quickSortCount(d, 0, 5);
    check(arrStr(d, 6) == "1 5 7 8 9 10", "quickSortCount sorts");
    cout << "manual example: comparisons=" << comparisons << " swaps=" << swaps << endl;
    check(comparisons == 11 && swaps == 5, "quickSortCount manual example: 11 comparisons, 5 swaps");

    int s[] = {1, 2, 3, 4, 5, 6};
    comparisons = swaps = 0;
    quickSortCount(s, 0, 5);
    check(comparisons == 15, "sorted input, last pivot: 15 = n(n-1)/2 comparisons (worst case)");

    int m[] = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(m, 0, 6);
    check(arrStr(m, 7) == "3 9 10 27 38 43 82", "mergeSort");
    return 0;
}
