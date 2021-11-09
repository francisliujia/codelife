def nested_sum(li):
	result = 0
	for element in li:
		result += sum(element)
	return result

t = [[1,2], [3], [4, 5, 6]]
printqs(nested_sum(t))