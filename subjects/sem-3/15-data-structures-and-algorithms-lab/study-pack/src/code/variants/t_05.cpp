// Exp 5 + 6 assignments. Use with inputMatrix/displayMatrix from Exp 5.
#include "check.h"

// ---- addMatrix ----
// Both matrices must have the SAME order (rows x cols)
void addMatrix(int A[][10], int B[][10], int S[][10], int rows, int cols)
{
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            S[i][j] = A[i][j] + B[i][j];
}
// ---- end ----

// ---- subtractMatrix ----
void subtractMatrix(int A[][10], int B[][10], int D[][10], int rows, int cols)
{
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            D[i][j] = A[i][j] - B[i][j];
}
// ---- end ----

// ---- isSymmetric ----
// Symmetric = square AND A[i][j] == A[j][i] everywhere (A equals its transpose)
bool isSymmetric(int A[][10], int rows, int cols)
{
    if (rows != cols)
        return false;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            if (A[i][j] != A[j][i])
                return false;
    return true;
}
// ---- end ----

int main()
{
    int A[10][10] = {{1, 2, 3}, {4, 5, 6}}, B[10][10] = {{6, 5, 4}, {3, 2, 1}}, R[10][10];
    addMatrix(A, B, R, 2, 3);
    check(R[0][0] == 7 && R[0][2] == 7 && R[1][1] == 7, "addMatrix");
    subtractMatrix(A, B, R, 2, 3);
    check(R[0][0] == -5 && R[1][2] == 5 && R[1][1] == 3, "subtractMatrix");
    int S[10][10] = {{1, 7, 3}, {7, 4, 5}, {3, 5, 6}};
    check(isSymmetric(S, 3, 3), "isSymmetric yes");
    S[0][1] = 8;
    check(!isSymmetric(S, 3, 3), "isSymmetric no");
    check(!isSymmetric(A, 2, 3), "isSymmetric non-square");
    return 0;
}
