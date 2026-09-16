class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no duplicates; no cycles

        graph = {node: [] for node in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, prev_node, cycle):
            if node in cycle: 
                return False
            if node in visited:
                return True

            cycle.add(node)
            for adj_node in graph[node]:
                if adj_node != prev_node and not dfs(adj_node, node, cycle):
                    return False

            visited.add(node)
            cycle.remove(node)

            return True

        dfs(0, None, set())

        return len(visited) == n