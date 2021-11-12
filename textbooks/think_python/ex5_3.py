def is_trianle(a, b, c):
	if a > b + c:
		print('No')
	elif b > a + c:
		print('No')
	elif c > a + b:
		print('No')
	else:
		print('Yes')

def prompting():
	a = input('enter the length of side a:')
	b = input('enter the length of side b:')
	c = input('enter the length of side c:')

	is_trianle(int(a), int(b), int(c))

# prompting()

def recurse(n, s):
	if n == 0:
		print(s)
	else:
		recurse(n-1, n+s)
recurse(3, 0)

import turtle
bob = turtle.Turtle()

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	t.fd(length*n)
	t.lt(angle)
	draw(t, length, n-1)
	t.rt(2*angle)
	draw(t, length, n -1)
	t.lt(angle)
	t.bk(length*n)

draw(bob, 20, 5)
turtle.mainloop()
















