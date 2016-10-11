class Graph:
	def __init__(self, graph):
		self.graph=graph;
	def dfs(self, graph, start, visited):
		if start not in visited:
			print(start);
			visited.add(start);
		for next in graph[start]-visited:
			self.dfs(graph, next, visited);
		return visited;

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
