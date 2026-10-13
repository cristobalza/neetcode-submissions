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

        res = -1 * heapq.heappop(maxheap)
        while maxheap:

            if res == maxheap[0]:
                res = 0

            else:
                val = -1 * heapq.heappop(maxheap)

                res = abs(res - val)

        return res
        