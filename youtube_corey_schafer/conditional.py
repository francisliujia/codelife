# language = 'Python'

# if language == 'Python':
# 	print('conditional was true')
# elif language == 'Java':
# 	print('language is Java.')
# else:
# 	print('no match')

a = [1,2,3]
b = [1,2,3]

b = a 

print(id(a))
print(id(b))

print(a == b)
print(a is b)