'''
aliens = []
for alien_number in range (30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] == 10

	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

for alien in aliens[:5]:
	print(alien)

print("...")
''
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['python', 'go'],
	'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")
''

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

''

# message = input("Tell me something and I will reapeat it back to you:")
# print(message)

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f'\nHello, {name}')
''

number = int(input("enter a number, and I will tell you if it's even or odd:"))

if number % 2 == 0:
	print(f"the number {number} is even.")
else:
	print(f"teh number {number} is odd.")
''

# current_number = 1
# while current_number <= 10:
# 	print(current_number)
# 	current_number += 1

prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'q/Q' to end the program."

message = ''
while message != 'q' and message != 'Q':
	message = input(prompt)

	if message != 'quit':
		print(message)
		'''


# current_number = 0
# while current_number < 10:
# 	current_number += 1
# 	if current_number % 2 == 0:
# 		continue
# 	print(current_number)


# unconfirmed_users = ['alice', 'brian', 'edison']
# confirmed_users = []

# while unconfirmed_users:
# 	current_user = unconfirmed_users.pop()
# 	print(f"verifying user: {current_user.title()}")
# 	confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())

'''
responses = {}

polling_active = True

while polling_active:
	name = input("what is your name?\n")
	response = input("which city would you wanna go?")

	responses[name] = response 
	repeat = input("would you like to let another person to respond?(yes/no)\n")
	if repeat == 'no':
		polling_active = False

print("\n----poll results---")
for name, response in responses.items():
	print(f"{name} would like to go to {response}.")

'''

# def get_formatted_name(first_name, last_name):
# 	full_name = f"{first_name} {last_name}"
# 	return full_name.title()

# while True:
# 	print("\nplease tell me your name:")
# 	print("enter 'q' at any time to quit.")
# 	f_name = input("first name: ")
# 	if f_name == 'q':
# 		break
# 	l_name = input("last name: ")
# 	if l_name == 'q':
# 		break

# 	formatted_name = get_formatted_name(f_name, l_name)
# 	print(f"\nHello, {formatted_name}!")

# def greet_users(names):
# 	for name in names:
# 		msg = f"Hello, {name.title()}!"
# 		print(msg)


# usernames = ['hannah', 'mag', 'gen',]
# greet_users(usernames)
'''

unprinted_designs = ['phone case', 'troll', 'smartcard',]
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"print model: {current_design}")
	completed_models.append(current_design)

print("\nthe following models have been printed:")
for completed_model in completed_models:
	print(completed_model.title())

'

def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model:{current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['gun', 'smartcard', 'doll',]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
''

def make_pizza(size, *toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(22, 'mushrooms', 'green peppers', 'extra cheese')


''
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')

print(user_profile)
''

class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
''

class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.model} {self.make}"
		return long_name.title()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery_size = 75

	def describe_battery(self):
		print(f"this car has a {self.battery_size}-kwh battery.")

# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()

	def fill_gas_tank(self):
		print("this car does not need a gas tank!")
'''

# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# print(contents.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

	# for line in lines:
	# 	print(line)

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))





