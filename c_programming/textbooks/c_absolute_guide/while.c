# include<stdio.h>

main(){

	int ctr = 0;
	while (ctr < 5)
	{
	printf("counter is at %d.\n", ++ctr);
	}
	while (ctr > 1)
	{
		printf("counter is at %d.\n", --ctr);
	}

	return 0;
}