#include<iostream>
using namespace std;

int main()
{
	int x, y, z, tot, result = 0, max, n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		tot = 0;
		cin >> x >> y >> z;
		if (x == y && y == z)
			tot = x * 1000 + 10000;
		else if (x == y || x == z || y == z)
		{
			if (x == y || x == z)
				tot = x * 100 + 1000;
			else
				tot = y * 100 + 1000;
		}
		else
		{
			if (x >= y && x >= z)
				max = x;
			else if (y >= x && y >= z)
				max = y;
			else
				max = z;
			tot = max * 100;
		}
		result = tot > result ? tot : result;
	}
	cout << result;
}