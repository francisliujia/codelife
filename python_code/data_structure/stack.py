# pop/push element O(1)
# search element by value O(n)

'''
- function calling in any programming language is 
managed using a stack
- undo(ctr + z) functionality in any editor uses 
stach to track down last set of operations

python: list, collections.deque, queue.LifoQueue
'''

from collections import deque

# stack = deque()
# # print(dir(stack))
# stack.append('element 1')
# stack.append('element 2')
# stack.append('element 3')
# stack.append('element 4')
# print(stack)
# p1 = stack.pop()
# print(p1)
# print(stack)

class Stack:
	def __init__(self):
		self.container = deque()

	def push(self, val):
		self.container.append(val)

	def pop(self):
		return self.container.pop()

	def peek(self):
		return self.container[-1]

	def is_empty(self):
		return len(self.container) == 0

	def size(self):
		return len(self.container)

s = Stack()
s.push(5)
print(s.peek())
s.pop()
print(s.is_empty())

s.push(2)
s.push(3)
s.push(5)
print(s.size())