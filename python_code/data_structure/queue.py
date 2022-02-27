# python: list, collections.deque, queue.LifoQueue
# first in first out, just like a queue in real life

from collections import deque

class Queue:
	def __init__(self):
		self.queue = deque()

	def push(self, val):
		self.queue.appendleft(val)
	
	def pop(self):
		if len(self.queue) == 0:
			print('empty queue')
			return

		return self.queue.pop()

	def is_empty(self):
		return len(self.queue) == 0
	
	def size(self):
		return len(self.queue)

	def front(self):
		return self.queue[-1]

if __name__ == "__main__":
	
	queue = Queue()
	queue.push(1)
	queue.push(2)
	queue.push(3)
	print(queue.queue)