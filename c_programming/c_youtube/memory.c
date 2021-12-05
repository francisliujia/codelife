#include <stdio.h>
#include <stdlib.h>

int main()
{

	int age1 = 30;
	int age2 = 30;
	double gpa = 4.5;
	char grade = 'A';

	printf("age1:%p\nage2:%p\ngpa:%p\ngrade:%p",&age1,&age2, &gpa, &grade);
	
	return 0;
}