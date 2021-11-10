'''
1. when working with classes, regular methods automatically pass
	the instance as the first argument and we call that self;

2. class methods automatically pass the class as the first argument,
	and we call that cls
	class methods can be used as alternative structors

3. staticmethods don't pass anything automatically, they don't pass
	the instance or the class; so really they behave just like regular
	classes except we include them in our classes because they have some
	logical connection with the class

'''

# //////////////////// 1 ///////////
# class Employee:
# 	pass

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 20000


# print(emp_1.email)
# print(emp_2.email)


# ////////////// 2 /////////////////
class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
# print(emp_2.fullname())

emp_1.fullname()
print(Employee.fullname(emp_1))

import sys
print(sys.executable)
print(sys.version)












