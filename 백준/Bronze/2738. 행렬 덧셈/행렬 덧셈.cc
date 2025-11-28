#include<iostream>
using namespace std;

int main()
{
	int n1, n2;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n1 >> n2;

	int** num1 = new int* [n1];
	int** num2 = new int* [n1];

	for (int i = 0; i < n1; i++)
		num1[i] = new int[n2];

	for (int i = 0; i < n1; i++)
		num2[i] = new int[n2];

	for (int i = 0; i < n1; i++)
	{
		for (int j = 0; j < n2; j++)
			cin >> num1[i][j];
	}

	for (int i = 0; i < n1; i++)
	{
		for (int j = 0; j < n2; j++)
			cin >> num2[i][j];
	}

	for (int i = 0; i < n1; i++)	
	{
		for (int j = 0; j < n2; j++)
		{
			num1[i][j] += num2[i][j];
			cout << num1[i][j]<<' ';
		}
		cout << '\n';
	}

	for (int i = 0; i < n1; i++)
	{
		delete[] num1[i];
		delete[] num2[i];
	}

	delete[] num1;
	delete[] num2;
}