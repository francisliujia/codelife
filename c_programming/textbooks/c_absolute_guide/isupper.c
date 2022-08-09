#include <stdio.h>
#include <string.h>
#include <ctype.h>

main(){

	int i;
	int hasUpper, hasLower, hasDigit;
	char user[25], password[25];

	hasUpper = hasLower = hasDigit = 0;

	printf("what is your username? ");
	scanf(" %s", user);
	printf("what is your password? ");
	scanf(" %s", password);

	for (i= 1; i < strlen(password); i++){
		if (isdigit(password[i])){
			hasDigit = 1;
			continue;
		}
		if (isupper(password[i])){
			hasUpper = 1;
			continue;
		}
		if (islower(password[i])){
			hasLower = 1;
		}
	}
	if ((hasDigit)&&(hasLower)&&(hasUpper)){
		printf("\n\nexcellent work, %s, \n", user);
		printf("your password has upper and lower case ");
		printf("letters and a number.");

	}
	else{
		printf("\n\nyou should consider a new password,%s.\n", user);
		printf("one that uses upper and lowecase letters and a number.\n");

	}
	return 0;
}