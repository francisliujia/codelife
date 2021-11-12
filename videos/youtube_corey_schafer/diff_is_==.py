# what is the difference between == and is?
# == checks for equality
# is checks for identity

# l1 = [1,2,4,5]
# l2 = [1,2,4,5]


# if l1 == l2:
# 	print (True)
# else:
# 	print(False)


# if l1 is l2:
# 	print (True)
# else:
# 	print(False)

# l1 = [1,2,4,5]
# l2 = l1

# if l1 is l2:
# 	print (True)
# else:
# 	print(False)

l1 = [1,2,4,5]
l2 = l1

# l1[0] = 7

# print(l1)
# print(l2)


print(id(l1))
print(id(l2))









