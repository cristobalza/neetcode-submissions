class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1

            elif nums[m] >= target:
                r = m

            else:

                return m

        return -1 if l < len(nums) and nums[l] != target else l