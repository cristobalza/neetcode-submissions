class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float("-inf")

        prefix, suffix = 0, 0

        for i in range(len(nums)):
            prefix = nums[i] * prefix if prefix != 0 else nums[i] * 1
            suffix = nums[len(nums) - 1 - i] * suffix if suffix != 0 else nums[len(nums) - 1 - i] * 1

            res = max(res, max(prefix, suffix))

        return res