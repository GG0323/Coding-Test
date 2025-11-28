#include<iostream>
using namespace std;

int main()
{
	int H, M;
	cin >> H >> M;
	M -= 45;
	if (M < 0)
	{
		if (H == 0)
			H = 23;
		else
			H--;
		M += 60;
	}
	cout << H << ' ' << M;
}