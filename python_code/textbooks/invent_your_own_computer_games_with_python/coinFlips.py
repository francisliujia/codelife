import random

print('I will flip a coin 1000 times. Guess how many times it will come heads. (press enter to begin)')

input()
flips = 0
heads = 0

while flips < 1000:
	if random.randint(0, 1) == 1:
		heads += 1
	flips += 1

	if flips == 900:
		print(f'900 flips and there have been {heads} heasds.')
	if flips == 100:
		print(f'At 100 tosses, heads has come up {heads} times')
	if flips == 500:
		print(f'Half way done, and heads has come up {heads} times')

print(f'\nOut of 1000 coin tosses, heads came up {heads} times!')
print('\nWere you close?')