def has_duplicates(li):
	if len(li) == 0:
		return 'list is empty'
	elif len(li) == 1:
		return 'this list only contains one element'

	precious_elem = li[0]
	for elem in sorted(li):
		if precious_elem == elem:
			return True
		precious_elem = elem
	return False


t = [4, 7, 2, 7, 3, 8, 9]
print(has_duplicates(t))