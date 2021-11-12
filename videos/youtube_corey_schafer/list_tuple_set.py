# courses = ['history', 'math', 'physics', 'compsci']
# courses_2 = ['art', 'education']

# nums = [1,2,4,1,5,6,7,8]


# courses.append('art')
# courses.insert(0, 'philosophy')

# print(courses[1:3])


# courses.insert(0, courses_2)
# courses.extend(courses_2)

# print(courses[0])


# courses.remove('math')

# courses.pop()

# popped = courses.pop()

# print(popped)

# courses.reverse()

# courses.sort()

# the original list is altered
# courses.sort(reverse=True)
# nums.sort(reverse=True)

# the original list is not altered

# sorted_courses = sorted(courses)

# print(sorted_courses)
# print(min(nums))
# print(sum(nums))

# print(courses.index('compsci'))

# for item in courses:
	# print(item)


# for index, course in enumerate(courses, start=1):
# 	print(index, course)


# for index, course in enumerate(courses):
# 	print(index, course)
# print('math' in courses)

# course_str = ', '.join(courses)

# new_list = course_str.split(', ')

# print(course_str)
# print(new_list)



# mutable 
# list_1 = ['history', 'math', 'physics', 'compsci']
# list_2 = list_1


# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# immutable 
# tuple_1 = ('history', 'math', 'physics', 'compsci')
# tuple_2 = tuple_1


# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)


# set
# unlike tuple and list, sets don't care about orders 
# can be used to remove duplicated valued, because set doesn't support duplicates 
# used to test if a value is in a group
# cs_courses = {'history', 'math', 'physics', 'compSci',}
# art_courses = {'history', 'math', 'art', 'design',}

# # print(cs_courses)
# # print('math' in cs_courses)

# print(cs_courses.intersection(art_courses))
# print(cs_courses.union(art_courses))


# create empty lists, tuples and sets

empty_list = []
empty_list = list()

empty_tuple = ()
empty_list = tuple()

empty_set = {}
empty_list = set()







