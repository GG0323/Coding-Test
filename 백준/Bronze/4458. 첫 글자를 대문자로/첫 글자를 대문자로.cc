#include<iostream>
#include<string>
using namespace std;

int main() {
	int n;
	string str;
	cin >> n;
	cin.ignore();

	for (int i = 0; i < n; i++)
	{
		getline(cin, str);
		str[0] = toupper(str[0]);
		cout << str << '\n';
	}
}