class BinarySearchTreeNode:
	def __init__(self, data):
		self.data = data 
		self.left = None 
		self.right = None 

	def add_child(self, data):
		if data == self.data:
			return
		if data < self.data:
			# add data in the left tree
			if self.left:
				self.left.add_child(data) 
			else:
				self.left = BinarySearchTreeNode(data)
		else:
			# add data in the right tree 
			if self.right:
				self.right.add_child(data) 
			else:
				self.right = BinarySearchTreeNode(data)

	def in_order_traversal(self):
		elements = []
		if self.left:
			elements += self.left.in_order_traversal()

		elements.append(self.data)

		if self.right:
			elements += self.right.in_order_traversal()

		return elements

	def search(self, val):
		if self.data == val:
			return True

		if val < self.data:
			# val might be in left subtree
			if self.left:
				return self.left.search(val)
			else:
				return False

		if val > self.data:
			# val might be in right subtree
			if self.right:
				return self.right.search(val)
			else:
				return False

	def post_order_traversal(self):
		elements = []
		if self.left:
			elements += self.left.post_order_traversal()
		if self.right:
			elements += self.right.post_order_traversal()
		elements.append(self.data)
		return elements

	def pre_order_traversal(self):
		elements = [self.data]
		if self.left:
			elements += self.left.pre_order_traversal()
		if self.right:
			elements += self.right.pre_order_traversal()
		return elements

	def find_min(self):
		if self.left is None:
			return self.data
		else:
			return self.left.find_min()

	def find_max(self):
		if self.right is None:
			return self.data
		else:
			return self.right.find_max()

	def calculate_sum(self):
		left_sum = self.left.calculate_sum() if self.left else 0
		right_sum = self.right.calculate_sum() if self.right else 0
		return self.data + left_sum + right_sum


	def delete(self, val):
		if val < self.data: # val < data
			if self.left:
				self.left = self.left.delete(val)
		elif val > self.data: # val > data
			if self.right:
				self.right = self.right.delete(val)

		else: # val == data; now we need to delete it
				# 1. has no child, 2. has left child, 3. has right child
			if self.left is None and self.right is None:
				return None 
			if self.left is None:
				return self.right 
			if self.right is None:
				return self.right

			min_val = self.right.find_min()
			self.data = min_val
			self.right = self.right.delete(min_val)

		return self 



def build_tree(elements):
	root = BinarySearchTreeNode(elements[0])

	for i in range(1, len(elements)):
		root.add_child(elements[i])

	return root 

if __name__ == '__main__':
	nums = [23, 33, 1, 4, 8, 10, 55, 78] 
	nums_tree = build_tree(nums)
	print('Min: ', nums_tree.find_min())
	print('Max: ', nums_tree.find_max())
	print('Sum: ', nums_tree.calculate_sum())

	print('In order traversal: ', nums_tree.in_order_traversal())
	# print('pre order traversal: ', nums_tree.pre_order_traversal())
	# print('Post order traversal: ', nums_tree.post_order_traversal())

	nums_tree.delete(10)
	print('In order traversal: ', nums_tree.in_order_traversal())







