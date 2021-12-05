import random

your_name = input('Hello! What is your name?')

target_number = random.randint(1, 20)

print(f'\nHi, {your_name.capitalize()}, I am going to think of a number\
 between 1 and 20, you have got six chances to guess the right number.\n')

guess_count =0
for guess_count in range(6):
	try:
		guess = int(input('Take a guess:\n'))
	except Exception as e:
		print('\nThe input is invalid.\nPlease input an integer.\n')
		continue

	if guess < target_number:
		print(f'\nYour guess is too low.\n\
			You have {5-guess_count} chances left.')
	if guess > target_number:
		print(f'\nYour guess is too high.\n\
			You have {5-guess_count} chances left.')
	if guess == target_number:
		break

if guess == target_number:
	print(f'Congrats! You got it right in {guess_count+1} times!')
if guess != target_number:
	print(f'Sorry, you have run out of chances. The target_number is {target_number}.\n\
		Good luck next time. Goodbye.')


