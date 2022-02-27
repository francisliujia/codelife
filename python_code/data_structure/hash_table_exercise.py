class HashTable(object):

	def __init__(self):
		self.MAX = 10
		self.arr = [None for i in range(self.MAX)]

	def get_hash(self, key):
		hash = 0 
		for char in key:
			hash += ord(char)
		return hash % self.MAX

	def __getitem__(self, key):
		h = self.get_hash(key)
		if self.arr[h] is None:
			return  
		prob_range = self.get_prob_range(h)
		for prob_index in prob_range:
			element = self.arr[prob_index]
			if element in None:
				return
			if element[0] == key:
				return element[1]

	def __setitem__(self, key, val):
		h = self.get_hash(key)
		if self.arr[h] is None:
			self.arr[h] = (key, val)
		else:
			new_h = self.find_slot(key, h)
			self.arr[new_h] = (key, val)
		print(self.arr)

	def get_prob_range(self, index):
		return [*range(index, len(self.arr))] + [*range(0, index)]

	def find_slot(self, key, index):
		prob_range = self.get_prob_range(index)
		for prob_index in prob_range:
			if self.arr[prob_index] is None:
				return prob_index
			if self.arr[prob_index][0] == key:
				return prob_index
		raise Exception('hashmap full')

	def __delitem__(self, key):
		h = self.get_hash(key)
		prob_range = self.get_prob_range(h)
		for prob_index in prob_range:
			if prob_index in prob_range:
				if self.arr[prob_index] is None:
					return
				if self.arr[prob_index][0] == key:
					self.arr[prob_index] = None
				
		print(self.arr)


lst = [*range(5, 8)] + [*range(0, 4)]
print(lst)

print()
t = HashTable()
t['march 6'] = 22
t['march 17'] = 55
t['march 17'] = 44
# print(t)
t['nov 1'] = 1
t['march 13'] = 444
del t['march 13']











