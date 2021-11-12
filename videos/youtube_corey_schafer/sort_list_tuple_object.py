# li = [9,1,4,3,5,6,7,2,5]

# s_li = sorted(li, reverse=True)
# print('Sorted variable:\t', s_li)

# li.sort(reverse=True)

# print('Original variable:\t', li)

# li = [-3,-6,-5,1,3,4,]
# s_li = sorted(li, key=abs)
# print(s_li)



class Employmee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age 
		self.salary = salary

	def __repr__(self):
		return '({}, {}, {})'.format(self.name, self.age, self.salary)


e1 = Employmee('Carl', 37, 70000)
e2 = Employmee('Sarah', 29, 80000)
e3 = Employmee('John', 43, 90000)


employees = [e1, e2,e3]


# def e_sort(emp):
# 	return emp.name

# s_employees = sorted(employees, key=e_sort)

# s_employees = sorted(employees, key=lambda e: e.name)

from operator import attrgetter

s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)









