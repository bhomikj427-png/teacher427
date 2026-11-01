// Exp 10 assignment: Circular Queue using an array.
// Same as the linear queue, except rear and front wrap around with  % MAX.
#include <iostream>
using namespace std;

#define MAX 5
int cq[MAX];
int front = -1, rear = -1;

bool isEmpty() { return front == -1; }
bool isFull()  { return (rear + 1) % MAX == front; }   // next slot after rear is front

void enqueue(int value)
{
    if (isFull())
    {
        cout << "Queue Overflow!" << endl;
        return;
    }
    if (isEmpty())
        front = 0;
    rear = (rear + 1) % MAX;                 // 4 -> 0 : wrap around
    cq[rear] = value;
    cout << value << " inserted into queue." << endl;
}

void dequeue()
{
    if (isEmpty())
    {
        cout << "Queue Underflow!" << endl;
        return;
    }
    cout << cq[front] << " deleted from queue." << endl;
    if (front == rear)                       // last element removed
        front = rear = -1;
    else
        front = (front + 1) % MAX;
}

void display()
{
    if (isEmpty())
    {
        cout << "Queue is empty." << endl;
        return;
    }
    cout << "Queue elements are:" << endl;
    int i = front;
    while (true)
    {
        cout << cq[i] << " ";
        if (i == rear)
            break;
        i = (i + 1) % MAX;
    }
    cout << endl;
}

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
            enqueue(value);
        }
        else if (choice == 2)
            dequeue();
        else if (choice == 3)
            display();
        else if (choice == 4)
            cout << "Program terminated." << endl;
        else
            cout << "Invalid choice!" << endl;
    } while (choice != 4);

    return 0;
}
