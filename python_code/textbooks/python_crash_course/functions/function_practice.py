'''''
def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('jesse')
''
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='dog',pet_name= 'peqi')
describe_pet(animal_type='snake',pet_name= 'kaite')
''
def describe_pet(pet_name, animal_type= 'dog'):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name= 'willi')
''
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mashrooms', 'green peppers', 'extra cheese')
''
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(12, 'pepperoni')
make_pizza(122, 'mashrooms', 'green peppers', 'extra cheese')
''

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location= 'princeton', field= 'physics')
print(user_profile)
''
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')
''

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')
''
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushroms', 'green peppers', 'extra cheese')
''

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')
'''

from functions.pizza import  *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')




