#include<iostream>
using namespace std;

int main()
{
	int max = 0, r, c, num;
	for (int i = 1; i < 10; i++)
	{
		for (int j = 1; j < 10; j++)
		{
			cin >> num;
			if (max <= num)
			{
				max = num;
				r = i;
				c = j;
			}
		}
	}
	cout << max << '\n' << r << ' ' << c;
}