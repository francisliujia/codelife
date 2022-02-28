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

	def print_tree(self, level):
		if self.get_level() > level:
			return
		spaces = ' '* self.get_level()* 3
		prefix = spaces + '|--' if self.parent else ''
		print(prefix + self.data)
		if self.children:
			for chisld in self.children:
				# print(child.data)
				child.print_tree(level)


def build_location_tree():

	root = TreeNode('Global')

	india = TreeNode('India')

	gujarat = TreeNode('Gujarat')
	gujarat.add_child(TreeNode('Ahemedabad'))
	gujarat.add_child(TreeNode('Baroda'))

	karnataka = TreeNode('Karnataka')
	karnataka.add_child(TreeNode('Banglura'))
	karnataka.add_child(TreeNode('Mysoro'))

	india.add_child(gujarat)
	india.add_child(karnataka)

	usa = TreeNode('USA')

	nj = TreeNode('New Jersey')
	nj.add_child(TreeNode('Princeton'))
	nj.add_child(TreeNode('Trenton'))
	
	ca = TreeNode('California')
	ca.add_child(TreeNode('San Francisco'))
	ca.add_child(TreeNode('Mountain View'))
	ca.add_child(TreeNode('Palo Alto'))

	usa.add_child(nj)
	usa.add_child(ca)

	root.add_child(india)
	root.add_child(usa)

	return root 


if __name__ == '__main__':
	location_node = build_location_tree() 
	location_node.print_tree(9)








