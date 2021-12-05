class A:
	def spam(self):
		print('A spam')

class B(A):
	def spam(self):
		print("B spam")
		super.spam()

c = B()
