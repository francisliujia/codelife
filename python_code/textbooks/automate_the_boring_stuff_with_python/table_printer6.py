table_data = [
	['apples', 'oranges', 'cherries', 'banana', ],
	['alice', 'bob', 'carol', 'david', ],
	['dogs', 'cats', 'moose', 'goose', ],]

def print_data(data):
	row_num = len(data)
	col_num = len(data[0])

	for y in range(col_num):
		for x in range(row_num):
			print(data[x][y], end='  ')
		print()

print_data(table_data)

