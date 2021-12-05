#include <stdio.h>
int main()
{
	int a = 5;
	int b = 20;
	int c;

	if (a && b)
	{
		printf("Line 1 - is true\n");
	}
	if (a || b)
	{
		printf("Line 2 - is true\n");
	}
	a = 0;
	b = 10;
	if (a && b)
	{
		printf("Line 3 - is true\n");
	}
	else
	{
		printf("Line 3 - is false\n");
	}
	if (!(a && b))
	{
		printf("Line 4 - if true\n");
	}
}