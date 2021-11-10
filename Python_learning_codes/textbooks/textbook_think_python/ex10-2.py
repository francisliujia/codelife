def cumsum(li):
	result = []
	total = 0
	for element in li:
		total += element
		result.append(total)
	return result

t = [1, 2, 3]
print(cumsum(t))