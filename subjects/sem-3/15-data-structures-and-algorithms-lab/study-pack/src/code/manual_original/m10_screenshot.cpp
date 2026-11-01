// Exp 10 main() exactly as in the manual's IMPLEMENTATION screenshot (functions trimmed to stubs).
#include <iostream>
using namespace std;
void enqueue(int value) { cout << value; }
void dequeue() {}
int main()
{
    int choice, value;
    do
    {
        cout << "\n1. Enqueue" << endl;
        cout << "2. Dequeue" << endl;
        cout << "3. Display" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        if (choice == 1)
        {
            cout << "Enter value to enqueue: ";
            cin >> value;
        }
        enqueue(value);
        else if (choice == 2)
        {   dequeue();
        else if (choice == 3)
        {   cout << "Program terminated." << endl;
        else
    } while (choice != 4);
    return 0;
}
