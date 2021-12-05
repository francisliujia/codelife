import random

NUM_DIGITS = 3
MAX_GUESS = 10

def get_secret_num():
	number = list(range(10))
	random.shuffle(number)
	secret_num = ''
	for i in range(NUM_DIGITS):
		secret_num += str(number[i])
	return secret_num

def get_clues(guess, secret_num):
	if guess == secret_num:
		return 'You got it right!'

	clues = []
	for i in range(len(guess)):
		if guess[i] == secret_num[i]:
			clues.append('Fermi')
		elif guess[i] in secret_num:
			clues.append('pico')

	if len(clues) == 0:
		return 'Bagels'

	clues.sort()
	return ' '.join(clues)

def is_only_digits(num):
	if num == '':
		return False
	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False
	return True



print('''
I am thinking of a %s-digit number. Try to guess what it is.
The clues I give are...
when I say: That means:

	Bagels: None of the digits is correct.
	Pico: One digit is correct but in the wrong position.
	Fermi: One digit is correct and in the right position.
	''' %(NUM_DIGITS))


while True:
	secret_num= get_secret_num()
	print("I have thought of a number. You have %s guesses to get it." %(MAX_GUESS))

	guess_count = 1
	while guess_count <= MAX_GUESS:
		guess = ''
		while len(guess) != NUM_DIGITS or not is_only_digits(guess):
			print('\nGuess #%s: ' %(guess_count))
			guess = input()

		print(get_clues(guess, secret_num))
		guess_count += 1

		if guess == secret_num:
			break
		if guess_count > MAX_GUESS:
			print("You have run out of guesses. The answer is %s" %secret_num)

	print('Do you want to play again? (yes/no)')
	if not input().lower().startswith('y'):
		break
















