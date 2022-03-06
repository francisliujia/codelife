# time complexity: O(n**2)
# space complexity O(1)

def bubble_sort(elements):
	size = len(elements)

	for x in range(size - 1):
		swapped = False
		for y in range(size - 1, x):
			if elements[y] > elements[y+1]:
				temp = elements[y]
				elements[y] = elements[y + 1]
				elements[y + 1] = temp
				swapped = True
		if not swapped:
			break



if __name__ == '__main__':
	elements = [1,4,3,5,8, 90, 45,23,44]
	s_elements = ['Lincoln', 'Abraham', 'lee', 'francis', ]
	bubble_sort(s_elements)
	print(s_elements)
