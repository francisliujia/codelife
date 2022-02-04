# def hello_func(greeting, name='you'):
	# print("Hello Function.")
	# return 'Hello Function'
	# return '{} ,{}.'.format(greeting, name)


# print(hello_func().upper())

# print(hello_func('HI', "francis"))


# def student_info(*args, **kwargs):
# 	print(args)
# 	print(kwargs)


# courses = ['math', 'art']
# info = {'name': 'john', "age": 22}


# student_info('math', 'art', name="john", age=22)
# student_info(*courses, **info)


month_days = [0, 31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
	if not 1 <= month <= 12:
		return "invalid Month"

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]




# print(is_leap(2020))
print(days_in_month(2017, 2))







