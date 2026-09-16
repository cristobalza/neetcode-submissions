"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        graph = {} #old: new

        def dfs(vertex):
            if vertex in graph:
                return graph[vertex]

            new_vertex = Node(vertex.val)
            graph[vertex] = new_vertex

            for adj_vertex in vertex.neighbors:
                new_vertex.neighbors.append(dfs(adj_vertex))
            
            return graph[vertex]

    
        return dfs(node) if node else None
        