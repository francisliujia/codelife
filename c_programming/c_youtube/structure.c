#include <stdio.h>
#include <stdlib.h>

struct Student{

	char name[50];
	char major[50];
	int age;
	double gpa;
};

int main()
{

	struct Student student1;
	student1.age = 22;
	student1.gpa = 4.0;
	strcpy(student1.name, "Jerry");
	 strcpy(student1.major, "business");

	printf("%s\n", student1.name );

	
	return 0;
}
