#include <iostream>
using namespace std;
#define MAX 5                         // size of the array that holds the queue
class Queue {
    int a[MAX];                       // the boxes
    int front, rear;                  // front = next to leave, rear = last to join
public:
    Queue() { front = -1; rear = -1; }               // empty queue
    void enqueue(int x) {
        if (rear == MAX - 1) { cout << "Queue full (overflow)\n"; return; }
        if (front == -1) front = 0;                   // first element ever
        a[++rear] = x;                                // move rear, then store
        cout << x << " added\n";
    }
    void dequeue() {
        if (front == -1 || front > rear) { cout << "Queue empty (underflow)\n"; return; }
        cout << a[front++] << " deleted\n";           // read front, then move it
    }
    void display() {
        if (front == -1 || front > rear) { cout << "Queue empty\n"; return; }
        cout << "Queue: ";
        for (int i = front; i <= rear; i++) cout << a[i] << " ";
        cout << "\n";
    }
};
int main() {
    Queue q; int ch, x;
    do {
        cout << "1.Add 2.Delete 3.Display 4.Exit: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Value: "; cin >> x; q.enqueue(x); break;
            case 2: q.dequeue(); break;
            case 3: q.display(); break;
        }
    } while (ch != 4);
    return 0;
}
