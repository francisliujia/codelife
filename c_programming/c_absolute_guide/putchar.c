#include <stdio.h>
#include <string.h>

main(){

	int i;
	char msg[25];
	printf("Type up to 25 character and then press enter...\n");
	for (i =0; i<25; i++){
		msg[i] = getchar();
		if (msg[i] == '\n'){
			i--;
			break;
		}

	}

putchar('\n');
for (; i>0; i--){
	putchar(msg[i]);
}

putchar('\n');



	return 0;
}