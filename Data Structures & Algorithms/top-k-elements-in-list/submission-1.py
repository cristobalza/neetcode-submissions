class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = collections.Counter(nums)

        maxheap = []

        for k, v in hmap.items():
            heapq.heappush(maxheap, (-v, k))

        res = []

        while maxheap:
            res.append(heapq.heappop(maxheap)[1])

        return res[:k-1]