class Quantity:
	__counter = 0 

	def __init__(self):
		cls = self.__class__
		prefix = cls.__name__
		index = cls.__counter 
		self.storage_name = '_{}#{}'.format(prefix, index)
		cls.__counter += 1 

	def __get__(self, instance, owner):
		return getattr(instance, self.storage_name)

	def __set__(self, instance, value):
		if value > 0:
			setattr(instance, self.storage_name, value)
		else:
			raise ValueError('value much be greater than 0')

class LineItem:
	weight = Quantity()
	price = Quantity()

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price 



# coconuts = LineItem('brizilian coconut', 20, 12.9)
# print(coconuts.weight, coconuts.price)
# print(getattr(raisins, '_Quantity#0'), getattr(raisins, '_Quantity#1'))


import model_v5 as model 

class LineItem2:
	 description = model.NonBlank()
	 weight = model.Quantity()
	 price = model.Quantity()

	 def __init__(self, description, weight, price):
	 	self.description = description
	 	self.weight = weight
	 	self.price = price


	 def subtotal(self):
	 	return self.weight * self.price

	 	












