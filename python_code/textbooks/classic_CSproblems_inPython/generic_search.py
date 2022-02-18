from __future__ import annotations 
from typing import TypeVar, Generic, Deque
from typing import Protocol
from heapq import heappush, heappop
from math import sqrt

T = TypeVar('T')


def linear_contains(iterable, key):
	for i in iterable:
		if i == key:
			return True
		return False


C = TypeVar('C', bound='Comparable')


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


class Stack(Generic[T]):

	def __init__(self):
		self._container = []

	@property
	def empty(self):
		return not self._container

	def push(self, item):
		self._container.append(item)

	def pop(self):
		return self._container.pop()  # lifo

	def __repr__(self):
		return repr(self._container)


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


class Queue(Generic[T]):
	def __init__(self):
		self._container: Deque[T] = Deque()

	@property
	def empty(self):
		return not self._container

	def push(self, item):
		self._container.append(item)

	def pop(self):
		self._container.popleft()  # fifo

	def __repr__(self):
		return repr(self._container)


def bfs(initial, goal_test, successors):
	frontier = Queue()
	frontier.push(Node(initial, None))
	explored = {initial}

	while not frontier.empty:
		current_node = frontier.pop()
		current_state: Node[T] = current_node.state
		if goal_test(current_state):
			return current_node
		for child in successors(current_state):
			if child in explored:
				continue
			explored.add(child)
			frontier.push(Node(child, current_node))
	return None 


class PriorityQueue(Generic[T]):
	def __init__(self):
		self._container = []

	@property
	def empty(self):
		return not self._container

	def push(self, item):
		heappush(self._container, item)  # in by priority

	def pop(self):
		return heappop(self._container)  # out by priority

	def __repr__(self):
		return repr(self._container)


def astar(initial, goal_test, successors, heuristic):
	frontier = PriorityQueue()
	frontier.push(Node(initial, None, heuristic(initial)))
	explored = {initial, 0.0}

	while not frontier.empty:
		current_node = frontier.pop()
		current_state = current_node.state
		if goal_test(current_state):
			return current_node
		for child in successors(current_node):
			new_cost = current_node.cost + 1 
			if child not in explored or explored[child] > new_cost:
				explored[child] = new_cost
				frontier.push(Node(child, current_node, new_cost, heuristic(child)))
	return None 


class Node(Generic[T]):
	def __init__(self, state, parent, cost=0.0, heuristic=0.0):
		self.state = state 
		self.parent = parent
		self.cost = cost 
		self.heuristic = heuristic

	def __lt__(self, other):
		return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def node_to_path(node):
	path = [node.state]
	while node.parent is not None:
		node = node.parent
		path.append(node.state)
	path.reverse()
	return path 


def euclidean_distance(goal):
	def distance(m1):
		xdist = m1.column - goal.column 
		ydist = m1.row - goal.row 
		return sqrt((xdist * xdist) + (ydist * ydist))
	return distance


def manhattan_distance(goal):
	def distance(m1):
		xdist = abs(m1.column - goal.column)
		ydist = abs(m1.row - goal.row)
		return xdist + ydist
	return distance


if __name__ == "__main__":
	print(linear_contains([1, 23, 4, 6, 63, 88], 23))
	print(binary_contains(['h', 'b', 'c', 'y', 'r', 'e', ], 'e'))
	# print(binary_contains(''))
