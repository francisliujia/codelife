def do_four(f):
	print(f)
	print(f)
	print(f)
	print(f)

def print_grid_a1():
	border = ('+ ' + '- ' * 4) * 2 + '+'
	middle = '|         |         |'
	print(border)
	do_four(middle)
	print(border)
	do_four(middle)
	print(border)

print_grid_a1()

print('-' * 20)

def print_grid_a2():
	border = '+ - - - - + - - - - +'
	middle = '|         |         |'
	print(border)
	do_four(middle)
	print(border)
	do_four(middle)
	print(border)

print_grid_a2()

print('-*' * 20)

def print_grid_b():
	border = ('+ - - - - ') * 4 + '+'
	middle = ('|         ') * 4 + '|'
	print(border)
	do_four(middle)
	print(border)
	do_four(middle)
	print(border)
	do_four(middle)
	print(border)
	do_four(middle)
	print(border)

print_grid_b()












