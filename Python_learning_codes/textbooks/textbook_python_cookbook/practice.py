from collections import deque

	def search(lines, pattern, history=5):
		previous_lines = deque(maxlen=history)
		for line in lines:
			if pattern in line:
				yield line, previous_lines
			previous_lines.append(line)


if__name == '__main__':
	with open(zen.txt) as f:
		for line, prevlines in search(f, "python", 5):
			for line in prevlines:
				print(pline, end="")
			print(line, end="")
			print('-'*20)
