
# ========== 1========
# not using generator
# def square_numbers(nums):
# 	result = []
# 	for i in nums:
# 		result.append(i*i)
# 	return result


# my_nums = square_numbers([1,2,3,4,5])

# print(my_nums)


# =============== 2 =================
# using generator
# generators don't hold the entire result in memory,
# it yields one result at a time, waiting us for the next result
# def square_numbers(nums):
# 	for i in nums:
# 		yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])
# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))
# print (next(my_nums))


# ==============3==============
# def square_numbers(nums):
# 	for i in nums:
# 		yield (i*i)


# my_nums = square_numbers([1,2,3,4,5])

# for num in my_nums:
# 	print(num)


# +++++++++++++++ 4 ++++++++++++++
# list comprehension
# my_nums = [x*x for x in [1,2,3,4,5]]


# for num in my_nums:
# 	print(num)



# ==============5==============
# my_nums = (x*x for x in [1,2,3,4,5])

# print(my_nums)

# for num in my_nums:
# 	print(num)


# ============6============
my_nums = (x*x for x in [1,2,3,4,5])

print(list(my_nums))



