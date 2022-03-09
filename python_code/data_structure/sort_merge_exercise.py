def merge_sort(arr, key, decending=False):
	if len(arr) <= 1:
		return arr 

	mid = len(arr)//2
	left = arr[:mid]
	right = arr[mid:]

	left = merge_sort(left, key, decending)
	right = merge_sort(right, key, decending)

	return merge_two_sorted_lists(left, right, key, decending)

def merge_two_sorted_lists(left_list, right_list, key, decending=False):
	merged = []
	if decending:
		while len(left_list) > 0 and len(right_list) > 0:
			if left_list[0][key] >= right_list[0][key]:
				merged.append(left_list.pop(0))
			else:
				merged.append(right_list.pop(0))
	else:
		while len(left_list) > 0 and len(right_list) > 0:
			if left_list[0][key] <= right_list[0][key]:
				merged.append(left_list.pop(0))
			else:
				merged.append(right_list.pop(0))

	merged.extend(left_list)
	merged.extend(right_list)
	return merged

if __name__ == "__main__":
	elements = [
	        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
	        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
	        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
	        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
	    ]

	new_list = merge_sort(elements, key='time_hours', decending=True)
	print(new_list)