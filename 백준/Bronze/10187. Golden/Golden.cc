#include<iostream>
using namespace std;

int main() {
	double a, b, gold = 1.61803399, scale = 0.01 * gold;

	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> a >> b;
		(a / b >= gold - scale && a / b <= gold + scale) ? cout << "golden\n" : cout << "not\n";
	}
}