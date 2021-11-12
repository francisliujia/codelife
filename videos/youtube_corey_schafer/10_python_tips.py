# condition = False

# # if condition:
# 	# x = 1
# # else:
# 	# x = 0


# # ||

# x = 1 if condition else 0

# print(x)



# num1 = 1000000000000
# num2 = 1000000000
# # ||

# num1 = 1_000_000_000_000
# num2 = 1_000_000_000


# total = num1 + num2
# # print(total)
# print(f'{total:,}')

# f = open('test.txt','r')

# file_contents = f.read()

# f.close()


# ||

# with open('test.txt', 'r') as f:
# 	file_contents = f.read()



# words = file_contents.split(' ')
# word_count = len(words)
# print(word_count)



# names = ['corey', 'chris', 'dave', 'travis']


# index = 0
# for name in names:
# 	print(index, name)
# 	index += 1

# ||

# for index, name in enumerate(names, start=1):
	# print(index, name)


# people use bad codes because they don't know some funcs exit

names = ['peter parker', 'clark kent', 'wade wilson', 'bruce wayne']
heros = ['spiderman', 'superman', 'deadpool', 'batman']
universe = ['marvel', 'DC', 'marvel', 'dc']

# for index, name in enumerate(names):
# 	hero = heros[index]
# 	print(f'{name} is actually {hero}')


# print(dict(zip(names, heros)))
# print(list(zip(names, heros)))

# ||


# zip() returns a tuple

# for name, hero, universe in zip(names, heros, universe):
# 	print(f'{name} is actually {hero} from{universe}')


# for value in zip(names, heros, universe):
# 	types = type(value)
# 	print(value, types)
# 	# print(value, f'{type(value)}')
# # print(type(value))


# unpacking

# a,b = 1,2

# a, _ = 1,2
# print(a)
# # print(b)

# a,b,*c = (1,2,3,4,5)
# print(a)


# a,*b,c = (1,2,4,5,6,9)
# print(a)
# print(b)
# print(c)



class Person():
	pass

person = Person()

# first_key = 'first'
# first_val = 'corey'

# # setattr(person, 'first', 'corey')
# setattr(person, first_key, first_val)


# first = getattr(person, first_key)

# print(first)

# person.first_key = first_val

# print(person.first)
# print(person.first)



# person_info = {'first': 'corey', 'last':'Schafer'}

# for key, value in person_info.items():
# 	setattr(person, key, value)

# # print(person.first)
# # print(person.last)


# for key in person_info.keys():
# 	print(getattr(person, key))



# person.first = 'corey'
# person.last = 'schafer'

# print(person.first)
# print(person.last)



# username = input('Username: ')
# password = input('Password: ')

# print('Logging In...')


from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print('Logging In...')
































