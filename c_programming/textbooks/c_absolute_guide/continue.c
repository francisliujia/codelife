#include <stdio.h>
main(){

	int i;

	for(i= 1; i <= 10; i++){
		if ((i%2) == 1){
			printf("I am rather odd..\n");
		continue;
	}

	printf("even up!\n");
}

	return 0;
}