''''
message = input("Tell me something, and i will repeat it back to you: ")
print(message)
''

name = input("Please enter your name: ")
print("Hello " + name + "!")
''
prompt = "If you tell us who you are, we can personalize the messages you see,"
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"Hello, {name}!")
''

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little bit older.")
''
number = input("Enter a number, and I will tell you if its even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
''

message = input("Which car would you like to rent?")
print("Let me see if I can find you a " + message + ".")
''

number = input("How many people in your dinner group? ")
number = int(number)
if number >= 8:
    print("Please be waiting the notice for the available table")
else:
    print("Your table is ready!")
''

number = input("Tell me a number, and I tell you if it's a multiple of ten oe not?")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"{number} is not a multiple of ten.")
''

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
''
prompt = "\n Tell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
''
prompt = "\n Tell me something, and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
''

prompt = "\n please enter the name of city you have visited:"
prompt += "\n Enter 'quit' when you are finished. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

''


prompt = "Please enter the topping you want to order:"
prompt += "\n Enter 'quit' when you are finished."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit'
    print(message)
''
prompt = "Please enter the topping you want to order:"
prompt += "\n Enter 'quit' when you are finished."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
''

prompt = "Please enter the topping you want to order:"
prompt += "\n Enter 'quit' when you are finished."

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)
''

prompt = "How old are you?"
prompt += "\nPlease enter 'quit' when you are finished."
while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    if age <= 3:
        print("You are free to enter.")
    elif age <= 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")
''
x = 2
while x < 1:
    x += 1
    print(x)
''
unconfirmed_users = ['francis', 'plamena', 'adam']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
''
pets = ['dog', 'cat', 'python', 'parrot', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
''
responses = {}
polling_active = True
while polling_active:
    name = input("what is your name?")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

    print("\n-------Poll Results------")
    for name, response in responses.items():
        print(f"{name} would like to climb{response}.")
''
sandwiches_orders = ['pastrami','pocket', 'veggie', 'beef',
                     'chicken', 'club','pastrami', 'pastrami']
finished_sandwiches = []
print("Sorry, we have run out of pastrami today.\n")
while 'pastrami' in sandwiches_orders:
    sandwiches_orders.remove('pastrami')

while sandwiches_orders:
    current_orders = sandwiches_orders.pop()
    print(f"I am working on your {current_orders} sandwiches.")
    finished_sandwiches.append(current_orders)

print("\n")
for finished_sandwiche in finished_sandwiches:
    print(f"I have make you a {finished_sandwiche} sandwiches.")
'''

responses = {}
polling_active = True
name = input("What is your name?")
response = input("what is your dream place to visit?")
responses[name] = response
repeat = input("Would you like to let another to response? (yes/no)")
if repeat == 'no':
    polling_active = False

print("-----poll results------")
for name, response in responses.items():
    print(f"{name.title()} would like to visit{response.title()}.")




