from __future__ import print_function, division

def str_fill(i, n):
	return str(i).zfill(n)

def are_reversed(i, j):
	return str_fill(i, 2) == str_fill(j, 2)[::-1]

def num_instances(diff, flag=False):
	daughter = 0
	count = 0
	while True:
		mother = daughter + diff
		if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
			count = count + 1
			if flag:
				print(daughter, mother)
		if mother > 120:
			break
		daughter += 1
	return count


def check_diffs():
	diff = 10
	while diff < 70:
		n = num_instances(diff)
		if n > 0:
			print(diff, n)
		diff += 1
		
print('diff #instances')
check_diffs()
print()
print('daughter mother')
num_instances(18, True)
