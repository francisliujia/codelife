
# ----------------1. object and classes-----------------

# class Human:
# 	pass 


# same as:
# class Human(object):
# 	pass 

# print(dir(Human))
# print(Human.__bases__)

# print(type(Human), Human.__class__)


# a = 9 
# b = 1.0

# print(type(a), type(b))

# __class__ is an attribute on the object that refers to the class
# from which the object was created.

'''
type is used to find the type or class of an object.
It accepts an object whose type we want to find out
as the first argument and returns the type or class
of that object.
'''


# create a Human obj
# human_obj = Human()
# print(type(human_obj), human_obj.__class__)


# def simple_function():
# 	pass 

# print(type(simple_function), simple_function.__class__)


# metaclass
# Even type of object class is - type
# print(type(int), type(float), type(object))




# ------------- 2.The object instantiation process in Python ---------------
# class Human:
# 	def __init__(self, first_name, last_name):
# 		self.first_name = first_name
# 		self.last_name = last_name

# human_obj = Human('francis', 'lee')

'''
Object creation in Python is a two-step process.
In the first step, Python creates the object, and
in the second step, it initializes the object. Most
of the time, we are only interested in the second step
(i.e., the initialization step). Python uses the __new__
method in the first step (i.e., object creation)
and uses the __init__ method in the second step
(i.e., initialization).
'''


# overwriting 
# class Human:
# 	def __new__(cls, first_name=None):
# 		obj = super().__new__(cls)

# 		if first_name:
# 			obj.name = first_name
# 		else:
# 			obj.name = 'francis'
# 		print(type(obj))
# 		return obj 

# virat = Human()
# print(virat.name)
# sachin = Human('Sachin')
# print(sachin.name)


# class Animal:
# 	def __new__(cls):
# 		obj = super().__new__(Human)
# 		print("type of obj: ", type(obj))
# 		return obj 



# cat = Animal()
# print(type(cat))

# class Human:
# 	def __init__(self, first_name):
# 		self.first_name = first_name
# 		return self

# human_obj = Human("caro")

# class Human:
# 	def __new__(cls, *args, **kwargs):
# 		print('inside __new__ method')
# 		print('===> args arguments:', args)
# 		print('===> kwargs arguments:', kwargs)

# 		human_obj = super(Human, cls).__new__(cls)
# 		print('===> human_obj instance: ', human_obj)
# 		return human_obj

# 	def __init__(self, first_name, last_name):
# 		print('inside __init__ method')
# 		self.first_name = first_name
# 		self.last_name = last_name

# 		print('===> human_obj instance inside __init__:', self, self.first_name, self.last_name)





# ---------------------- 3. __callable__ method ----------------------
# def print_function():
# 	print('i am a callable object')

# print_function()

# a = 10 
# # try:
# 	a()
# except Exception as e:
# 	print(e)

# print(callable(print_function))
# print(callable(a))
# print(callable(Human))
# human_obj = Human('francis', 'lee')
# print('---->', callable(human_obj))
# # human_obj()


# class Human:
# 	def __init__(self, first_name, last_name):
# 		print('inside __init__ method')
# 		self.first_name = first_name
# 		self.last_name = last_name

# 	def __call__(cls):
# 		print('inside __call__ method')

# humna_obj = Human('francis', 'lee')
# print(humna_obj())
# print(humna_obj.__call__())
# print(callable(humna_obj))

# For all objects that are callable, their classes
# must implement the __call__ method.



# def print_function():
# 	print('i am a callable object')

# # print_function()

# print_function.__call__()


# class type:
# 	def __call__():
# 		print('that\'s call method')




# ================== complete class structure =============
'''
class Human:
	def __new__(cls, *args, **kwargs):
		human_obj = super(Human, cls).__new__(cls)
		return human_obj

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __call__(cls, *args, **kwargs):
		human_obj = cls.__new__(*args, **kwargs)

		if human_obj is not None and isinstance(human_obj, cls) and hasattr(human_obj, '__init__'):
			human_obj.init(*args, **kwargs)
		return human_obj
'''



# case 1
'''
If the returned object from the __new__ method is of type Human
(i.e., the class of the __init__ method), the __init__ method will be called.
'''
# class Human:
# 	def __new__(cls, *args, **kwargs):
# 		print(f'==> creating the object with cls {cls} and args {args}')
# 		obj = super().__new__(cls)
# 		print(f'==> object created with obj {obj} and type {type(obj)}')
# 		return obj 

# 	def __init__(self, first_name, last_name):
# 		print(f'==> started : __init__ method of Human class with self: {self}')
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		print(f'==> ended: __init__ method of Human class')

# human_obj = Human('francis', 'lee')
# print(human_obj)



# Case 2: 
# If the __new__ method does not return anything,
# then __init__ will not be called.

# class Human:
# 	def __new__(cls, *args, **kwargs):
# 		print(f'creating the obj with cls: {cls} and args: {args} ')
# 		obj = super().__new__(cls)
# 		print(f'object created with obj: {obj} and type: {type(obj)}')
# 		print('not returning object from __new__ method, hence the __init__ method will not nne called.')

# 	def __init__(self, first_name, last_name):
# 		print(f"started: __init__ method of Human class with self: {self}")
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		print(f'ended: __init__ method of Human class ')

# human_obj = Human('francis', 'lee')
# print(human_obj)



# Case 3: 
# The __new__ method returns an integer object.

# class Human:
# 	def __new__(cls, *args, **kwargs):
# 		print(f'===> creating the obj with cls: {cls} and args: {args} ')
# 		obj = super().__new__(cls)
# 		print(f' ===> object created with obj: {obj} and type: {type(obj)}')
# 		print('not returning object from __new__ method, hence the __init__ method will not nne called.')
# 		return 10

# 	def __init__(self, first_name, last_name):
# 		print(f"===> started: __init__ method of Human class with self: {self}")
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		print(f'===> ended: __init__ method of Human class ')

# human_obj = Human('francis', 'lee')
# print(human_obj)
