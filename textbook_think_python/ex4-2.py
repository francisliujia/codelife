from __future__ import print_function, division
from ex4 import arc
import turtle

def petal(t, r, angle):
	for i in range(2):
		arc(t, r, angle)
		t.lt(180-angle)

def flower(t, n, r, angle):
	for i in range(n):	
		petal(t, r, angle)
		t.lt(360.0/n)

def move(t, length):
	t.pu()
	t.fd(length)
	t.pd()

bob = turtle.Turtle()

move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.mainloop()




