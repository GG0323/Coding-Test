#include<iostream>
using namespace std;

int main()
{
	int hour, minute, time;
	cin >> hour >> minute >> time;
	minute += time;
	if (minute >= 60)
	{
		hour += minute / 60;
		minute %= 60;
	}
	if (hour >= 24)
		hour -= 24;
	cout << hour << ' ' << minute;
}