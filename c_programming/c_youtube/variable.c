#include <stdio.h>
#include <stdlib.h>

int main()
{
	char characterName[]  = "John";
	int characterAge = 35;

	printf("my name is %s\n", characterName);
	printf("i am %d years old.\n", characterAge);

	characterAge = 23;
	printf("I don't like being %d years old.\n", characterAge);
	printf("i have a friend.\n");
	printf("i don't like the name %s. \n", characterName);

}