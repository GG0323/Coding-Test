#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void tmp(int *num)
{
	int temp;
	temp = *num;
	*num = *(num + 1);
	*(num + 1) = temp;

}

int main(void)
{
	int num[5], yes = 1;
	
	for (int i = 0; i < 5; i++)
		scanf("%d", &num[i]);

	while(yes)
	{	
		yes = 0;
		for (int i = 0; i < 4; i++)
		{
			if (num[i] > num[i + 1])
			{
				tmp(&num[i]);
				for (int j = 0; j < 5; j++)
					printf("%d ", num[j]);
				puts("");
				yes = 1;
			}
		}
	}

	return 0;
}