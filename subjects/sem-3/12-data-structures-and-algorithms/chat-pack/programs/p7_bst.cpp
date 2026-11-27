#include <iostream>
using namespace std;
struct Node { int data; Node *left, *right; };
Node* insert(Node* r, int x) {
    if (r == NULL) { r = new Node; r->data = x; r->left = r->right = NULL; return r; }
    if (x < r->data) r->left = insert(r->left, x);     // smaller goes left
    else r->right = insert(r->right, x);               // bigger goes right
    return r;
}
void preorder(Node* r)  { if (r) { cout << r->data << " "; preorder(r->left); preorder(r->right); } }
void inorder(Node* r)   { if (r) { inorder(r->left); cout << r->data << " "; inorder(r->right); } }
void postorder(Node* r) { if (r) { postorder(r->left); postorder(r->right); cout << r->data << " "; } }
int main() {
    int a[] = {45, 36, 76, 23, 89, 115, 98, 39, 41, 56, 69, 48};
    Node* root = NULL;
    for (int i = 0; i < 12; i++) root = insert(root, a[i]);
    cout << "Preorder:  "; preorder(root);  cout << "\n";
    cout << "Inorder:   "; inorder(root);   cout << "\n";
    cout << "Postorder: "; postorder(root); cout << "\n";
    return 0;
}
