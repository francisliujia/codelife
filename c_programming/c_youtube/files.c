#include <stdio.h>
#include <stdlib.h>

int main()
{
	char line [255];
	FILE * fpointer = fopen("employees.txt", "r");
	fgets(line, 255, fpointer);
	printf("%s\n", line);

	// fprintf(fpointer, "Jim, salesmen\nram, receptionist\noscar, accounting");

	fclose(fpointer);


	return 0;
}