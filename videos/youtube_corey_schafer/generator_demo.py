# def square_nums(nums):
# 	result = [num**2 for num in nums]
# 	return result

# my_nums = square_nums([1,2,34])
# print(my_nums)




def square_nums(nums):
	for i in nums:
		yield (i**2)



my_nums = [i**2 for i in nums]


my_nums = square_nums([1,2,34])
# print(my_nums)

for num in my_nums:
	print(num)