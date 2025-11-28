#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	int a, b, c, d, l;
	cin >> l >> a >> b >> c >> d;
	int Kavg = a / c + (a % c != 0), Mavg = b / d + (b % d != 0);
	cout << l - max(Kavg, Mavg);
}
