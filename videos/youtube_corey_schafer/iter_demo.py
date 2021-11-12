# nums = [1,2,3]

# i_nums = iter(nums)

# # print(i_nums)
# # print(dir(i_nums))

# # for num in nums:
# # 	print(num)

# while True :
# 	try:
# 		item = next(i_nums)
# 		print(item)
# 	except Exception as e:
# 		print(e)
# 		break




# # print(next(i_nums))
# # print(next(i_nums))
# # print(next(i_nums))
# # print(next(i_nums))
# # # print(dir(nums))


class MyRange:
	def __init__(self, start, end):
		self.value = start
		self.end = end 

	def __iter__(self):
		return self

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration
		current = self.value 
		self.value += 1
		return current



def my_range(start):
	current = start
	# while current < end:
	while True:
		yield current
		current += 1



# nums = MyRange(1, 10)
nums = my_range(1)
for num in nums:
	print(num)
# print(next(nums))
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())



