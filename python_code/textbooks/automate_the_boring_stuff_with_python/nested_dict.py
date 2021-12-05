all_guest = {
	'Alice':{'apples':'5', 'pretzels':'12'},
	'Bob':{'ham sandwiches':'3', 'apples':'2'},
	'Carol':{'cups':'3', 'apple pies':'1'},
}

def total_brought(guests, item):
	num_brought = 0
	for k, v in guests.items():
		num_brought = num_brought + int(v.get(item, 0))
	return num_brought

print('Number of things being brought:')
print(' - apples        ' + str(total_brought(all_guest,'apples')))
print(' - cups          ' + str(total_brought(all_guest,'cups')))
print(' - cakes         ' + str(total_brought(all_guest,'cakes')))
print(' - ham sandwiches' + str(total_brought(all_guest,'ham sandwiches')))
print(' - apple pies    ' + str(total_brought(all_guest,'apple pies')))
