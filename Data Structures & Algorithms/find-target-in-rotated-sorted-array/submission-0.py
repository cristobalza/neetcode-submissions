class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        Input: nums = [3,4,5,6,1,2], target = 1
                       l         r
                             m


        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] <= target:
                if nums[l] <= target:
                    l = m + 1
                else:
                    r = m

            else:
                if target <= nums[r]:
                    l = m + 1
                else:
                    r = m
        
        return l if nums[l] == target else -1