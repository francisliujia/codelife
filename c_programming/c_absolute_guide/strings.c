#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char kid1 [12];
	// kid can hold an 11-character name
	// kid2 will be 7 characters (maddie plus 0)
	char kid2 [] = "Maddie";
	char kid3[7] = "andrew";
	char hero1[] = "batman";
	char hero2[30] = "spideman";
	char hero3[25];

		kid1[0] = 'k'; 
		kid1[1] = 'a'; 
		kid1[2] = 't';
		kid1[3] = 'i';
		kid1[4] = 'e';
		kid1[5] = '\0';


		strcpy(hero3, "the incredible Hulk");
		printf("%s\'s favorite hero is %s.\n", kid1, hero1);
		printf("%s\'s favorite hero is %s.\n", kid2, hero2);
		printf("%s\'s favorite hero is %s.\n", kid3, hero3);

	return 0;
}