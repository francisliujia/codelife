import socket

s = socket.socket()
print('socket created')

s.bind('localhost', 9999)

s.listen(3)

print("waiting for the connections")

while True:
	c, addr = s.accept()
	print("connneted with", addr)

	c.send("welcome to Telusko")

	c.close()
