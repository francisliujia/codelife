#include <stdio.h>

int main(){
	char topping[24];
	int slices;
	int month, day, year;
	float cost;

	printf("how much does a pizza cost in your area?\n");
	printf("enter as £xx.xx\n");
	scanf(" $%f", &cost);

	printf("what is your favorite one-word topping\n");
	scanf(" %s", topping);

	printf("How many slices of %s pizza\n", topping);
	printf("Can  you eat in one sitting?\n");
	scanf(" %d", &slices);

	printf("what is today's date (enter it in xx/xx/xx format).\n");
	scanf("%d%d%d", &month, &day, &year);

	printf("\n\n why not treat yourself to dinner on %d%d%d", month, day, year);
	printf("\nand have %d slices of %s pizza!\n", slices, topping);
	printf("It will only cost you $%.2f!\n", cost );

	return 0;
}