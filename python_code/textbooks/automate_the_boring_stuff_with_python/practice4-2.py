grid = [
		['.', '.', '.', '.', '.', '.'],
		['.', '0', '0', '.', '.', '.'],
		['0', '0', '0', '0', '.', '.'],
		['0', '0', '0', '0', '0', '.'],
		['.', '0', '0', '0', '0', '0'],
		['0', '0', '0', '0', '0', '.'],
		['0', '0', '0', '0', '.', '.'],
		['.', '0', '0', '.', '.', '.'],
		['.', '.', '.', '.', '.', '.'],
		]




def plot_grid(grid):
	row_num = len(grid)
	col_num = len(grid[0])

	for col in range(col_num):
		for row in range(row_num):
			print(grid[row][col], end='')
		print()

plot_grid(grid)



list = []
for y in range(len(grid[0])):
# print(x)
	for x in range(len(grid)):
		print(grid[x][y],end='')
		# return y
	print()


# def value(list):
# 	for x in grid:
# 	# print(x)
# 		for y in x:
# 			# return y
# 			print(y, end='')
# 		print()

# value(grid)

list = [[], [], [], [], [], [], [], [], []]



