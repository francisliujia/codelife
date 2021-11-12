student = {'name': 'John', 'age': 25, 'courses':['math', 'CompSci']}



# student['phone'] = '3333-3333'
# student['name'] = 'James'
# student.update({'name':'Jane', 'age': 26, 'phone': '3333-66666'})
# del student['age']

# age = student.pop('age')

# print(student['courses'])
# print(student.get('name'))
# print(student.get('phone'))
# print(student.get('phone', 'Not found'))
# print(student)
# print(age)
# print(len(student))
# print(student.values())
# print(student.keys())
# print(student.items())

# for key in student:
	# print(key)

for key, value in student.items():
	print(key, value)