person = {'name': 'Jenn', 'age': 21}

# sentence = 'my name id ' + person['name'] + 'and i am ' + str(person['age']) + ' years old.'
# sentence = 'My name is {0} and i am {1} years old.'.format(person['name'], person['age'])
# sentence = 'My name is {0[name]} and i am {1[age]} years old.'.format(person, person)
# sentence = 'My name is {0[name]} and i am {0[age]} years old.'.format(person)

# l = ['Jenn', 23]
# sentence = 'My name is {0[0]} and i am {0[1]} years old.'.format(l)

# sentence = "My name is {name} and I am {age} years old.".format(**person)
# print(sentence)

# tag = 'hi'
# text = 'This is headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)

# print(sentence)

# class Person():
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# p1 = Person('Jack', 33)

# sentence = "My name is {0.name} and I am {0.age} years old.".format(p1) 
# print(sentence)


# sentence = "My name is {name} and I am {age} years old.".format(name='Jenn', age='30')
# print(sentence)


# for i in range(1, 11):
# 	# sentence = 'The value is {:02}'.format(i)
# 	sentence = 'The value is {:.2f}'.format(i)
# 	print(sentence)


# sentence = '1 MB is equal to {:,} bytes.'.format(1000**2)
# print(sentence)

import datetime
my_date = datetime.datetime(2016, 9, 24,12,30,45)
# print(my_date)


# sentence = '{:%B, %d, %Y}'.format(my_date)
# print(sentence)

sentence = "{0:%B %d %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(my_date)
print(sentence)















