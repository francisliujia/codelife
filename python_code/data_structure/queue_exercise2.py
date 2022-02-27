from queue import Queue

def make_binary_num(n):
	num_queue = Queue()
	# print(dir(num_queue))
	num_queue.push('1')

	for i in range(n):
		front = num_queue.front()
		print('===>', front)
		num_queue.push(front + '0')
		num_queue.push(front + '1')
		num_queue.pop()

if __name__ == '__main__':
	make_binary_num(10)