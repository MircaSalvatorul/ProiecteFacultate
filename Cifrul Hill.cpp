// Cifrul Hill.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
const int lung=26;
using namespace std;

typedef struct {
    int matrix[2][2], v[2];

}cheie;

int determinant(int matrix[][2]) {

    return ((matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1]));
}

int cmmdc(int a) {
    int b = lung;
    while (a != b) {
        if (a > b) { a = a - b; }
        else b = b - a;
    }
    return a;
}

int criptare(cheie k, string p) {
    int d = determinant(k.matrix);

}


int main()
{
    string mes;
    cheie k;
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            cin >> k.matrix[i][j];
    for (int i = 0; i < 2; i++)
        cin >> k.v[i];
   
    //criptare

}
