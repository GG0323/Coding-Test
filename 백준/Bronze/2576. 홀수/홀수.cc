#include<iostream>
using namespace std;

int main()
{
	int num, tot = 0, min = 100, count = 0;
	for (int i = 0; i < 7; i++)
	{
		cin >> num;
		if (num % 2 != 0)
		{
			tot += num;
			min = num < min ? num : min;
			count++;
		}
	}
	if (count > 0)
		cout << tot << '\n' << min;
	else
		cout << -1;
}