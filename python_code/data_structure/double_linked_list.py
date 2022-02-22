class Node:
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

class Double_linked_list:
	def __init__(self):
		self.head = None 

	def print_forward(self):
		if self.head is None:
			print('linked list is empty') 
			return

		itr = self.head 
		llstr = ''
		while itr:
			llstr += str(itr.data) + '-->'
			itr = itr.next 
		print(llstr)

	def print_backword(self):
		if self.head is None:
			print('Linked list is empty') 
			return

		last_node = self.get_last_node()
		itr = last_node
		llstr = ''

		while itr:
			llstr += itr.data + '->'
			itr = itr.prev
		print('Linked list in reverse:', llstr)

	def get_last_node(self):
		itr = self.head 
		while itr.next:
			itr = itr.next
		return itr

	def get_length(self):
		count = 0
		itr = self.head 
		while itr.next:
			count += 1
			itr = itr.next
		return count

	def insert_at_beginning(self, data):
		if self.head == None:
			node = Node(data, self.head, None)
			self.head = node
		else:
			node = Node(data, self.head, None)
			self.head.prev = node 
			self.head = node

	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None, None)
			return

		itr = self.head 
		while itr.next:
			itr = itr.next 

		itr.next = Node(data, None, itr)

	def insert_at(self, index, data):
		if index < 0 or index > self.get_length():
			raise Exception('Invalid index')

		if index ==0:
			self.insert_at_beginning(data)
			return

		count = 0
		itr = self.head 
		while itr:
			if count == index - 1:
				node = Node(data, itr.next, itr)
				if node.next:
					node.next.prev = node 
				itr.next = node 
				break 
			itr = itr.next 
			count += 1

	def remove_at(self, index):
		if index < 0 or index>=self.get_length():
			raise Exception('invalid index')

		if index == 0:
			self.head = self.head.next 
			self.head.prev = None 
			return

		count = 0
		itr = self.head 
		while itr:

			if count == index:
				itr.prev.next = itr.next
				if itr.next:
					itr.next.prev = itr.prev

			itr = itr.next
			count += 1

	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)

if __name__ == "__main__":
	ll = Double_linked_list()
	ll.insert_values(['hello', 'new', 'world', 'start', 'game'])
	ll.print_forward()
	ll.print_backword()
	ll.insert_at_end('francis')
	ll.print_forward()
	ll.insert_at(2, 'banana')
	ll.print_forward()
	ll.remove_at(1)
	ll.print_forward()
