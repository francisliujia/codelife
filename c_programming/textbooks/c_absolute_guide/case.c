#include <stdio.h>
#include <stdlib.h>
main(){

	int choice;
	printf("what do you want to do?\n");
	printf("1. add new contact\n");
	printf("2. editing existing contact.\n");
	printf("3. call contact\n");
	printf("4. text contact\n");
	printf("5. exit\n");

	do 
	{
		printf("enter your choice: ");
		scanf(" %d", &choice);
		switch (choice)
		{

			case(1): printf("\nto add you will need the contact's \n");
					 printf("First name, lase name, and number.\n");
					 break;

			case(2): printf("\nget ready to enter the name of");
					 printf("name of the \n");
					 printf("contact you wish to change.\n");
					 break;

			case(3): printf("\nwhich contact do you wish to call?\n");
					 break;

			case(4): printf("\nwhich contact do you wish to text?\n");

			case(5): exit(1);

			default: printf("\n%d is not a valid choice.\n", choice);
					 printf("try again.\n");
					 break;
		}

	}while ((choice <1)||(choice > 5));
	return 0;
}
