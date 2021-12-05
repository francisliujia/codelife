#include <stdio.h>
#include <stdlib.h>

int main()
{

	double num1;
	double num2;
	char op;

	printf("enter a number: \n");
	scanf("%lf", &num1);
	printf("Enter operator:\n");
	scanf(" %c", &op);
	printf("enter a number: \n");
	scanf("%lf", &num2);

	if (op == '+'){
		printf("%f\n",num1 + num2);
	}else if(op == '-'){
		printf("%f\n", num1 - num2);
	}else if(op == '*'){
		printf("%f\n", num1 * num2);
	}else if(op == '/'){
		printf("%f\n", num1 / num2);
	}else{
		printf("Invalid operator\n");
	}



	
	return 0;
}