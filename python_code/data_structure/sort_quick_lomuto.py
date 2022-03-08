def swap(a, b, arr):
	if a != b:
		temp = arr[a] 
		arr[a] = arr[b] 
		arr[b] = temp

def partition(elements, start, end):
	pivot = elements[end]
	p_index = start 
	for i in range(start, end):
		if elements[i] <= pivot:
			swap(i, p_index, elements)
			p_index += 1
	swap(p_index, end, elements)
	return p_index

def quick_sort(elements, start, end):
	if len(elements) == 1:
		return
	if start < end:
		pi = partition(elements, start, end)
		quick_sort(elements, start, pi-1)
		quick_sort(elements, pi+1, end)

tests = [
    [11,9,29,7,2,15,28],
    [3, 7, 9, 11],
    [25, 22, 21, 10],
    [29, 15, 28],
    [],
    [6]
]


for ele in tests:
	quick_sort(ele, 0, len(ele)-1)
	print(ele)







	