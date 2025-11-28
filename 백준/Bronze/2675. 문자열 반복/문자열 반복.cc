#include<iostream>
#include<string>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{	
		string p;
		int t;
		cin >> t >> p;
		for (int i = 0; i < p.size(); i++)
		{
			for (int j=0;j<t;j++) cout << p[i];
		}
		cout << '\n';
	}
}
