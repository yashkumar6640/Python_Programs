
class Graph:
	def __init__(self, graph):
		self.graph=graph;
	def dfs(self, graph, start):
		visited, stack = set(), [start];
		while stack:
			vertex=stack.pop();
			if vertex not in visited:
				print(vertex);
			if vertex not in visited:
				visited.add(vertex);
				stack.extend(graph[vertex] - visited);
		return visited;
graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])
            }
g=Graph(graph);

g.dfs(graph, 'A');