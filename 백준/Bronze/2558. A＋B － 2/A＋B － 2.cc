#include<iostream>
using namespace std;
int main()
{
	int* num = new int[2];
	for (int i = 0; i < 2; i++)
	{
		cin >> num[i];
	}
	cout << num[0] + num[1];
	delete[]num;
}