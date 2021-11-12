# decorators

# 1. closure
# //////////// 1///////////
# def outer_function():
# 	message = 'Hi'

# 	def inner_function():
# 		print(message)
# 	return inner_function()


# outer_function()

# ////////////// 2 //////////////
# def outer_function():
# 	message = 'Hi'

# 	def inner_function():
# 		print(message)
# 	return inner_function


# my_func = outer_function()
# my_func()
# my_func()
# my_func()
# my_func()

# //////////// 3////////////
# def outer_function(msg):
# 	message = msg

# 	def inner_function():
# 		print(message)
# 	return inner_function


# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()

# ////////// 4 ////////////
# def outer_function(msg):
# 	def inner_function():
# 		print(msg)
# 	return inner_function


# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()


 # 2. decorator
'''a decorator is just a dunction that takes another function as 
 an arguement, adds some functionality, and then returns another 
 function, all of these without altering the source code of the 
 original function that you passed'''

# ////////// 1////////////
# def outer_function(msg):
# 	def inner_function():
# 		print(msg)
# 	return inner_function


# def decorator_function(message):
# 	def wrapper_function():
# 		print(message)
# 	return wrapper_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()


# ////////////////// 2///////////
# def decorator_function(original_function):
# 	def wrapper_function():
# 		return original_function()
# 	return wrapper_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()


# //////////////////// 3 //////////////
# def decorator_function(original_function):
# 	def wrapper_function():
# 		return original_function()
# 	return wrapper_function


# def display():
# 	print('display function ran')

# decorated_display = decorator_function(display)

# decorated_display()

# /////////////////////////// 4 //////////////////////
# def decorator_function(original_function):
# 	def wrapper_function():
# 		print('wrapper executed this before {}'.format(original_function.__name__))
# 		return original_function()
# 	return wrapper_function


# def display():
# 	print('display function ran')

# decorated_display = decorator_function(display)

# decorated_display()


# /////////////// 5 ////////////////
# def decorator_function(original_function):
# 	def wrapper_function():
# 		print('wrapper executed this before {}'.format(original_function.__name__))
# 		return original_function()
# 	return wrapper_function


# def display():
# 	print('display function ran')


# display = decorator_function(display)
# display()


# same as uppper
# ////////////////////// 6 //////////
# def decorator_function(original_function):
# 	def wrapper_function():
# 		print('wrapper executed this before {}'.format(original_function.__name__))
# 		return original_function()
# 	return wrapper_function


# @decorator_function
# def display():
# 	print('display function ran')

# display()


# //////////// 7 /////////
# def decorator_function(original_function):
# 	def wrapper_function():
# 		print('wrapper executed this before {}'.format(original_function.__name__))
# 		return original_function()
# 	return wrapper_function


# @decorator_function
# def display():
# 	print('display function ran')


# def display_info(name, age):
# 	print('display_info ran with arguements ({}, {})'.format(name, age))


# display_info('John', 25)

# display()


# //////////////// 8 //////////
# use function as decorator

# def decorator_function(original_function):
# 	def wrapper_function(*args, **kwargs):
# 		print('wrapper executed this before {}'.format(original_function.__name__))
# 		return original_function(*args, **kwargs)
# 	return wrapper_function


# @decorator_function
# def display():
# 	print('display function ran')

# @decorator_function
# def display_info(name, age):
# 	print('display_info ran with arguements ({}, {})'.format(name, age))


# display_info('John', 25)

# display()



# ///////////////// 9 /////////////////
#  use class as decorator
# def decorator_function(original_function):
# 	def wrapper_function(*args, **kwargs):
# 		print('wrapper executed this before {}'.format(original_function.__name__))
# 		return original_function(*args, **kwargs)
# 	return wrapper_function

# # //////////////

# class decorator_class(object):

# 	def __init__(self, original_function):
# 		self.original_function = original_function

# 	def __call__(self, *args, **kwargs):
# 		print('call method executed this before {}'.format(self.original_function.__name__))
# 		return self.original_function(*args, **kwargs)


# @decorator_class
# def display():
# 	print('display function ran')

# @decorator_class
# def display_info(name, age):
# 	print('display_info ran with arguements ({}, {})'.format(name, age))


# display_info('John', 25)

# display()



# //////////////////////  10 ///////////////

# def my_logger(orig_func):
# 	import logging
# 	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO) 

# 	def wrapper(*args, **kwargs):
# 		logging.info(
# 			'Ran with args: {}, and kwargs:{}'.format(args, kwargs))
# 		return orig_func(*args, **kwargs)

# 	return wrapper

# def my_timer(orig_func):
# 	import time

# 	def wrapper(*args, **kwargs):
# 		t1 = time.time()
# 		result = orig_func(*args, **kwargs)
# 		t2 = time.time() - t1
# 		print('{} ran in : {} sec'.format(orig_func.__name__, t2))
# 		return result
# 	return wrapper

# @decorator_function
# def display():
# 	print('display function ran')




# @my_logger
# def display_info(name, age):
# 	print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info('Hank', 23)


# import time

# @my_timer
# def display_info(name, age):
# 	time.sleep(1)
# 	print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info("Hank", 25)


# //////////// ////////
# import time

# @my_timer
# @my_logger
# def display_info(name, age):
# 	time.sleep(1)
# 	print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info("Hank", 25)

# //////////////////////////
# import time

# @my_logger
# @my_timer

# def display_info(name, age):
# 	time.sleep(1)
# 	print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info("Hank", 25)



# //////////////////////  10 ///////////////
from functools import wraps

def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO) 

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		logging.info(
			'Ran with args: {}, and kwargs:{}'.format(args, kwargs))
		return orig_func(*args, **kwargs)

	return wrapper

def my_timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1
		print('{} ran in : {} sec'.format(orig_func.__name__, t2))
		return result
	return wrapper


import time

@my_logger
@my_timer

def display_info(name, age):
	time.sleep(1)
	print('display_info ran with arguments ({}, {})'.format(name, age))

# display_info = my_timer(display_info)
# print(display_info.__name__)

display_info("Hank", 33)








