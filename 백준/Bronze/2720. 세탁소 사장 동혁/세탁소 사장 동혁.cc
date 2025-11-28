#include<iostream>
using namespace std;

int main()
{
	int T, C;
	int qdnp[] = { 25,10,5,1 };
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> C;
		for (int j = 0; j < 4; j++)
		{
			cout << C / qdnp[j] << ' ';
			C %= qdnp[j];
		}
		cout << '\n';
	}
}