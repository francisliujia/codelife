class Test:
	def class_method(self):
		print("this is a class method")

def monkey_method():
	print("this is a monkey method")


Test.class_method = monkey_method
Test.class_method()