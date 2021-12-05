message = 'it was a cold day in December, the clocks are stricking twenty.'

count = dict()
for char in message:
	count.setdefault(char, 0)
	count[char] += 1

import pprint
# print(count)
pprint.pprint(count)