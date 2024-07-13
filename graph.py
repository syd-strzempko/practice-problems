'''
	 -2-A-2-
	B		C
	|3		|
	D---4-\	1
	|1 	   \|
	E --2-- F
'''
from collections import defaultdict

class Graph():

	def __init__(self, vertices=[], edges=[]):
		self.graph = defaultdict(dict)
		self.matrix = [[0 for y in range(0, len(vertices))] for x in range(0, len(vertices))]
		self.vertices = vertices # List of strings
		self.edges = edges # List of tuples

	# Complexity - O(V+E) time, < O(v^2) space
	def create_graph(self, undirected=False):
		for vertex, source, weight in self.edges:
			self.graph[vertex][source] = weight
			# Undirected
			if (undirected):
				self.graph[source][vertex] = weight

	# Complexity - O(V+E) time, == O(v^2) space
	def create_matrix(self):
		for vertex, source in self.edges:
			self.matrix[vertex][source] = weight
			# IF UNDIRECTED
			self.matrix[source][vertex] = weight

	# QUEUE - FILO
	# TODO - how does this cause shortest path
	# TODO - how do we find cycles - just modify S.T. when we look at neighbors, check against set of found
	def BFS_and_print(self, start):
		found = set()
		queue = [start] 

		while queue:
			# Take from back of queue; mark as found, print, and then add all unfound children
			val = queue.pop()
			found.add(val)
			print(val)
			queue = [neighbor for neighbor, weight in self.graph[val].items() if neighbor not in found] + queue

	# STACK - FIFO [RECURSIVE] --> go all the way then work backwards
	def DFS_and_print(self, start):
		found = set()
		self._DFS(found,start)

	def _DFS(self, found, val):

		print(val)
		found.add(val)

		for neighbor, weight in self.graph[val].items():
			if neighbor not in found:
				self._DFS(found, neighbor)

	# A list L where any x->y will be guaranteed to have index(x) < index(y)
	def Topological_Sort(self, start):

		found = set()
		topo = []

		return self._Topological_Sort(found, topo, start)[::-1]

	def _Topological_Sort(self, found, topo, val):

		found.add(val)

		# Rather than just iterating thru neighbors, first we ensure there are any unfound
		# If there are no unfound neighbors, then we can add to our list @ the end
		unfound_neighbors = [neighbor for neighbor, weight in self.graph[val].items() if neighbor not in found]
		if unfound_neighbors:
			for neighbor in unfound_neighbors:
				self._Topological_Sort(found, topo, neighbor)
		topo.append(val)
		return topo

	def Kruskals(self, start):

		# TODO - The MST we are building out - we want it to be a bunch of trees and we slowly prune/combine them

		e = 0 # Counter for edges to stop iterating when edges = # vertices - 1

		# Aux set of linked lists such that we can access parent[v1] and compare to parent[v2] instantly
		# Need to be able to link this to the MST structure so that we can easily look up group representative
		parent = {v: v for v in self.vertices} # Starts as len(vertices), where each vertex is its own parent
		# EG; graph ABC -> [A, B, C], then when B gets joined to A and A becomes rep, [A, A, C], etc

		# Sort edges
		sorted_edges = sorted(self.edges, key=lambda x: x[2], reverse=True)
		# Get smallest edge; add to tree if it does not form a cycle
		while sorted_edges and e != (len(self.vertices) - 1):
			v1, v2, weight = sorted_edges.pop()
			v1_parent = parent[v1]
			v2_parent = parent[v2]
			if v1_parent == v2_parent:
				continue
			v1_group = [x for x, parent in parent.items() if parent == v1_parent]
			v2_group = [x for x, parent in parent.items() if parent == v2_parent]
			# We want to see which group is bigger, so that relabeling smaller group is more efficient
			if len(v1_group) >= len(v2_group):
				for v2_member in v2_group:
					parent[v2_member] = v1_parent
			else:
				for v1_member in v1_group:
					parent[v1_member] = v2_parent
			print(parent)
			e += 1

	def Prims(self, start): 

		MST = defaultdict(dict) # { V1: {V2 : weight} }
		# if self.graph[(self.graph[start][0][0])] 
		included_vertices = {start}

		# Until vertices == included vertices
		while (len(included_vertices) < len(self.vertices)): # Outer v loop

			# Find all edges leading out from included_vertices
			# Iterate thru MST of included vertices and pull list of connections
			# Filter connections by external connections (v2)
			# Then flatten out
			# (v(always less than v, incrementing by v) work * deg(v) -> could max-amortize as V*E? )
			connected = [b for c in [[[vertex, v2, weight] for v2, weight in self.graph[vertex].items() if v2 not in included_vertices] for vertex in included_vertices] for b in c]
			print(connected)
			# Find minimum edge
			minimum_ext_edge = min(connected, key=lambda x: x[2])
			print(minimum_ext_edge)
			included_vertices.add(minimum_ext_edge[1])
			MST[minimum_ext_edge[0]][minimum_ext_edge[1]] = minimum_ext_edge[2]
			print(MST)

			# O(V^2) Time complexity

	def BellmanFord(self, start, end):

		distance = { v: float("Inf") for v in self.vertices }

		distance[start] = 0
		# To get path - need a structure with predecessor to work backwards from
		predecessor = { v: None for v in self.vertices }
		predecessor[start] = start

		arr = [start]

		for i in range(len(self.vertices) - 1):
			# Each time update distances given iterative building of best-edge
			for v1, v2, weight in self.edges:
				if distance[v1] != float("Inf") and distance[v1] + weight < distance[v2]: # Means that edge makes lower distance from start -> v2
					distance[v2] = distance[v1] + weight
					predecessor[v2] = v1

		# Now that we have looked at edges v-1 times, we have best distances
		# One more iteration with any decrease in weights will mean negative cycle 
		for v1, v2, weight in self.edges:
				if distance[v1] != float("Inf") and distance[v1] + weight < distance[v2]:
					return 'Negative cycle present'

		path = [end]
		parent = end
		while parent != start:
			parent = predecessor[parent]
			path.append(parent)

		return(f'Path is {"->".join(path[::-1])} with distance {distance[end]}')

	def Dijkstra(self, start, end):

		distance = { v: float("Inf") for v in self.vertices }
		distance[start] = 0
		visited = {start}

		predecessor = { v: None for v in self.vertices }
		predecessor[start] = start

		queue = [(start, 0)] # Ideally a priority heap; we will just add sorted by weight per iteration s.t. we loosely maintain this

		while len(visited) < len(self.vertices) and queue:

			cur = queue.pop()

			unvisited_neighbors = sorted([(neighbor, weight) for neighbor, weight in self.graph[cur[0]].items() if neighbor not in visited], key=lambda x: x[1], reverse=True)

			for edge in unvisited_neighbors:

				if distance[cur[0]] + edge[1] < distance[edge[0]]:
					distance[edge[0]] = distance[cur[0]] + edge[1]
					predecessor[edge[0]] = cur[0] # Predecessor updated depending on min

			queue = unvisited_neighbors + queue
			visited.add(cur[0])

		path = [end]
		parent = end
		while parent != start:
			parent = predecessor[parent]
			path.append(parent)

		return(f'Path is {"->".join(path[::-1])} with distance {distance[end]}')

exVertices = ['A','B','C','D','E','F']
exEdges = [('A','B', 2),('A','C', 2),('B','D', 3),('D','E', 1),('D','F', 4),('C','F', 1),('E','F', 2)]

graph = Graph(exVertices,exEdges)
graph.create_graph(False)
# graph.BFS_and_print('A')
# print('---')
# graph.DFS_and_print('A')
# print('---')
# print(graph.Topological_Sort('A'))
# graph.Prims('A')
print(graph.BellmanFord('A', 'F'))
print(graph.Dijkstra('A', 'F'))

