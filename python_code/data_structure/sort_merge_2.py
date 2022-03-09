def merge_sort(arr):
	if len(arr) <= 1:
		return arr 

	mid = len(arr)//2
	left = arr[:mid]
	right = arr[mid:]

	merge_sort(left)
	merge_sort(right)

	merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
	len_a = len(a)
	len_b = len(b)
	i = j = k =  0

	while i < len_a and j < len_b:
		if a[i] <= b[j]:
			arr[k] = a[i]
			# sorted_list.append(a[i])
			i += 1
		else:
			b[j] <= a[i]
			arr[k] = b[j]
			# sorted_list.append(b[j])
			j += 1
		k += 1

	while i < len_a:
		arr[k] = a[i]
		# sorted_list.append(a[i])
		i += 1
		k += 1
	while j < len_b:
		arr[k] = b[j]
		# sorted_list.append(b[j])
		j += 1
		k += 1


# a = [1,2,3,4]
# b = [5,6,7,8]
c = [12,5,2,6,77,1,5,89,0,3]
merge_sort(c)
print(c)
