#include <iostream>
using namespace std;
struct Node { int data; Node* next; };
Node* head = NULL;
void insertEnd(int x) {
    Node* t = new Node; t->data = x; t->next = NULL;
    if (!head) { head = t; return; }
    Node* p = head; while (p->next) p = p->next; p->next = t;
}
void display() { for (Node* p = head; p; p = p->next) cout << p->data << " -> "; cout << "NULL\n"; }
void reverse() {
    Node *prev = NULL, *curr = head, *nxt;
    while (curr != NULL) {
        nxt = curr->next;      // 1. save the rest of the list
        curr->next = prev;     // 2. flip this arrow backwards
        prev = curr;           // 3. step prev forward
        curr = nxt;            // 4. step curr forward
    }
    head = prev;               // last box is the new first box
}
int main() {
    insertEnd(10); insertEnd(20); insertEnd(30); insertEnd(40);
    display(); reverse(); display();
    return 0;
}
