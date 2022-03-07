'''
piviot; partitioning
Hoare Partition
Lomuto partition 

	- average time complexity: O(nlogn)
	- worst case time complexity: O(n**2)
'''

def swap(a, b, arr):
	if a != b:
		arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
	pivot_index = start
	pivot = elements[pivot_index]

	# start = pivot_index + 1
	# end = len(elements) - 1

	while start < end:
		while start < len(elements) and  elements[start] <= pivot:
			start += 1
		while elements[end] >= pivot:
			end -= 1

		if start < end:
			swap(start, end, elements)
	swap(pivot_index, end, elements )
	return end 

def quick_sort(element, start, end):
	if start < end
		pi = partition(elements, start, end) 
		quick_sort(elements, start, pi-1)
		quick_sort(elements, pi+1, end)


elements = [11, 9, 29, 7, 2, 15, 28]
quick_sort(elements, 0, len(elements)-1)
print(elements)
