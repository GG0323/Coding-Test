#include<iostream>
using namespace std;

int main()
{
	int n, num, tmp = 0, tot = 0, count = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		if (num > 0 && tmp == num)
			count++;
		else count = 0;
		tot += num + count;
		tmp = num;
	}
	cout << tot;
}