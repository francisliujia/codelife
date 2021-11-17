import random
import string

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
    =====''', '''
  +---+
  |   |
  O   |
      |
      |
      |
    =====''', '''
  +---+
  |   |
 [O   |
  |   |
      |
      |
    =====''', '''
  +---+
  |   |
 [O]  |
 /|   |
      |
      |
    =====''', '''
  +---+
  |   |
 [O]  |
 /|\  |
      |
      |
    =====''', '''
  +---+
  |   |
 [O]  |
 /|\  |
 /    |
      |
    =====''', '''
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
    =====''','''
  +---+
  |   |
 [0]  |
 /|\  |
 / \  |
      |
    =====''', '''
  +---+
  |   |
 [0]  |
 /|\  |
 / \  |
      |
    =====''']


# word_list = '''ant bloon bat bear beaver bager camel cat cobra cougar
# 			coyote crow dog donky eagel duck ferret fox frog goat goose hawk
# 			lion lizard llama mole monkey moose mouse mule newt otter owl panda
# 			parrot pigeon rabbit ram raven rhino salmon seal shark sheep
# 			sjunk sloth snake spider stork swan tiger toad trout turkey turtle
# 			weasel whale wolf wombat zebra
# 		'''.split()

word_list ={
						'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
						'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
						'Fruit': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloup mango strawberry tomato'.split(),
						'Animal': 'bat bear beaver cat cougar crab dear dog donkey duck eagle fish frog goat leech lion lizard monkey moose otter owl panda python rabbit rat shark sheep skunk squid tpger turkey turtle weasel whale wolf wombat zebra'.split()
						}


def intro():
	print('''Welcome to hangman game. You will be given a random word. 
In order to complete the game,you need to guess the word letter by letter.
You can only guess one letter at one time.Hangman will have one drawing once
you missed one guess. You have to complete the word before the hangman drawing
is complete.''')


def get_word(word_list):
	target_word_key = random.choice(list(word_list.keys()))
	target_word = random.choice(list(word_list[target_word_key]))
	# print(target_word)
	return target_word, target_word_key 


def show_board(missed_letters, correct_letters, target_word):
	print(f'{HANGMAN[len(missed_letters)]}\n')

	print('Missed letters:', end='')
	for letter in missed_letters:
		print(letter +'', end=' ')
	print()

	blanks = '_' * len(target_word)

	for i in range(len(target_word)):
		if target_word[i] in correct_letters:
			blanks = blanks[:i] + target_word[i] + blanks[i+1:]

	print()
	for letter in blanks:
		print(letter + ' ', end='')
	print()


def get_guess(already_guessed):
	while True:
		guess = input('\nGuess a letter:\n')
		guess.lower()
		if len(guess) != 1:
			print('\n\t\t\tINVALID INPUT\nPlease enter a single letter.\n')
		elif guess in already_guessed:
			print(f'\n\t\t\tINVALID INPUT\nThe letter ** {guess} ** already has been gussed, please choose another letter.\n')
		elif guess not in string.ascii_lowercase:
			print('\n\t\t\tINVALID INPUT\nPlease enter a letter.')
		else:
			return guess


def play_again():
	print('Do you want to play again? \n(yes/no)')
	return input().lower().startswith('y')


def pick_level():
	difficult_level = ''
	while difficult_level not in 'EMH':
		print('Which level do you want to play?\n(Choice: E: Easy, M: Medium, H: Hard)')
		difficult_level = input().upper()

	if difficult_level == 'M':
		del HANGMAN[1]
		del HANGMAN[2]

	if difficult_level == 'H':
		del HANGMAN[1]
		del HANGMAN[2]
		del HANGMAN[3]
		del HANGMAN[4]
		del HANGMAN[5]

	return HANGMAN



print()
# print('\t\t\t H A N G M A N')
print()
# difficult_level = ''
# while difficult_level not in 'EMH':
# 	print('Which level do you want to play?\n(Choice: E: Easy, M: Medium, H: Hard)')
# 	difficult_level = input().upper()

# if difficult_level == 'M':
# 	del HANGMAN[1]
# 	del HANGMAN[2]

# if difficult_level == 'H':
# 	del HANGMAN[1]
# 	del HANGMAN[2]
# 	del HANGMAN[3]
# 	del HANGMAN[4]
# 	del HANGMAN[5]
missed_letters = ''
correct_letters = ''
target_word, secret_set = get_word(word_list)
game_is_done = False

while True:
	print()
	print('\t\t\t H A N G M A N')
	print()
	intro()
	pick_level()
	print()
	# for i in HANGMAN:
	# 	print(i)
	print(f'\t\tThe target word is in ** {secret_set} ** .')
	show_board(missed_letters, correct_letters, target_word)

	guess = get_guess(missed_letters + correct_letters)

	if guess in target_word:
		correct_letters = correct_letters + guess

		found_all_letters = True
		for i in range(len(target_word)):
			if target_word[i] not in correct_letters:
				found_all_letters = False
				break

		if found_all_letters:
			print(f'Congrats!\nThe target word is {target_word}!')
			game_is_done = True

	else:
		missed_letters = missed_letters + guess

		if len(missed_letters) == len(HANGMAN) - 1:
			show_board(missed_letters, correct_letters, target_word)
			print()
			print(f'Sorry. You have run out of guesses with {len(missed_letters)} incorrect guesses. \
				and {len(correct_letters)} correct guesses!\nThe target word is: ***{target_word}***\n')
			game_is_done = True

	if game_is_done:
		if play_again():
			missed_letters = ''
			correct_letters = ''
			game_is_done = False
			target_word, secret_set = get_word(word_list)
		else:
			break














