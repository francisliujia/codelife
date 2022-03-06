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

def find_all_occurances(num_list, num_to_find):
	index = binery_search(num_list, num_to_find)
	indices = [index]

	i = index - 1
	while i >=0:
		if num_list[i] == num_to_find:
			indices.append(i)
		else:
			break
		i -= 1 

	i = index + 1
	while i >=0:
		if num_list[i] == num_to_find:
			indices.append(i)
		else:
			break
		i += 1 

	return sorted(indices)




