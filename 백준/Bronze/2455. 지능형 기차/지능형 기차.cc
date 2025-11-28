#include<iostream>
using namespace std;

int main()
{
	int in, out, max = 0, tot = 0;

	for (int i = 0; i < 4; i++)
	{
		cin >> out >> in;
		tot -= out;
		tot += in;
		max = tot > max ? tot : max;
	}
	cout << max;
}