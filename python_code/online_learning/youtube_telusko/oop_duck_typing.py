class Pycharm:
	def execute(self):
		print('executing')
		print('running')


class Myeditor:

	def execute(self):
		print('spell check')
		print('convention')
		print('executing')
		print('running')


class Laptop:
	def code(self, ide):
		ide.execute()


ide = Myeditor()

lap1 = Laptop()
lap1.code(ide)