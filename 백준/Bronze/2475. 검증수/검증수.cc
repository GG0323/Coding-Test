#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>

int main(void)
{
	int a, b, c, d, e;
	scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
	printf("%d", (int)(pow(a, 2) + pow(b, 2) + pow(c, 2) + pow(d, 2) + pow(e, 2)) % 10);

	return 0;
}