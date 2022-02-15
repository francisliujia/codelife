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

















