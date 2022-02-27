from queue import Queue
import time
import threading



queue = Queue()

def place_order(order_list):
	for i in orders:
		queue.push(i)
		print('==> placing order...', i)
		time.sleep(.5)
	print(queue.is_empty())

def serve_orders():
	time.sleep(1)
	while not queue.is_empty():
		item = queue.pop()
		print('--> serving order...', item)
		time.sleep(2)


if __name__ == '__main__':
	orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
	t1 = threading.Thread(target=place_order, args=(orders,))
	t2 = threading.Thread(target=serve_orders)
	
	t1.start()
	t2.start()



