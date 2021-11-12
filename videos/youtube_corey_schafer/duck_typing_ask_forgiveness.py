# duck typing and easier to ask forgiveness than permission (EAFP)

# class Duck:

# 	def quack(self):
# 		print('quack, quack')

# 	def fly(self):
# 		print('flap, flap')

# class Person:

# 	def quack(self):
# 		print('I am quacking like a duck!')

# 	def fly(self):
# 		print("I am flapping my arms!")


# ==== 1 ====
# def quack_and_fly(thing):
# 	if isinstance(thing, Duck):
# 		thing.quack()
# 		thing.fly()
# 	else:
# 		print('this has to be a Duck!')

# 	print()

# ========2======
# def quack_and_fly(thing):
# 	thing.quack()
# 	thing.fly()
# 	print()


# =============3=========
# def quack_and_fly(thing):
# 	# LBYL(non-pythonic)
# 	if hasattr(thing, 'quack'):
# 		if callable(thing.quack)
# 			thing.quack()

# 	if hasattr(thing, 'fly'):
# 		if callable(thing.fly):
# 			thing.fly()

# 	print()



# ==========4==============
# def quack_and_fly(thing):
# 	# EAFP (PYTHONIC)
# 	try:
# 		thing.quack()
# 		thing.fly()
# 	except AttributeError as e:
# 		print(e)
	# print()



# # ========== 5 ==============
# def quack_and_fly(thing):
# 	# EAFP (PYTHONIC)
# 	try:
# 		thing.quack()
# 		thing.fly()
# 		thing.bark()
# 	except AttributeError as e:
# 		print(e)
# 	print()




# d = Duck()
# quack_and_fly(d)

# p = Person()
# quack_and_fly(p)

# person ={'name':'Jess', 'age':23, 'job':'Programmer'}
# person = {'name':'Jess', 'age': 23}

# LBYL (non-pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
# 	print("i am {name}. I am {age} years old and I am a {job}".format(**person))
# else:
# 	print('Missing some keys')

# # EAFP(Pythonic)
# try:
# 	print("i'am {name}. I'am {age} years old and i am a {job}".format(**person))
# except KeyError as e:
# 	print("missing {} key".format(e))



# my_list = [1,2,3,4,5,6]
# # non-pythonic
# if len(my_list) >= 6:
# 	print(my_list[5])
# else:
# 	print('that index does not exist')

# Pythonic
# try:
# 	print(my_list[5])
# except IndexError:
# 	print('that index does not exist')



import os

# ============= 1 =============
# my_file = "/tmp/test.txt"

# # race condition
# if os.access(my_file, os.R_OK):
# 	with open(my_file) as f:
# 		print(f.read())
# else:
# 	print('file can not be accessed')


# ================= 2 ==============
# no race-condition
try:
	f = open(my_file)
except IOError as e:
	print('file cannot be accessed')
else:
	with f:
		print(f.read())
 

























