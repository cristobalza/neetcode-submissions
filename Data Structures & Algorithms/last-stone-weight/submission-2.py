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
            s1 = heapq.heappop(maxheap)
            s2 = heapq.heappop(maxheap)

            if s1 - s2 == 0:
                continue

            elif s2 > s1:
                heapq.heappush(maxheap, s2 - s1)

        return abs(maxheap[0]) if maxheap else 0 
        