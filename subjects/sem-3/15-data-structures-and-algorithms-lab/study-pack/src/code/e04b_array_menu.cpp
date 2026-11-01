// Exp 4 assignment: menu-driven insertion AND deletion on one array
#include <iostream>
using namespace std;

int arr[100], n = 0;

void display()
{
    if (n == 0)
        cout << "Array is empty." << endl;
    else
    {
        cout << "Array: ";
        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
        cout << endl;
    }
}

void insertAt(int pos, int value)            // pos is 1-based
{
    if (n >= 100)
        cout << "Array is full." << endl;
    else if (pos < 1 || pos > n + 1)
        cout << "Invalid position." << endl;
    else
    {
        for (int i = n; i >= pos; i--)
            arr[i] = arr[i - 1];
        arr[pos - 1] = value;
        n++;
    }
}

void deleteAt(int pos)
{
    if (n == 0)
        cout << "Array is empty." << endl;
    else if (pos < 1 || pos > n)
        cout << "Invalid position." << endl;
    else
    {
        cout << "Deleted element: " << arr[pos - 1] << endl;
        for (int i = pos - 1; i < n - 1; i++)
            arr[i] = arr[i + 1];
        n--;
    }
}

int main()
{
    int choice, pos, value;
    do
    {
        cout << "\n1. Insert  2. Delete  3. Display  4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1)
        {
            cout << "Enter position and value: ";
            cin >> pos >> value;
            insertAt(pos, value);
        }
        else if (choice == 2)
        {
            cout << "Enter position: ";
            cin >> pos;
            deleteAt(pos);
        }
        else if (choice == 3)
            display();
        else if (choice != 4)
            cout << "Invalid choice!" << endl;
    } while (choice != 4);

    return 0;
}
