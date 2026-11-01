// Test helper for the assignment drivers (not shown in the pack).
#include <iostream>
#include <string>
using namespace std;

inline void check(bool ok, const string &what)
{
    cout << (ok ? "PASS " : "FAIL ") << what << endl;
}

inline string arrStr(const int a[], int n)
{
    string s;
    for (int i = 0; i < n; i++)
        s += to_string(a[i]) + (i < n - 1 ? " " : "");
    return s;
}
