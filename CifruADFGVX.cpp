#include <iostream>
#include <string>
using namespace std;
int main() {
	srand(time(NULL));
	string ad = " ADFGVX" ;
	char v[] = "ABCDEFGHIJKLMNOQPRSTUVWXYZ1234567890";
    char mat[7][7];
	for (int i = 0; i < 7; i++) {
		mat[i][0] = ad[i];
		mat[0][i] = ad[i];
	}
	int lung = 36;
	for (int i = 1; i < 7; i++) 
		for (int j = 1; j < 7; j++) {
			int index = rand()%lung;
			mat[i][j] = v[index];
			
			v[index] = v[lung-1];
			lung--;
		}
	for (int i = 0; i < 7; i++) {
		for (int j = 0; j < 7; j++) {
			cout << mat[i][j]<<' ';
		}
		cout << endl;
	}
	string p, k, c1, c;
	cout << "p:";
	getline(cin, p);
	cout << "k:";
	getline(cin, k);
	for (int a = 0; a < p.length(); a++) {
		for(int i=1;i<7;i++)
			for (int j = 1; j < 7; j++) {
				if (p[a] == mat[i][j]) {
					c1 += mat[i][0];
					c1 += mat[0][j];
				}
			}
	}
	char mat2[10][15];
	for (int i = 0; i < k.length(); i++) {
		mat2[0][i] = k[i];
	}
	int linii = 0;
	if (c1.length() % k.length() == 0) {
		linii = c1.length() / k.length();
	}
	else linii = c1.length() / k.length() + 1;

	int n = 0;
	for (int i = 1; i < linii + 1; i++)
		for (int j = 0; j < k.length(); j++) {
			mat2[i][j] = ' ';
			mat2[i][j] = c1[n];
			n++;
		}
	for (int i = 1; i < linii + 1; i++) {

		for (int j = 0; j < k.length(); j++)
			cout << (char)mat2[i][j];
		cout << endl;
	}
	cout << endl;
}