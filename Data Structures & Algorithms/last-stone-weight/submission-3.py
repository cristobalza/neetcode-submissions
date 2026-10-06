class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        """

        Input: stones = [2,3,6,2,4]
         
        sort

        Input: stones = [6,4,3,2,2]

        [2,3,2,2]
        [1,2,2]
        [1,2]
        [1]


        """

        maxheap = []

        for stone in stones:
            heapq.heappush(maxheap, -stone)

        while len(maxheap) > 1:
            sy = -1 * heapq.heappop(maxheap)
            sx = -1 * heapq.heappop(maxheap)

            if sy == sx:
                continue

            elif sy > sx:
                heapq.heappush(maxheap, -1 * (sy - sx))

        return abs(maxheap[0]) if maxheap else 0 
        