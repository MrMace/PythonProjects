#import dictionary for graph
from collections import defaultdict

#function add edge to graph
graph = defaultdict(list)
def addEdge(graph, u, v):
    graph[u].append(v)
    
#define of function
def generate_edges(graph):
    edges = []
        
    #for nodes in graph
    for node in graph:
            
        #for neighbors
        for neighbour in graph[node]:
                
                
            #if edge exists then append
            edges.append((node, neighbour))
                
    return edges
    

#declare of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')

print(generate_edges(graph))
5 mins