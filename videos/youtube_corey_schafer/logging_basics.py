import logging

import employee


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

'''
1. debug: detailed information, typically of interest only when diagnosing problems
2. info: confirmation that things are working as expected
3. warning: an indication that something unecpected happened, or indicative of some problem
	in the near future, (e.g. 'disk spece low'). the software is still working as expected.
4. error: due to more serious problem, the software has not been able to perform some function.
5. critical: a serious error, indicating that the program itself may be unable to continue running.
'''

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename = 'test.log', level=logging.DEBUG,
# 	format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
	return x + y

def subtract(x, y):
	return x - y
	
def mutiply(x, y):
	return x * y

def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		logger.exception('tried to devide by zero')
	else:
		return result

num_1 = 20
num_2 = 0

# ///////////// 1  ///////////
# add_result = add(num_1, num_2)
# print('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# sub_result = subtract(num_1, num_2)
# print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# mul_result = mutiply(num_1, num_2)
# print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# div_result = divide(num_1, num_2)
# print('Div: {} / {} = {}'.format(num_1, num_2, div_result))
	

# ///////////// 2  ///////////
add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = mutiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
	