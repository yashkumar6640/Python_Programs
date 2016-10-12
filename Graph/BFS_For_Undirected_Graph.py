class Graph:
	def __init__(self, graph):
		self.graph=graph;
	def bfs(self, graph, start):
		visited, queue=set(), [start];
		while queue:
			vertex=queue.pop(0);
			if vertex not in visited:
				print(vertex);
			if vertex not in visited:
				visited.add(vertex);
			queue.extend(graph[vertex] - visited);
		return visited;


graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])
        }

g=Graph(graph);
g.bfs(graph, 'A');
