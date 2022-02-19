class A:
	def show(self):
		print('in A show')

class B(A):
	# pass
	def show(self):
		print('in B show')

# a1 = A()
# a1.show()

a1 = B()
a1.show()