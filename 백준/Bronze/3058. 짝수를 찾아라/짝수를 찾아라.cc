#include <iostream>
using namespace std;

int main() {
    int t, n, min, tot;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        min = 100;
        tot = 0;
        for (int j = 0; j < 7; j++)
        {
            cin >> n;
            if (n % 2 == 0)
            {
                min = min < n ? min : n;
                tot += n;
            }
        }
        cout << tot << ' ' << min << '\n';
    }
}