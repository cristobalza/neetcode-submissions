class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """

        [10,9,2,5,3,7,101,18]

        sort()

        [2,3,5,7,9,10,18,101]
                          




        """
        n = len(nums)

        dp = [1] * n

        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                if nums[l] < nums[r]:
                    dp[l] = max(dp[l], 1 + dp[r])

        return max(dp)
