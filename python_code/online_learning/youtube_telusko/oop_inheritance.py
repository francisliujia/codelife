class A: #super/parent class
	def feature1(self):
		print('feature1 is working')

	def feature2(self):
		print('feature2 is working')


class D: #super/parent class
	def feature6(self):
		print('feature6 is working')

class B(A): # sub/child class single level inheritance
	def feature3(self):
		print('feature3 is working')

	def feature4(self):
		print('feature4 is working')

class C(B): # sub/child class  mutiple level inheritance
	def feature3(self):
		print('feature5 is working')


class F(A, D): # mutiple inheritance
	def feature7(self):
		print('feature6 is working')





a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature2()