#include <stdio.h>

int main()
{
	int a = 21;
	int b = 10;
	int c;

	c = a + b;
	printf("the value of line 1 - c is %d\n",c);
	c = a - b;
	printf("the value of line 2 - c is %d\n",c);
	c = a * b;
	printf("the value of line 3 - c is %d\n",c);
	c = a / b;
	printf("the value of line 4 - c is %d\n",c);
	c = a % b;
	printf("the value of line 5 - c is %d\n",c);
	c= a++;
	printf("the value of line 6 - c is %d\n",c);
	c = a--;
	printf("the value of line 7 - c is %d\n",c);

}