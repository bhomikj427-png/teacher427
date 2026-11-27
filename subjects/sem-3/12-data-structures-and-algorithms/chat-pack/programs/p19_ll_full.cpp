// A1 B1 + A1 D2: singly linked list - insert begin/end, delete, search, display, sort by swapping data
#include <iostream>
using namespace std;
struct Node {
    int data;
    Node *next;
};
Node *head = NULL;
void insertBegin(int x) {
    Node *n = new Node; n->data = x;
    n->next = head;                              // new box points at the old first box
    head = n;                                    // head now points at the new box
}
void insertEnd(int x) {
    Node *n = new Node; n->data = x; n->next = NULL;
    if (head == NULL) { head = n; return; }      // empty list: it becomes the head
    Node *p = head;
    while (p->next != NULL) p = p->next;         // walk to the last box
    p->next = n;                                 // hook the new box on
}
void deleteValue(int x) {
    if (head == NULL) { cout << "List empty\n"; return; }
    if (head->data == x) {                       // deleting the first box
        Node *t = head; head = head->next; delete t;
        cout << "Deleted " << x << "\n"; return;
    }
    Node *p = head;
    while (p->next != NULL && p->next->data != x) p = p->next;   // stop one box BEFORE it
    if (p->next == NULL) { cout << x << " not found\n"; return; }
    Node *t = p->next;
    p->next = t->next;                           // bypass the box
    delete t;                                    // free its memory
    cout << "Deleted " << x << "\n";
}
void search(int x) {
    int pos = 1;
    for (Node *p = head; p != NULL; p = p->next, pos++)
        if (p->data == x) { cout << x << " found at position " << pos << "\n"; return; }
    cout << x << " not found\n";
}
void display() {
    for (Node *p = head; p != NULL; p = p->next) cout << p->data << " -> ";
    cout << "NULL\n";
}
void sortList() {                                // swap DATA, not links
    for (Node *p = head; p != NULL; p = p->next)
        for (Node *q = p->next; q != NULL; q = q->next)
            if (p->data > q->data) { int t = p->data; p->data = q->data; q->data = t; }
}
int main() {
    int n, x;
    cout << "How many nodes? "; cin >> n;
    cout << "Enter " << n << " values: ";
    for (int i = 0; i < n; i++) { cin >> x; insertEnd(x); }
    cout << "\nList: "; display();
    insertBegin(5); cout << "After insertBegin(5): "; display();
    deleteValue(30); cout << "List: "; display();
    search(40);
    sortList(); cout << "Sorted: "; display();
    return 0;
}
