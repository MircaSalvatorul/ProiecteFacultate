// ProiectCripto.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

/* dupa o criptare prin playfair, dar si una prin adfgvx, voi transforma cheia intr-un vector de coordonate,
* shiftand fiecare litera din a cu indicele din vectorul cheii.
*/

#include <iostream>
#include <string>

using namespace std;

string ad = " adfgvx";

char v[] = "abcdefghijklmnoqprstuvwxyz1234567890";
char mat[7][7];
string p1, c1, c2, d, d1, d2, p, k, c;

int k1[100]{};

struct index {
	int x, y;
};

void table() {
	for (int i = 0; i < 7; i++) {
		mat[i][0] = ad[i];
		mat[0][i] = ad[i];
	}
	int lung = 36;
	for (int i = 1; i < 7; i++)
		for (int j = 1; j < 7; j++) {
			int index = rand() % lung;
			mat[i][j] = v[index];

			v[index] = v[lung - 1];
			lung--;
		}
	for (int i = 0; i < 7; i++) {
		for (int j = 0; j < 7; j++) {
			cout << mat[i][j] << ' ';
		}
		cout << endl;
	}
}
	void convert(string s)
	{
		int i, j = 0, f = 0;
		for (i = 0; i < s.size(); i++){
			if ((s[i] > 47 && s[i] < 58) || (s[i] > 96 && s[i] < 123)){
				if ((i + f) % 2 != 0 && p1[j - 1] == s[i]){
					p1 += 'x';
				}
				else{
					p1 += s[i];
				}
				j++;
			}
			else{
				f++;
			}
		}
		if (j % 2 != 0){
			p1 += 'x';
			j++;
		}
	}

struct index findIndex(char ch)
{
	int i, j;
	struct index f {};
	for (i = 1; i < 7; i++){
		for (j = 1; j < 7; j++){
			if (mat[i][j] == ch){
				f.x = i;
				f.y = j;
				i = 6;
				j = 6;
			}
		}
	}
	return f;
}
void pf()
{
	int i, ax, ay, bx, by;
	struct index f;
	for (i = 0; i < p1.length(); i = i + 2){
		f = findIndex(p1[i]);
		ax = f.x;
		ay = f.y;
		f = findIndex(p1[i + 1]);
		bx = f.x;
		by = f.y;
		if (ax == bx){
			if (by + 1 > 6){
				c1 += mat[ax][1];
			}
			else{
				c1 += mat[ax][(by + 1) % 7];
			}
			if (ay + 1 >6){
				c1 += mat[ax][1];
			}
			else{
				c1 += mat[ax][(ay + 1) % 7];
			}
		}
		else if (ay == by){
			if (bx + 1 > 6){
				c1 += mat[1][by];
			}
			else{
				c1 += mat[(bx + 1) % 7][by];
			}
			if (ax +1>6){
				c1 += mat[1][ay];
			}
			else{
				c1 += mat[(ax + 1) % 7][ay];
			}
		}
		else{
			c1 += mat[ax][by];
			c1 += mat[bx][ay];
		}
		cout << c1[i] << c1[i + 1];
	}
}
void dpf()
{
	int i, ax, ay, bx, by;
	struct index f;
	for (i = 0; i < d1.length(); i = i + 2){
		f = findIndex(d1[i]);
		ax = f.x;
		ay = f.y;
		f = findIndex(d1[i + 1]);
		bx = f.x;
		by = f.y;
		if (ax == bx){
			if (by - 1 == 0){
				d2 += mat[ax][6];
			}
			else{
				d2+= mat[ax][(by - 1) % 7];
			}
			if (ay - 1 == 0){
				d2+= mat[ax][6];
			}
			else{
				d2 += mat[ax][(ay - 1) % 7];
			}
		}
		else if (ay == by){
			if (bx - 1 == 0){
				d2 += mat[6][by];
			}
			else{
				d2 += mat[(bx - 1) % 7][by];
			}
			if (ax - 1 == 0){
				d2 += mat[6][ay];
			}
			else{
				d2 += mat[(ax - 1) % 7][ay];
			}
		}
		else{
			d2 += mat[ax][by];
			d2 += mat[bx][ay];
		}
		cout << d2[i] << d2[i + 1];
	}
}

void adf() {
	for (int a = 0; a < c1.length(); a++) {
		for (int i = 1; i < 7; i++)
			for (int j = 1; j < 7; j++) {
				if (c1[a] == mat[i][j]) {
					c2 += mat[i][0];
					c2 += mat[0][j];
				}
			}
	}
	cout << c2;
}
void encrypt() {
	int n = 0;
	for (int a = 0; a < k.length(); a++)
		for (int i = 1; i < 7; i++)
			for (int j = 1; j < 7; j++)
				if (k[a] == mat[i][j]) {
					k1[n] = i;
					k1[n + 1] = j;
					n = n + 2;
				}

	p1 = c2;
	n = 0;
	for (int i = 0; i < p1.length(); i++)
		for (int j = 1; j < 7; j++)
			if (p1[i] == mat[0][j]) {
				c += mat[0][(j + k1[n]) % 7];
				n++;
			}
}
void decrypt() {
	int n = 0;
	for (int i = 0; i < c.length(); i++)
		for (int j = 0; j < 7; j++)
			if (c[i] == mat[0][j]) {
				d += mat[0][(j - k1[n] + 7) % 7];
				n++;
			}
	for (int a = 0; a < d.length(); a = a + 2) {
		int l, c;
		for (int i = 1; i < 7; i++)
			if (d[a] == mat[i][0])
				l = i;
		for (int i = 1; i < 7; i++)
			if (d[a + 1] == mat[0][i])
				c = i;
		d1 += mat[l][c];
	}
}

int main()
{
	
	srand(time(NULL));
	table();
	cout << "p:";
	getline(cin, p);
	cout << "k:";
	getline(cin, k);
	convert(p);
	if (p1.length() != k.length()) {
		cout << "lungimea cheii trebuie sa fie egala cu lungimea textului, introdu din nou cheia: ";
		getline(cin, k);
	}
	cout << "Textul dupa criptare prin playfair: ";
	pf();
	cout << endl;
	cout << "Textul dupa criptare prin ADFGVX: ";
	adf();
//si acum partea amuzanta...at this point vreau sa iau fiecare litera din k, ii gasesc i si j si adaug asta la p. yes thats what ill do
	encrypt();
	cout << endl<< "textul final: ";
	cout << c;
//FAEN FINALLY acum decriptarea... la care nu am nicio idee la ora 12 30 pe 26
	decrypt();
	cout << endl << "Decriptare dupa adfgvx:";
	cout << d1<<endl;
	cout << "decriptarea finala: ";
	dpf();
	//TERMINAT LA 1 43 YAHOOO. 20 MINUTES LEFT WHO??
	//NEVERMIND ULTIMA DECRIPTARE NU E BUNA
	//deci este problema ca atunci cand scrie pe linie mi le scrie invers. to be resolved
}