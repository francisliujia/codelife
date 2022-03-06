'''
graph:

- node: the objects
- edges: connections between nodes

graph types:
	- undirected graph: facebook friends suggestions
	- directed graph: flight routes


difference between tree and graph:
	- in tree there should be only one path between two nodes
	- tree can be thought a special type of graph

grapth applications:
	- find all path
	- find the shortest path


	- maps
	- internet connections
	- facebook
	- Amazon product recommendation


weighted graph:
	- in some cases, the edges will be weighted, these will be called 

'''

class Graph:

	def __init__(self, edges):
		self.edges = edges
		self.graph_dict = {}
		for start, end in self.edges:
			if start in self.graph_dict:
				self.graph_dict[start].append(end)
			else:
				self.graph_dict[start] = [end]
		print('graph dict:', self.graph_dict)


	def get_path(self, start, end, path=[]):
		path = path + [start]

		if start == end:
			return  [path]

		if start not in self.graph_dict:
			return []

		paths = []
		for node in self.graph_dict[start]:
			if node not in path:
				new_paths = self.get_path(node, end, path)
				for p in new_paths:
					paths.append(p)
		return paths


	def get_shortest_path(self, start, end, path=[]):
		path = path + [start]

		if start not in self.graph_dict:
			return None 
		if start == end:
			return path

		shortest_path = None 
		for node in self.graph_dict[start]:
			if node not in path:
				sp = self.get_shortest_path(node, end, path)
				if sp:
					if shortest_path is None or len(sp) < len(shortest_path):
						shortest_path = sp 
		return shortest_path

if __name__ == '__main__':
	routes = [
	('Mumbai', 'Paris'),
	('Mumbai', 'Dubai'),
	('Paris', 'Dubai'),
	('Paris', 'NYC'),
	('Dubai', 'NYC'),
	('NYC', 'Toronto'),
	] 

	route_graph = Graph(routes)
	start = 'Paris'
	end = 'NYC'
	# path = route_graph.get_path(start, end)
	path = route_graph.get_shortest_path(start, end)
	print('avaiable path is:', path)



















