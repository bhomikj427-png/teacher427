// circular queue with an array of 5 (fixes the linear queue's false "full")
#include <iostream>
using namespace std;
#define MAX 5
class CQueue {
    int a[MAX], front, rear, count;
public:
    CQueue() { front = 0; rear = -1; count = 0; }
    void enqueue(int x) {
        if (count == MAX) { cout << "Queue full, cannot add " << x << "\n"; return; }
        rear = (rear + 1) % MAX;                 // step right, wrap 4 -> 0
        a[rear] = x; count++;
        cout << "Added " << x << " at index " << rear << "\n";
    }
    void dequeue() {
        if (count == 0) { cout << "Queue empty\n"; return; }
        cout << "Removed " << a[front] << "\n";
        front = (front + 1) % MAX;               // front wraps the same way
        count--;
    }
    void display() {
        cout << "Queue (front -> rear): ";
        for (int i = 0, k = front; i < count; i++, k = (k + 1) % MAX) cout << a[k] << " ";
        cout << "\n";
    }
};
int main() {
    CQueue q;
    for (int x = 10; x <= 50; x += 10) q.enqueue(x);   // fill all 5
    q.enqueue(60);                                      // full
    q.dequeue(); q.dequeue();                           // free index 0 and 1
    q.enqueue(60); q.enqueue(70);                       // reuse them (wrap)
    q.display();
    return 0;
}
