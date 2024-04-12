// AlgoritmCezar.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;
string criptare(string p, int k) {
	string c;
	for (int i = 0; i < p.length(); i++) {
		if (p[i] <= 'z' && p[i] >= 'a')
			c += (p[i] + k - 'a') % 26 + 'a';
		else if (p[i] < 'Z' && p[i]>'A')
			c += (p[i] + k - 'A') % 26 + 'A';
		else c += p[i];
	}
	return c;
}
string decriptare(string c, int k) {
	string d;
	for (int i = 0; i < c.length(); i++)
		if (c[i] <= 'z' && c[i] >= 'a')
			d += (c[i] - k - 'a' + 26) % 26 + 'a';
		else if (c[i] < 'Z' && c[i]>'A')
			d += (c[i] - k - 'A' + 26) % 26 + 'A';
		else d += c[i];
	return d;
}

int main()
{
	int k;
	string p,c,d;
		getline(cin,p);cin >> k;
		cout << p <<' '<< k;
	//criptare
		c = criptare(p, k);
		cout << c<<endl;
	//decriptare
		d = decriptare(c, k);
		cout << d;
	return 0;

}


