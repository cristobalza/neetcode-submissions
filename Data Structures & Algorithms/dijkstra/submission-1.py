class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = collections.defaultdict(list)

        for src_node, adj_node, weight in edges:
            adj[src_node].append((adj_node, weight))

        shortest = {} # src node: weight

        minheap = []
        minheap.append((0, src)) # weight, node

        while minheap:
            weight, node = heapq.heappop(minheap)
            if node in shortest:
                continue

            shortest[node] = weight

            for adj_node, adj_weight in adj[node]:
                if adj_node not in shortest:
                    heapq.heappush(minheap, [adj_weight + weight, adj_node])

        # check unreacheable nodes
        for node in range(n):
            if node not in shortest:
                shortest[node] = -1

        return shortest