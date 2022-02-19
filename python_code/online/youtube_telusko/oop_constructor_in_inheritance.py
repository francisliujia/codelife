class A:

	def __init__(self):
		print('in A init')

	def feature1(self):
		print('feature1-A is working')

	def feature2(self):
		print('feature2 is working')

# class B(A):

# 	def __init__(self):
# 		super().__init__()
# 		print('in B init')

# 	def feature3(self):
# 		print('feature3 is working')

# 	def feature4(self):
# 		print('feature4 is working')

class B:

	def __init__(self):
		print('in B init')

	def feature1(self):
		print('feature1-B is working')

	def feature4(self):
		print('feature4 is working')


class C(A,B):
	def __init__(self):
		super().__init__()
		print('in C init')


# method resolution order(MRO) left--> right

# a1 = A()
# a1.feature1()
# b1 = B()
c1 = C()
c1.feature1()











