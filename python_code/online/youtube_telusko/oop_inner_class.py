class Student:

	def __init__(self, name, rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop()

	def show(self):
		print(self.name, self.rollno)
		self.lap.show()


	class Laptop:
		def __init__(self):
			self.brand = 'HP'
			self.cpu = 'i7'
			self.ram = 8

		def show(self):
			print(self.brand, self.cpu, self.ram)

s1 = Student('Navin', 2)
s2 = Student('Kerwin', 3)

s1.show()
# print(s1.name, s1.rollno)

print(s1.lap.brand)