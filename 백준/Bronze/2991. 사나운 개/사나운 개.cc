#include <iostream>
using namespace std;
int main() {
    int a, b, c, d, pmn[3], tmp1, tmp2;
    int result[3] = { 0 };

    cin >> a >> b >> c >> d;

    for (int i = 0; i < 3; i++)
    {
        cin >> pmn[i];
        tmp1 = pmn[i] % (a + b);
        tmp2 = pmn[i] % (c + d);
        if (tmp1 <= a && tmp1 != 0) result[i]++;
        if (tmp2 <= c && tmp2 != 0) result[i]++;
    }

    for (int i = 0; i < 3; i++)
        cout << result[i] << '\n';
}