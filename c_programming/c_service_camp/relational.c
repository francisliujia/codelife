# include <stdio.h>

int main()
{
	int a = 21;
	int b = 10;
	int c;

	if (a == b)
	{
		printf("Line 1 - a is equal to b\n");
	}
	else
	{
		printf("Line 1 - a is not equal to b\n");
	}
	if (a < b)
	{
		printf("Line 2 - a is less than b\n");
	}
	else
	{
		printf("Line 2 -a is not less than b\n");
	}
	if (a > b)
	{
		printf("Line 3 -a is greater than b\n");
	}
	else
	{
		printf("Line 3- a is not greater than b\n");
	}
	a = 5;
	b = 20;
	if (a <= b)
	{
		printf("Line 4 -a is less or equal to b\n");
	}
	if (b >= a)
	{
		printf("Line 5 -a is greater or equal to a\n");
	}

}







