# # s1 = set([1,2,4,5])
# s1 = {1,2,3,4,5}
# s2 = {6,7,8}
# # s1.add(6)


# # s1.update([12, 45,55], s2)
# # print(dir(s1))
# # s1.remove(6)
# s1.discard(6)

# # s1 = set()
# # create an empty set
# print(s1)


# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = {3, 4, 5}

# # s4 = s1.intersection(s2)
# # s4 = s1.intersection(s2, s3)
# # s4 = s1.difference(s2)
# # s4 = s2.difference(s1)

# s4 = s1.symmetric_difference(s2)
# print(s4)



# l1 = [1,2,3,1,2,3]
# l2 = list(set(l1))
# print(l2)

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']


# result = set(gym_members).intersection(developers)
result = set(employees).difference(developers,gym_members)
print(result)



















