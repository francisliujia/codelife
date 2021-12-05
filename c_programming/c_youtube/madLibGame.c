#include <stdio.h>
#include <stdlib.h>

int main()
{

	char color[20];
	char pluralNoun[20];
	char celebrityF[20];
	char celebrityL[20];

	printf("enter a color: \n");
	scanf("%s", color);

	printf("enter a plural noun: \n");
	scanf("%s", pluralNoun);

	printf("enter a celebrity: \n");
	scanf("%s%s", celebrityF, celebrityL);

	printf("----------------\n");

	printf("Roses are %s\n", color);
	printf("%s are blue,\n", pluralNoun);
	printf("I love %s %s.\n", celebrityF, celebrityL);

	printf("----------------\n");

	return 0;



}