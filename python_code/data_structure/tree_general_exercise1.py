class TreeNode(object):
	def __init__(self, name, designation):
		self.name = name 
		self.designation = designation
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

	def print_tree(self, property_name):
		if property_name == 'both':
			value = f'{self.name} ({self.designation})' 
		elif property_name == 'name':
			value = self.name 
		else:
			value = self.designation

		spaces = ' '* self.get_level()* 3
		prefix = spaces + '|--' if self.parent else ''
		print(prefix + value)
		if self.children:
			for child in self.children:
				child.print_tree(property_name)


def build_management_tree():
	infra_head = TreeNode('Vishwa', 'Infrastructure Head')
	infra_head.add_child(TreeNode('Dhaval', "cloud manager"))
	infra_head.add_child(TreeNode('Abhijit', "App manager"))
	
	cto = TreeNode('Chinmay', 'CTO')
	cto.add_child(infra_head)
	cto.add_child(TreeNode('Asmir', 'Application Head'))

	hr_head = TreeNode('Gels', 'HR head')
	hr_head.add_child(TreeNode('Peter', "Recruitment Manager"))
	hr_head.add_child(TreeNode('Waqas', "plicy Manager"))

	ceo = TreeNode('Nilupul', 'CEO')
	ceo.add_child(cto)
	ceo.add_child(hr_head)


	return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy



