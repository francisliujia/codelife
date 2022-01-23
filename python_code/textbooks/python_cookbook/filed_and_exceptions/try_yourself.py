'''''
filename = "learning_python.txt"

print("---reading the entire file---")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n---looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n---Storing the lines in lists")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())


print("\n---change elements in the file")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip().replace('Python', 'C'))


name = input("What is your name?")
filename = 'guest.txt'
with open(filename, 'w') as f:
    f.write(name)
''

filename = 'guest.book.txt'
print("Enter 'q' when you finished.")

while True:
    name = input("\nWhat is your name? ")
    if name == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")


''
filename = 'programming_pool.txt'

responses = []
while True:
    response = input("\nWhy do you like programming?")
    responses.append(response)

    continue_pool = input("Would you like to let someone else to respond? (y/n)")
    if continue_pool != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
''

try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("sorry, i really need a number. ")
else:
    sum = x + y
    print(f"the {sum} of {x} and {y} is sum")

''
print("enter 'q' at any time you want to quit.:)")

while True:
    try:
        x = input("Give me a number: ")
        if x == 'q':
            break
        else:
            x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break
        else:
            y = int(y)

    except ValueError:
        print("sorry, i really need a number.")
    else:
        sum = x + y
        print(f"the {sum} of {x} and {y} is sum")
''

filenames = ['cat.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, this file cannot be found.")

''
filenames = ['cat.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass

''
def count_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        count_word = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {count_word} times."
        print(msg)


filename = 'alice.txt'
count_words(filename, 'the')
''


import json

number = input("What's your favorite number?")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print(("Thanks! I'll remember that."))
''

import json

with open('favorite_number.json') as f:
    number = json.load(f)
print(f"I know your favorite number! It's {number}, haha! ")
''

import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump("Thanks, will remember that.")
else:
    print(f"I know your favorite number! It {number} haha.")

'''
import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}?(y/n)")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We will remember you when you are back, {username}:).")

greet_user()