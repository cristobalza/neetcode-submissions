class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

        self.minheap = []

        for num in nums:
            heapq.heappush(self.minheap, num)

            if len(self.minheap) > self.k:
                heapq.heappop(self.minheap)
        

    def add(self, val: int) -> int:

        heapq.heappush(self.minheap, val)

        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        return self.minheap[0]



