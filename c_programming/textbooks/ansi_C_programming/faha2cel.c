# include <stdio.h>

/* print fahrenjeit-celsius table
	for fahr = 0, 20, ..., 300 */

int main()
{
	float fahr, celsius;
	int lower, upper, step;

	lower = 0;
	upper = 300;
	step = 20;

	printf("Fahrenheit - Celsius Table\n\n");
	fahr = lower;
	while (fahr <= upper){
		celsius = 5.0/9.0 * (fahr - 32.0);
		printf("%3.0f\t\t%6.2f\n", fahr, celsius);
		fahr += step;
	}
}