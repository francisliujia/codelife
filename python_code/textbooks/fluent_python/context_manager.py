class LookingGlass:
	def __enter__(self):
		import sys
		self.original_write = sys.stdout.write
		sys.stdout.write = self.reverse_write
		return 'BABBERROCKY'

	def reverse_write(self, text):
		self.original_write(text[::-1])

	def __exit__(self, exc_type, exc_val, traceback):
		import sys 
		sys.stdout.write = self.original_write
		if exc_type is ZeroDivisionError:
			print('Please do not devide by zero')
			return True

with LookingGlass() as what:
	print('Alice, kiss me')
	print(what)