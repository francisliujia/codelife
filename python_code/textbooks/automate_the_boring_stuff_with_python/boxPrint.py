def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('symbol must be a singlecharacter string')
	if width <= 2:
		raise Exception('width must be greatere than 2')
	if height <= 2:
		raise Exception('height must be greatere than 2')
	print(symbol * width)
	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3,3)):
	try:
		boxPrint(sym, w, h)
	except Exception as e:
		print('An exception happened: ' + str(e))
