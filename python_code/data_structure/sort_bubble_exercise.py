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

elements = [
    { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
]

bubble_sort_dict(elements, key='name')
print(elements)