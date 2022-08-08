from collections import deque


undirectedGraph = {
    'A': ['B', 'C', 'F'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'E', 'F'],
    'D': ['C', 'F'],
    'E': ['A', 'B', 'C', 'F'],
    'F': ['B', 'D', 'E'],
}

directedGraph = {
    'A': ['B', 'C'],
    'B': ['A', 'F'],
    'C': ['E', 'D'],
    'D': [],
    'E': ['A'],
    'F': ['D', 'E'],
}

# Breadth First Search of a Graph
def bfs(graph, node):
    visited = [] # List to keep track of visited nodes
    queue = deque() # Initialize a queue
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.popleft()
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                
    return visited

print("Undirected Graph: ")
print(bfs(undirectedGraph, 'D'))

print("\nDirected Graph: ")
print(bfs(directedGraph, 'D'))

#--------------------------------------------------------------

# Dijkstra Algorithm - Pseudocode

"""
    function Dijkstra(Graph, source):             
        dist[source] := 0                         # Distance from source to source is set to 0
        for each vertex v in Graph:               # Initializations
            if v != source
            dist[v] := infinity                   # Unknown distance function from source to each node set to infinity
            add v to Q                            # All nodes initially in Q
    
    while Q is not empty:                         # The main loop
        v := vertex in Q with min dist[v]         # In the first run-through, this vertex is the source node
        remove v from Q
        
        for each neighbor u of v:                 # where neighbor u has not yet been removed from Q
            alt := dist[v] + length(v,u)
            if alt < dist[u]:                     # A shorter path to u has been found
                dist[u] := alt                    # Update distance of u
        
    return dist[]
end function
    """
    
#-----------------------------------------------------------------------------------------------------------------------------------
   
graph = dict() 
graph['A'] = ['B', 'C'] 
graph['B'] = ['E','A'] 
graph['C'] = ['A', 'B', 'E','F'] 
graph['E'] = ['B', 'C'] 
graph['F'] = ['C'] 
