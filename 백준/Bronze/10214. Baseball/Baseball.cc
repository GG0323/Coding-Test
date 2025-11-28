#include<iostream>
using namespace std;

int main() {
	int T, Y[2], K[2];
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		Y[1] = 0;
		K[1] = 0;
		for (int j = 0; j < 9; j++)
		{
			cin >> Y[0] >> K[0];
			Y[1] += Y[0];
			K[1] += K[0];
		}

		if (Y[1] > K[1])
			cout << "Yonsei\n";
		else if (Y[1] < K[1])
			cout << "Korea\n";
		else
			cout << "Draw\n";
	}
}