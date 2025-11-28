#include<iostream>
using namespace std;

int main()
{
	int bg, minb = 2000, sp, mins = 2000;
	for (int i = 0; i < 3; i++)
	{
		cin >> bg;
		if (minb > bg)
			minb = bg;
	}
	for (int i = 0; i < 2; i++)
	{
		cin >> sp;
		if (mins > sp)
			mins = sp;
	}
	cout << minb + mins - 50;
}
