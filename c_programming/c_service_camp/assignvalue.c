#include <stdio.h>
int main()
{
	int a = 21;
	int c ;
	c = a;
	printf("Line 1 - id equal to c = %d\n",c);

	c += a;
	printf("Line 2 - += is equal to c, = %d\n",c);

	c -= a;
	printf("Line 3 - -= id is %d\n",c );

	c *= a;
	printf("Line 4 - *= is %d\n",c);
	c /= a;
	printf("Line 5 - /= id %d\n",c);
	c = 200;
	c %= a;
	printf("Line 6 - operatation is %d\n",c);
}