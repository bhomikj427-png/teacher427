// Exp 11 assignments. Same struct Node and global head as Exp 11
// (insert at end + delete from beginning = the experiment itself).
#include "check.h"

struct Node
{
    int data;
    Node *next;
};
Node *head = NULL;

void insert(int value)                       // Exp 11's insert at end
{
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = NULL;
    if (head == NULL) { head = newNode; return; }
    Node *temp = head;
    while (temp->next != NULL) temp = temp->next;
    temp->next = newNode;
}

string listStr()
{
    string s;
    for (Node *t = head; t != NULL; t = t->next)
        s += to_string(t->data) + (t->next ? " " : "");
    return s;
}

// ---- insertBegin ----
void insertBegin(int value)
{
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = head;                    // new node points to the old first node
    head = newNode;                          // and becomes the first node
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
    if (head->next == NULL)                  // only one node
    {
        cout << head->data << " deleted from list." << endl;
        delete head;
        head = NULL;
        return;
    }
    Node *temp = head;
    while (temp->next->next != NULL)         // stop at the SECOND-last node
        temp = temp->next;
    cout << temp->next->data << " deleted from list." << endl;
    delete temp->next;
    temp->next = NULL;                       // it is now the last node
}
// ---- end ----

// ---- search ----
int search(int key)                          // 1-based position, -1 if absent
{
    int pos = 1;
    Node *temp = head;
    while (temp != NULL)
    {
        if (temp->data == key)
            return pos;
        temp = temp->next;
        pos++;
    }
    return -1;
}
// ---- end ----

// ---- countNodes ----
int countNodes()
{
    int count = 0;
    for (Node *temp = head; temp != NULL; temp = temp->next)
        count++;
    return count;
}
// ---- end ----

// ---- displayReverse ----
// Recursion: first print the REST of the list in reverse, then this node
void displayReverse(Node *p)
{
    if (p == NULL)
        return;
    displayReverse(p->next);
    cout << p->data << " ";
}
// call it as:  displayReverse(head);
// ---- end ----

// ---- insertAtPos ----
void insertAtPos(int pos, int value)         // pos 1 = new first node
{
    if (pos < 1)
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
    for (int i = 1; i < pos - 1 && temp != NULL; i++)   // go to node pos-1
        temp = temp->next;
    if (temp == NULL)
    {
        cout << "Invalid position." << endl;
        return;
    }
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = temp->next;              // 1) new node points ahead
    temp->next = newNode;                    // 2) then link it in (order matters!)
}
// ---- end ----

// ---- deleteAtPos ----
void deleteAtPos(int pos)
{
    if (head == NULL || pos < 1)
    {
        cout << "Invalid position." << endl;
        return;
    }
    Node *del;
    if (pos == 1)
    {
        del = head;
        head = head->next;
    }
    else
    {
        Node *temp = head;
        for (int i = 1; i < pos - 1 && temp != NULL; i++)   // go to node pos-1
            temp = temp->next;
        if (temp == NULL || temp->next == NULL)
        {
            cout << "Invalid position." << endl;
            return;
        }
        del = temp->next;
        temp->next = del->next;              // bypass the node
    }
    cout << del->data << " deleted from list." << endl;
    delete del;
}
// ---- end ----

int main()
{
    insert(10); insert(20); insert(30);
    insertBegin(5);
    check(listStr() == "5 10 20 30", "insertBegin");
    deleteEnd();
    check(listStr() == "5 10 20", "deleteEnd");
    check(search(10) == 2 && search(99) == -1, "search");
    check(countNodes() == 3, "countNodes");
    cout << "reverse: ";
    displayReverse(head);
    cout << endl;
    insertAtPos(2, 7);
    insertAtPos(5, 25);
    insertAtPos(1, 1);
    check(listStr() == "1 5 7 10 20 25", "insertAtPos");
    insertAtPos(9, 0);
    check(countNodes() == 6, "insertAtPos invalid");
    deleteAtPos(3);
    deleteAtPos(1);
    deleteAtPos(4);
    check(listStr() == "5 10 20", "deleteAtPos");
    deleteAtPos(4);
    check(listStr() == "5 10 20", "deleteAtPos invalid");
    deleteEnd(); deleteEnd(); deleteEnd(); deleteEnd();
    check(head == NULL && countNodes() == 0, "deleteEnd to empty");
    return 0;
}
