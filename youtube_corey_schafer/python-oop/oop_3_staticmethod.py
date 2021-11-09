
class Employee:

	raise_amount = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str_1.split('-')
		return cls(first, last, pay)

	@staticmethod
	# you don't access the instance or the class anywhere within
	# the function
	def is_workday(day):
		# 0-4: MOn- Fri; 5-6: Sat - Sun
		if day.weekday() == 5 or day.weekday() == 6:
			return False

		# if day.weekday() == 5:
		# 	return False
		# elif day.weekday() == 6:
		# 	return False
		return True

import datetime
my_date = datetime.date(2021, 8, 14)

print(Employee.is_workday(my_date))


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


















