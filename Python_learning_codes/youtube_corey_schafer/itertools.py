import itertools

def get_state(person):
	return person["state"]

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]




person_group = itertools.groupby(people, get_state)

copy1, copy2 = itertools.tee(person_group)

print(i for i in copy1)

for key, group in person_group:
	print(key, len(list(group)))
	print(key)
	for person in group:
		print(person)
	print()







# counter = itertools.count(start = 5, step=-2.5)
# counter = itertools.cycle([1,2,3])
# counter = itertools.cycle(('On', 'off'))
# counter = itertools.repeat(4)
# counter = itertools.repeat(4, times=5)

# squares = map(pow, range(10), itertools.repeat(2))

# # squares = itertools.starmap(pow,[(0,2),(2,4),(4,5)])

# # print(list(squares))


# # for num in counter:
# 	# print(num)

# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))
# # print(next(counter))

# # data = [100, 200, 300, 400]
# # # daily_date = list(zip(itertools.count(), data))
# # daily_date = list(zip(range(10), data))

# # daily_date = list(itertools.zip_longest(range(10), data))
# # print(daily_date)
# import operator

# def lt_2(n):
# 	if n< 2:
# 		return True
# 	return False

# letters = ['a', 'b', 'c', 'd']
# numbers = [ 1,2,3,2,1,0]
# names = ['Coreay', 'Nicole']

# selectors = [True, True, False, True]


# # result = itertools.compress(letters, selectors)
# # result = filter(lt_2, numbers)
# # result = itertools.filterfalse(lt_2, numbers)
# # result = itertools.dropwhile(lt_2, numbers)
# result = itertools.takewhile(lt_2, numbers)
# result = itertools.accumulate(numbers, operator.mul)




# for item in result:
# 	print(item)




# result = itertools.combinations(letters, 2)
# result = itertools.permutations(letters, 2)
# result = itertools.product(numbers, repeat=4)
# ||
# ||
# result = itertools.combinations_with_replacement(numbers,4)

# count = 0
# for item in result:
# 	print(item)
# 	count += 1
# print(count)

# combined = letters + numbers + names
# combined = itertools.chain(letters, numbers, names)
# combined = itertools.islice(range(10), 1, 5, 2)

# for item in combined:
# 	print(item)


# with open('tested.log', 'r') as f:
# 	header = itertools.islice(f,3)


# 	for line in header:
# 		print(line, end='')


