class Student:

	school = "Moonhamod"

	def __init__(self, m1, m2, m3):

		self.m1 = m1
		self.m2 = m2
		self.m3 = m3

	def avg(self):
		return round((self.m1 + self.m2 + self.m3) / 3, 3)

	@classmethod
	def getSchool(cls):
		return cls.school

	@staticmethod
	def info():
		print('this is a student class, nothing to do with class vals and instance vals')


s1 = Student(44, 66, 44)
s2 = Student(23, 44, 55)

print(f"s1: {s1.avg()}, s2:{s2.avg()}")
print("s1: {}, s2: {}".format(s1.avg(), s2.avg()))

Student.info()
print(Student.getSchool())