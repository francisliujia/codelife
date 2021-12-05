#include <stdio.h>
#include <stdlib.h>

double cube(double num){
	double result = num*num*num;
	return result; //return keyword breaks out the function
	printf("something\n");

}

int main() {

	printf("answer %f\n", cube(10.0) );
	return 0;

}