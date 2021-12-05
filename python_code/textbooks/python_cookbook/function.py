# def avg(first, *rest):
# 	return (first + sum(rest)) / (1 + len(rest))


# print(avg(1,2,3))
# print(avg(12,45,44))


# import html

# def make_element(name, value, **attrs):
# 	keyvals = [' %s="%s" ' % item for item in attrs.items()]
# 	attr_str  = ''.join(keyvals)
# 	element = '<{name}{attrs}>{value}</{name}>'.format(
# 		name = name,
# 		attrs=attr_str,
# 		value = html.escape(value)
# 		)
# 	return element


# print(make_element('item', 'albatross', size='large', quantity=6))

# print(make_element('p', '<spam>'))


# def recv(maxsize, *, block):
# 	'receive a message'
# 	pass


# print(recv(1024, True))
# print(recv(122, block=True))


# def mininum(*values, clip=None):
# 	m = min(values)
# 	if clip is not None:
# 		if clip > m:
# 			m = clip
# 		else:
# 			 m
# 	return m

# print(mininum(1,3,4,-5,4,7))
# print(mininum(123,-4,5,4,6,7, clip=0))

def add(x:int, y:int) -> int:
	return x + y

print(add(2,3))





