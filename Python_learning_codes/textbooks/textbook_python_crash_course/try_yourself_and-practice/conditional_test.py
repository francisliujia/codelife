'''
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print(" Is car == 'audi'? I predict False")
print(car == 'audi')
print("\n\n")

car = 'toyota'
print("Is car == 'bmw'? I predict False")
print(car == 'bmw')

print("Is car not 'bmw'? I predict True")
print(car != 'bmw')
print("\n\n")

name = 'francis'
print("Is he francis? I predict True")
print(name == 'francis')

print("Is he not francis? I predict False")
print(name == "lee")

fruit = 'apple'
print("is this fruit == 'apple'? I predict True")
print(fruit == 'apple')

print("is this == 'banana'? i predict False")
print(fruit == 'banana')

print("is this != 'banana'? I predict True")
print(fruit != 'banana')

hight = 'tall'
print("is he == 'tall'? I predict True")
print(hight == 'tall')

print("Is he == 'short'? I prdict False")
print(hight == 'short')

print("Is he != 'short'? I prdict True.")
print(hight != 'short')
''

guests = ['francis', 'francesco', 'leena', 'plamena']
female = 'leena'
if female == 'leena':
    print("She is so hot!")
    print(female.upper() + " is so hot!")

''

size_a = 23
size_b = 36
print(size_a == size_b)
print(size_a != size_b)
print(size_a > size_b)
print(size_a >= size_b)
print(size_a < size_b)
print(size_a <= size_b)

print("\n")
print(size_a == size_b and size_a < size_b)
print(size_a == size_b or size_a < size_b)
'''

pretty_girls = ['plamena', 'helen', 'kaite', 'Laura']
girl = 'emily'

if girl not in pretty_girls:
    print("Hey, that " + girl.title() + " is not as gorgeous as us!")

else:
    print("You are so pretty!")
