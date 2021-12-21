import time 

def calProd():
	product = 1 
	for i in range(1, 100_000):
		product *= i
	return product

start_time = time.time()
prod = calProd()
end_time = time.time()
print("the result is %s and lenth is %s" % (prod, len(str(prod))))
print("this takes %s seconds to run" % (end_time - start_time))