class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        Input: nums = [3,4,5,6,1,2], target = 1
                       l         r
                             m

        nums=[4,5,6,7,0,1,2]
              l           r
                    m
                      l.  r 
                        m

        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] <= target:
                if nums[l] <= target < nums[m]:
                    l = m + 1
                else:
                    r = m

            else:
                if nums[m] < target <= nums[r]:
                    r = m
                else:
                    l = m + 1
        
        return l if nums[l] == target else -1