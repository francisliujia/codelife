def find_sum(n):
	sum = 0 
	for i in range(1, n+1):
		sum += i  
	return sum 

# print(find_sum(5))

def find_sum2(n):
	if n == 1:
		return 1
	else:
		return n + find_sum2(n - 1)

# print(find_sum2(5))

# 0,1,1,2,3,5,8,13

def fib(n):
	if n == 0 or n == 1:
		return n 
	return fib(n-1) + fib(n-2)

print(fib(6))
