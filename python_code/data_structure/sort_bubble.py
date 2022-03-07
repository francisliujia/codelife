# time complexity: O(n**2)
# space complexity O(1)

def bubble_sort(elements):
	size = len(elements)

	for x in range(size - 1):
		swapped = False
		for y in range(size - 1 - x):
			if elements[y] > elements[y+1]:
				temp = elements[y]
				elements[y] = elements[y + 1]
				elements[y + 1] = temp
				swapped = True
		if not swapped:
			break


def bubble_sort_dict(elements, key=None):
	size = len(elements)

	for i in range(size - 1):
		swapped = False
		for j in range(size - 1 - i):
			a = elements[j][key]
			b = elements[j + 1][key]
			if a > b:
				temp = elements[j]
				elements[j] = elements[j+1]
				elements[j+1] = temp
				swapped = True
		if not swapped:
			break






if __name__ == '__main__':
	# elements = [1,4,3,5,8, 90, 45,23,44]
	# s_elements = ['Lincoln', 'Abraham', 'lee', 'francis', ]
	# bubble_sort(s_elements)
	# print(s_elements)

	elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

	bubble_sort_dict(elements, sort_key='name')
	print(elements)






