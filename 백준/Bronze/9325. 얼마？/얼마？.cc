#include<iostream>
#include<string>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T, s, n, op, price, tot;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cin >> s >> n;
		tot = 0;
		for (int j = 0; j < n; j++)
		{
			cin >> op >> price;
			tot += op * price;
		}
		cout << s + tot << '\n';
	}

}