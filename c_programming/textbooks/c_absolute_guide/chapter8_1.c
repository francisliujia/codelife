#include <stdio.h>
int main()
{
	char firstInitial;
	char lastInitial;
	int age;
	int favirite_number;

	printf("What letter does your first name begin with?\n");
	scanf("%c", &firstInitial);

	printf("What letter does your lst name begin with?\n");
	scanf("%c", &lastInitial);

	printf("how old are you?\n");
	scanf(" %d", &age);

	printf("What is your favorite number number?\n");
	scanf(" %d", &age);

	printf("\nYour initials are %c%c. and you are %d years old",
		firstInitial, lastInitial, age);

	printf("\nYour favorite number is %d.", favirite_number);


	return 0;
}