#include<iostream>
#include<string>
using namespace std;

int main()
{
	int T;
	double num;
	string ch;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> num >> ch;
		if (ch == "kg")
			printf("%.4f lb\n", num * 2.2046);
		else if (ch == "lb")
			printf("%.4f kg\n", num * 0.4536);
		else if (ch == "l")
			printf("%.4f g\n", num * 0.2642);
		else if (ch == "g")
			printf("%.4f l\n", num * 3.7854);
	}
}