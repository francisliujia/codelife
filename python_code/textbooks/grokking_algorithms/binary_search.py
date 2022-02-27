def binary_search(list, item):
	low = 0
	high = len(list) - 1
	count = 1 
	while low <= high:
		print('{} try'.format(count))
		mid = (low + high) // 2
		guess = list[mid]
		if guess > item:
			high = high - 1
		elif guess < item:
			low = mid + 1
		else:
			guess == item
			return 'the item is at position: {}'.format(mid)
		count += 1
	return None 

list1 = [1,3,4,5,6,7,8,9,12,34,56]
print(binary_search(list1, 34))
