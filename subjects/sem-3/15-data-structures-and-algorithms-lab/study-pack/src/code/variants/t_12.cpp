// Exp 12 assignments. Same struct Node and global head as Exp 12.
// Rule for every function: the last node is the one whose next == head.
#include "check.h"

struct Node
{
    int data;
    Node *next;
};
Node *head = NULL;

void insert(int value)                       // Exp 12's insert at end
{
    Node *newNode = new Node;
    newNode->data = value;
    if (head == NULL) { head = newNode; newNode->next = head; return; }
    Node *temp = head;
    while (temp->next != head) temp = temp->next;
    temp->next = newNode;
    newNode->next = head;
}

string listStr()
{
    if (head == NULL) return "";
    string s;
    Node *t = head;
    do { s += to_string(t->data) + (t->next != head ? " " : ""); t = t->next; } while (t != head);
    return s;
}

bool isCircular()                            // test: walking n steps returns to head
{
    if (head == NULL) return true;
    Node *t = head;
    for (int i = 0; i < 1000; i++) { t = t->next; if (t == head) return true; }
    return false;
}

// ---- insertBegin ----
// Like insert at end, but afterwards head moves to the new node
void insertBegin(int value)
{
    Node *newNode = new Node;
    newNode->data = value;
    if (head == NULL)
    {
        head = newNode;
        newNode->next = head;
        return;
    }
    Node *last = head;
    while (last->next != head)               // the last node must point to the new first node
        last = last->next;
    newNode->next = head;
    last->next = newNode;
    head = newNode;
}
// ---- end ----

// ---- deleteEnd ----
void deleteEnd()
{
    if (head == NULL)
    {
        cout << "List is empty." << endl;
        return;
    }
    if (head->next == head)                  // only one node
    {
        cout << head->data << " deleted from list." << endl;
        delete head;
        head = NULL;
        return;
    }
    Node *temp = head;
    while (temp->next->next != head)         // stop at the second-last node
        temp = temp->next;
    cout << temp->next->data << " deleted from list." << endl;
    delete temp->next;
    temp->next = head;                       // new last node closes the circle
}
// ---- end ----

// ---- search ----
int search(int key)                          // 1-based position, -1 if absent
{
    if (head == NULL)
        return -1;
    Node *temp = head;
    int pos = 1;
    do
    {
        if (temp->data == key)
            return pos;
        temp = temp->next;
        pos++;
    } while (temp != head);
    return -1;
}
// ---- end ----

// ---- countNodes ----
int countNodes()
{
    if (head == NULL)
        return 0;
    int count = 0;
    Node *temp = head;
    do
    {
        count++;
        temp = temp->next;
    } while (temp != head);
    return count;
}
// ---- end ----

// ---- displayReverse ----
// Recursion that stops when it comes back round to head
void reverseFrom(Node *p)
{
    if (p->next != head)
        reverseFrom(p->next);
    cout << p->data << " ";
}

void displayReverse()
{
    if (head == NULL)
        cout << "List is empty.";
    else
        reverseFrom(head);
    cout << endl;
}
// ---- end ----

// ---- insertAtPos ----
void insertAtPos(int pos, int value)         // pos 1 = new first node
{
    int n = countNodes();
    if (pos < 1 || pos > n + 1)
    {
        cout << "Invalid position." << endl;
        return;
    }
    if (pos == 1)
    {
        insertBegin(value);
        return;
    }
    Node *temp = head;
    for (int i = 1; i < pos - 1; i++)        // go to node pos-1
        temp = temp->next;
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = temp->next;              // for pos = n+1 this is head: circle stays closed
    temp->next = newNode;
}
// ---- end ----

// ---- deleteAtPos ----
void deleteAtPos(int pos)
{
    int n = countNodes();
    if (pos < 1 || pos > n)
    {
        cout << "Invalid position." << endl;
        return;
    }
    if (pos == 1)                            // same as Exp 12's deleteNode()
    {
        Node *last = head;
        while (last->next != head)
            last = last->next;
        Node *del = head;
        cout << del->data << " deleted from list." << endl;
        if (n == 1)
            head = NULL;
        else
        {
            head = head->next;
            last->next = head;
        }
        delete del;
        return;
    }
    Node *temp = head;
    for (int i = 1; i < pos - 1; i++)
        temp = temp->next;
    Node *del = temp->next;
    temp->next = del->next;
    cout << del->data << " deleted from list." << endl;
    delete del;
}
// ---- end ----

int main()
{
    insert(10); insert(20); insert(30);
    insertBegin(5);
    check(listStr() == "5 10 20 30" && isCircular(), "insertBegin");
    deleteEnd();
    check(listStr() == "5 10 20" && isCircular(), "deleteEnd");
    check(search(20) == 3 && search(99) == -1, "search");
    check(countNodes() == 3, "countNodes");
    displayReverse();
    insertAtPos(2, 7);
    insertAtPos(5, 25);
    insertAtPos(1, 1);
    check(listStr() == "1 5 7 10 20 25" && isCircular(), "insertAtPos");
    insertAtPos(9, 0);
    check(countNodes() == 6, "insertAtPos invalid");
    deleteAtPos(3);
    deleteAtPos(1);
    deleteAtPos(4);
    check(listStr() == "5 10 20" && isCircular(), "deleteAtPos");
    deleteAtPos(1); deleteAtPos(1); deleteAtPos(1);
    check(head == NULL && countNodes() == 0, "deleteAtPos to empty");
    insertBegin(42);
    check(listStr() == "42" && head->next == head, "insertBegin on empty");
    deleteEnd();
    check(head == NULL, "deleteEnd single");
    return 0;
}
