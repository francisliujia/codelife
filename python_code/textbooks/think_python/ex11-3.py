from __future__ import print_function, division

cache = {}
def ackermann(m, n):
	if m == 0:
		return n + 1
	if n == 0:
		return ackermann(m-1, 1)
	if (m, n) in cache:
		return cache[m, n]
	else:
		cache[m, n] = ackermann(m -1, ackermann(m, n -1))
		return cache[m ,n]

print(ackermann(3, 4))
print(ackermann(3, 6))