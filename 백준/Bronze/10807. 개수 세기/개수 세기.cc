#include<iostream>
using namespace std;

int main(void)
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int n, v, count = 0;
	cin >> n;
	int* p = new int[n];
	for (int i = 0; i < n; i++) cin >> *(p + i);
	cin >> v;
	for (int i = 0; i < n; i++)
	{
		if (*(p + i) == v)
			count++;
	}
	cout << count;
	delete[]p;
}