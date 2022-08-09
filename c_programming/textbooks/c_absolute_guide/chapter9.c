#include <stdio.h>
int main(){

	float a = 19.0;
	float b = 5.0;
	float floatAnswer;
	int x = 29;
	int y = 5;
	int intAnswer;

	floatAnswer = a/b;
	printf("%f divided by %f equals %f\n", a, b, floatAnswer);
	floatAnswer = x/y;
	printf("%d divided by %d equals %d\n", x, y, intAnswer);

	intAnswer = a/b;
	printf("%f divided by %f equals %d\n",a,b,intAnswer);
	intAnswer = x%y;
	printf("%d modules (i.e. remainder of) %d equals %d \n" ,x,y,intAnswer);



	return 0;
}