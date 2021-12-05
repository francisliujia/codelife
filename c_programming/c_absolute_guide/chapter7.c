#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "chapterFile.h"

int main()
{
	int age;
	char childname[14] = "Thomas";
	printf("\n%s have %d kids.\n", FAMILY, KIDS);

	age = 11;
	printf("the oldest, is %s, is %d years old.\n", childname, age);

	strcpy(childname, "Christoper");
	age = 6;
	printf("The middle boy, is %s, he is %d years old.\n", childname, age);

	age = 3;
	strcpy(childname, "Benjamin");
	printf("The youngerest, %s is %d years old.\n", childname, age);


	return 0;
}