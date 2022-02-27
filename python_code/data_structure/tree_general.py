class TreeNode(object):
	def __init__(self, data):
		self.data = data 
		self.children = []
		self.parent = None 

	def add_child(self, child):
		child.parent = self
		self.children.append(child)

	def get_level(self):
		level = 0 
		p = self.parent
		while p:
			level += 1
			p = p.parent
		return level 

	def print_tree(self):
		# print(self.data)
		spaces = ' '* self.get_level()* 3
		prefix = spaces + '|--' if self.parent else ''
		print(prefix + self.data)
		if self.children:
			for child in self.children:
				# print(child.data)
				child.print_tree()



def build_product_tree():
	root = TreeNode('Electronics')
	
	laptop = TreeNode('Laptop')
	laptop.add_child(TreeNode("Mac"))
	laptop.add_child(TreeNode("Surface"))
	laptop.add_child(TreeNode("ThinkPad"))

	cellphone = TreeNode('cell phone')
	cellphone.add_child(TreeNode("iPhone"))
	cellphone.add_child(TreeNode("Pixel"))
	cellphone.add_child(TreeNode("Vivo"))

	tv = TreeNode('tv')
	tv.add_child(TreeNode("Samsung"))
	tv.add_child(TreeNode("LG"))

	root.add_child(laptop)
	root.add_child(cellphone)
	root.add_child(tv)

	print(tv.get_level())

	return root

if __name__ == '__main__':
	root = build_product_tree()
	# print(root.get_level())
	root.print_tree()



