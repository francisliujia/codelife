# import math
# def distance(x1, y1, x2, y2):
# 	dx = x2 - x1
# 	dy = y2 - y1
# 	dsquared = dx**2 + dy**2
# 	result = math.sqrt(dsquared)
# 	return result


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# a = fibonacci(7)
# print(a)

def factorial(n):
	space = ' ' * (4*n)
	print(space, 'factorial', n)
	if n == 0:
		print(space, 'returning 1')
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		print(space, 'returning', result)
		return result
s = factorial(4)
print(s)
	