#include <iostream>
using namespace std;

int main()
{
    int arr[5] = {10, 20, 30, 40, 50};       // indexes 0..4

    cout << "for loop: ";
    for (int i = 0; i < 5; i++)              // start; keep going while true; step
        cout << arr[i] << " ";
    cout << endl;

    cout << "backwards with while: ";
    int i = 4;
    while (i >= 0)
    {
        cout << arr[i] << " ";
        i--;
    }
    cout << endl;

    int choice;
    do                                       // body runs at least once
    {
        cout << "Enter 0 to stop: ";
        cin >> choice;
    } while (choice != 0);

    return 0;
}
