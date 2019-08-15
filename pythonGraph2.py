graph = {'a': ['c'],'b':['d'],'c':['e'],'d':['a','d'],'e':['b','c']}

def findShortestPath(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return path
    
    shortest = None
    for node in graph[start]:
        if node not in path:
            newPath = findShortestPath(graph,node,end,path)
            if newPath:
                if not shortest or len(newPath) < len(shortest):
                    shortest = newPath
                return shortest
print(findShortestPath(graph,'d','c'))