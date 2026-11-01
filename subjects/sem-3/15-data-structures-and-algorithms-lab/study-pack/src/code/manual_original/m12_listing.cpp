// Exp 12 as printed in the PROGRAM listing (main completed from the screenshot, menu lines as printed).
#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node* next;
};

Node* head = NULL;

void insert(intvalue)
{
    Node* newNode = new Node;
    newNode->data = value;
    if(head == NULL)
    {
        head = newNode;
        newNode->next = head;
    }
    else
    {   Node* temp = head;
        while(temp->next != head)
        {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = head;
    }
    cout << value << " inserted into list." << endl;
}

void deleteNode()
{
    if(head == NULL)
    {
        cout << "List is empty." << endl;
    }
    else if(head->next == head)
    {   cout << head->data << " deleted from list." << endl;
        delete head;
        head = NULL;
    }
    else
    {   Node* temp = head;
        Node* last = head;
        while(last->next != head)
        {
            last = last->next;
        }
        cout << head->data << " deleted from list." << endl;
        head = head->next;
        last->next = head;
    }   delete temp;
}

int main()
{
    int choice, value;
    do
    {   cout << "\n1. Insert
        cout << "\n2. Delete
        cout << "\n3. Traverse
        cout << "\n4. Exit
        cout << "Enter your choice: ";
        cin >> choice;
        if(choice == 1)
        {   cin >> value;
            insert(value);
        }
        else if(choice == 2)
            deleteNode();
    } while(choice != 4);
    return 0;
}
