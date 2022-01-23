# class computer:
# 	def process(self):
# 		print('Running')

# com = computer()
# com.process()

from abc import ABC, abstractmethod

class Computer(ABC):
	@abstractmethod
	def process(self):
		pass 

class Laptop(Computer):
	def process(self):
		print("It's running")

class Programmer:
	def work(self, com):
		print("solving problems")
		com.process()




# com = computer()
com1 = Laptop()
# com1.process()
# com.process()
pro1 = Programmer()
pro1.work(com1)






