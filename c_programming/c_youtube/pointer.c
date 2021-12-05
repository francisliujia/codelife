#include <stdio.h>
#include <stdlib.h>

int main()
{
	int age = 30;
	int * pAge = &age;
	double gpa = 5.0;
	double * pGpa = &gpa;
	char grade = 'A';
	char * pGrade = &grade;


	printf("age's memory address: %p", &age);
	
	return 0;
}