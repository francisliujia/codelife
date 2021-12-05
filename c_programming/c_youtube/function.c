# include <stdio.h>
# include <stdlib.h>


void sayHi(char name[]){
	printf("Hello %s", name);


}

int main() //errors
{

	sayHi("mike");
	sayHi("dickens");
	sayHi("jerner");

	return 0;
}

