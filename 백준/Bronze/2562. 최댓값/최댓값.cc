#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int num[9] = { 0 };
	int i=0, max;

	for (int j = 0; j < 9; j++) {
		scanf("%d", &num[j]);
	}

	max = num[0];
	for (int j = 0; j < 9; j++)
	{
		if (max < num[j])
		{
			max = num[j];
			i = j;
		}
	}
	printf("%d\n%d\n", max, i + 1);

	return 0;
}