class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node, prev, visited):
            if node in visited: 
                return 

            visited.add(node)

            for adj_node in graph[node]:
                if adj_node != prev and adj_node not in visited:
                    dfs(adj_node, node, visited)

            return 
        
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        res = 0

        for node in range(n):
            if node not in visited:
                res += 1
                dfs(node, None, visited)

        return res
        