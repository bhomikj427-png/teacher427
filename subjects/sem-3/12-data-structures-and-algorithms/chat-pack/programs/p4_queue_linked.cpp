#include <iostream>
using namespace std;
struct Node { int data; Node* next; };
class Queue {
    Node *front, *rear;              // front = leaves first, rear = joined last
public:
    Queue() { front = rear = NULL; }
    void insert(int x) {             // enqueue at rear
        Node* t = new Node; t->data = x; t->next = NULL;
        if (rear == NULL) front = rear = t;        // first node is both ends
        else { rear->next = t; rear = t; }         // link after rear, move rear
        cout << x << " inserted\n";
    }
    void remove() {                  // dequeue from front
        if (front == NULL) { cout << "Queue empty (underflow)\n"; return; }
        Node* t = front;
        cout << t->data << " deleted\n";
        front = front->next;                       // move front forward
        if (front == NULL) rear = NULL;            // queue became empty
        delete t;                                  // free the old box
    }
    void display() {
        if (front == NULL) { cout << "Queue empty\n"; return; }
        cout << "Queue: ";
        for (Node* p = front; p != NULL; p = p->next) cout << p->data << " ";
        cout << "\n";
    }
};
int main() {
    Queue q; int ch, x;
    do {
        cout << "1.Insert 2.Delete 3.Display 4.Exit: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Value: "; cin >> x; q.insert(x); break;
            case 2: q.remove(); break;
            case 3: q.display(); break;
        }
    } while (ch != 4);
    return 0;
}
