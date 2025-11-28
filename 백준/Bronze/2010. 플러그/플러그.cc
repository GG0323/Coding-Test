#include<iostream>
using namespace std;

int main() {
	int n, result = 0;
	cin >> n;
	int* p = new int[n];

	cin >> p[0];
	result += p[0];

	for (int i = 1; i < n; i++)
	{
		cin >> p[i];
		result += p[i] - 1;
	}

	cout << result;

	delete[]p;
}