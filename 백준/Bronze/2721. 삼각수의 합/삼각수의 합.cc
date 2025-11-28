#include<iostream>
using namespace std;

int main() {
	int t, n, result;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		result = 0;
		cin >> n;
		for (int j = 1; j <= n; j++)
		{
			result += j * ((j + 1) * (j + 2) / 2);
		}
		cout << result << "\n";
	}
}