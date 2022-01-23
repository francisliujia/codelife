'''
def display_message():
    print("Hello everyone, I am learning to create functions on Python.")
display_message()
''
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")
favorite_book('gone with the wind')
''
def make_shirt (size, message):
    print(f"I want a {size} size T-shirt.")
    print(f"I want it says '{message}'\n")
make_shirt('large', 'I loke Python.')
make_shirt('medium', 'I love Plamela Kolewa.')
''
def make_shirt (message,size= 'large'):
    print(f"I want a {size} size T-shirt.")
    print(f"I want it says '{message}'\n")
make_shirt('I love Python.')
''
def make_shirt (size, message= 'I love Plamena Kolewa'):
    print(f"I want a {size} size T-shirt.")
    print(f"I want it says '{message}'\n")
make_shirt('large')
make_shirt('small', 'Programmer are loopy.')
''
def describe_city(name, country= 'scotland'):
    print(f"{name.title()} is in {country.title()}.")
describe_city('stirling', 'scotland')
describe_city('edinburgh')
describe_city('glasgow')
describe_city('inverness')
describe_city('paris', 'france')
''
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('francis', 'lee')
print(musician)
''
def get_formatted_name(first_name, last_name, middle_name= ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('francis', 'lee')

print(musician)
''
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('francis', 'lee')
print(musician)
''
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('francis', 'lee', age=55)
print(musician)
''
def get_informatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' at any time to quit.")

    f_name = input("First name")
    if f_name == 'q':
        break
    l_name = input("Last name ")
    if l_name == 'q':
        break
    formatted_name = get_informatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
''
def city_country(city_name, country_name):
     return f"{city_name.title()}, {country_name.title()}"

city = city_country('stirling', 'scotland')
print(city)
city = city_country('glasgow', 'scotland')
print(city)
city = city_country('edin burgh', 'scotland')
print(city)
''
def build_album(album_title, artist_title, track=None):
    album = {'title': album_title.title(), 'artist': artist_title.title()}
    if track:
        album['tracks'] = track
    return album
album = build_album('ride the lightning','metallica' )
print(album)
album = build_album('ninth symphony', 'beethoven' )
print(album)
album = build_album('red-headed stranger', 'willie nelson')
print(album)
album = build_album('piece of mind', 'iron maiden', 24)
print(album)
''

def build_album(album_title, artist_title, track=None):
    album_dic = {'title': album_title.title(), 'artist': artist_title.title()}
    if track:
        album_dic['tracks'] = track
    return album_dic
while True:
    print("Please enter the titles of a artists and his or her name below.")
    print("Enter 'q' when you are finished.")
    album_t = input("Which album are you thinking of: ")
    if album_t == 'q':
        break
    artist_n = input("Who is the artist: ")
    if artist_n == 'q':
        break
    album = build_album(album_t, artist_n)

    print(album)
print("Thank you for participating!")
''

def greet_users(names):
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)
usernames = ['francis', 'jelmer', 'touseef']
greet_users(usernames)
''
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design.title()}")
    completed_models.append(current_design)

print(f"\nThe following models have been designed:")
for completed_model in completed_models:
    print(completed_model.title())
''
def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_design = unprinted_models.pop()
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been completed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
''

def show_girls(names):
    for name in names:
        print(name.title())

names = ['francis lee', 'plamena kolewa', 'jelmer van ginkel']
show_girls(names)
''
def send_messages(unsent_messages, sent_messges):
    while unsent_messages:
        current_message= unsent_messages.pop()
        print(f"{current_message.title()}, I love you!")
        sent_messges.append(current_message.title())

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message.title())

unsent_messages = ['fancis lee', 'plamena kolewa', 'jelmer van ginkel']
sent_messages = []
send_messages(unsent_messages, sent_messages)
show_sent_messages(sent_messages)
''
def send_messages(unsent_messages, sent_messges):
    while unsent_messages:
        current_message= unsent_messages.pop()
        print(f"{current_message.title()}, I love you!")
        sent_messges.append(current_message.title())

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent: ")
    for sent_message in sent_messages:
        print(sent_message.title())


unsent_messages = ['fancis lee', 'plamena kolewa', 'jelmer van ginkel']
sent_messages = []
send_messages(unsent_messages[:], sent_messages)
show_sent_messages(sent_messages)
print("Show the original list:")
print(unsent_messages)
''
def make_sandwich(*items):
    print("\nYou will have a sandwich containing the following items:")
    for item in items:
        print(f"...adding {item} to your sandwich")
    print("Your sandwich is ready!")

make_sandwich('potato')
make_sandwich('hot dog', 'apple slices', 'banana slices', 'zukinee')
''
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('francis', 'lee', location= 'stirling', field= 'computer science',
                             girl_friend= 'plamena kolewa',
                             spoken_languages= ['english', 'chinese', 'spanish','python', 'c'])
print(user_profile)
''
def car_profile(manifacturer, model, **car_info):
    car_info['brand'] = manifacturer
    car_info['model'] = model
    return car_info
car = car_profile('bmw', 507, price= '£1m', weight= '2t')
print(car)
''

import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
''
import printing_functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
''
from printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
''
from printing_functions import print_models as pm, show_completed_models as sc
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
sc(completed_models)
'''
from functions.printing_functions import *
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)




