import random

num1 = random.randint(1,10)
num2 = random.randint(1,10)

print('what is' + str(num1)+ '+' + str(num2) + '?')
answer = int(input())
if answer == num1 + num2:
	print('Correct!')
else:
	print('Nope! The answer is ' + str(num1 + num2))



