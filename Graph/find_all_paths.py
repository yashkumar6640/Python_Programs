def find_all_paths(graph, start, end, path=[]):
    path=path + [start];
    if start == end:
        print(path);
        return None;
    if start not in graph:
        return None;
    for node in graph[start]:
        if node not in path:
            newpath=find_all_paths(graph, node, end, path);
            if newpath: return newpath;
    return None;

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

print(find_all_paths(graph, 'A', 'D'));