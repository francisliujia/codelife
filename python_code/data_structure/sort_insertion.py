'''
only suitable for the small or medium elements sorting
'''

def insertion_sort(elements):
	for i in range(1, len(elements)):
		anchor = elements[i]
		j = i - 1
		while j >= 0 and anchor < elements[j]:
			elements[j+1] = elements[j]
			j -= 1 
		elements[j+1] = anchor


elements = [11, 23,2,5,32,77,67]
insertion_sort(elements)
print(elements)