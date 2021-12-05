import random
import time

def displayIntro():
	print(''' You are in a land full of gragons. In front of you,
		you see two caves. In one cave, the dragon is friendly,
		and will share his treasure with you. The other dragon
		is greedy and hungry, and will eat you on sight.
		''', end=('\n'))


def chose_cave():
	cave = ''
	while cave != '1' and cave != '2':
		cave = input('Which cave would you go into? (1 or 2)')

	return cave

def check_cave(chosen_cave):
	print('You approaching the cave...')
	time.sleep(2)
	print('It\'s dark and spooky...')
	time.sleep(2)
	print('A huge dragon jumps out in fron of you!\
		She opens her jaws and ...', end=('\n'))
	time.sleep(2)

	lucky_cave = random.randint(1,2)

	if chosen_cave == str(lucky_cave):
		print('Gives you her treasure!')
	else:
		print('Googles you down in one bite...')

play_again= 'yes'
while play_again.lower() == 'yes' or play_again.lower() == 'y':
	displayIntro()
	cave_number = chose_cave()
	check_cave(cave_number)

	print('Do you want to play again? (yes or no)')
	play_again = input()



