class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        nums = [3,0,1]
                0 1 2

        range(n+1) = [0, 1, 2, 3]

        for num in nums:
            check in set

        ---

        sum(nums) = 3 + 0 + 1 = 4

        (0 - 3) + (1 - 0) + (2 - 1) = -3 + 1 + 1 = -1

        for num in nums:
            sum

        n = 3 -> n + above = 3 + - 1 = 2
        """

        all_vals = range(0, len(nums) + 1)

        for num in all_vals:
            if num not in set(nums):
                return num