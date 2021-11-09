def add(x, y):
	return x + y

def subtract(x, y):
	return x - y
	
def mutiply(x, y):
	return x * y

def divide(x, y):
	if y==0:
		raise ValueError('cannot devide by zero!')
		return x / y 