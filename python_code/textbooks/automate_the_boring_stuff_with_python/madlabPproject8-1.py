
def madlab():
	print('Enter an adjective:')
	adj = input()
	print('Enter a noun:')
	noun1 = input()
	print('Enter a verb:')
	verb = input()
	print('Enter a noun:')
	noun2 = input()

	return f'The {adj} panda walked to the {noun1} and then {verb}.A nearby {noun2} was unaffected by these events.'

print(madlab())
