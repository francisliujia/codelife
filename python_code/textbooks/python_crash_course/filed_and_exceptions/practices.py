'''''
with open('pi_digits.txt') as file_objects:
    contents = file_objects.read()
    print(contents.strip())


filename = 'pi_digits.txt'
with open(filename) as file_objects:
    for line in file_objects:
        print(line.rstrip())


filename = 'pi_digits.txt'
#stores the lines of the file in a list inside the with block
# and print the lines outside the with block
with open(filename) as file_objects:
    lines = file_objects.readlines()

for line in lines:
    print(line.rstrip())


filename = 'pi_digits.txt'
with open(filename) as file_objects:
    lines = file_objects.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

filename = 'pi_digits.txt'
with open(filename) as file_objects:
    lines = file_objects.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


filename = 'pi_million_digits.txt'
with open(filename) as file_objects:
    lines = file_objects.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))



filename = 'pi_million_digits.txt'
with open(filename) as file_objects:
    lines = file_objects.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday,in the form ddmmyyyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doese not appear in the first million digits of pi.")
''

filename = "programming.txt"
with open(filename, 'w') as file_objects:
    file_objects.write("I loving programming!\n")
    file_objects.write("I love creating new games.\n")

''
filename = "programming.txt"
with open(filename, 'a') as file_objects:
    file_objects.write("I also love finding meaning in large database.\n")
    file_objects.write("I love creating  apps that can run in a browser.")
    
''
try:
    print(5/0)
except ZeroDivisionError:
    print("you cannot divide by zero!")
''

print("Give me two numbers, and i will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nenter a number: ")
    if first_number == 'q':
        break
    second_number = input("enter another number: ")
    if second_number == 'q':
        break

    answer = int(first_number) / int (second_number)
    print(answer)
    ''

while True:
    first_number = input("\nenter a number: ")
    if first_number == 'q':
        break
    second_number = input("enter another number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can not divide by zero!")
    else:
        print(answer)
''
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} cannot be found.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"the file {filename} has about {num_words} words.")
''


def count_words(filename):
    #count the approximate number of words in a file.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry the file {filename} cannot be found.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick', 'little_women.txt']
for filename in filenames:
    count_words(filename)

print("\n")

def count_words(filename):
    #count the approximate number of words in a file.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick', 'little_women.txt']
for filename in filenames:
    count_words(filename)

''
import json
numbers = [2, 3, 5, 5, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

import json
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)
''


import json
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We will remember you when you come back, {username}!")

''
import json
fielname = 'username.json'

with open(fielname) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

''

import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We will remember you when you come back, {username}!")
else:
    print(f"Welcmome back, {username}!")

''
import json
def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We will remember you when you come back, {username}!")
    else:
        print(f"Welcmome back, {username}!")

greet_user()
'''

import json

def get_stored_name():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_uswername():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username

def greet_user():
    username = get_stored_name()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_uswername()
        print(f"We will remember you when you come back, {username}!")


greet_user()