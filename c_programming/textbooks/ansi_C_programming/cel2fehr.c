#include "stdio.h"

int main(){
	float fahr, celsius;
	int lower, upper, step;

	lower = -30;
	upper = 300;
	step = 10;

	printf("celsius to Fahrenheit Table\n");
	celsius = lower;
	while (celsius <= upper){
		fahr = 32.0 + celsius * 9.0/ 5.0;
		printf("%3.0f \t\t %6.2f\n", celsius, fahr);
		celsius += step;

	}

}