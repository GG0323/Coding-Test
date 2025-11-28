#include<iostream>
using namespace std;

int main() {
	int tot, book;
	cin >> tot;
	for (int i = 0; i < 9; i++)
	{
		cin >> book;
		tot -= book;
	}
	cout << tot;
}