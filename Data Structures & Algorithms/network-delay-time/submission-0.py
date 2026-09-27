class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        minheap = []
        visit = set()
        res_t = 0
        minheap.append((0, k))
        
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue

            visit.add(n1)
            res_t = w1

            for n2, w2 in graph[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1 + w2, n2))

        return res_t if len(visit) == n else -1
        