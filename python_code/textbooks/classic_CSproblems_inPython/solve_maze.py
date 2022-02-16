from enum import Enum 
from typing import List, NamedTuple, Callable, Optional
import random 
from math import sqrt 
from generic_search import dfs, node_to_path, Node 

class Cell(str):
	EMPTY = ' '
	BLOCKED = 'X'
	START = 'S'
	GOAL = 'G'
	PATH = '*'


class MazeLocation(NamedTuple):
	row: int
	column: int

class Maze:

	def __init__(self, rows=10, columns=10, sparseness=0.2, start=MazeLocation(0, 0), goal=MazeLocation(9, 9)):
		self._rows = rows 
		self._columns = columns
		self.start = start
		self.goal = goal
		self._grid = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
		self._randomly_fill(rows, columns, sparseness)
		self._grid[start.row][start.column] = Cell.START
		self._grid[goal.row][goal.column] = Cell.GOAL

	def _randomly_fill(self, rows, columns, sparseness):
		for row in range(rows):
			for column in range(columns):
				if random.uniform(0, 1) < sparseness:
					self._grid[row][column] = Cell.BLOCKED

	def __str__(self):
		output = ''
		for row in self._grid:
			output += ''.join([c.value for c in row]) + '\n'
		return output

	def goal_test(self, m1):
		return m1 == self.goal 

	def successors(self, m1):
		locations = []
		if m1.row + 1 < self._rows and self._grid[m1.row +1][m1.column] != Cell.BLOCKED:
			locations.append(MazeLocation(m1.row + 1, m1.column))
		if m1.row - 1 >= 0 and self._grid[m1.row - 1][m1.column] != Cell.BLOCKED:
			locations.append(MazeLocation(m1.row - 1, m1.column))
		if m1.column + 1 < self._columns and self._grid[m1.row][m1.column + 1] != Cell.BLOCKED:
			locations.append(MazeLocation(m1.row, m1.column + 1))
		if m1.column - 1 >= 0 and self._grid[m1.row][m1.column - 1] != Cell.BLOCKED:
			locations.append(MazeLocation(m1.row, m1.column - 1))
		return locations

	def mark(self, path):
		for maze_location in path:
			self._grid[maze_location.row][maze_location.column] = Cell.PATH
			self._grid[self.start.row][self.start.column] = Cell.START
			self._grid[self.goal.row][self.goal.column] = Cell.GOAL

	def clear(self, path):
		for maze_location in path:
			self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
			self._grid[self.start.row][self.start.column] = Cell.START
			self._grid[self.goal.row][self.goal.column] = Cell.GOAL


if __name__ == '__main__':
	m = Maze()
	print(m)
	solution1 = dfs(m.start, m.goal_test, m.successors)
	if solution1 is None:
		print('no solution found using depth-first search')
	else:
		path1 = node_to_path(solution1)
		m.mark(path1)
		print(m)
		m.clear(path1)

















