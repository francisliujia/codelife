symbols = '@£$%^'
codes = []
for symbol in symbols:
	codes.append(ord(symbol))

# print(codes)

codes = [ord(symbol) for symbol in symbols]
# print(codes)

beyond_ascii = [ord(s) for s in symbols if ord(s)>70]
# print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c>50, map(ord, symbols)))
# print(beyond_ascii)

colors = ['black', 'white']
sizes = ['S' 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)

# print(tuple(ord(symbol) for symbol in symbols))


import array 
re = array.array('I', (ord(symbol) for symbol in symbols))
# print(re)



lax_coordinates = (33.9425, -118.40009)
city, year, pop, chg, area = ('Tokoy', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '3123443'), ('BRA', 'CE43143'), ('ESP', 'XDA52345')]
# for passport in sorted(traveler_ids):
	# print('%s/%s' % passport)

# for country, _ in traveler_ids:
	# print(country)


a, b, *rest = range(6)
# print(a, b, *rest)


metro_areas = [
				('Tokyo', 'JP', 36.1243, (23.213432, -12343214)),
				('Delhi NCR', 'IN',21.212 , (2134, 42314)),
				('New York', 'US', 314, (1234132, -12341)),
				('Mexico City', 'MX', 214123, (1243, 14132)),
				('Sao Paulo', 'BR', 1243124, (12341324, -1234234)),
				]

# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (lat, longt) in metro_areas:
# 	if longt <= 0:
# 		print(fmt.format(name, lat, longt))

from collections import namedtuple
City = namedtuple('City', 'name country population coordiinates')
tokyo = City('Tokyo', 'JP', 36.1243, (23.213432, -12343214))
# print(tokyo)


# print(City._fields)

latlong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN',21.212 , latlong(2134, 42314))
delhi = City._make(delhi_data)
# print(delhi._asdict())

# for k, v in delhi._asdict().items():
# 	print(k+':', v)


# s = 'bicycle'
# print(s[::3])
# print(s[::-1])
# print(s[::-2])


import bisect, sys 
# HAYSTACK = [1,4,5,6,8,12,15,20,21,23,23,26,29,30]
# NEEDLES = [0, 1,2,5,8,10,22,23,29,30,31]
# ROW_FORMAT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

# def demo(bisect_fn):
# 	for needle in reversed(NEEDLES):
# 		position = bisect_fn(HAYSTACK, needle)
# 		offset = position *  '  |'
# 		print(ROW_FORMAT.format(needle, position, offset))

# if __name__ == "__main__":
# 	if sys.argv[-1] == 'left':
# 		bisect_fn = bisect.bisect_left
# 	else:
# 		bisect_fn = bisect.bisect 

# print('DEMO:', bisect_fn.__name__)
# print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
# demo(bisect_fn)


# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
# 	i = bisect.bisect(breakpoints, score)
# 	return grades[i]


# grades = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
# print(grades)













