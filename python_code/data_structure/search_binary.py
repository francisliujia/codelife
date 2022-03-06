def binery_search(num_list, item_to_find):
	low = 0
	high = len(num_list) - 1
	mid = 0

	while low <= high:
		mid = (low + high) // 2
		mid_num = num_list[mid]

		if mid_num > item_to_find:
			high = mid - 1
		elif mid_num < item_to_find:
			low = mid + 1
		else:
			return mid
	return -1 


def binary_search_recursion(num_list, num_to_find, left_index, right_index):
	if right_index < left_index:
		return -1 
	mid_index = (left_index + right_index) // 2
	if mid_index >= len(num_list) or mid_index < 0:
		return -1
		
	mid_num = num_list[mid_index]

	if mid_num < num_to_find:
		left_index = mid_index + 1 
	elif mid_num > num_to_find:
		right_index = mid - 1
	else:
		return mid_index
	return binary_search_recursion(num_list, num_to_find, left_index, right_index)

if __name__ == '__main__':

	list1 = [1,2,3,4,5]
	ret = binery_search(list1, 3)
	print(ret)
	ret2 = binary_search_recursion(list1, 3, 0, len(list1))
	print(ret2)
