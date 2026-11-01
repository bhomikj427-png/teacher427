// Exp 10 assignments. The array-queue ones use the globals of Exp 10 (queueArr, front, rear, MAX).
#include "check.h"

#define MAX 5
int queueArr[MAX];
int front = -1, rear = -1;

void enqueue(int value)
{
    if (rear == MAX - 1) { cout << "Queue Overflow!" << endl; return; }
    if (front == -1) front = 0;
    queueArr[++rear] = value;
}

// ---- peek ----
void peek()
{
    if (front == -1)
        cout << "Queue is empty." << endl;
    else
        cout << "Front element is " << queueArr[front] << endl;   // look, don't remove
}
// ---- end ----

// ---- emptyFull ----
bool isEmpty() { return front == -1; }
bool isFull()  { return rear == MAX - 1; }
// ---- end ----

// ---- frontRear ----
void showFrontRear()
{
    if (front == -1)
        cout << "Queue is empty." << endl;
    else
        cout << "Front = " << queueArr[front] << ", Rear = " << queueArr[rear] << endl;
}
// ---- end ----

// ---- reverseQueue ----
// Reverse the elements between front and rear: swap the two ends, move inwards
void reverseQueue()
{
    if (front == -1)
        return;
    int i = front, j = rear;
    while (i < j)
    {
        int temp = queueArr[i];
        queueArr[i] = queueArr[j];
        queueArr[j] = temp;
        i++;
        j--;
    }
}
// ---- end ----

// ---- linkedQueue ----
// Queue using a linked list: no fixed size, so no overflow.
// Enqueue at the rear end of the list, dequeue from the front end.
struct QNode
{
    int data;
    QNode *next;
};
QNode *qFront = NULL, *qRear = NULL;

void enqueueLL(int value)
{
    QNode *newNode = new QNode;
    newNode->data = value;
    newNode->next = NULL;
    if (qRear == NULL)                       // empty queue
        qFront = qRear = newNode;
    else
    {
        qRear->next = newNode;
        qRear = newNode;
    }
}

int dequeueLL()                              // returns -1 if empty
{
    if (qFront == NULL)
    {
        cout << "Queue Underflow!" << endl;
        return -1;
    }
    QNode *temp = qFront;
    int value = temp->data;
    qFront = qFront->next;
    if (qFront == NULL)                      // queue became empty
        qRear = NULL;
    delete temp;
    return value;
}
// ---- end ----

// ---- fcfs ----
// CPU scheduling (First Come First Served): processes wait in a queue in arrival order.
// Waiting time of a process = sum of burst times of everyone before it.
float fcfs(int burst[], int n)
{
    int waiting = 0, totalWait = 0;
    cout << "Process\tBurst\tWaiting\tTurnaround" << endl;     // \t = tab
    for (int i = 0; i < n; i++)              // dequeue in FIFO order
    {
        int turnaround = waiting + burst[i];
        cout << "P" << i + 1 << "\t" << burst[i] << "\t" << waiting << "\t" << turnaround << endl;
        totalWait += waiting;
        waiting += burst[i];
    }
    cout << "Average waiting time = " << (float)totalWait / n << endl;
    return (float)totalWait / n;
}
// ---- end ----

int main()
{
    check(isEmpty() && !isFull(), "empty at start");
    enqueue(10); enqueue(20); enqueue(30);
    peek();
    showFrontRear();
    check(queueArr[front] == 10 && queueArr[rear] == 30, "front/rear");
    reverseQueue();
    check(arrStr(queueArr, 3) == "30 20 10", "reverseQueue");
    enqueue(40); enqueue(50);
    check(isFull(), "isFull");

    enqueueLL(1); enqueueLL(2); enqueueLL(3);
    int a = dequeueLL(), b = dequeueLL();
    enqueueLL(4);
    int c = dequeueLL(), d = dequeueLL();
    check(a == 1 && b == 2 && c == 3 && d == 4 && qFront == NULL && qRear == NULL, "linked queue FIFO");
    check(dequeueLL() == -1, "linked queue underflow");

    int burst[] = {24, 3, 3};
    check(fcfs(burst, 3) == 17.0f, "fcfs average waiting time (0+24+27)/3 = 17");
    return 0;
}
