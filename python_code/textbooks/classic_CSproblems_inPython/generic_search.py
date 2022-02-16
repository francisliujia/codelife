from __future__ import annotations 
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing  import Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable, key):
	for i in iterable:
		if i  == key:
			return True
		return False

C = TypeVar('C', bound='Comparable')


class Stack(Generic[T]):

	def __init__(self):
		self._container= []

	@property
	def empty(self):
		return not self._container

	def push(self, item):
		self._container.append(item)

	def pop(self):
		return self._container.pop()

	def __repr__(self):
		return repr(self._container)

class Node(Generic[T]):
	def __init__(self, state: T, parent: Optional[Node], cost=0.0, heuristic= 0.0):
		self.state = state 
		self.parent = parent
		self.cost = cost 
		self.heuristic = heuristic

	def __lt__(self, other):
		return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def dfs(initial, goal_test, successors):
	frontier = Stack()
	frontier.push(Node(initial, None))
	explored = {initial}

	while not frontier.empty:
		current_node = frontier.pop()
		current_state = current_node.state 
		if goal_test(current_state):
			return current_node
		for child in successors(current_state):
			if child in explored:
				continue
			explored.add(child)
			frontier.push(Node(child, current_node))
	return None 


def node_to_path(node):
	path = [node.state]
	while node.parent is not None:
		node = node.parent
		path.append(node.state)
	path.reverse()
	return path 



class Comparable(Protocol):
	def __eq__(self, other):
		...

	def __lt__(self, other):
		...

	def __gt__(self, other):
		return (not self < other) and self != other

	def __le__(self, other):
		return (self < other) and self == other

	def __ge__(self, other):
		# return (self > other) and self == other
		return not self < other 


def binary_contains(gene, key_coden):
	low = 0 
	high = len(gene) - 1 
	while low <= high:
		mid = (low + high) // 2
		if gene[mid] < key_coden:
			low = mid + 1 
		elif gene[mid] > key_coden:
			high = mid - 1
		else:
			return True
	return False

if __name__ == "__main__":
	print(linear_contains([1, 23, 4, 6,63, 88], 23))
	print(binary_contains(['h', 'b', 'c', 'y', 'r', 'e', ], 'e'))
	# print(binary_contains(''))

















