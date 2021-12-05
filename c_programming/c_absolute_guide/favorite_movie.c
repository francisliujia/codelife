#include <stdio.h>
#include <string.h>
main(){

	int ctr, numberMovies, rating, favRating, leastRating;
	char movieName[40], favorite[40], least[40];
	favRating = 0;
	leastRating = 10;

	do {
		printf("how many movies have you seen this year? ");
		scanf(" %d", &numberMovies);

		if (numberMovies < 1){
			printf("no movies have! how can you rank them?\ntry again.!\n\n\n");


		}
	}
	while(numberMovies < 1);
	for (ctr = 1; ctr <= numberMovies; ctr++){
		printf("\n what was the name of the movie?");
		printf("(onw-word title only!)");
		scanf(" %s", movieName);
		printf("on a scale of 1 to 10, what would ");
		printf("you rate it?");
		scanf(" %d", &rating);

		if (rating > favRating){
			strcpy(favorite, movieName);
			favRating = rating;

		}
		if (rating < leastRating){
			strcpy(least, movieName);
			leastRating = rating;
		}
	}

	printf(" your favorite movie was %s.\n", favorite);
	printf("\nyour least-favorate movie was %s.\n", least);



	return 0;
}