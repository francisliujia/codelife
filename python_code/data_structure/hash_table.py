# # 1. searching by list
# stock_price = []
# with open('stock_price.csv', 'r') as f:
# 	for line in f:
# 		tokens = line.split(',')
# 		day = tokens[0]
# 		price = tokens[1]
# 		stock_price.append([day, price])

# print(stock_price)

# for ele in stock_price:
# 	if ele[0] == '9-Mar':
# 		print(ele[1])


# # 2. search via dict

# stock_price = {}
# with open('stock_price.csv', 'r') as f:
# 	for line in f:
# 		tokens = line.split(',')
# 		day = tokens[0]
# 		price = tokens[1]
# 		stock_price[day] = price

# print(stock_price)
# print(stock_price['9-Mar'])



def get_hash(key):
	h = 0
	for char in key:
		h += ord(char)
	return h % 100

# ret = get_hash('march 6')
# print(ret)


class HashTable:
	def __init__(self):
		self.MAX = 100 
		self.arr = [None for i in range(self.MAX)]

	def get_hash(self, key):
		h = 0
		for char in key:
			h += ord(char)
		return h % self.MAX	

	def __setitem__(self, key, val):
		h = self.get_hash(key)
		self.arr[h] = val	

	def __getitem__(self, key):
		h = self.get_hash(key)
		return self.arr[h]

	def __delitem__(self, key):
		h = self.get_hash(key)
		self.arr[h] = None

	# def get(self, key):
	# 	h = self.get_hash(key)
	# 	return self.arr[h]

	# def add(self, key, val):
	# 	h = self.get_hash(key)
	# 	self.arr[h] = val


t = HashTable()
# # print(t.get_hash('march 6'))
# t.add('march 6', 130)
# rt = t.get('march 6')
# print(rt)

t['march 6'] = 130
t['march 2'] = 444
t['march 3'] = 666

del t['march 2']
print(t.arr)
rt = t['march 2']
print(rt)
rt = t['march 6']
rt = t['march 3']


print(t)