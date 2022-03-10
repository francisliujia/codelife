# shortcomings with insertion sort:
# 1) comparisions  2) swaps

# 1. start with gap= n/2 and sort sub arrays
# 2. keep reducing gap by n/2 in and keep on sorting
# 3. last iteration should have gap = 1. at this point 
# 		it as same as insertion sort.

def shell_sort(arr):
	size = len(arr)
	gap = size // 2

	while gap > 0:
		for i in range(gap, size):
			anchor = arr[i]
			j = i 
			while j >= gap and arr[j-gap] > anchor:
				arr[j] = arr[j-gap]
				j -= gap  
			arr[j] = anchor
		gap = gap // 2

elements = [21, 28, 29, 17, 8, 4, 25, 22, 32, 9]
shell_sort(elements)
print(elements)