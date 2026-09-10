class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = collections.Counter(nums)

        maxheap = []

        for key, val in hmap.items():
            heapq.heappush(maxheap, (-val, key))

        res = []

        while maxheap:
            res.append(heapq.heappop(maxheap)[1])

        return res if len(res) <= k else res[:k]