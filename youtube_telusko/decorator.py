'''
a decorator is just a function that takes another function as 
an arguement, adds some functionality, and then returns another 
function. all of this without altering the original function you passed in.
'''

# decorator
# def outer_function():
# 	message = 'Hi'

# 	def inner_function():
# 		print(message)
# 	return inner_function

# my_func = outer_function()
# my_func()



# def outer_function(msg):
# 	message = msg

# 	def inner_function():
# 		print(message)
# 	return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()



# def outer_function(msg):
# 	# message = msg

# 	def inner_function():
# 		print(msg)
# 	return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()



# def decorator_function(original_function):
# 	def wrapper_function():
# 		return original_function()
# 	return wrapper_function


# def display():
# 	print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()



# def decorator_function(original_function):
# 	def wrapper_function():
# 		print(f'wrapper executed this before {original_function.__name__}')
# 		return original_function()

# 	return wrapper_function


# def display():
# 	print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()


# @decorator_function
# def display():
# 	print('display function ran')

# display()


# display = decorator_function(display)
# display()



'''
*args, **kwargs allow us to 
'''

# def decorator_function(original_function):
# 	def wrapper_function(*args, **kwargs):
# 		print(f'wrapper executed this before {original_function.__name__}')
# 		return original_function(*args, **kwargs)

# 	return wrapper_function


# class decorator_class(object):
# 	def __init__(self, original_function):
# 		self.original_function = original_function

# 	def __call__(self, *args, **kwargs):
# 		print(f'call method executed this befor {original_function.__name__}')
# 		return self.original_function(*args, **kwargs)



# @decorator_function
# def display():
# 	print('display function ran')


# @decorator_function
# def display_info(name, age):
# 	print(f'display_info ran with arguement {name, age}')

# display_info('John', 25)

# display()

from functools import wraps

def my_logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level= logging.INFO)

	@wrags(orig_func)
	def wrapper(*args, **kwargs):
		logging.info(
			f'Ran with args and kwargs: {args, kwargs}')
		return orig_func(*args, **kwargs)

	return wrapper

def my_timer(orig_func):
	import time

	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = orig_func(*args, **kwargs)
		t2 = time.time() - t1

		print(f'{orig_func.__name__} ran in {t2}.')
		return result
	return wrapper




# @my_logger
# @my_timer
def display_info(name, age):
	print(f'display_info ran with arguement {name, age}')

display_info('Francis', 35)
print(display_info.__name__)







