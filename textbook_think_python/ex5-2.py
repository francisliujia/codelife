def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print('Holy smokes, Fermat was wrong!')
	else:
		print('no, that doesn’t work.')


def prompting():
	a = input('input your value of a: ')
	b = input('input your value of b: ')
	c = input('input your value of c: ')
	d = input('input your value of d: ')

	check_fermat(int(a), int(b), int(c), int(c))

prompting()

