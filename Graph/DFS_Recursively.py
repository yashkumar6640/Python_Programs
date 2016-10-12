class Graph:
	def __init__(self, graph):
		self.graph=graph;
	def dfs(self, graph, vertex, visited):
		if vertex not in visited:
			print(vertex);
			visited.add(vertex);
		for next in graph[vertex]-visited:
			self.dfs(graph, next, visited);
		return;

graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])
            }

visited=set();
g=Graph(graph);
g.dfs(graph, 'A', visited);