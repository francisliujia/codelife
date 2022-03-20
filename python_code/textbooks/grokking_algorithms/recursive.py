def countdown(i):
	print(i)
	if i <= 0:
		return
	else:
		countdown(i - 1)

# countdown(100)

def greet(name):
	print('hello, ' + name + '!')
	greet2(name)
	print('getting ready to say goodbye...')
	bye()

def greet2(name):
	print('How are you, ' + name + '?')

def bye():
	print('ok bye!')

# greet('francis')


def fact(x):
	if x == 1:
		return 1 
	else:
		return x * fact(x -1)

print(fact(5))
