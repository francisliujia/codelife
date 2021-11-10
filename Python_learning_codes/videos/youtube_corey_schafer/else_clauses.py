# my_list = [1,2,3,4,5]

# for i in my_list:
# 	print i
# 	if i == 7:
# 		break
# else:
# 	print 'Hit the For/else statement'


def find_index(to_sesarch, target):
	for i, value in enumerate(to_sesarch):
		# print i, value
		if value == target:
			break
	else:
		return -1
		# print i
	return i



my_list = ['Corey', 'Rick', "John"]
index_location = find_index(my_list,'Steve')

print 'Location of the target is index :{}'.format(index_location)