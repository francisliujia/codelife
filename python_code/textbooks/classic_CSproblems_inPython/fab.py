# def fib1(n: int) -> int:
# 	return fib1(n-1) + fib1(n-2)

# print(fib1(4))


# def fib2(n):
# 	if n < 2:
# 		return n 
# 	else:
# 		return fib2(n-1) + fib2(n-2) 
# f2 = fib2(9)
# print(f2)

# print(fib2(i) for i in range(11))

# for i in range(10):
# 	print(fib2(i))


# fib 3
# from typing import Dict 
# memo: Dict[int, int] = {0: 0, 1: 1}

# def fib3(n: int) -> int:
# 	if n not in memo:
# 		memo[n] = fib3(n-1) + fib3(n-2)
	# return memo[n]


# print(fib3(100))

# fib4

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fib4(n):
# 	if n < 2:
# 		return n 
# 	else:
# 		return fib4(n-1) + fib4(n-2)

# print(fib4(22))


# # fib5

# def fib5(n):
# 	if n == 0: return n 
# 	last = 0 
# 	_next =1
# 	for _ in range(1, n):
# 		last, _next = _next, last + _next
# 	return _next


# print(fib5(22))

# for _ in range(1, 10):
# 	l, n = n, l + n 
# 	print(n)


# fib6

# def fib6(n):
# 	yield 0
# 	if n > 0:
# 		yield 1
# 	last = 0 
# 	_next =1
# 	for _ in range(1, n):
# 		last, _next = _next, last + _next
# 		yield _next


# for i in fib6(60):
# 	print(i)








