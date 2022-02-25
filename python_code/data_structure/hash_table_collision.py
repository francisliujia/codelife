# 1. use linked-list
# 2. use linear probing

class HashTable:
	def __init__(self):
		self.MAX = 10 
		self.arr = [[] for i in range(self.MAX)]

	def get_hash(self, key):
		h = 0
		for char in key:
			h += ord(char)
		return h % self.MAX	

	def __setitem__(self, key, val):
		h = self.get_hash(key)
		found = False
		for index, element in enumerate(self.arr[h]):
			if len(element) == 2 and element[0] == key: # if key already exists, modify the pair 
				self.arr[h][index] = (key, val)
				found = True 
		if not found: # key does not exits
			self.arr[h].append((key, val))

	def __getitem__(self,key):
		h = self.get_hash(key)
		for element in self.arr[h]:
			if element[0] == key:
				return element[1]

	def __delitem__(self, key):
		h = self.get_hash(key)
		for index, kv in enumerate(self.arr[h]):
			if kv[0] == key:
				del self.arr[h][index]


t = HashTable()
t['march 6'] = 130
t['march 2'] = 444
t['march 3'] = 666
t['march 17'] = 121
r1 = t.get_hash('march 17')
r2 = t.get_hash('march 6')
del t['march 6']
print(t.arr)
print(r1, r2)
