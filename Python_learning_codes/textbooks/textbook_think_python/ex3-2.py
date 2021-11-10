def do_twice(f, v):
	f(v)
	f(v)

def print_twice(francis):
	print(francis)
	print(francis)

do_twice(print_twice, 'spam')

def do_four(f, v):
	do_twice(f, v)
	do_twice(f, v)
	
do_four(print_twice, 'spam')
