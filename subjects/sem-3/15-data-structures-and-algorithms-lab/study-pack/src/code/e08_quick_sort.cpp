#include <iostream>
using namespace std;

// Function to swap two elements (& = work on the caller's variables)
void swapElements(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

// Function to partition the array around the last element
int partitionArray(int arr[], int low, int high)
{
    int pivot = arr[high];                   // last element as pivot
    int i = low - 1;                         // end of the "smaller than pivot" zone

    for (int j = low; j < high; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swapElements(arr[i], arr[j]);
        }
    }
    swapElements(arr[i + 1], arr[high]);     // pivot goes just after the small zone
    return i + 1;                            // pivot's final index
}

// Function to implement Quick Sort
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partitionArray(arr, low, high);
        quickSort(arr, low, pi - 1);         // sort left part
        quickSort(arr, pi + 1, high);        // sort right part
    }
}

// Function to display the array
void displayArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main()
{
    int n;
    int arr[100];                            // FIX: was int arr[n] (not standard C++)

    cout << "Enter number of elements: ";
    cin >> n;

    if (n < 1 || n > 100)
    {
        cout << "n must be between 1 and 100.";
        return 0;
    }

    cout << "Enter elements of the array:" << endl;
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    cout << "Original Array: ";
    displayArray(arr, n);

    quickSort(arr, 0, n - 1);

    cout << "Sorted Array using Quick Sort: ";
    displayArray(arr, n);

    return 0;
}
