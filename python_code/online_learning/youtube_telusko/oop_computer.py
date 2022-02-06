class Computer:

	def __init__(self):
		self.name = 'Navin'
		self.age = 33

	def update(self):
		self.age = 10 

	def compare(self, other):
		return True if self.age  == other.age else False

c1 = Computer()
c1.age = c1.update()
c2 = Computer()

if c1.compare(c2):
	print('They have the same value')
else:
	print('they are different')