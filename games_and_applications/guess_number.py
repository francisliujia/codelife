import random

guess_count = 0

name = input('\nHello there, what is your name:')

print(f"\n\nHi {name.upper()}, I am going to think a number between 1 and 20. \nNOW, Take a guess and you hava 6 chances in total.\n\n")

target_number = random.choice(range(20))
total_guess = 6
guess_count = 0
while total_guess:
	guess_numer = input('What is your guess:')
	try:
		guess_numer = int(guess_numer)
	except Exception as e:
		print('\n\n******* INVALID INPUT! *********\nPlease input an integer.\n')
		continue


	if guess_numer > target_number:
		guess_count += 1
		total_guess = total_guess - 1
		if total_guess < 1:
			print(f"\n\nYou have run out of chance, \nthe target number is ** {target_number} **. Good luck next time, Goodbye.\n\n")			
		else:
			print(f'\nThe target numner is less than your guess, you have {total_guess} chances left.')
	elif guess_numer < target_number:
		guess_count += 1
		total_guess = total_guess - 1
		if total_guess < 1:
			print(f"\n\nSorry, you have run out of chances, \nThe target number is ** {target_number} **. Good luck next time. Goodbye.\n\n")	
		else:
			print(f'\nThe target number is greater than your guess, you have {total_guess} chances left.')
	elif guess_numer == target_number:
		print('\n\nCongrats! You got it right!')
		break





