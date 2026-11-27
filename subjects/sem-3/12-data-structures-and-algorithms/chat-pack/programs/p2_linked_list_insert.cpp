#include <iostream>
using namespace std;
struct Node {                         // one box: data + arrow to the next box
    int data;
    Node* next;
};
Node* head = NULL;                    // arrow to the first box (NULL = empty list)
void insertBegin(int x) {
    Node* t = new Node;               // make a new box
    t->data = x;
    t->next = head;                   // new box points to old first box
    head = t;                         // head now points to new box
}
void insertEnd(int x) {
    Node* t = new Node;
    t->data = x; t->next = NULL;      // last box points to nothing
    if (head == NULL) { head = t; return; }
    Node* p = head;
    while (p->next != NULL) p = p->next;   // walk to the last box
    p->next = t;                      // old last box points to new box
}
void insertAfter(int key, int x) {
    Node* p = head;
    while (p != NULL && p->data != key) p = p->next;   // find the box holding key
    if (p == NULL) { cout << key << " not found\n"; return; }
    Node* t = new Node;
    t->data = x;
    t->next = p->next;                // FIRST: new box points to p's old next
    p->next = t;                      // THEN: p points to new box
}
void display() {
    for (Node* p = head; p != NULL; p = p->next) cout << p->data << " -> ";
    cout << "NULL\n";
}
int main() {
    insertEnd(12); insertEnd(24); insertEnd(36); insertEnd(48); insertEnd(60);
    display();
    insertBegin(6);       display();
    insertAfter(36, 42);  display();
    insertEnd(72);        display();
    return 0;
}
